#!/usr/bin/env python3
"""Toy Python checking of OCL-like reservation invariants and operation effects.

NOT an OCL parser, OMG interpreter, UML conformance test, model checker,
or authorization for a real implementation. Uses JSON data fixtures.
"""
from __future__ import annotations
from pathlib import Path
import json


def validate(document:dict) -> list[str]:
    errors=[]
    reservations=document.get('reservations')
    if not isinstance(reservations,list):return ['reservations must be a list']
    ids=set();workers=set()
    for i,r in enumerate(reservations):
        prefix=f'reservations[{i}]'
        if not isinstance(r,dict):errors.append(prefix+' must be an object');continue
        rid=r.get('id');status=r.get('status');worker=r.get('worker')
        if not isinstance(rid,str) or not rid.strip():
            errors.append(prefix+' has blank/nonstring identifier')
        elif rid in ids:errors.append(prefix+' duplicates identifier '+rid)
        else:ids.add(rid)
        if status not in ('Pending','Active','Closed'):
            errors.append(prefix+' has invalid state')
        if status=='Active' and (not isinstance(worker,str) or not worker.strip()):
            errors.append(prefix+' is active without worker')
        if status!='Active' and worker is not None:
            errors.append(prefix+' has worker outside Active state')
        if worker is not None:
            if not isinstance(worker,str) or not worker.strip():
                errors.append(prefix+' has invalid worker')
            elif worker in workers:
                errors.append(prefix+' duplicates assigned worker '+worker)
            else:workers.add(worker)
    return errors


def activate(document:dict, reservation_id:str, worker_id:str) -> dict:
    """Pure operation. Preconditions + postconditions are checked explicitly."""
    before=validate(document)
    if before:raise ValueError('Invalid initial model: '+repr(before))
    old=document['reservations']
    targets=[r for r in old if r['id']==reservation_id]
    if len(targets)!=1 or targets[0]['status']!='Pending' or not worker_id.strip():
        raise ValueError('Precondition: existing pending reservation and nonblank worker required')
    if any(r['worker']==worker_id for r in old):
        raise ValueError('Precondition: worker is already allocated')
    updated={'reservations':[
      {**r,'status':'Active','worker':worker_id} if r['id']==reservation_id else dict(r)
      for r in old]}
    if validate(updated):raise AssertionError('Poststate violates invariant')
    if sum(r['status']=='Active' for r in updated['reservations']) != sum(r['status']=='Active' for r in old)+1:
        raise AssertionError('Postcondition: active count must increase exactly once')
    return updated


def read(path:Path)->dict:
    return json.loads(path.read_text(encoding='utf-8'))

if __name__=='__main__':
    folder=Path(__file__).resolve().parent.parent/'data'
    for name in ('reservation-valid.json','reservation-duplicate-worker.json','reservation-missing-worker.json'):
        print(name,validate(read(folder/name)))
    print('after activate:',activate(read(folder/'reservation-valid.json'),'R-2','W-8'))
