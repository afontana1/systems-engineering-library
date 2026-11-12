#!/usr/bin/env python3
"""Teaching calculator: exact one-sided binomial failure bound from a latency CSV.

Assumes independent, identically distributed binary trials and a predeclared
population. Does not declare operational verification or infer subgroup coverage.
"""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def upper_failure_bound(failures: int, n: int, confidence: float = 0.95) -> float:
    """One-sided Clopper-Pearson binomial upper confidence limit."""
    if n < 1 or not 0 <= failures <= n or not 0 < confidence < 1:
        raise ValueError("Require n>=1, 0<=failures<=n, and 0<confidence<1")
    alpha = 1.0 - confidence
    if failures == n:
        return 1.0
    if failures == 0:
        return 1.0 - alpha ** (1.0 / n)

    def binomial_cdf(k: int, p: float) -> float:
        if p <= 0:
            return 1.0
        if p >= 1:
            return 0.0
        logs = [
            math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
            + j * math.log(p) + (n - j) * math.log1p(-p)
            for j in range(k + 1)
        ]
        m = max(logs)
        return math.exp(m) * sum(math.exp(v - m) for v in logs)

    low, high = 0.0, 1.0
    for _ in range(80):
        mid = (low + high) / 2.0
        if binomial_cdf(failures, mid) > alpha:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def needed_zero_failure_sample(target_success: float = 0.99, confidence: float = 0.95) -> int:
    if not 0 < target_success < 1 or not 0 < confidence < 1:
        raise ValueError("probabilities must lie strictly between 0 and 1")
    return math.ceil(math.log1p(-confidence) / math.log(target_success))


def analyze_csv(path: Path, threshold_s: float = 4.0, confidence: float = 0.95,
                target_success: float = 0.99) -> dict:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        required = {"request_id", "duration_s", "scenario", "build"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"CSV must include {sorted(required)}")
        rows = list(reader)
    if not rows:
        raise ValueError("CSV must contain at least one observation")
    durations = []
    for row in rows:
        duration = float(row["duration_s"])
        if not math.isfinite(duration) or duration < 0:
            raise ValueError("durations must be finite and nonnegative")
        durations.append(duration)
    failures = sum(t > threshold_s for t in durations)
    bound = upper_failure_bound(failures, len(rows), confidence)
    return {
        "n": len(rows), "failures": failures, "upper_failure_probability": bound,
        "target_success": target_success, "confidence": confidence,
        "sampling_sufficient": bound <= 1.0 - target_success,
        "scenarios": sorted({r["scenario"] for r in rows}),
        "builds": sorted({r["build"] for r in rows}),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="CSV: request_id,duration_s,scenario,build")
    parser.add_argument("--threshold-s", type=float, default=4.0)
    parser.add_argument("--confidence", type=float, default=0.95)
    parser.add_argument("--target-success", type=float, default=0.99)
    args = parser.parse_args()
    if args.threshold_s < 0 or not 0 < args.target_success < 1:
        parser.error("threshold must be nonnegative; target must be 0..1")
    results = analyze_csv(args.csv, args.threshold_s, args.confidence, args.target_success)
    for key, value in results.items():
        print(f"{key}: {value}")
    print("Zero-failure minimum n:", needed_zero_failure_sample(args.target_success, args.confidence))
    print("CAUTION: statistical screening is not configuration acceptance or verification.")
    print("Check sampling assumptions, exclusions, measurement uncertainty and strata.")


if __name__ == "__main__":
    main()
