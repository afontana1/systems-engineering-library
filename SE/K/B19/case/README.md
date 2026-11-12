# NS-ENT19.1 — Regional Mobility and Emergency Access Enterprise Transformation

**Use statement.** These files add a *new* entirely synthetic enterprise portfolio and process model to Book 19. The course describes the required enterprise case, but its original teaching material does **not** supply these particular investment costs, capacities, probabilities, authorization statuses, or case outcomes. They are constructed to teach reasoning and cannot establish real consent, affordability, reliability or operational value. The Book 18 emergency trip-slot model uses different assumptions; no calibration or quantitative continuity between the two models is claimed.

## Reproduce the model

From the repository root run:

```sh
python3 SE/K/B19/tools/step03_book19_enterprise.py
python3 scripts/check_step03_book19.py
```

The generator reads `case/controlled-inputs.json`, runs a 26-week first-in-first-out cohort workload model and a separate four-hour scenario capacity screen, enumerates dependency-valid portfolios, and overwrites `computed-evidence.json`, `portfolio-screen.csv`, `scenario-screen.csv`, `enumerated-portfolios.csv`, and `weekly-flow.csv` reproducibly. Only Python's standard library is required. Values are **not forecasts**; do not use them for dispatch, acquisitions or public funding decisions.

## Controlled case artifacts

- [Original, editable inputs](controlled-inputs.json) and [decision/authorization register](authority-and-incentives.csv).
- [Enterprise value and metric dictionary](value-measure-dictionary.csv), [three end-to-end value streams](enterprise-value-stream.csv), [capability/dependency view](capability-and-dependency.csv), and [architecture diagram](architecture.svg).
- [Full portfolio screens](portfolio-screen.csv), [all dependency-valid portfolio combinations](enumerated-portfolios.csv), [all scenario/portfolio scores](scenario-screen.csv), [weekly workload flow](weekly-flow.csv), and [machine-readable evidence](computed-evidence.json).
- [Transition roadmap](transformation-roadmap.csv), [pilot and stop rules](experiment-and-stop-rules.csv), and [decision/evidence register](decision-and-evidence.csv).

The queue separates new arrivals from opening backlog, computes time in process **for completed cases only**, and retains unresolved work explicitly. The cohort queue is deterministic; it does not include correlated arrival variation, multiple queues, severity classes, priority preemption, service failures, or person-level impacts. The numeric screen requires affordable resources, dependency-valid investments, a minimum 90% accessible and standard trip-slot fraction, a 95% 26-week coordination closure fraction, and 95% scenario-weight coverage. It **does not** model actual cross-owner authority; all authorizations and public legitimacy checks remain pending. Scenario weights sum to one but are invented, and do not represent incident frequencies or measured reliability. No alternative earns a deployment authorization.

## Interpreting the worked decision

The constructed capacity-first portfolio costs $3.15M and 8 FTE and passes the three non-flood scenarios (85% weight), below the 95% target. It closes 99.09% of coordination requests in its workforce scenario but only 91.21% in flood. The fully integrated portfolio passes all four numeric scenarios but costs $4.90M and consumes 12 FTE, exceeding the invented $3.60M and 8-FTE caps; its authority gates also remain open. Under 65 instead of 50 arrivals per week the capacity-first nominal closure falls to about 84.09%. The appropriate disposition is **HOLD** for any operational recommendation, accompanied by bounded pilots, agreement negotiation, and independent observations.

## Version and evidence limits

`architecture.dot` is editable and `architecture.svg` is generated from Graphviz, but the published site only needs the SVG. The files contain no genuine hospital or mobility operations data. A review must validate numerical assumptions, legal/policy applicability, vendor/labor agreements, equity burden, climate resilience, lifecycle cost and discounting, and the ability to measure outcomes in the real system. Evidence IDs and decision rights are scoped to this fictional lesson; they are not approvals.
