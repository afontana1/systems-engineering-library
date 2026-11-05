"""Northstar teaching tools: 2x2 factorial contrasts and redundancy assumptions."""
from pathlib import Path
import math,csv,json,statistics
HERE=Path(__file__).parent

def factorial(rows):
    cells={}
    for r in rows:
        cells.setdefault((r['temp'],r['algorithm']),[]).append(float(r['wait']))
    if set(cells)!={('cold','base'),('cold','optimized'),('warm','base'),('warm','optimized')}:
        raise ValueError('Required cells missing')
    m={key:statistics.mean(vals) for key,vals in cells.items()}
    interaction=(m['warm','optimized']-m['warm','base'])-(m['cold','optimized']-m['cold','base'])
    df=sum(len(vals)-1 for vals in cells.values())
    mse=sum(sum((x-m[key])**2 for x in vals) for key,vals in cells.items())/df
    se=math.sqrt(mse*sum(1/len(vals) for vals in cells.values()))
    return {'means':{str(k):v for k,v in m.items()},'interaction':interaction,'mse':mse,'se':se,
            'ci95_approx':(interaction-2.306*se,interaction+2.306*se)}

def availability(uptime,repair,common_cause):
    if uptime<=0 or repair<0 or not 0<=common_cause<1:raise ValueError('Bad input')
    single=uptime/(uptime+repair)
    independent=1-(1-single)**2
    return {'single':single,'independent_pair':independent,
            'adjusted_pair':(1-common_cause)*independent}

if __name__=='__main__':
    with (HERE/'factorial.csv').open(newline='') as f:rows=list(csv.DictReader(f))
    print(json.dumps({'factorial':factorial(rows),'availability':availability(200,5,.008)},indent=2))
