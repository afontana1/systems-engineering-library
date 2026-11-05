import unittest
from model_graph import ModelGraph,ModelError,sample
from trip_domain import Trip,Status
from reservation_service import ReservationService
from performance_budget import margin_ms,little_law,downtime_minutes

class CompanionTests(unittest.TestCase):
    def test_model_queries(self):
        g=sample();self.assertIn('N-1',g.impact('R-1'))
        self.assertIn('T-1',g.impact('R-1'))
        self.assertEqual(g.orphan_requirements(),[])
    def test_duplicate_id(self):
        g=ModelGraph();g.element('R','Requirement','r')
        with self.assertRaises(ModelError):g.element('R','Requirement','r')
    def test_dangling_link(self):
        g=ModelGraph();g.element('R','Requirement','r')
        with self.assertRaises(ModelError):g.link('R','verifiedBy','MISSING')
    def test_trip_legal_path(self):
        t=Trip('17',active_assignment='V-1')
        for event in ('confirm','board','finish'):t.apply(event)
        self.assertEqual(t.status,Status.COMPLETED)
        self.assertIsNone(t.active_assignment)
    def test_trip_rejects_illegal_event(self):
        t=Trip('17')
        with self.assertRaises(ValueError):t.apply('finish')
    def test_trip_requires_assignment(self):
        t=Trip('17')
        with self.assertRaises(ValueError):t.apply('confirm')
    def test_idempotency(self):
        s=ReservationService(['V1']);a=s.reserve('same','T1','V1');b=s.reserve('same','T1','V1')
        self.assertEqual(a,b);self.assertTrue(a.accepted);self.assertEqual(len(s.assigned),1)
    def test_same_token_modified_request(self):
        s=ReservationService(['V1']);s.reserve('same','T1','V1')
        with self.assertRaises(ValueError):s.reserve('same','T2','V1')
    def test_no_double_booking(self):
        s=ReservationService(['V1']);self.assertTrue(s.reserve('a','T1','V1').accepted)
        self.assertFalse(s.reserve('b','T2','V1').accepted)
    def test_budget(self):self.assertEqual(margin_ms(900,{'a':650}),250)
    def test_little(self):self.assertEqual(little_law(25,0.4),10)
    def test_downtime(self):self.assertAlmostEqual(downtime_minutes(.999,30),43.2)
if __name__=='__main__':unittest.main()
