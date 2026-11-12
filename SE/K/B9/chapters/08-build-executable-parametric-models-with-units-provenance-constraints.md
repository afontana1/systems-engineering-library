# Chapter 08 — Build executable parametric models with units, provenance, constraints, and linked analytics

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 8 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 8](../labs/lab-08-build-executable-parametric-models-with-units-provenance-constraints.md) → attempt the [original Week 8 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w08.md) remains available for a quick recap.

## The decision behind the theory

The integrated model now contains properties and thresholds, but it cannot yet calculate whether candidate architectures meet them. **Essential question:** How can the model execute or invoke quantitative relationships without losing units, provenance, uncertainty, or reproducibility?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Choose analyses based on decisions and requirements, not because a parametric diagram is available. Define the question, output measure, alternatives, uncertainty, and acceptance use first.

Use value types and units consistently. Celsius/Kelvin offsets, percentages, rates, currency years, coordinate frames, and time bases require explicit semantics beyond a unit label.

Keep simple governing equations and their bindings visible in the model. Use external notebooks or services for data cleaning, statistical fitting, optimization, large simulation, or methods that need stronger testing and libraries.

Treat external analyses as controlled model elements: owner, version, input schema, output schema, assumptions, environment, verification tests, run ID, result ID, and applicability.

Verification should include independent hand cases, dimensional analysis, boundary/extreme cases, monotonicity, regression tests, and comparison with an independent implementation where consequence warrants.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Elicit, derive, validate, and query system requirements from the integrated analysis**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Explore the trade space with alternatives, uncertainty, sensitivity, and model-based decision records**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Executable parametrics are constraints with provenance

A parametric diagram can connect quantities symbolically, but executable analysis requires dimensional consistency, parameter meaning, and assumptions. An expression for fleet energy demand needs units, operating duration, vehicle count, duty cycle, usable capacity, and reserve definition. Without those, a number reported to three decimal places may represent an incoherent mixture of physical quantities.

Parametrics are especially valuable at change boundaries. A new duty cycle should propagate through energy, charging, thermal, cost, and availability constraints. But automatic recomputation does not validate the inputs or the structure. Each parameter requires provenance and an operating domain. The analyst should test conservation, extreme values, and sensitivity, then distinguish modeled feasibility from observed performance. Model execution makes assumptions inspectable; it does not make the assumptions true.

## Deeper theory: executable parametrics connect algebra to engineering authority

### Constraints are meaningful only with units and boundaries

An executable parametric model can capture relations such as `energy = power × duration` or `requiredStorage ≥ missionEnergy/reserveFactor`, but mathematical executability does not ensure physical truth. Every value needs units, source, validity conditions, and a configuration to which it applies. A quantity recorded as 15 without specifying kilowatts or kilowatt-hours can silently invalidate an energy budget. Dimensional consistency detects some errors, yet a dimensionally correct relation can still be causally wrong—especially when it omits efficiencies, transient loads, or environment.

The model must also distinguish parameters supplied from evidence from parameters inferred by solving constraints. An equation `P = VI` cannot determine voltage and current independently when only power is known. This is an identifiability issue, not a solver defect. Additional constraints may eliminate a family of mathematically possible solutions, but those constraints must come from justified physics or design choices. A solver returning one number from underdetermined information can conceal arbitrary defaults.

### Sensitivity and uncertainty are different operations

A local sensitivity such as `∂E/∂P = t` for `E=Pt` describes how output changes with input near a reference point while other quantities are held fixed. It does not reveal how uncertain power actually is, whether power and duration covary, or whether the model form itself is credible. A first-order variance approximation uses derivatives and the input covariance matrix; it can fail for nonlinear thresholds, strong skewness, discontinuous modes, or large uncertainty. Monte Carlo methods can help but are only as good as the model and input distribution.

Consider an electrical demand model based on nominal operation. If emergency heating is activated only below a threshold temperature, a smooth average-power approximation can miss the branch that governs minimum reserve. An executable model should represent distinct modes or bounded conditions and make it impossible to present a nominal estimate as a worst-case proof. Sensitivity checks should include limiting cases, dimensional checks, and scenario changes tied to the mission rather than arbitrary parameter sweeps.

### Provenance turns a calculation into reviewable evidence

A model result should identify the requirement it evaluates, upstream parameter versions, solver method, assumptions, units, configuration, and execution record. If the mass budget changes after a battery supplier update, reviewers need to know whether the change propagated to braking, energy, and structural calculations. Recomputing one result without tracing dependent constraints creates a visually updated but inconsistent baseline.

Parametric equations should also be verified against independently calculated examples and challenged with invalid inputs. An executable model can produce exact-looking results with incorrect property mappings, sign conventions, or conversions. In the Northstar case, the model earns credibility when an engineer can explain each relation, reproduce its output, test where it fails, and show how a changed assumption affects the decision. Automation increases consistency only when semantic control keeps pace with computational convenience.

## Worked engineering example from the course

The learner models usable energy, route distance, energy intensity, cold multiplier, reserve fraction, charger power, charging efficiency, vehicle count, and availability. A unit-aware Python function calculates daily energy margin and charging demand. The first run shows a 19% discrepancy with the in-tool model because the notebook treats charger power in watts while the model exports kilowatts. A schema and Pint unit check prevent recurrence. Boundary tests cover zero demand, maximum cold multiplier, one failed charger, and inaccessible vehicle removal.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An energy budget has E_required = distance × energy_per_km + idle_hours × auxiliary_power. For 86 km, 0.72 kWh/km, 3 h idle, and 1.8 kW auxiliary, E_required = 67.32 kWh. If usable storage is 64 kWh the modeled design lacks energy margin. Keep all quantities with units and parameter provenance.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A consequential equation uses untyped or inconsistent units.
* External analysis inputs are manually copied without provenance or synchronization control.
* A result is accepted because two implementations share the same untested logic.
* The analysis has no trace to a decision, requirement, measure, or configuration.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a value type?
2. What is a binding?
3. Why use an external analytic model?
4. What is dimensional analysis?

<details><summary>Explain the answers</summary>

**1. What is a value type?** A reusable definition of value semantics such as dimension, unit, quantity kind, constraints, and representation.

**2. What is a binding?** A relationship asserting equality or connection among constraint parameters and model properties.

**3. Why use an external analytic model?** It may provide stronger numerical, statistical, optimization, testing, data, or performance capability while the system model preserves context and traceability.

**4. What is dimensional analysis?** Checking that equations and results are consistent in physical dimensions and units.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 8](../labs/lab-08-build-executable-parametric-models-with-units-provenance-constraints.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[07 — Previous chapter](07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md) · [09 — Next chapter](09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md) · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — executable parametrics and dimensional assurance

### Bind physical quantities to controlled assumptions

For a candidate with \(N\) vehicles, mean cycle \(T_c\) minutes, and per-vehicle daily energy \(e\), the teaching model calculates

\[
\mu=\frac{60N}{T_c}\ \mathrm{trips/hour},\qquad E_d=Ne\ \mathrm{kWh/day}.
\]

For \(C\) chargers, charging power \(P\) kW, window \(t\) hours and efficiency \(\eta\), the simple gross energy-recovery bound is

\[
E_{rec}=CPt\eta\ \mathrm{kWh},\qquad M=E_{rec}-E_d.
\]

Variant B uses \(N=12\), \(T_c=48\) min, \(e=20\) kWh/day, \(C=4\), \(P=30\) kW, \(t=2.5\) h and \(\eta=0.90\). Thus \(\mu=15\) trips/h, \(E_d=240\) kWh/day, \(E_{rec}=270\) kWh and \(M=30\) kWh. The [editable model](../case/model.json) and [executable checker](../tools/step03_book9_model_check.py) use those same inputs.

### Recalculate after a change rather than reusing a green icon

The supplier changes the assumed charger to **27 kW at 82% efficiency**. Under otherwise unchanged assumptions, \(E_{rec}=4(27)(2.5)(0.82)=221.4\) kWh, so \(M=-18.6\) kWh. Adding a fifth charger would give \(5(27)(2.5)(0.82)=276.75\) kWh and a **36.75-kWh** nominal margin. However, the fifth unit is only a *design alternative*: no electrical integration, footprint, safety or acquisition evidence has been collected. Read this as an energy-screening calculation, not a charging-infrastructure approval.

### Check units, structural validity and validity range

`kW × h` yields kWh. Replacing hours with minutes without dividing by 60 creates an exact-looking 60× error. The equation also assumes steady charger power, unrestricted battery acceptance, available connectors, a complete charging window and aggregate energy fungibility. Real vehicles may have different charge states or taper curves. A robust parametric audit includes dimension checking, input domain checks, limiting cases, monotonicity, and a second independently computed estimate; the checker rejects nonpositive cycle times and efficiencies outside `(0,1]`.

**Exercise.** How long would four changed chargers need, at fixed 27 kW and 82% efficiency, to deliver 240 kWh?

<details><summary>Worked answer</summary>

\(t=240/[4(27)(0.82)]\approx2.710\) hours. It exceeds the 2.5-hour window by roughly 12.6 minutes, making the unchanged four-charger configuration infeasible under the assumed operating schedule. Real charge taper would require a more detailed model.

</details>
