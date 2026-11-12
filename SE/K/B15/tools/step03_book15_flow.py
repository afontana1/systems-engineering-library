#!/usr/bin/env python3
"""NS-ASE15.1 finite-horizon engineering workflow simulator, standard library only.

Educational capacity/queue model, NOT an operational forecast, safety argument,
software test oracle, or validated stochastic arrival/service model.
"""
from __future__ import annotations
import argparse, csv, json, math
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'case/controlled-inputs.json'
STAGES=('engineering','review','integration','assurance','release')


def require(ok:bool,message:str)->None:
    if not ok:raise ValueError(message)


def positive_integer(x, label):
    require(type(x) is int and x>0,f'{label} must be a positive integer')


def validate(cfg):
    require(isinstance(cfg,dict),'configuration must be an object')
    require(cfg.get('model_id')=='NS-ASE15.1','model identifier mismatch')
    positive_integer(cfg.get('horizon_days'),'horizon_days')
    require(tuple(cfg.get('stages',[]))==STAGES,'stage schema/order mismatch')
    arrivals=cfg.get('arrival_days');require(isinstance(arrivals,list) and arrivals,'arrivals missing')
    require(all(type(x) is int and 0<=x<cfg['horizon_days'] for x in arrivals),'bad arrival times')
    require(arrivals==sorted(arrivals),'arrival days must be ascending')
    service=cfg.get('nominal_service_days',{})
    require(set(service)==set(STAGES),'service stage schema')
    for k,v in service.items():positive_integer(v,'service '+k)
    cases=cfg.get('scenarios',{});require(set(cases)=={'status_quo','flow_only','assured_learning','supplier_disruption'},'scenario names')
    for name,case in cases.items():
        require(set(case)=={'capacity','wip_cap','supplier_delay','rework_every'},'scenario keys '+name)
        require(set(case['capacity'])==set(STAGES),'capacity stage schema '+name)
        for key,v in case['capacity'].items():positive_integer(v,f'{name}.{key}.capacity')
        positive_integer(case['wip_cap'],name+'.wip_cap')
        require(type(case['supplier_delay']) is int and case['supplier_delay']>=0,'supplier delay')
        positive_integer(case['rework_every'],name+'.rework_every')
    a=cfg.get('assurance_case',{})
    positive_integer(a.get('critical_item_modulo'),'critical item divisor')
    positive_integer(a.get('supplier_item_modulo'),'supplier item divisor')
    require(a.get('rework_return_stage')=='review','only review rework represented')
    h=cfg.get('hypothesis',{});require(set(h)=={'max_mean_end_to_end_days','max_unreleased_critical_items','min_released_fraction'},'hypothesis schema')
    require(type(h['max_mean_end_to_end_days']) in (int,float) and math.isfinite(h['max_mean_end_to_end_days']) and h['max_mean_end_to_end_days']>0,'max mean latency')
    require(type(h['max_unreleased_critical_items']) is int and h['max_unreleased_critical_items']>=0,'max critical')
    require(type(h['min_released_fraction']) in (float,int) and math.isfinite(h['min_released_fraction']) and 0<=h['min_released_fraction']<=1,'fraction target')
    eco=cfg.get('illustrative_economics',{});require(set(eco)=={'baseline_weekly_fixed_cost_units','improved_weekly_fixed_cost_units','value_per_accepted_release_units','comparison_weeks'},'economics schema')
    for k,v in eco.items():require(type(v) in (int,float) and math.isfinite(v) and v>=0,'nonnegative economics '+k)
    positive_integer(eco['comparison_weeks'],'comparison weeks')
    return True


def percentile_nearest(values,quantile):
    require(values and 0<quantile<=1,'quantile needs nonempty values and (0,1]')
    return sorted(values)[math.ceil(quantile*len(values))-1]


def simulate(cfg,scenario):
    validate(cfg)
    require(scenario in cfg['scenarios'],'unknown scenario')
    case=cfg['scenarios'][scenario]
    arrivals=cfg['arrival_days'];service=cfg['nominal_service_days']
    # day-end queueing: completion can be admitted to the next stage only the following day.
    # The capacity limit governs admitted WIP; backlog waits are included in total latency.
    backlog=deque();q={s:deque() for s in STAGES};in_service={s:[] for s in STAGES}
    released=[];items={};history=[];position=0
    for day in range(cfg['horizon_days']):
        while position<len(arrivals) and arrivals[position]==day:
            no=position+1
            item={'id':f'CHG-{no:03d}','number':no,'arrival_day':day,'admit_day':None,'release_day':None,
                  'critical':(no%cfg['assurance_case']['critical_item_modulo']==0),
                  'supplier':(no%cfg['assurance_case']['supplier_item_modulo']==0),
                  'rework_required':no%case['rework_every']==0,'reworked':False,
                  'completed':[],'stage_visits':{s:0 for s in STAGES},'rework_events':0,
                  'evidence':{'configuration':f'cfg-r{no:03d}','review':False,'integration':False,'assurance':False,'safety':False,'security':False}}
            items[item['id']]=item;backlog.append(item);position+=1
        count_wip=sum(len(q[s])+len(in_service[s]) for s in STAGES)
        # First in first out means no hidden removal of safety-critical requests.
        while backlog and count_wip<case['wip_cap']:
            item=backlog.popleft();item['admit_day']=day;q['engineering'].append(item);count_wip+=1
        # Start operations using today's free capacity, before completion loop.
        for stage in STAGES:
            while q[stage] and len(in_service[stage])<case['capacity'][stage]:
                item=q[stage].popleft()
                extra=case['supplier_delay'] if stage=='integration' and item['supplier'] else 0
                in_service[stage].append([item,service[stage]+extra])
                item['stage_visits'][stage]+=1
        completed=[]
        for stage in STAGES:
            pending=[]
            for item,remaining in in_service[stage]:
                if remaining>1:pending.append([item,remaining-1])
                else:completed.append((stage,item))
            in_service[stage]=pending
        for stage,item in completed:
            item['completed'].append(stage)
            ev=item['evidence'];ev['configuration']=f'cfg-r{item["number"]:03d}'
            if stage=='engineering':q['review'].append(item)
            elif stage=='review':ev['review']=True;q['integration'].append(item)
            elif stage=='integration':ev['integration']=True;q['assurance'].append(item)
            elif stage=='assurance':
                if item['rework_required'] and not item['reworked']:
                    item['reworked']=True;item['rework_events']+=1;ev['review']=False;ev['integration']=False;ev['assurance']=False;ev['safety']=False;ev['security']=False
                    q['review'].append(item)
                else:
                    ev['assurance']=True;ev['safety']=True if item['critical'] else 'not-applicable'
                    ev['security']=True;q['release'].append(item)
            elif stage=='release':
                require(evidence_ready(item),'release prohibited without full evidence')
                item['release_day']=day+1;released.append(item)
        outstanding=sum(len(q[s])+len(in_service[s]) for s in STAGES)
        require(outstanding<=case['wip_cap'],'WIP capacity exceeded')
        require(len(backlog)+outstanding+len(released)==position,'conservation violation')
        history.append({'scenario':scenario,'day':day+1,'arrived':position,'released':len(released),'backlog':len(backlog),'admitted_wip':outstanding,'rework_events':sum(x['rework_events'] for x in items.values())})
    elapsed=[i['release_day']-i['arrival_day'] for i in released]
    admitted=[i['release_day']-i['admit_day'] for i in released]
    open_critical=sum(i['critical'] and i['release_day'] is None for i in items.values())
    summary={'scenario':scenario,'arrivals':len(arrivals),'released':len(released),'unreleased':len(items)-len(released),
             'backlog_at_horizon':len(backlog),'open_critical':open_critical,
             'release_fraction':len(released)/len(arrivals),
             'mean_total_lead_days':sum(elapsed)/len(elapsed) if elapsed else None,
             'p90_total_lead_days':percentile_nearest(elapsed,.9) if elapsed else None,
             'mean_admitted_lead_days':sum(admitted)/len(admitted) if admitted else None,
             'rework_count':sum(i['rework_events'] for i in items.values()),
             'maximum_wip':max(h['admitted_wip'] for h in history),
             'horizon_days':cfg['horizon_days']}
    # The scenario's safety-release predicate is a *release* guardrail; unresolved safety
    # critical items do not automatically mean an unsafe release, but preclude authorization.
    h=cfg['hypothesis']
    summary['screening_pass']=(summary['release_fraction']>=h['min_released_fraction'] and
          summary['mean_total_lead_days'] is not None and summary['mean_total_lead_days']<=h['max_mean_end_to_end_days'] and
          summary['open_critical']<=h['max_unreleased_critical_items'])
    return {'summary':summary,'items':list(items.values()),'history':history}


def evidence_ready(item):
    ev=item.get('evidence',{})
    return (isinstance(ev,dict) and all(ev.get(k) is True for k in ('review','integration','assurance','security'))
        and ev.get('configuration')==f'cfg-r{item.get("number",-1):03d}'
        and (ev.get('safety') is True if item.get('critical') else ev.get('safety')=='not-applicable'))


def bayesian_assurance(prior_defect=.20,sensitivity=.85,specificity=.90):
    for label,p in [('prior',prior_defect),('sensitivity',sensitivity),('specificity',specificity)]:
        require(type(p) in (float,int) and math.isfinite(p) and 0<=p<=1,'probability invalid '+label)
    p_positive=prior_defect*sensitivity+(1-prior_defect)*(1-specificity)
    require(p_positive>0,'no positive-result event; posterior undefined')
    return {'p_positive':p_positive,'posterior_defect_if_positive':prior_defect*sensitivity/p_positive,
            'posterior_defect_if_negative':prior_defect*(1-sensitivity)/(1-p_positive) if p_positive<1 else None}


def decision_gate(release_fraction,mean_total_lead_days,open_critical,hypothesis):
    require(type(release_fraction) in (float,int) and math.isfinite(release_fraction) and 0<=release_fraction<=1,'bad fraction')
    require(type(mean_total_lead_days) in (float,int) and math.isfinite(mean_total_lead_days) and mean_total_lead_days>=0,'bad lead time')
    require(type(open_critical) is int and open_critical>=0,'bad unresolved critical count')
    return (release_fraction>=hypothesis['min_released_fraction'] and mean_total_lead_days<=hypothesis['max_mean_end_to_end_days'] and open_critical<=hypothesis['max_unreleased_critical_items'])


def write_csv(path,rows):
    require(rows,'cannot export empty CSV')
    with path.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)


def export(cfg,where):
    where.mkdir(parents=True,exist_ok=True)
    outputs={k:simulate(cfg,k) for k in cfg['scenarios']}
    write_csv(where/'scenario-summary.csv',[o['summary'] for o in outputs.values()])
    write_csv(where/'daily-flow.csv',[row for out in outputs.values() for row in out['history']])
    write_csv(where/'item-evidence.csv',[{'scenario':scenario,'id':i['id'],'class':'critical' if i['critical'] else 'routine',
      'supplier':i['supplier'],'arrival_day':i['arrival_day'],'admit_day':i['admit_day'],
      'release_day':i['release_day'],'released':i['release_day'] is not None,
      'rework_events':i['rework_events'],'configuration':i['evidence']['configuration'],
      'review_ok':i['evidence']['review'],'integration_ok':i['evidence']['integration'],
      'assurance_ok':i['evidence']['assurance'],'safety_ok':i['evidence']['safety'],
      'security_ok':i['evidence']['security']} for scenario,out in outputs.items() for i in out['items']])
    (where/'model-results.json').write_text(json.dumps({'model_id':cfg['model_id'],'assurance_bayes':bayesian_assurance(),
         'scenarios':{k:v['summary'] for k,v in outputs.items()}},indent=2)+'\n',encoding='utf-8')
    return outputs


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,default=INPUT)
    p.add_argument('--output',type=Path,default=ROOT/'case')
    args=p.parse_args();cfg=json.loads(args.input.read_text(encoding='utf-8'));validate(cfg)
    out=export(cfg,args.output)
    for name,data in out.items():print(name,json.dumps(data['summary']))

if __name__=='__main__':main()
