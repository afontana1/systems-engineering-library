# Chapter 7 — Morphological and set-based concepts

*Book 6: System Conceptual Design · Week 7 — Generate physical concept families with morphological and set-based methods*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 7](../labs/lab-07-generate-physical-concept-families-with-morphological-a.md) without looking at the solution → return to [Week 7 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w07.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **morphological and set-based concepts**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Morphological analysis creates structured divergence: enumerate choices along independent dimensions before combining them. Feasibility screening comes before preference scoring, and the elimination reason should be recorded. Set-based reasoning keeps several promising alternatives alive while the most consequential uncertainty is retired.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Morphological design separates functions into alternative solution principles, exploring combinations before prematurely locking architecture.

### Distinguishing related ideas

The Cartesian product of options includes infeasible combinations; compatibility constraints and common assumptions must filter them before scoring.

### Interpretation and boundary conditions

Keeping multiple feasible concepts alive temporarily can be valuable when uncertain operating data may reverse a preferred choice.

## Deeper theory: concept generation is a search over feasible combinations

### A morphological table defines a possibility space, not a product catalog

In morphological analysis, engineers separate a system into key functions or design dimensions and list feasible means for realizing each. The naive Cartesian product of options can become enormous: five dimensions with four options each produce `4^5 = 1,024` combinations. But many are incompatible, redundant, or physically impossible. The rigorous task is therefore to identify constraints and interactions, then explore *feasible families* of architectures. If onboard autonomy requires local perception while one proposed communication strategy assumes continuous remote control, the combination needs a specific degraded-mode concept or should be rejected.

Option independence is a convenience of table layout, not a property of the engineering world. A larger battery changes mass, braking distance, charging demand, and accessible floor geometry. A centralized dispatch algorithm changes communications load and the authority needed onboard. Cross-consistency assessment can reject incompatible pairs, but some incompatibilities involve three or more interacting choices and cannot be captured by pairwise checks alone. A concept family should therefore retain a rationale for feasibility, not merely a combinatorial identifier.

### Set-based design preserves information before irreversible selection

A point-design approach chooses one concept and iterates toward feasibility. Set-based design maintains several alternatives or parameter ranges while evidence narrows the feasible region. It is particularly useful when early assumptions are weak and changing suppliers or physical interfaces later will be expensive. The approach is not an excuse to leave every decision open. Engineers should retire dominated or infeasible regions as soon as defensible evidence allows, while protecting strategically useful options where uncertainty remains consequential.

A simple way to express the feasible set is `F = {x : g_j(x) ≤ 0 for all mandatory constraints j}`. The functions `g_j` encode conditions such as peak power, vehicle envelope, allowable response time, or minimum accessibility. Real constraints have uncertain parameters; one can use conservative bounds, probabilistic constraints, or staged experiments, provided the chosen decision rule is explicit. The distinction between “not yet shown feasible” and “shown infeasible” matters. Treating absent evidence as proof of impossibility can prematurely eliminate innovative concepts; treating absent evidence as feasibility can expose the mission to unjustified risk.

### Modularity and option value can justify seemingly inefficient choices

A replaceable communications module may cost more initially than a tightly integrated board but reduce the future cost of responding to an uncertain network standard. That flexibility is an *option*, valuable only when there is a credible future decision and a mechanism for exercising it. The value does not arise from declaring every interface modular; modularity itself adds connectors, packaging, verification work, and possible performance loss. The engineering decision is about the expected consequences of reversibility in a specific uncertain future.

For Northstar, an early architecture could preserve both local and centrally supervised dispatch as controlled candidates until a targeted communications demonstration discriminates between them. The evolving concept space should show excluded combinations, reasons, relevant evidence, and remaining uncertainties. Morphological exploration is most powerful when it creates traceable diversity of ideas and then progressively converts that diversity into justified design commitments—not when it generates hundreds of unevaluated boxes.

## Worked engineering case

Three fleet modes × two dispatch arrangements × two stop concepts produce 12 nominal combinations. Removing four combinations for accessibility and right-of-way conflicts leaves eight candidates, not a ranked winner.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A numerical score must not rescue an alternative that violates a mandatory safety constraint. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Timing, interfaces, allocations, and Functional Architecture Review](06-timing-interfaces-allocations-and-functional-architectu.md); the next connection is [Resource, affordability, schedule, feasibility, and optimization models](08-resource-affordability-schedule-feasibility-and-optimiz.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Create a 3×2×2 morphology table and document exclusion criteria for any infeasible combination.

**Problem B — Adversarial review.** How many concept families remain after objective feasibility screening?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 7: Morphological and set-based concepts](../labs/lab-07-generate-physical-concept-families-with-morphological-a.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 7 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
