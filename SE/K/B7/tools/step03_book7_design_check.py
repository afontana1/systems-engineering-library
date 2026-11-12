#!/usr/bin/env python3
"""NS-DI7.1 educational design review; synthetic assumptions, not operational qualification."""
from __future__ import annotations
import csv,json,math
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'case'

def model():return json.loads((BASE/'model-baseline.json').read_text())
def records(name):
 with (BASE/name).open(newline='') as f:return list(csv.DictReader(f))

def schedule(tasks):
 finish={};paths={}
 for task in tasks:
  pred=task['predecessors']
  if any(p not in finish for p in pred):raise ValueError('Non-topological or missing predecessor')
  before=max(pred,key=lambda p:finish[p]) if pred else None
  start=finish[before] if before else 0
  finish[task['id']]=start+task['duration_w']
  paths[task['id']]=(paths[before] if before else [])+[task['id']]
 final=max(finish,key=lambda p:finish[p]);return {'finish_weeks':finish,'total_weeks':finish[final],'critical_path':paths[final]}

def audit(d=None):
 d=d or model();problems=[];req=records('requirements.csv');ev=records('evidence-register.csv')
 ids=[r['id'] for r in req]; seen=[r['requirement_id'] for r in ev]
 if len(ids)!=len(set(ids)):problems.append('duplicate requirement IDs')
 if len(seen)!=len(set(seen)):problems.append('duplicate evidence requirement IDs')
 for r in ev:
  if r['requirement_id'] not in ids:problems.append('unknown requirement '+r['requirement_id'])
 if set(ids)-set(seen):problems.append('requirements without evidence '+str(sorted(set(ids)-set(seen))))
 if sum(float(v) for v in d['timing']['degraded_ms'].values())!=sum(float(r['latency_degraded_ms']) for r in records('interfaces.csv')):problems.append('interface timing drift')
 for a in records('allocation.csv'):
  for rid in a['requirement_ids'].split(';'):
   if rid not in ids:problems.append('invalid allocated requirement '+rid)
 for row in ev:
  if row['status']=='CURRENT_LAB_TEST' and row['evidence_baseline']!=d['baseline']:
   problems.append('mislabelled current evidence '+row['requirement_id'])
 return problems

def factorial():
 rows=records('doe-synthetic.csv');cells={}
 for row in rows:
  key=(row['gateway'],row['dispatch']);cells.setdefault(key,[]).append(float(row['response_ms']))
 if set(cells)!={('standard','serial'),('fast','serial'),('standard','parallel'),('fast','parallel')}:raise ValueError('incomplete 2x2 factorial')
 means={k:sum(v)/len(v) for k,v in cells.items()}
 a=means['standard','serial'];b=means['fast','serial'];c=means['standard','parallel'];d=means['fast','parallel']
 return {'cell_means_ms':{f'{k[0]}_{k[1]}':v for k,v in means.items()},'gateway_main_ms':((b+d)-(a+c))/2,'dispatch_main_ms':((c+d)-(a+b))/2,'interaction_difference_ms':(d-c)-(b-a),'synthetic_tail_probability_at_450ms_if_gaussian':0.5*math.erfc((450-d)/(20*math.sqrt(2)))}

def report(d=None):
 d=d or model();t=d['timing'];r=d['reliability'];s=d['support'];z=d['safety']
 nominal=sum(t['nominal_ms'].values());degraded=sum(t['degraded_ms'].values());deadline=t['deadline_ms']
 variant={'original':degraded,'fast_gateway':degraded-t['redesign_savings_ms']['gateway_fast'], 'parallel_dispatch':degraded-t['redesign_savings_ms']['dispatch_parallel'],'combined':degraded-sum(t['redesign_savings_ms'].values())}
 years=s['years'];rate=s['discount_rate'];annuity=sum((1+rate)**(-n) for n in range(1,years+1))
 ev=records('evidence-register.csv'); evidence={x['requirement_id']:('STALE' if x['evidence_baseline']!=d['baseline'] else x['status']) for x in ev}
 pure_mission=math.exp(-r['independent_failure_rate_per_h']*r['mission_h'])
 shared_mission=math.exp(-(r['independent_failure_rate_per_h']+r['shared_failure_rate_per_h'])*r['mission_h'])
 operational_availability=r['mtbf_h']/(r['mtbf_h']+r['mttr_h']+r['mean_logistics_delay_h'])
 return {
  'nominal_latency_ms':nominal,'degraded_latency_ms':degraded,'latency_variants_ms':variant,'minimum_reserve_ms':deadline*t['minimum_design_reserve_fraction'],
  'combined_margin_ms':deadline-variant['combined'],
  'energy_total_kwh':sum(v for k,v in d['energy'].items() if k!='budget_kwh_per_shift'),
  'energy_margin_kwh':d['energy']['budget_kwh_per_shift']-sum(v for k,v in d['energy'].items() if k!='budget_kwh_per_shift'),
  'mission_reliability_independent_only':pure_mission,'mission_reliability_including_shared_rate':shared_mission,
  'inherent_availability':r['mtbf_h']/(r['mtbf_h']+r['mttr_h']),'operational_availability_proxy':operational_availability,
  'safety_top_event_per_demand':z['common_cause_per_demand']+(1-z['common_cause_per_demand'])*z['brake_failure_per_demand']*z['interlock_failure_per_demand'],
  'expected_spares_restoration_hours':s['spares_fill_probability']*s['local_restore_h']+(1-s['spares_fill_probability'])*s['shortage_restore_h'],
  'discounted_lifecycle_cost_musd':s['initial_musd']+(s['annual_operation_musd']+s['annual_support_musd'])*annuity+s['decommission_musd']/(1+rate)**years,
  'schedule':schedule(d['schedule']['tasks']),'factorial':factorial(),
  'evidence':evidence,'readiness':'HOLD' if any(x!='CURRENT_LAB_TEST' for x in evidence.values()) or shared_mission<0.98 or operational_availability<0.99 else 'REVIEW_REQUIRED',
  'structural_errors':audit(d),
 }
if __name__=='__main__':print(json.dumps(report(),indent=2))
