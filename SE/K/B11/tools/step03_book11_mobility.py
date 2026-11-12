#!/usr/bin/env python3
"""NS-MS11.1 synthetic campus mobility discrete-event demonstration; Python stdlib.

Does not simulate ridesharing, drivers, network travel, field validation, or safety.
The authoring scripts use seed-controlled common exogenous requests across alternatives.
"""
from __future__ import annotations
import csv
import heapq
import json
import math
import random
from pathlib import Path
from statistics import mean, stdev

BASE=Path(__file__).resolve().parents[1]
CASE=BASE/'case'

def load():
    d=json.loads((CASE/'model-assumptions.json').read_text(encoding='utf8'))
    validate(d)
    return d

def validate(d):
    required=('schedule','day_minutes','accessible_share','chargers','battery_trigger_fraction','accessible_fraction_of_fleet','base_travel_triangular_min','trip_energy_fraction_range')
    if not all(k in d for k in required):raise ValueError('missing configuration field')
    if not (0<=d['accessible_share']<=1 and 0<d['accessible_fraction_of_fleet']<=1 and 0<d['battery_trigger_fraction']<1):raise ValueError('invalid proportions')
    if not isinstance(d['chargers'],int) or d['chargers']<1:raise ValueError('chargers must be positive integer')
    if d['day_minutes']!=720:raise ValueError('declared horizon must be 720 minutes')
    before=0
    for part in d['schedule']:
        if part['start_min']!=before or part['end_min']<=before or part['rate_per_hour']<0:raise ValueError('noncontiguous schedule, invalid rate')
        before=part['end_min']
    if before!=d['day_minutes']:raise ValueError('schedule does not cover day')
    for key in ('base_travel_triangular_min','charging_triangular_min','standard_board_triangular_min'):
        lo,mode,hi=d[key]
        if not 0<lo<=mode<=hi:raise ValueError('triangular parameters invalid')
    lo,hi=d['trip_energy_fraction_range']
    if not 0<lo<=hi<1:raise ValueError('invalid energy range')
    if not (d['accessible_board_lognormal_median_min']>0 and d['accessible_board_lognormal_p90_min']>d['accessible_board_lognormal_median_min']):raise ValueError('invalid accessible boarding parameters')
    if not d['vehicle_candidates'] or len(set(d['vehicle_candidates']))!=len(d['vehicle_candidates']) or any(not isinstance(x,int) or x<1 for x in d['vehicle_candidates']):raise ValueError('invalid fleet candidates')
    return True

def nearest_rank(values,p):
    if not values or not 0<=p<=1:raise ValueError('nonempty data and p in [0,1] required')
    return sorted(values)[max(0,math.ceil(len(values)*p)-1)]

def generate_requests(d,seed,stress=False):
    """Independent nonhomogeneous Poisson increments, common across fleet alternatives."""
    rng=random.Random(seed)
    demand=1.2 if stress else 1.0
    sigma=math.log(d['accessible_board_lognormal_p90_min']/d['accessible_board_lognormal_median_min'])/1.2815515655446004
    requests=[]
    for segment in d['schedule']:
        current=float(segment['start_min']);rate=segment['rate_per_hour']*demand/60
        if not rate:continue
        while True:
            current+=rng.expovariate(rate)
            if current>=segment['end_min']:break
            accessible=rng.random()<d['accessible_share']
            board=(rng.lognormvariate(math.log(d['accessible_board_lognormal_median_min']),sigma)
                   if accessible else rng.triangular(d['standard_board_triangular_min'][0],d['standard_board_triangular_min'][2],d['standard_board_triangular_min'][1]))
            travel=rng.triangular(d['base_travel_triangular_min'][0],d['base_travel_triangular_min'][2],d['base_travel_triangular_min'][1])*(1.3 if stress else 1.0)
            energy=rng.uniform(*d['trip_energy_fraction_range'])
            requests.append(dict(id=len(requests)+1,time=current,accessible=accessible,boarding=board,travel=travel,energy=energy))
    return requests

def simulate(d,requests,fleet,seed=0,trace=False):
    if not isinstance(fleet,int) or fleet<1:raise ValueError('invalid fleet')
    if not isinstance(requests,list):raise TypeError('requests must be list')
    if any(x['time']<0 or x['time']>=d['day_minutes'] or x['boarding']<0 or x['travel']<=0 or not 0<x['energy']<1 or not isinstance(x['accessible'],bool) for x in requests):raise ValueError('invalid request')
    if any(requests[i]['time']>requests[i+1]['time'] for i in range(len(requests)-1)):raise ValueError('requests must be time sorted')
    rng=random.Random(seed+500000)
    accessible_count=math.ceil(fleet*d['accessible_fraction_of_fleet'])
    vehicles=[{'id':i,'accessible':i<accessible_count,'soc':1.,'state':'idle'} for i in range(fleet)]
    events=[];serial=0
    def push(t,typ,detail):
        nonlocal serial
        serial+=1;heapq.heappush(events,(t,serial,typ,detail))
    for r in requests:push(r['time'],'arrival',r)
    waiting=[];charge_queue=[];charging=0;waits=[];standard_waits=[];acc_waits=[];completed=0;started=0
    busy_minutes=0.;charge_minutes=0.;max_queue=0; event_trace=[];count_by_close=None
    def log(t,event,identifier):
        if trace:event_trace.append((round(t,4),event,identifier))
    def dispatch(t):
        nonlocal started,busy_minutes,charging,charge_minutes
        while True:
            choice=None
            for pos,r in enumerate(waiting):
                vid=next((v['id'] for v in vehicles if v['state']=='idle' and (not r['accessible'] or v['accessible'])),None)
                if vid is not None:choice=(pos,vid);break
            if choice is None:break
            pos,vid=choice;r=waiting.pop(pos);v=vehicles[vid]
            assert v['state']=='idle'
            wait=t-r['time'];waits.append(wait)
            if r['accessible']:acc_waits.append(wait)
            else:standard_waits.append(wait)
            duration=r['boarding']+r['travel'];v['state']='trip';v['soc']-=r['energy'];busy_minutes+=max(0.,min(t+duration,d['day_minutes'])-t)
            if v['soc']<0:raise ValueError('battery capacity violated; revise energy/charging rule')
            push(t+duration,'trip_done',vid);started+=1;log(t,'pickup',r['id'])
    for_tick=0
    while events:
        t,_,typ,detail=heapq.heappop(events)
        if count_by_close is None and t>=d['day_minutes']:
            count_by_close=len(waiting)
        if typ=='arrival':waiting.append(detail);log(t,'arrival',detail['id'])
        elif typ=='trip_done':
            v=vehicles[detail];assert v['state']=='trip';completed+=1
            if v['soc']<d['battery_trigger_fraction']:
                v['state']='charge_queue';charge_queue.append(v['id']);log(t,'charge_queued',v['id'])
            else:v['state']='idle'
        elif typ=='charge_done':
            v=vehicles[detail];assert v['state']=='charging'
            charging-=1;v['soc']=1.;v['state']='idle';log(t,'charge_done',detail)
        while charge_queue and charging<d['chargers']:
            vid=charge_queue.pop(0);v=vehicles[vid];assert v['state']=='charge_queue'
            v['state']='charging';charging+=1
            dt=rng.triangular(d['charging_triangular_min'][0],d['charging_triangular_min'][2],d['charging_triangular_min'][1])
            charge_minutes+=max(0.,min(t+dt,d['day_minutes'])-t);push(t+dt,'charge_done',vid);log(t,'charge_start',vid)
        dispatch(t)
        max_queue=max(max_queue,len(waiting))
        if charging>d['chargers'] or any(v['soc']<0 or v['soc']>1 for v in vehicles):raise AssertionError('resource invariant')
        for_tick+=1
        if for_tick>1000000:raise RuntimeError('event upper bound hit')
    if count_by_close is None:count_by_close=len(waiting)
    if len(waits)!=len(requests) or completed!=started or waiting or charge_queue or charging:
        raise AssertionError('flow conservation failed')
    n=len(requests)
    return {'fleet':fleet,'requests':n,'accessible_requests':sum(x['accessible'] for x in requests),
      'p90_wait_min':nearest_rank(standard_waits,.9) if standard_waits else None,
      'p90_accessible_wait_min':nearest_rank(acc_waits,.9) if acc_waits else None,
      'mean_wait_min':mean(waits) if waits else 0.,
      'not_picked_up_by_close':count_by_close,
      'fraction_not_picked_up_by_close':count_by_close/n if n else 0.,
      'fleet_trip_busy_fraction':busy_minutes/(fleet*d['day_minutes']),
      'charger_busy_fraction':charge_minutes/(d['chargers']*d['day_minutes']),
      'max_wait_queue':max_queue,'trace':event_trace if trace else None}

def summary(xs):
    if not xs:raise ValueError('replications required')
    n=len(xs);mu=mean(xs);s=stdev(xs) if n>1 else 0.
    # 30-replication demonstration: t_(0.975,29) = 2.045230; other n uses large-sample approximation.
    critical=2.045230 if n==30 else 1.96
    margin=critical*s/math.sqrt(n)
    return {'mean':mu,'sample_sd':s,'mean_ci95':[mu-margin,mu+margin],'n':n}

def experiment(d=None,stress=False,n=30,seeds=None):
    d=d or load()
    if not isinstance(n,int) or n<2:raise ValueError('n >= 2 required')
    if seeds is None:seeds=list(range(1000,1000+n))
    if len(seeds)!=n or len(set(seeds))!=n:raise ValueError('distinct seeds required')
    records=[]
    for seed in seeds:
        requests=generate_requests(d,seed,stress=stress)
        for fleet in d['vehicle_candidates']:
            result=simulate(d,requests,fleet,seed=seed)
            result.update(seed=seed,scenario='stress' if stress else 'baseline')
            records.append(result)
    return records

def report(records):
    out={}
    for fleet in sorted({r['fleet'] for r in records}):
        rows=[r for r in records if r['fleet']==fleet]
        out[fleet]={name:summary([r[name] for r in rows if r[name] is not None]) for name in ('p90_wait_min','p90_accessible_wait_min','fraction_not_picked_up_by_close','mean_wait_min','fleet_trip_busy_fraction','charger_busy_fraction')}
        out[fleet]['zero_accessible_days']=sum(r['p90_accessible_wait_min'] is None for r in rows)
    return out

def export():
    d=load();baseline=experiment(d);stress=experiment(d,stress=True)
    cols=('scenario','seed','fleet','requests','accessible_requests','p90_wait_min','p90_accessible_wait_min','mean_wait_min','not_picked_up_by_close','fraction_not_picked_up_by_close','fleet_trip_busy_fraction','charger_busy_fraction','max_wait_queue')
    with (CASE/'replication-output.csv').open('w',newline='',encoding='utf8') as f:
        writer=csv.DictWriter(f,fieldnames=cols);writer.writeheader();writer.writerows({k:r.get(k) for k in cols} for r in baseline+stress)
    with (CASE/'summary.json').open('w',encoding='utf8') as f:json.dump({'baseline':report(baseline),'stress':report(stress)},f,indent=2)
    return {'baseline':report(baseline),'stress':report(stress)}

if __name__=='__main__':
    out=export()
    for scenario,items in out.items():
        print(scenario)
        for k,v in items.items():
            print(k,'standard p90 daily mean',round(v['p90_wait_min']['mean'],2),
                 'accessible p90 daily mean',round(v['p90_accessible_wait_min']['mean'],2),
                 'mean nonpickup fraction',round(v['fraction_not_picked_up_by_close']['mean'],4))
    print('All records and assumptions synthetic; not pilot qualification.')
