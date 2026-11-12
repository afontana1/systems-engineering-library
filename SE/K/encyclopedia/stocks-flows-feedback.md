# Stocks, flows, and feedback loops

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

A **stock** is an accumulated quantity; a **flow** is a rate that increases or decreases a stock; a **feedback loop** links system state to decisions that change future flows. Stock–flow modeling explains why apparently reasonable actions create delays, overshoot, oscillation, or policy resistance. A causal-loop diagram suggests relationships; a quantified stock–flow model must additionally preserve units, initial conditions, constraints, and conservation.

## Theory: conservation and dynamics

For stock `S(t)`, `dS/dt = inflow(t) - outflow(t)`. If `S` is vehicles awaiting maintenance (vehicles), both flows must be vehicles/day. Using counts and rates interchangeably creates dimensional errors that numerical solvers cannot fix. In a first-order backlog-reduction model, `dB/dt = arrivals - B/τ`, where `τ` is the mean clearing time. With constant arrivals `a`, the equilibrium is `B* = aτ`; after a disturbance, the idealized return is exponential with characteristic time `τ`.

Delays and saturation reshape behavior. A manager who increases hiring whenever backlog is high may create an oscillation if recruiting and training take months and hiring decisions use stale information. Nonlinear constraints—limited training capacity, fatigue, or resource competition—can change which feedback loop dominates over time. Causal inference still requires evidence; a feedback diagram alone cannot identify effect sizes or establish that a policy caused an observed change.

## Worked example: a backlog that cannot be managed by slogans

A maintenance shop receives 18 repairs/day and clears backlog at rate `B/4` repairs/day. Its equilibrium backlog is `18 × 4 = 72 repairs`. Starting from 100 repairs, the initial net change is `18 - 100/4 = -7 repairs/day`. A target of 20 repairs cannot be achieved sustainably without reducing arrival rate or shortening effective clearance time; staffing overtime for two weeks may reduce the backlog temporarily but cannot change the equilibrium. A policy simulation should include repair capacity, rework, parts delays, and fatigue before recommending sustained overtime.

## Engineering use and evidence

Inventory the stocks that cannot change instantaneously, quantify their inflows/outflows, and identify information delays, decision policies, nonlinear limits, and feedback polarity. Check that stocks cannot become negative under the chosen numerical method and time step. Test extreme conditions, historical reference modes, unit consistency, and competing structural hypotheses. Use intervention experiments to distinguish a credible causal explanation from a diagram that merely fits past behavior.

## Limitations and connections

Aggregated stocks can conceal distributional inequity, local bottlenecks, or rare mission failures. Many parameters are difficult to identify from limited data. Connect this topic to **complexity and emergence**, **process improvement**, **queueing**, **policy learning**, and **enterprise dynamics**.

## Technical analysis: conservation and numerical stability

Let `B(t)` be an unfinished-work backlog in items, `a(t)` the arrival rate (items/day), and `c(t)` the actual completion rate (items/day). A conserved balance is `dB/dt = a(t) − c(t)`, subject to `B ≥ 0` and a completion policy that cannot serve more work than is available. If arrivals are constant at 12 items/day and completions average only 10/day, backlog grows by about 60 items over a 30-day interval. A “20% productivity improvement” on a different team does not alter this equation unless it increases *actual end-to-end completions*.

A simple feedback policy could command `c = min(c_max, B/τ)` with target clearing time `τ`. For constant arrival rate `a` below capacity, the unconstrained equilibrium is `B* = aτ`. With `τ=2 days` and `a=10/day`, `B*=20 items`. Explicit Euler integration when unconstrained gives `B_(k+1)=B_k+Δt(a−B_k/τ)`; its linear error factor is `1−Δt/τ`. Numerical convergence requires `0<Δt<2τ` and nonoscillatory convergence requires `0<Δt≤τ` for this simplified linear segment. A four-day step at `τ=2` lies at the instability boundary and can produce spurious oscillations or negative inventories without safeguards.

A dynamic model is only as credible as its stock definition, time units, delays, and policy assumptions. Test dimensional consistency and conservation at every step, then compare simulated reference behavior with historical evidence. Numerical artifacts must not be mistaken for organizational feedback.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.
- [SEBoK · Guide to the Systems Engineering Body of Knowledge, v2.14 (2026)](https://sebokwiki.org/wiki/Main_Page) — Community-maintained secondary guide; use its references for further research.

## Step 02 deeper treatment: executable accounting and policy feedback

A causal arrow from demand to backlog describes influence but not units or accumulation. For \(B\) requests in a queue with arrival rate \(a\) and completion rate \(c\), the stock accounting relation is \(dB/dt=a-c\). If \(a=10\) requests/hour, \(c=12\) requests/hour and \(B(0)=30\), a capacity-saturated idealization clears the initial backlog in 15 hours. If demand increases to 13/hour, the same capacity produces sustained growth of 1 request/hour instead. The model must stop service from consuming nonexistent requests; naive integration can otherwise generate negative backlog.

A **model check** should test dimensions, bounds, extreme conditions, time-step convergence, alternative causal structures and held-out observational behavior. “Fixes that fail” is a hypothesis about a delayed adverse feedback, not a universal explanation. An intervention that shortens assignment time might increase demand enough to worsen final pickup time; that alternative loop must be represented before treating the model as decision credible. Follow the complete [stock–flow verification example](systems-dynamics-model-checks.md) and [critical boundary analysis](critical-systems-thinking.md).

## Follow the knowledge

**Related concepts**

- [Complexity, emergence, and adaptation](complexity-emergence.md)
- [Flow, work in process, and bottlenecks](flow-wip-and-queues.md)
- [Interventions, policy resistance, and learning loops](intervention-and-learning.md)
- [The enterprise as a system](enterprise-as-system.md)

**Go deeper in the 240-chapter textbooks**

- [Book 13, Chapter 05: Book 13 · Chapter 05 — Translate feedback hypotheses into stocks, flows, units, and accumulation equations](../B13/chapters/05-translate-feedback-hypotheses-into-stocks-flows-units-and-accumulati.md)
- [Book 13, Chapter 07: Book 13 · Chapter 07 — Explain delays, nonlinearities, oscillation, overshoot, and changing loop dominance](../B13/chapters/07-explain-delays-nonlinearities-oscillation-overshoot-and-changing-loo.md)
- [Book 19, Chapter 05: Week 05 · Enterprise Systems Engineering · Chapter 05 — Enterprise dynamics, feedback, delays, and current-state assessment](../B19/chapters/05.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
