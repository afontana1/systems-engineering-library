# Quantitative performance and reliability without misleading averages

**Concept library essay · Phase 1**

## From a headline metric to a measurable hypothesis
Latency requirements need trigger, endpoints, workload, environment, statistic and threshold. A 500 ms average and a 500 ms 99th percentile describe different performance distributions. If 1% of requests take 20 seconds, an average can remain seemingly reasonable while users experience serious delays. Always inspect a histogram or percentile table and document how load and failures were generated.

An end-to-end budget is useful for reasoning, even before code. Suppose a rider update has contributions of 80 ms ingress, 150 ms queuing, 120 ms processing, 100 ms persistence and 200 ms egress. The 650 ms sum leaves 250 ms under a 900 ms nominal target. But queuing is load-sensitive, and independent percentile budgets cannot simply be added to prove an end-to-end percentile without statistical assumptions. Measure the composed system.

## Queueing intuition
Little's Law relates average in-system work, arrival rate and average time: **L = λW** for a stable system over an appropriate observation period. If a service receives 25 requests per second and average total response time is 0.4 seconds, expected average concurrent requests in the system is 10. This does not imply every burst is safe. A bottleneck approaching saturation can have rapidly rising queues even when mean service duration changes little.

## Reliability accounting
A nominal monthly 99.9% availability target gives 0.1% downtime budget. At 30 days, 0.001 × 43,200 minutes = **43.2 minutes**. However, actual SLA formulas may exclude maintenance, distinguish partial errors, or use request-based success rather than clock availability. Expose the denominator and measurement rules. Series availability of independent components can multiply component probabilities; common-cause failures and dependent infrastructure invalidate naïve independence assumptions.

## Uncertainty and decisions
Use an experiment ledger: hypothesis, fixed conditions, varied factors, observed samples, confidence/limitations and release implication. A load test of 1,000 synthetic calls in a lab does not establish field availability over a month. Favor explicit limitations over false precision. `tools/performance_budget.py` calculates basic budgets and illustrates what the math can and cannot claim.

[Back to Phase 1 library](../README.md)
