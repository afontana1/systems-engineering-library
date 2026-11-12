"""Independent numerical, boundary and evidence checks for synthetic NS-QSE4.1."""
import copy, hashlib, json, math, tempfile, unittest
from pathlib import Path
from ns_qse_case import (INPUT,aggregate,control_multiplier,daily_results,evidence_comparison,
    generate_arrivals,load,mixture_moments,paired_bootstrap_delta,posterior_summary,
    quantile,queue,run,save,thermal_euler,thermal_exact,validate)

CFG=load()
class ModelTests(unittest.TestCase):
    def test_inputs(self):
        self.assertEqual(sum(CFG['counts']['clear']),120)
        self.assertEqual(sum(CFG['counts']['storm']),216)
        self.assertEqual(len(CFG['counts']['storm']),12)
        self.assertEqual(sum(CFG['scenario_weights'].values()),1)
    def test_rates(self):
        a=posterior_summary(CFG['counts']['clear'],CFG['gamma_prior'],700)
        b=posterior_summary(CFG['counts']['storm'],CFG['gamma_prior'],701)
        self.assertAlmostEqual(a['posterior_mean_per_hour'],10)
        self.assertAlmostEqual(b['posterior_mean_per_hour'],218/12.2)
        self.assertTrue(a['conditional_95pct_interval_per_hour'][0]<a['posterior_mean_per_hour']<a['conditional_95pct_interval_per_hour'][1])
    def test_mixture(self):
        r=mixture_moments([10,18],[.5,.5])
        self.assertEqual(r['expected_count'],14)
        self.assertEqual(r['count_variance'],30)
    def test_mixture_unequal(self):
        r=mixture_moments([10,18],[.8,.2])
        self.assertAlmostEqual(r['expected_count'],11.6)
        self.assertAlmostEqual(r['count_variance'],21.84)
    def test_regime_separation(self):
        result,_=run(CFG)
        self.assertAlmostEqual(result['conditional_mixture']['count_variance'],29.414135984950292)
    def test_queue_trace(self):
        r=queue([0,1,2],2,5)
        self.assertEqual(r['waits'],[0,0,3])
        self.assertEqual(r['finish_times'],[5,6,10])
        self.assertEqual(r['timely'],3)
    def test_queue_empty(self):
        r=queue([],2,10)
        self.assertEqual((r['count'],r['timely'],r['p90_wait_minutes']),(0,0,0))
    def test_queue_conservation(self):
        result,rows=run(CFG)
        self.assertEqual(len(rows),4*3*12)
        for row in rows:
            self.assertGreaterEqual(row['requests'],0)
            self.assertTrue(0<=row['timely']<=row['requests'])
            self.assertTrue(0<=row['overtime_completions']<=row['requests'])
            self.assertTrue(math.isfinite(row['mean_wait_minutes']))
            self.assertGreaterEqual(row['p90_wait_minutes'],row['mean_wait_minutes']*0)
        for policy in result['policies'].values():
            for scenario in policy['scenarios'].values():
                self.assertTrue(0<=scenario['timely_fraction']<=1)
                self.assertTrue(0<=scenario['overtime_fraction']<=1)
    def test_capacity_monotonicity_common_stream(self):
        for d,n in enumerate(CFG['counts']['storm']):
            arrivals=generate_arrivals(n,24041+202000+d)
            a=queue(arrivals,2,10)['waits']
            b=queue(arrivals,3,10)['waits']
            self.assertTrue(all(y<=x+1e-10 for x,y in zip(a,b)))
            c=queue(arrivals,2,8)['waits']
            self.assertTrue(all(y<=x+1e-10 for x,y in zip(a,c)))
    def test_reproducible_streams(self):
        self.assertEqual(generate_arrivals(20,99),generate_arrivals(20,99))
        self.assertNotEqual(generate_arrivals(20,99),generate_arrivals(20,100))
    def test_paired(self):
        a=paired_bootstrap_delta([1,2,3],[0,1,2])
        self.assertAlmostEqual(a['mean_delta'],1)
        self.assertEqual(a['percentile_95pct_interval'],[1,1])
    def test_nominal_waits(self):
        r,_=run(CFG)
        self.assertAlmostEqual(r['factorial']['baseline'],16.87970720431435)
        self.assertAlmostEqual(r['factorial']['capacity_average_effect'],-9.598227189805502)
        self.assertAlmostEqual(r['factorial']['interaction_difference_in_differences'],3.8262974957228817)
        self.assertAlmostEqual(r['paired_storm_delta_baseline_minus_combined']['mean_delta'],14.533256612518896)
    def test_constraints(self):
        r,_=run(CFG)
        self.assertEqual(r['recommended_screen_choice'],'combined')
        self.assertFalse(any(p['all_scenarios_screen_pass'] for p in r['policies'].values()))
        self.assertAlmostEqual(r['policies']['combined']['scenarios']['compound']['timely_fraction'],.8295454545454546)
        self.assertIn('HOLD',r['deployment_disposition'])
    def test_thermal(self):
        self.assertAlmostEqual(thermal_exact(2,CFG),37.64437811779848)
        self.assertAlmostEqual(thermal_euler(CFG,1),38.56)
        self.assertAlmostEqual(thermal_euler(CFG,.25),37.8377110975)
        self.assertLess(abs(thermal_euler(CFG,.25)-thermal_exact(2,CFG)),abs(thermal_euler(CFG,1)-thermal_exact(2,CFG)))
    def test_control(self):
        self.assertEqual(control_multiplier(.4,1.6,.25),.5)
        self.assertEqual(control_multiplier(.4,1.6,1),-1)
        self.assertLess(control_multiplier(.4,1.6,1.25),-1)
    def test_credibility(self):
        c=evidence_comparison(CFG)
        self.assertAlmostEqual(c['synthetic_bias_minutes'],-1.375)
        self.assertAlmostEqual(c['synthetic_rmse_minutes'],math.sqrt(29/8))
        self.assertFalse(c['permissions_all_granted'])
        self.assertIn('not external validation',c['evidence_kind'])
    def test_permission_cannot_be_optimized(self):
        changed=copy.deepcopy(CFG)
        changed['decision']['all_scenarios_timely_fraction_floor']=0
        r,_=run(changed)
        self.assertTrue(all(p['all_scenarios_screen_pass'] for p in r['policies'].values()))
        self.assertIn('HOLD',r['deployment_disposition'])
    def test_invalid_inputs(self):
        def bad(update):
            cfg=copy.deepcopy(CFG);update(cfg)
            with self.assertRaises((ValueError,KeyError,TypeError)):validate(cfg)
        changes=[
            lambda a:a['counts']['storm'].__setitem__(0,-1),
            lambda a:a['counts']['storm'].__setitem__(0,1.5),
            lambda a:a['gamma_prior'].__setitem__('shape',0),
            lambda a:a['gamma_prior'].__setitem__('rate_hours',float('nan')),
            lambda a:a['service_design'].__setitem__('small_servers',0),
            lambda a:a['policies']['capacity'].__setitem__('servers',-1),
            lambda a:a['policies']['capacity'].__setitem__('service_minutes',0),
            lambda a:a['policies']['capacity'].__setitem__('daily_added_cost_usd',-1),
            lambda a:a['scenario_weights'].__setitem__('storm',.5),
            lambda a:a['scenario_weights'].__setitem__('storm',float('inf')),
            lambda a:a['decision'].__setitem__('all_scenarios_timely_fraction_floor',1.1),
            lambda a:a['permissions'].__setitem__('operator','yes'),
            lambda a:a['thermal'].__setitem__('conductance_per_hour',0),
            lambda a:a['synthetic_credibility_comparison'].__setitem__('model_minutes',[1])]
        for change in changes:
            with self.subTest(change=repr(change)):bad(change)
    def test_invalid_queue(self):
        for arrivals,servers,service in [([2,1],2,10),([0],0,10),([0],2,0),([-1],2,10),([float('nan')],2,10),([float('inf')],2,10)]:
            with self.subTest(args=(arrivals,servers,service)):
                with self.assertRaises(ValueError):queue(arrivals,servers,service)
    def test_invalid_stats(self):
        with self.assertRaises(ValueError):quantile([], .5)
        with self.assertRaises(ValueError):quantile([1,2],1.01)
        with self.assertRaises(ValueError):mixture_moments([1,2],[.5,.4])
        with self.assertRaises(ValueError):paired_bootstrap_delta([1],[2])
        with self.assertRaises(ValueError):control_multiplier(.4,1.6,0)
        with self.assertRaises(ValueError):thermal_euler(CFG,.3)
    def test_generated_artifact_round_trip(self):
        src=INPUT.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            r=save(INPUT,tmp)
            self.assertEqual(r['input_sha256'],hashlib.sha256(src).hexdigest())
            self.assertEqual(json.loads((Path(tmp)/'ns-qse4-results.json').read_text()),r)
            self.assertEqual((Path(tmp)/'ns-qse4-policy-days.csv').read_bytes(),
                (INPUT.parent.parent/'outputs/ns-qse4-policy-days.csv').read_bytes())

if __name__=='__main__':unittest.main()
