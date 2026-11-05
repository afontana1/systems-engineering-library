# Laboratory — State invariants, retries and stale-data safety

*Architecture and Assurance · Applied investigation · Fictional Northstar system*

[Read associated textbook chapter](../chapters/03-behavior.html) · [Download executable model](../code/model_checks.py) · [Open sequence index](../INDEX.html)

## Case briefing

A dispatch client retries after a timeout, while a second client requests the same available vehicle. The first assignment may have committed before its acknowledgement was lost. Later, the road-status feed becomes stale. The dispatcher must preserve exclusivity and a defined fallback mode.

## Experiment and analysis tasks

1. Use `ReservationBook` to show that the same key/payload is idempotent, a key with changed payload is rejected, and two keys cannot both claim one vehicle.
2. Write the request state transition table, including cancellation and timeout paths missing from the introductory five-state model.
3. Describe a non-atomic two-thread interleaving that violates assignment exclusivity, then repair it with an atomic guarded commit.
4. Use `route_status_ok` at 4, 5 and 6 seconds of data age. Distinguish information freshness from physical road state.
5. Write one safety property and one liveness property. State the fairness and network recovery assumptions required for liveness.

## Submission package

Submit a reproducibility log (exact parameter values and code version), a model or data table, a primary engineering finding, a plausible counterexample, a one-page assumption and uncertainty register, and a **300–500 word** decision memo. Preserve adverse results. If you vary a parameter, show both the baseline and modified results rather than silently replacing an earlier outcome.

## Hints and instructor check

<details><summary>Reference observations — open only after attempting the lab</summary>

Repeated identical commands have the same effect in the teaching module; conflicting payloads fail; a second claimant receives rejection. Age 5 seconds is accepted by the example rule, 6 seconds is rejected. A strong answer explicitly avoids claiming distributed exactly-once delivery or real-world road safety from these checks.

</details>

## Assessment rubric (100 points)

| Criterion | Points | What constitutes persuasive performance |
|---|---:|---|
| Conceptual and modeling correctness | 25 | Types, definitions, units and assumptions are justified |
| Reproducible evidence | 25 | Another reader can regenerate each numerical or state result |
| Adverse case and sensitivity | 20 | At least one meaningful counterexample is analyzed |
| Engineering decision quality | 20 | Scope, limitations, residual risks and next test are explicit |
| Traceability and communication | 10 | Version, data, and claims are clearly linked |

A numerically correct result with a missing denominator, incompatible revision, or hidden failed case does not earn full evidence credit. This exercise is a synthetic teaching investigation, not a deployment approval.

## Files for this laboratory

[Download lab instructions (Markdown)](03-behavior.md) · [Download Jupyter notebook](../notebooks/03-behavior.ipynb) · [Download executable Python model](../code/model_checks.py) · [Open code and lab browser](../../LAB-LIBRARY.html).
