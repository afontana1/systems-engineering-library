# Stock-flow models, delays, and policy resistance

*Graduate study for Book 13 — Systems Thinking and Dynamics. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> Why does a well-intended policy often improve a metric briefly and then make the system worse?

## Theory and conceptual structure

Systems dynamics begins by distinguishing **stocks** from **flows**. A stock is an accumulation with a unit, boundary and conservation relationship: unfinished engineering work, trained operators, reserve vehicles, or technical debt. A flow is its rate of change. A causal-loop diagram helps surface feedback hypotheses, but it does not establish that a simulation conserves units or even contains a physically possible mechanism. A stock-flow model forces those ambiguities to be resolved.

Suppose a dispatch unit has a backlog. New requests enter at an arrival rate; completed requests leave at a service rate constrained by available capacity. Increasing target throughput is ineffective if service completion is limited by verification or maintenance resources. Worse, pressure to close work faster can increase rework, returning additional work to the backlog. This creates a reinforcing loop beneath a superficially balancing policy.

Delays matter. Decision makers often act on yesterday's backlog estimate. A large corrective response to a delayed signal may overshoot, especially when vehicles or trained operators cannot be added instantly. Discrete-time simulation additionally depends on step size. A stable continuous feedback law may oscillate in a coarse forward-Euler model; the distinction must be tested rather than assumed.

Policy experiments should examine unintended consequences and time horizons, not merely one steady-state outcome. A temporary reduction in reported backlog may be purchased by suppressing demand or redefining completion. Model credibility requires independently checked stocks, observables, calibration data and counterfactual interventions. When a system contains strategic organizational actors, a stock-flow model may be an incomplete causal account of incentives and changing rules.

## Formal model and derivation

\[\frac{dB}{dt}=\lambda(t)+r(t)-\mu(t),\qquad B(t)\ge0.\]
For a simplified proportional backlog response, \(dB/dt=-k(B-B^*)\), forward Euler gives \(e_{n+1}=(1-kh)e_n\). Stability requires \(|1-kh|<1\), or \(0<kh<2\). A delay or saturation changes this analysis.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Set k = 0.6/day, step h = 1 day. The discrete error multiplier is 0.4, giving convergent adjustment toward target. With h = 4 days, multiplier is −1.4; simulated error oscillates with increasing magnitude even though the underlying continuous first-order model decays. The numerical artifact should not be misinterpreted as evidence of a real unstable organization. Now add a three-day staffing delay: the **real** closed loop can become unstable even with a numerically sound solver.

![Model of the linked reasoning steps](../figures/13-feedback-dynamics.svg)

## Counterexample and critical review

**Counterexample:** A policy cuts “time to completion” by removing independent review, which later increases escaped defects and rework. A model without the rework stock predicts permanent improvement. The missing mechanism, not the solver, is the decisive error.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

For k=.6 and h=1, determine the Euler multiplier.

<details><summary>Worked answer and engineering interpretation</summary>

1−0.6×1 = 0.4, which is stable and monotonic.

</details>

### Problem 2

For the same model at h=4, explain the simulated behavior.

<details><summary>Worked answer and engineering interpretation</summary>

Multiplier 1−2.4 = −1.4; the discrete approximation diverges with alternating sign, even though the original ODE is stable.

</details>

### Problem 3

Design an additional stock to capture quality degradation from accelerated closures.

<details><summary>Worked answer and engineering interpretation</summary>

Track unresolved defects or technical debt; increase that stock through rushed completion and decrease it through rework/remediation capacity. Feed it back into effective arrival or service rates.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/13-feedback-dynamics.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 13 and its existing weekly lessons](../../B13/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)
