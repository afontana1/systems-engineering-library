import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.architecture import validate_model,load_model
from src.event_sim import Scenario, Request, simulate,load_events, synthetic_demand, paired_experiment,check_nonoverlap
from src.evidence import trace_audit,read_csv,sha
from src.run_advanced import run

class AdvancedLabTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.events=load_events(ROOT/'data/requests.csv')
  cls.specs={x['id']:Scenario(**x) for x in json.loads((ROOT/'data/scenarios.json').read_text())}

 def test_model_valid(self): self.assertTrue(validate_model(load_model(ROOT/'models/architecture.json'))['valid'])
 def test_unknown_endpoint(self):
  m=load_model(ROOT/'models/architecture.json');m['interfaces'][0]['to']='UNKNOWN'
  self.assertFalse(validate_model(m)['valid'])
 def test_duplicate_model_ids(self):
  m=load_model(ROOT/'models/architecture.json');m['components'][1]['id']=m['components'][0]['id']
  self.assertFalse(validate_model(m)['valid'])
 def test_absent_acceptance_rejected(self):
  m=load_model(ROOT/'models/architecture.json');m['requirements'][0]['acceptance']=''
  self.assertFalse(validate_model(m)['valid'])
 def test_baseline_complete(self):
  x=simulate(self.events,self.specs['BASE']);self.assertEqual((x['completed'],x['unique_requests'],x['duplicates_ignored']),(12,12,1))
 def test_baseline_nonoverlap(self): self.assertTrue(simulate(self.events,self.specs['BASE'])['vehicle_nonoverlap'])
 def test_outage_reduces(self):
  b=simulate(self.events,self.specs['BASE']);f=simulate(self.events,self.specs['OUTAGE']);self.assertLess(f['completed'],b['completed'])
 def test_outage_avoided(self):
  x=simulate(self.events,self.specs['OUTAGE']);self.assertTrue(all(not(r['vehicle']=='V01' and r['start_min']<70 and r['finish_min']>0) for r in x['records'] if r['status']=='completed'))
 def test_loss_visible(self):
  x=simulate(self.events,self.specs['LOSS']);self.assertGreater(x['lost_messages'],0)
  self.assertEqual(x['lost_messages']+x['completed']+x['unserved_capacity'],x['unique_requests'])
 def test_delay_not_better(self):
  a=simulate(self.events,self.specs['BASE']);b=simulate(self.events,self.specs['DELAY'])
  self.assertLessEqual(b['completed'],a['completed'])
 def test_telemetry_block(self):
  x=simulate(self.events,self.specs['TELEMETRY'])
  self.assertTrue(all(r['start_min']>=45 for r in x['records'] if r['status']=='completed'))
 def test_one_vehicle_nonoverlap(self): self.assertTrue(simulate(self.events,self.specs['LOW-CAPACITY'])['vehicle_nonoverlap'])
 def test_repeatable(self):
  self.assertEqual(simulate(self.events,self.specs['LOSS']),simulate(self.events,self.specs['LOSS']))
 def test_conflicting_payload_rejected(self):
  x=simulate(self.events+[replace(self.events[0],origin='Z')],self.specs['BASE']);self.assertEqual(x['rejected_conflicts'],1)
 def test_cross_id_delivery_key_rejected(self):
  x=simulate(self.events+[replace(self.events[0],request_id='DIFFERENT')],self.specs['BASE']);self.assertEqual(x['rejected_conflicts'],1)
 def test_bad_probability(self): self.assertRaises(ValueError,Scenario,id='BAD',drop_probability=1.1)
 def test_bad_vehicle(self): self.assertRaises(ValueError,Scenario,id='BAD',vehicles=1,outage_vehicle=2)
 def test_nan_time(self): self.assertRaises(ValueError,Scenario,id='BAD',trip_min=float('nan'))
 def test_synthetic_repeat(self): self.assertEqual(synthetic_demand(9,15),synthetic_demand(9,15))
 def test_synthetic_count(self): self.assertEqual(len(synthetic_demand(2,10)),10)
 def test_paired_repeat(self):
  a=paired_experiment(self.specs['BASE'],self.specs['OUTAGE'],replications=12,seed=2)
  b=paired_experiment(self.specs['BASE'],self.specs['OUTAGE'],replications=12,seed=2)
  self.assertEqual(a,b)
 def test_paired_interval_contains_mean(self):
  a=paired_experiment(self.specs['BASE'],self.specs['OUTAGE'],replications=15,seed=3)
  self.assertLessEqual(a['approximate_normal_95pct_interval'][0],a['paired_mean_difference'])
  self.assertGreaterEqual(a['approximate_normal_95pct_interval'][1],a['paired_mean_difference'])
 def test_trace_valid(self):
  x=trace_audit(read_csv(ROOT/'data/requirements-v12.csv'),read_csv(ROOT/'data/verification-plan.csv'),set(self.specs))
  self.assertTrue(x['pass_links'])
 def test_bad_trace(self):
  r=read_csv(ROOT/'data/requirements-v12.csv');t=read_csv(ROOT/'data/verification-plan.csv');t[0]['requirements']='X'
  self.assertFalse(trace_audit(r,t,set(self.specs))['pass_links'])
 def test_sha_stable(self): self.assertEqual(sha(ROOT/'data/requests.csv'),sha(ROOT/'data/requests.csv'))
 def test_empty(self): self.assertEqual(simulate([],self.specs['BASE'])['completed'],0)
 def test_nonoverlap_detects_violation(self):
  rows=[{'status':'completed','vehicle':'V01','start_min':0,'finish_min':10},
        {'status':'completed','vehicle':'V01','start_min':9,'finish_min':20}]
  self.assertFalse(check_nonoverlap(rows))
 def test_horizon_enforced(self):
  r=simulate([Request('Z',75,'A','B','z')],self.specs['BASE']);self.assertEqual(r['unserved_capacity'],1)
 def test_runner_files(self):
  with tempfile.TemporaryDirectory() as folder:
   out=run(folder,replications=10)
   self.assertTrue(out['fixture_checks_pass'])
   for name in ('scenario-results.json','scenario-summary.csv','provenance.json'):
    self.assertTrue((Path(folder)/name).is_file())

if __name__=='__main__':unittest.main()
