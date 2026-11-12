# Chapter 04 — Couple electrical, electromechanical, thermal, and fluid domains

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-couple-electrical-electromechanical-thermal-and-fluid-domains.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w04.md) remains available for a quick recap.

## The decision behind the theory

The final project must contain significant interaction between system types. This week creates that interaction and tests whether energy, causality, units, and numerical behavior remain coherent across domain boundaries.

**Essential question:** Can the integrated physical model exchange power, heat, and mass without hidden inconsistency or unstable coupling?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Use power-conjugate variables: voltage/current, torque/angular velocity, force/velocity, pressure/volume flow, and temperature/entropy or heat flow as appropriate.
* Choose battery fidelity based on decision: ideal source, equivalent circuit, state-of-charge, temperature-dependent resistance, and degradation are different model claims.
* Thermal lumps require explicit capacitance, heat generation, conduction/convection paths, and boundary conditions. Fluid models require pressure, flow, resistance, pump behavior, and storage/compressibility assumptions.
* Cross-domain verification includes total energy accounting: chemical/electrical input equals mechanical work, stored energy change, thermal loss, and residual numerical error within tolerance.
* Acausal tools simplify physical connection but can create high-index algebraic systems. Causal tools make computation order visible but may force artificial signal direction.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Model translational and rotational mechanical dynamics with realistic losses and constraints**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Link MBSE, XML metadata, collaborative environments, and reusable M&S assets**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Coupled electromechanical and thermal behavior emerges because energy transfers across domains with losses and delayed state changes.

### Distinguishing related ideas

Treating battery energy, motor torque and temperature as independent budgets can predict impossible simultaneous performance.

### Interpretation and boundary conditions

An integration model must respect units, power conservation and heat accumulation even when individual subsystem solvers appear correct.

## Deeper theory: multi-domain models are systems of conserved quantities

Mechanical, electrical, thermal, and fluid systems are often taught as unrelated equation sets. A useful systems-engineering perspective is that their interactions are organized by a small number of physical principles: conservation, constitutive relations, energy transfer, and boundary conditions. A component model is not credible merely because its equations run. Its variables must describe a coherent physical state, and its interconnections must transfer conserved quantities consistently.

### Energy provides a common language across domains

For a vehicle climbing a grade, mechanical power delivered at the wheels is approximately \(P_m=Fv\). An electrical traction system draws battery power \(P_e\), part of which becomes mechanical work and part heat. In an idealized model with efficiency \(\eta\), \(P_m=\eta P_e\), but \(\eta\) may depend on motor speed, torque, temperature, and control strategy. The heat generation term is not an arbitrary tuning parameter: in a simplified energy budget it is \(P_{\mathrm{loss}}=P_e-P_m\). If the electrical and thermal submodels each count the same loss independently, the integrated simulation violates conservation despite the independent subsystems appearing plausible.

A lumped thermal state can be modeled by

\[C_T\frac{dT}{dt}=P_{\mathrm{loss}}-hA(T-T_a),\]

where \(C_T\) is effective thermal capacitance, \(hA\) is the effective heat-transfer conductance, and \(T_a\) is ambient temperature. The model shows the interplay between energy conversion and temperature: high motor load raises losses; rising temperature may reduce permissible torque; the vehicle controller may limit acceleration; that limitation can increase trip time. A multi-domain model is valuable because such coupled consequences are invisible when disciplines supply only independent point estimates.

### State variables and algebraic constraints

A state variable records information needed to predict future evolution under specified inputs. Battery state of charge, vehicle velocity, and motor temperature are plausible states. Current in a resistive branch may instead be determined algebraically from voltage and resistance, depending on the electrical model. Coupled models often therefore have both differential equations and algebraic constraints, forming a **differential-algebraic equation (DAE)** system. Treating every quantity as an independently integrated state introduces artificial dynamics; imposing conflicting algebraic constraints can make the system unsolvable.

Dimensional analysis offers a first defense. A heat balance equates power terms, all measured in watts, to a thermal-capacity term measured in joules per kelvin times kelvins per second. A structural model may connect variables with the right names but wrong units—for instance, watt-hours to joules or angular speed in revolutions per minute to radians per second. Successful numerical integration cannot rescue a physically inconsistent equation.

### Energy storage and dissipative elements shape dynamics

The difference between storage and dissipation is central. A mass stores kinetic energy \(\tfrac12 mv^2\); an ideal inductor stores magnetic energy \(\tfrac12 Li^2\); a thermal capacitance stores internal energy relative to a reference state. Friction, electrical resistance, and heat transfer dissipate or redistribute energy. The placement of storage elements determines the number and character of dynamic states. Coupling a fast electrical transient to a slow thermal response creates multiple time scales, which can make a numerical model stiff.

Stiffness is not simply a system that changes quickly. It occurs when numerical stability is constrained by fast modes even though the engineering quantity of interest may evolve slowly. An explicit fixed-step method may need a very small step to remain stable, whereas an appropriate implicit solver can often advance the slow dynamics efficiently. Choosing a solver is a modeling decision linked to the model's eigenvalues and algebraic structure, not merely a software preference.

### Boundary assumptions are where models break

Suppose a drive-train model assumes an unlimited cooling supply and a thermal model assumes constant motor efficiency. Each may pass local unit tests, yet their composition can conceal an overheating limit. The combined system needs an explicit contract for what crosses the boundary: power, torque, temperature, mass flow, and state-dependent constraints. When a battery-management controller suddenly curtails power, the thermal and mechanical states should evolve consistently through the event. Events that change equations or constraints may require hybrid-system treatment and careful event localization.

A useful physical credibility test is a **closed energy ledger** over a defined interval: starting stored energy plus supplied energy minus delivered work, exported heat, and final stored energy should balance within a stated numerical tolerance. Such a ledger does not by itself prove all mechanisms are correct, but it is a stronger claim than “the graphs look reasonable.” Multi-domain engineering becomes rigorous when every coupling has a physical meaning and the integrated model respects the conservation properties of the system it represents.

## Worked engineering example from the course

The motor draws 70 kW electrical and delivers 63 kW mechanical at 90% efficiency, creating 7 kW heat. Battery internal resistance adds 3 kW heat. The coolant loop removes 8 kW while the battery thermal mass absorbs 2 kW, closing the instantaneous thermal balance. An initial integrated model accidentally subtracts motor loss from battery heat and reports falling temperature under high load. The energy audit identifies the sign defect immediately.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An electric heater drawing 2 kW for 30 minutes adds 1 kWh thermal/electrical transfer before efficiency losses. In a battery/thermal model, energy is conserved across electrical, mechanical and thermal ports; inconsistent sign conventions produce fictitious energy.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** At constant 12 m/s, deceleration of 2 m/s² gives what ideal stopping distance?

<details><summary>Show a reasoned solution</summary>

d=v²/(2a)=144/4=36 m, excluding delays, grade and friction uncertainty.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Energy, heat, or mass residual exceeds tolerance without disposition.
* Interface units or ownership are implicit.
* Initialization produces a hidden nonphysical transient used in results.
* A domain is included cosmetically without significant interaction or decision relevance.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a conserving interface?
2. Why record energy residual?
3. What is an algebraic loop?
4. When is a simple battery model acceptable?

<details><summary>Explain the answers</summary>

**1. What is a conserving interface?** An interface whose across/through variables enforce the relevant conservation law.

**2. Why record energy residual?** To detect signs, missing losses, inconsistent components, and numerical drift.

**3. What is an algebraic loop?** A set of instantaneous dependencies requiring simultaneous solution.

**4. When is a simple battery model acceptable?** When its omitted dynamics cannot change the intended decision within required accuracy.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-couple-electrical-electromechanical-thermal-and-fluid-domains.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-model-translational-and-rotational-mechanical-dynamics-with-realisti.md) · [05 — Next chapter](05-link-mbse-xml-metadata-collaborative-environments-and-reusable-m-s-a.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: close the electrical and thermal power balance

### Power ports, storage and losses

A coupled model is physically accountable when each domain states what enters, leaves, dissipates and accumulates. For motoring, wheel power is \(P_w>0\), battery-side traction power is \(P_w/0.91\); during regen \(P_w<0\), stored electrical credit is \(0.69P_w\). That piecewise relation is an **assumed efficiency map**, not a full converter and motor circuit. Add cabin heating/cooling and a flow-dependent coolant pump. With approximate bus voltage \(V=650\) V, current proxy \(I=(P_{\mathrm{traction}}+P_{\mathrm{aux}})/V\), cell-resistance parameter \(R=0.115\,\Omega\), battery energy obeys

\[
\dot E=-(P_\mathrm{traction}+P_\mathrm{aux}+I^2R).
\]

The extra \(I^2R\) is **subtracted** from stored energy so Joule heating cannot appear from nowhere. The proxy is not an algebraically self-consistent battery terminal-voltage model under load; a physically derived internal-resistance circuit would solve terminal voltage and current together. At high current the approximation may be inaccurate, and must not be used to size fuses or conductors.

### Thermal and coolant flow coupling

For a single lumped pack temperature \(T_b\), the simplified first law is

\[
C_b\frac{dT_b}{dt}=I^2R+\alpha P_{\mathrm{aux}}-UA(\dot m)(T_b-T_a),
\quad UA(\dot m)=35+900\dot m\ \mathrm{W/K},
\]

where \(C_b=860{,}000\) J/K, \(\alpha=0.22\), and coolant mass flow \(\dot m\) is kg/s in the specified 0.05–0.35 range. The separate pump surrogate is \(P_{\mathrm{pump}}=100+14{,}000\dot m^3\) W. The \(UA\) relation bundles exchanger effectiveness and flow rather than resolving coolant temperature or fluid hydraulics: it is not a CFD model. For \(T_b=42^\circ C\), \(T_a=38^\circ C\), low flow 0.05 yields \(UA=80\) W/K and cooling 320 W; 0.30 yields \(UA=305\) W/K and 1220 W. The pump requires approximately 102 W versus 478 W. More cooling can raise electrical demand.

At fixed \(UA\) and constant heat input \(Q\), the exact thermal response is \(T(t)=T_a+Q/UA+(T_0-T_a-Q/UA)e^{-UA t/C_b}\). The time constants are \(860000/80=10750\) s (low flow) and \(860000/305\approx2820\) s (high flow). Compare these to the synthetic duty cycle, not only a single instantaneous temperature. The thermal-model initial state is 31°C for *all* weather scenarios; this may underrepresent a hot-soaked vehicle, so the first-pass result cannot bound true peak temperatures.

### Worked coupled trade-off from reproducible experiments

Across the case's 16 synthetic parameter draws and 24 repeated route cycles (84 km), hot low-flow produces mean peak modeled pack temperature **41.88°C** and mean battery use about **32.38 kWh**. Hot high-flow produces about **40.98°C** and **33.36 kWh**, respectively. Thus increasing coolant flow reduces the toy peak by roughly **0.90°C** but costs approximately **0.98 kWh** over the route repetition set. These are model-specific parameter effects, not observed efficacy or an optimal cooling policy. The summary is machine-readable in [summary.json](../case/summary.json); every raw paired row is in [experiment-results.csv](../case/experiment-results.csv).

### Interface and solver contract

Power ports are in W with positive consumption; energy storage is kWh in the implementation but J in the ODE; temperature differences are K, temperatures are reported °C; coolant flow is kg/s. A component exchange must say whether supplied power includes internal losses to prevent double counting. When combining a 10 ms controller, 0.5 s Euler plant and slower thermal dynamics, specify sample-and-hold and event timestamp semantics. Failure to do so creates time-alignment artifacts that masquerade as physical damping.

### Exercises with explained solutions

**A.** Given \(P_{\mathrm{traction}}=30\) kW and \(P_{\mathrm{aux}}=4\) kW, compute the current proxy and ohmic heat. **Solution.** \(I=34000/650\approx52.31\) A, hence \(I^2R\approx315\) W. This is thermal input and battery depletion in the simplified model. A measured bus voltage is needed to refine the estimate.

**B.** A reviewer integrates 1 kW for 30 minutes and writes “30 kWh.” **Solution.** Correct energy is \(1\times0.5=0.5\) kWh; time must be converted to hours. Audit all conversion boundaries.

**C.** If ambient exceeds battery temperature, what does \(UA(T_b-T_a)\) mean? **Solution.** It becomes **negative cooling**, i.e., net heat transfer *into* the pack. Clamping it to zero would violate the model's heat balance and suppress hot-soak behavior.

**Deliverable:** an electrical/thermal boundary ledger with signs and units, a high/low-flow paired comparison, and a list of physical measurements required to replace every surrogate.
