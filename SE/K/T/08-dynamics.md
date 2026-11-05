# Stocks, feedback, controls, and numerical stability

*Core Concepts · Quantitative methods · T08*

> Connect feedback-loop stories to reproducible models with units and stability conditions.

**Recommended preparation:** [Queueing, congestion, and discrete-event simulation](07-queues.md)

**Related course companions:** [Book 12](../B12/OPEN-BOOK.html), [Book 13](../B13/OPEN-BOOK.html), [Book 6](../B6/OPEN-BOOK.html)

## 1. Feedback is a causal loop with delay
Consider a regional fleet operator trying to reduce passenger wait. Longer waits lead managers to add vehicles; added vehicles reduce waits. This is a balancing loop, but procurement delay and changing demand can produce overshoot. Conversely, long waits may cause passengers to abandon the service, reducing measured demand and deceptively improving the wait metric. A causal-loop diagram is a hypothesis about influence, not proof of the net system dynamics.

Make the loop quantitative. A **stock** accumulates: queued demand, available battery energy, trained staff, or unresolved engineering changes. A **flow** changes the stock over time. Conservation gives \(\frac{dQ}{dt}=\lambda(t)-s(t)\) when \(Q>0\), with a nonnegativity constraint at the boundary and explicit handling of rejections and abandonment. Units must match: requests/hour cannot be added to requests without multiplying by a time step.

## 2. A feedback policy can oscillate
Suppose an operator increases fleet supply in proportion to queue error: \(u(t)=k(Q(t)-Q^*)\). Larger gain \(k\) responds faster in a simplified model, but delays, discrete vehicle counts, minimum service times, and actuator constraints can make aggressive control unstable. The correct controller must include realistic saturation and timing; “more responsive” is not automatically “safer.”

In a linear first-order recovery model \(\dot x=-kx\), the exact solution is \(x(t)=x(0)e^{-kt}\) for \(k>0\). Forward Euler gives \(x_{n+1}=(1-k\Delta t)x_n\), which is numerically stable only if \(|1-k\Delta t|<1\), or \(0<k\Delta t<2\). A simulator may appear to oscillate solely because the time step is too large.

## 3. Calibration and validation answer different questions
Calibration estimates unknown parameters from data; validation asks whether the model predicts the behavior that matters for a specified use. Fitting a training trajectory perfectly does not validate a policy counterfactual. A useful protocol reserves scenarios for out-of-sample assessment and tests extreme but plausible conditions.

Look for dimensionless ratios. If repair time is long relative to failure interval, backlog behaves differently than if recovery is fast. If controller delay is comparable to the characteristic response time, naive proportional tuning may fail. Ratios generalize across systems better than one calibrated numerical case.

## 4. Never confuse a policy model with a policy mandate
A model of staffing, traffic, or public service behavior has political and organizational boundaries. Include stakeholders who experience side effects, and examine whether the metric rewards shifting burden onto other groups. Feedback models are aids to structured argument, not substitutes for accountable policy choice.

## 5. Test stability, not just numerical plausibility
A numerical simulation should not be trusted merely because it returns smooth curves. Perform a time-step refinement study: solve with \(\Delta t\), then halve it, and compare outputs relevant to the decision. If the answer changes materially, discretization error is too large or the model contains a discontinuity that needs careful treatment. This is part of numerical verification, distinct from validating the physical or organizational model.

For a simple stock-flow queue, enforce the nonnegative stock constraint with an explicit event or projection method. Do not casually let numerical integration create negative passengers. If abandonment occurs, add a flow with units of requests/hour and a behavior model; do not hide abandoned requests by adjusting the arrival rate after the fact.

When analyzing feedback, identify time constants and delays. A controller that adjusts staffing every hour cannot instantly fix a demand peak lasting ten minutes. Conversely, overreacting to short-term noise can create cycling staffing and unstable costs. Measurement delay, actuation delay, and smoothing policies are part of the system dynamics.

**Check your reasoning:** A simulated controller oscillates with a five-hour step but converges with a half-hour step. That is evidence of a numerical problem or interaction with sampled control, not proof that the real system oscillates. Investigate the discretization before drawing policy conclusions.

## Guided worked example

### Worked numerical check
With \(k=0.5\ \mathrm{h}^{-1}\), \(x_0=10\), and \(\Delta t=1\ \mathrm h\), one Euler step yields \(x_1=5\); the exact value is \(10e^{-0.5}\approx6.065\). The discretization error is approximately 1.065. With \(\Delta t=5\) hours, \(1-k\Delta t=-1.5\), so repeated Euler steps oscillate and grow even though the continuous system decays. Numerical instability is not a physical prediction.

## Independent transfer exercise

Compare Euler trajectories at 0.25, 1, and 5-hour time steps for a first-order recovery model. Identify which result is physically credible and document the stability condition.

[Open the companion hypothetical lab](labs/08-dynamics-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

The report distinguishes continuous-system dynamics from numerical artifacts and checks units, step size, and model applicability.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
