#!/usr/bin/env python3
"""Illustrative Phase 0 calculations. Not validated for safety, finance or contracts.
Run: python phase0_calculators.py
Library calls: weighted_score, cost_estimate, cpm, evm.
"""
from collections import deque


def weighted_score(scores, weights):
    """Scores and weights are parallel numeric sequences; weights sum to one."""
    assert len(scores) == len(weights) > 0
    assert all(w >= 0 for w in weights)
    assert abs(sum(weights) - 1.0) < 1e-9
    return sum(s * w for s, w in zip(scores, weights))


def cost_estimate(hours, loaded_rate, fixed_costs=(), contingency_fraction=0.0):
    """Illustrative subtotal and contingency; does not enforce accounting convention."""
    if min(hours, loaded_rate, contingency_fraction) < 0 or any(c < 0 for c in fixed_costs):
        raise ValueError('Negative values are not valid in this simple teaching model')
    subtotal = hours * loaded_rate + sum(fixed_costs)
    return {'subtotal': subtotal, 'contingency': subtotal * contingency_fraction,
            'planned_total': subtotal * (1+contingency_fraction)}


def cpm(activities):
    """Activity on node CPM. Mapping ID->{duration:int/float,preds:list of IDs}.
    No calendars, lags, time constraints or resource limitations modeled.
    Returns earliest/latest start/finish, float, critical activities, finish.
    """
    ids = list(activities)
    if not ids:
        raise ValueError('Need at least one activity')
    succ = {a: [] for a in ids}
    indegree = {a: len(activities[a]['preds']) for a in ids}
    for a, entry in activities.items():
        if entry['duration'] < 0:
            raise ValueError('Negative duration: '+a)
        for p in entry['preds']:
            if p not in activities:
                raise ValueError('Unknown predecessor '+p+' for '+a)
            succ[p].append(a)
    ready = deque(a for a in ids if indegree[a]==0)
    order = []
    while ready:
        a = ready.popleft()
        order.append(a)
        for s in succ[a]:
            indegree[s]-=1
            if indegree[s]==0:
                ready.append(s)
    if len(order)!=len(ids):
        raise ValueError('Cyclic schedule logic')
    ES,EF,LS,LF={},{},{},{}
    for a in order:
        ES[a] = max((EF[p] for p in activities[a]['preds']), default=0)
        EF[a] = ES[a]+activities[a]['duration']
    finish=max(EF.values())
    for a in reversed(order):
        LF[a] = min((LS[s] for s in succ[a]), default=finish)
        LS[a] = LF[a] - activities[a]['duration']
    return {'finish':finish,'activities':{a:{'ES':ES[a],'EF':EF[a],
        'LS':LS[a],'LF':LF[a],'float':LS[a]-ES[a]} for a in ids},
        'critical':[a for a in order if abs(LS[a]-ES[a])<1e-9]}


def evm(bac, pv, ev, ac):
    """Cumulative EVM, CPI-trend EAC assumption. None when denominator invalid."""
    if min(bac, pv, ev, ac)<0:
        raise ValueError('Negative cumulative totals are not supported')
    cpi=ev/ac if ac else None
    spi=ev/pv if pv else None
    eac=(ac+(bac-ev)/cpi) if cpi and ev<=bac else None
    tcpi=(bac-ev)/(bac-ac) if bac>ac else None
    return {'CV':ev-ac, 'SV':ev-pv, 'CPI':cpi, 'SPI':spi,
            'EAC_CPI':eac, 'VAC':bac-eac if eac is not None else None,
            'TCPI_BAC':tcpi}

if __name__=='__main__':
    net={'A':{'duration':3,'preds':[]},'B':{'duration':5,'preds':['A']},
         'C':{'duration':4,'preds':['A']},'D':{'duration':3,'preds':['B','C']},
         'E':{'duration':2,'preds':['D']}}
    print('Trade A, B:',weighted_score((90,60,70),(.5,.3,.2)),
          weighted_score((70,85,80),(.5,.3,.2)))
    print('Cost:',cost_estimate(160,130,(18000,2500,6000),.10))
    print('CPM:',cpm(net))
    print('EVM:',evm(500000,250000,200000,240000))
