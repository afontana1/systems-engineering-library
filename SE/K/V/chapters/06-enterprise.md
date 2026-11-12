# 6 · Evaluating an enterprise intervention without confusing change with cause

*Graduate methods companion · Enterprise Systems Engineering (Book XIX)*

An enterprise system is partly technical, partly institutional, and partly political in the ordinary sense of conflicting legitimate interests. Optimizing a dispatch algorithm is not equivalent to improving regional mobility if agencies do not share authority, staff cannot act on recommendations, or disadvantaged communities experience greater service loss. The systems engineer must distinguish **mechanism**, **outcome**, **causal evidence**, and **legitimacy**.

## 6.1 Start with the outcome and its distribution

Northstar is considering a shared dispatch protocol across two independently governed transport agencies. Intended outcomes include fewer missed medical trips, faster service during incidents, and predictable handoff between agencies. The protocol also changes who can authorize deviations, who bears cost, and how failures are reported. A design that reduces average wait may still harm rural riders if the optimizer prioritizes dense routes.

Define outcomes by population and context: for subgroup $g$ let $Y_g$ represent missed-trip fraction, service time, or another measurable consequence. An average effect $\Delta\bar Y$ can hide opposite subgroup effects. Report disaggregated outcomes, operational coverage, uncertainty, and stakeholder-selected fairness constraints. Equity need not imply equal performance on every metric; it requires transparent treatment of whose losses and benefits the decision counts.

## 6.2 A before-after difference is not necessarily causal

Suppose an intervention district improves its mean service wait from 22 to 16 minutes, a 6-minute reduction. During the same period a comparison district improves from 20 to 18 minutes, a 2-minute reduction. A difference-in-differences estimate of the intervention effect is

$$\widehat\tau_{\mathrm{DiD}}=(16-22)-(18-20)=-4\ \mathrm{minutes}.$$

The interpretation is that the intervention is associated with an *additional* 4-minute reduction, conditional on a key assumption: absent treatment, the intervention and comparison areas would have followed parallel trends in the outcome. That assumption cannot be proven from a single before and after period. Examine multiple pretreatment periods, composition changes, seasonality, displacement, and policy spillovers.

If dispatches are redirected from the comparison district to support the treated district, the control is contaminated. If patient mix changes after a hospital closure, the outcome population is no longer comparable. If only completed trips are measured, a shift toward rejecting difficult requests can manufacture an apparently favorable mean.

## 6.3 Causal diagrams expose hidden pathways

A conceptual directed acyclic graph may include demand severity $D$, agency staffing $S$, policy $P$, and wait time $W$. Staffing may affect both adoption of $P$ and $W$, making $S$ a confounder. Demand severity may influence staffing decisions and waiting time. Adjusting for a variable *caused by* the policy may instead block part of the true effect or create selection bias. There is no universal rule that 'more covariates' gives a better causal estimate.

A defensible evaluation records the intervention's intended mechanism, the units assigned to it, the comparison strategy, plausible confounders, the time horizon, and falsification checks. In some settings randomization is possible; in others an interrupted time series, synthetic control, or carefully justified quasi-experiment may be appropriate. Each design has a distinct identifying assumption.

## 6.4 Feedback, incentives and implementation failure

Enterprise policy changes behavior. When a new performance target rewards short response times, teams may prioritize easily served trips or revise classifications. This is not always deliberate gaming; it can arise naturally from constrained resources. The measured indicator becomes a control input, changing the system being measured.

A stock-flow model of qualified operators might use

$$\frac{dN}{dt}=h(t)-a(t)-q(t),$$

where $N$ is the workforce stock, $h$ hiring/training completions, $a$ attrition, and $q$ temporary reassignment. Improving dispatch software without training enough operators may produce a backlog of authorizations. Because hiring and training are delayed, short-term staffing fixes can create oscillation or long-run capacity deficits.

Map feedback loops before proposing an enterprise transformation: new reporting improves visibility, which may trigger increased audit workload; increased workload can slow service, which provokes more reporting. The loop can be balancing or reinforcing depending on decision rules and delay.

## 6.5 Portfolio choices and governance boundaries

Enterprise architecture usually involves multiple projects with shared constraints: capital budget, specialized staff, network access, regulation, and public trust. A portfolio formulation might maximize $\sum_i v_i x_i$ subject to $\sum_i c_i x_i\le B$, where $x_i\in\{0,1\}$. But assigning a single dollar-equivalent value $v_i$ to every public consequence can erase distributional harm and non-negotiable constraints. A responsible portfolio process separates legally or ethically required minima from discretionary preferences.

Constituent systems retain their own missions. A regional interoperability contract must therefore specify decision rights, data usage permissions, emergency exceptions, dispute handling, joint incident review, and exit conditions. Technical connectivity alone does not establish shared authority or consent.

## 6.6 Evidence can support a trial without proving transformation

A plausible board decision is to authorize a restricted pilot in a clearly defined set of districts, accompanied by prospective success metrics, subgroup safeguards, independent incident reporting, and a pre-announced stop condition. The pilot should use an evaluation design capable of detecting unintended effects and should be reversible where feasible. 'We observed an improvement' is a finding; 'the policy caused the improvement' is a stronger inference; 'the policy ought to be expanded' adds a values and governance judgment.

## Worked problems with explained solutions

**A.** Calculate difference-in-differences from 22→16 and 20→18 minutes. **Solution:** $(-6)-(-2)=-4$ minutes under the identifying assumptions.

**B.** Why might a lower average wait be misleading after a route policy change? **Solution:** Demand composition, rejected requests, geographic reallocation, and adverse subgroup outcomes can change the reported denominator or distribution.

**C.** Name the stock and flows in a qualified-operator workforce model. **Solution:** Stock $N$; inflows of completed hiring/training, outflows of attrition and reassignment. Feedback and delays influence those flows.

**D.** A shared protocol improves network interoperability but removes local agency emergency override. Has the enterprise architecture necessarily improved? **Solution:** No. Decision authority, accountability, safety, resilience, and legitimacy may have worsened despite technical compatibility.

## Research challenge

Design a 12-month evaluation of Northstar's shared dispatch protocol. Specify three primary outcomes, two distributional safeguards, a defensible comparison strategy, an intervention-fidelity measure, independent incident review, and evidence required before expansion.

**Practice:** [Enterprise evaluation lab](../labs/06-enterprise.html) · [Causal-analysis notebook](../notebooks/06-enterprise.ipynb).

## 6.7 Heterogeneous effects and policy transport

An average causal estimate may be the wrong target when treatment effects vary sharply across regions. Let $\tau_g$ denote the effect for stakeholder group $g$. A policy can reduce overall mean waiting time while increasing wait for a smaller group. Transporting a pilot estimate to another district requires assumptions about differences in geography, staffing, demand, and authority. An intervention that depends on experienced operators may fail when adopted by an under-resourced agency even if the software implementation is identical.

In a multilevel system, assignment units and analysis units differ. If policy is adopted at the agency level but outcomes are recorded for individual trips, treating all trips as independent overstates the effective sample size. Clustered uncertainty or hierarchical modeling may be needed. Spillovers can further violate the idea that one agency's outcome is unaffected by another's treatment. The evaluation design should map such interference rather than treat it as a footnote.

## 6.8 Ethics and revisability as engineering requirements

The legitimacy of an intervention is not established only by aggregate efficiency. Stakeholders may value local accountability, informed consent, privacy, and the ability to contest an automated decision. These can be modeled as explicit constraints, design requirements, and governance processes. For example, a policy might require that every denied emergency trip has a documented explanation and a human appeal channel within a specified time. The requirement can be tested, while its normative adequacy still requires stakeholder deliberation.

A graduate-level enterprise recommendation should include a theory of change, causal identification strategy, implementation risks, distributional monitoring, reversal conditions, and a plan to learn from failure. It should also state who has authority to end the pilot. The technically simplest design may not be the institutionally viable one.

<!-- STEP04-CONNECTED-EVIDENCE-START -->
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
<!-- STEP04-CONNECTED-EVIDENCE-END -->
