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
