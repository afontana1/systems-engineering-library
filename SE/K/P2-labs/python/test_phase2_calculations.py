import unittest
from math import isclose
from phase2_calculations import *
class TestCalculations(unittest.TestCase):
    def test_latency(self): self.assertEqual(latency_budget(.2,.4,.7,.5,.2,deadline=2)['margin_s'],0)
    def test_latency_over(self): self.assertFalse(latency_budget(.2,.4,.7,.5,.5,deadline=2)['meets_nominal'])
    def test_latency_bad(self):
        with self.assertRaises(ValueError):latency_budget(-1,deadline=2)
    def test_energy(self):self.assertAlmostEqual(energy_window(32,60,1200),1.6)
    def test_energy_derate(self):self.assertAlmostEqual(energy_window(32,60,900),1920/900)
    def test_energy_zero(self):
        with self.assertRaises(ValueError):energy_window(32,60,0)
    def test_backlog(self):self.assertEqual(throughput_backlog(8,6,3),6)
    def test_backlog_zero(self):self.assertEqual(throughput_backlog(5,6,3),0)
    def test_backlog_invalid(self):
        with self.assertRaises(ValueError):throughput_backlog(-1,6,3)
    def test_series(self):self.assertAlmostEqual(series_reliability([.99,.98]),.9702)
    def test_series_none(self):self.assertEqual(series_reliability([]),1)
    def test_series_invalid(self):
        with self.assertRaises(ValueError):series_reliability([1.01])
    def test_availability(self):self.assertAlmostEqual(intrinsic_availability(100,5),100/105)
    def test_availability_invalid(self):
        with self.assertRaises(ValueError):intrinsic_availability(0,5)
    def test_zero_failure(self):self.assertAlmostEqual(zero_failure_upper(30),.09503385285530419)
    def test_zero_failure_invalid(self):
        with self.assertRaises(ValueError):zero_failure_upper(0)
    def test_score(self):self.assertAlmostEqual(weighted_value([.8,.6],[.25,.75]),.65)
    def test_score_weights(self):
        with self.assertRaises(ValueError):weighted_value([.8,.6],[.5,.3])
    def test_mean(self):self.assertEqual(mean([2,3,4]),3)
    def test_mean_empty(self):
        with self.assertRaises(ValueError):mean([])
    def test_percentile(self):self.assertEqual(nearest_rank([1,2,3,4,5],.9),5)
    def test_percentile_low(self):self.assertEqual(nearest_rank([1,2,3,4,5],.01),1)
    def test_coverage(self):self.assertAlmostEqual(coverage({'a':['T1'],'b':[],'c':['T2']}),2/3)
    def test_coverage_empty(self):
        with self.assertRaises(ValueError):coverage({})
    def test_nonrobust(self):self.assertEqual(compare_decision(.73,.72,.04)['robust_order'],'unresolved')
    def test_robust(self):self.assertEqual(compare_decision(.73,.62,.04)['robust_order'],'first')
if __name__=='__main__': unittest.main()
