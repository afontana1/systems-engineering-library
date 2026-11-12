# NS-CD6.1 — System Conceptual Design case

**Synthetic teaching material.** This is a new conceptual-design baseline, not the deployment configuration of Books 1–5. Never present any modeled value as an observed mobility-service outcome.

## Study the controlled artifacts

- [Concept and decision inputs](concepts.csv) and [machine-readable assumptions](model-baseline.json).
- [Requirements and verification plans](requirements.csv), [functional model](functions.csv), and [evidence register](evidence-register.csv).
- [Editable architecture diagram](architecture.dot) and [accessible diagram](architecture.svg).
- [Synthetic 2×2 experiment](doe-synthetic.csv); these are hypothetical simulator outputs, *not* independent field samples.
- [Reproducible concept auditor](../tools/step03_book6_concept_check.py) using Python's standard library.

## Decision problem and constraints

A campus mobility service must accommodate an assumed 42-trip/hour event surge with a **10% reserve**, a *modeled* 90th-percentile pickup wait no greater than 12 minutes, accessibility-offer coverage of at least 95%, capital estimate no greater than $3.0 million, and annual operating estimate no greater than $1.2 million. The scope is 250 service days at 8 hours/day. All numbers are invented for teaching.

Four **different concept families** are considered: (A) a scheduled fixed loop, (B) pooled on-demand vehicles, (C) a hybrid trunk-and-feeder design, and (D) brokered partner service. Do not equate low capital cost with feasible operations or apply value weights to infeasible concepts.

Required peak capacity with reserve is

\[C_{\min}=42(1+0.10)=46.2\ \mathrm{trips/h}.\]

At the declared utilization assumptions, A produces 53.33 trips/h, B 47.60, C 52.80, and D 45.00. A fails coverage; D fails reserve capacity, wait, and annual operating cost. B and C satisfy the **point-estimate** screens. The weighted illustrative value scores are 0.6847 (B) and 0.7320 (C). C is **recommended for a controlled pilot only**, not cleared for field deployment or production procurement.

## Why the decision remains conditional

For C, a 10% throughput loss leaves 47.52 trips/h, above the 46.2 trips/h nominal-reserve threshold, while a 15% loss leaves 44.88 trips/h below threshold. Its nominal interface chain totals 420 ms under a 500 ms analytic budget, but a degraded case totals 560 ms. A current pilot p90 wait observation is absent; accessibility coverage has not been independently tested; the booking fallback has not been tested; and one configuration evidence record belongs to the previous baseline.

**Evidence gate:** selection for a pilot is not readiness for an operational release. In particular, nominal cost and capacity estimates alone do not verify the requirements.

## Mathematics to reproduce

For a five-year constant-dollar cost model with end-of-year OPEX and 5% discount rate,

\[PV_5=\sum_{t=1}^{5}(1.05)^{-t} \approx 4.32948;\qquad LCC_C=2.25+0.98PV_5\approx 6.493\ \mathrm{million\ USD}.\]

For wait, accessibility, and operating-cost partial values, respectively, use anchored linear scales over 8–14 minutes, 90–100%, and $0.8–1.3M/year. With weights 0.40/0.30/0.30 the higher feasible value is C. If the wait weight varies while the other two share the remainder equally, B first overtakes C at approximately 0.5327. This weight sensitivity is not a probability of success.

The 2×2 synthetic experiment shows a -3.1 minute *mean main effect* for the higher policy setting, a -1.5 minute main effect for reserve capacity, and a -0.6 minute difference-of-differences interaction. No empirical significance should be claimed from manufactured replicate data.

## Investigations

1. Explain the bias introduced by interviewing only riders who already use the shuttle.
2. Recompute capacity after a 15% utilization reduction, and draft the pilot observation needed to replace the utilization assumption.
3. Determine the switching wait weight, then discuss whether the value anchors make sense for an accessibility-focused population.
4. Distinguish an insufficient degraded timing result from a proof that the hybrid concept can never meet the requirement.
5. Prepare a concept handoff record separating immutable constraints from unresolved assumptions and experiment conditions.

## Reference standards and method sources

- [NASA Systems Engineering Handbook, system design processes](https://www.nasa.gov/reference/4-0-system-design-processes/) — stakeholder expectations, concept alternatives, requirements, iterative design and validation.
- [NASA Systems Engineering Handbook, trade-study glossary](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — transparent criteria, assumptions, data and sensitivity.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — experimental design and interpretation. Source links guide deeper review; the local explanation is the primary instructional content.
