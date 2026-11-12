"""Executable audit of synthetic T1 teaching case and intentional failures."""
from __future__ import annotations
import copy,json,math,unittest
from pathlib import Path
from t1_evidence import audit, euler_recovery, zero_failure_upper, DEFAULT

class T1Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.data=json.loads(DEFAULT.read_text(encoding='utf-8'))
    def case(self):return copy.deepcopy(self.data)
    def test_request_conservation(self):
        o=audit(self.case()); c=o['request_accounting']
        self.assertEqual((c['arrivals'],c['served'],c['rejected'],c['pending']),(40,32,5,3))
    def test_guard_band_and_access(self):
        o=audit(self.case());self.assertEqual((o['timely_nominal'],o['timely_guarded'],o['accessible_guarded']), (32,26,6))
        self.assertEqual(o['timely_guarded_all_fraction'],.65);self.assertEqual(o['accessible_guarded_fraction'],.75)
    def test_zero_failure_confidence(self):
        self.assertAlmostEqual(zero_failure_upper(300), .009936081944457708,places=12)
    def test_invalid_confidence(self):
        for n,c in ((0,.95),(True,.95),(-1,.95),(10,1),(10,0),(10,float('nan'))):
            with self.subTest(n=n,c=c),self.assertRaises(ValueError):zero_failure_upper(n,c)
    def test_queueing(self):
        o=audit(self.case())['mm1'];self.assertEqual(o['rho'],.8)
        self.assertEqual((o['mean_in_system_min'],o['mean_wait_queue_min'],o['L'],o['Lq']),(30,24,4,3.2))
    def test_euler(self):
        o=audit(self.case())['euler'];self.assertAlmostEqual(o['coarse']['estimate'], .3)
        self.assertAlmostEqual(o['refined']['estimate'],.463250390625)
        self.assertLess(abs(o['refined']['estimate']-o['refined']['exact']),abs(o['coarse']['estimate']-o['coarse']['exact']))
        self.assertLess(o['unstable_factor'],-1)
    def test_invalid_euler(self):
        for x in ((0,1,1),(.7,-1,1),(.7,.3,1),(.7,1,0)):
            with self.subTest(x=x),self.assertRaises(ValueError):euler_recovery(*x)
    def test_redundancy(self):
        o=audit(self.case())['reliability'];self.assertAlmostEqual(o['independent_parallel'],.9991)
        self.assertAlmostEqual(o['common_cause_adjusted'],.9641315)
        self.assertLess(o['common_cause_adjusted'],.98)
    def test_invalid_reliability(self):
        for k,v in (('channel_reliability',float('nan')),('channel_reliability',-1),('common_cause_probability',1.01)):
            d=self.case();d[k]=v
            with self.subTest(k=k,v=v),self.assertRaises(ValueError):audit(d)
    def test_robust_infeasible(self):
        o=audit(self.case())['candidates'];self.assertEqual([r['vehicles'] for r in o if r['nominal_feasible']],[2]);self.assertFalse(any(r['robust_feasible'] for r in o))
    def test_evidence_and_authorization(self):
        o=audit(self.case());self.assertEqual(o['actionable_evidence'],2)
        self.assertFalse(o['authorization']['all_granted']);self.assertFalse(o['deployment_screen']['passes'])
    def test_change_revision_still_draft(self):
        d=self.case(); d['evidence'][4]['revision']=d['expected_revision']
        self.assertEqual(audit(d)['actionable_evidence'],2)
    def test_granted_permissions_still_insufficient(self):
        d=self.case();d['granted_permissions']=d['required_permissions'][:]
        self.assertFalse(audit(d)['deployment_screen']['passes'])
    def test_replayed_request_rejected(self):
        d=self.case();d['requests'].append(copy.deepcopy(d['requests'][0]))
        with self.assertRaises(ValueError):audit(d)
    def test_corrupt_status_rejected(self):
        d=self.case();d['requests'][0]['status']='ghost'
        with self.assertRaises(ValueError):audit(d)
    def test_pending_cannot_have_latency(self):
        d=self.case(); r=next(r for r in d['requests'] if r['status']=='pending');r['latency_s']=0
        with self.assertRaises(ValueError):audit(d)
    def test_invalid_guard(self):
        d=self.case();d['clock_uncertainty_s']=-.1
        with self.assertRaises(ValueError):audit(d)
    def test_duplicate_evidence(self):
        d=self.case();d['evidence'][1]['requirement']=d['evidence'][0]['requirement']
        with self.assertRaises(ValueError):audit(d)
    def test_paired_effect(self):
        o=audit(self.case());self.assertAlmostEqual(o['paired_effect_min'],-3.5)
        self.assertAlmostEqual(o['paired_se_min'],.5627314338711378)
    def test_paired_malformed(self):
        d=self.case();d['paired_candidate_wait_min'].pop()
        with self.assertRaises(ValueError):audit(d)
    def test_finance(self):
        o=audit(self.case())['finance'];self.assertAlmostEqual(o['A_pv'],1544.6496058741)
        self.assertAlmostEqual(o['B_pv'],1499.5572832308)
        self.assertAlmostEqual(o['required_saving_per_year'],73.441712926249)
    def test_outputs_reproducible(self):
        recorded=json.loads((DEFAULT.parent/'t1-results.json').read_text(encoding='utf-8'))
        self.assertEqual(audit(self.case()),recorded)

if __name__=='__main__':unittest.main()
