## Step 04 integrated case — NS-CE4.1: causal evaluation across authority boundaries

The enterprise-level question is not merely whether the resilient dispatch design passes a model screen. It is whether a governed intervention improves service for affected communities **without transferring risk, restricting access, or bypassing institutional consent**. A before-and-after plot can mislead when weather, staffing, economic conditions, and service eligibility change during the same period.

### Difference-in-differences as a conditional identification strategy

The synthetic pilot's mean wait falls from 22 to 16 minutes, a naive improvement of $-6$ minutes. The comparison area's mean falls from 20 to 18 minutes, a change of $-2$ minutes. The two-group, two-period difference-in-differences estimate is

$$\widehat\tau_{\rm DiD}=(16-22)-(18-20)=-6-(-2)=-4\ \text{min}.$$

Under **parallel untreated trends**, no differential concurrent interventions, consistent outcome definition and measurement, stable group composition, and manageable spillovers, this subtraction can help identify an average treatment effect for the treated. The case gives only one before and one after period; it **cannot establish parallel trends**, provide a meaningful sampling uncertainty estimate, or exclude confounding. The model therefore records `causal_claim_identified: false` even though the arithmetic is correct.

For accessible requests the pilot falls from 28 to 24 minutes, while the comparison group rises from 24 to 25 minutes. The analogous contrast is $(24-28)-(25-24)=-4-1=-5$ minutes. This illustrates potentially different treatment impacts; it does **not** demonstrate that the accessible service meets the threshold from Chapter 3. That chapter's request-level timely outcome is only 62.5% for the accessible group in a separate synthetic cohort. These two metrics use different populations and measures and should not be conflated.

### Causal diagrams and alternative explanations

A plausible causal graph includes intervention $Z$, wait time $Y$, pre-existing site capability $X$, storm severity $W$, staffing $S$, and rider eligibility $E$. Both $W$ and $S$ may affect where the intervention is deployed and how waits evolve. The potential-outcome contrast $E[Y(1)-Y(0)]$ is not identified by the same site's observed before/after values without a defensible counterfactual for $Y(0)$ after intervention. The comparison group supplies a candidate trend, but only if its untreated trend is appropriate.

Further complication: a successful dispatch algorithm may shift demand between service modes. Such **interference** violates a simple no-spillover assumption. A queue reduction for standard riders may coincide with more denied accessible requests; average minutes alone conceal the distributional cost. Deployed policies may also induce behavior change, supplier retraining, and feedback loops that make the early treatment effect unrepresentative of long-run results.

### Governance must be evaluated independently

A credible staged enterprise trial would preregister the time window, primary and subgroup outcomes, adverse-event definitions, data access, feedback collection, approval thresholds, and rollback triggers. Multiple operators and community representatives would review whether the outcome measure is legitimate. The four approval booleans in the controlled case are all false, so even a hypothetically favorable $\widehat\tau$ cannot authorize deployment. A signatory has to verify the safety, accessibility, privacy, and operational basis, not merely inspect a green score.

The integrated case fails distinct necessary conditions: Chapter 2 finds stale/inconsistent dispatch events; Chapter 3 observes unmet timely-service screens; Chapter 4 finds an analytically unstable storm queue; Chapter 5 finds only 20% actionable local evidence coverage; and this chapter cannot identify an operational causal effect. Fixing one condition does not cure the others. The enterprise plan should track each as a separately owned risk with measurable closure evidence.

### Worked policy review

**Worked exercise 1 — subtracting trends.** An executive claims the program caused the entire six-minute pilot improvement. What estimate does the toy comparison produce? **Solution:** $-4$ minutes, not $-6$. The extra two minutes are consistent with the comparison trend, but the -4 estimate remains conditional on unverifiable assumptions in this two-period dataset.

**Worked exercise 2 — selection bias.** Suppose storm-affected riders move out of the pilot group after the intervention, reducing measured wait. What changes? **Solution:** Group composition changes, making the pilot's before/after difference partly a population-selection effect. A stable cohort, explicit inclusion rules, and sensitivity analysis are needed before causal attribution.

**Worked exercise 3 — release gate.** All numerical screens are subsequently made green, but the accessibility consultation is unsigned. Can the integrated model declare deployment approved? **Solution:** No. Review and authorization require independently established institutional authority; approval is not a derived numerical quantity.

**Adverse case.** Change the comparison group's post-period wait to 16 minutes. Recompute the difference-in-differences: $(-6)-(-4)=-2$ minutes. The conclusion's dependence on counterfactual trends is transparent. Additional pre-periods, documented adoption, contemporaneous shocks, preregistered inference, and affected-party review remain necessary to progress beyond synthetic exercises.
