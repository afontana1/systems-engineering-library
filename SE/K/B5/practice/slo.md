# Advanced Workshop · Performance Budgets, Queueing Tails, and Quality Attributes

*Book 5 · Week 8 · service-level objectives · response-time tails · utilization · load shedding*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-slo.md). The assessed course obligations remain in [the curriculum](../../../C/P1/EN645764.html).

## 1. A performance claim requires an observable contract

“Fast booking” is not a testable quality attribute. A service-level objective might state: *under a specified arrival profile and healthy dependency configuration, at least 95% of accepted requests complete within 2 seconds, and rejected requests produce an explicit response within 1 second.* It must identify observation points, clocks, sampling window, inclusion rules, and what counts as failure. A low average response time can conceal disastrous tail latency or a high rejection rate.

Software performance is a systems engineering problem because the end-user delay passes through identity, admission, allocation, fleet response, database commit, and notification. If calls are sequential, their delays accumulate. If independent branches can execute in parallel, the critical path is governed by the maximum branch duration—provided their synchronization and failure behavior are modeled. Network uncertainty and shared locks can defeat naïve parallelism assumptions.

## 2. Understand queue stability before percentiles

For an idealized single-server M/M/1 FCFS queue with Poisson arrival rate \(\lambda\) and exponentially distributed service times at rate \(\mu\), utilization is \(\rho=\lambda/\mu\). Stability requires \(\lambda<\mu\). The mean **time in system**—queue waiting plus service—is

\[
W=\frac{1}{\mu-\lambda}.
\]

The complete sojourn time is exponentially distributed with rate \(\mu-\lambda\), yielding a 95th percentile

\[
W_{0.95}=\frac{-\ln(0.05)}{\mu-\lambda}.
\]

At \(\lambda=8\)/hour and \(\mu=10\)/hour, utilization is 80%, mean system time is 0.5 hours and the p95 system time is approximately 1.498 hours. The fact that the *service* average is six minutes does not make the customer-facing mean six minutes; congestion adds 24 minutes in this model. This is a modeling illustration, **not a justified prediction** for real Northstar operations: arrivals may be scheduled or bursty, there may be many servers, and dispatch time is not exponential.

## 3. Why percentiles cannot simply be added

Imagine four software hops with respective p95 delays of 100, 150, 200, and 100 ms. Their sum of p95s is 550 ms, but it is generally **not the p95 of the sum**. The joint distribution, dependence, and branching must be known. A conservative worst-case bound is possible if individual hard maxima truly exist, but p95 is not a hard maximum. When components share a database or congestion event, tail delays may be correlated. Measure or simulate the end-to-end path directly with representative workload, alongside per-hop attribution.

Suppose two tasks run concurrently while an initial 120 ms authentication step and a final 80 ms commit are sequential. If the parallel tasks take 200 and 150 ms in the selected deterministic scenario, the path takes 120 + max(200,150) + 80 = 400 ms. Adding a 90 ms retry yields 490 ms. These are **scenario durations**, not measured service percentile guarantees.

## 4. Turn a budget into an experiment

A latency budget must allocate testable responsibilities to interfaces and components, then reserve margin for variability, monitoring overhead, and fault behavior. Generate a workload with a known distribution, measure completions *and* rejected/time-out outcomes, and plot throughput versus offered load. As offered load approaches sustained service capacity, queue delay and timeout behavior may become nonlinear. Include dependency degradation and burst arrival patterns, not only a steady-state mean.

For a two-second deadline, a design that responds in 300 ms to the requests it accepts but rejects half the demand does not automatically meet the user service goal. Define a separate **availability-of-service** measure for all eligible requests. Clearly distinguish application availability from mission service effectiveness and from the availability of the underlying vehicle fleet.

## 5. Make quality-attribute tradeoffs explicit

Caching may lower latency but increases the risk of stale authorization or route information. Parallel execution improves speed but complicates synchronization and duplicate-safe side effects. Stronger consistency may delay confirmation but protects critical invariants. Review these tradeoffs against system-level hazard and stakeholder needs; do not let a response-time chart silently choose the mission's risk posture.

## Worked problem set — attempt before revealing solutions

### Problem 1

For an M/M/1 queue with 8 arrivals/hour and 10 completions/hour, compute utilization and mean system time.

<details><summary>Show solution 1</summary>

Utilization = 0.8. Mean system time = 1/(10−8) = 0.5 hours = 30 minutes.

</details>

### Problem 2

Under the same assumptions, calculate the p95 system time.

<details><summary>Show solution 2</summary>

−ln(0.05)/(10−8) ≈ 1.498 hours, approximately 89.9 minutes. This depends on the stationary M/M/1 FCFS model.

</details>

### Problem 3

Two parallel tasks last 200 and 150 ms, after 120 ms authentication and before 80 ms commit. Compute the path.

<details><summary>Show solution 3</summary>

120 + max(200, 150) + 80 = 400 ms. A 90 ms retry would make the indicated scenario 490 ms.

</details>

### Problem 4

Why can you not add four hop-level p95 values and label the sum the total p95?

<details><summary>Show solution 4</summary>

The percentile of a sum depends on the joint delay distribution; individual percentiles do not determine the aggregate percentile or correlation.

</details>

## Independent transfer to the Northstar case

Create a small table for arrival rates 5, 7, 8, 9 and 9.5 requests/hour with service rate 10/hour. Compute utilization, mean system time, and p95 in `book5.py`. Compare the modeled trend with a hard two-second web API objective and explain why units and system boundaries matter. Propose a load experiment that measures all eligible requests and at least one correlated-failure scenario.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-slo.md) · [Python source](book5.py) · [Experiment dataset](book5-failures.csv) · [Interactive workbench](WORKBENCH.html).
