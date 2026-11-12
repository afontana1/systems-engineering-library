# Chapter 04 — Use archetypes and mental models to generate competing intervention hypotheses

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-use-archetypes-and-mental-models-to-generate-competing-intervention-.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w04.md) remains available for a quick recap.

## The decision behind the theory

Systems archetypes can accelerate recognition of recurring structures, but they can also become labels that replace analysis. **Essential question:** Which generic feedback structures illuminate the case, and where do they oversimplify it?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Archetypes are reusable structural hypotheses, not diagnoses. Apply them by mapping each role in the generic structure to a defined case variable, checking the causal mechanisms, and identifying the behavior the structure should generate. More than one archetype may operate simultaneously.

The mobility case may contain growth and underinvestment: better service increases demand; demand approaches capacity; performance falls; pressure for capacity investment rises, but delayed budgets and underestimation of suppressed demand limit investment. It may also contain shifting the burden: overtime and emergency maintenance relieve immediate failures while reducing time for preventive maintenance and training.

Mental models matter because decision rules are part of system structure. “Low reported accessible demand means capacity is sufficient” can create a self-sealing loop when unreliable service suppresses requests. The model should represent the operational consequence of the belief, not merely list it in a stakeholder table.

Intervention hypotheses should span event response, parameter change, information flow, rule, goal, self-organization, and paradigm. Do not declare higher leverage automatically better; high-leverage changes can be politically difficult, slow, or unsafe.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Build causal-loop diagrams as testable feedback hypotheses**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Translate feedback hypotheses into stocks, flows, units, and accumulation equations**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

System archetypes are reusable explanatory patterns that guide inquiry, not diagnoses to impose on every case.

### Distinguishing related ideas

'Fixes that fail' and 'shifting the burden' can resemble the same time series while implying different causal mechanisms.

### Interpretation and boundary conditions

Use archetypes to propose observable tests and alternative structures rather than classify an organization by metaphor alone.

## Graduate depth: archetypes as competing structural hypotheses

### Why an archetype is not a diagnosis

An archetype such as *fixes that fail*, *shifting the burden*, or *limits to growth* is a reusable description of interacting feedback loops. It is not proof that a particular organization exhibits that structure. A tempting symptom-response cycle can be produced by several distinct mechanisms, including exogenous shocks, measurement bias, delayed capacity additions, or adaptive behavior. Archetypes provide a vocabulary for generating hypotheses; their value is realized only when those hypotheses are translated into observable stocks, decisions, and delays.

Take a backlog problem. A quick remedy may authorize overtime, temporarily raising service capacity. In a *fixes that fail* hypothesis, overtime also raises fatigue and future rework, causing the backlog to return. In an alternative hypothesis, backlog grows because demand is seasonal and overtime is simply too small. Both may fit a short period of initial improvement followed by renewed delay. The two explanations imply different interventions. Before declaring a reinforcing loop, identify the proposed pathway from intervention to delayed consequence and the measurement that could reveal it.

### Translate loop stories into state variables

A proposed causal loop becomes more disciplined when expressed as a minimal state model. Let `B` be backlog, `C` effective capacity, and `F` cumulative fatigue. One possible structural sketch is `dB/dt = arrivals - completions(C,F,B)`, `dF/dt = a*overtime - b*recovery`, and `C_effective = C_nominal*g(F)`, where `g(F)` decreases as fatigue rises. The parameters `a` and `b`, and the function `g`, require evidence or clearly labeled illustrative assumptions. Writing these relations exposes that the story relies on fatigue accumulation and a consequential effect on productivity. If data show no fatigue-related decline, this candidate explanation loses support.

Loop polarity follows local causal signs, but polarity alone does not predict net system behavior. A balancing loop can overshoot because delays and adjustment gains are large; a reinforcing loop can be bounded by saturation. Loop dominance can switch with state and time horizon. Likewise, a causal diagram without explicit stock quantities may confuse a flow with its accumulated consequence. A production rate and total unfinished work are not interchangeable variables.

### Mental models, power, and changing incentives

Organizational policies are themselves responses to what decision-makers believe. Managers may perceive long waits as a staffing problem, while frontline workers attribute them to unsuitable dispatch rules and inaccessible stops. Different boundaries identify different interventions. Evidence should be gathered from both operational data and stakeholder accounts, but agreement among participants does not make a causal pathway true. Incentives also change behavior after a policy is announced: a measured target can induce reclassification of work rather than improvement in actual service.

For Northstar, contrast two hypotheses about missed accessible trips: insufficient accessible vehicles versus dispatch priority that reallocates them to general demand. A procurement proposal addresses the first; a protected-resource rule addresses the second. Simulated experiments can compare these interventions, but the model must first include the relevant rule and its governing authority. The mature use of archetypes is therefore comparative and falsifiable: retain multiple structures until evidence discriminates them, record who is affected by the boundary, and state what learning would justify changing the intervention.

## Worked engineering example from the course

Map the pattern “add overtime after missed trips” to shifting the burden. Symptomatic relief increases completed trips quickly; overtime increases fatigue and reduces training/preventive work; later errors and failures increase missed trips. The fundamental solution—workforce pipeline and preventive capacity—has a longer delay. The example then shows a legitimate role for overtime as a bounded contingency when paired with triggers, caps, and fundamental investment.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

“Fixes that fail” occurs when overtime temporarily reduces backlog but fatigue later raises errors and rework. A useful archetype identifies the delay and leverage points; simply labeling a diagram does not establish causality.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A maintenance stock has 30 open jobs. The next week brings 12 new jobs and 15 closures. What is the new stock?

<details><summary>Show a reasoned solution</summary>

New stock = 30+12−15=27. If the modeled closure rate exceeds available work, cap it or reformulate the flow.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* archetypes are used only as labels;
* case variables do not map to the generic structure;
* no disconfirming evidence is identified;
* mental models are discussed but not connected to decisions or structure;
* the learner claims one archetype proves the policy recommendation.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-use-archetypes-and-mental-models-to-generate-competing-intervention-.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-build-causal-loop-diagrams-as-testable-feedback-hypotheses.md) · [05 — Next chapter](05-translate-feedback-hypotheses-into-stocks-flows-units-and-accumulati.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 4

*Integrated chapter: Chapter 04 — Use archetypes and mental models to generate competing intervention hypotheses. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Archetypes as competing structural hypotheses

The **fixes-that-fail** archetype predicts that a short-term capacity response repairs the visible symptom but strengthens a slower mechanism that re-creates the symptom. Candidate Northstar implementation: surge staffing raises daily trip capacity, reduces backlog, adds vehicle stress and over time creates unavailable fleet. An alternative **shifting-the-burden** hypothesis would posit that repeated surge shifts resources or attention away from preventive maintenance, causing repair capability to erode. These are *different* structures: the checked synthetic model includes surge-dependent failure hazard but **does not** include a stock of management attention, organizational learning or staff burnout. It can demonstrate the first, not both.

Every archetype claim must specify what observations would contradict it. If overtime usage increases but the measured breakdown rate stays constant after controlling for vehicle age, usage hours and road conditions, the modeled wear pathway is not supported. If repair staff increases without reducing the fleet unavailable duration, a bottleneck elsewhere may dominate. Draw the competing mechanism before making a policy recommendation; archetype labels by themselves are not evidence.

### A controlled counterfactual comparison

Under identical nominal demand and failure assumptions for 360 days, the *status quo* yields about 92.74% cumulative completion and 11.995 mean active vehicles. The *surge-only* policy raises completion to about 94.97%, while mean active vehicles decline to 11.869 and surge vehicle-days approximately double from 201.2 to 401.1. These paired numbers illustrate the hypothesized side effect: short-term output benefit and a slower wear channel coexist. The more realistic hypothesis could be different—technology or labor rules may prevent this behavior—and the code itself does not prove either archetype applies at a campus.

The *maintenance-first* alternative raises mean active vehicles to about 12.709 while achieving 95.73% completion, but uses an assumed repair-effort index of 594 rather than 360. Because that index is not dollars, one cannot simply compute return on investment. Compare also access loss, variance under stress, staff burden, implementability and budget capacity; a single throughput average is inadequate.

**Worked exercise.** A director calls the surge result evidence that the “shifting the burden” archetype has been confirmed. Diagnose the mistake. **Solution:** the model increased failure hazard with surge; it did not model diversion of repair resources. Fixes-that-fail is consistent with the equations; shifting-the-burden remains a rival hypothesis requiring an endogenous maintenance-investment or skill stock. Both need real observational tests. A structure labels a candidate mechanism rather than proving a named social pattern.

**Practice extension:** Introduce a maintenance capability stock and sketch how it could recover after an investment delay, noting how you would avoid double-counting vehicles.

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
