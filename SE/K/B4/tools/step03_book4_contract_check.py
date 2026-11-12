#!/usr/bin/env python3
"""Northstar NS-OO4.1 OOAD study-case regression and SQLite contract demonstration.

The code checks THIS teaching schema, not UML/OCL language conformance, formal
verification, distributed-system atomicity, or operating safety.
"""
from __future__ import annotations
import csv
import json
import sqlite3
from pathlib import Path

CASE = Path(__file__).resolve().parents[1] / 'case'


def data():
    return json.loads((CASE / 'model-baseline.json').read_text(encoding='utf-8'))


def structural_issues(doc):
    problems = []
    requirements = {r['id']: r for r in doc['requirements']}
    if len(requirements) != len(doc['requirements']): problems.append('duplicate requirement ID')
    owners = [rid for component in doc['components'] for rid in component['owns']]
    for rid in requirements:
        if owners.count(rid) != 1: problems.append(f'{rid}: expected exactly one responsibility owner')
    for u in doc['use_cases']:
        for rid in u['requirements']:
            if rid not in requirements: problems.append(f'{u["id"]}: unknown requirement {rid}')
    state_set = set(doc['states'])
    for t in doc['transitions']:
        if t['from'] not in state_set or t['to'] not in state_set:
            problems.append('unknown state in transition')
    if len({(t['from'], t['event']) for t in doc['transitions']}) != len(doc['transitions']):
        problems.append('nondeterministic transition keyed by state and event')
    return problems


def evidence_status(doc):
    revisions = {r['id']: r['revision'] for r in doc['requirements']}
    results = {}
    for item in doc['evidence']:
        rid = item['requirement']
        if rid not in revisions: results[rid] = 'UNKNOWN_REQUIREMENT'
        elif item['status'] != 'PASS': results[rid] = 'NOT_EXECUTED'
        elif item['revision'] != revisions[rid] or item['baseline'] != doc['baseline']:
            results[rid] = 'STALE'
        else: results[rid] = 'CURRENT_SYNTHETIC_PASS'
    return results


def setup_db():
    db = sqlite3.connect(':memory:')
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript('''
        CREATE TABLE reservation (
            id INTEGER PRIMARY KEY, token TEXT NOT NULL UNIQUE,
            vehicle TEXT NOT NULL, slot TEXT NOT NULL, accessibility INTEGER NOT NULL,
            state TEXT NOT NULL CHECK(state IN ('ASSIGNED', 'CANCELLED')));
        CREATE TABLE assignment (
            id INTEGER PRIMARY KEY, reservation_id INTEGER NOT NULL REFERENCES reservation(id),
            vehicle TEXT NOT NULL, slot TEXT NOT NULL,
            state TEXT NOT NULL CHECK(state IN ('ACTIVE', 'RELEASED')));
        CREATE UNIQUE INDEX one_active_vehicle_slot
            ON assignment(vehicle, slot) WHERE state='ACTIVE';
        CREATE TABLE audit_event (
            id INTEGER PRIMARY KEY, reservation_id INTEGER NOT NULL REFERENCES reservation(id),
            event_type TEXT NOT NULL, actor TEXT NOT NULL);
    ''')
    return db


def book_reservation(db, token, accessible, vehicle, slot, telemetry_age, known_vehicles, *, actor='rider-demo'):
    """Demo transaction. An external API would require more authorization and isolation analysis."""
    old = db.execute('SELECT id,vehicle,slot,accessibility FROM reservation WHERE token=?', (token,)).fetchone()
    if old:
        return ('SAME_RESERVATION' if (old[1], old[2], old[3]) == (vehicle, slot, int(accessible))
                else 'REJECT_TOKEN_MISMATCH', old[0])
    record = known_vehicles.get(vehicle)
    if record is None: return 'REJECT_UNKNOWN_VEHICLE', None
    if accessible and not record['accessible']: return 'REJECT_ACCESSIBILITY', None
    # The demonstration uses a controlled observation from the model fixture.
    # Never permit a caller to replace an old observation with a fabricated age.
    if telemetry_age != record['telemetry_age_s']: return 'REJECT_OBSERVATION_MISMATCH', None
    if record['telemetry_age_s'] > 15: return 'REJECT_STALE', None
    try:
        with db:
            cur = db.execute('INSERT INTO reservation(token,vehicle,slot,accessibility,state) VALUES(?,?,?,?,?)',
                             (token, vehicle, slot, int(accessible), 'ASSIGNED'))
            rid = cur.lastrowid
            # Final guard is in the store, not the read-before-write test.
            db.execute('INSERT INTO assignment(reservation_id,vehicle,slot,state) VALUES(?,?,?,?)',
                       (rid, vehicle, slot, 'ACTIVE'))
            db.execute('INSERT INTO audit_event(reservation_id,event_type,actor) VALUES(?,?,?)',
                       (rid, 'assigned', actor))
        return 'ACCEPT', rid
    except sqlite3.IntegrityError:
        # A competing identical token may have won after our initial lookup.
        # Inspect the committed winner before classifying the rejection.
        existing = db.execute('SELECT id,vehicle,slot,accessibility FROM reservation WHERE token=?', (token,)).fetchone()
        if existing:
            match = (existing[1], existing[2], existing[3]) == (vehicle,slot,int(accessible))
            return ('SAME_RESERVATION' if match else 'REJECT_TOKEN_MISMATCH', existing[0])
        return 'REJECT_CONFLICT', None


def cancel_reservation(db, rid, actor='rider-demo'):
    with db:
        changed = db.execute("UPDATE reservation SET state='CANCELLED' WHERE id=? AND state='ASSIGNED'", (rid,)).rowcount
        if not changed: return False
        db.execute("UPDATE assignment SET state='RELEASED' WHERE reservation_id=? AND state='ACTIVE'", (rid,))
        db.execute('INSERT INTO audit_event(reservation_id,event_type,actor) VALUES(?,?,?)',
                   (rid, 'cancelled', actor))
    return True


def run_fixtures(doc=None, fixture_path=None):
    doc = doc or data()
    known = {v['id']: v for v in doc['vehicles']}
    db = setup_db()
    outcomes, accepted = {}, {}
    with (fixture_path or (CASE/'scenario-fixtures.csv')).open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            outcome, rid = book_reservation(db, row['token'], row['accessibility']=='true',
                                            row['vehicle'],row['slot'],int(row['telemetry_age_s']),known)
            outcomes[row['scenario']] = outcome
            assert outcome == row['expected_result'], (row['scenario'],outcome,row['expected_result'])
            if rid is not None: accepted[row['scenario']] = rid
    assert accepted['F-01'] == accepted['F-02'], 'idempotent retry did not return original id'
    # Token reuse with different payload must not silently accept a changed request.
    assert book_reservation(db,'idem-a',True,'V-02','PM-02',5,known)[0]=='REJECT_TOKEN_MISMATCH'
    # A cancellation commits release and its audit event; then the same slot can be reused.
    assert cancel_reservation(db,accepted['F-07'])
    assert not cancel_reservation(db,accepted['F-07'])
    assert book_reservation(db,'idem-g',False,'V-01','AM-04',4,known)[0]=='ACCEPT'
    # Domain action checks are not the database guarantee: bypass the application layer.
    rid = accepted['F-04']
    try:
        with db:
            db.execute("INSERT INTO assignment(reservation_id,vehicle,slot,state) VALUES(?,?,?,'ACTIVE')",
                       (rid, 'V-02', 'AM-02'))
    except sqlite3.IntegrityError:
        duplicate_blocked = True
    else:
        duplicate_blocked = False
    assert duplicate_blocked, 'partial UNIQUE index failed'
    assert db.execute("SELECT COUNT(*) FROM assignment WHERE state='ACTIVE' AND vehicle='V-02' AND slot='AM-02'").fetchone()[0] == 1
    return outcomes, db


def verify():
    doc=data()
    assert not structural_issues(doc), structural_issues(doc)
    timing = doc['timing_ms']
    total = timing['authentication'] + timing['policy_check'] + timing['commit_and_event']
    assert total == 350 and timing['requirement_max']-total == 150
    status=evidence_status(doc)
    assert len(status)==7
    assert status['SW-06']=='STALE' and status['SW-07']=='NOT_EXECUTED'
    assert list(status.values()).count('CURRENT_SYNTHETIC_PASS') == 5
    results, db = run_fixtures(doc)
    assert len(results)==7
    # Negative fixture on a copy must report missing ownership.
    copy=json.loads(json.dumps(doc))
    copy['components'][0]['owns'].remove('SW-01')
    assert any('SW-01' in x for x in structural_issues(copy))
    print('NS-OO4.1: 7 requirements, 3 use cases, 7 fixture scenarios')
    print('Service-path estimate: 350 ms, illustrative margin: 150 ms')
    print('Evidence: 5 current synthetic passes, 1 stale, 1 planned')
    print('Fixtures: '+', '.join(k+'='+v for k,v in results.items()))
    print('SQLite: conditional uniqueness, cancellation, token replay and audit transaction passed')
    db.close()


if __name__=='__main__': verify()
