#!/usr/bin/env python3
"""NS-DA14.1: reproducible *synthetic* selection and scalable-design examples.

Standard library only. Does not validate procurement readiness, optimize actual
service operations, replace Book 11 events/Book 12 physics, or infer empirical
uncertainty. Regenerate: python3 tools/step03_book14_decision.py --write
"""
from __future__ import annotations
import argparse, csv, itertools, json, math
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
CASE=HERE/'case'
METRICS=('cost_musd','wait_p90_min','accessible_coverage','deployment_months','availability','emissions_tco2e_annual')
MINIMIZE={'cost_musd','wait_p90_min','deployment_months','emissions_tco2e_annual'}
OBJ=('cost_musd','wait_p90_min','emissions_tco2e_annual','access_gap')


def require_number(n, label):
    if isinstance(n,bool) or not isinstance(n,(int,float)) or not math.isfinite(n):
        raise ValueError(f'{label} must be finite numeric')


def validate(cfg):
    if cfg.get('model_id')!='NS-DA14.1':raise ValueError('Wrong controlled model ID')
    pilots=cfg['pilot_alternatives']
    if sorted(p['id'] for p in pilots)!=list('ABCDEF'):raise ValueError('Expected unique alternatives A through F')
    for row in pilots:
        for k in METRICS+('integration_risk',):require_number(row[k],row['id']+' '+k)
        if not 0<=row['accessible_coverage']<=1 or not 0<=row['availability']<=1:raise ValueError('Invalid pilot fraction')
        if any(row[k]<0 for k in ('cost_musd','wait_p90_min','deployment_months','emissions_tco2e_annual')):raise ValueError('Negative pilot physical measure')
    c=cfg['illustrative_pilot_constraints']
    for key,val in c.items():require_number(val,key)
    if not 0<=c['min_accessible_coverage']<=1 or not 0<=c['min_availability']<=1:raise ValueError('Invalid pilot threshold')
    val=cfg['value_model'];w=val['weights'];anchors=val['anchors']
    if set(w)!=set(METRICS) or set(anchors)!=set(METRICS):raise ValueError('Value dimensions differ from declared metrics')
    for k in METRICS:
        require_number(w[k],'weight '+k)
        if w[k]<0:raise ValueError('Negative weight')
        lo,hi=anchors[k];require_number(lo,'lower anchor '+k);require_number(hi,'upper anchor '+k)
        if hi<=lo:raise ValueError('Degenerate anchor '+k)
    if abs(sum(w.values())-1)>1e-9:raise ValueError('Weights must sum to one')
    if set(val['higher_is_better'])-set(METRICS):raise ValueError('Unknown benefit metric')
    grid=cfg['design_grid'];expected={'architecture','fleet','chargers','reserve','dispatch','automation','zones','speed_mph'}
    if set(grid)!=expected or any(not isinstance(v,list) or not v or len(set(v))!=len(v) for v in grid.values()):raise ValueError('Invalid design factors')
    if any(x not in ('hybrid','demand') for x in grid['architecture']) or any(x not in ('schedule','priority') for x in grid['dispatch']) or any(x not in ('human','supervised') for x in grid['automation']):raise ValueError('Unsupported architecture/policy')
    for k in ('fleet','chargers','zones','speed_mph'):
        if any(isinstance(v,bool) or not isinstance(v,int) or v<1 for v in grid[k]):raise ValueError('Invalid integer design range')
    if any(isinstance(r,bool) or not isinstance(r,(int,float)) or not 0<=r<.5 for r in grid['reserve']):raise ValueError('Invalid reserve fraction')
    for k,v in cfg['design_constraints'].items():require_number(v,k)
    for state,v in cfg['states'].items():
        require_number(v['probability'],'probability '+state)
        if not 0<=v['probability']<=1 or set(v['payoffs'])!={'C','D'}:raise ValueError('Invalid state')
        for payoff in v['payoffs'].values():require_number(payoff,'state payoff')
    if abs(sum(x['probability'] for x in cfg['states'].values())-1)>1e-9:raise ValueError('State probabilities not normalized')
    d=cfg['diagnostic']
    for k,v in d.items():require_number(v,k)
    if not 0<=d['sensitivity_adverse']<=1 or not 0<=d['specificity_normal']<=1 or d['total_cost_value_points']<0:raise ValueError('Invalid diagnostic')
    return cfg


def feasible_pilot(p,c):
    reasons=[]
    for name,field,op in [('cost','cost_musd','max'),('deployment','deployment_months','max'),('accessible coverage','accessible_coverage','min'),('availability','availability','min'),('integration risk','integration_risk','max')]:
        threshold=c[{'cost':'max_cost_musd','deployment':'max_deployment_months','accessible coverage':'min_accessible_coverage','availability':'min_availability','integration risk':'max_integration_risk'}[name]]
        if (op=='max' and p[field]>threshold) or (op=='min' and p[field]<threshold):reasons.append(name)
    return reasons


def value_breakdown(row, spec):
    terms={}
    for k in METRICS:
        a,b=spec['anchors'][k];v=(row[k]-a)/(b-a)
        if k in MINIMIZE:v=1-v
        # Anchors define declared desirability domain; clipping must be disclosed.
        v=max(0,min(1,v))
        terms[k]=spec['weights'][k]*v
    return terms


def dominates(a,b,keys,eps=1e-12):
    return all(a[k]<=b[k]+eps for k in keys) and any(a[k]<b[k]-eps for k in keys)


def pareto(rows,keys):
    return [r for r in rows if not any(dominates(o,r,keys) for o in rows if o is not r)]


def pilot_results(cfg):
    p=cfg['pilot_alternatives'];feasible=[];res=[]
    for row in p:
        reasons=feasible_pilot(row,cfg['illustrative_pilot_constraints'])
        terms=value_breakdown(row,cfg['value_model'])
        record=dict(row,feasible=not reasons,rejected_by='; '.join(reasons),value_score=sum(terms.values()))
        res.append(record)
        if not reasons:feasible.append(record)
    # Pilots cannot be Pareto compared on risk as though the ordinal 1-5 scores were cardinal.
    benefit={'accessible_coverage','availability'}
    for row in feasible:
        row['pareto_efficient']=not any(other is not row and all((other[k]>=row[k] if k in benefit else other[k]<=row[k]) for k in METRICS) and any((other[k]>row[k] if k in benefit else other[k]<row[k]) for k in METRICS) for other in feasible)
    for row in res:
        if 'pareto_efficient' not in row:row['pareto_efficient']=False
    return res


def evaluate_design(a, stress='nominal'):
    """Nonvalidated teaching-response surface; never output as fleet prediction."""
    n,c,r,z,s=a['fleet'],a['chargers'],a['reserve'],a['zones'],a['speed_mph']
    for name,v in [('fleet',n),('chargers',c),('reserve',r),('zones',z),('speed_mph',s)]:require_number(v,name)
    if not (8<=n<=20 and 3<=c<=10 and 0<=r<=.25 and 2<=z<=8 and 12<=s<=25):raise ValueError('Design outside declared physical bounds')
    if a['architecture'] not in ('hybrid','demand') or a['dispatch'] not in ('schedule','priority') or a['automation'] not in ('human','supervised'):raise ValueError('Unknown design choice')
    active=n*(1-r)
    cost=3.25+.39*n+.26*c+.11*(z-4)+.12*n*r+(.45 if a['architecture']=='hybrid' else .10)+(.7 if a['automation']=='supervised' else 0)+(.14 if a['dispatch']=='priority' else 0)
    # Contracted support and accessible vehicle availability excluded, do not equate to empirical availability.
    wait=27-1.00*active+2.8*active/(c+1)+.015*(active-13)**2+.48*(z-4)+(.2 if a['architecture']=='demand' else -.85)+(-1.25 if a['dispatch']=='priority' else 0)+.06*(20-s)
    coverage=min(.998, .83+.012*active+.007*(z-4)+(.018 if a['architecture']=='demand' else .012)+(.019 if a['dispatch']=='priority' else 0))
    availability=.948+.0011*c-.0003*n+(.003 if a['automation']=='human' else -.004)
    emissions=160-3.0*active+1.9*c+(4 if a['architecture']=='demand' else 0)+(.4*(s-18))
    risk=2 if a['automation']=='human' else 3
    if stress=='high_demand':wait=wait*1.18+1.2;coverage=max(0,coverage-.027)
    elif stress=='charger_loss':wait+=.12*active;availability-=.012
    elif stress=='winter':cost+=.15;emissions*=1.16;wait+=.5
    elif stress!='nominal':raise ValueError('Unknown stress scenario')
    if not all(math.isfinite(x) for x in (cost,wait,coverage,availability,emissions)):raise ValueError('Nonfinite design result')
    return dict(a,cost_musd=cost,wait_p90_min=wait,accessible_coverage=coverage,access_gap=1-coverage,availability=availability,emissions_tco2e_annual=emissions,integration_risk=risk,vehicles_per_charger=n/c,stress=stress)


def design_feasibility(row,limits):
    rules=[('cost_musd','max_cost_musd','max'),('wait_p90_min','max_wait_p90_min','max'),('accessible_coverage','min_accessible_coverage','min'),('vehicles_per_charger','max_vehicles_per_charger','max'),('availability','min_availability','min'),('integration_risk','max_integration_risk','max')]
    return [name for name,threshold,op in rules if (op=='max' and row[name]>limits[threshold]) or (op=='min' and row[name]<limits[threshold])]


def enumerate_designs(cfg):
    grid=cfg['design_grid'];keys=list(grid)
    for values in itertools.product(*(grid[k] for k in keys)):
        row=evaluate_design(dict(zip(keys,values)))
        failures=design_feasibility(row,cfg['design_constraints'])
        row.update(feasible=not failures,excluded_by='; '.join(failures),design_id='DA-'+''.join(str(grid[k].index(v)) for k,v in zip(keys,values)))
        yield row


def doe():
    base=dict(architecture='hybrid',fleet=14,chargers=6,reserve=.15,dispatch='priority',automation='human',zones=4,speed_mph=18)
    rows=[]
    for n,c,r in itertools.product((12,18),(4,8),(.1,.2)):
        x=dict(base,fleet=n,chargers=c,reserve=r)
        y=evaluate_design(x)
        rows.append({'run':len(rows)+1,'fleet':n,'chargers':c,'reserve':r,'wait_p90_min':y['wait_p90_min'],'cost_musd':y['cost_musd']})
    return rows


def gauss(a,b):
    n=len(b);M=[list(a[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=max(range(k,n),key=lambda r:abs(M[r][k]))
        if abs(M[j][k])<1e-12:raise ValueError('Singular surrogate matrix')
        M[k],M[j]=M[j],M[k]
        div=M[k][k];M[k]=[v/div for v in M[k]]
        for i in range(n):
            if i==k:continue
            fac=M[i][k];M[i]=[x-fac*y for x,y in zip(M[i],M[k])]
    return [row[-1] for row in M]


def features(x):
    # Center and scale to make the normal-equation fit auditable and stable.
    n=(x['fleet']-14)/4;c=(x['chargers']-6)/2;r=(x['reserve']-.15)/.05
    return [1,n,c,r,n*n,c*c,r*r,n*c,n*r,c*r]


def fit_surrogate(rows,target):
    if not rows or len({(r['fleet'],r['chargers'],r['reserve']) for r in rows})<10:
        raise ValueError('A quadratic surrogate needs at least ten distinct design settings')
    X=[features(r) for r in rows];y=[r[target] for r in rows];p=len(X[0]);ridge=1e-8
    return gauss([[sum(x[i]*x[j] for x in X)+(ridge if i==j else 0) for j in range(p)] for i in range(p)],[sum(x[i]*v for x,v in zip(X,y)) for i in range(p)])


def surrogate_experiment():
    base=dict(architecture='hybrid',fleet=14,chargers=6,reserve=.15,dispatch='priority',automation='human',zones=4,speed_mph=18)
    train=[evaluate_design(dict(base,fleet=n,chargers=c,reserve=r)) for n,c,r in itertools.product((10,12,16,18),(4,6,8),(.1,.15,.2))]
    test=[evaluate_design(dict(base,fleet=n,chargers=c,reserve=r)) for n,c,r in itertools.product((11,13,15,17),(5,7),(.125,.175))]
    models={k:fit_surrogate(train,k) for k in ('cost_musd','wait_p90_min')}
    records=[]
    for row in test:
        result={k:row[k] for k in ('fleet','chargers','reserve')}
        for name,coef in models.items():
            prediction=sum(a*b for a,b in zip(features(row),coef))
            result[name+'_true']=row[name];result[name+'_prediction']=prediction;result[name+'_error']=prediction-row[name]
        records.append(result)
    summary={k:{'mae':sum(abs(r[k+'_error']) for r in records)/len(records),'maximum_absolute_error':max(abs(r[k+'_error']) for r in records)} for k in models}
    return models,records,summary


def information_value(cfg):
    """VOI requires *elicited* state probabilities and utility values; none are observed."""
    states=cfg['states'];diagnostic=cfg['diagnostic']
    expected={a:sum(st['probability']*st['payoffs'][a] for st in states.values()) for a in ('C','D')}
    no_test=max(expected.values());perfect=sum(st['probability']*max(st['payoffs'].values()) for st in states.values());evpi=perfect-no_test
    joint={}
    for state,st in states.items():
        ppositive=diagnostic['sensitivity_adverse'] if state=='adverse' else 1-diagnostic['specificity_normal']
        joint[state,'positive']=st['probability']*ppositive
        joint[state,'negative']=st['probability']*(1-ppositive)
    decisions={};total=0
    for outcome in ('positive','negative'):
        probabilities={state:joint[state,outcome] for state in states}
        options={a:sum(probabilities[state]*states[state]['payoffs'][a] for state in states) for a in ('C','D')}
        chosen=max(options,key=options.get)
        decisions[outcome]={'outcome_probability':sum(probabilities.values()),'posterior_adverse':joint['adverse',outcome]/sum(probabilities.values()),'best_decision':chosen,'weighted_payoff':options[chosen]}
        total+=options[chosen]
    evsi=total-no_test;net=evsi-diagnostic['total_cost_value_points']
    if evpi+1e-9<evsi or evsi < -1e-9:raise AssertionError('VOI ordering violated')
    return dict(no_test_expected_by_alternative=expected,no_test_best=max(expected,key=expected.get),no_test_value=no_test,perfect_information_value=perfect,evpi=evpi,diagnostic_conditional=decisions,with_test_value=total,evsi=evsi,net_value=net)


def write_csv(path,rows):
    if not rows:raise ValueError('No rows')
    with path.open('w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def run(cfg):
    validate(cfg)
    pilot=pilot_results(cfg)
    designs=list(enumerate_designs(cfg))
    feasible=[x for x in designs if x['feasible']]
    efficient=pareto(feasible,OBJ)
    experiment=doe();coeff,test,error=surrogate_experiment();voi=information_value(cfg)
    return dict(pilot=pilot,designs=designs,efficient=efficient,doe=experiment,holdout=test,coeff=coeff,holdout_error=error,voi=voi)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    cfg=json.loads((CASE/'decision-inputs.json').read_text());out=run(cfg)
    feasible=[r for r in out['pilot'] if r['feasible']]
    summary={'model_id':cfg['model_id'],'pilot_feasible':[r['id'] for r in feasible], 'pilot_preferred':max(feasible,key=lambda r:r['value_score'])['id'], 'pilot_scores':{r['id']:r['value_score'] for r in out['pilot']},'design_total':len(out['designs']),'design_feasible':sum(x['feasible'] for x in out['designs']),'design_efficient':len(out['efficient']),'doe_runs':len(out['doe']),'surrogate_train_runs':36,'surrogate_holdout_runs':len(out['holdout']),'surrogate_holdout_error':out['holdout_error'],'information_value':out['voi'],'warning':'All decision thresholds, value weights, design-response equations, and likelihoods are illustrative; no real procurement or design qualification.'}
    print(json.dumps(summary,indent=2))
    if args.write:
        write_csv(CASE/'pilot-screening.csv',out['pilot'])
        write_csv(CASE/'design-candidates.csv',out['designs'])
        write_csv(CASE/'efficient-designs.csv',out['efficient'])
        write_csv(CASE/'factorial-doe.csv',out['doe'])
        write_csv(CASE/'surrogate-holdout.csv',out['holdout'])
        (CASE/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n',encoding='utf8')

if __name__=='__main__':main()
