# Hypothetical Lab 4 — The Requirements Clinic

**Course link:** EN.645.662 Week 4 · **Book:** [Chapter 4](../chapters/04-requirements.md) · **Time:** 100–130 minutes · **Type:** requirements-quality audit and evidence planning.

## Situation

An inexperienced requirements team has produced the following statements:

1. `R-01`: “The shuttle shall be safe, secure, and convenient.”
2. `R-02`: “The dispatcher shall always respond instantly.”
3. `R-03`: “The system shall use database Brand Z.”
4. `R-04`: “The application shall provide updates quickly.”
5. `R-05`: “The vehicle shall send its status every two seconds and stop safely on network loss.”
6. `R-06`: “The service shall support accessible boarding.”

No source needs, operating-domain conditions, or verification methods are provided. Your task is *not* to turn these six lines into official requirements by adding arbitrary numbers.

## Your work

1. Tag each statement with quality defects: ambiguity, compound obligation, unverifiable claim, unjustified design prescription, missing operating condition, missing source, or uncertain authority.
2. Rewrite at least four as **candidate** requirements. Explicitly mark any invented conditions or thresholds as placeholders requiring stakeholder agreement or analysis.
3. Define an acceptance observation and verification method for each candidate. Include the configuration, offered input, measured outcome, and failure treatment.
4. Link every candidate to a need or document that the upstream source is still missing. Distinguish a missing upstream justification from a missing test method.
5. Run `tools/trace_audit.py` on `data/requirements-clinic.csv` and explain why passing a structural audit would *not* demonstrate semantic correctness.
6. Evaluate this fictional evidence: 992 of 1,000 independent eligible status events meet an eight-second threshold. Calculate the observed fraction and use the script's one-sided Wilson lower bound. Explain the difference between a sample pass rule and a high-confidence long-run claim.

## Output

`LAB04_RequirementsRepair.md`, `LAB04_TraceMatrix.csv`, and an annotated one-page verification plan. The original Week 4 guide requires a much larger baseline and must be completed separately.

<details><summary>Worked critique and reference answer</summary>

`R-01` combines subjective qualities; decompose after risk and stakeholder analysis. `R-02` uses an absolute without a measurable time. `R-03` is a possible justified constraint only if the design authority can establish its source. `R-05` combines reporting and degraded behavior; separate them because their methods and pass/fail outcomes differ. `R-06` needs a detailed boarding scenario and compatible envelope. An acceptable illustrative rewrite is: “For an accepted request under test profile DP-01, the dispatch service shall emit an assigned/rejected/degraded event within eight seconds for at least 99% of eligible requests,” **provided** the event semantics, profile, threshold rationale, and statistical acceptance policy are specified elsewhere. In the fictional dataset the observed fraction is 99.2%; a one-sided 95% Wilson lower bound is approximately 98.586%, which does not establish a population success probability of at least 99% at that stated confidence. Structural trace coverage cannot detect a test that measures the wrong variable.

</details>

## Transfer

Go back to the original Week 4 requirement-quality rubric. Use the lab as a rehearsal for the full requirements and verification baseline, not a replacement for its broader scope or independent review.


## Extended worked problems and lab

Study the [worked problem workshop on evidence applicability and requirements](../practice/trace.md), then complete the [extended laboratory](../practice/lab-trace.md). The exercises are separate from the original assessed coursework.
