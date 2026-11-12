#!/usr/bin/env python3
"""NS-CPS12.1 synthetic coupled longitudinal-energy-thermal teaching model.

Standard library only. Run from any directory:
 python SE/K/B12/tools/step03_book12_coupled_vehicle.py --write

A low-order explicit Euler *screening* implementation, not a tool conforming to
FMI/HLA/Modelica, not a vehicle qualification model, not a real-time/HIL test.
"""
from __future__ import annotations
import argparse, csv, json, math, random
from pathlib import Path

CASE=Path(__file__).resolve().parents[1]/'case'
FIELDS=('scenario','sample','mass_kg','drag_area_m2','rolling_coefficient',
        'ambient_c','coolant_flow_kg_per_s','trips','distance_km','duration_min',
        'mean_trip_time_min','battery_energy_used_kwh','ending_soc','max_battery_temp_c',
        'net_wheel_work_kwh','battery_traction_energy_kwh','auxiliary_energy_kwh',
        'resistive_loss_kwh','heat_rejected_kwh','energy_balance_error_kwh','mechanical_balance_error_kwh','thermal_balance_error_kwh',
        'max_wheel_power_kw','reserve_pass','trip_time_pass','thermal_pass')

def load(path:Path=CASE/'model-inputs.json') -> dict:
    d=json.loads(path.read_text(encoding='utf8'))
    validate(d)
    return d

def validate(d:dict) -> None:
    def positive(k):
        v=d.get(k)
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<=0:
            raise ValueError('invalid positive parameter: '+k)
    for k in ('mass_kg','battery_usable_kwh','nominal_bus_v','battery_resistance_ohm',
              'battery_heat_capacity_j_per_k','motor_power_limit_kw','regen_power_limit_kw',
              'wheel_radius_m','drag_area_m2','air_density_kg_per_m3','gravity_m_per_s2',
              'acceleration_limit_mps2','braking_limit_mps2','speed_control_gain_per_s',
              'charger_kw','charger_efficiency','dt_s','sample_count',
              'cooling_ua_base_w_per_k','cooling_ua_per_flow_w_per_k_per_kgps'):
        positive(k)
    for k in ('payload_kg','pump_power_base_w','pump_power_flow_gain_w_per_kgps_cubed',
              'cold_cabin_power_kw','hot_cabin_power_kw','mild_cabin_power_kw'):
        v=d.get(k)
        if not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:raise ValueError(k)
    for k in ('initial_soc','motoring_efficiency','regen_efficiency','aux_heat_fraction'):
        v=d.get(k)
        if not isinstance(v,(int,float)) or not math.isfinite(v) or not 0<v<=1:raise ValueError(k)
    for k in ('rolling_coefficient','coolant_flow_kg_per_s'):
        v=d.get(k)
        if not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:raise ValueError(k)
    if not 0<d['charger_efficiency']<=1:raise ValueError('charger efficiency')
    if not 0<d['dt_s']<=2.0:raise ValueError('unverified integration step')
    if not isinstance(d['drive_repetitions'],int) or isinstance(d['drive_repetitions'],bool) or not 1<=d['drive_repetitions']<=100:raise ValueError('drive_repetitions')
    if not isinstance(d['sample_count'],int) or isinstance(d['sample_count'],bool) or not 2<=d['sample_count']<=100:raise ValueError('sample_count')
    if not isinstance(d.get('sample_seed'),int):raise ValueError('sample_seed')
    if d['battery_warning_c']>=d['battery_limit_c']:raise ValueError('thermal limits')
    if not -40<=d['initial_battery_temp_c']<=75:raise ValueError('initial temperature')
    if not isinstance(d.get('route'),list) or len(d['route'])<2:raise ValueError('route')
    seen=set()
    for s in d['route']:
        if s.get('id') in seen or not isinstance(s.get('id'),str):raise ValueError('segment id')
        seen.add(s['id'])
        if not 0<s.get('length_m',0)<1e6 or not 0<s.get('target_speed_mps',0)<40 or abs(s.get('grade',2))>0.10:raise ValueError('segment')
    if not isinstance(d.get('scenarios'),list) or len(d['scenarios'])<2:raise ValueError('scenarios')
    ss=set()
    for s in d['scenarios']:
        if not isinstance(s.get('id'),str) or s['id'] in ss:raise ValueError('scenario ID')
        ss.add(s['id'])
        if not -20<=s.get('ambient_c',100)<=45 or not 0.05<=s.get('coolant_flow_kg_per_s',0)<=0.35 or not 0.5<=s.get('grade_multiplier',0)<=1.5:raise ValueError('scenario range')
    u=d.get('uncertainty',{})
    if not 0<=u.get('mass_delta_kg',-1)<d['mass_kg'] or not 0<=u.get('drag_area_delta_m2',-1)<d['drag_area_m2']:raise ValueError('uncertainty spread')
    if not 0<u.get('rolling_coefficient_min',0)<=u.get('rolling_coefficient_max',0)<=0.03:raise ValueError('uncertainty rolling range')
    for k in ('reserve_soc_min','trip_time_max_min','battery_temperature_limit_c'):
        if not math.isfinite(d.get('requirements',{}).get(k,float('nan'))):raise ValueError('requirement '+k)
    if not 0<d['requirements']['reserve_soc_min']<1:raise ValueError('reserve requirement')
    if d['requirements']['trip_time_max_min']<=0:raise ValueError('time requirement')
    if d['requirements']['battery_temperature_limit_c']<=d['battery_warning_c']:raise ValueError('thermal requirement')


def segment_at(d:dict, distance_m:float) -> dict:
    length=sum(s['length_m'] for s in d['route'])
    p=distance_m%length
    for s in d['route']:
        if p<s['length_m']:return s
        p-=s['length_m']
    return d['route'][-1]

def run(d:dict, scenario:dict, variation:dict|None=None, *, dt_s:float|None=None,
        repetitions:int|None=None, return_trace:bool=False) -> dict:
    """Integrate speed, position, battery energy and temperature without external dependencies.

    Mechanical power is F_motor*v, battery traction power accounts for efficiency.
    Heat uses I^2R plus specified auxiliary heat fraction; thermal cooling is UA(T-Ta).
    There is no battery voltage sag or battery chemistry model, and the route is periodic.
    """
    validate(d)
    if scenario not in d['scenarios'] and not all(k in scenario for k in ('ambient_c','coolant_flow_kg_per_s','grade_multiplier','id')):raise ValueError('scenario specification')
    variation=variation or {}
    m=d['mass_kg']+d['payload_kg']+variation.get('mass_delta_kg',0.)
    cd=d['drag_area_m2']+variation.get('drag_area_delta_m2',0.)
    cr=variation.get('rolling_coefficient',d['rolling_coefficient'])
    if not 1000<=m<=6000 or cd<=0 or not 0<cr<=0.03:raise ValueError('invalid variation')
    flow=scenario['coolant_flow_kg_per_s'];ambient=scenario['ambient_c'];gm=scenario['grade_multiplier']
    if not 0.05<=flow<=0.35 or not -20<=ambient<=45 or not 0.5<=gm<=1.5:raise ValueError('invalid scenario')
    dt=d['dt_s'] if dt_s is None else dt_s
    if not 0<dt<=2:raise ValueError('dt bounds')
    loops=d['drive_repetitions'] if repetitions is None else repetitions
    if not isinstance(loops,int) or not 1<=loops<=100:raise ValueError('repetitions')
    route_length=sum(s['length_m'] for s in d['route']);target=loops*route_length
    x=0.;v=0.;temp=d['initial_battery_temp_c'];energy=d['battery_usable_kwh']*d['initial_soc']
    max_temp=temp;max_wheel_power=0.;t=0.;wheel_j=traction_battery_j=aux_j=ir_j=cooling_j=0.
    resist_j=grade_j=0.;temp_start=temp
    # Optional coarse trace contains one point per route lap for visualization without enormous files.
    trace=[];next_lap=route_length
    while x<target:
        seg=segment_at(d,x)
        f_res=m*d['gravity_m_per_s2']*(cr+seg['grade']*gm)+0.5*d['air_density_kg_per_m3']*cd*v*v
        a_request=max(-d['braking_limit_mps2'],min(d['acceleration_limit_mps2'],d['speed_control_gain_per_s']*(seg['target_speed_mps']-v)))
        desired_force=m*a_request+f_res
        power_limited_force=d['motor_power_limit_kw']*1000/max(v,2.0)
        regen_limited_force=d['regen_power_limit_kw']*1000/max(v,2.0)
        traction_force=max(-regen_limited_force,min(power_limited_force,desired_force))
        a=(traction_force-f_res)/m
        oldv=v
        v=max(0.,v+a*dt)
        meanv=(oldv+v)*.5
        x+=meanv*dt
        wheel_power=traction_force*meanv
        if wheel_power>=0:traction_battery_power=wheel_power/d['motoring_efficiency']
        else:traction_battery_power=wheel_power*d['regen_efficiency']
        cabin_kw=(d['cold_cabin_power_kw'] if ambient<5 else d['hot_cabin_power_kw'] if ambient>30 else d['mild_cabin_power_kw'])
        pump_power=d['pump_power_base_w']+d['pump_power_flow_gain_w_per_kgps_cubed']*flow**3
        aux_power=1000*cabin_kw+pump_power
        # Proxy battery current (does not resolve under-load voltage drop); Joule loss is illustrative.
        battery_power=traction_battery_power+aux_power
        current=battery_power/d['nominal_bus_v']
        q_ohmic=current*current*d['battery_resistance_ohm']
        ua=d['cooling_ua_base_w_per_k']+d['cooling_ua_per_flow_w_per_k_per_kgps']*flow
        q_cooling=ua*(temp-ambient) # may be negative: ambient heats the pack
        q_in=q_ohmic+d['aux_heat_fraction']*aux_power
        temp+=(q_in-q_cooling)*dt/d['battery_heat_capacity_j_per_k']
        energy-=(battery_power+q_ohmic)*dt/3_600_000
        wheel_j+=wheel_power*dt
        resist_j+=(m*d['gravity_m_per_s2']*cr+0.5*d['air_density_kg_per_m3']*cd*meanv*meanv)*meanv*dt
        grade_j+=m*d['gravity_m_per_s2']*seg['grade']*gm*meanv*dt
        traction_battery_j+=traction_battery_power*dt
        aux_j+=aux_power*dt;ir_j+=q_ohmic*dt;cooling_j+=q_cooling*dt
        max_temp=max(max_temp,temp)
        max_wheel_power=max(max_wheel_power,abs(wheel_power)/1000)
        t+=dt
        if x>=next_lap:
            if return_trace:trace.append({'lap':len(trace)+1,'time_min':round(t/60,3),'soc':round(energy/d['battery_usable_kwh'],6),'temp_c':round(temp,5),'distance_km':round(x/1000,4)})
            next_lap+=route_length
        if energy<=0 or t>100000:raise ValueError('energy or time horizon exhausted; physically infeasible scenario')
    used=d['battery_usable_kwh']*d['initial_soc']-energy
    # Battery energy is traction plus cabin/pump; algebraic check is separately testable.
    balance=(used-(traction_battery_j+aux_j+ir_j)/3_600_000)
    kinetic_change_j=0.5*m*v*v
    mechanical_balance=(wheel_j-resist_j-grade_j-kinetic_change_j)/3_600_000
    thermal_balance=(d['battery_heat_capacity_j_per_k']*(temp-temp_start)-(ir_j+d['aux_heat_fraction']*aux_j-cooling_j))/3_600_000
    r=d['requirements'];mean_trip=t/60/loops
    return dict(scenario=scenario['id'],sample=-1,mass_kg=round(m,4),drag_area_m2=round(cd,5),rolling_coefficient=round(cr,6),
      ambient_c=ambient,coolant_flow_kg_per_s=flow,trips=loops,distance_km=round(x/1000,5),
      duration_min=round(t/60,4),mean_trip_time_min=round(mean_trip,4),
      battery_energy_used_kwh=round(used,5),ending_soc=round(energy/d['battery_usable_kwh'],7),
      max_battery_temp_c=round(max_temp,5),net_wheel_work_kwh=round(wheel_j/3_600_000,5),
      battery_traction_energy_kwh=round(traction_battery_j/3_600_000,5),
      auxiliary_energy_kwh=round(aux_j/3_600_000,5),resistive_loss_kwh=round(ir_j/3_600_000,5),
      heat_rejected_kwh=round(cooling_j/3_600_000,5),energy_balance_error_kwh=round(balance,9),
      mechanical_balance_error_kwh=round(mechanical_balance,9),thermal_balance_error_kwh=round(thermal_balance,9),
      max_wheel_power_kw=round(max_wheel_power,4),
      reserve_pass=int(energy/d['battery_usable_kwh']>=r['reserve_soc_min']),
      trip_time_pass=int(mean_trip<=r['trip_time_max_min']),thermal_pass=int(max_temp<=r['battery_temperature_limit_c']),
      trace=trace if return_trace else [])


def sample_parameters(d:dict,n:int|None=None) -> list[dict]:
    n=d['sample_count'] if n is None else n
    if not isinstance(n,int) or n<2:raise ValueError('sample count')
    g=random.Random(d['sample_seed']);u=d['uncertainty'];pairs=[]
    for i in range(n):
        pairs.append(dict(sample=i, mass_delta_kg=g.uniform(-u['mass_delta_kg'],u['mass_delta_kg']),
          drag_area_delta_m2=g.uniform(-u['drag_area_delta_m2'],u['drag_area_delta_m2']),
          rolling_coefficient=g.uniform(u['rolling_coefficient_min'],u['rolling_coefficient_max'])))
    return pairs


def experiment(d:dict) -> list[dict]:
    params=sample_parameters(d)
    rows=[]
    for p in params:
        for scenario in d['scenarios']:
            row=run(d,scenario,p)
            row['sample']=p['sample'];row.pop('trace')
            rows.append(row)
    return rows


def summarize(d:dict,rows:list[dict]) -> dict:
    output={'case_id':d['case_id'],'version':d['version'],'inference':'Synthetic parameter screening; not probability of real system compliance',
      'sampling':'Fixed-seed uniform range samples are not calibrated operational probabilities',
      'number_of_samples':d['sample_count'],'by_scenario':{}}
    for sc in d['scenarios']:
        rs=[r for r in rows if r['scenario']==sc['id']]
        if len(rs)!=d['sample_count']:raise ValueError('scenario replicates missing')
        summary={}
        for k in ('battery_energy_used_kwh','ending_soc','max_battery_temp_c','mean_trip_time_min'):
            xs=sorted(r[k] for r in rs)
            summary[k]={'mean':round(sum(xs)/len(xs),6),'min':xs[0],'max':xs[-1]}
        for k in ('reserve_pass','trip_time_pass','thermal_pass'):
            summary[k+'_count']=sum(r[k] for r in rs)
        output['by_scenario'][sc['id']]=summary
    return output


def write(d:dict= None) -> dict:
    if d is None:d=load()
    rows=experiment(d)
    with (CASE/'experiment-results.csv').open('w',encoding='utf8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS);writer.writeheader();writer.writerows({k:r[k] for k in FIELDS} for r in rows)
    summary=summarize(d,rows)
    (CASE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
    return summary

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true',help='refresh controlled experiment CSV and summary JSON')
    ap.add_argument('--dt',type=float,default=None,help='step in seconds for demonstration')
    ap.add_argument('--laps',type=int,default=None,help='drive route repetitions for demonstration')
    args=ap.parse_args()
    if args.write:print(json.dumps(write(),indent=2))
    else:
        d=load();print(json.dumps(run(d,d['scenarios'][0],dt_s=args.dt,repetitions=args.laps),indent=2))
