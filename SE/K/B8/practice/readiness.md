# Workshop 6 · A favorable latency metric can conceal a failed service

*Companion to Book VIII, Chapter 10 · Evidence sufficiency and readiness decisions*

## Separate the numerator from the population

A test report claims Northstar meets its 90th-percentile passenger-wait limit: the completed-trip wait p90 is 18 minutes. Management wants to authorize operations. A detailed audit of the 12 synthetic requests finds that **10 were served and 2 were dropped**. An apparent pass on latency cannot substitute for evidence about availability and unserved requests. A metric that silently excludes failures can reward a system for refusing difficult work.

A defensible test plan names each metric's **population, inclusion rule, statistic, limit and decision authority** before execution. The sample dataset contains ten waits: 5, 7, 10, 12, 13, 14, 15, 16, 18, 20 minutes, plus two dropped requests. The nearest-rank empirical 90th percentile uses the ordered observation at rank \(\lceil 0.9n\rceil\). With \(n=10\), it is the ninth observation, **18 minutes**. Other quantile conventions can yield different values, so the method belongs in the protocol.

The completed-service fraction is \(10/12\approx0.8333\), below the fictional service-coverage requirement of 0.95. Even if a latency test passes at a limit of 18 minutes, the overall gate **fails**. A separate requirement of *zero lost safety-critical messages* would also need its own evidence and authority.

## Construct a claim–argument–evidence table

| Claim | Measurement | Gate | Result |
|---|---|---|---|
| Completed-trip wait | Nearest-rank p90, completed requests only | At most 18 minutes | Pass on this dataset |
| Request completion | Served divided by all eligible requests | At least 0.95 | Fail: 0.833 |
| Fault-handling behavior | Executed fault scenarios and recorded state | All specified fault constraints satisfied | Not established by this dataset |

The third row is neither automatically passing nor failing: the dataset does not evaluate it. This is why an integrated review distinguishes **pass**, **fail**, **not tested**, **inapplicable**, and **invalid evidence**. Treating all nonpasses as “open tests” destroys diagnostic information and distorts readiness.

## Conditional readiness and uncertainty

The 12-request synthetic fixture is not a random sample of regional demand, so it does not automatically yield a population-level confidence bound. Even if requests were independent random opportunities, a point estimate of 10/12 would carry large sampling uncertainty. The correct recommendation is a *bounded no-go pending defect remediation and stronger representative evidence*, not a blanket declaration that the system will always fail or always succeed.

A review board should also demand traceable test procedures, stable configuration identifiers, calibration or measurement records where relevant, deviation logs, known sensor limitations, and explicit operational constraints. Decisions need a stated authority, not merely an engineering vote.

## Worked problems

**Problem 1.** Using the stated nearest-rank rule, calculate the p90 for the ten served requests.

<details><summary>Worked solution 1</summary>

Rank \(\lceil0.9\times10\rceil=9\); the ninth ordered wait is 18 minutes. Declare the quantile method; a software package may default to interpolation instead.
</details>

**Problem 2.** A team removes the two dropped requests and reports 100% completion. What is the denominator error?

<details><summary>Worked solution 2</summary>

The completion denominator must include all **eligible requests**, not only successfully completed ones. Otherwise the definition excludes precisely the service failures it is supposed to measure.
</details>

**Problem 3.** Suppose one more request is served but at a 30-minute wait. Does that automatically improve the readiness case?

<details><summary>Worked solution 3</summary>

Completion rises to 11/12 (91.7%) but remains below 95%; the latency p90 may worsen. You must calculate each gate separately and avoid using a composite score to conceal a failed mandatory constraint.
</details>

**Problem 4.** What would a defensible review recommendation say?

<details><summary>Worked solution 4</summary>

“The fixed-case completed-trip p90 met the specified threshold under the declared quantile convention, but completion failed 10/12 versus the 95% gate. This evidence does not establish operational readiness. Correct the service loss, repeat representative tests on the controlled configuration, and close the other required acceptance claims.”
</details>

## Transfer to engineering work

Download the request outcome CSV and compute metrics independently. Construct an evidence ledger with method, denominator, configuration, result and authority. Draft a one-page readiness recommendation, including a concise dissent argument. This exercise complements the original Book VIII evidence-sufficiency chapter rather than replacing the full test planning assignment.
