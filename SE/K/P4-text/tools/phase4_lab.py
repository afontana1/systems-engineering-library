"""Phase 4 conceptual calculations. All values and examples are synthetic.

Standard library only; no output constitutes evidence for field operations.
"""
from __future__ import annotations
import math
import statistics
from collections import defaultdict
from datetime import datetime


def little_law_time(wip: float, throughput_per_week: float) -> float:
    """Return weeks. Assumes a stable observed boundary and compatible long-run averages."""
    if wip < 0 or throughput_per_week <= 0: raise ValueError('nonnegative WIP and positive throughput required')
    return wip / throughput_per_week


def mm1_system_time(arrival_per_week: float, service_per_week: float) -> float:
    """Expected system time in weeks for ideal M/M/1, assuming λ<μ and exponential service."""
    if arrival_per_week < 0 or service_per_week <= arrival_per_week: raise ValueError('unstable or invalid M/M/1 queue')
    return 1 / (service_per_week - arrival_per_week)


def critical_path(tasks: dict[str, tuple[float, list[str]]]) -> tuple[float, dict[str, float]]:
    """Tasks maps ID -> (duration, predecessor IDs); no resource constraints or stochastic durations."""
    results: dict[str,float] = {}; visiting=set()
    def finish(task):
        if task in results: return results[task]
        if task in visiting: raise ValueError('cycle in task graph')
        if task not in tasks: raise ValueError('missing predecessor')
        d, predecessors=tasks[task]
        if d < 0: raise ValueError('negative duration')
        visiting.add(task)
        val=d+max((finish(p) for p in predecessors),default=0.0)
        visiting.remove(task); results[task]=val
        return val
    for t in tasks:finish(t)
    return max(results.values(),default=0.0),results


def evidence_closure(edges: list[dict[str,str]], requirement: str, release_version: str) -> bool:
    """Toy closure: direct requirement -> test with approved run under exact release version.

    NOT a complete argument-based safety assurance system; all evidence must be reviewed.
    """
    return any(e.get('from_id')==requirement and e.get('edge_type')=='verified_by'
               and e.get('to_version')==release_version and e.get('approved')=='yes'
               and bool(e.get('to_id')) for e in edges)


def twin_freshness(observed_iso: str, used_iso: str, max_age_seconds: float) -> tuple[float,bool]:
    """Naive timestamps must use same timezone; offset-aware ISO recommended."""
    if max_age_seconds<0: raise ValueError('age limit must be nonnegative')
    t1=datetime.fromisoformat(observed_iso);t2=datetime.fromisoformat(used_iso)
    if (t1.tzinfo is None)!=(t2.tzinfo is None):raise ValueError('timezone mismatch')
    age=(t2-t1).total_seconds()
    if age < 0: raise ValueError('observation timestamp after decision')
    return age,age<=max_age_seconds


def independent_series_success(probabilities: list[float]) -> float:
    """Probability of all events: requires *independence*, rarely valid for common-cause failures."""
    if any(p<0 or p>1 for p in probabilities): raise ValueError('probability outside [0,1]')
    return math.prod(probabilities)


def process_summary(times: list[float]) -> dict[str,float]:
    """Nearest-rank p90. Positive completed case durations only; censoring must be analyzed separately."""
    if not times or any(t<0 or not math.isfinite(t) for t in times):raise ValueError('invalid case times')
    ordered=sorted(times)
    return {'mean':statistics.mean(ordered),'median':statistics.median(ordered),
            'p90_nearest_rank':ordered[math.ceil(0.9*len(ordered))-1], 'n':len(ordered)}


def difference_in_differences(treatment_before: float,treatment_after: float,
                              comparison_before: float,comparison_after: float) -> float:
    """Difference between changes of group means; causal interpretation requires parallel trends, etc."""
    nums=(treatment_before,treatment_after,comparison_before,comparison_after)
    if any(not math.isfinite(v) for v in nums):raise ValueError('finite group means required')
    return (treatment_after-treatment_before)-(comparison_after-comparison_before)

if __name__=='__main__':
    print('Synthetic instructional demos:')
    print('Little-law weeks',little_law_time(18,3))
    print('M/M/1 weeks',mm1_system_time(4,5))
    print('Critical path',critical_path({'detect':(8,[]),'patch':(24,['detect']),'verify':(32,['patch']),
                                               'prepare_training':(10,['detect']),'authorize':(24,['verify','prepare_training'])})[0])
    print('Twin freshness',twin_freshness('2026-10-01T10:00:00+00:00','2026-10-01T10:03:00+00:00',300))
    print('Independent mission',independent_series_success([.95,.95,.95]))
    print('Process summary',process_summary([8,9,12,13,15,18,21,22,34,66]))
    print('Difference-in-differences on illustrative means',difference_in_differences(30,20,28,25))
