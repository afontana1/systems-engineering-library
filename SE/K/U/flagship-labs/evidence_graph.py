"""Small auditable assurance graph lab; NOT a safety-case certification system."""
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class Evidence:
    result_id: str
    requirement_id: str
    configuration: str
    status: str  # accepted, rejected, pending
    observable: str

@dataclass(frozen=True)
class Requirement:
    requirement_id: str
    expected_observable: str
    critical: bool = False


def audit(requirements: Iterable[Requirement], evidence: Iterable[Evidence], configuration: str):
    """Evaluate recorded evidence alignment. A matching label is not proof of semantic validity."""
    rows = []
    evidence = list(evidence)
    for req in requirements:
        matching = [e for e in evidence if e.requirement_id == req.requirement_id]
        accepted = [e for e in matching if e.status == 'accepted'
                    and e.configuration == configuration and e.observable == req.expected_observable]
        stale = [e.result_id for e in matching if e.configuration != configuration]
        mismatched = [e.result_id for e in matching if e.observable != req.expected_observable]
        rows.append({'requirement': req.requirement_id, 'critical': req.critical,
                     'has_applicable_accepted_evidence': bool(accepted),
                     'applicable_ids': [e.result_id for e in accepted],
                     'stale_ids': stale, 'wrong_observable_ids': mismatched})
    return rows


def structural_coverage(rows):
    if not rows:
        return None  # no zero/zero = 100% illusion
    return sum(r['has_applicable_accepted_evidence'] for r in rows) / len(rows)


if __name__ == '__main__':
    reqs = [Requirement('R-PICKUP', 'curb_arrival_seconds', True),
            Requirement('R-API', 'api_latency_ms')]
    results = [Evidence('E-101', 'R-PICKUP', 'build-4.2', 'accepted', 'api_latency_ms'),
               Evidence('E-102', 'R-API', 'build-4.2', 'accepted', 'api_latency_ms')]
    print(audit(reqs, results, 'build-4.2'))
    print('Coverage:', structural_coverage(audit(reqs, results, 'build-4.2')))
