# Chapter 12 — A defendable design is a consistent set of claims

*Book IV: Object-Oriented Analysis and Design · Week 12 — Baseline and defend the integrated OOAD design*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 12](../labs/lab-12-baseline-and-defend-the-integrated-ooad-desig.md) before attempting [the assessed Week 12 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w12.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **baseline and defend the integrated ooad design** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

The capstone integrates use cases, analysis concepts, states, interfaces, design collaborations, constraints, persistence and tests. Each view should answer a review question without contradicting the others. A useful defense reports a known limitation and the experiment needed to close it rather than claiming that UML diagram volume proves readiness.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

A software design baseline is a mutually consistent account of identity, behavior, responsibilities, interfaces and planned verification.

### Distinguishing related ideas

A neat collection of UML diagrams is not sufficient if a sequence permits an operation that the state machine forbids.

### Interpretation and boundary conditions

A strong defense compares views for contradictions and states which implementation decisions are intentionally left open.

## Worked Northstar example

A stakeholder adds a last-minute request: riders may transfer an active trip to another passenger. This challenges identity, authorization, state transitions, privacy and storage simultaneously. Trace the change through all affected views instead of editing only the use-case title.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## Graduate synthesis: architecture closure as a consistency proof

### Multiple views must describe one admissible system

A final object-oriented design commonly contains class, sequence, state, deployment, and interface views. Each is a projection of the same system, not an independent work product. The class view assigns ownership and invariants; sequence models prescribe interactions; state machines constrain legal event order; deployment identifies failure domains; interfaces define data semantics and service guarantees. A baseline is coherent only if the projections can describe at least one common implementation and operating behavior.

This can be understood as a satisfiability problem. Let `C_class`, `C_sequence`, `C_state`, and `C_deploy` be sets of design constraints. The baseline is *structurally realizable* only if there exists a design `D` such that `D` satisfies their conjunction. A sequence that shows doors opening after the shuttle begins motion may contradict a state-machine guard requiring zero speed. Each diagram can be internally neat while the conjunction is impossible. A rigorous review looks for cross-view contradictions and identifies whether an interface contract, allocation, or scenario assumption must change.

### Quantify how architecture boundaries create risk

Interfaces are both functional contracts and failure-propagation paths. Suppose a dispatch workflow requires an authorization service, localization service, and vehicle controller, each with independent availability 0.99 during a mission window. A naïve series approximation gives `0.99³ ≈ 0.9703`, lower than any component's availability. The calculation is only illustrative: common power, shared networks, and correlated maintenance can produce worse outcomes; graceful degradation and local caching can improve service availability. The point is that component quality does not automatically compose into system quality.

Architecture review should identify which decisions can be made locally during partition or latency spikes. For example, a vehicle should not rely on a continuously available remote dispatch server to enter a safe stop state. Define *control ownership*, timeout semantics, retry idempotency, and the degraded operational envelope. Record those decisions in interfaces, state machines, and deployment assumptions simultaneously; otherwise a resilience claim becomes invisible in the design package.

### Closure is a versioned argument, not a frozen picture

The final baseline should contain a controlled list of assumptions, unresolved concerns, and evidence references. A change to boarding capacity may touch occupancy invariants, accessible-boarding timings, queue estimates, software contracts, vehicle configuration, and test procedures. Treat this as a dependency impact query rather than a manual request to “update the diagrams.” The impacted set is the transitive closure of links from the changed element, checked by a reviewer for false positives and missing dependencies.

A defensible technical review distinguishes *verified consistency* (no detected contradiction in checked constraints), *validated fitness* (the design addresses stakeholder needs in intended use), and *accepted residual risk* (an authority permits use despite identified uncertainty). None implies the others. For Northstar, a signed design package might authorize a limited-campus pilot while explicitly excluding unmapped routes and unsupervised nighttime service. That scope statement is part of the design's meaning, not fine print added after engineering is done.

## What can go wrong—and why

Diagrams may be internally consistent but still solve the wrong problem; revisit actor goals and original constraints.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 12: A defendable design is a consistent set of claims](../labs/lab-12-baseline-and-defend-the-integrated-ooad-desig.md), you will: Present a ten-minute design defense and a change-impact matrix for trip transfer. Include two alternative solutions and the test evidence each would require. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 12 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](11-design-persistence-and-conduct-the-design-rea.md) and leads toward your final course defense. Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w12.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: defend the integrated design baseline

### 12.1 Trace requirements through obligations and evidence

A design readiness review should assemble the requirement, operational scenario, domain invariant, component responsibility, persistence enforcement, test record, and applicable baseline as a connected claim. The [traceability sheet](../case/traceability.csv) maps `SW-01` to `SW-07` through their use cases, owners and tests. A link is not itself proof, and “PASS” without matching revision, context and execution is not current evidence.

The [controlled dataset](../case/model-baseline.json) has seven requirements and seven test records: five *current synthetic passes*, `T-06` marked PASS against `SW-06` revision 1 after the requirement moved to revision 2, and `T-07` still PLANNED. The correct evidence count is therefore five current synthetic passes, **one stale claim, and one unexecuted claim**. The case is not ready for unqualified approval even if all the structural links exist.

### 12.2 A defensible review argument

| Review question | Current evidence | Disposition |
|---|---|---|
| Does model ownership cover each requirement? | Case checker: each has one declared primary owner | Structurally covered |
| Can ordinary duplicate requests be handled safely? | Idempotency and uniqueness in SQLite fixtures | Demonstrated for scoped synthetic cases |
| Are all constraint revisions tested? | SW-06 evidence refers to superseded revision | Open — rerun freshness acceptance |
| Is audit lineage verified? | SW-07 test exists only as a plan | Open — execute and inspect provenance |
| Are operations safe at realistic load? | Only illustrative latency budget; no field distribution | Open — conduct measured performance test |

This is a **conditional design-readiness decision**: continue engineering and independent validation, while withholding any claim of deployed safety or complete verification. The review should distinguish architectural consistency, unit or fixture test success, independently observed evidence, and operational authorization.

### 12.3 Change impact is part of the design

Suppose the telemetry-freshness threshold changes from 15 seconds to 8 seconds. Reevaluate the policy, data timestamp assumptions, `SW-06`, `UC-02`, fixture `F-06`, and the test evidence revision; recalculate normal-case eligibility (V-02's 6-second data still meet an 8-second threshold) and edge cases. Simply editing the requirement text while leaving test results unchanged creates a false assurance chain. The same logic applies when slot semantics change to overlapping intervals: class associations, OCL predicates, schema constraints, and concurrency tests all require coordinated updates.

**Solved checkpoint.** A reviewer counts seven verified requirements because seven test IDs exist. The corrected count is five current synthetic PASS entries, one stale revision and one planned test. Even the five current fixtures are not field verification; the result supports targeted design confidence, not final acceptance.

**Capstone exercise.** Use the [traceability CSV](../case/traceability.csv), [design decisions](../case/design-decisions.csv), and [checker](../tools/step03_book4_contract_check.py) to issue a one-page review disposition. Include two evidence gaps, one production risk the fixtures omit, a proposed acceptance test, and what baseline artifacts must change if the service introduces interval-based scheduling.
