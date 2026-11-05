# Chapter 6 — State machines are executable constraints on lifecycles

*Book IV: Object-Oriented Analysis and Design · Week 6 — Model state-dependent behavior and conduct the Analysis Model Review*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 6](../labs/lab-06-model-state-dependent-behavior-and-conduct-th.md) before attempting [the assessed Week 6 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w06.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **model state-dependent behavior and conduct the analysis model review** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

State-dependent behavior should be described as a finite set of states and legal transitions triggered by events and guarded by conditions. A method named cancel() does not by itself define which states permit cancellation. Hierarchical states reduce duplication but can hide precedence if guards are ambiguous. Treat state invariants and unreachable states as testable properties.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

A state machine defines which events are legal in which states and therefore makes temporal business rules inspectable.

### Distinguishing related ideas

State and event are not synonyms: 'reserved' is persistent state, while 'reserve requested' is a trigger whose outcome depends on guards and current state.

### Interpretation and boundary conditions

Illegal transitions should be refused without silently mutating the aggregate; concurrency can expose violations not seen in a single-threaded diagram.

## Deeper theory: state models define the legal histories of a system

### A state is an abstraction with behavioral consequences

A state machine partitions a potentially unbounded history into situations for which future behavior can be described by the same rules. In a simple labeled transition system, states form a set `S`, events a set `E`, and a transition relation `T ⊆ S × E × S` describes allowed changes. Guards restrict when a transition is enabled; effects change data or issue commands. A state such as `BoardingAuthorized` must have a precise meaning: is it a durable permission recorded by the service, a command sent to the vehicle, or an observed physical door state? Conflating these creates a model that appears internally consistent but cannot be implemented or tested reliably.

A guard is not the same as an action. If a transition requires `vehicleStopped ∧ zoneClear`, the model needs to say which observations support those predicates and how old they may be. Reading the values and issuing an authorization are not necessarily atomic operations; the vehicle can begin moving in between. This time-of-check/time-of-use gap is an architectural problem, not a syntax error. Solutions may involve a local interlock, a token bound to a fresh state version, or a control protocol that revalidates the safety condition at actuation.

### Concurrency makes event order part of correctness

An object can receive `ConfirmBoarding` and `CancelTrip` from different sources. If their order is unspecified, two valid message sequences can produce incompatible outcomes unless conflict semantics are explicit. Orthogonal state regions can model concurrent aspects such as communications mode and vehicle motion, but the Cartesian combination introduces combinations that may be forbidden. Hierarchical states reduce repetitive transitions by sharing parent behavior; they do not eliminate the need to analyze cross-region constraints.

For a shuttle trip, define a safety property: *boarding authorization is never effective while the vehicle is moving*. This is an invariant over reachable states or traces. A liveness property might say: *every accepted trip eventually reaches completion or an explicitly reported terminal exception*, subject to assumptions about continued service and fair scheduling. Safety rules out bad histories; liveness rules out indefinite nonprogress. A machine can satisfy every local transition guard yet violate liveness by cycling forever between `Retrying` and `Waiting`.

### Temporal claims need an execution model

A diagram that shows a `Timeout` event without a clock model has left open whether timeout is measured from request arrival, assignment issuance, or the most recent retry. Distributed systems also introduce clock skew, duplicate events, and messages received after an earlier request has been superseded. Version identifiers, monotonic clocks, and explicit expiry conditions may be needed before a state machine's apparent safety claim can survive implementation.

Verification asks whether all relevant traces of the modeled system obey the constraints, not merely whether a few illustrative scenarios look plausible. State-space exploration can uncover deadlocks and unexpected interleavings, but only relative to modeled events, finite bounds, and environmental assumptions. Abstraction can hide a race as easily as it can enable analysis. A useful Northstar state model therefore records the environment's possible actions, the authority behind commands, the atomicity assumptions, and the abnormal histories that matter for passenger safety. A visually tidy lifecycle is not evidence that these semantics are resolved.

## Worked Northstar example

Reservation has NEW, HELD, CONFIRMED, CANCELLED and COMPLETED. Confirming a CANCELLED reservation is forbidden. Running the same confirm event twice should have no additional resource effect; this is idempotence, not a second transition.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### State transition test table

| Current | Event | Guard | Result |
|---|---|---|---|
| NEW | reserve | capacity available | HELD |
| HELD | confirm | hold valid | CONFIRMED |
| HELD | timeout | no confirmation | CANCELLED |
| CANCELLED | confirm | any | REJECTED, state unchanged |
| CONFIRMED | complete | trip actually finished | COMPLETED |
| CONFIRMED | confirm | duplicate key | CONFIRMED, no additional effect |

Each transition must preserve the invariant “one active booking for a request key.” A state machine built only with happy-path arrows is under-specified. Also test that `complete` cannot be applied to HELD and that a retry after a timeout cannot reserve a second vehicle.

## What can go wrong—and why

A “state” invented for every minor flag produces combinatorial explosion; too few states hide illegal behavior.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 6: State machines are executable constraints on lifecycles](../labs/lab-06-model-state-dependent-behavior-and-conduct-th.md), you will: Build a transition table for six events and test it with adversarial event orderings. Produce two counterexample traces. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 6 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](05-analyze-dynamic-behavior-and-discover-collabo.md) and leads toward [next chapter](07-assign-responsibilities-and-build-the-static-.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w06.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Advanced worked practice

- [Deep workshop — State Machines, Invariants, and Idempotent Commands](../practice/state.md)
- [Corresponding independent laboratory](../practice/lab-state.md)
- [Interactive workbench](../practice/WORKBENCH.html)
