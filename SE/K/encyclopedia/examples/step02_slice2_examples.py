#!/usr/bin/env python3
"""Reproducible, synthetic Step-02 slice-2 calculations (Python stdlib only).

This program checks mathematical examples; it cannot validate physical models or
assert language/standards conformance. Usage: python3 step02_slice2_examples.py
"""
from __future__ import annotations
from itertools import product
from math import ceil, exp, log
import json


def portfolio():
    options={'A':(4,7),'B':(3,5),'C':(5,9)}
    scenarios={}
    for dependency in (False,True):
        feasible=[]
        for bits in product((0,1),repeat=3):
            chosen={name for name,on in zip(options,bits) if on}
            cost=sum(options[k][0] for k in chosen)
            if cost>8 or (dependency and 'C' in chosen and 'A' not in chosen):continue
            feasible.append({'chosen':sorted(chosen),'cost':cost,'value':sum(options[k][1] for k in chosen)})
        best=max(feasible,key=lambda d:(d['value'],-d['cost']))
        scenarios['requires_A' if dependency else 'independent']=best
    return scenarios


def motor_point():
    current=4.0;speed=20.0;resistance=2.0;emf=0.1;torque=0.1;drag=0.01;load=0.2;thermal=4.0
    return {'voltage_V':round(resistance*current+emf*speed,6),
            'torque_balance_Nm':round(torque*current-drag*speed-load,6),
            'temperature_rise_K':round(current*current*resistance/thermal,6),
            'rise_at_5A_K':round(25*resistance/thermal,6)}


def service_availability():
    a=.9995**3
    return {'journey_availability':a,'30_day_equivalent_unavailable_minutes':43200*(1-a),
            'target_99_9_downtime_minutes':43200*(1-.999)}


def support():
    factor=(1-1.04**(-6))/.04
    annual=18000
    tail=1-exp(-2)*sum(2**k/__import__('math').factorial(k) for k in range(4))
    return {'maintenance_savings_PV_USD':annual*factor,'net_savings_USD':annual*factor-70000,
            'lead_time_stockout_probability':tail,'inherent_A_4hr':200/204,'inherent_A_8hr':200/208}


def operational_trials():
    n=ceil(log(.05)/log(.995))
    return {'min_zero_failure_trials':n,'bound_at_300':1-.05**(1/300),'bound_at_600':1-.05**(1/600)}


def pilot():
    return {'diff_in_diff_minutes':(24-30)-(28-29),'revised_control_diff_in_diff':(24-30)-(25-29)}


def morphology():
    cases=list(product(('camera','lidar'),('onboard','edge','central'),('standard','extended')))
    allowed=[c for c in cases if not (c[0]=='camera' and c[1]=='central')]
    return {'total':len(cases),'allowed':len(allowed),'with_binary_monitor_total':len(cases)*2,'with_binary_monitor_allowed':len(allowed)*2}


def run():
    return {'portfolio':portfolio(),'motor':motor_point(),'service':service_availability(),
            'support':support(),'operational':operational_trials(),'pilot':pilot(),
            'morphology':morphology(),'decision_queue_6week_growth':(6-5)*6,
            'stale_distance_m':2*(.05+.08)}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
