"""Distinguish planned verification links from evidence of passed execution."""
import csv
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data" / "verification-status.csv"

def audit(path=DATA):
    with Path(path).open(newline='') as f: rows=list(csv.DictReader(f))
    if not rows or len({r['requirement_id'] for r in rows}) != len(rows):raise ValueError('Missing or duplicate requirements')
    planned=sum(r['planned'].lower()=='yes' for r in rows)
    passed=sum(r['execution'].lower()=='passed' and r['configuration_compatible'].lower()=='yes' for r in rows)
    return dict(total=len(rows),planned=planned,planned_fraction=planned/len(rows),passed=passed,passed_fraction=passed/len(rows),unresolved=len(rows)-passed)

if __name__=='__main__':print(audit())
