# Chapter 8 — Parametrics prevent attractive but impossible models

*Book III: Introduction to Model-Based Systems Engineering · Week 8 — Values, units, measures, constraints, parametrics, and analysis integration*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 8](../labs/lab-08-values-units-measures-constraints-parametrics.md) before attempting [the assessed Week 8 coursework](../../../C/P1/EN645631.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-631-w08.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **values, units, measures, constraints, parametrics, and analysis integration** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Parametric models connect properties and constraints to analysable quantities. Their value is in making dependencies explicit: units, valid ranges, distribution assumptions and configurations. A value is not sufficiently defined if its source or unit is ambiguous. Distinguish model definition from parameter observation, and compare analytic predictions with scenario outputs.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

### Parametrics connect architecture to physical possibility

Architecture diagrams describe possible relationships, but parametric models test whether the relationships satisfy constraints. A battery, route plan, climate system, and charging window can all be individually plausible while the fleet is infeasible as a coupled whole. The critical step is choosing quantities with clear units and scopes: energy per trip, usable capacity, charging power, duty cycle, and uncertainty margin. A parametric constraint expresses a relationship among those quantities independently of diagram layout.

A constraint is not an observation. A calculated margin can be positive only because a model omits cold-weather consumption, battery aging, or charger contention. Trace each parameter to its source or explicit assumption, and test limiting cases before trusting detailed numerical output. A model capable of changing a design decision is more valuable than one with many decorative equations. In this sense, parametrics make architectural preferences answerable to conservation, capacity, timing, and other non-negotiable realities.


## Deeper theory — parametric models as conservation arguments

### Equations acquire meaning from system boundaries

A parametric model is more than a collection of arithmetic formulas attached to blocks. It is a declaration of which quantities matter, how they relate and which assumptions make the relationship valid. The first task is to identify the conservation laws or physical mechanisms: energy is consumed, vehicles occupy capacity, time passes, battery temperature changes, messages move through bounded channels. Only then should we select parameters. Otherwise a plausible-looking constraint network can encode quantities that happen to have matching units but no causal relationship.

For a shuttle, suppose electrical demand has traction and auxiliary components. A useful first-order model is

\[
E_{\mathrm{required}}=e_{\mathrm{km}}D+P_{\mathrm{aux}}T,
\]

where \(e_{\mathrm{km}}\) is energy per driven kilometer, \(D\) is route distance, \(P_{\mathrm{aux}}\) is average auxiliary power and \(T\) is operating time. The model is a *balance over a specified time horizon*, not an exact battery prediction. It excludes regenerative-braking dynamics, temperature-dependent efficiency, charger losses and degradation unless those are included deliberately elsewhere. Its value is that each term carries a defensible interpretation and set of units.

### Dimensional analysis is a first consistency test

The traction term has units (kWh/km)×km = kWh. The auxiliary term has units kW×h = kWh. Their sum is meaningful. A calculation that adds “energy margin in kWh” directly to “charging rate in kW” is dimensionally invalid even if a spreadsheet accepts it. Dimensional analysis cannot catch every modeling error, but it rejects many physically meaningless equations before numerical calibration creates false confidence.

Let \(e_{\mathrm{km}}=0.24\) kWh/km, \(D=180\) km, \(P_{\mathrm{aux}}=2\) kW and \(T=10\) h. Then traction requires 43.2 kWh and auxiliary systems require 20 kWh, so total nominal demand is 63.2 kWh. A battery nominally rated at 75 kWh with an assumed usable fraction of 0.85 offers 63.75 kWh. The nominal margin is only 0.55 kWh, less than 1% of nominal demand. The striking result is not the decimal; it is the sensitivity of the feasibility claim to assumptions that were previously invisible.

If traction intensity rises modestly from 0.24 to 0.26 kWh/km, the traction requirement becomes 46.8 kWh and total demand becomes 66.8 kWh. The same architecture is now infeasible without charging, reducing route distance, lowering auxiliary load or changing battery assumptions. A model that reports only “passes at nominal parameters” conceals that fragility.

### Constraints are not predictions

An equality such as the energy balance can describe a physical approximation. An inequality such as \(E_{\mathrm{required}} \leq E_{\mathrm{usable}}\) states a feasibility condition. The two play different roles. A requirement may impose the inequality, while a simulation or physical measurement provides estimates of the terms. An architecture that satisfies the algebra under invented nominal values is not automatically safe to operate. The result is a conditional design argument: *if* the parameters and simplifications characterize the intended operating domain, *then* the modeled energy constraint holds.

A parametric diagram therefore should record not just variables but their units, bounds, provenance, operating conditions and ownership. Values copied from a supplier's brochure may use a different temperature, duty cycle or battery state-of-health assumption than the shuttle program. Linking incompatible assumptions can produce a mathematically coherent but operationally false model.

### Sensitivity and uncertainty as model questions

For the simple model, the partial derivative with respect to route distance is \(\partial E/\partial D=e_{\mathrm{km}}\); with respect to auxiliary power it is \(\partial E/\partial P_{\mathrm{aux}}=T\). These derivatives describe local sensitivity. They do not say which input is actually most uncertain. An input can have a large derivative but be measured accurately, or a small derivative but be highly variable. For small independent uncertainties, a first-order variance approximation is

\[
\operatorname{Var}(E)\approx D^2\operatorname{Var}(e_{\mathrm{km}})+e_{\mathrm{km}}^2\operatorname{Var}(D)+T^2\operatorname{Var}(P_{\mathrm{aux}})+P_{\mathrm{aux}}^2\operatorname{Var}(T),
\]

with covariance terms required whenever inputs are dependent. Independence often fails: cold weather increases auxiliary demand and can worsen propulsion efficiency simultaneously. Ignoring that correlation tends to understate the risk of simultaneous high loads.

### Linking parametrics to architecture decisions

A parameter does not become meaningful because it appears in SysML or a spreadsheet. It becomes useful when it changes a decision. A low energy margin may motivate an early charging experiment, an alternate route concept or an additional contingency requirement. When an input changes, the model should identify the affected constraint, responsible components and associated verification evidence. The virtue of model-based parametrics is not prettier equations: it is the ability to carry assumptions consistently through allocation, design alternatives and change review.

## Worked Northstar example

For 2 vehicles each completing 3 trips/hour, nominal capacity is 6 trips/hour. Demand of 8 trips/hour exceeds that simple capacity, even though neither a requirements nor a structure diagram necessarily shows the contradiction. Represent trips_per_hour with units, compute utilization 8/6 > 1 and mark the configuration infeasible under steady-state assumptions.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.

### Dimensional and feasibility reasoning

Consider **two vehicles**, each completing **three trips per hour**. Maximum modeled throughput is `2 × 3 = 6 trips/hour`. If expected arrivals are **8 requests/hour**, the capacity ratio is `8/6 = 1.333`. Under sustained, steady arrivals with no pooling and unchanged trip duration, backlog cannot stabilize: workload grows by about two trip requests per hour. This is a feasibility constraint, not an estimate of an individual passenger's precise wait.

A valid parametric element should attach units to all inputs, record the source of the service-rate estimate, identify this no-pooling assumption and identify its applicable configuration. In a more detailed model, variable journey durations and pooling would change the expression; that uncertainty should be represented, not hidden.

## What can go wrong—and why

A calculation with precise decimals can still be wrong if demand is peak demand and supply is average capacity, or if trips include multiple passengers.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 8: Parametrics prevent attractive but impossible models](../labs/lab-08-values-units-measures-constraints-parametrics.md), you will: Create a constraints table for fleet size, trip rate, request rate and maximum utilization. Inject a unit mismatch and a capacity violation; record whether each is model error or design shortfall. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 8 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](07-logical-architecture-functional-allocation-de.md) and leads toward [next chapter](09-candidate-physical-architectures-model-based-.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-631-w08.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Extended worked problems and lab

Study the [worked problem workshop on energy budget parametrics](../practice/energy.md), then complete the [extended laboratory](../practice/lab-energy.md). The exercises are separate from the original assessed coursework.

## Worked parametric constraint and uncertainty check

The [MBSE semantic-modeling method guide](../../methods/mbse-semantic-modeling-handbook.md) extends this chapter with executable trace rules, a guarded booking-state invariant, and an energy-margin example. The critical point is that a **parametric constraint makes an engineering assumption testable**; it does not make that assumption correct.

For a serial mission segment, approximate required electrical energy by

\[
E_{\mathrm{req}}=e_dD+P_{\mathrm{aux}}T,
\]

where traction energy intensity \(e_d\) is kWh/km, route length \(D\) is km, auxiliary power \(P_{\mathrm{aux}}\) is kW, and mission duration \(T\) is h. For 0.24 kWh/km, 180 km, 2 kW and 10 h, the demand is \(43.2+20=63.2\) kWh. If usable battery energy is 70 kWh under those conditions, margin is 6.8 kWh. Under a cold-weather intensity of 0.29 kWh/km with all else unchanged, demand rises to 72.2 kWh and margin becomes **−2.2 kWh**.

The statement \(E_{\mathrm{req}}\leq E_{\mathrm{usable}}\) is a feasibility constraint; the example does not establish how likely it is to be violated. A credible engineering model should carry values, dimensions, conditions, source data, configuration, and credible parameter intervals. A model revision that updates 0.24 to 0.29 without triggering an impact query on the energy-margin claim is a **model-governance failure** even if every diagram renders correctly.

**Practice:** Derive the maximum route distance permitted under both traction-intensity assumptions, retaining the 20-kWh auxiliary load and 70-kWh usable energy. Solutions: \(D_{\max}=(70-20)/0.24\approx208.3\) km nominal and \(D_{\max}=50/0.29\approx172.4\) km cold. The assumed 180-km route is therefore feasible in the nominal case and infeasible in the cold case. Real battery reserves, cell limits and contingencies must be specified separately.

## Step 03 integrated reference: quantitative constraints and uncertainty

### Use quantities with units and declared scope

A parametric relation becomes an engineering model when its variables have defined units, valid ranges, boundary conditions, and an identifiable decision. NS-MB3 uses a simplified energy model for a 24-trip shift. The per-trip traction energy is route distance multiplied by energy per kilometer; auxiliary energy adds a fixed quantity per trip:

\[
E_{\mathrm{shift}}=N(d e+E_{\mathrm{aux}}).
\]

For \(N=24\) trips, \(d=1.8\ \mathrm{km/trip}\), \(e=0.36\ \mathrm{kWh/km}\), and \(E_{\mathrm{aux}}=0.20\ \mathrm{kWh/trip}\), demand is

\[
E_{\mathrm{shift}}=24(1.8\times 0.36+0.20)=20.352\ \mathrm{kWh}.
\]

The synthetic battery has 40 kWh nameplate capacity and a 25% reserved fraction, giving an illustrative usable limit of \(40(1-0.25)=30\ \mathrm{kWh}\) and a margin of \(9.648\ \mathrm{kWh}\). The units agree: kilometers cancel in \(d e\). Comparing the result with a power limit in kilowatts would be a dimensional error.

### Derive sensitivity, don't only recalculate the base case

A first-order sensitivity to the energy rate is

\[
\frac{\partial E_{\mathrm{shift}}}{\partial e}=Nd
=43.2\ \mathrm{km}.
\]

If the traction rate rises by \(0.05\ \mathrm{kWh/km}\), the first-order increase is \(43.2\times0.05=2.16\ \mathrm{kWh}\), leaving \(7.488\ \mathrm{kWh}\) of model margin. The equality is exact for this linear model. It does not include temperature, route elevation, vehicle loading, battery age, auxiliary transients or charging losses. An engineering decision needs parameter bounds, measured calibration data and a scenario-specific reserve policy.

The ideal fleet capacity check is another constraint: \(n\times 3\ge8\). Candidate A (two vehicles) fails the bound; B (three) and C (four) satisfy it. Energy and throughput are therefore distinct feasibility filters. A vehicle count alone does not prove shift-range sufficiency, and a battery margin alone does not prove peak-hour service.

### When uncertainty matters

For small uncertainty about inputs, a first-order propagation formula is

\[
\operatorname{Var}(E)\approx\nabla E^{\mathsf T}\Sigma\nabla E,
\]

where \(\Sigma\) includes cross-covariances. Treating route length, energy rate and auxiliary demand as independent is an assumption, not a default fact. For highly nonlinear or bounded quantities, use scenario propagation or Monte Carlo with a justified joint distribution, then validate the model against observed shift data. A mean that fits does not establish the upper tail needed for reserve assurance.

**Exercise with answer.** If the traction rate becomes \(0.41\ \mathrm{kWh/km}\), what is the new demand? \(E=24(1.8\times0.41+0.20)=22.512\ \mathrm{kWh}\), leaving \(7.488\ \mathrm{kWh}\). This result is a conditional model calculation, not a battery certification.
