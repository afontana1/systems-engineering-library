#!/usr/bin/env python3
"""Check structural completeness and configuration-currency of a tiny teaching model.

A clean audit proves a set of JSON link rules, not correctness of the system,
conformance to SysML v2, integrity of the records, or adequacy of evidence.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

DEFAULT=Path(__file__).resolve().parents[1]/'data/campus-mobility-release.json'


def unique_map(items, category, errors):
    result={}
    for item in items:
        key=item.get('id')
        if not key or key in result:
            errors.append(f'{category}: missing or duplicate ID {key!r}')
        else:
            result[key]=item
    return result


def audit(data):
    errors=[]; warnings=[]
    req=unique_map(data['requirements'],'requirements',errors)
    ev=unique_map(data['evidence'],'evidence',errors)
    haz=unique_map(data['hazards'],'hazards',errors)
    controls=unique_map(data['controls'],'controls',errors)
    components=set(data['components'])
    for r in req.values():
        rid=r['id']
        if r.get('component') not in components:errors.append(f'{rid}: allocation missing')
        if r.get('hazard') not in haz:errors.append(f'{rid}: hazard reference missing')
        if r.get('control') not in controls:errors.append(f'{rid}: control reference missing')
        if not r.get('need'):errors.append(f'{rid}: originating need missing')
        if not r.get('evidence'):errors.append(f'{rid}: no evidence links')
        for eid in r.get('evidence',[]):
            if eid not in ev:errors.append(f'{rid}: missing evidence {eid}')
            elif ev[eid].get('requirement')!=rid:errors.append(f'{rid}: reversed evidence reference {eid}')
    for h in haz.values():
        for cid in h.get('controls',[]):
            if cid not in controls:errors.append(f'{h["id"]}: missing control {cid}')
    for cid,c in controls.items():
        if c.get('owner') not in components:errors.append(f'{cid}: unknown component owner')
        if not c.get('evidence'):errors.append(f'{cid}: no control evidence')
        for eid in c.get('evidence',[]):
            if eid not in ev:errors.append(f'{cid}: missing evidence {eid}')
    for eid,e in ev.items():
        if e.get('requirement') not in req:errors.append(f'{eid}: no parent requirement')
        if e.get('baseline') != data['baseline']:errors.append(f'{eid}: stale model baseline {e.get("baseline")}')
        if e.get('build') != data['build']:errors.append(f'{eid}: stale software build {e.get("build")}')
        if e.get('result') != 'PASS':errors.append(f'{eid}: not a passing observation')
        if 'observed_max_s' in e:
            if e['observed_max_s'] > e['limit_s']:errors.append(f'{eid}: timing limit exceeded')
        if e.get('limitations'):warnings.append(f'{eid}: {e["limitations"]}')
    if data.get('open_questions'):warnings += [f'Open question: {q}' for q in data['open_questions']]
    return {'baseline':data['baseline'],'requirements':len(req),'hazards':len(haz),'evidence':len(ev),'errors':errors,'warnings':warnings,'structurally_consistent':not errors}


def run(path=DEFAULT):
    return audit(json.loads(Path(path).read_text(encoding='utf-8')))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fixture',nargs='?',type=Path,default=DEFAULT)
    args=parser.parse_args(); result=run(args.fixture)
    print(json.dumps(result,indent=2))
    raise SystemExit(1 if result['errors'] else 0)
