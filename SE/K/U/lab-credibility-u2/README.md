# NS-U2.1 — Independent cross-lab credibility and evidence challenge

**Scope:** the preserved [v11 integrated laboratory](../integrated-lab/README.html) (ten stages) and [v12 advanced laboratory](../advanced-lab/README.html) (eight stages). This U2 extension runs the two original models **as different software systems** and examines what their results can and cannot establish. The existing scenarios, requirements, source code, notebooks and tests are not overwritten.

## Start and reproduce

From `SE/K/U/lab-credibility-u2` with Python 3.10+ and its standard library:

```bash
python -m unittest code.test_bridge -v
python -m code.bridge
```

Run `python -m unittest discover -s tests -v` in each original v11/v12 laboratory to run their original tests. The bridge runs the two existing `src` modules independently using isolated subprocesses and temporary output directories, so Python packages with the same name cannot contaminate each other. It runs both twice and checks byte-identical output files. The cross-lab report is saved as [JSON](outputs/u2-cross-lab-results.json).

The [controlled gate rules](data/gates.json) are invented teaching criteria, not negotiated service obligations or actual approvals. The [18-stage crosswalk](U2-OUTCOME-CROSSWALK.csv) maps the new extensions to the original lessons. Original source hashes are recorded in [original-file-hashes.json](data/original-file-hashes.json).

## Station 1 — Reconcile the denominator

Both fixed fixtures contain **13 rows / 12 unique events** with one exact duplicate. Their original nominal runners complete **12/12**. The duplicate must never become a new passenger or a second successful delivery. For any completed scenario, count every unique request as either completed, lost, or unserved; do not let lost requests disappear from the denominator.

## Station 2 — Distinguish two degraded designs

The v11 one-vehicle case completes **6/12**. The v12 `OUTAGE` scenario also completes **6/12**, but it configures two resources and blocks one resource until minute 70. The matching numerator does **not** make these designs identical. A cross-version engineering change must explicitly compare assumptions, state transitions, fault rules, timing and evidence scope.

## Station 3 — Truth ledger versus operational observability

The v12 `LOSS` scenario records **8 completions and 4 injected losses** in the simulator's truth ledger. It does not establish that a real receiver can detect a message it never saw. Describe an end-to-end acknowledgment design that would make loss externally observable; provide failure and timeout tests before claiming it works.

## Station 4 — Independent mechanical invariants

For each completed event, verify `arrival ≤ received ≤ start < finish ≤ horizon` and verify that intervals on the same resource do not overlap. For an outage resource, completed intervals must not intersect the blocked window. The U2 code checks both models *independently of their own booleans*. Negative tests deliberately corrupt a ledger record and expect the audit to reject it.

## Station 5 — Repetition and statistical credibility

The preserved v12 report used **20** seeded synthetic streams and reported difference **−0.375** with approximate interval **[−0.428651, −0.321349]**. Its saved JSON and provenance are **byte-identical** to a fresh 20-replication replay. U2 separately uses **120** replications and reports difference **−0.423611** for `OUTAGE − BASE`, with approximate interval **[−0.439265, −0.407957]**. The different counts identify different experiment configurations; neither establishes field credibility. That quantifies Monte Carlo sampling precision conditional on its invented generator, not the accuracy of the physical demand model. For illustration only, a Wilson lower 95% bound on `12/12` would be approximately **0.7575** under independent Bernoulli sampling; the hand-constructed fixed fixture **does not meet that sampling assumption**.

## Station 6 — Evidence gates and review

The demonstration nominal screen passes at 100%; the fault screen fails at 50%. Both original request datasets lack accessibility-specific fields. The U2 evidence table contains stale or out-of-scope records, and four field permission flags are false. The final output is **HOLD for field deployment**. No manipulation of output scores can override absence of a qualified authorization. The `assess_claim` function demonstrates the boolean gate's operation, not a real authorization mechanism.

## Guided challenge and explained answer

**Challenge.** A team reports “we have repeated our tests exactly, the baseline completed 12/12 requests, and the simulator can see message losses. Can we release a dispatch service?”

**Worked resolution.** The team has shown reproducible **software** behavior for a small synthetic fixture. The degraded screen fails; the modeled lost messages are visible only to the simulator's truth ledger; subgroup evidence is missing; and there is no field validation or authorization. A technically defensible decision is to retain the learning prototype, document its model boundaries, plan tests on independently supported data and relevant populations, and obtain decisions from legitimate authorities before operational work. The numerical result alone cannot discharge those obligations.

## Known limitations

No software here controls real vehicles. Neither runner models roads, accessibility service categories, human operations, genuine network loss detection, operational privacy controls, or realistic correlated environmental disruptions. The new independent auditor still reads output records from the same underlying models and is not an independent physical qualification test. Hashes support change detection; they do not authenticate the author, prove model validity or grant permission. A desktop browser is not required to execute the Python lessons.
