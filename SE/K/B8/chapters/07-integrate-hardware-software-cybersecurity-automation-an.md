# Chapter 7 — Hardware, cyber, automation and tools

*Book 8: System Test and Evaluation · Week 7 — Integrate hardware, software, cybersecurity, automation, and test-tool evidence*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 7](../labs/lab-07-integrate-hardware-software-cybersecurity-automation-an.md) without looking at the solution → return to [Week 7 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w07.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **hardware, cyber, automation and tools**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

The test system can be a source of faults. Separate product defects from harness defects, flaky infrastructure, cyber attack effects and data-loss mechanisms. Automation increases repeatability but can repeat a wrong oracle with remarkable consistency.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Integrated testing exposes interactions among hardware, software, cybersecurity controls, automation and tools.

### Distinguishing related ideas

A network-in-the-loop setup can reproduce protocol behavior without reproducing radio interference, environmental stress or operator workload.

### Interpretation and boundary conditions

Choose test layers by the failure mechanism of interest, and avoid claiming that one laboratory substitutes for every other environment.

## Worked engineering case

A test suite reports 100 passes, but 30 cases reused stale expected outputs after an interface change. The pass count cannot establish coverage of the new revision.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

More automated runs do not fix wrong acceptance logic. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Write formal qualification procedures and conduct the Test Readiness Review](06-write-formal-qualification-procedures-and-conduct-the-t.md); the next connection is [Plan environmental, quality, reliability, maintainability, safety, and acceptance testing](08-plan-environmental-quality-reliability-maintainability-.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Audit an automated test suite for oracle validity, configuration match and instrumentation side effects.

**Problem B — Adversarial review.** Can a malicious input cause a different failure than random network noise?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Graduate depth: trustworthy integration of test systems and cyber-physical evidence
### Test infrastructure is part of the measurement model

A test bench does not passively observe the system. It contributes clocks, sensors, data acquisition, software drivers, load generators, network behavior, and control logic. These elements can change the behavior under test or bias the recorded result. For example, a high-frequency telemetry logger may alter processor scheduling, while a network emulator may reproduce mean latency but omit burst loss and route changes. Engineers must model how the measurement chain maps the true phenomenon into the recorded observation before treating automated test output as authoritative.

A simplified observation model is `y = h(x, e, c) + b + epsilon`, with true system state `x`, environment `e`, configuration `c`, systematic bias `b`, and random error `epsilon`. This is not a universal physical equation; it makes the sources of evidence distortion explicit. Calibration addresses some biases, repeatability studies address some random variation, and independent observation can reveal hidden tool failures. A test tool used to make acceptance decisions may itself require qualification commensurate with its ability to conceal defects.

### Cybersecurity and functional testing share hidden state

Test environments increasingly include identity services, signed firmware, over-the-air updates, cloud logging, and privileged automation. Security controls can modify timing, startup, network traffic, and failure recovery. Testing functionality with authentication disabled may not support a claim about the production configuration. Conversely, penetration tests can perturb physical devices and must be planned with safeguards and authority boundaries. Evidence should identify which production controls were represented, which were substituted, and whether substitutions affect the relevant claim.

Suppose Northstar's hardware-in-the-loop rig confirms a safe stop on command loss. The result depends on the fault-injection mechanism, simulated sensor responses, timing fidelity, and real controller build. If the test disconnects the network cleanly but real failure produces delayed, reordered, and replayed messages, the demonstrated failure mode is narrower than the requirement. A broader test strategy combines nominal integration tests, adversarial message conditions, hardware fault injection, and operationally plausible recovery sequences.

### Automation reduces transcription errors but adds correlated failure risk

Automated pipelines improve repeatability when scripts, fixtures, and pass criteria are versioned. Yet a bug in a shared test helper can invalidate hundreds of apparently independent test results. Independence of evidence depends on common-cause structure, not the count of green checks. Teams should include test-tool self-checks, reference cases known to fail, review of acceptance calculations, and occasional independent measurement paths. A pass result without a record of raw data and processing transformations is hard to challenge.

Treat the test environment as a configured system with its own dependency graph. For every important claim, record the unit under test, fixture revision, firmware and software versions, security settings, stimulation profile, instrument calibration, clocks, raw measurements, analysis version, and decision rule. Then decide what differences between laboratory and field environments limit transfer of the conclusion. This makes integration of hardware, software, automation, and cybersecurity an explicit part of assurance rather than an assortment of specialized checklists.

## Practice before the assessed course work

[Hypothetical Laboratory 7: Hardware, cyber, automation and tools](../labs/lab-07-integrate-hardware-software-cybersecurity-automation-an.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 7 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-TE8.1 — cyber, software, and automation evidence

### The interface is part of the security boundary

A cyber-physical requirement concerns behavior after a malicious or malformed event, not just possession of a security control. TE8-R08 requires stale or replayed dispatch commands to be rejected **without actuation**. A test therefore observes both the software acceptance decision and the downstream physical action. The adversarial stimulus must include a duplicated authenticated message, reordered sequence numbers, timestamp changes, clock loss and a retry after an ambiguous acknowledgment. A false reject can also impair service availability: the evaluator records both safety/security outcomes and operational effects.

Software test automation should produce *traceable evidence*: stimulus hash, interface version, device identity, test runner version, expected response, observed response, raw log checksum and qualification of the harness. A green unit-test badge is inadequate if the deployment artifact was built from a different commit or if the emulator silently ignores the actuator path. Automation can repeat a known assertion reliably; it cannot decide whether the assertion expresses the right system-level risk.

### Concurrency and security interact

Imagine a stale command re-enters the queue during recovery, while two brokers each retry a reservation. The transaction invariant 'one vehicle has no more than one active owner' must survive both **interleaving** and **replay**. Countermeasures may combine idempotency keys, uniqueness constraints, sequence windows and durable transaction logs. A test should cause interleavings deliberately, not rely on rare accidental collisions. Use the Book 4–5 software-contract examples for component-level intuition; TE8's task is to evaluate the integrated deployment baseline and its physical interface effects.

The [campaign evidence register](../case/evidence-register.csv) marks TE8-E07 **PLANNED**. The absence of a cyber test is neither a confirmed vulnerability nor a passed control. It is an open evidence item whose disposition depends on mission hazard and release rules.

**Exercise.** An automated test reports 'replay rejected' from a mocked API, but no controller output is recorded. Name the missing end-to-end evidence.

<details><summary>Worked answer</summary>

Instrument the real or representative controller and prove that replayed commands do not cause actuation, including during clock skew, reconnection and service restart. Record build provenance, stimulus and physical output. The API-only assertion is useful unit evidence, but its scope is narrower than TE8-R08.

</details>
