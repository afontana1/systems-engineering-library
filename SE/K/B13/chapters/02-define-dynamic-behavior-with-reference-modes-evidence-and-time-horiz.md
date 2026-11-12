# Chapter 02 — Define dynamic behavior with reference modes, evidence, and time horizons

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 2 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 2](../labs/lab-02-define-dynamic-behavior-with-reference-modes-evidence-and-time-horiz.md) → attempt the [original Week 2 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w02.md) remains available for a quick recap.

## The decision behind the theory

A system-dynamics model should explain a problem’s important behavior, not merely reproduce a convenient dataset. Reference modes make that obligation explicit. **Essential question:** What historical, desired, feared, and counterfactual behavior must the model explain?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A reference mode is a qualitative or quantitative description of behavior over time that the model is expected to help explain. It is not necessarily a target for curve fitting. Several reference modes may be required because the system’s problem is the relationship among quantities—for example, completed trips improve while maintenance backlog accumulates and trust later falls.

Every graph needs a variable definition, unit, time scale, historical interval, future horizon, data source, and uncertainty note. Start the vertical axis at zero when interpretation requires magnitude, but do not force zero when it hides meaningful variation; record the decision. Avoid dual-axis graphs that imply relationships through scale choice.

Use multiple reference modes: historical behavior, a desired trajectory, a feared trajectory, and a counterfactual “without intervention” hypothesis. A target alone is not a reference mode because it says nothing about the current pattern or causal challenge.

The time horizon must include the delays through which policies produce consequences. A three-month horizon may favor overtime; a three-year horizon may reveal burnout, attrition, and declining capacity. Boundary and horizon choices are linked.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Establish why systems thinking is needed and frame a learning challenge**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Build causal-loop diagrams as testable feedback hypotheses**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Reference modes turn vague concern into behavior over time

Systems thinking begins by asking what pattern of behavior requires explanation. “Maintenance is getting worse” could mean backlog is growing, downtime is becoming more variable, costs are rising, or recovery after disruption is slowing. A reference mode records the behavior of a specific variable over a meaningful horizon and distinguishes observed data from an expected or feared trajectory. Without this discipline, the modeler may mistake a snapshot for a trend.

Time scale matters because a policy can improve a fast variable while harming a slow one. Increasing overtime may immediately reduce outstanding jobs yet gradually increase fatigue and error rates, creating future work. A reference mode should therefore consider delays and the possibility that causal relationships change dominance over time. The purpose is not to fit an elegant curve but to constrain the explanations the model must be capable of producing. A useful reference mode can be contradicted by evidence and revised accordingly.

## Graduate depth: reference modes, time horizons, and the identification problem

### Patterns in time are questions about structure

System dynamics begins with behavior over time because an explanation of a system should account for trajectories, not only a snapshot. A reference mode is a qualitative or quantitative history of a variable over a meaningful interval: growing backlog, oscillating inventory, declining service quality, or a delayed recovery. The choice of time horizon is causal. A six-day view can show a queue clearing, while a six-month view shows repeated failure because staffing attrition changes capacity. A reference mode should include units, population, aggregation interval, and evidence quality; otherwise two analysts can agree about a graph while describing different systems.

The behavior of a stock `S(t)` is governed by accumulation: `dS/dt = inflow(t) - outflow(t)`. The same observed upward trend can result from rising inflow, falling outflow, or both. Even a flat stock does not imply inactivity; it can conceal large, approximately balanced opposing flows. Consequently, a time series alone rarely identifies the underlying mechanism. A causal hypothesis must name stocks, policies, delays, and information pathways that generate the behavior and must be compared with plausible alternatives.

### Feedback and delays create characteristic shapes

For a simplified corrective process, assume the desired stock is `S_star` and the net adjustment rate is `(S_star - S)/tau`. Then `dS/dt = (S_star - S)/tau`, with solution `S(t) = S_star + [S(0)-S_star] exp(-t/tau)` for constant `S_star` and positive `tau`. The exponential shape follows from the assumed proportional adjustment law, not from a universal property of organizational recovery. If perceived stock is delayed or intervention overshoots, the shape may become oscillatory; if capacity saturates, recovery can be nearly linear and then slow sharply. Distinguishing these mechanisms determines which policy levers could actually help.

Observe also the difference between trend and variation. Daily service demand may contain weekly cycles, weather shocks, and a structural upward trend. Smoothing can reveal low-frequency behavior but also remove early warnings or create apparent lag. A reference mode should not be selected to make a favorite archetype fit. Describe plausible alternative explanations, which data would distinguish them, and how model behavior will be tested outside the calibration interval.

### Illustration: an apparently stable backlog

Northstar's average unserved-trip backlog may stay near 40 requests for several weeks. This appears stable. Yet if requests arrive at 80 per day and 80 leave, the same stock level could represent an efficient system with rapid turnover or a long-lived set of difficult accessibility requests while easier requests cycle through. Subpopulation stocks and age distributions are needed to reveal the difference. Aggregate equilibrium can coexist with inequitable delay.

A credible reference mode therefore has multiple aligned measures: backlog size, flow rates, waiting-time distribution, vehicle availability, abandonment, and service by passenger class. Each measure should have a physical or institutional definition and a trustworthy collection process. The graduate-level lesson is not that every wiggle must be explained by feedback. It is that proposed structure must reproduce the *relevant* behavior for the decision while remaining transparent about the unobserved mechanisms that could also explain it.

## Worked engineering example from the course

The dataset shows wait time improves through Quarter 3, then worsens while demand remains high. A single wait-time graph suggests a service problem. Adding maintenance backlog, active fleet, trust, and budget reveals an overshoot pattern: performance improvements increase demand; workload and deferred maintenance accumulate; availability falls; trust and funding weaken. The example distinguishes measured quarterly data from estimated trust and marks both accordingly.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A reference mode is a time-series sketch or measured trajectory with meaningful units and horizon. A target of 95% completion cannot be evaluated by a snapshot that hides weekday surges or delayed maintenance.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A maintenance stock has 30 open jobs. The next week brings 12 new jobs and 15 closures. What is the new stock?

<details><summary>Show a reasoned solution</summary>

New stock = 30+12−15=27. If the modeled closure rate exceeds available work, cap it or reformulate the flow.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* axes, units, or evidence status are missing;
* targets are substituted for historical behavior;
* a single graph is used to define a multivariable problem;
* causal conclusions are asserted from temporal sequence alone;
* the horizon excludes known implementation or maintenance delays.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 2](../labs/lab-02-define-dynamic-behavior-with-reference-modes-evidence-and-time-horiz.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[01 — Previous chapter](01-establish-why-systems-thinking-is-needed-and-frame-a-learning-challe.md) · [03 — Next chapter](03-build-causal-loop-diagrams-as-testable-feedback-hypotheses.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 2

*Integrated chapter: Chapter 02 — Define dynamic behavior with reference modes, evidence, and time horizons. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Distinguish an observed reference mode from a simulated trajectory

A behavior-over-time graph must specify its vertical quantity, unit, population, collection interval, time axis and the range of uncertainty. The course's eight-quarter table includes requests/day, completed trips/day, p90 wait in **minutes**, active fleet in vehicles, maintenance backlog in **vehicle-days**, trust in index points, and accessible fulfillment as a proportion. These should be seven **separate** properly scaled plots; putting a trust index and a service wait on one axis produces a visually persuasive but meaningless slope comparison. Quarterly p90 values are summaries of unshown trip-level waits, not individual observations or a continuous trajectory. A model that lacks travel-time distributions cannot legitimately predict the p90 wait statistic.

Form competing reference modes: sustained expansion with increasing delays, stable service after repair relief, demand reduction driven by falling trust, and recovery after a delayed investment. The key shape from quarter 3 to quarter 6 is a wait reversal (14.2 to 23.1 minutes) while active fleet falls (13.4 to 11.9); there are too few observations to infer the delay mechanism. Annotate quarter 4 as a proposed turning point, and challenge that proposal against maintenance records and changing rider mix.

### Worked baseline and measurement logic

Quarter-5 request completion ratio is \(1110/1370=0.8102\) and quarter-1 ratio is \(805/920=0.8750\). Calling these *same-quarter completion-to-request ratios* avoids pretending they are individual fulfilled-trip fractions: carryover work may make the numerator and denominator represent different cohorts. The model instead reports cumulative completions divided by cumulative arrivals over 360 days, with explicit starting and ending backlog. Its status-quo nominal ratio is about **0.92736**, which must **not** be used to overwrite the original observed ratios; different time bases and invented parameters explain the difference.

The stock-model reference mode is also bounded: initial standard backlog 265 requests, accessible backlog 45, total fleet 14 with 1.9 unavailable, trust 63, and a separate first-order perception stock. The initial active fleet of 12.1 is chosen for a synthetic starting point and is not a fitted estimate of the first-quarter fleet.

**Worked exercise.** From the course table, wait grows from 16.8 in quarter 4 to 23.1 in quarter 6. Compute the absolute change and say what remains unknown. **Solution:** \(23.1-16.8=6.3\) minutes, about 37.5% of the quarter-4 wait. We do not know rider sample sizes, confidence intervals, seasonal bias, accessibility-specific waits, or whether a small number of long waits caused the p90 shift. Therefore an apparent rising curve is a problem definition, not validation of a feedback model.

**Practice extension:** Specify two new data collections that would discriminate between delayed repair and demand-composition explanations without conflating the observed p90 with model abandonment.

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
