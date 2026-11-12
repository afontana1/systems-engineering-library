# Chapter 10 — Specify physical architectures, variants, configurations, instances, and lifecycle baselines

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-specify-physical-architectures-variants-configurations-instances-and.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w10.md) remains available for a quick recap.

## The decision behind the theory

The selected direction must become a controlled physical solution family that supports procurement, integration, operation, maintenance, and evolution. **Essential question:** How can common architecture and valid variation be represented without uncontrolled duplication or configuration ambiguity?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Physical architecture includes hardware, software, data stores, communication, humans, facilities, support equipment, suppliers, and organizational responsibilities where they are part of the realized system.

Realization maps logical responsibility to physical implementation. Many-to-many mappings are common and should be explicit for integration, verification, safety, and change analysis.

Use types for common definitions, variants for valid alternatives, configurations for selected combinations, and instances for actual or planned individual realizations. Operating state is not a product variant.

Define option compatibility and applicability. A battery option may require a charger, thermal, software, mass, maintenance, and verification option set. Invalid combinations should be prevented or detected.

Baselines identify approved configurations at lifecycle gates. Preserve as-designed, as-built, as-tested, as-deployed, and as-maintained differences where the decision requires them.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Explore the trade space with alternatives, uncertainty, sensitivity, and model-based decision records**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Extend the modeling language and automate queries, validation rules, matrices, and generated products**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Physical model variants must bind architecture abstractions to the exact instances and configurations being evaluated.

### Distinguishing related ideas

A type-level assertion such as 'every controller has redundancy' may fail for a specific vehicle variant with a shared power bus.

### Interpretation and boundary conditions

Configuration-specific analysis prevents evidence from one variant silently being reused for another.

## Worked engineering example from the course

The common vehicle type has mobility, energy, compute, communication, passenger, accessibility, and safety subsystems. Variants include standard 8-seat, accessible 6-seat, and winter-enhanced accessible. A copied package initially carries an obsolete 76-kWh usable-energy value into the winter variant while the battery type now specifies 84 kWh. The learner replaces copies with specialization and property redefinition, adds compatibility rules between thermal kit and charger firmware, creates ten planned vehicle instances, and distinguishes the as-designed fleet configuration from the as-tested pilot configuration.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A type is not an operational instance. A `VehicleType` can have an 80-kWh nominal pack, while instance V02 has 65-kWh measured available energy following degradation. A qualification result for V01 is not automatically evidence for V02. Preserve variant, instance, and effective dates.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Variants are maintained as uncontrolled copied packages.
* A state or operating mode is represented as a product configuration.
* Invalid option combinations cannot be detected.
* As-designed and as-tested configurations are treated as identical despite known differences.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a variant?
2. What is an instance?
3. What is configuration applicability?
4. What is a baseline?

<details><summary>Explain the answers</summary>

**1. What is a variant?** A valid alternative form of a common system or element defined by controlled variation.

**2. What is an instance?** A particular realized or planned individual with identity and values based on one or more types/configurations.

**3. What is configuration applicability?** The condition under which an element, requirement, interface, analysis, or V&V item applies to a configuration.

**4. What is a baseline?** An approved, identified configuration used as a reference for control and further work.

</details>


## Graduate depth: variants and configurations as a product-family state space
### An architecture is instantiated through controlled choices

Physical architecture modeling must distinguish a general design definition, its allowed variants, a particular configured instance, and the as-built or as-operated state. A generic controller block may admit multiple processors, sensor options, or communication links; those options are not all simultaneously present in one deployed vehicle. Confusing type with instance leads to invalid resource sums and erroneous evidence transfer. A successful test on one configuration supports another only when the differences are irrelevant to the tested claim or justified by additional analysis.

A configuration can be represented as a vector `c = (v_1, v_2, ..., v_n)` of selected variant options subject to compatibility constraints. The apparent combination count is a product of option counts, but many combinations are infeasible because of electrical, mechanical, software, interface, or regulatory dependencies. A constraint model can prune invalid configurations; a configuration graph can record compatible versions and required migrations. Neither replaces physical validation when the combined behavior has not been observed.

### Equivalence is claim-specific

Two vehicle variants may be equivalent for passenger information display behavior and non-equivalent for braking distance. Equivalence must therefore be expressed relative to an observable property and an operating envelope. When a sensor is replaced, engineers should identify which interface semantics, timing properties, calibration assumptions, electromagnetic characteristics, and failure modes change. A blanket declaration that the substitute is “functionally equivalent” may be too weak for safety or reliability claims.

For Northstar, an alternative battery pack might share the same command messages while changing mass, charging thermal load, and emergency isolation behavior. A model with only electrical interface matching would miss the mechanical and safety consequences. The physical architecture needs linked parameter, interface, hazard, and verification views to identify such cross-domain effects. This shows why model-based configuration control is a systems concern rather than simply file versioning.

### Baselines change across lifecycle states

The as-designed baseline records intended structure, the as-built baseline records actual parts and software builds, and the as-operated baseline includes maintenance replacements, calibration, settings, and current restrictions. These states may diverge legitimately, but decisions require explicit reconciliation. A maintenance replacement should trigger checks that the approved configuration rules remain satisfied and that evidence is still applicable. When it does not, the system may need constrained operation until sufficient testing or engineering assessment is complete.

An architecture library gains power from reusable types and constraints, but reuse increases the consequences of a mistaken common assumption. Automated queries should flag incompatible variant pairs, orphaned allocations, obsolete interface versions, and tests linked only to obsolete configurations. Human reviewers should examine emergent effects that such queries cannot express. The goal is controlled variability: engineers can choose among feasible product families while preserving the ability to state exactly which system was built, what it can do, and why the supporting evidence is relevant.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-specify-physical-architectures-variants-configurations-instances-and.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md) · [11 — Next chapter](11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — variants, configurations and instances

### One family model, different controlled realizations

A modeling *type* describes a reusable definition; a *variant* is a configured selection from available options; an *instance* represents a particular occurrence; and a *baseline* freezes an approved configuration and its associated data. Conflating these levels makes results appear to transfer between products when they do not. The architecture array in [model.json](../case/model.json) declares variants A, B and C with immutable teaching assumptions until an explicit change is approved. It does **not** represent twelve individually controlled vehicles or an operational fleet inventory.

A variant-specific calculation must use that variant's fleet size, cycle, chargers, efficiency, and daily energy assumption. If variant C uses five chargers and 14 vehicles, copying variant B's four-charger recovery output would produce a false result. The [auditor](../tools/step03_book9_model_check.py) recomputes each alternative from its own fields and rejects invalid physical parameter values.

### Configuration baselines govern evidence applicability

The assurance claim concerns a specific configuration and operating environment. Evidence `E06` in [the register](../case/evidence-register.csv) describes an older `NS-MBA9.0` assignment-safety demonstration, while the study uses `NS-MBA9.1`. It is **stale for the new build** unless an approved applicability case explains why relevant parts are unchanged. A newer report from an unrelated vehicle instance is not inherently more applicable than an older controlled report on the correct configuration; pedigree is not a timestamp contest.

For change `CR-42`, the immediate impact graph flags `I02`, `M05`, `R05`, and `E05`. Before migrating to `NS-MBA9.2`, the board must decide if the change affects physical wiring, charger certifications, depot availability and test procedures not represented in this small graph. The model must support a *configuration-controlled review*, not just a choice among pretty variant diagrams.

**Exercise.** Can a passing nominal charger calculation for B be copied as evidence of C's recharge capability?

<details><summary>Worked answer</summary>

No. C has a different fleet energy load and charger count, and its physical integration is not defined by the B analysis. Recompute C under its own configuration and run profile, then independently evaluate evidence applicability.

</details>
