# Chapter 12 — The final baseline is a reasoned technical argument

*Book V: Software Systems Engineering · Week 12 — Assess technology trends and defend the integrated software baseline*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 12](../labs/lab-12-assess-technology-trends-and-defend-the-integ.md) before attempting [the assessed Week 12 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w12.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **assess technology trends and defend the integrated software baseline** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Emerging tools and architectures can improve the system, but novelty is not a requirement. The capstone should defend architecture, threat and hazard analyses, delivery evidence and operating constraints as one coherent baseline. Distinguish demonstrated capability from forecast scalability and from speculative technology trends.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Software assurance is an argument constrained by operational evidence, not a declaration that all tests have passed.

### Distinguishing related ideas

Functional tests, fault injection, security evaluation and operational monitoring support different claims; none alone captures system-level adequacy.

### Interpretation and boundary conditions

A defensible release decision states residual risks and the mechanisms that will detect, contain and reverse unexpected behavior.

## Worked Northstar example

An executive asks to add AI-based dispatch to the verified shuttle release. A proof-of-concept accuracy score cannot justify the safety, privacy and reliability claims of a new controller. Treat it as a candidate change, identify new hazards, establish evaluation data and maintain fallback authority.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## Graduate synthesis: software baseline decisions under a changing threat and technology landscape

### Separate architectural invariants from implementation choices

Technology trends matter only insofar as they alter an engineering decision. Replacing a message broker, adopting a new autonomy library, or moving a service to an edge computer affects latency, security, maintainability, verification burden, and supplier exposure. A final baseline should protect stable system invariants—safe-stop authority, data provenance, accessibility rules, minimum observability—while documenting why particular technical mechanisms implement them. Otherwise a “future-proof” architecture is merely a collection of recent products.

Architectural fitness is multidimensional. A simple weighted score `V = Σ wᵢ vᵢ` can summarize competing attributes, but only when weights reflect stakeholder tradeoffs and scores are commensurate. A 10% latency improvement cannot compensate for violating a mandatory safety constraint just because the weighted total increases. Use *feasibility constraints* first (`p99 latency <= target`, authenticated safety command paths, specified fail-safe response), then compare admissible alternatives on cost, adaptability, and operating burden.

### Dependability is sustained behavior, not a passing release test

Software reliability differs from hardware wear-out. Defects may remain latent until a rare state or new environmental configuration activates them. For a service with incident arrival rate `λ` and average recovery time `MTTR`, the simple steady-state availability approximation `A = MTBF / (MTBF + MTTR)` is useful only when incident and repair processes fit its assumptions. A platform can report 99.9% uptime yet miss every critical morning dispatch window; *time-weighted availability* is not the same as mission-weighted availability. Evaluate service consequences and recovery distribution, not only aggregate uptime.

Suppose the dispatch service tolerates no more than 43.2 minutes of downtime per 30-day month for 99.9% availability. A single 50-minute failure breaches the objective even if the mean response latency stays excellent. Conversely, a maintenance interruption outside contracted service hours may have little operational impact. Model the agreed service window and safety-critical functions separately. Security changes also interact with availability: aggressive authentication retries can overload a recovery service during a network partition unless retry budgets and backoff are designed.

### Preserve proof obligations through upgrades

A technology migration should identify the claims it threatens, the old and new configurations, and the evidence needed to reestablish confidence. For a new sensor-fusion component, that might include data schema compatibility, closed-loop timing tests, fault-injection behavior, and a rollback strategy. A test passed on a simulation build is not automatically evidence for the deployed binary. Reproducible builds, dependency inventories, signed artifacts, and test-to-build provenance make the argument inspectable.

The design-review question is therefore *which properties must remain true as technology changes, and how will we know?* Record the invariants, change triggers, evidence owners, and operational constraints. For Northstar, adoption of a fashionable autonomy model is not justified until its failure behavior, observability, lifecycle support, and integration cost are credibly compared with the established baseline. Engineering maturity is the capacity to change without losing the reasons a system was trusted.

## What can go wrong—and why

Technology trend assessments should include opportunity cost, migration risk and the evidence that would cause a recommendation to change.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 12: The final baseline is a reasoned technical argument](../labs/lab-12-assess-technology-trends-and-defend-the-integ.md), you will: Defend an integrated software release packet, respond to one adversarial change request and issue a conditional go/no-go recommendation. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 12 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](11-manage-delivery-operations-maintenance-evolut.md) and leads toward your final course defense. Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w12.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: the release decision as a structured engineering argument

### Combine claims instead of averaging them

Book 5 concludes with the NS-SW5.1 release board. A successful model calculation is relevant, but the board must consider every mandatory obligation. The candidate service rate of 20 requests/s yields a *model-only* peak p95 proxy of **469.57 ms** against a 500 ms boundary. That result supports further testing, not production acceptance. The register simultaneously shows a availability-risk warning, stale build provenance and an unexecuted recovery drill. These are independent blockers, not low-scoring features that can be outweighed by performance.

| Decision dimension | Synthetic evidence | Engineering conclusion |
|---|---|---|
| Peak performance | Analytical queue proxy 469.57 ms at 10/s | Promising, needs end-to-end measurement |
| Availability | 36 of 43.2 allowance minutes used | Only 7.2 minutes remain |
| Release exposure | Hypothetical canary could consume 9 minutes | Exceeds budget by 1.8 minutes |
| Build identity | `BLD-50` belongs to NS-SW5.0 | Stale for NS-SW5.1 |
| Recovery | `DRILL-51` is planned but unexecuted | Recovery requirement open |
| Reservation invariants | Synthetic transaction checks pass | Useful but not distributed-field proof |

The correct decision in this teaching case is **NO-GO**. A conditional approval would need explicit authority and scope, renewed build evidence, executed recovery evidence, and an exposure plan compatible with the service policy. The table illustrates the logic; it does not replace a formal authorization process for a real system.

### A technology choice is an experiment with migration costs

A new message broker, managed database, service mesh or observability backend may reduce one weakness while adding dependencies, security surface, licensing constraints or team skill requirements. Evaluate alternatives using a capability claim, failure mode, migration mechanism, training and rollback plan, operational measurements and evidence refresh cost. Do not select a technology just because the vendor describes it as cloud native or fault tolerant.

A trustworthy adoption proposal names which requirements improve, which evidence becomes stale, how a canary would be measured, who can terminate it, and what would falsify the claimed benefit. Never reuse synthetic input as if it were operational data. Where an external standard is cited, check that the revision and use are appropriate to the project rather than declaring compliance by association.

### Capstone investigation

Run `python3 SE/K/B5/tools/step03_book5_system_check.py --json` from the root. Inspect the evidence status and edit a *copy* of the case to evaluate a hypothetical recovery-drill pass. **Question:** Would changing `DRILL-51` to a pass make release valid? **Answer:** No. SWS-02 remains at risk under the proposed canary, the build attestation remains stale, and nine prospective downtime minutes still exceed the 7.2-minute remaining budget. Correct release decisions must be conjunctions of required claims, not averages of unrelated measures.

**Connection to next studies.** The software system's assurance data should inform integration testing, lifecycle supportability, enterprise risk, and eventual systems-of-systems operations. Treat this chapter as a pattern for evidence-based technical review, not a shortcut to certification.
