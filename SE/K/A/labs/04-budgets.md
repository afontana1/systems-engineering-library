# Laboratory — End-to-end budgets, common causes and hard feasibility

*Architecture and Assurance · Applied investigation · Fictional Northstar system*

[Read associated textbook chapter](../chapters/04-budgets.html) · [Download executable model](../code/model_checks.py) · [Open sequence index](../INDEX.html)

## Case briefing

The design team has proposed a new dispatch configuration. Nominal latency and energy numbers are favorable, but adverse demand increases queue waiting and a common communications dependency can disable redundant channels.

## Experiment and analysis tasks

1. Calculate five serial operation times (0.8, 0.5, 2.0, 1.2 and 1.0 seconds) and the margin against a 7-second response requirement. Explain why the result is not a 95th-percentile claim.
2. Compute energy margins for every row in `data/budgets.csv`, preserving units and naming any infeasible cases.
3. Compare independent two-channel reliability at .95 per channel with a 3% common-cause outage under the chapter’s conditional model.
4. Vary a hypothetical M/M/1 arrival rate from 8 to 9 requests/hour with service capacity 10/hour; explain the nonlinear delay.
5. Prepare a concept decision in which infeasible choices are eliminated before weights are applied. Propose a critical validation test for each model.

## Submission package

Submit a reproducibility log (exact parameter values and code version), a model or data table, a primary engineering finding, a plausible counterexample, a one-page assumption and uncertainty register, and a **300–500 word** decision memo. Preserve adverse results. If you vary a parameter, show both the baseline and modified results rather than silently replacing an earlier outcome.

## Hints and instructor check

<details><summary>Reference observations — open only after attempting the lab</summary>

Nominal timing is 5.5 seconds with 1.5 seconds unallocated margin. With a 3% shared event and .95 residual channel reliability the modeled success is .967575, not .9975. Some energy rows fail when margin becomes negative. A correct report treats queue estimates as idealized diagnostics and does not use them as fleet verification.

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

[Download lab instructions (Markdown)](04-budgets.md) · [Download Jupyter notebook](../notebooks/04-budgets.ipynb) · [Download executable Python model](../code/model_checks.py) · [Open code and lab browser](../../LAB-LIBRARY.html).
