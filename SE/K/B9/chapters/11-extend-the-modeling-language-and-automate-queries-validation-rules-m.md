# Chapter 11 — Extend the modeling language and automate queries, validation rules, matrices, and generated products

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 11 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 11](../labs/lab-11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) → attempt the [original Week 11 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w11.md) remains available for a quick recap.

## The decision behind the theory

Generic language constructs do not automatically express project-specific assurance, accessibility, analytic, or configuration concepts, and manual reviews do not scale. **Essential question:** What bounded language extension and automation will improve semantic quality without creating an ungoverned private language?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Extend only when a concept has stable semantics, repeated use, required properties/constraints, and review value. First test whether standard elements, specialization, value types, requirements, or a reusable library are sufficient.

A good extension defines purpose, base element, properties, units, multiplicities, allowed relationships, constraints, notation, examples, anti-examples, owner, version, and migration path.

Keep the extension small. Examples for this course include AccessibleServiceConstraint, AnalyticResult, EvidenceClaim, ModelUse, InterfaceContract, or ConfigurationApplicability. Do not recreate the entire project vocabulary as stereotypes.

Automated quality combines queries, tables, matrices, validation rules, and generated products. Rules should have stable IDs, severity, rationale, scope, detection logic, repair guidance, false-positive handling, and tests.

Report generation is not document export by screenshot. A generated product should include source element IDs, baseline/version, generation time, query/filter definition, and controlled narrative sections where human judgment is required.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Specify physical architectures, variants, configurations, instances, and lifecycle baselines**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Verify and validate the model, assess the design, respond to change, and defend the final baseline**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Automation should interrogate the model, not sanctify it

Automated model queries can detect missing ownership, inconsistent units, orphaned verification records, or invalid relationships across thousands of elements. Their power comes from making architectural rules operationally checkable. However, a model can pass every structural query while expressing the wrong operational concept. Semantic assumptions and stakeholder acceptance remain outside many automated validators.

Good model automation distinguishes syntactic conformance, semantic consistency, and fitness for an engineering decision. Reports should identify exceptions with severity and configuration rather than compressing every issue into a single green/red status. The most valuable automated query often asks a question that was previously too expensive to answer manually—such as which safety cases are impacted by a particular interface revision. This turns the model into an active engineering information system while preserving the need for human judgment about adequacy.

## Worked engineering example from the course

The project repeatedly needs to connect a requirement or decision claim to an external analytic run with model version, code version, dataset hash, configuration, inputs, uncertainty, result, and validity conditions. Standard dependency plus comments is inconsistent, so the learner creates a minimal AnalyticResult extension/library concept, validation rules requiring provenance and applicability, a query listing stale results after property changes, and a generated evidence appendix. Migration tests show how existing ad hoc result blocks are converted and how the extension can map to SysML v2 metadata in a future tool.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A stereotype `«risk-bearing-interface»` is useful only if its semantics and validation rules are explicit. Require each marked interface to have a hazard link, responsible owner, fault condition, and verification evidence. Otherwise language extension decorates diagrams but does not improve inference.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: metamodels, executable queries, and semantic model quality

### Automation is only as sound as the type system

A modeling language extension introduces new types, relations, and invariants. If a custom `SafetyCriticalFunction` stereotype is added without a formal definition of what it denotes, dashboards can count objects precisely while communicating an ambiguous fact. In metamodel terms, define a set of admissible entities, the allowed relationship signatures, and the predicates that well-formed models must satisfy. For example, an `allocatedTo` relation may require a function at its source and a capable architecture component at its target. A query should not accept arbitrary links just because a spreadsheet column contains the word “allocation.”

A useful automated rule takes the form: for every safety-critical function `f`, there exists a hazard-control rationale, an allocated implementation, and a verification case that exercises the function under its intended context. This can be expressed with first-order quantifier logic—`∀f: Critical(f) => ∃a,t: Allocated(f,a) ∧ Verifies(t,f)`—but presence of graph links is weaker than adequacy. A model can pass the rule with a test titled “verify safety,” even if no test method or acceptance criterion exists. Effective rules must inspect the quality of evidence, not only its cardinality.

### Queries require provenance and reproducible semantics

The results of a model query depend on a baseline, library version, tool behavior, scope filters, and interpretation of the relation types. A generated traceability matrix without that provenance can become stale the moment someone modifies the model. Treat a query output as a derived artifact: record the source model commit, query definition, execution tool version, timestamp, parameters, and exception handling. Re-execute rather than manually editing a supposedly generated report. If a tool silently drops unresolved references, its output may falsely suggest completeness.

In Northstar, a change to the dispatch function should trigger queries for allocated components, message interfaces, timing constraints, hazard controls, and acceptance tests. A basic dependency traversal follows directed links; a more sophisticated impact analysis distinguishes *causal dependence* from mere documentation reference. Graph reachability gives a useful candidate set, but cannot prove every reachable element needs change or every omitted element is safe. An engineer must review semantic completeness and cross-tool gaps.

### Measure rule quality with counterexamples

Validation rules can make two different errors. A **false negative** misses a genuinely defective model; a **false positive** flags a legitimate exception. Testing the rule requires deliberately crafted counterexamples, not only a large model that happens to pass. Introduce a missing verification case, an invalid allocation type, a duplicate identifier, and a valid justified waiver. Observe whether the rule responds as intended. When rule exceptions are permitted, require a named approver, reason, scope, and expiration trigger so exceptions do not become invisible loopholes.

The graduate-level objective is **semantic assurance by automation**, not automation for its own sake. A reusable query is powerful because it encodes a carefully reviewed question and can be rerun as the system changes. Its authority comes from a defensible metamodel and evidence interpretation—not the sophistication of the query language or the attractiveness of its generated charts.

## Phase 3 technical reference: A constraint must have defined semantics and an enforcement boundary

An engineering modeling language needs typed entities, a declared population of objects, null semantics, and the meaning of each constraint. The illustrative OCL invariant `Reservation.allInstances()->isUnique(r | r.id)` checks identifier uniqueness over the currently evaluated model population—not necessarily across remote databases. An operation contract restricting activation to a pending reservation cannot by itself prevent concurrent races. The [full OCL and persistence treatment](../../methods/uml-ocl-software-contracts.md) provides invariants, preconditions, postconditions, JSON counterexamples and explicit limits of a simple Python audit. Use it to justify the validation-rule scope before claiming automated model quality.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The extension duplicates a standard construct without justification.
* Custom semantics exist only in diagram notation or tribal knowledge.
* Validation rules have no tests, stable IDs, or repair guidance.
* Generated products cannot identify their model baseline or source elements.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a profile?
2. What is a model library?
3. What is validation severity?
4. What is a false positive?

<details><summary>Explain the answers</summary>

**1. What is a profile?** A mechanism for extending a modeling language through defined stereotypes, properties, constraints, and notation without changing the base metamodel.

**2. What is a model library?** Reusable model content such as value types, definitions, patterns, requirements, or domain elements that may avoid language extension.

**3. What is validation severity?** The classified consequence and required response when a model rule is violated.

**4. What is a false positive?** A rule reports a violation even though the modeled content is acceptable for the stated context.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 11](../labs/lab-11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[10 — Previous chapter](10-specify-physical-architectures-variants-configurations-instances-and.md) · [12 — Next chapter](12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md) · [Book index](../README.md)

## Phase 4 technical reading: Ground custom relations in typed semantics

A custom «risk-bearing interface» stereotype or evidence extension is useful only if its invariants are explicit: required hazard links, owner, configuration, verification observation, and applicability limits. The Campus Mobility JSON exercise defines a small type inventory and tests those relations against a release baseline. It catches mismatched results after a version change; it does **not** demonstrate compliance with OMG's SysML v2 grammar or KerML semantics. The [reference guide](../../methods/model-baselines-and-evidence.md) separates model-language conformance, semantic queries, configuration review and operational validation, and specifies what a real tool-validated `.sysml` exercise would require.

## Phase 5 technical reading: Split language conformance from project validation

An automated query should state what it establishes. A parser checks language syntax; a semantic modeler resolves definitions/usages and valid relations; a project checker can inspect allocation IDs and evidence configurations; tests support empirical behavior; authorities disposition residual risk. The Campus Mobility case's cross-document checker discovers mismatched owners and stale configuration labels but does not recognize SysML v2 abstract syntax. The [four-layer validation plan](../../methods/sysml-v2-modeling-and-traceability.md) gives specific outputs and negative tests for each layer, avoiding false claims of formal proof from a JSON snapshot.

## Step 03 integrated technical reference: NS-MBA9.1 — governed queries, validation rules and model exchange

### Make a query library that fails loudly

The Python checker implements a small **domain-specific typed graph**, not a conforming SysML parser. It accepts `need → requirement` only for `derives`, and `requirement → function` only for `allocatedTo`. It rejects duplicate identifiers, unknown dependencies, invalid interface units, missing allocations and evidence that pretends an old baseline is current. The [executable source](../tools/step03_book9_model_check.py) can be inspected and edited without proprietary tooling.

Each query should have a purpose, expected field types, unit definitions, controlled version and negative-case test. A query returning zero orphan requirements does not validate that requirements are true; a query returning every required interface name does not prove that messages can be exchanged safely. Separate **syntactic validation**, **structural/model-semantic validation**, **equation regression**, **engineering interpretation**, and **acceptance authority**.

### Change impact is a directed graph problem

For each model analysis, the dossier records upstream dependencies and downstream requirements. The impact function uses graph reachability to report everything explicitly connected to a changed element. When `I02` changes, the query returns `I02, M05, R05, E05`. Algorithmically, a breadth-first traversal explores each reachable node once; for a finite adjacency graph the time complexity is \(O(V+E)\). This is useful even with thousands of model elements, but only if important dependencies have been modeled. Run an adversarial test by deleting the `I02 → M05` relation: the impact report becomes incomplete without necessarily raising a syntax error. That is a missing-semantics defect, not a software exception.

A formal SysML v2 language/conformance check must use an appropriate implementation of the [OMG specification](https://www.omg.org/spec/SysML/2.0) and pinned libraries. SysML v2 is grounded in KerML and includes normative semantics; a JSON object that happens to contain words such as `requirement` and `part` does not inherit that conformance. For an actual tool interoperability exercise, separately check import/export identity, versioned API responses, and semantic round-trip equivalence.

**Exercise.** A generated report includes every requirement ID but omits which test configuration produced its compliance status. What validation rule is missing?

<details><summary>Worked answer</summary>

An evidence-applicability rule linking each result to a valid test, exact baseline, measurement method and source record. Presence of a requirement ID is only syntactic coverage. Negative-test the generator with a deliberately stale evidence row and ensure the report does not silently show green.

</details>
