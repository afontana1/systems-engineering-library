# 03 · Architecture viewpoints, state models, and interface contracts

**Concept dossier · MBSE / object-oriented modeling / integration**

## Why one diagram is never enough

An architecture is a set of decisions and descriptions that explain how a system is organized to satisfy concerns. Different **viewpoints** answer different questions: structure shows parts and their connections; behavior shows sequences and modes; allocation shows where functions are realized; interfaces specify interactions and assumptions; assurance links decisions to risks and evidence. A block diagram without behavior or assumptions cannot answer whether the system remains coherent during faults.

Choose views according to **stakeholder questions**, then keep correspondences explicit. A functional model of “authorize trip, assign vehicle, guide rider, complete journey” should correspond to concrete software, people and hardware responsibilities. The correspondence is not always one-to-one.

## State machines prevent impossible narratives

Consider the trip lifecycle:

`REQUESTED → CONFIRMED → ACTIVE → COMPLETED`

Additional paths include `REQUESTED → REJECTED`, `CONFIRMED → CANCELLED`, and `ACTIVE → INTERRUPTED → RESOLVED`. The machine is not merely a picture. It specifies **allowed transitions**, **guards**, **effects** and **invariants**.

Example invariant: A trip must not enter `ACTIVE` before a qualified vehicle is assigned and a boarding location has been communicated. An event handler that skips the guard can violate the service policy even if its individual method passes a unit test.

A **guard** is a condition that must hold for a transition; an **effect** is what the transition changes. A team must decide whether a timed-out external request leaves the system in its old state, produces a retry state, or creates an ambiguous outcome requiring reconciliation. Those are architectural decisions.

## Design-by-contract across services

Suppose dispatch sends `AssignTrip(trip_id, vehicle_id, version)` to a vehicle service. An interface contract should define:

- Schema: fields, units, nullability and validation.
- Semantics: whether the operation creates a reservation, confirms an assignment or merely asks for one.
- State preconditions: only a `CONFIRMED` trip may be activated.
- Timing and failure: deadlines, retries, duplicate events, reordering and partial failure.
- Authority and security: which principal may change assignment and how it is authenticated.
- Observability: correlation ID, version, timestamps and explicit error result.

**Idempotency** is important: processing the same request twice should not create two bookings. Repeated delivery may still occur even when the caller tries only once. A simple strategy stores a stable request key and the associated result, with transactionally enforced uniqueness. This does not magically solve distributed atomicity: downstream side effects require additional design.

## Worked failure scenario

Dispatch publishes assignment A, loses its acknowledgment, retries, and then receives a delayed cancel event. Without versioned state transitions, a vehicle may accept a stale assignment after cancellation. A safer design defines a monotonic assignment version and a legal transition check, records processed event IDs, and treats conflicts as detectable exceptions. State diagrams expose the race; interface contracts specify how implementations respond.

## From model to test

Create a **transition coverage table**. For each allowed edge, test the nominal transition and representative invalid preconditions. Add fault injection: duplicate messages, stale versions, missing acknowledgment and concurrent cancellations. State coverage alone is not behavioral completeness, but it offers a systematic starting point.

A model can be *syntactically correct* and *semantically wrong*. Verification asks whether the model follows its language/consistency rules; validation asks whether its behavior represents intended system use. Model review requires both.

## Practice

**A.** An interface diagram shows two services connected. What essential information is missing? **Answer:** message/data semantics, constraints, timing, failure handling, authority and versioning.

**B.** A trip can be cancelled from `ACTIVE`; must `CANCELLED` always be the terminal state? **Answer:** not necessarily. Recovery, safe stop, compensation and audit may require intermediate states. Define the operational meaning before drawing transitions.

**C.** What is an architecture correspondence? **Answer:** an asserted relationship between elements in different views, such as a function allocated to a component, subject to consistency rules.

**Transfer artifact:** a context view, a seven-state transition table, a written interface contract and three counterexample tests.

## Connections

[Requirements](02-requirements-evidence.md) · [Software quality attributes](04-software-quality.md) · [Digital thread](11-digital-thread.md).  
**Existing primers:** [Views and viewpoints](../../encyclopedia/views-and-viewpoints.md), [Interface control](../../encyclopedia/interface-control.md), [Functional vs physical](../../encyclopedia/functional-vs-physical.md).
