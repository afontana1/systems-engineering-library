# Queueing, congestion, and discrete-event simulation

*Core Concepts · Quantitative methods · T07*

> Understand why variability and utilization make response times nonlinear.

**Recommended preparation:** [Uncertainty, statistical evidence, and Bayesian decisions](06-inference.md)

**Related course companions:** [Book 10](../B10/OPEN-BOOK.html), [Book 11](../B11/OPEN-BOOK.html), [Book 12](../B12/OPEN-BOOK.html), [Book 15](../B15/OPEN-BOOK.html)

## 1. Capacity is not the same as responsiveness
Imagine a dispatch center processing shuttle requests. Its average service capacity may exceed average arrivals, yet riders still experience severe delays. Random arrivals occasionally create backlogs; higher utilization means fewer idle intervals remain to absorb them. Little's Law, \(L=\lambda W\), relates average number in system, throughput, and average time in system **when flow is stable and the measurement boundaries agree**. It does not by itself predict waiting time.

For an ideal M/M/1 queue with Poisson arrivals at rate \(\lambda\), exponentially distributed service at rate \(\mu\), one server, and \(\lambda<\mu\), the mean sojourn time is \(W=1/(\mu-\lambda)\). This depends critically on the model. If \(\lambda=8\) per hour and \(\mu=10\), \(W=0.5\) hours. At \(\lambda=9\), \(W=1\) hour. The arrival rate increased only 12.5%, but mean time doubled.

## 2. Know what event simulations represent
A discrete-event model advances from one state-changing event to the next: request arrival, service start, service completion, vehicle failure, or recovery. It should specify queue discipline, resource occupancy, termination conditions, event ordering for simultaneous times, and whether unserved requests are counted. An event log makes the simulation auditable.

The model's **conceptual validity** must come before code correctness. If requests disappear when no vehicle is available, a perfectly tested program may falsely show short waits. A useful internal invariant is arrivals = completed + queued + rejected + otherwise-accounted-for requests at the chosen observation horizon.

## 3. Separate warm-up, replication, and scenario uncertainty
A finite simulation starting with an empty queue often understates steady-state congestion. One remedy is warm-up removal after demonstrating the system has settled; another is explicitly modeling a finite-day service with realistic morning conditions. To estimate uncertainty, use multiple independent replications and report variability across replication-level statistics. Treating every request in one simulation run as independent exaggerates sample size when they share congestion and operating conditions.

For comparing two alternatives, paired random streams can reduce noise: run both scenarios with the same synthetic demand realization, then analyze within-pair differences. Pairing does not eliminate uncertainty in the demand model itself.

## 4. Choose metrics that resist gaming
Track completed share, rejected share, queue length, mean and tail waits, recovery time, and subgroup performance. Conditional wait among served requests is useful but must not be the sole metric. Record which population defines each denominator. In safety and service engineering, missing outcomes are often the most important outcomes.

## 5. Bridge the analytical model and simulation
Analytical queue models offer interpretable limiting behavior; simulations can represent more realistic scheduling, failures, and finite horizons. Use both. First calculate the ideal M/M/1 baseline. Next implement a first-in-first-out single-server event simulation with the same Poisson/exponential assumptions. Run enough replications to see whether the estimated mean aligns with the analytical benchmark. Only then add dispatch-specific rules, vehicle travel time, priority requests, or service interruptions.

A simulation should have conservation checks. If 100 requests arrived, and 76 completed while 12 remained queued, the other 12 must be explicitly accounted for as rejected, cancelled, or otherwise resolved. A model that silently drops them can look faster while providing worse service. Verify units and timestamp ordering, especially when service completion and a new arrival occur at identical simulation times.

**Scenario validity is different from statistical precision.** A narrow confidence interval around a simulated mean does not imply a credible real-world result if arrivals do not follow the assumed distribution. Compare measured inter-arrival times and service times where data exist. Test sensitivity to correlated peaks, weather interruptions, and priority dispatch.

**Check your reasoning:** Increasing the service rate from 10 to 12/hour under an M/M/1 arrival rate of 8/hour reduces mean time from 30 to 15 minutes. Is that guarantee transferable to the Northstar fleet? Not directly. Multi-vehicle routing, travel times, boarding, geography, and scheduling policy can violate core M/M/1 assumptions.

## Guided worked example

### Worked case: utilization sensitivity
For \(\lambda=8,\mu=10\) per hour, utilization \(\rho=0.8\), mean time \(W=30\) min, and mean number in system \(L=\lambda W=4\). If capacity falls to \(\mu=9\), \(W=60\) min and \(L=8\), provided the M/M/1 assumptions apply. If arrival rate equals or exceeds service rate, a stable stationary mean does not exist in this model.

## Independent transfer exercise

Run the event-based queue exercise with 8, 9, and 10 arrivals/hour against a nominal 10/hour service rate. Compare the formula and finite-horizon simulated outcomes, including unsuccessful requests.

[Open the companion hypothetical lab](labs/07-queues-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Show why the M/M/1 steady-state result cannot be used when arrival rate is at or above service rate. Discuss simulation warm-up and queue discipline.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.


<!-- STEP04-T1-START -->

## Step 04 T1 — Evidence-driven correction and worked transfer

### T1 audit finding: reconcile service and queue statistics before interpreting speed

For the finite NS-T4.1 observation window, the required accounting identity is \(N_{arrivals}=N_{served}+N_{rejected}+N_{pending}\). Inserting the fixture yields \(40=32+5+3\). An event log that records an extra completion without a matching request identifier violates this identity, even if its estimated average wait decreases. Requests rejected immediately and requests pending at closing must not quietly disappear from the outcome denominator.

Compare this finite-case ledger with an **independent idealized M/M/1 analytical benchmark**: \(\lambda=8\) requests/hour, \(\mu=10\) services/hour, and \(\rho=0.8\). Mean time **in the entire system** is \(W=1/(\mu-\lambda)=0.5\) hour (30 minutes). Mean queue *waiting* time excludes service: \(W_q=W-1/\mu=0.4\) hour (24 minutes). Little's Law gives \(L=\lambda W=4\) requests in system and \(L_q=\lambda W_q=3.2\) waiting. These are steady-state expectations, **not** measurements from the forty requests.

**Practice and explained solution.** If a candidate reports 33 served, five rejected, and three pending from forty arrivals, the sum is 41: identify a duplicate or a faulty state transition before calculating performance. In the ideal M/M/1 benchmark, increasing arrival rate to nine/hour raises \(W\) to 60 minutes; it does not imply a particular finite-shift completion fraction. [Reproduce the distinction](labs/T1-INTEGRATED-CASE.md).

<!-- STEP04-T1-END -->
