"""Simplified event-time examples, not a validated safety control."""
from pathlib import Path
import csv
DATA=Path(__file__).resolve().parents[1]/'data'/'fault-injection-events.csv'

def is_fresh(measurement_time,receipt_time,limit=5):
    if limit<0:raise ValueError('limit cannot be negative')
    if receipt_time < measurement_time:raise ValueError('inconsistent event order in simplified model')
    return receipt_time-measurement_time <= limit

def evaluate(path=DATA):
    with Path(path).open(newline='') as f:rows=list(csv.DictReader(f))
    return [(r['event_id'],is_fresh(float(r['measurement_time_s']),float(r['broker_receipt_s']),float(r['assumed_age_limit_s']))) for r in rows]

if __name__=='__main__':print(evaluate())
