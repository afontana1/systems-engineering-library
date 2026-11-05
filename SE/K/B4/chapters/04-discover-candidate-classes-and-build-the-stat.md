# Chapter 4 — Class discovery turns language into relationships

*Book IV: Object-Oriented Analysis and Design · Week 4 — Discover candidate classes and build the static analysis model*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 4](../labs/lab-04-discover-candidate-classes-and-build-the-stat.md) before attempting [the assessed Week 4 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w04.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **discover candidate classes and build the static analysis model** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Association represents a semantic link between objects; composition implies strong lifecycle ownership; generalization requires genuine substitutability. Attributes describe essential state; operations should be attached where information and responsibility meet. A UML class diagram is not an entity-relationship diagram with different glyphs.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Class discovery is the progressive refinement of candidate entities into identities, responsibilities, associations and invariants.

### Distinguishing related ideas

Noun extraction is a starting heuristic, not proof that every noun deserves a class; some nouns denote values, events, roles or transient calculations.

### Interpretation and boundary conditions

A 'VehicleAvailability' object may be a derived view of schedule state rather than independent mutable truth; modeling that distinction prevents divergence.

## Deeper theory: object discovery as a theory of identity and responsibility

Turning requirements prose into classes seems straightforward until one asks what a class represents. A noun in a stakeholder story may be a persistent domain entity, a transient value, a role, a process, a user-interface label, or merely a linguistic convenience. An object-oriented model should not be a mechanical noun extractor. It should explain which entities retain identity across change, which invariants must remain true, and which responsibilities belong together so that those invariants can be maintained.

The conceptual distinction between an **entity** and a **value** is especially powerful. A reservation has an identity even if its requested time changes; two reservations with equal times are still distinct commitments. A duration of 15 minutes is a value and need not carry a unique identity. Confusing the two leads to brittle designs: an address stored as a mutable entity may acquire unnecessary lifecycle complexity, while a reservation represented as an anonymous value may lose its audit history. Identity should be justified by the problem domain, not by the convenience of a programming-language class declaration.

### Invariants reveal natural responsibility boundaries

An invariant is a condition intended to remain true at relevant system boundaries. For a shuttle capacity model, \(0\leq \text{reservedSeats}(v,t)\leq \text{capacity}(v)\) is one possible invariant, although accessibility configuration and operational restrictions may make the capacity state-dependent. The relevant design question is: **which component has sufficient information and authority to preserve this invariant?** If three services can independently change seat allocations without a shared concurrency protocol, no single service can enforce the guarantee. Responsibilities should align with the invariants and consistency boundaries they must protect.

A domain model can therefore be organized around **aggregates**: clusters of related objects with rules maintained at a defined transaction boundary. This is not permission to put every function into one enormous class. It is a reminder that splitting an invariant across asynchronous actors creates an explicit distributed-consistency problem. A `Reservation` object may own lifecycle transitions; a `VehicleCapacity` aggregate may own allocation decisions; an event log may preserve the facts needed for audit. Their boundaries depend on what must be changed atomically and what may be eventually consistent.

### Association, composition, and dependency express different claims

A UML association states that instances can be related; multiplicity constrains allowable cardinalities. Composition asserts a stronger whole-part lifetime relation. A dependency indicates that one classifier's specification or implementation may be affected by another, but it need not imply stored object references. These relations cannot be selected merely for visual neatness. For example, a vehicle is assigned to a trip but does not ordinarily cease to exist when the trip is canceled; modeling the vehicle as a compositional part of a trip would misrepresent ownership and lifecycle. Likewise, an operator role may be linked to several vehicles without being an intrinsic part of any vehicle.

Multiplicity constraints also require time interpretation. “One reservation has exactly one vehicle” may be false while a request is pending, true after successful dispatch, and false again after cancellation. A static class diagram can state a structural relation, but a state machine or constraint language may be needed to express the conditional multiplicity. A model that hides time inside supposedly timeless associations invites contradictions later in design.

### Coupling measures consequences of change

Good classes are not necessarily the smallest possible classes. They are units whose internal changes usually preserve external contracts and whose responsibilities form a coherent explanation. Excessive coupling means a change to one concept forces unrelated concepts to change because the design has leaked details across boundaries. Excessive fragmentation can be equally harmful: a business rule is scattered across many thin objects and no object can explain or enforce it. High cohesion is best understood causally—features change together because they serve the same responsibility—rather than as a numerical target.

A useful counterexample is a single `ShuttleManager` class that manages bookings, charging, accessibility, personnel and route permissions. It can be coded quickly and may initially pass all tests. Yet it combines state with different owners, rates of change, and assurance concerns. Conversely, creating separate objects for every single verb in a use case can produce a network of calls without clear invariant ownership. Domain-driven boundaries lie between these extremes, guided by responsibility, identity, state, and the costs of enforcing consistency.

The purpose of class discovery is thus to construct a **conceptual explanation of the domain that remains meaningful as the software evolves**. Programming classes are one possible implementation of that explanation, not the explanation itself.

## Worked Northstar example

A Rider creates many Requests; each active Request may have zero or one Assignment; a Vehicle can be assigned many trips over time but only one overlapping active movement under this teaching rule. Model the multiplicity and time qualifier instead of accidentally asserting “one vehicle, one trip ever.”

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Choosing composition merely because one object references another can prohibit legitimate independent lifetimes.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 4: Class discovery turns language into relationships](../labs/lab-04-discover-candidate-classes-and-build-the-stat.md), you will: Construct a seven-class analysis model with at least four associations, multiplicities and two written invariants. Remove one unnecessary class. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 4 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](03-capture-functional-requirements-with-use-case.md) and leads toward [next chapter](05-analyze-dynamic-behavior-and-discover-collabo.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w04.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
