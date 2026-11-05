# State machines, invariants and precise behavioral contracts

**Concept library essay · Phase 1**

## Why state matters more than method names
A request may be valid in one state and forbidden in another. A model that exposes `cancelTrip()` without a state contract cannot tell you whether cancellation is allowed after boarding, during a pending assignment or after completion. State models make this visible. A transition consists of source state, triggering event, optional guard, effect and target state. An event that arrives outside its permitted state requires an explicit disposition, not a vague promise to 'handle errors'.

Represent a small trip lifecycle:

```text
Requested --confirm--> Confirmed --board--> InProgress --finish--> Completed
    |                    |
  cancel               cancel (under policy)
    v                    v
 Canceled             Canceled
```

An invariant might be: at most one assignment is active for a trip. The state machine alone does not guarantee this across concurrent database transactions. A precise contract requires both model-level assertion and implementation-level enforcement. This illustrates the different roles of UML/OCL, test cases, and database constraints.

## Think with counterexamples
Take the claim 'every confirmed trip has an active vehicle.' Construct objects that challenge it: confirmed trip with zero assignments, two active assignments, assignment to an unavailable vehicle, or an assignment that expired one microsecond ago. Is the claim supposed to hold before or after a transaction completes? If a system is eventually consistent, which authoritative component enforces it? Do not allow ambiguity over time windows to hide in natural language.

## Connect model and executable tests
For each transition write a positive test, a rejected-event test and one cross-object invariant test. Add stale-message and duplicate-message variants. An operation's precondition tells callers when a command is meaningful; its postcondition describes what the command guarantees if it succeeds. Tests should also check that a rejected command leaves persistent state unchanged unless audit requirements explicitly demand a side effect.

## Practice
Create an event/state acceptance table with five states and events `confirm`, `board`, `cancel`, `finish`, `reset`. For every illegal combination specify error, no-op or escalation. Compare this table to `tools/trip_domain.py` and extend the provided tests.

[Back to Phase 1 library](../README.md)
