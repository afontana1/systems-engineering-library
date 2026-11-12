# Chapter 07 — Explain delays, nonlinearities, oscillation, overshoot, and changing loop dominance

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 7 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 7](../labs/lab-07-explain-delays-nonlinearities-oscillation-overshoot-and-changing-loo.md) → attempt the [original Week 7 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w07.md) remains available for a quick recap.

## The decision behind the theory

Many policies fail because decision makers underestimate delay, saturation, and the way dominant feedback changes over time. **Essential question:** Which dynamic structures generate the observed transition from improvement to stress and recovery?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Delays have different meanings. A material delay represents entities moving through stages; an information delay represents gradual perception or reporting; a decision delay represents time to authorize action; an implementation delay represents time to create capacity. Choosing a delay function only for curve shape weakens causal validity.

Nonlinearities are expected in real systems: capacity limits, thresholds, congestion, fatigue, learning curves, and response saturation. Use lookup functions when the relationship is bounded, documented, and hard to express analytically. Test endpoints and extrapolation.

Oscillation typically requires balancing feedback with delay or inertia. Overshoot requires growth that continues after the system passes a sustainable level because limiting feedback is delayed. Collapse requires damage to carrying capacity or another reinforcing decline mechanism.

Loop dominance is a qualitative explanation of which feedback contributes most to behavior in a period. Do not infer dominance solely from loop count or visual prominence. Use structure experiments: disable, weaken, or isolate loops and compare behavior while respecting model meaning.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Implement and verify the first executable Vensim model**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Test structure and behavior, use data responsibly, and make a credibility claim**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Delays can turn locally corrective policies into oscillating or overshooting systems because feedback acts on outdated state.

### Distinguishing related ideas

Increasing controller aggressiveness is not always faster recovery; with sufficient delay it amplifies alternating over- and under-correction.

### Interpretation and boundary conditions

Distinguish physical lags, information delays and decision delays because they invite different interventions.


## Deeper theory — why corrective feedback can create oscillation

### Feedback is a dynamic relationship, not a circular arrow

A balancing loop aims to reduce a difference between desired and actual conditions. It is tempting to assume that stronger corrective action always improves performance. But a controller acts on information that may be delayed, filtered or noisy, and its actions may affect a stock gradually. Strong action in response to stale information can overshoot the target, triggering an opposite correction and producing recurring oscillation. The loop is “balancing” in intent while its realized behavior may be unstable.

Consider a shuttle operator trying to keep backlog near a target level. When backlog exceeds the target, the operator adds temporary capacity. When it falls below, capacity is removed. If vehicles require hours to redeploy, or reports reflect yesterday's demand, the control action may arrive after the need has passed. An increase in staffing can then become excessive capacity; the next report triggers a decrease; and the system repeats the pattern. This can happen without any irrational actor. Individually reasonable delayed decisions collectively create the observed dynamics.

### A deliberately simple difference-equation model

Let \(x_k\) be deviation from a desired stock at discrete time \(k\). Suppose the controller applies a fraction \(g\) of the measured error each period. With no sensing delay, a linear approximation is

\[
x_{k+1}=x_k-gx_k=(1-g)x_k.
\]

The deviation contracts when \(|1-g|<1\), which implies \(0<g<2\). For \(0<g<1\), correction is monotone. For \(1<g<2\), the sign alternates but the magnitude decays: overshoot occurs without divergence. At \(g=1.2\), the deviation is multiplied by -0.2 every period, so the system converges quickly in this idealization. This is a statement about a simplified linear, unconstrained discrete system—not a universal rule for real fleet operations.

Now suppose feedback is delayed by one full period:

\[
x_{k+1}=x_k-gx_{k-1}.
\]

Looking for solutions of the form \(x_k=r^k\) yields the characteristic equation \(r^2-r+g=0\). When its roots are complex, their product is \(g\), so their modulus is \(\sqrt{g}\). For \(g=1.2\), the modulus exceeds one: oscillations grow rather than decay. The same nominal corrective gain that was stable with immediate information becomes unstable with a one-period delay. That is a precise illustration of why timing belongs in causal explanation.

### Nonlinearity can limit or worsen the oscillation

Real policies saturate. Only a finite number of drivers can be called in, only so many vehicles can charge, and overtime becomes costly. Saturation can bound an unstable cycle, producing persistent oscillation instead of unlimited growth. It can also create *integral windup*: a controller accumulates a large internal corrective signal while an actuator is already at its limit, then overshoots badly once conditions change. Hysteresis or dead bands may avoid unnecessary switching, but at the cost of accepting a range of deviations around the target.

Delays also arise in several places: sensing, reporting, authorization, resource recruitment, physical movement and the effect of actions on accumulated work. Treating all of them as one unspecified “delay” can disguise the correct intervention. Faster dashboards will not fix a six-week vehicle procurement delay; buying vehicles will not fix incorrect backlog reporting. A useful model separates delay mechanisms when their intervention implications differ.

### Changing loop dominance and policy resistance

A system may initially be governed by one feedback loop and later by another. Adding vehicles can reduce waiting, encouraging more passengers to use the service. Demand then increases, eroding the original benefit. In the short run, extra capacity is a balancing response to congestion; in the longer run, induced demand can create a reinforcing mechanism. This does not prove the intervention was misguided; it means the policy changed the environment in which its own success is measured.

Similarly, a process-improvement program may reduce backlog while staff are fully engaged, but as pressure falls, management withdraws resources and backlog returns. The system resists a policy not because people dislike improvement, but because the policy changes incentives and constraints. Feedback models allow such explanations to be made explicit, compared with data and challenged by competing hypotheses.

### Interpretation before intervention

A causal-loop diagram identifies candidate feedback structures; it cannot by itself establish their quantitative importance. To explain timing, oscillation or stability, a model needs stocks, rates, delays and a defensible time horizon. Calibration against one attractive historical curve does not establish that an intervention will work in a different demand regime. Responsible use compares several plausible structures and asks which predictions would discriminate among them.

The central conceptual lesson is that *good intentions are not a stability proof*. Effective system design must consider how information arrives, how quickly action changes state, where saturation occurs and whether the intervention creates new incentives. Sometimes the highest-leverage solution is not stronger correction; it is shorter delays, clearer state information, slower gain or a changed operating rule.

## Worked engineering example from the course

Add a trust perception stock with a three-month adjustment time and a maintenance-capacity fatigue lookup. Demand grows through trust and service quality, while maintenance backlog reduces active fleet after a delay. The model initially shows growth, then overshoot and oscillatory recovery. A structure experiment removes the trust delay; oscillation decreases. Removing maintenance fatigue prevents collapse but not initial overshoot. The example demonstrates changing loop dominance rather than attributing behavior to one permanent loop.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A capacity expansion can initially reduce backlog then trigger induced demand, eventually increasing it again. Delays can make policies look successful for weeks and fail months later. Model horizon must be long enough to observe the delayed effect.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A service backlog begins at 40 requests, with 12 new requests and 9 completions per day for 5 days. Compute the ending stock.

<details><summary>Show a reasoned solution</summary>

Backlog = 40 + 5×(12−9)=55. This is a stock balance, not a claim about service quality.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* delay type is selected only to improve fit;
* lookup endpoints or units are undocumented;
* oscillation is accepted without time-step testing;
* loop dominance is asserted without structure experiments;
* saturation or physical bounds can be violated;
* the model adds complexity without improving explanation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 7](../labs/lab-07-explain-delays-nonlinearities-oscillation-overshoot-and-changing-loo.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[06 — Previous chapter](06-implement-and-verify-the-first-executable-vensim-model.md) · [08 — Next chapter](08-test-structure-and-behavior-use-data-responsibly-and-make-a-credibil.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 7

*Integrated chapter: Chapter 07 — Explain delays, nonlinearities, oscillation, overshoot, and changing loop dominance. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Perception delay and nonlinear response form a behavioral mechanism

The operations team does not respond directly to true requests in the system; its staffing/dispatch response depends on perceived backlog \(P\), an informational accumulation with \(dP/dt=(B-P)/\tau_P\) and \(\tau_P=18\) days. Under a fixed true backlog step from 0 to 100 requests, this first-order stock responds as \(P(t)=100(1-e^{-t/18})\). After 18 days, perception has reached only 63.2% of the new level; after \(18\ln 2\approx12.48\) days, it is halfway there. This lag is not a literal 18-day transportation delay and should not be implemented as such without evidence.

The dispatch surge rule saturates with information: \(s(P)=s_{max}P/(P+380)\), dimensionless, so for \(s_{max}=0.12\), at perceived backlog 380 requests, the surge is 0.06 and cannot exceed 0.12. Its slope \(ds/dP=s_{max}\cdot380/(P+380)^2\) decreases with increasing backlog. This nonlinearity prevents unlimited overtime in the toy model and creates a changing feedback gain. Wear increases breakdown hazard by \(1+1.8s\), so a corrective response has a delayed adverse side channel through unavailable vehicles. Whether the actual system oscillates depends on feedback strengths and timing; an 18-day smoothing stock alone does not establish oscillation or instability.

### Worked delay and sensitivity examples

At \(P=310\) requests, \(s=0.053913\); at \(P=690\) requests, \(s=0.07738\). Doubling perceived backlog from 310 does not double surge because the function saturates. If 12 active vehicles each deliver 93 potential trips/day, the change in surge from 0.0539 to 0.0774 changes instantaneous capacity by only \(12\times93\times(0.0774-0.0539)\approx26.2\) trips/day, before considering wear, fairness and demand feedback. This is a partial derivative demonstration, not an actual predicted policy outcome.

The model's status-quo nominal mean active fleet (11.995) differs from the surge-only mean (11.869), even while surge-only increases completion. The two variables move differently because overtime changes both capacity and failure hazard; the decision maker should not focus on output alone. Sensitivity cases with a 20% higher breakdown hazard test whether the ranking survives an adverse maintenance environment.

**Worked exercise.** A student claims that increasing \(\tau_P\) from 18 to 36 days doubles the final backlog. **Solution:** that claim does not follow from the delay equation. It changes the temporal response to backlog, and feedback with capacity and wear can affect the long-run trajectory nonlinearly. One must rerun the coupled equations, compare time histories and inspect possible instability rather than assume a proportional effect.

**Practice extension:** Sketch the true-backlog and perceived-backlog curves after a step change, annotate half-times, and distinguish immediate surge effects from deferred failure effects.

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
