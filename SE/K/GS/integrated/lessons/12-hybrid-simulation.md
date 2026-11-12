## NS-GS4.1 extension — a convergent solver can miss a discrete safety event

The case couples a continuous battery-energy state to a discrete command that should stop the mission at a reserve threshold. The toy power trajectory is chosen because it permits an **exact solution**, making the numerical error independently checkable. See [inputs](../integrated/data/ns-gs4.1-case.json), [model](../integrated/code/ns_gs_case.py), and [results](../integrated/outputs/ns-gs4.1-results.json).

### State model, exact integral, and event definition

Define \(E(t)\) in kWh and a load \(P(t)=a+bt\), where \(a=4\) kW and \(b=0.5\) kW/hour. The differential equation is \(dE/dt=-P(t)\); with \(E(0)=18\), integration gives \(E(t)=18-4t-0.25t^2\), where \(t\) is hours. At three hours, \(E(3)=3.75\) kWh. Reserve is 4.0 kWh. The exact guard crossing solves \(18-4t-0.25t^2=4\), or \(t=(-4+\sqrt{30})/0.5\approx2.95445\) h. A continuous guard therefore trips **before** the three-hour deadline.

### Numerical method and falsifying counterexample

Left-point explicit Euler with step \(h\), assuming \(T/h=n\) is integral, uses \(E_{i+1}=E_i-(a+bi h)h\). Summing the arithmetic series gives

\[E_h(T)=E_0-aT-\frac{b}{2}(T^2-Th),\qquad E_h(T)-E(T)=\frac{bTh}{2}.\]

At \(T=3\), step \(h=0.5\) returns \(4.125\) kWh and fails to observe the threshold before the run terminates. At \(h=0.25\), final energy is \(3.9375\) kWh and the first **grid-detected** crossing is 3.0 h—still later than the true crossing. At \(h=0.125\), error halves again to 0.09375 kWh, as the first-order formula predicts. A lower residual alone is not enough; event localization, minimum step and guard semantics need explicit tests.

### Worked exercise and explained solution

**Problem.** At \(h=0.125\) h, what final energy and left-Euler error should a reproducibility check expect?

**Solution.** Error \(=(0.5)(3)(0.125)/2=0.09375\) kWh. Estimated final \(3.75+0.09375=3.84375\) kWh. The correct crossing remains about 2.95445 h. Do **not** report the grid time of 3 h as a verified safe event trigger. The [integrated lab](../integrated/labs/INTEGRATED-CASE.html) adds a rejected step-size input as a negative test.

**Canonical overlap.** The [simulation-uncertainty flagship](../../U/flagships/F08-simulation-uncertainty.html) addresses wider validation questions; this exercise isolates numerical event error.
