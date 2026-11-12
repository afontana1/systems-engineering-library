# System dynamics: stock–flow correctness and intervention experiments

**Reference entry · Systems thinking, feedback and simulation · Worked technical treatment**

## An influential diagram is not yet an executable model

A causal-loop diagram proposes feedback and polarity; a **stock–flow model** specifies quantities with dimensions and explicit rates of change. Stocks accumulate flows, creating memory and delays. When moving from a qualitative diagram to a runnable model, confirm that the flows act on the correct stock, dimensions match, nonnegativity and capacity constraints are respected, and the chosen time step does not create numerical artifacts.

In a service-backlog example, let \(B(t)\) be outstanding requests (requests), \(a(t)\) new arrivals (requests/hour), and \(c(t)\) completed requests (requests/hour). The continuous accounting equation is

\[
\frac{dB}{dt}=a(t)-c(t),\qquad B(t)\geq0.
\]

A simplified hourly discrete update is \(B_{k+1}=\max(0,B_k+a_k\Delta t-c_k\Delta t)\), with \(\Delta t=1\,\mathrm h\), **provided** the completion rule does not consume more requests than exist or arrive during the interval. The clipping operation is an accounting safety guard, not a complete behavioral model of an actual queue.

## Worked baseline and intervention

Suppose the backlog starts at \(B_0=30\), arrivals are constant at 10 requests/hour, and service capacity is 12 requests/hour while work is available. The idealized net depletion is two requests/hour, reaching zero after 15 hours. If arrivals increase to 13/hour and capacity stays at 12/hour, the backlog **grows** by one request/hour while capacity is saturated. A policy intended to speed clearance may instead increase demand by improving visibility of service, creating a balancing/reinforcing interaction that the first model omitted.

The simple arithmetic is useful because it exposes a checkable limiting case. A Vensim or Python implementation that predicts a negative backlog at hour 16 without any empty-queue handling violates the model's state invariant. A numerical solver could still run without warning; the engineering model would be wrong.

## Validation has multiple layers

1. **Dimensional consistency:** stock units equal rate times time; probabilities are dimensionless.
2. **Structural and boundary checks:** does the diagram include delayed effects, staffing, induced demand and abandonment if they matter to the decision?
3. **Extreme-conditions tests:** zero arrivals, zero capacity, empty backlog, and very large backlog must behave plausibly.
4. **Time-step sensitivity:** compare \(\Delta t=1\), 0.5 and 0.1 hours when the model includes fast feedback or nonlinear constraints.
5. **Historical or held-out data checks:** if field data exist, compare trends and mechanisms without fitting every parameter to the validation set.
6. **Policy sensitivity:** vary the intervention and assumptions, then distinguish robust direction of effect from point predictions.

A simulation that passes dimensional checks can still be invalid for policy use if its causal structure excludes an important reinforcing loop. A visually plausible causal diagram can still violate conservation or exceed resource constraints when executed.

## Feedback archetypes and critique

“Fixes that fail” describes a short-term symptomatic improvement that causes a delayed worsening side effect. “Shifting the burden” describes dependence on symptom relief rather than a fundamental remedy. These are diagnostic hypotheses, not universal laws; operational data and a testable structure are required before claiming an archetype explains a real system.

For Campus Mobility, increasing dispatch automation could lower immediate assignment delay yet draw more demand, saturate a vehicle bottleneck, and lengthen pickup times. Draw both the intended short loop and the delayed unintended loop, then identify observations that would distinguish this hypothesis from an unrelated seasonal demand surge.

## Exercise and references

Start with \(B_0=30\) and compute hourly backlog for four hours under both arrival scenarios. Add an abandonment flow \(q(B)\) with units requests/hour, and test that its rate never exceeds available requests over the time step. State how you would use a historical holdout period to challenge the model rather than simply calibrate it.

- [MIT OpenCourseWare](https://ocw.mit.edu/) — open systems dynamics learning resources; search its course catalog for course-specific materials.
- John D. Sterman, *Business Dynamics* (2000) — stocks, feedback, model testing and policy resistance.
- Related: [stocks and flows](stocks-flows-feedback.md); [simulation credibility](model-vv-and-credibility.md); [critical systems thinking](critical-systems-thinking.md).

*Scope:* The backlog rates are synthetic and omit stochastic variability, priority and queue disciplines.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
