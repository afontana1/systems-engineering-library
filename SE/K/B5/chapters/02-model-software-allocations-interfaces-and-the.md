# Chapter 2 — Traceability connects implementation to justified choices

*Book V: Software Systems Engineering · Week 2 — Model software allocations, interfaces, and the digital thread*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 2](../labs/lab-02-model-software-allocations-interfaces-and-the.md) before attempting [the assessed Week 2 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w02.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **model software allocations, interfaces, and the digital thread** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Allocations assign requirements to software elements; interface definitions bind those elements to neighbors; a digital thread links evolving artifacts and evidence by identity and version. Do not conflate a trace link with causal proof. A digital thread is useful only if queries can detect what changes, what evidence expires and what is still undecided.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Traceability is a network of justified transformations

Software traceability is not a spreadsheet that proves completeness when every row has a link. It is a chain of claims about why one representation is an adequate realization of another. A stakeholder need becomes an allocated software obligation; that obligation constrains interfaces and state transitions; those constraints motivate implementation choices and verification scenarios. At each transformation, information may be lost or new assumptions introduced. A link without a rationale cannot expose that loss.

A useful trace model distinguishes **derived-from**, **allocated-to**, **implemented-by**, and **verified-by** instead of treating every edge as “related to.” It also records revision identity: a test that passed against an old interface cannot automatically support a changed one. Bidirectional queries matter because missing upstream justification and missing downstream evidence are different problems. Traceability improves change-impact analysis, but only if the relationships have semantics that make the impact query meaningful.

## Deeper theory: allocation transforms system obligations into software contracts

### Decomposition is valid only when the obligations compose

A system requirement such as “complete an emergency-stop request within 300 ms” cannot simply be assigned to the software service and marked addressed. The end-to-end delay includes sensing, communication, scheduling, processing, command propagation, and actuator response. A useful allocation decomposes the budget into terms such as `T_total = T_sensor + T_network + T_compute + T_actuator + T_margin`. Each term needs a defined measurement boundary and credible upper-bound or probabilistic interpretation. Without this agreement, subsystem teams may each comply locally while the composed system violates its obligation.

Not every requirement decomposes additively. An access-control requirement may need consistent enforcement across an API gateway, service layer, and database. A confidentiality property depends on end-to-end data handling, not an assigned encryption component alone. Allocation must therefore distinguish budgets that sum, invariants that must hold at every relevant boundary, and emergent outcomes that require integrated verification.

### Allocation is also placement of state and failure responsibility

When software functions are separated into services, decisions about state ownership become architecture decisions. Two modules that both update the canonical reservation count may create races and conflicting views of capacity. Assigning a single writer can simplify consistency but creates a bottleneck and a possible single point of failure. Replication can improve availability while introducing synchronization delay and conflict-resolution policies. The correct choice depends on the required consistency model and what incorrect state would cost.

Consider a network partition: the campus shuttle may remain physically able to operate while disconnected from central dispatch. Should the local controller accept new bookings, continue previously authorized trips, or enter a safe standby mode? The answer depends on service priority and hazard constraints. The software allocation model should identify which components can make each decision and what assumptions they need about communication freshness.

### Traceability must preserve rationale, not only links

A requirement-to-component link establishes an intended responsibility, but not why a particular placement was chosen. A richer record includes interface constraints, alternative placements considered, safety or latency budgets, architectural assumptions, and verification responsibilities. When a component changes, this rationale helps distinguish harmless refactoring from a change that reopens a system trade. A complete-looking matrix may conceal a missing allocation decision if all rows simply link to a single generic software subsystem.

A model of traceability can be analyzed as a directed graph. Requirements with no implementing path are coverage gaps; components with no justified need may indicate accidental complexity; heavily connected nodes reveal integration concentrations and potential change hotspots. These are screening indicators, not proofs of correctness. Semantic mismatches—different units, meanings, timing rules, or failure expectations—require engineering inspection and tests.

### Budget uncertainty travels across interfaces

Suppose component latencies are measured under independent low-load tests. Summing their averages understates the chance of an unacceptable tail event if all components slow under peak demand. A shared network queue or CPU resource introduces dependence. For assurance, the allocation must specify whether each delay bound is deterministic, a percentile under a workload distribution, or an observed maximum under test. Percentiles of separate components cannot generally be summed to obtain the same percentile for the end-to-end service without assumptions about dependence.

Software allocation is consequently not clerical trace maintenance. It is the disciplined transformation of stakeholder obligations into component responsibilities and compositional assumptions that can be challenged through architecture analysis and integrated evidence.

## Worked Northstar example

Requirement R-12 constrains acknowledgement to three seconds, service API ACK implements the interface, telemetry measurement M-12 logs timings, and verification run E-12 checks the threshold. If the service timeout changes from two to five seconds, an automated impact report should flag both R-12 and E-12 for review.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Code commit hashes without semantic links to requirements are provenance, not complete traceability.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 2: Traceability connects implementation to justified choices](../labs/lab-02-model-software-allocations-interfaces-and-the.md), you will: Build a five-layer digital-thread table and run a change-impact analysis for an interface-timeout change. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 2 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](01-define-the-software-systems-engineering-role-.md) and leads toward [next chapter](03-interpret-and-critique-the-system-model-for-s.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w02.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: allocation, interfaces and versioned traceability

### Trace a requirement through a specific interface

Consider **SWS-03**, which prohibits overlapping accepted reservations for the same vehicle and slot. Its responsible element is `allocation-store`. The [IF-02 contract](../case/interfaces.csv) specifies `CommitAssignment`, a 160 ms timeout, and *reconciliation by token* after an uncertain acknowledgment. This matters because a client-side timeout does **not** mean the transaction failed. The server may have committed and lost the reply. Retrying a new reservation blindly can create a conflicting claim even when the underlying database is healthy.

A defensible allocation trace runs from the stakeholder's no-double-booking need to SWS-03, to the allocation-store owner, to IF-02, to the atomic uniqueness invariant, to transaction tests, and finally to evidence bound to a particular revision. An interface ID is not enough; the trace also needs the *reason* the transaction property is necessary. A diagram that draws an arrow from API to database does not express commitment or exactly-once semantics.

### Prove the budget is explicit

The reservation path contains an illustrative fixed contribution of 70 ms network, 45 ms authentication, and 55 ms commit: a total of 170 ms **before** the variable dispatch wait. If the end-to-end requirement is 500 ms, the variable part has at most 330 ms in the nominal decomposition:

\[B_{\mathrm{variable}}=500-(70+45+55)=330\text{ ms}.\]

A component owner cannot promise “fast enough” independently; budget assumptions must be consistent across the trace. Moreover, simply summing reported per-stage 95th percentiles is generally invalid because stages can be correlated. We use fixed amounts here specifically to expose the mechanism; the real test must measure *end-to-end* requests at a declared load.

### Version edges, not just nodes

Evidence `BLD-50` in [the model baseline](../case/model-baseline.json) is marked `PASS`, yet refers to NS-SW5.0. The software under consideration is NS-SW5.1. Evidence currency depends on the identity of the tested artifact, relevant environment and the change-impact argument. Merely changing the label on a spreadsheet would be invalid. In a controlled digital thread, a revision produces an impact set: changed contracts, affected components, tests to repeat, and claims whose evidence no longer applies.

**Exercise.** A developer increases the IF-02 timeout from 160 to 240 ms but leaves the user-visible 500 ms requirement unchanged. How should reviewers respond? **Answer.** Reconsider the path budget and retry behavior. The proposed change could consume 80 ms of margin and prolong uncertainty after partial failure; it is not an isolated configuration tweak. Re-run integration, timeout, duplicate-attempt and tail-latency tests.

**Reference records:** [Requirements](../case/requirements.csv), [interfaces](../case/interfaces.csv), and [evidence](../case/evidence-register.csv).
