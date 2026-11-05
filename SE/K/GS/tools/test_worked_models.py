import unittest
from worked_models import *
class ModelsTest(unittest.TestCase):
    def test_evm(self):
        x=earned_value(3.2,4.,4.,9.);self.assertAlmostEqual(x['cpi'],.8);self.assertAlmostEqual(x['eac'],11.25)
    def test_evm_boundary(self):
        with self.assertRaises(AssertionError):earned_value(1,0,2,3)
    def test_energy(self):self.assertAlmostEqual(energy_margin(120,.8,10,2,180,.9,.9,20),9.8)
    def test_energy_sensitivity(self):self.assertAlmostEqual(energy_margin(120,.9,10,2,180,.9,.9,20),-2.2)
    def test_guard(self):self.assertAlmostEqual(guard_time(45,30,6),2.5)
    def test_guard_invalid(self):
        with self.assertRaises(AssertionError):guard_time(20,30,6)
    def test_euler_good(self):self.assertAlmostEqual(euler_multiplier(.6,1),.4)
    def test_euler_bad(self):self.assertAlmostEqual(euler_multiplier(.6,4),-1.4)
    def test_evpi(self):
        x=evpi(.3,90,40,75,70);self.assertAlmostEqual(x['a'],75);self.assertAlmostEqual(x['b'],73.5);self.assertAlmostEqual(x['evpi'],9)
    def test_evpi_zero(self):self.assertAlmostEqual(evpi(0,90,40,75,70)['evpi'],0)
    def test_flow(self):self.assertAlmostEqual(flow_time(24,8),3)
    def test_flow_invalid(self):
        with self.assertRaises(AssertionError):flow_time(24,0)
    def test_evidence_stale(self):self.assertFalse(evidence_freshness(108,100,5))
    def test_evidence_current(self):self.assertTrue(evidence_freshness(105,100,5))
    def test_did(self):self.assertEqual(diff_in_diff(18,11,15,12),-4)
    def test_did_neutral(self):self.assertEqual(diff_in_diff(18,11,18,11),0)
    def test_mission(self):
        x=mission_availability(.95,.95,.8,.03);self.assertAlmostEqual(x['independent'],.9805);self.assertAlmostEqual(x['with_common'],.951085)
    def test_common_zero(self):self.assertAlmostEqual(mission_availability(.95,.95,.8,0)['with_common'],.9805)
    def test_portfolio(self):
        x=portfolio_value([3,4,2],[7,6,4],6);self.assertEqual(x,(11,(1,0,1)))
    def test_portfolio_dependency(self):
        x=portfolio_value([3,4,2],[7,6,4],6,[(0,1)]);self.assertEqual(x,(10,(0,1,1)))
    def test_delay(self):
        x=group_delay(.8,[12,20],[8,32]);self.assertAlmostEqual(x['before'],13.6);self.assertAlmostEqual(x['after'],12.8);self.assertEqual(x['rural_change'],12)
    def test_delay_equal(self):self.assertAlmostEqual(group_delay(.8,[8,8],[8,8])['after'],8)
if __name__=='__main__':unittest.main()
