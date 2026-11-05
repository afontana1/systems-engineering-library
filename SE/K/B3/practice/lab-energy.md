# Extended laboratory · Energy margin and constraint review

**Course:** Book 3, Week 8 · **Time:** 90–130 minutes · **Companion reading:** [Energy budget parametrics](energy.md)

## Your role

A supplier presents a nominally feasible energy budget. Your mission lead requires operation under cold-weather conditions. This is a fictional teaching scenario, not a validated operational system. Do not alter original evidence to make it pass; preserve a copy of the source data and record any changes as experimental scenarios.

## Inputs and method

Download and read [`energy.json`](energy.json) and [`tools.py`](tools.py). Run `python tools.py` from this directory, capture the terminal output and record the Python version, data revision and assumptions. You can change parameters in a separate working copy; the provided source remains the reference fixture.

## Investigation sequence

1. Compute allowable energy, trip energy, total demand and margin for both supplied operating cases.
2. Construct a property dictionary that records units and source for all six model parameters.
3. Derive minimum nominal capacity needed for cold operation at the existing reserve fraction.
4. Propose a test campaign to measure the key rate and HVAC parameters under representative configurations.

## Extension challenge

Add a 10% capacity fade to the cold case and calculate the revised margin. Decide whether the reserve should be applied before or after fade and document your convention.

## Engineering submission

Submit a **two-page technical memorandum** with (a) precise question and baseline/configuration, (b) method and assumptions, (c) calculations and a reproducibility note, (d) uncertainty and counterargument, and (e) a defensible conclusion. Attach a changed dataset or script only if you have documented the change. Finally complete the original Week 8 assessed course assignment separately.

<details><summary>Reference checkpoints — open after your attempt</summary>

Mild margin +2.42 kWh; cold margin −3.28 kWh. Cold minimum capacity at 20% reserve: 29.10 kWh. These values check arithmetic only; the quality of your decision also depends on assumptions, evidence provenance and limitations.
</details>
