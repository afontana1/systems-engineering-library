# Extended laboratory · Architecture decision hearing

**Course:** Book 1, Week 8 · **Time:** 100–130 minutes · **Companion reading:** [Architecture choice and reversal](trade.md)

## Your role

A sponsor asks why candidate C was discarded and whether candidate B remains preferred if cost priorities rise. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`trade.csv`](trade.csv) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Load the alternatives file and explicitly apply every hard constraint before ranking.
2. Recalculate normalized scores and explain the units and assumed normalization endpoints.
3. Sweep cost weight from 0 to 0.7 while maintaining the stated ratio of the other weights. Find and document the decision reversal.
4. Write a two-sided recommendation: strongest case for B, strongest case for A and what further evidence would break the tie.

## Extension challenge

Propose a new architecture D that is feasible but dominated. Explain why adding a dominated option should not change the ranking of A and B under fixed normalization bounds.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 8 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

C is infeasible; initial scores A=0.575, B=0.675. The crossover cost weight is 0.375. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
