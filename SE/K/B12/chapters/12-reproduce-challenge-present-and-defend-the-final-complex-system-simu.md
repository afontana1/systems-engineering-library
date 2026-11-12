# Chapter 12 — Reproduce, challenge, present, and defend the final complex-system simulation study

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 12 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 12](../labs/lab-12-reproduce-challenge-present-and-defend-the-final-complex-system-simu.md) → attempt the [original Week 12 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w12.md) remains available for a quick recap.

## The decision behind the theory

The final week turns a technically interesting model into a controlled engineering evidence package. The learner must reproduce the results, respond to a consequential change, and state exactly what lifecycle action the evidence supports.

**Essential question:** Can an independent reviewer reproduce the study, challenge its weakest assumptions, and reach the same bounded conclusion?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Build one final evidence map: decision → requirement/measure → model and interface → input/data → experiment → result → uncertainty/validation → risk → recommendation.
* Reproduction starts from a clean clone or package. Install the documented environment, verify hashes/versions, run tests, execute designated runs, and regenerate figures and reports.
* The live challenge changes one consequential element: battery supplier resistance, coolant-pump degradation, new winter distribution, charger interface delay, route grade error, controller sample time, cost escalation, or requirement threshold.
* The learner must use controlled traces and scripts to identify affected equations, parameters, components, experiments, cost results, evidence, and recommendation. Manual narrative alone does not pass.
* The final use recommendation states accepted configuration, conditions, validity domain, decision supported, authority, confidence/uncertainty, residual risk, non-uses, monitoring, and revisit triggers.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Assess continuous, discrete, hybrid, fixed-step, real-time, HIL, and final credibility constraints**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **the integrated course decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

A defensible complex simulation is reproducible from named model versions, initial conditions, parameter sources and solver settings.

### Distinguishing related ideas

A successful single run establishes neither numerical consistency nor robustness to plausible environmental variation.

### Interpretation and boundary conditions

A final review must separate computational correctness, model adequacy and decision relevance, then state what new evidence would invalidate each.

## Worked engineering example from the course

The baseline recommends the existing cooling loop for PDR because the joint probability of energy reserve and battery-temperature compliance is 0.91. During the defense, pump efficiency is reduced from 0.80 to 0.66 and the charger introduces a 150-ms control-message delay. The trace identifies thermal-fluid parameters, controller rate transitions, HLA/FMI interface timing, winter experiments, battery replacement cost, and five V&V cases. Re-execution lowers joint compliance to 0.73 and creates two timing overruns. The revised recommendation is conditional: qualify the alternate pump and interface timing before design release.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A final simulation recommendation should include model versions, test cases, numerical tolerances, observed data comparisons, factor sensitivity, independent reproducibility and the decision's operating envelope. A captivating visualization is not an evidence chain.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** At constant 12 m/s, deceleration of 2 m/s² gives what ideal stopping distance?

<details><summary>Show a reasoned solution</summary>

d=v²/(2a)=144/4=36 m, excluding delays, grade and friction uncertainty.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: defending a complex simulation as a scientific inference

### Reproducibility is a chain of controlled transformations

A simulation study supports a decision only when its model boundary, configuration, inputs, execution process, and interpretation can be reconstructed. The artifact is more than a program file. It includes the conceptual-model specification, parameter definitions and units, input distributions, random-number streams, solver settings, scenario definitions, warm-up rules, output processing, and decision criterion. Each is capable of changing the recommendation. If a reviewer can rerun the software but cannot recover the evidence behind input choices, the study is computationally repeatable yet scientifically underjustified.

Independent replication is particularly important in stochastic models. Suppose an intervention reduces average wait by 0.3 minutes. If the standard error of the estimated improvement is 0.4 minutes, the direction of the effect is uncertain; claiming decisive improvement is unjustified. Paired scenarios with common random numbers can reduce variance by exposing each alternative to comparable demand realizations, provided the pairing is meaningful. The confidence interval should target the *difference between alternatives*, not merely each standalone mean. A narrow interval around a biased or invalid model is still untrustworthy.

### Separate three sources of error

**Numerical error** arises from discretization, solver tolerance, and implementation. **Statistical error** arises from finite random samples and estimated parameters. **Model-form error** arises because the abstraction omits or misrepresents mechanisms. These errors cannot all be reduced by running more replications. A time-step refinement test may detect numerical instability; repeated independent runs quantify stochastic sampling variation; comparison with field measurements and alternative model structures probes model-form uncertainty. A combined claim must explain which error mechanisms were examined and which remain unbounded.

For Northstar, a vehicle simulation might correctly reproduce route times but omit curbside loading conflicts. More replications reduce Monte Carlo uncertainty while leaving the omitted conflict systematic. A useful challenge case deliberately adds realistic dwell-time variation and measures whether the preferred fleet policy still meets its service threshold. If the policy ranking reverses, the conclusion is sensitive to an omitted operational mechanism, not merely to unlucky simulation seeds.

### Present conditional conclusions, not theatrical certainty

An effective defense begins with the decision and a small number of consequential alternatives. State the operational envelope, acceptability constraints, evidence for key parameters, and uncertainty in the result. Then show at least one counterexample or threshold at which the recommendation would change. This communicates the actual useful range of the simulation. Aggregate scores should not obscure a critical safety, equity, or feasibility constraint.

Version the model source and the exact data used in the reported plots; attach execution instructions and summaries of independent checks. If an assumption changes after review, record whether the change affects only presentation, alters uncertainty, or reverses a decision. A mature final simulation study is **revisable without losing provenance**. Its success is not that its preferred answer survives every question, but that decision-makers can tell precisely what the model demonstrates, where the inference stops, and what evidence would improve it.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A critical result cannot be reproduced from controlled source.
* The final model lacks significant interaction between at least two system types.
* A critical unit, conservation, interface, timing, or validity defect remains unresolved.
* The learner preserves the preferred recommendation after challenge evidence invalidates its conditions.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is the final evidence chain?
2. What must a reproduction log record?
3. Why require a live challenge?
4. Who owns the decision?

<details><summary>Explain the answers</summary>

**1. What is the final evidence chain?** Trace from decision and requirements through models, data, experiments, results, credibility, risk, and recommendation.

**2. What must a reproduction log record?** Environment, versions, commands, inputs, hashes/configuration, tests, runs, outputs, and deviations.

**3. Why require a live challenge?** To demonstrate that the model is usable for change impact rather than only for a rehearsed presentation.

**4. Who owns the decision?** The designated authority; the analyst owns transparent evidence and recommendation.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 12](../labs/lab-12-reproduce-challenge-present-and-defend-the-final-complex-system-simu.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[11 — Previous chapter](11-assess-continuous-discrete-hybrid-fixed-step-real-time-hil-and-final.md) · End of the book · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: final credibility argument and challenge defense

### A claim is only as strong as its weakest relevant evidence link

The final project must answer *which decision, on which model, with which evidence*. Use an assurance-style claim structure rather than presenting attractive graphs. Top-level screening claim: “NS-CPS12.1 can be independently rerun and exposes plausible energy/thermal trends for a bounded synthetic vehicle configuration.” Supporting evidence includes the controlled [inputs](../case/model-inputs.json), reference [program](../tools/step03_book12_coupled_vehicle.py), [per-sample outputs](../case/experiment-results.csv), [summary](../case/summary.json), unit/negative-input checks, conservation residuals and [credibility register](../case/credibility-register.csv). It does **not** follow that the model is validated against real vehicles, conformant with FMI/HLA, thermally safe at the cell level, or appropriate for procurement and operational deployment.

### Three error classes deserve three different reviews

1. **Conceptual/model-form error:** the periodic route has net elevation change, heat transfer is lumped, battery current uses a fixed-bus-voltage proxy, and real boarding, charger sharing and faults are absent. Better integration arithmetic will not cure incorrect abstractions.
2. **Numerical/implementation error:** explicit-Euler step size, grade guard timing, force saturation, unit conversions, parameter parsing and bookkeeping require analytic benchmarks and regression tests. Conservation closure is valuable but not sufficient.
3. **Input/evidence error:** mass/drag bounds and synthetic ambient cases are not statistically calibrated or field-validated; the 16 ranges are design probes, not real-world reliability probabilities.

A defense should separate all three, specify which decision claims each threatens, and propose discriminating measurements. For example, instrumented road dynamometer measurements could assess traction power; a thermal chamber with pack thermocouples could assess gradients and \(UA\); an actual charger session could assess power taper; route topography and time stamps could close the elevation and duty-cycle gaps.

### Reconstruct the important results, then challenge them

The published 24-route-repetition duty cycle covers **84 km** in approximately **155.15 min** in this simplified speed-target model. Across 16 fixed-seed parameter combinations, the mean hot/low-flow battery use is **32.38 kWh**, hot/high-flow **33.36 kWh**, and the mean peak lumped temperatures approximately **41.88°C** and **40.98°C**. All configured synthetic samples meet the model's algebraic reserve, mean route time and lumped thermal screens. However, the route has nonzero net climb per repetition; its 24 repeats are *not* a true closed campus loop. The initial battery temperature is fixed, the example does not model charger sessions, and a deterministic sample pass rate is not a measured probability of system compliance. Therefore **screening calculations reproduced; design qualification HOLD** is the bounded final position.

The most revealing challenge changes structure, not just numbers. Ask: *what happens if the trip returns to the same elevation; the pack starts at 43°C; coolant flow is lost; a braking event occurs on a wet grade; the vehicle is delayed at stops; controller sampling must be 10 ms?* Current results cannot answer many of those questions. That limitation is not a technicality; it is a rationale for a prioritized validation program and additional model states.

### Decision argument table

| Claim | Present evidence | Remaining gap | Responsible next action |
|---|---|---|---|
| Simulated parameter set is repeatable | seed, JSON, CSV, checked code | cross-platform tool-version lock | configuration owner records revision hashes |
| Algebraic electrical/heat bookkeeping is consistent | computed residuals and regression | independent physical circuit/thermal model | electrical/thermal owner builds benchmark |
| Synthetic temperature threshold not exceeded | 16 model draws per scenario | sensor hotspots, hot soak, cooling failures | thermal engineer plans instrumented tests |
| Route trip time meets algebraic screen | model speed integration | boarding, traffic, stop dwell, vehicle interactions | operations engineer measures actual duty cycle |
| Ready for real-time/HIL use | no evidence | WCET, jitter, signal scaling and fail-safe response | controls lead rejects HIL use pending bench tests |

### Independent reproducibility procedure

1. Verify [case model](../case/model-inputs.json) has version `1.0` and is not silently edited.
2. Re-run `python SE/K/B12/tools/step03_book12_coupled_vehicle.py --write` with Python 3; compare deterministic scenario rows and machine-readable summary.
3. Execute `python scripts/check_step03_book12.py` to exercise numerical invariants, negative inputs, all twelve publication representations and provenance checks.
4. Review the full editorial audit and outcome crosswalk. Browser rendering and external FMI/HLA conformance are separate, documented test categories.
5. Write the residual uncertainty, decision boundary, dissenting challenge and condition for reopening the HOLD.

The above is a workflow students can follow; the published scripts must be rerun on the intended local environment rather than assumed successful in every future context.

### Exercises with fully explained solutions

**A.** A presenter claims 80 successful scenario runs prove an operational 100% thermal compliance rate. **Answer.** The 80 runs are deterministic combinations of five synthetic scenarios and 16 bounded parameter draws. They do not sample real deployment exposure, pack hot spots or component faults, and the route is not physical. The correct statement is 80/80 model results satisfy this *one represented lumped-temperature threshold*.

**B.** An independent review reproduces the summary CSV, but field measurements show a 6°C hotspot above the modeled lumped temperature. Pass or HOLD? **Answer.** HOLD for physical qualification. Reproducibility does not override contradictory validation evidence; add spatial thermal states or a defensible hotspot margin, calibrate and rerun tests before re-evaluating.

**C.** Would a conformant FMU alone justify using this model to select a battery supplier? **Answer.** No. FMI conformance establishes interface/execution requirements, not model-form adequacy, empirical calibration or acquisition fitness. The procurement decision needs controlled representative testing, requirements coverage, risk assessment and acceptance authority.

**Final deliverable:** a reproducible evidence package, a worked derivation for each physical domain, sensitivity and adverse-case results, a 12-outcome evidence map, a challenged decision memo and signed review of what evidence would allow the HOLD to be reconsidered. The earlier chapters remain available as independent teaching sources, but the final decision must integrate their limits rather than stack independent “passes.”
