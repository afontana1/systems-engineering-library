# Chapter 10 — Apply systems thinking to healthcare and human-service delivery

**Technical concept reading:** [Reference method: healthcare and human-service systems](../../encyclopedia/healthcare-and-human-service-systems.md). This reference includes assumptions, worked results, limits and a solved exercise.

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-apply-systems-thinking-to-healthcare-and-human-service-delivery.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w10.md) remains available for a quick recap.

## The decision behind the theory

Healthcare and other human-service systems combine physical flow, clinical or service need, workforce capacity, behavior, access, quality, and delayed outcomes. **Essential question:** How can policies that improve throughput locally worsen system demand, workforce capability, or patient outcomes over time?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Aggregate healthcare models require special care. A stock may represent patients waiting for beds, patients in care, discharged patients at risk, trained staff, or staff fatigue. These aggregations support policy learning but can conceal heterogeneity, clinical pathways, and inequity.

A common feedback structure links crowding to pressure for rapid discharge, rapid discharge to insufficient transition support, transition quality to readmission, and readmission back to crowding. Another links workload to burnout, burnout to absence/turnover, staffing to workload, and workload back to burnout.

Policies should be portfolios: inpatient capacity, discharge coordination, community support, workforce development, prevention, scheduling, and information. A throughput-only policy may shift burden outside the modeled boundary.

Compare model forms explicitly. System dynamics can explain long-horizon workforce and demand feedback; discrete-event simulation may be needed for detailed queues, resource schedules, and patient classes. Hybrid or linked evidence may be appropriate.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Apply feedback modeling to supply management and inventory dynamics**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Design robust policy portfolios and identify leverage, resistance, and unintended consequences**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Human-service systems contain resource constraints, feedback from outcomes to behavior and delays in recognizing unmet needs.

### Distinguishing related ideas

Reducing average service time may worsen access if difficult cases are routed away from the measured queue.

### Interpretation and boundary conditions

Model both service capacity and the social process determining who arrives, waits, disengages or returns.

## Graduate depth: feedback, equity, and capacity in human-service systems

### Demand is shaped by the service itself

Healthcare and human services differ from simple production systems because service quality, access, unmet need, and client behavior feed back into future demand. A clinic can reduce its measured waiting list by restricting eligibility, while underlying need and delayed harm rise. A transportation assistance program can increase requests as reliability builds trust and previously excluded people begin to seek service. In both cases, observed arrival counts are not merely exogenous demand; they are partly outcomes of policy, reputation, and the barriers that users face.

A compact stock-flow model can distinguish `N(t)`, the stock of people needing service; `Q(t)`, the queue of accepted referrals; and `R(t)`, the stock of resolved cases. The accepted-referral flow is not identical to new need, and completion is not identical to recovery or durable resolution. A simple relation `dQ/dt = accepted_referrals - completed_cases - withdrawals` can conserve referral counts, but withdrawal should not automatically count as success. Some withdrawals represent improved need; others represent abandonment after excessive delay. Separating these causes is essential for interpreting whether queue reduction is an improvement.

### Capacity, delay, and behavioral response

Little's Law, `L = lambda*W`, relates average number in a stable system to throughput and mean time in system when its assumptions and measurement boundaries hold. It cannot by itself show why a queue exists or how a nonstationary intervention will behave. A service system with arrival rate close to maximum capacity can exhibit sharply increasing waits as utilization approaches saturation. Appointment cancellations, repeated contact, rework after incomplete assessments, and staff burnout create additional arrival and service loops that can magnify congestion.

A capacity intervention can therefore have two opposing long-run effects. More staff raise the completion rate, but lower waits can uncover latent demand. A naive evaluation comparing pre- and post-intervention queue length might judge the program unsuccessful despite improved access and outcomes. Conversely, excluding harder cases can lower average completion time while harming equity. Evaluate throughput, time to meaningful resolution, unmet need, and distribution across populations jointly; no single metric is an adequate proxy for human benefit.

### Heterogeneity, fairness, and causal interpretation

Aggregating all clients into an average patient or traveler hides differences in service requirements, urgency, geography, language access, and ability to use alternatives. Classifying needs can improve the model, but categories must be tied to legitimate decisions and protected from misuse. An expedited priority policy may reduce the worst delays for high-urgency cases while lengthening waits for lower-urgency people. An average reduction in waiting is not automatically a fair improvement. Equity analysis must state whose outcomes count, how disparate burden is measured, and which constraints cannot be traded away.

Human response also makes calibration difficult. If only successful cases have recorded completion times, the observed mean is conditioned on remaining in the system; those who abandon service are missing non-randomly. Survey responses can reflect access barriers and selection effects. Policy evaluations should examine the observation process and counterfactual alternatives, not simply fit a curve to the available cases. A systems model is valuable because it forces such missing pathways to be named, but it does not certify causal effects by virtue of having feedback loops.

### Interpreting a Northstar service policy

Assume a fictional Northstar assistance program reports a decline in its referral queue after switching to automated intake. One interpretation is genuine efficiency. Another is that users with limited connectivity have stopped applying; a third is that referrals are processed quickly but unresolved cases reenter later. Model the distinctions between need, application, acceptance, completion, repeat demand, and abandonment. The decision should rely on separate measurements for time-to-resolution, downstream outcomes, and access rather than a single 'queue cleared' indicator.

This approach connects system dynamics with operations research, human factors, and public-service governance. Queueing methods estimate congestion given a specified arrival/service process; feedback models help explain how that process changes as people react to policy. Both are needed when a policy alters the process it is intended to improve. The most credible recommendations acknowledge ethical constraints, behavior adaptation, measurement selection, and the possibility that gains in one part of the system shift burden elsewhere.

## Worked engineering example from the course

An emergency department expands rapid-discharge targets. Initially length of stay improves. Inadequate follow-up increases readmissions after a delay; workload rises; burnout and turnover reduce effective capacity; crowding returns worse than before. A portfolio combining discharge support, staffing pipeline, and upstream access improves outcomes more slowly but sustainably. The example also identifies subgroup inequity hidden by aggregate averages.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

In a clinic, a policy that reduces average intake time can increase rework when rushed assessments send patients back through the process. Service measures need repeat visits, quality and equity, not just throughput.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A maintenance stock has 30 open jobs. The next week brings 12 new jobs and 15 closures. What is the new stock?

<details><summary>Show a reasoned solution</summary>

New stock = 30+12−15=27. If the modeled closure rate exceeds available work, cap it or reformulate the flow.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* throughput is treated as the only objective;
* readmission/rework or workforce feedback is ignored;
* aggregate results are generalized to all populations without caveat;
* patient/service safety or ethical limits are omitted;
* policy benefits occur only by shifting burden outside the boundary;
* model form is not justified.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-apply-systems-thinking-to-healthcare-and-human-service-delivery.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-apply-feedback-modeling-to-supply-management-and-inventory-dynamics.md) · [11 — Next chapter](11-design-robust-policy-portfolios-and-identify-leverage-resistance-and.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 10

*Integrated chapter: Chapter 10 — Apply systems thinking to healthcare and human-service delivery. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Human-service systems have stocks, delays and unmeasured consequences

A bed/care-capacity example can be represented with occupied beds \(C\), waiting clients \(W\), admission rate \(a\) and discharge rate \(d\), all in consistent people and people/day units. The accounting law is \(dC/dt=a-d\) while \(dW/dt=\lambda-a\) when all waiting clients remain eligible and do not abandon. This is a teaching simplification only: real hospitals require illness severity, acuity, discharge placement, care pathways, staffing, safety, exclusion criteria, mortality, privacy and equity. A model of bed flow does not justify clinical prioritization.

The [worked human-service transfer](../case/human-service.csv) uses 18 beds with 15 initially occupied, demand 3.5 clients/day and a six-day mean stay represented by \(d=C/6\) discharges/day. At initial census 15, the first day's modeled discharge is \(15/6=2.5\), and admitting 3.5 leaves 16 occupied. When all 18 beds fill, daily modeled discharges approach 3.0, which is less than 3.5 incoming clients/day; the difference accumulates in the waitlist. By day 30, the model records approximately **13.11** waiting clients. This backlog is not a patient harm estimate; no outcomes or urgent exceptions are modeled.

### Feedback questions that a static throughput metric misses

One proposed real feedback channel is `occupancy ↑ → staff workload ↑ → turnover/absence ↑ → available beds or discharge capability ↓ → occupancy pressure ↑`. Another is delayed discharge support: increasing discharge-support capacity may reduce stay length but require upstream coordination and can shift costs to other services. The toy model includes neither workforce stocks nor heterogeneous stay times; presenting this causal loop as a numerical model outcome would be unjustified. It identifies what additional validation is needed.

Policy evaluation should separate protected patient outcomes from convenience measures. A solution that reduces the queue by rejecting more referrals is not equivalent to a real capacity improvement; the same boundary warning applies to the Northstar mobility abandonment flow. For healthcare use, include independent clinical governance and operational evidence before any real-world application.

**Worked exercise.** Holding 18 beds fixed, what mean stay supports 3.5 discharges/day at full occupancy under this homogeneous formula? **Solution:** solve \(18/L=3.5\), giving \(L=18/3.5\approx5.14\) days. Reducing average stay from six to about 5.14 days would make modeled full-occupancy discharge capacity equal arrivals in this *steady-state approximation*. It does **not** prove a safe or feasible discharge policy; case mix, care outcomes and day-to-day variation are absent.

**Practice extension:** Add a waiting-client abandonment/referral-out stock and discuss ethical reasons for keeping it visible rather than labeling all completed discharges “success.”

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
