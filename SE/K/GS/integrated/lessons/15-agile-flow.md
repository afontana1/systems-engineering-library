## NS-GS4.1 extension — boundary choice can reverse a flow improvement

Agile flow measurements are often reported at the team boundary. The release decision, however, occurs only after evidence has been accepted by independent reviewers. The controlled case provides a fixed admitted work-in-process (WIP) of 18 changes, a nominal engineering completion rate of 0.75 changes/day, and an accepted-evidence rate of 0.60 changes/day.

### Use Little's law with an explicitly stable boundary

For a stationary, flow-conserving system with consistent counting, \(L=\lambda W\). A naive engineering-only estimate is \(W_{eng}=18/0.75=24\) days. For the same 18 admitted changes and an evidence-backed throughput of 0.60/day, \(W_{release}=18/0.60=30\) days. The apparent six-day difference comes from which **completion event** defines throughput. These are steady-state illustrative calculations, not simulation forecasts for a finite start-up period.

The acceptance ratio is \(0.60/0.75=0.80\). A leader can raise engineering starts or sprint closures without increasing accepted releases if the assurance stage is the bottleneck. A queue that is growing is not in stationary Little's-law equilibrium; measuring its current WIP divided by yesterday's throughput can mislead. Distinguish admitted WIP, unadmitted demand, delivered items awaiting approval, and rejected changes.

### Operating policy and falsifying case

An improvement policy should define explicit WIP limits, review service rates, evidence aging rules and rework routes. Prioritizing accessible emergency changes may shorten time for that population but increase unaccepted or aged work elsewhere. Consequently the throughput model must be connected to [group outcomes](20-critical-interventions.html), not interpreted as universal welfare. Evidence closure should be a release gate; a favorable internal cycle-time chart is a leading indicator rather than proof of safety.

### Worked exercise and explained solution

**Problem.** Holding admitted WIP at 18, how fast must accepted release flow become to reach 20 days average release lead time?

**Solution.** By \(\lambda=L/W\), required accepted throughput is \(18/20=0.90\) changes/day, 50% above the current 0.60. This assumes stationarity and the same admitted boundary; it does not establish that reviewers can sustainably achieve the rate. Derive a capacity and evidence plan in the [integrated lab](../integrated/labs/INTEGRATED-CASE.html).

**Canonical overlap.** The [queues-and-dynamics depth notebook](../../U/depth-notebooks/03-queues-and-dynamics.ipynb) treats queue models more generally; here the new issue is engineering versus **accepted** closure.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
