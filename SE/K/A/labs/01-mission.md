# Laboratory — Boundary and mission-evidence challenge

*Architecture and Assurance · Applied investigation · Fictional Northstar system*

[Read associated textbook chapter](../chapters/01-mission.html) · [Download executable model](../code/model_checks.py) · [Open sequence index](../INDEX.html)

## Case briefing

Your team is asked to certify that a fictional regional dispatch service is “dependable.” The provided demand file contains twelve eligible requests, ten completions, and two unresolved requests. Some completed requests have short waits; not everyone was served. A manager wants to publish only the completed-request 90th-percentile wait. Your task is to decide whether this is acceptable and design an alternative scorecard.

## Experiment and analysis tasks

1. Draw two system boundaries: one that excludes, and one that includes, the human operator. Specify which performance and safety claims each can support.
2. Compute completion fraction and fraction of all eligible requests served within 20 minutes. Report missing results explicitly; do not discard them.
3. Produce six linked artifacts: mission need, two stakeholder needs, two verifiable requirements and one planned test; label every relationship type.
4. Challenge one verification procedure: identify a plausible false positive and repair the measurement contract.
5. Write a 300-word technical review decision and a separate counterargument from an accessibility advocate.

## Submission package

Submit a reproducibility log (exact parameter values and code version), a model or data table, a primary engineering finding, a plausible counterexample, a one-page assumption and uncertainty register, and a **300–500 word** decision memo. Preserve adverse results. If you vary a parameter, show both the baseline and modified results rather than silently replacing an earlier outcome.

## Hints and instructor check

<details><summary>Reference observations — open only after attempting the lab</summary>

An acceptable result reports 10/12 = 83.3% completion and 10/12 timely completions for this data; completing within 20 minutes does not mean meeting a 90% population-wide completion requirement. A correct report includes the denominator, measurement interval and unresolved-request policy. A good boundary analysis describes who controls the operator’s actions and what the software can observe.

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

[Download lab instructions (Markdown)](01-mission.md) · [Download Jupyter notebook](../notebooks/01-mission.ipynb) · [Download executable Python model](../code/model_checks.py) · [Open code and lab browser](../../LAB-LIBRARY.html).
