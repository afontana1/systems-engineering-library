# Morphological analysis for engineering alternatives

**Reference entry · Design-space exploration and decision quality**

## Generate before prematurely converging

Morphological analysis decomposes a solution into functions or design parameters and explores combinations of alternatives. It is useful when teams cling to the incumbent architecture or make every choice independently. A **morphological box** is not merely brainstorming: options need precise semantics, compatibility rules, mandatory constraints and a method to evaluate surviving complete architectures. Treat feasibility, evidence strength and preference as distinct questions.

Consider three illustrative architecture dimensions for a Campus Mobility fleet: sensing mode (`camera`, `lidar`), control location (`onboard`, `edge`, `central`), and power design (`standard`, `extended`). Their unconstrained Cartesian product contains

\[
N=2\times3\times2=12
\]

configurations. Suppose the team makes a *hypothetical* engineering constraint that a `central` control location is not allowed with `camera`-only sensing because the control-loop latency and robustness claim has not been established. That excludes exactly two combinations, leaving **10** candidates before other constraints. This is not a real safety ruling; an actual rejection must cite a measured or derived acceptance condition.

## Feasibility before optimization

A concept matrix may include binary compatibility rules \(g_j(x)\le0\), quantitative timing/power envelopes, operating-mode restrictions and supplier constraints. Reject infeasible options first, then assess remaining alternatives on cost, mission outcomes, verification burden and upgrade flexibility. Be careful: a coarse morphological option such as “onboard” may conceal multiple detailed architectures with different performance. If the option is too vague to be tested, refine its definition rather than fabricating a precise score.

A robust process has successive gates: generate combinations → screen impossibilities with recorded assumptions → build basic function/interface views → perform first-order calculations → select prototypes and discriminating experiments → evaluate alternatives with the same measures. Keep the eliminated options and reasons in a decision log for future revisions.

## Worked reversal due to evidence

Initially ten candidates remain because two `camera-central` combinations are excluded. A validated communications redesign later allows one camera-central combination only under the `extended` power configuration. Then **11** combinations are conditionally admissible, with one remaining excluded. The change is an evidence-driven update to the feasible set, not a change of preference weights. Record the new configuration, operating envelope, and validation evidence before reusing the candidate.

## Exercise with solution

Add a binary option for an independent safety monitor. Before compatibility filtering the box has \(2\times3\times2\times2=24\) combinations. If the two original exclusions hold regardless of monitor choice, four are rejected and 20 remain. Explain why this count assumes independence across the *other* choices and why safety-monitor existence is not proof of independence from a shared power supply. Compare two admissible designs using hard constraints first, then Pareto dominance.

## Sources and limitations

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — architecture alternatives, decision analysis and trade studies.
- [SEBoK: Systems Engineering and Management](https://sebokwiki.org/wiki/Systems_Engineering_and_Management) — systems-engineering decision context.

Related: [architecture variants](architecture-variants-and-configurations.md), [trade studies](engineering-trades.md), [Pareto analysis](pareto-and-value.md), [design-risk retirement](design-risk-retirement.md). The option constraints are deliberately synthetic and do not constitute an evaluated safety architecture.
