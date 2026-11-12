# NS-GS4.1 — Eleven-station graduate engineering methods laboratory

This is a **synthetic, offline and reproducible** emergency-access program, not field data or deployment authorization. The exercise does not replace the eleven original laboratories or notebooks. Reproduce results with `python3 ../code/ns_gs_case.py` when working in this lab folder, or from the repository root with `python3 SE/K/GS/integrated/code/ns_gs_case.py`. Inputs: [controlled JSON](../data/ns-gs4.1-case.json); [computed results](../outputs/ns-gs4.1-results.json); [executable model](../code/ns_gs_case.py); [claim/method crosswalk](../data/claim-method-crosswalk.csv).

## Two independent decision checks

Compute a **hard-gated** feasibility predicate instead of ranking infeasible choices by weighted means:

\[F_p=\bigwedge_{s\in S}\left(t_{ps}\ge t_{min}\;\land\;a_{ps}\ge a_{min}\right).\]

For cross-domain credibility, the final approval logic additionally requires current evidence, affirmative authority records and an explicit no-group-harm condition:

\[A=F_p\land E_{current}\land P_{authorized}\land H_{no\ harm}.\]

These formulas encode *conditions to check*, not a claim that the synthetic thresholds are approved project requirements. A HOLD result should identify missing evidence and accountable decision owners.

## Workflow, result control and negative evidence

Run the model unchanged, record the output file's SHA-256 hash, then copy the input data into a separate working file and make one change at a time. Do not overwrite the controlled original for an exercise. Run `python3 -m unittest discover -s SE/K/GS/integrated/code -p 'test_*.py'` from the repository root. Every station has a calculation, a falsification test, and an evidence decision. Keep a requirement → method → artifact → decision chain, identify synthetic versus observed values, and distinguish numerical verification from validation.

## Station 1 — Evidence-qualified schedule and costs

Study: [chapter 02-earned-value](../../chapters/02-earned-value.html). Claim ID: `C-COST`.

**Task.** Reconstruct ordinary CPI, evidence-qualified CPI, both EACs, and the implications of the 0.95M forecast gap.

**Explained checkpoint.** CPI 0.8; evidence CPI 0.675; trend EAC 11.25M; bottom-up EAC 10.3M. Neither is deployment proof. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 2 — Correlated energy and reserve constraints

Study: [chapter 09-parametric-models](../../chapters/09-parametric-models.html). Claim ID: `C-ENERGY`.

**Task.** Derive the traction-plus-auxiliary energy budget with units. Recompute after reducing auxiliary load until the headroom is zero.

**Explained checkpoint.** Consumption 22 kWh; available energy above reserve 21.636 kWh; margin −0.364 kWh; auxiliary reduction ≈0.1213 kW. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 3 — Numerical event localization

Study: [chapter 12-hybrid-simulation](../../chapters/12-hybrid-simulation.html). Claim ID: `C-EVENT`.

**Task.** Derive exact event-crossing time and compare Euler approximations at 0.5, 0.25 and 0.125 hours. Explain the false negative.

**Explained checkpoint.** Exact crossing ~2.95445 h; coarse Euler ends 4.125 kWh and misses the threshold; final approximation error halves when step halves. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 4 — Delayed feedback stability

Study: [chapter 13-feedback-dynamics](../../chapters/13-feedback-dynamics.html). Claim ID: `C-FEEDBACK`.

**Task.** Derive characteristic roots for instant and delayed feedback and test gains 0.7 and 1.2.

**Explained checkpoint.** Instant stability 0<g<2; one-step-delay stability 0<g<1. Gain 1.2 oscillates with growing magnitude. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 5 — Hard constraints and scenario-weighted decisions

Study: [chapter 14-decision-science](../../chapters/14-decision-science.html). Claim ID: `C-DECISION`.

**Task.** Compute each scenario-weighted policy score and apply **per-scenario** hard accessible and timely constraints.

**Explained checkpoint.** Integrated weighted timely 0.933, weighted access 0.917 but compound case fails; screening coverage 0.80 under invented scenario weights. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 6 — Accepted versus engineering flow boundaries

Study: [chapter 15-agile-flow](../../chapters/15-agile-flow.html). Claim ID: `C-FLOW`.

**Task.** Show how admitted WIP and accepted throughput change Little-law lead time and identify nonstationarity risks.

**Explained checkpoint.** 18/0.75=24 days internal; 18/0.60=30 days evidence-backed. Little-law assumes a stable coherent boundary. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 7 — Revision/freshness/approval provenance

Study: [chapter 16-digital-thread](../../chapters/16-digital-thread.html). Claim ID: `C-TRACE`.

**Task.** Evaluate all four evidence records against version, age, approval and the stricter operational authority gate.

**Explained checkpoint.** Only 1 of 4 requirement evidence paths actionable; R-SAFETY stale/unapproved, R-INTEROP revision-mismatched, R-PRIVACY unapproved. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 8 — Difference-in-differences causal identification

Study: [chapter 17-process-causality](../../chapters/17-process-causality.html). Claim ID: `C-CAUSAL`.

**Task.** Recalculate the pilot DID when the control post mean falls to 13 minutes; specify missing causal assumptions.

**Explained checkpoint.** Original DID −4 minutes; revised DID 0 minutes; cannot claim causality without credible parallel trends and no interference. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 9 — Common cause and throughput min cut

Study: [chapter 18-mission-networks](../../chapters/18-mission-networks.html). Claim ID: `C-NETWORK`.

**Task.** Derive parallel-path reliability with common-cause outage and analyze a 60-slot dispatch outage.

**Explained checkpoint.** Independent 0.99506; common-cause 0.9552576; after dispatch outage 60<62 accessible requested slots. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 10 — Dependency-aware enterprise choices

Study: [chapter 19-enterprise-portfolios](../../chapters/19-enterprise-portfolios.html). Claim ID: `C-PORTFOLIO`.

**Task.** Enumerate feasible portfolio subsets with dependencies. Explain why backup+inclusion is invalid.

**Explained checkpoint.** Best illustrated value 3.9 with inclusion+interop costing 1.35M/staff 4; backup requires assurance, so backup+inclusion alone violates dependency. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Station 11 — Distributional harm and decision authority

Study: [chapter 20-critical-interventions](../../chapters/20-critical-interventions.html). Claim ID: `C-EQUITY`.

**Task.** Demonstrate mean improvement versus rural harm. Discuss approvals, grievance channel and reversible stop rule.

**Explained checkpoint.** Mean wait improves 15→13.25 minutes while rural wait worsens by 5; road, labor and privacy approval flags are false; HOLD. A correct number is necessary but insufficient: state which parameter might falsify the conclusion, who owns the affected decision, and what empirical or review evidence would change the disposition.

**Negative test.** Change one controlled input to an invalid value or an adverse but physically meaningful case. Confirm whether the model rejects an invalid type, changes the computed conclusion, or correctly refuses an authorization inference. Record the new input and resulting output without silently replacing the supplied reference.

## Final synthesis and submission

Submit (1) calculation notebook or annotated Python run, (2) eleven-row claim/evidence matrix, (3) four-column uncertainty taxonomy distinguishing aleatory, epistemic, numerical and governance uncertainty, (4) at least three deliberately adverse inputs, (5) corrections to invalid evidence, and (6) a **HOLD** or bounded experiment recommendation. Required minimum approval conditions include current requirement-specific evidence, passing all mandatory scenarios, no imposed group harm, and affirmative authority records. Where those conditions fail, specify a responsible owner and a measurable next action rather than deleting the condition. The tests verify arithmetic and repository publication; they do not validate a real emergency service.
