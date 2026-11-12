## Step 04 integrated case — NS-CE4.1: structured paths are not current evidence

A digital thread is valuable because it can reveal missing, stale, or contradictory arguments. It is dangerous when a link's mere existence is treated as proof. The synthetic NS-CE4.1 ledger has five connected **claim → requirement → artifact** paths. All five exist structurally; only one is currently actionable under a narrow, stated set of checks.

### Model an evidence path as a typed assertion

An actionable path needs more than a claim identifier. Let $e$ be an evidence record and let $r_b$ be the current release revision. A simple necessary screen is

$$A(e)=I[h(e)=h_{\rm recorded}]\,I[r_e=r_b]\,I[s_e=s_{\rm required}]\,I[\mathrm{status}(e)=\mathrm{PASS}],$$

where $h$ is a SHA-256 content digest over the example's **declared payload string**, $r_e$ is evidence revision, and $s_e$ is the tested scope. Each indicator is necessary for the local screen; their conjunction is **not** an accreditation of the test method, authenticity of signatures, or independence of reviewers. Real evidence systems also require immutable artifact storage, key management, credentialed review, meaningful semantic change control, and trust boundaries.

The controlled ledger reports:

| Claim | Artifact | Recorded problem | Actionable? |
|---|---|---|---|
| CL-CAP | EV-CAP | Tested nominal scope, but storm scope required | No |
| CL-WAIT | EV-WAIT | Revision 2.0, while build is 2.1 | No |
| CL-ACCESS | EV-ACCESS | Current revision, but recorded FAIL | No |
| CL-INT | EV-INT | Interface contract evidence revision 2.0 | No |
| CL-ENT | EV-ENT | Current, matching scope, PASS status | Yes for **narrow local path screen** |

Hence structural coverage is $5/5=100\%$ but actionable local coverage is $1/5=20\%$. The fifth path is **not** a validated causal enterprise claim; it only passes the explicitly simplified metadata checks. None of the required `safety_approval`, `accessibility_consultation`, `data_governance_approval`, and `operations_authorization` flags is granted in the case JSON. These omissions are separately disqualifying and cannot be made good by adding more evidence links.

### Change impact and provenance attack examples

Suppose an analyst copies `EV-WAIT` from release 2.0 into a 2.1 readiness dashboard. The link target exists, the status remains PASS, and the recorded content digest still matches. Yet the evidence is **stale** for 2.1 until a reviewed impact assessment or new verification establishes its applicability. Conversely, if an artifact's payload changes without updating the recorded digest, a digest check detects the mutation; updating both payload and digest can still conceal an unauthorized rewrite. A digest verifies content consistency relative to a trusted baseline, not authorship or professional approval.

To run the adversarial exercise, copy the JSON, alter an evidence payload without changing `sha256`, and rerun the checker in a temporary Python process. The affected path must gain `digest_mismatch`. If instead you update the revision string alone, it must still retain any unresolved status or scope failures. A real digital thread would also distinguish evidence generated for the same model from independent bench measurement; two paths based on one unverified simulation do not create two independent proofs.

### Granular assurance and defeaters

A defensible assurance argument states a bounded claim: 'The specified dispatch interface satisfied requirement REQ-INT under the listed test environment, revision, timestamp policy, and input class.' The *warrant* links a test result to that claim, and a *defeater* identifies conditions under which the warrant fails (such as clock drift, unseen demand regimes, or a producer schema revision). The path is re-evaluated when a defeater becomes plausible. A verified model trace and a signed operational release are distinct evidence types, with distinct authorized decision makers.

**Worked exercise 1 — coverage.** A dashboard reports 100% coverage because every requirement links to an artifact. Calculate actionability. **Solution:** One of five paths passes the local metadata screen, so actionable coverage = 20%. Even 100% actionability would not override missing authorizations.

**Worked exercise 2 — repaired revision.** Change `EV-WAIT` revision from 2.0 to 2.1 without changing its payload and without new validation. Does the record become credible? **Solution:** The toy checker may mark it actionable if all local fields match; this demonstrates the *limit* of the checker. Authentic release evidence requires a legitimate revision record, justified model applicability, and independent verification—not a string edit.

**Adverse case.** Duplicate a claim row in the ledger. The model must reject ambiguity rather than silently overwrite one evidence source. The six chapters' joint example deliberately ends with HOLD; the release decision remains outside the programmatic checker.
