# When a response surface deserves your trust

**Cross-course pathways:** Metrics 7; Decision Science 8–10; Advanced M&S 7 and 12.

## Predictive fit is not a decision guarantee

A surrogate approximates an expensive physics model or discrete-event simulator. Linear regression, response-surface quadratics and Gaussian processes differ in flexibility, data needs and uncertainty representation. Select the approximation by the smoothness and discontinuities of the real response; avoid forcing a polynomial across a mode change, capacity threshold or abrupt controller switch.

Partition experiments into design/training, validation and final confirmation. Random splitting can leak information when repeated runs share the same weather scenario or parameter configurations; group by scenario or time when future conditions differ. Report residual patterns, held-out error, domain and failure cases alongside an aggregate RMSE.

## Demonstration

Suppose simulated mean wait at fleet counts 2, 3 and 4 is 18, 11 and 9 min. A quadratic interpolant can pass through all three points. That does not justify predicting physical behavior at fleet 1 or 8, and it cannot guarantee the 95th percentile. A fitted polynomial may become nonmonotonic or predict negative wait outside the observed domain. The surrogate needs constraints or explicit use bounds.

Optimization often seeks the most favorable region for the surrogate, which is also where its approximation error can be exploited. After choosing a candidate optimum, rerun the original high-fidelity model with fresh seeds and adverse scenarios. If the candidate loses its margin, update the surrogate and decision rather than rationalizing away the discrepancy.

## What to write in the model card

List input domains and units, training scenarios, model family, hyperparameters, validation strategy, key error metrics including tails, uncertainty treatment, high-fidelity confirmation and prohibited uses. Refit after domain changes. A narrow but truthful use claim is more valuable than a broad unsupported one.

**Challenge:** Design a validation set for a two-variable surrogate (fleet count and demand rate) that includes peak-demand boundary combinations and a held-out weather regime.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
