# Chapter 5 — Iteration must still produce system evidence

*Book V: Software Systems Engineering · Week 5 — Integrate agile product engineering with systems evidence*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 5](../labs/lab-05-integrate-agile-product-engineering-with-syst.md) before attempting [the assessed Week 5 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w05.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **integrate agile product engineering with systems evidence** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Agile work delivers increments; systems assurance needs controlled requirements, configurations and independently reviewable evidence. These are not mutually exclusive. Define a done criterion that includes risk-appropriate tests, interface contracts, provenance, monitoring and change impact. Use small batches to detect contradictions early while preserving a continuous release story.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Iteration shortens learning only when evidence is preserved

An iterative team can deliver features rapidly while accumulating uncertainty about the system as a whole. A short development cycle is useful because it reduces the delay between a hypothesis, an implementation, and a meaningful observation. If the increment is not evaluated against operational quality attributes and system constraints, however, the team is merely producing artifacts more frequently.

For safety-related software, incremental assurance requires deliberate test selection, configuration control, and explicit treatment of unresolved hazards. Technical debt is not merely untidy code; it is a growing mismatch between the system's assumed contracts and its actual structure or behavior. Continuous integration should therefore preserve an evidence trail showing which requirements, interfaces, dependencies, and tests apply to each build. Speed of iteration and rigor of evidence are not opposites, but rigor must be engineered into the iteration rather than postponed to a mythical final integration phase.

## Deeper theory: iteration and assurance as complementary control loops

Agile iteration is often described as the opposite of formal systems engineering, but that contrast confuses the cadence of producing changes with the obligation to demonstrate that those changes are acceptable. Iteration answers how frequently the team learns and revises; assurance answers what evidence is needed before a changed system is relied on. An engineering program needs both a **delivery loop** and an **evidence loop**. The loops can move at different rates: software may change daily while a physical hazard-control claim requires weeks of testing under controlled conditions.

A software increment is not automatically a useful increment at the system level. A new route-optimization feature may be internally complete but depend on an unverified vehicle interface, an outdated accessibility policy or a dispatcher procedure that has not been trained. The system-level value of the increment arises only when its assumptions are satisfied. This motivates an **integration-ready definition of done** that includes interface compatibility, configuration, relevant verification, observed failure behavior, and a clear statement of what is not yet supported.

### The economics of small batches is conditional

Smaller work batches can reduce the time between discovering a problem and responding to it. In a simple flow system, Little's Law relates average work in process \(L\), throughput \(\lambda\), and mean flow time \(W\): \(L=\lambda W\), assuming stable conditions and consistent boundaries. Reducing WIP can improve flow time when throughput is maintained. But this identity does not prove that arbitrarily small batches are optimal. Physical test setup, certification overhead, shared specialists, and integration equipment create fixed costs. Excessively small batches can increase context switching or leave crucial end-to-end behaviors untested.

The more useful principle is to choose batch sizes that expose uncertainty without creating needless integration overhead. A vehicle-control team may integrate software frequently into a simulated environment while performing representative hardware-in-the-loop qualification less frequently. The two cadences should be connected by configuration traceability so that evidence collected at one level can be interpreted at another.

### Continuous testing is not continuous proof

Automated tests provide repeatable observations about the tested configuration, inputs and environment. Passing them does not establish the absence of failures outside that scope. A unit test of a braking command validator cannot on its own establish safe stopping distance under a slippery road condition. Conversely, delaying all testing to a final acceptance campaign hides inexpensive defects until they interact with hardware, operators and interfaces.

A layered evidence strategy uses fast tests for local invariants, integration tests for contracts, representative simulation for scenarios, and physical or operational tests where model fidelity is insufficient. The layers have different error models and different kinds of relevance. A static analysis warning, a model-checking counterexample, and a physical test observation do not carry equivalent evidence simply because they are all recorded in a dashboard.

### Architectural changeability differs from organizational willingness

An architecture can have well-defined interfaces and still be difficult to change because the authority to update those interfaces is fragmented among suppliers, safety teams, and operations. Conversely, a highly responsive team may produce rapid local changes in a tightly coupled system that become expensive to integrate. Agility is an **emergent property of architecture, governance, capability and evidence**, not just sprint frequency.

A revealing example is a dispatch improvement that changes request timeout behavior from ten seconds to three. The service team can implement it in one iteration, but the mobile application, operator procedures, message retry policies and monitoring alarms may assume ten seconds. Shortening the timeout could multiply retries, causing additional queueing and eventually worse availability. A fast deployment can therefore create a slower and less dependable system. The proper systems-engineering response is to model the contract impact and test the revised end-to-end behavior, not simply to demand longer sprints or more approvals.

### Assurance debt accumulates differently from code debt

Code debt describes design compromises that raise future implementation costs. **Assurance debt** describes a widening gap between the current configuration and the evidence that supports claims about it. If the software changes but safety analyses, interface records and operational procedures do not, the organization may be unable to defend continued use even when the implementation seems to work. That gap should be visible as a governed backlog with explicit release implications; it cannot be paid off solely by refactoring code.

The deepest lesson is that adaptation and discipline are not opposing values. A well-designed learning system uses short cycles to reveal errors early and uses explicit evidence standards to prevent unvalidated changes from being mistaken for established capability.

## Worked Northstar example

A sprint finishes a booking API but no one has tested duplicate messages or vehicle-offline behavior. The code may be merged but the system capability is not evidence-complete. Add those cases to the acceptance gate and make release readiness depend on configuration-specific results.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Velocity measures delivery throughput, not mission effectiveness or safety confidence.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 5: Iteration must still produce system evidence](../labs/lab-05-integrate-agile-product-engineering-with-syst.md), you will: Rework two user stories into evidence-linked capabilities with acceptance tests, architecture implications and a bounded release decision. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 5 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](04-frame-the-software-architecture-within-the-sy.md) and leads toward [next chapter](06-design-and-evaluate-architecture-with-quality.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w05.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
