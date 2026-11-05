import unittest
from model_checks import *

class ArchitectureModelTests(unittest.TestCase):
    def setUp(self):
        self.model={'nodes':[{'id':'N','type':'Need'},{'id':'R','type':'Requirement','criticality':'high'},
            {'id':'C','type':'Component'},{'id':'T','type':'Test'},{'id':'E','type':'Evidence'}],
            'edges':[{'source':'R','target':'N','type':'refines'},
            {'source':'R','target':'C','type':'allocatedTo'},
            {'source':'R','target':'T','type':'verifiedBy'},
            {'source':'T','target':'E','type':'produces'}]}
    def test_valid_model(self):self.assertEqual(validate_model(self.model),[])
    def test_missing_test(self):
        self.model['edges']=self.model['edges'][:2]
        self.assertIn('missing-test:R',validate_model(self.model))
    def test_missing_allocation(self):
        self.model['edges']=[x for x in self.model['edges'] if x['type']!='allocatedTo']
        self.assertIn('missing-allocation:R',validate_model(self.model))
    def test_wrong_edge_type(self):
        self.model['edges'].append({'source':'C','target':'N','type':'verifiedBy'})
        self.assertIn('type-violation:C:verifiedBy:N',validate_model(self.model))
    def test_broken(self):
        self.model['edges'].append({'source':'R','target':'nope','type':'verifiedBy'})
        self.assertIn('broken-edge:R:nope',validate_model(self.model))
    def test_duplicate(self):
        self.model['nodes'].append({'id':'N','type':'Need'})
        self.assertIn('duplicate-node-id',validate_model(self.model))
    def test_unknown_type(self):
        self.model['nodes'].append({'id':'X','type':'Weird'})
        self.assertIn('unknown-node-type:X',validate_model(self.model))
    def test_energy(self):self.assertAlmostEqual(energy_margin(24,24,.62,1.8,4),3.32)
    def test_energy_adverse(self):self.assertAlmostEqual(energy_margin(24,24,.75,1.8,4),.2)
    def test_energy_negative(self):
        with self.assertRaises(ValueError):energy_margin(24,-1,.6,2,4)
    def test_route_fresh(self):self.assertTrue(route_status_ok('OPEN',101,105,5))
    def test_route_stale(self):self.assertFalse(route_status_ok('OPEN',101,107,5))
    def test_route_future(self):self.assertFalse(route_status_ok('OPEN',108,107,5))
    def test_route_closed(self):self.assertFalse(route_status_ok('CLOSED',105,105,5))
    def test_reserve_success(self):self.assertEqual(ReservationBook(['V']).reserve('a','r1','V'),'ASSIGNED:V')
    def test_reserve_duplicate(self):
        b=ReservationBook(['V']);self.assertEqual(b.reserve('a','r1','V'),b.reserve('a','r1','V'))
        self.assertEqual(len(b.busy),1)
    def test_reserve_conflict(self):
        b=ReservationBook(['V']);b.reserve('a','r1','V')
        with self.assertRaises(ValueError):b.reserve('a','r2','V')
    def test_reserve_exclusive(self):
        b=ReservationBook(['V']);b.reserve('a','r1','V')
        self.assertEqual(b.reserve('b','r2','V'),'REJECTED:vehicle-unavailable')
    def test_reserve_unknown(self):
        with self.assertRaises(ValueError):ReservationBook(['V']).reserve('a','r1','x')
    def test_series(self):self.assertAlmostEqual(series_reliability([.9,.8]),.72)
    def test_common(self):self.assertAlmostEqual(parallel_with_common_cause(.95,.03),.967575)
    def test_common_no_common(self):self.assertAlmostEqual(parallel_with_common_cause(.95,0),.9975)
    def test_common_invalid(self):
        with self.assertRaises(ValueError):parallel_with_common_cause(1.2,.03)
    def test_zero(self):self.assertAlmostEqual(zero_failure_upper(30),.0950338529)
    def test_min_sample(self):self.assertEqual(min_trials_for_upper(.01),299)
    def test_zero_invalid(self):
        with self.assertRaises(ValueError):zero_failure_upper(0)
    def test_evidence_good(self):self.assertEqual(check_evidence([{'requirement':'R','test_id':'T','evidence_id':'E','revision':'v1','status':'PASS'}],'v1'),[])
    def test_evidence_revision(self):self.assertEqual(check_evidence([{'requirement':'R','test_id':'T','evidence_id':'E','revision':'v1','status':'PASS'}],'v2'),[('R','stale-revision')])
    def test_evidence_failed(self):self.assertEqual(check_evidence([{'requirement':'R','test_id':'T','evidence_id':'E','revision':'v2','status':'FAIL'}],'v2'),[('R','nonpass')])
    def test_evidence_missing(self):self.assertEqual(check_evidence([{'requirement':'R','test_id':'','evidence_id':'E','revision':'v2','status':'PASS'}],'v2'),[('R','missing-evidence-reference')])

if __name__=='__main__':unittest.main()
