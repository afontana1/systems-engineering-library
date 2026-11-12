# Coupled multi-domain physical models

**Reference entry · Dynamic systems, multiphysics modeling, and simulation**

## Why coupled models differ from stacked diagrams

Electromechanical systems exchange energy between domains. An electrical current produces torque; shaft velocity produces back electromotive force; resistive power becomes heat; temperature may change resistance or torque capability. Modeling each discipline in isolation misses feedback and constraints. The model must preserve dimensional consistency, identify state variables, and specify which approximation is valid over the intended operational envelope.

Consider a hypothetical motor driving an auxiliary actuator. Its minimal *lumped, linearized* state model is

\[
L\dot i=V-Ri-k_e\omega,\qquad
J\dot\omega=k_ti-b\omega-\tau_L,\qquad
C_T\dot T=i^2R-h(T-T_a).
\]

Here \(i\) is current (A), \(V\) voltage (V), \(L\) inductance (H), \(R\) resistance (Ω), \(\omega\) angular speed (rad/s), \(J\) inertia (kg m²), \(b\) viscous drag (N m s/rad), \(\tau_L\) load torque (N m), \(C_T\) effective thermal capacity (J/K), and \(h\) heat-transfer conductance (W/K). In coherent SI units, \(k_t\) and \(k_e\) are related for an idealized energy-conserving motor, but do not assume their numerical identity under arbitrary unit conventions or with gear/transmission losses.

## Worked steady-state constraint

Choose illustrative \(R=2\ \Omega\), \(k_e=0.10\ \mathrm{V\,s/rad}\), \(k_t=0.10\ \mathrm{N\,m/A}\), \(b=0.01\ \mathrm{N\,m\,s/rad}\), \(\tau_L=0.20\ \mathrm{N\,m}\) and \(h=4\ \mathrm{W/K}\). At \(i=4\ \mathrm A\) and \(\omega=20\ \mathrm{rad/s}\), mechanical balance holds because \(0.10(4)=0.01(20)+0.20\). Electrical balance requires \(V=2(4)+0.10(20)=10\ \mathrm V\). Resistive loss is \(i^2R=32\ \mathrm W\), giving a predicted steady temperature rise \(T-T_a=32/4=8\ \mathrm K\).

This is a **point solution**, not a dynamic verification. At higher supply voltage the operating point moves and heat rises quadratically with current. A thermal limit may be violated even when average torque requirements are met. If actuator load depends on pressure or flow, introduce a fluid-state model and explicit coupling (e.g. hydraulic power \(pQ\)), plus conversion efficiencies. Never connect quantities merely because they have the same symbol.

## Simulation and numerical credibility

A forward Euler step for a state \(x\) is \(x_{n+1}=x_n+\Delta t f(x_n,u_n)\). For the isolated electrical subsystem its characteristic time constant is \(\tau_e=L/R\); an integration step comparable to this time scale may be inaccurate or unstable. Report timestep convergence using at least two refined steps and compare against an analytic or independent benchmark. For coupled or stiff systems, implicit integration or an appropriate multirate solver may be necessary.

**Interface contract:** state variable, unit, sign convention, update/communication rate, frame of reference, solver responsibility, event ordering, initialization, parameter version, and acceptable extrapolation range. A logical SysML connection does not, by itself, establish numerical compatibility.

## Exercise with check

A reviewer incorrectly writes thermal generation as \(iR\). Explain why this cannot be watts: amperes times ohms yields volts, whereas \(i^2R\) yields watts. If current increases from 4 to 5 A while \(R,h\) remain fixed, the steady temperature rise becomes \(25(2)/4=12.5\ \mathrm K\), a **56.25%** increase from 8 K, not 25%. Identify why constant \(R\) becomes questionable at elevated winding temperature.

## Assumptions and sources

The motor uses constant parameters, one thermal node, no saturation, no contact friction, no mechanical compliance and constant ambient temperature. Real actuators require geometry, environmental, material and qualification data. Related: [parametric models](parametric-models-and-units.md), [model credibility](model-vv-and-credibility.md), [stocks and flows](stocks-flows-feedback.md).

- [Modelica Association FMI 3.0 specification](https://fmi-standard.org/docs/3.0/) — model exchange and co-simulation interface contracts.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — system analysis, requirements and validation.

*Scope:* Illustrative equations and numbers; not an experimentally calibrated motor or certified multiphysics model.
