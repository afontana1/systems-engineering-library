# Multiobjective engineering decisions without score theater

**Cross-course pathways:** Decision Science 2, 4, 5 and 8; MBSE Analytics 9; Metrics 10.

## Three gates before a recommendation

**Gate 1 — feasibility:** hard constraints such as acceptable safety conditions, accessible service and capacity. An infeasible design is not rescued by a high preference score. **Gate 2 — dominance:** alternative A dominates B (for all-minimize objectives) if it is no worse on every objective and better on at least one. **Gate 3 — preferences and uncertainty:** among the Pareto-efficient alternatives, evaluate stakeholder trade-offs, uncertainty and robustness.

For points `(cost, waiting time)` A=(900,15), B=(1000,12), C=(1100,14), B dominates C because it is cheaper and faster; neither A nor B dominates the other. `pareto_min` returns their indices `[0,1]`.

## What a weight means

A weight in additive multiattribute value should reflect the *importance of moving an attribute from its worst to its best defined endpoint*. Suppose normalized cost value for A is 1 and B is 0, whereas wait-time value for A is 0 and B is 1. With cost swing weight w, additive scores are `V_A=w` and `V_B=1-w`. They tie at `w=0.5`. The calculation is transparent but depends on agreed endpoints, independence assumptions and the shape of the value functions.

A raw weight of “60% safety, 40% cost” has no meaning without defining the safety and cost swings. Never normalize non-compensable safety criteria into a score that lets low cost offset unacceptable risk.

## Sensitivity and regret

Evaluate decisions across plausible weights and uncertain states. A robust candidate can sacrifice a little expected performance to avoid catastrophic regret. Report switching thresholds, not simply the top-ranked option. A Pareto chart is an argument about trade-offs; it is not a final approval and does not establish predicted performance as valid.

**Exercise:** Add D=(1050,11). Which existing points are now dominated? **Answer:** B=(1000,12) remains nondominated because it is cheaper than D; A remains; C is still dominated by B or D. The frontier is A, B, D.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
