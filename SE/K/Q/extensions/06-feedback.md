## Step 04 integrated case — NS-QSE4.1: control, discretization and false stability

The battery thermal exercise in Chapter 5 is a plant model. Feedback can be introduced without adding a black-box controller. Define the deviation \(x=T-T_{\rm ref}\), and imagine the thermal plant is linearized near an equilibrium with unforced decay \(\dot x=-a x\). A proportional cooling action \(u=Kx\) for \(x>0\) yields \(\dot x=-(a+K)x\) only **while the actuator is unsaturated and the cooling sign is appropriate**. Here \(a\) and \(K\) both have units \(\mathrm h^{-1}\). The continuous-time eigenvalue is \(-a-K\), stable for \(a+K>0\). This conclusion refers to the local linear model, not to every operating regime of a real battery.

### A numerical controller can destabilize a stable continuous system

For Euler with sample period \(h\), \(x_{k+1}=[1-h(a+K)]x_k\). Define the amplification multiplier \(m=1-h(a+K)\). Discrete asymptotic stability requires \(|m|<1\); zero error is reached in one step when \(m=0\). Taking \(a=0.4\ \mathrm h^{-1}\), \(K=1.6\ \mathrm h^{-1}\):

- At \(h=0.25\) h, \(m=1-0.25(2)=0.5\): the idealized deviation halves at each sample.
- At \(h=1\) h, \(m=1-1(2)=-1\): error alternates in sign at unchanged magnitude. It is **marginal, not asymptotically stable**.
- At \(h=1.25\) h, \(m=-1.5\): the linear numerical recursion diverges.

These are **sampled-controller/numerical-map results**. They must not be represented as physically observed instability. If the controller is actually digital with a zero-order hold and continuous plant, the exact sampled-data mapping differs from Euler's approximation. Derive that mapping before specifying a real sampling interval.

### Why actuator constraints and delayed measurements change the model

A realistic cooling command is bounded: \(u_k=\operatorname{clip}(Kx_k,0,u_{\max})\), with \(u_{\max}\) in temperature-rate units. Below the reference, the simple rule requests no cooling; above saturation it cannot deliver the linearized gain. Introduce a one-step sensor delay and the recurrence may become \(x_{k+1}=(1-ah)x_k-hKx_{k-1}\). Its characteristic equation is \(r^2-(1-ah)r+hK=0\). Stability now depends on *both* roots lying inside the unit circle, not on the one-state multiplier alone. Controller performance can deteriorate if cooling power drains vehicle energy needed for emergency service. Safety limits and operator authority are separate acceptance conditions.

### Designed verification and validation experiments

A verification experiment should compare numerical state trajectories with the exact unforced plant solution and should explicitly test \(h=0.25\), \(h=1\), and an unstable theoretical step. A validation experiment needs separately measured sensor errors, actuator saturation, varying heat input, and delayed telemetry. A fault-injection test might force cooling unavailable during the compound dispatch condition. Until those measurements exist, no controller gain or sampling rate is approved.

<details><summary>Worked exercises and interpretation</summary>

1. **Stability bound.** Solve \(-1<1-h(a+K)<1\), giving \(0<h<2/(a+K)\). At \(a+K=2\ \mathrm h^{-1}\), the strict stable range is \(0<h<1\ \mathrm h\).
2. **Finite recursion.** With \(x_0=8\ ^\circ\mathrm C\) and \(m=0.5\), successive deviations are 4, 2, 1°C. With \(m=-1\), they are -8, +8, -8°C: bounded oscillation does not imply convergence.
3. **Actuator limit.** Why can an unconstrained linear stability proof fail during grid outage? The cooling actuator may saturate or lose power; its assumed linear feedback coefficient is then not delivered, even though the algebra is correct.

</details>

The same distinction between local linear dynamics, software timing, and operational qualification applies to Book 12 cyber-physical integration and Book 13 system dynamics.
