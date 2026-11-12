# Chapter 11 — Design robust policy portfolios and identify leverage, resistance, and unintended consequences

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 11 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 11](../labs/lab-11-design-robust-policy-portfolios-and-identify-leverage-resistance-and.md) → attempt the [original Week 11 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w11.md) remains available for a quick recap.

## The decision behind the theory

The strongest policy is rarely the one that produces the largest improvement in one base-case run. **Essential question:** Which portfolio changes the underlying structure across plausible conditions without creating unacceptable transition or distributional harm?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Sensitivity is not leverage. A parameter may strongly affect output but be infeasible to change, while a modest rule or information intervention may restructure behavior. Leverage claims require a mechanism, feasible action, and policy experiment.

Build portfolios around complementary mechanisms. For mobility, a policy could combine preventive-maintenance capacity, staged demand growth, transparent service reliability information, accessibility reservation protection, and a budget rule tied to lifecycle condition rather than only ridership.

Test policies across demand growth, funding delay, workforce productivity, failure rate, trust response, and external shock scenarios. Examine transient burden, not only end-state averages. A policy that succeeds after five years may be unacceptable if it creates severe first-year access loss.

Policy resistance arises when actors or feedback processes offset the intervention. Anticipate adaptation: riders change behavior, staff game metrics, departments shift costs, and political support responds to visible outcomes. Create monitoring and revision triggers as part of the policy.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Apply systems thinking to healthcare and human-service delivery**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Defend the integrated systems insight, model use, and learning strategy**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Policy resistance emerges from the response of the system to intervention

A policy changes the conditions under which people and organizations make choices. Increasing inspection intensity may detect more defects initially, but it may also shift effort away from preventive maintenance, causing an eventual increase in defects. A policy that looks beneficial along a single causal path can activate compensating loops elsewhere. These effects are not necessarily irrational resistance; they may be coherent responses to incentives, resource limits, and information delays.

Robust policy design compares interventions across plausible causal structures and time horizons. It pays attention to who bears costs, who changes behavior, and what indicators might create perverse incentives. Leverage is not synonymous with a large immediate effect. Sometimes modifying a rule governing information or authority changes system behavior more durably than increasing capacity. The correct interpretation remains conditional because an intervention can alter the very relationships used to predict its outcome.

## Deeper theory: policy resistance is adaptation inside the system boundary

A policy is a proposed intervention in a system whose participants continue to make decisions after the intervention begins. This matters because the behavior being changed is often produced by feedback. Adding vehicles to a fleet can initially reduce delays. The improved service may attract new demand, increase road congestion, change maintenance loading, or prompt budget reductions elsewhere. A before-and-after comparison that holds all those responses fixed describes an intervention in a different system from the one that will actually exist.

### Structure produces the pattern, not merely the initial event

Consider a service-level gap \(e(t)=S^*-S(t)\), where \(S^*\) is desired service and \(S(t)\) is observed service. A management rule might increase investment in proportion to the gap: \(u(t)=K e(t)\). But investment takes time to become usable capacity, and measured service may reflect conditions several weeks ago. Even when the sign of corrective action is appropriate, the combination of gain, delay, and slow infrastructure can generate overshoot. Increasing \(K\) may cause a faster initial response while increasing oscillation after capacity finally arrives.

That is one form of **policy resistance**: an intervention creates compensating feedback that partially defeats the intervention. A fleet expansion might also induce new usage, changing the demand rate \(\lambda\) in the queueing model. If the model treats \(\lambda\) as constant, it can exaggerate long-term improvements. The important engineering question is not simply whether more capacity lowers delay *for fixed demand*, but how demand, pricing, perception, workforce, and maintenance respond to the changed service.

### Leverage points depend on which behavior must change

A leverage point is a place where a feasible intervention alters the system's long-run pattern meaningfully. Changing a numerical parameter can matter, but sometimes changing the information available to decision makers has more durable effects. Suppose spare-part buyers see only parts on shelves, not pending orders. Increasing safety stock may reduce immediate shortages; exposing the order pipeline changes the information structure that caused repeated overordering. The latter may reduce oscillation without permanently increasing inventory. Yet it can create new failure modes if reported pipeline information becomes stale or is manipulated.

Leverage is conditional, not mystical. A small change to an information delay may have a large effect near a stability boundary and little effect elsewhere. A change to a decision rule may create surprising behavior when the policy crosses a capacity threshold. Models should therefore distinguish **structural assumptions**—who reacts to what, with which delay—from numerical parameter choices. Sensitivity analysis of parameters is insufficient when the structure itself may be wrong.

### Policy portfolios and interaction effects

A policy portfolio combines interventions such as additional vehicles, scheduled preventive maintenance, demand smoothing, and operator training. The combined outcome is not necessarily the sum of individual gains. Demand smoothing might allow the same fleet to meet a tighter response-time target; additional vehicles might then produce little incremental benefit. Conversely, extra vehicles without charging infrastructure may increase congestion at charging stations. This is an interaction effect in the causal structure, not simply an accounting adjustment.

A robust policy should be compared across multiple plausible futures: normal demand, demand growth, equipment shortages, supplier disruption, and high-latency communications. Let \(J(p,s)\) be the outcome under policy \(p\) in scenario \(s\). A policy maximizing average performance across assumed scenario probabilities may differ from one minimizing worst-case loss. Neither objective is automatically correct; the selected decision rule reflects risk tolerance, equity commitments, and the consequences of rare failures. The presence of mathematically defined objectives does not remove the need for explicit governance choices.

### Learning policies rather than predicting the future perfectly

A systems-dynamics model usually supports **conditional reasoning**: if the represented feedbacks and assumptions hold, these patterns are plausible. It seldom justifies precise predictions far beyond its validated horizon. Policy experiments can nevertheless be useful if they distinguish mechanisms. For example, a capacity expansion and an information-delay reduction may yield similar short-term waiting times but opposite patterns in inventory, cost, and recovery after a shock. Monitoring those different signatures helps determine which hypothesis better describes the operating system.

Policy evaluation must also account for burden shifting. A fleet metric may improve because the service stops accepting requests from difficult routes; global averages improve while access worsens for the most vulnerable population. A boundary that includes only accepted requests misses this effect. Policy design is therefore a synthesis of dynamics, decision theory, measurement, and ethics: the engineer must define who is included, what adaptive behavior matters, and what would count as evidence that the intervention remains beneficial over time.

## Worked engineering example from the course

Four mobility portfolios are compared:

1. **Capacity push:** add vehicles only.
2. **Maintenance first:** increase preventive capacity and parts visibility.
3. **Demand shaping:** staged service expansion plus reservation rules.
4. **Integrated learning portfolio:** maintenance, staged growth, accessibility protections, workforce pipeline, transparent reliability metrics, and adaptive budget triggers.

The capacity push wins for first-year wait time but later increases depot congestion and backlog. The integrated portfolio improves more slowly, avoids overshoot across most scenarios, and has explicit trigger-based adaptation.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An intervention portfolio can pair added capacity with demand smoothing and preventive maintenance. Stress policy under optimistic, base, adverse and delayed-response scenarios; prefer transparent robustness criteria over one fitted optimum.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A service backlog begins at 40 requests, with 12 new requests and 9 completions per day for 5 days. Compute the ending stock.

<details><summary>Show a reasoned solution</summary>

Backlog = 40 + 5×(12−9)=55. This is a stock balance, not a claim about service quality.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* leverage is inferred only from parameter sensitivity;
* policies are compared in one base scenario;
* transition harm or implementation delay is ignored;
* model structural uncertainty is omitted;
* no ranking-reversal or threshold analysis is performed;
* recommendation lacks monitoring and revision triggers.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 11](../labs/lab-11-design-robust-policy-portfolios-and-identify-leverage-resistance-and.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[10 — Previous chapter](10-apply-systems-thinking-to-healthcare-and-human-service-delivery.md) · [12 — Next chapter](12-defend-the-integrated-systems-insight-model-use-and-learning-strateg.md) · [Book index](../README.md)

## Step 03 integrated NS-FB13.1 case: feedback, conservation, and policy learning — Week 11

*Integrated chapter: Chapter 11 — Design robust policy portfolios and identify leverage, resistance, and unintended consequences. Northstar NS-FB13.1 is a transparent teaching baseline; the following methods are not field-validated.*

### Policy portfolios require more than a single attractive baseline

The declared policies change three independent levers: maximum surge fraction, repair-capacity multiplier, and reserved accessible-trip capacity fraction. A comparison that holds only one lever constant may conceal an interaction; a portfolio that improves a mean can create additional wear, transfer burden between groups, or exceed budgets. We therefore report paired experiments with the same initial stocks and four structured conditions. The policy owner must predeclare trade-off priorities and unacceptable harms; a model cannot choose equitable outcomes autonomously.

Under nominal assumptions, **maintenance-first** achieves about 95.73% total completion with about 4.31% accessible abandonment; **combined maintenance + access priority** achieves about 95.63% total completion with roughly 0.013% accessible abandonment. Combined's slightly lower overall completion is not numerical noise to be dismissed: allocation can reserve trips for an accessible subgroup even when standard demand is high. Meanwhile, nominal standard-group abandonment in the access-first policy rises to about 8.66% versus 7.28% status quo. All outcomes are determined by a deliberately simple capacity-reservation rule and do not estimate real rider fairness.

For adverse demand (+8%), the combined policy's overall completion falls to about **91.6%** and maintenance-first to **91.8%**. A policy that passes a nominal target but fails under plausible loads may not be robust. Conversely, no monetary budget was modeled: the repair index increases from 360 to 594 for maintenance and combined, which is a relative effort surrogate only. A cost-benefit conclusion requires actual dollar estimates, procurement and staffing lead times and stakeholder-valued benefits. The original guide's improvement budget is a quarterly \$k figure and cannot be directly compared to this dimensionless index.

### A transparent decision and sensitivity record

Define outcomes: group-specific abandonment, completion-to-arrivals ratio, daily/peak backlog, active fleet, wear exposure and implementation burden. First reject variants violating non-negotiable access or safety constraints; then compare robust performance against variations in demand, failures, trust feedback and observation delay. The current experiment ranges are **not** probabilistic uncertainty distributions and contain no Monte Carlo sampling. Trace each recommendation to one or more model output fields and a named unverified assumption.

**Worked exercise.** Which policy is “best” from the nominal totals alone? **Solution:** it is underdetermined. Maintenance-first has a marginally higher completion fraction than combined, but combined strongly improves the modeled accessible outcome at increased standard abandonment and equal repair-effort index. Without an approved equity constraint, budget valuation, evidence about demand and external legal obligations, no single utility ranking is defensible. A review can state conditional dominance under an explicit chosen objective, not universal preference.

**Practice extension:** Construct a Pareto chart of completion, accessible abandonment and repair index, and report whether the status-quo policy is dominated under those *declared* metrics without claiming applicability outside the synthetic model.

### Reproduce the evidence and challenge the result

The [NS-FB13.1 case dossier](../case/INDEX.html) publishes its [controlled inputs](../case/model-inputs.json), [Python calculation model](../tools/step03_book13_feedback.py), [policy-by-condition evidence](../case/experiment-results.csv), [equation and unit crosswalk for Vensim](../case/vensim-equation-crosswalk.md), and [claim limitations](../case/credibility-register.csv). Reproduce results with `python3 SE/K/B13/tools/step03_book13_feedback.py --write` from the repository root. This is a **synthetic teaching simulation**: correctly conserving its stocks and reproducing its output does **not** calibrate the causal structure or authorize real mobility policy. The Book 11 event simulator and Book 12 physical vehicle model answer other questions and are not dynamically coupled.
