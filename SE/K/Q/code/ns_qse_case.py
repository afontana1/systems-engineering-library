#!/usr/bin/env python3
"""NS-QSE4.1: controlled synthetic quantitative dispatch case. Python stdlib only.

This is a reproducible methodological exercise, not a calibrated campus or
emergency operations model. Random streams are fixed; stream independence is
an *assumption*, and synthetic withheld values are NOT physical validation.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, random, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'data/ns-qse4-case.json'


def finite(x, name, low=None, strict=False):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x):
        raise ValueError(f'{name}: finite numeric value required')
    if low is not None and (x <= low if strict else x < low):
        raise ValueError(f'{name}: out of permitted range')
    return x


def validate(cfg):
    if set(cfg['counts']) != {'clear', 'storm'}: raise ValueError('exactly clear and storm counts required')
    for scenario, counts in cfg['counts'].items():
        if len(counts) < 2: raise ValueError('at least two hours per scenario')
        for n in counts:
            if type(n) is not int or n < 0: raise ValueError('nonnegative integer demand required')
    prior = cfg['gamma_prior']
    finite(prior['shape'], 'shape', 0, True); finite(prior['rate_hours'], 'rate', 0, True)
    sd = cfg['service_design']
    for k in ('slow_minutes', 'fast_minutes', 'timely_limit_minutes'): finite(sd[k], k, 0, True)
    for k in ('small_servers', 'large_servers'):
        if type(sd[k]) is not int or sd[k] <= 0: raise ValueError('positive integer servers required')
    w = cfg['scenario_weights']
    if set(w) != {'clear', 'storm', 'compound'}: raise ValueError('three scenarios required')
    for k, p in w.items(): finite(p, k, 0)
    if abs(sum(w.values()) - 1) > 1e-10: raise ValueError('scenario weights must sum to one')
    for p in cfg['policies'].values():
        if type(p['servers']) is not int or p['servers'] <= 0: raise ValueError('policy servers invalid')
        finite(p['service_minutes'], 'service', 0, True)
        finite(p['daily_added_cost_usd'], 'cost', 0)
    cd=cfg['compound_design']
    for name in ('demand_multiplier','service_multiplier'): finite(cd[name], name, 0, True)
    dec=cfg['decision']; finite(dec['wait_cost_usd_per_request_min'],'wait penalty',0)
    finite(dec['all_scenarios_timely_fraction_floor'], 'screen', 0)
    if dec['all_scenarios_timely_fraction_floor']>1: raise ValueError('screen >1')
    th=cfg['thermal']
    for name in th: finite(th[name],name)
    if th['conductance_per_hour']<=0 or th['duration_hours']<=0: raise ValueError('physical time/constants must be positive')
    comp=cfg['synthetic_credibility_comparison']
    if len(comp['model_minutes']) != len(comp['withheld_generator_minutes']) or len(comp['model_minutes'])<2:
        raise ValueError('paired comparison lengths must match')
    for key in comp:
        for v in comp[key]: finite(v,key,0)
    if set(cfg['permissions']) != {'operator','accessible_stakeholder_review','safety','data_governance'} or any(type(v) is not bool for v in cfg['permissions'].values()):
        raise ValueError('permissions must be explicit booleans')
    return cfg


def load(path=INPUT): return validate(json.loads(Path(path).read_text(encoding='utf-8')))


def quantile(values, p):
    if not values or not 0<=p<=1: raise ValueError('quantile needs values and 0<=p<=1')
    x=sorted(values); pos=(len(x)-1)*p; lo=int(pos); hi=min(len(x)-1,lo+1)
    return x[lo]+(x[hi]-x[lo])*(pos-lo)


def mixture_moments(rates, weights):
    if len(rates)!=len(weights) or not rates: raise ValueError('rates and weights must match')
    if any(not math.isfinite(x) or x<0 for x in rates+weights) or abs(sum(weights)-1)>1e-10:
        raise ValueError('nonnegative rates and normalized weights required')
    mu=sum(r*w for r,w in zip(rates,weights))
    return {'expected_count':mu,'count_variance':mu+sum(w*(r-mu)**2 for r,w in zip(rates,weights))}


def posterior_summary(counts, prior, seed):
    n=sum(counts); hours=len(counts)
    shape=prior['shape']+n; rate=prior['rate_hours']+hours
    rng=random.Random(seed)
    samples=[rng.gammavariate(shape,1/rate) for _ in range(4000)]
    return {'synthetic_total':n,'exposure_hours':hours,'posterior_shape':shape,
            'posterior_rate_hours':rate,'posterior_mean_per_hour':shape/rate,
            'conditional_95pct_interval_per_hour':[quantile(samples,.025),quantile(samples,.975)]}


def generate_arrivals(count, seed):
    if type(count) is not int or count<0: raise ValueError('invalid count')
    rng=random.Random(seed)
    return sorted(rng.uniform(0,60) for _ in range(count))


def queue(arrivals, servers, service_minutes, timely_limit=12):
    if type(servers) is not int or servers<=0: raise ValueError('positive integer servers required')
    finite(service_minutes,'service_minutes',0,True); finite(timely_limit,'timely_limit',0)
    if any(not isinstance(t,(int,float)) or not math.isfinite(t) or t<0 for t in arrivals):
        raise ValueError('arrival times must be nonnegative and finite')
    if list(arrivals)!=sorted(arrivals): raise ValueError('arrivals must be ordered')
    # Every arrival is eventually served; post-window completion is counted as overtime.
    available=[0.0]*servers
    waits=[]; finishes=[]
    for t in arrivals:
        pos=min(range(servers),key=lambda i:(available[i],i))
        start=max(t,available[pos]); wait=start-t
        available[pos]=start+service_minutes
        waits.append(wait); finishes.append(available[pos])
    return {'count':len(waits),'mean_wait_minutes':statistics.mean(waits) if waits else 0,
            'p90_wait_minutes':quantile(waits,.9) if waits else 0,
            'timely':sum(w<=timely_limit+1e-12 for w in waits),
            'overtime_completions':sum(t>60 for t in finishes),
            'waits':waits,'finish_times':finishes}


def daily_results(cfg, scenario, policy_name, seed=24041):
    if scenario not in ('clear','storm','compound'):raise ValueError('unknown scenario')
    p=cfg['policies'][policy_name]
    counts=cfg['counts']['storm' if scenario=='compound' else scenario]
    rows=[]
    for d,n in enumerate(counts):
        if scenario=='compound': n=math.ceil(n*cfg['compound_design']['demand_multiplier'])
        # Common random numbers: each day receives the same stream across policies.
        source='storm' if scenario=='compound' else scenario
        streams={'clear':101,'storm':202,'compound':303}
        service=p['service_minutes']*(cfg['compound_design']['service_multiplier'] if scenario=='compound' else 1)
        r=queue(generate_arrivals(n,seed+streams[scenario]*1000+d),p['servers'],service,cfg['service_design']['timely_limit_minutes'])
        rows.append({'scenario':scenario,'policy':policy_name,'day':d+1,'requests':n,
            'mean_wait_minutes':r['mean_wait_minutes'],'p90_wait_minutes':r['p90_wait_minutes'],
            'timely':r['timely'],'overtime_completions':r['overtime_completions']})
    return rows


def aggregate(rows):
    n=sum(r['requests'] for r in rows)
    return {'days':len(rows),'requests':n,'mean_daily_wait_minutes':statistics.mean(r['mean_wait_minutes'] for r in rows),
       'request_weighted_mean_wait_minutes':sum(r['mean_wait_minutes']*r['requests'] for r in rows)/n if n else 0,
       'timely_fraction':sum(r['timely'] for r in rows)/n if n else 1,
       'overtime_fraction':sum(r['overtime_completions'] for r in rows)/n if n else 0}


def paired_bootstrap_delta(a,b,seed=4102,reps=2500):
    if len(a)!=len(b) or len(a)<2: raise ValueError('paired replication vectors required')
    finite(reps,'reps',1,True)
    delta=[x-y for x,y in zip(a,b)]; rng=random.Random(seed)
    draws=[sum(delta[rng.randrange(len(delta))] for _ in delta)/len(delta) for _ in range(int(reps))]
    return {'mean_delta':statistics.mean(delta),'percentile_95pct_interval':[quantile(draws,.025),quantile(draws,.975)]}


def thermal_exact(t, cfg, cooling=None):
    th=cfg['thermal']; finite(t,'time',0)
    a=th['conductance_per_hour']; cool=th['cooling_deg_c_per_hour'] if cooling is None else cooling
    equilibrium=th['ambient_deg_c']+(th['heat_deg_c_per_hour']-cool)/a
    return equilibrium+(th['initial_deg_c']-equilibrium)*math.exp(-a*t)


def thermal_euler(cfg, h, cooling=None):
    th=cfg['thermal']; finite(h,'h',0,True)
    n=round(th['duration_hours']/h)
    if abs(n*h-th['duration_hours'])>1e-9:raise ValueError('h must divide the time horizon')
    x=th['initial_deg_c']; cool=th['cooling_deg_c_per_hour'] if cooling is None else cooling
    for _ in range(n): x+=h*(th['conductance_per_hour']*(th['ambient_deg_c']-x)+th['heat_deg_c_per_hour']-cool)
    return x


def control_multiplier(a, k, h):
    for name,x in [('a',a),('k',k),('h',h)]: finite(x,name,0,True)
    return 1-h*(a+k)


def evidence_comparison(cfg):
    d=cfg['synthetic_credibility_comparison']; errors=[p-r for p,r in zip(d['model_minutes'],d['withheld_generator_minutes'])]
    return {'synthetic_bias_minutes':statistics.mean(errors),'synthetic_rmse_minutes':math.sqrt(statistics.mean(e*e for e in errors)),
      'evidence_kind':'synthetic withheld-generator cross-check, not external validation',
      'permissions_all_granted':all(cfg['permissions'].values())}


def run(cfg):
    validate(cfg)
    results={}
    prior=cfg['gamma_prior']
    results['posterior']={s:posterior_summary(cfg['counts'][s],prior,i+700) for i,s in enumerate(('clear','storm'))}
    rates=[results['posterior'][s]['posterior_mean_per_hour'] for s in ('clear','storm')]
    results['conditional_mixture']=mixture_moments(rates,[.5,.5])
    policies={}
    allrows=[]
    for pname,p in cfg['policies'].items():
        grouped={}; arow=[]
        for scenario in ('clear','storm','compound'):
            rows=daily_results(cfg,scenario,pname)
            grouped[scenario]=aggregate(rows); arow+=rows;allrows+=rows
        weights=cfg['scenario_weights']; dec=cfg['decision']
        wait_penalty=sum(weights[s]*grouped[s]['request_weighted_mean_wait_minutes']*sum(r['requests'] for r in arow if r['scenario']==s)/grouped[s]['days']*dec['wait_cost_usd_per_request_min'] for s in weights)
        policies[pname]={'scenarios':grouped,'weighted_wait_penalty_usd_per_window':wait_penalty,
           'illustrative_cost_plus_wait_penalty_usd':wait_penalty+p['daily_added_cost_usd'],
           'all_scenarios_screen_pass':all(grouped[s]['timely_fraction']>=dec['all_scenarios_timely_fraction_floor'] for s in weights)}
    # Two-factor factorial in storm conditions; mean daily wait is response.
    combo={name:policies[name]['scenarios']['storm']['mean_daily_wait_minutes'] for name in policies}
    interaction=combo['combined']-combo['capacity']-combo['process']+combo['status_quo']
    results['factorial']={'baseline':combo['status_quo'],'capacity':combo['capacity'],
        'process':combo['process'],'combined':combo['combined'],
        'capacity_average_effect':((combo['capacity']+combo['combined'])-(combo['status_quo']+combo['process']))/2,
        'process_average_effect':((combo['process']+combo['combined'])-(combo['status_quo']+combo['capacity']))/2,
        'interaction_difference_in_differences':interaction}
    p1=daily_results(cfg,'storm','status_quo');p2=daily_results(cfg,'storm','combined')
    results['paired_storm_delta_baseline_minus_combined']=paired_bootstrap_delta([r['mean_wait_minutes'] for r in p1],[r['mean_wait_minutes'] for r in p2])
    results['policies']=policies
    t=cfg['thermal']['duration_hours']
    results['thermal']={'exact_deg_c':thermal_exact(t,cfg),'euler_h1_deg_c':thermal_euler(cfg,1),
      'euler_h025_deg_c':thermal_euler(cfg,.25), 'uncooled_exact_deg_c':thermal_exact(t,cfg,0),
      'control_multiplier_h025':control_multiplier(.4,1.6,.25),'control_multiplier_h1':control_multiplier(.4,1.6,1)}
    results['credibility']=evidence_comparison(cfg)
    results['recommended_screen_choice']=min(policies,key=lambda p:policies[p]['illustrative_cost_plus_wait_penalty_usd'])
    results['deployment_disposition']='HOLD: unvalidated synthetic case and absent required permissions'
    return results,allrows


def save(cfg=INPUT, out=None):
    path=Path(cfg); obj=load(path)
    results,rows=run(obj)
    results['input_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    outdir=Path(out) if out else ROOT/'outputs'
    outdir.mkdir(parents=True,exist_ok=True)
    (outdir/'ns-qse4-results.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    with (outdir/'ns-qse4-policy-days.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['policy','scenario','day','requests','mean_wait_minutes','p90_wait_minutes','timely','overtime_completions'])
        writer.writeheader();writer.writerows(rows)
    return results


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',default=str(INPUT));parser.add_argument('--output-dir')
    args=parser.parse_args()
    r=save(args.input,args.output_dir)
    print(json.dumps({'case_id':'NS-QSE4.1','choice':r['recommended_screen_choice'],'disposition':r['deployment_disposition'],
        'policies':{k:{'cost_plus_wait':round(v['illustrative_cost_plus_wait_penalty_usd'],2),'screen':v['all_scenarios_screen_pass']} for k,v in r['policies'].items()}},indent=2))
