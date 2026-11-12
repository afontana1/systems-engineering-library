# Chapter 10 — Build, validate, and use surrogate models without hiding approximation error

*Book 14 · EN.645.784 · Decision Science and Analytics in Systems Engineering · Week 10 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 10](../labs/lab-10-build-validate-and-use-surrogate-models-without-hiding-approximation.md) → attempt the [original Week 10 assessment](../../../C/P3/EN645784.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-784-w10.md) remains available for a quick recap.

## The decision behind the theory

A surrogate can make expensive analysis searchable, but it adds another model layer. **Essential question:** When is an approximation good enough to support design exploration, and where must the original model remain authoritative?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the decision science and analytics in systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Choose the surrogate based on intended use: interpolation, screening, optimization, uncertainty propagation, or explanation. One model may not serve all purposes.

Reserve independent validation or use cross-validation appropriate to architecture groups and data dependence. Random splits can overstate performance when nearby design points are nearly duplicates.

Evaluate error in engineering units, relative to decision thresholds, and by critical regions. Check monotonicity or physics expectations where applicable.

Frontier preservation matters: a small average error can reorder close designs or create false Pareto points.

Confirm final candidate designs with the original model. Carry approximation uncertainty into optimization and robustness analysis.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Design computational experiments to learn efficiently from the design space**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Analyze uncertainty, sensitivity, robustness, regret, and value of information**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Surrogate models approximate expensive simulations and inherit their domain, noise and bias limitations.

### Distinguishing related ideas

A high goodness-of-fit score across training points does not certify decisions near a sparsely sampled constraint boundary.

### Interpretation and boundary conditions

Use uncertainty estimates and out-of-sample checks, especially when the proposed optimum lies at the edge of the sampled region.

## Deeper theory: a surrogate model trades computational expense for a new source of uncertainty

When a high-fidelity simulation is too expensive to run thousands of times, engineers may fit a surrogate that predicts the simulation's outputs from a smaller experimental dataset. A surrogate can enable design exploration, optimization, and sensitivity analysis, but it is a **model of a model**. It inherits uncertainty from the original simulator and introduces additional approximation error. Treating a surrogate's quick answer as equivalent to a verified high-fidelity simulation erases that second uncertainty source.

### Approximation, interpolation, and extrapolation are different claims

Suppose an expensive fleet simulation maps battery capacity \(b\), charger count \(c\), and demand scenario \(d\) to missed-service percentage \(y=f(b,c,d)\). A regression or Gaussian-process surrogate \(\hat f\) is trained on selected simulation runs. Predicting at a point surrounded by representative training cases is interpolation; predicting at a new charger configuration far outside the training domain is extrapolation. A smooth interpolant may behave plausibly outside the domain even where its predictions are physically impossible. Predictions need a documented **domain of applicability**.

Approximation error should be distinguished from the stochastic output noise of the original model. If each high-fidelity simulation run includes random demand, the observed output may be \(y=f(x)+\epsilon\), where \(\epsilon\) represents finite-run variation. A surrogate fitted without addressing that noise may learn accidental variation instead of the systematic response. Replications at selected design points can help estimate the noise level; the most efficient design may allocate runs both to new design points and to replication of informative existing points.

### Why selecting only the best-looking prediction is dangerous

An optimizer using \(\hat f\) may gravitate to locations where the surrogate is overly optimistic. This is a form of **optimizer's curse**: extreme predicted values can arise partly from model error, and optimization actively seeks them out. Consequently, a surrogate-derived optimum should be checked with the authoritative simulator or real evidence. It is not enough to report low cross-validation error averaged across the whole training region if the engineering decision concentrates near a tight feasibility boundary.

For a constraint \(f(x)\leq L\), an approximate prediction \(\hat f(x)=L-0.2\) is not reassuring if credible approximation error is \(\pm 1.0\). The decision is close to the boundary at which errors change feasibility. An uncertainty-aware design might enforce \(\hat f(x)+\delta(x)\leq L\), where \(\delta(x)\) is a justified local error allowance, but a fitted standard deviation is not automatically a calibrated coverage guarantee. Its interpretation depends on model structure, sampling design, and validation.

### Active learning should follow decision value

One strategy is to add high-fidelity runs where surrogate uncertainty is large. Another is to run where the current decision may change: near a constraint boundary or among nearly tied alternatives. The second approach is often more efficient for engineering decisions because learning about an irrelevant region may not affect the recommended design. This connects surrogate modeling with value of information: the useful next experiment is the one expected to improve the decision, not necessarily the one most likely to reduce global prediction error.

A challenge arises with correlated design variables. If historic designs always paired large batteries with many chargers, a surrogate may be unable to distinguish the effect of each. A high apparent fit to the observed design combinations does not establish reliable predictions for a large battery with few chargers. Experimental design should deliberately investigate identifiable mechanisms and physically plausible combinations, rather than relying on data volume alone.

### A defensible validation argument

A useful validation strategy distinguishes training data, model selection data, and genuinely withheld test cases. Randomly splitting highly correlated replications can yield inflated confidence because nearly identical operating cases appear in both sets. Held-out scenarios should reflect the intended use: new weather conditions, different demand patterns, or alternative fleet configurations if the surrogate will be used there. Residual plots should be examined for heteroscedasticity and systematic bias, not only summarized in a single \(R^2\) value.

The most important result of a surrogate study is often the **boundary of trust**. It states which regions and decisions the approximation can support, where fresh high-fidelity runs are needed, and how predictions change as new evidence arrives. The surrogate is a tool for allocating scarce computational attention. It becomes dangerous when its numerical convenience is mistaken for independent physical knowledge.

## Worked engineering example from the course

A Gaussian process predicts wait time accurately in dense midrange designs but underestimates high-demand failure near capacity limits. A global RMSE of 0.7 minutes looks acceptable, yet several false-efficient designs appear. The use statement restricts the surrogate to screening and requires original-model confirmation within two minutes of the wait threshold.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A surrogate regression trained on x in [1,5] has no general guarantee at x=9. Validate error where decisions are sensitive, use independent holdout runs and penalize choices whose apparent advantage is smaller than approximation error.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A design succeeds with probability 0.8 for benefit $500k, otherwise loses $100k. What is expected value before acquisition cost?

<details><summary>Show a reasoned solution</summary>

EV=0.8×500k+0.2×(−100k)=$380k. A risk-averse or budget-constrained decision maker may still reject it.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Training fit is presented as validation.
* Data leakage contaminates the assessment.
* The surrogate is used outside its validated region without warning.
* Final recommendations are not confirmed with the original model.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is generalization error?
2. What is extrapolation?
3. Why assess frontier preservation?
4. What is active learning?

<details><summary>Explain the answers</summary>

**1. What is generalization error?** Prediction error on relevant unseen data.

**2. What is extrapolation?** Prediction outside or beyond the support of training data, often with greater uncertainty.

**3. Why assess frontier preservation?** Decision use may depend on relative ordering and non-dominance rather than average prediction error.

**4. What is active learning?** Selecting new expensive evaluations based on model uncertainty and decision relevance.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 10](../labs/lab-10-build-validate-and-use-surrogate-models-without-hiding-approximation.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[09 — Previous chapter](09-design-computational-experiments-to-learn-efficiently-from-the-desig.md) · [11 — Next chapter](11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) · [Book index](../README.md)

## Step 03 integrated NS-DA14.1 decision-analysis laboratory: Chapter 10

### A surrogate's test error is bounded by where it was tested

To teach computational acceleration without importing opaque libraries, NS-DA14.1 fits a quadratic surrogate by linear least squares with a small regularizer. Inputs are centered and scaled: \(u=(n-14)/4\), \(v=(c-6)/2\), \(q=(r-0.15)/0.05\). The feature vector is \(\phi=[1,u,v,q,u^2,v^2,q^2,uv,uq,vq]\). Coefficients solve \((X^TX+10^{-8}I)\hat\beta=X^Ty\) with pivoted Gaussian elimination, allowing reproduction using Python's standard library. This implementation is intentionally not a high-reliability linear-algebra library; ill-conditioning, solver choice and precision deserve independent checking on larger datasets.

**Training/holdout discipline.** The [surrogate code](../tools/step03_book14_decision.py) trains on 36 configurations (fleets 10/12/16/18, chargers 4/6/8, reserve .10/.15/.20) for a *single* fixed service architecture and policy, then evaluates 16 separately held-out combinations (fleets 11/13/15/17, chargers 5/7, reserve .125/.175). Neither training outcomes nor held-out rows are drawn from actual operations; they come from the *same analytic toy oracle*. On that in-domain test, wait mean absolute error is approximately **0.04743 min**, with maximum absolute error **0.10745 min**. Cost MAE is near arithmetic noise because the chosen cost function is within this quadratic feature family.

### Adequacy relative to a decision boundary

For each holdout \(i\), compute residual \(e_i=\hat y_i-y_i\), mean absolute error \(\mathrm{MAE}=N^{-1}\sum_i|e_i|\), and maximum absolute error \(\max_i|e_i|\). Even a 0.107-minute maximum error may be unacceptable if a hard 15-minute wait gate is separated by only 0.05 minute from an approximate prediction. A candidate at predicted 14.97 minutes should be **re-evaluated with the original function**; a surrogate's pass is not a feasibility certificate. Residual diagnostics should be reported by location in the design space, including high-demand and low-charger regions. Predictions for a different architecture, a bounded-autonomy configuration or an unobserved speed regime are extrapolations outside this fitted model.

**Exercise with explained solution.** A surrogate returns \(\hat W=14.96\) min for a design and has a 0.10745-minute maximum observed holdout error. Can the analyst certify \(W\le15\)? **Solution:** No. The holdout maximum is not a guaranteed uncertainty bound, but even using it as a screening margin gives an upper value \(14.96+0.10745=15.06745\) minutes, above the gate. The original oracle should be rerun and the model-form error/validation gap retained. In a real simulation case, propagate stochastic numerical uncertainty and metamodel approximation separately.

**Boundary warning.** Excellent agreement with the same synthetic response generator establishes surrogate *emulation fidelity only*. It says nothing about whether actual passengers, battery thermal behavior or vehicle dispatch follow that generator. Never label this surrogate physically validated.
