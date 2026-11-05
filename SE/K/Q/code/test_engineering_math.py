import math, unittest
from engineering_math import *
class Tests(unittest.TestCase):
 def test_probability(self): self.assertAlmostEqual(poisson_zero(8,.25),math.exp(-2))
 def test_gamma(self): self.assertAlmostEqual(posterior_gamma_mean(2,.2,120,10),122/10.2)
 def test_gamma_invalid(self):
  with self.assertRaises(ValueError):posterior_gamma_mean(-1,1,2,3)
 def test_zero30(self): self.assertAlmostEqual(zero_failure_upper(30),.0950338529,places=7)
 def test_zero100(self): self.assertAlmostEqual(zero_failure_upper(100),.0295130496,places=7)
 def test_zero_invalid(self):
  with self.assertRaises(ValueError): zero_failure_upper(0)
 def test_queue(self):
  r=mm1(8,10);self.assertAlmostEqual(r['minutes_in_queue'],24);self.assertAlmostEqual(r['minutes_in_system'],30)
 def test_queue_heavy(self): self.assertAlmostEqual(mm1(9,10)['minutes_in_system'],60)
 def test_queue_unstable(self):
  with self.assertRaises(ValueError): mm1(10,10)
 def test_factorial(self): self.assertEqual(factorial_effects(18,14,12,7),(-6.5,-4.5,-1,-.25))
 def test_decay(self): self.assertAlmostEqual(decay_exact(100,.5,2),36.7879441171)
 def test_euler(self): self.assertAlmostEqual(euler_decay(100,.5,1,2),25)
 def test_euler_fine(self): self.assertAlmostEqual(euler_decay(100,.5,.25,8),100*.875**8)
 def test_control(self):self.assertAlmostEqual(control_multiplier(.4,1,1.6,.25),.5)
 def test_control_limit(self):self.assertEqual(control_multiplier(.4,1,1.6,1),-1)
 def test_expected(self): self.assertEqual(expected_values(.3)['prefer'],'A')
 def test_evpi(self):self.assertAlmostEqual(expected_values(.3)['EVPI'],12)
 def test_cross(self):self.assertAlmostEqual(expected_values(25/65)['A'],expected_values(25/65)['B'])
 def test_linear(self):self.assertAlmostEqual(linear_uncertainty(.1,.3),math.sqrt(.13))
 def test_deterministic(self):self.assertEqual([x['wait'] for x in deterministic_queue([0,1,2],2)],[0,1,2])
 def test_negative(self):
  with self.assertRaises(ValueError):poisson_zero(-1,1)
 def test_multi_wait(self):self.assertEqual(deterministic_queue([0],2)[0]['finish'],2)
if __name__=='__main__':unittest.main()
