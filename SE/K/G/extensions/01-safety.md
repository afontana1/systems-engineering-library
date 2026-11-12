## Integrated case NS-G4.1 — Safety contract and evidence age

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. Safety claim as an executable obligation

The regional dispatch mission asks the scheduler to authorize a mobility movement only when the road authority's route status is acceptably current. Trace the **loss** (passengers enter a closed corridor) to the **hazard** (departure permitted under obsolete knowledge), then to an operational **constraint**: *Do not issue departure permission if the effective upper bound on route-evidence age exceeds 30 s or the currently authorized route revision differs from the token revision.* The owner of an approved degraded operating mode is separate from the route cache; the teaching predicate does **not** model such authorization.

The code checks one decision predicate, not the entire temporal logic requirement. For a clock bound at decision time, combine observation-to-decision delay, possible execution latency, and adverse clock skew:

\[
A_{\max}=(t_d-t_o)+\Delta_{execute}+\epsilon_{clock},
\qquad m=30\,\mathrm{s}-A_{\max}.
\]

Here \(t_o\) is the observation timestamp and \(t_d\) is the permission decision timestamp, both in seconds on the stipulated clock reference. \(\Delta_{execute}\) bounds delayed actuation and \(\epsilon_{clock}\) is a one-sided worst-case clock error—not a stochastic standard deviation. If timestamps can come from unrelated clocks, the bound needs a synchronization specification and empirical error evidence; arithmetic alone does not fix that omission.

**Worked calculation.** The baseline observation is at 100 s, decision at 126 s, maximum execution delay 5 s and clock uncertainty 3 s. Then \(A_{\max}=26+5+3=34\) s, and \(m=-4\) s: a signed baseline authorization fails even without a known road closure. In the coordinated policy the observation is refreshed to 110 s, yielding \(A_{\max}=16+5+3=24\) s, or **6 s** of nominal margin. In the compound disruption, extra clock uncertainty of 5 s gives 29 s, leaving just 1 s; that case still fails other engineering constraints. A route-interface revision drift from R2 to R3 defeats the nominal permission even though its age remains 24 s.

### G2. Why this is an incomplete safety demonstration

A finite trace containing a departure with \(A_{\max}>30\) is a counterexample to this constrained property. But a *passing* predicate cannot establish the invariance of the property over every controller state, message ordering, network partition, and operator action. The case assumes valid signatures, bounded skew, and an authoritative route-source revision; cryptographic verification and certificate revocation are not implemented. An authorization may also be harmful when a fail-closed response prevents accessible evacuation. That competing loss requires a separately reviewed degraded-mode design, not a silent exception coded into the predicate.

Allocate evidence by claim: test the clock and scheduling bound, independently check revision provenance, exercise cancellation/delay race conditions, observe operator override behavior, and record signed institutional permissions. For each evidence item store baseline revision, intended use, evaluator, test date, and unresolved hazards. A passing latency regression is **necessary evidence within scope**, not a substitute for a safety case.

### G3. Sensitivity and counterexample

At the coordinated policy's 24-second nominal bound, an additional 7-second skew makes \(A_{\max}=31\) s and changes a pass into a fail. Under the stipulated 30-second limit, the maximum additional one-sided skew is 6 seconds. Do not describe a stochastic confidence bound as a hard worst-case bound without deriving the tail risk. In a real system, build a timed state model for issued, revoked, received and executed permissions and check the cancellation race rather than only testing isolated messages.

### Worked exercise with explained solution

**Problem.** Keep the coordinated policy's 16-second observation-to-decision age and 3-second skew, but increase execution latency from 5 to 12 seconds. Determine the permission decision, the margin, and one change that restores the screen.

**Solution.** \(A_{\max}=16+12+3=31\) s, hence margin \(-1\) s and the simplified screen fails. Reducing the execution bound by at least 1 second would meet the inclusive limit if all other assumptions hold; refreshing the authoritative observation later is another option, but would need a new measured delay budget and an interface-specific validity mechanism. Neither change by itself authorizes deployment.

**Review question.** Which independent agency grants road-closure authority, and where is its permission verified? The JSON records `road_authority: false`. Even a numerical pass must therefore remain **HOLD**.
