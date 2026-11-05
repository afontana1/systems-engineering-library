# D06 · Queueing, Little's Law and the near-saturation effect

**Skill:** Explain why a seemingly small utilization increase can create a very large delay.
![Instructional diagram for 06 queue utilization](../diagrams/03-queue.svg)



## Conservation before probability

For a stable long-run queue, Little's Law says `L=λW`, where L is average number in the system, λ is average completion throughput, and W is mean total time in the system. Its conditions include a well-defined boundary and stable averages; it does **not** require Poisson arrivals. If 30 jobs occupy a process on average and it completes 12 jobs/day, `W=30/12=2.5 days`.

## Derive M/M/1 results under stronger assumptions

For a single-server queue with Poisson arrivals at rate λ, independent exponential service times at rate μ, infinite buffer, first-come/first-served service and `λ < μ`, the equilibrium utilization is `ρ=λ/μ`. The steady-state state probabilities are `P(N=n)=(1−ρ)ρ^n`. Summing the geometric series for expected occupancy yields:

`L = ρ/(1−ρ) = λ/(μ−λ)`.

Using Little's Law, `W = L/λ = 1/(μ−λ)`. Since mean service time is `1/μ`, mean waiting before service is `Wq = W−1/μ = λ/[μ(μ−λ)]`.

For arrivals `λ=12/hour`, service capacity `μ=15/hour`: utilization = `0.8`, average total time = `1/3 hour = 20 minutes`, average queue waiting = `16 minutes`, and mean occupancy `L=4`. Increase arrival rate to 14/hour: utilization rises to 93.3%, but `W=1 hour`. Delay triples though demand increased by only 16.7%.

## Do not overextend the model

Vehicle dispatch may have batching, finite fleets, priority rules, correlated arrivals, outages and travel-time distributions far from exponential. Then use a different analytic model or a credible discrete-event simulator. Empirically verify arrival and service patterns before trusting an M/M/1 calculation.

If λ reaches or exceeds μ under these idealized steady-state assumptions, no finite stationary mean queue length exists. Capacity planning should include contingency, surge demand and acceptable tail delays, not only the average.

## Practice

**Question:** Why does reducing average service time from 4 to 3.75 minutes have different effects at low and high demand?

<details><summary>Solution</summary>

Capacity increases from 15 to 16 jobs/hour. At λ=12, W changes from 20 to 15 minutes; at λ=14, W changes from 60 to 30 minutes. The nonlinear benefit is greatest when capacity is close to demand, given the model assumptions.

</details>

**Transfer artifact:** Boundary, arrival/service evidence, λ, μ, utilization, delay, model checks and a sensitivity curve. See [flow, WIP and queues](../../encyclopedia/flow-wip-and-queues.md).
