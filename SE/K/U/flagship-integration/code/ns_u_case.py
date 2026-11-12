#!/usr/bin/env python3
"""NS-U4.1 flagship teaching case. Synthetic, deterministic, standard library only.

This executable supplies quantitative examples and counterexamples; it is NOT
an operational dispatch simulation, a safety qualification, or a SysML parser.
"""
from __future__ import annotations
import copy
import json
import math
from pathlib import Path
from statistics import mean,stdev

BASE=Path(__file__).resolve().parents[1]
INPUT=BASE/'data/ns-u4.1-case.json'
OUTPUT=BASE/'outputs/ns-u4.1-results.json'

class InvalidCase(ValueError): pass

def check(d):
    for root in ('requirements','demand','policies','scenarios','diagnostic','reliability','claims','interface_events','institutional_authorizations'):
        if root not in d: raise InvalidCase(f'missing {root}')
    if set(d['demand'])!={'standard','accessible'}:raise InvalidCase('two demand classes required')
    s,a=d['demand'].values()
    if not s or len(s)!=len(a) or any(type(v)!=int or v<0 for v in s+a):raise InvalidCase('nonnegative equal-length integer arrivals required')
    for p in d['policies'].values():
        if any(type(p[k])!=int or p[k]<0 for k in ('standard_capacity','accessible_capacity')):raise InvalidCase('capacities must be nonnegative integers')
        if not math.isfinite(p['added_cost_million']) or p['added_cost_million']<0:raise InvalidCase('invalid cost')
    weights=[v['weight'] for v in d['scenarios'].values()]
    if not all(math.isfinite(w) and w>=0 for w in weights) or not math.isclose(sum(weights),1,abs_tol=1e-9):raise InvalidCase('scenario weights must sum to 1')
    for v in d['scenarios'].values():
        if not all(math.isfinite(v[x]) and v[x]>0 for x in ('demand_factor','capacity_factor')):raise InvalidCase('scenario factors must be positive')
    for k in ('timely_fraction','accessible_timely_fraction','mission_availability','scenario_coverage'):
        if not 0<=d['requirements'][k]<=1:raise InvalidCase('invalid screening requirement')
    for k in ('prior_blocked','sensitivity','false_positive'):
        if not 0<=d['diagnostic'][k]<=1:raise InvalidCase('invalid diagnostic probability')
    if not 0<d['reliability']['component_availability']<=1 or not 0<=d['reliability']['common_cause_failure']<1:raise InvalidCase('invalid reliability')
    if d['requirements']['clock_uncertainty_seconds']<0:raise InvalidCase('invalid clock uncertainty')
    if len(d['paired_wait_min']['baseline'])!=len(d['paired_wait_min']['integrated']) or len(d['paired_wait_min']['baseline'])<3:raise InvalidCase('paired trials mismatch')
    if not all(math.isfinite(x) and x>=0 for v in d['paired_wait_min'].values() for x in v):raise InvalidCase('nonfinite wait')
    if len({c['id'] for c in d['claims']})!=len(d['claims']):raise InvalidCase('duplicate claim identifier')
    if not d['required_interface_revision']:raise InvalidCase('revision required')

def flows(d,policy,scenario):
    """FIFO within each service class; unused capacity does not transfer classes.

    Timely means served in the arrival window. This is NOT a pickup-time model.
    Unfinished requests remain visible at the observation horizon.
    """
    totals={};records={}
    for group in ('standard','accessible'):
        old=0;arrivals=0;served=0;timely=0;steps=[]
        for v in d['demand'][group]:
            new=math.floor(v*scenario['demand_factor']+.5)
            cap=math.floor(policy[group+'_capacity']*scenario['capacity_factor']+.5)
            use=min(old+new,cap)
            # Old requests take service priority; fresh service is bounded by remaining capacity.
            on_time=min(new,max(0,use-old))
            after=old+new-use
            steps.append({'arrivals':new,'capacity':cap,'served':use,'timely':on_time,'unfinished':after})
            old=after;arrivals+=new;served+=use;timely+=on_time
        assert arrivals==served+old
        totals[group]={'arrivals':arrivals,'served':served,'timely':timely,'unfinished':old,'timely_fraction':timely/arrivals if arrivals else None}
        records[group]=steps
    total_arrivals=sum(v['arrivals'] for v in totals.values())
    total_timely=sum(v['timely'] for v in totals.values())
    passing=(total_timely/total_arrivals>=d['requirements']['timely_fraction'] and
             (totals['accessible']['timely_fraction'] is not None and totals['accessible']['timely_fraction']>=d['requirements']['accessible_timely_fraction']))
    return {'by_class':totals,'trace':records,'timely_fraction':total_timely/total_arrivals if total_arrivals else None,'passes_screen':passing}

def check_events(d):
    known={};committed=set();problems=[];duplicates=0
    for i,e in enumerate(d['interface_events'],1):
        if e['revision']!=d['required_interface_revision']:problems.append({'index':i,'type':'stale_revision'});continue
        key=e['event_id']
        if key in known:
            if known[key]==e:duplicates+=1
            else:problems.append({'index':i,'type':'conflicting_replay'})
            continue
        known[key]=e
        if e['type']=='COMMIT':committed.add(e['request_id'])
        elif e['type']=='ACK':
            if e['request_id'] not in committed:problems.append({'index':i,'type':'ack_before_commit'})
        else:problems.append({'index':i,'type':'unknown_event'})
    return {'distinct_event_ids_seen':len(known),'exact_duplicates':duplicates,'violations':problems,'conforming':not problems}

def run(d):
    check(d)
    policies={};coverage={}
    for pn,p in d['policies'].items():
        records={n:flows(d,p,s) for n,s in d['scenarios'].items()}
        weight=sum(d['scenarios'][n]['weight'] for n,v in records.items() if v['passes_screen'])
        policies[pn]={'added_cost_million':p['added_cost_million'],'scenarios':records,'scenario_weight_covered':weight,'all_scenarios_pass':all(v['passes_screen'] for v in records.values())}
        coverage[pn]=weight
    threshold=d['requirements']['dispatch_latency_seconds'];guard=d['requirements']['clock_uncertainty_seconds']
    latencies=[7.9 if i in (50,55,60,65,70) else 6.5 if i<72 else 10.0 for i in range(80)]
    group=[i%5==0 for i in range(80)]
    nominal=sum(t<=threshold for t in latencies)
    conservative=sum(t+guard<=threshold for t in latencies)
    a_n=sum(g for g in group);a_ok=sum(g and t+guard<=threshold for g,t in zip(group,latencies))
    pri=d['diagnostic']['prior_blocked'];se=d['diagnostic']['sensitivity'];fp=d['diagnostic']['false_positive']
    denom=pri*se+(1-pri)*fp
    if denom==0: raise InvalidCase('alarm evidence has probability zero')
    posterior=pri*se/denom
    denom2=posterior*se+(1-posterior)*fp
    second=posterior*se/denom2 if denom2 else None
    diffs=[x-y for x,y in zip(d['paired_wait_min']['baseline'],d['paired_wait_min']['integrated'])]
    tcrit=2.201 # 95% two-sided Student t, df=11, only valid with 12 pairs
    if len(diffs)!=12:raise InvalidCase('current teaching CI uses n=12 and t_11=2.201')
    sem=stdev(diffs)/math.sqrt(len(diffs));mdi=mean(diffs)
    fact=d['factorial_wait_min']
    ev=d['project']
    did=d['difference_in_differences']
    rel=d['reliability']; availability=(1-rel['common_cause_failure'])*(1-(1-rel['component_availability'])**2)
    k=d['feedback']['decay_per_min'];u=d['feedback']['input_per_min']
    if k<=0:raise InvalidCase('decay must be positive')
    actionable=[c['id'] for c in d['claims'] if c['evidence_revision']==d['required_interface_revision'] and c['scope']==c['required_scope'] and c['reviewed'] and c['approved']]
    event=check_events(d)
    permitted=all(d['institutional_authorizations'].values())
    ready=bool(permitted and event['conforming'] and len(actionable)==len(d['claims']) and coverage['integrated']>=d['requirements']['scenario_coverage'] and availability>=d['requirements']['mission_availability'] and conservative/len(latencies)>=d['requirements']['timely_fraction'] and a_ok/a_n>=d['requirements']['accessible_timely_fraction'])
    return {
       'identity':d['id'],'model_scope':'synthetic instructional arithmetic, not operational qualification',
       'policies':policies,
       'dispatch_acceptance':{'n':len(latencies),'nominal_timely':nominal,'guarded_timely':conservative,'accessible_n':a_n,'accessible_guarded_timely':a_ok,'guarded_fraction':conservative/len(latencies),'accessible_guarded_fraction':a_ok/a_n},
       'bayesian_alarm':{'one_positive_posterior':posterior,'second_independent_positive_posterior':second},
       'paired_experiment':{'n':len(diffs),'differences':diffs,'mean_improvement_min':mdi,'sem':sem,'student_t_95_interval':[mdi-tcrit*sem,mdi+tcrit*sem]},
       'factorial':{'interaction_minutes':fact['11']-fact['10']-fact['01']+fact['00']},
       'project':{'critical_path_duration_days':max(sum(ev['path_abc']),sum(ev['path_adc'])),'cost_performance_index':ev['earned_value']/ev['actual_cost'],'schedule_variance':ev['earned_value']-ev['planned_value']},
       'causal':{'difference_in_differences_minutes':(did['treatment_post']-did['treatment_pre'])-(did['comparison_post']-did['comparison_pre'])},
       'dynamic':{'equilibrium_requests':u/k,'euler_stable_step_limit_min':2/k,'euler_2min_multiplier':1-2*k,'euler_6min_multiplier':1-6*k},
       'reliability':{'independent_redundancy':1-(1-rel['component_availability'])**2,'common_cause_joint_availability':availability},
       'interface':event,
       'evidence':{'actionable_ids':actionable,'actionable_count':len(actionable),'required_count':len(d['claims']),'authorizations':d['institutional_authorizations']},
       'readiness':{'disposition':'REVIEW' if ready else 'HOLD','reason':'Synthetic model and missing/stale evidence cannot authorize deployment; REVIEW is only permission to seek review.'}}

def main():
    case=json.loads(INPUT.read_text(encoding='utf-8'))
    out=run(case)
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('NS-U4.1',out['readiness']['disposition'], 'evidence',out['evidence']['actionable_count'],'/',out['evidence']['required_count'])
    for k,v in out['policies'].items():print(k, v['scenario_weight_covered'],v['scenarios']['normal']['timely_fraction'])
if __name__=='__main__':main()
