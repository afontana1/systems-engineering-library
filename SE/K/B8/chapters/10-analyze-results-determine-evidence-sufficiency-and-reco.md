# Chapter 10 — Evidence sufficiency and decision statistics

*Book 8: System Test and Evaluation · Week 10 — Analyze results, determine evidence sufficiency, and recommend remedial action*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 10](../labs/lab-10-analyze-results-determine-evidence-sufficiency-and-reco.md) without looking at the solution → return to [Week 10 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w10.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **evidence sufficiency and decision statistics**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Analyze the planned estimand before comparing with the predeclared boundary. Missingness, selection bias, clustered trials and measurement drift can make a nominal confidence interval misleading. Distinguish statistical significance, engineering importance and safety-critical acceptance.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Evidence sufficiency is a relation between claim strength, test conditions, uncertainty and the consequence of error.

### Distinguishing related ideas

Zero observed failures gives a probability bound only under a justified sampling model; it is not proof that failures are impossible.

### Interpretation and boundary conditions

A readiness review should distinguish lack of observed problems from demonstrated confidence at the required level.

## Deeper theory: sufficiency of evidence is a decision about uncertainty

### Failure to detect a defect is not proof that none exists

A hypothesis test that fails to reject a null hypothesis has not usually established equivalence or compliance. Suppose Northstar specifies a maximum acceptable average response time. A conventional significance test against a zero-effect hypothesis can produce a large `p` value even when data are too sparse to rule out a practically important delay. An acceptance decision is better tied to a defined performance threshold, a confidence interval or other uncertainty statement, and explicit consequences of false acceptance and false rejection. Statistical significance and engineering importance answer different questions.

Equivalence testing requires predeclared bounds for differences considered practically unimportant. Noninferiority testing asks whether a proposed design is no worse than a comparator by more than an authorized margin. Both differ from claiming two systems are “the same” because a standard comparison was not significant. The margin comes from mission needs, clinical or operational relevance where applicable, and risk authority—not from choosing a value after seeing favorable data.

### One-sided claims and uncertainty budgets

If the requirement is “the mean response time must not exceed eight seconds,” the relevant inference may be an upper confidence bound on that mean, conditional on sampling assumptions and the test environment. If the requirement concerns the 99th-percentile response, a confidence bound on the mean is inadequate even if it is extremely precise. Measurement error, temporal dependence, workload shifts, and missing observations can invalidate nominal coverage. The evidence statement should distinguish what quantity was estimated from the original claim of compliance.

An illustrative observation of zero failures in 100 independent identical demands does not justify a zero failure probability. A rough one-sided 95-percent upper bound from the binomial model is about `3/100`, the familiar rule of three. That bound relies on independence, identical exposure conditions, and accurate failure detection; repeated attempts within a single common-cause scenario may provide far less information. Safety-critical rare-event claims often require architectural arguments, analysis, and fault testing in addition to operational sampling.

### Multiplicity and stopping rules matter

If engineers inspect dozens of outcomes and announce whichever result looks favorable, the nominal false-positive risk is not the advertised risk for the whole decision. Similarly, checking results after every new observation and stopping when a `p` value crosses a conventional threshold changes the procedure's error behavior. Predefine primary endpoints, the intended sample plan, acceptance rules, and how exploratory findings will be treated. Sequential or Bayesian approaches can support adaptive data collection, but only when their assumptions and decision thresholds are explicit.

A test report should separate observed data, estimation and model uncertainty, unresolved discrepancies, applicability limitations, and authorized disposition. One failed requirement cannot automatically be offset by passing many unrelated requirements; risk-critical criteria may be noncompensatory. For Northstar, evidence sufficiency means that the combined body of tests, analyses, inspections, and operational observations supports the precise configuration and use conditions proposed for approval. It is a reasoned assurance judgment with uncertainty, not the percentage of test cases marked green.

## Worked engineering case

A mean wait of 13 minutes against a 15-minute requirement is not enough if the requirement governs the 95th percentile. Data excluding unserved trips may systematically understate actual passenger burden.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Changing the acceptance rule after seeing the data is not independent evaluation. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Execute tests and control data, deviations, discrepancies, and corrective action](09-execute-tests-and-control-data-deviations-discrepancies.md); the next connection is [Evaluate operational use, deployed systems, systems of systems, AI, and autonomy](11-evaluate-operational-use-deployed-systems-systems-of-sy.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Compute a sample mean and empirical p95 with and without unserved trips; explain what is not measurable.

**Problem B — Adversarial review.** Which uncertainty most affects the readiness decision?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 10: Evidence sufficiency and decision statistics](../labs/lab-10-analyze-results-determine-evidence-sufficiency-and-reco.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 10 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Extended worked problems and lab

Study the [worked problem workshop on test evidence and readiness](../practice/readiness.md), then complete the [extended laboratory](../practice/lab-readiness.md). The exercises are separate from the original assessed coursework.
