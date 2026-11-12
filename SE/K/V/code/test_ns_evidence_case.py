"""Deterministic and adversarial unit checks for NS-CE4.1 (stdlib only)."""
import copy
import hashlib
import json
import math
import tempfile
import unittest
from pathlib import Path
from ns_evidence_case import (INPUT,RESULT,load,run,candidate_screen,interface_screen,
    trial_screen,simulation_screen,evidence_screen,enterprise_screen)

class ConnectedEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d=load();cls.r=run(cls.d)

    def test_case_revision(self):self.assertEqual(self.d['revision'],'2.1')
    def test_three_alternatives(self):self.assertEqual(len(self.r['concepts']),3)
    def test_only_resilient_passes(self):
        self.assertEqual([x['id'] for x in self.r['concepts'] if x['robust_screen_pass']],['resilient'])
    def test_regional_nominal_but_not_storm(self):
        row=self.r['concepts'][1];self.assertTrue(row['nominal_service_pass']);self.assertFalse(row['storm_service_pass'])
    def test_storm_boundary(self):
        d=copy.deepcopy(self.d);d['alternatives'][2]['storm_p90_wait_minutes']=16.1
        self.assertFalse(candidate_screen(d)[2]['robust_screen_pass'])
    def test_storm_cost_boundary(self):
        d=copy.deepcopy(self.d);d['alternatives'][2]['capex_million']=7.81
        self.assertFalse(candidate_screen(d)[2]['cost_pass'])
    def test_interface_four_faults(self):
        self.assertEqual({x['type'] for x in self.r['interfaces']['violations']},
                         {'gap','duplicate_or_reordered','stale','revision_mismatch'})
        self.assertEqual(len(self.r['interfaces']['violations']),4)
    def test_interface_stale_age(self):
        stale=next(x for x in self.r['interfaces']['violations'] if x['type']=='stale')
        self.assertAlmostEqual(stale['age_seconds'],3.5)
    def test_interface_clean_traces(self):
        d=copy.deepcopy(self.d)
        d['interface']['contract_revision']='2.1'
        d['interface']['events']=[{'sequence':i,'timestamp_seconds':i,'observed_at_seconds':i+.1}
                                  for i in range(1,5)]
        self.assertTrue(interface_screen(d)['contract_pass'])
    def test_interface_bad_clock(self):
        d=copy.deepcopy(self.d);d['interface']['events'][0]['observed_at_seconds']=-1
        with self.assertRaises(ValueError):
            self._load_copy(d)
    def test_traced_population(self):
        self.assertEqual(self.r['testing']['requests'],80)
        self.assertEqual(self.r['testing']['timely'],65)
        self.assertEqual(self.r['testing']['unserved'],6)
        self.assertEqual(self.r['testing']['served'],74)
    def test_correct_denominator(self):
        x=self.r['testing'];self.assertAlmostEqual(x['population_timely_fraction'],65/80)
        self.assertAlmostEqual(x['served_only_timely_fraction'],65/74)
        self.assertGreater(x['served_only_timely_fraction'],x['population_timely_fraction'])
    def test_accessible_subgroup(self):self.assertEqual(self.r['testing']['accessible_timely_fraction'],10/16)
    def test_both_trials_fail(self):
        self.assertFalse(self.r['testing']['timeliness_screen_pass'])
        self.assertFalse(self.r['testing']['zero_failure_screen_pass'])
    def test_exact_bound(self):
        self.assertAlmostEqual(self.r['testing']['zero_failure_upper_exact_iid'],1-.05**(1/60),places=12)
    def test_299_independent_trials(self):
        d=copy.deepcopy(self.d);d['acceptance']['zero_failure_trials']=299
        self.assertTrue(trial_screen(d)['zero_failure_screen_pass'])
    def test_negative_count_rejected(self):
        d=copy.deepcopy(self.d);d['trial_groups']['accessible']['unserved']=-1
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_missing_accessible_group_rejected(self):
        d=copy.deepcopy(self.d);del d['trial_groups']['accessible']
        with self.assertRaises((KeyError,ValueError)):trial_screen(d)
    def test_zero_trial_rejected(self):
        d=copy.deepcopy(self.d);d['acceptance']['zero_failure_trials']=0
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_mm1_nominal(self):
        self.assertAlmostEqual(self.r['simulation']['nominal_utilization'],.8)
        self.assertAlmostEqual(self.r['simulation']['nominal_mm1_total_minutes'],30)
    def test_storm_unstable(self):self.assertFalse(self.r['simulation']['stress_stationary_mean_defined'])
    def test_near_saturation(self):
        d=copy.deepcopy(self.d);d['simulation']['baseline_arrivals_per_hour']=9.5
        self.assertAlmostEqual(simulation_screen(d)['nominal_mm1_total_minutes'],120)
    def test_unstable_nominal_rejected(self):
        d=copy.deepcopy(self.d);d['simulation']['baseline_arrivals_per_hour']=10
        with self.assertRaises(ValueError):simulation_screen(d)
    def test_paired_differences(self):
        self.assertEqual(self.r['simulation']['paired_reduction_minutes'],[3,4,1,2,7,0])
        self.assertAlmostEqual(self.r['simulation']['paired_mean_reduction_minutes'],17/6)
    def test_paired_interval(self):
        lo,hi=self.r['simulation']['illustrative_t_interval_minutes']
        self.assertAlmostEqual(lo,.2268695891005459)
        self.assertAlmostEqual(hi,5.439797077566121)
    def test_invalid_paired_data(self):
        d=copy.deepcopy(self.d);d['simulation']['paired_treatment_wait_minutes'].pop()
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_structural_vs_actionable(self):
        self.assertEqual(self.r['provenance']['structural_coverage'],1)
        self.assertEqual(self.r['provenance']['actionable_coverage'],.2)
    def test_path_defects(self):
        e={x['claim']:x for x in self.r['provenance']['paths']}
        self.assertIn('scope_mismatch',e['CL-CAP']['defects'])
        self.assertIn('revision_stale',e['CL-WAIT']['defects'])
        self.assertIn('does_not_pass',e['CL-ACCESS']['defects'])
        self.assertTrue(e['CL-ENT']['actionable'])
    def test_tampering_detected(self):
        d=copy.deepcopy(self.d);d['evidence'][4]['payload']+='ALTERED'
        self.assertIn('digest_mismatch',evidence_screen(d)['paths'][4]['defects'])
    def test_same_digest_invalid_revision(self):
        d=copy.deepcopy(self.d);d['evidence'][4]['revision']='2.0'
        self.assertFalse(evidence_screen(d)['paths'][4]['actionable'])
    def test_duplicate_claim_rejected(self):
        d=copy.deepcopy(self.d);d['evidence'].append(copy.deepcopy(d['evidence'][0]))
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_permissions_must_be_explicit(self):
        d=copy.deepcopy(self.d);d['permissions']['safety_approval']='yes'
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_approval_unavailable(self):self.assertFalse(self.r['provenance']['all_permissions_explicitly_granted'])
    def test_did(self):
        self.assertEqual(self.r['enterprise']['difference_in_differences_minutes'],-4)
        self.assertEqual(self.r['enterprise']['accessible_difference_in_differences_minutes'],-5)
    def test_did_changed_comparator(self):
        d=copy.deepcopy(self.d);d['enterprise']['comparison_post_wait_minutes']=16
        self.assertEqual(enterprise_screen(d)['difference_in_differences_minutes'],-2)
    def test_no_causal_certification(self):self.assertFalse(self.r['enterprise']['causal_claim_identified'])
    def test_no_deployment(self):
        self.assertFalse(self.r['integrated_technical_screen_pass'])
        self.assertIn('HOLD',self.r['deployment_disposition'])
    def test_all_local_screens_green_still_not_release_authorization(self):
        d=copy.deepcopy(self.d)
        d['interface']['contract_revision']='2.1'
        d['interface']['events']=[{'sequence':i,'timestamp_seconds':i,'observed_at_seconds':i+.1}
                                  for i in range(1,5)]
        for group in d['trial_groups'].values():
            group['timely']+=group['late']+group['unserved']
            group['late']=0;group['unserved']=0
        d['acceptance']['zero_failure_trials']=299
        d['simulation']['stress_arrivals_per_hour']=9
        for e in d['evidence']:
            e['revision']=d['revision'];e['scope']=e['required_scope'];e['status']='PASS'
        for flag in d['permissions']:d['permissions'][flag]=True
        result=run(d)
        self.assertTrue(result['integrated_technical_screen_pass'])
        self.assertIn('HOLD',result['deployment_disposition'])
        self.assertFalse(result['enterprise']['causal_claim_identified'])
    def test_invalid_nan_rejected(self):
        d=copy.deepcopy(self.d);d['simulation']['service_per_hour']=float('nan')
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_unknown_evidence_state_rejected(self):
        d=copy.deepcopy(self.d);d['evidence'][0]['status']='UNREVIEWED'
        with self.assertRaises(ValueError):self._load_copy(d)
    def test_snapshot(self):
        saved=json.loads(RESULT.read_text(encoding='utf-8'))
        self.assertEqual(saved.pop('input_sha256'),hashlib.sha256(INPUT.read_bytes()).hexdigest())
        self.assertEqual(saved,self.r)
    @staticmethod
    def _load_copy(data):
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'copy.json';path.write_text(json.dumps(data),encoding='utf-8')
            return load(path)

if __name__=='__main__':unittest.main()
