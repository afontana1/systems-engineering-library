import unittest
from math import isclose
from system_models import *

class GraduateModelsTest(unittest.TestCase):
    def test_age(self): self.assertEqual(conservative_age(18,4,7,3),32)
    def test_age_fail(self):
        with self.assertRaises(ValueError): conservative_age(1,1,1,-1)
    def test_allow_fresh(self): self.assertTrue(authorize(20,0,30,3))
    def test_reject_stale(self): self.assertFalse(authorize(29,0,30,3))
    def test_reject_unsigned(self): self.assertFalse(authorize(5,0,30,signature_valid=False))
    def test_reject_revision(self): self.assertFalse(authorize(5,0,30,current_revision=False))
    def test_reject_future_observation(self): self.assertFalse(authorize(0,1,30))
    def test_queue(self): self.assertAlmostEqual(mm1(5,8)['wait_queue_h']*60,12.5)
    def test_queue_system(self): self.assertAlmostEqual(mm1(5,8)['time_system_h']*60,20)
    def test_queue_high_load(self): self.assertAlmostEqual(mm1(7,8)['wait_queue_h']*60,52.5)
    def test_unstable_queue(self):
        with self.assertRaises(ValueError): mm1(8,8)
    def test_ppv(self): self.assertAlmostEqual(alarm_ppv(.01,.95,.05),.0095/(.0095+.0495))
    def test_ppv_zero_alarm(self):
        with self.assertRaises(ValueError):alarm_ppv(0,.9,0)
    def test_reservation_repeat(self):
        r=ReservationService(1);self.assertEqual(r.reserve('r','payload'),'CONFIRMED');self.assertEqual(r.reserve('r','payload'),'CONFIRMED');self.assertEqual(r.capacity,0)
    def test_reservation_mismatch(self):
        r=ReservationService(1);r.reserve('r','p');self.assertEqual(r.reserve('r','other'),'CONFLICT')
    def test_reservation_full(self):
        r=ReservationService(0);self.assertEqual(r.reserve('r','p'),'FULL')
    def test_retry(self): self.assertAlmostEqual(retry_amplification(80,.25,100)['offered'],80/.75)
    def test_retry_instability(self): self.assertFalse(retry_amplification(80,.25,100)['stable'])
    def test_serial(self): self.assertAlmostEqual(serial_availability(.995,.995,.995),.995**3)
    def test_parallel(self): self.assertAlmostEqual(parallel_common_cause(.98,.01),.989604)
    def test_parallel_2(self): self.assertAlmostEqual(parallel_common_cause(.98,.02),.979608)
    def test_budget(self):self.assertAlmostEqual(error_budget(300000,.9995),150)
    def test_paths(self): self.assertAlmostEqual(any_path_available(.9,.8),.98)
    def test_bad_probability(self):
        with self.assertRaises(ValueError): any_path_available(1.1,.8)
    def test_graph(self):self.assertTrue(reachable([('O','A'),('A','H'),('O','B'),('B','H')],'O','H'))
    def test_graph_cut(self):self.assertFalse(reachable([('O','A'),('A','H')],'O','H',{'A'}))
    def test_graph_alt(self):self.assertTrue(reachable([('O','A'),('A','H'),('O','B'),('B','H')],'O','H',{'A'}))
    def test_bayes(self):self.assertEqual(beta_bernoulli_update(1,9,2,18),(3,27,.1))
    def test_backlog(self):self.assertEqual(backlog(8,12,10,4),16)
    def test_backlog_floor(self):self.assertEqual(backlog(0,0,100,10),0)
    def test_subgroup(self):self.assertAlmostEqual(subgroup_mean([(90,8),(10,35)]),10.7)
    def test_subgroup_other(self):self.assertAlmostEqual(subgroup_mean([(80,9),(20,30)]),13.2)
    def test_did(self):self.assertAlmostEqual(difference_in_differences(24,17,20,18),-5)
    def test_did2(self):self.assertAlmostEqual(difference_in_differences(30,20,25,22),-7)

if __name__=='__main__':unittest.main()
