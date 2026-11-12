# Chapter 12 — Apply M&S to production and sustainment, survey advanced methods, and defend the final baseline

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 12 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 12](../labs/lab-12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md) → attempt the [original Week 12 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w12.md) remains available for a quick recap.

## The decision behind the theory

Models continue to change after a development decision. **Essential question:** How should the model be governed, updated, reused, and retired while preserving credibility and preventing use beyond evidence?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Production and sustainment simulations address capacity, spares, repair, staffing, reliability growth, availability, supply chains, upgrade timing, and operational policy.

Model monitoring compares predictions with new observations and identifies drift. Updates require configuration control, regression verification, revalidation, and possibly reaccreditation.

Use the right next method: feedback and long-term policy for systems dynamics; heterogeneous autonomous actors for agent-based models; physical trajectories and controls for continuous models; fast approximation for surrogates; coupled environments for federations.

A final recommendation should include decision, evidence, uncertainty, sensitivity, limitations, residual risk, and explicit conditions for change.

Model retirement is a controlled lifecycle decision when the use ends, evidence becomes obsolete, maintenance cost exceeds value, or a successor replaces it. Archive provenance and results needed for audit.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Plan and evaluate verification, validation, credibility, and accreditation for intended use**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **the integrated course decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Using simulation during sustainment requires monitoring whether operational mechanisms drift away from calibration assumptions.

### Distinguishing related ideas

A model of launch operations may become unreliable after dispatch policies, rider mix or maintenance practices change.

### Interpretation and boundary conditions

A credible decision process has explicit triggers for recalibration, retirement or restricted use rather than treating past validation as permanent accreditation.

## Worked engineering example from the course

The pilot fleet is approved at 12 vehicles with four chargers for weekday service, conditional on event-day staffing and additional disruption data. Three months of operations trigger model update because charging duration drifts in winter. The update passes regression verification, requires partial revalidation, and changes the event-service recommendation but not weekday fleet size.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A maintenance simulation with spare stock has replenishment lead time and shared supplier constraints. A constant replacement delay hides backorders. The model is adequate only if its sustainment decision is robust to these omitted mechanisms.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A simulation delivers 12, 14, 16, 18, 20 and 22 completed requests in six independent runs. Calculate sample mean.

<details><summary>Show a reasoned solution</summary>

The mean is (12+14+16+18+20+22)/6=17 completed requests. Six replications are insufficient to claim a rare-event guarantee.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: sustainment models as evolving operational hypotheses

### Development models expire as assets age

A simulation supporting design selection may use as-new component performance, controlled operating procedures, and a narrow demand envelope. Production and sustainment introduce manufacturing variability, repair queues, spares policies, aging, software patches, and changes in users. The model must be revalidated when those conditions change. A continuously updated model is not automatically a “digital twin”; operational usefulness depends on traceable identity, input timeliness, calibrated behavior, and decisions that the model is authorized to support.

For a repairable asset with mean time between failures `MTBF` and mean restoration time `MTTR`, an elementary intrinsic availability estimate is `A = MTBF / (MTBF + MTTR)`. Fleet availability can differ sharply because maintenance teams and spare parts are shared resources. A simple product of independent asset availabilities ignores correlated supply shortages and simultaneous environmental failures. Discrete-event sustainment simulation can represent repair queues, inventory constraints, priority rules, and delayed replenishment. Its output should include both expected availability and low-probability fleet-shortage episodes.

### Production capacity interacts with learning and rework

A nominal production line rate is not the same as delivered accepted units. Suppose workstations each process 10 units/day but a quality test rejects 8% for rework, and the rework consumes the same station capacity. Ignoring scrap and rework overstates sustainable output. At an idealized steady state with eventual successful repair and no extra handling overhead, processing effort per accepted unit is approximately `1/(1 − 0.08) ≈ 1.087` attempts. Real lines need additional buffers, inspections, and repair time, and rework may be correlated with batch quality. A model that captures only arithmetic throughput will miss congestion and rising cycle time near saturation.

Use conservation reasoning: what enters a buffer must eventually be processed, rejected, rerouted, or remain in inventory. During commissioning, transients may dominate; treating a short startup simulation as steady state produces misleading utilization and wait metrics. Validation should compare modeled queue lengths, rework rates, and turnaround times against observed batches, not just match the final shipment count.

### Model governance follows configuration and operating context

A sustainment model needs a maintenance policy owner, data-quality checks, change logs, and periodic recalibration triggers. If a new supplier changes component reliability, or software updates alter fault-detection behavior, conclusions from the old baseline may no longer apply. Distinguish the physical configuration, operational procedures, model executable, parameter dataset, and analytical report as separately versioned artifacts. Provenance allows reviewers to determine which advice was valid for which fleet.

A final defense should show at least one counterexample: a spares policy that looks economical at average failure rates but collapses when correlated failures occur. Explain whether model predictions are used to rank alternatives, set inventory, or justify safety-critical availability claims, because required credibility differs. **Sustainment is an ongoing learning loop**, not a one-time endorsement of a simulation completed during development.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The final package cannot reproduce a key result.
* The model is recommended for a prohibited or unsupported use.
* Update and reaccreditation triggers are absent.
* New evidence is ignored to preserve the original recommendation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is model drift?
2. When is reaccreditation needed?
3. Why use a surrogate model?
4. What should a retirement package preserve?

<details><summary>Explain the answers</summary>

**1. What is model drift?** Growing mismatch between model assumptions/parameters and the changing system or environment.

**2. When is reaccreditation needed?** When changes materially affect the intended use, evidence, risk, configuration, or acceptance conditions.

**3. Why use a surrogate model?** To approximate expensive model behavior for rapid exploration, while carrying approximation error and scope.

**4. What should a retirement package preserve?** Versions, provenance, use decisions, limitations, key results, and audit records.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 12](../labs/lab-12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[11 — Previous chapter](11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) · End of the book · [Book index](../README.md)

## Step 03 integrated mobility simulation case: sustainment, governance and final defense

### A model is a configuration-controlled operational hypothesis

If a mobility service eventually enters production, its demand, battery behavior, staffing, chargers and accessibility policy will change. An early-fleet sizing model must therefore have an **expiration and recalibration plan**. The [assumptions file](../case/model-assumptions.json) declares synthetic day demand, service and charge distributions. The [credibility record](../case/credibility-register.csv) specifies what needs independent measurement. In sustainment, use controlled telemetry with privacy-respecting aggregation and appropriate authorization; avoid retaining rider identities simply to make simulation easier.

A monitoring design should record by day and scenario: total requests, accessible share, standard and accessible pickup p90, not picked up at close, charger contention, breakdowns, staffing mismatch, demand shift and exceptional events. Statistical process monitoring can detect distribution drift, but a single automated threshold cannot diagnose whether the change comes from data, implementation, operating conditions or real deterioration. Every update should carry a new baseline identifier and re-run the deterministic verification suite; major structural changes require renewed validation, not just new random seeds.

### Reconcile capacity and risk over the lifecycle

A design may have adequate nominal daily throughput yet produce unacceptable tail waits under peaks. A production system introduces new coupled hazards: charger unavailability, maintenance scheduling, pedestrian interactions, operator fatigue, route disruptions and accessibility equipment failures. A defensible lifecycle model connects these variables to decisions about spare fleet, service policies, preventive maintenance and staffing, while keeping unmodeled dependencies visible. A digital twin or live data feed is not automatically more credible; instrumentation and configuration synchronization can introduce new errors and cyber/privacy risks. Advanced approaches—agent-based passenger behavior, network simulation, stochastic optimization or hybrid continuous-discrete energy dynamics—need independent justification proportional to the particular decision.

### Final case finding and reproducibility protocol

The [30-seed baseline and stress results](../case/replication-output.csv) screen the four course candidate fleets. Under the current single-request model, no tested fleet reaches all three synthetic operational targets: 12-minute standard p90, 15-minute accessible p90, and less than 1% awaiting pickup at close. The **best screened candidate is not the same as an acceptable candidate**. The integrated recommendation is **HOLD for pilot readiness; revise the conceptual model, gather referent measurements and explore new feasible configurations**. The result neither rejects the actual Phase 2 concept nor certifies the real fleet.

To reproduce the study from a repository checkout, run `python SE/K/B11/tools/step03_book11_mobility.py`. The command validates JSON assumptions, reconstructs 30 baseline and 30 stress days for each of four fleets with seeds 1000–1029, and writes [the full output CSV](../case/replication-output.csv) and [machine-readable summary](../case/summary.json). Then run `python scripts/check_step03_book11.py` to exercise numerical, negative and publication checks. All inputs and results are fictional; the suite is not a field accreditation parser or standards assessment.

### Defense scenario and worked solution

**Question.** The sponsor says: “Fourteen vehicles are better than twelve, and the 95% interval for their *difference* excludes zero. Approve the procurement.” Provide an engineering response. **Solution.** The paired comparison indicates a repeatable modeled improvement conditional on synthetic demand and the event rules; the 14-vehicle scenario still misses the explicit modeled service constraints and lacks staff, pooled-rides and field validation. Therefore a statistically nonzero *relative improvement* does not establish absolute requirement satisfaction, operational readiness, affordability, accessibility compliance or authority to approve. Propose a controlled alternatives study and pilot evidence plan with explicit owners and gated decisions.

The [course guide](../../../C/P3/EN645757.md) remains the assessment authority; this expanded material supplies worked theory, code and challenge exercises rather than replacing rubrics or independent engineering review.

[Case dossier](../case/INDEX.html) · [Book index](../README.md).
