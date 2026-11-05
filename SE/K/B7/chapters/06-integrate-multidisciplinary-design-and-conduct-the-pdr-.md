# Chapter 6 — Cross-discipline preliminary design review

*Book 7: System Design and Integration · Week 6 — Integrate multidisciplinary design and conduct the PDR-style review*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 6](../labs/lab-06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md) without looking at the solution → return to [Week 6 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w06.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **cross-discipline preliminary design review**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A preliminary design review tests internal consistency: power, mass, timing, human authority, fault behavior, maintenance and interfaces must agree. Red-team disagreements should become decisions with owners, not optimistic footnotes. An incomplete model can still support a conditional review if the boundary is explicit.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

A preliminary design review tests whether a coherent implementation path exists across mechanical, electrical, software, human and operational disciplines.

### Distinguishing related ideas

A discipline-specific pass is insufficient when heat, power, timing and accessibility constraints are coupled through the same architecture.

### Interpretation and boundary conditions

Review disagreements should become explicit interface decisions or experiments, not be deferred as 'integration details'.

## Deeper theory: design reviews as compositional feasibility arguments

A preliminary design review is sometimes treated as an administrative presentation of completed drawings. Its deeper purpose is to establish whether the evolving system architecture is *collectively feasible*: whether independently developed disciplines can satisfy their allocated obligations when combined. Mechanical, electrical, software, safety, human factors and operations models may each be locally reasonable yet mutually incompatible. A review must examine the **cross-boundary assumptions** on which the global design depends.

For example, the electrical team may show enough nominal battery energy for a route, while the controls team assumes a higher processor duty cycle, thermal management assumes additional cooling power, and operations reserves emergency energy. Each estimate may be correct within its own model; their combination can still violate the system margin. The review needs a common configuration, operational scenario and consistent unit basis before adding their effects. This is a form of **compositional reasoning**: local claims are used to support a global claim only when their interfaces and environmental assumptions align.

### Review maturity is a vector, not a percentage

A design is mature in several partly independent dimensions: requirements stability, architecture completeness, analytical credibility, supplier feasibility, interface closure, hazard control and testability. Reporting “85% design complete” hides the possibility that one unclosed safety-critical interface prevents responsible advancement. A vector of maturity arguments is more informative than a single score. The weakest dimension is not always the most expensive, but a missing prerequisite can invalidate the usefulness of progress in other dimensions.

A credible PDR can approve further detailed design with documented open items. It need not certify operational readiness. It should, however, identify what is sufficiently established, what uncertainty remains, who owns each open issue, and what evidence is required before the next commitment. Distinguishing **risk acceptance** from **risk ignorance** is crucial: an open risk with an understood mechanism and funded mitigation is not the same as an unexamined assumption hidden in an interface drawing.

### Constraint closure is the organizing logic

Let \(x\) denote a candidate set of design choices, and let each discipline contribute constraints \(g_i(x)\leq0\). The overall feasible set is \(F=\{x:g_i(x)\leq0\text{ for all }i\}\). A review does not prove feasibility merely by checking that every discipline has a solution in its own local variable space. If those solutions require incompatible shared values—mass, power, schedule, temperature, bandwidth or staff availability—the intersection \(F\) may be empty. The purpose of integrated budgets and interface agreements is to expose and resolve these conflicts while change remains affordable.

The mathematical picture is simplified because many constraints are uncertain and some are qualitative. Still, it explains why a system can fail even when no team has made an arithmetic error. Electrical margin and thermal margin may both look positive if each assumes the other uses less power. Constraint closure requires shared assumptions and explicit ownership of slack.

### Interfaces and hazards must be reviewed together

An interface is not just a transfer of information or energy. It is also a possible path for failure propagation. An invalid route permission from a central service may be syntactically accepted by a vehicle controller, even if every component's local unit tests pass. A review must ask what happens when the input is stale, missing, delayed, contradictory or malicious. Fault containment depends on which side of the interface is authorized to reject or override the command.

Human and organizational interfaces also matter. A dispatcher may be described as an external stakeholder in one document and as an essential safety control in another. If human intervention is credited as hazard mitigation, the design must make realistic claims about alert timing, workload, training, available information and authority. A human role cannot be counted as an abstract perfect backup that has no latency or failure probability.

### Review evidence has a provenance problem

Analysis outputs must be tied to model versions, assumptions and data. A mass budget from one architecture revision cannot be silently combined with a charging calculation from another. Reviews need configuration consistency across drawings, simulation cases, requirements and risk statements. Evidence traceability is therefore not paperwork after the design; it is part of the reasoning that lets reviewers combine results into one argument.

A productive review makes disagreements visible. The best outcome is not always an unconditional approval. Conditional approval, limited continuation or a targeted prototype may be the rational response when the design is plausible but the evidence supporting a consequential interface is not yet sufficient. The review is an engineering decision about **how much uncertainty can responsibly be carried forward**.

## Worked engineering case

A power budget requires 4.5 kW peak while the available supply is rated 4.1 kW. The arithmetic shortfall is 0.4 kW before safety margin; it cannot be closed by presentation polish.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Review readiness measures closure of contradictions, not the number of slides presented. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Use prototypes and experiments to retire technology and design risk](05-use-prototypes-and-experiments-to-retire-technology-and.md); the next connection is [Design for reliability, availability, and maintainability](07-design-for-reliability-availability-and-maintainability.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Construct a multidisciplinary conflict table and recommend design, requirement or demonstration changes.

**Problem B — Adversarial review.** Which conflict threatens several disciplines simultaneously?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 6: Cross-discipline preliminary design review](../labs/lab-06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 6 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Advanced worked practice

- [Deep workshop — Interface Contracts and End-to-End Timing Budgets](../practice/interfaces.md)
- [Corresponding independent laboratory](../practice/lab-interfaces.md)
- [Interactive workbench](../practice/WORKBENCH.html)
