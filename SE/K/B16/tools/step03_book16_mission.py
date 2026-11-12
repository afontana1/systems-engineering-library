#!/usr/bin/env python3
"""NS-DME16.1 synthetic digital-mission evidence laboratory (stdlib only).

Usage: python SE/K/B16/tools/step03_book16_mission.py [--out PATH]
No Internet, external data, credentials, physical-system qualifications or dependencies.
JSON files are controlled inputs; never treat a passing model query as certification.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path

CASE = Path(__file__).resolve().parents[1] / 'case'
KINDS = {'requirement', 'function', 'component', 'interface', 'test', 'evidence', 'activity', 'decision'}
EDGE_TYPES = {
    'allocated_to': ('requirement', 'function'),
    'realized_by': ('function', 'component'),
    'checked_by': ('requirement', 'test'),
    'produced': ('test', 'evidence'),
    'uses_interface': ('test', 'interface'),
    'depends_on': ('activity', 'function'),
    'informs': ('requirement', 'decision'),
}
CLEARANCE = {'reader': 0, 'engineer': 1, 'assurance': 2}
SENSITIVITY = {'public': 0, 'internal': 1, 'restricted': 2}
GROUPS = ('standard', 'accessible', 'critical')


def inputs():
    return json.loads((CASE / 'controlled-inputs.json').read_text(encoding='utf-8'))


def validate(cfg):
    if cfg.get('intended_use') != 'course-screening':
        raise ValueError('Use-specific authority is not interchangeable with operational qualification')
    graph = cfg['graph']
    nodes = graph['nodes']
    by_id = {n['id']: n for n in nodes}
    if len(by_id) != len(nodes) or not nodes:
        raise ValueError('Duplicate or missing object IDs')
    for node in nodes:
        if node['kind'] not in KINDS or not node['revision'] or not node['owner']:
            raise ValueError('Node missing valid kind, configuration or owner')
        if node['sensitivity'] not in SENSITIVITY:
            raise ValueError('Unrecognized sensitivity label')
        if not node['authority_for'] or cfg['intended_use'] not in node['authority_for']:
            raise ValueError('Authority scope absent for current intended use')
    edges = set()
    for e in graph['links']:
        if e['from'] not in by_id or e['to'] not in by_id or e['relation'] not in EDGE_TYPES:
            raise ValueError('Dangling node or unrecognized edge semantics')
        a, b = EDGE_TYPES[e['relation']]
        if by_id[e['from']]['kind'] != a or by_id[e['to']]['kind'] != b:
            raise ValueError('Relationship violates typed graph semantics')
        key = (e['from'], e['relation'], e['to'])
        if key in edges:
            raise ValueError('Duplicate relation')
        edges.add(key)
    m = cfg['mission']
    probs = m['scenario_probability']
    if not probs or abs(math.fsum(probs.values()) - 1.0) > 1e-10 or any(p < 0 or not math.isfinite(p) for p in probs.values()):
        raise ValueError('Scenario weights must be finite nonnegative probabilities summing to one')
    for field in ('daily_demand', 'vehicle_productivity_per_day'):
        if set(m[field]) != set(GROUPS) or any(v <= 0 or not math.isfinite(v) for v in m[field].values()):
            raise ValueError('Demand and productivity require positive finite values for every group')
    if set(probs) != set(m['scenario_capacity_factors']):
        raise ValueError('Scenario factors and probabilities must cover same names')
    for factors in m['scenario_capacity_factors'].values():
        if set(factors) != set(GROUPS) or any(v < 0 or v > 1 or not math.isfinite(v) for v in factors.values()):
            raise ValueError('Capacity factor outside [0,1]')
    for policy in m['policies']:
        if any(policy[g+'_vehicles'] < 0 or type(policy[g+'_vehicles']) is not int for g in GROUPS):
            raise ValueError('Fleet counts must be nonnegative integers')
        if policy['incremental_cost_usd'] < 0:
            raise ValueError('Negative intervention cost')
        if set(policy['interventions']) - set(m['continuity_uplifts']):
            raise ValueError('Unknown intervention')
    if len({x['id'] for x in m['policies']}) != len(m['policies']):
        raise ValueError('Duplicate policies')
    for group, floor in m['service_floors'].items():
        if group not in GROUPS or not 0 <= floor <= 1:
            raise ValueError('Invalid minimum service requirement')
    if not 0 <= m['minimum_scenario_coverage'] <= 1:
        raise ValueError('Invalid mission reliability screening threshold')
    twin = cfg['twin']
    for k in ('predicted_soc', 'observed_soc'):
        if not 0 <= twin[k] <= 1: raise ValueError('SOC reading outside physical bounds')
    if twin['prediction_sigma'] <= 0 or twin['observation_sigma'] <= 0:
        raise ValueError('Nonpositive standard deviation')
    if twin['observation_age_minutes'] < 0 or twin['maximum_age_minutes'] < 0:
        raise ValueError('Negative timestamps')
    return by_id, edges


def get_artifact(cfg, object_id, role, use='course-screening'):
    if role not in CLEARANCE:raise PermissionError('Unknown role, fail closed')
    nodes, _ = validate(cfg)
    if object_id not in nodes:raise KeyError(object_id)
    record = nodes[object_id]
    if CLEARANCE[role] < SENSITIVITY[record['sensitivity']]:
        raise PermissionError('Role lacks clearance to retrieve object')
    if use not in record['authority_for']:
        raise PermissionError('Object not authoritative for requested use')
    return record


def trace(cfg):
    nodes, links = validate(cfg)
    def targets(source, rel):
        return [nodes[t] for s, r, t in sorted(links) if s == source and r == rel]
    results = []
    for r in sorted((n for n in nodes.values() if n['kind'] == 'requirement'), key=lambda n: n['id']):
        fs = targets(r['id'], 'allocated_to')
        ts = targets(r['id'], 'checked_by')
        components = [c for f in fs for c in targets(f['id'], 'realized_by')]
        evidence = [e for t in ts for e in targets(t['id'], 'produced')]
        linked = bool(fs and ts and components and evidence)
        status = 'LINK_GAP' if not linked else 'CURRENT'
        if linked:
            for t in ts:
                e_rows = targets(t['id'], 'produced')
                interfaces = targets(t['id'], 'uses_interface')
                for e in e_rows:
                    if e.get('result') != 'pass' or e.get('test_revision') != t['revision']:
                        status = 'STALE_OR_FAILED_EVIDENCE'
                    if interfaces and any(e.get('interface_revision') != i['revision'] for i in interfaces):
                        status = 'STALE_INTERFACE_EVIDENCE'
        results.append({'requirement': r['id'], 'linked': linked, 'evidence_status': status,
                        'configuration_screen_complete': status == 'CURRENT',
                        'operationally_qualified': False,
                        'evidence_ids': ','.join(e['id'] for e in evidence)})
    return results


def impact(cfg, changed_id):
    nodes, edges = validate(cfg)
    if changed_id not in nodes:raise KeyError(changed_id)
    tests = sorted(s for s,rel,t in edges if rel == 'uses_interface' and t == changed_id)
    evidence = sorted(t for s,rel,t in edges if rel == 'produced' and s in tests)
    requirements = sorted(s for s,rel,t in edges if rel == 'checked_by' and t in tests)
    decisions = sorted(t for s,rel,t in edges if rel == 'informs' and s in requirements)
    return {'changed':changed_id,'affected_tests':tests,'affected_evidence':evidence,
            'affected_requirements':requirements,'affected_decisions':decisions}


def supplier_change(cfg, new_revision='2.0'):
    # Caller should use deepcopy before modification.
    node = next(n for n in cfg['graph']['nodes'] if n['id'] == 'IF-DISPATCH')
    node['revision'] = new_revision
    return trace(cfg)


def mission(cfg):
    validate(cfg)
    m = cfg['mission']; rows = []; summaries = []
    for policy in m['policies']:
        coverage = 0.0
        expectations = {g:0.0 for g in GROUPS}
        for scen, probability in m['scenario_probability'].items():
            served = {}
            fractions = {}
            for group in GROUPS:
                factor = m['scenario_capacity_factors'][scen][group]
                for intervention in policy['interventions']:
                    factor += m['continuity_uplifts'][intervention].get(scen,{}).get(group,0)
                factor = min(1.0,factor)
                capacity = policy[group+'_vehicles'] * m['vehicle_productivity_per_day'][group] * factor
                served[group] = min(m['daily_demand'][group], capacity)
                fractions[group] = served[group]/m['daily_demand'][group]
                expectations[group] += probability*fractions[group]
            feasible = all(fractions[g]+1e-12 >= m['service_floors'][g] for g in GROUPS)
            if feasible: coverage += probability
            rows.append({'policy':policy['id'],'scenario':scen,'probability':probability,
                         **{'served_'+g:round(served[g],6) for g in GROUPS},
                         **{'fraction_'+g:round(fractions[g],6) for g in GROUPS},
                         'all_groups_meet_floor':feasible})
        summaries.append({'policy':policy['id'],'incremental_cost_usd':policy['incremental_cost_usd'],
                          'scenario_coverage':round(coverage,10),
                          **{'expected_fraction_'+g:round(expectations[g],10) for g in GROUPS},
                          'passes_coverage_screen': coverage+1e-12 >= m['minimum_scenario_coverage']})
    return rows,summaries


def twin(cfg):
    validate(cfg)
    t = cfg['twin']
    age = t['observation_age_minutes']
    if age > t['maximum_age_minutes']:
        return {'status':'STALE_REJECT','age_minutes':age,'posterior_soc':None,
                'threshold_assessment':'NOT_EVALUATED'}
    vprior = t['prediction_sigma']**2
    vobs = t['observation_sigma']**2
    gain = vprior/(vprior+vobs)
    unbiased_observation = t['observed_soc']-t['sensor_bias']
    posterior = t['predicted_soc']+gain*(unbiased_observation-t['predicted_soc'])
    naive = t['predicted_soc']+gain*(t['observed_soc']-t['predicted_soc'])
    return {'status':'FRESH_BOUNDED_ESTIMATE', 'age_minutes':age,'kalman_gain':gain,
            'bias_corrected_observation':unbiased_observation,'posterior_soc':posterior,
            'posterior_sigma':math.sqrt((1-gain)*vprior),'naive_uncorrected_soc':naive,
            'threshold_assessment':'INVESTIGATE' if posterior < t['investigate_below_soc'] else 'ABOVE_ILLUSTRATIVE_THRESHOLD'}


def write_csv(path,rows):
    if not rows:raise ValueError('Empty output cannot be a result')
    with path.open('w',encoding='utf-8',newline='') as f:
        w = csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader();w.writerows(rows)


def produce(cfg, dest):
    validate(cfg);dest.mkdir(parents=True,exist_ok=True)
    tr = trace(cfg)
    comparison, summaries = mission(cfg)
    twin_result = twin(cfg)
    import copy
    changed = copy.deepcopy(cfg)
    after = supplier_change(changed)
    change = {'change':'Supplier dispatch interface changed from 1.0 to 2.0 without retest',
              'impact':impact(changed,'IF-DISPATCH'),
              'before_current':sum(x['configuration_screen_complete'] for x in tr),
              'after_current':sum(x['configuration_screen_complete'] for x in after),
              'after':after}
    output = {'case_id':cfg['case_id'],'revision':cfg['revision'], 'intended_use':cfg['intended_use'],
              'mission_summary':summaries,'trace_summary':{'requirements':len(tr),
              'current_screening_evidence':sum(x['configuration_screen_complete'] for x in tr),
              'operationally_qualified':0},'twin_result':twin_result,
              'decision':'HOLD_OPERATIONAL_QUALIFICATION',
              'reasons':['No policy reaches the illustrative joint-scenario threshold',
                         'Synthetic evidence does not qualify an operational system',
                         'Supplier interface change requires affected evidence to be regenerated']}
    write_csv(dest/'mission-scenarios.csv',comparison)
    write_csv(dest/'mission-summary.csv',summaries)
    write_csv(dest/'trace-quality.csv',tr)
    (dest/'supplier-impact.json').write_text(json.dumps(change,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    (dest/'model-results.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    return output


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=CASE)
    args=parser.parse_args()
    result=produce(inputs(),args.out)
    print(json.dumps({'case':result['case_id'],'decision':result['decision'],
                      'mission':result['mission_summary'],'trace':result['trace_summary'],
                      'twin':result['twin_result']},indent=2))
