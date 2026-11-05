# Extended laboratory · Factorial experiment analysis

**Course:** Book 10, Week 6 · **Time:** 120–150 minutes · **Companion reading:** [Factorial effects and interactions](factorial.md)

## Your role

A supplier claims an optimized dispatch algorithm has the same effect in warm and cold operating conditions. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`factorial.csv`](factorial.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Calculate four cell means and the algorithm benefit within each temperature.
2. Calculate the difference-in-differences interaction and its standard error from the independent replications.
3. Report a model-conditional 95% interval and define the experimental unit.
4. Design an independent randomized confirmation experiment that controls demand scenario and fault profile.

## Extension challenge

Introduce a fifth factor, demand burstiness. Explain why adding it without changing the design may confound existing factor estimates.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 6 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Interaction 4.0 minutes; MSE 1; SE sqrt(4/3); model-conditional 95% interval approximately [1.34, 6.66]. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
