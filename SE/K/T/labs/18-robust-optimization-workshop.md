# Practice Lab T18 — Robust optimization: feasibility before preference

## Scenario
A mobility authority must pick one of three fleet configurations with hard service and energy constraints. Demand and service capacity are uncertain.

## Investigation
1. Inspect [fleet-options.csv](fleet-options.csv) and reject alternatives failing either hard nominal constraint before applying preferences.
2. Run [robust_choice.py](../tools/robust_choice.py) at a minimum service requirement of 10 and energy cap 30.
3. Lower the assumed per-vehicle service capacity from 6 to 4. Identify when the feasible set becomes empty and what redesign options remain.
4. Add a hypothetical energy-storage investment that permits 36 kWh/hour. Recompute feasibility, but do not automatically approve the most expensive choice.
5. Write a decision memo distinguishing hard constraints, uncertain parameters, preferences, and unmodeled risks.

## Deliverable
Submit a feasibility matrix, a sensitivity plot or table, and a proposed next experiment. Avoid using weighted scores to compensate for a failed hard requirement.

[Return to the textbook chapter](../18-robust-optimization.md)
