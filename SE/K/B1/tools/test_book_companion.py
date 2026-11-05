import unittest
from pathlib import Path
from service_measures import from_csv as measures,compute
from trace_audit import from_csv as trace
from confidence import wilson_lower
P=Path(__file__).resolve().parents[1] / 'data'

class BookExercises(unittest.TestCase):
    def test_total(self):
        x=measures(P/'request-outcomes.csv')['ALL']
        self.assertEqual((x['eligible'],x['completed'],x['timely']),(16,12,10))
        self.assertAlmostEqual(x['timely_given_completed'],10/12)
        self.assertAlmostEqual(x['timely_given_eligible'],10/16)
    def test_evening_denominator(self):
        x=measures(P/'request-outcomes.csv')['evening']
        self.assertEqual((x['eligible'],x['completed'],x['timely']),(8,4,4))
        self.assertAlmostEqual(x['timely_given_completed'],1.0)
        self.assertAlmostEqual(x['timely_given_eligible'],0.5)
    def test_day(self):
        x=measures(P/'request-outcomes.csv')['day']
        self.assertEqual((x['eligible'],x['completed'],x['timely']),(8,8,6))
    def test_no_completed_while_timely(self):
        with self.assertRaises(ValueError):
            compute([dict(eligible='1',completed='0',timely='1',period='x')])
    def test_trace_gaps(self):
        a=trace(P/'requirements-clinic.csv')
        self.assertEqual(a['count'],6)
        self.assertEqual(set(a['critical_without_test']),{'R-01','R-06'})
        self.assertIn('R-03',a['missing_source'])
    def test_wilson(self):
        self.assertAlmostEqual(wilson_lower(992,1000),0.985858359,places=7)
        self.assertLess(wilson_lower(992,1000),0.99)
    def test_wilson_bounds(self):
        self.assertGreaterEqual(wilson_lower(0,100),0)
        self.assertLess(wilson_lower(100,100),1)
        with self.assertRaises(ValueError):wilson_lower(101,100)
    def test_wilson_confidence(self):
        self.assertLess(wilson_lower(99,100,0.99),wilson_lower(99,100,0.95))

if __name__=='__main__':unittest.main()
