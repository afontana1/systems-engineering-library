"""Reproducible evidence packaging and requirements/scenarios trace audit."""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path

def read_csv(path):
    with Path(path).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def trace_audit(requirements, tests, scenario_ids):
    errors=[]
    reqs={r['id'] for r in requirements}
    tids={t['test_id'] for t in tests}
    if len(reqs)!=len(requirements) or len(tids)!=len(tests):errors.append('duplicate IDs')
    linked=set(); covered_scenarios=set()
    for t in tests:
        for rid in filter(None,t['requirements'].split(';')):
            if rid not in reqs:errors.append(f"{t['test_id']} refers to nonexistent {rid}")
            else:linked.add(rid)
        for sid in filter(None,t['scenarios'].split(';')):
            if sid not in scenario_ids:errors.append(f"{t['test_id']} refers to nonexistent scenario {sid}")
            else:covered_scenarios.add(sid)
    missing=sorted(reqs-linked)
    if missing:errors.append('requirements without tests: '+', '.join(missing))
    return dict(pass_links=not errors,errors=errors,requirements_linked=len(linked),
                requirements_total=len(reqs),scenarios_linked=sorted(covered_scenarios),
                caveat='Links and syntax do not establish test adequacy')

def manifest(root,relpaths):
    result={}
    for rel in sorted(relpaths):
        p=Path(root)/rel
        if not p.is_file():raise FileNotFoundError(rel)
        result[rel]=sha(p)
    return result
