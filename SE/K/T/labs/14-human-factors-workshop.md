# Practice Lab T14 — Human factors: design for decisions made under pressure

## Scenario
The Northstar operations center receives both high-priority access alerts and routine telemetry notifications. During an evacuation, some route changes are acknowledged but not yet applied.

## Investigation
1. Draft a five-state command lifecycle: submitted, accepted, pending application, applied, and independently confirmed. Add a failure transition from each active state.
2. Draw two operator screens: one that reports only connection state, and a second that reports evidence freshness, confidence, and required action. Explain why the second supports better decisions.
3. Use [alarm-workload.csv](alarm-workload.csv) to classify routine and critical alarms. Compute total volume and list which conditions need escalation.
4. Design a 12-scenario usability experiment. Specify the error severity classification before running it, and include two cases with simultaneous alerts.
5. Explain why a queue formula can reveal workload risk but cannot serve as a validated model of human cognition.

## Deliverable
Submit a control-authority matrix, an alarm taxonomy, and a test plan with observable acceptance criteria. Show how an operator recovers from a command that was acknowledged but never applied.

[Return to the textbook chapter](../14-human-factors.md)
