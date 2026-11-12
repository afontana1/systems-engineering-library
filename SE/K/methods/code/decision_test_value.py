#!/usr/bin/env python3
"""Reproducible educational Bayes decision / value-of-information model (cost in k$)."""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Inputs:
    prior_fault: float = 0.20
    sensitivity: float = 0.90
    specificity: float = 0.95
    ship_fault_cost: float = 100.0
    redesign_cost: float = 15.0
    test_cost: float = 5.0


def calculate(x: Inputs = Inputs()) -> dict:
    for name in ("prior_fault", "sensitivity", "specificity"):
        if not 0 <= getattr(x, name) <= 1:
            raise ValueError(f"{name} must be a probability")
    if min(x.ship_fault_cost, x.redesign_cost, x.test_cost) < 0:
        raise ValueError("costs must not be negative")
    p_pos_and_fault = x.prior_fault * x.sensitivity
    p_neg_and_fault = x.prior_fault * (1 - x.sensitivity)
    p_pos_and_sound = (1 - x.prior_fault) * (1 - x.specificity)
    p_neg_and_sound = (1 - x.prior_fault) * x.specificity
    p_pos = p_pos_and_fault + p_pos_and_sound
    p_neg = p_neg_and_fault + p_neg_and_sound
    assert abs(p_pos + p_neg - 1) < 1e-10
    prior_ship = x.prior_fault * x.ship_fault_cost
    baseline = min(prior_ship, x.redesign_cost)
    # Compute unconditional contribution by joint events; valid even if event probability is zero.
    positive_ship_joint = p_pos_and_fault * x.ship_fault_cost
    positive_redesign_joint = p_pos * x.redesign_cost
    negative_ship_joint = p_neg_and_fault * x.ship_fault_cost
    negative_redesign_joint = p_neg * x.redesign_cost
    positive_decision = "ship" if positive_ship_joint <= positive_redesign_joint else "redesign"
    negative_decision = "ship" if negative_ship_joint <= negative_redesign_joint else "redesign"
    policy_loss = min(positive_ship_joint, positive_redesign_joint) + min(negative_ship_joint, negative_redesign_joint)
    perfect_loss = x.prior_fault * min(x.ship_fault_cost, x.redesign_cost) + (1 - x.prior_fault) * min(0.0, x.redesign_cost)
    evpi = baseline - perfect_loss
    evsi = baseline - policy_loss
    assert -1e-8 <= evsi <= evpi + 1e-8, "EVSI must be between zero and EVPI"
    return {
        "no_test_decision": "ship" if prior_ship <= x.redesign_cost else "redesign",
        "no_test_optimal_loss_kusd": baseline,
        "probability_positive": p_pos,
        "posterior_fault_positive": p_pos_and_fault / p_pos if p_pos else None,
        "posterior_fault_negative": p_neg_and_fault / p_neg if p_neg else None,
        "decision_after_positive": positive_decision,
        "decision_after_negative": negative_decision,
        "expected_loss_after_test_before_fee_kusd": policy_loss,
        "evpi_kusd": evpi,
        "evsi_kusd": evsi,
        "net_improvement_kusd": evsi - x.test_cost,
        "peak_wait_violation_H": 0.30 * 0.60 + 0.70 * 0.08,
        "peak_wait_violation_M": 0.30 * 0.12 + 0.70 * 0.02,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    for key in Inputs.__dataclass_fields__:
        p.add_argument(f"--{key.replace('_', '-')}", type=float, default=getattr(Inputs(), key))
    x = Inputs(**vars(p.parse_args()))
    for key, value in calculate(x).items():
        print(f"{key}: {value}")
    print("Illustrative inputs only. Validate action feasibility, costs and likelihoods.")


if __name__ == "__main__":
    main()
