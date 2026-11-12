#!/usr/bin/env python3
"""Reproduce the NS-CD6.1 *synthetic* conceptual-design case, no third-party packages.

These calculations are a decision-study teaching example, not an approved
mobility-system model, safety argument or observed field measurement.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path

CASE=Path(__file__).resolve().parents[1]/'case'

def records(name):
    with (CASE/name).open(newline='',encoding='utf8') as f:return list(csv.DictReader(f))

def model():return json.loads((CASE/'model-baseline.json').read_text(encoding='utf8'))

def capacity(c):
    if c['vehicles'] and c['roundtrip_min']<=0:raise ValueError('Invalid cycle time')
    if not (0<=c['utilization']<=1 and 0<=c['pod_utilization']<=1 and 0<=c['contract_factor']<=1):raise ValueError('Invalid usable fractions')
    fixed=(c['vehicles']*c['seats']*60/c['roundtrip_min']*c['utilization']) if c['vehicles'] else 0
    pods=c['pods']*c['pod_trips_h']*c['pod_utilization']
    contract=c['contract_trips_h']*c['contract_factor']
    return fixed+pods+contract

def feasible(c,d):
    t=d['thresholds']
    return (capacity(c)>=t['peak_capacity_min'] and c['p90_wait_min']<=t['p90_wait_max_min'] and
            c['accessible_coverage_pct']>=t['accessible_coverage_min_pct'] and
            c['capex_musd']<=t['capex_max_musd'] and c['opex_musd_per_year']<=t['opex_max_musd_per_year'])

def partial_values(c,d):
    a=d['value']['anchors']
    clamp=lambda x:max(0.0,min(1.0,x))
    return {'wait':clamp((a['wait_min'][1]-c['p90_wait_min'])/(a['wait_min'][1]-a['wait_min'][0])),
            'coverage':clamp((c['accessible_coverage_pct']-a['coverage_pct'][0])/(a['coverage_pct'][1]-a['coverage_pct'][0])),
            'opex':clamp((a['opex_musd'][1]-c['opex_musd_per_year'])/(a['opex_musd'][1]-a['opex_musd'][0]))}

def value(c,d):
    p=partial_values(c,d)
    return sum(p[k]*w for k,w in d['value']['weights'].items())

def switching_wait_weight(c1,c2,d):
    """Weight on wait where equally weighted remaining attributes make c1=c2."""
    a,b=partial_values(c1,d),partial_values(c2,d)
    delta_w=a['wait']-b['wait']
    other=((a['coverage']+a['opex'])-(b['coverage']+b['opex']))/2
    return -other/(delta_w-other)

def life_cycle_cost(c,d):
    years=d['cost']['years'];r=d['cost']['discount_rate']
    if years<=0 or r<0:raise ValueError('Invalid discount assumptions')
    factor=sum((1+r)**(-t) for t in range(1,years+1))
    return c['capex_musd']+c['opex_musd_per_year']*factor

def main_effects():
    data=records('doe-synthetic.csv')
    means={}
    for p in (-1,1):
        for f in (-1,1):
            vals=[float(x['p90_wait_min']) for x in data if int(x['policy_code'])==p and int(x['reserve_code'])==f]
            if len(vals)!=3:raise ValueError('Expected three synthetic replicates per cell')
            means[p,f]=sum(vals)/len(vals)
    policy=((means[1,-1]+means[1,1])-(means[-1,-1]+means[-1,1]))/2
    reserve=((means[-1,1]+means[1,1])-(means[-1,-1]+means[1,-1]))/2
    interaction=(means[1,1]-means[-1,1])-(means[1,-1]-means[-1,-1])
    return {'cell_means':{f'{p},{f}':m for (p,f),m in means.items()},'policy_main_min':policy,'reserve_main_min':reserve,'difference_in_differences_min':interaction}

def schedule(d):
    tasks=d['schedule']['tasks'];result={}
    for t in tasks:
        ps=t['predecessors']
        if any(p not in result for p in ps):raise ValueError('Unordered or missing predecessor')
        start=max((result[p] for p in ps),default=0)
        result[t['id']]=start+t['duration_weeks']
    return {'earliest_finish_weeks':result,'project_weeks':max(result.values())}

def audit(d):
    errors=[]
    req=records('requirements.csv');ev=records('evidence-register.csv');func=records('functions.csv');summary=records('concepts.csv')
    ids={x['id'] for x in req}
    if len(ids)!=len(req) or len(req)!=8:errors.append('requirement identity/size mismatch')
    if len(ev)!=len(ids) or {x['requirement'] for x in ev}!=ids:errors.append('evidence coverage mismatch')
    if len({x['id'] for x in ev})!=len(ev):errors.append('duplicate evidence identifiers')
    if len(func)!=5 or len({x['id'] for x in func})!=len(func):errors.append('function identity mismatch')
    for f in func:
        if any('CD6-'+v not in ids for v in f['requirement_suffixes'].split(',')):
            errors.append('unknown function-to-requirement reference')
    if len(summary)!=len(d['concepts']) or {x['id'] for x in summary}!={c['id'] for c in d['concepts']}:
        errors.append('alternative summary mismatch')
    else:
        matched={x['id']:x for x in summary}
        for c in d['concepts']:
            r=matched[c['id']]
            for key in ['p90_wait_min','accessible_coverage_pct','capex_musd','opex_musd_per_year']:
                if not math.isclose(float(r[key]),float(c[key]),abs_tol=1e-9):errors.append('summary data drift '+c['id']+' '+key)
    return errors

def evidence_statuses(d):
    result={}
    for x in records('evidence-register.csv'):
        if x['baseline']!=d['baseline']:status='STALE'
        elif x['status']=='MODEL_PASS':status='PROVISIONAL_MODEL_PASS'
        elif x['status']=='MODEL_FAIL':status='FAILED_MODEL_CASE'
        elif x['status'] in ('PLANNED','NOT_EXECUTED'):status='NO_EXECUTED_TEST'
        else:status=x['status']
        result[x['requirement']]=status
    return result

def report(d):
    if audit(d):raise ValueError('Invalid controlled case: '+repr(audit(d)))
    options=[{'id':c['id'],'name':c['name'],'effective_trips_per_hour':round(capacity(c),6),
              'screen_pass':feasible(c,d),'value':round(value(c,d),6),'lcc_musd':round(life_cycle_cost(c,d),6)} for c in d['concepts']]
    feasible_ids=[x for x in options if x['screen_pass']]
    if not feasible_ids:raise ValueError('No feasible modeled options')
    winner=max(feasible_ids,key=lambda x:x['value'])
    b,c=next(x for x in d['concepts'] if x['id']=='B'),next(x for x in d['concepts'] if x['id']=='C')
    ev=evidence_statuses(d)
    return {'baseline':d['baseline'],'capacity_required_trips_per_hour':d['demand']['peak_trips_per_hour']*(1+d['demand']['reserve_fraction']),
            'options':options,'screened_winner_for_pilot_only':winner['id'],'wait_weight_switch_B_over_C':switching_wait_weight(b,c,d),
            'C_nominal_timing_ms':sum(d['timing']['nominal_ms']),'C_degraded_timing_ms':sum(d['timing']['degraded_ms']),
            'C_capacity_after_10pct_loss':capacity(c)*.90,'C_capacity_after_15pct_loss':capacity(c)*.85,
            'doe':main_effects(),'schedule':schedule(d),'evidence':ev,
            'operational_release':'HOLD','decision_note':'C is a conditional concept for experiment, not an operationally verified design'}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--json',action='store_true');args=parser.parse_args()
    data=report(model())
    if args.json:print(json.dumps(data,indent=2))
    else:
        for o in data['options']:print(f"{o['id']}: capacity={o['effective_trips_per_hour']:.2f}/h screen={o['screen_pass']} value={o['value']:.4f} LCC=${o['lcc_musd']:.3f}M")
        print('Recommended for pilot:',data['screened_winner_for_pilot_only'],'operational release:',data['operational_release'])
        print('DOE:',data['doe'])

if __name__=='__main__':main()
