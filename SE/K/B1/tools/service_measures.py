"""Synthetic teaching-data service measures, not an operational assessment."""
import csv
from collections import defaultdict
from pathlib import Path


def compute(records):
    out = {}
    by = defaultdict(list)
    for r in records:
        if int(r['eligible']) != 1:
            continue
        by['ALL'].append(r)
        by[r['period']].append(r)
    for period, rows in by.items():
        n = len(rows)
        completed = sum(int(r['completed']) for r in rows)
        timely = sum(int(r['timely']) for r in rows)
        if any(int(r['timely']) > int(r['completed']) for r in rows):
            raise ValueError('A timely trip cannot be an incomplete trip')
        out[period] = dict(eligible=n, completed=completed, timely=timely,
                           completion=completed/n if n else None,
                           timely_given_completed=timely/completed if completed else None,
                           timely_given_eligible=timely/n if n else None)
    return out


def from_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return compute(list(csv.DictReader(f)))


if __name__ == '__main__':
    for group, measures in from_csv(Path(__file__).resolve().parents[1] / 'data' / 'request-outcomes.csv').items():
        print(group, measures)
