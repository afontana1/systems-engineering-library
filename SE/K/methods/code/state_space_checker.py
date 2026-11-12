#!/usr/bin/env python3
"""Tiny exhaustive state-space checker for two requests and capacity one.

This is notation-independent teaching code, not a SysML interpreter or proof
about real concurrent software.  A deliberate mutant demonstrates discovery of
a shortest counterexample trace.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass

CAPACITY = 1
TERMINAL = {'CANCELLED', 'COMPLETED'}


@dataclass(frozen=True)
class State:
    status: tuple[str, str] = ('CREATED', 'CREATED')
    allocated: int = 0


def violations(s: State) -> list[str]:
    errors = []
    if not 0 <= s.allocated <= CAPACITY:
        errors.append('capacity invariant violated')
    if s.allocated != sum(st == 'ASSIGNED' for st in s.status):
        errors.append('allocation ledger disagrees with assigned states')
    return errors


def transition(s: State, command: str, i: int, mutant: bool = False) -> State:
    statuses = list(s.status)
    status = statuses[i]
    allocated = s.allocated
    if command == 'VALIDATE' and status == 'CREATED':
        statuses[i] = 'VALIDATED'
    elif command == 'ASSIGN':
        if mutant and status in ('VALIDATED', 'ASSIGNED'):
            statuses[i] = 'ASSIGNED'
            allocated += 1   # WRONG: duplicate assignment increments, ignores capacity
        elif status == 'VALIDATED' and allocated < CAPACITY:
            statuses[i] = 'ASSIGNED'
            allocated += 1
        # An already ASSIGNED request is idempotent in the corrected model.
    elif command == 'CANCEL' and status not in TERMINAL:
        if status == 'ASSIGNED':
            allocated -= 1
        statuses[i] = 'CANCELLED'
    elif command == 'COMPLETE' and status == 'ASSIGNED':
        statuses[i] = 'COMPLETED'
        allocated -= 1
    return State(tuple(statuses), allocated)


def explore(mutant: bool = False) -> dict:
    start = State()
    queue = deque([(start, ())])
    seen = {start}
    commands = ('VALIDATE', 'ASSIGN', 'CANCEL', 'COMPLETE')
    while queue:
        current, trace = queue.popleft()
        problems = violations(current)
        if problems:
            return {'states': len(seen), 'counterexample': trace,
                    'violations': problems, 'final': current}
        for i in (0, 1):
            for command in commands:
                successor = transition(current, command, i, mutant)
                if successor not in seen:
                    seen.add(successor)
                    queue.append((successor, trace + (f'{command}({i})',)))
    return {'states': len(seen), 'counterexample': None, 'violations': [], 'final': None}


if __name__ == '__main__':
    print('Corrected state machine:', explore())
    print('Deliberately defective state machine:', explore(mutant=True))
