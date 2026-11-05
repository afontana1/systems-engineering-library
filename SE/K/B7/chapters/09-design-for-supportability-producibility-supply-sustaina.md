# Chapter 9 — Supportability and life-cycle costs

*Book 7: System Design and Integration · Week 9 — Design for supportability, producibility, supply, sustainability, and disposal*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 9](../labs/lab-09-design-for-supportability-producibility-supply-sustaina.md) without looking at the solution → return to [Week 9 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w09.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **supportability and life-cycle costs**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Support architecture includes spares, repair knowledge, update channels, suppliers, staffing, consumables and end-of-life handling. Compare alternatives using consistent boundaries across acquisition and operations. A cheap vehicle platform may impose expensive recurring uptime and supply risks.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Supportability connects the design to the organization and infrastructure required to keep it useful across its lifecycle.

### Distinguishing related ideas

A cheaper component may impose higher total cost through training, proprietary diagnostics, long lead times or difficult replacement.

### Interpretation and boundary conditions

Maintainability and producibility therefore belong in early architecture decisions, not only procurement planning.

## Deeper theory: supportability is a dynamic property of the architecture

### Purchase price is only one term in the engineering decision

Life-cycle cost includes acquisition, integration, training, energy, preventive maintenance, corrective repair, spares, upgrades, downtime consequences, and end-of-life handling. A discounted representation is `LCC = C_0 + Σ_t C_t/(1+r)^t`, where `r` is the agreed real or nominal discount rate consistent with how future costs are expressed. This arithmetic becomes misleading if an expensive vehicle and a cheaper vehicle are assumed to deliver identical service, useful life, and safety outcomes without evidence. Cost evaluation should use a common mission boundary and explicitly handle differences in delivered capability.

A low-cost component can create a high-cost interface: proprietary diagnostics may require specialist travel, restricted parts can delay restoration, and a short obsolescence cycle may force redesign of adjacent subsystems. Those effects follow from architectural coupling and procurement choices. Design for supportability therefore starts when interfaces, diagnostic access, replaceable units, maintenance authority, and supply strategy are being defined—not after a bill of materials has been frozen.

### Repair time is not the same as service-restoration time

A technician may repair a failed controller in one hour, yet a replacement may take three days to arrive. Operational downtime includes fault detection, diagnosis, administrative delay, logistics, travel, repair, test, and return to service. A simplified intrinsic availability relation using mean time between failures and mean time to repair omits much of that support pipeline. Operational availability requires a support concept aligned to where vehicles operate, inventory placement, staffing hours, and the authorization needed to return a repaired system to service.

Spare-parts planning is probabilistic. A single spare does not guarantee restoration if correlated failures affect multiple vehicles during a weather event or a supplier batch defect. Demand for parts depends on fleet size, duty cycles, failure distributions, preventive replacement, and repair turnaround. Inventory optimization trades holding cost against stockout risk and resulting unavailability. Service-level targets should distinguish the probability a part is immediately available from the probability the mission itself can continue through reallocation or degraded operation.

### Architecture decisions propagate into sustainability and end of life

A replaceable module may increase mass or connector count but extend useful life by making upgrades economical. A sealed assembly may perform better initially but impose expensive replacement or waste at failure. End-of-life considerations include safe energy storage disposal, recoverable materials, data sanitization, and the ability to remove hazardous components. Environmental claims require comparable system boundaries and conditions; shifting repair or recycling burdens outside the accounting boundary does not make them disappear.

For Northstar, supportability evidence should link the expected failure and maintenance model to the actual fleet operating schedule. Ask whether a vehicle unavailable during a short peak window causes disproportionate service loss compared with off-hours downtime. Then connect the maintenance concept to architecture, diagnostics, supply lead times, and verification following repair. A credible life-cycle decision values not merely a system that can be manufactured and deployed, but one that can remain safe, useful, affordable, and governable through changing operational conditions.

## Worked engineering case

A component costing $12,000 with a $2,500 annual support obligation over five years totals $24,500 before discounting, failures or disposal. Another option at $16,000 and $1,000/year totals $21,000 under the same simplifications.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Lowest acquisition cost and lowest lifecycle cost are not synonyms. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Design for human performance, safety, security, usability, and resilience](08-design-for-human-performance-safety-security-usability-.md); the next connection is [Plan system integration and conduct the Integration Readiness Review](10-plan-system-integration-and-conduct-the-integration-rea.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Build an undiscounted life-cycle comparison, then list the omitted sources of uncertainty.

**Problem B — Adversarial review.** What supplier discontinuation would invalidate the support strategy?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 9: Supportability and life-cycle costs](../labs/lab-09-design-for-supportability-producibility-supply-sustaina.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 9 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Advanced worked practice

- [Deep workshop — Reliability Allocation, Common Cause, and Integration Evidence](../practice/integration.md)
- [Corresponding independent laboratory](../practice/lab-integration.md)
- [Interactive workbench](../practice/WORKBENCH.html)
