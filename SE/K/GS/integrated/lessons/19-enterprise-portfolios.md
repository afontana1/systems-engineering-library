## NS-GS4.1 extension — portfolio dependency and constrained value

The enterprise proposes four illustrative investments: interoperability, backup capacity, inclusion and assurance. Their costs, staffing and additive **teaching-value units** are declared in the controlled JSON; these are **not** validated monetary benefits. The backup investment requires assurance to be selected at the same time. Budget is 2.0 synthetic million dollars with five available staff units.

### Finite constrained optimization

Let binary variable \(x_i\) indicate investment \(i\). Choose \(\max\sum_i v_i x_i\), subject to \(\sum_i c_i x_i\le2.0\), \(\sum_i h_i x_i\le5\), and \(x_{backup}\le x_{assurance}\). The executable enumerator evaluates all \(2^4=16\) subsets and rejects those violating cost, staffing, or dependencies. Eight are feasible. The best scored set is **interoperability + inclusion**, cost \(0.60+0.75=1.35\), staff \(2+2=4\), and illustrative value \(1.6+2.3=3.9\). Unspent budget does not imply an overlooked better portfolio; discrete dependencies and labor limits matter.

### What the mathematical optimum omits

The objective assumes additive and comparable value units. In a real enterprise, interventions can overlap, substitute for one another, or shift risk between communities. An isolated backup project cannot simply claim its modeled value without required assurance funding, and an affordable portfolio is not necessarily one with authorization. Future phases can be staged as real options, but options have value only if their decision triggers, expiry and information quality are specified.

### Worked exercise and explained solution

**Problem.** Why is backup + inclusion invalid even though its cost is \(1.10+0.75=1.85\) and staff need is five?

**Solution.** The selection violates \(x_{backup}\le x_{assurance}\) because backup is selected but assurance is not. Adding assurance costs another 0.50 and needs two more staff; the three-part combination exceeds **both** limits. The integrated [laboratory](../integrated/labs/INTEGRATED-CASE.html) has students redesign the dependency or funding rationale rather than delete a necessary acceptance activity.

**Canonical overlap.** [Decisions-and-architecture flagship](../../U/flagships/F02-decisions-and-architecture.html) gives broader multiobjective context; this example focuses on auditable dependencies.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
