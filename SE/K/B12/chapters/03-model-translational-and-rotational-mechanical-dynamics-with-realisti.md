# Chapter 03 — Model translational and rotational mechanical dynamics with realistic losses and constraints

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-model-translational-and-rotational-mechanical-dynamics-with-realisti.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w03.md) remains available for a quick recap.

## The decision behind the theory

Mechanical models are often deceptively simple. Tire radius, inertias, gear ratios, grade, drag, friction, saturation, and coordinate conventions can create large errors or hidden energy sources.

**Essential question:** Does the mechanical model conserve energy and produce credible force, torque, speed, and distance behavior across the operating envelope?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Use one reference direction and record all sign conventions. Distinguish vehicle speed, wheel speed, motor speed, and slip.
* Reflect rotating inertias carefully. A gear ratio changes speed, torque, and apparent inertia; inconsistent conventions can produce order-of-magnitude error.
* Check instantaneous power across each ideal interface. With losses, the output power must not exceed input power.
* Model saturation and constraints explicitly: maximum motor torque, tire-road traction, braking limits, and speed limits.
* Calibration is not validation. Estimate drag and rolling resistance from one synthetic coast-down set, then evaluate on a separate route profile.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Derive dynamic-system mathematics, standard forms, block diagrams, and numerical evidence**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Couple electrical, electromechanical, thermal, and fluid domains**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Mechanical dynamics follow from state variables and balance laws, with constitutive models specifying friction, drag, compliance and actuator response.

### Distinguishing related ideas

A kinematic trajectory gives motion without explaining forces; a dynamic model predicts how forces and control inputs change motion.

### Interpretation and boundary conditions

Parameter uncertainty matters most near physical limits where small changes in traction or mass can reverse feasibility.

## Deeper theory: mechanics as constrained energy exchange

### Choose generalized coordinates before choosing a solver

A dynamic mechanical model begins with physical degrees of freedom and constraints, not with block-diagram convenience. For a vehicle on a grade, longitudinal position `s` and wheel angle `φ` might initially appear independent. Under ideal rolling without slip, `ds/dt = r dφ/dt`, where `r` is the effective tire radius; the constraint removes one degree of freedom. If traction limits or braking slip matter, that constraint is no longer exact, and longitudinal tire slip must become an explicit state or constitutive relation. A model that enforces perfect rolling cannot predict wheel lock, however finely its equations are integrated.

Choose sign conventions consistently. Let forward be positive, road grade angle be `α`, and tractive force be `F_t`. One simplified force balance is `m dv/dt = F_t − mg sin(α) − c_r mg cos(α) sign(v) − (1/2)ρ_a C_D A v|v|`. Here aerodynamic drag scales approximately with speed squared and acts opposite motion; rolling loss is more complicated near zero speed than a raw sign function suggests. Each term carries a distinct physical assumption. The effective longitudinal inertia may include rotational components such as `J_w/r²` when wheel inertias are represented through the rolling constraint. Ignoring that inertia can make simulated acceleration and braking physically optimistic.

### Power flow exposes hidden contradictions

A gearbox transforms speed and torque: ideally `ω_out = ω_in/G` and `τ_out = G τ_in`; for positive motoring with efficiency `η`, the output mechanical power is `P_out = η P_in`. Efficiency is not generally the same in regenerative braking, at low power, or under temperature limits. A lossless gear block with a torque multiplier but no corresponding speed reduction creates energy from nowhere. Across a drivetrain, a useful accounting identity is `ΔE_stored = E_supplied − E_dissipated − E_exported`, with consistent boundaries. Potential energy `mgh`, translational kinetic energy `mv²/2`, rotational kinetic energy `Jω²/2`, and battery energy should agree with the modeled work and heat flows.

For a 1,600 kg hypothetical shuttle increasing speed from 0 to 10 m/s on level ground, translational kinetic energy increases by 80 kJ before rolling, aerodynamic, wheel-inertia, and conversion losses. A propulsion model reporting 50 kJ drawn from storage for that acceleration with no other energy source violates the balance. Conversely, regenerative braking cannot return the entire kinetic energy if tire, inverter, battery, and friction-brake losses exist. Check energy residuals over complete drive cycles; a residual that drifts with time may indicate a numerical or modeling defect even if the velocity trace looks plausible.

### Friction, saturation, and contact change the equation class

A simple viscous friction law `F = −bv` is smooth but does not capture stiction, breakaway, or tire-road saturation. Coulomb friction may require set-valued behavior at zero speed; braking force also cannot exceed what the tire-road contact can transmit under the assumed surface conditions. Motor torque limits depend on speed and thermal state, often producing a torque-limited region followed by a power-limited region. Saturation makes the combined system piecewise nonlinear. Controls tuned against an unbounded torque source may demand impossible deceleration when passengers most need predictable stopping distances.

Contact and constraints can create algebraic relationships alongside differential states. Introducing compliance regularizes some numerical problems but also creates artificial stiffness and energy storage. If a rigid-body solver and electrical drive solver exchange torque and speed at coarse steps, each can use stale values and violate power consistency. Choosing a small numerical step helps only within the implemented equations; it cannot correct a physically incorrect force law or unsuitable operating boundary.

### Identification and uncertainty connect the model to evidence

Mass, drag area, rolling resistance, gearing, and friction are not all equally identifiable from one acceleration run. Several parameter combinations can fit the same speed trace, especially without elevation, power, and braking measurements. Structural identifiability asks whether ideal data could distinguish parameters; practical identifiability asks whether available noisy measurements do so. Correlated estimates should be propagated together. The strongest mechanical argument combines dimensional checks, limiting cases, conservation residuals, calibrated observations from different maneuvers, and explicit claims about where the model should not be trusted. For Northstar, a level-road fit is not evidence of safe stopping behavior on a wet grade.

## Worked engineering example from the course

A 2,850-kg shuttle climbs a 6% grade at 12 m/s. Grade force is approximately 1,676 N; rolling resistance at coefficient 0.010 adds about 280 N; aerodynamic drag with drag area 1.9 m² and air density 1.2 kg/m³ adds about 164 N. Required wheel power before acceleration is roughly 25.4 kW. A model that reports 18 kW has a sign, gear, or loss defect. A separate energy integral over the hill is used to check mechanical work against elevation gain and losses.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A vehicle moving at 12 m/s that decelerates at constant 2 m/s² stops in t=v/a=6 s and ideal distance d=v²/(2a)=36 m. Rolling resistance, road grade, controller delay and traction limits require extra margins.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For x˙=−2x, x(0)=1 and Euler step h=0.2, calculate the first two numerical states.

<details><summary>Show a reasoned solution</summary>

x1=1+0.2(−2)=0.6 and x2=0.6+0.2(−1.2)=0.36. The exact states are e^(−0.4)≈0.6703 and e^(−0.8)≈0.4493.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Power is created across an interface without explanation.
* Gear or reference-frame conventions are ambiguous.
* Calibration data are reused as sole validation evidence.
* Traction, torque, or braking constraints are ignored when they affect the decision.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Why check both force and energy?
2. What is reflected inertia?
3. How should grade be modeled?
4. Why use holdout data?

<details><summary>Explain the answers</summary>

**1. Why check both force and energy?** They detect different defects: instantaneous balance versus integrated work.

**2. What is reflected inertia?** Rotational inertia transformed through a gear ratio to an equivalent inertia at another shaft.

**3. How should grade be modeled?** As the gravitational force component along the route with a controlled sign convention.

**4. Why use holdout data?** To evaluate predictive behavior beyond calibration.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-model-translational-and-rotational-mechanical-dynamics-with-realisti.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-derive-dynamic-system-mathematics-standard-forms-block-diagrams-and-.md) · [04 — Next chapter](04-couple-electrical-electromechanical-thermal-and-fluid-domains.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: force, torque, work and mechanical limits

### From generalized coordinates to wheel tractive effort

Treat the shuttle as a point mass moving longitudinally on a prescribed route, with wheel radius \(r=0.39\) m. At road speed \(v\), a rolling wheel rotates at \(\omega=v/r\) under a **no-slip assumption**. Let the route grade be the small slope fraction \(g_r\), rather than angle radians. For moderate grades, \(\sin\theta\approx g_r\) and \(\cos\theta\approx1\). The required motor contact force for longitudinal acceleration \(a\) is

\[
F_t=ma+mgC_{rr}+mg g_r+\tfrac12\rho C_dA v^2,
\qquad P_w=F_tv,\quad \tau_\mathrm{wheel}=F_tr.
\]

These terms have different physical origins: mass times acceleration is change in kinetic energy; rolling losses dissipate energy; grade moves gravitational potential; aerodynamic drag grows quadratically with speed. They must not be merged into a generic “efficiency factor” when studying hill duty cycles. The motor shaft torque is not identical to wheel torque unless gear ratio and transmission losses have been accounted for; the toy model uses only contact wheel force.

### Numerical calculation on the controlled route

With the controlled curb mass \(m_c=2850\) kg and synthetic passenger payload of 300 kg, the modeled moving mass is **3150 kg**. The route uses the source guide's curb-mass baseline while taking payload as one declared operating scenario; a full study would vary payload by stop and verify axle loads.

At \(v=10\) m/s, \(C_{rr}=0.010\), \(g_r=0.06\), \(\rho=1.225\) kg/m³ and \(C_dA=1.9\) m², the baseline road forces are **309.02 N** rolling, **1854.09 N** grade and **116.38 N** drag. The constant-speed contact force is **2279.48 N**, with wheel power **22.79 kW**. Contact torque is approximately **889 N·m** and wheel speed \(\omega=25.64\) rad/s. The motoring battery traction requirement at 91% assumed efficiency is **25.05 kW** before cabin load, pump and ohmic losses. A 1000 m 6% climb requires approximately \(m g \Delta h=3150(9.81)(60)=1.85\) MJ of elevation energy even without drag or rolling resistance.

### Conservation checks that expose hidden defects

Integrated force balance is \(\Delta K=\int(F_t-F_r)v\,dt\), with \(K=mv^2/2\). If grade is separated from dissipative resistance, \(\int P_w dt=\Delta K+\Delta U_g+W_{rr}+W_d\). The case tool records a mechanical residual. When comparing exact continuous force balance with discretized positions, error should diminish under step refinement. Negative wheel power is regenerative in the toy model only up to a specified 65 kW; actual electric vehicles also have pack charging, traction-control, temperature and slip constraints which are omitted.

Abrupt speed targets at route boundaries are idealizations. Real stops need jerk and adhesion limits; wheel spin, lock-up, steering and road curvature invalidate the longitudinal no-slip assumption. A model that exactly closes its energy balance can still be **unsafe** if its stopping distance is not represented.

### Constrained power and feasibility

The controller requests \(a_\mathrm{req}=\mathrm{clip}(k_v(v_\mathrm{ref}-v),-1.25,0.9)\) m/s² with \(k_v=0.45\,s^{-1}\). The required force is constrained by \(|P_w|\le180\) kW in propulsion and \(P_w\ge-65\) kW in regeneration, implemented with a low-speed force proxy. When the requested force exceeds the available limit, actual \(a=(F_t-F_r)/m\) departs from target. The controller is a heuristic, not a motor/inverter torque-speed map. Label results as *regulated traction proxy* rather than controller qualification.

### Guided calculation and sensitivity

Suppose the grade of the 900 m second segment is doubled from 6% to 12% (outside the case's declared validated input band; the code disallows grades above 10% in its source route). Ignoring motor saturation, additional climb energy is \(mg(0.06)(900)=1.67\) MJ, or 0.464 kWh at the wheel; at 91% efficiency it is roughly 0.509 kWh extra electrical draw. The numerical experiment instead permits a bounded **grade multiplier up to 1.5**, not arbitrary data outside its validator. This is why an extrapolated analytic calculation and a configured simulator output serve different purposes.

### Exercises and worked solutions

**A.** If wheel radius is increased 1.5% while required contact force is fixed, what happens to contact torque? **Answer.** \(\tau=Fr\) increases by 1.5%. At equal road speed the wheel angular rate decreases by about \(1/1.015-1=-1.48\%\); wheel power \(Fv\) stays constant in this ideal no-slip representation. Real drivetrain gearing may change efficiency.

**B.** At 10 m/s, change aerodynamic drag area from 1.9 to 2.2 m². Find incremental drag force. **Answer.** \(\Delta F=0.5(1.225)(0.3)(100)=18.375\) N; additional wheel power is 183.75 W. At higher speed the \(v^3\) power dependence makes the same area change much more consequential.

**C.** Why is a downhill segment not guaranteed to replenish all climbing energy? **Answer.** Rolling and aerodynamic losses dissipate work, the regenerative efficiency is below unity, battery charging may be restricted, and terminal kinetic energy matters. An idealized symmetric elevation profile is not energy-neutral.

**Deliverable:** a dimensioned free-body diagram, a force/work audit for a route segment, and an adverse friction or power-limit test against the [baseline model](../case/INDEX.html).
