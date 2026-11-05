import unittest
from decision_audit import weighted_scores, pairwise_threshold, winners
from verification_audit import audit
from freshness_check import is_fresh, evaluate

class TestBookV14(unittest.TestCase):
    def test_trade_nominal(self):
        s=weighted_scores();self.assertAlmostEqual(s['Central turnkey'],70);self.assertAlmostEqual(s['Federated integration'],74.5);self.assertAlmostEqual(s['Local demonstrator'],73.5)
    def test_weight_threshold(self):self.assertAlmostEqual(pairwise_threshold(),23/55)
    def test_invalid_weights(self):
        with self.assertRaises(ValueError):weighted_scores((0.4,0.4,0.4))
    def test_weight_winner(self):self.assertEqual(list(winners([.5]))[0][1],'Federated integration')
    def test_uncertain_resilience(self):
        rows=[dict(concept='Federated integration',resilience='70',affordability='60',maintainability='70')]
        self.assertAlmostEqual(weighted_scores(rows=rows)['Federated integration'],67)
    def test_review_audit(self):
        x=audit();self.assertEqual(x['total'],24);self.assertEqual(x['planned'],24);self.assertEqual(x['passed'],18);self.assertEqual(x['unresolved'],6)
    def test_freshness(self):self.assertTrue(is_fresh(0,5));self.assertFalse(is_fresh(0,5.1))
    def test_delay_case(self):self.assertFalse(dict(evaluate())['E-02'])
    def test_invalid_clock(self):
        with self.assertRaises(ValueError):is_fresh(6,5)

if __name__=='__main__':unittest.main()
