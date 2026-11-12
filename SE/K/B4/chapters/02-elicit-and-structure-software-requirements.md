# Chapter 2 — Software requirements need multiple kinds of precision

*Book IV: Object-Oriented Analysis and Design · Week 2 — Elicit and structure software requirements*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 2](../labs/lab-02-elicit-and-structure-software-requirements.md) before attempting [the assessed Week 2 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w02.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **elicit and structure software requirements** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Functional requirements specify observable capabilities; quality constraints specify performance, availability, security and other measures. Business rules, data rules and interface commitments should not collapse into an undifferentiated wish list. Clarify external events, actors, state changes and exception handling before inferring class design.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Software requirements span observables and internal contracts

A system requirement such as “reserve a vehicle” is incomplete until the parties agree on observable success, legal rejection, concurrency, timing, and error semantics. Requirements that describe only the happy path fail to constrain the cases in which software systems most often break. An externally visible contract might state that each accepted booking has a unique reservation ID and that repeated submission of the same request key cannot create a second active booking.

This does not dictate a database or framework. It defines an invariant that many architectures could implement. Keep **what must be observable** distinct from **how the implementation realizes it**. Nonfunctional qualities also need operational contexts: a latency target under nominal demand is different from one under degraded connectivity. Translating stakeholder language into precise contracts is a form of analysis because each newly stated exception or condition exposes a choice that users and system owners may not yet have made.

## Worked Northstar example

“Passengers can cancel” is incomplete. Specify whether cancellation is permitted before boarding, the resulting reservation status, vehicle release behavior, and response under duplicated cancellation commands. Distinguish a rule from the chosen class that will enforce it.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

An apparently atomic user story can hide several independent obligations and contradictory edge conditions.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 2: Software requirements need multiple kinds of precision](../labs/lab-02-elicit-and-structure-software-requirements.md), you will: Turn eight raw stakeholder statements into testable functional rules, constraints, data definitions and open questions. Build a small scenario acceptance table. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 2 deliverable and grading rubric.


## Deeper theory: software requirements as contracts over observable traces

### Different requirement types demand different logic

A functional software requirement specifies an observable relation between inputs, states, and outcomes. A safety requirement restricts unacceptable traces; a liveness requirement demands that something good eventually occurs; a performance requirement bounds time or resource use under defined workload. Treating all of these as “the system shall” sentences without semantic distinction makes them difficult to verify. “Never unlock a moving vehicle” is a safety invariant. “Eventually acknowledge an accepted dispatch request” is a liveness claim and needs assumptions about communication availability and recovery. “Acknowledge within two seconds for 99% of requests” is a statistical service claim with a defined population and measurement boundary.

Temporal logic offers a precise vocabulary. A simplified invariant can be written `G(moving -> not door_unlocked)`, where `G` means “globally, at every modeled time.” A progress claim might be `G(request_accepted -> F(response_sent))`, where `F` means “at some future time.” The second assertion is false if a request can remain pending forever; to make it credible, define fairness, timeout, cancellation, and failure behaviors. Formal notation does not resolve stakeholder ambiguity on its own; it exposes the ambiguity so that engineers can decide its intended semantics.

### Preconditions, postconditions, and error behavior are one contract

An API requirement should identify valid inputs, authorized callers, persistent-state assumptions, return values, side effects, and failure responses. For a ride booking call, “create a booking” is incomplete if duplicate retries can create two active bookings. An idempotency key changes the contract from “create a new record for each call” to “retries of the same logical request have one committed effect within a specified retention window.” The retention window and collision behavior matter. This is a requirement about state evolution across partial failures, not merely an implementation preference.

Requirements need refinement relationships. A high-level statement about safe rider pickup may refine into constraints on door state, localization confidence, vehicle speed, user notifications, and emergency stop. Refinement should preserve the external obligation while partitioning implementable responsibilities. If a child requirement assumes flawless network access but the parent promise applies during network loss, decomposition has introduced an undocumented restriction. A good review explicitly compares the assumed operating domains of parent and child claims.

### Testability depends on a measurement model

To verify a two-second response requirement, define the triggering event, completion event, clocks, population, excluded conditions, confidence target, and treatment of timeouts. Suppose 995 of 1,000 requests complete within two seconds. The observed proportion is 99.5%, but it is not proof that the long-run proportion is at least 99% with arbitrary confidence. Sampling uncertainty, temporal correlation, load mix, and test-system measurement error all matter. An adequate acceptance plan specifies a decision rule and how much evidence is required before results are observed.

The governing distinction is between *specification correctness* and *implementation correctness*. Code can satisfy an ambiguous or incomplete specification while failing the real mission. Software requirement engineering must therefore connect trace semantics to operational scenarios and stakeholder effects. A more formal requirement is useful only when it preserves the needed behavior rather than making a mistaken assumption more precise.

## Continuity

This chapter builds from [previous chapter](01-establish-the-ooad-problem-scope-and-modeling.md) and leads toward [next chapter](03-capture-functional-requirements-with-use-case.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w02.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: requirements as enforceable software contracts

### 2.1 Write an observable behavior, not an implementation preference

A software requirement should identify a trigger, intended response, observable outcome, acceptance rule, and boundary conditions. Compare “use a reservation database” with `SW-03`: *for two submissions carrying an identical request token and identical immutable payload, return the same reservation identifier without creating another assignment*. The second statement supports a repeatable test while leaving technology choices open.

The [controlled requirement set](../case/model-baseline.json) includes seven synthetic requirements. They cover durable reservation identity, unique active assignment, retry idempotency, cancellation, accessibility, telemetry freshness, and audit provenance. A traceability relationship is meaningful only when a specific test can distinguish a compliant implementation from a noncompliant one.

### 2.2 Specify failure and boundary cases

For a request \(r=(k,p)\), with token \(k\) and immutable payload \(p\), let \(F(k,p)\) denote its result. Idempotency requires

\[
\operatorname{id}(F_{t_1}(k,p))=\operatorname{id}(F_{t_2}(k,p))\quad (t_2>t_1).
\]

Operationally, a repeated submission should return the first durable reservation ID. A different payload submitted under the same token should fail explicitly, rather than silently borrowing the old reservation. This is not the same as guaranteeing exactly-once processing over a network; it is a bounded application contract with durable deduplication.

| Requirement | Positive acceptance scenario | Adversarial scenario |
|---|---|---|
| SW-03 | Retry same token and payload: identical ID | Same token with changed vehicle: reject |
| SW-04 | Cancel active reservation: slot becomes available | Cancel twice: do not emit duplicate state change |
| SW-05 | Accessible rider: eligible vehicle | Non-accessible vehicle: reject before commit |
| SW-06 | Telemetry age 6 s: eligible | Age 22 s: reject at 15-s freshness limit |

Distinguish the 15-second **maximum acceptable observation age** from a 15-second sampling period. A nominal update frequency does not guarantee an observation is current at decision time. The effective age is decision timestamp minus observation timestamp, ideally measured using a common trusted time basis and taking network delay into account.

### 2.3 Quantify a timing budget without overclaiming

The illustrative command path includes authentication (120 ms), policy decision (80 ms), and transactional commit plus audit event (150 ms). Its modeled serial latency is

\[
L=120+80+150=350\ \mathrm{ms};\qquad M=500-L=150\ \mathrm{ms}.
\]

A 150-ms arithmetic margin does **not** prove a 500-ms performance requirement. Queueing, network retransmission, tail latencies, clock measurement, load, and dependency correlations remain unmeasured. A performance test should specify the percentile, workload, observation method, and configuration. If the requirement is for the 99th percentile, comparing only average component times is invalid.

**Solved checkpoint.** A review report links `SW-06` to a test marked PASS at revision 1. The requirement is now revision 2. The correct disposition is *stale evidence*, even if the result is plausible. Rerun the relevant acceptance test against the new requirement interpretation and the declared baseline.

**Exercise.** Rewrite “the interface shall be fast” as a measurable requirement, naming the load, event origin, event endpoint, tail percentile, and maximum time. Do not infer those values from the 350-ms illustrative budget; assign and justify them as design assumptions.
