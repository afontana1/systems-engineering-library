# Chapter 5 — Sequence models expose missing responsibility

*Book IV: Object-Oriented Analysis and Design · Week 5 — Analyze dynamic behavior and discover collaborations*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 5](../labs/lab-05-analyze-dynamic-behavior-and-discover-collabo.md) before attempting [the assessed Week 5 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w05.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **analyze dynamic behavior and discover collaborations** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A sequence diagram describes collaborations for a scenario, including messages, ordering and control transfers. An object should not be asked to decide based on data it does not have; excessive controller logic can reveal poor responsibility allocation. The diagram must remain consistent with domain state changes.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Message sequences reveal distributed responsibility

A sequence diagram is not valuable simply because it orders calls from top to bottom. It represents who is permitted to make decisions, which information each party possesses, and where synchronization or failure occurs. If a booking service asks a fleet allocator for a vehicle and immediately confirms before the allocator has durably reserved capacity, the sequence contains a race even though every message arrow is syntactically valid.

The deeper issue is knowledge across time. One component may know that it sent a command without knowing whether the receiver executed it. A timeout does not imply failure; a retry does not imply safety. Sequence analysis must distinguish **command**, **acknowledgment**, **commit**, and **notification**. Showing alternate and failure flows is therefore not optional decoration: it clarifies the semantics of partial completion. The design must specify whether compensation, deduplication, or a shared transaction boundary restores the intended invariant.

## Deeper theory: interactions, time, and the location of responsibility

A static object model answers which kinds of things exist and how they are related. It cannot by itself explain how a customer request becomes a durable promise. That explanation requires **collaboration among participants over time**. Sequence models make these collaborations visible, but they are only useful when their messages correspond to meaningful domain transitions rather than a screen-by-screen transcription of a user interface.

In Northstar, `RequestPickup` may pass through input validation, eligibility checks, capacity allocation and notification. An apparently natural design sends `validate` and `reserve` messages to several collaborators in succession. Yet the critical question is not how many messages are drawn. It is where the system establishes the *commit point*: the moment after which the customer is entitled to rely on the reservation. A message labeled `OK` before capacity is durably allocated is an acknowledgment, not a business commitment. The distinction determines which failures must be recoverable and which effects must be idempotent.

### Sequence diagrams are partial orders, not movie scripts

A message diagram is often read as a single execution trace, but many systems contain concurrency, retries, asynchronous callbacks and timeouts. One scenario cannot represent the entire behavior space. In a synchronous call, the caller may wait for a response while the server continues processing. In an asynchronous workflow, messages can be delivered out of order, more than once, or after the sender stops waiting. The logical structure is a **partial order of events**: some causally precede others, while concurrent events need not have one globally agreed order.

Suppose two users request the last vehicle position at nearly the same time. A sequence diagram showing request A followed by request B does not prove the system will behave correctly if B reaches a storage service first. The relevant correctness property concerns **all permitted interleavings**. A capacity-allocation object may need an atomic compare-and-update operation, optimistic concurrency control, or another consistency mechanism. The design should identify that mechanism rather than assume a single threaded diagram captures reality.

### Behavioral responsibility follows ownership of change

One design puts every decision in a coordinator that instructs passive objects. Another distributes decisions among domain objects that maintain their own invariants. Neither is universally correct. The question is which component has the authority, information and transactional capability to preserve important rules while keeping coupling manageable. A booking coordinator can orchestrate steps, but a reservation state transition should not depend on arbitrary UI behavior. Likewise, capacity ownership should be explicit so that retries do not create duplicate allocations.

An object interaction can be specified using a **precondition**, a **postcondition**, and a **frame condition**: what must be true before an operation, what it guarantees afterward if successful, and which state it does not modify. For `ReserveSeat`, an illustrative contract is that the request is eligible and capacity exists; success yields exactly one committed reservation with an unchanging identifier; unrelated reservations remain unaffected. The frame condition matters because a method that achieves a local goal by silently changing other reservations can pass a narrow happy-path test while violating system meaning.

### Lifecycle models complement collaborations

A state machine defines states such as `Requested`, `Confirmed`, `Active`, `Completed`, `Cancelled`, with legal transitions and guards. A sequence diagram shows how participating objects coordinate to cause one of those transitions. If a sequence diagram contains `Completed → Confirmed` without an explicit exceptional rule, it conflicts with the lifecycle model. This conflict is valuable: it exposes the need for a new domain event, such as a correction or rescheduling transaction, rather than an ad hoc overwrite of history.

Time introduces more than ordering. A deadline is a property of elapsed time, while eventual progress is a property of state transitions under fairness assumptions. A promise that every request *eventually* receives a decision can be logically satisfied after several days, even if passengers need a decision within thirty seconds. The behavior contract must distinguish **liveness** from **bounded response**, and its implementation must identify which components control the clock and how timeouts are interpreted.

The deeper aim of interaction modeling is to discover where domain promises are established and revoked. Good diagrams let a reviewer trace a business claim through messages, state ownership, failure handling, and recovery without confusing a method invocation with the successful completion of the mission.

## Worked Northstar example

BookingService asks CapacityPolicy whether a slot is available, requests a durable hold from ReservationRepository, then publishes confirmation. If publishing fails after the hold, a retry must discover the existing reservation rather than reserve another vehicle. The sequence needs an explicit compensation or idempotency path.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Diagrams that show only successful synchronous calls conceal timing, retry and partial-failure semantics.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 5: Sequence models expose missing responsibility](../labs/lab-05-analyze-dynamic-behavior-and-discover-collabo.md), you will: Draw normal, timeout and duplicate-message sequences. Identify who owns the idempotency key and how the result survives restart. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 5 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](04-discover-candidate-classes-and-build-the-stat.md) and leads toward [next chapter](06-model-state-dependent-behavior-and-conduct-th.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w05.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: sequence models and collaboration boundaries

### 5.1 Derive messages from responsibilities

A useful dynamic design model makes it clear **who knows a fact and who can change it**. In `UC-02`, a dispatcher initiates a command; `ReservationService` validates the token and request; `AssignmentPolicy` evaluates eligibility; a repository commits reservation, assignment and audit event. This division ensures that the UI is not the system of record and that policy is testable without a live database.

| Order | Message | Contract |
|---|---|---|
| 1 | `submit(token, payload)` | Request has authenticated actor and canonical payload |
| 2 | `findExisting(token)` | Existing result must agree with payload |
| 3 | `isEligible(vehicle, request, observation)` | Accessible and freshness rules hold |
| 4 | `commitAssignment(...)` | Transaction preserves active-slot uniqueness |
| 5 | `appendEvent(...)` | Audit record committed atomically with state change |
| 6 | `return(reservationId)` | ID identifies durable committed reservation |

Sequence order does not itself provide atomicity. An interaction diagram showing a check before an insert may accidentally expose a race: two handlers each see an empty slot, then both insert. The linearization point must be tied to a real database uniqueness constraint or another justified serializing mechanism. See the [executable transaction example](../tools/step03_book4_contract_check.py).

### 5.2 Make failures explicit

Consider the failure after the reservation row is inserted but before its assignment row is written. If these operations share a transaction, rollback returns the database to its previous valid state. If the audit writer is an independently reachable service, transaction boundaries are no longer automatically shared. A design might instead use a transactional outbox and asynchronous delivery, which changes the external consistency contract and demands retry/deduplication tests. The case deliberately keeps the audit event in one SQLite transaction to teach the simpler guarantee without claiming distributed atomicity.

A message sequence should include guards and exceptional responses. With an accessibility-required request, policy rejection must occur before the commit. With stale telemetry, the caller receives a rejection that communicates the freshness reason without exposing another rider's information.

### 5.3 Quantifying interactions

The baseline budgets 120 ms for authentication, 80 ms for policy, and 150 ms for commit and event: a **serial-path estimate** of \(350\) ms. If authentication and policy can safely overlap, a different model is necessary: \(L_{parallel}=\max(L_{auth},L_{policy})+L_{commit}\), which equals \(270\) ms for the illustrative values. Parallelization is not an automatic optimization; policy might depend on identity attributes, invalidating independence. And neither equation establishes a measured tail latency.

**Solved checkpoint.** Two identical HTTP retries arrive at nearly the same instant. A sequence diagram with `findExisting()` followed by `insert()` is insufficient. The durable unique token index provides the conflict point; the losing request must query the committed winner and verify payload identity before returning the original result.

**Exercise.** Add a notification service that is temporarily unavailable. Show two designs: one in which notification failure rolls back booking, and another where booking commits and notification retries asynchronously. State the user-facing guarantees and operational tradeoffs of each.
