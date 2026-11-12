# Chapter 5 — Prototypes as risk-retirement tools

*Book 7: System Design and Integration · Week 5 — Use prototypes and experiments to retire technology and design risk*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 5](../labs/lab-05-use-prototypes-and-experiments-to-retire-technology-and.md) without looking at the solution → return to [Week 5 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w05.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **prototypes as risk-retirement tools**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Choose prototype fidelity from the question being asked. A quick interface mockup may reveal human confusion, while a bench network probes latency and failure recovery. Neither should be promoted into field-reliability evidence without a defensible transfer argument.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Prototypes should retire the most consequential uncertainty

A prototype can be impressive yet informationally weak if it reproduces only the scenario that the architecture was already expected to handle. Its purpose is not to look like the eventual product but to create evidence that changes an engineering decision. A mock interface may reveal operator comprehension, a breadboard may expose electrical noise, and a hardware-in-the-loop setup may reveal timing behavior. Their fidelity differs because each targets a different uncertainty.

Designing a prototype begins by stating which competing explanations or alternatives it must discriminate. If the decision is whether onboard computation can meet a deadline, high fidelity in passenger seating adds little; realistic timing, workload and fault behavior matter. A negative result is useful when it is diagnostic. A positive result is useful only within its tested boundary. Distinguish *risk retirement*—learning enough to choose a path—from *qualification*, which establishes compliance of a specified design under acceptance conditions.

## Deeper theory: prototyping as the disciplined purchase of information

A prototype is not a miniature version of the finished product in any universally meaningful sense. It is an experimental representation built to answer a particular question. A plywood boarding mock-up may be better than an expensive vehicle prototype for discovering reach and visibility problems. A hardware-in-the-loop simulator may reveal controller timing faults that a beautiful full-scale model cannot. The **fidelity of a prototype is multidimensional**: physical geometry, software behavior, time response, environmental exposure, operator interaction and failure behavior may each match the intended system to different degrees.

The central planning question is therefore not “How realistic can we make it?” but “Which uncertain claim matters enough that evidence should be acquired now, and which features must the prototype preserve for that evidence to be relevant?” If the claim concerns passenger reachability, geometry and realistic user participation matter. If it concerns scheduling throughput, arrival distributions, service-time variability and capacity rules matter. If it concerns safe degraded operation, timing, fault responses and authority transitions matter. Extra fidelity in irrelevant dimensions can consume money without increasing decision value.

### A prototype creates evidence through a measurement model

Prototype observations do not transfer automatically to the final design. The transfer depends on an argument connecting the prototype's conditions to the deployment conditions. A scaled mechanical test may preserve geometric ratios but fail to preserve stiffness or inertia because different physical quantities scale with different powers of length. A software simulation may execute the production algorithm while simplifying the network and clock behavior. A representative operator rehearsal may capture workflow but omit the cognitive stress of a real emergency. Each mismatch is a possible source of **model-form uncertainty**.

A useful prototype plan therefore states an intended claim \(C\), the observable \(Y\) relevant to that claim, the prototype configuration \(P\), the operational configuration \(O\), and assumptions \(A\) that justify inference from observations on \(P\) to \(O\). The evidence supports \(C\) only to the extent that \(A\) is credible. A prototype can be repeatable and internally valid yet lack external validity because it omits the mechanism that dominates field performance.

### Risk retirement differs from demonstration

A public demonstration is optimized to show a system working under chosen conditions. A risk-retirement experiment is optimized to distinguish plausible failure hypotheses. Suppose engineers suspect that charger communication is unreliable when a vehicle is hot and nearly depleted. A demonstration at room temperature and high charge may show successful nominal operation but gives little evidence about the suspected hazard. A risk-directed prototype deliberately explores the boundary conditions, even if that makes the result less visually impressive.

This distinction can be expressed with expected-loss reasoning. Suppose the wrong charging architecture would create substantial rework after procurement. An early test is valuable if its result could change the selection or the required mitigation. A test that merely repeats an already well-supported nominal claim may add confidence but little decision value. Perfect information is rarely attainable; the goal is to reduce uncertainty sufficiently to justify the next commitment.

### Prototype failure is not necessarily project failure

A prototype built to challenge a design hypothesis has succeeded as an experiment if it reliably reveals that the hypothesis is wrong. The program fails intellectually when observations are reinterpreted to preserve the preferred answer. If a fault-injection prototype unexpectedly produces stale route permissions after reconnection, that result may motivate a stronger interface contract, independent monitoring or architectural relocation of authority. The discovery can reduce future operational risk even if it temporarily worsens schedule metrics.

Prototype results should be configuration-specific. The tested hardware revision, software build, test environment, calibration, operator procedure and data-generation method are all part of the evidence. Without these attributes, later teams may incorrectly treat a successful test of one variant as proof about another. This is particularly dangerous when a demonstration is repeated after several undocumented fixes and the final pass is presented without the earlier failures.

### When an experiment should stop

A prototype can become a development project in its own right, absorbing effort long after its original question has been answered. The exit condition should therefore be defined in advance: a discrimination threshold, a safety condition, a confidence target, or a decision rule specifying what evidence is sufficient to proceed or redesign. An inconclusive result is still informative if it reveals that the measurement or prototype fidelity was inadequate. In that case, increasing the number of repetitions may not solve the problem; the experiment's model may need redesign.

Prototyping is best understood as **structured learning before expensive commitment**. Its quality comes from a sharp question, an appropriate representation, attention to transfer validity and an honest account of the remaining unknowns—not from the prototype's visual resemblance to the final product.

## Worked engineering case

A bench dispatcher succeeds 40 of 50 scripted trials; this estimates performance for those conditions, not operational availability under weather, cyber threats or high demand.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A prototype that only demonstrates the preferred concept cannot discriminate between alternatives. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Mature the physical architecture, interfaces, and performance budgets](04-mature-the-physical-architecture-interfaces-and-perform.md); the next connection is [Integrate multidisciplinary design and conduct the PDR-style review](06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Pick three distinct design risks and choose the cheapest prototype whose result could actually retire each risk.

**Problem B — Adversarial review.** What result would cause the team to change the design?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 5: Prototypes as risk-retirement tools](../labs/lab-05-use-prototypes-and-experiments-to-retire-technology-and.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 5 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-DI7.1 — experiments that can overturn a design claim

### Design a test to distinguish competing explanations

The gateway and dispatcher redesigns may interact. An experiment should therefore vary both rather than benchmark them one at a time in a single favorable configuration. The controlled [synthetic 2×2 dataset](../case/doe-synthetic.csv) has three illustrative readings in each cell. Its cell means are 488 ms for standard gateway/serial dispatch, 472 ms for fast/serial, 451 ms for standard/parallel, and 428 ms for fast/parallel.

For a balanced two-factor design, the *gateway main effect* is the average fast-minus-standard contrast across dispatch settings:

\[
E_G=\frac{(472+428)-(488+451)}{2}=-19.5\ \mathrm{ms}.
\]

The dispatcher main effect is \(-40.5\) ms. The interaction contrast is

\[
I=(428-451)-(472-488)=-7\ \mathrm{ms}.
\]

The interaction means that the saving from one change depends on the other setting. It is not a statistical significance claim; these few illustrative readings were constructed for arithmetic practice. A proper experiment would randomize configuration order, block environmental drift, repeat independent trials, verify timestamps, estimate variance and assess whether the operational request population was represented.

### The tail matters more than a favorable mean

Suppose, solely as a hypothetical *distributional model*, the combined design's response time were normal with mean 428 ms and standard deviation 20 ms. Then

\[
P(T>450)=1-\Phi\left(\frac{450-428}{20}\right)\approx 0.1357.
\]

A 428-ms mean therefore cannot establish a 450-ms p99 target; it would be a serious category error to equate mean performance with a tail requirement. Real latency can be skewed, multimodal or heavy-tailed. The Gaussian illustration is not fitted to the twelve constructed records and should not be reported as measured service risk.

**Exercise.** A team advertises the fastest synthetic cell as proof that the system will meet the 500-ms 99th-percentile requirement. Identify three missing evidence elements.

<details><summary>Worked resolution</summary>

The team needs representative randomized and sustained degraded-load observations, a justified end-to-end percentile estimator with uncertainty, and configuration-controlled evidence tying the exact gateway/dispatcher build to the requirement. It must also account for clock accuracy, correlated retry storms and the margin policy. Without these, record MODEL_ONLY or TEST_PENDING.

</details>
