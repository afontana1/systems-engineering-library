# Chapter 11 — Persistence design is about identity and failure recovery

*Book IV: Object-Oriented Analysis and Design · Week 11 — Design persistence and conduct the Design Readiness Review*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 11](../labs/lab-11-design-persistence-and-conduct-the-design-rea.md) before attempting [the assessed Week 11 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w11.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **design persistence and conduct the design readiness review** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Persistence maps domain identity and lifecycle to durable storage while preserving transactional invariants. Distinguish an object reference from a stable identifier; repositories need explicit concurrency behavior. Migration plans must preserve meaning across versions, not merely copy columns. Query performance is part of the design when latency matters.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Persistence is a temporal identity problem

Persistence is often taught as selecting tables or object-relational mapping rules, but the central question is what must remain true across crashes, retries, migrations, and software upgrades. A reservation ID, vehicle ID, and request key refer to entities with different lifecycles. Conflating them can make a restarted service interpret an old command as a new reservation or lose the ability to reconcile a partial transaction.

A durable data model encodes **identity**, **invariants**, and **history**. An event log can preserve change provenance but may require projections to answer current-state queries efficiently. A relational snapshot can support strong consistency while hiding the causal sequence that produced a value unless history is retained separately. Schema migration is consequently a behavior change: old and new versions may disagree about valid states. The appropriate design depends on failure recovery requirements and which statements must remain auditable—not simply on storage performance.

## Deeper theory: persistence is a model of identity across failures and time

### Object identity and stored identity solve different problems

An object in memory may be represented by a reference valid for one process lifetime. A durable trip record must remain identifiable after restart, migration, schema change, and integration with outside systems. A synthetic immutable identifier can stabilize references when human-facing attributes change; a natural key such as passenger email is mutable and may not even be unique over time. Identity, uniqueness, and equivalence are separate notions. Two versions of one trip are not two different trips, and two identical-looking bookings may still be distinct obligations.

Persistence also forces engineers to define the boundaries of an aggregate: which state transitions must succeed or fail together? If assigning a vehicle requires reserving its capacity and recording the trip, a transaction should prevent one step from committing without the other when those records share an atomic boundary. Across independent services, a single database transaction may be unavailable. A saga or compensating-action protocol trades strong atomicity for explicit recovery states; it does not guarantee that the world returns perfectly to its original state after every failure.

### Concurrency is a domain invariant problem

Suppose two dispatch workers observe one free accessible seat and both attempt to allocate it. Validating availability before updating it is insufficient if both reads occur before either write. Pessimistic locking, serializable transactions, or optimistic concurrency with a version check can protect the invariant that confirmed allocations do not exceed capacity. The right mechanism depends on contention, latency, failure mode, and the cost of retries. Database isolation-level labels are not interchangeable promises: the engineer needs to know which anomalies the chosen mechanism actually prevents.

Messaging adds another layer. If an assignment event is delivered twice after a crash, the consumer should not charge the passenger twice or allocate a second seat. An idempotency key ties repeated deliveries to one logical command. “Exactly once” is rarely an end-to-end property without carefully defined transactional boundaries; application-level deduplication and recovery are often more realistic. A durable outbox can bridge database changes and message publication, though it still requires duplicate-tolerant consumers.

### Historical truth and operational truth can diverge

Event sourcing retains a sequence of recorded domain changes from which projections are rebuilt. It can improve auditability, but only if event meaning and version evolution remain controlled. Replaying events using new code may produce a different projection unless business rules, schemas, and migrations are handled deliberately. A mutable current-state table answers “What does the system currently believe?”; an append-only record can additionally answer “What did it believe when a decision was made?” Both may be needed for Northstar's incident reconstruction.

Durability is also constrained by privacy, retention, and deletion duties. Keeping every rider event forever may assist debugging yet violate justified data-minimization limits. Engineering design should define retention classes, cryptographic protection, access authority, audit logging, and legally required erasure pathways without assuming one storage pattern solves all objectives. The definitive persistence design states identities, invariants, transaction boundaries, recovery behavior, temporal semantics, and evidence of restore capability—not merely table names and object-relational mappings.

## Worked Northstar example

Two booking processes both read “slot free.” Without serialization or a uniqueness constraint, both can commit overlapping reservations. Use an atomic conditional write or unique constraint with retry. A cache improves reads but cannot be the sole authority for a safety-relevant slot hold.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### A concrete concurrency anomaly

Two transaction workers both read “vehicle slot free,” each decides to insert a reservation, and each commits. Under weak isolation and without a uniqueness rule, both may succeed. A possible control is a database constraint on a normalized active slot key, with a transaction that retries or reports a conflict. That solution has tradeoffs: interval overlap is more complex than equality on discrete slots, and a cache cannot be the independent source of truth.

The design needs an identity strategy for requests, an isolation/constraint mechanism, recovery semantics and an executable two-worker test. A reassuring class diagram alone cannot rule out the race.

## What can go wrong—and why

Database schema diagram completeness is not evidence that concurrent operations preserve business rules.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 11: Persistence design is about identity and failure recovery](../labs/lab-11-design-persistence-and-conduct-the-design-rea.md), you will: Design a reservation table and transaction with a concurrency test. Plan migration of status values while two service versions are deployed. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 11 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](10-express-precise-constraints-with-ocl-and-exec.md) and leads toward [next chapter](12-baseline-and-defend-the-integrated-ooad-desig.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w11.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Advanced worked practice

- [Deep workshop — Responsibility, Persistence, and Concurrent Design](../practice/design.md)
- [Corresponding independent laboratory](../practice/lab-design.md)
- [Interactive workbench](../practice/WORKBENCH.html)

## Step 03 integrated reference: persistence, transactions, and recovery

### 11.1 A schema can enforce a domain invariant

The synthetic repository uses separate reservation, assignment, and audit-event tables. The essential concurrency defense is a **partial unique index**:

```sql
CREATE UNIQUE INDEX one_active_vehicle_slot
  ON assignment(vehicle, slot)
  WHERE state = 'ACTIVE';
```

It permits multiple historical released assignments while excluding two simultaneously active assignments for the same vehicle and slot. SQLite's constraint is a useful demonstration of the invariant; it does not address interval overlaps, distributed stores, clock semantics, or a production authorization model.

A separate `UNIQUE(token)` reservation constraint establishes stable retry identity, but a duplicate token is safe to reuse only when its immutable payload matches the original. Otherwise token collision can alias two different user intents. A robust API must also define token scope, lifetime, and actor binding, not simply place arbitrary strings in a column.

### 11.2 Preserve cross-table invariants atomically

The booking transaction must insert the reservation, active assignment, and audit event as one commit or roll them all back. In the [Python demonstration](../tools/step03_book4_contract_check.py), a failed assignment insert causes the reservation insert to roll back. Cancellation similarly releases the active assignment and records a cancellation event in one transaction. These examples use standard-library `sqlite3` and do not need a network service.

The recovery rule should say what is durable, not just “use a transaction.” If a process crashes after commit but before returning a response, retry must return the already committed reservation. If it crashes before commit, retry may create it exactly once under the unique token constraint. Testing both sides of this boundary is essential to the claimed idempotency contract.

### 11.3 Decision boundary and sizing

The illustrative synchronous path is \(L=120+80+150=350\) ms against a 500-ms target, leaving a 150-ms arithmetic margin. That is a budget, not performance evidence. Database lock contention, filesystem behavior, transaction logging, and loaded workloads may change tail latency. A measurement plan must declare throughput, contention mix, percentile and baseline hardware; the test data should record actual outcomes rather than reuse these budget numbers as observations.

The schema does not specify personally identifiable information retention. A real design requires a privacy threat model, access restrictions, auditable deletions or retention, and migration policy. An audit record can need long-lived provenance even when rider-identifying data must be minimized—an explicit design tension.

**Solved checkpoint.** `F-05` tries to assign a second reservation to `V-01` in `AM-01`. The unique index rejects it, the transaction rolls back, and no orphan reservation becomes visible. A preflight `SELECT` by itself would not have guaranteed this result under concurrency.

**Exercise.** Extend the schema to support a time interval. Propose a locking or exclusion mechanism appropriate to your chosen database engine and a two-client race test. Explain why copying SQLite syntax directly to another engine may not preserve semantics.
