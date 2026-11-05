import unittest
from mission_capacity import cycles,boardings
from timing_budget import serial_budget
from concept_trade import evaluate,tie_weight
from reliability import serial_independent,parallel_independent,simple_common_cause,inherent_availability
from test_statistics import zero_failure_upper_bound,nearest_rank_percentile,pass_fraction
from factorial_experiment import effects

class Checks(unittest.TestCase):
    def test_capacity(self): self.assertAlmostEqual(cycles(2,480,.85,24),34)
    def test_boardings(self): self.assertAlmostEqual(boardings(2,480,.85,24,3),102)
    def test_bad_cycle(self):
        with self.assertRaises(ValueError):cycles(2,480,.85,0)
    def test_timing(self): self.assertEqual(serial_budget({'a':80,'b':570},900)['nominal_margin_ms'],250)
    def test_tie(self): self.assertAlmostEqual(tie_weight(.9,.4,.7,.8),2/3)
    def test_weights(self):
        with self.assertRaises(ValueError):evaluate({'a':{'x':.5}},{'x':.2},{})
    def test_hard_gate(self):self.assertFalse(evaluate({'a':{'x':.5}},{'x':1},{'gate':lambda x:False})[0][1])
    def test_serial(self):self.assertAlmostEqual(serial_independent([.98,.98]),.9604)
    def test_parallel(self):self.assertAlmostEqual(parallel_independent([.98,.98]),.9996)
    def test_common_cause(self):self.assertAlmostEqual(simple_common_cause([.98,.98],.99),.989604)
    def test_availability(self):self.assertAlmostEqual(inherent_availability(500,5),500/505)
    def test_zero_bound(self):self.assertAlmostEqual(zero_failure_upper_bound(100),.0295130496,places=8)
    def test_99th(self):self.assertEqual(nearest_rank_percentile([1,2,3,4,5],.99),5)
    def test_outcomes(self):self.assertAlmostEqual(pass_fraction([True,False,True]),2/3)
    def test_factorial(self): self.assertEqual(effects(15,10,12,7),{'effect_A':-5,'effect_B':-3,'difference_of_differences':0})
    def test_interaction(self): self.assertEqual(effects(15,11,12,5)['difference_of_differences'],-3)

if __name__=='__main__':unittest.main()
