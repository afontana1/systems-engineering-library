# Chapter 2 — Closing the system specification

*Book 7: System Design and Integration · Week 2 — Close the system specification*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 2](../labs/lab-02-close-the-system-specification.md) without looking at the solution → return to [Week 2 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w02.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **closing the system specification**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A specification is an agreement about observable performance across normal and abnormal conditions. Decompose stakeholder goals into testable system clauses while preserving parent rationale and acceptance method. A design-specific statement can be justified, but should not masquerade as a mission need.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### A system specification is a contract between viewpoints

The system specification is not simply a longer list of requirements. It is a structured agreement across operational needs, design obligations, externally observable behavior, and verification criteria. Requirements can be individually clear yet collectively inconsistent: one may demand emergency stopping within a short interval while another mandates a communications architecture incapable of carrying commands that quickly. Finding this inconsistency requires reasoning about **interactions**, not just checking sentence quality.

Specifications must also distinguish what is fixed from what is an allocation choice. A system-level stopping distance may be non-negotiable, while how the distance budget is divided across detection, decision, actuation, and dynamics remains a design problem. Derived requirements document the consequences of those allocations; they should not be treated as independent customer wishes. When assumptions change, the derivation needs to be revisited. A coherent specification is therefore a network of justified claims whose dependencies can be inspected.

## Deeper theory: a system specification is a consistent set of obligations

### Requirements closure is more than writing every “shall”

A system specification should be complete enough to bound design responsibility without pretending to predict every detail of implementation. Its quality depends on whether requirements can be interpreted together under the same operating assumptions. Individual statements may each appear testable yet be mutually inconsistent. For example, “accept every valid request immediately” and “never exceed finite vehicle capacity” cannot both be met under unbounded demand unless acceptance is explicitly distinguished from fulfillment. Requirements engineering must discover such contradictions before they become integration defects.

One way to reason about closure is to treat each requirement as a predicate over possible system behaviors. The specification defines the behaviors that satisfy all relevant predicates simultaneously. If the intersection is empty, no design can comply. If the intersection is too broad, unsafe or useless behaviors may still be permitted. Formal methods can help detect inconsistency in bounded models, but ordinary engineering reviews can also test the logic through adversarial scenarios and precise definitions.

### Verification criteria and operational meaning must align

A requirement to complete requests within five seconds is incomplete without defining the event that starts the clock, the event that stops it, relevant operating modes, and whether failures or refusals count. The testable number alone does not resolve semantic ambiguity. Definitions should include units, populations, environmental ranges, interfaces, tolerances, and the authority that can approve exceptions. If a requirement applies only during normal operation, degraded-mode obligations must be specified elsewhere rather than silently assumed away.

This distinction prevents a common error: equating **measurability** with **adequacy**. An easily measured threshold can be precise but irrelevant to the stakeholder's purpose. Conversely, an important service outcome may require decomposition into several observable measures. Traceability should preserve that reasoning so the specification remains connected to the ConOps rather than becoming a disconnected catalog of tests.

### Derived requirements require explicit rationale

Top-level system obligations often imply subordinate constraints. A 300 ms end-to-end safety response may require timing budgets for sensing, decision logic, communications, and actuation. Those budgets are design allocations, not stakeholder statements. Their sum must preserve a defensible margin, and the allocation must account for the fact that shared resources create dependence. If individual subsystem budgets are each expressed as a 99th percentile, the sum is not necessarily the 99th percentile of total response time.

A derived requirement should identify its parent need, assumptions, allocation logic, and verification method. This makes it possible to revisit the derivation when technology, loading, or architecture changes. Without the rationale, downstream teams may optimize a local threshold whose numerical value has lost its relationship to system success.

### Interface contracts are part of the specification

A physical or software boundary does not remove the obligation to agree on exchange meaning. Two components can satisfy their own requirements while disagreeing about units, timestamp origins, failure states, or timeout behavior. An interface contract should state not only what data cross the boundary but also the permissible sequences, temporal bounds, fault reporting, and ownership of recovery. Verification should challenge mismatches deliberately, not rely solely on successful nominal exchanges.

The final specification is therefore not “closed” when its table has no empty cells. It is closed enough for the next design decision when important obligations are consistent, allocated to responsible owners, backed by plausible verification paths, and traceable to stakeholder outcomes. Residual ambiguity should be visible and managed, not disguised as maturity.

## Worked engineering case

“Fast response” is not verifiable. “For accepted requests under Scenario E, 95% receive a dispatch decision in ≤2.0 s” identifies statistic, denominator, condition and threshold; the precise scenario still needs a revision.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Overprecision without a stated test population makes a requirement less—not more—verifiable. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Receive the concept baseline and plan design maturation](01-receive-the-concept-baseline-and-plan-design-maturation.md); the next connection is [Allocate requirements and define component functions](03-allocate-requirements-and-define-component-functions.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Rewrite four ambiguous clauses and mark the evidence method, threshold, exclusions and source for each.

**Problem B — Adversarial review.** Which clauses remain ambiguous at a test boundary?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 2: Closing the system specification](../labs/lab-02-close-the-system-specification.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 2 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-DI7.1 — specification closure

### Write obligations that can be contradicted

A system specification is an internally consistent, testable set of obligations. An attractive feature list is not sufficient. For DI7-R02, "fast response" is ambiguous; "degraded end-to-end command response not exceeding 500 milliseconds at the specified 99th percentile" identifies the measured variable, operating regime and decision threshold. Even that wording must still specify timestamp locations, warm-up conditions, request population, and the definition of degraded mode. A percentile requirement concerns a **distribution**; a deterministic component sum is only a feasibility estimate.

Define each requirement as a tuple \(r=(q,\,S,\,L,\,m,\,b)\), where \(q\) is the measured quantity, \(S\) the scenario, \(L\) the threshold, \(m\) the verification method and \(b\) the applicable baseline. If any element is missing, ambiguity can reappear during testing. DI7-R03 similarly fixes energy at no more than 30 kWh **per defined shift**, not per trip. The baseline lists traction 22.4, heating 2.1 and communications 1.8 kWh, giving 26.3 kWh and a modeled 3.7-kWh allowance. That result cannot be exported to a longer or colder duty cycle without recomputation.

### Allocation and consistency checks

Trace each requirement into an owned subsystem and a verification obligation. A link from a requirement to a named component is **coverage**; it is not necessarily a feasible allocation. For example, DI7-R02 is allocated across five serial stages. Their degraded component estimates add to 490 ms, nominally below 500 ms. But the project requires a **10% design reserve**, or 50 ms. Feasible allocation under that policy requires an estimated path of at most 450 ms. Thus the allocation passes the nominal deadline test but fails the design-reserve policy.

The [interface register](../case/interfaces.csv) provides the stages, units, owners and failure behavior. A specification review should reject data drift between this register and the timing model. It should also detect a false completeness claim when verification is planned or refers to the wrong version.

**Exercise.** If an engineer adds a 15-ms cryptographic operation without changing the 500-ms system deadline, assess the original degraded design and the proposed combined redesign.

<details><summary>Worked resolution</summary>

The original path becomes 505 ms: it fails the deadline. The combined redesign is 440 + 15 = 455 ms: it meets the absolute deadline but misses the 450-ms maximum imposed by the 10% reserve policy. The team must adjust implementation, renegotiate the constraint through configuration control, or obtain approved risk acceptance—not simply erase the margin rule.

</details>
