#!/usr/bin/env python3
"""Reproducible database interleaving showing atomic uniqueness vs check-then-act.
Uses sqlite3 and temporary databases; not a proof of distributed correctness.
"""
from __future__ import annotations
import sqlite3,tempfile
from pathlib import Path


def setup(path:Path, enforce:bool):
    with sqlite3.connect(path) as db:
        db.execute('CREATE TABLE reservations(request_id TEXT PRIMARY KEY, worker TEXT NOT NULL, status TEXT NOT NULL)')
        if enforce:
            db.execute("CREATE UNIQUE INDEX one_active_worker ON reservations(worker) WHERE status='active'")


def race(enforce:bool):
    with tempfile.TemporaryDirectory() as folder:
        dbpath=Path(folder)/'reservations.sqlite';setup(dbpath,enforce)
        a=sqlite3.connect(dbpath);b=sqlite3.connect(dbpath)
        try:
            # Both look before either writes. This is a specific *possible* interleaving,
            # not a scheduler or an attempt to mimic full transactional concurrency.
            prior_a=a.execute("SELECT COUNT(*) FROM reservations WHERE worker='W1' AND status='active'").fetchone()[0]
            prior_b=b.execute("SELECT COUNT(*) FROM reservations WHERE worker='W1' AND status='active'").fetchone()[0]
            a.execute("INSERT INTO reservations VALUES ('R1','W1','active')");a.commit()
            second_accepted=True
            try:
                b.execute("INSERT INTO reservations VALUES ('R2','W1','active')");b.commit()
            except sqlite3.IntegrityError:
                b.rollback();second_accepted=False
            rows=a.execute("SELECT request_id,worker,status FROM reservations ORDER BY request_id").fetchall()
            # A retry of an already recorded request must not create a second record.
            try:
                a.execute("INSERT INTO reservations VALUES ('R1','W1','active')");a.commit()
                replay_prevented=False
            except sqlite3.IntegrityError:
                a.rollback();replay_prevented=True
            return {'prechecks':(prior_a,prior_b),'second_accepted':second_accepted,
                    'rows':rows,'replay_prevented':replay_prevented}
        finally:a.close();b.close()


def main():
    for enforced in (False,True):
        result=race(enforced)
        print(('guarded' if enforced else 'unguarded')+': '+str(result))

if __name__=='__main__':main()
