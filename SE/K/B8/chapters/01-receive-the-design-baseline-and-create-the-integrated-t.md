# Chapter 1 — T&E strategy and acceptance authority

*Book 8: System Test and Evaluation · Week 1 — Receive the design baseline and create the integrated T&E strategy*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 1](../labs/lab-01-receive-the-design-baseline-and-create-the-integrated-t.md) without looking at the solution → return to [Week 1 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w01.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **t&e strategy and acceptance authority**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Test and evaluation begins with claims and decisions, not available equipment. The evidence strategy names qualification, development, operational and model-based methods; each has different permissible conclusions. A stable test article and traceable decision authority are prerequisites to making an unconditional assertion.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

A test strategy chooses what knowledge is needed before which decision, instead of treating every test as equally important.

### Distinguishing related ideas

Developmental tests diagnose mechanisms; qualification tests establish bounded compliance; operational evaluations assess mission performance in context.

### Interpretation and boundary conditions

A single favorable test can support one claim while leaving the broader readiness question unanswered.

## Worked engineering case

A design arrives with twelve top-level performance claims, but three rely on unresolved map and telemetry assumptions. A readiness strategy should identify those three as conditional until the article and operating envelope are fixed.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A large volume of test data is not equivalent to evidence relevant to the review decision. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is the Phase 1 architecture and foundation books; the next connection is [Trace requirements and stakeholder expectations to objectives, methods, and critical test parameters](02-trace-requirements-and-stakeholder-expectations-to-obje.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Classify eight candidate tests as developmental, qualification, integration or operational evidence and justify each.

**Problem B — Adversarial review.** What question must the final test board be empowered to answer?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: test strategy as sequential learning under decision risk

### Tests produce evidence for decisions, not just pass/fail labels

An integrated test-and-evaluation strategy begins with the question a decision authority must answer: is a design safe to integrate, ready for qualification, compliant with a requirement, or effective in realistic operations? These are not interchangeable claims. A successful component bench test may establish dimensional or electrical compliance without demonstrating operational suitability. A successful operational exercise may support mission value without independently measuring each contractual subsystem limit. A mature strategy matches the test method, environment, instrumentation, and decision threshold to the intended inference.

Tests differ in what they can observe and control. Analysis can explore a broad parameter range quickly but depends on model credibility. Hardware-in-the-loop testing can reproduce demanding interface transitions but may omit physical coupling. Field trials capture real interaction but are often expensive, hazardous, and difficult to repeat. The efficient sequence uses lower-risk methods to eliminate weak candidates and reserves high-fidelity exposure for claims that cannot be established otherwise. This is a design of evidence, not a mandatory progression in which every test type automatically deserves equal weight.

### Uncertainty has consequences for acceptance rules

Suppose a component is required to withstand at least 100 units of load. A measured failure threshold of 104 units with a calibration uncertainty of ±6 units may not support a conservative claim of compliance, because plausible values include 98. The decision rule must specify guard bands, uncertainty interpretation, retest policy, and the relative consequences of false acceptance and false rejection. Changing these rules after seeing results creates confirmation bias. The test plan must identify what would count as failure, inconclusive evidence, and invalid execution.

Statistical success claims have their own limits. If zero failures occur in `n` independent, representative trials, the familiar approximate 95% upper bound on failure probability is `3/n` for sufficiently large `n`. At 300 trials this is approximately 1%. It does not demonstrate a failure probability of one in a million. The approximation assumes independent, identically distributed exposures and an adequately defined event. Repeating the same easy scenario 300 times is not equivalent to 300 representative mission exposures; common causes and distribution shift can dominate the risk.

### A test architecture should challenge assumptions early

Plan tests around critical interfaces, limiting modes, environmental boundaries, human actions, and fault recovery. Each planned test needs an identified requirement or hypothesis, an operating configuration, controllable inputs, observed outputs, instrumentation accuracy, and a reproducible procedure. Test cases should include adverse conditions likely to distinguish competing failure explanations. For Northstar, a booking flow should be examined under network partition, delayed acknowledgment, repeated request, loss of vehicle location, and peak demand—not only a nominal route.

The strategy is revisable as evidence accumulates. An unexpected discrepancy may warrant a new diagnostic test before the remaining qualification sequence proceeds. Yet test adaptation needs governance so that the team does not endlessly retune pass criteria around the observed behavior. The key product of test strategy is a defensible path from limited observations to bounded technical decisions, including honest identification of claims that remain untested.

## Practice before the assessed course work

[Hypothetical Laboratory 1: T&E strategy and acceptance authority](../labs/lab-01-receive-the-design-baseline-and-create-the-integrated-t.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 1 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
