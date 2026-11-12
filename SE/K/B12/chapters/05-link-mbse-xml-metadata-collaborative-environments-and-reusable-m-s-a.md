# Chapter 05 — Link MBSE, XML metadata, collaborative environments, and reusable M&S assets

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-link-mbse-xml-metadata-collaborative-environments-and-reusable-m-s-a.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w05.md) remains available for a quick recap.

## The decision behind the theory

Advanced simulation is usually developed by multiple disciplines and reused across programs. Without semantic metadata, provenance, review state, tests, and configuration rules, a repository becomes a collection of executable but unsafe artifacts.

**Essential question:** How can another engineer discover, understand, execute, assess, and safely reuse this model?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Define authoritative ownership. The system model may own requirement and interface intent; the simulation repository owns executable source and tests; the data repository owns observations and provenance; the decision record owns the approved use.
* Metadata must support both people and automation: title, purpose, domain, owner, version, tool, dependencies, inputs, outputs, units, interfaces, validity range, tests, evidence, license, security, and known limitations.
* A collaborative environment includes identity/access, configuration, issue/change management, model execution, data services, review workflows, compute resources, and reproducible reporting.
* Reuse is a new use. Reassess intended purpose, operating domain, data, interfaces, fidelity, validation referents, numerical platform, and licensing/security constraints.
* Store review findings and dispositions alongside assets. A green status without the evidence and conditions is not meaningful.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Couple electrical, electromechanical, thermal, and fluid domains**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Design interoperable HLA/FMI federations, LVC interfaces, and composable co-simulations**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Model reuse requires semantic interoperability, not file compatibility

A simulation asset becomes reusable when another engineer can recover what its quantities mean, which assumptions bound it, and how its inputs and outputs correspond to an external model. Exporting an XML file or connecting tools through middleware does not ensure that two teams agree on coordinate frames, units, time origins, or state initialization. A vehicle model reporting velocity in kilometers per hour and a controller expecting meters per second can exchange perfectly valid numbers and still produce a dangerous design error.

Metadata should therefore describe identities, units, reference frames, parameter provenance, validity domains, solver assumptions, and version dependencies. Trace links to a systems model are valuable only if they record whether a parameter was measured, estimated, derived, or chosen for demonstration. Reuse creates an additional governance obligation: when a source model changes, its consumers must know which results may no longer be valid. Interoperability is fundamentally about shared **meaning across independently evolving artifacts**.

## Graduate depth: model exchange as semantic preservation and configuration control

### Moving a model does not automatically preserve its meaning

A digital engineering environment often moves structure and parameter values among SysML repositories, simulation solvers, spreadsheets, XML documents, and collaborative databases. These artifacts may contain syntactically valid information while disagreeing about its engineering meaning. An element named `mass` could describe dry mass, loaded vehicle mass, or a subsystem estimate with different units and configuration baselines. A connection that imports a value is not evidence that the receiving model interpreted the quantity correctly.

Treat exchange as a mapping between typed, versioned representations. A source model may define quantity `q_s` using unit `u_s`, reference frame `f_s`, valid interval `I_s`, and provenance `p_s`. The target quantity `q_t = T(q_s)` is trustworthy only if the transformation `T` preserves the necessary semantics. For physical values, dimensional compatibility and coordinate transformations are essential. For behavioral interfaces, execution order, initialization, event timing, and what constitutes a valid state transition may matter more than field names. XML schema validation can establish permitted document structure; it cannot establish that the engineering concept represented by a field is the right one.

### Traceability is not the same as evidence

A link from a system requirement to a simulation parameter can show where the parameter came from, but it cannot by itself prove that the parameter value is correct or that a simulator is valid for the requirement's intended use. A useful trace includes the claim being supported, a controlled source identifier, units, transformation rule, owner, validity range, and an assurance activity. For example, a battery thermal model might use a maximum allowable temperature from the current component specification, while its convection coefficient comes from calibration tests. Both quantities appear in the same equation but have very different evidentiary status.

One can view the integrated environment as a directed provenance graph. Nodes are requirements, parts, interface definitions, datasets, executable models, and results; edges are typed relations such as *allocated to*, *derived from*, *measured by*, or *computed using*. Change impact analysis traverses only edges whose semantics justify dependency. A parameter-name search misses indirect effects, while declaring every artifact dependent on every other artifact creates an unmanageable false-positive graph. The graph should distinguish a mechanical dependency from an administrative reference and should explicitly identify unresolved connections.

### Configuration and reproducibility in collaborative work

A credible analysis is reproducible with an identified architecture model version, input dataset version, solver configuration, numerical tolerances, library versions, and random seeds where relevant. A model review that captures only the resulting plot cannot reconstruct what was simulated. The reproducibility chain should also record unit conversions and assumptions about initialization; a perfectly archived executable can still yield an invalid decision if it used a stale or ambiguous input.

Imagine Northstar changes from one vehicle battery supplier to another. A shared schema imports nominal energy capacity correctly, but the degradation model still references the old supplier's temperature-dependent performance curve. The digital thread is connected while the engineering inference is invalid. A robust handoff checks interface contracts, meaning, assumptions, numerical units, and representative end-to-end behaviors. The key boundary is that interoperability makes evidence *available* to a decision-maker; only validation and configuration discipline make that evidence fit for a particular decision.

## Worked engineering example from the course

A thermal FMU is cataloged as ‘validated.’ The metadata reveals validation only from 15–30°C, coolant flow above 0.15 kg/s, and a particular battery module. The shuttle winter scenario reaches −15°C and flow can fall to 0.08 kg/s during a pump fault. The reuse assessment marks the asset conditionally reusable for nominal summer studies but unacceptable for the winter fault decision until new evidence is produced.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A model interface must define parameter identifiers, units, versions and ownership. Exporting an XML file is not itself integration; if one model uses Celsius as an absolute temperature and another expects kelvin, a syntactically valid exchange can be physically wrong.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For x˙=−2x, x(0)=1 and Euler step h=0.2, calculate the first two numerical states.

<details><summary>Show a reasoned solution</summary>

x1=1+0.2(−2)=0.6 and x2=0.6+0.2(−1.2)=0.36. The exact states are e^(−0.4)≈0.6703 and e^(−0.8)≈0.4493.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* An executable result cannot be traced to its model, data, and configuration.
* Reuse is approved solely because an asset ran previously.
* Dependencies, licenses, or security constraints are undocumented.
* The repository stores only screenshots or binaries without source/evidence.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an authoritative source?
2. Why is ‘validated’ insufficient metadata?
3. What is a reusable asset package?
4. Why use machine-readable metadata?

<details><summary>Explain the answers</summary>

**1. What is an authoritative source?** The controlled location responsible for a defined class of information.

**2. Why is ‘validated’ insufficient metadata?** Validation is conditional on intended use, domain, referent, and evidence.

**3. What is a reusable asset package?** Source or binary plus metadata, interfaces, dependencies, tests, evidence, limitations, and license/security information.

**4. Why use machine-readable metadata?** To enable automated discovery, validation, reporting, and change impact.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-link-mbse-xml-metadata-collaborative-environments-and-reusable-m-s-a.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-couple-electrical-electromechanical-thermal-and-fluid-domains.md) · [06 — Next chapter](06-design-interoperable-hla-fmi-federations-lvc-interfaces-and-composab.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: governed MBSE and simulation assets

### Separate engineering meaning, file syntax and execution semantics

Model-based systems engineering (MBSE) can express stakeholder needs, architecture blocks, allocation and interface requirements; a numerical simulation specifies state derivatives and step semantics. Exchanging XML or JSON **syntax** between tools does not prove those models share the same **meaning**. The shuttle's `battery_usable_kwh=145` might denote beginning-of-life usable capacity, aged usable capacity or nominal rating. A receiving model that interprets it as joules, or as total nameplate capacity, can produce plausible-looking but incorrect results. A model-asset record must therefore declare at least identifier, version, author/owner, intended use, source provenance, variable definition, unit, validity range, execution assumptions, review status and dependencies.

The controlled [case model JSON](../case/model-inputs.json) is deliberately small enough for a human reviewer to inspect. It fixes the route, physical assumptions, controller gains, sampling ranges and synthetic requirements. The implementation refuses a nonpositive capacity, duplicate route segment identifier, invalid efficiency, impossible scenario flow or out-of-range integration step. **Schema/semantic validation** catches some incorrect inputs before an expensive run; it does not replace calibrated data or an independent model review.

### A workable versioned asset contract

For each source item assign an immutable logical identifier and a concrete revision:

| Asset | Controlled identifier | Consumer | Required invariant |
|---|---|---|---|
| Shuttle plant parameters | `NS-CPS12.1/plant/1.0` | Python integration | SI units, declared ranges, known initialization |
| Route scenario | `NS-CPS12.1/route/1.0` | force/power model | sequence length positive; grade as fraction |
| Requirement `R-THERM` | `NS-CPS12.1/req/thermal/1.0` | result evaluator | maximum °C and declared time horizon |
| Result set | `NS-CPS12.1/results/1.0` | reviewer | input revision, seed, code revision, units |

A revision to `cooling_ua_per_flow_w_per_k_per_kgps` changes model physics and *must* invalidate derived experiment CSV and any previously issued case decision. This is a dependency graph, not merely a filename convention. The source JSON is readable by humans, but real projects should additionally record content hashes and tool/container versions. The [credibility register](../case/credibility-register.csv) records the validity status of each important dependency.

### Derive a reproducible digital thread

Suppose a thermal engineer revises \(UA(\dot m)=35+900\dot m\) to \(UA(\dot m)=35+650\dot m\) W/K. At 0.30 kg/s the modeled transfer coefficient changes from 305 to 230 W/K, **24.6% lower**, so all hot-flow temperature claims are potentially stale. A correct change process identifies the parameter ID, affected equations, requirement R-THERM, test evidence, generated results and decision memo; it then regenerates those results. Merely changing a diagram label while leaving the CSV untouched breaks the evidence chain.

The controlled tool can reconstruct experiment results deterministically with `python SE/K/B12/tools/step03_book12_coupled_vehicle.py --write`. Its use of a fixed pseudorandom seed is sufficient for a **teaching reproduction** on the declared Python runtime. Full formal provenance additionally needs a source commit ID, hashes, platform/solver build, test run and signed review. A notebook screenshot and a model simulation export are not independently reproducible evidence unless the original data and run controls remain available.

### From structured metadata to collaborative review

A minimal interface record can be represented in JSON (or translated to XML), for example:

```json
{"name":"pack_temp","type":"Float64","unit":"degC","causality":"output",
 "source":"thermal_plant","sample_period_s":0.5,"validity":[-20,55],
 "owner":"thermal_model_owner","version":"1.0"}
```

This is *illustrative metadata*, not FMI `modelDescription.xml`, a SysML v2 repository format or a conforming XML schema. The essential properties are **unit, causal ownership, timing and range**; using the word “standard” without conforming to its schema would create a dangerous interoperability claim.

Collaborative teams need a review rule: authors may propose parameter changes; domain owners check physical meaning; integrators check execution and test breakage; decision owners accept intended use. Do not share a mutable “latest-model.json” without a revision record, because readers cannot tell which results belong to which assumptions.

### Exercise and worked answer

**A.** A dataset reports battery capacity as `145000` with no unit. Can it be accepted? **Solution.** No: 145,000 Wh would be 145 kWh, whereas 145,000 kWh is three orders of magnitude different; both are syntactically valid numbers. An automated parser must reject missing units or require a controlled conversion, and a reviewer must confirm “usable” versus “nominal” semantics.

**B.** A researcher changes the warning threshold from 44 to 46°C but not the physical limit. Which downstream artifacts change? **Solution.** Any warning event/alert outputs, requirements trace, potential control-mode transition tests, and final risk memo. If the current code only reports max temperature, its absence of a warning-control implementation must remain explicit; do not imply a controller update occurred.

**C.** A file imports successfully into another tool. Is reuse verified? **Solution.** File parse success checks representation compatibility only; check time semantics, units, physical conservation, supported input range and benchmark outputs at controlled reference points before claiming equivalence.

**Deliverable:** a model-asset catalog with owners/versions and a requirement-to-equation-to-test trace. Include a deliberately malformed parameter file and show that validation rejects it; attach the [reference simulator](../tools/step03_book12_coupled_vehicle.py).
