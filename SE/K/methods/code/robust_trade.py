#!/usr/bin/env python3
"""Exhaustive evaluation of six hypothetical design alternatives.

Monetary loss equivalents are assumptions, not measured market values.
No claims about globally optimal designs or real-world feasibility are made.
"""
from __future__ import annotations
import csv
import math
import sys
from pathlib import Path

SCENARIOS = ('normal_s', 'peak_s', 'disruption_s')
DEFAULT_PROB = (0.6, 0.3, 0.1)


def read_designs(path: Path) -> list[dict]:
    designs = []
    with path.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            d = {'design': row['design']}
            for col in ('cost_kusd', 'energy_kwh', *SCENARIOS):
                d[col] = float(row[col])
                if not math.isfinite(d[col]) or d[col] < 0:
                    raise ValueError('Each input must be finite and nonnegative')
            designs.append(d)
    if not designs or len(set(d['design'] for d in designs)) != len(designs):
        raise ValueError('Need unique design identifiers')
    return designs


def objective(d):
    return (d['cost_kusd'], d['energy_kwh'], max(d[s] for s in SCENARIOS))


def dominates(a, b):
    x, y = objective(a), objective(b)
    return all(v <= w for v, w in zip(x, y)) and any(v < w for v, w in zip(x, y))


def analyze(designs, probabilities=DEFAULT_PROB, latency_loss_rate=10, max_delay=None):
    if len(probabilities) != 3 or any(not math.isfinite(p) or p < 0 for p in probabilities) or not math.isclose(sum(probabilities), 1, abs_tol=1e-10):
        raise ValueError('Three scenario probabilities must sum to 1')
    if not math.isfinite(latency_loss_rate) or latency_loss_rate < 0:
        raise ValueError('Invalid latency-loss conversion')
    efficient = [d['design'] for d in designs if not any(dominates(other, d) for other in designs if other is not d)]
    feasible = [d for d in designs if max_delay is None or max(d[s] for s in SCENARIOS) <= max_delay]
    if not feasible:
        raise ValueError('No feasible designs under scenario constraint')
    loss = {d['design']: [d['cost_kusd'] + latency_loss_rate*d[s] for s in SCENARIOS] for d in feasible}
    best_by_scenario = [min(values[i] for values in loss.values()) for i in range(3)]
    expected = {name: sum(p*l for p, l in zip(probabilities, values)) for name, values in loss.items()}
    regret = {name: [l-best_by_scenario[i] for i, l in enumerate(values)] for name, values in loss.items()}
    max_regret = {name: max(values) for name, values in regret.items()}
    return {
        'pareto': sorted(efficient), 'feasible': sorted(d['design'] for d in feasible),
        'expected_loss': expected, 'regret': regret, 'max_regret': max_regret,
        'best_expected': min(expected, key=expected.get),
        'best_minimax_regret': min(max_regret, key=max_regret.get),
    }


def switching_disruption_probability(designs, first='D', second='A',
                                     peak_probability=0.3, latency_loss_rate=10):
    """Disruption probability q at equal expected loss, holding peak p fixed.

    Nominal probability is 1 - peak_probability - q. Results outside the
    probability simplex are not physically meaningful for these assumptions.
    """
    if not 0 <= peak_probability <= 1:
        raise ValueError('Invalid peak probability')
    options={d['design']:d for d in designs}
    if first not in options or second not in options:
        raise ValueError('Unknown design')
    def losses(d):
        return [d['cost_kusd']+latency_loss_rate*d[s] for s in SCENARIOS]
    a=losses(options[first]); b=losses(options[second])
    delta=[x-y for x,y in zip(a,b)]
    intercept=(1-peak_probability)*delta[0]+peak_probability*delta[1]
    slope=delta[2]-delta[0]
    if math.isclose(slope,0,abs_tol=1e-12):return None
    q=-intercept/slope
    return q if 0<=q<=1-peak_probability else None


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1]/'data/design-trade-scenarios.csv'
    designs = read_designs(path)
    print('All:', analyze(designs))
    print('Worst-delay <= 8s feasible subset:', analyze(designs, max_delay=8.0))
    print('D vs A disruption switching probability:', switching_disruption_probability(designs))
