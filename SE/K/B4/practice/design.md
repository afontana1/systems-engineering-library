# Advanced Workshop · Responsibility, Persistence, and Concurrent Design

*Book 4 · Week 11 · domain boundaries · optimistic concurrency · repository patterns · design review*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-design.md). The assessed course obligations remain in [the curriculum](../../../C/P1/EN605704.html).

## 1. Distinguish objects from tables and endpoints

A software system that stores reservation records can still be poorly object-oriented. If a single `TripService` class validates authorization, calculates routes, edits database rows, emits messages, and controls the GUI, the named classes do not give meaningful separation of concerns. The purpose of OO design is to assign responsibilities so that each change has a predictable location and each invariant has a clear owner. Domain entities such as `Reservation`, services such as `AllocationPolicy`, and infrastructure adapters such as `ReservationRepository` play different roles.

The first decision is not which pattern to use. It is **which information and rules must change together**. The reservation's state transition and the consumption of seat capacity cannot be updated independently if the architecture promises no double allocation. A repository hides persistence details; it does not make two separate writes atomic. Transaction boundaries cross class boundaries, and the design must make those boundaries explicit.

## 2. A minimal aggregate and its contract

Suppose `Reservation` owns its state transitions, a `VehicleLoad` aggregate owns capacity, and an `AllocationCoordinator` performs a transaction that updates both or neither. The coordinator should not expose general `setStatus()` operations. Instead it accepts `reserve(request_key, vehicle_id)` and validates identity, vehicle capacity, service window, and idempotency. Its output is a typed result such as `Confirmed(id)`, `Rejected(reason)`, or `Conflict(expected_version, actual_version)`. A rejected operation should not leave a half-reserved seat.

This boundary is a design hypothesis, not a universal answer. In a distributed architecture where a single transaction cannot span systems, use a saga with compensating actions and define provisional states. The policy must state what happens if the compensation fails. The inability to guarantee global atomicity is an architectural tradeoff to expose at design review, not a reason to describe eventual consistency as instant correctness.

## 3. Worked example: optimistic locking

A reservation begins at version 0 with state `REQUESTED`. Analyst A reads `(0, REQUESTED)` and proposes `HELD`; analyst B reads the same version and proposes `CANCELLED`. If A commits first, the record becomes `(1, HELD)`. B's update must be conditional on the expected version still being 0. It therefore returns `CONFLICT` and changes nothing. B then rereads version 1 and applies the business rule for cancelling a held reservation. In the included model, `commit(0, 'HELD')` succeeds while `commit(0, 'CANCELLED')` conflicts.

Optimistic concurrency is appropriate where collisions are infrequent and transactions can be retried safely. It does not solve all races: two aggregates can each be updated consistently while a cross-aggregate invariant fails. It also does not guarantee fairness or prevent starvation when collisions persist. Document when you need a pessimistic lock, unique constraint, outbox, single-writer dispatcher, or revised aggregate boundary.

## 4. Patterns can preserve or hide intent

The **Repository** pattern provides an abstraction over loading and saving aggregate state. The **Strategy** pattern can isolate alternative allocation policies. **State** objects can encapsulate complex state-specific behavior, but are not mandatory for a small, stable transition matrix. The **Observer** pattern fits notification, but business correctness must not depend on an observer that might run later or fail. Prefer the least elaborate design that preserves the required invariants and permits substitution under test.

Evaluate every proposed pattern against a concrete anticipated change. If dispatch policy may change from earliest-available to accessibility-prioritized, a replaceable policy is valuable. If the only effect of introducing eight factories is to make the call graph longer, the pattern may worsen maintainability. Architectural quality is evidenced by focused changes and reproducible tests, not by the number of named patterns drawn.

## 5. Design an evidence-bearing review

A mature design review includes a responsibility map, an interaction sequence for a success case and a failure case, a storage consistency statement, a concurrency hazard, a migration path, and tests for atomicity and recoverability. If a schema migration adds `version` but old clients ignore it, the new guard may be ineffective. If an event is published before commit, a downstream consumer may observe a reservation that later rolls back. Solve these questions at the design boundary rather than declaring that a database makes everything safe.

The course's Week 11 persistence and readiness work is an appropriate place to evaluate these claims. A strong submission is able to trace a scenario all the way through domain behavior, persistence, events, and acceptance evidence without relying on undocumented framework magic.

## Worked problem set — attempt before revealing solutions

### Problem 1

Two writers read version 4; the first updates to 5. Should the second succeed with an update conditioned on version 4?

<details><summary>Show solution 1</summary>

No. It must report a conflict because its view is stale. A separate business-level retry may reread the state and re-evaluate validity.

</details>

### Problem 2

A message is emitted before the booking database transaction commits. What failure can occur?

<details><summary>Show solution 2</summary>

A consumer can act on an event for a booking that is rolled back. Use an outbox or other transactional publication strategy with duplicate-safe consumers.

</details>

### Problem 3

When is a Strategy object better than a large conditional?

<details><summary>Show solution 3</summary>

When the allocation algorithm varies independently, is expected to change, and its alternatives can be tested under one contract. A stable three-branch rule may be clearer as a conditional.

</details>

### Problem 4

Can a repository guarantee a cross-service seat-capacity invariant?

<details><summary>Show solution 4</summary>

Not merely by being a repository. The transaction/coordination design must enforce the invariant, or the system must explicitly represent provisional states and compensation.

</details>

## Independent transfer to the Northstar case

Compare two designs: one monolithic booking handler and one domain/infrastructure separation. Trace a duplicated reservation event across each design. Simulate two writers with the supplied versioned-trip implementation. Draw a sequence diagram for the failure path and propose a transaction boundary, event-publication rule, and five architecture tests. Include one reason not to adopt a new design pattern.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-design.md) · [Python source](book4.py) · [Experiment dataset](book4-requests.csv) · [Interactive workbench](WORKBENCH.html).
