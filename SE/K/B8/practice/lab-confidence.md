# Extended laboratory · Zero-failure demonstration challenge

**Course:** Book 8, Week 4 · **Time:** 90–130 minutes · **Companion reading:** [Zero-failure confidence and test design](confidence.md)

## Your role

A supplier has completed 30 failure-free emergency-stop simulations and is asking for a 99% reliability claim. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`requests.csv`](requests.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Calculate the exact one-sided 95% upper failure-probability bound after 30 failure-free independent opportunities.
2. Calculate the required zero-failure sample size for a 1% upper bound under the same assumptions.
3. Write an experiment plan that defines one failure opportunity and addresses representativeness, dependence and configuration.
4. Draft a short supplier briefing that distinguishes observed performance, statistical inference and unresolved assurance gaps.

## Extension challenge

Suppose half of all trials run an identical seed and initial state. Explain why 299 executions would not provide the asserted coverage.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 4 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Thirty zero-failure trials give upper bound about 0.0950. The minimum for a 1% bound is 299 independent failure-free trials. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
