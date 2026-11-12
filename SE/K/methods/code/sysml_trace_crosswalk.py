#!/usr/bin/env python3
"""Cross-document checks for educational CSV artifacts vs baseline JSON.
Does NOT parse or validate SysML v2 textual notation; use an official parser for that.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'

def records(name):
    with (DATA/name).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))

def validate():
    errors=[]
    baseline=json.loads((DATA/'campus-mobility-release.json').read_text())
    requirement_rows=records('campus-requirements.csv')
    req={r['id']:r for r in requirement_rows}
    if len(req)!=len(requirement_rows):errors.append('duplicate requirement ID')
    model_req={r['id']:r for r in baseline['requirements']}
    if req.keys()!=model_req.keys():errors.append('baseline requirement ID mismatch')
    for key,row in req.items():
        if row['version']!=baseline['baseline']:errors.append(key+': baseline mismatch')
        if key in model_req:
            for col,prop in [('allocation','component'),('hazard','hazard'),('stakeholder_need','need')]:
                if row[col]!=model_req[key][prop]:errors.append(f'{key}: {col} mismatch')
    evidence={r['id']:r for r in baseline['evidence']}
    matrix=records('campus-verification-matrix.csv')
    if {r['requirement'] for r in matrix}!=set(req):errors.append('verification matrix requirement coverage mismatch')
    if len({r['requirement'] for r in matrix})!=len(matrix):errors.append('duplicate verification matrix row')
    for row in matrix:
        if row['requirement'] not in req:errors.append('unrecognized VCRM requirement')
        ev=evidence.get(row['evidence'])
        if ev is None or ev['requirement']!=row['requirement']:errors.append('VCRM evidence mismatch')
        if row['configuration']!=baseline['baseline']+' / '+baseline['build']:errors.append('VCRM stale configuration')
        if not row['open_limitation'].strip():errors.append('VCRM missing limitations')
    interface_rows=records('campus-interfaces.csv')
    if len({r['id'] for r in interface_rows})!=len(interface_rows):errors.append('duplicate interface ID')
    for row in interface_rows:
        if row['sender'] not in baseline['components'] and row['sender']!='operator-console':errors.append('interface sender missing: '+row['sender'])
        if row['receiver'] not in baseline['components'] and row['receiver']!='operator-console':errors.append('interface receiver missing: '+row['receiver'])
        if row['max_age_ms'].isdigit() and int(row['max_age_ms']) < int(row['update_period_ms']):
            errors.append('max age shorter than update period: '+row['id'])
    hazard_ids={h['id'] for h in baseline['hazards']}
    hazard_rows=records('campus-hazard-log.csv')
    if {r['id'] for r in hazard_rows}!=hazard_ids:errors.append('hazard register coverage mismatch')
    for row in hazard_rows:
        if row['id'] not in hazard_ids:errors.append('unrecognized hazard')
        if not row['causal_gaps'] or row['disposition']!='OPEN':errors.append('unresolved hazard incorrectly closed')
    for row in records('campus-change-impact.csv'):
        if row['from_baseline']!=baseline['baseline']:errors.append('change source baseline mismatch')
        if row['affected_evidence'] not in evidence:errors.append('unrecognized change evidence')
        if row['review_status']!='OPEN':errors.append('change impact deceptively closed')
    return errors

if __name__=='__main__':
    errors=validate()
    print('Cross-document audit:', 'PASS (structural only)' if not errors else '\n'.join(errors))
    raise SystemExit(1 if errors else 0)
