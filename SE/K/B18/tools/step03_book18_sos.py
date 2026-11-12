#!/usr/bin/env python3
"""NS-SOS18.1: standard-library illustrative SoS mission screening.

The deterministic flow allocator is a bounded engineering teaching model, NOT
network traffic simulation, interoperability conformance, or field validation.
"""
from __future__ import annotations
import argparse
import csv
import copy
import json
import math
from pathlib import Path

CASE = Path(__file__).resolve().parents[1] / 'case'
ROUTES = ('shuttle','paratransit','bus','rail')
RESOURCES = ROUTES + ('dispatch','hospital','accessible_intake')
KNOWN_POLICIES = ('status-quo','backup-power','data-federation','integrated')


def load(path: Path | None = None):
    with (path or CASE / 'controlled-inputs.json').open(encoding='utf-8') as stream:
        return json.load(stream)


def finite(x, minimum=0, maximum=math.inf):
    return type(x) in (int,float) and math.isfinite(x) and minimum <= x <= maximum


def validate(c):
    if not isinstance(c,dict) or c.get('case_id')!='NS-SOS18.1' or c.get('intended_use')!='synthetic instructional architecture screening only':
        raise ValueError('Wrong case or claimed intended use')
    if not finite(c.get('time_horizon_hours'),1,24):raise ValueError('Horizon')
    t=c.get('targets',{})
    for key,lo,hi in [('accessible_trips',1,1000),('standard_trips',1,1000),('max_data_age_min',0.01,120),('joint_coverage',0.01,1)]:
        if not finite(t.get(key),lo,hi):raise ValueError('Target '+key)
    r=c.get('resources',{})
    if set(r)!=set(RESOURCES) or any(not finite(r[k],1,10000) for k in RESOURCES):raise ValueError('Resources')
    g=c.get('governance',{})
    if any(not isinstance(g.get(k),str) or not g.get(k) for k in ('dispatch_owner','hospital_owner','paratransit_owner','rail_owner','interface_expected_revision','interface_current_revision')):raise ValueError('Authority/contract')
    if type(g.get('evidence_current')) is not bool:raise ValueError('Evidence must be boolean')
    scenarios=c.get('scenarios',[])
    if [s.get('id') for s in scenarios]!=['normal','grid','flood','comms']:raise ValueError('Scenario identity/order')
    if not math.isclose(sum(s.get('probability',0) for s in scenarios),1,abs_tol=1e-12):raise ValueError('Probability mass')
    for s in scenarios:
        if not finite(s.get('probability'),0,1):raise ValueError('Scenario probability')
        validate_scenario(s)
    validate_scenario(c.get('stress_scenario',{}))
    ps=c.get('policies',[])
    if [p.get('id') for p in ps]!=list(KNOWN_POLICIES):raise ValueError('Policy identity/order')
    for p in ps:
        if not finite(p.get('added_cost_musd'),0,1000):raise ValueError('Policy cost')
        for sid,delta in p.get('overrides',{}).items():
            if sid not in [s['id'] for s in scenarios] or not isinstance(delta,dict):raise ValueError('Unknown scenario override')
            if set(delta)-{'factors','data_age_min'}:raise ValueError('Unexpected override')
            factors=delta.get('factors',{})
            if set(factors)-set(RESOURCES) or any(not finite(v,0,1) for v in factors.values()):raise ValueError('Override factors')
            if 'data_age_min' in delta and not finite(delta['data_age_min'],0,120):raise ValueError('Override freshness')
    b=c.get('bayes',{})
    for k in ('prior_block','initial_alarm_sensitivity','initial_alarm_false_positive','independent_confirm_sensitivity','independent_confirm_false_positive'):
        if not finite(b.get(k),0.00001,0.99999):raise ValueError('Bayesian input '+k)
    if not isinstance(c.get('assumptions'),list) or len(c['assumptions'])<5:raise ValueError('Explicit limitations absent')
    return True


def validate_scenario(s):
    if not isinstance(s.get('id'),str) or not s['id']:raise ValueError('Missing scenario')
    if not finite(s.get('data_age_min'),0,120):raise ValueError('Data age')
    factors=s.get('factors',{})
    if not isinstance(factors,dict) or set(factors)!=set(RESOURCES) or any(not finite(v,0,1) for v in factors.values()):raise ValueError('Scenario factors')


def posterior(prior,sensitivity,false_positive):
    if any(not finite(v,0,1) for v in (prior,sensitivity,false_positive)):raise ValueError('Invalid Bayes probability')
    positive=prior*sensitivity+(1-prior)*false_positive
    if positive==0:raise ValueError('Impossible evidence')
    return prior*sensitivity/positive


def bayes_study(c):
    b=c['bayes']
    first=posterior(b['prior_block'],b['initial_alarm_sensitivity'],b['initial_alarm_false_positive'])
    second=posterior(first,b['independent_confirm_sensitivity'],b['independent_confirm_false_positive'])
    return {'prior_block':b['prior_block'],'first_positive_posterior':first,'second_independent_positive_posterior':second}


def effective(s,p):
    factors=dict(s['factors'])
    data_age=s['data_age_min']
    delta=p.get('overrides',{}).get(s['id'],{})
    factors.update(delta.get('factors',{}))
    if 'data_age_min' in delta:data_age=delta['data_age_min']
    return factors,data_age


def screen(c,policy,scenario,revision=None,evidence_current=None):
    validate(c)
    p=next((x for x in c['policies'] if x['id']==policy),None)
    if p is None:raise ValueError('Unknown policy')
    s=next((x for x in c['scenarios']+[c['stress_scenario']] if x['id']==scenario),None)
    if s is None:raise ValueError('Unknown scenario')
    factors,age=effective(s,p)
    cap={k:c['resources'][k]*factors[k] for k in RESOURCES}
    # Parallel channels are bottlenecked by their independently owned
    # interfaces, and shared capacity is allocated to accessible service first.
    access_path=min(cap['shuttle']+cap['paratransit'],cap['accessible_intake'])
    standard_path=cap['bus']+cap['rail']
    common=min(cap['dispatch'],cap['hospital'])
    access=min(c['targets']['accessible_trips'],access_path,common)
    standard=min(c['targets']['standard_trips'],standard_path,max(0,common-access))
    g=c['governance']
    current_revision = g['interface_current_revision'] if revision is None else revision
    fresh_evidence = g['evidence_current'] if evidence_current is None else evidence_current
    if not isinstance(current_revision,str) or not current_revision or type(fresh_evidence) is not bool:raise ValueError('Invalid interface change')
    interface_current=current_revision==g['interface_expected_revision'] and fresh_evidence
    flow_ok=access+1e-9>=c['targets']['accessible_trips'] and standard+1e-9>=c['targets']['standard_trips']
    data_ok=age<=c['targets']['max_data_age_min']
    qualifies=flow_ok and data_ok and interface_current
    return {'policy':policy,'scenario':scenario,'probability':s.get('probability',None),'access_path_capacity':round(access_path,4),'standard_path_capacity':round(standard_path,4),'shared_capacity':round(common,4),'accessible_delivered':round(access,4),'standard_delivered':round(standard,4),'data_age_min':age,'flow_ok':flow_ok,'data_ok':data_ok,'interface_current':interface_current,'joint_screen_pass':qualifies}


def evaluate(c):
    validate(c)
    result=[]
    detailed=[]
    for policy in c['policies']:
        rows=[screen(c,policy['id'],s['id']) for s in c['scenarios']]
        probability=sum(row['probability'] for row in rows if row['joint_screen_pass'])
        result.append({'policy':policy['id'],'cost_musd':policy['added_cost_musd'],'joint_coverage':round(probability,6),'target':c['targets']['joint_coverage'],'nominal_screen_pass':probability+1e-10>=c['targets']['joint_coverage'],'compound_stress_pass':screen(c,policy['id'],c['stress_scenario']['id'])['joint_screen_pass']})
        detailed.extend(rows)
    return result,detailed


def write_csv(path,rows):
    with path.open('w',encoding='utf-8',newline='') as stream:
        w=csv.DictWriter(stream,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)


def publish(c):
    summary,details=evaluate(c)
    write_csv(CASE/'policy-coverage.csv',summary)
    write_csv(CASE/'scenario-screens.csv',details)
    record={'case_id':c['case_id'],'model_kind':'illustrative deterministic bottleneck screening, not field calibration','bayes':bayes_study(c),'scenario_assumptions':c['assumptions'],'stress_all_policies':{p['id']:screen(c,p['id'],c['stress_scenario']['id']) for p in c['policies']},'live_constituent_change':screen(c,'integrated','normal',revision='2.0',evidence_current=False),'decision':'HOLD pending real constituent agreements, performance data, interface tests, hazard review, and authorizing review'}
    (CASE/'computed-evidence.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    return summary


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    c=load();validate(c)
    if args.check:
        s,_=evaluate(c)
        print('Validated synthetic model:',s)
    else:
        print(json.dumps(publish(c),indent=2))

if __name__=='__main__':main()
