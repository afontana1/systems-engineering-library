"""Northstar teaching tools: typed model validation and energy constraints."""
from pathlib import Path
import json
HERE=Path(__file__).parent

def model_status(model):
    edges=model['edges']; runs={r['test']:r for r in model['executions']}
    out={}
    for req in model['requirements']:
        rid=req['id']
        b=[e['source'] for e in edges if e['kind']=='satisfies' and e['target']==rid and e['source'].startswith('B')]
        t=[e['source'] for e in edges if e['kind']=='verifies' and e['target']==rid and e['source'].startswith('T')]
        if not b:out[rid]='MISSING_SATISFACTION';continue
        if not t:out[rid]='MISSING_TEST';continue
        found=[runs[x] for x in t if x in runs]
        if not found:out[rid]='NO_EXECUTION';continue
        versioned=[r for r in found if r['req_rev']==req['rev']]
        if not versioned:out[rid]='STALE_EXECUTION';continue
        match=[r for r in versioned if r['config']==model['release_config']]
        if not match:out[rid]='WRONG_CONFIGURATION';continue
        out[rid]='SUPPORTED' if any(r['result']=='PASS' for r in match) else 'FAILED'
    return out

def budget(s):
    for k in ['length_km','rate_kwh_per_km','hvac_kwh_per_trip','trips','capacity_kwh','reserve_fraction']:
        if s[k]<0:raise ValueError('negative parameter: '+k)
    if s['reserve_fraction']>=1:raise ValueError('reserve fraction must be <1')
    demand=s['trips']*(s['length_km']*s['rate_kwh_per_km']+s['hvac_kwh_per_trip'])
    allowed=s['capacity_kwh']*(1-s['reserve_fraction'])
    return {'demand_kwh':demand,'allowable_kwh':allowed,'margin_kwh':allowed-demand,'feasible':allowed>=demand}

if __name__=='__main__':
    model=json.loads((HERE/'model.json').read_text())
    scenarios=json.loads((HERE/'energy.json').read_text())
    print(json.dumps({'model':model_status(model),'energy':{k:budget(v) for k,v in scenarios.items()}},indent=2))
