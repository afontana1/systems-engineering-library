# Chapter 01 — Receive the baseline, define intended use, and tailor the MBSE method and modeling plan

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 1 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 1](../labs/lab-01-receive-the-baseline-define-intended-use-and-tailor-the-mbse-method-.md) → attempt the [original Week 1 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w01.md) remains available for a quick recap.

## The decision behind the theory

The program has several models and documents, but no agreed authoritative baseline or modeling purpose. **Essential question:** What model-based work is necessary for this decision, and how will the project know that the model is adequate and controlled?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Begin with a receiving audit, not immediate remodeling. Record source, owner, version, purpose, status, tool, schema, and known defects for every inherited asset. An attractive model with unknown provenance is not an authoritative baseline.

Intended use is narrower than a project slogan. Define the review or decision, owner, alternatives, claims, consequence of error, required confidence, time horizon, and users. One model may support multiple uses, but each use needs its own adequacy statement.

Tailor the method by mapping engineering questions to model content, analyses, viewpoints, queries, products, and reviews. Do not remove a method step simply because the tool makes it inconvenient.

The modeling plan is part of technical planning. Include information architecture, package structure, identity and naming, element ownership, access, branch/baseline strategy, libraries, profiles, data exchange, validation, report generation, and retirement.

Define measurable quality indicators such as orphan count, unresolved validation severity, trace coverage, duplicated semantic content, stale generated products, unowned interfaces, and failed analytic synchronization. Metrics do not replace judgment, but they make review repeatable.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **the preparatory technical courses**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A model-based analytics effort begins with an intended engineering decision and an inventory of which parts of the inherited model can support it.

### Distinguishing related ideas

Model completeness is relative to use: a structural model adequate for component allocation may be insufficient for trip-time or energy prediction.

### Interpretation and boundary conditions

Tailoring should specify required semantics, units, configuration identity and model queries before creating additional diagrams.

## Worked engineering example from the course

The inherited shuttle model contains 2,418 elements in three top-level packages. A receiving query finds 46 requirements without verification links, 17 behaviors with no owner, two physical variants using different units for usable energy, and a generated interface document that is three revisions behind. The learner narrows the intended use to selecting a winter/accessibility expansion baseline, declares the requirements and configuration packages authoritative after correction, treats legacy diagrams as views rather than sources, and defines five mandatory queries and three review baselines.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A model is not authoritative because its file name says so. Define a baseline with model revision M3, 48 requirements, 12 stakeholder needs, 9 analysis runs, and 4 unresolved queries. Completeness is not the ratio 48/12; it is whether each required relation has a defined semantic meaning and a reviewer can detect missing evidence.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The modeling plan is a list of diagrams rather than a plan for engineering information and decisions.
* No authoritative source or identity scheme is established.
* Tool choice is treated as methodology.
* Critical inherited defects are ignored to preserve schedule.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is intended use?
2. What is a derived view?
3. Why tailor OOSEM?
4. What is a model baseline?

<details><summary>Explain the answers</summary>

**1. What is intended use?** The bounded decision, claim, review, or activity for which a model and its evidence are judged adequate.

**2. What is a derived view?** A presentation generated from authoritative model content; it should not become an uncontrolled competing source.

**3. Why tailor OOSEM?** Projects differ in decisions, lifecycle, risk, organization, and available evidence; tailoring preserves required reasoning while avoiding ritual work.

**4. What is a model baseline?** An identified, controlled configuration of model content and associated artifacts approved for a stated purpose.

</details>


## Deeper theory: model intended use and semantic governance

### Model credibility cannot be separated from the decision

A model may be excellent for requirement allocation and inadequate for safety assurance, even when its structure and syntax are identical. Credibility concerns whether a particular model supports a particular inference under declared conditions. A geometric model can verify packaging clearances but not necessarily fatigue life. A logical state model can expose unreachable modes while leaving sensor uncertainties unrepresented. An intended-use statement should name the decision, relevant domain, known abstractions, expected outputs, evidence basis, and consequences of being wrong. This prevents a model from acquiring more authority than its validation warrants.

Model-based systems engineering often combines multiple viewpoints: stakeholder needs, functions, behavior, logical structure, physical structure, parametrics, and verification. Their shared identifiers and relationships can improve consistency, but views also contain different abstractions. A state labeled “ready” in a software model need not mean the same thing as “ready for service” in an operational availability model. The modeling method must control these distinctions through defined states, transition conditions, and typed relationships, not rely on matching words.

### Consistency is necessary, not sufficient, for truth

A model can be internally consistent and wrong about physical reality. A queueing simulation may faithfully implement an incorrect passenger arrival process; a parametric energy model may correctly calculate from underestimated terrain resistance. Automated model checks can detect missing units, broken links, cycles where prohibited, or unsatisfied constraints. They cannot demonstrate that the represented mechanism is true unless coupled to empirical or independently justified evidence. The verification of the model implementation and the validation of its representation answer different questions.

An important semantic obligation is preserving invariant meaning across refinement. Suppose a logical requirement states that dispatch never issues conflicting vehicle assignments. When the architecture is split into cloud and edge components, a refinement must preserve the original invariant under the assumed message-delivery and failure model. If consistency is weakened during network outages, the design needs an explicit operating restriction or revised top-level requirement. A diagram that uses the same label at both levels has not established behavioral equivalence.

### Model evolution needs more than version numbers

Engineering projects change terminology, topology, requirements, and tool chains. An element ID should identify a persistent concept when that meaning remains stable; redefining the concept while retaining the ID can silently corrupt traceability. Splitting one element into two requires explicit supersession or derived-from relationships, so users can interpret old verification records correctly. A model change impact analysis should cover data schema, queries, reports, evidence associations, and partner exchange formats. Semantic versioning principles can help, but only if the team defines which changes are breaking in its domain.

Model governance should include representation review, query regression tests, authority ownership, access control, export fidelity, and independent challenge of critical assumptions. For example, a round-trip export/import test can verify whether constraints, units, IDs, and stereotypes survive exchange. Even perfect transfer does not prove the model represents reality. A credible model is a controlled argument with a known domain of applicability, not a self-certifying digital twin.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 1](../labs/lab-01-receive-the-baseline-define-intended-use-and-tailor-the-mbse-method-.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

Start of the book · [02 — Next chapter](02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) · [Book index](../README.md)
