# Chapter 1 — Framing before solutions

*Book 6: System Conceptual Design · Week 1 — Reopen the problem and audit the incumbent baseline*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 1](../labs/lab-01-reopen-the-problem-and-audit-the-incumbent-baseline.md) without looking at the solution → return to [Week 1 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w01.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **framing before solutions**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A solution-neutral problem statement is not a promise to consider everything. It fixes an outcome, affected population, operating envelope, and decision horizon while leaving implementable means open. Distinguish a true binding constraint from an inherited preference; the latter must be challenged as a hypothesis.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Conceptual design should first test whether the problem boundary and success criteria are right, because optimizing the wrong objective efficiently worsens the outcome.

### Distinguishing related ideas

A legacy solution is evidence about history and constraints, not proof that the same architecture is required in the future.

### Interpretation and boundary conditions

Reopen assumptions about riders, route geography and charging availability before comparing vehicle options.

## Worked engineering case

A 25-minute event-day accessible pickup is a service failure; it does not establish that autonomy is necessary. Compare fixed-route, staffed on-demand, accessible paths, and staged automation against arrival reliability and accessibility.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

An incumbent fleet can be technically impressive yet the wrong response to the underlying access need. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is the Phase 1 architecture and foundation books; the next connection is [Stakeholder evidence and current-state analysis](02-stakeholder-evidence-and-current-state-analysis.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Rewrite “purchase 12 autonomous shuttles” as an access outcome, then label five inherited design assumptions.

**Problem B — Adversarial review.** Would you let the current fleet architecture determine who is interviewed? Explain the distortion.

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: problem framing as causal inference and decision design

### A problem statement already contains a model

An engineering team rarely receives a neutral problem description. “The campus needs more shuttles” assumes that vehicle count causes poor service, even though dispatch logic, access policy, stop placement, or rider information may dominate the outcome. A sound problem framing separates an observed shortfall from a proposed intervention. State the observed outcome, the population and conditions for which it occurs, the competing explanations, and the decision that needs to be made. This keeps the engineering process from inheriting the incumbent architecture's assumptions before alternatives have been examined.

A causal diagram helps distinguish symptoms, mechanisms, and confounders. Suppose wait time increases during bad weather. Weather may simultaneously increase trip demand, reduce vehicle speed, and change riders' tolerance for walking. Correlation between vehicle utilization and wait time then does not establish that utilization alone is the root cause. Intervening on dispatch policy will have a different effect from increasing fleet size. The relevant question is counterfactual: what would the service outcome have been under a different feasible decision but otherwise comparable conditions?

### Outcomes, capabilities, and technical measures occupy different layers

A stakeholder may value completed accessible journeys, while engineers measure request-processing latency. Faster processing can support the outcome, but its effect depends on vehicle supply, boarding accessibility, reliability, and operating policy. The causal chain should be made explicit: an architectural variable changes a capability; that capability changes a service mechanism; that mechanism changes stakeholder outcomes under a demand scenario. An attractive technical measure without this chain can optimize a quantity with little mission value.

Define a problem as a decision under uncertainty. Let alternatives `a` yield uncertain outcomes `Y(a, θ)` where `θ` includes demand, human behavior, environment, and implementation performance. The organization values those outcomes through a utility or value model `U(Y)`, subject to mandatory constraints. This representation shows why early conceptual design should retain multiple alternatives: evidence may reveal that a presently attractive solution is highly sensitive to an uncertain assumption. A reversible experiment can be more valuable than an early irreversible commitment even when the experiment adds schedule time.

### Choosing measurements changes what can be learned

If demand is estimated from completed rides, unserved or abandoned requests disappear. The resulting data underestimates unmet demand and can justify exactly the wrong fleet policy. Similarly, surveys limited to existing riders exclude those for whom the service is inaccessible. Before collecting data, specify the target population, how observations enter the dataset, and how that selection mechanism might depend on the outcome. Missing demand is not zero demand. An initial stakeholder boundary that excludes nonusers creates both technical bias and a legitimacy problem.

A disciplined framing exercise for Northstar might compare three hypotheses: insufficient vehicles, inefficient dispatch, and inaccessible pickup locations. For each, name a distinguishing observable prediction and a plausible test. Fleet saturation during peaks supports the first hypothesis only if booking attempts and dispatch failures are measured; high empty-vehicle time with long waits points toward allocation or access mechanisms. No single diagnostic is conclusive. The initial concept gate should approve a question, an evidence plan, and explicit assumptions—not conceal uncertainty inside a prematurely selected product.

## Practice before the assessed course work

[Hypothetical Laboratory 1: Framing before solutions](../labs/lab-01-reopen-the-problem-and-audit-the-incumbent-baseline.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 1 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Step 03 integrated reference: NS-CD6.1 — distinguish the mission from the incumbent

The controlled [NS-CD6.1 concept study](../case/INDEX.html) begins before there is a preferred vehicle design. The decision question is: *Which service concept could provide reliable, accessible campus mobility within a bounded cost and operational envelope?* It is deliberately **not** “How do we deploy an autonomous shuttle?” Autonomy is a candidate means; access and completed journeys are the outcome. This distinction protects later analyses from validating a design merely because it resembles the incumbent.

### Construct a decision frame rather than a solution brief

Define (1) the beneficiaries and excluded groups; (2) the operational scenario; (3) the success metrics and their denominators; (4) nonnegotiable constraints; (5) the decision being authorized; and (6) the evidence that might overturn the preferred concept. For the case, the specified event surge is 42 requested trips per hour, and a 10% planning reserve raises the capacity screen to

\[C_{\min}=42(1+0.10)=46.2\ \text{effective trips/h}.\]

This is an **assumed study demand**, not a measured arrival distribution. A point estimate of capacity above 46.2 is necessary for screening, not proof of acceptable waits, wheelchair access, or recovery during faults. Keep three types of statement separate: stakeholder outcome (“eligible people can reach events”), performance requirement (“accessible-offer coverage at least 95%”), and implementation (“four fixed-route vehicles”). Only the third picks an architecture.

### Examine the incumbent without inheriting it

Four concept families remain open: fixed-loop A, pooled on-demand B, hybrid trunk-and-feeder C, and contracted broker D. The model yields effective peak capacities of 53.33, 47.60, 52.80, and 45.00 trips/h. If the team evaluated capacity alone, A would look strongest. Yet A's assumed accessible-offer coverage is only 92%, below the 95% requirement. Its apparent capacity advantage cannot compensate for a failed hard constraint. Conversely D's attractive capital estimate does not make its insufficient reserve capacity acceptable.

This is a **counterexample to premature optimization**: maximizing fleet throughput before defining who needs service can produce an apparently efficient design that systematically excludes intended users. Log every inherited assumption with an owner and a test; keep a competing explanation alive. For instance, a long pickup delay might result from scheduling, incomplete accessible-service coverage, or event surges—not necessarily insufficient automation.

### Reproducible inquiry and answer

Open [the controlled alternative table](../case/concepts.csv) and [checker](../tools/step03_book6_concept_check.py). **Exercise:** If the peak request estimate rises to 48 trips/h while the reserve requirement stays 10%, which concepts retain nominal capacity? **Answer:** The new threshold is \(48(1.10)=52.8\) effective trips/h. A (53.33) and C (52.80) reach that threshold under unchanged utilization, while B (47.60) and D (45.00) do not. But A still fails accessible coverage. Equal capacity at a single assumed operating point does not establish robust feasibility, so the next decision remains an experiment, not procurement.

**Boundary:** All figures in this example are synthetic. Before a real concept review, use observational demand data stratified by peak periods and accessibility needs, and make the uncertainty range explicit. NASA's [system-design guidance](https://www.nasa.gov/reference/4-0-system-design-processes/) treats stakeholder expectations, operational concepts, requirements, alternatives, and validation as an iterative loop rather than one-way architecture selection.
