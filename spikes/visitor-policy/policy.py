"""Small deterministic itinerary boundary. No LLM, authentication or live APIs."""
from datetime import datetime

def instant(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))

def evaluate(candidate, fixture, constraints):
    """Accept only known, current activity IDs; render facts from authority data.

    Candidate prose and executable tools are intentionally outside this contract.
    The real application must derive constraints outside the model (visitor form
    or visitor-confirmed interpretation), and authenticate its fact sources.
    """
    def fail(reason):
        return {'decision': 'fallback', 'reason': reason, 'options': []}
    if fixture.get('budget_available') is not True:
        return fail('budget_unavailable')
    if fixture.get('provider_available') is not True:
        return fail('provider_unavailable')
    if not isinstance(candidate, dict) or set(candidate) != {'activity_ids', 'source_refs'}:
        return fail('schema')
    ids, refs = candidate['activity_ids'], candidate['source_refs']
    if not isinstance(ids, list) or not 1 <= len(ids) <= 3 or any(not isinstance(i, str) for i in ids) or len(set(ids)) != len(ids):
        return fail('schema')
    if not isinstance(refs, list) or not refs or any(not isinstance(r, dict) or set(r) != {'id','version'} or not isinstance(r['id'],str) or type(r['version']) is not int for r in refs):
        return fail('schema')
    try:
        now = instant(fixture['now'])
        docs = {d['id']: d for d in fixture['documents']}
        seen = set()
        for ref in refs:
            key = (ref['id'], ref['version'])
            if key in seen: return fail('duplicate_source')
            seen.add(key)
            doc = docs.get(ref['id'])
            if not doc or doc['version'] != ref['version'] or doc['approved'] is not True or instant(doc['expires_at']) <= now:
                return fail('source_invalid')
        options=[]
        for aid in ids:
            a=fixture['activities'].get(aid)
            if not a: return fail('unknown_activity')
            if a['status'] != 'open': return fail('not_open')
            age=(now-instant(a['observed_at'])).total_seconds()
            if age < 0 or age > fixture['freshness_seconds']: return fail('status_not_current')
            if constraints.get('wheelchair') and a.get('step_free') is not True: return fail('access_constraint')
            if a['duration_minutes'] > constraints.get('max_minutes',float('inf')): return fail('time_constraint')
            if a.get('minimum_height_cm',0) > constraints.get('child_height_cm',float('inf')): return fail('height_constraint')
            if (a['source_id'],a['source_version']) not in seen: return fail('source_missing')
            options.append({'activity_id':aid,'name':a['name'],'status':'open','status_at':a['observed_at'],'step_free':a['step_free'],'minutes_including_route':a['duration_minutes'],'source':{'id':a['source_id'],'version':a['source_version']}})
    except (KeyError, TypeError, ValueError, OverflowError):
        return fail('invalid_authority_data')
    return {'decision':'show_options','reason':'policy_pass','options':options,'display_mode':'independent_options_not_a_combined_route'}
