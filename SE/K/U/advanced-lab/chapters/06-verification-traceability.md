# A06 — Verification, traceability and evidence provenance

**Competency:** trace each new requirement to implementation, executable checks, experimental configuration and an honest claim boundary.

## Evidence is a chain, not a score

The [v12 requirements register](../data/requirements-v12.csv) has six deliberately narrow claims. V12-R02 claims that **completed assignments do not overlap for the same modelled resource**. It does not claim the trip is drivable, that resources are safe, or that independent processes could never race. The [verification plan](../data/verification-plan.csv) names tests and scenarios for each requirement. The model checker checks whether links resolve, while the software tests investigate behavior.

Three often-confused activities should be separated:

- **Verification:** is the built artifact consistent with its specification? The interval check does this for the toy scheduler.
- **Validation:** does that specification/model meet the actual stakeholder need in its intended environment? This would require real-world evidence not present here.
- **Accreditation/acceptance:** is a qualified authority prepared to authorize a particular use? There is no such authority in this learning package.

## Provenance and reproducibility

The runner writes `scenario-results.json` (scenario records and automated checks), `scenario-summary.csv` (a compact report), and `provenance.json` (SHA-256 hashes of input and implementation files, plus hashes of the two results files). A hash detects changed file bytes when compared to a trusted prior record; it is not a guarantee that the source was valid or that the run used a trustworthy environment.

For an engineering review, provenance needs a **claim/evidence/limitation** ledger: for each requirement, identify the test, its exact configuration, the observed result, the reviewer, any failed cases and the unresolved threats to interpretation. If a reviewer changes `trip_min` after generating the outputs, the old results must not be silently reused.

## Worked trace

`V12-R03 → V12-T03 → LOSS → scenario-results.json → unobserved_message_loss records` proves that the demonstration *records* synthetic losses rather than counting them as completed requests. It does not prove that a real intake service could observe losses without external acknowledgements. If a user concludes “request loss is safely handled,” the evidence chain is overextended.

Similarly, `V12-R04 → V12-T04 → OUTAGE` checks avoidance of a specified blocked interval. Tests should additionally mutate the interval and verify boundary behavior at the start/end minute; otherwise the result may only reflect a favorable fixture.

## Practice and deliverable

**Exercise 1.** Can a requirement-to-test link by itself establish test adequacy?

<details><summary>Worked answer</summary>No. The test may assert the wrong thing, exercise only one case, or depend on a poor model. Structural traceability is necessary for review but never sufficient.</details>

**Exercise 2.** What evidence becomes stale after editing `scenarios.json`?

<details><summary>Worked answer</summary>At minimum scenario outputs, summary metrics, provenance hashes, comparisons, experiment conclusions and any review claim based on them. Regenerate and rerun tests.</details>

**Submit:** an assurance argument for V12-R01–R06 with explicit defeaters, a reviewed trace audit and one intentionally broken trace example. Related: [v11 evidence stage](../../integrated-lab/chapters/07-verification-evidence.md).
