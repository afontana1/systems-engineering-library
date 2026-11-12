# Discrete-event simulation and queues

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

**Discrete-event simulation (DES)** represents a system whose state changes at specific event times: an arrival, resource seizure, task completion, failure, repair, or timeout. Between events the modeled discrete state is ordinarily unchanged. DES is especially useful when contention, sequencing, and stochastic variability affect a decision. It differs from a static spreadsheet because time, queues, and competing entities can change outcomes even if average demand and capacity remain the same.

## Theory: state, event calendar, and statistical output

A DES state might include queue contents, available vehicles, active assignments, and a timestamped event calendar. Processing the next event advances simulated time, changes state, and schedules future events. Essential invariants include nonnegative inventory, no simultaneous exclusive ownership, and conservation of entities except for declared entry and exit events. Random inputs should describe empirically justified distributions and dependencies; assuming independent exponential times solely for convenience can distort tail delays.

For an idealized stable `M/M/1` queue with Poisson arrivals at rate `λ`, exponential service rate `μ`, and `λ < μ`, mean time in the system is `W = 1/(μ - λ)`. This closed-form result is a **benchmark**, not a general law for dispatch networks with priority, batching, shift changes, and nonstationary demand. A simulation should reproduce known analytic cases before claiming credibility for harder ones. Warm-up deletion, replication length, random seed policy, and confidence intervals influence any reported result.

## Worked example: utilization drives nonlinear delay

At `λ = 9` jobs/hour and `μ = 12` jobs/hour, the idealized mean system time is `1/(12 - 9) = 1/3 hour`, or 20 minutes. Raising arrivals to 11/hour increases the theoretical mean to 60 minutes, even though the service rate remains unchanged. Utilization rises from 75% to 91.7%; delay rises threefold. A discrete-event model can then test nonexponential service, priority rules, shift schedules, and failed servers, but its output uncertainty must be estimated over independent replications or defensible batch means.

## Engineering use and evidence

Define entities, events, resources, priorities, preemption rules, arrivals, routing logic, timeouts, observation windows, and collected metrics before implementation. Verify event ordering with traces for small cases; enforce invariants programmatically. Validate at least baseline throughput, occupancy, and delay distributions against operational data, with separate scenarios for peak and degraded conditions. Compare alternatives using common random numbers when the experimental design supports paired analysis.

## Limitations and connections

A queue simulation can be mechanically correct yet omit human adaptation, upstream abandonment, or feedback that changes arrival behavior. Rare events require deliberate sampling and uncertainty analysis. Connect DES to **conceptual modeling**, **flow/WIP/queues**, **design of experiments**, **model credibility**, and **operational metrics**.

## Technical analysis: a simulation event list is an executable model, not reality

A discrete-event simulation (DES) advances simulated time from event to event. A minimal single-server queue has state `(t, queue_length, server_busy, event_calendar)`. For each arrival, generate an arrival event; if the server is idle, schedule completion at `t + service_time`, otherwise enqueue the request. On completion, either start the next queued request or mark the server idle. **Conservation check:** at every simulation instant, `arrivals_so_far − departures_so_far = waiting + in_service`, assuming no abandonment or losses. This invariant catches lost and duplicated entities before any performance claims are considered.

For a checkable benchmark, let arrivals be Poisson at `9/hour` and service times exponential at `12/hour`. Under the stationary M/M/1 model, `ρ = 0.75`, mean number waiting is `Lq = ρ²/(1−ρ) = 2.25`, and mean queue wait is `Wq = Lq/λ = 0.25 hour = 15 minutes`. The predicted mean total time is `W = 1/(12−9) hour = 20 minutes`. A correctly implemented long-run simulator should approach these theoretical values within statistical sampling error—not match them exactly in one finite run.

Estimate uncertainty from **independent replications** or justified batch-means procedures; sequential observations from one queue are autocorrelated. Remove or diagnose initialization bias, define the warm-up and stopping rules, and check rare-event counts separately. These results do not transfer to finite shifts, appointment arrivals, correlated storms, or priority dispatch without revising the model and validation evidence.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.
- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.

## Phase 3 technical reference: Interpreting simulation output, not just generating it

A stationary queue's theoretical mean and a finite run's reported mean answer different questions. For an idealized stable M/M/1 model, \(E[W]=1/(\mu-\lambda)\), so nine arrivals and twelve services per hour imply **20 minutes mean total system time**. A simulated customer trace can check an implementation, but one long run yields *autocorrelated* waiting times. Pooling every customer as an independent observation understates uncertainty. Instead, use independent replications and estimate a mean from replication averages, or use carefully designed and diagnosed batch means. A deliberately short warm-up can bias a long-run estimate; deleting early time from a genuine finite shift changes the target estimand. The [complete simulation-output and credibility chapter](../methods/simulation-output-and-credibility.md) gives 40 reproducible independent replications, a paired upgrade comparison, t intervals and an explicit evidence table.

## Phase 5 technical reading: Calibrated inputs and rare-event precision are different issues

A queueing simulation can reproduce analytic transient/steady-state benchmarks yet still misrepresent real arrival bursts. With independent Poisson count observations of 39 and 51 over two synthetic five-hour periods, the maximum-likelihood rate is \(\hat\lambda=(39+51)/(5+5)=9\) arrivals/hour. An approximate profile-likelihood interval is [7.2664, 10.9896]/hour, much wider than a fixed-parameter Monte Carlo error bar. Separately, a direct 50,000-run estimate of \(P(Z>4)\) expects only 1.58 events; correct importance sampling yields a much more precise estimate under the assumed Gaussian model. The [calibration and rare-event guide](../methods/simulation-calibration-and-rare-events.md) derives both estimators, tests a withheld synthetic count and explains why neither calculation validates a physical system.



## Step 02 review studio — check a simulator against an analytic limiting case

Use an M/M/1 queue only where its assumptions are declared: independent Poisson arrivals, exponential service, one server, stationary rates, stable system, and appropriate buffer behavior. With an illustrative arrival rate of 6 jobs/hour and service rate 10 jobs/hour, utilization is `ρ=6/10=0.60` and mean time in system is `W=1/(10−6) h = 15 minutes`.

**Solved exercise:** what happens if arrivals rise to 9 jobs/hour with service fixed at 10? The analytic mean becomes `W=1/(10−9)=1 hour`. This sharp growth illustrates why capacity margins matter near saturation; it does not imply that the real shuttle service satisfies an M/M/1 model. A simulator should recover the analytical benchmark within Monte Carlo uncertainty *when the corresponding assumptions are enforced*.

**Validation boundary:** correct event scheduling and random-number handling verify implementation; representative demand, service-time, cancellation, routing, and nonstationary effects are separate external-validation issues. Report warm-up, replication count, seed policy, and uncertainty instead of a single impressive point estimate.

## Follow the knowledge

**Related concepts**

- [Flow, work in process, and bottlenecks](flow-wip-and-queues.md)
- [Conceptual modeling and intended use](conceptual-m-and-s.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)
- [Design of experiments and sensitivity](design-of-experiments.md)

**Go deeper in the 240-chapter textbooks**

- [Book 11, Chapter 05: Book 11 · Chapter 05 — Implement discrete-event processes, resources, queues, priorities, and statistics](../B11/chapters/05-implement-discrete-event-processes-resources-queues-priorities-and-s.md)
- [Book 11, Chapter 08: Book 11 · Chapter 08 — Analyze transient and steady-state output with defensible run controls](../B11/chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md)
- [Book 17, Chapter 07: Week 07 · Systems Engineering Process Improvement · Book chapter: Process modeling and simulation for improvement decisions](../B17/chapters/07.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
