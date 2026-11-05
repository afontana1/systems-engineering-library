import math
import tempfile
from pathlib import Path
import unittest
from graduate_models import *

class GraduateCalculations(unittest.TestCase):
    def test_feasible_1(self):self.assertFalse(feasible(98,18))
    def test_feasible_2(self):self.assertTrue(feasible(112,14))
    def test_feasible_3(self):self.assertTrue(feasible(105,16))
    def test_feasible_4(self):self.assertFalse(feasible(105,16.01))
    def test_score_1(self):self.assertAlmostEqual(score_difference(.4),0)
    def test_score_2(self):self.assertLess(score_difference(.25),0)
    def test_score_3(self):self.assertGreater(score_difference(.6),0)
    def test_score_4(self):
        with self.assertRaises(ValueError):score_difference(2)
    def test_bayes_1(self):self.assertAlmostEqual(posterior(.25,.85,.9)[0],.2875)
    def test_bayes_2(self):self.assertAlmostEqual(posterior(.25,.85,.9)[1],.73913043478)
    def test_bayes_3(self):self.assertAlmostEqual(posterior(.25,.85,.9)[2],.05263157895)
    def test_bayes_4(self):
        before,after=expected_test_cost();self.assertAlmostEqual(before,.436);self.assertAlmostEqual(after,.2654,places=3)
    def test_budget_1(self):self.assertEqual(deterministic_budget((120,240,170,90),600),-20)
    def test_budget_2(self):self.assertEqual(deterministic_budget((85,210,150,80),600),75)
    def test_budget_3(self):self.assertAlmostEqual(quantile_joint_guarantee((.01,)*4),.96)
    def test_budget_4(self):
        with self.assertRaises(ValueError):deterministic_budget((-1,2),4)
    def test_upper_1(self):self.assertAlmostEqual(zero_failure_upper(60),.0487029,places=5)
    def test_upper_2(self):self.assertEqual(required_zero_failure_trials(.01),299)
    def test_upper_3(self):self.assertGreater(zero_failure_upper(10),zero_failure_upper(100))
    def test_upper_4(self):
        with self.assertRaises(ValueError):zero_failure_upper(0)
    def test_pair_1(self):self.assertAlmostEqual(paired_summary([5,9,7,11],3.182)[0],8)
    def test_pair_2(self):self.assertAlmostEqual(paired_summary([5,9,7,11],3.182)[1],3.892,places=2)
    def test_pair_3(self):self.assertAlmostEqual(paired_summary([5,9,7,11],3.182)[2],12.108,places=2)
    def test_pair_4(self):
        with self.assertRaises(ValueError):paired_summary([5],2)
    def test_queue_1(self):self.assertAlmostEqual(mm1(8,10)[0],.8)
    def test_queue_2(self):self.assertAlmostEqual(mm1(8,10)[1],.5)
    def test_queue_3(self):self.assertAlmostEqual(mm1(8,10)[2],.4)
    def test_queue_4(self):
        with self.assertRaises(ValueError):mm1(10,10)
    def test_coverage_1(self):
        rows=[{'linked':True,'passing':True,'threshold':True,'evidence':True,'revision':'v2'} for _ in range(3)]
        rows += [{'linked':True,'passing':True,'threshold':False,'evidence':True,'revision':'v2'} for _ in range(2)]
        rows += [{'linked':True,'passing':False,'threshold':True,'evidence':True,'revision':'v2'} for _ in range(1)]
        rows += [{'linked':True,'passing':True,'threshold':True,'evidence':True,'revision':'v1'} for _ in range(4)]
        self.assertEqual(coverage(rows,'v2'),(1.0,.3))
    def test_coverage_2(self):
        with self.assertRaises(ValueError):coverage([],'v1')
    def test_did_1(self):self.assertEqual(difference_in_differences(22,16,20,18),-4)
    def test_did_2(self):self.assertEqual(difference_in_differences(1,1,1,1),0)
    def test_workforce_1(self):self.assertEqual(workforce_step(40,5,2,1),42)
    def test_workforce_2(self):
        with self.assertRaises(ValueError):workforce_step(1,0,2,0)
    def test_digest_1(self):
        with tempfile.TemporaryDirectory() as t:
            f=Path(t)/'x';f.write_text('a');old=digest(f);f.write_text('b');self.assertNotEqual(old,digest(f))

if __name__=='__main__':unittest.main()
