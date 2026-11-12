# Chapter 6 — Qualification procedures and readiness

*Book 8: System Test and Evaluation · Week 6 — Write formal qualification procedures and conduct the Test Readiness Review*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 6](../labs/lab-06-write-formal-qualification-procedures-and-conduct-the-t.md) without looking at the solution → return to [Week 6 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w06.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **qualification procedures and readiness**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A qualification procedure must be executable by an independent team: specify configuration, setup, calibration, personnel, stimuli, data fields, expected results, stop conditions and deviation process. A test readiness review gates the act of testing, not the later claim of product readiness.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Formal qualification procedures make actions and decision rules reproducible across people, equipment and configurations.

### Distinguishing related ideas

A test step without preconditions, expected results, anomaly handling and evidence identity can produce data without interpretable meaning.

### Interpretation and boundary conditions

Hold points should protect both safety and evidentiary validity when an unexpected condition arises.

## Worked engineering case

If a latency gauge’s calibration expired last week, the procedure may execute correctly while the resulting data lack metrological pedigree. The reviewer must address that defect before accepting the data.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

“Operator knows what to do” is not a controlled procedure. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Construct the integration test approach, SIL/HIL paths, and informal tests](05-construct-the-integration-test-approach-sil-hil-paths-a.md); the next connection is [Integrate hardware, software, cybersecurity, automation, and test-tool evidence](07-integrate-hardware-software-cybersecurity-automation-an.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Write a five-step procedure with numerical pass conditions, safe aborts and evidence capture; run a paper TRR.

**Problem B — Adversarial review.** Which entry condition would prevent a safe test start?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: qualification procedures as reproducible measurement systems

### A test procedure is an executable scientific protocol

A qualification procedure should enable independent operators to reproduce not only actions but also the conditions under which observations have meaning. It must define the article configuration, software and firmware versions, calibration state, test environment, stimulus, setup tolerances, timing, data-recording paths, anomaly handling, and objective criteria. A procedure that merely instructs “verify safe operation” hides the interpretation inside the operator's judgment. Such a result can be difficult to defend when a supplier disputes failure or when the same article later behaves differently.

The complete measurement chain includes the measurand, sensor, signal conditioning, sampling, timestamping, storage, transformation, and decision rule. Errors can enter at any step. A force sensor may be accurate but sampled too slowly to observe a brief impact peak; a correct log may use a clock that drifts relative to actuator data. Calibration of an individual sensor does not guarantee correctness of a multi-instrument derived quantity. A test report should therefore document uncertainty contributions and synchronization assumptions relevant to the acceptance threshold.

### Readiness is about controllable risk and interpretability

Test readiness review asks whether the test can be executed safely and whether its results will answer the intended question. Confirm physical protection, emergency shutdown, personnel qualification, configuration control, instrumentation capability, data retention, and handling of foreseeable faults. A script that exercises a hazardous transition without an adequately independent emergency stop may be analytically informative but unacceptable to run. Safety controls can themselves change test fidelity, so their influence on measured outcomes should be documented.

A practical readiness decision distinguishes critical conditions from administrative deficiencies. Missing sensor calibration can invalidate compliance evidence; a cosmetic report-format issue usually does not. An open discrepancy may be acceptable if it cannot affect the tested claim and the rationale is recorded. It is not acceptable simply because a schedule milestone is approaching. A conditional authorization should state precise operating limits and the authority who can stop the test.

### Repeatability and reproducibility are separate claims

Repeatability concerns variation when the same team, equipment, and method test essentially identical conditions. Reproducibility concerns consistency across operators, facilities, instruments, or implementations. If two laboratories differ materially, the discrepancy could reflect a real configuration effect, calibration mismatch, interpretation difference, or unmodeled environmental condition. Averaging their numbers is not a substitute for understanding the cause. A measurement-system analysis can partition some sources of variability, but only within its chosen sampling design and model assumptions.

For Northstar, consider a braking test whose result depends on commanded speed, slope, surface friction, load, software release, and the state of regenerative braking. Recording “stopping distance = 6.3 m” is not enough. The defensible evidence record includes those factors, uncertainty, test timestamp, procedure revision, raw observations, permitted deviations, and the responsible witnesses. When an apparent pass occurs very close to a limit, guard-banding and retest policy must follow the preapproved rule. A qualification procedure converts a physical experiment into auditable evidence; it cannot eliminate the limits of the represented scenario.

## Practice before the assessed course work

[Hypothetical Laboratory 6: Qualification procedures and readiness](../labs/lab-06-write-formal-qualification-procedures-and-conduct-the-t.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 6 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-TE8.1 — procedures and an evidence-aware Test Readiness Review

### Make the test repeatable enough to be challenged

A qualified procedure identifies purpose, requirement, article and instrument identifiers, calibration status, prerequisites, hazards, stimuli, operator steps, data collection, expected result, stop conditions, deviations and signatures. For TE8-R01 the procedure must define the *start event* and *end event* for every latency datum. It must also specify how lost, truncated or duplicated responses count: silently removing a timeout from the denominator biases a tail-performance result in the favorable direction.

The [test-plan extract](../case/test-plan.csv) is a concise control register, not a substitute for a fully approved procedural package. The [evidence register](../case/evidence-register.csv) must join the procedure version and article baseline to each result. A readiness review also examines test personnel, equipment and software dependencies, test safety, schedule, data integrity, contingency actions, and the authority to stop on unexpected behavior.

### Distinguish readiness to test from readiness to deploy

A readiness review may authorize a **bounded diagnostic experiment** while forbidding unrestricted field operation. For example, TE8-R03 reliability and TE8-R04 availability have **failed model assessments**, but controlled tests could still legitimately gather missing failure-rate and logistics data, with hazard mitigations. Likewise, TE8-R08 replay-defense testing is still **planned**. It may be suitable for a segregated cyber test bench but not live autonomous dispatch.

Define a disposition table: READY (environment and safety controls satisfied), READY WITH RESTRICTIONS (specified safe envelope), and NOT READY (uncontrolled hazard or invalid instruments). This status concerns the upcoming *test*, not the underlying requirement. Explicit distinction prevents 'TRR passed' from being reported as 'product qualified.'

**Exercise.** A team wants to run TE8-P-07 replay injection on an operating fleet because it can gather realistic logs. What review question blocks immediate approval?

<details><summary>Worked answer</summary>

A deliberately invalid command could actuate an unsafe controller. Require a segregated or appropriately safeguarded environment, declared stop conditions, independent authorization, and a controlled baseline before test start. Realism does not override test safety.

</details>
