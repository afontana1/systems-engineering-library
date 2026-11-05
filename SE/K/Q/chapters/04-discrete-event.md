# Discrete-event simulation, queues and service systems

*Textbook-depth conceptual sequence · EN.645.757 / EN.645.758 / EN.645.756 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 11](../../B11/OPEN-BOOK.html), [Book 12](../../B12/OPEN-BOOK.html), [Book 10](../../B10/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## A queue is a dynamic system, not a waiting-time formula

A dispatch queue arises from interactions among arrivals, available service capacity, policies and randomness. The average service time alone does not predict average wait: variability creates congestion and customers interact through shared resources. A discrete-event simulation (DES) represents state changes at particular event times. The state might contain the queue of outstanding requests, each vehicle's availability, service priorities and pending messages. A priority queue orders events; the simulation advances the clock directly to the next event rather than incrementing time in tiny fixed steps.

To construct an event model, define (1) state variables, (2) arrival and completion events, (3) event ordering at equal timestamps, (4) queue discipline, (5) resource acquisition/release rules, (6) stochastic streams and (7) termination logic. State updates must preserve invariants: a vehicle cannot serve two incompatible jobs simultaneously, a completed request cannot be completed twice, and an unaccepted request should not be counted as successful service.

## Analytic benchmark: the M/M/1 queue

For a first check, consider a single-server queue with Poisson arrivals at rate \(\lambda\), independent exponentially distributed service durations with rate \(\mu\), first-come-first-served service and unlimited waiting capacity. Define utilization \(\rho=\lambda/\mu\). The steady-state exists for \(\lambda<\mu\). For this specific model, \(L=\rho/(1-\rho)\) is average number in system and \(W=1/(\mu-\lambda)\) is average time in system. The average queue waiting component is \(W_q=\lambda/[\mu(\mu-\lambda)]\). Little's Law \(L=\lambda W\) is broader than M/M/1, but its application requires consistent boundaries and stable long-run accounting.

At eight requests/hour and service rate ten/hour, \(\rho=0.8\); \(W=1/(10-8)=0.5\) hour or 30 minutes. Mean service duration is only six minutes; the other 24 minutes are expected queue waiting. Increasing arrivals to nine/hour doubles mean time in system to 60 minutes even though workload rises by only 12.5%. This nonlinear congestion effect explains why operating close to capacity is risky. At \(\lambda\ge\mu\), do not produce a steady-state mean; the standard infinite-capacity model has no stationary workload distribution.

## Why a simulation differs from the benchmark

The real Northstar system has multiple vehicles, travel between requests, charging periods, outages, message delays and admission controls. The M/M/1 formula is no longer the answer. It remains a valuable **unit test**: if a DES configured to approximate M/M/1 produces wildly different steady-state averages, investigate event ordering, time units, warm-up and random-number generation. Agreement at a benchmark does not validate the more complex model's structural assumptions.

Consider a request-arrival event at time 08:00:00 and a vehicle-release event at exactly the same time. Which runs first? Both orders may be defensible, but they can yield different reported waits and blocking decisions. Declare a tie-break convention and test it. Similarly, cancellation and reassignment require explicit state transitions. Hidden event-ordering rules can create statistically stable but physically impossible outputs.

## Warm-up, horizon and replication

Starting an empty system at time zero biases the early average downward when the intended system is already operating. For steady-state studies, investigate a warm-up period and discard initial transient outputs using a documented method. For finite emergency missions, the initial empty state may actually be correct—then do not discard the relevant beginning of the mission. Ending at the last arrival can omit all requests that remain unfinished; ending after queue clearance answers a different question. Define the horizon consistently with the operational requirement.

Run multiple independent replications or well-designed batches. The unit of statistical replication is an independently sampled demand/scenario stream, not each request within one run. Retain full denominators: completed, rejected, abandoned, and incomplete requests. If 20% of customers vanish from the queue, a low average wait among the survivors is not good performance.

## Worked design experiment

Suppose one vehicle configuration is simulated under four demand conditions. Synthetic outcomes show mean served-customer wait of 12, 16, 10, and 8 minutes, with completed fractions 0.95, 0.88, 0.60 and 0.50. Ranking by wait alone says the last condition is best. Reporting joint metrics reveals it is worst at serving demand. A balanced decision uses a predefined measure of effectiveness such as timely service across **all** eligible requests, with subgroup constraints and an explicit penalty or separate reporting for refusals. Comparing designs should use paired demand streams, operationally meaningful scenarios, and uncertainty intervals for differences.


## Further depth: event calendars and conservation invariants

An event-driven implementation generally keeps a priority queue of tuples such as `(time, priority, sequence, event_type, payload)`. The monotonically increasing sequence number ensures deterministic tie-breaking when times and priorities match. For an arrival, record the request and either allocate a free server or append it to a queue. For a completion, release the server and start the next queued job. Each event handler should assert invariants: no negative queue length, exactly one terminal state per request, and no server performing more than its allowed number of simultaneous jobs. These assertions are as important as the final average wait.

For a closed finite experiment, a conservation identity is

\[N_{arrivals}=N_{completed}+N_{rejected}+N_{cancelled}+N_{unfinished}.\]

If the identity fails, a state transition is missing or counted twice. Track unfinished requests at the horizon separately; do not silently classify them as completed or erase them. A small deterministic scenario with exactly known event times is a more useful first verification test than a large random simulation producing plausible-looking charts.

Simulation uncertainty has at least two layers. *Input uncertainty* concerns whether arrival, travel or failure distributions match reality. *Output simulation error* concerns sampling a finite number of streams from the selected model. More seeds reduce the second, not the first. When comparing policies, using common random numbers can reduce variance of differences, but doing so requires careful mapping of stochastic streams: if one policy consumes extra random draws in a different order, naive global-seed pairing may not yield comparable external scenarios. Separate arrival, service and failure random-number streams or pre-generate scenarios.

### Verification mini-case

Three requests arrive at times 0, 1 and 2; one server needs two minutes for each request, first-come-first-served. With completion processed before arrival at equal time, starts occur at 0, 2 and 4; completions at 2, 4 and 6; waiting times are 0, 1 and 2 minutes. Average queue wait is 1 minute. This six-minute deterministic example should be exactly reproduced before any stochastic experiments are interpreted.

## Problems — attempt first

1. Compute \(\rho,W,W_q\) for \(\lambda=8,\mu=10\) per hour.
2. Why is \(\lambda=11,\mu=10\) not a legitimate stationary M/M/1 case?
3. List two event tie-break rules a vehicle dispatcher must define.
4. What does a 10-minute conditional wait among completed jobs conceal if 30% of all arrivals were rejected?

<details><summary>Worked answers and engineering interpretation</summary>

1. Utilization 0.8; mean in-system time 0.5 h = 30 min; mean queue delay \(8/[10(2)]=0.4\) h = 24 min.
2. Offered load exceeds service capacity and the unrestricted workload grows without a stable stationary distribution.
3. Arrival versus completion on the same timestamp; cancellation versus assignment/dispatch acknowledgment on the same timestamp. Document the choice.
4. It excludes unsuccessful requests from the average; report service fraction, total count, reasons for refusal, and conditional delay rather than implying universal timely service.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/04-discrete-event.html) · [Download editable Markdown lab](../labs/04-discrete-event.md) · [Open the associated notebook](../notebooks/04-discrete-event.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)
