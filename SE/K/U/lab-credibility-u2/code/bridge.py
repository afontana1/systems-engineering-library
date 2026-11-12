"""NS-U2.1: independently replay two *different* synthetic labs; audit their claim boundaries.

Python 3.10+ standard library only. v11 and v12 are executed in separate subprocesses,
preventing their similarly named `src` packages from colliding. No operational use.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]  # SE/K/U
THIS = Path(__file__).resolve().parents[1]
SOURCE = {
 'v11': ROOT/'integrated-lab',
 'v12': ROOT/'advanced-lab',
}
FILES = {
 'v11': ['data/config.json','data/requests.csv','data/requirements.csv',
         'data/verification-matrix.csv','data/hazards.csv','src/northstar.py',
         'src/assurance.py','src/run_lab.py'],
 'v12': ['data/scenarios.json','data/requests.csv','data/requirements-v12.csv',
         'data/verification-plan.csv','models/architecture.json','src/architecture.py',
         'src/event_sim.py','src/evidence.py','src/run_advanced.py'],
}

def sha(b): return hashlib.sha256(b).hexdigest()

def replay(lab: str, replications=120):
 if lab not in SOURCE: raise ValueError('unknown lab')
 src=SOURCE[lab]
 with tempfile.TemporaryDirectory(prefix='ns-u2-') as d:
  # Legacy runner invocation, intentionally unmodified; all generated outputs stay outside source tree.
  script=('from src.run_lab import run; run(%r)' if lab=='v11'
          else f'from src.run_advanced import run; run(%r,replications={replications})') % d
  p=subprocess.run([sys.executable,'-c',script],cwd=src,capture_output=True,text=True,timeout=40)
  if p.returncode: raise RuntimeError(lab+': '+p.stderr[-1300:])
  out=Path(d)
  result_file='results.json' if lab=='v11' else 'scenario-results.json'
  obj=json.loads((out/result_file).read_text(encoding='utf-8'))
  outputs={f.name:sha(f.read_bytes()) for f in out.iterdir() if f.is_file()}
  return obj,outputs

def audit_v11(res):
 errors=[]; a=res['baseline']; f=res['degraded_one_vehicle']
 for name,r in [('fixed',a),('one_vehicle',f)]:
  if r['served']+r['unserved']!=r['unique_requests']: errors.append(name+': request conservation')
  if r['input_events']!=r['unique_requests']+r['duplicates_ignored']:errors.append(name+': duplication accounting')
  for x in r['assignments']:
   if x['status']=='completed':
    if (x['start_min']<x['arrival_min'] or x['finish_min']>r['config']['end_min']+1e-9):
     errors.append(name+': invalid completed record')
    if abs((x['finish_min']-x['start_min'])-r['config']['trip_min'])>1e-6 or abs(x['wait_min']-(x['start_min']-x['arrival_min']))>1e-6:
     errors.append(name+': trip duration or wait mismatch')
  audit='\n'.join(f"{x['request_id']}:{x['status']}:{x['vehicle']}:{x['start_min']}" for x in r['assignments'])
  if sha(audit.encode('utf-8'))!=r['audit_sha256']:
   errors.append(name+': audit hash mismatch')
  per={}
  for x in r['assignments']:
   if x['status']=='completed':per.setdefault(x['vehicle'],[]).append((x['start_min'],x['finish_min']))
  for intervals in per.values():
   if any(y[0]<x[1]-1e-9 for x,y in zip(sorted(intervals),sorted(intervals)[1:])):
    errors.append(name+': overlapping assignments')
 if not res['traceability']['link_integrity_pass']:errors.append('v11 trace links do not resolve')
 return errors

def audit_v12(res):
 errors=[]
 for name,r in res['scenarios'].items():
  if r['unique_requests']!=r['completed']+r['lost_messages']+r['unserved_capacity']:
   errors.append(name+': request conservation')
  if r['duplicates_ignored']+r['unique_requests']+r['rejected_conflicts']!=r['input_events']:
   errors.append(name+': raw event conservation')
  if r['completed']!=sum(x['status']=='completed' for x in r['records']):errors.append(name+': completed ledger count')
  if r['lost_messages']!=sum(x['status']=='unobserved_message_loss' for x in r['records']):errors.append(name+': loss ledger count')
  if r['unserved_capacity']!=sum(x['status']=='unserved_capacity' for x in r['records']):errors.append(name+': unserved ledger count')
  if len({x['request_id'] for x in r['records']})!=r['unique_requests']:errors.append(name+': repeated request')
  ledger=json.dumps(r['records'],sort_keys=True,separators=(',',':'))
  if sha(ledger.encode('utf-8'))!=r['evidence_sha256']:
   errors.append(name+': ledger hash mismatch')
  per={};s=r['scenario']
  for x in r['records']:
   if x['status']!='completed':continue
   if not (x['arrival_min'] <= x['received_min'] <= x['start_min'] < x['finish_min'] <= s['horizon_min']+1e-9):
    errors.append(name+': invalid event clock')
   if abs(x['wait_min']-(x['start_min']-x['arrival_min']))>1e-6 or abs((x['finish_min']-x['start_min'])-s['trip_min'])>1e-6:
    errors.append(name+': duration or wait mismatch')
   per.setdefault(x['vehicle'],[]).append((x['start_min'],x['finish_min']))
   blocks=[(s['telemetry_block_start'],s['telemetry_block_end'])]
   if x['vehicle']==f"V{s['outage_vehicle']:02d}":blocks.append((s['outage_start'],s['outage_end']))
   for lo,hi in blocks:
    if lo<hi and max(lo,x['start_min']) < min(hi,x['finish_min'])-1e-9:
     errors.append(name+': assignment intersects fault interval')
  if any(y[0]<x[1]-1e-9 for t in per.values() for x,y in zip(sorted(t),sorted(t)[1:])):
   errors.append(name+': overlapping resource')
 if not res['trace']['pass_links']:errors.append('v12 trace links do not resolve')
 return errors

def assess_claim(claim, evidence, permissions, required_scope):
 """Typed claim gate: a passing numerical result cannot replace exact scope and authority."""
 if not isinstance(claim,bool): raise TypeError('claim must be boolean')
 if not isinstance(evidence,list) or not isinstance(permissions,dict):raise TypeError('invalid gate evidence')
 return bool(claim and evidence and all(
   e.get('current') is True and e.get('scope')==required_scope and
   e.get('independently_reviewed') is True for e in evidence)
   and permissions and all(v is True for v in permissions.values()))

def wilson_lower(k,n,z=1.96):
 if not isinstance(n,int) or not isinstance(k,int) or n<1 or k<0 or k>n or not math.isfinite(z) or z<=0:
  raise ValueError('invalid binomial parameters')
 p=k/n; zz=z*z
 return (p+zz/(2*n)-z*math.sqrt(p*(1-p)/n+zz/(4*n*n)))/(1+zz/n)

def run():
 gates=json.loads((THIS/'data/gates.json').read_text(encoding='utf-8'))
 a,ah=replay('v11');b,bh=replay('v12')
 b20,b20h=replay('v12',replications=20)
 stored_v12={f.name:sha(f.read_bytes()) for f in (SOURCE['v12']/'outputs').iterdir() if f.is_file()}
 stored_snapshot_verified=(stored_v12==b20h)
 baseline_manifest=json.loads((THIS/'data/original-file-hashes.json').read_text(encoding='utf-8'))
 unchanged=all(sha((SOURCE[lab]/rel).read_bytes())==baseline_manifest[f'{SOURCE[lab].name}/{rel}']
               for lab,paths in FILES.items() for rel in paths)
 # Two reruns are a byte-for-byte replay check of each source's generated products.
 _,ah2=replay('v11'); _,bh2=replay('v12')
 replay_ok=(ah==ah2 and bh==bh2)
 errs=audit_v11(a)+audit_v12(b)
 s=b['scenarios'];fixed=a['baseline']; other=s['BASE']
 if fixed['unique_requests']!=other['unique_requests'] or fixed['served']!=other['completed']:
  errs.append('cross-lab nominal fixture divergence')
 service_screen=(fixed['served_fraction']>=gates['screening']['fixed_completion_fraction_min']
                 and other['completion_fraction']>=gates['screening']['fixed_completion_fraction_min'])
 fault_screen=(a['degraded_one_vehicle']['served_fraction']>=gates['screening']['fault_completion_fraction_min']
               and s['OUTAGE']['completion_fraction']>=gates['screening']['fault_completion_fraction_min'])
 has_access_data=False # Neither original request CSV contains an accessibility attribute.
 record={
  'case':'NS-U2.1','baseline_unchanged':unchanged,'controlled_gate_sha256':sha((THIS/'data/gates.json').read_bytes()),'input_digests':{
    name:{rel:sha((SOURCE[name]/rel).read_bytes()) for rel in files} for name,files in FILES.items()},
  'source_output_sha256':{'v11':ah,'v12':bh}, 'repeat_replay_byte_stable':replay_ok,
  'preserved_v12_snapshot':{'original_replications':b20['experiment']['replications'],
                            'original_paired_difference':b20['experiment']['paired_mean_difference'],
                            'original_95pct_interval':b20['experiment']['approximate_normal_95pct_interval'],
                            'original_output_byte_identical_to_20_replication_replay':stored_snapshot_verified},
  'v11':{'fixed_completed':fixed['served'],'unique':fixed['unique_requests'],
         'p90_wait_min':fixed['p90_wait_min'],'degraded_completed':a['degraded_one_vehicle']['served']},
  'v12':{sid:{'completed':r['completed'],'lost_messages':r['lost_messages'],
          'unserved_capacity':r['unserved_capacity'],'unique':r['unique_requests'],
          'p90_wait_min':r['p90_wait_min']} for sid,r in s.items()},
  'fixed_fixture_wilson_lower_demonstration':round(wilson_lower(other['completed'],other['unique_requests']),6),
  'statistics_caveat':'Wilson calculation assumes independent Bernoulli trials; fixed hand-designed requests do not satisfy this sampling interpretation',
  'paired_experiment':b['experiment'],
  'checks':{'original_v12_20_replication_snapshot_verified':stored_snapshot_verified,'original_runner_files_unchanged':unchanged,'independent_replay':replay_ok,'independent_ledger_audit':not errs,
            'nominal_fixed_screen':service_screen,'degraded_scenario_screen':fault_screen,
            'accessibility_evidence_available':has_access_data,
            'all_required_permissions':all(gates['field_permissions'].values()),
            'in_scope_independently_reviewed_field_evidence':assess_claim(
              service_screen,gates['evidence'],gates['field_permissions'],'field_accessibility')},
  'errors':errs,
  'status':'HOLD for field deployment',
  'interpretation':'v11 single vehicle and v12 faulted vehicle are not the same intervention. Toy event-ledger losses are visible to the simulator, not demonstrably observed by a real intake system. Synthetic software verification is not field validation.'
 }
 if errs or not replay_ok or not unchanged or not stored_snapshot_verified: raise RuntimeError('Cross-lab integrity check failed: '+str(errs))
 return record

if __name__=='__main__':
 out=run();p=THIS/'outputs/u2-cross-lab-results.json';p.parent.mkdir(exist_ok=True)
 p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 print(json.dumps({'status':out['status'],'checks':out['checks'],'source_output_sha256':out['source_output_sha256']},indent=2))
