# Chapter 12 — Verify and validate the model, assess the design, respond to change, and defend the final baseline

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 12 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 12](../labs/lab-12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md) → attempt the [original Week 12 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w12.md) remains available for a quick recap.

## The decision behind the theory

The final model must support a real design recommendation and survive independent challenge. **Essential question:** Is the integrated model correct, credible, current, and sufficient for selecting and baselining the winter/accessibility expansion architecture?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Build an explicit evidence chain: decision and intended use → stakeholder outcomes → scenarios and measures → behavior → logical and physical architecture → interfaces → requirements → analyses and results → V&V evidence → risk and recommendation.

Model verification includes schema/rule validation, semantic review, relationship and coverage queries, executable calculation tests, report-generation checks, configuration/variant tests, and reproducibility from controlled source.

Model validation is intended-use dependent. Compare behavior and outputs with source evidence, subject-matter expertise, test/operational data, prior accepted models, and stakeholder review. Document disagreement and limits.

Design assessment considers feasibility, completeness, margins, requirement compliance, integration/test readiness, affordability, supportability, accessibility, safety, cybersecurity, robustness, and residual risk. A model may be valid while the design remains unacceptable.

The live challenge changes one consequential element: a new accessibility regulation, a colder weather distribution, a charger supplier change, a discovered timing defect, or a revised budget. The learner must use the model to find and revise impacts rather than narrate them from memory.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Extend the modeling language and automate queries, validation rules, matrices, and generated products**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **the integrated course decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Model validation asks whether the chosen abstraction and the evidence behind it are fit for the intended decision.

### Distinguishing related ideas

A model may satisfy structural consistency checks and still misrepresent real rider demand or operations.

### Interpretation and boundary conditions

A final defense should identify which conclusions are robust to credible parameter changes and which depend on unresolved field measurements.

## Worked engineering example from the course

The final recommendation selects a 10-vehicle mixed accessible fleet with four 100-kW chargers, separated safety authorization, and staged winter deployment. During the defense, a supplier changes charger efficiency from 0.94 to 0.86 and removes a communication feature. The impact query identifies energy-margin equations, charging interfaces, one state transition, two requirements, three variants, seven verification cases, the cost model, and the generated interface specification. The rerun reduces joint compliance probability from 0.88 to 0.71. The learner revises the recommendation to qualify an alternate charger or add a fifth charger before full winter deployment and updates the decision conditions.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Change C42 increases peak passenger demand by 30%. Query the trace graph for objectives → capacity assumptions → assigned functions → parametric results → verification cases. A structurally valid graph that cannot identify an obsolete 20-request/hour experiment is not an adequate decision support system.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: model acceptance as an argument across viewpoints

### Verification and validation answer different questions

A model baseline is a finite representation of a much larger physical and organizational system. **Model verification** asks whether the constructed representation is internally consistent with its specification and implemented rules. **Model validation** asks whether it is adequate for a stated decision about intended use. A SysML requirements diagram can have no dangling identifiers and still misstate how accessible boarding works. Conversely, a validated user need can be poorly represented by inconsistent blocks, allocations, and behavior diagrams. A final review must examine both directions.

Model acceptance can be expressed as a structured argument: a claim, a set of evidence items, and a warrant explaining why the evidence supports the claim under particular assumptions. For example, “the selected architecture can meet peak demand” may depend on a capacity model, field-calibrated arrival data, a fleet-availability assumption, and an explicit service-level threshold. The warrant is not simply a hyperlink; it explains why those abstractions and data are applicable to Northstar's peak-hour operating envelope.

### Propagate change through an evidence dependency graph

Let a modeled requirement `r` depend on several functions, interface allocations, state transitions, and analysis parameters. Changing any of those elements can invalidate the original verification evidence. An impact query can identify the transitive closure of downstream dependents, but semantic review determines which items actually need reanalysis. If the boarding door cycle changes from 10 to 15 seconds, a capacity analysis, accessibility demonstration, software timeout rule, and schedule may be affected even when a simple requirement trace does not explicitly connect all four. Completeness of links is part of the assurance case.

Requiring every model element to trace to everything can be as damaging as having too few links. Distinguish the types `derives`, `satisfies`, `allocatedTo`, `refines`, `verifies`, and `assumes`; each supports a different inference. A test linked to a function does not automatically verify the availability requirement for the mission. That additional conclusion needs a model of service uptime, restoration, and scenario distribution.

### Model credibility has a decision boundary

Suppose two designs predict mean wait times of 4.8 and 5.2 minutes. A choice based on a 0.4-minute gap is unwarranted if measurement error, demand uncertainty, and model-form differences produce a one-minute uncertainty band. The relevant question is whether the expected advantage is *decision robust*. Use paired scenarios where possible, examine the sign of the difference under plausible inputs, and report threshold-crossing configurations. A model may be accepted for comparative screening even when insufficient for contractual compliance demonstration.

An effective final model package therefore includes versioned source data, modeling assumptions, rule checks, known limitations, counterexamples, numerical results, and instructions for reexecution. Reviewers should attempt an independent reproduction and deliberately violate a critical invariant to test whether model checks detect it. They should also challenge whether the abstraction hides organizational responsibilities, human recovery actions, or physical states. The best defense is not that all diagrams agree, but that **the model remains useful and corrigible when reality or project assumptions change**.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A critical result, query, or generated product cannot be reproduced from controlled source.
* The final model contains unresolved critical semantic or configuration defects.
* Model validity is claimed without intended-use evidence or limitations.
* The live challenge is dismissed, hidden, or handled outside configuration control to preserve the preferred recommendation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is model verification?
2. What is model validation?
3. What is design assessment?
4. Why separate recommendation from authority?

<details><summary>Explain the answers</summary>

**1. What is model verification?** Evidence that the model and its implementations, equations, queries, transformations, and configurations conform to their specifications and intended logic.

**2. What is model validation?** Evidence that the model is an adequate representation for its stated intended use.

**3. What is design assessment?** Evaluation of whether the proposed design, based on integrated evidence, is feasible, compliant, robust, supportable, and ready for a decision or next lifecycle step.

**4. Why separate recommendation from authority?** A model-based technical recommendation does not replace customer, safety, regulatory, contractual, or program decision authority.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 12](../labs/lab-12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[11 — Previous chapter](11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) · End of the book · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — defend a conditional decision

### Build a review argument from reproducible claims

The final product is not twelve isolated diagrams; it is a **controlled, revisable chain of assumptions, relations, calculations and evidence**. For NS-MBA9.1, the declared deterministic screen supports choosing variant B for further analysis: its 15 trips/hour ideal capacity exceeds 14, its assumed 240-kWh daily energy is below 260, and its nominal charging recovery of 270 kWh exceeds demand by 30 kWh. But `R03` has only a planned accessible-service test, `R06` has only an earlier-baseline concurrency test, and `R02` has a point-model latency result rather than an operational percentile demonstration. The disposition must therefore be **CONDITIONAL STUDY ONLY**.

When supplier request CR-42 changes charger power and efficiency, the reexecution reduces B's modeled recharge from 270 to 221.4 kWh and reverses its charging feasibility screen. The dependency query identifies `I02 → M05 → R05 → E05`. A fifth charger restores an idealized 36.75-kWh recovery margin, but still needs procurement, installation, fire/safety, electrical-load and operating-envelope checks. Never let proposed remediation overwrite the original failure or erase the change history.

### Verification, validation and decision authority have distinct roles

*Model verification* covers consistency against intended representation: typed links, units, calculated results, schemas and query behavior. *Model validation* asks whether the abstraction fits its decision context and whether inputs/behavior resemble representative operations. *System verification* assesses actual obligations on an identified test article. *Decision authorization* accepts residual risks with accountable governance. Passing any one does not imply the others.

Prepare a defense by attempting to invalidate your strongest claim: raise cycle time above the 51.43-minute threshold, perturb charge efficiency, remove an essential trace relationship, insert a stale test record, and test a duplicated resource allocation. The [case checker](../tools/step03_book9_model_check.py) will detect certain structural and numerical problems; it **cannot** discover every omitted real-world risk or prove SysML language conformance.

### Review deliverables and unresolved evidence

Provide a model baseline manifest, requirement source rationale, scenario coverage, typed trace matrix, functioning analyses and unit policy, variant comparison, change-impact report, reviewed evidence statuses, and explicit decision conditions. Record who can approve a waiver, who owns each remaining test, what operating envelope will be sampled, and which baselines are permitted for the next study. Preserve all counterexamples as part of the review record.

**Exercise.** A review board sees four `MODELED` items, one `PLANNED` item and one `STALE` item. The four modeled calculations all pass their screens. May the board declare `6/6 requirements verified`?

<details><summary>Worked answer</summary>

No. Four model-based estimates are conditional analysis, not automatically executed system verification. One field experiment is unexecuted, and the other demonstration belongs to a different configuration. The correct decision is a documented **conditional study recommendation**, with owner-assigned evidence actions and no operational approval. If future trials contradict the model, update the claims rather than defending the original recommendation by rhetorical certainty.

</details>
