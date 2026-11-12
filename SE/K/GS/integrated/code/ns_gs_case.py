#!/usr/bin/env python3
"""NS-GS4.1 cross-method teaching case. All data synthetic. Python standard library only.
Usage: python3 SE/K/GS/integrated/code/ns_gs_case.py
"""
from __future__ import annotations
import itertools,json,math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'data/ns-gs4.1-case.json'
OUTPUT=ROOT/'outputs/ns-gs4.1-results.json'

def finite_number(x,name):
    if isinstance(x,bool) or not isinstance(x,(float,int)) or not math.isfinite(x):
        raise ValueError(f'{name} must be a finite number')
    return x

def fraction(x,name):
    finite_number(x,name)
    if not 0<=x<=1: raise ValueError(f'{name} outside [0,1]')
    return x

def nonnegative(x,name):
    finite_number(x,name)
    if x<0: raise ValueError(f'{name} negative')
    return x

def earned_value(x):
    p=x['project']
    for k in ('pv_m','ev_m','accepted_ev_m','ac_m','bac_m','etc_m'):nonnegative(p[k],k)
    if min(p['ac_m'],p['pv_m'],p['bac_m'])<=0:raise ValueError('EVM denominators and BAC must be positive')
    if p['accepted_ev_m']>p['ev_m'] or p['ev_m']>p['bac_m']:raise ValueError('earned-value bounds violated')
    return dict(cpi=p['ev_m']/p['ac_m'],spi=p['ev_m']/p['pv_m'],evidence_cpi=p['accepted_ev_m']/p['ac_m'],
                efficiency_eac_m=p['bac_m']*p['ac_m']/p['ev_m'] if p['ev_m']>0 else None,
                bottomup_eac_m=p['ac_m']+p['etc_m'])

def energy_margin(x):
    p=x['energy'];
    for k in ('distance_km','intensity_kwh_per_km','mission_h','aux_kw','battery_kwh','reserve_kwh'):nonnegative(p[k],k)
    fraction(p['soc'],'soc');fraction(p['eta'],'eta')
    consumption=p['distance_km']*p['intensity_kwh_per_km']+p['mission_h']*p['aux_kw']
    usable=p['battery_kwh']*p['soc']*p['eta']-p['reserve_kwh']
    return dict(consumption_kwh=consumption,usable_kwh=usable,margin_kwh=usable-consumption,
                derivative_intensity_km=-p['distance_km'],derivative_distance_kwh_per_km=-p['intensity_kwh_per_km'])

def hybrid(x):
    p=x['hybrid']; E0=p['initial_energy_kwh']; Emin=p['minimum_energy_kwh'];a=p['load_kw']; b=p['load_slope_kw_per_h'];T=p['horizon_h']
    for k in ('initial_energy_kwh','minimum_energy_kwh','load_kw','load_slope_kw_per_h','horizon_h'):nonnegative(p[k],k)
    if Emin>=E0 or a<=0 or T<=0:raise ValueError('invalid hybrid event parameters')
    exact=E0-a*T-b*T*T/2
    if b>0:cross=(-a+math.sqrt(a*a+2*b*(E0-Emin)))/b
    else:cross=(E0-Emin)/a
    rows=[]
    for h in p['steps_h']:
        finite_number(h,'step_h')
        if h<=0 or abs(T/h-round(T/h))>1e-9:raise ValueError('step must divide horizon')
        n=round(T/h); energy=E0
        first_trigger=None
        for i in range(n):
            energy-=(a+b*i*h)*h
            if first_trigger is None and energy<=Emin:first_trigger=(i+1)*h
        rows.append(dict(step_h=h,final_kwh=energy,error_kwh=energy-exact,first_grid_trigger_h=first_trigger))
    return dict(exact_final_kwh=exact,exact_threshold_h=cross,euler=rows)

def delayed_feedback(x):
    p=x['feedback']; results={}
    if isinstance(p['steps'],bool) or not isinstance(p['steps'],int) or not 1<=p['steps']<=10000:raise ValueError('feedback steps must be a positive bounded integer')
    finite_number(p['initial_error'],'initial_error');finite_number(p['previous_error'],'previous_error')
    for field in ('safe_gain','unstable_gain'):
        g=p[field];finite_number(g,field)
        if g<0:raise ValueError('feedback gain negative')
        prev=float(p['previous_error']);curr=float(p['initial_error']);seq=[prev,curr]
        for _ in range(p['steps']):
            next_value=curr-g*prev;prev,curr=curr,next_value;seq.append(curr)
        results[field]=dict(gain=g,series=seq,max_abs=max(map(abs,seq)),last=seq[-1])
    return results

def policy_screen(x):
    sc=x['scenarios']; policies=x['policies']; t=x['thresholds']
    w=[fraction(s['weight'],'weight') for s in sc]
    if not sc or abs(sum(w)-1)>1e-9:raise ValueError('scenario weights must sum to 1')
    for k in ('timely','accessible'):fraction(t[k],k)
    nonnegative(t['budget_m'],'budget_m');nonnegative(t['staff'],'staff')
    if len({s['id'] for s in sc})!=len(sc):raise ValueError('duplicate scenario')
    if len({p['id'] for p in policies})!=len(policies):raise ValueError('duplicate policy id')
    records=[]
    for p in policies:
        nonnegative(p['cost_m'],'cost');nonnegative(p['staff'],'staff')
        if len(p['timely'])!=len(sc) or len(p['accessible'])!=len(sc):raise ValueError('policy length mismatch')
        for field in ('timely','accessible'):
            for v in p[field]:fraction(v,field)
        feasible=p['cost_m']<=t['budget_m'] and p['staff']<=t['staff']
        scenarios_pass=[p['timely'][i]>=t['timely'] and p['accessible'][i]>=t['accessible'] for i in range(len(sc))]
        records.append(dict(id=p['id'],cost_m=p['cost_m'],weighted_timely=sum(a*b for a,b in zip(p['timely'],w)),
            weighted_accessible=sum(a*b for a,b in zip(p['accessible'],w)),
            scenario_pass=dict(zip([s['id'] for s in sc],scenarios_pass)),
            screening_coverage=sum(w[i] for i,v in enumerate(scenarios_pass) if v),resource_feasible=feasible,
            passes_all_scenarios=feasible and all(scenarios_pass)))
    return records

def flow(x):
    p=x['flow'];w=nonnegative(p['admitted_wip'],'wip');engineering=finite_number(p['engineering_rate_per_day'],'engineering_rate');accepted=finite_number(p['accepted_rate_per_day'],'accepted_rate')
    if engineering<=0 or accepted<=0 or accepted>engineering:raise ValueError('invalid flow rates')
    return dict(internal_flow_days=w/engineering,evidence_backed_flow_days=w/accepted,acceptance_ratio=accepted/engineering)

def evidence(x):
    p=x['evidence'];maxage=nonnegative(p['max_age_days'],'max_age_days')
    if not p['requirements']:raise ValueError('cannot approve empty evidence register')
    records=[]; ids=set()
    for r in p['requirements']:
        if r['id'] in ids:raise ValueError('duplicate requirement')
        ids.add(r['id']);age=nonnegative(r['age_days'],'age_days')
        if not isinstance(r['approved'],bool):raise ValueError('approval must be bool')
        reasons=[]
        if r['expected_rev']!=r['artifact_rev']:reasons.append('revision_mismatch')
        if age>maxage:reasons.append('stale')
        if not r['approved']:reasons.append('unapproved')
        records.append(dict(requirement=r['id'],artifact=r['artifact'],actionable=not reasons,reasons=reasons))
    return dict(actionable=sum(r['actionable'] for r in records),total=len(records),records=records)

def difference_in_differences(x):
    p=x['pilot'];
    for k,v in p.items():finite_number(v,k)
    return dict(estimate_min=(p['treated_post_min']-p['treated_pre_min'])-(p['control_post_min']-p['control_pre_min']),
                prerequisite='Only causal if parallel trends, stable outcome definitions and no spillovers hold')

def mission_network(x):
    p=x['network'];
    for k in ('primary_a','primary_b','backup','common_cause'):fraction(p[k],k)
    for k in ('dispatch_slots','constituent_slots','accessible_demand_slots'):nonnegative(p[k],k)
    independent=1-(1-p['primary_a']*p['primary_b'])*(1-p['backup'])
    return dict(independent_availability=independent,common_cause_availability=independent*(1-p['common_cause']),
                available_slots=min(p['dispatch_slots'],p['constituent_slots']),
                accessible_demand_met=min(p['dispatch_slots'],p['constituent_slots'])>=p['accessible_demand_slots'])

def portfolio(x):
    p=x['portfolio'];options=p['options']; budget=nonnegative(p['budget_m'],'budget');staff=nonnegative(p['staff_limit'],'staff')
    if not options:raise ValueError('portfolio options empty')
    ids=[o['id'] for o in options]
    if len(ids)!=len(set(ids)):raise ValueError('duplicate investment ID')
    for o in options:
        for k in ('cost_m','staff','value'):nonnegative(o[k],k)
        for dep in o['requires']:
            if dep not in ids or dep==o['id']:raise ValueError('invalid dependency')
    feasible=[]
    for choice in itertools.product((False,True),repeat=len(options)):
        selected={ids[i] for i,b in enumerate(choice) if b}
        cost=sum(o['cost_m'] for o in options if o['id'] in selected)
        labor=sum(o['staff'] for o in options if o['id'] in selected)
        if cost>budget+1e-9 or labor>staff+1e-9:continue
        if any(not set(o['requires']).issubset(selected) for o in options if o['id'] in selected):continue
        feasible.append(dict(investments=sorted(selected),cost_m=cost,staff=labor,value=sum(o['value'] for o in options if o['id'] in selected)))
    if not feasible:raise ValueError('no feasible portfolio')
    return dict(best=max(feasible,key=lambda row:(row['value'],-row['cost_m'])),feasible_count=len(feasible))

def equity(x):
    p=x['equity'];share=fraction(p['urban_share'],'urban_share')
    for k in ('urban_before_min','urban_after_min','rural_before_min','rural_after_min','maximum_group_harm_min'):nonnegative(p[k],k)
    before=share*p['urban_before_min']+(1-share)*p['rural_before_min']
    after=share*p['urban_after_min']+(1-share)*p['rural_after_min']
    rural_change=p['rural_after_min']-p['rural_before_min']
    return dict(before_min=before,after_min=after,mean_improvement_min=before-after,rural_harm_min=rural_change,
                no_group_harm=rural_change<=p['maximum_group_harm_min'])

def run(x):
    if x.get('id')!='NS-GS4.1':raise ValueError('wrong case identity')
    results={'case_id':x['id'],'cost_and_evidence':earned_value(x),'energy':energy_margin(x),'hybrid':hybrid(x),
             'delayed_feedback':delayed_feedback(x),'policy_screen':policy_screen(x),'flow':flow(x),
             'digital_evidence':evidence(x),'pilot_did':difference_in_differences(x),'mission_network':mission_network(x),
             'portfolio':portfolio(x),'equity':equity(x)}
    approvals=x['authority']
    if set(approvals)!=set(('road_authority','labor','privacy')) or any(not isinstance(v,bool) for v in approvals.values()):raise ValueError('authority flags must contain three named Boolean decisions')
    results['readiness']={'joint_technical_pass':any(p['passes_all_scenarios'] for p in results['policy_screen']),
       'evidence_complete':results['digital_evidence']['actionable']==results['digital_evidence']['total'],
       'authority_complete':all(approvals.values()),'no_group_harm':results['equity']['no_group_harm']}
    results['readiness']['authorize']=all(results['readiness'].values())
    results['readiness']['disposition']='PASS_FOR_REVIEW' if results['readiness']['authorize'] else 'HOLD'
    return results

if __name__=='__main__':
    inputs=json.loads(INPUT.read_text(encoding='utf-8'))
    result=run(inputs)
    OUTPUT.parent.mkdir(exist_ok=True,parents=True)
    OUTPUT.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({'disposition':result['readiness']['disposition'],'weighted_timely':[(p['id'],p['weighted_timely']) for p in result['policy_screen']],
                      'exact_energy':result['hybrid']['exact_final_kwh'],'evidence':result['digital_evidence']['actionable']},indent=2))
