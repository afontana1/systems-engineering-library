# Parametric model semantics and sensitivity under correlated inputs

*Graduate study for Book 9 — Applied Analytics for MBSE. Companion to the existing course materials; the definitions, mathematics and decisions below are educational rather than operational approvals.*

## The governing question

> What precisely must be true before a parametric calculation can support an architecture decision?

## Theory and conceptual structure

A parametric model is a typed statement about relationships among quantities, not merely a spreadsheet of values. Each variable needs a definition, unit, valid range, source, uncertainty representation and configuration version. An equation can be algebraically correct and still apply to the wrong system configuration. For instance, a mobility service's daily energy demand must distinguish propulsion, idle power, heating, charging losses and reserve assumptions.

**Dimension checking** rejects expressions such as adding kilowatt-hours to kilowatts. It cannot catch all semantic errors: two energies may be in the same units but refer to different mission periods or system boundaries. Therefore model review should include a quantity dictionary, operational scenario, dependency graph and explicit assertion of intended use. A downstream decision should identify which model outputs are evidence versus which are planning assumptions.

Parametric constraints form a feasible region. A design may have excellent weighted performance yet violate a minimum charging reserve. Feasibility is checked *before* preference aggregation. Local sensitivity (partial derivatives) quantifies response to a small parameter change. Global scenario analysis asks whether the preference persists across important nonlinearities, discrete choices and parameter correlations. Derivative-based ranking is not an adequate substitute for an uncertainty model when the system crosses thresholds.

Correlated inputs matter. High passenger demand may coincide with severe weather, higher heating energy, and slower charging. Treating them as independent understates adverse combinations. Monte Carlo sampling should preserve a justified joint distribution, then report the estimated probability of violating each requirement and its sampling uncertainty. Such an estimated probability is conditional on the distribution, model structure and synthetic data—not an empirical certification of fleet safety.

## Formal model and derivation

\[E_{need}=d\,e_{km}+t\,P_{aux},\qquad E_{available}=B\,s\,\eta-r.\]
The energy margin is \(M=E_{available}-E_{need}\). For first-order uncertainty, \(\operatorname{Var}(M)\approx J\Sigma J^T\), where \(J\) is the row vector of derivatives and \(\Sigma\) the covariance matrix. Off-diagonal covariance terms cannot be dropped without justification.

The formalism is useful only inside an explicit **model contract**: a defined system boundary, input ranges, configuration, assumptions, uncertainty sources, and an intended decision. Check both units and the semantics of the variables before executing the arithmetic. The result is a conditional engineering claim, not an unconditional guarantee.

## Fully worked Northstar case

Assume distance d = 120 km, consumption e = 0.8 kWh/km, auxiliary load P = 2 kW for t = 10 h: E_need = 116 kWh. A 180 kWh battery with state-of-charge fraction 0.90 and conversion efficiency 0.90, minus a 20 kWh reserve, gives E_available = 125.8 kWh and margin = 9.8 kWh. An increase in consumption to 0.90 raises mission demand by 12 kWh, erasing the margin. The preferred vehicle is thus not robust to a plausible energy assumption despite positive nominal feasibility.

![Model of the linked reasoning steps](../figures/09-parametric-models.svg)

## Counterexample and critical review

**Counterexample:** A model records 0.95 “availability” from vehicle-component uptime and uses it directly as end-to-end service availability. The number is dimensionless and passes type checks, but its semantics exclude routing, personnel and dispatch communications. Model consistency requires a defined event (“request served within target”) and a separate mapping from subsystem states to that event.

An independent reviewer should be able to reproduce the favorable result and find at least one material scenario in which it changes. A sensitivity study that does not touch an important assumption can be technically reproducible but decision-irrelevant. Record the source of every number, identify the accountable acceptance authority, and state what the evidence cannot establish.

## Graduate problem set

Attempt each problem before opening the worked solution. In a graded submission, supply units, formulas, assumptions, and a reasoned interpretation—not just the numerical result.

### Problem 1

Recompute the margin when auxiliary power rises from 2 kW to 2.5 kW for ten hours.

<details><summary>Worked answer and engineering interpretation</summary>

Energy demand rises by 5 kWh; margin falls from 9.8 to 4.8 kWh. The system is still nominally feasible, but reserve sensitivity is higher.

</details>

### Problem 2

What is dM/de for the stated mission distance?

<details><summary>Worked answer and engineering interpretation</summary>

−d = −120 km; every additional 0.1 kWh/km reduces margin by 12 kWh, assuming the same operating route.

</details>

### Problem 3

Why can a large Monte Carlo sample not compensate for an invalid independence assumption?

<details><summary>Worked answer and engineering interpretation</summary>

It reduces numerical sampling error around the wrong distribution; structural bias remains. Reconstruct the joint input model or bound the output under dependence scenarios.

</details>


## Laboratory and research transfer

Complete [the accompanying graduate laboratory](../labs/09-parametric-models.html). Produce the artifact described there, compare your result to at least one alternative hypothesis, and record what additional evidence would change your recommendation.

## Connections to the curriculum

- [Open Book 9 and its existing weekly lessons](../../B9/OPEN-BOOK.html).
- [Find supplementary calculations and datasets](../INDEX.html).
- The canonical curriculum remains the source of assessed requirements; this study explains one demanding conceptual thread and does not replace its assignments.

## Additional reference reading

These external resources complement the fictional examples; they are not required for offline use.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook)
