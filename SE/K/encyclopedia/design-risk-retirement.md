# Design-risk retirement: experiments that change an engineering decision

**Reference entry · Concept design, integration and review · Worked technical treatment**

## Risk retirement is an evidence claim

A prototype or experiment **retires design risk** only to the extent that its results reduce a specified uncertainty enough to support a decision. Building a demonstrator, completing a test, or showing an attractive plot is an activity; risk reduction is a claim about the changed credibility of a failure mechanism or design assumption. State the initial uncertainty, the experiment's discrimination power, the result, and the residual risk explicitly.

An engineering experiment should identify the hypothesis, critical failure mode, controlled design version, relevant environmental conditions, measurement chain, acceptance criterion, repeatability, and proposed next action. Separate a technical feasibility experiment from qualification, production acceptance, and operational validation: the conditions and evidence scopes differ.

## A zero-failure result is not zero risk

Suppose the Campus Mobility door controller has no unsafe openings in \(n=30\) independent, identically distributed test demands under one declared bench configuration. With a binomial frequentist one-sided 95% upper confidence bound, solve

\[
(1-p_U)^{30}=0.05\quad\Rightarrow\quad p_U=1-0.05^{1/30}\approx0.0950.
\]

This result does **not** demonstrate a failure probability below 1% at 95% confidence. To establish a similar zero-failure upper bound below 1% under the same idealized independence conditions requires \(n\geq\log(0.05)/\log(0.99)\approx298.1\), so **at least 299 trials**. These calculations describe a statistical model, not real-world assurance. Common-cause errors, unrepresentative operating conditions, test article changes, and unobserved hazards can invalidate the inference.

A Bayesian calculation with a uniform \(\mathrm{Beta}(1,1)\) prior after zero failures in 30 trials yields a \(\mathrm{Beta}(1,31)\) posterior. Its one-sided 95% credible bound is \(1-0.05^{1/31}\approx0.0921\). Similar numbers arise here, but confidence and credibility intervals have different interpretations and assumptions.

## Choose the experiment that can change the choice

Imagine alternatives A and B differ mainly in door sensor latency at high temperature. A low-temperature nominal functional demonstration has little discriminatory value. An instrumented thermal sweep with fault injection can reveal a specific causal mechanism. Its experimental design should exercise threshold regions and plausible interactions, not just average operating conditions. If the unacceptable hazard mechanism cannot be excited or observed, the experiment may prove little about it, even when every recorded trial passes.

Define an **evidence-to-decision table**: hypothesis; test variable; observed response; required effect size; uncertainty; failure/acceptance rule; configuration; decision enabled; remaining questions. Stop or pivot when new results cannot materially change the chosen design, rather than indefinitely collecting convenient nominal runs.

## Prepare for a technical review

Bring the before/after risk statement, signed configuration, calibration records, raw and processed data, model assumptions, contradictory evidence, and disposition of anomalies. A high risk can remain open despite a successful demonstration; a lower residual risk can be accepted only by authorized decision-makers with the relevant scope.

## Exercise and failure modes

Recompute the one-sided zero-failure bound for 100 trials and explain why it is still above 1%. Propose a test that exposes a shared power-supply failure instead of repeated independent software invocations. Common errors include assuming test cases are independent when they share software and environment, confusing engineering demonstration with acceptance, and retiring a hazard because an associated requirement has a green status.

## References and connections

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — technical risk, integration, V&V and review processes.
- [NASA Systems Engineering Handbook, verification matrix appendix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — requirement-to-evidence structure.
- Related: [statistical acceptance](statistical-acceptance-and-confidence.md); [hazards](system-safety-and-hazards.md); [verification matrix](verification-matrix.md); [engineering reviews](architecture-review-and-evidence.md).

*Scope:* Statistical examples assume independent identical Bernoulli trials and do not certify safety or fitness for deployment.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
