# Chapter 1 — Analysis discovers concepts; design assigns responsibilities

*Book IV: Object-Oriented Analysis and Design · Week 1 — Establish the OOAD problem, scope, and modeling discipline*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 1](../labs/lab-01-establish-the-ooad-problem-scope-and-modeling.md) before attempting [the assessed Week 1 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w01.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **establish the ooad problem, scope, and modeling discipline** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Object-oriented analysis starts in the problem domain rather than code syntax. A class candidate represents an enduring concept with identity, state and behavior, not every noun in a stakeholder interview. Separate domain objects from UI controls, persistence records, and external integrations. Use traceable scenarios to decide which concepts are stable enough to model.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Object-oriented analysis discovers enduring domain concepts and invariants before design commits to classes, storage or implementation patterns.

### Distinguishing related ideas

An actor is an external role; an object is a modeled entity with identity and state; a class is a design abstraction. Similar nouns may imply very different responsibilities.

### Interpretation and boundary conditions

Model a reservation's lifecycle before deciding whether it should be a database row, an event stream or an in-memory object.

## Worked Northstar example

Request, Trip, Vehicle and Assignment are plausible domain concepts. “Blue Button” is UI presentation and “database row” is storage representation, neither an automatic domain class. A Trip retains identity through reassignment while its Assignment changes.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Premature implementation classes make the analysis model brittle; pure noun harvesting creates empty classes with no defensible responsibility.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 1: Analysis discovers concepts; design assigns responsibilities](../labs/lab-01-establish-the-ooad-problem-scope-and-modeling.md), you will: Read an invented dispatcher interview and propose six candidate objects, rejecting at least three false candidates with reasons. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 1 deliverable and grading rubric.


## Graduate depth: object models as boundaries of responsibility
### Domain discovery precedes class design

Object-oriented analysis begins by understanding concepts that matter to the problem, not by converting every noun in an interview into a class. “Passenger,” “trip request,” “fare,” and “vehicle assignment” might denote persistent identities, temporary values, policies, or events. Their distinctions depend on business invariants and behavior. A request may be a durable entity with identity over time; a location reading is often a value with no independent lifecycle; a cancellation is an event whose causal relevance comes from when it occurred. Treating every noun as an object encourages anemic data containers and poorly located responsibilities.

The domain boundary also establishes ownership of truth. If an external dispatch service owns vehicle eligibility, a local `Vehicle` object may hold a versioned snapshot rather than authoritative state. This difference affects consistency, failure recovery, and security. A conceptual class diagram may express associations and multiplicities, but it should also expose lifecycles, invariants, and the actions that can legitimately change state. Analysis can remain technology-neutral while still imposing strong semantic obligations on later design.

### Invariants clarify why an abstraction exists

An invariant is a property that must remain true across every permitted state transition. For a journey request, one possible invariant is `assigned_vehicle != null` only when the request is in an assigned or later compatible state. A stronger safety rule might require every door-opening authorization to reference a currently valid service and interlock state. These are illustrative rules; the actual invariants depend on an explicit safety and operating specification. An object operation can be described by a precondition, postcondition, and frame condition identifying what it must not change.

This is design-by-contract reasoning. If a cancellation operation is invoked, its precondition might permit cancellation only from certain states; its postcondition records a terminal outcome and releases a reservation; its frame condition protects unrelated rider records. When a method has many side effects across unrelated concepts, the model is signaling tangled responsibilities. A well-chosen abstraction groups data with behavior necessary to protect an invariant, not merely data fields that occur in the same document.

### Coupling is both a technical and organizational cost

Dependencies between classes can propagate change and errors. A component that directly knows payment, routing, telemetry, and notification details becomes expensive to modify and hard to test. Dependency inversion and explicit interfaces can reduce coupling, but abstraction also has overhead. A tiny prototype may not justify elaborate service boundaries; a long-lived safety-critical product may. Decisions should follow expected change rates, failure consequences, and the need for independent testing.

In the Northstar case, the routing engine should not silently authorize boarding simply because it calculated a route. Separating planning from safety authorization establishes an enforceable boundary and a clearer test surface. Still, drawing an interface does not guarantee runtime isolation: shared databases and privileged credentials can defeat the intended separation. Object analysis therefore connects to architecture, safety assurance, and access-control design. The goal is not the maximum number of objects, but a conceptual model in which important responsibilities and constraints are visible, stable, and defensible.

## Continuity

This chapter builds from the earlier Foundation books and leads toward [next chapter](02-elicit-and-structure-software-requirements.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w01.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: defining the domain and its invariants

### 1.1 The difference between a concept and a software responsibility

Continue the [NS-OO4.1 reservation-service case](../case/INDEX.html) throughout this book. A rider makes a reservation; a dispatcher allocates a vehicle; a cancellation frees capacity. The **analysis** model answers what must remain true even if the implementation changes. The **design** model answers which components will enforce those truths. The vocabulary overlaps but the models are not interchangeable.

A `Reservation` has a stable identity and lifecycle; a `Vehicle` has eligibility attributes; an `Assignment` relates a reservation to a vehicle for a defined time slot. A `ReservationService` is a service boundary, not automatically a domain entity. A button and a database row are presentation and persistence constructs. Classifying them separately prevents the common mistake of treating every noun as a class.

| Analysis concept | Identity or value? | Domain rule | Candidate design owner |
|---|---|---|---|
| Reservation | Entity: survives reassignment | A request token cannot create two different reservations | ReservationService + repository |
| Assignment | Association entity: slot-specific | Only one active assignment per vehicle and slot | AssignmentPolicy + persistent constraint |
| Location reading | Timestamped value | Age at the decision must not exceed 15 s | Eligibility policy |
| Audit event | Immutable fact | Describes actor, transition and committed version | Transactional audit writer |

This classification is an *hypothesis*. Challenge it with change scenarios: if reservation identity survives a reassignment, `Assignment` cannot be the same entity as `Reservation`. If a location reading is updated in place, the system loses the exact information used to authorize an earlier allocation. Thus its observation time and provenance must survive long enough for the intended evidence purpose.

### 1.2 Turn business rules into proof obligations

For a vehicle \(v\) and service slot \(s\), define the set of active assignments

\[
A(v,s)=\{a\mid a.vehicle=v \land a.slot=s \land a.state=ACTIVE\}.
\]

Requirement `SW-02` becomes \(|A(v,s)|\leq 1\). This statement is stronger than the procedural suggestion “check whether a vehicle is already booked.” A read-before-write check can be true for two competing requests at the same time. The invariant must be preserved at the mutation boundary, including under contention.

`SW-05` adds an implication: an accessibility-required reservation that has an active assignment must be assigned an accessibility-eligible vehicle. `SW-03` adds a token-to-reservation mapping: repeated requests with the *same* token **and payload** return the same durable identity, while reuse with a changed payload is an error. These are three distinct obligations; no single class diagram proves them.

### 1.3 Scope and evidence

The case assumes one reservation database and discrete service slots. It omits schedule overlaps across adjacent slots, live safety interlocks, authorization, real-world privacy policy, and cross-region replication. The diagrams therefore do not constitute a safety case or a production architecture. The [case baseline](../case/model-baseline.json) and [diagram](../diagrams/oo4-reservation-model.svg) are controlled examples; the [Python/SQLite checker](../tools/step03_book4_contract_check.py) tests selected invariants, not all environmental claims.

**Solved checkpoint.** A team calls `TripRequest`, `Reservation`, `BlueConfirmButton`, and `INSERT` four “business classes.” Keep `Reservation` as an entity, treat `TripRequest` as an input command unless it has a separately evidenced lifecycle, classify the button as presentation, and `INSERT` as a persistence operation. The distinction allows the UI or database technology to change without redefining the customer's business rule.

**Exercise.** A trip can span two slots. Modify \(|A(v,s)|\leq1\) so that overlapping time intervals, not equal slot labels, count as conflict. Explain why a unique `(vehicle,slot)` index would then be insufficient. An acceptable answer proposes an interval-overlap predicate and a transaction/locking enforcement mechanism, not merely an extra `if` statement.
