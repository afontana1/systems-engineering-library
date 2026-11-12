#!/usr/bin/env python3
"""Synthetic NS-MB3 graph and feasibility checks; standard library only.

This checks a deliberately simplified JSON teaching schema; it does not parse
SysML, validate standard conformance, or certify operational performance.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / 'case/model-baseline.json'
EVIDENCE = DEFAULT.with_name('evidence-register.csv')


def evaluate(model: dict) -> dict:
    reqs = model['requirements']; needs = {n['id'] for n in model['needs']}
    components = set(model['components'])
    tests = {t['id']: t for t in model['tests']}
    issues = []
    evidence = {}
    req_ids = [r['id'] for r in reqs]
    if len(req_ids) != len(set(req_ids)):
        issues.append('duplicate requirement ID')
    for r in reqs:
        rid = r['id']
        if r['need'] not in needs: issues.append(f'{rid}: unrecognized stakeholder need')
        if r['allocated_to'] not in components: issues.append(f'{rid}: missing allocated component')
        t = tests.get(r['test'])
        if not t or t['requirement'] != rid:
            evidence[rid] = 'NO_LINKED_TEST'; continue
        if t['req_revision'] != r['revision'] or t['baseline'] != model['baseline']:
            evidence[rid] = 'STALE_EVIDENCE'; continue
        if t['result'] != 'PASS':
            evidence[rid] = 'NO_PASS_RESULT'; continue
        evidence[rid] = 'LINKED_FIXTURE_ONLY'
    for f in model['functions']:
        if f['component'] not in components:issues.append(f"{f['id']}: allocation target absent")
    for i in model['interfaces']:
        if i['source'] not in components or i['target'] not in components:
            issues.append(f"{i['id']}: unknown interface endpoint")
        if i['max_age_ms'] <= 0: issues.append(f"{i['id']}: invalid age budget")
    p = model['assumptions']
    peak = p['scheduled_peak_trips_per_hour']
    candidate_checks = {c['id']:{'capacity_per_hour':c['vehicles']*p['trips_per_vehicle_per_hour'],
                                   'headroom_per_hour':c['vehicles']*p['trips_per_vehicle_per_hour']-peak,
                                   'cost_million_usd':c['cost_million_usd']}
                        for c in model['candidates']}
    nominal = sum(p['nominal_latency_ms']); degraded = sum(p['degraded_latency_ms'])
    energy = p['shift_trips'] * (p['route_km'] * p['traction_kwh_per_km'] + p['aux_kwh_per_trip'])
    allowable = p['battery_kwh'] * (1 - p['reserve_fraction'])
    return {'case_id':model['case_id'], 'baseline':model['baseline'], 'structural_issues':issues,
            'evidence':evidence, 'candidates':candidate_checks,
            'nominal_latency_ms':nominal,'degraded_latency_ms':degraded,
            'nominal_latency_margin_ms':400-nominal,'degraded_latency_margin_ms':400-degraded,
            'shift_energy_kwh':round(energy,6),'allowable_energy_kwh':allowable,
            'energy_margin_kwh':round(allowable-energy,6)}


def compare_evidence(model: dict, csv_file: Path) -> list[str]:
    diagnostics=[]
    tests = {t['id']: t for t in model['tests']}
    with csv_file.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f):
            t=tests.get(row['test_id'])
            if not t: diagnostics.append(f"{row['test_id']}: no matching model test");continue
            if (row['requirement_id'] != t['requirement'] or
                int(row['requirement_revision']) != t['req_revision'] or
                row['baseline'] != t['baseline'] or row['outcome'] != t['result']):
                diagnostics.append(f"{row['test_id']}: test/register fields disagree")
    return diagnostics


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('model',nargs='?',type=Path,default=DEFAULT)
    args=ap.parse_args()
    model=json.loads(args.model.read_text(encoding='utf-8'))
    result=evaluate(model)
    if args.model.resolve()==DEFAULT.resolve():
        result['evidence_register_disagreements']=compare_evidence(model,EVIDENCE)
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
