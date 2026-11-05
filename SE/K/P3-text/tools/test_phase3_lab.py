"""Run with: python -m unittest discover -s tools -p 'test_*.py'"""
import math
import unittest
from phase3_lab import (mean_interval_normal,factorial_2x2,correlated_sum_mc,mm1_metrics,
                        deterministic_queue,des_queue,stock_flow,euler_cooling,pareto_min,
                        expected_value_and_evpi,sample_cost_npv,write_demo_csv)

class MathTests(unittest.TestCase):
    def test_interval_center(self):
        self.assertAlmostEqual(mean_interval_normal([4,5,6])[1],5)
    def test_interval_positive_width(self):
        lo,mid,hi=mean_interval_normal([1,2,3,4]);self.assertLess(lo,mid);self.assertGreater(hi,mid)
    def test_interval_reject_single(self):
        with self.assertRaises(ValueError):mean_interval_normal([1])
    def test_effect_a(self):
        self.assertAlmostEqual(factorial_2x2(2,6,2,6)['A_effect'],4)
    def test_effect_interaction(self):
        self.assertAlmostEqual(factorial_2x2(1,1,1,3)['AB_effect'],1)
    def test_mc_reproducible(self):
        self.assertEqual(correlated_sum_mc(200,seed=4),correlated_sum_mc(200,seed=4))
    def test_mc_analytic_dependence(self):
        self.assertAlmostEqual(correlated_sum_mc(200,rho=1)['analytic_sd'],3)
    def test_mm1_little(self):
        v=mm1_metrics(8,12);self.assertAlmostEqual(v['L'],8*v['W'])
    def test_mm1_reject_unstable(self):
        with self.assertRaises(ValueError):mm1_metrics(12,12)
    def test_queue_simple(self):
        self.assertEqual(deterministic_queue([0,1,2],3)['waits'],[0,2,4])
    def test_des_matches_known(self):
        self.assertEqual(des_queue([0,1,2],[3,3,3])['waits'],[0,2,4])
    def test_des_departures(self):
        self.assertEqual(des_queue([0,1,2],[3,3,3])['departures'],[3,6,9])
    def test_des_zero(self):
        self.assertEqual(des_queue([],[])['departures'],[])
    def test_stock_conserve_growth(self):
        self.assertAlmostEqual(stock_flow(5,12,10,hours=4)[-1][1],13)
    def test_stock_nonnegative(self):
        self.assertGreaterEqual(stock_flow(1,0,10,hours=3)[-1][1],0)
    def test_cooling_refinement(self):
        self.assertLess(euler_cooling(step_min=.1)['abs_error'],euler_cooling(step_min=1)['abs_error'])
    def test_cooling_analytic(self):
        self.assertAlmostEqual(euler_cooling()['exact'],20+30*math.exp(-1))
    def test_pareto(self):
        self.assertEqual(pareto_min([(900,15),(1000,12),(1100,14)]),[0,1])
    def test_pareto_duplicate(self):
        self.assertEqual(pareto_min([(1,1),(1,1)]),[0,1])
    def test_evpi(self):
        r=expected_value_and_evpi([[50,-20],[25,25]],[.5,.5]);self.assertEqual(r['best_action_index'],1)
        self.assertAlmostEqual(r['EVPI'],12.5)
    def test_evpi_nonnegative(self):
        self.assertGreaterEqual(expected_value_and_evpi([[3,0],[0,1]],[.4,.6])['EVPI'],-1e-9)
    def test_npv(self):
        self.assertAlmostEqual(sample_cost_npv(100,50,2,0),0)
    def test_discount(self):
        self.assertLess(sample_cost_npv(0,20,4,.1),sample_cost_npv(0,20,4,0))
    def test_demo_file(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as p:
            dest=write_demo_csv(Path(p)/'x.csv');self.assertEqual(len(dest.read_text().splitlines()),25)

if __name__=='__main__':unittest.main()
