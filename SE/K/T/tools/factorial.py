"""Balanced 2x2 cell means and difference-of-differences interaction."""
import csv
from collections import defaultdict
from pathlib import Path

def effects(rows):
    by=defaultdict(list)
    for r in rows: by[(int(r['vehicles']),r['policy'])].append(float(r['wait_min']))
    required={(1,'FCFS'),(1,'PRIORITY'),(2,'FCFS'),(2,'PRIORITY')}
    if set(by)!=required or not all(by.values()): raise ValueError('Require four nonempty cells')
    means={key:sum(v)/len(v) for key,v in by.items()}
    a,b,c,d=(means[(1,'FCFS')],means[(1,'PRIORITY')],means[(2,'FCFS')],means[(2,'PRIORITY')])
    return dict(means=means,fleet_effect=(c+d-a-b)/2,policy_effect=(b+d-a-c)/2,interaction=(d-c)-(b-a))

if __name__=='__main__':
    with (Path(__file__).parent.parent/'labs/factorial-results.csv').open() as f:
        print(effects(list(csv.DictReader(f))))
