# Parametric models: constraints, dimensions, and defensible calculations

**Reference entry · MBSE and quantitative engineering · Worked technical treatment**

## What a parametric model asserts

A **parametric model** connects measured, assumed, or designed quantities through equations and inequalities. Unlike a labeled block diagram, it makes a testable quantitative claim: if the declared parameters and model assumptions hold, the calculated relation should hold. In an MBSE environment the constraint may be attached to parts, interfaces, allocations, and verification results, but a diagram by itself does not execute, calibrate, or validate the equation.

A useful constraint record includes: identifier; input and output quantities with units; expression; admissible domain; parameter source; configuration or version; uncertainty; solver assumptions; and a test that could falsify the claim. Distinguish a *definition* (such as power being energy per time), a *physical approximation* (constant efficiency), and a *requirement* (power shall not exceed an electrical limit).

## Dimensions are part of the semantics

For propulsion, idealized mechanical power is force times speed, \(P_m=Fv\); electrical input power under a constant efficiency assumption is

\[
P_e=\frac{Fv}{\eta},\qquad 0<\eta\leq1.
\]

Here \(F\) is measured in newtons, \(v\) in metres per second, \(\eta\) is dimensionless, and \(P_e\) is watts. The expression is **not** a general battery model: it omits startup transients, regeneration, temperature effects, auxiliary loads, conversion losses, and duty-cycle dependence. Every omitted mechanism is a model-form limitation, not merely a missing decimal place.

Suppose a hypothetical Campus Mobility shuttle requires \(F=1{,}200\,\mathrm N\) at \(v=2.0\,\mathrm{m/s}\), with \(\eta=0.80\). Then \(P_m=2{,}400\,\mathrm W\) and \(P_e=3{,}000\,\mathrm W\). For ten minutes at those assumed constants,

\[
E=P_e t=3\,\mathrm{kW}\times\frac{10}{60}\,\mathrm h=0.50\,\mathrm{kWh}.
\]

The number is an illustrative energy increment, **not** a real vehicle energy or range estimate. Confusing watts, watt-hours, kilowatts, and kilowatt-hours is a dimensional error; multiplying kW by seconds without converting time is a numerical error.

## Link the model to architecture and requirements

An executable trace might be: `REQ-POWER` -> `batterySubsystem.maxDischargePower` -> `tractionController` -> `PARAM-POWER-01` -> `TEST-POWER-02`. This is not verified merely because every identifier exists. The relation also needs compatible quantity types, consistent assumptions, and evidence valid for the system version. If a motor controller changes from a nominal 80% efficiency model to a measured efficiency surface, the input relation and its uncertainty need review.

Require \(P_e\leq3.2\,\mathrm{kW}\) under the specified scenario. The calculated 3.0 kW is only a **model-predicted margin** of 0.2 kW. A system test with sensor uncertainty may produce a different acceptance decision; see [measurement uncertainty and guard bands](measurement-traceability-and-calibration.md).

## Sensitivity and uncertainty

Under the stated equation, local sensitivities are \(\partial P_e/\partial F=v/\eta\), \(\partial P_e/\partial v=F/\eta\), and \(\partial P_e/\partial\eta=-Fv/\eta^2\). These derivatives reveal why uncertain efficiency can have asymmetric consequences, especially near small \(\eta\). When input estimates are correlated, use covariance propagation or a justified Monte Carlo model rather than summing isolated error bars. A plausible-looking parametric diagram cannot compensate for an uncalibrated efficiency assumption.

## Practical audit and exercise

For every quantitative constraint: (1) list quantities and dimensions; (2) state feasible input ranges; (3) check limiting cases; (4) reproduce one result independently; (5) apply a negative test such as \(\eta=0\) or inconsistent units; (6) record the model and evidence versions. Recalculate the example for \(\eta=0.70\): does the same 3.2 kW limit still hold? It does not: \(P_e=3.4286\,\mathrm{kW}\), under otherwise unchanged assumptions. Explain why the boundary is about the assumed operating point, not guaranteed lifetime compliance.

## References and connections

- [NASA Systems Modeling Handbook for Systems Engineering, NASA-HDBK-1009](https://standards.nasa.gov/node/3111) — model elements and engineering work products.
- [OMG SysML v2 specification](https://www.omg.org/spec/SysML/2.0) — language semantics; a language-conformant parser must validate any purported SysML text independently.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — uncertainty, modeling and experimental validation.
- Related: [model, method, language and tool](model-language-method-tool.md); [model queries and validation rules](model-queries-and-validation.md); [correlated input uncertainty](../methods/correlated-uncertainty-propagation.md).

*Scope:* All numbers are hypothetical teaching values. The constraints are explanatory mathematical expressions, not a certified SysML v2 model or safety justification.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
