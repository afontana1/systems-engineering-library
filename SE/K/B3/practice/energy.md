# Workshop 4 · Parametric modeling with units and operational margins

*Companion to Book III, Chapter 8 · Values, units, measures, constraints and parametrics*

## How a valid diagram can describe an impossible service

A conceptual shuttle model includes six scheduled trips, a route length, an energy-use rate, HVAC loads, and a battery capacity. Every connector looks correct. But can the proposed vehicle operate for the required service window **without violating its reserve policy**? A parametric model turns the architecture into quantitative constraints whose units, assumptions and sensitivity can be examined before procurement.

Let a trip require \(L\) kilometers of travel at \(r\) kWh/km, plus an HVAC and auxiliary energy load \(H\) kWh/trip. Let \(n\) be the scheduled number of trips, \(C\) the nominal usable capacity, and \(f\) the reserve fraction. These are not dimensionless decorations; their meaning and conditions must be controlled in the model dictionary.

\[
E_{\mathrm{trip}}=Lr+H,\quad E_{\mathrm{demand}}=n(Lr+H),\quad E_{\mathrm{allowable}}=C(1-f),\quad M=E_{\mathrm{allowable}}-E_{\mathrm{demand}}.
\]

A feasible **energy budget** requires \(M\ge0\). This is necessary but not sufficient for a feasible service: charging power, passenger weight, weather, driving duty cycle, battery aging, reserve policy and scheduling may impose additional constraints.

## Worked baseline: mild operating conditions

Use \(L=12\) km, \(r=0.19\) kWh/km, \(H=0.65\) kWh, \(n=6\), \(C=25\) kWh and \(f=0.20\). Then each trip uses \(12(0.19)+0.65=2.93\) kWh; six trips need \(17.58\) kWh. The allowable energy is \(25(0.8)=20\) kWh, leaving margin \(M=2.42\) kWh. The normalized margin is \(2.42/20\approx12.1\%\) of allowable energy. Reporting “12% margin” without a specified denominator would be ambiguous.

Now change the environment to a cold-weather scenario: \(r=0.24\) kWh/km and \(H=1.0\) kWh/trip. Each trip needs \(3.88\) kWh, and six trips need \(23.28\) kWh. The margin is \(-3.28\) kWh: the service window is infeasible under the stated assumptions. Both calculations can be arithmetically correct; the design review must determine which scenarios are part of the operational requirement.

## Sensitivity and model semantics

For fixed trip count and length,

\[
\frac{\partial E}{\partial r}=nL=72\ \mathrm{km},\qquad
\frac{\partial E}{\partial H}=n=6.
\]

Increasing the assumed energy intensity by 0.01 kWh/km increases service demand by \(72(0.01)=0.72\) kWh. Increasing auxiliary use by 0.1 kWh/trip adds 0.6 kWh. These derivatives show which assumptions deserve attention, but they do not provide probability distributions. To support a probabilistic claim about energy sufficiency, one needs a justified joint distribution of conditions, including correlations among temperature, terrain and auxiliary load.

## Units are part of the architecture

A number `190` might mean Wh/km; `0.19` might mean kWh/km. They are equivalent if and only if the unit conversion is explicit. A tool that silently compares values across such units can produce a plausible-looking result that is wrong by a factor of 1,000. Model properties should include value, unit, source, measurement context, time validity and configuration. The constraint block then relates those properties, while a verification procedure measures the real energy budget.

The **model boundary** excludes fleet-level energy sharing and mid-window recharging in this example. If a design assumes charging between trips, add time-dependent energy state and charging constraints; do not quietly add “available charge” to the total without scheduling the charger resource.

## Worked problems

**Problem 1.** Calculate the mild-weather margin in kWh and as a percentage of allowable energy.

<details><summary>Worked solution 1</summary>

Allowable 20 kWh; demand 17.58 kWh; margin 2.42 kWh. Ratio 2.42/20 = 0.121 = 12.1%. State the denominator.
</details>

**Problem 2.** How much must nominal capacity grow to support the cold-weather case with the same 20% reserve?

<details><summary>Worked solution 2</summary>

Need \(C(0.8)\ge23.28\), hence \(C\ge29.10\) kWh. Relative to 25 kWh, that is at least 4.10 kWh additional nominal capacity under the chosen simplified capacity definition.
</details>

**Problem 3.** The energy-intensity estimate increases by 0.02 kWh/km. What happens to demand for six 12-km trips?

<details><summary>Worked solution 3</summary>

Increase is \(6(12)(0.02)=1.44\) kWh. Re-evaluate margin and any affected charging assumptions.
</details>

**Problem 4.** Why can't a positive energy margin establish the design is operationally feasible?

<details><summary>Worked solution 4</summary>

The budget omits charge rate, instantaneous power, usable capacity variation, charger availability, route timing, passenger loads and degraded modes. It establishes one necessary condition only.
</details>

## Transfer to engineering work

Use the JSON parameter scenarios and Python calculator. Make one change to operating assumptions, regenerate margins, and update the architecture claim. Create an explicit model property dictionary with units and sources, a constraint diagram or table, and a verification concept for measuring actual energy performance under the worst relevant environment. Compare your result with Book III Chapter 8's original parametric modeling exercise.
