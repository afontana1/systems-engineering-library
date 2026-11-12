#!/usr/bin/env python3
"""Reproduce Book 1's synthetic, cross-chapter Campus Mobility examples.

No external dependencies, no operational-safety claims, no learner tracking.
Run: python3 SE/K/B1/tools/step03_case_check.py
"""
import csv
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / 'case'


def check():
    data = json.loads((BASE / 'northstar-reference-baseline.json').read_text())
    assert data['baseline'] == 'NS-B1'
    req = {r['id']: r for r in data['requirements']}
    assert len(req) == len(data['requirements'])
    comps = set(data['components'])
    checks = set()
    with (BASE / 'traceability.csv').open(newline='') as file:
        links = list(csv.DictReader(file))
    for link in links:
        assert link['requirement'] in req
        assert link['component'] in comps
        assert link['verification'] and link['test_baseline']
        assert link['requirement'] not in checks
        checks.add(link['requirement'])
    assert checks == set(req)
    stale = [r for r in links if r['test_baseline'] != data['baseline']]
    assert len(stale) == 1 and stale[0]['requirement'] == 'NS-R-04'

    # Chapter 2: expected cost before test; test is worth no more than EVPI.
    known_cost = 120
    novel_expected = 90 + 0.30 * 100
    assert novel_expected == known_cost  # illustration of a decision tie
    # Chapter 5/7: deterministic latency allocations, NOT percentiles.
    latency_s = data['latency_budget_seconds']
    allocated = sum(latency_s.values())
    assert math.isclose(allocated, 1.65, abs_tol=1e-10)
    assert math.isclose(2.5-allocated, 0.85, abs_tol=1e-10)
    # Chapter 8: trade score and pairwise switch point.
    options = data['decision_scores']
    weights = dict(resilience=.5, affordability=.3, maintainability=.2)
    scores = {name: sum(weights[k]*val[k] for k in weights) for name,val in options.items()}
    assert scores == {'turnkey':70.0, 'federated':74.5, 'demonstrator':73.5}
    tie = 23/55
    assert 0 < tie < 0.8
    # Chapter 10: redundant independent channels conditional on shared cause absent.
    common, a, b = .003, .01, .02
    top_event = common + (1-common)*a*b
    assert math.isclose(top_event, .0031994, abs_tol=1e-12)
    # Chapter 11: exact one-sided independent Bernoulli bound for zero failures.
    n, alpha = 300, .05
    p_upper = 1-alpha**(1/n)
    assert .0099 < p_upper < .0100
    # Chapter 9: EVM is an indicator, NOT evidence of technical acceptance.
    cpi, spi = 320/360,320/400
    assert math.isclose(cpi,8/9) and spi == .8
    # Chapter 12: distinguish structural completeness from evidence currency.
    return {'requirements':len(req),'links':len(links),'stale':len(stale),
            'allocated_latency_s':round(allocated,3),'latency_margin_s':round(2.5-allocated,3),
            'decision_scores':scores,'pairwise_weight_switch':round(tie,6),
            'shared_cause_top_event':round(top_event,7),
            'zero_failures_95pct_upper':round(p_upper,7),'CPI':round(cpi,4),'SPI':spi}

if __name__ == '__main__':
    print(json.dumps(check(),indent=2))
