# Chapter 3 — Use cases describe externally valuable behavior

*Book IV: Object-Oriented Analysis and Design · Week 3 — Capture functional requirements with use cases and scenarios*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 3](../labs/lab-03-capture-functional-requirements-with-use-case.md) before attempting [the assessed Week 3 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w03.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **capture functional requirements with use cases and scenarios** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A use case is a goal-driven interaction between an actor and a system under stated preconditions and postconditions. Its main success path is only a skeleton; alternate and exception flows often determine architecture. Avoid treating every button click as a use case and avoid writing only informal user stories without success guarantees.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Use cases describe externally observable goals and their paths through a system boundary, including exceptions that reveal hidden commitments.

### Distinguishing related ideas

A use case differs from a user-interface screen: the same goal may span several screens and services, while a screen may support multiple goals.

### Interpretation and boundary conditions

The important analytical question is what counts as success or justified rejection when payment, capacity or network state changes midway.

## Deeper theory: use cases are contracts about observable behavior

### A useful use case defines a boundary of responsibility

A use case is not a sequence of interface screens or a list of software classes. It describes how an external actor obtains a valued outcome from the system of interest. The actor requests a service; the system guarantees some observable response if stated preconditions hold. That framing determines what counts as success and what must be specified for failures. A booking service that displays “reservation accepted” without durably committing a ride has fulfilled a screen-flow description but violated the actor's implied service contract.

Contract reasoning makes the difference explicit. A precondition states what the environment must establish before the promised behavior begins. A postcondition states what a successful use case guarantees; an invariant states what must remain true in every permitted state. For instance, `confirmed_reservations <= available_capacity` is a candidate invariant only if capacity is defined over a time interval and includes accessibility constraints. If the business allows overbooking with compensation, the invariant must instead capture the intended policy. Precise contracts reveal hidden choices that informal narratives often suppress.

### Exceptional paths are part of the normal specification

Suppose a customer submits a booking and the client times out before receiving a response. The transaction may have been committed, rejected, or not processed. Blind retrying can create duplicate trips unless the operation has a well-defined idempotency policy. A robust use-case description distinguishes request identity, transaction identity, confirmation state, and user-visible recovery. These concerns belong in the externally observable contract even if their implementation later uses message queues or database transactions.

Alternative and exceptional paths should be grouped by the obligation they alter. “No vehicle available” is a business outcome; “identity provider unavailable” is an infrastructure failure; “operator takes manual control” is a mode transition. Their interactions affect consistency, safety, and recovery. Modeling only the happy path creates a design that is easy to draw but cannot guide dependable implementation.

### Temporal properties complement pre- and postconditions

Some requirements are about sequences rather than endpoints. A safety property forbids an unacceptable state: a vehicle must not dispatch without a valid authorization. A liveness property demands eventual progress: a valid accepted booking must eventually be served or explicitly canceled within a bounded interval. An invariant can protect against an unauthorized dispatch yet still permit requests to remain stuck forever. Both kinds of property are needed.

Time also determines whether conditions are meaningful. A reservation confirmed at 08:00 cannot rely on capacity measured at 07:50 if vehicles may be reassigned in between. The design needs a rule for when availability is reserved, when it expires, and what concurrent transactions are permitted. These timing semantics later shape sequence diagrams, state machines, locking or messaging choices, and acceptance tests.

### Behavioral decomposition must preserve the external promise

A use case can be decomposed into collaborating responsibilities, but the decomposition is correct only if the collaborators collectively satisfy the observable contract. Allocating identity, scheduling, dispatch, and notification to separate services creates interface obligations about order, failures, retries, and compensation. No collaborator should be assigned a requirement it cannot satisfy alone, such as “guarantee end-to-end trip completion.” That guarantee belongs to the composed service and demands evidence at the integration level.

Use cases therefore serve as a bridge from stakeholder language to formal contracts and architecture. Their value is not the number of pages describing interaction but how sharply they expose success, refusal, recovery, concurrency, and accountability before the design hardens.

## Worked Northstar example

BookTrip begins with an authenticated rider and an available service window; success creates exactly one confirmed reservation. If no capacity exists, the system returns an explicit refusal and leaves no partial allocation. If an answer is lost, retry must not create a second reservation.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Fully dressed use-case miniature

**Actor:** authenticated passenger. **Goal:** reserve one place on a shuttle. **Precondition:** service is operating and a request identifier is available. **Success guarantee:** exactly one confirmed reservation exists for that identifier. **Main path:** passenger chooses a trip; system checks the service window; system obtains a capacity hold; system records and returns confirmation. **Alternative:** when capacity is exhausted, system returns rejection with no hold. **Failure extension:** acknowledgement is lost after commit; client retries with the same key and retrieves the existing confirmation.

The success guarantee is not a promise that every booking succeeds. It is an invariant about *what success means*. Do not write the failure extension as “the system retries until it works”; define retry limits and the surviving state.

## What can go wrong—and why

A use-case model without alternate flows gives designers no contract for recoverable failure.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 3: Use cases describe externally valuable behavior](../labs/lab-03-capture-functional-requirements-with-use-case.md), you will: Write a fully dressed BookTrip use case with three alternate paths and one idempotency invariant. Trace steps to domain objects and obligations. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 3 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](02-elicit-and-structure-software-requirements.md) and leads toward [next chapter](04-discover-candidate-classes-and-build-the-stat.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w03.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
