# Chapter 01 — Frame the decision, distinguish problem types, and expose decision-process risk

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 1 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 1](../labs/lab-01-frame-the-decision-distinguish-problem-types-and-expose-decision-pro.md) → attempt the [original Week 1 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w01.md) remains available for a quick recap.

## The decision behind the theory

Systems engineers often begin calculating before confirming what must be decided. **Essential question:** What decision is being made, by whom, at what time, with what authority, and what common failure modes could corrupt the process before analysis begins?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A decision is a commitment to action or allocation; an analysis is evidence offered to support it. The analyst does not own every decision.

Selection problems compare predefined alternatives. Design problems create alternatives through architecture choices and continuous variables. Allocation, sequencing, portfolio, and policy decisions require different structures.

Decision quality concerns framing, objectives, alternatives, information, reasoning, commitment, and implementation. Outcome quality also depends on uncertainty after the decision.

Frame decisions with authority, deadline, irreversibility, affected stakeholders, alternatives/design freedom, constraints, downstream decisions, and criteria for reopening.

Use a pre-mortem before analysis: imagine the decision failed and identify framing, data, preference, organizational, and implementation causes.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **the preparatory technical courses**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Translate stakeholder values into objectives, measures, and value structure**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Decision analysis begins by separating factual uncertainty from value disagreement and controllable choice.

### Distinguishing related ideas

A technical problem has a known objective and constraints; a decision problem also asks whose preferences count and how uncertainty affects action.

### Interpretation and boundary conditions

Premature scoring can disguise a dispute about objectives as a numerical disagreement about alternatives.

## Worked engineering example from the course

A committee asks, “Which shuttle is best?” The corrected decision is: “By 30 November, the vice president for operations will select one 18-month campus mobility pilot package, within a $3.5M pilot authorization, to improve peak and accessible mobility while preserving a reversible path to a five-year service.” This reveals authority, deadline, scope, budget, outcomes, and reversibility.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Classify whether the task is selecting a discrete option, setting continuous design parameters, or learning about an uncertainty. The decision frame determines which analytics are useful; an optimizer cannot repair a missing stakeholder objective.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Show a reasoned solution</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Graduate synthesis: the decision frame determines the mathematics

### Classify the question before choosing a method

An engineering decision can be a feasibility question (“does any design meet all requirements?”), a ranking problem (“which admissible design is preferred?”), a portfolio choice (“which investments should be combined?”), or a sequential decision (“what should we learn before committing?”). These are not interchangeable mathematical problems. A weighted trade study is appropriate for some rankings but cannot repair an infeasible architecture. Optimization may discover a nominal optimum but cannot settle disagreements about who gets to define harm or value.

Represent a simple decision as choosing `a` from feasible actions `A`, conditional on uncertain state `θ`, with outcome model `y = f(a,θ)`. Then distinguish hard constraints `g_j(a,θ) <= 0` from a value function `V(y)`. In stochastic contexts, decide whether a requirement must hold in every credible scenario, with a specified probability, or on average. Those choices embody different risk tolerances. An expected-utility maximizer can rationally take a small probability of severe failure under one value function; an accountable public-service decision may prohibit that outcome by constraint.

### Identify structural sources of decision bias

Decision framing creates a reference class and a set of alternatives. If Northstar begins with “which autonomous shuttle should we purchase?” it excludes potential solutions such as schedule coordination, accessible demand-responsive service, or improving pedestrian connectivity. This is a *solution-biased* frame. The correct problem might be reliable, equitable campus mobility under specified demand and budget conditions. Opening the alternative set often changes the value of subsequent technical calculations more than improving precision within a restricted set.

Anchoring, sunk-cost effects, and authority pressure can influence otherwise numerate engineering teams. Guard against these with a documented objective hierarchy, predeclared acceptance constraints, independent alternatives, and a recorded comparison protocol before the favored design's results are known. Formal methods do not eliminate judgment; they make important judgment points inspectable. A decision process that changes weights after viewing the ranking may be performing advocacy rather than analysis.

### Model the decision process itself as a risk-bearing system

A decision has inputs, transformations, responsible actors, error modes, and feedback. A simple value-of-information analysis may show that a field observation could prevent an irreversible fleet purchase; the governance process must still permit time and budget for the observation. Conversely, a perfect-information strategy can be irrational when delay costs exceed the likely value of additional learning. Use decision trees to reveal sequential options and state which transitions are reversible.

For Northstar, compare an immediate six-vehicle purchase with a limited pilot plus a later expansion option. The pilot may cost more initially yet preserve flexibility if actual demand is low. Its value depends on whether observations distinguish demand states and whether expansion can occur in time. Decision science is most powerful when it exposes **the price of assumptions, the conditions for changing course, and the authority to act**, rather than treating a chosen score as objective truth.

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Decision authority or timing is absent.
* Selection and design problems are silently combined.
* A preferred solution is embedded in the decision statement.
* The pre-mortem is generic and disconnected from the case.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is decision quality?
2. What is a selection problem?
3. What is a design problem?
4. Why use a pre-mortem?

<details><summary>Explain the answers</summary>

**1. What is decision quality?** The quality of framing, objectives, alternatives, information, reasoning, commitment, and implementation—not whether uncertainty happened to produce a favorable outcome.

**2. What is a selection problem?** A decision among predefined alternatives.

**3. What is a design problem?** A decision in which alternatives must be generated through architectural or parametric choices.

**4. Why use a pre-mortem?** To expose plausible failure mechanisms before commitment and reduce overconfidence.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 1](../labs/lab-01-frame-the-decision-distinguish-problem-types-and-expose-decision-pro.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

Start of the book · [02 — Next chapter](02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 01

### Decision definition precedes algorithm selection

The **Autonomous Campus Mobility 2030** course case contains two related but different decisions. Project 1 is a *selection*: an authorized decision maker chooses one of six predefined eighteen-month demonstration packages A–F. Project 2 is a *design*: the analyst creates possible five-year mobility-service architectures and explores their parameters. In selection, the candidate list is held fixed for a controlled comparison; in design, search-space construction is itself an engineering judgment. Neither a pilot decision nor a simulated Pareto-efficient design constitutes authorization to procure, deploy autonomy, or certify accessibility.

Use this sample charter as an editable teaching artifact: **decision**—choose a *conditional pilot* from A–F; **authority**—campus operations executive with accessibility and safety signoffs; **decision date**—the governance review, not a fictitious contractual date; **decision horizon**—18 months of pilot operation; **data boundary**—the course's five-year cost estimates and specified predicted performance; **hard constraints**—the separately marked hypothetical thresholds in [decision-inputs.json](../case/decision-inputs.json); **exclusions**—vendor approval, legally sufficient accessible service, labor negotiation and field qualification. The 18-month pilot authorization cannot be inferred from five-year total-cost figures. In particular, the course's illustrative $3.5M pilot authorization mentioned in a Week 1 framing example is a different monetary boundary from the controlled **$10.4M five-year screening threshold** used in this demonstration. The latter does not establish pilot affordability.

### Formal decision object and claim chain

For a selection decision, specify a finite set \(A=\{A,B,C,D,E,F\}\), state variables \(\theta\), feasible alternatives \(F(\theta)\subseteq A\), and preferences \(V(a\mid w)\). A preference-based recommendation is \(a^*\in\operatorname{argmax}_{a\in F(\theta)}V(a\mid w)\); if \(F\) is empty, the proper result is **reframe or gather evidence**, not silently relax a safety condition. A good analysis distinguishes (1) observed or supplied course evidence, (2) assumed model relationships, (3) the stakeholder value function, and (4) authorizing governance. The six original attribute vectors are reproduced unchanged from Course Section 7, while the added thresholds, weights and scenario payoffs are new synthetic examples.

**Worked framing example.** A careless charter says “buy the best self-driving shuttle.” It implicitly narrows the option set to autonomy and may eliminate an accessible van or hybrid fleet before analysis. Our revised charter admits A–F, screens against stated accessibility, deployment and readiness thresholds, and preserves alternative generation for Project 2. An attractive score for B would not override its modeled accessibility coverage of **0.88**, sixteen-month deployment time, availability **0.940**, and integration-risk category 5 under the *illustrative* thresholds. The score is not the authority.

**Exercise and explained solution.** Suppose a sponsor raises the five-year cost cap to $11M but retains all other gates. Can B become eligible? **Solution:** No. Although $10.6M would now satisfy cost, B still fails accessible coverage (0.88 below 0.95), deployment (16 above 12), availability (0.940 below 0.95), and integration risk (5 above 3). This is why the decision charter must contain *all* gates and the review must keep a rejection register rather than simply sorting by one attribute.

**Engineering limitation.** Cognitive bias mitigation requires independent challenge, not a formula. Record anchoring toward autonomy, conflicts of interest in the candidate-generation committee, unit mismatch in cost boundaries, and missing field proof. [Full case dossier](../case/INDEX.html) links the decision charter, candidate CSV and accountable evidence register.
