# Chapter 12 — Concept baseline and handoff

*Book 6: System Conceptual Design · Week 12 — Final concept baseline, oral defense, and handoff*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 12](../labs/lab-12-final-concept-baseline-oral-defense-and-handoff.md) without looking at the solution → return to [Week 12 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w12.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **concept baseline and handoff**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

The conceptual-design handoff transfers not only drawings and preferred options but decision rationale, alternatives rejected, assumptions, model versions and evidence gaps. A receiving team must be able to reconstruct why the baseline holds and what would invalidate it.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

A concept baseline should transfer both a preferred architecture and a record of unresolved assumptions to detailed design.

### Distinguishing related ideas

A down-select is not the assertion that uncertainty disappeared; it is an authorization to invest further conditional on stated evidence and exit criteria.

### Interpretation and boundary conditions

The next team needs the rejected alternatives, decision thresholds and sensitive parameters so a later surprise can trigger a justified reconsideration.

## Worked engineering case

A mixed-fleet concept can baseline accessible service zones while treating autonomous operations as conditional pending demonstration. These statements must not share an unconditional approval status.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Graduate synthesis: concept handoff as preservation of design freedom

### A good baseline constrains the right things

The purpose of a conceptual baseline is not to make every downstream choice permanent. It fixes the stakeholder need, operating envelope, success measures, interfaces already committed, and assumptions that justify a preferred concept. It leaves room for detailed engineering to optimize implementation as new evidence emerges. Prematurely fixing an actuator supplier or software framework can consume design freedom without improving mission assurance; failing to fix accessible boarding requirements can cause later optimization to undermine the original need.

Think of the concept as a feasible design set `F = {x : g_j(x) <= 0 for all mandatory constraints j}`. Concept handoff should communicate the defining constraints of `F`, not just its favored point `x*`. Detailed engineering then searches within the admissible set while confirming that the underlying constraints remain valid. If a candidate violates a mandatory accessible-boarding clearance, it is not rescued by a better weighted cost score. Conversely, a different controller implementation may be acceptable if it preserves the validated service and safety properties.

### Pass uncertainty as a first-class interface

The usual interface-control document specifies dimensions, voltages, commands, and data formats. A graduate-level handoff also specifies *uncertainty contracts*: the demand distribution used for fleet sizing, sensor uncertainty under rain, the worst-case response-time budget, the expected maintenance restoration profile, and unverified assumptions that downstream teams must test. A nominal requirement can be dangerously precise. “Response within two seconds” may hide whether it is a mean, maximum, 99th percentile, or bound under a specified load.

For a closed-loop function with sensing delay `t_s`, compute delay `t_c`, network delay `t_n`, and actuation delay `t_a`, a first-order timing budget is `t_total = t_s + t_c + t_n + t_a`. If upper bounds are 0.15, 0.20, 0.40, and 0.45 seconds, the worst-case summed bound is 1.20 seconds before scheduling jitter, queueing, and clock synchronization are considered. Independent average values cannot be simply added to claim a worst-case guarantee. The receiving teams need the intended percentile or bound and how correlated delays will be handled.

### Make traceability operational rather than decorative

A meaningful handoff links mission outcome to stakeholder requirement, functional allocation, interface constraint, analysis artifact, verification method, and decision authority. Each link should have a semantics: “derived from,” “satisfies,” “verified by,” and “assumes” are not interchangeable. If a change to vehicle mass invalidates an energy model, the receiving design team should be able to find which range claim and procurement decision depend on that model.

For Northstar, preserve both the approved shuttle concept and the unselected alternatives, including the reasons for rejection and conditions that might reverse the ranking. This prevents teams from reinventing rejected approaches without understanding the evidence, while allowing adaptation when a previously uncertain technology improves. The final concept defense should present **what is fixed, what remains provisional, what evidence closes each uncertainty, and who is empowered to change the baseline**. That is the foundation for responsible detailed design.

## Competing explanations and failure modes

The beautiful final slide cannot replace a configuration-controlled claim-to-evidence trail. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Risk, opportunity, affordability, schedule, and Concept Validation Review](11-risk-opportunity-affordability-schedule-and-concept-val.md); the next connection is the receiving team and next review phase. Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Produce a decision-log excerpt and baseline manifest; require the next team to challenge five inherited assumptions.

**Problem B — Adversarial review.** Which design decision is unsafe to freeze without a new test?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 12: Concept baseline and handoff](../labs/lab-12-final-concept-baseline-oral-defense-and-handoff.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 12 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Step 03 integrated reference: NS-CD6.1 — concept baseline, traceability and responsible handoff

The final product of conceptual design is **a controlled argument and a set of design freedoms**, not just a selected vehicle type. NS-CD6.1 records a conditional preference for hybrid concept C while retaining B as an alternative if transfer assumptions, feeder reliability or accessibility evidence overturn the initial result. The purpose of the handoff to System Design & Integration is to make the next team's decisions reversible where they can be, and explicit where they cannot.

### Construct a handoff that can be audited

The case package contains [requirements](../case/requirements.csv), [functional inputs/outputs](../case/functions.csv), [concepts and assumptions](../case/model-baseline.json), [trade inputs](../case/concepts.csv), [synthetic experiment responses](../case/doe-synthetic.csv), [architecture diagram](../case/architecture.svg), and [configuration-aware evidence](../case/evidence-register.csv). A defensible design baseline distinguishes: (a) stakeholder constraints that must be protected, (b) selected architectural hypotheses, (c) uncertain parameters requiring measurement, and (d) unresolved review conditions. Keep each artifact's identifier, owner, revision, source, units and applicability scenario stable.

A simple readiness classification makes the limits visible. CD6-R01, R03, R04 and R05 have **provisional modeled support**, CD6-R02 and R07 lack executed field evidence, CD6-R06 contains a failed degraded model scenario, and CD6-R08 references an outdated NS-CD6.0 record. Even a complete-looking traceability graph cannot turn those statuses into demonstrated system compliance. The controlled [Python audit](../tools/step03_book6_concept_check.py) reports `operational_release: HOLD` on purpose.

### State a decision with explicit conditions

The concept team may recommend “proceed to a tightly bounded C pilot design” conditioned on (1) validating transfer-aware capacity and wait-time cohorts; (2) independently checking accessible offer coverage and non-user exclusions; (3) resolving degraded timing and operator fallback; (4) obtaining credible supplier estimates and lifecycle support assumptions; and (5) gathering current test evidence against the declared baseline. A review chair should reject vague conditions such as “improve reliability later” because they are not verifiable.

A stable handoff includes the expected artifact of each experiment, an acceptance or stopping threshold, the decision owner, and the retained alternative triggered by failure. It also records **negative results**—for example, the modeled 560 ms degraded chain—because deleting an unfavorable calculation would erase the rationale for the architecture's next change.

### Capstone exercise and explained answer

**Exercise:** A successor project updates only the verification spreadsheet to NS-CD6.1 but performs no new test after an interface change. Is the package current? **Answer:** No. Updating a label does not make old evidence applicable. The new configuration needs either a justified equivalence analysis demonstrating unchanged relevant behavior or new measurements under the changed architecture. The handoff should identify who can approve that equivalence and which safety or accessibility claims cannot be waived by the concept team.

**Boundary and review source:** This is a synthetic education package, not an engineering approval or regulated-system safety case. NASA's [system-design guidance](https://www.nasa.gov/reference/4-0-system-design-processes/) emphasizes consistency among ConOps, requirements, design solutions and validation; downstream design must revisit the assumptions rather than treating the concept report as proof of realization.
