#!/usr/bin/env python3
"""Reproduce NS-SW5.1 teaching calculations and audit declared evidence.

Uses only Python's standard library. Synthetic records are NOT operational evidence.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path

CASE=Path(__file__).resolve().parents[1]/'case'

def model(): return json.loads((CASE/'model-baseline.json').read_text(encoding='utf-8'))
def records(name):
    with (CASE/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def time_budget(days=30, objective=0.999, observed=36):
    permitted=(1-objective)*days*24*60
    return {'permitted_min': permitted, 'observed_min':observed,
            'remaining_min':permitted-observed, 'observed_fraction':observed/(days*24*60)}

def queue_p95_ms(arrivals,service, fixed_ms=170):
    if service <= arrivals: raise ValueError('M/M/1 unstable or at saturation')
    return -math.log(0.05)/(service-arrivals)*1000+fixed_ms

def series_availability(a=0.9995,b=0.9995,common_cause=0.001):
    if not all(0<=x<=1 for x in (a,b,common_cause)):
        raise ValueError('Probabilities must be in [0,1]')
    return a*b*(1-common_cause)

def retry_attempts(first_failure_prob, max_attempts=2):
    """Expected attempts for independent/repeated failure with constant p. No backoff/load feedback."""
    if not 0<=first_failure_prob<=1 or max_attempts<1: raise ValueError('invalid retry assumptions')
    return sum(first_failure_prob**i for i in range(max_attempts))

def evidence_status(doc):
    r={}
    for e in doc['evidence']:
        key=e['requirement']
        if e['baseline']!=doc['baseline']: status='STALE'
        elif e['status']=='PLANNED': status='NOT_EXECUTED'
        elif e['status']=='AT_RISK': status='SLO_RISK'
        elif e['status']=='FAIL': status='FAILED_SYNTHETIC_CHECK'
        elif e['status']=='PASS': status='CURRENT_SYNTHETIC_PASS'
        else: status='UNKNOWN'
        if key in r: raise ValueError('Duplicate evidence key: '+key)
        r[key]=status
    return r

def audit(doc):
    errors=[]
    ids=[x['id'] for x in doc['requirements']]
    owners=set(doc['components'])
    if len(ids)!=len(set(ids)):errors.append('duplicate requirement')
    if any(x['owner'] not in owners for x in doc['requirements']):errors.append('unknown component owner')
    if any(x['requirement'] not in ids for x in doc['evidence']):errors.append('orphan verification evidence')
    if any(x['from'] not in owners or x['to'] not in owners for x in doc['interfaces']):errors.append('unknown interface endpoint')
    if {e['requirement'] for e in doc['evidence']}!=set(ids):errors.append('requirements lack evidence records')
    for filename,key,col in [('requirements.csv','requirements','id'),('interfaces.csv','interfaces','id'),('evidence-register.csv','evidence','requirement')]:
        if [x[col] for x in records(filename)] != [x[col] for x in doc[key]]:
            errors.append('CSV/model mismatch: '+filename)
    return errors

def gate(doc, hypothetical_canary_min=9):
    incident_minutes=sum(float(x['duration_min']) for x in records('incident-log.csv'))
    current=time_budget(doc['assumptions']['days'],doc['assumptions']['availability_slo'],incident_minutes)
    statuses=evidence_status(doc)
    blockers=[k+': '+s for k,s in statuses.items() if s != 'CURRENT_SYNTHETIC_PASS']
    if hypothetical_canary_min>current['remaining_min']+1e-9:
        blockers.append('projected canary downtime exceeds remaining time budget')
    return {'budget':current,'statuses':statuses,'blockers':blockers,'release':'NO_GO' if blockers else 'REVIEW_REQUIRED'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    opts=parser.parse_args()
    doc=model()
    problems=audit(doc)
    result={'baseline':doc['baseline'],'structural_issues':problems,
            'queue_baseline_p95_ms':queue_p95_ms(10,18),
            'queue_candidate_p95_ms':queue_p95_ms(10,20),
            'ideal_series_availability':series_availability(common_cause=0),
            'availability_with_common_cause':series_availability(),
            'expected_attempts_two_tries_p06':retry_attempts(0.06),
            **gate(doc)}
    if opts.json:print(json.dumps(result,indent=2))
    else:
        print('Synthetic teaching case:',result['baseline'])
        print('M/M/1 proxy p95 (baseline / candidate): %.2f / %.2f ms'%(result['queue_baseline_p95_ms'],result['queue_candidate_p95_ms']))
        print('30-day error budget: %.1f allowed, %.1f remaining min'%(result['budget']['permitted_min'],result['budget']['remaining_min']))
        print('Evidence:',result['statuses'])
        print('Release decision:',result['release'])
        for b in result['blockers']:print(' -',b)
    if problems:raise SystemExit('Structural case defects: '+str(problems))
    return result

if __name__=='__main__':main()
