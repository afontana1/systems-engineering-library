# Chapter 9 — Executing and controlling discrepancies

*Book 8: System Test and Evaluation · Week 9 — Execute tests and control data, deviations, discrepancies, and corrective action*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 9](../labs/lab-09-execute-tests-and-control-data-deviations-discrepancies.md) without looking at the solution → return to [Week 9 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w09.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **executing and controlling discrepancies**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Execution requires a contemporaneous, tamper-evident trail of what was intended, what happened and what configuration produced it. Distinguish procedure deviations, product discrepancies and environmental/instrument faults; all can affect the disposition of evidence. Retests need a trace back to root cause and controlled change.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Discrepancy management treats anomalies as possible changes to the validity of test evidence, not merely defects to close.

### Distinguishing related ideas

A failed test, a faulty instrument and a wrong test configuration require different disposition, even if they produce the same red status.

### Interpretation and boundary conditions

Reruns should explain what changed and whether earlier successful evidence remains representative.

## Deeper theory: test execution creates evidence only under configuration control

### A result is a tuple of conditions, not a pass label

A test result has meaning only as a statement about a specific item under a specific procedure and environment. At minimum, the evidentiary record should identify the system configuration, requirement version, procedure version, calibration state, input conditions, raw observations, processing rules, deviations, and decision authority. The pass/fail label is a conclusion drawn from these materials. If a software patch is installed halfway through execution but the run is reported as a single configuration, the evidence no longer supports a well-defined system claim.

Data provenance matters especially when analysis scripts transform raw observations. Filtering outliers, aligning clocks, correcting sensor offsets, and converting units may be legitimate, but each transformation changes what can be reconstructed. Keeping raw data and versioned processing instructions makes the result auditable. A beautiful final chart without reconstructable inputs cannot support the same level of assurance as an independently repeatable measurement chain.

### An anomaly is a hypothesis about the observation

An unexpected result may reflect a product failure, a flawed test setup, a measurement problem, a requirement ambiguity, or incorrect assumptions in the expected output. Declaring every anomaly a product defect wastes effort; dismissing anomalies as “test noise” hides hazards. Anomaly control should preserve the original observation, competing causal hypotheses, isolating tests, and the disposition rationale. The disposition can be “no product change” only when there is adequate evidence for that conclusion.

For example, a command delay spike during a fault-injection test might reveal a recovery algorithm that monopolizes CPU time. It might instead arise from a time synchronization error in the logger. Retesting without changing anything may reproduce a spike but not distinguish these explanations. Comparing independent clocks, inspecting CPU traces, and repeating under controlled conditions offers stronger causal discrimination.

### Retesting is not the same as demonstrating closure

When a discrepancy is corrected, the test campaign needs to establish three things: the original failure mechanism was addressed, the changed configuration meets the affected obligation, and the change did not introduce unacceptable regression. A single successful rerun can support the second point under narrow conditions while leaving the others unresolved. Regression scope should be based on dependency analysis and failure mechanism, not exclusively on organizational ownership of the edited component.

Sometimes tests cannot be repeated exactly: environmental chambers have changed, prototypes are modified, or field events are rare. In that case the record should distinguish repeated evidence from analytical equivalence arguments and document any residual uncertainty. The phrase “verified by similarity” is an engineering claim requiring justified similarity dimensions and explicit differences, not a substitute for missing data.

### Sequential observation can create selection bias

An execution team that stops testing immediately after a clean run or repeatedly adjusts conditions until a pass appears can bias apparent reliability. The stopping rule and allowed rerun policy need to be established in advance when statistical claims are intended. The probability of eventually observing a pass is not the same as the probability that a randomly selected mission will succeed. This is especially important when failures are intermittent or correlated across runs.

A trustworthy test campaign treats negative results as information, not as administrative obstacles. Preserving anomalies, deviations, and unresolved limitations allows acceptance authorities to judge what is actually known. The objective is a defensible statement about system behavior under specified conditions—not a dashboard with the highest possible percentage of green cells.

## Worked engineering case

During Step 7, a tester substitutes a spare radio with different firmware. The recorded performance may be real, but it is not evidence for the baselined article unless equivalence is demonstrated and the deviation approved.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Silently replacing a test article destroys the interpretation of a seemingly clean result. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Plan environmental, quality, reliability, maintainability, safety, and acceptance testing](08-plan-environmental-quality-reliability-maintainability-.md); the next connection is [Analyze results, determine evidence sufficiency, and recommend remedial action](10-analyze-results-determine-evidence-sufficiency-and-reco.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Build a discrepancy log for three synthetic failures and specify who authorizes retest and closure.

**Problem B — Adversarial review.** Can the result be used if the deviation cannot be reconstructed?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 9: Executing and controlling discrepancies](../labs/lab-09-execute-tests-and-control-data-deviations-discrepancies.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 9 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
