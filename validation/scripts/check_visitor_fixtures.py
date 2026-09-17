#!/usr/bin/env python3
"""Resolve every synthetic case; no provider call and no answer-quality score."""
from pathlib import Path
import copy,json
R=Path(__file__).resolve().parents[2]
D=R/'validation/datasets'
def materialize(case):
 path=(D/case['fixture']['path']).resolve()
 assert path.is_relative_to(D.resolve()) and path.is_file()
 result=json.loads(path.read_text());result['now']=case['fixture']['now']
 for key,value in case['fixture']['overrides'].items():
  parts=key.split('.');obj=result
  for part in parts[:-1]:
   if isinstance(obj,list):obj=next(x for x in obj if x['id']==part)
   else:obj=obj[part]
  assert parts[-1] in obj,key
  obj[parts[-1]]=copy.deepcopy(value)
 return result
if __name__=='__main__':
 cases=json.loads((D/'visitor-scenario-specifications.json').read_text())['cases']
 assert len(cases)==48 and len({c['id'] for c in cases})==48
 for c in cases:
  f=materialize(c);o=c['oracle']
  assert c['result'] is None and o['result'] is None
  assert o['decision'] and o['required_facts'] and o['forbidden_claims']
  assert set(o['required_source_ids']) <= {d['id'] for d in f['documents']}
 print('PASS: 48 synthetic cases; concrete fixtures, overrides and source references resolve. No model evaluation executed.')
