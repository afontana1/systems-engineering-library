#!/usr/bin/env python3
"""NS-G4.1 synthetic safety/human/software/resilience/SoS/enterprise evidence case.

This is a *screening and teaching model*, NOT operational dispatch code, security
verification, formal proof, or authorization. Standard library only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from collections import deque
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / 'data/ns-g4.1-case.json'
OUTPUT = BASE / 'outputs/ns-g4.1-results.json'


def positive_number(x, name, zero_ok=False):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) or (x < 0 if zero_ok else x <= 0):
        raise ValueError(f'invalid {name}')
    return float(x)


def probability(x, name):
    val=positive_number(x, name, zero_ok=True)
    if val>1: raise ValueError(f'{name} is not a probability')
    return val


def read_case(path=INPUT):
    raw=json.loads(Path(path).read_text(encoding='utf-8'))
    if raw.get('case_id')!='NS-G4.1': raise ValueError('incorrect case identity')
    for k in ('policies','scenarios'):
        if not raw.get(k) or len(set(x['id'] for x in raw[k]))!=len(raw[k]):
            raise ValueError('duplicate or absent '+k)
    total=sum(probability(s['weight'],'scenario weight') for s in raw['scenarios'])
    if abs(total-1)>1e-10: raise ValueError('scenario weights must sum to one')
    for p in raw['policies']:
        for k in ('added_cost_million','operator_service_per_hour','urban_mean_wait_minutes','accessible_mean_wait_minutes'):
            positive_number(p[k],k,zero_ok=(k!='operator_service_per_hour'))
        for k in ('local_node_availability','common_outage_probability','alarm_false_positive_rate'):
            probability(p[k],k)
    for arc in raw['sos']['arcs']:
        positive_number(arc['capacity'],'arc capacity',zero_ok=True)
        if arc['from']==arc['to']: raise ValueError('self loop')
    return raw


def bound_age(decision, observation, execution, skew):
    for x,n in [(decision,'decision time'),(observation,'observation time'),(execution,'execution delay'),(skew,'clock skew')]:
        positive_number(x,n,zero_ok=True)
    if decision < observation: raise ValueError('observation in future')
    return decision-observation+execution+skew


def queue_wait_minutes(arrival, service):
    positive_number(arrival,'arrival',zero_ok=True)
    positive_number(service,'service')
    if arrival>=service: return None  # no finite stationary M/M/1 expectation
    return 60*arrival/(service*(service-arrival))


def alarm_ppv(prevalence,sensitivity,false_positive):
    p=probability(prevalence,'prevalence');s=probability(sensitivity,'sensitivity');f=probability(false_positive,'false positive rate')
    den=s*p+f*(1-p)
    if den==0:raise ValueError('zero probability of positive alarm')
    return s*p/den


def retry_load(external, retry, service):
    positive_number(external,'external events',zero_ok=True)
    p=probability(retry,'retry probability')
    positive_number(service,'server rate')
    if p==1: return {'offered_per_second': None,'stable':False}
    offered=external/(1-p)
    return {'offered_per_second':offered,'stable':offered<service}


def trace_audit(events):
    """Sequential reference protocol: reserve -> commit -> ack. Duplicate replay allowed.
    Detects invalid ordering and conflicting payloads. Not a concurrency proof.
    """
    next_seq={};states={};payloads={};seen=set();issues=[];duplicates=0
    allowed={'RESERVE':(None,'reserved'),'COMMIT':('reserved','committed'),'ACK':('committed','acknowledged')}
    for e in events:
        key=e['key'];event=(key,e['seq'],e['type'],e['payload_hash'])
        if event in seen:
            duplicates+=1;continue
        seen.add(event)
        if key in payloads and payloads[key]!=e['payload_hash']:
            issues.append(f"{e['event_id']}:payload_conflict");continue
        if not isinstance(e['seq'],int) or isinstance(e['seq'],bool) or e['seq']!=next_seq.get(key,1):
            issues.append(f"{e['event_id']}:sequence_gap");continue
        action=e['type'];need,nxt=allowed.get(action,(False,None))
        if need is False or states.get(key)!=need:
            issues.append(f"{e['event_id']}:illegal_transition");continue
        payloads.setdefault(key,e['payload_hash']);states[key]=nxt;next_seq[key]=e['seq']+1
    return {'accepted_unique_events':sum(v-1 for v in next_seq.values()),'idempotent_duplicates':duplicates,'violations':issues,'state_by_key':states}


def availability(local, common, route, dispatch):
    """Independent local replica faults *conditional on* absence of common outage;
    serial route and dispatch components are also assumed independent."""
    local=probability(local,'local availability');common=probability(common,'common outage')
    route=probability(route,'route availability');dispatch=probability(dispatch,'dispatch availability')
    return (1-common)*(1-(1-local)**2)*route*dispatch


def max_flow(arcs, source, sink, excluded=frozenset(), loss=0, rail_boost=0, para_boost=0):
    """Edmonds-Karp integer-like capacity flow. Flows are abstract trip slots,
    not guaranteed physically schedulable trips or independent paths."""
    positive_number(loss,'capacity loss',zero_ok=True)
    if source==sink: raise ValueError('different endpoints required')
    if source in excluded or sink in excluded: return 0.0
    residual={}
    for e in arcs:
        a,b=e['from'],e['to']
        if a in excluded or b in excluded:continue
        cap=positive_number(e['capacity'],'arc capacity',zero_ok=True)
        if a=='Dispatch' and b=='Rail':cap+=rail_boost
        if a=='Rail' and b=='Care':cap+=rail_boost
        if a=='Dispatch' and b=='Paratransit':cap+=para_boost
        if a=='Paratransit' and b=='Care':cap+=para_boost
        if a=='Request' and b=='Dispatch': cap=max(0,cap-loss)
        if cap<0:raise ValueError('negative adjusted arc')
        residual[(a,b)]=residual.get((a,b),0)+cap
        residual.setdefault((b,a),0.0)
    total=0.0
    while True:
        parent={source:None};queue=deque([source])
        while queue and sink not in parent:
            u=queue.popleft()
            for (a,b),cap in residual.items():
                if a==u and cap>1e-10 and b not in parent:
                    parent[b]=a;queue.append(b)
        if sink not in parent:break
        cap=math.inf;v=sink
        while v!=source:cap=min(cap,residual[(parent[v],v)]);v=parent[v]
        v=sink
        while v!=source:
            u=parent[v];residual[(u,v)]-=cap;residual[(v,u)]+=cap;v=u
        total+=cap
    return total


def difference_in_differences(ent):
    for k in ('treated_pre_minutes','treated_post_minutes','comparison_pre_minutes','comparison_post_minutes'):
        positive_number(ent[k],k,zero_ok=True)
    return ((ent['treated_post_minutes']-ent['treated_pre_minutes'])
            -(ent['comparison_post_minutes']-ent['comparison_pre_minutes']))


def pretrend_gap(ent):
    a=ent['treated_pre_pre_minutes'];b=ent['comparison_pre_pre_minutes']
    if len(a)!=2 or len(b)!=2:raise ValueError('need two pre-intervention values for each group')
    return (a[1]-a[0])-(b[1]-b[0])


def evaluate(case, policy, scenario):
    safety=case['safety'];svc=case['service'];rel=case['reliability'];sos=case['sos'];ent=case['enterprise']
    age=bound_age(safety['decision_clock_seconds'],policy['observed_clock_seconds'],
                  safety['execution_window_seconds'],safety['skew_bound_seconds']+scenario['clock_skew_extra_seconds'])
    expected=scenario['revision_override'] or safety['expected_route_revision']
    safe=(age<=safety['freshness_limit_seconds'] and safety['valid_signature']
          and policy['route_revision']==expected)
    arrival=svc['alarm_arrival_per_hour']*scenario['demand_multiplier']
    wait=queue_wait_minutes(arrival,policy['operator_service_per_hour'])
    ppv=alarm_ppv(svc['case_prevalence'],svc['alarm_sensitivity'],policy['alarm_false_positive_rate'])
    retry=retry_load(svc['external_events_per_second'],svc['retry_probability'],svc['software_service_per_second'])
    common=policy['common_outage_probability']+scenario['common_outage_add']
    joint=availability(policy['local_node_availability'],common,
                       rel['route_authority_availability'],rel['dispatch_availability'])
    flow=max_flow(sos['arcs'],sos['source'],sos['sink'],set(scenario['disabled_constituents']),
                  scenario['capacity_loss'],policy['rail_capacity_delta'],policy['paratransit_capacity_delta'])
    need=sos['min_accessible_slots']*scenario['demand_multiplier']
    latency_ok=wait is not None and wait<=svc['max_queue_wait_minutes']
    checks={'route_authorized':safe,'human_queue':latency_ok,'alarm_quality':ppv>=svc['min_alarm_ppv'],
            'retry_stable':retry['stable'],'joint_availability':joint>=rel['min_joint_availability'],
            'accessible_flow':flow>=need}
    return {'policy':policy['id'],'scenario':scenario['id'],'freshness_bound_seconds':age,
            'route_revision_matches':policy['route_revision']==expected,
            'operator_wait_minutes':wait,'alarm_ppv':ppv,'software_retry_offered_per_second':retry['offered_per_second'],
            'joint_availability':joint,'accessible_max_flow_slots':flow,'accessible_needed_slots':need,
            'checks':checks,'technical_screen_pass':all(checks.values())}


def run(case):
    if case['case_id']!='NS-G4.1':raise ValueError('wrong case')
    trace=trace_audit(case['sample_events'])
    ent=case['enterprise'];missing=[p for p in ent['require_permissions'] if not ent['permissions_granted'].get(p,False)]
    results=[];summaries=[]
    for policy in case['policies']:
        matrix=[evaluate(case,policy,s) for s in case['scenarios']]
        results.extend(matrix)
        coverage=sum(s['weight'] for s,r in zip(case['scenarios'],matrix) if r['technical_screen_pass'])
        gap=policy['accessible_mean_wait_minutes']-policy['urban_mean_wait_minutes']
        enterprise_gate=(policy['added_cost_million']<=ent['max_added_cost_million']
                         and gap<=ent['max_group_wait_gap_minutes'] and not missing)
        summaries.append({'policy':policy['id'],'added_cost_million':policy['added_cost_million'],
            'scenario_technical_coverage_weight':round(coverage,6),'wait_gap_minutes':gap,
            'resource_and_equity_screen':policy['added_cost_million']<=ent['max_added_cost_million'] and gap<=ent['max_group_wait_gap_minutes'],
            'enterprise_permission_gate':enterprise_gate,'operational_authorized':False,
            'disposition':'HOLD: technical screening does not confer authorization'})
    return {'case_id':case['case_id'],'revision':case['revision'],
        'model_scope':'Synthetic finite-scenario screening; not statistical reliability, signature verification, calibration, or authorization',
        'interface_trace_audit':trace,
        'enterprise':{'difference_in_differences_minutes':difference_in_differences(ent),
                      'pretrend_difference_minutes':pretrend_gap(ent),
                      'missing_permissions':missing,
                      'causal_claim_validated':False},
        'runs':results,'policies':summaries,
        'overall_disposition':'HOLD: no validated deployment authority, even if a policy clears selected numerical screens'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',default=str(INPUT));parser.add_argument('--output',default=str(OUTPUT))
    args=parser.parse_args()
    p=Path(args.input);case=read_case(p)
    report=run(case);report['input_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
    target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('NS-G4.1:',len(report['runs']),'case/policy pairs; interface violations:',len(report['interface_trace_audit']['violations']))
    for p in report['policies']:
        print(p['policy'], 'scenario screen',round(100*p['scenario_technical_coverage_weight'],1),'%',p['disposition'])

if __name__=='__main__':main()
