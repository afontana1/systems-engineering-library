# Chapter 5 — Behavior is a family of complementary projections

*Book III: Introduction to Model-Based Systems Engineering · Week 5 — Behavior modeling: use cases, activities/actions, interactions, states, and modes*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 5](../labs/lab-05-behavior-modeling-use-cases-activities-action.md) before attempting [the assessed Week 5 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w05.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **behavior modeling: use cases, activities/actions, interactions, states, and modes** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Use cases state externally visible goals; activities describe flow and control; sequences identify interactions; state machines constrain legal lifecycles. These are different answers to different questions. Begin with the observable mission event, then add details only where they improve assurance. State transitions require guards, triggering events and observable effects. Treat rejected and interrupted states as first-class behavior.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Multiple behavior views are complementary projections

Activity flows, sequences, and state machines emphasize different properties of the same system. An activity view helps explain the causal or informational steps needed to produce an outcome. A sequence view shows interactions across participants and makes ownership of messages visible. A state machine constrains which transitions are legal for an entity at a given moment. None fully subsumes the others. A reservation can follow a plausible activity path while violating its lifecycle by being accepted twice after concurrent requests.

These views must be reconciled through shared identities and event definitions. If “cancel” means a user request in one diagram but a completed cancellation in another, superficially matching labels hide incompatible semantics. Use a traceable event vocabulary and check whether each behavioral model admits or forbids the same important scenarios. The richest insight often appears where two valid-looking views disagree: that discrepancy reveals a missing condition, an unstated authority, or a transition that was never specified.

## Deeper theory: behavioral views and the semantics of observable events

A behavioral model tries to say what a system can do, in what order, and under which conditions. Different diagram types capture different **projections of one underlying behavior**. A use case emphasizes a goal achieved through actor-system interaction. An activity model emphasizes flows of control or objects through actions. A sequence model emphasizes message ordering among participants. A state machine emphasizes how the future actions available to an entity depend on its history. None is a complete definition of the system, and two diagrams can each look plausible while asserting incompatible behavior.

The theoretical foundation is a **transition system**. Let \(S\) be the set of states, \(E\) the set of events, and \(\rightarrow\subseteq S\times E\times S\) a transition relation. A trace is a sequence \(s_0\xrightarrow{e_1}s_1\xrightarrow{e_2}\cdots\). A behavior model specifies which traces are possible or permitted. A sequence diagram selects some traces and their event ordering; a state machine constrains traces by state-dependent rules. A use case explains why certain traces matter to a stakeholder, but usually does not enumerate the complete trace set. This gives an intellectual test for model coherence: do the views disagree about which traces are legal?

### The acceptance event is not a single obvious thing

Northstar receives a `ReserveTrip` request. In one diagram, a message labeled `accepted` may mean that the transport layer received bytes. In another, it may mean that the server validated the request. In a third, it means the reservation is committed to durable storage and no additional customer can take the same capacity. These interpretations imply different allowed future traces. If the customer is promised a seat, only the third event may support that claim. The model must distinguish **received, validated, committed, and communicated** events rather than reusing one ambiguous “success” symbol.

A state-machine representation might allow `Requested → Validated → Reserved → Completed`, with exceptional paths to `Rejected` or `Cancelled`. But state names alone are insufficient. The transition from `Validated` to `Reserved` needs a guard such as `capacity_available AND route_permission_current`, and perhaps a postcondition establishing a unique reservation identifier. If route permissions may expire between validation and commit, the model must define whether the guard is re-evaluated or whether the operation is atomic with respect to that data.

### Concurrency introduces partial ordering

In distributed systems, there may be no globally agreed instantaneous order for all events. A passenger can cancel while the dispatcher assigns a vehicle. A payment callback may arrive after a timeout. A sequence diagram that draws events in a vertical line can accidentally imply serial execution where the implementation permits interleaving. The useful concept is a **happens-before** relation: some events are ordered by program or message causality, while others are concurrent. A design must specify whether competing commands commute, conflict, or require synchronization. Without that distinction, two local views may both appear correct while global capacity becomes inconsistent.

This is also why a behavioral model needs more than safety properties. “Never allocate the same seat twice” is a safety property: there is a finite counterexample trace if it fails. “Every accepted request eventually reaches a terminal state” is a liveness property: it requires assumptions about fair processing, network availability, and recovery. A model that prevents every duplicate by refusing all requests satisfies the first property but fails the mission. Assurance must consider both classes and their operational assumptions.

### Abstraction is a promise about what was omitted

A diagram may omit persistence, clocks, retries, or human interventions because they are irrelevant to a particular question. That omission is valid only if conclusions derived from the diagram do not depend on the omitted features. A simplified use case can teach the passenger's goal without representing a database transaction. It cannot by itself establish consistency under concurrent reservation attempts. A useful model explanation therefore states which observations it preserves and which it intentionally abstracts away.

One way to test consistency across views is to choose a contested scenario—two simultaneous requests for the last seat, followed by a message retry—and trace it through the use case, activity, sequence, and state-machine descriptions. The exercise is conceptual, not merely graphical: if the views authorize different final states, the engineering team has found a specification conflict. The point of MBSE is not to produce more pictures but to make such disagreements discoverable before they are embodied in code or hardware.

## Worked Northstar example

For a trip request, states are CREATED, ACCEPTED, ASSIGNED, CANCELLED and COMPLETED. ASSIGNED→COMPLETED requires pickup and drop-off evidence; CANCELLED→ASSIGNED is illegal without a new request identity. A sequence diagram of duplicate API messages demonstrates that a repeated ACCEPT event must not create another assignment.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### A behavioral proof obligation

Let the request state be one of `{CREATED, ACCEPTED, ASSIGNED, CANCELLED, COMPLETED}`. Define a transition function `δ(state,event)` that either returns a new state or rejects the event. A duplicate `ACCEPT` command should not allocate capacity twice. One test is to evaluate `δ(ACCEPTED, ACCEPT)` and confirm that no second resource reservation is made. Another is to try `δ(CANCELLED, ASSIGN)`; absent an explicit reopening protocol, the model should reject it.

When a sequence view shows a second successful assignment while the state machine forbids it, the correct response is a discrepancy, not two independently “correct” diagrams. Trace the conflict to the responsible requirement and owner.

## What can go wrong—and why

An activity diagram can describe processing order while accidentally allowing impossible state transitions; cross-view consistency must be checked.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 5: Behavior is a family of complementary projections](../labs/lab-05-behavior-modeling-use-cases-activities-action.md), you will: Draft a use case, a five-state transition table and two interaction traces for trip cancellation. Include a guard for “vehicle no longer eligible.” The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 5 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](04-requirements-modeling-relationship-semantics-.md) and leads toward [next chapter](06-structure-interfaces-ports-connections-and-th.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w05.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
