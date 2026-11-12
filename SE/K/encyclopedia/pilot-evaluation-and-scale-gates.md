# Pilot experiments, red teams, and scale decisions

**Reference entry · Enterprise transition, improvement evidence and independent review**

## The distinction among trial, evaluation and adoption

A pilot tests whether a proposed intervention works in a defined setting. An **implementation trial** also asks whether people can actually operate, maintain and govern the change. A scale decision must account for selection bias, dependencies, costs, training, transferability, harms and recovery if the intervention fails. A positive demonstration against an easy scenario is not evidence of general readiness. A red team should independently challenge assumptions, implementation pathways and adverse outcomes rather than merely review slide quality.

Write an evaluation charter before the pilot: problem and target population; stakeholder values; comparison condition; primary and safety measures; data collection window; inclusion/exclusion rules; noninferiority or improvement criteria; statistical approach; decision authority; escalation triggers; and rollback. Lock down the measurement definitions; do not select a favorable metric after inspecting the data. Record organizational and technical dependencies such as onboarding capacity, supplier support, security reviews and incident response staffing.

## Worked comparative pilot

Suppose a new dispatch workflow is piloted while a similar nonpilot service continues unchanged. Synthetic mean waiting times (minutes) are:

| Group | Before | After | Change |
|---|---:|---:|---:|
| Pilot | 30 | 24 | −6 |
| Comparison | 29 | 28 | −1 |

A simple difference-in-differences point estimate is

\[
(24-30)-(28-29)=-6-(-1)=-5\ \text{minutes}.
\]

The interpretation is **five minutes more improvement than the comparison group** under assumptions that include parallel counterfactual trends and no interference. These four means provide no standard error or confidence interval; sample counts, variance and clustering would be required. If the pilot received more experienced staff or an easier route mix, the estimate may be biased. The calculation is a prompt for causal critique, not a validated effect.

## Red-team the scale claim

Challenge at least five families of assumptions: **causal identification** (selection and seasonality); **technical margins** (traffic, latency, interface faults); **human adoption** (training, access, error recovery); **enterprise execution** (funding, suppliers, operating support); and **assurance** (hazard controls, security, privacy, evidence currency). Require a contradiction log: claim, strongest counterexample, test or source, severity, decision effect, owner and closure status. A team should not be allowed to close a safety-critical contradiction merely because project benefits are attractive.

A rational gate offers more than go/no-go: expand, revise, run a discriminating experiment, deploy conditionally in a narrow envelope, suspend, or reverse. Assign each open uncertainty a trigger and owner. A staged deployment should preserve version mapping so a new software release cannot inherit pilot evidence without reviewing relevant differences.

## Exercise with solution direction

If the comparison service improves by 4 minutes instead of 1 while the pilot remains unchanged, the difference-in-differences estimate becomes \(-6-(-4)=-2\) minutes. Explain why apparent gains can change without modifying the pilot data. Identify one plausible selection mechanism and an empirical check. Draft three scale-gate conditions: an outcome threshold, a safety stop rule, and a support readiness threshold.

## Primary sources and caveats

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — transition, technical assessments, validation and decision analysis.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — experiment design and statistical evaluation.

Related: [design-risk retirement](design-risk-retirement.md), [process improvement](process-improvement.md), [critical systems thinking](critical-systems-thinking.md), [stakeholder needs](stakeholders-and-needs.md). The comparison example is invented; a difference-in-differences estimator requires defensible design and uncertainty analysis before causal inference.
