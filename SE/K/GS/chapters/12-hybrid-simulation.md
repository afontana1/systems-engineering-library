# Hybrid simulation: numerical integration and discrete operating events

*Graduate study for Book 12 — Advanced Systems Modeling and Simulation. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> When a system mixes continuous physics with software-controlled switching, what exactly is the simulator approximating?

## Theory and conceptual structure

Many engineered systems cannot be represented faithfully by only an event queue or only a differential equation. A vehicle battery is a continuous stock of energy, while charging-state transitions, dispatch assignments and emergency stops are discrete events. The combined object is a **hybrid dynamical system**: a continuous state evolves under a mode-dependent differential equation, and guards trigger mode changes or state resets.

The model must state which solver owns time, how simultaneous events are ordered, whether a boundary event is detected between integration points, and what state changes occur at a transition. A simplistic simulator that checks a low-energy threshold only at 15-minute samples can miss a safety-critical crossing at minute 4. Evidence from a “no violation observed” run then reflects the sampling design rather than the intended safety property.

Numerical integration introduces approximation error. Euler's method advances \(x_{n+1}=x_n+h f(t_n,x_n)\), with global error generally proportional to h for sufficiently smooth problems. Reducing h should change outputs in a predictable manner. A convergence study compares successive step sizes against a reference solution or a defensible tolerance, but **convergence is not validation**: the solver can converge very accurately to the wrong differential equations.

Event detection can introduce chattering. If a controller switches from charging to driving whenever energy exceeds 30 kWh, and back when it falls below 30, numerical noise can produce rapid repeated toggles. Hysteresis—different entry and exit thresholds—prevents pathological switching but modifies behavior and must be documented. Conservation balances also provide model-wide invariant checks after every event.

## Formal model and derivation

\[\dot E(t) =\begin{cases}-P_d,&q(t)=\text{driving}\\\eta P_c,&q(t)=\text{charging}.\end{cases}\]
A guard \(E(t)\le E_{min}\) changes discrete mode \(q\). Energy continuity holds unless the model explicitly includes a physically justified reset. A step-size study compares \(E_h(T)\), \(E_{h/2}(T)\), and the event times.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Suppose a vehicle starts at 45 kWh, consumes 6 kW while driving, and must enter a safe mode at 30 kWh. Exact linear depletion reaches the guard after 2.5 hours. A simulator checking only every hour might switch at three hours with 27 kWh remaining: it violates the very reserve rule it was meant to evaluate. Locate the crossing inside the step or use an event-finding solver; then assert that no dispatch is permitted beyond the guard.

![Model of the linked reasoning steps](../figures/12-hybrid-simulation.svg)

## Counterexample and critical review

**Counterexample:** Two simulations agree to six decimal places when step size is halved, but both ignore cold-weather heating. Their numerical consistency says nothing about mission validity. Add observational comparison, operating envelope, input uncertainty and a discrepancy plan before claiming predictive credibility.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

For E0=45 kWh, P=6 kW and a 30 kWh threshold, derive the guard time.

<details><summary>Worked answer and engineering interpretation</summary>

Solve 45−6t=30; t=2.5 hours. Detect the event inside the integration interval.

</details>

### Problem 2

Why does a fixed one-hour sampling rule violate the threshold in the case?

<details><summary>Worked answer and engineering interpretation</summary>

At t=2 h energy is 33; at t=3 h energy is 27. The first observed violation is 3 kWh late; the guard should trigger at 2.5 h.

</details>

### Problem 3

How does hysteresis alter a 30-kWh charge/driving mode switch?

<details><summary>Worked answer and engineering interpretation</summary>

Use e.g. enter charging at 30 kWh and leave charging only at 35 kWh, with an explicit operating constraint preventing dispatch below reserve. This prevents chatter but increases charge dwell time.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/12-hybrid-simulation.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 12 and its existing weekly lessons](../../B12/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)
