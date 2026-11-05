"""Trace and risk-mitigation coverage checks; presence of links is not validity evidence."""
import csv
from collections import defaultdict


def read_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def audit_traceability(requirements, tests, hazards):
    rid = [r['req_id'] for r in requirements]
    tid = [t['test_id'] for t in tests]
    hid = [h['hazard_id'] for h in hazards]
    if len(set(rid))!=len(rid) or len(set(tid))!=len(tid) or len(set(hid))!=len(hid):
        raise ValueError('duplicate identifier in trace source')
    if not rid:
        raise ValueError('no requirements supplied')
    req_set, test_set = set(rid), set(tid)
    broken = []
    req_to_tests = defaultdict(set)
    for t in tests:
        for r in t['req_ids'].split(';'):
            if r not in req_set:
                broken.append(f"test {t['test_id']} -> unknown requirement {r}")
            else:
                req_to_tests[r].add(t['test_id'])
    haz_to_test = {}
    for h in hazards:
        tests_claimed = set(filter(None, h['verification_test_ids'].split(';')))
        haz_to_test[h['hazard_id']] = tests_claimed
        for t in tests_claimed:
            if t not in test_set:
                broken.append(f"hazard {h['hazard_id']} -> unknown test {t}")
    req_uncovered = sorted(req_set - set(req_to_tests))
    hazard_uncovered = sorted(h for h,ts in haz_to_test.items() if not ts)
    return dict(requirements=len(rid), requirements_with_tests=len(rid)-len(req_uncovered),
                trace_coverage_fraction=(len(rid)-len(req_uncovered))/len(rid),
                missing_requirement_test_links=req_uncovered,
                hazards_with_test_links=len(hid)-len(hazard_uncovered),
                hazards_missing_test_links=hazard_uncovered,
                dangling_references=broken,
                link_integrity_pass=(not broken and not req_uncovered and not hazard_uncovered),
                caveat='Link presence verifies a graph property, not correctness, independence or sufficiency of tests')
