# Chapter 10 — Extend the model to population or biological dynamics and communicate behavior through visualization

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-extend-the-model-to-population-or-biological-dynamics-and-communicat.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w10.md) remains available for a quick recap.

## The decision behind the theory

The source course includes populations, disease, visualization, and animation to broaden model-form judgment. This week uses a bounded passenger-exposure case to compare compartmental, agent, and hybrid reasoning while reinforcing ethical communication and model limits.

**Essential question:** How should model form and visualization change when the system contains heterogeneous people, contact processes, and uncertain biological behavior?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* A compartmental model groups people by state and usually assumes mixing within defined groups. It is useful for mechanisms and scenarios but may be inappropriate when contact structure and individual heterogeneity drive outcomes.
* Agent or network models can represent individual schedules, contacts, and interventions but require more data, computation, and validation.
* Keep the exercise synthetic. The purpose is model-form comparison and coupling to occupancy/ventilation, not clinical or policy advice.
* Visualization must show denominators, units, time, uncertainty, scenarios, thresholds, and events. Use accessible labels and descriptions; avoid deceptive axes or animation that implies precision.
* A good animation is reproducible from source and supports a question such as mode transition, spatial flow, heat path, or queue evolution. It does not replace quantitative analysis.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Integrate technical performance with lifecycle cost, resources, maintenance, and affordability**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Assess continuous, discrete, hybrid, fixed-step, real-time, HIL, and final credibility constraints**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Population and biological dynamics often contain nonlinear responses, delayed effects and constraints that change with state.

### Distinguishing related ideas

A model calibrated during low load may fail when saturation, adaptation or resource exhaustion changes the governing mechanism.

### Interpretation and boundary conditions

Drawing a plausible curve is not validation; the model must represent the processes believed to create that curve.

## Worked engineering example from the course

A synthetic SEIR model represents a 1,000-person campus population while shuttle occupancy and ventilation change effective contact during trips. A homogeneous-mixing model predicts little difference among routes; a schedule-stratified model identifies one high-occupancy transfer period as dominant. Because transmission and contact parameters are illustrative, the result is presented only as a demonstration of model-form sensitivity, not as a health recommendation.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A population model dN/dt=rN(1−N/K) with r=0.2/month and K=1000 grows initially faster at small N and slows near carrying capacity. Do not map the equation onto real populations without validating meanings of N, r and K.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** At constant 12 m/s, deceleration of 2 m/s² gives what ideal stopping distance?

<details><summary>Show a reasoned solution</summary>

d=v²/(2a)=144/4=36 m, excluding delays, grade and friction uncertainty.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: population dynamics and visualizations as causal models

### Choose a model structure that preserves physical meaning

Population models are valuable for understanding flows among states, but the terms must represent distinct processes. A simple susceptible–infected–recovered system uses `dS/dt = −βSI/N`, `dI/dt = βSI/N − γI`, and `dR/dt = γI`, where `N = S + I + R` is constant when births, deaths, and migration are excluded. The conservation equation follows by adding the three derivatives: the flows cancel. If a simulator allows the total to drift substantially under a closed-population assumption, the error may lie in numerical integration, units, or implementation logic.

The parameter `β` represents effective transmission per unit time under the model's mixing assumption, and `γ` represents recovery rate. The basic reproduction number in this homogeneous model is `R₀ = β/γ` when almost everyone is susceptible. That ratio is not portable without qualification to heterogeneous networks, changing contact behavior, or finite seasonal populations. The same intellectual discipline applies to any resource-flow system: define states, mechanisms, units, conservation rules, and boundary processes before animating outputs.

### Distinguish observation, latent state, and policy response

Measured case counts are not identical to actual infection prevalence: reporting rates, detection delays, and behavior may change together. An observed decline can reflect fewer infections, lower testing, or slower reporting. If the model is calibrated only to visible counts, multiple parameter combinations may reproduce the same curve. This is *non-identifiability*. More graphical detail cannot solve it. Additional measurements, experimental contrasts, or explicit uncertainty bounds are required to distinguish competing hypotheses.

Visual communication can intensify the problem. A smooth animated map suggests continuous certainty even when observations are sparse and model predictions vary widely. Display uncertainty intervals, population denominators, data provenance, and the distinction between historical observation and forecast. A color scale with changing limits can make an unchanging process look dramatic; fixed and labeled scales are essential when viewers compare time steps.

### Transfer the reasoning back to engineering systems

Northstar's demand, fleet, and service processes also exhibit stocks, flows, and feedback. Passengers waiting at stops form a stock, new arrivals are an inflow, and boarded passengers are an outflow. If `W(t)` denotes people waiting, `dW/dt = arrivals(t) − boardings(t)` in a simplified continuous approximation, with `W >= 0` and boarding constrained by capacity. A simulator that boards more passengers than are waiting violates the intended semantics even if an animation appears smooth. Demand adaptation can create endogenous feedback: long waits reduce future ridership, masking poor service if the analyst reports only observed queue length.

A responsible complex-systems visualization therefore communicates *mechanism and uncertainty* together. Show what flows cause changes, which variables are unobserved, and which assumptions are merely scenario choices. Biological dynamics are not a decorative analogy; they teach why systems with similar-looking curves can have very different causal structures and require different interventions.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Synthetic results are presented as real health evidence or advice.
* Homogeneous mixing or contact structure assumptions are hidden.
* Visualization omits denominator, uncertainty, or scenario conditions.
* Animation replaces rather than supports analysis.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is homogeneous mixing?
2. Why use an SEIR rather than SIR model?
3. When prefer an agent model?
4. What is visualization validity?

<details><summary>Explain the answers</summary>

**1. What is homogeneous mixing?** An assumption that contacts occur uniformly within the modeled population or group.

**2. Why use an SEIR rather than SIR model?** To represent a latent exposed period when it matters to timing.

**3. When prefer an agent model?** When individual heterogeneity, networks, schedules, or localized interventions drive the question.

**4. What is visualization validity?** The view accurately represents controlled data, scales, uncertainty, and model meaning.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-extend-the-model-to-population-or-biological-dynamics-and-communicat.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-integrate-technical-performance-with-lifecycle-cost-resources-mainte.md) · [11 — Next chapter](11-assess-continuous-discrete-hybrid-fixed-step-real-time-hil-and-final.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: population dynamics and truthful visualization

### Why a population model belongs in an advanced simulation course

A battery-electric shuttle is a cyber-physical system. The source-course scope also asks students to model population and biological dynamics, which are structurally different but share requirements for governing equations, state constraints, parameter meaning, initial conditions and numerical checks. Treat the biological example as a *separate educational extension*, not as an epidemiological forecast or an assertion about a real health system. The common theme is how stocks, flows and feedback create time-dependent behavior and how visual output can mislead decision makers.

A minimal SIR stock model partitions a fixed synthetic population \(N=S+I+R\) into susceptible, infectious and removed states:

\[
\dot S=-\beta SI/N,\quad
\dot I=\beta SI/N-\gamma I,\quad
\dot R=\gamma I.
\]

The rates \(\beta,\gamma\) have inverse-time units; \(N\) is constant only in this closed, no-demography abstraction. Summing equations yields \(\dot N=0\), an invariant that a numerical model should preserve to within integration error. For \(N=1000\), initial \(S=990,I=10,R=0\), \(\beta=0.25\,\mathrm{day}^{-1}\) and \(\gamma=0.10\,\mathrm{day}^{-1}\), initial derivatives are \(\dot S=-2.475\) persons/day, \(\dot I=+1.475\) persons/day, \(\dot R=+1.0\) persons/day; the sum is zero. The initial effective reproduction quantity in this simplistic homogeneous model is \(\beta S/(\gamma N)=2.475\). These values are fully invented teaching inputs and cannot guide public-health policy.

### Compare differential and discrete implementations

A forward-Euler daily update \(S_1=S_0-h\beta S_0I_0/N\), and similarly for \(I,R\), preserves total \(S+I+R\) algebraically if the same flow is credited/debited. For \(h=1\) day, the first state becomes \((987.525,11.475,1.0)\). Larger \(h\) can drive stocks negative despite a mathematically nonnegative continuous solution; use smaller steps or a positivity-preserving integrator for credible long-term runs. Parameter uncertainty and changing contact networks can dominate numerical truncation error. Even when an ODE integrates correctly, lack of observed population-mixing structure can invalidate any forecast.

The shuttle has analogous conservation constraints: battery energy decreases by consumptive power, thermal energy changes by heat-generation minus rejection, mechanical work changes kinetic/potential energy. A plot that smooths state discontinuities or suppresses a negative stock gives the appearance of correctness while hiding a broken invariant. Plot *both* the primary state and the conservation residual where practical.

### Visualization is an evidence interface

For a vehicle duty-cycle plot, the x axis must say **time in minutes**, not “iteration”; the y axis must state **pack temperature °C** or **SOC fraction**, not an ambiguous “performance.” Annotate the 44°C warning and 48°C limit separately, and avoid implying a temperature band is an uncertainty interval unless it is generated by a specified uncertainty method. The recorded [lap trace](../tools/step03_book12_coupled_vehicle.py) can reproduce the pack's synthetic temperature and SOC at each of 24 lap boundaries using `return_trace=True`. A single curve has no validated field confidence interval.

Static snapshots can hide event ordering. If an animation interpolates between states, disclose whether interpolation is purely cosmetic or part of the numerical integrator. If a route visualization uses non-geographical segments with fictitious grades, do not overlay them on real campus roads without correcting geometry and elevation closure. Use accessible text alternatives and tables for critical values; visualization cannot replace a traceable CSV or scientific argument.

### Two worked interpretation failures

First, a monotonic declining SOC line seems reassuring at 84 km if it ends above 20%. But because the case's 24-lap route has nonzero net elevation gain, its energy number is a sensitivity teaching result, not a validated range estimate. Second, an SIR curve may show a smooth infection peak at a deterministic \(\beta\) even though true contact structure is heterogeneous, interventions change with time, and an individual-based model may yield a very different distribution. In both cases the “smoothness” of the curve says almost nothing about model validity.

### Exercises and explained answers

**A.** Calculate SIR derivative conservation. **Answer.** \(\dot S+\dot I+\dot R= -\beta SI/N+(\beta SI/N-\gamma I)+\gamma I=0\); the flow between compartments cancels. If a coded model changes \(N\) with no declared births/deaths, it has a bookkeeping defect.

**B.** What is one false claim an 84 km SOC plot could suggest? **Answer.** “Real-world range is established.” The plot shows a deterministic abstract mission with fixed auxiliary loads, no stop dwell, and artificial grade topology. Pair it with the boundary and missing evidence.

**C.** A warning line is 44°C but the modeled maximum 41.88°C. Is the hardware qualified? **Answer.** No. Spatial cell temperature, initial hot soak, sensor bias, cooling faults, pack aging and validated duty-cycle conditions are not represented.

**Deliverable:** one population-balance calculation, one model-output visualization annotated with units and limitations, and a visualization audit documenting what a viewer might falsely infer.
