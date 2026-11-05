# Reliability, availability, and maintainability: three different promises

**Canonical reference · Safety and assurance · Expanded reference · Internal editorial review; independent peer review not performed**

## Definition and why the distinction matters

**Reliability** is the probability that an item performs its required function without failure during a stated interval under stated conditions. **Maintainability** concerns the time or probability of restoring a failed item to service under specified support conditions. **Availability** concerns whether the required function is operable at an instant or during an interval. High reliability does not imply high operational availability, and high availability does not imply the absence of dangerous failures. NASA explicitly treats these as related but distinct disciplines, assessed across design, operation, and support.

For a shuttle dispatch center, an outage lasting four hours and one hundred transient disconnects may produce very different user consequences even if their total downtime is identical. Reliability claims must define the function, failure criteria, environment and mission time. Availability claims must state whether planned maintenance, spare-part delays, logistics, and support staffing count as downtime. Maintainability claims must specify diagnostics, repair skills, access, and resources.

## Mechanisms: failure, repair, and support

A nonrepairable item with a constant failure rate `λ` has survival function `R(t) = exp(−λt)` and mean time to failure `MTTF = 1/λ`. Constant hazard is a simplifying model, not a definition of reliability. Fatigue, wear-out, infant mortality, and changing stress often violate it. Repairable fleets require models of recurrent events; simple “failure rate = 1/MTBF” reasoning is not always valid under nonstationarity or incomplete observation. Field studies must account for units that are still operating when data are collected (*right censoring*).

Under a two-state, alternating up/down process with stationary conditions, mean uptime `MTBF` and mean active restoration time `MTTR`, a long-run availability approximation is `A = MTBF/(MTBF + MTTR)`. More elaborate *operational* availability adds waiting for technicians, spares, transport, administrative downtime, and sometimes scheduled maintenance. Always name the measure used rather than reporting “availability” without a denominator.

A repair distribution also matters: the mean alone can conceal rare but lengthy outages. When exponential repair times of mean 5 hours are assumed, the probability of restoration within 8 hours is `1 − exp(−8/5) ≈ 0.7981`. A contract demanding a ninety-fifth percentile repair time cannot be verified merely by meeting a five-hour mean.

## Worked comparison: mission reliability and repairable availability

Assume an illustrative unit has a constant failure rate of `1/200 = 0.005 per hour` and a mean active repair time of 5 hours, with full support always available. Reliability for an uninterrupted 20-hour mission is `R(20) = exp(−0.005×20) = exp(−0.1) ≈ 0.9048`, **90.48%**. Its idealized long-run steady availability is `A = 200/(200+5) ≈ 0.9756`, **97.56%**. Both figures may be mathematically correct, but neither is an interchangeable answer to “What is the chance the full 20-hour mission succeeds?”

If spare-part delay averages another 10 hours per failure and is included as down time, the simplified availability becomes `200/(200+5+10) ≈ 93.02%`. That reduction motivates lifecycle design decisions involving diagnostics, module replacement, technician placement, and stock policy—not merely buying a more reliable component. Because the failures are assumed independent of repair/availability state and the process stationary, the illustrative formulas should not be used unchanged for common-cause shocks or scheduled shutdowns.

## Architecture, censored data, and common causes

Redundant components can improve reliability only when the success criterion and dependencies are modeled correctly. A parallel architecture fails if all required alternatives are unavailable; a series mission fails if any indispensable function fails. Shared power, updates, operators, environmental exposure, and the same faulty requirement can defeat nominal redundancy. Fault trees, Markov models, event simulations, and reliability block diagrams encode different assumptions and suit different decisions.

For evidence, collect failure taxonomy, operating hours, exposure severity, incomplete lifetimes, maintenance actions, return-to-service criteria, spare supply time and configuration identifiers. Distinguish inherent/achieved/operational availability and record who owns each measure. Forecast assumptions should be tested against field observations instead of allowing historical averages to obscure degradation.

## Failure modes and engineering decision

- Treating a zero-failure demonstration as proof of perfect reliability.
- Combining repair times from incompatible maintenance policies without stratification.
- Reporting percent availability without distinguishing user-visible service from individual component uptime.
- Assuming independent failures for elements exposed to identical stresses or upgrades.

At review, demand reliability at the mission duration, restoration distribution, service-availability definition, evidence about common causes, and the economic consequences of staffing and spares. Reliability is a life-cycle system property, not a single component data-sheet number.

## Selected source-to-claim references

- **R1 · Distinct RAM disciplines and lifecycle activities:** [NASA Office of Safety and Mission Assurance, Reliability and Maintainability — policy and guidance](https://sma.nasa.gov/sma-disciplines/reliability-and-maintainability).
- **R2 · R&M program objectives:** [NASA-STD-8729.1A, NASA R&M Standard for Spaceflight and Support Systems — document scope](https://standards.nasa.gov/standard/nasa/nasa-std-87291).

## Follow the knowledge

- **Prerequisites:** [Probability and dependence](probability-and-dependence.md), [System boundaries](system-of-interest.md).
- **Related concepts:** [System safety and hazards](system-safety-and-hazards.md), [Resilience and graceful degradation](resilience-adaptability.md), [Statistical acceptance](statistical-acceptance-and-confidence.md).
- **Go deeper:** [Book 7, Chapter 7 — Reliability and maintainability](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md); [Book 10, Chapter 8 — Reliability, availability and censored evidence](../B10/chapters/08-analyze-reliability-availability-maintainability-degradation-and-cen.md).
