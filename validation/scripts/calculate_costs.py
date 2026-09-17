#!/usr/bin/env python3
"""Recalculate illustrative costs/capacity; --check verifies the committed result."""
from pathlib import Path
import argparse,json
R=Path(__file__).resolve().parents[2]
def base_calculate(d):
 subtotal=sum(x['quantity']*x['unit_cost'] for x in d['one_off'])
 upfront=round(subtotal*(1+d['contingency_rate']),2)
 monthly=sum(x['amount'] for x in d['monthly']);months=d['horizon_months']
 total=round(upfront+monthly*months,2)
 benefit_months=max(0,months-d['benefit_start_month']+1)
 c=d['capacity'];events=c['sensors']/c['sample_interval_seconds'];buffer=events*c['average_event_bytes']*3600*c['outage_hours']
 return {'status':d['status'],'currency':d['currency'],'one_off_subtotal':subtotal,'one_off_with_contingency':upfront,'monthly_run_cost':monthly,'horizon_months':months,'total_cost':total,'sensitivity_total_cost':{k:round(total*v,2) for k,v in d['sensitivity_factors'].items()},'benefit_months':benefit_months,'break_even_monthly_incremental_contribution_from_benefit_start':round(total/benefit_months,2) if benefit_months else None,'illustrative_benefits':[{'name':b['name'],'total_incremental_contribution':b['monthly_incremental_contribution']*benefit_months,'net_after_total_cost':round(b['monthly_incremental_contribution']*benefit_months-total,2)} for b in d['benefit_scenarios']],'capacity':{'events_per_second':events,'estate_buffer_GB_decimal':round(buffer/1e9,3),'average_gateway_buffer_MB_with_headroom_decimal':round(buffer/c['gateways']*c['storage_headroom_factor']/1e6,2),'average_api_requests_per_second':round(c['visitors_per_day']*c['api_calls_per_visit']/(c['open_hours_per_day']*3600),2),'burst_api_requests_per_second':round(c['visitors_per_day']*c['api_calls_per_visit']/(c['open_hours_per_day']*3600)*c['burst_factor'],2),'arrival_people_per_second':round(c['visitors_per_day']/(c['arrival_window_hours']*3600),3),'lane_capacity_people_per_second':round(c['admission_lanes']/c['seconds_per_admission'],3),'raw_vibration_GB_per_day_decimal':round(c['raw_vibration_sensors']*c['raw_vibration_axes']*c['raw_vibration_bytes_per_axis']*c['raw_vibration_hz']*86400/1e9,3)}}
def calculate(d):
 result=base_calculate(d);c=d['capacity'];p=d['pilot']
 events=c['sensors']/c['sample_interval_seconds']
 archive=events*c['average_event_bytes']*86400*c['recovery_archive_days']
 pending=events*c['average_event_bytes']*3600*c['outage_hours']
 result['capacity']['recovery_archive_GB_decimal']=round(archive/1e9,3)
 result['capacity']['average_gateway_pending_plus_archive_MB_with_headroom']=round((archive+pending)/c['gateways']*c['storage_headroom_factor']/1e6,2)
 sub=p['hardware_allocation']+sum(x['quantity']*x['unit_cost'] for x in p['person_days'])
 result['pilot']={'subtotal':sub,'one_off_with_contingency':round(sub*(1+p['contingency_rate']),2),'operation_cost':p['monthly_run_cost']*p['duration_months'],'total_ceiling':round(sub*(1+p['contingency_rate'])+p['monthly_run_cost']*p['duration_months'],2),'relationship_to_full_envelope':p['relationship_to_full_envelope']}
 # Staged funding and independent experiment allocations are planning choices.
 stages=d['staged_operation']
 assert sum(s['months'] for s in stages)==d['horizon_months']
 assert sum(s['one_off_allocation'] for s in stages)==result['one_off_with_contingency']
 staged_run=sum(s['months']*s['monthly_cost'] for s in stages)
 staged_total=round(result['one_off_with_contingency']+staged_run,2)
 result['staged']={'run_cost':staged_run,'total_cost':staged_total,'stages':stages,'break_even_monthly_contribution':round(staged_total/result['benefit_months'],2),'illustrative_benefits':[{'name':b['name'],'total_incremental_contribution':b['monthly_incremental_contribution']*result['benefit_months'],'net_after_total_cost':round(b['monthly_incremental_contribution']*result['benefit_months']-staged_total,2)} for b in d['benefit_scenarios']]}
 packages=[]
 for x in p['packages']:
  subtotal=x['hardware']+x['delivery_days']*650+x['installation_days']*450+x['training_days']*450+x['data_days']*350+x['specialist_days']*800
  packages.append({'name':x['name'],'subtotal':subtotal,'one_off_with_contingency':round(subtotal*(1+p['contingency_rate']),2),'run_cost':x['monthly_run_cost']*p['duration_months'],'total':round(subtotal*(1+p['contingency_rate'])+x['monthly_run_cost']*p['duration_months'],2)})
 assert sum(x['total'] for x in packages)==result['pilot']['total_ceiling']
 assert sum(x['hardware'] for x in p['packages'])==p['hardware_allocation']
 for field,item in [('delivery_days','Delivery'),('installation_days','Installation'),('training_days','Training'),('data_days','Data preparation'),('specialist_days','Specialist review')]:
  assert sum(x[field] for x in p['packages'])==next(x['quantity'] for x in p['person_days'] if x['item']==item)
 result['pilot']['packages']=packages
 slot_capacity=c['admission_lanes']/c['seconds_per_admission']*c['slot_minutes']*60
 result['capacity']['theoretical_people_per_slot']=slot_capacity
 result['capacity']['proposed_timed_entry_people_per_slot']=c['timed_entry_people_per_slot']
 result['capacity']['slot_headroom_fraction']=round(1-c['timed_entry_people_per_slot']/slot_capacity,4)
 result['capacity']['hours_to_schedule_daily_visits_at_cap']=round(c['visitors_per_day']/c['timed_entry_people_per_slot']*c['slot_minutes']/60,2)
 return result
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
 result=calculate(json.loads((R/'design/cost-inputs.json').read_text()));path=R/'validation/results/cost-model.json'
 if a.check:
  assert json.loads(path.read_text())==result,'Cost results are stale; rerun validation/scripts/calculate_costs.py'
  print('Cost model matches committed inputs and results.')
 else:path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
