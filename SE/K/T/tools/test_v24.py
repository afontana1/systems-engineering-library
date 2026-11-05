"""Self-checking lab arithmetic without third-party dependencies."""
import unittest, math
from hazard_checks import authorized
from clearance import permit
from factorial import effects
from reliability import mission_reliability,availability,series,parallel
from robust_choice import evaluate
from lifecycle import present_cost,annuity_factor

class TestMethods(unittest.TestCase):
    def test_zone_accept(self):self.assertTrue(authorized(12,8,True))
    def test_zone_stale(self):self.assertFalse(authorized(12,4,True))
    def test_zone_invalid_clock(self):self.assertFalse(authorized(4,8,True))
    def test_zone_missing_signature(self):self.assertFalse(authorized(12,8,True,False))
    def test_zone_wrong_revision(self):self.assertFalse(authorized(12,8,True,True,False))
    def test_clearance(self):
        m=dict(signature_valid=True,route='R1',revision=19,issued_at=10,action='CLEAR')
        self.assertTrue(permit(m,'R1',19,12,True))
        self.assertFalse(permit(m,'R1',20,12,True))
        self.assertFalse(permit(m,'R1',19,20,True))
    def test_factorial(self):
        r=[dict(vehicles=x,policy=p,wait_min=y) for x,p,y in [(1,'FCFS',38),(1,'PRIORITY',30),(2,'FCFS',22),(2,'PRIORITY',18)]]
        v=effects(r)
        self.assertAlmostEqual(v['fleet_effect'],-14)
        self.assertAlmostEqual(v['policy_effect'],-6)
        self.assertAlmostEqual(v['interaction'],4)
    def test_reliability(self):
        self.assertAlmostEqual(mission_reliability(500,10),math.exp(-.02))
        self.assertAlmostEqual(availability(500,5),500/505)
        self.assertAlmostEqual(series(.95,.95),.9025)
        self.assertAlmostEqual(parallel(.95,.95),.9975)
    def test_reliability_errors(self):
        with self.assertRaises(ValueError):mission_reliability(0,1)
        with self.assertRaises(ValueError):parallel(1.2,.3)
    def test_robust(self):
        o=[('A',6,12,2),('B',12,24,4),('C',18,36,5)]
        self.assertEqual([v['name'] for v in evaluate(o) if v['feasible']],['B'])
        self.assertEqual([v['name'] for v in evaluate(o,service_multiplier=2/3) if v['feasible']],[])
    def test_pv(self):
        self.assertAlmostEqual(present_cost(1000,200,3,.05),1544.649606,places=4)
        self.assertAlmostEqual(present_cost(1200,110,3,.05),1499.557283,places=4)
        self.assertAlmostEqual(annuity_factor(3,.05),2.723248,places=5)
    def test_zero_discount(self):self.assertEqual(present_cost(100,10,3,0),130)

if __name__=='__main__':unittest.main(verbosity=2)
