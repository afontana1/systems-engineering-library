#!/usr/bin/env python3
"""NS-FB13.1: transparent synthetic stock/flow policy experiments.

Stdlib only. Teaching analog to an SD model; it is NOT a validated Vensim
model, executable .mdl, DEM DES model, or calibrated campus mobility forecast.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
INPUTS = HERE / 'case/model-inputs.json'
FIELDS=['policy','sensitivity','completion_fraction','standard_abandon_fraction',
        'accessible_abandon_fraction','mean_active_vehicles','mean_trust_index',
        'ending_backlog_requests','ending_unavailable_vehicles','surge_vehicle_days',
        'repair_cost_index','max_backlog_requests','conservation_error_requests',
        'fleet_conservation_error_vehicles']

def number(value,label,lo=None,hi=None):
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError(f'{label}: finite numeric value required')
    if lo is not None and value<lo or hi is not None and value>hi:
        raise ValueError(f'{label}: out of allowed range')
    return float(value)

def validate(d):
    if not isinstance(d,dict) or d.get('model_id')!='NS-FB13.1':
        raise ValueError('Unexpected or missing model_id')
    pos=['days','time_step_days','total_vehicles','base_requests_per_day',
         'trips_per_active_vehicle_day','base_breakdown_hazard_per_vehicle_day',
         'repair_time_days','repair_capacity_vehicles_per_day','abandon_time_days',
         'perception_time_days','trust_response_days','surge_backlog_half_saturation']
    for k in pos:number(d.get(k),k,1e-10)
    for k in ('initial_standard_backlog','initial_accessible_backlog','initial_perceived_backlog'):
        number(d.get(k),k,0)
    for k in ('initial_unavailable_vehicles',):number(d.get(k),k,0,d['total_vehicles'])
    number(d.get('initial_trust_index'),'initial_trust_index',0,100)
    number(d.get('accessible_request_fraction'),'accessible_request_fraction',0.01,.5)
    number(d.get('surge_breakdown_stress'),'surge_breakdown_stress',0,8)
    if d['time_step_days']>1 or d['days']>3650:
        raise ValueError('The bounded teaching integrator requires dt <=1 and horizon <=3650 days')
    if abs(d['days']/d['time_step_days']-round(d['days']/d['time_step_days']))>1e-8:
        raise ValueError('time grid must contain an integral number of steps')
    if not isinstance(d.get('scenarios'),list) or len(d['scenarios'])<2:
        raise ValueError('At least two policies required')
    if not isinstance(d.get('sensitivity'),list) or not d['sensitivity']:
        raise ValueError('Sensitivity scenarios required')
    for field,rows in [('scenarios',d['scenarios']),('sensitivity',d['sensitivity'])]:
        ids=[r.get('id') for r in rows if isinstance(r,dict)]
        if len(ids)!=len(rows) or len(set(ids))!=len(ids) or any(not isinstance(i,str) or not i for i in ids):
            raise ValueError('Unique nonblank scenario identifiers required')
    for s in d['scenarios']:
        number(s.get('surge_max_fraction'),'surge_max_fraction',0,.5)
        number(s.get('repair_multiplier'),'repair_multiplier',.2,3)
        number(s.get('accessible_capacity_fraction'),'accessible_capacity_fraction',.05,.5)
    for s in d['sensitivity']:
        number(s.get('demand_multiplier'),'demand_multiplier',.6,1.4)
        number(s.get('failure_multiplier'),'failure_multiplier',.5,2)
    return d

def clamp(x,low,high):return min(high,max(low,x))

def simulate(d,policy,stress,dt=None,trace=False):
    validate(d)
    if policy not in d['scenarios'] or stress not in d['sensitivity']:
        raise ValueError('Undeclared policy or sensitivity')
    dt=d['time_step_days'] if dt is None else number(dt,'dt',0,1)
    nsteps=d['days']/dt
    if abs(nsteps-round(nsteps))>1e-8:raise ValueError('Horizon must be divisible by time step')
    u=d['initial_unavailable_vehicles']
    bs=d['initial_standard_backlog'];ba=d['initial_accessible_backlog']
    p=d['initial_perceived_backlog'];trust=d['initial_trust_index']
    input_initial=bs+ba
    total_arr=total_serv=total_abandon=0.
    arr_s=arr_a=aband_s=aband_a=0.
    fleet_int=trust_int=surge_days=0.
    max_backlog=bs+ba; records=[]
    for i in range(round(nsteps)):
        active=d['total_vehicles']-u
        demand=d['base_requests_per_day']*stress['demand_multiplier']*(.75+.25*trust/70)
        demand=max(0,demand)
        ais=demand*(1-d['accessible_request_fraction']);aia=demand*d['accessible_request_fraction']
        surge=policy['surge_max_fraction']*p/(p+d['surge_backlog_half_saturation'])
        capacity=active*d['trips_per_active_vehicle_day']*(1+surge)
        # Daily-equivalent accessibility reservation: unused reservation is transferable.
        abandoned_a=min(ba/d['abandon_time_days'],ba/dt)
        abandoned_s=min(bs/d['abandon_time_days'],bs/dt)
        # Reservation guarantees accessible demand first access to the declared share.
        # Unused reservation spills to standard work; remaining idle total capacity
        # can serve additional accessible requests above the protected share.
        eligible_a=aia+ba/dt-abandoned_a
        eligible_s=ais+bs/dt-abandoned_s
        served_a=min(capacity*policy['accessible_capacity_fraction'],eligible_a)
        served_s=min(capacity-served_a,eligible_s)
        served_a+=min(capacity-served_a-served_s,eligible_a-served_a)
        # All terms are rates (requests/day); Euler multiplies by dt once.
        next_a=ba+dt*(aia-served_a-abandoned_a)
        next_s=bs+dt*(ais-served_s-abandoned_s)
        if min(next_a,next_s)<-1e-7:raise ArithmeticError('Negative queue indicates flawed integration')
        next_a=max(0,next_a);next_s=max(0,next_s)
        breakdown=min(active/dt,active*d['base_breakdown_hazard_per_vehicle_day']*stress['failure_multiplier']*(1+d['surge_breakdown_stress']*surge))
        repair=min(u/dt, u/d['repair_time_days']*policy['repair_multiplier'], d['repair_capacity_vehicles_per_day']*policy['repair_multiplier'])
        u=u+dt*(breakdown-repair)
        if u<0 or u>d['total_vehicles']+1e-6:raise ArithmeticError('Fleet stock out of bounds')
        u=clamp(u,0,d['total_vehicles'])
        target_trust=clamp(82-.11*(abandoned_a+abandoned_s)-5*surge-0.03*next_a,20,88)
        trust=clamp(trust+dt*(target_trust-trust)/d['trust_response_days'],0,100)
        p=max(0,p+dt*((next_a+next_s)-p)/d['perception_time_days'])
        total_arr+=dt*demand; total_serv+=dt*(served_s+served_a);total_abandon+=dt*(abandoned_s+abandoned_a)
        arr_s+=dt*ais;arr_a+=dt*aia;aband_s+=dt*abandoned_s;aband_a+=dt*abandoned_a
        fleet_int+=dt*active;trust_int+=dt*trust;surge_days+=dt*active*surge
        bs,ba=next_s,next_a
        max_backlog=max(max_backlog,bs+ba)
        if trace and (i+1) % max(1,round(1/dt)) == 0:
            records.append(dict(day=round((i+1)*dt,6),available_vehicles=round(d['total_vehicles']-u,6),
                                standard_backlog=round(bs,6),accessible_backlog=round(ba,6),
                                perceived_backlog=round(p,6),trust_index=round(trust,6),
                                nominal_capacity_per_day=round(capacity,6)))
    res=dict(policy=policy['id'],sensitivity=stress['id'],
         completion_fraction=total_serv/total_arr,
         standard_abandon_fraction=aband_s/arr_s,accessible_abandon_fraction=aband_a/arr_a,
         mean_active_vehicles=fleet_int/d['days'],mean_trust_index=trust_int/d['days'],
         ending_backlog_requests=bs+ba,ending_unavailable_vehicles=u,
         surge_vehicle_days=surge_days,
         repair_cost_index=d['days']*policy['repair_multiplier'],max_backlog_requests=max_backlog,
         conservation_error_requests=input_initial+total_arr-total_serv-total_abandon-bs-ba,
         fleet_conservation_error_vehicles=u+(d['total_vehicles']-u)-d['total_vehicles'])
    return (res,records) if trace else res

def experiments(d):
    validate(d)
    return [simulate(d,p,s) for s in d['sensitivity'] for p in d['scenarios']]

def inventory_transfer(days=35, lead_days=4, position_aware=True):
    """Deterministic units/day supplier example; orders cannot arrive before lead time."""
    if type(days) is not int or not 1<=days<=365 or type(lead_days) is not int or not 1<=lead_days<=30:
        raise ValueError('Invalid inventory horizon or replenishment delay')
    inventory=160.0; backorders=0.0; pipeline=[20.0]*lead_days
    generated=[]; inbound=fulfilled=ordered=0.0
    for day in range(days):
        received=pipeline.pop(0);inbound+=received;inventory+=received
        demand=20.0 if day<7 else 28.0
        need=demand+backorders
        shipped=min(need,inventory);inventory-=shipped
        backorders=need-shipped;fulfilled+=shipped
        target=180.0
        # Position-aware ignores already-on-order? No: on-order supply prevents duplicate orders.
        gap=target-inventory-(sum(pipeline) if position_aware else 0)+backorders
        ordered_today=min(100.0,max(0.0,gap))
        pipeline.append(ordered_today);ordered+=ordered_today
        generated.append(dict(day=day+1,demand=demand,received=received,shipped=shipped,
                              inventory=inventory,backorders=backorders,order=ordered_today,
                              pipeline=sum(pipeline)))
    assert abs(160.0+inbound-fulfilled-inventory)<1e-8
    return generated

def human_service_transfer(days=30, beds=18.0, arrivals_per_day=3.5, stay_days=6.0):
    """Highly simplified throughput model, not clinical prediction or triage advice."""
    if not all(type(x) in (int,float) and math.isfinite(x) and x>0 for x in
               (beds,arrivals_per_day,stay_days)) or type(days) is not int or not 1<=days<=365:
        raise ValueError('Invalid service-flow inputs')
    census=min(beds,15.0);waiting=0.0;arr_total=adm_total=leave_total=0.0
    records=[]
    for day in range(days):
        departure=min(census,census/stay_days)
        capacity=beds-(census-departure)
        admission=min(capacity,arrivals_per_day+waiting)
        census+=admission-departure
        waiting+=arrivals_per_day-admission
        arr_total+=arrivals_per_day;adm_total+=admission;leave_total+=departure
        records.append(dict(day=day+1,census=census,waiting=waiting,departures=departure,
                            admissions=admission))
    assert abs(15+adm_total-leave_total-census)<1e-8
    assert abs(arr_total-adm_total-waiting)<1e-8
    return records

def write(d):
    results=experiments(d)
    path=HERE/'case/experiment-results.csv'
    with path.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,FIELDS);w.writeheader()
        for r in results:w.writerow({k:f'{r[k]:.9f}' if type(r[k]) is float else r[k] for k in FIELDS})
    _,records=simulate(d,d['scenarios'][0],d['sensitivity'][0],trace=True)
    path=HERE/'case/status-quo-daily.csv'
    with path.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,records[0].keys());w.writeheader();w.writerows(records)
    nominal={r['policy']:{k:round(v,6) if isinstance(v,float) else v for k,v in r.items()}
             for r in results if r['sensitivity']=='nominal'}
    out={'model_id':'NS-FB13.1','purpose':'synthetic structural feedback and policy screening',
         'calibrated':False,'policy_results_nominal':nominal,
         'range_by_policy':{p['id']:{metric:[round(min(r[metric] for r in results if r['policy']==p['id']),6),round(max(r[metric] for r in results if r['policy']==p['id']),6)]
             for metric in ('completion_fraction','accessible_abandon_fraction','ending_backlog_requests')}
             for p in d['scenarios']}}
    (HERE/'case/summary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    for name,records in [('inventory-position-aware.csv',inventory_transfer(position_aware=True)),
                         ('inventory-naive.csv',inventory_transfer(position_aware=False)),
                         ('human-service.csv',human_service_transfer())]:
        with (HERE/'case'/name).open('w',encoding='utf8',newline='') as f:
            w=csv.DictWriter(f,records[0].keys());w.writeheader();w.writerows(records)

    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--dt',type=float);p.add_argument('--policy',default='status_quo');p.add_argument('--sensitivity',default='nominal');a=p.parse_args()
    d=validate(json.loads(INPUTS.read_text(encoding='utf8')))
    if a.write:
        print(json.dumps(write(d)['policy_results_nominal'],indent=2))
    else:
        policy=next(x for x in d['scenarios'] if x['id']==a.policy)
        stress=next(x for x in d['sensitivity'] if x['id']==a.sensitivity)
        print(json.dumps(simulate(d,policy,stress,a.dt),indent=2))
