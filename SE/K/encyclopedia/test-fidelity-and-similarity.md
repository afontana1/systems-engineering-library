# Test fidelity and similarity: deciding what laboratory evidence transfers

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## Fidelity is relative to a decision

**Test fidelity** describes how faithfully a test represents the aspects of the intended operational system and environment that matter for a particular decision. Physical resemblance is not sufficient. A high-fidelity graphical simulator may omit network delays essential to command safety, while a visually simple hardware-in-the-loop rig may faithfully reproduce timing and electrical behavior for the very property being tested. The relevant question is: *Which causal mechanisms does this evidence preserve, and which does it omit?*

A defensible similarity argument identifies a source test article, target system, governing mechanisms, dimensionless relationships or critical parameter ranges, boundary conditions, measurement chain, software and hardware configurations, and meaningful discrepancies. NASA-STD-7009B frames model credibility around intended use, verification, validation and uncertainty characterization. NASA's "test as you fly" philosophy encourages representative configurations; neither statement implies that every environment or operational event can be reproduced exactly.

## A transfer-of-evidence argument

Represent a test claim as `C=(configuration, environment, operating modes, property, tolerance, population)`. Evidence from a different configuration `C'` transfers only if discrepancies are analyzed and either shown irrelevant or bounded conservatively. For example, a laboratory test of two software nodes sharing one clock cannot demonstrate behavior under real cross-clock skew unless timing and communication assumptions are addressed. Evidence from a single carefully tuned prototype does not, by itself, establish manufacturing variation across a fleet.

When physics is dominated by ratios rather than individual variables, similarity analysis can help. For mechanical or fluid systems, nondimensional groups may control behavior, but their selection requires an adequate physical model. Geometry scaling, material properties, thermal boundary conditions and time scaling can conflict. Do not call two tests similar solely because their plots look alike.

## Worked example: scenario coverage is not event probability

Suppose a shuttle verification suite contains 100 scenarios, and 90 pass. Reporting "90% operational reliability" is invalid: scenarios are not necessarily sampled from the operating distribution, and a pass/fail count is not a demand-weighted estimate. If the ten failures all involve a rare but catastrophic boarding hazard, the result is not interpretable as a benign 10% deficit. Conversely, a targeted hazard suite can intentionally over-sample uncommon conditions. Test coverage tells us what was exercised; reliability requires an appropriate denominator, statistical sampling assumptions and observed outcomes.

For an illustrative operational weighting, suppose 80% of demands occur under condition A with estimated success 99%, and 20% under condition B with 90% success. If these are credible conditional probabilities and the mixture weights are appropriate, overall success is `0.8×0.99 + 0.2×0.90 = 0.972`, or 97.2%. This calculation is *not* a conclusion justified by a 100-scenario convenience suite; it requires population and dependence evidence. If the mixture changes during a storm or supply outage, the overall figure changes.

## Design experiments around the gap

Prioritize the unknowns that could reverse an acceptance decision: time-sensitive behavior, coupled environmental loads, human handoff, fleet communication, sensor degradation, uncommon fault combinations and software update sequencing. Combine analytical, laboratory, simulated, field and operational evidence with explicit provenance. Report discrepancies and sensitivity, rather than burying failed cases under a high aggregate score. A model-to-physical comparison requires calibrated inputs, independent checks and a justified validation domain.

## Limits and review questions

An effective review asks: What mechanism do we think causes failure? Which parts of that mechanism are reproduced? Where could the test apparatus change the result? How were operating conditions sampled? What constraints limit transfer to fielded units? What evidence remains absent? A passing test supports only the bounded property, configuration, environment and population for which the test was designed and justified.

## Selected source-to-claim references

- **F1 · Model verification, validation, uncertainty and credibility for intended use.:** [NASA-STD-7009B, Standard for Models and Simulations](https://standards.nasa.gov/standard/nasa/nasa-std-7009). Model verification, validation, uncertainty and credibility for intended use.
- **F2 · Flight-like configuration and operationally representative verification philosophy.:** [NASA GSFC GOLD Rules, Test as You Fly (rule 1.09)](https://standards.nasa.gov/system/files/tmp/GSFC-STD-1000RevI_Approved_0.pdf). Flight-like configuration and operationally representative verification philosophy.


## Step 02 review exercise: evidence transfer under a changed configuration

**Decision.** A bench rig demonstrates a controller responds within 120 ms when sensor packets arrive at 20 Hz. In operation, sensor packets may arrive at 8 Hz and have up to 40 ms of timestamp skew. The pass result does not by itself transfer: the rig has not represented the operational arrival process or the clock boundary. At 20 Hz, the nominal interarrival interval is \(1/20=0.05\) s. At 8 Hz it is \(1/8=0.125\) s, a **75 ms** increase. If the controller only evaluates new data on arrival, the possible sampling contribution already exceeds the rig's by up to 75 ms even before accounting for skew or execution time.

**Method.** Define the target claim (maximum age of information at the point of control), the test's sampling and clock assumptions, then build a discrepancy budget. Use \(A_{\rm op}\leq A_{\rm bench}+\Delta_{\rm sample}+\Delta_{\rm skew}+\Delta_{\rm other}\) only if the increments are justified as worst-case bounds *for the same age definition*. Here a hypothetical 120 + 75 + 40 = **235 ms** conservative budget would fail a 180 ms target. Do not add the quantities as though they were independent random errors unless the probability model warrants it. The remedy may be higher sampling frequency, bounded interpolation or an operational hardware-in-the-loop test.

**Exercise (solution included).** If the target is 250 ms and another 25 ms of bounded transport delay is established, is the 235 ms estimate sufficient? **No:** the conservative total becomes 260 ms. Also check that all component bounds can legitimately occur together. A different test population, software baseline, sensor accuracy or failed-case sampling can invalidate the transfer regardless of the timing arithmetic.

## Follow the knowledge

- **Prerequisites:** [Verification, validation, and acceptance: the three different decisions](v-and-v.md), [Simulation verification, validation, and credibility](model-vv-and-credibility.md).
- **Related concepts:** [Environmental qualification: test severity is not operational realism](environmental-qualification-and-test-levels.md), [Human systems integration: people are part of the architecture](human-systems-integration.md), [Assurance cases: what evidence supports which engineering claim?](assurance-cases-and-evidence.md).
- **Go deeper:** [Book 8 · Chapter 6: Qualification procedures and readiness](../B8/chapters/06-write-formal-qualification-procedures-and-conduct-the-t.md), [Book 8 · Chapter 8: Environmental and specialty qualification](../B8/chapters/08-plan-environmental-quality-reliability-maintainability-.md), [Book 12 · Chapter 08 — Model natural and man-made environments as dynamic, correlated scenario systems](../B12/chapters/08-model-natural-and-man-made-environments-as-dynamic-correlated-scenar.md).
