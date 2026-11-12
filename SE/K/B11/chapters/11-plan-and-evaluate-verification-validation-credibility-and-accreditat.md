# Chapter 11 — Plan and evaluate verification, validation, credibility, and accreditation for intended use

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 11 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 11](../labs/lab-11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) → attempt the [original Week 11 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w11.md) remains available for a quick recap.

## The decision behind the theory

A model may be correctly implemented yet invalid for the decision, or credible for one use but not another. **Essential question:** What evidence is sufficient for an identified authority to accept this model for this specific use?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Verification evaluates implementation against specifications; validation evaluates representation against real-world knowledge for intended use; accreditation is an authority decision that the model is acceptable for a specified use.

Credibility is supported by evidence across conceptual model, data, implementation, results, uncertainty, history, user qualifications, configuration, and review. It is not a single score unless a governance framework defines one.

Independence is risk-based. The same person may perform multiple tasks in a low-consequence classroom model, but must still separate developer claims from reviewer evidence and record conflicts.

Validation uses multiple referents: data, theory, expert judgment, comparative models, experiments, trend and boundary behavior, and operational experience.

Accreditation should carry scope, configuration, conditions, limitations, expiration/review triggers, and prohibited uses.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Use M&S to support integration, verification, validation, and test decisions**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Apply M&S to production and sustainment, survey advanced methods, and defend the final baseline**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Model credibility is relative to the consequence of use

Simulation credibility should not be assigned a universal badge of “validated.” A model useful for ranking alternative scheduling rules might be inadequate for predicting absolute passenger waiting times, and completely unsuitable for certifying a safety requirement. Credibility depends on the decision, the cost of being wrong, and the physical mechanisms that must be represented. Validation against one dataset supports only a bounded inference about similar conditions.

Verification asks whether the model was implemented as intended; validation examines its correspondence to relevant observed phenomena; uncertainty analysis explores how unknown inputs and structures affect the result. These activities reinforce one another but are not substitutes. An accredited model is not infallible; accreditation authorizes a defined use under a stated governance process. A credible report should therefore articulate which comparisons are robust, which claims depend on calibration choices, and what evidence would cause the recommendation to change.

## Deeper theory: credibility as a structured inference about model use

### Verification, validation, and acceptance ask different questions

*Verification* asks whether the model implementation correctly realizes its specified computational design. *Validation* asks whether its representation of the world is sufficiently accurate for its intended use. *Accreditation* is a decision by an accountable authority that a model is acceptable for a specified purpose. A program can pass all code unit tests while modeling the wrong demand mechanism, and a model that closely predicts ordinary-day travel times may still be unacceptable for emergency evacuation decisions. These are not mutually substitutable labels or a single numerical score.

The intended-use statement should specify the decision, outputs, operating envelope, required distinctions between alternatives, consequences of a wrong result, and limitations of available evidence. A useful credibility argument follows the chain `decision → consequential claim → model assumption → test → evidence → residual uncertainty`. For Northstar, a model claim that a dispatch design has fewer missed critical transfers needs evidence about high-load operations, accessibility classes, and correlated failures; agreement on an average Tuesday is insufficient. The assurance argument must be narrow enough that an evaluator can identify exactly which claims have support.

### Predictive accuracy is not identical to decision fidelity

Suppose two dispatch policies have modeled missed-transfer rates of 4% and 6%. A comparison may be decision-relevant if the *difference* is modeled credibly, even when absolute rates are biased. Conversely, a model with a low average error can systematically reverse the ranking of policies near saturation. Define reference observations `y_i`, predictions `ŷ_i`, and residuals `r_i = y_i − ŷ_i`. A small aggregate root-mean-square error can conceal error concentrated on rare but severe events. Assess calibration by regime, class, geography, and time, using withheld conditions where feasible. Compare model predictions to measured uncertainty, not to a fabricated noiseless truth.

Validation data themselves are limited. Incident logs may exclude travelers who never requested service, timestamps from different agencies may not share a clock, and the operational baseline may have changed since collection. An apparently successful test on historical data may involve data leakage if model parameters were selected after seeing those same outcomes. Distinguish development data, calibration data, independent challenge cases, and the final acceptance evidence. When independent observations are impossible, use conservation laws, limiting cases, expert review, and cross-model comparisons while saying that these do not equal empirical validation.

### Uncertainty should be propagated through the actual decision

Represent parameters and scenario conditions by `θ`, and the decision-relevant output by `g(θ)`. Uncertainty in `θ` can come from measurement error, natural variability, or missing model structure; these sources merit different interventions. Parameter sampling propagates uncertainty within the assumed structure but does not reveal a missing road-closure mechanism. If evidence permits a joint distribution `p(θ)`, predictive outcomes are a mixture `p(y) = ∫ p(y|θ)p(θ)dθ`. A tight simulation confidence interval over random seeds can coexist with a wide interval from uncertain demand, or from structural choices that have not been quantified at all.

For an acceptance decision, report where the recommendation changes, not only its probability under one prior. If the preferred Northstar policy fails under plausible synchronized vehicle and communication outages, a sponsor may require operational restrictions, a backup mode, or additional testing. Decision consequences matter: a model used to schedule optional staffing need not meet the same credibility burden as one used to justify reducing evacuation capacity. Confidence is therefore proportional neither to the size of the simulation nor to the authority of its developer.

### A credibility case has an expiration condition

A model's acceptance should specify the version and configuration, responsible maintainers, evidence provenance, environmental ranges, and triggers for re-evaluation. A route redesign, new priority rule, software update, or change in traveler behavior may invalidate a previous model-use decision. Governance distinguishes the model builder, technical reviewer, operational owner, and accepting authority to limit self-certification. The resulting credibility case is not a certificate of universal truth: it is a traceable, revisable warrant for using a bounded representation to support a consequential engineering judgment.

## Worked engineering example from the course

The mobility model is verified and matches weekday operations, but no evidence supports emergency-event crowd behavior. The authority accepts it for weekday fleet sizing with limitations and rejects its use for emergency evacuation planning. A separate data and model-development plan is required for that use.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Verification asks whether implementation matches the specified conceptual model; validation asks whether the model adequately represents the system for an intended decision. Independent accreditation, if used, is a separate authority judgment.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Phase 3 technical reference: Build a scoped credibility case

Use a queue benchmark to distinguish credibility claims. The exact formula \(E[W]=1/(\mu-\lambda)\) is a verification oracle **only for the idealized M/M/1 conceptual model**; reproducing 20 minutes at \(\lambda=9,\mu=12\) cannot validate real-world arrivals, priorities, abandonments, or service-time dependence. A model credibility argument should list: intended decision and consequence; operating envelope; code and solution verification; input provenance; independent validation data; uncertainty partition; structural discrepancies; and accountable acceptance authority. A 95% Monte Carlo confidence interval measures sampling precision, not a blanket 95% probability of actual mission correctness. Study the [full worked credibility matrix](../../methods/simulation-output-and-credibility.md) and identify which real Northstar measurements could challenge the model.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Verification is presented as validation.
* The accreditation authority or intended use is unspecified.
* Known discrepancies or limitations are omitted from the use statement.
* The same data are used for fitting and claimed as independent validation without disclosure.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Can a model be valid in general?
2. What is accreditation?
3. What is conceptual-model validation?
4. Why tailor V&V?

<details><summary>Explain the answers</summary>

**1. Can a model be valid in general?** Validation is always relative to intended use, conditions, resolution, and acceptance criteria.

**2. What is accreditation?** An authority decision that an M&S and its evidence are acceptable for a specified use.

**3. What is conceptual-model validation?** Evaluation that the conceptual representation, assumptions, and rules are adequate for intended use.

**4. Why tailor V&V?** Effort and independence should match decision consequence, uncertainty, novelty, and available evidence.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 11](../labs/lab-11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[10 — Previous chapter](10-use-m-s-to-support-integration-verification-validation-and-test-deci.md) · [12 — Next chapter](12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md) · [Book index](../README.md)

## Phase 5 technical reading: Credibility in high-consequence tail predictions

For a normal toy exceedance \(P(Z>4)\approx3.167\times10^{-5}\), 50,000 direct draws yield only 1.58 expected events. Shifting the sampling distribution and applying the correct density ratio can reduce numerical error without changing the target; it does not validate the Gaussian model or assign a real-world failure probability. A credibility argument must address calibration data, held-out scenarios, model-form discrepancies, proposal diagnostics, error decomposition and operating envelope. The [worked simulation calibration and rare-event method](../../methods/simulation-calibration-and-rare-events.md) provides testable computations and explicit limits on their decision relevance.

## Step 03 integrated mobility simulation case: VV&A credibility argument

### Four distinct judgments

* **Verification:** does the code correctly implement the specified event logic (including queue, energy and charger invariants)?
* **Validation:** do the model and its outputs adequately represent the *real* campus for the stated intended use and operating conditions?
* **Credibility:** is the total evidence, with limitations and independent review, trustworthy enough relative to the decision's consequence?
* **Accreditation/acceptance for use:** has an authorized decision body approved a bounded use? A student, developer or test runner cannot grant this merely by reporting an internal pass.

The [NS-MS11.1 credibility register](../case/credibility-register.csv) documents computational tests as a **tested** software claim, but input distribution validity as assumed and accessible-tail/charger-location validation as missing. There is **no** accreditation request or approval in the synthetic case. The course's NASA/DoD references motivate role-based evidence discipline; this teaching checker is **not** a standards-conformance tool or a substitute for authoritative requirements interpretation.

### Construct a claim–evidence–limitation argument

**Claim C1:** The implementation consistently schedules requests, trips and chargers for declared synthetic scenarios. *Evidence:* deterministic queue trace, mass-conservation/resource checks, controlled seeds and negative tests. *Defeater:* code changes, untested tie conditions, or incorrect triangular parameter ordering. **Claim C2:** The model's 14-vehicle baseline fails the fictional wait-time thresholds. *Evidence:* versioned assumptions, 30 independent replications and per-day p90 output with modeled confidence interval. *Defeater:* model-form error, omitted ride pooling, changed demand or unrepresentative tail assumptions. **Claim C3:** Fourteen vehicles cannot meet real operational needs. *Not supported.* No independent real-world referent or full dispatch and staffing model exists. Distinguishing C2 from C3 is the central professional obligation.

### Use a proportional credibility scorecard carefully

Rather than reducing credibility to one arbitrary score, classify evidence by source, regime, independence and consequence. A simple worksheet can show each claim's intended use, configuration, uncertainty budget, available tests, independent reviewer, expiration trigger and owner. It must expose *disqualifying gaps*, not average them away. A credible model for **initial option screening** can be unacceptable for public statements, final procurement or operational certification. The credibility register is a starting artifact, not an accreditation decision record.

An example *expiration condition* is material variation in the accessible-trip fraction from 0.14, introduction of ride pooling, a new charger site, changed dispatch priority, or demand spikes outside the tested scenarios. Such changes require configuration review, new tests and potentially a new validation program. “Passed 30 seeds” is not a timeless property of the model.

### Worked decision and exercise

Suppose two independent teams obtain the same sample mean daily p90 of 36.4 minutes using identical assumptions. One team labels the result “operationally verified.” The other labels it “synthetic screening evidence, no field qualification.” Which statement is defensible? **Solution:** only the second. Agreement may improve computational reproducibility, but both teams may share the same incorrect referent and model structure. The decision authority needs an assessment of validation evidence, intended-use boundaries, risks and consequences before accepting a use.

**Red-team exercise.** Change accessible share from 0.14 to 0.22 and rerun the fixed input generator. Does any computed difference prove discrimination in a real dispatch system? **Answer:** no; it tests sensitivity of the *modeled policy*, which may itself allocate accessible vehicles poorly. The discrepancy identifies the need for user-centered review and an alternative dispatch policy; field data and stakeholder input are still needed.

[Evidence register](../case/credibility-register.csv) · [Chapter 12](12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md).
