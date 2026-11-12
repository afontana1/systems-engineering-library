## NS-GS4.1 extension — coherent dimensional and joint-stress screening

A single valid parametric equation can still fail if its input scenarios are assembled inconsistently. Our synthetic battery-electric emergency vehicle uses a deliberately simple energy budget; it is not a validated thermal/drive-cycle model. Inputs and program: [case JSON](../integrated/data/ns-gs4.1-case.json), [model](../integrated/code/ns_gs_case.py), [results](../integrated/outputs/ns-gs4.1-results.json).

### Dimensioned budget and active constraint

Let \(d\) denote trip distance (km), \(e\) traction energy per distance (kWh/km), \(t\) elapsed hours (h), and \(P_a\) auxiliary load (kW). Demand is \(E_{need}=de+tP_a\) in kWh. Let \(B\) be nameplate battery energy (kWh), \(s\) state-of-charge fraction, \(\eta\) usable efficiency and \(R\) operational reserve (kWh). Headroom is

\[H=Bs\eta-R-de-tP_a.\]

For \(B=42\), \(s=0.70\), \(\eta=0.94\), \(R=6\), \(d=80\), \(e=0.23\), \(t=3\), and \(P_a=1.2\), the supply above reserve is \(21.636\) kWh and demand is \(18.4+3.6=22.0\) kWh, so \(H=-0.364\) kWh. The design is infeasible under this synthetic input combination even though a convenient, less stressful route may pass.

### Derivative screening is not uncertainty propagation

Locally, \(\partial H/\partial d=-e=-0.23\) kWh/km and \(\partial H/\partial e=-d=-80\) km. If \(d\) and \(e\) are random, the first-order variance of their product contains \(2de\operatorname{Cov}(d,e)\), not merely separate variance terms. Positive storm-driven correlation increases tail exposure. A test based on independently sampled pleasant-weather distances and storm-energy coefficients may create a physically inconsistent synthetic scenario. Check units, conditional dependence, bounded inputs, and the operating envelope **before** interpreting a Monte Carlo percentile.

### Worked exercise and explained solution

**Problem.** Keeping all other inputs fixed, what reduction in auxiliary power is required to reach exactly zero headroom over three hours?

**Solution.** Solve \(H+3\Delta P=0\), where \(\Delta P\) is a reduction in kW: \(\Delta P=0.364/3\approx0.1213\) kW. New load \(\approx1.0787\) kW. This is a mathematical boundary, **not** a sufficient design margin: measurement uncertainty, battery aging and cold-weather derating remain omitted. In the [integrated lab](../integrated/labs/INTEGRATED-CASE.html), explore headroom under a *coherent joint* storm scenario rather than optimizing one parameter in isolation.

**Canonical overlap.** [Optimization-and-control flagship](../../U/flagships/F06-optimization-and-control.html) teaches general formulations; this extension focuses on source-dependent, unit-checked operational use.
