#!/usr/bin/env python3
"""Synthetic change-to-evidence process screening model for Book 17.

Purpose: teach flow accounting, priority safeguards, uncertainty, and controlled
policy comparisons. NOT validated observations, ISO/CMMI appraisal, or evidence
that a real organization can change its process safely.
"""
from __future__ import annotations
import argparse
import copy
import csv
import heapq
import json
import math
import random
import statistics
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
STAGES=('analysis','evidence','review','implementation','verification')
BASE_DAYS={'analysis':2.15,'evidence':1.35,'review':0.65,'implementation':2.6,'verification':1.25}
CLASSES={'routine':1.0,'supplier':1.55,'safety_access':1.85,'cyber':1.65}


def load():
    return json.loads((HERE/'case/controlled-inputs.json').read_text(encoding='utf-8'))


def validate(cfg):
    if cfg.get('case_id')!='NS-PI17.1' or cfg.get('intended_use')!='instructional-policy-screen':
        raise ValueError('Missing case identity or non-permitted use')
    g=cfg.get('generation',{})
    if not isinstance(g.get('seed'),int) or type(g.get('n')) is not int or g['n']<10 or g['n']>500:
        raise ValueError('Invalid generation definition')
    if not math.isfinite(g.get('mean_arrival_days',float('nan'))) or g['mean_arrival_days']<=0:
        raise ValueError('Nonpositive arrival interval')
    if not isinstance(cfg.get('policies'),list) or len(cfg['policies'])<2:
        raise ValueError('Missing policy alternatives')
    names=set()
    for p in cfg['policies']:
        if not p.get('name') or p['name'] in names:raise ValueError('Duplicate or blank policy')
        names.add(p['name'])
        if set(p.get('workers',{}))!=set(STAGES):raise ValueError('Unknown/omitted service stage')
        if any(type(w) is not int or w<1 or w>20 for w in p['workers'].values()):raise ValueError('Invalid staffing')
        for f in ('cadence_days','service_factor','rework_probability','false_positive_probability'):
            v=p.get(f)
            if not isinstance(v,(int,float)) or not math.isfinite(v):raise ValueError('Invalid parameter '+f)
        if not 0<=p['rework_probability']<=.8 or not 0<=p['false_positive_probability']<=.8:
            raise ValueError('Invalid probabilities')
        if p['cadence_days']<=0 or p['service_factor']<=0:raise ValueError('Invalid service or meeting cadence')
        if type(p.get('max_rework')) is not int or not 0<=p['max_rework']<=5:
            raise ValueError('Invalid rework cap')
    return True


def make_requests(cfg,seed=None):
    validate(cfg)
    g=cfg['generation'];rng=random.Random(g['seed'] if seed is None else seed)
    n=g['n'];t=0.0;items=[]
    for i in range(1,n+1):
        t+=rng.expovariate(1/g['mean_arrival_days'])
        cl=rng.choices(tuple(CLASSES),weights=(.49,.21,.18,.12),k=1)[0]
        # A common latent complexity value makes service stages correlated.
        complexity=rng.triangular(.7,1.8,1.0)
        items.append({'id':f'PI17-{i:03}','arrival_day':round(t,6),'class':cl,
                      'complexity':round(complexity,6),'critical':cl in ('safety_access','cyber'),
                      'evidence_required':cl in ('safety_access','cyber')})
    return items


def quantile(values,q):
    if not values or not 0<=q<=1:raise ValueError('Nonempty sample and probability required')
    data=sorted(values);k=(len(data)-1)*q;i=math.floor(k)
    return data[i]+(data[min(i+1,len(data)-1)]-data[i])*(k-i)


def simulate(cfg,policy,requests,seed=1717, stress_multiplier=1.0):
    if not math.isfinite(stress_multiplier) or stress_multiplier<=0:raise ValueError('Invalid stress')
    for x in requests:
        if x.get('class') not in CLASSES or not isinstance(x.get('complexity'),(int,float)) or not math.isfinite(x['complexity']) or x['complexity']<=0:
            raise ValueError('Invalid request class or complexity')
        if not x.get('id') or not isinstance(x.get('arrival_day'),(int,float)) or not math.isfinite(x['arrival_day']) or x['arrival_day']<0:
            raise ValueError('Invalid identifier or arrival time')
        required=x['class'] in ('safety_access','cyber')
        if type(x.get('evidence_required')) is not bool or x['evidence_required']!=required or x.get('critical')!=required:
            raise ValueError('Criticality/evidence obligation mismatch')
    if len({x['id'] for x in requests})!=len(requests):raise ValueError('Duplicate request identifier')
    rng=random.Random(seed)
    p=next((p for p in cfg['policies'] if p['name']==policy),None)
    if p is None:raise ValueError('Unknown policy')
    sequence=0;calendar=[];queues={s:[] for s in STAGES};working={s:0 for s in STAGES}
    counters={x['id']:{'request':x,'starts':{},'wait':{},'rework':0,'false_alarms':0,'done':False,'held':False,'finish':None} for x in requests}
    events=[]
    def push(t,kind,stage,key):
        nonlocal sequence
        sequence+=1;heapq.heappush(calendar,(t,sequence,kind,stage,key))
    for x in requests:push(x['arrival_day']*stress_multiplier,'arrive','analysis',x['id'])
    def dispatch(stage,now):
        capacity=p['workers'][stage]
        while queues[stage] and working[stage]<capacity:
            key,queued_at=queues[stage].pop(0);item=counters[key];req=item['request']
            start=now
            if stage=='review':
                cadence=p['cadence_days']
                start=math.ceil((now-1e-10)/cadence)*cadence
            # bounded, non-Gaussian service time with common case complexity
            factor=rng.triangular(.75,1.35,1)
            duration=BASE_DAYS[stage]*CLASSES[req['class']]*req['complexity']*factor
            duration*=p['service_factor'] if stage in ('analysis','evidence') else 1.0
            if stage=='evidence' and item['false_alarms']:
                duration+=.25*item['false_alarms']
            working[stage]+=1
            item['wait'][stage]=item['wait'].get(stage,0.0)+start-queued_at
            item['starts'][stage]=item['starts'].get(stage,0)+1
            push(start+duration,'done',stage,key)
            events.append({'request':key,'stage':stage,'queued_at_day':round(queued_at,5),
                           'started_at_day':round(start,5),'ended_at_day':round(start+duration,5),
                           'visit':item['starts'][stage]})
    while calendar:
        now,_,kind,stage,key=heapq.heappop(calendar)
        row=counters[key]
        if kind=='arrive':
            queues[stage].append((key,now));dispatch(stage,now)
            continue
        working[stage]-=1
        if working[stage]<0:raise ArithmeticError('Negative resource occupancy')
        if stage=='review':
            # review gate returns incomplete work for revision; bounded to avoid
            # a pathological nontermination and report any cap as unresolved.
            risk=.08 if row['request']['critical'] else 0.0
            revisit=min(.95,p['rework_probability']+risk)
            if rng.random()<revisit:
                if row['rework']<p['max_rework']:
                    row['rework']+=1
                    push(now,'arrive','analysis',key)
                else:
                    row['held']=True;row['finish']=now
            else:push(now,'arrive','implementation',key)
        elif stage=='evidence':
            # False positives create work but no assertion of a safety escape.
            if rng.random()<p['false_positive_probability']:
                row['false_alarms']+=1
            push(now,'arrive','review',key)
        elif stage=='verification':
            # Critical cases cannot be released if they skipped their gate.
            if row['request']['evidence_required'] and not row['starts'].get('evidence'):
                row['held']=True
            else:row['done']=True
            row['finish']=now
        else:
            dest=STAGES[STAGES.index(stage)+1]
            push(now,'arrive',dest,key)
        dispatch(stage,now)
    if any(not (r['done'] or r['held']) for r in counters.values()):raise ArithmeticError('Lost work')
    if any(working.values()) or any(queues.values()):raise ArithmeticError('Unbalanced system')
    all_leads=[r['finish']-r['request']['arrival_day']*stress_multiplier for r in counters.values()]
    closed=[r for r in counters.values() if r['done']]
    closed_leads=[r['finish']-r['request']['arrival_day']*stress_multiplier for r in closed]
    if any(v<0 for v in all_leads):raise ArithmeticError('Negative time')
    after_last=max(r['finish'] for r in counters.values()) if counters else 0
    total_wait=sum(sum(r['wait'].values()) for r in counters.values())
    rows=[]
    for key,r in counters.items():
        rows.append({'request':key,'class':r['request']['class'],
                     'arrival_day':round(r['request']['arrival_day']*stress_multiplier,4),
                     'finish_day':round(r['finish'],4),
                     'elapsed_days':round(r['finish']-r['request']['arrival_day']*stress_multiplier,4),
                     'queue_days':round(sum(r['wait'].values()),4),'rework':r['rework'],
                     'false_alarms':r['false_alarms'],'outcome':'released' if r['done'] else 'held',
                     'evidence_visits':r['starts'].get('evidence',0),'verification_visits':r['starts'].get('verification',0)})
    result={'policy':policy,'input_count':len(requests),'released':len(closed),
            'held':len(requests)-len(closed),'reworked_cases':sum(r['rework']>0 for r in counters.values()),
            'rework_loops':sum(r['rework'] for r in counters.values()),
            'false_alarms':sum(r['false_alarms'] for r in counters.values()),
            'lead_mean_all_days':round(statistics.mean(all_leads),4),
            'lead_median_all_days':round(quantile(all_leads,.5),4),
            'lead_p90_all_days':round(quantile(all_leads,.9),4),
            'lead_mean_released_days':round(statistics.mean(closed_leads),4) if closed else None,
            'queue_time_total_days':round(total_wait,4),
            'time_last_case_day':round(after_last,4),
            'critical_released_without_evidence':sum(r['done'] and r['request']['evidence_required'] and not r['starts'].get('evidence') for r in counters.values())}
    return result,rows,events


def experiment(cfg,seed=1717,replications=24):
    validate(cfg)
    if type(replications) is not int or replications<2 or replications>1000:
        raise ValueError('Invalid replication count')
    base=make_requests(cfg)
    raw=[]
    for rep in range(replications):
        for p in cfg['policies']:
            # Common case mix, independent stochastic service/rework stream for
            # each policy; same replicate seed enables matched index comparison,
            # but not common-random-number event correspondence.
            out,_,_=simulate(cfg,p['name'],base,seed=seed+rep)
            raw.append({'replicate':rep,'policy':p['name'],**out})
    summary=[]
    for p in cfg['policies']:
        d=[r for r in raw if r['policy']==p['name']]
        for metric in ('lead_mean_all_days','lead_p90_all_days','held','reworked_cases'):
            a=[float(x[metric]) for x in d]
            mean=statistics.mean(a)
            se=statistics.stdev(a)/math.sqrt(len(a))
            summary.append({'policy':p['name'],'metric':metric,'replications':len(a),
                            'mean':round(mean,4),'sd':round(statistics.stdev(a),4),
                            'normal_approx_95_lower':round(mean-1.96*se,4),
                            'normal_approx_95_upper':round(mean+1.96*se,4)})
    return raw,summary


def audit_events(rows,required_before='SafetyReview',approval='Approve'):
    """Basic conformance to explicit ordering: one Submit, review before approval.

    This is NOT a BPMN conformance engine or a complete safety assessment.
    """
    cases={}
    for r in rows:
        if not r.get('case') or not r.get('activity'):
            raise ValueError('Missing event identifier/activity')
        try:day=float(r['day'])
        except (ValueError,TypeError,KeyError):raise ValueError('Malformed event timestamp')
        if not math.isfinite(day) or day<0:raise ValueError('Invalid event day')
        cases.setdefault(r['case'],[]).append((day,r['activity']))
    violations=[]
    for key,events in sorted(cases.items()):
        earliest={}
        for day,activity in events:earliest.setdefault(activity,day)
        if sum(a=='Submit' for d,a in events)!=1:
            violations.append({'case':key,'rule':'EXACTLY_ONE_SUBMISSION'})
        if approval in earliest and (required_before not in earliest or earliest[required_before]>=earliest[approval]):
            violations.append({'case':key,'rule':'REVIEW_BEFORE_APPROVAL'})
        if approval in earliest and earliest.get('Submit',math.inf)>earliest[approval]:
            violations.append({'case':key,'rule':'SUBMISSION_BEFORE_APPROVAL'})
    return violations


def factorial(cfg,requests,replications=24):
    """Two-factor demonstration, holding all baseline resources fixed.

    Shorter board cadence is not a stand-alone causal field effect; service
    quality and staffing may respond in a real process.
    """
    rows=[]
    for cadence in (7,2):
        for rework in (.27,.15):
            alt=copy.deepcopy(cfg)
            alt['policies']=[copy.deepcopy(next(p for p in cfg['policies'] if p['name']=='baseline')),
                             copy.deepcopy(next(p for p in cfg['policies'] if p['name']=='reviewer-only'))]
            p=alt['policies'][0];p['name']='factorial';p['cadence_days']=cadence;p['rework_probability']=rework
            for rep in range(replications):
                out,_,_=simulate(alt,'factorial',requests,seed=1717+rep)
                rows.append({'cadence_days':cadence,'rework_probability':rework,'replicate':rep,
                             'mean_lead_days':out['lead_mean_all_days'],'p90_lead_days':out['lead_p90_all_days'],
                             'held':out['held']})
    return rows


def pilot_difference_in_differences():
    # Four wholly invented group-period aggregate means: not actual pilot data.
    records=[{'group':'intervention','period':'before','mean_days':38.0,'n':30},
             {'group':'intervention','period':'after','mean_days':25.0,'n':30},
             {'group':'comparison','period':'before','mean_days':36.0,'n':30},
             {'group':'comparison','period':'after','mean_days':33.0,'n':30}]
    delta=(25-38)-(33-36)
    return records,delta


def write_csv(path,rows):
    if not rows:return
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def build(cfg=None):
    cfg=cfg or load();validate(cfg);case=HERE/'case';case.mkdir(exist_ok=True)
    items=make_requests(cfg)
    write_csv(case/'synthetic-requests.csv',items)
    outputs=[]
    for p in cfg['policies']:
        result,rows,events=simulate(cfg,p['name'],items)
        outputs.append(result)
        if p['name']=='baseline':
            write_csv(case/'baseline-case-outcomes.csv',rows)
            write_csv(case/'baseline-event-log.csv',events)
    write_csv(case/'single-run-policy-results.csv',outputs)
    raw,summary=experiment(cfg)
    write_csv(case/'replication-results.csv',raw)
    write_csv(case/'replication-summary.csv',summary)
    write_csv(case/'factorial-results.csv',factorial(cfg,items))
    stresses=[]
    for p in cfg['policies']:
        out,_,_=simulate(cfg,p['name'],items,stress_multiplier=.65)
        stresses.append({'scenario':'compressed-arrivals-65pct',**out})
    write_csv(case/'arrival-stress-results.csv',stresses)
    pilot,delta=pilot_difference_in_differences()
    write_csv(case/'illustrative-pilot-groups.csv',pilot)
    source_log=HERE.parent/'P4-LAB/data/process-events.csv'
    with source_log.open(newline='',encoding='utf8') as f:violations=audit_events(list(csv.DictReader(f)))
    write_csv(case/'shared-lab-event-violations.csv',violations)
    print(json.dumps(outputs,indent=2))
    return outputs


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--build',action='store_true');args=parser.parse_args()
    build()
