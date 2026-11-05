"""Structural trace audit. A clean result never establishes semantic validity."""
import csv
from pathlib import Path


def audit(rows):
    rows = list(rows)
    duplicate_ids = sorted({r['requirement_id'] for r in rows if sum(x['requirement_id'] == r['requirement_id'] for x in rows)>1})
    return {
        'count':len(rows),
        'missing_source':[r['requirement_id'] for r in rows if not r['source_need'].strip()],
        'missing_test':[r['requirement_id'] for r in rows if not r['test_id'].strip()],
        'critical_without_test':[r['requirement_id'] for r in rows if r['criticality'].lower()=='high' and not r['test_id'].strip()],
        'duplicate_ids':duplicate_ids,
    }


def from_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return audit(csv.DictReader(f))


if __name__ == '__main__':
    print(from_csv(Path(__file__).resolve().parents[1] / 'data' / 'requirements-clinic.csv'))
