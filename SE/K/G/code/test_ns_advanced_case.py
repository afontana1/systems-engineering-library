"""Adverse-case and numerical regression suite for NS-G4.1 (standard library)."""
import copy
import hashlib
import json
import math
import tempfile
import unittest
from pathlib import Path
from ns_advanced_case import (INPUT,OUTPUT,read_case,bound_age,queue_wait_minutes,alarm_ppv,
    retry_load,trace_audit,availability,max_flow,difference_in_differences,pretrend_gap,evaluate,run)


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case=read_case()
        cls.results=run(cls.case)

    def test_case_identity(self):self.assertEqual(self.case['case_id'],'NS-G4.1')
    def test_result_identity(self):self.assertEqual(self.results['revision'],'1.0')
    def test_reproducible(self):
        actual=json.loads(OUTPUT.read_text());self.assertEqual(actual.pop('input_sha256'),hashlib.sha256(INPUT.read_bytes()).hexdigest());self.assertEqual(actual,run(self.case))
    def test_scenarios(self):self.assertEqual(len(self.results['runs']),15)
    def test_weight(self):self.assertAlmostEqual(sum(x['weight'] for x in self.case['scenarios']),1)
    def test_bad_weight(self):
        with tempfile.TemporaryDirectory() as d:
            c=copy.deepcopy(self.case);c['scenarios'][0]['weight']=.56
            path=Path(d)/'bad.json';path.write_text(json.dumps(c))
            with self.assertRaises(ValueError):read_case(path)
    def test_duplicate_policy(self):
        with tempfile.TemporaryDirectory() as d:
            c=copy.deepcopy(self.case);c['policies'][1]['id']='baseline'
            path=Path(d)/'bad.json';path.write_text(json.dumps(c))
            with self.assertRaises(ValueError):read_case(path)
    def test_bad_probability(self):
        with tempfile.TemporaryDirectory() as d:
            c=copy.deepcopy(self.case);c['policies'][0]['common_outage_probability']=1.5
            path=Path(d)/'bad.json';path.write_text(json.dumps(c))
            with self.assertRaises(ValueError):read_case(path)
    def test_negative_flow(self):
        with self.assertRaises(ValueError):max_flow(self.case['sos']['arcs'],'Request','Care',loss=-1)
    def test_same_endpoint(self):
        with self.assertRaises(ValueError):max_flow(self.case['sos']['arcs'],'Request','Request')
    def test_disabled_source(self):self.assertEqual(max_flow(self.case['sos']['arcs'],'Request','Care',{'Request'}),0)
    def test_nominal_flow(self):self.assertEqual(max_flow(self.case['sos']['arcs'],'Request','Care'),68)
    def test_guarded_flow(self):self.assertEqual(max_flow(self.case['sos']['arcs'],'Request','Care',rail_boost=8,para_boost=7),70)
    def test_rail_outage_flow(self):self.assertEqual(max_flow(self.case['sos']['arcs'],'Request','Care',{'Rail'},rail_boost=8,para_boost=7),32)
    def test_compound_flow(self):self.assertEqual(max_flow(self.case['sos']['arcs'],'Request','Care',loss=12,rail_boost=8,para_boost=7),58)
    def test_zero_capacity_graph(self):self.assertEqual(max_flow([{'from':'A','to':'B','capacity':0}],'A','B'),0)
    def test_bounds(self):self.assertEqual(bound_age(126,100,5,3),34)
    def test_fresh(self):self.assertEqual(bound_age(126,110,5,3),24)
    def test_compound_clock(self):self.assertEqual(bound_age(126,110,5,8),29)
    def test_negative_clock(self):
        with self.assertRaises(ValueError):bound_age(100,90,2,-1)
    def test_future_clock(self):
        with self.assertRaises(ValueError):bound_age(100,101,0,0)
    def test_bad_nan(self):
        with self.assertRaises(ValueError):bound_age(float('nan'),0,0,0)
    def test_queue_baseline(self):self.assertAlmostEqual(queue_wait_minutes(8.4,9.6),43.75)
    def test_queue_guarded(self):self.assertAlmostEqual(queue_wait_minutes(8.4,12.2),10.8714408973)
    def test_queue_critical(self):self.assertIsNone(queue_wait_minutes(12.2,12.2))
    def test_queue_overload(self):self.assertIsNone(queue_wait_minutes(15,12.2))
    def test_queue_zero_arrival(self):self.assertEqual(queue_wait_minutes(0,10),0)
    def test_queue_negative(self):
        with self.assertRaises(ValueError):queue_wait_minutes(-1,10)
    def test_ppv(self):self.assertAlmostEqual(alarm_ppv(.03,.9,.04),.027/(.027+.0388))
    def test_ppv_bad(self):
        with self.assertRaises(ValueError):alarm_ppv(.03,.9,1.5)
    def test_ppv_zero(self):
        with self.assertRaises(ValueError):alarm_ppv(0,1,0)
    def test_retry(self):self.assertAlmostEqual(retry_load(80,.25,112)['offered_per_second'],80/.75)
    def test_retry_failure(self):self.assertFalse(retry_load(80,.30,112)['stable'])
    def test_retry_non_terminating(self):self.assertIsNone(retry_load(80,1,112)['offered_per_second'])
    def test_retry_negative(self):
        with self.assertRaises(ValueError):retry_load(80,-.1,112)
    def test_trace(self):
        t=trace_audit(self.case['sample_events']);self.assertEqual(t['accepted_unique_events'],3)
        self.assertEqual(t['idempotent_duplicates'],1)
        self.assertEqual(t['violations'],['E5:illegal_transition','E6:payload_conflict'])
    def test_trace_sequence_gap(self):
        t=trace_audit([{'event_id':'x','key':'x','seq':2,'type':'RESERVE','payload_hash':'p'}]);self.assertIn('x:sequence_gap',t['violations'])
    def test_trace_unknown_event(self):
        t=trace_audit([{'event_id':'x','key':'x','seq':1,'type':'REMOVE','payload_hash':'p'}]);self.assertIn('x:illegal_transition',t['violations'])
    def test_availability(self):self.assertAlmostEqual(availability(.992,.003,.998,.996),.9909625503375361)
    def test_common_outage(self):self.assertLess(availability(.992,.038,.998,.996),.985)
    def test_negative_availability(self):
        with self.assertRaises(ValueError):availability(.992,-.1,.998,.996)
    def test_did(self):self.assertEqual(difference_in_differences(self.case['enterprise']),-5)
    def test_pretrend(self):self.assertEqual(pretrend_gap(self.case['enterprise']),0)
    def test_pretrend_missing(self):
        e=copy.deepcopy(self.case['enterprise']);e['treated_pre_pre_minutes']=[2]
        with self.assertRaises(ValueError):pretrend_gap(e)
    def test_gates(self):
        outcomes={x['policy']:x for x in self.results['policies']}
        self.assertEqual(outcomes['coordinated_guardrails']['scenario_technical_coverage_weight'],.55)
        self.assertTrue(outcomes['coordinated_guardrails']['resource_and_equity_screen'])
        for x in outcomes.values():self.assertFalse(x['operational_authorized'])
    def test_permissions(self):self.assertEqual(self.results['enterprise']['missing_permissions'],['road_authority','labor_representative','privacy_officer'])
    def test_missing_permissions_remain_hold(self):
        c=copy.deepcopy(self.case)
        for k in c['enterprise']['permissions_granted']:c['enterprise']['permissions_granted'][k]=True
        self.assertFalse(run(c)['policies'][-1]['operational_authorized'])
    def test_no_fictional_causal_validation(self):self.assertFalse(self.results['enterprise']['causal_claim_validated'])
    def test_inaccessible_failure(self):
        r=next(x for x in self.results['runs'] if x['policy']=='coordinated_guardrails' and x['scenario']=='rail_outage')
        self.assertEqual(r['accessible_max_flow_slots'],32)
        self.assertFalse(r['checks']['accessible_flow'])
    def test_interface_drift_failure(self):
        r=next(x for x in self.results['runs'] if x['policy']=='coordinated_guardrails' and x['scenario']=='interface_drift')
        self.assertFalse(r['route_revision_matches']);self.assertFalse(r['checks']['route_authorized'])
    def test_nominal_pass(self):
        r=next(x for x in self.results['runs'] if x['policy']=='coordinated_guardrails' and x['scenario']=='nominal')
        self.assertTrue(r['technical_screen_pass'])
    def test_compound_fail(self):
        r=next(x for x in self.results['runs'] if x['policy']=='coordinated_guardrails' and x['scenario']=='compound_grid_flood')
        self.assertFalse(r['technical_screen_pass'])
        self.assertLess(r['joint_availability'],.985)
    def test_every_policy_and_scenario_preserved(self):
        self.assertEqual({(r['policy'],r['scenario']) for r in self.results['runs']},
                         {(p['id'],s['id']) for p in self.case['policies'] for s in self.case['scenarios']})
    def test_bad_scenario_age(self):
        c=copy.deepcopy(self.case);c['scenarios'][0]['clock_skew_extra_seconds']=-10
        with self.assertRaises(ValueError):run(c)
    def test_immutable_report_order(self):self.assertEqual(run(self.case),run(self.case))

if __name__=='__main__':unittest.main()
