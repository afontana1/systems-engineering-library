# NS-FB13.1 — Vensim equation and unit crosswalk (not an executed `.mdl`)

**Purpose:** support a student implementing an independent authoritative Vensim model for EN.645.781. The checked executable artifact in this release is Python. Vensim PLE was **not** installed or run; the following mathematical crosswalk is neither a claim of syntactic Vensim `.mdl` conformity nor evidence of executable model equivalence. Rates are daily; `TIME STEP = 0.5 day`, `FINAL TIME = 360 day`.

| Stock (unit) | Initial value | Differential equation | Main hazards/guards |
|---|---:|---|---|
| Unavailable fleet (vehicles) | 1.9 | `dU/dt = breakdowns - repairs` | `0<=U<=14` vehicles, with bounded rates |
| Standard request backlog (requests) | 265 | `dBs/dt = standard_arrivals - standard_completed - standard_abandoned` | Cap completions by realizable available work |
| Accessible request backlog (requests) | 45 | `dBa/dt = accessible_arrivals - accessible_completed - accessible_abandoned` | Explicit priority allocation; no negative backlog |
| Perceived backlog (requests) | 310 | `dP/dt = (Bs+Ba-P)/18` | First-order information delay, 18 days |
| Trust index (index units) | 63 | `dT/dt = (target_trust-T)/45` | bounded 0–100; synthetic response hypothesis |

Algebraic variables (units): `active_vehicles=14-U` (vehicles); `demand_rate=1260*demand_multiplier*(0.75+0.25*T/70)` (requests/day); `accessible_arrivals = demand_rate*0.14` (requests/day); `surge = surge_max*P/(P+380)` (dimensionless); `capacity=active_vehicles*93*(1+surge)` (requests/day); `breakdowns=active_vehicles*0.00645*failure_multiplier*(1+1.8*surge)` (vehicles/day); `repairs=MIN(U/24*repair_multiplier,0.12*repair_multiplier)` (vehicles/day). The Python code additionally caps rates at available stock per Euler step and allocates completions by accessible reservation followed by standard capacity. For an independent Vensim version, make these step-specific guards explicit and test structural invariance as time step changes. `target_trust=MAX(20,MIN(88,82-0.11*(abandoned_s+abandoned_a)-5*surge-0.03*Ba))` is an assumed behavioral function; coefficients have dimensional units suppressed in the shorthand and must be declared as conversion factors when running Vensim dimensional analysis.

## Translation and parity protocol

1. Define the five stocks above using Vensim `INTEG` and the five initial conditions; define units for each conversion coefficient (`index day/request`, `index/request`, etc.).
2. Define each inflow/outflow as a rate; use `MIN` and `MAX` guards and document any solver-specific semantics and nonnegativity assumptions.
3. Run `0.5`-day integration for 360 days and compare `status_quo` nominal final backlog, average active fleet, cumulative completions, and group abandonment with `summary.json`.
4. Repeat at one and quarter-day steps; inspect time-step sensitivity of both primary output measures and any threshold guard transitions.
5. Use Vensim's dimension and equation checks. Delayed observation is modeled as a first-order stock, **not** a pure transportation delay. Confirm that diagram feedback signs agree with the equations.
6. Version any differences and run perturbations (zero accessible demand, saturated repairs, demand shock). Do not label the model validated until structure, reference modes, and policy consequences are challenged by independent reviewers.

## Important limitations

The imported eight-quarter synthetic course observations are **not fitted** by these parameters. `abandoned` is a deliberately simplified cancellation mechanism; `trust` is an illustrative proxy, not a survey construct; capacity is homogeneous in vehicles and no passenger travel-time distribution is simulated. Book 11's dispatch event simulation and Book 12's vehicle physics are separate representations and **not dynamically coupled** to this model.
