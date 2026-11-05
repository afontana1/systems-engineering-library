# Chapter 12 — The capstone is a defense of claims

*Book III: Introduction to Model-Based Systems Engineering · Week 12 — Integrated model baseline, capstone review, oral defense, and lessons learned*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 12](../labs/lab-12-integrated-model-baseline-capstone-review-ora.md) before attempting [the assessed Week 12 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w12.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **integrated model baseline, capstone review, oral defense, and lessons learned** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

An integrated model baseline is a defended argument about a particular system version, not a museum of diagrams. The review should ask whether stakeholder needs flow through requirements, behavior, allocation, analysis, design alternatives and verification evidence without unexplained gaps. A good defense exposes disputed assumptions and residual risks instead of polishing them away.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

A model-based review tests whether linked claims survive a change in configuration, scenario or evidence—not merely whether diagrams are complete.

### Distinguishing related ideas

The model is an argument scaffold; the physical system and measured observations remain distinct from the representation.

### Interpretation and boundary conditions

A credible review can trace from a stakeholder need through function, allocation, interface, test and decision while identifying where each transformation could be wrong.

## Worked Northstar example

The shuttle model claims peak service for 8 requests/hour with 2 vehicles at 3 trips/hour each. The capacity constraint contradicts the mission claim. The correct review action is not to hide the constraint but to identify the gap, bound the operating envelope, and propose a new candidate or an experiment that could change the assumptions.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Model trace completeness, model correctness and operational fitness are distinct achievements; the first does not guarantee the others.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 12: The capstone is a defense of claims](../labs/lab-12-integrated-model-baseline-capstone-review-ora.md), you will: Prepare a ten-minute design defense with a six-claim evidence matrix, one acknowledged contradiction, and a change scenario posed by a red-team reviewer. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 12 deliverable and grading rubric.


## Graduate depth: integrated model baselines as consistency arguments
### A model baseline is not a single master diagram

An integrated systems model is a network of claims about intended use, requirements, functions, structure, behavior, interfaces, and verification. Its quality rests on the meaning and consistency of those claims. A project may store all diagrams in one repository and still contain contradictory units, disconnected identities, circular requirements, or incompatible state assumptions. Conversely, separate tools can support a coherent baseline when explicit contracts, common identifiers, transformation rules, and revision relationships preserve meaning. Tool centralization is therefore neither necessary nor sufficient for semantic integration.

Treat the model as a typed graph `G = (V, E, T)`, where vertices are model elements, edges represent declared relations, and `T` maps each node and edge to a meaning and set of allowed properties. A trace from a mission need to a test case is only valid if its intermediate relations have the intended semantics. For example, `satisfy` says something different from `verify`; a requirement linked to a structure element is not thereby tested. Schema checks can catch missing references and invalid types, while domain checks must evaluate whether the relation is substantively correct.

### Consistency is layered, not binary

Syntactic consistency asks whether the repository conforms to its metamodel. Dimensional consistency asks whether quantities can be compared: adding a distance to a time is meaningless even if both are numbers. Behavioral consistency asks whether a sequence diagram permits only actions allowed by the state model. Allocative consistency asks whether every required function has responsible components and plausible interface pathways. Evidential consistency asks whether a verification result belongs to the configuration and requirement revision it purports to support. Passing one class of check does not establish the others.

A Northstar model may allocate rider authorization to software and physical interlocks but show a nominal route that bypasses the software check under communication loss. An automated query can detect that an allocated function lacks a verifying test, but discovering the contradictory operating mode may require scenario execution or expert review. The strongest approach combines executable invariants, reviewable trace examples, and targeted inspection of high-consequence scenarios.

### Change propagation is an epistemic problem

Suppose the interface latency limit changes from 200 to 120 milliseconds. A dependency query can identify linked functions, components, measures, and tests; it cannot guarantee that every semantic consequence has been modeled. The team should define an impact frontier containing directly related elements plus indirect effects such as resource utilization, retry policy, and human feedback. This resembles change propagation in software dependency graphs: relationships inform the search, while engineering reasoning determines completeness.

Review decisions should preserve the model commit, relevant tool versions, imported datasets, validation rules, waivers, and unresolved anomalies. A positive review is a claim about **this** baseline for **this** intended use and evidence scope, not permanent approval of an abstraction. When the system changes, automated checks and independent review must be rerun as appropriate. The capstone defense should therefore offer a traceable argument, demonstrate a failing test that the model can catch, identify blind spots it cannot catch, and explain what would invalidate its recommendation. That is stronger than a tour of attractive diagrams.

## Continuity

This chapter builds from [previous chapter](11-model-quality-queries-reports-change-impact-g.md) and leads toward your final course defense. Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w12.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
