#!/usr/bin/env python3
"""NS-ENT19.1: deterministic synthetic enterprise transformation screening.

Uses only Python's standard library. The weekly cohort queue is an instructional
work-conservation model, not a calibrated service/queueing or enterprise forecast.
Physical four-hour trip-slot screens are separate from 26-week governance workload.
No approval, consent, measured success rate or authority can be inferred.
"""
from __future__ import annotations
import argparse
import csv
import itertools
import json
import math
from collections import deque
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
DATA=BASE/'case/controlled-inputs.json'

def validate(inputs):
    required=('horizon_weeks','opening_requests','weekly_arrivals','initial_adoption','budget_cap_usd_m','workforce_cap_fte')
    for name in required:
        if name not in inputs or not isinstance(inputs[name],(int,float)) or isinstance(inputs[name],bool):raise ValueError(f'Missing or non-numeric {name}')
    if not isinstance(inputs['horizon_weeks'],int) or inputs['horizon_weeks']<=0:raise ValueError('horizon_weeks must be positive integer')
    for name in ('opening_requests','weekly_arrivals','stress_weekly_arrivals'):
        if not isinstance(inputs[name],int) or inputs[name]<0:raise ValueError(f'{name} must be nonnegative integer')
    if inputs['weekly_arrivals']==0:raise ValueError('Arrivals must be positive for closure calculation')
    for key in ('initial_adoption','adoption_growth_with_governance','adoption_attrition','budget_cap_usd_m','workforce_cap_fte','accessible_demand_four_hours','standard_demand_four_hours','accessible_min_fraction','standard_min_fraction','coordination_min_completion_fraction','joint_scenario_target_probability'):
        if not isinstance(inputs[key],(int,float)) or not math.isfinite(inputs[key]):raise ValueError(f'Finite numeric value required: {key}')
    if inputs['stress_weekly_arrivals']<=inputs['weekly_arrivals']:raise ValueError('Stress must exceed baseline arrivals')
    for name in ('budget_cap_usd_m','workforce_cap_fte','accessible_demand_four_hours','standard_demand_four_hours'):
        if inputs[name]<=0:raise ValueError(f'Positive required: {name}')
    for name in ('initial_adoption','adoption_growth_with_governance','adoption_attrition','accessible_min_fraction','standard_min_fraction','coordination_min_completion_fraction','joint_scenario_target_probability'):
        if not 0<=inputs[name]<=1:raise ValueError(f'Fraction outside [0,1]: {name}')
    ids=[i['id'] for i in inputs['investments']]
    if len(ids)!=len(set(ids)) or not ids:raise ValueError('Duplicate or empty investment identifiers')
    lookup={i['id']:i for i in inputs['investments']}
    for i in inputs['investments']:
        if any(not isinstance(i[k],(int,float)) or not math.isfinite(i[k]) for k in ('cost_usd_m','fte','weekly_clearance_gain','accessible_gain','standard_gain')):raise ValueError('Non-finite/non-numeric investment property')
        if i['cost_usd_m']<0 or i['fte']<0 or i['weekly_clearance_gain']<0:raise ValueError('Negative investment resource or capacity')
        if any(g<0 for g in (i['accessible_gain'],i['standard_gain'],i.get('flood_accessible_gain',0),i.get('flood_standard_gain',0))):raise ValueError('Negative physical increments unsupported')
        if len(i['requires'])!=len(set(i['requires'])) or any(dep not in lookup or dep==i['id'] for dep in i['requires']):raise ValueError('Bad dependencies')
    def visit(k,trail):
        if k in trail:raise ValueError('Cyclic investment dependency')
        for dep in lookup[k]['requires']:visit(dep,trail|{k})
    for i in ids:visit(i,set())
    if not inputs.get('scenarios') or len(set(s['id'] for s in inputs['scenarios']))!=len(inputs['scenarios']):raise ValueError('Scenario IDs missing/duplicated')
    if abs(sum(s['probability'] for s in inputs['scenarios'])-1)>1e-9:raise ValueError('Scenario probabilities must sum to 1')
    for s in inputs['scenarios']:
        if any(not isinstance(s[k],(int,float)) or not math.isfinite(s[k]) for k in ('probability','weekly_clearance','accessible_capacity','standard_capacity')):raise ValueError('Non-finite scenario parameter')
        if not 0<=s['probability']<=1 or s['weekly_clearance']<0 or s['accessible_capacity']<0 or s['standard_capacity']<0:raise ValueError('Invalid scenario values')
    for name,chosen in inputs['portfolios'].items():
        if len(set(chosen))!=len(chosen) or any(k not in lookup for k in chosen):raise ValueError(f'Bad portfolio {name}')
    return lookup

def portfolio_resources(chosen,lookup):
    return (round(sum(lookup[k]['cost_usd_m'] for k in chosen),4),round(sum(lookup[k]['fte'] for k in chosen),4))

def prerequisites_ok(chosen,lookup):
    return all(set(lookup[k]['requires']).issubset(chosen) for k in chosen)

def run_queue(inputs,chosen,lookup,scenario,arrivals=None,weekly_records=False):
    arrivals=inputs['weekly_arrivals'] if arrivals is None else arrivals
    if not isinstance(arrivals,int) or arrivals<=0:raise ValueError('positive integer arrivals required')
    # FIFO cohorts carry a synthetic request origin week; week -1 is opening work.
    queue=deque([[-1,inputs['opening_requests']]]) if inputs['opening_requests'] else deque()
    adoption=inputs['initial_adoption']
    completed=0;duration_sum=0;weeks=[];maximum=0
    for t in range(inputs['horizon_weeks']):
        queue.append([t,arrivals])
        gain=sum(lookup[k]['weekly_clearance_gain'] for k in chosen)
        capacity=scenario['weekly_clearance'] + round(adoption*gain)
        available=capacity
        while available>0 and queue:
            origin,count=queue[0]
            moved=min(count,available)
            completed+=moved;duration_sum+=moved*(t-origin+1)
            queue[0][1]-=moved;available-=moved
            if queue[0][1]==0:queue.popleft()
        backlog=sum(n for _,n in queue)
        maximum=max(maximum,backlog)
        weeks.append({'week':t+1,'arrivals':arrivals,'processing_capacity':capacity,'completed_total':completed,'unresolved':backlog,'adoption':round(adoption,6)})
        if 'G' in chosen:
            adoption=min(1,max(0,adoption+inputs['adoption_growth_with_governance']*(1-adoption)-inputs['adoption_attrition']*adoption))
        else:
            adoption=max(0,adoption-inputs['adoption_attrition']*adoption)
    total=inputs['opening_requests']+arrivals*inputs['horizon_weeks']
    unresolved=sum(n for _,n in queue)
    assert total==completed+unresolved
    return {'total_requests':total,'completed':completed,'unresolved':unresolved,'completion_fraction':completed/total,'mean_completed_delay_weeks':duration_sum/completed if completed else None,'maximum_unresolved':maximum,'final_adoption':adoption,'weekly':weeks if weekly_records else []}

def screen(inputs,chosen,lookup,scenario,arrivals=None):
    q=run_queue(inputs,chosen,lookup,scenario,arrivals)
    flood=scenario['id']=='flood'
    a=scenario['accessible_capacity']+sum(lookup[k]['accessible_gain']+(lookup[k].get('flood_accessible_gain',0) if flood else 0) for k in chosen)
    s=scenario['standard_capacity']+sum(lookup[k]['standard_gain']+(lookup[k].get('flood_standard_gain',0) if flood else 0) for k in chosen)
    a=min(a,inputs['accessible_demand_four_hours']);s=min(s,inputs['standard_demand_four_hours'])
    ar=a/inputs['accessible_demand_four_hours'];sr=s/inputs['standard_demand_four_hours']
    capacity_pass=ar+1e-10>=inputs['accessible_min_fraction'] and sr+1e-10>=inputs['standard_min_fraction']
    coord_pass=q['completion_fraction']+1e-10>=inputs['coordination_min_completion_fraction']
    return {'scenario':scenario['id'],'probability':scenario['probability'],'accessible_served':a,'standard_served':s,'accessible_fraction':ar,'standard_fraction':sr,'physical_pass':capacity_pass,'coordination_pass':coord_pass,'joint_pass':capacity_pass and coord_pass,**{k:v for k,v in q.items() if k!='weekly'}}

def analyze(inputs,name,chosen,lookup):
    selected=set(chosen)
    cost,fte=portfolio_resources(selected,lookup)
    dependencies=prerequisites_ok(selected,lookup)
    affordable=cost<=inputs['budget_cap_usd_m']+1e-9 and fte<=inputs['workforce_cap_fte']+1e-9
    results=[screen(inputs,selected,lookup,s) for s in inputs['scenarios']]
    coverage=sum(r['probability'] for r in results if r['joint_pass'])
    numeric_eligibility=dependencies and affordable and coverage+1e-9>=inputs['joint_scenario_target_probability']
    return {'name':name,'investments':','.join(sorted(selected)) or '(none)','cost_usd_m':cost,'fte':fte,'dependencies_pass':dependencies,'affordable':affordable,'joint_coverage':round(coverage,8),'all_numeric_gates_pass':numeric_eligibility,'authority_approved':False,'scenario_results':results}

def enumerate_portfolios(inputs,lookup):
    ids=sorted(lookup)
    result=[]
    for size in range(len(ids)+1):
        for subset in itertools.combinations(ids,size):
            if prerequisites_ok(set(subset),lookup):
                result.append(analyze(inputs,'+'.join(subset) if subset else 'empty',list(subset),lookup))
    return result

def csv_write(path,rows,fields):
    with path.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

def build(inputs,write=True):
    lookup=validate(inputs)
    result=[analyze(inputs,n,p,lookup) for n,p in inputs['portfolios'].items()]
    enumeration=enumerate_portfolios(inputs,lookup)
    shock=screen(inputs,set(inputs['portfolios']['capacity_first']),lookup,inputs['scenarios'][0],inputs['stress_weekly_arrivals'])
    summary={'case_id':inputs['case_id'],'synthetic':True,'use':'teaching and bounded screening only','authorization':'HOLD: independent authority, public legitimacy, data and labor agreements not obtained','portfolios':result,'enumerated_dependency_valid_portfolios':len(enumeration),'resource_feasible_portfolios':sum(p['affordable'] for p in enumeration),'threshold_pass_portfolios':sum(p['all_numeric_gates_pass'] for p in enumeration),'best_resource_feasible_coverage':max(p['joint_coverage'] for p in enumeration if p['affordable']),'capacity_first_arrival_stress':shock}
    if write:
        case=BASE/'case';case.mkdir(exist_ok=True)
        fields=['name','investments','cost_usd_m','fte','dependencies_pass','affordable','joint_coverage','all_numeric_gates_pass','authority_approved']
        csv_write(case/'portfolio-screen.csv',result,fields)
        rows=[{'portfolio':p['name'],**r} for p in result for r in p['scenario_results']]
        csv_write(case/'scenario-screen.csv',rows,['portfolio','scenario','probability','accessible_served','standard_served','accessible_fraction','standard_fraction','physical_pass','coordination_pass','joint_pass','total_requests','completed','unresolved','completion_fraction','mean_completed_delay_weeks','maximum_unresolved','final_adoption'])
        csv_write(case/'enumerated-portfolios.csv',enumeration,fields)
        csv_write(case/'weekly-flow.csv',run_queue(inputs,set(inputs['portfolios']['capacity_first']),lookup,inputs['scenarios'][0],weekly_records=True)['weekly'],['week','arrivals','processing_capacity','completed_total','unresolved','adoption'])
        (case/'computed-evidence.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--inputs',type=Path,default=DATA);parser.add_argument('--no-write',action='store_true');args=parser.parse_args()
    summary=build(json.loads(args.inputs.read_text(encoding='utf8')),write=not args.no_write)
    print('NS-ENT19.1 synthetic portfolio analysis')
    for row in summary['portfolios']:
        print(f"{row['name']}: cost=${row['cost_usd_m']:.2f}M FTE={row['fte']} coverage={row['joint_coverage']:.1%} numeric={row['all_numeric_gates_pass']}")
    print('Valid portfolios:',summary['enumerated_dependency_valid_portfolios'],'Affordable:',summary['resource_feasible_portfolios'],'Best coverage:',summary['best_resource_feasible_coverage'])
    print('Capacity-first arrival-stress closure:',round(summary['capacity_first_arrival_stress']['completion_fraction'],4),'HOLD authority')
