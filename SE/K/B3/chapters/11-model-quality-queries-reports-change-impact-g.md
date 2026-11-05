# Chapter 11 — Quality queries are executable arguments

*Book III: Introduction to Model-Based Systems Engineering · Week 11 — Model quality, queries, reports, change impact, governance, and SysML transition*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 11](../labs/lab-11-model-quality-queries-reports-change-impact-g.md) before attempting [the assessed Week 11 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w11.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **model quality, queries, reports, change impact, governance, and sysml transition** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Model quality has at least two dimensions: structural integrity and decision usefulness. Structural checks find orphan requirements, untyped links, missing owners, invalid units and unresolved source differences. Decision checks ask whether the model predicts or explains something important with sufficient credibility. Both need repeatable queries and versioned reports.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Model quality can be phrased as executable questions

Manual inspection of a large model becomes unreliable because omissions and inconsistencies are distributed across many views. A model-quality rule is a query that asks whether a stated invariant holds: every safety-relevant requirement has an owner; every interface has direction and type; no verification record points to a retired configuration; every operational event has a defined recipient. These rules are **necessary conditions for model integrity**, not complete proof that the engineering design is correct.

A useful query returns a reproducible list of exceptions rather than a single reassuring percentage. “Ninety-eight percent linked” hides the importance of the remaining two percent. A missing link on an informational report differs sharply from a missing link on a braking command. Query results must therefore retain criticality, provenance, and review context. Automated checks free reviewers to spend attention on semantics and suitability, which are harder to encode, while still preventing routine structural mistakes from accumulating.

## Deeper theory: model queries are tests of representation and meaning

### A query can be correct while its conclusion is wrong

Consider a model-quality query that reports, “All requirements have verification links.” If the rule searches only objects explicitly typed `Requirement`, but imported requirements were misclassified as comments, the query can return 100 percent coverage while omitting obligations. That is a *completeness* problem with the model population. Separately, if a link labeled `verifiedBy` actually points to an unapproved draft procedure, the syntactic relation exists but its semantics are wrong. Query correctness therefore depends on the metamodel, population boundary, relationship meaning, and evidence status—not just working code.

Database reasoning distinguishes closed-world interpretations, under which absent facts are treated as false, from open-world interpretations, under which absence may mean unknown. An engineering repository often mixes the two. A missing interface owner should be a clear violation when every interface is required to have one; a missing fatigue-test result may simply mean testing has not yet occurred. Queries must report `fail`, `pass`, and sometimes `unknown` or `not applicable`, rather than silently converting missing evidence into success or failure without regard to lifecycle state.

### Graph invariants make structural assurance executable

Useful invariants include: every approved requirement has at least one justified parent or approved origin; every safety-critical function has a responsible element; every interface has compatible port directions and units; and every formal verification verdict identifies the tested configuration. These are conditional rules. A requirement at concept stage may legitimately lack a final test case, whereas an acceptance-ready requirement should not. A strong rule encodes that distinction rather than using a single global red/green threshold.

A traceability graph also supports impact analysis by reachability. If a voltage tolerance changes, traverse downstream requirements, parameters, components, interfaces, test cases, and affected documents. But not every reachable node is genuinely affected: transitive links can be broad and semantically weak. Conversely, an omitted dependency can make an automated impact report dangerously short. Graph traversal yields candidates for engineering review, not an oracle of causality. Query results should preserve source, configuration, path, and reasons for including each impacted item.

### Test the query rules, not just the model

Quality automation is software and requires its own verification. Construct controlled mutations: delete a required owner, reverse an interface direction, change a unit, attach an outdated verification result, or introduce a broken trace. The corresponding rule should fail for the intended reason. Also introduce permitted exceptions to test false positives. Sensitivity to injected faults measures whether the checks can actually detect the defect classes they claim to cover; executing a rule without errors is much weaker evidence.

Metrics also face selection bias. A dashboard can report fewer rule violations because engineers improved the model, because they deleted hard-to-model objects, or because a rule no longer scans a relevant package. Trend comparisons require stable definitions, enumerated exclusions, and model-version provenance. In the Northstar case, model quality is not the number of green indicators; it is the defensible relationship between repository structure, real engineering obligations, and questions that reviewers can reproduce. The strongest repository makes both claims and uncertainty discoverable.

## Worked Northstar example

A change to vehicle telemetry freshness may affect requirement R-21, interface I-LOC, mode DEGRADED, safety hazard H-4 and verification T-21. A change-impact query should walk typed edges and disclose uncertainty, rather than relying on one engineer remembering every affected view.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Migrating a schema to a newer SysML representation without defining the meaning of each relationship can create apparently successful but semantically lossy models.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 11: Quality queries are executable arguments](../labs/lab-11-model-quality-queries-reports-change-impact-g.md), you will: Run three completeness queries and one impact query on the supplied relationship CSV. Propose a review gate and migration-check acceptance rule. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 11 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](10-verification-and-validation-modeling-configur.md) and leads toward [next chapter](12-integrated-model-baseline-capstone-review-ora.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w11.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.
