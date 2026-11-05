# Feedback turns a causal story into a dynamic model

**Cross-course pathways:** Systems Thinking 1–12; Simulation Foundations 1 and 12; Decision Science 11.

## Signs describe direction, not goodness

A positive causal link means “an increase in X, everything else fixed, tends to increase Y relative to what it otherwise would have been.” It does not mean X is beneficial. A balancing feedback loop counteracts change; reinforcing loops amplify. A narrative about feedback remains a hypothesis until it produces an observable, falsifiable behavior pattern.

Imagine greater ridership produces revenue, which supports service frequency, which attracts ridership: reinforcing. However, ridership also increases queueing and waiting, reducing attractiveness: balancing. Which dominates can change over time. The causal diagram alone does not determine whether the system will oscillate; stocks, equations, thresholds, delays and parameters are still needed.

## Stock versus flow

Let Q be people waiting and λ and μ be people per hour entering and boarding. The conservation identity is `dQ/dt=λ-μ_eff`, with `μ_eff≤Q/dt + λ` in a discrete numerical step to prevent departures without passengers. Units must match: people/hour times hours gives people. Starting with Q=5 and λ=12/h and μ=10/h over four hours gives Q=13, assuming no saturation or abandonment. Verify with `stock_flow(5,12,10,hours=4)`.

An actual service includes abandonment, time-dependent demand, capacity adaptation and multiple queues. Document these omissions and their potential effects.

## Delay produces unintuitive decisions

Suppose management orders vehicles based on the backlog *four weeks ago*. The queue may already have declined by the time vehicles arrive. A model can represent perceived queue as a smoothed or delayed state and a capacity adjustment with its own delivery delay. Test the intervention with the delay halved and doubled; if its benefit reverses, the model suggests a monitoring experiment rather than a universal prescription.

**Extreme-condition tests:** zero arrivals should not produce phantom passengers; no vehicles should not allow departures; unlimited capacity should eliminate *service* backlog under the model's assumptions; stocks must not become negative.

**Challenge:** distinguish an observed peak in ridership from evidence of an internal reinforcing loop. Demand seasonality and reporting changes are rival explanations that require data.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
