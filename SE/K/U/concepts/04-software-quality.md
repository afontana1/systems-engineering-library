# 04 · Software architecture, distributed behavior, and quality attributes

**Concept dossier · OOAD / software systems engineering / digital engineering**

## Quality attributes change architecture decisions

Functionality answers “What does the system do?” A **quality attribute** addresses *how well* it performs in a specified environment: reliability, latency, modifiability, security, safety, recoverability and more. These attributes interact. A replicated service may improve tolerance to one host failure yet introduce more coordination and data-consistency failure modes.

Express a quality concern as a **scenario**, not an adjective:

> During a single-node failure while trips are active, the dispatch service shall restore authorized assignment queries within an agreed recovery interval without creating duplicate active assignments.

This has a stimulus, environment, artifact, response and measurable response metric. The recovery interval needs stakeholder justification; it is not a universal architecture constant.

## A distributed service is a partial-failure machine

In a monolithic program, a function call usually succeeds or throws locally. Across a network, a timeout does **not** reveal whether the remote service performed the action. The request may have succeeded while its response was lost. Retrying is often necessary, but duplicate execution can corrupt business state unless operations are idempotent or compensatable.

A robust trip-assignment interaction might use:

1. A stable idempotency key per requested assignment.
2. A durable write that atomically records assignment state and a pending event.
3. A delivery mechanism that may retry events.
4. Consumers that deduplicate and enforce versioned state transitions.
5. Reconciliation for exceptions, delayed messages and orphan assignments.

These mechanisms improve behavior under selected faults; they do not promise exactly-once end-to-end effects. Define consistency boundaries, transactions and failure semantics explicitly.

## OO responsibilities are part of the solution

Object-oriented design helps assign coherent responsibilities: `Trip` owns legal lifecycle transitions; `AssignmentPolicy` chooses among eligible vehicles; `NotificationGateway` hides a provider-specific protocol; `AuditRecord` captures attribution. Avoid “god objects” that know every subsystem. Also avoid blindly splitting everything into microservices, which converts local method calls into network uncertainty and deployment cost.

**Domain invariant:** A single active trip cannot be assigned simultaneously to two distinct vehicles unless an explicit handoff protocol allows a brief transitional representation. This invariant belongs at the authoritative state boundary, not only in a UI check.

## Trade-off worked example

Architecture A uses a central single-writer dispatch service. It simplifies global assignment invariants but creates a dependency on its availability. Architecture B permits regional writers and later reconciliation. B may reduce latency during partitions but risks conflicting assignments and complex reconciliation. Choose based on operational scenarios, failure consequences and the consistency properties stakeholders actually need—not a slogan about “scalability.”

Security must also be scenario-based. A valid login is not sufficient if one contractor can issue unauthorized trip reassignment commands. Specify principal, action, object, context, audit and deny-by-default behavior; include malicious inputs and credential expiry in tests.

## Observe and test

Collect correlated request IDs, outcome metrics, failures, clock/ordering assumptions, resource saturation, retries and reconciliation events. Test concurrency and recovery with controlled fault injection, then evaluate whether evidence matches the required operating envelope. A clean unit-test suite does not establish distributed-service resilience.

## Exercises with answers

**A.** A request timed out. Is it safe to repeat it? **Answer:** only if the operation and its downstream effects are designed for repeated delivery or compensation; a timeout does not imply nonexecution.

**B.** Does two-instance replication double availability? **Answer:** no. Shared dependencies, correlated failures, routing and recovery design matter; availability is not simply an instance count.

**C.** Name a quality-attribute trade. **Answer:** strongly consistent assignment simplifies exclusivity but may reduce availability during a network partition; quantify impacts in defined scenarios.

**Transfer artifact:** a quality-attribute scenario catalog, two alternative architecture decision records and a failure-injection matrix.

## Connections

[State and interface models](03-architecture-states.md) · [Reliability and resilience](10-reliability-resilience.md) · [Agile assurance](12-agility-assurance.md).  
**Existing primer:** [Software quality attributes](../../encyclopedia/software-quality-attributes.md).
