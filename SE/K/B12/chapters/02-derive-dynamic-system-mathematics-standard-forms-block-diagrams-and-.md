# Chapter 02 — Derive dynamic-system mathematics, standard forms, block diagrams, and numerical evidence

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-derive-dynamic-system-mathematics-standard-forms-block-diagrams-and-.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w02.md) remains available for a quick recap.

## The decision behind the theory

A graphical simulation is only as defensible as the equations, state definitions, units, and numerical method beneath it. This week builds a transparent dynamic-model baseline before domain complexity is added.

**Essential question:** How do we know the executable dynamics represent the equations rather than the solver’s artifacts?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Begin with free-body or conservation statements. Define positive directions, reference frames, units, and initial conditions before rearranging equations.
* A transfer function suppresses initial conditions and internal-state meaning; state space retains states and supports multivariable, nonlinear, and control analyses.
* Block diagrams expose causality chosen by the modeler. Acausal equation-based tools solve the equation set and often make multi-domain reuse easier, but they do not eliminate modeling assumptions.
* Numerical verification needs more than a successful run. Compare step sizes, solver families, tolerances, energy or mass balance, event handling, and independent calculations.
* Store a solver decision record with dynamics, stiffness evidence, accuracy target, runtime, and real-time implications.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Frame the advanced M&S decision, intended use, architecture, and credibility strategy**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Model translational and rotational mechanical dynamics with realistic losses and constraints**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## A deeper explanation: equations, states, and simulation are not the same thing

### Dynamics begin with what can accumulate

The first conceptual choice in dynamic modeling is not the numerical solver; it is the **state**. A state variable contains information about the system's past that is needed to predict its future once the inputs are known. Position and velocity are states of a moving vehicle because its future motion cannot generally be predicted from position alone. A battery's state of charge is a state because energy is accumulated. In a queue, the number of waiting requests can be a state because it records the accumulated difference between arrivals and completions.

This is why conservation laws are such powerful starting points. For stored quantity \(x\), a basic balance is

\[
\frac{dx}{dt}=\text{inflow}-\text{outflow}+\text{generation}-\text{consumption}.
\]

The equation is not merely a convenient algebraic pattern. It says what can change the stored quantity and imposes discipline on units and boundaries. For a battery energy model, power must integrate to energy; for a population or queue model, flow rates must integrate to counts. If the units do not reconcile, the proposed mechanism is already suspect.

### Differential equations embody causal assumptions

Consider a vehicle speed model \(m\dot v=F(u)-bv\), where \(m\) is effective mass, \(F(u)\) is commanded tractive force, and \(bv\) approximates speed-dependent resistance. The equation encodes several assumptions: motion is one-dimensional; mass is treated as constant; resistance is linear; and the controller changes force through the specified input. Those assumptions are not consequences of calculus. They are *modeling decisions* made before solving the equation.

If \(F\) is constant, speed approaches \(F/b\), with time scale \(m/b\). This tells us what the model predicts about settling and sensitivity before a single simulation is run. Doubling mass slows the response; increasing resistance reduces both the time scale and equilibrium speed. The analytical structure gives physical intuition that an isolated time plot cannot provide. At low speed or during wheel slip the linear-resistance model may be inappropriate, which is a limitation of the model, not the numerical integrator.

### State-space and transfer-function viewpoints answer different questions

State-space models expose how internal states evolve: \(\dot x=Ax+Bu\), \(y=Cx+Du\) for a linear time-invariant approximation. They make initial conditions, internal coupling, controllability, and observability visible. A transfer function instead captures the input-output relation under the assumptions used to construct it, often including zero initial conditions. Both can be correct, but neither is a complete physical description. A transfer function that accurately predicts speed response may say little about battery temperature if that state is omitted.

The same distinction matters in multi-domain simulations. A shuttle's mechanical, electrical, and thermal states are linked: motor power affects torque and heat; temperature influences component limits; limits change available acceleration and route feasibility. Solving each subsystem in isolation and passing values between them can conceal feedback or create numerical artifacts at coupling boundaries. A coupled formulation reveals those dependencies but increases stiffness, computational cost, and sensitivity to uncertain parameters.

### Numerical solutions are approximations to a mathematical model

For \(\dot x=-kx\), forward Euler gives \(x_{n+1}=x_n(1-kh)\), where \(h\) is the time step. The exact physical idealization decays smoothly for \(k>0\). Euler's approximation instead behaves according to the multiplier \(1-kh\). It is stable for \(0<kh<2\), can alternate in sign for \(1<kh<2\), and grows artificially when \(kh>2\). A plot showing growing oscillation may therefore be evidence of **solver instability**, not a property of the proposed design.

This leads to three separate questions. **Model formulation:** Does the equation represent the intended phenomenon? **Numerical verification:** Does the implemented solver approximate that equation with sufficient accuracy? **Empirical validation:** Does the equation, even when solved accurately, predict the relevant real-world observations? Better time-step convergence answers the second question. It cannot by itself answer the third.

### Events change the structure of the mathematics

Engineering systems rarely remain in one smooth operating regime. A battery controller may reduce power above a temperature threshold. A shuttle may transition from moving to stopped at a safety event. A queue may become empty and prevent further departures until an arrival occurs. These events change constraints or equations and may create discontinuities. A fixed-step simulation can step over such an event, using an invalid equation longer than intended.

Hybrid modeling requires discrete state logic alongside continuous dynamics, with carefully defined event detection, reset rules, and ordering. The essential conceptual insight is that **the semantics of a state transition are part of the model**, not merely a code implementation detail.

A credible dynamic model therefore has a transparent chain: physical or operational mechanism → state definition → governing equations → operating modes → numerical method → comparison with evidence → bounded claims. Understanding that chain is more valuable than memorizing the menu of solvers in a software package.

### Dynamic equations follow from state, conservation, and constitutive laws

A dynamic model needs state variables whose present values, together with the inputs, determine how the system can evolve. Conservation laws constrain quantities that cannot appear or disappear without a flow: charge, mass, energy, or inventory. Constitutive laws then specify relationships such as resistive loss, motor torque, heat transfer, or service capacity. The differential equations are a compact expression of those mechanisms, not merely a curve-fitting exercise.

A numerical solver replaces continuous change with finite computational steps. That approximation adds a separate source of error whose behavior depends on the algorithm and time step. A stable physical system can appear unstable under a poorly chosen explicit integration step; conversely, a solver can suppress behavior of interest through excessive numerical damping. Distinguish **physical instability**, **model-structure error**, **parameter uncertainty**, and **numerical instability**. Convergence checks and analytical limiting cases address different parts of that chain and are essential before interpreting a simulated transient as an engineering finding.

## Graduate depth: numerical dynamics, stability, and identifiability

### Governing equations and the meaning of state

A dynamic model is usually a differential or differential-algebraic relationship, not merely a connected set of blocks. In a state-space representation, `dx/dt = f(x,u,p,t)` and `y = g(x,u,p,t)`, the state `x` contains variables whose values carry the system's memory; `u` is an externally imposed input; `p` contains parameters; and `y` is the measured or decision-relevant output. A useful test of a proposed state is this: given the current state and future inputs, can the model calculate future behavior without requiring a hidden history? Position and velocity are states for a moving vehicle because knowing position alone cannot determine its immediate future position.

Start from physical balances before selecting a solver. For a lumped thermal mass, conservation of energy yields `C*dT/dt = Q_in - h*A*(T-T_ambient)`, with heat capacity `C` in joules per kelvin and `h*A` in watts per kelvin. The characteristic time constant is `tau = C/(h*A)`. That ratio reveals why a high-capacity mass responds slowly and provides a scale for numerical step selection. It also reveals a structural limitation: if the object has large internal temperature gradients, one lumped temperature can no longer represent it adequately. A smaller time step cannot repair an inadequate physical model.

### Stability is not the same as accuracy

For the scalar decay equation `dx/dt = -a*x`, forward Euler gives `x_(k+1) = (1-a*h)*x_k`. With `a>0`, the numerical solution decays stably only when `0 < a*h < 2`; monotone decay requires the tighter range `0 < a*h <= 1`. A true physical system can therefore be stable while a poor integration step produces oscillation or divergence. An implicit Euler step has factor `1/(1+a*h)` and is stable for any positive step, but may still suppress important fast transients. Solver stability prevents one class of numerical defect; it does not establish physical fidelity.

A system may contain both slow thermal modes and fast electrical modes. Their time scales can differ by orders of magnitude, creating *stiffness*. Explicit schemes then need extremely small steps for stability even if the decision only concerns slow behavior. An implicit or specialized stiff solver may be appropriate, but discontinuous control logic and zero-crossing events still need careful treatment. Treating a relay switch as a smooth derivative for convenience can create behavior that the actual controller cannot exhibit.

### Observability, estimation, and evidence

A model also has an inverse problem: can its states and parameters be determined from available measurements? For a linear system `dx/dt = A*x+B*u`, `y = C*x`, observability concerns whether the measurements over time distinguish different initial states. Parameter identifiability is related but different: two parameter combinations can produce nearly identical outputs, so calibration alone may not reveal which physical mechanism is responsible. For example, a temperature curve may constrain the ratio `C/(h*A)` well while failing to identify `C` and `h*A` separately. Additional measurements or input excitations are needed.

In Northstar's fictional electrical-thermal subsystem, a calibrated motor temperature curve could hide an incorrect heat-transfer coefficient offset by an incorrect effective thermal mass. Predicting temperature during a new duty cycle may then be unreliable despite excellent fit to the calibration experiment. A defensible workflow checks conservation, units, steady-state limits, numerical convergence under step refinement, sensitivity to uncertain parameters, and agreement with independent transient data. A solver's small error estimate refers to the integration problem it was given; it is not a certificate that the engineering system has been represented correctly.

## Worked engineering example from the course

For a first-order battery thermal lump, C dT/dt = Q_in − hA(T−T_amb), the analytic step response provides a referent. With C=420 kJ/K, hA=0.9 kW/K, and a 12-kW heat step, the time constant is 466.7 s and the steady rise is 13.3 K. A coarse explicit fixed step of 120 s produces visible phase and amplitude error; 10 s and a variable-step solver agree within the 0.2 K acceptance tolerance. The regression test checks steady state, time constant, monotonicity, and energy balance.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

For m x¨ + c x˙ + k x = F(t), let m=1000 kg, c=400 Ns/m and k=20,000 N/m. Natural angular frequency is √(k/m)=√20≈4.47 rad/s; damping ratio c/(2√(km))≈0.0447. A low damping ratio predicts oscillation; the equation is not just notation.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** At constant 12 m/s, deceleration of 2 m/s² gives what ideal stopping distance?

<details><summary>Show a reasoned solution</summary>

d=v²/(2a)=144/4=36 m, excluding delays, grade and friction uncertainty.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* A critical equation has inconsistent units or sign conventions.
* The model is accepted because it produces a plausible plot.
* Solver settings or initial conditions are undocumented.
* Tool-to-tool agreement is claimed as validation of the physical system.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a state?
2. Why compare step sizes?
3. When is a transfer function insufficient?
4. What is a limiting-case test?

<details><summary>Explain the answers</summary>

**1. What is a state?** The minimum information needed with future inputs to determine future system behavior.

**2. Why compare step sizes?** To estimate numerical convergence and detect discretization-driven conclusions.

**3. When is a transfer function insufficient?** For nonlinear, multivariable, mode-dependent, or initial-condition-sensitive behavior.

**4. What is a limiting-case test?** A test at a parameter limit where behavior is known or simplifies.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-derive-dynamic-system-mathematics-standard-forms-block-diagrams-and-.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-frame-the-advanced-m-s-decision-intended-use-architecture-and-credib.md) · [03 — Next chapter](03-model-translational-and-rotational-mechanical-dynamics-with-realisti.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: dynamic equations, state and solver evidence

### Build a state vector from storage mechanisms

A genuine dynamic model must state *what can retain memory*. For the coupled shuttle let \(x=(s,v,E,T_b)\) be route distance in metres, vehicle speed in m/s, remaining usable battery energy in joules, and lumped pack temperature in kelvin (differences numerically equal °C differences). Inputs \(u\) include reference speed, road grade, ambient temperature and coolant flow; algebraic outputs are wheel power, battery current and losses. The continuous plant is a set of ODEs, while the route-segment and cooling-mode selectors are discrete guards. With \(F_t\) traction force and \(F_r\) total road load,

\[
\dot s=v,\quad \dot v=\frac{F_t-F_r}{m},\quad
\dot E=-P_\mathrm{battery},\quad
C_b\dot T_b=Q_\mathrm{gen}-UA(T_b-T_a).
\]

Writing \(E\) in joules produces the clean derivative \(-P\) in watts; the downloadable program reports kWh and explicitly divides joules by 3,600,000. Avoid the common silent error of integrating watts over seconds and labeling the result kWh. A block diagram is a computational arrangement, whereas the ODEs supply the physical meaning and the traceable assumptions. A transfer function is valid only for an appropriate *linear time-invariant* subsystem around a stated operating point; route guards and saturation prevent a global LTI transfer function for the full shuttle.

### Derive and verify an analytical reference before trusting a time-step result

For constant applied force \(F_0\), lumped linear resistance \(kv\), and constant mass, the test equation \(m\dot v=F_0-kv\) has

\[
v(t)=\frac{F_0}{k}\bigl(1-e^{-kt/m}\bigr),\quad v(0)=0,
\qquad \tau=m/k.
\]

Choose \(m=3100\,\mathrm{kg}\), \(k=100\,\mathrm{N\,s/m}\), \(F_0=900\,\mathrm N\). The steady speed is 9 m/s and \(\tau=31\) s. At 10 s the exact speed is \(9(1-e^{-10/31})\approx2.48\) m/s. Forward Euler updates \(v_{n+1}=v_n+h(F_0-kv_n)/m\); with \(h=2\) s and five updates it gives approximately 2.55 m/s. Reproduce at 1 s and 0.5 s; an error decreasing with step size provides evidence of solver implementation but not physical validation.

For a scalar decay \(\dot y=-\lambda y\), Euler's amplification is \(g=1-h\lambda\). Stability requires \(|g|<1\), or \(0<h\lambda<2\); low numerical error generally requires a much smaller step. At a discontinuous grade or control-mode switch, verify event ordering and shorten the step even if the smooth system is stable. A step size inherited from a 10 ms controller is **not** proof that the complete multi-domain model satisfies real-time constraints.

### Derive the coupled energy and thermal states explicitly

The code takes motor wheel power \(P_w=F_tv\) and uses efficiencies \(\eta_m=0.91\), \(\eta_r=0.69\): battery traction power is \(P_w/\eta_m\) during propulsion and \(\eta_rP_w\) during regeneration (negative charging sign). Auxiliary power \(P_a\) and internal ohmic loss \(I^2R\), with the simplified current proxy \(I=(P_\mathrm{traction}+P_a)/650\), are added to battery energy depletion. Internal heat is \(I^2R+0.22P_a\). The model records electrical, mechanical and thermal balance residuals; those residuals should be near zero *within the model equations*, but they cannot prove the assumed efficiency/heat model is correct.

### Reproduce a numerical convergence and invariance experiment

Run `python SE/K/B12/tools/step03_book12_coupled_vehicle.py --laps 1 --dt 1` and compare `--dt 0.5` and `--dt 0.25`. Define relative metric change \(\delta(h)=|M(h)-M(h/2)|/\max(|M(h/2)|,\epsilon)\). Report the actual \(M\) and \(\delta\), not just “stable.” For an energy accounting check use

\[
\epsilon_E=E_\mathrm{used}-\frac{W_\mathrm{traction,batt}+W_\mathrm{aux}+Q_\mathrm{ohmic}}{3.6\times10^6}\quad [\mathrm{kWh}].
\]

The report's \(\epsilon_E\) is algebraically tiny by construction. Separately test the *mechanical* balance against change in kinetic and potential energy plus road dissipation; it is more sensitive to the numerical step and grade boundary. The implementation is an explicit-Euler educational demonstration; it does not solve DAEs, stiff electrochemical states or HIL transport timing.

### Exercises with explained answers

**A.** Which state disappears if battery temperature is assumed fixed? **Answer.** \(T_b\) becomes a parameter, and the thermal first-order differential equation and its initial-condition dependence disappear; a fixed-temperature electrical efficiency result can no longer support a thermal-limit claim.

**B.** At the above LTI reference point, estimate how long a speed step takes to reach 63.2% of steady velocity. **Answer.** \(\tau=31\) s, because \(1-e^{-1}\approx0.632\). This is not the shuttle's actual acceleration time: actuator force, grade, aerodynamic drag and mode changes have been suppressed.

**C.** A solver returns a nearly zero energy residual yet incorrect travel times. Explain. **Answer.** Consistent power accounting can coexist with an incorrect controller gain, speed target, event guard or tire force; invariants test internal consistency, not external truth. Record solver refinement, analytic benchmark and independent measurement as separate evidence classes.

**Deliverable:** analytical benchmark, step-size table, balance-residual table and a claim-by-claim numerical verification memo linked to [source and inputs](../case/INDEX.html).
