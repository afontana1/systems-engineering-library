### F06 extension · Hard constraints, robustness, and bounded controllers

**Separate engineering tasks.** Constrained design chooses architecture parameters; operational control chooses actions as state changes. NS-U4.1's optimization problem seeks minimum added cost subject to $q_s\ge0.90$ and $a_s\ge0.85$ for every required scenario $s$. Under the controlled four-option set, **no option is robustly feasible**. Integrated costs 2.1 million illustrative units and passes only normal operation (0.45 scenario weight); it is *not* a deployable optimum. Reporting it as 'best feasible' would silently drop surge, grid, and compound constraints.

**Why weighted averages can mislead.** If an investigator replaces hard requirements with $\sum_s w_s q_s$, a strong normal result can compensate numerically for a disastrous compound case. A weighted expectation describes one preference calculation; it does not enforce an independent severe-event limit or equitable accessible service. A useful screening worksheet shows which constraint fails, by how much, under each scenario.

**Control stability.** For feedback $\dot B=u-kB$, a forward-Euler control/model update with step $h$ is stable only for $0<h<5$ minutes when $k=0.4/\text{min}$. Even with a stable continuous controller, stale sensor data, actuation saturation and unmodeled travel delays can produce transient overshoot. A controller cannot create fleet capacity, road permission or signed route-clearance evidence.

**Worked exercise and solution.** Suppose a reviewer lowers only the overall timely target to 0.80. Guardrails then passes normal overall timing ($\approx0.819$) and accessible timing (1.00), but the grid and compound cases still fail. This is a revised *policy constraint*, not new observed evidence. The board must record who is allowed to change that requirement and why it protects the mission.

**Reproduce:** [model output](../flagship-integration/outputs/ns-u4.1-results.json), [D02](../derivations/02-weighted-trades-and-reversal.md), [D08](../derivations/08-stocks-flow-numerics.md).
