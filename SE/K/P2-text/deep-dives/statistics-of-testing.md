# How many tests, and what a pass really means

*Phase 2 concept library deep dive · Independent instructional synthesis*

## Separate statistics from acceptance authority
A test requirement needs a measurement quantity, population, environment and threshold. An empirical pass proportion measures observed outcomes for the tested sample, not automatically long-run reliability. If trials are independent, identical Bernoulli demands with unknown failure probability `p`, observing zero failures among `n` trials gives a one-sided upper 95% bound `p_upper = 1 − 0.05^(1/n)` by solving `(1 − p)^n = 0.05`. This approximation is exact under that simple Bernoulli model for zero failures.

For 100 trials it is about 2.95%; for 3,000 trials it is about 0.0998%. This does not mean 3,000 similar button clicks can validate a complex autonomous system: independence, representativeness and comprehensive failure definition may be much harder than increasing the count. If test cases share a bug trigger or environment, effective independent information can be far lower.

## Means and percentiles ask different questions
For latency measurements `x1,…,xn`, the sample mean estimates central tendency. The 99th percentile concerns the upper tail and should not be estimated using the average or merely `mean + 2 × standard deviation` without a justified distribution. One simple *empirical* nearest-rank percentile is the sorted value at index `ceil(0.99n)`. This gives a descriptive result, not a confidence bound on population p99. For 100 observations, nearest rank p99 is the 99th sorted observation, extremely sensitive to tail sampling and workload selection.

An acceptance plan for p99 under a threshold needs predetermined sample scheme, treatment of timeouts, instrumentation uncertainty and a statistical decision rule agreed with the authority. If the threshold is near the instrument's uncertainty range, classify the outcome as inconclusive or use an explicit guard band as policy dictates.

## Measurement uncertainty cannot be ignored
A clock offset of 200 ms may dominate a 900 ms response limit. Calibrate or verify synchronization at relevant start and end points. Capture analysis code and raw logs so stakeholders can audit exclusions and transformations. For censored, dropped and timed-out observations, the data collection design must preserve the existence of failed requests; otherwise the reported tail is selected for success.

## Exercises and answers
1. **Zero failures in 200 trials:** `1−0.05^(1/200) ≈ 1.487%` one-sided upper bound under the Bernoulli assumptions.
2. **Nearest-rank p99 of sorted values with n=50:** `ceil(49.5)=50`; the maximum observed value, not a population confidence statement.
3. **Two failures in 100 trials:** empirical success is 98%. This alone cannot establish a 99% underlying success requirement, and the formal disposition depends on the preapproved acceptance rule.

[Back to Phase 2 companion index](../README.md)
