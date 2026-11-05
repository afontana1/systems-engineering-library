# Chapter 9 — A physical architecture is a trade, not a picture

*Book III: Introduction to Model-Based Systems Engineering · Week 9 — Candidate physical architectures, model-based trades, and alternative evaluation*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 9](../labs/lab-09-candidate-physical-architectures-model-based-.md) before attempting [the assessed Week 9 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w09.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **candidate physical architectures, model-based trades, and alternative evaluation** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Logical functions can be embodied in different physical configurations. Compare alternatives using common scenarios, comparable measures, consistent boundary assumptions, and explicit stakeholder priorities. Hard constraints exclude infeasible concepts before weighted preference scoring. A model-based trade should leave the rejected alternatives traceable for a later change in priorities.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Candidate physical architectures are configurations of constraints and decisions, not simply alternative pictures.

### Distinguishing related ideas

Comparing options requires a common operational scenario, consistent measure definitions and explicit assumptions about availability and degradation.

### Interpretation and boundary conditions

An architecture that wins on average capacity may lose when charging windows and shared communication faults are included in the feasible region.

## Worked Northstar example

Architecture A has high capital expense but low dispatch latency; Architecture B is cheaper but needs more network coverage. If B violates a strict offline-operability requirement, no amount of weighted score should make it admissible. After screening, test whether a ±20% change in latency weight reverses the ranking.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Decision screening and sensitivity

For a weighted utility `U = w·latency_score + (1−w)·cost_score`, let candidate A score 90 on latency and 50 on cost, and candidate B score 60 and 85. Then `U_A = 50+40w`, `U_B = 85−25w`, so the ranking reverses at `w=35/65≈0.5385`. Below that weight B ranks higher; above it A does. First, however, screen both against non-negotiable constraints. The equality identifies *preference sensitivity*, not evidence that either candidate meets its requirements.

Represent the alternative configuration, model revision, stakeholder weighting and evidence for criterion scores as separately reviewable objects.

## What can go wrong—and why

A single aggregated score hides uncertainty, non-compensable risks and the reason a stakeholder values one criterion.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 9: A physical architecture is a trade, not a picture](../labs/lab-09-candidate-physical-architectures-model-based-.md), you will: Assess three physical candidates using a constraints screen and weighted score, then perform a decision-weight sensitivity check and create a decision log. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 9 deliverable and grading rubric.


## Deeper theory: architecture trade spaces are constrained hypothesis sets

### A physical architecture is a mapping with feasibility obligations

Moving from logical functions to physical subsystems introduces a mapping `a: F → C` from functions to component resources, possibly with replication, sharing, or split responsibility. Allocation is not arbitrary. A component must have the required capability, its interfaces must satisfy data and energy contracts, and its timing and safety assumptions must support the mission behavior. A single processor may host several functions, but the functions then share failure modes, memory bandwidth, power, and scheduling resources. A distributed allocation may improve fault isolation while adding network delays and synchronization complexity.

The architecture trade is constrained by more than top-level performance. If an alternative violates a safety rule, mass limit, licensing constraint, or a hard environmental condition, a high weighted score should not rescue it. Let feasible alternatives satisfy `g_j(x, θ) ≤ 0` for all mandatory constraints `j` under the stated design assumptions `θ`. Objectives such as cost, maintainability, energy consumption, and service latency can then be evaluated within the feasible set. This separation prevents a method from treating an unacceptable safety consequence as though it were simply a low preference score.

### Interfaces and common causes determine much of the risk

Two architectures with the same number of components can have different integration risk because of interface topology. A highly connected component is often a single point for propagation of interface or change defects. Graph analysis can identify cut vertices, critical communication paths, and places where a common mode disables multiple functions. But topology is not destiny: redundancy succeeds only if replicas do not share decisive vulnerabilities. Two dispatch servers on the same electrical feed are not independent protection against loss of that feed. Failover tests must represent the intended detection and switchover behavior, not only steady-state operation.

A conceptual comparison might examine a central dispatch architecture and a federated dispatch architecture. Centralization simplifies consistency and may reduce duplicate assignments; federation can preserve local operation during a network partition. Neither is inherently superior. The decision depends on what “available service” means during partition, how stale information is handled, whether autonomous local assignments are safe, and what reconciliation occurs afterward. Those are operational and state-consistency questions that a box diagram cannot settle.

### Robust selection requires uncertainty and sensitivity analysis

Suppose architecture A has nominal lifecycle cost 90 units and average delay 7 seconds, while B costs 98 and has delay 5 seconds. Without an explicit value function and hard thresholds, declaring B “better” is unjustified. A stakeholder may require delay below six seconds, making A infeasible; another may accept eight seconds and prioritize affordability. Even the numbers are conditional: a narrow test load may understate tail delay, and cost estimates may omit cybersecurity maintenance. Explore parameter ranges, scenario mixes, and threshold crossings before presenting a single ranking.

A useful model artifact contains the selected architecture, rejected alternatives, credible conditions under which the decision would reverse, and the specific evidence needed to reduce those uncertainties. This records the *decision's robustness*. The architecture model is a hypothesis about real behavior and life-cycle burden; only analysis, prototyping, and testing within relevant conditions can progressively substantiate it.

## Continuity

This chapter builds from [previous chapter](08-values-units-measures-constraints-parametrics.md) and leads toward [next chapter](10-verification-and-validation-modeling-configur.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w09.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
