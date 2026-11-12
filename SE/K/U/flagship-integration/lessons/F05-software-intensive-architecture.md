### F05 extension · Stateful command contracts and replay safety

**Contract and trust boundary.** A dispatch `COMMIT` authorizes a specific request revision, while `ACK` acknowledges a previously committed request. The precondition for `ACK(r)` is $state(r)=COMMITTED$; the postcondition is $state(r)=ACKNOWLEDGED$, with preserved request ID, sequence, authenticated sender, and the current interface revision. The system should reject acknowledgements before a matching commit, malformed sequences, stale revisions and conflicting replays.

**Idempotency is not merely duplicate suppression.** NS-U4.1's event fixture includes an exact replay of event `E2`. Because both ID and contents match, it is accepted as a no-op and counted as one exact duplicate. A later replay of `E1` carries a different payload digest; accepting it as the same event could substitute a new action without a corresponding audit trail. The checker reports `conflicting_replay` instead of approving it.

**Worked trace.** The first `E1` commit advances request `R1`; `E2` then acknowledges it. Event `E3` acknowledges request `R2` before any commit, violating the state-machine invariant. The conflicting `E1` replay violates immutability. Event `E4` claims interface revision 1.0 when revision 2.0 is required. The fixture therefore records *three distinct violations and one safe exact duplicate*. A passing JSON checker illustrates a contract, not formal proof of all concurrent histories or network attacks.

**Architecture implication.** Make command identity immutable; require per-request ordering; bind messages to a configuration revision; log security-relevant rejects; and separately verify the authority of the sender. At-least-once delivery can be tolerated only if repeated commands are idempotent by *content and authorization scope*. A retry storm may still overload the service even if no command executes twice.

**Worked exercise and solution.** A replay uses the correct event ID but changes the destination address. The correct response is reject and raise a conformance/security event; treating both records as duplicates would hide a potentially unsafe reroute. Conversely, re-sending exactly the same authorized message should have no additional side effect.

**Reproduce:** [D11 behavioral contracts](../derivations/11-state-machines-contracts.md), [event checker](../flagship-integration/code/ns_u_case.py), [input trace](../flagship-integration/data/ns-u4.1-case.json).
