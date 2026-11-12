# Chapter 3 — Read system models critically

*Book V: Software Systems Engineering · Week 3 — Interpret and critique the system model for software realization*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 3](../labs/lab-03-interpret-and-critique-the-system-model-for-s.md) before attempting [the assessed Week 3 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w03.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **interpret and critique the system model for software realization** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A system model can be complete-looking and internally inconsistent. Software engineers must question allocation assumptions, performance budgets and unmodeled failure modes before committing to implementation. Convert vague model elements into explicit contracts, test scenarios and unresolved questions. Model authority should be clear: a diagram may be illustrative while a requirements baseline is normative.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Reading system models critically means asking which semantics and authoritative configurations each diagram represents.

### Distinguishing related ideas

A line indicating data flow does not guarantee delivery; a requirement-to-component allocation does not guarantee implementation or evidence.

### Interpretation and boundary conditions

Before trusting a model-derived software backlog, check version consistency, interface ownership and unstated timing or environmental conditions.

## Deeper theory: reading architecture models as claims, not illustrations

A model can be syntactically well formed and still be misleading. A block diagram may show correctly connected services while omitting the operational conditions under which those connections fail. A requirement relationship may be valid according to the metamodel while linking an unsuitable test to the claim. **Model criticism** therefore operates at several levels: syntax, semantics, explanatory adequacy, predictive accuracy, and evidential relevance. These levels should not be collapsed into a single “model quality” score.

The first level, syntax, asks whether the representation follows its language rules. A valid connector joins allowable endpoints; a property has a legal type; an identifier resolves. The second, semantics, asks what the representation asserts. Does a dashed arrow mean data flow, dependency, refinement, or verification? The third asks whether the model contains the mechanisms needed for its intended analysis. A service boundary diagram without retry paths may be adequate for organizational responsibility but inadequate for analyzing overload propagation. The fourth asks whether outputs agree with appropriate observations or independent calculations. The fifth asks whether those outputs bear on the operational claim being made.

### Views are abstractions with preservation obligations

A view omits detail to make some questions easier to answer. When Northstar depicts dispatch as a single software component, it may be intentionally abstracting the database, message broker and cloud deployment. That is acceptable for evaluating functional allocation. It is not adequate to infer that a reservation is atomic or that the service has no single point of failure. A disciplined reviewer asks which properties are **preserved under abstraction**. If a conclusion concerns concurrency or recovery, details hidden by a functional view may be essential.

This distinction is related to formal refinement. A more detailed design refines an abstract design when its observable behavior satisfies the abstract specification under stated assumptions. Simply adding more classes and connectors does not prove refinement; the detailed model may introduce traces that violate a requirement, such as duplicated booking commits. Refinement is about preservation of claims while implementation detail is introduced, not about increasing diagram density.

### Traceability is necessary but not sufficient for evidence

A requirement-to-test relationship can be checked mechanically for missing links, but the mere existence of a link does not establish that the test is capable of detecting violations. Suppose a requirement promises that every boarding interface remains usable under rain. A linked test performed in a dry laboratory may establish correct basic operation but not weather robustness. The correct evidential relationship depends on test conditions, coverage, measurement validity, configuration, and the acceptance rule. Evidence must be **relevant, sufficiently discriminating, and configuration matched**.

One useful perspective is a directed claim–argument–evidence network. A top-level claim is decomposed into subclaims about component behavior, interface compatibility and operational conditions. Each subclaim may be supported by tests, analysis or inspection; the links between them are arguments that rely on assumptions. This is a different network from an MBSE dependency graph, though they can share identifiers. A model may support impact analysis without replacing an independent assurance argument.

### Critical reading exposes hidden system boundaries

A design document that reports 99.9% service availability may not say whether the measure excludes upstream identity providers, cellular networks, planned maintenance or failed passenger interactions. The number's arithmetic may be correct under a narrow denominator and irrelevant to the mission. A model critic asks **what event was counted, over which population, in which environment, and for which configuration**. The same applies to performance and reliability estimates. Outputs without context encourage false certainty.

There is also a governance dimension. Models are usually maintained by specific teams, on specific schedules, using particular tools. If the authoritative performance budget is updated but the operational scenario model remains stale, both can be locally “approved” yet globally inconsistent. Technical governance should distinguish the **source of authority** for each property and the process by which changes propagate. A digital thread improves traceability only if the linked artifacts retain meaningful identifiers, revisions and ownership.

The purpose of critical model reading is constructive rather than adversarial. It identifies what a model can explain, what it cannot yet explain, and which unresolved claims require another representation or independent evidence. A precise, modest model may be more useful than an elaborate but unjustified one.

## Worked Northstar example

A context diagram shows a positioning feed but no latency constraint; a state model assumes positions are fresh. Software cannot implement both interpretations safely. Define telemetry freshness, fallback behavior and a planned stress test before accepting the allocation.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Relying on “the system model says so” is especially dangerous when model authors and software teams use different meanings of availability or real time.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 3: Read system models critically](../labs/lab-03-interpret-and-critique-the-system-model-for-s.md), you will: Conduct a model discrepancy review: log five ambiguities, assign owners and propose acceptance criteria for closure. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 3 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](02-model-software-allocations-interfaces-and-the.md) and leads toward [next chapter](04-frame-the-software-architecture-within-the-sy.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w03.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: critique the model by trying to falsify it

### Why an apparently complete model can still be misleading

The [architecture](../case/architecture.svg) identifies reservation API, telemetry ingestion, allocation store, operator interface, platform, and release pipeline. It exposes ownership and communication, but it does **not** establish whether messages are delivered, transactions are atomic, clocks are synchronized, or an operator follows a safe manual process. These omissions are expected in a structural view. The engineering error is to *infer* those properties from the view without additional contracts or evidence.

For each modeled edge, write at least three questions: what can fail, which party detects the failure, and which party remains responsible for the result? For **IF-03**, stale telemetry may result from sensor failure, network delay or replay. A simple data-flow diagram might show only that a location is available. The required behavior is stronger: the reservation API must reject observations older than five seconds, including apparently plausible but old samples.

### Turn model claims into falsifiable checks

A typed model-checking query can establish that every requirement has a declared owner and every interface endpoint is a known component. The [Python audit](../tools/step03_book5_system_check.py) performs this check against the controlled JSON and CSV. A positive result only establishes structural consistency of those records, not correctness of the system. The checker also verifies that each requirement has an evidence *entry*; Chapter 10 asks whether the evidence is adequate and current.

Apply three distinct tests to SWS-03: structural—does the allocation-store own the no-overlap obligation?; design—does the database schema enforce uniqueness of `(vehicle, slot)` for active reservations?; behavioral—do concurrent requests and retries preserve that property in realistic deployment conditions? This separation prevents a successful JSON audit from being mistaken for a proof of concurrent database behavior.

### Boundary critique and counterexample

Imagine both the application and its synthetic monitor run on the same failed cloud instance. The model contains a monitor component and reports no errors while the host is down because no measurements arrive. An “absence of errors” dashboard then falsely implies availability. This is a missing-measurement problem, not merely a missing component. To correct the model, specify the external observation boundary, lost-probe accounting and outage denominator.

**Exercise.** Add an interface whose `from` component is `mobile-client`, which is absent from the baseline. Run the structural checker. **Expected result.** It flags an unknown endpoint. Now add the component and rerun. **Interpretation.** The structure passes, but delivery semantics, authorization and real mobile-device tests remain unverified. The model checker is useful because it makes missing references visible; its limitations are just as important.
