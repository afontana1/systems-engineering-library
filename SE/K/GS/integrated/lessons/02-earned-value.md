## NS-GS4.1 extension — evidence-weighted completion and forecast identifiability

This integrated emergency-access program has a **cost baseline** and a separate **acceptance baseline**. Do not confuse a cost performance index with readiness. Source: [controlled case](../integrated/data/ns-gs4.1-case.json); reproduce using [the standard-library model](../integrated/code/ns_gs_case.py) and inspect [the output record](../integrated/outputs/ns-gs4.1-results.json). All amounts are synthetic millions of dollars.

### Method and derivation: two denominators, two forecasts

The baseline specifies \(PV=4.0\), \(EV=3.2\), \(AC=4.0\), and \(BAC=9.0\). First compute \(CPI=EV/AC=0.80\) and \(SPI=EV/PV=0.80\). Only \(2.7\) units of EV, however, are backed by currently accepted requirements evidence. The evidence-qualified efficiency is \(CPI_{e}=2.7/4.0=0.675\). The latter is an **instructional diagnostic**, not a replacement for ANSI/EIA earned-value definitions. It prevents the engineer from asserting that budgeted completion and accepted technical completion have identical boundaries.

Two competing final-cost hypotheses are \(EAC_{trend}=BAC/CPI=9/.8=11.25\) and \(EAC_{bottom}=AC+ETC=4+6.3=10.3\). The \(0.95\) difference is explained by different assumptions about how efficiently the remaining work will be done. If technical acceptance is delayed, neither forecast by itself tells us when a mission can be fielded. Decompose the remaining \(6.3\) into hardware, integration, verification and contingencies before assigning confidence intervals.

### Assumptions and sensitivity

The trend forecast assumes stationarity of cost efficiency; it will be biased if remaining evidence is more difficult than the work already earned. The bottom-up forecast relies on the adequacy of the new ETC. Derivative \(\partial EAC_{trend}/\partial CPI=-BAC/CPI^2=-14.0625\) million per unit CPI at \(CPI=0.8\): a decrease of 0.05 in CPI changes the extrapolation by approximately +0.703 million locally (the exact recalculation is 12.0, +0.75). State both the derivative and the recalculated value, rather than silently substituting a linear approximation.

### Worked exercise and explained solution

**Problem.** If the evidence-qualified EV increases from 2.7 to 3.0 with unchanged cost, determine the new evidence-qualified efficiency and whether the program is approved.

**Solution.** \(CPI_e=3/4=0.75\), an improvement of 0.075. Approval does **not** follow: the four requirements must have current, configuration-matching and authorized evidence, and the integrated scenario screen must pass. Audit whether the added 0.3 was independently accepted rather than merely reported. The associated [integrated laboratory](../integrated/labs/INTEGRATED-CASE.html) requires an evidence-adjusted EAC rationale.

**Canonical overlap.** This extension is narrower than the project-management textbook: it studies a measurement-boundary conflict. See [flagship requirements-to-assurance](../../U/flagships/F01-requirements-to-assurance.html) for the larger assurance argument.
