import csv
import json
import math
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.northstar import Config, Request, load_requests, deduplicate, nearest_rank, dispatch, synthetic_replications
from src.assurance import read_rows, audit_traceability
from src.run_lab import run, no_vehicle_overlap

class NorthstarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.events=load_requests(ROOT/'data/requests.csv')
        cls.config=Config(**json.loads((ROOT/'data/config.json').read_text()))

    def test_unique_and_duplicate(self):
        r,n=deduplicate(self.events)
        self.assertEqual((len(r),n),(12,1))
    def test_conflicting_id_rejected(self):
        self.assertRaises(ValueError,deduplicate,self.events+[replace(self.events[0],origin='C')])
    def test_reused_delivery_key_rejected(self):
        self.assertRaises(ValueError,deduplicate,self.events+[replace(self.events[0],request_id='NEW')])
    def test_bad_passengers(self):
        d=vars(self.events[0]).copy();d['passengers']='2'
        self.assertRaises(ValueError,Request.from_row,d)
    def test_bad_arrival(self):
        d=vars(self.events[0]).copy();d['arrival_min']='nan'
        self.assertRaises(ValueError,Request.from_row,d)
    def test_negative_arrival(self):
        d=vars(self.events[0]).copy();d['arrival_min']='-1'
        self.assertRaises(ValueError,Request.from_row,d)
    def test_same_origin_destination(self):
        d=vars(self.events[0]).copy();d['destination']=d['origin']
        self.assertRaises(ValueError,Request.from_row,d)
    def test_wrong_vehicle_count(self):
        self.assertRaises(ValueError,Config,vehicles=0)
    def test_wrong_trip_duration(self):
        self.assertRaises(ValueError,Config,trip_min=0)
    def test_percentile(self):
        self.assertEqual(nearest_rank([1,2,3,4,5],.9),5)
    def test_percentile_empty(self):
        self.assertIsNone(nearest_rank([],.9))
    def test_baseline_success(self):
        result=dispatch(self.events,self.config)
        self.assertTrue(result['demonstration_pass'])
        self.assertEqual((result['served'],result['unserved']),(12,0))
    def test_baseline_wait(self):
        self.assertEqual(dispatch(self.events,self.config)['p90_wait_min'],20)
    def test_baseline_ledger(self):
        self.assertEqual(dispatch(self.events,self.config)['duplicates_ignored'],1)
    def test_no_overlap(self):
        self.assertTrue(no_vehicle_overlap(dispatch(self.events,self.config)['assignments']))
    def test_one_vehicle_fails(self):
        r=dispatch(self.events,replace(self.config,vehicles=1))
        self.assertFalse(r['demonstration_pass'])
        self.assertLess(r['served_fraction'],0.95)
    def test_no_queue_empty(self):
        r=dispatch([],self.config)
        self.assertEqual(r['served'],0)
        self.assertFalse(r['demonstration_pass'])
    def test_near_horizon_reject(self):
        r=dispatch([replace(self.events[0],arrival_min=74)],self.config)
        self.assertEqual(r['unserved'],1)
    def test_deterministic_digest(self):
        self.assertEqual(dispatch(self.events,self.config)['audit_sha256'],dispatch(self.events,self.config)['audit_sha256'])
    def test_stochastic_repeatable(self):
        a=synthetic_replications(self.config,count=20,seed=7)
        b=synthetic_replications(self.config,count=20,seed=7)
        self.assertEqual(a,b)
    def test_stochastic_interval(self):
        r=synthetic_replications(self.config,count=100,seed=3)
        self.assertLessEqual(r['approximate_95pct_interval_for_replication_mean'][0],r['mean_served_fraction'])
        self.assertGreaterEqual(r['approximate_95pct_interval_for_replication_mean'][1],r['mean_served_fraction'])
    def test_trace_coverage(self):
        r=audit_traceability(read_rows(ROOT/'data/requirements.csv'),read_rows(ROOT/'data/verification-matrix.csv'),read_rows(ROOT/'data/hazards.csv'))
        self.assertEqual(r['trace_coverage_fraction'],1)
        self.assertTrue(r['link_integrity_pass'])
    def test_bad_trace(self):
        requirements=[{'req_id':'REQ-01'}]
        tests=[{'test_id':'T-1','req_ids':'NOPE'}]
        hazards=[{'hazard_id':'H-1','verification_test_ids':'T-1'}]
        self.assertFalse(audit_traceability(requirements,tests,hazards)['link_integrity_pass'])
    def test_missing_hazard_test(self):
        req=[{'req_id':'REQ-01'}];tests=[{'test_id':'T1','req_ids':'REQ-01'}]
        hazards=[{'hazard_id':'H1','verification_test_ids':''}]
        self.assertEqual(audit_traceability(req,tests,hazards)['hazards_missing_test_links'],['H1'])
    def test_full_run(self):
        with tempfile.TemporaryDirectory() as d:
            result=run(d)
            self.assertTrue(result['all_fixture_checks_pass'])
            self.assertTrue((Path(d)/'results.json').is_file())
            self.assertTrue((Path(d)/'input-hashes.json').is_file())
            with (Path(d)/'dispatch-assignments.csv').open(newline='') as stream:
                self.assertEqual(len(list(csv.DictReader(stream))),12)

if __name__=='__main__':unittest.main(verbosity=2)
