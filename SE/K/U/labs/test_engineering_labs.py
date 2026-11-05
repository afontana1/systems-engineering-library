import unittest
from math import exp
from engineering_labs import *

class TestEngineeringLabs(unittest.TestCase):
 def test_zero100(self):self.assertAlmostEqual(zero_failure_upper_bound(100),0.0295130496,places=8)
 def test_zero300(self):self.assertAlmostEqual(zero_failure_upper_bound(300),1-0.05**(1/300))
 def test_zero_validation(self):
  with self.assertRaises(ValueError):zero_failure_upper_bound(0)
 def test_factorial_A(self):self.assertEqual(factorial_2x2(7,5,15,10)['A_effect'],-3.5)
 def test_factorial_B(self):self.assertEqual(factorial_2x2(7,5,15,10)['B_effect'],6.5)
 def test_factorial_interaction(self):self.assertEqual(factorial_2x2(7,5,15,10)['interaction_contrast'],-3)
 def test_pareto(self):self.assertEqual(pareto_indices([(560,11,97),(470,13,98)],(True,True,False)),[0,1])
 def test_pareto_domination(self):self.assertEqual(pareto_indices([(2,4),(3,5),(2,4)],(True,True)),[0,2])
 def test_pareto_validation(self):
  with self.assertRaises(ValueError):pareto_indices([(1,2)],(True,))
 def test_evpi(self):
  a,b,c,d=expected_value_perfect_info([.5,.5],[[100,20],[65,65]])
  self.assertEqual((a,b,c,d),(1,65,82.5,17.5))
 def test_evpi_nonnegative(self):self.assertGreaterEqual(expected_value_perfect_info([1],[[0],[3]])[-1],0)
 def test_evpi_bad_weights(self):
  with self.assertRaises(ValueError):expected_value_perfect_info([.4,.4],[[1,2]])
 def test_mm1_low(self):self.assertAlmostEqual(mm1_mean_system_time(9,15)*60,10)
 def test_mm1_high(self):self.assertAlmostEqual(mm1_mean_system_time(14,15)*60,60)
 def test_mm1_unstable(self):
  with self.assertRaises(ValueError):mm1_mean_system_time(15,15)
 def test_little(self):self.assertEqual(little_law_wip(8/24,3*24),24)
 def test_euler1(self):self.assertEqual(euler_decay(100,.5,1,1)[0],50)
 def test_euler2(self):self.assertEqual(euler_decay(100,.5,.5,2)[0],56.25)
 def test_euler_exact(self):self.assertAlmostEqual(euler_decay(100,.5,1,1)[1],100*exp(-.5))
 def test_critical(self):
  tasks={'A':(2,[]),'B':(4,['A']),'C':(3,['A']),'D':(2,['B','C']),'E':(1,['D'])}
  self.assertEqual(simple_critical_path(tasks),(9,['A','B','D','E']))
 def test_critical_cycle(self):
  with self.assertRaises(ValueError):simple_critical_path({'A':(1,['B']),'B':(1,['A'])})
 def test_reliability_series(self):self.assertAlmostEqual(reliability_series([.98,.98]),.9604)
 def test_reliability_parallel(self):self.assertAlmostEqual(reliability_parallel([.98,.98]),.9996)
 def test_did(self):self.assertAlmostEqual(difference_in_differences(.80,.89,.83,.87),.05)
 def test_audit(self):
  result=audit_traceability({'R1','R2','R3'},{'T1','T2'},{'E1'},[('R1','verified_by','T1'),('T1','produces','E1'),('R2','verified_by','T2')])
  self.assertEqual(result['no_verification_method'],['R3'])
  self.assertEqual(result['no_evidence_chain'],['R2'])
 def test_queue_seed(self):self.assertEqual(simulate_mm1(9,15,200,7),simulate_mm1(9,15,200,7))
 def test_queue_wait(self):
  r=simulate_mm1(9,15,30000,10)
  self.assertAlmostEqual(r['mean_system_time_h'],1/6,delta=.025)
if __name__=='__main__':unittest.main()
