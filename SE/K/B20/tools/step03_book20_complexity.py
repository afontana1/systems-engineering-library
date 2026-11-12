#!/usr/bin/env python3
"""NS-CPLX20.1: transparent constructed 26-window policy thought experiment.

It can screen numerical capacity and record exclusion, but cannot confer legitimacy,
identify causal effects, validate interviews, certify legal authority or approve pilots.
Python standard library only. All input values are hypothetical.
"""
from __future__ import annotations
import csv
import json
import math
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
DATA=BASE/'case'

def validate(d):
    if not isinstance(d,dict) or d.get('case_id')!='NS-CPLX20.1':raise ValueError('Case identifier missing')
    intfields=['observation_weeks','base_accessible_requests','base_standard_requests','stop_consecutive_weeks']
    for key in intfields:
        if type(d.get(key)) is not int or d[key]<1:raise ValueError('Invalid integer '+key)
    if d['observation_weeks']>500:raise ValueError('Unbounded horizon')
    for key in ['initial_trust_proxy','abandonment_fraction','adaptation_demand_sensitivity','trust_gain','trust_loss_from_unmet','illustrative_service_floor','stop_floor']:
        x=d.get(key)
        if type(x) not in (int,float) or not math.isfinite(x) or not 0<=x<=1:raise ValueError('Invalid probability-like parameter '+key)
    if d['stop_floor']>d['illustrative_service_floor']:raise ValueError('Stop threshold above normal screen')
    for key in ['policies','scenarios','approval_evidence']:
        if not isinstance(d.get(key),dict if key!='scenarios' else list) or not d[key]:raise ValueError('Empty '+key)
    if len(set(d['policies']))!=len(d['policies']):raise ValueError('Duplicate policy')
    for policy,p in d['policies'].items():
        for key in ('accessible_capacity','standard_capacity','additional_cost_m'):
            v=p.get(key)
            if type(v) not in (int,float) or not math.isfinite(v) or v<0:raise ValueError('Invalid '+policy+':'+key)
    ids=[];weight=0
    for s in d['scenarios']:
        name=s.get('id')
        if not isinstance(name,str) or not name or name in ids:raise ValueError('Duplicate/empty scenario')
        ids.append(name)
        for key in ('weight','accessible_supply_factor','standard_supply_factor','accessible_demand_factor','standard_demand_factor'):
            v=s.get(key)
            if type(v) not in (int,float) or not math.isfinite(v) or v<0:raise ValueError('Invalid scenario '+key)
        if s['weight']>1 or s['accessible_supply_factor']>2 or s['standard_supply_factor']>2 or s['accessible_demand_factor']>2 or s['standard_demand_factor']>2:raise ValueError('Implausible controlled scenario')
        weight+=s['weight']
    if not math.isclose(weight,1,abs_tol=1e-10):raise ValueError('Scenario weights do not sum to 1')
    if set(d['approval_evidence'])!={'affected_group_consent','independent_safety_review','labor_agreement','privacy_authority','sponsor_authorization'} or any(type(v)!=bool for v in d['approval_evidence'].values()):raise ValueError('Authorization evidence malformed')
    return d

def simulate(d, policy_id, scenario_id, *, weekly=False):
    validate(d)
    if policy_id not in d['policies']:raise ValueError('Unknown policy')
    matches=[s for s in d['scenarios'] if s['id']==scenario_id]
    if len(matches)!=1:raise ValueError('Unknown scenario')
    p=d['policies'][policy_id];s=matches[0]
    trust=d['initial_trust_proxy']
    backlog={'accessible':0,'standard':0}
    generated={'accessible':0,'standard':0}
    served={'accessible':0,'standard':0}
    abandoned={'accessible':0,'standard':0}
    stop_run=0;first_stop=None;history=[]
    for week in range(1,d['observation_weeks']+1):
        demand_factor=1+d['adaptation_demand_sensitivity']*(trust-0.5)
        arrivals={'accessible':round(d['base_accessible_requests']*s['accessible_demand_factor']*demand_factor),
                  'standard':round(d['base_standard_requests']*s['standard_demand_factor']*demand_factor)}
        capacity={'accessible':math.floor(p['accessible_capacity']*s['accessible_supply_factor']),
                  'standard':math.floor(p['standard_capacity']*s['standard_supply_factor'])}
        observed={}
        for group in ('accessible','standard'):
            generated[group]+=arrivals[group]
            available=backlog[group]+arrivals[group]
            complete=min(available,capacity[group])
            remainder=available-complete
            # Abandonment is explicitly counted, never erased from the stock balance.
            drop=math.floor(remainder*d['abandonment_fraction'])
            backlog[group]=remainder-drop
            served[group]+=complete
            abandoned[group]+=drop
            observed[group]={'arrivals':arrivals[group],'capacity':capacity[group],'served':complete,'abandoned':drop,'backlog':backlog[group],
                             'window_service_fraction':complete/available if available else 1}
            if generated[group]!=served[group]+abandoned[group]+backlog[group]:raise AssertionError('Conservation defect')
        # Trust is a *constructed demand-response proxy*, not legitimacy or survey evidence.
        a=observed['accessible'];t=observed['standard']
        unmet_access=(a['abandoned']+a['backlog'])/max(1,generated['accessible'])
        trust=min(1,max(0,trust+d['trust_gain']*(a['window_service_fraction']-0.9)-d['trust_loss_from_unmet']*unmet_access))
        if a['window_service_fraction']<d['stop_floor']:
            stop_run+=1
            if stop_run>=d['stop_consecutive_weeks'] and first_stop is None:first_stop=week
        else:stop_run=0
        history.append({'week':week,'policy':policy_id,'scenario':scenario_id,'trust_proxy':round(trust,8),
                        **{f'{group}_{k}':v for group,row in observed.items() for k,v in row.items()}})
    result={'policy':policy_id,'scenario':scenario_id,'weight':s['weight'],'accessible_generated':generated['accessible'],
        'accessible_served':served['accessible'],'accessible_abandoned':abandoned['accessible'],'accessible_backlog':backlog['accessible'],
        'standard_generated':generated['standard'],'standard_served':served['standard'],'standard_abandoned':abandoned['standard'],'standard_backlog':backlog['standard'],
        'accessible_fraction':served['accessible']/generated['accessible'],'standard_fraction':served['standard']/generated['standard'],
        'final_trust_proxy':trust,'stop_trigger_week':first_stop,
        'numerical_screen_pass':served['accessible']/generated['accessible']>=d['illustrative_service_floor'] and served['standard']/generated['standard']>=d['illustrative_service_floor'] and first_stop is None,
        'authorized':all(d['approval_evidence'].values())}
    return (result,history) if weekly else result

def build(d,write=False):
    validate(d)
    results=[simulate(d,p,s['id']) for p in d['policies'] for s in d['scenarios']]
    summary=[]
    for policy in d['policies']:
        subset=[r for r in results if r['policy']==policy]
        coverage=sum(r['weight'] for r in subset if r['numerical_screen_pass'])
        summary.append({'policy':policy,'additional_cost_m':d['policies'][policy]['additional_cost_m'],
                        'hypothetical_weighted_screen_coverage':round(coverage,8),
                        'status':'HOLD — approvals absent' if not all(d['approval_evidence'].values()) else 'Await independent field qualification',
                        'nominal_accessible_fraction':next(r['accessible_fraction'] for r in subset if r['scenario']=='nominal'),
                        'nominal_standard_fraction':next(r['standard_fraction'] for r in subset if r['scenario']=='nominal')})
    output={'case_id':d['case_id'],'observations':results,'policy_screen':summary,
            'limit':'Constructed scenario weights, trust proxy and screening limits. Not observed or causally validated. Authorization false.'}
    if write:
        (DATA/'computed-evidence.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
        for name,rows in [('scenario-results.csv',results),('policy-screen.csv',summary)]:
            with (DATA/name).open('w',newline='',encoding='utf8') as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        for policy in d['policies']:
            res,rows=simulate(d,policy,'nominal',weekly=True)
            with (DATA/f'weekly-{policy}.csv').open('w',newline='',encoding='utf8') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    return output

if __name__=='__main__':
    d=json.loads((DATA/'controlled-inputs.json').read_text(encoding='utf8'))
    for row in build(d,write=True)['policy_screen']:print(row)
