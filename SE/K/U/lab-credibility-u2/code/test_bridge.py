import copy
import json
import unittest
from pathlib import Path
from .bridge import ROOT, THIS, SOURCE, replay, audit_v11, audit_v12, wilson_lower, assess_claim, run

class CrossLabChecks(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.v11,_=replay('v11');cls.v12,_=replay('v12')
 def test_independent_nominal_matches(self):
  self.assertEqual(self.v11['baseline']['served'],self.v12['scenarios']['BASE']['completed'])
 def test_fixed_fixture_not_field_confidence(self):
  self.assertLess(wilson_lower(12,12),0.95)
 def test_wilson_invalid(self):
  for k,n in [(3,2),(-1,1),(0,0)]:
   with self.assertRaises(ValueError):wilson_lower(k,n)
 def test_v11_conservation(self):self.assertFalse(audit_v11(self.v11))
 def test_v12_conservation(self):self.assertFalse(audit_v12(self.v12))
 def test_adversarial_unserved(self):
  r=copy.deepcopy(self.v12);r['scenarios']['LOSS']['unserved_capacity']+=1
  self.assertTrue(any('conservation' in s for s in audit_v12(r)))
 def test_adversarial_lost_status(self):
  r=copy.deepcopy(self.v12);next(x for x in r['scenarios']['LOSS']['records'] if x['status']=='completed')['status']='unobserved_message_loss'
  self.assertTrue(audit_v12(r))
 def test_adversarial_overlap(self):
  r=copy.deepcopy(self.v11);r['baseline']['assignments'][1]['vehicle']='V01'
  r['baseline']['assignments'][1]['start_min']=8
  self.assertTrue(audit_v11(r))
 def test_adversarial_fault_intersection(self):
  r=copy.deepcopy(self.v12)
  x=next(x for x in r['scenarios']['OUTAGE']['records'] if x['status']=='completed')
  x['vehicle']='V01';x['start_min']=3;x['finish_min']=15
  self.assertTrue(audit_v12(r))
 def test_missing_permission_not_overridden(self):
  e=[{'current':True,'scope':'field_accessibility','independently_reviewed':True}]
  self.assertFalse(assess_claim(True,e,{'safety':False},'field_accessibility'))
 def test_wrong_evidence_scope(self):
  e=[{'current':True,'scope':'synthetic_software','independently_reviewed':True}]
  self.assertFalse(assess_claim(True,e,{'safety':True},'field_accessibility'))
 def test_stale_evidence(self):
  e=[{'current':False,'scope':'field_accessibility','independently_reviewed':True}]
  self.assertFalse(assess_claim(True,e,{'safety':True},'field_accessibility'))
 def test_valid_permission_mechanics_only(self):
  e=[{'current':True,'scope':'field_accessibility','independently_reviewed':True}]
  self.assertTrue(assess_claim(True,e,{'safety':True},'field_accessibility'))
 def test_falsified_wait(self):
  r=copy.deepcopy(self.v11);r['baseline']['assignments'][0]['wait_min']=99
  self.assertTrue(any('wait mismatch' in e for e in audit_v11(r)))
 def test_falsified_digest(self):
  r=copy.deepcopy(self.v12);r['scenarios']['BASE']['evidence_sha256']='0'*64
  self.assertTrue(any('ledger hash mismatch' in e for e in audit_v12(r)))
 def test_no_evidence(self):self.assertFalse(assess_claim(True,[],{'safety':True},'field_accessibility'))
 def test_replay_repeat_stability(self):
  _,a=replay('v11');_,b=replay('v11');self.assertEqual(a,b)
 def test_overall_report(self):
  record=run();self.assertFalse(record['checks']['degraded_scenario_screen'])
  self.assertFalse(record['checks']['accessibility_evidence_available'])
  self.assertTrue(record['checks']['original_v12_20_replication_snapshot_verified'])
  self.assertEqual(record['status'],'HOLD for field deployment')
if __name__=='__main__':unittest.main()
