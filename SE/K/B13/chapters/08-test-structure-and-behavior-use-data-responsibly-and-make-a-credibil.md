# Chapter 08 — Test structure and behavior, use data responsibly, and make a credibility claim

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 8 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 8](../labs/lab-08-test-structure-and-behavior-use-data-responsibly-and-make-a-credibil.md) → attempt the [original Week 8 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w08.md) remains available for a quick recap.

## The decision behind the theory

A system-dynamics model is credible for a purpose only when its structure, equations, behavior, and policy insights survive relevant tests. **Essential question:** What evidence is sufficient to use this model for policy learning, and what remains uncertain?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Testing is iterative and begins during formulation. Direct structure tests compare equations and decision rules with knowledge of the real system. Structure-oriented behavior tests examine whether the model responds correctly under extreme conditions, boundary changes, and isolated mechanisms. Behavior tests compare patterns, timing, amplitudes, turning points, and cross-variable relationships.

Fit statistics are evidence about behavior reproduction, not proof of causal correctness. Many structures can fit short, noisy data. Calibrate only parameters that have a defensible meaning and range; preserve a holdout period or behavioral feature when practical; report parameter correlations and nonidentifiability.

Reality Checks convert important expectations into repeatable assertions—for example, “with zero demand, completed trips eventually fall to zero,” or “active fleet cannot exceed total fleet.” If PLE limitations prevent direct automation, implement an equivalent documented test protocol.

Credibility is use-specific. A model may support qualitative policy learning but not point forecasting or safety certification. The use recommendation should name supported questions, unsupported uses, conditions, residual risk, and monitoring needs.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Explain delays, nonlinearities, oscillation, overshoot, and changing loop dominance**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Apply feedback modeling to supply management and inventory dynamics**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Structural tests ask whether a model deserves its behavior

A dynamic model can reproduce historical data by adjusting parameters even when its causal structure is wrong. Structural tests challenge whether each feedback, stock, flow, delay, and decision rule has a plausible mechanism. Extreme-condition tests can be particularly revealing: a service-completion function that remains positive with zero capacity violates the intended process, however well it fits ordinary observations.

Behavioral tests examine whether the simulated trajectories resemble observations and whether relevant qualitative patterns persist under alternative parameters. Neither structural plausibility nor data fit alone is enough. Data may not cover the policy intervention of interest, and several competing structures can fit the same past behavior. Credibility therefore involves triangulation: mechanism review, dimensional consistency, limiting-case tests, historical comparison, and examination of policy sensitivity. Good models make disagreement about causal explanations explicit rather than burying it in calibration.

## Deeper theory: structural credibility and policy learning in feedback models

### A good fit is a weak test of a strong causal claim

System-dynamics models are often intended to explain endogenous behavior: why decisions, delays, and accumulations produce a pattern from within the system. A model that replicates historical output could be using a genuine feedback structure or a fitted external time-series input. These are not equivalent explanations. If Northstar's maintenance backlog rises and then falls, a model might fit the curve by varying staffing exogenously, while an alternative explicitly models how backlog changes staffing decisions and training delays. Both may reproduce history; only the latter can analyze the consequences of changing the staffing rule without assuming the answer in advance.

This is a problem of structural identification. Let measured outputs be `y(t) = h(x(t), θ)` and dynamics `dx/dt = f(x,u,θ)`. Different structures and parameter sets can generate nearly identical `y(t)` over a limited observation interval. Parameter estimation cannot resolve that ambiguity by itself. Credibility therefore combines empirical fit with evidence for the hypothesized stocks, flows, feedback information, decision rules, and institutional constraints. The burden becomes stronger as the policy claim moves farther from the data used to calibrate the model.

### Testing behavior begins with conservation and dimensions

Structural tests ask whether equations respect units, nonnegativity, known capacities, and plausible directions of causation. Extreme-condition tests deliberately set important drivers to zero, very high values, or limiting values: if no vehicles can enter service, the model should not increase active fleet through a hidden path; if demand vanishes, queues must eventually clear unless another accumulation mechanism exists. A model may be numerically stable while violating conservation. Conversely, a mechanically consistent model can be inaccurate if a real behavioral feedback was omitted.

Behavior tests examine reference modes such as growth, delay, oscillation, overshoot, and collapse. They should include more than matching average magnitudes. A policy that reproduces the right end-of-year backlog by creating an impossible negative stock midyear is not credible. For simulated and measured series, a time-shifted peak may be more important than a small root-mean-square error, especially when emergency capacity is needed on a specific day. The acceptance test should follow the decision mechanism, not merely whichever goodness-of-fit statistic is easy to compute.

### Sensitivity is informative only when uncertainty is well classified

Local sensitivity estimates how output changes under a small parameter perturbation, for example `∂y/∂θ_i` near a baseline. Global analysis varies parameters over meaningful ranges, often jointly, and observes changes in output trajectories or decisions. Strong sensitivity to a staffing adjustment time is different from structural uncertainty about whether staffing actually responds to backlog. The first may be addressed with better measurements; the second requires competing models or field inquiry. Treating both as a single uniform Monte Carlo range disguises what learning is needed.

Policy conclusions also interact with uncertainty in values and incentives. A backlog-minimizing policy might increase overtime, fatigue, and future failure rates; an operating-cost metric can understate consequences for safety or access. Examine not only total backlog but peak critical-service loss, distribution of delays, unintended workload, and long-run recovery. If an intervention is favorable only when an uncertain hiring delay is implausibly short, the correct finding is conditional fragility, not a definitive improvement.

### Model credibility is a negotiated but falsifiable claim

Stakeholders may disagree about causal structure because they observe different parts of the system. Operators know workarounds; finance sees expenditure; affected travelers experience delays not captured in service databases. Such perspectives should generate explicit structural alternatives and evidence questions, not be averaged into a single consensus arrow. Document what observations would challenge each account, which mechanisms are well supported, and which exist for exploratory learning only. A credible policy model is often most useful as a disciplined way to discover nonobvious consequences and ask better questions. It should never be presented as an oracle whose numerical precision settles an organizational choice.

## Worked engineering example from the course

The model is tested against the eight-quarter synthetic data. A parameter search can fit wait time closely with both a maintenance-delay structure and an alternative trust-only structure. Cross-variable behavior reveals that the trust-only structure cannot reproduce maintenance backlog or active-fleet turning points. Extreme tests reveal negative backlog under one equation; the equation is corrected with a capacity and nonnegativity constraint. The credibility claim is limited to comparative policy learning over a five-year horizon.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Calibration to one series is weak evidence of correct structure. Test extreme conditions, dimensional consistency, parameter sensitivity, and whether the model explains multiple patterns without implausible compensating assumptions.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A maintenance stock has 30 open jobs. The next week brings 12 new jobs and 15 closures. What is the new stock?

<details><summary>Show a reasoned solution</summary>

New stock = 30+12−15=27. If the modeled closure rate exceeds available work, cap it or reformulate the flow.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* validity is based only on visual fit or R-squared;
* no alternative structure is tested;
* extreme-condition or numerical tests are absent;
* defects are corrected without regression evidence;
* the credibility claim exceeds the evidence;
* unsupported prediction or certification uses are implied.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 8](../labs/lab-08-test-structure-and-behavior-use-data-responsibly-and-make-a-credibil.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[07 — Previous chapter](07-explain-delays-nonlinearities-oscillation-overshoot-and-changing-loo.md) · [09 — Next chapter](09-apply-feedback-modeling-to-supply-management-and-inventory-dynamics.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 8

*Integrated chapter: Chapter 08 — Test structure and behavior, use data responsibly, and make a credibility claim. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Code verification, structural validity, and behavior credibility are separate gates

**Numerical verification** asks whether the written equations were implemented and solved consistently: no negative stocks, fleet balance \(A+U=14\), passenger conservation, stable answers under step refinement and repeatable fixed inputs. **Structural validation** asks whether repairs really depend on crew capacity, whether abandonment responds to delays as assumed, whether “trust” can legitimately be represented by one index, and whether passenger classes are meaningful. **Behavior validation** asks whether plausible calibrated parameters reproduce multiple independent reference modes under known uncertainty. Passing the first gate does not imply passing the second or third.

In the original eight-quarter data, maintenance backlog is expressed in **vehicle-days**, while the executable stock is **unavailable vehicles**. These are different quantities. Equating the two and choosing 24 as an initial vehicle count would fail dimensional analysis and exceed the 14-vehicle fleet bound. Likewise, the model's cumulative abandonment fraction is not the course's quarterly accessible-trip fulfillment measurement without defining compatible cohorts, counting rules and measurement processes. No actual calibration was performed; a visually plausible trajectory is not evidence of measured predictive skill.

### Falsification-oriented test matrix

The controlled script runs five policies under four declared sensitivity cases, for 20 paired outcomes. For status quo under nominal demand, 360-day cumulative completion is about **92.74%**; under demand +8% it is about **88.7%**; with failure hazard +20% it is about **91.2%**. A reviewer should examine whether the qualitative ranking is robust to plausible alternative rules—for example, introducing trip cancellation before acceptance or varying perceived backlog delay. The four cases are structured stresses, not quantiles or a confidence distribution.

Extreme tests have stronger diagnostic value than merely checking one attractive baseline. With zero active fleet, service cannot occur; with no initial backlog and no arrivals, both group backlogs must remain zero; with no repairs, unavailable vehicles cannot decrease unless a different outflow is modeled. Equations must not produce more completed trips than eligible arrivals plus outstanding work. For finite time steps, outflows must be capped so stocks cannot turn negative.

**Worked exercise.** An analyst reports a request balance residual of zero across twenty runs and calls the model “validated against observed service.” **Solution:** a conservation residual tests internal bookkeeping. It gives no information about whether observed arrivals and exits were measured, whether the synthetic trust function is defensible, or whether the correct system boundary was modeled. The appropriate claim is **verified conservation in the implemented simplified simulation**; external validation remains pending.

**Practice extension:** Develop a credible validation plan requiring anonymized rider timestamps, sampled failure/repair histories, questionnaire measurement, independent holdout quarters, and stakeholder review of accessibility metrics; state privacy and consent limits.

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
