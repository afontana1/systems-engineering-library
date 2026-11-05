# Chapter 3 — Stakeholder concern becomes a model view

*Book III: Introduction to Model-Based Systems Engineering · Week 3 — Stakeholders, concerns, needs, context, ConOps, and operational scenarios*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 3](../labs/lab-03-stakeholders-concerns-needs-context-conops-an.md) before attempting [the assessed Week 3 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w03.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **stakeholders, concerns, needs, context, conops, and operational scenarios** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A stakeholder is not the same as a user. Passengers, dispatch operators, maintainers, accessibility advocates, campus security and sponsors have different concerns; each deserves a view showing the relevant facts without fragmenting the underlying model. The operational context distinguishes external actors and systems from internal functions. A ConOps describes what happens under plausible conditions, including degraded operations rather than only the happy path.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

A viewpoint encodes a stakeholder concern and chooses which relationships make that concern visible; no single diagram is a neutral description of everything.

### Distinguishing related ideas

Requirements, operational scenarios and structural views are not interchangeable because each asserts different information and hides different uncertainties.

### Interpretation and boundary conditions

Compare an accessibility scenario with a fleet-capacity diagram: one exposes experience and timing, the other exposes resource limits; they need explicit consistency links.

## Worked Northstar example

In a late-night shuttle scenario, a rider requests pickup, dispatch assigns a vehicle, a location service reports a delayed position and an operator intervenes. Map the external actors, information exchanged, operational states and decision authority. The late report belongs in the scenario and may imply an additional requirement for freshness.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

An actor omitted from the context may later appear as an “unexpected” interface; an actor shown inside the system by mistake may hide a dependency the engineering team cannot control.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 3: Stakeholder concern becomes a model view](../labs/lab-03-stakeholders-concerns-needs-context-conops-an.md), you will: Hold a synthetic stakeholder hearing on late-night service. Produce one context model, three scenarios, and a concern-to-view mapping that records two conflicting concerns. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 3 deliverable and grading rubric.


## Graduate depth: stakeholder views as typed projections of system reality
### Stakeholder concerns are not yet model requirements

A concern expresses what someone needs to understand or protect; a requirement is a testable obligation that results from reconciling that concern with mission context and authority. If riders say “late-night service must feel safe,” the engineer cannot infer one definitive design feature. Safety perception may involve lighting, waiting time, visibility, emergency communications, assistance access, and prior experience. The modeling task begins by separating the concern, affected stakeholder, observable consequence, candidate measures, and uncertainties in interpretation. Stakeholder statements are evidence about preferences and experiences, not automatically a complete technical specification.

Model views are projections chosen to answer specific questions. A context view identifies external actors, exchanges, and boundary assumptions; an operational scenario describes a trajectory of interactions; a state machine represents permitted transitions; a parametric view represents measurable constraints. No single diagram proves that all other perspectives are consistent. Viewpoint governance should state the question, underlying model elements, included and excluded phenomena, granularity, and criteria for a valid answer. Otherwise two correct-looking diagrams may use incompatible meanings for “request,” “arrival,” or “service complete.”

### A scenario is a controlled slice of a possible history

A scenario can be modeled as a trace `tau = (e_0, e_1, ..., e_n)` of events, states, and timed observations. The trace does not represent the entire operating space. To test completeness, vary key conditions systematically: peak versus quiet demand, normal versus degraded communication, novice versus expert operator, and successful versus failed allocation. The purpose is not to enumerate all possible histories, which may be infeasible, but to expose categories of behavior that would change requirements or architectural choices.

Northstar's late-night boarding scenario might include a vehicle that is physically present but has lost dispatch authorization. A view showing only a successful boarding event omits the distinction between location and authority. A context diagram can expose the dispatch link; a state machine can forbid door release without authorization; a human-system view can specify what the rider is told. The relations across views become engineering assertions that can be checked, not aesthetic similarities between pictures.

### Model quality depends on consistency and provenance

A concern-to-view matrix is useful when it distinguishes **coverage** from **resolution**. Linking a rider-safety concern to a diagram demonstrates that someone addressed the concern, not that the design mitigates it. A stronger chain is `concern → measurable outcome → operational scenario → obligation → responsible element → planned evidence`. Each edge has a different meaning; conflating them produces false traceability. Conflicts should remain visible—for instance, security's preference to minimize data exposure may conflict with operations' request for detailed incident logs. The resolution needs an explicit authority, rationale, and accepted constraint.

The final check is whether the model can answer a consequential question and reveal what it cannot answer. A qualitative concern model may justify interviewing users or specifying a service response, but it cannot establish a statistically defensible satisfaction rate without observational data. A simulated scenario may help discover omissions, yet it does not validate real human reactions. Treat models as disciplined, revisable hypotheses about system behavior; their value comes from making assumptions visible, permitting cross-view checks, and directing evidence collection.

## Continuity

This chapter builds from [previous chapter](02-modeling-plan-methodology-language-tool-and-r.md) and leads toward [next chapter](04-requirements-modeling-relationship-semantics-.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w03.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
