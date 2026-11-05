# Bayesian updating, conditional dependence and information fusion

**Graduate companion concept essay · EN.645.771 · Phase 5**

*All case data are invented teaching examples; models and calculations are not approved operational or safety evidence.*

Bayesian reasoning combines prior belief and observed evidence. For a binary event `H` with alert `A`, Bayes' rule is `P(H|A)=P(A|H)P(H) / [P(A|H)P(H)+P(A|¬H)P(¬H)]`. It forces three questions into the open: how common is the event, how sensitive is the observation, and how often does it trigger without the event?

### Numerical example

An obstruction occurs on 5% of route checks. The detector alarms with probability 0.9 when obstructed and 0.15 when clear. Then the posterior obstruction probability following an alarm is `0.045/(0.045+0.1425)=0.24`. The alarm increases concern from 5% to 24%, but a positive alarm is still more likely to be false than true. This is not a verdict about an individual route without checking calibration and sampling.

### Why multiple feeds may mislead

If independent evidence `A` and `B` is conditionally independent given `H` and `¬H`, likelihood ratios can be multiplied: `posterior_odds = prior_odds × LR(A) × LR(B)`. But if both dashboards copy one upstream sensor, the evidence is not independent. Multiplying both likelihood ratios counts the same underlying observation twice. Record source lineage and retain disagreeing observations.

A Bayesian network encodes conditional dependencies. Whether an arrow supports an intervention requires separate causal assumptions. A network fitted to historical correlations might reflect hidden common causes or changed reporting patterns rather than stable causal mechanisms.

**Exercise.** Raise the event prior to 20% while keeping the detector properties unchanged. Compute the new posterior. Explain why a model deployed after a major storm needs recalibration even when its software remains unchanged.

---

[← Phase 5 contents](../README.md) · [Concept pathways](../KNOWLEDGE-THREADS.md) · [Further reading](../RESOURCE-SHELF.md)
