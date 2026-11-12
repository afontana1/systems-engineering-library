### D11 extension · Identity, ordering and revision as separate invariants

A minimal per-request protocol has states $NEW\to COMMITTED\to ACKNOWLEDGED$. An `ACK` must reference an already committed request; immutable event identifiers must not be replayed with changed payloads; and message revision must match the approved contract. In NS-U4.1, `E2` is an exact duplicate, counted once; `E3` acknowledges `R2` before commit; a later `E1` replay changes its digest; `E4` uses obsolete revision 1.0. The three latter conditions are violations independent of throughput. A Python state-machine checker samples declared properties but does not prove correctness under arbitrary concurrency.

**Exercise and solution.** A new revision-2.0 `COMMIT` for `R2` arriving *after* its premature `ACK` cannot retroactively make the earlier history conforming. Reject and review the exception rather than rewriting the order. [Event trace](../flagship-integration/data/ns-u4.1-case.json).
