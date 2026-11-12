#!/usr/bin/env python3
"""Small fault-tree experiment for the fictional Campus Mobility case.

Basic event independence is a MODEL ASSUMPTION, not measured evidence. This
teaching calculator accepts simple AND/OR gates and refuses unsupported forms.
"""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1]/'data/campus-mobility-release.json'


def events_in(gate):
    if isinstance(gate, str):
        return {gate}
    if not isinstance(gate, dict) or set(gate) not in ({'and'}, {'or'}):
        raise ValueError('Gate must be a basic-event name, or AND/OR with a list')
    key = next(iter(gate))
    parts = gate[key]
    if not isinstance(parts, list) or not parts:
        raise ValueError('Empty or non-list gate')
    return set().union(*(events_in(p) for p in parts))


def triggered(gate, active):
    if isinstance(gate, str):
        return gate in active
    op, parts = next(iter(gate.items()))
    results = [triggered(p, active) for p in parts]
    return all(results) if op == 'and' else any(results)


def probability(gate, rates):
    used = sorted(events_in(gate))
    if set(used) != set(rates):
        raise ValueError(f'Basic-event mismatch: {set(used)^set(rates)}')
    if any(isinstance(v, bool) or not isinstance(v,(float,int)) or not 0<=v<=1 for v in rates.values()):
        raise ValueError('Probabilities must be numbers in [0,1]')
    # Enumerate mutually exclusive assignments; correct even when an event
    # appears more than once in the expression. Scales as 2^N: teaching only.
    if len(used) > 16:
        raise ValueError('Enumeration is limited to 16 basic events')
    total = 0.0
    for flags in itertools.product((False,True),repeat=len(used)):
        active={name for name,flag in zip(used,flags) if flag}
        if triggered(gate,active):
            mass=1.0
            for name,flag in zip(used,flags):
                mass *= rates[name] if flag else 1-rates[name]
            total += mass
    return total


def minimal_cut_sets(gate):
    used=sorted(events_in(gate))
    cuts=[]
    for size in range(1,len(used)+1):
        for subset in itertools.combinations(used,size):
            s=set(subset)
            if triggered(gate,s) and not any(set(c).issubset(s) for c in cuts):
                cuts.append(subset)
    return cuts


def analyze(path=DEFAULT):
    model=json.loads(Path(path).read_text(encoding='utf-8'))
    tree=model['fault_tree']; rates=tree['events']; gate=tree['top']
    top=probability(gate,rates)
    return {'top_probability_per_demand':top,'minimal_cut_sets':[list(c) for c in minimal_cut_sets(gate)],'rates':rates}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fixture',nargs='?',type=Path,default=DEFAULT)
    result=analyze(parser.parse_args().fixture)
    print(json.dumps(result,indent=2))
