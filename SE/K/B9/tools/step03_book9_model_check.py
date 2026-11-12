#!/usr/bin/env python3
"""Book 9: transparent, synthetic model analytics and traceability checks.

No external dependencies. This is NOT a SysML/KerML parser or field qualification.
"""
from __future__ import annotations
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'case'

def source(name):
    return (ROOT/name).read_text(encoding='utf8')

def data(name):
    return json.loads(source(name))

def rows(name):
    with (ROOT/name).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f))

def screen(v,charger_kw=None,efficiency=None,chargers=None):
    """Deterministic capacity and energy screen, not a stochastic SLA estimate."""
    n=int(v['vehicles']);cycle=float(v['cycle_minutes']); demand=float(v['energy_per_vehicle_kwh']) * n
    power=float(v['charger_power_kw'] if charger_kw is None else charger_kw)
    eta=float(v['efficiency'] if efficiency is None else efficiency)
    c=int(v['chargers'] if chargers is None else chargers)
    window=float(v['charging_window_h'])
    if n<=0 or cycle<=0 or demand<0 or power<=0 or not 0<eta<=1 or c<=0 or window<=0:
        raise ValueError('Nonphysical model input')
    capacity=n*60/cycle
    recovered=c*power*window*eta
    return {'variant':v['id'],'nominal_trips_per_hour':capacity,'daily_kwh':demand,
            'recovered_kwh':recovered,'charging_margin_kwh':recovered-demand,
            'capacity_screen_pass':capacity>=14,'energy_screen_pass':demand<=260,
            'recovery_screen_pass':recovered>=demand,
            'all_three_screens_pass':capacity>=14 and demand<=260 and recovered>=demand}

def validate(model,requirements,evidence):
    """Enforce typed references, relationship meaning, units and evidence status."""
    if model['model_id']!='NS-MBA9.1' or model['configuration']!='NS-MBA9.1':
        raise ValueError('Unexpected configuration')
    groups=[('needs','need'),('functions','function'),('interfaces','interface'),('architecture','architecture'),('analyses','analysis')]
    types={}
    for key,kind in groups:
        for obj in model[key]:
            i=obj['id']
            if i in types:raise ValueError('Duplicate node ID '+i)
            types[i]=kind
    for r in requirements:
        i=r['id']
        if i in types:raise ValueError('Duplicate requirement ID '+i)
        types[i]='requirement'
    if len(requirements)!=6 or set(r['id'] for r in requirements)!={f'R{i:02}' for i in range(1,7)}:
        raise ValueError('Six controlled requirements expected')
    for r in requirements:
        if types.get(r['need'])!='need':raise ValueError('Requirement source missing')
        if not r['measure'] or not r['statement'] or not r['test']:raise ValueError('Incomplete requirement')
    valid_relations={('need','requirement'):'derives',('requirement','function'):'allocatedTo'}
    trace_ids=set()
    for edge in model['trace']:
        if edge['id'] in trace_ids:raise ValueError('Duplicate trace edge')
        trace_ids.add(edge['id'])
        expected=valid_relations.get((types.get(edge['from']),types.get(edge['to'])))
        if edge['kind']!=expected:raise ValueError('Invalid typed relation '+edge['id'])
    for r in requirements:
        if not any(e['from']==r['need'] and e['to']==r['id'] for e in model['trace']):
            raise ValueError('Missing derivation '+r['id'])
        if not any(e['from']==r['id'] and types.get(e['to'])=='function' for e in model['trace']):
            raise ValueError('Missing allocation '+r['id'])
    for i in model['interfaces']:
        if not i['owner'] or not i['value_type'] or i['unit'] not in ('none','kWh') or float(i['freshness_ms'])<=0:
            raise ValueError('Invalid interface metadata')
        if i['producer']==i['consumer']:raise ValueError('Self interface must be independently justified')
    for a in model['analyses']:
        if not a['unit'] or not a['depends_on'] or not a['requirements']:
            raise ValueError('Incomplete analysis metadata')
        if any(node not in types for node in a['depends_on']):raise ValueError('Unknown analysis dependency '+a['id'])
        if any(types.get(r)!='requirement' for r in a['requirements']):raise ValueError('Unknown requirement in analysis '+a['id'])
    if len(model['architecture'])!=3:raise ValueError('Three controlled variants expected')
    names=set()
    for ev in evidence:
        if ev['evidence_id'] in names:raise ValueError('Duplicate evidence')
        names.add(ev['evidence_id'])
        r=next((r for r in requirements if r['id']==ev['requirement_id']),None)
        if r is None or ev['test_id']!=r['test']:raise ValueError('Invalid evidence reference')
        if ev['status'] not in {'MODELED','PLANNED','STALE','EXECUTED'}:raise ValueError('Unknown evidence status')
        if ev['status']=='EXECUTED' and ev['baseline']!=model['configuration']:
            raise ValueError('Out-of-configuration evidence cannot be current')
        if ev['status']=='MODELED' and (ev['baseline']!=model['configuration'] or not ev['source'].startswith('M9-RUN-')):
            raise ValueError('Model evidence requires current run')
        if ev['status']=='PLANNED' and ev['source']!='none':
            raise ValueError('Planned test cannot claim result source')
        if ev['status']=='STALE' and ev['baseline']==model['configuration']:
            raise ValueError('STALE status requires baseline mismatch here')
    if len(evidence)!=6 or len({e['requirement_id'] for e in evidence})!=6:
        raise ValueError('One illustrative evidence item per requirement')
    return types

def impacted(model,evidence,origin):
    """Forward impact over declared model dependencies, requirement claims and evidence."""
    graph={}
    def edge(a,b):graph.setdefault(a,set()).add(b)
    for analysis in model['analyses']:
        for dep in analysis['depends_on']:edge(dep,analysis['id'])
        for req in analysis['requirements']:edge(analysis['id'],req)
    for ev in evidence:edge(ev['requirement_id'],ev['evidence_id'])
    seen={origin};queue=[origin]
    while queue:
        for n in sorted(graph.get(queue.pop(0),())):
            if n not in seen:seen.add(n);queue.append(n)
    return sorted(seen)

def report(model_override=None, requirements_override=None, evidence_override=None):
    m=model_override if model_override is not None else data('model.json')
    r=requirements_override if requirements_override is not None else rows('requirements.csv')
    ev=evidence_override if evidence_override is not None else rows('evidence-register.csv')
    validate(m,r,ev)
    screens={v['id']:screen(v) for v in m['architecture']}
    if screens['B']['all_three_screens_pass'] is not True:
        raise ValueError('Controlled baseline B screening no longer passes; revise decision record')
    b=next(a for a in m['architecture'] if a['id']=='B')
    changed=screen(b,charger_kw=27,efficiency=.82)
    remedial=screen(b,charger_kw=27,efficiency=.82,chargers=5)
    impact=impacted(m,ev,'I02')
    open_evidence=[e['requirement_id'] for e in ev if e['status']!='EXECUTED']
    return {'model_id':m['model_id'],'screens':screens,'charger_change_B':changed,
            'five_charger_option_B':remedial,'change_CR42_impacted_ids':impact,
            'evidence_statuses':{e['requirement_id']:e['status'] for e in ev},
            'current_executed_requirement_count':sum(e['status']=='EXECUTED' for e in ev),
            'open_requirements':open_evidence,
            'recommendation':'CONDITIONAL_STUDY_ONLY'}

if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
