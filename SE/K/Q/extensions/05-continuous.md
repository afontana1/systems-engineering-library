## Step 04 integrated case — a thermal balance and a falsifiable solver check

The queue model is discrete-event; the **same emergency-dispatch exercise** also requires a continuous battery thermal estimate. NS-QSE4.1 intentionally uses a single lumped state to teach a conservation law and numerical verification. It does **not** claim that the battery is spatially uniform, that its coolant loop has been validated, or that the model predicts a vehicle's safe operating envelope.

### Derive a first-order thermal state model

Let \(T\) be pack temperature in degrees Celsius; \(T_a=36\ ^\circ\mathrm C\) ambient temperature; \(a=0.4\ \mathrm h^{-1}\) the lumped thermal conductance divided by effective heat capacity; \(q=4\ ^\circ\mathrm C/\mathrm h\) the heat input divided by heat capacity; and \(u=1.5\ ^\circ\mathrm C/\mathrm h\) a constant cooling extraction, also normalized by capacity. The modeled energy balance is

\[
\frac{dT}{dt}=a(T_a-T)+q-u,
\qquad T(0)=32\ ^\circ\mathrm C.
\]

All terms have units of degrees Celsius per hour. This is an affine first-order differential equation, not a thermodynamic assertion that heat itself has temperature units. Starting from the physical balance \(C\,dT/dt=UA(T_a-T)+Q_{\rm heat}-Q_{\rm cooling}\), the normalization defines \(a=UA/C\), \(q=Q_{\rm heat}/C\) and \(u=Q_{\rm cooling}/C\). It neglects temperature dependence and dynamics in the cooling actuator. The equilibrium is \(T_\infty=T_a+(q-u)/a=42.25\ ^\circ\mathrm C\). Separation or the integrating factor gives

\[
T(t)=T_\infty+(T_0-T_\infty)e^{-at}.
\]

At two hours the exact answer is approximately **37.6444°C**; with cooling removed it becomes approximately **39.7094°C**. Neither temperature establishes battery safety without appropriate thresholds and physical validation.

### Numerical method and observed discretization error

Forward Euler approximates the derivative by \([T_{k+1}-T_k]/h\), giving \(T_{k+1}=T_k+h[a(T_a-T_k)+q-u]\). With \(h=1\) hour (two steps), the result is **38.5600°C**, about **0.9156°C** above the exact solution. With \(h=0.25\) hour (eight steps), the result is **37.8377°C**, about **0.1933°C** high. Reducing the step improves this case's error, but accuracy is not guaranteed merely by choosing a smaller number; a solution can remain wrong if physics or units are wrong. For the homogeneous decay, Euler's amplification factor is \(1-ah\), so explicit stability requires \(|1-ah|<1\), or \(0<ah<2\), while monotone decay requires the stronger \(0<ah\le1\).

The exact solution acts as a **code-verification benchmark** because it checks the implemented time integrator against an analytic solution to the *same equations*. It cannot validate the assumed \(a,q,u\) or the lumped thermal structure. External thermocouple readings, calibration records, power and coolant-flow measurements, and uncertainty propagation would be required for validation.

### Coupled engineering implication

Higher intake demand may increase traction and HVAC load, potentially raising \(q\), while grid disruption may reduce cooling effectiveness \(u\). That creates a physical dependence with the queue's compound scenario. This release does not compute such a joint physical coupling: it treats the thermal exercise as a companion model. Never interpret the two numerical reports as if they came from a coupled validated digital twin.

<details><summary>Worked exercises and interpretation</summary>

1. **Initial slope.** \(dT/dt\vert_{t=0}=0.4(36-32)+4-1.5=4.1\ ^\circ\mathrm C/\mathrm h\). Thus the first Euler step with \(h=1\) produces 36.1°C; the next produces 38.56°C.
2. **Uncooled equilibrium.** For \(u=0\), \(T_\infty=36+4/0.4=46\ ^\circ\mathrm C\). The two-hour transient is below the equilibrium because the initial temperature was lower.
3. **Numerical failure.** For \(h=6\) h, \(|1-0.4(6)|=1.4>1\): Euler errors grow from one homogeneous step to the next. The case runner rejects step sizes that do not divide the stated two-hour horizon; analyze this long-step limit algebraically rather than pretending it is a supported two-hour experiment.

</details>

The exact and Euler outputs are stored together in the controlled JSON report so a future edit that changes the time or units must also change the verification expectation.
