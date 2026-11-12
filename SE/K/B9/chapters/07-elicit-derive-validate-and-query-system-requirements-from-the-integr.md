# Chapter 07 — Elicit, derive, validate, and query system requirements from the integrated analysis

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w07.md) remains available for a quick recap.

## The decision behind the theory

Requirements are not merely imported text; they should be justified by stakeholder outcomes, behavior, architecture, interfaces, measures, risks, and V&V strategy. **Essential question:** Does the model contain a necessary, sufficient, consistent, feasible, and verifiable requirement baseline for the expansion decision?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Derive requirements from the integrated analysis and preserve the rationale. A requirement should not exist solely because an old document contained it.

Separate requirement validation from verification. Validation asks whether the requirement is the right statement of stakeholder and mission need; verification asks whether the implemented system satisfies it.

Use semantic properties and structured text where possible: condition, subject, action, object, value, unit, tolerance, environment, time basis, and verification method. Natural language remains necessary but should be analyzable.

Queries can find missing sources, rationale, measures, owners, satisfaction, verification, or parent traces; duplicate IDs; conflicting values; circular derivation; and configuration-inapplicable requirements. Human review is still needed for necessity, feasibility, and unintended incentives.

The midterm baseline should be navigable as one graph. The walkthrough must demonstrate cross-view reasoning, not a tour of diagrams.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Specify interfaces, exchanges, allocations, ownership, and model-based change exposure**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Build executable parametric models with units, provenance, constraints, and linked analytics**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Requirements derivation is a justified transformation from operational need and architecture constraints into inspectable obligations.

### Distinguishing related ideas

A derived constraint must include the assumptions that generated its threshold; otherwise later reviewers may preserve the number after the context changes.

### Interpretation and boundary conditions

Coverage queries should distinguish a requirement having a model link from a requirement having adequate, current evidence.

## Deeper theory: requirements derivation is controlled logical refinement

### A requirement link should express a reasoned transformation

A system requirement is usually not copied word for word from a stakeholder need. Needs describe valued outcomes; requirements impose technically meaningful obligations on the system; derived requirements constrain subsystems, interfaces, and operation. These represent progressively narrower spaces of permitted behavior. A valid derivation must retain the parent obligation under stated assumptions. Merely drawing a *derive* arrow does not prove the implication.

For example, an operational need to provide safe transport during loss of central communications may imply requirements for local stop authority, limited autonomy, fault detection, and operator notification. Whether these are sufficient depends on the hazard model, how long the outage may last, and what passengers are permitted to do. The derivation should include assumptions and an argument that the selected subordinate behaviors jointly satisfy the intended service and safety properties.

### Completeness and consistency are separate model queries

A traceability query can ask whether every top-level obligation has at least one allocated or derived path. This tests structural coverage. It cannot establish whether paths preserve semantics. A time limit may be derived into budgets whose sum is too large; a safety restriction may be weakened into a warning; two requirements may demand incompatible behavior in the same state. Useful quality analysis combines relationship queries with constraint checks and scenario-based review.

Requirements can be treated conceptually as predicates over system behaviors. Refinement narrows the permitted set while preserving the parent's necessary behaviors. If a design refines “dispatch only after authorization” into rules that check authorization only during initial connection, it fails to preserve the property under reconnection or credential revocation. State-based counterexamples expose the missing condition even though a requirements matrix may be fully linked.

### Semantic types prevent plausible-looking errors

Many requirement failures are type errors in engineering clothing. A “response time” may be reported in milliseconds at one interface and seconds at another, or a vehicle “available” state may mean operable to one team and unassigned to another. Models can mitigate this by using explicit units, event definitions, enumerations, state machines, and temporal scopes. An automatically checked equation can enforce dimensional consistency; a controlled vocabulary can distinguish similarly named concepts. Neither resolves the underlying engineering meaning unless the definitions are correct.

Quantitative thresholds also require assumptions about uncertainty. A 250 ms end-to-end requirement cannot be verified merely because four component averages sum to 240 ms. Tail latency, scheduling contention, and common-cause overload may cause failure despite the nominal calculation. The requirements model should link each allocated budget to the dependency and performance model supporting it.

### Validation asks whether the refined obligations are worth meeting

Verification examines whether a design or test meets a specified requirement; validation examines whether the requirements and their implementation support actual stakeholder needs. It is possible to achieve perfect trace coverage while building a service that serves only low-demand periods or excludes users requiring accessibility assistance. Revisiting operational scenarios and outcomes is therefore part of requirements validation, not an optional extra after engineering completion.

A mature requirements model preserves the rationale for decisions and dissent: who requested an outcome, what alternatives were considered, why a threshold was chosen, what evidence supports the choice, and under which conditions the interpretation is valid. This makes the integrated model an instrument for controlling change and challenging unsupported claims, rather than a storehouse of apparently complete boxes and arrows.

## Worked engineering example from the course

The source baseline says, ‘The system shall provide rapid service in winter.’ The model traces the statement to an accessibility and service outcome, defines the population and operating mode, links 95th-percentile wait time and service availability measures, derives separate system requirements for winter accessible wait and availability, allocates contributing properties to dispatch, fleet, charging, and recovery logical elements, and creates analysis/test verification cases. A query finds that the proposed 8-minute threshold has no stakeholder acceptance record, so it remains a candidate target until the decision owner approves it.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Suppose requirement R17 says “service shall be fast.” A usable derived requirement names the event, threshold, percentile, population, operating condition, and verification method: “At weekday peak load, at least 95% of eligible dispatch decisions are issued within 2 s.” That translation changes how test evidence can be attached.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Critical requirements have no stakeholder/mission rationale.
* Satisfy or verify links are used as decorative relationships without evidence meaning.
* A critical requirement is unverifiable or has an unapproved threshold.
* The midterm model cannot be navigated as one integrated baseline.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is requirement validation?
2. What is a derived requirement?
3. What is a circular derivation?
4. Why include verification intent early?

<details><summary>Explain the answers</summary>

**1. What is requirement validation?** Confirmation that a requirement correctly and adequately expresses stakeholder, mission, and lifecycle need.

**2. What is a derived requirement?** A lower-level or additional requirement logically necessary because of analysis, architecture, interface, risk, or constraint.

**3. What is a circular derivation?** A set of requirements justified only by one another with no external need, constraint, analysis, or decision foundation.

**4. Why include verification intent early?** It exposes ambiguity, infeasibility, missing measurement capability, and excessive cost before implementation.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md) · [08 — Next chapter](08-build-executable-parametric-models-with-units-provenance-constraints.md) · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — derived requirements and typed trace queries

### A requirement is a supported claim, not a graph node count

The case separates six verifiable obligations from four source needs. `R01` derives a numerical throughput threshold from `N01`; `R03` specifies a population fraction for accessible pickups from `N02`; `R05` is a charging-recovery inequality from `N03`. The [requirements file](../case/requirements.csv) records identifiers, measurands, thresholds and intended test routes, while [model.json](../case/model.json) holds typed `derives` and `allocatedTo` relations. These relations are machine-checkable only because their endpoint types are defined.

In this small model, an accepted `derives` edge must be **need → requirement**, and an `allocatedTo` edge must be **requirement → function**. The checker rejects an unknown target, incorrect semantic edge, duplicate identifier or missing allocation. A generic undirected graph that counts every link alike cannot tell whether a requirement is sourced from a legitimate need or merely referenced by a test plan.

### Trace coverage is not evidence sufficiency

Define structural derivation coverage as

\[
C_D=\frac{\#\{r:\exists n,\ n\overset{derives}{\longrightarrow}r\}}{\#\{r\}},
\]

and a separate operationally applicable evidence count for a declared baseline. A planned test is not a completed result; a model output may support design analysis but not a physical acceptance claim. The evidence register marks `E03` **PLANNED** and `E06` **STALE**. The latter belongs to baseline `NS-MBA9.0`, not current `NS-MBA9.1`.

A sound trace query must also report what is **absent**: no approved winter-accessibility sampling data for `R03`, no current HIL concurrency demonstration for `R06`, and no operational sampling distribution for the model-based `R02` latency estimate. Absence is a legitimate outcome and should drive an action owner.

**Exercise.** You find six of six requirements linked to intended tests, but one test is unexecuted and one was performed on an old build. What are the two coverage percentages?

<details><summary>Worked answer</summary>

Test-plan linking is 100%. If the other four tests had suitable executed current-baseline results, the maximum current executed coverage would be 4/6 = 66.7%. In this actual synthetic register, four items are *modeled*, not executed qualifications, so the current executed qualification count is **0/6**. State the denominator and evidence criterion explicitly.

</details>
