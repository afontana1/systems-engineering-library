#!/usr/bin/env python3
"""Northstar NS-QA10.1 quantitative case. Synthetic data; standard library only.

Computations are pedagogic. Normal tails and exponential life assumptions are
conditional models, NOT empirical certification of service-level requirements.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path
from statistics import mean, NormalDist

BASE=Path(__file__).resolve().parents[1]
CASE=BASE/'case'


def rows(filename):
    with (CASE/filename).open(newline='',encoding='utf8') as handle:
        return list(csv.DictReader(handle))


def factorial(records):
    cells={}
    for r in records:
        key=(r['environment'],r['controller'])
        if key not in {('mild','baseline'),('mild','optimized'),('cold','baseline'),('cold','optimized')}:
            raise ValueError('Unknown factorial treatment: '+str(key))
        value=float(r['latency_ms'])
        if not math.isfinite(value) or value<=0:
            raise ValueError('Invalid latency')
        cells.setdefault(key,[]).append(value)
    if len(cells)!=4 or any(len(v)<2 for v in cells.values()):
        raise ValueError('Need 4 cells with at least 2 observations each')
    if len({len(v) for v in cells.values()})!=1:
        raise ValueError('Balanced factorial example requires equal replication')
    means={f'{k[0]}:{k[1]}':mean(v) for k,v in cells.items()}
    mild=means['mild:optimized']-means['mild:baseline']
    cold=means['cold:optimized']-means['cold:baseline']
    interaction=cold-mild
    n=len(cells['mild','baseline'])
    df=4*(n-1)
    mse=sum(sum((y-mean(v))**2 for y in v) for v in cells.values())/df
    se=math.sqrt(4*mse/n)
    # critical value for df=20 only in the controlled teaching dataset
    ci=None if df!=20 else [interaction-2.085963*se,interaction+2.085963*se]
    return {'means_ms':means,'mild_controller_effect_ms':mild,
            'cold_controller_effect_ms':cold,'interaction_ms':interaction,
            'df_residual':df,'mse_ms2':mse,'se_interaction_ms':se,
            't_interval_95_interaction_ms':ci,'n_per_cell':n}


def reliability(records,mission_hours=50.0):
    if mission_hours<=0:raise ValueError('Mission time must be positive')
    observed=0;exposure=0.
    for r in records:
        hours=float(r['exposure_hours'])
        if not math.isfinite(hours) or hours<=0:raise ValueError('Invalid exposure')
        if r['outcome'] not in ('failure','right_censored'):raise ValueError('Invalid event type')
        observed+=int(r['outcome']=='failure');exposure+=hours
    if observed==0:raise ValueError('Zero-failure life test needs a bound, not 0 hazard MLE')
    rate=observed/exposure
    return {'failures':observed,'assets':len(records),'exposure_hours':exposure,
            'hazard_per_hour':rate,'mission_hours':mission_hours,
            'mission_reliability_exponential':math.exp(-rate*mission_hours)}


def correlated_energy(mu=25., sd_distance_km=4., sd_heating_h=1.5,
                      coeff_distance=.4,coeff_heating=.8,rho=.6,limit=29.):
    if not (-1<=rho<=1):raise ValueError('Invalid correlation')
    if sd_distance_km<0 or sd_heating_h<0:raise ValueError('Negative standard deviation')
    var=(coeff_distance*sd_distance_km)**2+(coeff_heating*sd_heating_h)**2+2*rho*coeff_distance*sd_distance_km*coeff_heating*sd_heating_h
    if var<0:raise ValueError('Invalid covariance')
    std=math.sqrt(var)
    p95=mu+NormalDist().inv_cdf(.95)*std
    exceedance=1-NormalDist(mu,std).cdf(limit) if std>0 else float(mu>limit)
    return {'mean_kwh':mu,'variance_kwh2':var,'sd_kwh':std,'p95_normal_kwh':p95,
            'limit_kwh':limit,'p_exceed_model':exceedance,'correlation':rho}


def lifecycle_trade(p=.2):
    if not 0<=p<=1:raise ValueError('Invalid disruption probability')
    a=(1-p)*50+p*140
    b=(1-p)*75+p*90
    return {'p_disruption':p,'A_expected_kusd':a,'B_expected_kusd':b,
            'switch_threshold':1/3,'preferred_expected': 'A' if a<b else ('B' if b<a else 'tie')}


def evidence_audit(records,baseline='QA-B10',valid_requirements=None):
    issue=[];seen=set()
    for r in records:
        if r['evidence_id'] in seen:raise ValueError('Duplicate evidence ID')
        seen.add(r['evidence_id'])
        if r['status'] not in ('executed','planned'):
            raise ValueError('Unrecognized evidence status')
        if r['status']!='executed':issue.append(f"{r['evidence_id']}: planned—not test evidence")
        if r['configuration']!=baseline:issue.append(f"{r['evidence_id']}: stale configuration")
        if valid_requirements is not None and r['requirement_id'] not in valid_requirements:
            issue.append(f"{r['evidence_id']}: orphan requirement reference")
    return issue


def compute():
    settings=json.loads((CASE/'model-assumptions.json').read_text(encoding='utf8'))
    req=rows('requirements.csv')
    if settings['baseline']!='QA-B10' or settings['model_id']!='NS-QA10.1':
        raise ValueError('Model baseline mismatch')
    expected={f'QA-{i:02d}' for i in range(1,6)}
    if {r['requirement_id'] for r in req}!=expected or len(req)!=len(expected):
        raise ValueError('Requirement identifiers not unique and complete')
    exp_rows=rows('factorial-trials.csv')
    if any(x['baseline']!=settings['baseline'] for x in exp_rows):
        raise ValueError('Factorial data from mismatched baseline')
    if len({x['trial_id'] for x in exp_rows})!=len(exp_rows):
        raise ValueError('Duplicate trial ID')
    life=rows('reliability-life.csv')
    if any(x['baseline']!=settings['baseline'] for x in life):
        raise ValueError('Life data from mismatched baseline')
    f=factorial(exp_rows)
    r=reliability(life,settings['mission_hours'])
    energy=settings['correlated_energy']
    kw={'mu':energy['mean_kwh'], 'sd_distance_km':energy['sd_route_distance_km'],
        'sd_heating_h':energy['sd_heating_hours'],
        'coeff_distance':energy['energy_per_route_km'],
        'coeff_heating':energy['energy_per_heating_hour'],
        'rho':energy['rho'], 'limit':settings['shift_energy_p95_limit_kwh']}
    e=correlated_energy(**kw)
    independent=correlated_energy(**{**kw,'rho':0.})
    t=lifecycle_trade()
    issues=evidence_audit(rows('evidence-register.csv'),settings['baseline'],expected)
    return {'factorial':f,'reliability':r,'energy_correlated':e,
            'energy_independent':independent,'trade':t,'evidence_issues':issues,
            'decision':'HOLD: energy tail and reliability models fail provisional screens; evidence remains incomplete'}


if __name__=='__main__':
    print(json.dumps(compute(),indent=2))
