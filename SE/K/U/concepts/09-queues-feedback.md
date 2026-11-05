# 09 · Discrete-event queues, stock-flow feedback, and congestion

**Concept dossier · modeling / system dynamics / Lean and agile engineering**

## Two different lenses on the same phenomenon

A discrete-event simulation describes individual entities and time-ordered events: a request arrives, a vehicle becomes available, a boarding starts, a trip finishes. A system-dynamics model describes aggregate **stocks**, **flows**, feedback and delays: open requests accumulate, completion drains the backlog, staffing policy alters capacity, and delayed reactions cause oscillations.

Both can be useful; neither automatically subsumes the other. Choose the resolution appropriate to the decision and the data available.

## Little's law is a consistency relation

Under suitable long-run stability and consistently defined system boundaries, **Little's law** is `L = λW`: average number in the system `L` equals average throughput rate `λ` multiplied by average time in system `W`. For a stable dispatch queue with throughput 12 requests/hour and average time 0.25 hour, average work in the system is `L=3` requests.

This is not a staffing formula and does not say the system will remain stable as load increases. If arrivals exceed capacity over a sustained period, the backlog grows and stationary averages may not exist. Do not mix waiting time *in queue* with total time *in system* or average arrival rate with a different throughput population.

## Utilization and nonlinear delay

In an idealized `M/M/1` queue, arrivals are Poisson with rate `λ`, service times exponential with rate `μ`, and stability requires `λ < μ`. Mean time in the system is `W=1/(μ−λ)`. Let service capacity be 15 requests/hour:

- At 9 arrivals/hour: `W=1/6 hour`, or 10 minutes.
- At 12 arrivals/hour: `W=1/3 hour`, or 20 minutes.
- At 14 arrivals/hour: `W=1 hour`, or 60 minutes.

Load grows from 60% to about 93% of capacity, but average delay grows sixfold. This illustrates why optimizing solely for high utilization can harm response time. The M/M/1 assumptions are rarely literally true for multi-vehicle dispatch; use it as a conceptual warning, not an operational forecast.

## Feedback adds dynamics

A stock-flow representation is:

`Backlog(t+Δt) = Backlog(t) + Arrivals(t,t+Δt) - Completed(t,t+Δt)`.

Suppose leadership sees a growing backlog and adds overtime after a two-week approval delay. Temporary productivity rises, but fatigue later increases defects and rework, causing the backlog to rise again. A balancing loop (add capacity → reduce backlog) can be undermined by a reinforcing loop (overtime → fatigue → rework → backlog). The delays matter because managers act on information that may describe a previous state.

In project engineering, a similar trap occurs when teams increase work-in-progress to look busy: more partly completed tasks add queues at specialized review and integration steps, increasing lead time even when total labor capacity stays constant.

## Experiments that distinguish hypotheses

Before expanding fleet size, compare three causes of long waits: insufficient service capacity, time-varying arrivals, and an interface bottleneck at dispatch approval. Measure event timestamps, queue length, blocked transitions and scenario mix. Run sensitivity analysis on arrival variability and service-time distributions; compare simulations with actual high-demand periods.

A change in observed mean wait after an intervention does not prove its causal mechanism without attention to demand mix, staffing, system updates and measurement changes.

## Exercises with answers

**A.** Throughput is 8 jobs/day and average lead time 3 days. Average WIP? **Answer:** 24 jobs under stable and consistently bounded conditions.

**B.** Can 95% utilization be fine if the average service time is short? **Answer:** possibly for a special deterministic or buffer-rich workflow, but in variable queues near-capacity utilization often produces highly nonlinear delays. Evaluate distributional assumptions.

**C.** Why can an overtime policy create oscillation? **Answer:** response and fatigue delays cause decision-makers to act on stale backlog signals, potentially overshooting and overcorrecting.

**Transfer artifact:** arrival/service log, reproducible queue simulation, stock-flow sketch and one explicit reinforcing/balancing loop.

## Connections

[Model credibility](08-model-credibility.md) · [Project baselines](06-cost-schedule.md) · [Agile flow](12-agility-assurance.md).  
**Legacy primers:** [Stocks, flows and feedback](../../encyclopedia/stocks-flows-feedback.md), [Flow, WIP and queues](../../encyclopedia/flow-wip-and-queues.md).
