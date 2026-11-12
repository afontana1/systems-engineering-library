# T1 integrated laboratory — When apparently good evidence cannot authorize a system

*Step 04 · Core Technical Concepts · NS-T4.1 · Synthetic classroom exercise*

> **Intended use:** Learn to reconcile requests, verify numerical methods, challenge dependency assumptions, check evidence provenance, and enforce noncompensatory authorization gates. This dataset contains no observations of a real Northstar service.

## Learning objectives and controlled artifacts

The data in [t1-case.json](t1-case.json) contains 40 invented dispatch requests, a latency limit and clock guard band, six paired simulation-stream comparisons, nominal/stressed vehicle choices, a common-cause assumption, five evidence paths, and an approval register. The standard-library [evidence checker](../tools/t1_evidence.py) produces [t1-results.json](t1-results.json); it does not simulate real vehicle movements. Run it from the repository root:

```bash
python3 SE/K/T/tools/t1_evidence.py --output SE/K/T/labs/t1-results.json
python3 -m unittest discover -s SE/K/T/tools -p 'test_t1_evidence.py'
python3 scripts/check_step04_technical_t1.py
```

Preserve the fixture before a modification, change one variable or state at a time, record the changed result and its engineering interpretation, and restore the original input for the baseline check. The script rejects malformed data; a technical or authority gate failing is a *legitimate model output*, not an exception to be hidden.

## Station 1 — Define what the service claim measures

Reconcile 40 arrivals into 32 served, five rejected, and three pending. The nominal service-time count includes 32 timely completions, but the 0.8-second clock guard band leaves 26. The all-request result is \(26/40=65\%\), not \(26/32\) and not \(32/32\). The accessible subgroup yields \(6/8=75\%\). **Counterexample:** insert a duplicate request ID; the checker must reject the input rather than improve the denominator.

## Station 2 — Statistical claims require a sampling design

Separately calculate the exact one-sided 95% upper failure bound after 300 independent trials with zero failures: \(1-0.05^{1/300}\approx0.009936\). Explain why this result cannot be used for the 40 correlated service records; they are not 300 independent zero-failure trials. Also distinguish a frequentist confidence bound on a Bernoulli failure probability from a posterior credible interval.

## Station 3 — A queue benchmark is not a finite service record

For a different hypothetical M/M/1 system, \(\lambda=8\) and \(\mu=10\) per hour. Derive \(\rho=0.8\), \(W=30\) minutes, \(W_q=24\) minutes, \(L=4\), and \(L_q=3.2\). Show that using a finite request ledger to claim these stationary quantities without validating Poisson/exponential assumptions is a model-use error.

## Station 4 — Verify the numerical solution, not only the code

For \(\dot x=-0.7x\), \(x(0)=1\), compare one Euler step of one hour (0.3), four 0.25-hour steps (0.463250), and the one-hour exact solution (0.496585). A three-hour Euler step multiplies by -1.1 and is unstable. Explain why stability, positivity, physical validity, and convergence are different checks.

## Station 5 — Shared dependencies change assurance and design choices

Two conditionally independent dispatch channels with individual success 0.97 yield an ideal 0.9991 parallel success rate. With an assumed 0.035 common-cause failure probability, the joint success is 0.9641315. Screen integer vehicles \(x=1,2,3\), demanding at least 10 requests/hour and no more than 30 kWh energy in a one-hour window: two vehicles pass nominal service but fail stressed service; three violate the energy budget. **The robust feasible set is empty.** These are different metrics and cannot compensate for each other.

## Station 6 — Evaluate evidence and decision permission independently

Only two of the five evidence paths match the required revision, verified status, and intended use. Merely changing a link revision while leaving a record in draft state cannot make it actionable. The road authority permission is granted, but labor and privacy permissions are absent. Do not combine these into an average score. The program must return `deployment_screen.passes = false` even if you hypothetically raise a service score.

## Station 7 — Experimental comparison and economics

The six paired demand-stream differences (candidate minus baseline) are -5, -4, -2, -5, -3, and -2 minutes. Compute the mean -3.5 minutes and standard error approximately 0.5627 minutes, treating streams—not passenger events—as the sampling unit. For three years of year-end costs discounted at 5%, calculate the two lifecycle present costs: 1544.65 and 1499.56 cost units, and the break-even annual saving of 73.44. Explain why neither a paired mean improvement nor a lower lifecycle cost can waive a hard requirement.

## Worked answer and submission standard

A defensible submission contains the original and modified result JSON, a table of changed assumptions, reproduction commands, at least two deliberately invalid inputs (duplicate ID and malformed time or evidence records), a short verification-versus-validation distinction, a cause-specific counterargument, and a signed-off **HOLD** recommendation for real-world deployment. No synthetic result in this exercise is a tested field outcome or operational authorization.

## Cross-references

Review [statistical inference](../06-inference.md), [queueing](../07-queues.md), [dynamics](../08-dynamics.md), [reliability](../09-assurance.md), [digital provenance](../11-digital-thread.md), [experimental design](../16-experimental-design.md), [maintenance](../17-reliability-maintenance.md), [robust optimization](../18-robust-optimization.md), [simulation credibility](../19-simulation-credibility.md), and [lifecycle economics](../20-lifecycle-economics.md).
