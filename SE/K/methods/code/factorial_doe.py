#!/usr/bin/env python3
"""Balanced 2x2 factorial teaching example; standard library only.

Run: python3 factorial_doe.py ../data/dispatch-factorial.csv
Numbers are synthetic; the code does not assert independence or causal validity.
"""
from __future__ import annotations
import csv
import math
import statistics
import sys
from pathlib import Path

T_975_DF12 = 2.17881283  # two-sided 95% Student-t critical value, 12 df


def analyze(path: Path) -> dict:
    cells = {(a, b): [] for a in (-1, 1) for b in (-1, 1)}
    orders = []
    with path.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            a, b = int(row['A']), int(row['B'])
            if (a, b) not in cells:
                raise ValueError('Factors must be -1 or +1')
            value = float(row['latency_ms'])
            if not math.isfinite(value) or value < 0:
                raise ValueError('Latency must be finite and nonnegative')
            cells[a, b].append(value)
            orders.append(int(row['run_order']))
    n = len(cells[-1, -1])
    if n < 2 or any(len(v) != n for v in cells.values()):
        raise ValueError('Balanced design with at least two runs in each cell required')
    if len(set(orders)) != len(orders):
        raise ValueError('Run order identifiers must be unique')
    means = {k: statistics.mean(v) for k, v in cells.items()}
    m = lambda a, b: means[(a, b)]
    effects = {
        'A': (m(1, -1) + m(1, 1) - m(-1, -1) - m(-1, 1)) / 2,
        'B': (m(-1, 1) + m(1, 1) - m(-1, -1) - m(1, -1)) / 2,
        'AB': (m(-1, -1) + m(1, 1) - m(1, -1) - m(-1, 1)) / 2,
    }
    df = 4 * (n - 1)
    sse = sum((x - means[k]) ** 2 for k, vs in cells.items() for x in vs)
    mse = sse / df
    se = math.sqrt(mse / n)
    # For this synthetic data set n=4 -> df=12; do not reuse t value at other n.
    return {'cells': means, 'effects': effects, 'n_cell': n, 'df': df,
            'mse': mse, 'effect_se': se,
            'effect_ci_95': {k: (v - T_975_DF12 * se, v + T_975_DF12 * se)
                             for k, v in effects.items()} if df == 12 else None}


def wilson_interval(k: int, n: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if not (isinstance(k, int) and isinstance(n, int) and 0 <= k <= n and n > 0):
        raise ValueError('Require integers 0 <= k <= n, n > 0')
    p = k / n
    den = 1 + z*z/n
    center = (p + z*z/(2*n)) / den
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
    return max(0.0, center-half), min(1.0, center+half)


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1]/'data/dispatch-factorial.csv'
    result = analyze(path)
    print('Cell means (ms):', result['cells'])
    print('Estimated effects (ms):', result['effects'])
    print('Residual df, MSE, effect SE:', result['df'], result['mse'], result['effect_se'])
    print('Illustrative 95% effect CIs:', result['effect_ci_95'])
    print('Wilson 95% interval for 0 of 20:', wilson_interval(0, 20))
