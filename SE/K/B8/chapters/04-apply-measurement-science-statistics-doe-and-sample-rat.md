# Chapter 4 — Measurement and statistical confidence

*Book 8: System Test and Evaluation · Week 4 — Apply measurement science, statistics, DOE, and sample rationale*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 4](../labs/lab-04-apply-measurement-science-statistics-doe-and-sample-rat.md) without looking at the solution → return to [Week 4 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w04.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **measurement and statistical confidence**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

First identify the estimand and sampling regime. Measurement uncertainty, natural variation, model uncertainty and sampling uncertainty are not interchangeable. Design experiments to control nuisance variables and reveal interactions; a single favorable mean hides tails and rare failure risk.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Measurement joins physical signals to inferential claims through calibration, resolution, bias, sampling and uncertainty.

### Distinguishing related ideas

Repeatability is not accuracy: repeated measurements can be tightly clustered around a biased value.

### Interpretation and boundary conditions

Acceptance thresholds must account for the measurement process so borderline readings are not falsely treated as decisive evidence.

## Deeper theory: measurement is an inference with traceable uncertainty

### A measurement is not the property itself

A sensor reports an observation transformed by calibration, resolution, environment, data processing, and a definition of what is being measured. For a measured response time, the measurand might be the interval from issuing a command at a specific interface to observing a physical actuator response under a specified load. Timing only the software handler measures a different quantity, even if both numbers are labeled “latency.” Metrology begins by defining the measurand and measurement model before collecting numbers.

A simple measurement equation can be expressed as `y = f(x1, x2, ..., xk)`, where the inputs include instrument readings, calibration corrections, and environmental parameters. For small uncertainties, the combined variance can be approximated by `u_y² = sum_i sum_j (df/dxi)(df/dxj) cov(xi,xj)`. The cross-covariance terms matter when instruments share a clock, calibration standard, or environmental influence. Taking a square root of summed individual variances without these terms assumes uncorrelated inputs, an assumption that often needs justification.

### Calibration traceability does not guarantee accuracy in context

A calibrated instrument can still produce misleading results because of incorrect placement, sensor dynamics, aliasing, clock drift, or use outside its calibrated range. A traceability chain links measurement results to standards through documented calibrations with uncertainties; it does not establish that the chosen procedure measures the engineering property of interest. Verification requires both a trustworthy instrument and a trustworthy mapping from instrument output to requirement.

Replicate measurements can estimate repeatability, but systematic bias may remain invisible. Measuring the same delayed command a thousand times with an incorrectly synchronized clock makes the average very precise and still wrong. Likewise, a statistically narrow confidence interval around a biased estimator does not represent the full measurement uncertainty. The test plan must distinguish variability, systematic effects, model error, and uncertainty introduced by sampling the operating environment.

### Decisions near thresholds require guard bands

Suppose a measured maximum response is 245 ms against a 250 ms limit, with expanded measurement uncertainty of roughly 12 ms under the stated procedure. Declaring unconditional compliance ignores the possibility that the true result exceeds the limit. A **decision rule** specifies how uncertainty affects acceptance, including whether a guard band is applied and who bears the risk of an incorrect pass or fail. A conservative rule may require the observed result to be below `limit - guard_band`. The size of the band depends on uncertainty, error costs, and the applicable contractual or regulatory basis; there is no universal number.

Confidence intervals, tolerance intervals, and prediction intervals answer different questions. A confidence interval concerns an estimated population parameter; a tolerance interval aims to cover a chosen fraction of the population; a prediction interval concerns a future observation. Substituting one for another is a frequent source of overconfident compliance claims, especially when a requirement concerns a percentile or a worst-case event.

### Sampling must represent the engineering question

Random samples from a convenient test population may not represent field operations. Temperature, battery condition, radio interference, accessibility use, and peak load can materially change the distribution being measured. Stratification or designed test conditions may be needed to expose mechanisms not frequently encountered in ordinary random trials. The report should preserve the sampling frame, exclusions, test configurations, and statistical assumptions. Measurement quality is demonstrated by the strength of the inference from observed data to the specified system behavior, not by the number of significant digits on the result.

## Worked engineering case

With zero failures in 30 independent Bernoulli trials, the exact one-sided 95% upper bound on failure probability is 1−0.05^(1/30)≈9.50%. It does not demonstrate failure probability below 1%.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Zero observed failures is evidence, not proof of zero risk. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Design test concepts, environments, architecture, and model-based evidence](03-design-test-concepts-environments-architecture-and-mode.md); the next connection is [Construct the integration test approach, SIL/HIL paths, and informal tests](05-construct-the-integration-test-approach-sil-hil-paths-a.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Specify a sampling plan for one high-percentile wait metric and one failure-rate claim; defend independence and measurement error assumptions.

**Problem B — Adversarial review.** How does common-cause dependence change your confidence statement?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 4: Measurement and statistical confidence](../labs/lab-04-apply-measurement-science-statistics-doe-and-sample-rat.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 4 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Extended worked problems and lab

Study the [worked problem workshop on zero-failure confidence and test design](../practice/confidence.md), then complete the [extended laboratory](../practice/lab-confidence.md). The exercises are separate from the original assessed coursework.
