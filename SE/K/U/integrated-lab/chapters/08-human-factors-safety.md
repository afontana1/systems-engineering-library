# L08 · Hazards, human factors, accessibility, and assurance limits

**Learning time:** 4–7 hours. **Gate:** Preliminary safety and human-factors review. **Prior reading:** [F07](../../flagships/F07-human-factors-and-safety.md).

## Technical correctness is not sufficient safety

A mathematically consistent scheduling algorithm can still produce harmful outcomes. A passenger with a mobility aid may need accessible boarding, longer dwell time, and reliable communication with a dispatcher. A trip treated as one fixed 12-minute unit conceals those needs. The [hazard log](../data/hazards.csv) names four early hazards, but it is intentionally incomplete. Hazard identification is iterative and contextual; a checklist without participant involvement is not an adequate human-factors process.

Consider a control structure: a rider submits a request, software creates an allocation, a dispatcher decides whether to accept and communicate it, and a vehicle operator executes or refuses the task. Relevant feedback includes service status, accessibility needs, time, and environmental conditions. Unsafe control actions may include allocating a vehicle when none can safely operate, failing to communicate refusal to the rider, or assigning a pickup without necessary assistance. These are **plausible teaching hypotheses**, not a completed hazard analysis for a real mobility service.

## Risk is not a decorative heat map

The example risk register uses unknown likelihood rather than inventing probabilities. Numerical risk-priority scores can hide uncertainty when severity is high and frequency is unknown. In this case, `H-03`—a vulnerable rider left without transport under degradation—has potentially serious consequences. The model detects limited capacity, but has no operator intervention or equitable fallback policy. Therefore the proposed control is a *future requirement*, not an implemented risk reduction.

Human-centered design requires observation and dialogue: cognitive workload, error tolerance, accessible instructions, timing, language, and escalation pathways. A fast interface with confusing failure messages can increase risk even if algorithmic averages improve. Ethics and stakeholder legitimacy must be built into acceptance criteria, not added as a concluding paragraph.

## Engineering activity

1. Draw a functional control structure that includes the passenger, dispatcher, software, and vehicle operator. Mark control commands and feedback signals.
2. Identify at least three unsafe control actions, their plausible causal contexts, and what evidence would be necessary to determine whether a control works.
3. Draft an accessibility validation protocol (participants, consent, scenarios, observable outcomes, bias reduction, privacy, and stopping rules). Clearly label it **not performed**.
4. Review `H-01` through `H-04` for their residual uncertainty and propose at least two new human-centered hazards; do not claim they are closed by unit tests.

## Knowledge check and explained answer

**Question.** A simulated scheduler avoids vehicle overlap. Does that close the double-assignment hazard?

<details><summary>Show explanation</summary>

Only within this single-threaded simulated allocator. A deployed service would need evidence for concurrency, human overrides, stale state, vehicle location, network delay, hardware faults and independent operational controls. Hazard closure depends on context-specific evidence, not one invariant's passing test.

</details>

**Gate evidence:** preliminary control structure, causal hazard analysis, proposed accessible user study, and residual-risk statement with decision authority identified.
