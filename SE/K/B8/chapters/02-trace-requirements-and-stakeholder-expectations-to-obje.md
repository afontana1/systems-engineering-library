# Chapter 2 — Requirements to critical test parameters

*Book 8: System Test and Evaluation · Week 2 — Trace requirements and stakeholder expectations to objectives, methods, and critical test parameters*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 2](../labs/lab-02-trace-requirements-and-stakeholder-expectations-to-obje.md) without looking at the solution → return to [Week 2 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w02.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **requirements to critical test parameters**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

The chain is need → requirement → test objective → controlled condition → measured parameter → decision rule. A critical test parameter is chosen for its influence on the operational mission, not because a sensor makes it easy to record. Acceptance rules must specify population, edge conditions and exclusions before results arrive.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### A critical test parameter is a measurable interpretation of a claim

Turning requirements into test parameters requires choosing a quantity, an operating condition, an observation method, and a decision rule. A requirement for “timely response” is not testable until the event that starts the clock and the event that stops it are defined. If the clock begins when a request enters the software but passengers experience delay before that point, the measurement may be precise while misrepresenting the operational outcome.

Measurement definitions create construct validity: do the numbers represent the property we claim to measure? Then measurement science asks whether the observations are accurate and precise enough for the threshold. A sensor with significant drift can conceal noncompliance even if repeated readings are consistent. The test designer should trace each parameter to a claim, an instrument, a calibration or reference, and the conditions under which the result will be interpreted. Testing is thus an exercise in **operationalizing meaning**, not merely collecting data.

## Deeper theory: a test objective is a claim about inference

Engineering test plans often begin by listing procedures and equipment. That approach can produce a busy test campaign without answering what the evidence is intended to establish. A better starting point is a **claim–observable–decision** chain. A requirement states a claim about the system in a specified operating context. An observable is a quantity or event that can be measured under controlled conditions. A decision rule converts observations into a conclusion with known limitations. The difficult reasoning occurs in the links between these three layers, not in the formatting of a test procedure.

Consider a requirement that 95% of trips be completed within an agreed journey-time threshold. What exactly constitutes a trip? Does the denominator include canceled, refused, abandoned or unfulfilled requests? Does the clock start at booking, promised pickup or actual boarding? Does completion mean arriving at a destination or receiving the correct notification? Each choice changes the population and event being measured. An apparently clear numerical threshold is not yet a testable specification until these operational meanings are fixed.

### Validity, repeatability and representativeness are different

A test can yield highly repeatable measurements of the wrong quantity. A dispatch simulator might reproduce exactly the same waiting times on each run, yet omit passenger boarding variability or charging interruptions that dominate the real service. Repeatability concerns variation under repeated measurement; **construct validity** concerns whether the measurement represents the intended concept; **external validity** concerns whether the findings transfer to the operational context. All three are necessary for strong evidence, and none can substitute for the others.

A useful measurement model is \(Y=h(X,E,C)+\epsilon\), where \(X\) represents system design, \(E\) operating environment, \(C\) relevant configuration, and \(\epsilon\) measurement error. A good test explains which variables are held fixed, which are deliberately varied, and which remain uncontrolled. If a latency test uses a dedicated network while field operations share connectivity with other services, the difference belongs in the evidence limitations. Repeating the dedicated-network test thousands of times does not remove the mismatch.

### Critical test parameters reflect failure mechanisms

Not every measured variable deserves equal attention. A **critical test parameter** is one whose variation or failure bears materially on the acceptance decision or mission risk. For an emergency stop, response time, sensing freshness, actuation delay and stopping distance may all be important. An average processor utilization value may be useful diagnostics but is not a substitute for observing the actual stop performance under relevant conditions.

Test parameters should arise from an analysis of what could defeat the claim. If the hazard is an outdated route permission, observing packet delivery success under ordinary connectivity does not directly test permission freshness. A test that deliberately delays or reorders updates may be more discriminating. This is why requirement traceability is not just a matrix linking IDs: it is a reasoning chain that shows **why each test would detect a relevant class of violation**.

### Statistical evidence requires a population model

Suppose a requirement concerns a failure probability \(p\). Under independent, identically distributed Bernoulli trials, observing zero failures in \(n\) trials yields a one-sided upper confidence bound \(p_U=1-\alpha^{1/n}\) at confidence level \(1-\alpha\). At 95% confidence and \(n=30\), the bound is about 9.5%, not zero. Even this bound is conditional: repeated trials on the same favorable route may not represent an operational population of routes, weather conditions, vehicle states and human interventions. Independence and representativeness are substantive assumptions, not decorations on the formula.

A confidence interval is also different from a direct probability statement about the fixed unknown parameter. Its frequentist interpretation concerns the performance of the construction procedure under repeated sampling. Engineers can use other inferential approaches, including Bayesian models, but should name the model and its assumptions rather than treating a number labeled “95%” as universal proof.

### Evidence depends on configuration and decision authority

A successful test of software version A, vehicle controller revision B and procedure C does not automatically certify a changed combination. The test record should identify those configurations, the environment, measurement methods, calibration, acceptance rule and disposition of anomalies. A test may legitimately support a limited claim, such as “the response-time target was met in the measured laboratory cases,” while leaving operational robustness undecided.

The test objective ultimately exists to support a governance decision. Acceptance criteria should be defined before observing results wherever practical, and failure dispositions should be explicit. A system that passes selected scenarios but lacks evidence for high-consequence edge cases may justify controlled continuation, redesign or additional investigation rather than a blanket readiness claim. Test engineering is the discipline of turning observations into **bounded, defensible knowledge**.

## Worked engineering case

“Measure request latency” is a task, not an objective. “Determine whether at least 95% of eligible event-day requests receive a valid decision within 2 seconds” is a decision-relevant objective; the denominator and confidence requirement remain to define.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A well-written test procedure cannot rescue an undefined acceptance criterion. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Receive the design baseline and create the integrated T&E strategy](01-receive-the-design-baseline-and-create-the-integrated-t.md); the next connection is [Design test concepts, environments, architecture, and model-based evidence](03-design-test-concepts-environments-architecture-and-mode.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Build a trace row for each of five system claims, including estimand, test article, method and decision authority.

**Problem B — Adversarial review.** Which CTP provides the most direct evidence of accessibility?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 2: Requirements to critical test parameters](../labs/lab-02-trace-requirements-and-stakeholder-expectations-to-obje.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 2 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
