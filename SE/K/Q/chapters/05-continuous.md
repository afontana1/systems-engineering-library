# Continuous dynamics, conservation and numerical integration

*Textbook-depth conceptual sequence · EN.645.758 / EN.645.781 / EN.645.757 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 12](../../B12/OPEN-BOOK.html), [Book 13](../../B13/OPEN-BOOK.html), [Book 11](../../B11/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## Build equations from flows and physical meaning

Some engineering states change continuously instead of jumping at discrete event times. Vehicle battery energy, backlog fluid approximations, inventories, temperatures and workforce levels may be described by differential equations. A state variable stores the system's memory. A conservation balance has the structure \(\dot x=\text{inflow}-\text{outflow}+\text{generation}-\text{loss}\). Each term must have units of state per unit time; this is a powerful modeling check. A derivative that adds kilowatt-hours directly to kilowatts is wrong before any simulation begins.

Suppose a battery stores energy \(E\) in kWh. With charging power \(P_c\), mechanical/electrical draw \(P_d\), charging efficiency \(\eta_c\), and time in hours, a simple model is \(dE/dt=\eta_c P_c-P_d\). With \(P_c=10\) kW, efficiency 0.9, and demand 6 kW, net energy increases at 3 kWh/hour. If draw is intermittent, the right-hand side is mode-dependent and may need discrete events. A continuous-only model of charging that ignores connector availability, interruptions and battery limits can produce impossible energy levels.

## A solvable first-order model

An instructive nonphysical surrogate for a recovering inventory, thermal disturbance or backlog is \(dx/dt=-kx\), where \(k>0\) has units of inverse time. Separation of variables gives \(dx/x=-kdt\); integrating yields \(\log|x(t)|=-kt+C\) and therefore \(x(t)=x_0e^{-kt}\). For \(x_0=100,k=0.5\) per hour, after two hours the analytic value is \(100e^{-1}\approx36.79\). This solution provides a reference for testing a numerical solver.

With forward Euler step \(h\), the recurrence is \(x_{n+1}=x_n+h(-kx_n)=(1-kh)x_n\). For this scalar system, numerical asymptotic stability requires \(|1-kh|<1\), or \(0<kh<2\). At \(k=0.5,h=1\), the factor is 0.5 and two Euler steps yield 25, a large error relative to 36.79. At \(h=0.25\), eight steps yield \(100(0.875)^8\approx34.36\), closer but still biased. At \(h=5\), the factor is −1.5, so the numerical solution oscillates and grows even though the true physical system decays. That is a **numerical artifact**, not an emergent physical instability.

## Error, stability and credibility are different

A stable algorithm can still be inaccurate at a chosen step size. Forward Euler has first-order global convergence for sufficiently smooth problems under appropriate assumptions: halving \(h\) should roughly halve the leading global error in a suitable regime. Higher-order methods can improve accuracy but have their own stability regions and computational costs. Stiff dynamics may require implicit solvers. Verify a solver with analytic cases, convergence studies, conservation checks and diagnostic events. Then validate the model structure with independent information about the real system. Solver verification is not model validation.

When an equation reaches a physical bound such as \(E=0\) or \(E=E_{max}\), clipping state values after an integration step may hide energy-balance violations. A defensible hybrid model uses explicit saturation logic, events and consistency checks. Constraining a state by fiat can be acceptable as an approximation if the discarded flow and conservation consequences are documented.

## Feedback and delays in dynamic behavior

If charging power depends on energy error, \(P_c=K(E_{target}-E)\), the state equation becomes a feedback model. Gains, limits and delays matter. A continuous feedback controller that works perfectly in a mathematical model might oscillate when sensor updates and actuation are delayed. A co-simulation can combine dispatch events with energy dynamics, but must define the time at which each model exchanges data. Inconsistent stepping can violate causality or conservation. A simulation architecture should document the coupling contract as explicitly as a software API.

For engineering decisions, perform structural sensitivity: change both rate parameters and model form. A faster-integrating solver does not solve uncertain charging-efficiency measurements or unknown battery aging. Uncertainty propagation and numerical convergence address different sources of error and should be reported separately.


## Further depth: dimensional analysis and solver comparisons

Nondimensionalization exposes which parameter ratios control system behavior. For \(\dot x=-kx\), define \(\tau=kt\) and \(X=x/x_0\). The equation becomes \(dX/d\tau=-X\), independent of the particular units chosen for time or state. The explicit Euler control quantity is \(kh\), not h alone. This tells the engineer immediately why a one-minute step could be excellent for a slowly varying inventory but disastrous for a millisecond-scale electrical control loop.

Convergence studies should compare the *same output functional* at identical physical times. If an event-driven controller switches power at a threshold, the output may change nonsmoothly as step size varies; an event root-finding method or hybrid solver may be necessary. Report both an error estimate and computational cost. A fixed-step solution with attractive plots is not a substitute for a step-refinement study.

Physical flows often create coupled constraints. If vehicle energy is \(E\) and battery temperature is \(T\), a model might include \(\dot E=\eta(T)P_c-P_d\) and \(C\dot T=P_{heat}-h_c(T-T_{ambient})\). Charging efficiency depends on temperature, while heat generation depends on charging. Modeling these as two independent constant-rate equations can miss the coupling most relevant to safety. A verified solver should be applied only after the model's state variables, equations, invariants and limits have been reviewed.

### Model comparison task

Implement forward Euler and a fourth-order Runge–Kutta method on the analytic decay test. At two progressively smaller steps, compare their errors at the same physical final time. Then introduce a piecewise charging cutoff and explain why the analytic reference is no longer directly applicable. Distinguish a numerical error you can measure from a structural modeling uncertainty that requires external evidence.

## Problems — attempt first

1. Calculate the net energy rate for 10-kW charging at 90% efficiency and 6-kW draw.
2. Derive Euler's step-size stability condition for \(\dot x=-kx\).
3. Compute analytic \(x(2)\) for \(x_0=100,k=0.5\), and compare with two one-hour Euler steps.
4. Explain why clipping a negative computed battery energy to zero without recording the deficit can mislead an engineer.

<details><summary>Worked answers and engineering interpretation</summary>

1. \(0.9(10)-6=3\) kWh/hour net increase, subject to charging availability and capacity limits.
2. Euler multiplier \(1-kh\) must have magnitude below one, giving \(0<kh<2\) for positive k and h.
3. Exact \(100e^{-1}\approx36.79\); Euler gives \(100(0.5)^2=25\), about 11.79 below exact.
4. Clipping hides unmet energy demand or unmodeled boundary behavior, artificially preserving feasibility and breaking an auditable conservation balance.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/05-continuous.html) · [Download editable Markdown lab](../labs/05-continuous.md) · [Open the associated notebook](../notebooks/05-continuous.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)
