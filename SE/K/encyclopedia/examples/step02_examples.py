#!/usr/bin/env python3
"""Reproduce selected Step 02 concept-backbone calculations.

All input values and scenarios are synthetic teaching assumptions; the program
is not a production engineering solver or certification-quality analysis.
Usage: python3 step02_examples.py [--case all|parametric|variants|queries|surrogate|fusion|risk|backlog]
"""
from __future__ import annotations
import argparse, itertools, json, math


def parametric():
    force_newton, speed_ms, efficiency, minutes = 1200, 2.0, 0.80, 10
    electrical_kw = force_newton * speed_ms / efficiency / 1000
    return {'mechanical_kw':force_newton*speed_ms/1000,
            'electrical_kw':electrical_kw,'energy_kwh':electrical_kw*minutes/60,
            'nominal_margin_kw':3.2-electrical_kw,
            'electrical_kw_at_70pct_efficiency':force_newton*speed_ms/.70/1000}


def variants():
    candidates=list(itertools.product(('central','distributed'),('standard','extended'),('primary','independent')))
    allowed=[dict(dispatch=d,battery=b,monitor=m) for d,b,m in candidates if not(d=='distributed' and m=='primary')]
    return {'all_combinations':len(candidates),'allowed_combinations':len(allowed),'allowed':allowed}


def queries():
    requirements={'r1','r2','r3','r4'}
    components={'dispatcher','brake'}
    allocations={('r1','dispatcher'),('r2','dispatcher'),('r3','brake')}
    allocated={a for a,b in allocations if b in components}
    missing=sorted(requirements-allocated)
    malformed=allocations|{('r5','dispatcher')}
    dangling=sorted({a for a,b in malformed if a not in requirements or b not in components})
    return {'covered':len(allocated),'total':len(requirements),'missing_allocation':missing,'dangling_requirement_reference':dangling}


def surrogate():
    fhat=lambda x:(x-2)**2+4
    f=lambda x:fhat(x)+.05*x*(x-2)*(x-4)
    return {str(x):{'predicted':fhat(x),'reference':f(x),'signed_error':fhat(x)-f(x)} for x in (0,2,3,4,6)}


def fusion():
    x1,u1,x2,u2=10,2,14,1
    w1,w2=1/u1**2,1/u2**2
    return {'estimate':(x1*w1+x2*w2)/(w1+w2),'standard_uncertainty':math.sqrt(1/(w1+w2))}


def risk():
    alpha=.05
    return {'upper_frequentist_n30':1-alpha**(1/30),
            'minimum_zero_failure_trials_for_1pct_bound':math.ceil(math.log(alpha)/math.log(.99)),
            'upper_bayesian_beta1_31':1-alpha**(1/31)}


def backlog():
    def project(arrivals, capacity, initial=30, hours=4):
        b=initial; values=[b]
        for _ in range(hours):
            b=max(0,b+arrivals-min(capacity,b+arrivals))
            values.append(b)
        return values
    return {'arrivals10_capacity12':project(10,12), 'arrivals13_capacity12':project(13,12), 'ideal_clearance_hours':15}


CASES={'parametric':parametric,'variants':variants,'queries':queries,'surrogate':surrogate,'fusion':fusion,'risk':risk,'backlog':backlog}

def run(case='all'):
    result={name:func() for name,func in CASES.items() if case in ('all',name)}
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',choices=['all',*CASES],default='all')
    args=parser.parse_args()
    print(json.dumps(run(args.case),indent=2,sort_keys=True))
