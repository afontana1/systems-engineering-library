# Chapter 4 — Concept-neutral requirements and gap experiments

*Book 6: System Conceptual Design · Week 4 — Conceptual requirements, use cases, gaps, and experiment planning*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 4](../labs/lab-04-conceptual-requirements-use-cases-gaps-and-experiment-p.md) without looking at the solution → return to [Week 4 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w04.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **concept-neutral requirements and gap experiments**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A conceptual requirement should constrain an observable outcome, not preselect its realization. Record a verification idea early, but keep alternatives open until evidence supports selection. A capability gap is a difference between needed and demonstrated behavior, not merely a feature missing from the incumbent concept.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Concept-neutral requirements preserve the space of possible implementations by specifying outcomes before committing to technology.

### Distinguishing related ideas

An empirical gap is not automatically a requirement for a specific feature; it may instead reveal a staffing, policy or interface constraint.

### Interpretation and boundary conditions

Separate acceptance thresholds from proposed means so alternative concepts can be compared fairly.

## Worked engineering case

“Two wheelchair-capable autonomous shuttles” dictates a solution. “At least 95% of eligible accessible requests are offered an appropriate pickup within 15 minutes during the defined event-day profile” states a measurable service claim, though it still needs definitions for eligible, offered, and event-day.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

An impressive precision target is not useful if eligibility or the population denominator is undefined. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Desired end state, ConOps, scenarios, and mission calculator v0.1](03-desired-end-state-conops-scenarios-and-mission-calculat.md); the next connection is [Functional architecture and mission-to-function traceability](05-functional-architecture-and-mission-to-function-traceab.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Convert four solution-loaded features into measurable, concept-neutral outcomes and plan one discrimination experiment per outcome.

**Problem B — Adversarial review.** Which requirements belong at the service level rather than the vehicle level?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: concept-neutral requirements and feasibility boundaries

### Requirements can accidentally encode the first design idea

“Install a central dispatch server” is a solution instruction, not a concept-neutral statement of required service behavior. A requirement such as “resolve accepted ride requests within an authorized response window under the defined demand envelope” allows centralized, distributed, or human-assisted dispatch to compete. Neutrality is not always appropriate: a law, safety constraint, or legitimate stakeholder mandate can require a particular implementation. The engineer must distinguish imposed constraints from assumptions and preferences rather than treat neutrality as an absolute virtue.

A useful requirement statement includes a subject, observable behavior, conditions, and acceptance rule. But observable outcomes cannot be defined independently of scenarios. A requirement for five-minute pickup means different things if it begins at booking, confirmation, or dispatch; the meaning also depends on geography, accessibility needs, simultaneous demand, and exclusions. Operating-domain boundaries are not afterthoughts: they determine the space in which feasibility and later evidence can be claimed.

### Feasibility is a conjunction of constraints, not an aspiration

Concept candidates live within a feasible region determined by physical, operational, organizational, and safety conditions. Let a vector `x` represent capacity, fleet size, charging policy, and operating speed. Each mandatory relationship `g_j(x, θ) ≤ 0` restricts possible solutions under scenario parameters `θ`. Capacity can be approximated by `capacity ≈ vehicles × effective trips per vehicle per hour × passengers per trip`, but effective trips depend on journey time, dwell, charging, routing, and interruptions. The simple expression is a screening model, not proof of an achievable service rate.

For illustration, four shuttles that each complete four trips per hour with an average of two passengers per trip offer a nominal 32 passenger trips per hour. If peak demand is 50 requests per hour, that simple steady-state capacity cannot meet the peak without backlog or changed operations. Even if average demand is 25, transient peaks can generate unacceptable waits. A concept-neutral requirement should therefore reflect the demand distribution and its temporal structure, not an invented average that flatters a design.

### Gap experiments should discriminate among explanations

An early experiment is valuable when it changes a consequential decision. If the major uncertainty is dwell time at an accessible stop, building a high-fidelity battery simulation may produce precise but irrelevant data. Instead, a supervised boarding trial can estimate dwell-time distribution and identify human-interface failure modes. Record assumptions, sample selection, environmental conditions, and what observation would favor one concept over another. A test with no predeclared discriminatory question may be persuasive theater rather than learning.

When deriving lower-level requirements, preserve parent intent and avoid over-constraining the solution. A subsystem timing limit may be necessary because a larger scenario budget requires it, but the engineer should show how the allocated budget supports the top-level outcome. If architecture changes, derived constraints may need to change while the stakeholder objective remains stable. The fundamental distinction is that **mission needs define success, constraints bound acceptable means, and design choices select a means within those bounds**. Confusing them produces brittle baselines and artificially narrow trade spaces.

## Practice before the assessed course work

[Hypothetical Laboratory 4: Concept-neutral requirements and gap experiments](../labs/lab-04-conceptual-requirements-use-cases-gaps-and-experiment-p.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 4 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Step 03 integrated reference: NS-CD6.1 — derive concept-neutral and testable requirements

A requirement is useful when different candidate designs can be judged against the *same* obligation. “Deploy seven autonomous pods” is a design selection, not a concept-neutral stakeholder need. The [eight controlled requirements](../case/requirements.csv) state operational capacity, pickup wait, accessible offer coverage, cost, timing, fallback and evidence currency separately. Each names a measurement, units, scenario and proposed verification technique.

### Separate thresholds from evidence and assumptions

The capacity requirement CD6-R01 is written against the **effective** service envelope \(C\ge46.2\) trips/h. It is a constraint derived from 42 trips/h peak demand and a 10% planning margin; the utilization factors used to estimate \(C\) are not themselves requirements. CD6-R02 concerns the 90th percentile *of actual pickup waits in the event-day eligible request population*; it cannot be verified by computing the mean waiting time of already served riders.

CD6-R03 introduces another denominator: eligible locations and requested service conditions. The assumed 98% coverage of concept C is a model entry, not a verified population estimate. CD6-R06 distinguishes nominal timing (under 500 ms) from degraded behavior, which requires an explicit safe fallback. Bundling those into one vague “responsive system” statement would hide the fact that nominal analysis passes while a degraded chain fails.

### Build a traceability chain with independent failure modes

A useful trace is `stakeholder need → measurable requirement → scenario → function → concept allocation → predicted measure → verification method → evidence → decision`. Repeated IDs are not sufficient: the evidence must be applicable to the declared baseline, measurement conditions and population. The [evidence register](../case/evidence-register.csv) has an intentionally outdated CD6-R08 record from NS-CD6.0; it also leaves CD6-R02 planned rather than executed. This is a teaching counterexample to treating a green spreadsheet cell as a verified engineering claim.

### Design a risk-retirement experiment

For CD6-R01, a useful pilot controls event-day demand and records observed throughput, refusal rate, stops and accessible requests. The pass criterion must specify a window and confidence treatment; the simple design-estimate calculation does not determine those parameters. For CD6-R07, perform a moderated outage scenario with participants who require accessible booking and record successful trip offers, manual recovery time and reasons for failure. The experimental result should be able to alter the concept recommendation—not merely decorate the final presentation.

### Practice and explained answer

**Exercise:** Rewrite “The shuttle will pick everyone up quickly” into two separate measurable requirements. **Answer:** State (i) a defined population, time window, and p90 pickup-wait threshold, such as CD6-R02, and (ii) a defined eligible origin/time coverage threshold, such as CD6-R03. Attach measurement instrumentation and a refusal denominator. Do not substitute “dispatch command latency” for rider pickup wait: subsystem timing and mission outcome are different measures.

**Boundary:** Thresholds in this synthetic package are study assumptions. Real requirements must be negotiated with stakeholders and reconciled to regulations, accessibility obligations, operating constraints and resources.
