# Feedback, stability and system dynamics

*Textbook-depth conceptual sequence · EN.645.781 / EN.645.758 / EN.645.784 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 13](../../B13/OPEN-BOOK.html), [Book 12](../../B12/OPEN-BOOK.html), [Book 14](../../B14/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## Why feedback changes the object of study

A static spreadsheet describes relationships at one moment; a feedback system describes how actions change the environment that drives later actions. In Northstar, adding vehicles can reduce waits, attract more demand, increase maintenance load, and eventually create shortages again. Whether that loop reinforces or balances itself depends on delays, gains, nonlinear constraints and decision rules. The word "feedback" is not itself a model. A useful model specifies causal variables, their units, state accumulation and the timing of information.

Distinguish reinforcing loops, which amplify a change, from balancing loops, which oppose a departure from a target. A causal-loop diagram is useful for hypothesis building but cannot establish the magnitude or stability of the dynamics. To simulate, identify stocks (vehicles available, backlog, trust, cash), flows (repairs, new trips, cancellations, expenditure) and algebraic relationships. A stock-flow diagram that sums rates with incompatible units is not executable science.

## A proportional controller in continuous time

Suppose \(e=r-y\) is the difference between desired backlog target r and measured backlog y. An idealized first-order plant has \(\dot y=-ay+bu\), where \(a,b>0\), and a proportional controller uses \(u=K(r-y)\). Substitution gives \(\dot y=-(a+bK)y+bKr\). For constant target, its closed-loop pole is \(-(a+bK)\), stable in this simplified model when \(a+bK>0\). The equilibrium is \(y^*=bKr/(a+bK)\), which does not generally equal r: proportional control can have steady-state error. Integral action may address that error but can worsen overshoot or windup under actuator constraints.

For a sampled controller using forward Euler with step h, deviations from equilibrium evolve as \(\delta y_{n+1}=[1-h(a+bK)]\delta y_n\). Even if the continuous system is stable, the discrete approximation is stable only if \(0<h(a+bK)<2\). With \(a=0.4,b=1,K=1.6\), the effective decay rate is 2/hour; a one-hour Euler update gives factor −1 (marginal numerical oscillation), while a quarter-hour step gives factor 0.5. A poor numerical implementation can mimic bad controller behavior.

## Delays and hidden state

In operations, decisions use information that is already old when the action arrives. A controller acting on a delayed measurement can overcorrect. For example, if vehicle availability reports lag by 20 minutes, the dispatcher may assign additional work to vehicles already occupied. Increasing gain to respond faster can destabilize the coordination loop. Modeling delay requires explicit history or delay states, not merely multiplying a control signal by a small factor. Saturation, hysteresis and deadbands matter because resources cannot vary continuously over all real values.

Control quality is more than stability. A stable system may converge slowly, settle at a biased target, violate a transient safety constraint, or require impossible control effort. Assess step response, overshoot, settling time, steady-state error, disturbance rejection, actuator saturation, and robustness to uncertainty. For safety-related service systems, include hard limits and graceful degradation independently of performance optimization.

## Feedback in organizations

The same logic applies at enterprise scale with different evidence limits. A management rule that allocates more staff when incidents rise can reduce incidents after a delay. If performance is evaluated sooner than the effect can appear, managers may repeatedly over-hire or cancel the intervention prematurely. Policy resistance occurs when stakeholders adapt incentives or behavior to an intervention, altering the system structure. These social models are hypotheses requiring interviews, historical evidence, and sensitivity analysis, not deterministic forecasts of human behavior.

Good system-dynamics work separates: (1) an observed pattern, (2) a candidate feedback explanation, (3) a quantified stock-flow model, (4) evidence testing alternatives, and (5) a policy robustness comparison. A single plausible loop diagram can support conversation but not an operational promise.

## Design a defensible control experiment

Set a demand shock that increases arrivals from 8 to 12 per hour at a fixed time. Evaluate one low-gain and one high-gain response with identical demand streams and identical charging limits. Record backlog over time, peak delay, missed service, control effort, and vehicle overuse. Then introduce a sensor delay and an actuator cap. If the high-gain strategy performs well only without delay or limits, the experiment has revealed a narrow validity domain rather than a universally better controller.


## Further depth: root locations, saturation and integrator windup

For a continuous linearized system \(\dot{\boldsymbol{x}}=A\boldsymbol{x}\), asymptotic stability under the ordinary linear time-invariant assumptions requires every eigenvalue of A to have negative real part. For a discrete update \(\boldsymbol{x}_{k+1}=A_d\boldsymbol{x}_k\), eigenvalues must lie strictly inside the unit circle. These criteria are about **local linearized behavior** when the real system is nonlinear. They do not guarantee acceptable transients, global stability, or safety under actuator limits.

A proportional-integral controller accumulates the error \(z(t)=\int_0^t(r-y)dt\) and sets \(u=K_p(r-y)+K_i z\). Under output saturation, the requested control can exceed the allowable actuator. If the integral term continues growing while saturated, the controller may overshoot badly after the limit is released. Anti-windup logic limits or back-calculates the integrator state. In a transport scheduling application, the analogous problem is repeatedly accumulating unmet "vehicles requested" when no additional vehicles exist. A policy must acknowledge real capacities rather than allow an unbounded virtual response.

Delay is especially important in feedback loops with long observation cycles. A management policy that allocates budget each quarter while staffing changes require six months can create alternating overreaction. The analyst should measure information latency and physical response latency separately. Test robustness across these delays and under plausible demand disturbances. A high-performance nominal controller may be an unreliable real-world policy if it requires unrealistic sensor timeliness.

### Quantitative sensitivity

For the simple closed-loop pole \(-(a+bK)\), changing gain K directly changes ideal convergence rate. Yet in the discrete Euler approximation the stable step h must shrink as \(a+bK\) increases. This is why numerical step selection, sensing cadence and control gain cannot be tuned independently. Distinguish a *discrete controller* derived from sampling theory from a *continuous controller numerically approximated* by Euler; the two have different design contracts.

## Problems — attempt first

1. Derive the closed-loop pole for \(\dot y=-ay+bu\) with \(u=K(r-y)\).
2. For \(a=0.4,b=1,K=1.6\), find the stable Euler step-size interval.
3. Why can a high-gain controller be undesirable despite faster nominal response?
4. Name a reinforcing and balancing feedback hypothesis in a transport service; state a measurement that could challenge each.

<details><summary>Worked answers and engineering interpretation</summary>

1. Substitution gives \(\dot y=-(a+bK)y+bKr\) and pole \(-(a+bK)\).
2. \(a+bK=2\). Stability requires \(0<2h<2\), hence \(0<h<1\) hour; h=1 is marginal for Euler.
3. Delays, saturation, noise amplification, oscillation and control effort can become unacceptable.
4. Reinforcing: improved service attracts more demand (measure post-improvement request rates). Balancing: maintenance prioritization reduces unavailable vehicles (measure lagged repair completions and fleet availability). Each is a hypothesis, not an observed fact until tested.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/06-feedback.html) · [Download editable Markdown lab](../labs/06-feedback.md) · [Open the associated notebook](../notebooks/06-feedback.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)

<!-- STEP04-QUANTITATIVE-START -->
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
<!-- STEP04-QUANTITATIVE-END -->
