# Chapter 8 — A design sequence should be realizable

*Book IV: Object-Oriented Analysis and Design · Week 8 — Realize use cases with dynamic design models*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 8](../labs/lab-08-realize-use-cases-with-dynamic-design-models.md) before attempting [the assessed Week 8 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w08.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **realize use cases with dynamic design models** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Interaction design must identify the interfaces and failure semantics required for a use case. Synchronous calls, asynchronous messages and stored events have different ordering and error consequences. Design contracts should describe timeouts, retries and durable-state guarantees, not simply restate the analysis narrative.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### A plausible design must admit a realizable execution order

Object collaborations become engineering designs only when their responsibilities can be executed without contradictions about ownership, state, and ordering. Consider a route planner that needs live vehicle availability, while the availability service waits for a route assignment before marking a vehicle as available. The dependency cycle can deadlock even when each class is individually coherent. A design review should therefore ask whether collaboration can make progress under realistic event orders and partial failures.

Coupling is not automatically bad: two objects may need close coordination because their invariant truly spans both. The design question is whether that coordination is explicit, enforceable, and affordable. Hiding an invariant behind many asynchronous messages can create an inconsistent interval in which no component sees the whole truth. Sometimes the correct remedy is to move responsibility into a single aggregate; sometimes it is to define an eventual-consistency policy. Neither choice is justified by a pattern name alone.

## Worked Northstar example

A ReserveCapacity command receives a request identifier and returns HELD or REJECTED. Between writing a reservation and publishing an event, the service may crash. A durable outbox can preserve the event for later delivery; consumers still need deduplication because delivery may repeat.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Treating event publication as exactly-once without a precise end-to-end definition is a classic distributed design mistake.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 8: A design sequence should be realizable](../labs/lab-08-realize-use-cases-with-dynamic-design-models.md), you will: Construct a design-level sequence for two concurrent bookings and crash recovery. Specify transaction boundary and the location of retry state. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 8 deliverable and grading rubric.


## Graduate depth: interaction design as an executable contract
### A sequence diagram implies a partial ordering

Dynamic object design is more than arranging messages from top to bottom. A sequence diagram specifies a set of causal ordering constraints among events, frequently leaving some operations concurrent. If message `m1` must precede `m2`, the design requires a **happens-before** relationship; messages on separate lifelines may lack a fixed order unless synchronization is explicit. Assuming the drawn order is a universally enforced runtime order can conceal race conditions in asynchronous systems. UML notation must be interpreted alongside its execution semantics and deployment assumptions.

A use case defines an observable success or refusal outcome, while a design realization distributes responsibility across collaborators. The realization is sound only if every admissible interaction preserves preconditions, invariants, and the use case's externally observable contract. For a simplified dispatch operation, the sequence may read eligibility, reserve capacity, commit assignment, and notify the rider. What happens if the reservation succeeds but notification fails? What happens if eligibility changes between reading and committing? Those questions cannot be resolved by merely adding another arrow.

### Atomicity and compensation change the design

If all steps run in one transactional resource, an atomic transaction can make the assignment visible only after its invariants are satisfied. Across distributed services, one global atomic transaction may be unavailable or undesirable. A saga-like process instead records intermediate states and compensating actions: reserve, confirm, or release. Compensation is not always an inverse operation—a rider may already have seen the initial notification, and a refunded payment may have fees or regulatory consequences. The resulting state model must include partial completion, retries, idempotency, and explicit expiry.

A useful correctness statement is a temporal property. For example, `G(confirmed → previously_authorized)` informally means a confirmed assignment always rests on appropriate prior authorization; the exact formalization requires a chosen temporal logic and a model of authorization validity. A liveness property such as “every accepted request eventually receives an outcome” must include fairness and external-service assumptions. In a system with permanent network failure, unqualified eventual completion may be impossible. Distinguishing safety properties (bad things never happen) from liveness properties (good things eventually happen) reveals why both state and interaction views are necessary.

### Design tests should challenge ordering assumptions

Walk through at least three traces: nominal completion, interrupted completion, and concurrent conflict. In the Northstar example, two dispatch workers may attempt to reserve the final available vehicle. A design that performs `read available; write assignment` without coordination is vulnerable to double allocation. The architecture may need a compare-and-swap, database constraint, lease, or serialized decision service. The right mechanism depends on latency, availability, deployment boundaries, and the criticality of the invariant.

An interaction design is credible when implementers can identify who owns each state transition, which operations are atomic, which messages can be repeated or lost, how timeouts are handled, and how failures become observable. Unit tests of individual classes cannot prove that distributed traces are correct. The design should enable integration, fault-injection, and scenario-based tests linked back to the use case and system requirements. The fundamental idea is refinement: each added design detail should preserve the externally promised behavior while making hidden failure modes manageable.

## Continuity

This chapter builds from [previous chapter](07-assign-responsibilities-and-build-the-static-.md) and leads toward [next chapter](09-apply-design-patterns-with-restraint.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w08.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
