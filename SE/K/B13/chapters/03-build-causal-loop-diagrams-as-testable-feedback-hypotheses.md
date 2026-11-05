# Chapter 03 — Build causal-loop diagrams as testable feedback hypotheses

*Book 13 · EN.645.781 · Systems Thinking and Systems Dynamics · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-build-causal-loop-diagrams-as-testable-feedback-hypotheses.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645781.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-781-w03.md) remains available for a quick recap.

## The decision behind the theory

Causal-loop diagrams can reveal feedback and support stakeholder learning, but vague variables and unsupported arrows create persuasive-looking fiction. **Essential question:** What causal structure could generate the reference modes, and how can each link be challenged?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the systems thinking and systems dynamics perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A CLD is a qualitative causal theory. Variables should be noun phrases representing quantities: “maintenance backlog,” not “maintenance problem”; “service frequency,” not “increase service.” Link polarity asks: if the cause increases above what it otherwise would have been, does the effect increase or decrease above what it otherwise would have been, all else equal?

Loop polarity follows the number of negative links: zero or an even number produces reinforcing feedback; an odd number produces balancing feedback. This rule is necessary but not sufficient. The analyst must still explain the loop narrative, delay, and likely behavior.

Do not draw arrows for sequence, association, flow, or “is related to.” Each link needs a causal statement and evidence grade. Record whether evidence is empirical, mechanistic, expert, analogical, or assumed. Add a delay mark only when the delay is meaningful relative to the behavior horizon.

A useful CLD is selective. A giant “spaghetti map” can display engagement while reducing insight. Use sectors, loop labels, a variable dictionary, and views for different questions. Preserve omitted mechanisms in the boundary register.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Define dynamic behavior with reference modes, evidence, and time horizons**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Use archetypes and mental models to generate competing intervention hypotheses**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## A deeper explanation: feedback is about structure, not circular arrows

### A causal loop is a hypothesis about a mechanism

It is tempting to treat a causal-loop diagram as an explanation merely because its arrows make a closed shape. But a closed loop can be drawn around almost any collection of variables. Its value depends on a plausible mechanism: what action changes which quantity, through what intermediate process, after what delay, and subject to what constraints? A causal loop is best regarded as a **hypothesis that can be challenged**, not a visual proof.

Northstar's service demand provides a useful illustration. Long waits may reduce passenger trust. Lower trust may reduce future bookings, which reduces observed congestion. If management responds only to observed queue length, it might wrongly conclude that capacity is sufficient precisely because passengers have abandoned the service. The measured variable, demand, has changed partly because the service failed. This is an example of endogenous adaptation: the system responds to its own performance, altering the data used to assess that performance.

### Positive and negative feedback are not value judgments

A reinforcing loop amplifies an initial change in its own direction; a balancing loop counteracts it. The words do not mean “beneficial” and “harmful.” A reinforcing loop can produce rapid learning or runaway failure. A balancing loop can stabilize temperature or entrench a poorly functioning policy. For example, a reputation loop—better service → greater trust → more riders → greater political support → better service—may be reinforcing and beneficial until congestion overwhelms capacity. Conversely, a control loop that reduces departures whenever operator workload rises may prevent overload but worsen passenger access.

The loop's behavior depends on more than its sign. The strength of relationships, delays, nonlinear saturation, limits, and the presence of other loops determine what happens over time. A reinforcing loop can dominate at first and then be constrained by a balancing loop; a delayed balancing response can overshoot its target and oscillate.

### Stocks create memory and inertia

A **stock** accumulates past flows. The number of pending requests is a stock; the booking arrival rate and completion rate are flows. The relationship is

\[
\frac{dQ}{dt}=\lambda(t)-\mu(t)
\]

when the server is busy and the simplified model is applicable. If arrivals exceed completions for an hour, a backlog remains even after the rates become equal. The system does not instantly return to normal. Capacity equal to current demand only prevents further growth; clearing the accumulated queue requires capacity greater than demand for some period.

This is the core explanation for why short-term fixes can fail. A policy that improves instantaneous processing speed may still leave unacceptable delays if the starting backlog is large. Likewise, organizational capability, trust, technical debt, and equipment condition all behave partly like stocks: they are accumulated slowly and cannot be restored by a single favorable event. Stocks are where systems retain their history.

### Delays change the meaning of a good policy

Suppose an operator increases resources when observed wait times exceed a target. Hiring, training, procurement, or schedule changes take time. During that delay the queue continues to grow; by the time resources arrive, demand may have shifted. If management repeatedly overreacts to delayed measurements, it may alternate between shortages and excess capacity. The intention is stabilizing, but the delayed response can produce oscillation.

Systems dynamics therefore separates **information delays** (data arrives or is interpreted late), **decision delays** (authorization and planning), and **physical delays** (capacity cannot change immediately). A diagram with all three collapsed into one arrow cannot explain which intervention will help. Reducing reporting delay may improve decisions without adding vehicles; reducing procurement delay affects a different part of the mechanism.

### Endogenous explanations compete with external explanations

If waiting time suddenly increases, an external cause—weather, road closure, demand shock—may be responsible. A feedback explanation might instead point to a locally created consequence: a dispatch rule that prioritizes short trips may leave long trips waiting, changing rider behavior and demand composition. These explanations can coexist. Good systems thinking does not insist every outcome must be caused internally. It asks which patterns can be explained by the system's own structure and which require outside disturbances.

That distinction suggests what evidence matters. Examine time histories, not only averages. Look for delays between interventions and effects. Compare competing structural explanations against observed reference patterns. Ask whether an intervention would produce different behavior under those explanations. A causal loop that fits any possible outcome offers little understanding.

### Policy resistance is often rational local behavior

An agency may introduce a booking rule intended to improve efficiency, only to find that local teams create unofficial workarounds. Labeling this “resistance to change” may miss its mechanism. The rule might impose costs on a unit whose performance is judged by a different measure; the workaround could be a rational adaptation to incompatible incentives. Once the workaround changes data quality, central management may respond with stricter rules, generating another reinforcing cycle of control and evasion.

The graduate-level lesson is that interventions change not only system parameters but also the behavior of agents within the system. A credible systems-dynamics explanation connects information, incentives, accumulated stocks, and delays to the observed time pattern. The arrow diagram is useful only when it helps tell that causal story precisely.

## The mechanism beneath the method

A causal-loop diagram is a hypothesis about feedback, not proof that a loop is present or dominant.

### Distinguishing related ideas

Polarity labels describe local directional influence, while behavior depends on strengths, delays, constraints and interacting loops.

### Interpretation and boundary conditions

A reinforcing loop can coexist with balancing limits; the observed trajectory requires understanding which mechanism dominates over time.

## Graduate depth: polarity, feedback dominance, and causal identification

### Causal-loop diagrams are hypotheses, not proof of causation

An arrow labeled positive means that, *all else equal*, an increase in the source tends to increase the target relative to what it otherwise would have been; a negative arrow means it tends to decrease it. This is a statement about the sign of a local causal response, not a claim that the variables are positively or negatively valued. A loop's sign is the product of its link signs. An even number of negative links gives a reinforcing loop; an odd number gives a balancing loop. But polarity by itself does not determine the speed, magnitude, stability, or policy value of the system's response.

Imagine a loop in which more outstanding service requests increase management pressure, which increases dispatch staffing, which increases completions, which decreases outstanding requests. This is balancing if staffing truly responds to the backlog and completions actually reduce it. The loop could still produce oscillation: delayed staffing decisions, hiring lead time, and abrupt reversal when the backlog falls may repeatedly overshoot the needed capacity. The arrow diagram contains the causal story, but not the rates or delays required to determine dynamic behavior.

### Accumulation and dimensional consistency

Feedback is especially consequential when an effect feeds a *stock*. If `B` is the backlog measured in requests, `dB/dt = arrivals - completions` has units of requests per day. A relationship such as `completions = staffing * productivity` is only meaningful if staffing is in worker-equivalents and productivity is in requests per worker-day. A causal-loop diagram that links backlog directly to wait time can omit the essential stock-flow relationship: arrivals accumulate until resources complete or abandon the work. Without the stock, an apparently plausible loop may imply unrealistically instantaneous adjustment.

Loop dominance can change with system state. At low demand, adding staff may strongly reduce backlog, whereas near road-capacity limits, congestion may neutralize the added capacity. Nonlinear saturation makes some arrows nearly ineffective in one operating range and influential in another. Even the sign of an indirect effect may change when a policy causes demand to increase; a faster service can attract additional users. Thus a loop classification is local to a modeled mechanism and does not establish a universal direction of total system response.

### Endogeneity, confounding, and intervention

A feedback hypothesis aims to explain behavior endogenously: changes arise from interactions within the declared boundary rather than being attributed entirely to external disturbances. This does not imply the boundary can exclude external shocks. The discipline is to make exogenous factors explicit, then ask how internal feedback amplifies, attenuates, or delays their effects. If requests and waiting times rise together, the relationship may reflect a common increase in demand rather than a direct effect of waiting on new requests. Correlation in a time series is insufficient to determine arrow direction.

Distinguish *observational fit* from an *intervention prediction*. Two causal stories may reproduce the same past backlog: one emphasizes demand surges, another emphasizes staffing instability. They respond differently to a staffing policy. To discriminate them, identify a natural experiment, an exogenous policy change, or measurements of intermediate mechanisms such as actual service productivity. Even then, feedback can violate simplistic before-and-after comparisons because interventions alter the very behaviors being measured.

### Interpreting Northstar policy resistance

Suppose Northstar shortens average waits by adding dispatchers. The visible early effect is a falling backlog. Months later, more users may adopt the service, shifting the arrival rate upward; leadership may then reduce resources because the backlog initially improved. The combined reinforcing adoption loop and balancing resource-response loop can restore waiting time close to its old level. An analyst who records only the early improvement may misidentify temporary relief as a durable solution.

A defensible causal-loop interpretation states the reference behavior, loop mechanisms, stock quantities, delays, alternative explanations, and evidence that would falsify the account. Then an executable stock-flow model can test whether the proposed structure actually generates the observed trajectory. The important graduate-level distinction is that a causal-loop diagram organizes mechanisms for investigation; its intuitive arrows do not replace equations, identification evidence, or careful evaluation of delayed unintended consequences.

## Worked engineering example from the course

Start with a service-growth loop: service quality → rider trust (+), rider trust → trip requests (+), trip requests → funding justification (+), funding justification → service investment (+), service investment → service quality (+). Add a capacity-stress balancing loop: trip requests → workload (+), workload → maintenance deferral (+), maintenance deferral → active fleet (−), active fleet → wait time (−), wait time → service quality (−). The example checks every polarity and shows that a “balancing” loop may create overshoot because the maintenance effect is delayed.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A reinforcing loop links higher satisfaction → more requests → more visibility → higher satisfaction, while a balancing loop links congestion → longer waits → fewer requests. A signed causal loop is a hypothesis about influence, not a quantitative dynamic model.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A service backlog begins at 40 requests, with 12 new requests and 9 completions per day for 5 days. Compute the ending stock.

<details><summary>Show a reasoned solution</summary>

Backlog = 40 + 5×(12−9)=55. This is a stock balance, not a claim about service quality.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* polarity is wrong or unexplained;
* variables are actions, judgments, or binary events;
* arrows represent sequence or correlation rather than causality;
* loop narratives do not close the feedback;
* evidence and uncertainty are absent;
* the diagram is unreadable and has no focused views.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does this conclusion depend on?

<details><summary>Explain the answers</summary>

**1. What does this conclusion depend on?** The configuration, intended use, input provenance, model assumptions, uncertainty and decision rule.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-build-causal-loop-diagrams-as-testable-feedback-hypotheses.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-define-dynamic-behavior-with-reference-modes-evidence-and-time-horiz.md) · [04 — Next chapter](04-use-archetypes-and-mental-models-to-generate-competing-intervention-.md) · [Book index](../README.md)
