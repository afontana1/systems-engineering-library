#!/usr/bin/env python3
"""NS-CE4.1 reproducible connected-evidence instructional calculations.

All input data are synthetic, all decision thresholds are examples. A PASS
from a local model is *never* an authorization to deploy.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'data/ns-evidence4-case.json'
RESULT = ROOT / 'outputs/ns-evidence4-results.json'


def ensure_number(x, label, minimum=0, upper=None):
    if isinstance(x, bool) or not isinstance(x, (int,float)) or not math.isfinite(x):
        raise ValueError(f'{label} must be finite numeric')
    if x < minimum or (upper is not None and x > upper):
        raise ValueError(f'{label} outside permitted range')
    return x


def load(path=INPUT):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    if data.get('case_id') != 'NS-CE4.1':raise ValueError('unexpected case identifier')
    if not isinstance(data.get('revision'),str) or not data['revision']:raise ValueError('missing revision')
    cs=data['constraints']
    for k in ('min_peak_trips','max_p90_wait_minutes','max_capex_million'):
        ensure_number(cs[k],k,0)
    ids=set()
    if not data['alternatives']:raise ValueError('empty alternatives')
    for row in data['alternatives']:
        if row['id'] in ids:raise ValueError('duplicate alternative id')
        ids.add(row['id'])
        for k in ('capex_million','nominal_peak_trips','nominal_p90_wait_minutes',
                  'storm_peak_trips','storm_p90_wait_minutes'):
            ensure_number(row[k],k)
    interface=data['interface']
    if not interface['events']:raise ValueError('missing interface test sequence')
    ensure_number(interface['max_age_seconds'],'max_age_seconds',0)
    for evt in interface['events']:
        if isinstance(evt['sequence'],bool) or not isinstance(evt['sequence'],int) or evt['sequence']<1:
            raise ValueError('invalid sequence id')
        ensure_number(evt['timestamp_seconds'],'timestamp_seconds')
        ensure_number(evt['observed_at_seconds'],'observed_at_seconds')
        if evt['observed_at_seconds']<evt['timestamp_seconds']:
            raise ValueError('received before timestamp')
    if not isinstance(data['trial_groups'],dict) or not data['trial_groups']:
        raise ValueError('empty trial groups')
    for g,counts in data['trial_groups'].items():
        for k in ('timely','late','unserved'):
            val=counts[k]
            if isinstance(val,bool) or not isinstance(val,int) or val<0:raise ValueError('invalid count '+g+'/'+k)
        if sum(counts.values())<1:raise ValueError('empty trial group '+g)
    a=data['acceptance']
    for k in ('min_total_timely_fraction','min_accessible_timely_fraction',
              'max_zero_failure_probability','alpha'):
        ensure_number(a[k],k,0,1)
    if not 0<a['alpha']<1:raise ValueError('alpha must be between 0 and 1')
    if isinstance(a['zero_failure_trials'],bool) or not isinstance(a['zero_failure_trials'],int) or a['zero_failure_trials']<1:
        raise ValueError('invalid number of trials')
    sim=data['simulation']
    for k in ('baseline_arrivals_per_hour','service_per_hour','stress_arrivals_per_hour',
              't_critical_df5_95_two_sided'):
        ensure_number(sim[k],k)
    for k in ('paired_baseline_wait_minutes','paired_treatment_wait_minutes'):
        if not isinstance(sim[k],list) or len(sim[k])<2:raise ValueError('too few paired observations')
        for v in sim[k]:ensure_number(v,k)
    if len(sim['paired_baseline_wait_minutes'])!=len(sim['paired_treatment_wait_minutes']):
        raise ValueError('unpaired scenarios')
    if len(sim['paired_baseline_wait_minutes'])!=6:
        raise ValueError('supplied t-critical value applies only to six pairs (df=5)')
    seen=set()
    if not data['evidence']:raise ValueError('no evidence paths')
    for e in data['evidence']:
        if e['claim'] in seen:raise ValueError('duplicate claim')
        seen.add(e['claim'])
        if not all(isinstance(e.get(k),str) and e[k] for k in (
                'claim','requirement','artifact','revision','status','scope','required_scope','payload','sha256')):
            raise ValueError('incomplete evidence row')
        if e['status'] not in ('PASS','FAIL','INCONCLUSIVE'):
            raise ValueError('invalid evidence status')
        if len(e['sha256'])!=64:raise ValueError('digest syntax')
    if not data['permissions'] or not all(isinstance(v,bool) for v in data['permissions'].values()):
        raise ValueError('permissions must be explicit booleans')
    for k,v in data['enterprise'].items():ensure_number(v,k)
    return data


def candidate_screen(data):
    c=data['constraints']
    outcome=[]
    for a in data['alternatives']:
        cost=a['capex_million']<=c['max_capex_million']
        nominal=a['nominal_peak_trips']>=c['min_peak_trips'] and a['nominal_p90_wait_minutes']<=c['max_p90_wait_minutes']
        storm=a['storm_peak_trips']>=c['min_peak_trips'] and a['storm_p90_wait_minutes']<=c['max_p90_wait_minutes']
        outcome.append({'id':a['id'],'cost_pass':cost,'nominal_service_pass':nominal,
                        'storm_service_pass':storm,'robust_screen_pass':cost and nominal and storm})
    return outcome


def interface_screen(data):
    item=data['interface'];violations=[];last=0
    for i,e in enumerate(item['events'],start=1):
        n=e['sequence']
        if n<=last:violations.append({'event':i,'type':'duplicate_or_reordered','sequence':n})
        elif n!=last+1:violations.append({'event':i,'type':'gap','sequence':n,'expected':last+1})
        last=max(last,n)
        age=e['observed_at_seconds']-e['timestamp_seconds']
        if age>item['max_age_seconds']:
            violations.append({'event':i,'type':'stale','age_seconds':round(age,6)})
    if item['contract_revision']!=item['observed_revision']:
        violations.append({'event':0,'type':'revision_mismatch'})
    return {'contract_pass':not violations,'violations':violations,
            'observed_revision':item['observed_revision'],'contract_revision':item['contract_revision']}


def trial_screen(data):
    groups=data['trial_groups'];a=data['acceptance']
    n=sum(sum(g.values()) for g in groups.values())
    timely=sum(g['timely'] for g in groups.values())
    served=sum(g['timely']+g['late'] for g in groups.values())
    acc=groups['accessible'];nacc=sum(acc.values())
    upper=1-a['alpha']**(1/a['zero_failure_trials'])
    return {'requests':n,'timely':timely,'served':served,'unserved':n-served,
            'population_timely_fraction':timely/n,
            'served_only_timely_fraction':timely/served if served else None,
            'accessible_timely_fraction':acc['timely']/nacc,
            'zero_failure_upper_exact_iid':upper,
            'timeliness_screen_pass':(timely/n>=a['min_total_timely_fraction'] and
                                      acc['timely']/nacc>=a['min_accessible_timely_fraction']),
            'zero_failure_screen_pass':upper<=a['max_zero_failure_probability']}


def simulation_screen(data):
    p=data['simulation'];lam=p['baseline_arrivals_per_hour'];mu=p['service_per_hour']
    if mu<=0:raise ValueError('nonpositive service rate')
    if lam>=mu:raise ValueError('nominal queue unstable: no stationary M/M/1 mean')
    before=p['paired_baseline_wait_minutes'];after=p['paired_treatment_wait_minutes']
    diffs=[x-y for x,y in zip(before,after)];n=len(diffs);mean=sum(diffs)/n
    s=math.sqrt(sum((d-mean)**2 for d in diffs)/(n-1))
    half=p['t_critical_df5_95_two_sided']*s/math.sqrt(n)
    return {'nominal_utilization':lam/mu,'nominal_mm1_total_minutes':60/(mu-lam),
            'stress_stationary_mean_defined':p['stress_arrivals_per_hour']<mu,
            'paired_reduction_minutes':diffs,'paired_mean_reduction_minutes':mean,
            'paired_sample_sd_minutes':s,'illustrative_t_interval_minutes':[mean-half,mean+half],
            'claim_of_validation':False}


def evidence_screen(data):
    outcomes=[]
    for e in data['evidence']:
        defects=[]
        if hashlib.sha256(e['payload'].encode('utf-8')).hexdigest()!=e['sha256']:
            defects.append('digest_mismatch')
        if e['revision']!=data['revision']: defects.append('revision_stale')
        if e['scope']!=e['required_scope']: defects.append('scope_mismatch')
        if e['status']!='PASS':defects.append('does_not_pass')
        outcomes.append({'claim':e['claim'],'requirement':e['requirement'],
                         'artifact':e['artifact'],'actionable':not defects,'defects':defects})
    return {'paths':outcomes,'structural_coverage':1.0,
            'actionable_coverage':sum(e['actionable'] for e in outcomes)/len(outcomes),
            'all_permissions_explicitly_granted':all(data['permissions'].values())}


def enterprise_screen(data):
    e=data['enterprise']
    effect=(e['pilot_post_wait_minutes']-e['pilot_pre_wait_minutes'])-(e['comparison_post_wait_minutes']-e['comparison_pre_wait_minutes'])
    accessible=(e['pilot_access_post_minutes']-e['pilot_access_pre_minutes'])-(e['comparison_access_post_minutes']-e['comparison_access_pre_minutes'])
    return {'naive_pilot_before_after_minutes':e['pilot_post_wait_minutes']-e['pilot_pre_wait_minutes'],
            'difference_in_differences_minutes':effect,'accessible_difference_in_differences_minutes':accessible,
            'parallel_trends_established':False,'causal_claim_identified':False}


def run(data):
    decisions=candidate_screen(data);interface=interface_screen(data);trial=trial_screen(data)
    sim=simulation_screen(data);evidence=evidence_screen(data);enterprise=enterprise_screen(data)
    ready=any(x['robust_screen_pass'] for x in decisions) and interface['contract_pass'] and trial['timeliness_screen_pass'] and trial['zero_failure_screen_pass'] and sim['stress_stationary_mean_defined'] and evidence['actionable_coverage']==1 and evidence['all_permissions_explicitly_granted']
    # Explicitly never equate such a hypothetical screen with operational approval.
    return {'case_id':data['case_id'],'revision':data['revision'],'concepts':decisions,
            'interfaces':interface,'testing':trial,'simulation':sim,'provenance':evidence,
            'enterprise':enterprise,'integrated_technical_screen_pass':ready,
            'deployment_disposition':'HOLD — synthetic evidence only; independent validation, approvals and stakeholder review required'}


def main():
    d=load();out=run(d)
    out['input_sha256']=hashlib.sha256(INPUT.read_bytes()).hexdigest()
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('case_id','integrated_technical_screen_pass','deployment_disposition')},indent=2))

if __name__=='__main__':main()
