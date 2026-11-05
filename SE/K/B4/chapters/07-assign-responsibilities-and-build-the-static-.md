# Chapter 7 — Design is the distribution of responsibility

*Book IV: Object-Oriented Analysis and Design · Week 7 — Assign responsibilities and build the static design model*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 7](../labs/lab-07-assign-responsibilities-and-build-the-static-.md) before attempting [the assessed Week 7 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w07.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **assign responsibilities and build the static design model** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Move from analysis objects to interfaces, services and collaborators with controlled dependencies. Low coupling is not no coupling: communication is necessary, but every dependency should have a reason. High cohesion means a class has a focused reason to change. Distinguish domain behavior from application orchestration and infrastructure adapters.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Assigning responsibilities shapes coupling and the ability to preserve invariants as requirements change.

### Distinguishing related ideas

An anemic model that lets every service update reservation state makes consistency a distributed convention rather than a locally enforced contract.

### Interpretation and boundary conditions

Put a rule near the owner of the authoritative state, while keeping cross-boundary collaboration explicit and testable.

## Worked Northstar example

Reservation enforces its own lifecycle invariant; BookingService coordinates a booking; CapacityGateway adapts external capacity information. If BookingService owns every rule, a second entry point can bypass the invariant. If Reservation directly calls a database driver, the domain becomes bound to infrastructure.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Too many tiny interfaces can obscure responsibility just as a single god object does.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 7: Design is the distribution of responsibility](../labs/lab-07-assign-responsibilities-and-build-the-static-.md), you will: Refactor a 12-method Dispatcher class into a domain aggregate, application service and two ports. Draw dependencies and defend one rejected alternative. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 7 deliverable and grading rubric.


## Deeper theory: responsibility allocation, coupling, and evolvable design

### Assign behavior to owners that can preserve invariants

Object-oriented design allocates responsibilities to objects, services, and modules. The central question is not which class name resembles a noun; it is where a rule can be enforced coherently in the presence of concurrent updates and failure. For example, the invariant “no vehicle may be committed to two overlapping assignments” should be owned by a component with access to the authoritative assignment state and an appropriate concurrency-control mechanism. If two unrelated services each maintain their own notion of availability, neither can enforce the invariant alone. A class diagram can look clean while the real consistency boundary is undefined.

Information hiding reduces the number of components that must change when an implementation decision changes. A module should expose stable contracts while concealing volatile policy or representation. However, excessive abstraction can create extra indirection and obscure latency, ownership, or failure behavior. The practical test is whether the proposed boundary isolates an anticipated source of change without breaking observable behavior. This connects classic software modularity to systems engineering change-impact analysis.

### Coupling is multidimensional

Two components can be loosely coupled in code but tightly coupled in deployment or data semantics. Separate microservices sharing one database schema are organizationally separate but can be technically coupled through migrations, transaction guarantees, and operational load. Likewise, an asynchronous queue removes direct invocation coupling but introduces message ordering, duplication, replay, and monitoring obligations. Architecture review should examine at least compile-time, runtime, data, temporal, security, and organizational dependencies. Reducing one form may increase another.

A useful change-propagation model treats components as vertices and dependency relations as edges. If component A depends on the exact internal structure of B, a B change may force A to change. The expected rework burden depends on the probability of change, the number and nature of dependencies, and the cost of verification after each change. Minimizing raw edge count is not always optimal: a shared, stable interface standard can be less risky than multiple supposedly independent ad hoc translators. Dependency *semantics* matter more than diagram density.

### Concurrency turns ownership into a correctness claim

Suppose two dispatch threads read one remaining available vehicle and both issue assignments. Even if each method is locally correct, their interleaving violates the system invariant. The solution may involve serialized transactions, atomic compare-and-swap, optimistic version checks, or a single authoritative scheduler. Each mechanism has assumptions about failure, contention, persistence, and recovery. A locking design that works on one process may fail when scaled to multiple processes. The architectural contract must state what consistency is promised, not only where the method is implemented.

For a Northstar design review, choose a critical invariant and walk through at least one concurrent or failure trace. Identify the state owner, who may mutate it, which observations are stale, and how an interrupted operation is retried or compensated. This reasoning can expose design flaws that normal happy-path class and sequence diagrams miss. Responsibility allocation remains a hypothesis until its contracts are challenged against realistic interleavings and operating conditions.

## Continuity

This chapter builds from [previous chapter](06-model-state-dependent-behavior-and-conduct-th.md) and leads toward [next chapter](08-realize-use-cases-with-dynamic-design-models.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w07.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
