# NS-SW5.1 — Software systems engineering case

**Teaching example only.** All requirements, metrics, incidents, interfaces and records are fictional. The case is connected to Books 1–4 by the campus-mobility setting, but the NS-SW5.1 identifier is an independent software configuration and must not be treated as interchangeable with earlier baselines.

## Read the engineering records

- [Requirements](requirements.csv) — eight testable obligations, owners, and acceptance criteria.
- [Interface contracts](interfaces.csv) — timeouts, duplicate handling, explicit failure modes.
- [Architecture diagram source](architecture.dot) and [rendered diagram](architecture.svg).
- [Evidence register](evidence-register.csv) — five current synthetic passes, one SLO-risk warning, one stale pass, and one planned check.
- [Incident log](incident-log.csv) — 36 synthetic downtime minutes in a 30-day window.
- [Release decisions](release-decisions.csv) — an example of blocking a deploy despite favorable partial evidence.
- [Machine-readable model](model-baseline.json) — the shared assumptions and cross-reference keys.
- [Reproducibility checker](../tools/step03_book5_system_check.py) — command: `python3 SE/K/B5/tools/step03_book5_system_check.py` from the repository root.

## System boundary and safety responsibility

The software accepts or rejects shuttle reservations, obtains bounded-age telemetry and creates an atomic reservation/audit event. It does **not** command physical vehicle motion without a separate controller and operator-approved safety architecture. Loss of the reservation service must not be confused with safe control of a physical vehicle. Safety-acceptance decisions are not modeled here.

## Canonical synthetic calculations

For a 30-day time-based 99.9% availability objective, the allowable unavailable minutes are

\[B=(1-0.999)\times 30\times 24\times 60=43.2\text{ min}.\]

Four incident records total 36 minutes; 7.2 minutes remain. A proposed nine-minute canary disruption would exceed that remaining budget by 1.8 minutes. The release should not proceed without a new risk decision and valid recovery evidence. These are illustrative time-based metrics; a request-based service-level indicator needs its own denominator and observed request data.

For an illustrative M/M/1 dispatch server, let request arrival rate be \(\lambda=10\) per second and candidate service rate \(\mu=20\) per second. The 95th percentile of *time in this ideal queueing system* is

\[t_{0.95}=\frac{-\ln(0.05)}{\mu-\lambda}=0.29957\text{ s}.\]

Adding **assumed deterministic** 70 ms of networking, 45 ms of authorization and 55 ms of commit overhead yields 469.57 ms. This is an optimistic analytical proxy, not a measured percentile or a proof that the user-facing SWS-01 requirement is met. At the original rate \(\mu=18\), the proxy is 544.47 ms and fails the 500 ms threshold.

## Investigation tasks

1. Explain why a matching requirements/evidence link does not prove release readiness if the evidence was collected against NS-SW5.0.
2. Recompute the time budget for a 28-day measurement window. Would the 36 minutes fit? Explain why changing the window after observing incidents is methodologically suspect.
3. Propose a test that validates the p95 analytical proxy at the declared peak arrival profile, including sample size, confidence treatment and percentile estimator.
4. Explain how a database uniqueness constraint and a bounded idempotent retry policy address different failure mechanisms.
5. Prepare an evidence-based release decision, explicitly distinguishing operational risk, modeled performance, and missing recovery tests.

## References (for further validation, not substitutes for the explanations)

- [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — secure development practices; consult publication status before asserting compliance.
- [Google SRE Workbook: Error Budget Policy](https://sre.google/workbook/error-budget-policy/) — service-specific balancing of reliability and changes.
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/otel/semantic-conventions/) — consistent observability fields; the specification evolves and does not validate this exercise's synthetic traces.
