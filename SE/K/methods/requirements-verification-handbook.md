# Requirements engineering and verification evidence

*Technical method guide · Requirements, measurement, test design, and assurance · Phase 1 expansion*

**What this chapter enables.** You should be able to convert a stakeholder outcome into a controlled technical obligation, allocate a quantified budget, develop a defensible acceptance test, and decide which requirement claims the resulting evidence actually supports. This is a complete illustrative procedure, not a substitute for a program-approved verification plan.

**Prerequisites:** [Stakeholder needs](../encyclopedia/stakeholders-and-needs.md), [system boundary](../encyclopedia/system-of-interest.md), [good requirements](../encyclopedia/good-requirements.md), and [verification versus validation](../encyclopedia/v-and-v.md).

## 1. An assurance chain starts with two different questions

Suppose the fictional Northstar Campus Shuttle program wants riders to obtain an assignment promptly, including during the morning rush. The stakeholder outcome is **predictable access to transportation**. An engineering team might define a measurable dispatch acknowledgement requirement. That technical requirement is only a *proxy* for part of the original outcome: fast assignment does not imply a vehicle arrives promptly or that riders with accessibility needs have equitable service.

Write an explicit chain:

1. **Need N-01:** riders can reliably obtain transportation during published service periods.
2. **Operational scenario S-01:** peak weekday demand, with nominal network availability and an offered load defined by a reproducible load generator.
3. **System requirement R-ACK-01:** the dispatch service shall return a definitive acceptance or rejection response within **4.0 seconds** for at least **99% of eligible requests** in scenario S-01.
4. **Architecture obligation A-ACK:** the inbound gateway, queue, scheduling algorithm, and notification interface must jointly support R-ACK-01.
5. **Verification case T-ACK:** a controlled test observes the request-to-response interval, with a predetermined sampling plan and decision rule.
6. **Evidence E-ACK:** source timestamps, code/build identifier, scenario parameters, instrument calibration, sample accounting, and reviewed results.
7. **Validation activity V-RIDE:** measure actual pickup delays and rider outcomes separately in representative service conditions.

The values and conditions above are **hypothetical teaching choices**. They are not a safety standard or a validated service-level target.

## 2. Design a requirement record rather than an isolated sentence

The requirement is not complete until terms and configuration are governed. The following is a compact reference record.

| Field | Example and why it matters |
|---|---|
| Identifier and revision | `R-ACK-01`, revision `B`; tests must cite the applicable revision |
| Subject and action | Dispatch service returns one definitive response |
| Trigger and start time | Receipt of a syntactically valid, unique request at the service ingress |
| End time | Response fully emitted at the controlled service-egress boundary |
| Population | Eligible requests; exclusion rules are approved *before* the run |
| Operating conditions | S-01 peak-load profile; software build, hardware, network, clock source, and seed recorded |
| Quantified claim | At least 99% meet 4.0 seconds |
| Verification method | Instrumented system test; independent log reconciliation |
| Decision authority | Named verification lead; exceptions cannot be silently discarded |
| Parent and rationale | N-01, S-01, expected user benefit, and documented assumptions |

A requirement can be unambiguous and still be **wrong for the mission**. Validate the *need-to-requirement translation* by asking users whether acknowledgement latency is causally related to what they value. Keep a separate response to rejection, retry storms, outages, and accessible communication needs; combining these into one statement hides failure modes.

## 3. Derive and check a timing allocation

A budget communicates engineering responsibility. For a simplified **serial, single-request critical path**, suppose a team proposes:

| Segment | Proposed engineering allowance |
|---|---:|
| Ingress parsing | 0.15 s |
| Authentication and gateway | 0.35 s |
| Queue and dispatch wait | 0.55 s |
| Scheduler | 1.15 s |
| Outbound response | 0.60 s |
| Contingency allocation | 0.70 s |
| **Allocated path** | **3.50 s** |
| **Unallocated headroom to 4.00 s** | **0.50 s** |

For the declared *serial worst-case allocation model*,

\[
T_{\mathrm{allocated}}=\sum_{i=1}^{5}T_i+T_{\mathrm{contingency}}=3.50\ \mathrm{s}.
\]

This is not a proof that 99% of requests respond within 4 seconds. If the values are 95th-percentile times, **their sum is not generally a 95th or 99th percentile** of the total. Queueing delay depends on arrival patterns and utilization. Parallel paths, shared resources, failures, and correlations require explicit modeling. Identify both the budget owner and the evidence needed to support every allocation.

**Change exercise.** If a new identity provider adds 0.65 seconds to the gateway bound, the allocated path becomes 4.15 seconds and exceeds the system threshold. A design change or requirement renegotiation is required; moving the number into “margin” without a technical plan is not an engineering solution.

## 4. Convert a percentile claim into a statistical test

The claim “at least 99% of eligible requests meet 4.0 seconds” is about a population proportion, not a sample maximum. Define an indicator for each eligible observation:

\[
X_i = \begin{cases}1,& T_i \leq 4.0\ \mathrm{s}\\0,& T_i>4.0\ \mathrm{s}.\end{cases}
\]

Let \(p_f=P(X_i=0)\) be the unknown failure probability in the *specified test population*. In a simplified independent, identically distributed Bernoulli model, if **zero failures** appear among \(n\) observations, then a one-sided exact \(100(1-\alpha)\%\) upper confidence limit is

\[
p_{f,U}=1-\alpha^{1/n}.
\]

For \(\alpha=0.05\) and \(n=300\), \(p_{f,U}\approx 0.00994\). Thus **300 zero-failure observations** provide a one-sided 95% confidence upper limit just below a 1% failure probability, *under those sampling assumptions*. The theoretical minimum is

\[
n\geq\left\lceil\frac{\ln\alpha}{\ln(1-p_{f,\max})}\right\rceil=299.
\]

That is not proof of zero risk, and the 95% confidence statement is about the statistical procedure's long-run coverage, not a 95% posterior probability that the parameter lies below 1%. If repeated requests share a common outage, trial independence fails; 300 tightly clustered events are not equivalent to 300 independent operational conditions. A program must justify representative load profiles, stratification, dependence, and sample selection.

For \(k>0\) failures, the one-sided exact binomial upper bound solves

\[
\sum_{j=0}^{k}{n\choose j}p_{f,U}^{j}(1-p_{f,U})^{n-j}=\alpha.
\]

The accompanying [standard-library verification calculator](code/verification_confidence.py) computes this bound from a latency CSV. It intentionally does **not** label a test result “verified”: statistical bounds are only one piece of the evidence review.

## 5. Measurement uncertainty changes a pass/fail decision

A measured time has instrument and synchronization uncertainty. For an *individual maximum-time requirement* (different from the 99% population claim), suppose the reported measured duration is 3.93 seconds with an expanded uncertainty of ±0.12 seconds at a declared coverage level. If the approved conservative rule requires the **upper uncertainty limit** below 4.0 seconds, the result is not a pass:

\[
3.93+0.12=4.05\ \mathrm{s}>4.00\ \mathrm{s}.
\]

Conversely a 3.82-second reading gives 3.94 seconds and passes that particular guard-banded rule. Do not automatically add ±0.12 seconds to each event and then apply a binomial model without defining how common-mode clock bias, event-level noise, and the percentile decision interact. Measurement uncertainty and operational variability are different phenomena.

## 6. A verification matrix must carry the *result*, not just the link

| Requirement | Method / case | Configuration | Acceptance | Recorded disposition |
|---|---|---|---|---|
| R-ACK-01 rev B | System timing test T-ACK | build `NS-2.3`; S-01 | One-sided 95% upper \(p_f\leq0.01\); approved sampling assumptions | **Pending** until data, uncertainty, and representativeness are reviewed |
| R-REJECT-02 rev A | Interface test T-REJECT | build `NS-2.3` | Each invalid request receives specified error code | **Pending** unless relevant executed evidence exists |
| N-01 | Rider validation V-RIDE | operational pilot | Stakeholder-approved service outcomes | **Not verified by T-ACK**; different evidence question |

A completeness number such as 100% “tests linked” only means the trace graph is populated. The review should distinguish **planned**, **executed**, **passed**, **accepted evidence**, **waived with authority**, and **not applicable**. Test data for build `NS-2.2` should not close a requirement about `NS-2.3` without documented equivalence or re-verification rationale.

### The minimum evidence packet

Keep the approved requirement revision; procedure revision; test article and build; software and calibration records; random seeds and generated demand; exact time origin; raw data; rejected/excluded events; deviations; uncertainty calculations; result summary; independent review; and a decision memo identifying the supported claim and unresolved limitations. A summary screenshot cannot replace the underlying observations.

## 7. Failure modes that invalidate otherwise impressive results

- **Wrong denominator:** excluding timeouts or invalid-looking responses *after* seeing the data biases the success fraction.
- **Wrong environment:** running at idle load says nothing about S-01 peak demand.
- **Wrong clock:** comparing timestamps from unsynchronized clocks can create fictitious speed or delay.
- **Wrong configuration:** a green result from an obsolete software build is not current evidence.
- **Wrong claim:** dispatch acknowledgement cannot, by itself, validate rider pickup time.
- **Wrong statistical model:** clustered observations may not support a binomial independence model.
- **Wrong incentives:** reaching “99%” overall can conceal poor outcomes for a relevant subgroup; report strata and operational exclusions.

## 8. Guided application with a worked answer

**Problem.** In a peak-load rehearsal of 12 requests, 11 finish within 4 seconds and one takes 4.1 seconds. Can the team close the 99% claim at one-sided 95% confidence?

**Solution.** No. The observed failure rate is 1/12 ≈ 8.33%, already above 1%. More importantly, such a tiny run provides weak population evidence. Calculate the exact one-sided upper confidence bound using [the bundled calculator](code/verification_confidence.py) and [sample data](data/latency-rehearsal.csv). Inspect whether one slow request was part of a correlated burst; its cause matters for the engineering response. Regardless of the statistical outcome, the team must review configuration and coverage before accepting evidence.

**Follow-on exercise.** Design a stratified plan that includes nominal connectivity, degraded connectivity, morning load and low-demand periods. Which strata belong inside the requirement's applicability conditions, which require separate requirements, and what statistical procedure accommodates the planned strata?

## Source basis and curriculum connections

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — lifecycle engineering and product verification/validation distinctions.
- [NASA Systems Engineering Handbook appendices C–E](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — requirement wording, verification matrix, validation plan.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — binomial and statistical methods context.
- [Book 1, Chapter 4](../B1/chapters/04-requirements.md), [Book 8, Chapter 10](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md), [EN.645.662 course](../../C/P0/EN645662.md), [EN.645.769 course](../../C/P2/EN645769.md).
- [Requirements concept](../encyclopedia/good-requirements.md), [verification matrix concept](../encyclopedia/verification-matrix.md), [traceability concept](../encyclopedia/traceability-graph.md).

**Scope note.** All numbers, configurations, and Northstar scenarios are invented for instruction. External sources provide methodological context; they have not reviewed these examples or established that this fictional system is acceptable.
