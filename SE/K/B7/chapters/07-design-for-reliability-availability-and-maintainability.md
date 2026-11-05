# Chapter 7 — Reliability and maintainability

*Book 7: System Design and Integration · Week 7 — Design for reliability, availability, and maintainability*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 7](../labs/lab-07-design-for-reliability-availability-and-maintainability.md) without looking at the solution → return to [Week 7 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w07.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **reliability and maintainability**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Reliability concerns survival during a mission; availability also includes repair and support delays; maintainability concerns restoration. Define time, conditions, mission and failure event before calculating. Independence assumptions for component failures need evidence, especially when components share power, software or maintenance crews.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Reliability engineering traces failure mechanisms, mission exposure and restoration resources rather than treating availability as a component property.

### Distinguishing related ideas

MTBF and MTTR summarize certain stochastic models; they do not by themselves represent aging, correlated failures, spares shortage or unsafe degraded modes.

### Interpretation and boundary conditions

Design decisions must account for how an item fails, how failure is detected, and whether restoration is possible during the mission window.


## Deeper theory — reliability, repairability and mission success are different quantities

### The distinction between surviving and being available

**Reliability** is the probability that an item performs a required function without failure over a specified interval and conditions. **Availability** concerns whether the function can be provided at a point in time or over a period, allowing for repair and restoration. **Maintainability** concerns how quickly and predictably a system can be restored after loss of function. They interact, but no one metric substitutes for the others. A frequently failing component that is instantly replaced can have high availability and poor mission reliability; a rarely failing component that takes weeks to repair can have strong short-mission reliability and poor fleet availability.

For a component with constant failure hazard \(\lambda\), the exponential survival model gives

\[
R(t)=\exp(-\lambda t).
\]

This follows from the assumption that the probability of failure during a short interval \(dt\), conditional on survival so far, is approximately \(\lambda\,dt\). It is a *memoryless* model. Mechanical wear-out, battery aging and environmental fatigue often violate it. Using the exponential model across an entire product life because it makes the algebra easy can hide increasing hazards precisely when maintenance planning becomes consequential.

### Repair changes the state model

In a simple two-state up/down model with exponential failure and repair rates, long-run steady-state availability is

\[
A=\frac{\mathrm{MTBF}}{\mathrm{MTBF}+\mathrm{MTTR}}.
\]

If mean time between failures is 200 hours and mean repair duration is five hours, the illustrative steady-state availability is about 97.56%. This result depends on a stationary alternating renewal model and on what is counted as downtime. Waiting for a replacement part, arranging transport, obtaining regulatory authorization and verifying restored configuration may dominate wrench time. A repair specification that ignores those delays can be technically true and operationally misleading.

A fleet service may need *mission availability*: can a suitable vehicle provide the requested ride at the needed time? A wheelchair-equipped vehicle in the depot may be mechanically operational but unavailable to a rider in a distant location. Thus geographic position, demand, operator staffing and resource pooling alter service availability. This is why equipment specifications must not be mistaken for system-level performance claims.

### Architecture determines the mathematical composition

For series elements required simultaneously and assumed independent, mission reliability is the product of component reliabilities. If two stages each have reliability 0.98 for the mission, the path reliability is \(0.98^2=0.9604\). For two interchangeable parallel elements each with reliability 0.98, idealized reliability becomes \(1-(1-0.98)^2=0.9996\). This apparent improvement is enormous but conditional: the elements must actually be able to substitute for one another, the switching mechanism must work and failure modes must be sufficiently independent.

If both elements depend on one network switch, one depot charger, one credential system or one flawed shared software release, the independent calculation is optimistic. A simple model with common-cause unavailability \(q\) multiplies the parallel reliability by \((1-q)\) when the shared event is independent of residual component failures. With \(q=0.02\), the apparently excellent 0.9996 becomes approximately 0.979608 for the relevant interval or state definition. Redundancy creates value only to the extent that it creates genuine *failure independence* and preserves capacity after a loss.

### Reliability blocks are not behavior models

A reliability block diagram treats success as a logical combination of component success events. It can be excellent for a fixed mission with well-defined dependencies. But systems may reconfigure after failures, degrade gradually, require repair while operating or encounter competing demands. A two-vehicle fleet that can serve ten riders per hour with both vehicles and five per hour with one is not simply “up” or “down.” A capacity threshold, queueing model or state-based reliability model may be needed to connect failures to passenger experience.

Fault trees explain how combinations of events can produce a specified top event. Failure modes and effects analysis starts from local modes and reasons forward to consequences. Markov or semi-Markov models represent transitions between operating, degraded and failed states. None is inherently “the correct reliability method”; the appropriate abstraction depends on what success means, whether time and repair matter, and what failure dependence must be represented.

### Design for maintainability is an architectural intervention

Repair time is partly designed, not merely measured after deployment. Modular replacement, diagnostic observability, accessible equipment, interchangeable parts, trained support staff and clear configuration records change the restoration process. A component can be highly reliable yet difficult to diagnose, producing long fleet outages after rare failures. Conversely, a design that isolates faults and permits safe degraded operation may deliver stronger service continuity without materially improving individual component failure rates.

This creates an economic and operational trade: extra diagnostics and spare capacity have costs, but they can reduce downtime and preserve mission performance under stress. The defensible design question is not “Can we make MTBF larger?” but “Which failure and restoration mechanisms dominate stakeholder loss under realistic demand, and which architectural change reduces that loss?” That question links RAM engineering to logistics, human factors, safety and systems-of-systems resilience.

## Worked engineering case

For exponentially distributed independent up and repair intervals, intrinsic availability A≈MTBF/(MTBF+MTTR). With 100 h and 5 h, A≈0.9524. Logistic delays can reduce achieved availability further.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

High component reliability does not imply system resilience to common-cause faults. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Integrate multidisciplinary design and conduct the PDR-style review](06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md); the next connection is [Design for human performance, safety, security, usability, and resilience](08-design-for-human-performance-safety-security-usability-.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Construct a three-component reliability block diagram and a spare/repair timeline with explicit assumptions.

**Problem B — Adversarial review.** What repair delay has the highest mission impact?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 7: Reliability and maintainability](../labs/lab-07-design-for-reliability-availability-and-maintainability.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 7 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
