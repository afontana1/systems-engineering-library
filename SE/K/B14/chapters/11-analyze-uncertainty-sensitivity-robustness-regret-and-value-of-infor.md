# Chapter 11 — Analyze uncertainty, sensitivity, robustness, regret, and value of information

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 11 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 11](../labs/lab-11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) → attempt the [original Week 11 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w11.md) remains available for a quick recap.

## The decision behind the theory

A design that is preferred at nominal values may fail under uncertain demand, cost, regulation, reliability, or stakeholder preference. **Essential question:** Which recommendation remains defensible across plausible futures, and which uncertainty is worth reducing?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Keep uncertainty types separate. Aleatory variability may be inherent; epistemic uncertainty may be reducible; model-form uncertainty reflects representation; preference uncertainty reflects value disagreement.

Sensitivity asks how outputs or decisions respond to changes. Uncertainty analysis characterizes the distribution/range of outcomes given uncertain inputs.

Robustness can mean feasibility across scenarios, low regret, stable ranking, acceptable downside, or resilience to preference changes. Define it before calculation.

Correlated inputs and conditional scenarios matter. Independent sampling can create impossible worlds.

Value of information compares expected decision improvement with the cost, delay, and feasibility of obtaining information. Partial information can be more actionable than perfect-information calculations.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Build, validate, and use surrogate models without hiding approximation error**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Integrate, communicate, and defend the engineering design decision**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Information is valuable when it can change an available action

Value of information measures the expected improvement in a decision achievable by learning something before committing. This requires a model of possible observations, how those observations change beliefs, and which actions remain available afterward. A perfectly accurate test has no decision value if every possible result leads to the same preferred choice, or if the answer arrives after the decision must be made.

Sensitivity analysis is related but different: it reveals how conclusions depend on inputs or preferences, without necessarily pricing a learning opportunity. Robustness examines performance over uncertainty sets, while regret compares a selected action with what would have been chosen under better knowledge. These tools answer complementary questions. The proper choice depends on whether the central problem is ignorance about the world, disagreement about value, limited resources, or the cost of irreversibility.

## Deeper theory: robustness, regret, and the economics of learning

### Sensitivity analysis asks what moves; robustness asks what survives

An engineering decision depends on design variables `a`, uncertain conditions `θ`, and a measure of consequence `L(a,θ)`. A local sensitivity derivative near one nominal `θ_0` shows how an output moves under a small change; it does not establish whether an alternative remains acceptable across a large, interacting range. A robust decision analysis evaluates performance over a defensible uncertainty set or distribution, including adverse combinations and structural alternatives. At Northstar, a shuttle-routing design may be superior in average weather yet fail when emergency demand and road closure occur together. Testing only one parameter at a time can miss that interaction.

Expected loss `E[L(a,θ)]` is a valid criterion when probabilities and consequence scales are supportable, but it can hide low-frequency, high-severity failure. Chance constraints such as `P(delay > threshold) ≤ ε` demand a statement about which population, time horizon, and probability model apply. Distributional robustness goes further by asking whether the recommendation survives plausible changes in the probability distribution itself. The more consequential the decision, the more important it is to distinguish *known variability* from *deep uncertainty* where probabilities are poorly justified.

### Regret is comparison against a scenario-specific benchmark

For a realized state `θ`, define regret for a loss-minimizing action as `R(a,θ) = L(a,θ) − min_b L(b,θ)`. The reference action is the best one that would have been selected with hindsight for that state; it is not necessarily feasible to know the state at commitment time. Minimax regret chooses the action with the smallest worst-case opportunity loss, not necessarily the smallest worst-case absolute damage. These criteria can disagree. A policy with consistently moderate losses may have low maximum loss but nontrivial regret whenever a specialized alternative performs much better. Naming the criterion makes that conflict visible.

Regret tables are also vulnerable to omitted alternatives and arbitrary uncertainty boundaries. Adding a new highly specialized candidate can change the hindsight benchmark for every scenario. Treat a minimax-regret result as a conditional statement about the examined alternatives and scenarios. Test whether the recommendation changes when scenario extremes, stakeholder priorities, and feasible options are reconsidered. There is no universally best robustness metric; each embodies a particular concern about risk, fairness, or missed opportunity.

### The value of information depends on a future decision

For a maximization problem, the expected value of perfect information is `EVPI = E_θ[max_a U(a,θ)] − max_a E_θ[U(a,θ)]`. Under consistent utilities and probabilities it cannot be negative before information costs, because a decision maker can always ignore the information. Sample information from a noisy test has lower or equal expected value than perfect knowledge of the same uncertain state. Its net value subtracts test expense, schedule penalties, and consequences of delayed commitment.

Consider two architectures: one cheap and sensitive to communications failure, the other expensive but resilient. A field test of network congestion is worth conducting if plausible results would move the preferred design across its cost-versus-risk threshold. Measuring a parameter that changes both architectures' performance equally may improve scientific understanding without improving this decision. Evaluation therefore follows a sequence: current best action; uncertain variable that could reverse it; feasible measurement; plausible test-result distributions; updated action; cost of learning. Precision is valuable only insofar as it supports a better intervention.

### Robust policies preserve options across time

A fixed design decision differs from an adaptive policy specifying how the organization responds as evidence arrives. Modular interfaces, reserved capacity, staged deployment, and reversible pilots create real options, but maintaining them can have carrying costs. A design can be justified by its ability to adapt rather than by superior present-day performance. Such reasoning must specify triggering observations, authority to act, lead time, and what can actually be reversed. A claim that the program can “pivot later” is empty if procurement contracts or safety approval make the alternative inaccessible. The final recommendation should identify a preferred action, a credible fallback, and the evidence that would trigger reconsideration.

## Worked engineering example from the course

Design H has the best nominal value but a 24% probability of violating accessible wait under demand and charging uncertainty. Design M has 5% violation probability and low maximum regret. Additional winter charging tests have high value because they distinguish H and M; another survey of already stable cost preferences has little decision value.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Option A has guaranteed cost $100 and B costs $80 with probability 0.7 or $160 with probability 0.3: E[B]=$104. A risk-neutral chooser prefers A, but minimax regret or budget breach could change the conclusion. Show the decision attitude explicitly.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Derivation clinic: from scenario assumptions to an actionable decision

The earlier illustration compares two designs with approximately 24% and 5% chances of violating an accessible-wait target. Those percentages should **never be presented as measured results without their underlying model**. Here is a fully disclosed *hypothetical* reconstruction, which readers can reproduce in the [Bayesian and decision-analysis method guide](../../methods/bayesian-decision-handbook.md).

Assume peak demand with probability 0.30. Under peak demand, design H violates the target with conditional probability 0.60, while design M violates with probability 0.12. Outside peak demand (probability 0.70), the respective conditional rates are 0.08 and 0.02. By the law of total probability,

\[
P(V\mid H)=0.30(0.60)+0.70(0.08)=0.236\approx23.6\%,
\]

\[
P(V\mid M)=0.30(0.12)+0.70(0.02)=0.050=5.0\%.
\]

This calculation gives students an auditable mathematical basis for the comparison. It is **not a verified claim about any actual mobility system**. The input probabilities would need operational evidence, justified conditioning assumptions, sensitivity analysis, and a calibrated model before a deployment decision.

### Price an imperfect observation before choosing the architecture

A different decision concerns whether to buy diagnostic information about a hidden controller fault. Assume a 20% prior fault probability; a faulty ship decision causes a 100 k$ loss; redesign costs 15 k$ and eliminates the modeled fault. Without testing, expected ship loss is 20 k$, so redesign is chosen. A test with 90% sensitivity and 95% specificity produces

\[
P(+)=0.9(0.2)+0.05(0.8)=0.22;\quad
P(F\mid +)=0.8182;\quad P(F\mid -)=0.02564.
\]

Since redesign is preferable when posterior fault probability exceeds 0.15, redesign after a positive and ship after a negative. The expected post-test policy loss before fee is \(0.22(15)+0.02(100)=5.3\) k$; thus EVSI is 9.7 k$, whereas EVPI is 12 k$. A 5 k$ test has **4.7 k$ net expected benefit** if there is no schedule penalty and assumptions hold. All amounts are in thousands of dollars.

The [calculator](../../methods/code/decision_test_value.py) reproduces these values and allows sensitivity changes. The key professional skill is to **recompute the optimal policy at each new parameter setting**, not simply differentiate an expected-loss formula while holding the old actions fixed.


## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Uncertainty types are collapsed into one arbitrary range.
* Dependencies are ignored despite material effect.
* Sensitivity of outputs is reported without sensitivity of the decision.
* Value of information ignores collection cost or decision timing.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is global sensitivity analysis?
2. What is regret?
3. What is robust feasibility?
4. What is decision reversal?

<details><summary>Explain the answers</summary>

**1. What is global sensitivity analysis?** Assessment of input influence across their joint uncertainty ranges, including nonlinearities/interactions depending on method.

**2. What is regret?** Loss relative to the best decision that would have been chosen for the realized state or scenario.

**3. What is robust feasibility?** Meeting required constraints across a defined uncertainty/scenario set or with a specified probability.

**4. What is decision reversal?** A change in the preferred decision due to altered data, uncertainty, preferences, or assumptions.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 11](../labs/lab-11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[10 — Previous chapter](10-build-validate-and-use-surrogate-models-without-hiding-approximation.md) · [12 — Next chapter](12-integrate-communicate-and-defend-the-engineering-design-decision.md) · [Book index](../README.md)

## Phase 4 technical reading: Safety controls are decision constraints, not just attributes

When comparing redundant sensing architectures, a design that scores best in cost/latency can still be infeasible because it fails a mandatory safety constraint. The Campus Mobility case deliberately does not give fabricated reliability estimates for alternatives A, B and C. Instead it shows how shared causes affect a toy fault tree and requires the engineer to justify probabilities before optimizing against them. A robust decision process first identifies hard controls and excluded pathways, then evaluates trade-off criteria, uncertainty, and evidence needs. Work the [connected case](../../methods/campus-mobility-engineering-case.md) and the [safety derivation](../../methods/safety-fault-trees-and-assurance.md) before reporting a preferred architecture.

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 11

### Robustness, regret and information value address different uncertainties

A finite-grid Pareto candidate can be feasible at nominal conditions and fail a structured stress. For the 18-vehicle/8-charger/hybrid/priority candidate, the nominal predicted wait is **14.0136 minutes** and availability **0.9544**. In an explicitly scripted high-demand stress, wait rises to **17.7360** minutes, above the 15-minute illustrative gate. In a `charger_loss` stress, wait rises to **15.9576** and availability drops to **0.9424**, failing both thresholds. Winter stress raises modeled energy-related annual emissions from **126.6** to **146.856 tCO2e**, though it remains within the defined *other* nominal gates. These are policy scenarios and response transformations, not a probability distribution or field predictions. The robust decision is **HOLD** pending better evidence, not “add a preference weight until it passes.”

### Derive EVPI, EVSI and a conditional policy

For a separate **C/D pilot information-value exercise**, assume state probabilities \(P(normal)=0.70\) and \(P(adverse)=0.30\). Conditional utilities are \(U(C,normal)=74\), \(U(C,adverse)=67\), \(U(D,normal)=80\), \(U(D,adverse)=57\). Without testing, \(E[U(C)]=0.7(74)+0.3(67)=71.9\) and \(E[U(D)]=0.7(80)+0.3(57)=73.1\), so D is preferred. With perfect information, take D in normal and C in adverse: \(0.7(80)+0.3(67)=76.1\) and \(EVPI=76.1-73.1=\mathbf{3.0}\) synthetic utility points. EVPI limits the gross value of information under these assumed probabilities and payoffs; it is not automatically a dollar budget.

For an imperfect diagnostic, sensitivity is 0.80 and specificity is 0.85. A positive result has probability 0.345 and posterior adverse probability \(0.24/0.345\approx0.69565\); the conditional best action is **C**. A negative result has probability 0.655 and posterior adverse probability \(0.06/0.655\approx0.09160\); the conditional best action is **D**. The probability-weighted conditional payoff is \(23.85+51.02=74.87\), yielding \(EVSI=74.87-73.1=\mathbf{1.77}\) points. With illustrative test burden 0.50 point, net value is **1.27 points**. The exact computation is reproduced in [summary.json](../case/summary.json).

### Worked regret and break-even exercise

**Exercise.** If diagnostic cost rises to 1.8 utility points, should this hypothetical test be purchased solely to improve the C/D choice? **Solution:** Net gain is \(1.77-1.8=-0.03\) points: no under the declared expected-utility assumptions. The maximum *total decision value* justifiable for this diagnostic is **1.77 points**, not EVPI 3.0. To convert to money requires a documented elicitation scale and a separate financial analysis. Moreover if the authority can defer and run a pilot to learn, the available decision strategies and payoff model change.

**Uncertainty discipline.** The 0.30 adverse probability is an elicited example, not derived from pilot integration-risk category. Do not double-count the category as a second probability modifier. For real use, audit correlation among demand, power loss, maintenance and accessible-trip failures, and account for preference disagreement and model-form uncertainty.
