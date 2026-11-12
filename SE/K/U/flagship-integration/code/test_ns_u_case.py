"""Numeric, boundary, and adversarial checks for synthetic NS-U4.1 results."""
import copy
import json
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ns_u_case import INPUT,OUTPUT,InvalidCase,check,check_events,flows,run

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.case=json.loads(INPUT.read_text());cls.out=run(cls.case)
    def test_reproduce_exact_record(self):self.assertEqual(self.out,json.loads(OUTPUT.read_text()))
    def test_four_policies_and_scenarios(self):
        self.assertEqual(len(self.out['policies']),4)
        for p,d in self.out['policies'].items():
            self.assertEqual(len(d['scenarios']),4)
            for scenario,result in d['scenarios'].items():
                for g,trace in result['trace'].items():
                    self.assertEqual(len(trace),6)
                    for step in trace:
                        self.assertEqual(step['unfinished'],max(step['unfinished'],0))
                        self.assertLessEqual(step['served'],step['capacity'])
                        self.assertLessEqual(step['timely'],step['arrivals'])
                    dat=result['by_class'][g]
                    self.assertEqual(dat['arrivals'],dat['served']+dat['unfinished'])
                    self.assertEqual(sum(x['arrivals'] for x in trace),dat['arrivals'])
                    self.assertEqual(sum(x['served'] for x in trace),dat['served'])
                    self.assertEqual(sum(x['timely'] for x in trace),dat['timely'])
    def test_robust_feasible_set_empty(self):
        self.assertEqual(self.out['policies']['integrated']['scenario_weight_covered'],.45)
        self.assertTrue(self.out['policies']['integrated']['scenarios']['normal']['passes_screen'])
        self.assertTrue(all(not x['all_scenarios_pass'] for x in self.out['policies'].values()))
        self.assertTrue(all(x['scenario_weight_covered']<.95 for x in self.out['policies'].values()))
    def test_acceptance_and_subgroup(self):
        p=self.out['dispatch_acceptance']
        self.assertEqual((p['nominal_timely'],p['guarded_timely'],p['n']),(72,67,80))
        self.assertEqual((p['accessible_guarded_timely'],p['accessible_n']),(10,16))
    def test_alarm_bayes(self):
        self.assertAlmostEqual(self.out['bayesian_alarm']['one_positive_posterior'],.12/.205)
        self.assertAlmostEqual(self.out['bayesian_alarm']['second_independent_positive_posterior'],.9186602870813396)
    def test_dependent_availability(self):
        self.assertAlmostEqual(self.out['reliability']['independent_redundancy'],.999775)
        self.assertAlmostEqual(self.out['reliability']['common_cause_joint_availability'],.96978175)
        self.assertLess(self.out['reliability']['common_cause_joint_availability'],.99)
    def test_factorial_paired_and_numerics(self):
        self.assertEqual(self.out['factorial']['interaction_minutes'],-3)
        self.assertAlmostEqual(self.out['paired_experiment']['mean_improvement_min'],37/6)
        a,b=self.out['paired_experiment']['student_t_95_interval']
        self.assertAlmostEqual(a,5.408401023667107)
        self.assertAlmostEqual(b,6.924932309666227)
        self.assertEqual(self.out['dynamic']['equilibrium_requests'],10)
        self.assertEqual(self.out['dynamic']['euler_stable_step_limit_min'],5)
        self.assertAlmostEqual(self.out['dynamic']['euler_6min_multiplier'],-1.4)
    def test_project_causal(self):
        self.assertEqual(self.out['project']['critical_path_duration_days'],10)
        self.assertAlmostEqual(self.out['project']['cost_performance_index'],100/130)
        self.assertEqual(self.out['project']['schedule_variance'],-20)
        self.assertEqual(self.out['causal']['difference_in_differences_minutes'],-7)
    def test_interface_has_three_distinct_defects(self):
        issues=[v['type'] for v in self.out['interface']['violations']]
        self.assertEqual(issues,['ack_before_commit','conflicting_replay','stale_revision'])
        self.assertEqual(self.out['interface']['exact_duplicates'],1)
        self.assertFalse(self.out['interface']['conforming'])
    def test_only_one_actionable_and_no_authorization(self):
        self.assertEqual(self.out['evidence']['actionable_ids'],['C1'])
        self.assertFalse(any(self.out['evidence']['authorizations'].values()))
        self.assertEqual(self.out['readiness']['disposition'],'HOLD')
    def test_reject_bad_weights(self):
        p=copy.deepcopy(self.case);p['scenarios']['normal']['weight']+=.1
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_negative_capacity(self):
        p=copy.deepcopy(self.case);p['policies']['integrated']['accessible_capacity']=-1
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_invalid_probability(self):
        p=copy.deepcopy(self.case);p['diagnostic']['false_positive']=1.5
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_zero_probability_alarm(self):
        p=copy.deepcopy(self.case);p['diagnostic'].update(prior_blocked=0,false_positive=0)
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_duplicate_claim_id(self):
        p=copy.deepcopy(self.case);p['claims'][1]['id']=p['claims'][0]['id']
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_malformed_arrivals(self):
        p=copy.deepcopy(self.case);p['demand']['accessible'][0]=-9
        with self.assertRaises(InvalidCase):run(p)
    def test_reject_mismatched_pairs(self):
        p=copy.deepcopy(self.case);p['paired_wait_min']['integrated'].pop()
        with self.assertRaises(InvalidCase):run(p)
    def test_stale_claim_cannot_be_signed_into_validity(self):
        p=copy.deepcopy(self.case);p['claims'][1]['reviewed']=True;p['claims'][1]['approved']=True
        self.assertEqual(run(p)['evidence']['actionable_count'],1)
    def test_corrected_events_do_not_erase_missing_approvals(self):
        p=copy.deepcopy(self.case);p['interface_events']=p['interface_events'][:3]
        self.assertTrue(run(p)['interface']['conforming'])
        self.assertEqual(run(p)['readiness']['disposition'],'HOLD')
    def test_all_claims_approved_but_no_institutional_authority(self):
        p=copy.deepcopy(self.case)
        for c in p['claims']:
            c.update(evidence_revision='2.0',scope=c['required_scope'],reviewed=True,approved=True)
        self.assertEqual(run(p)['evidence']['actionable_count'],5)
        self.assertEqual(run(p)['readiness']['disposition'],'HOLD')
    def test_missing_scope_blocks_approval(self):
        p=copy.deepcopy(self.case)
        p['claims'][2]['approved']=True
        self.assertEqual(run(p)['evidence']['actionable_count'],1)
    def test_floor_rounding_and_capacity(self):
        sc=self.case['scenarios']['compound'];p=self.case['policies']['integrated'];result=flows(self.case,p,sc)
        self.assertEqual(result['trace']['accessible'][0]['capacity'],4)
        self.assertEqual(result['trace']['standard'][0]['arrivals'],21)
        self.assertFalse(result['passes_screen'])
    def test_increasing_service_does_not_make_missing_authority_go_away(self):
        p=copy.deepcopy(self.case)
        for pol in p['policies'].values():
            pol['standard_capacity']=200;pol['accessible_capacity']=200
        self.assertEqual(run(p)['readiness']['disposition'],'HOLD')
    def test_common_cause_improvement_is_not_review(self):
        p=copy.deepcopy(self.case);p['reliability']['common_cause_failure']=.005
        self.assertGreater(run(p)['reliability']['common_cause_joint_availability'],.99)
        self.assertEqual(run(p)['readiness']['disposition'],'HOLD')

if __name__=='__main__':unittest.main()
