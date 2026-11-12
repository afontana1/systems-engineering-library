#!/usr/bin/env python3
"""Reproduce the synthetic NS-M1 project-control numbers (Python standard library)."""
import csv
import json
from pathlib import Path
from math import isclose

BASE=Path(__file__).resolve().parents[1]/'case'

def close(a,b, msg):
    if not isclose(a,b,rel_tol=1e-9,abs_tol=1e-9):
        raise AssertionError(f'{msg}: {a} != {b}')

def audit():
    j=json.loads((BASE/'northstar-management-baseline.json').read_text())
    r=list(csv.DictReader((BASE/'control-accounts.csv').open()))
    assert len(r)==len(j['control_accounts'])==5
    assert {x['account'] for x in r}=={x['id'] for x in j['control_accounts']}
    for row in r:
        control=next(x for x in j['control_accounts'] if x['id']==row['account'])
        for csvkey,jsonkey in [('BAC_MUSD','budget'),('PV_MUSD','pv'),('EV_MUSD','ev'),('AC_MUSD','ac')]:
            close(float(row[csvkey]),control[jsonkey],f'{row["account"]}/{csvkey}')
            if jsonkey!='ac': assert 0<=control[jsonkey]<=control['budget']
    sums={k:sum(x[k] for x in j['control_accounts']) for k in ('budget','pv','ev','ac')}
    bac,pv,ev,ac=(sums[k] for k in ('budget','pv','ev','ac'))
    close(bac,7.2,'BAC');close(pv,3.0,'PV');close(ev,2.4,'EV');close(ac,2.7,'AC')
    close(bac+j['management_reserve']+j['illustrative_fee'],j['illustrative_offer'],'offer')
    cpi=ev/ac; spi=ev/pv
    close(cpi,8/9,'CPI');close(spi,.8,'SPI')
    close(ev-ac,-.3,'CV');close(ev-pv,-.6,'SV')
    eac=ac+(bac-ev)/cpi
    close(eac,8.1,'EAC');close(bac-eac,-.9,'VAC')
    close((bac-ev)/(bac-ac),4.8/4.5,'TCPI BAC')
    close((bac-ev)/(eac-ac),8/9,'TCPI EAC')
    tasks=j['schedule_activities']; known={x['id']:x for x in tasks}
    ends={}
    for task in tasks:
        assert all(pred in ends for pred in task['predecessors']),'Non-topological or unknown predecessor'
        es=max((ends[p] for p in task['predecessors']),default=0)
        ends[task['id']]=es+task['weeks']
    close(ends['E'],13,'Network completion')
    close(ends['B'],6,'B end');close(ends['C'],5,'C end')
    expected_exposure=sum(x['probability']*x['incremental_cost'] for x in j['risk_scenarios'])
    close(expected_exposure,.16,'Simple expected incremental exposure')
    assert len(list(csv.DictReader((BASE/'decision-register.csv').open())))==4
    print('NS-M1: BAC %.2f PV %.2f EV %.2f AC %.2f CPI %.4f SPI %.4f EAC %.2f network %dw risk exposure %.2f' %
          (bac,pv,ev,ac,cpi,spi,eac,ends['E'],expected_exposure))
    return j

if __name__=='__main__': audit()
