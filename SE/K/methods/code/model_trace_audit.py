#!/usr/bin/env python3
"""Notation-independent MBSE example: check typed links and baseline-specific evidence.

This intentionally does NOT establish physical/operational compliance or SysML conformance.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_RELATIONS = {
    "derivesFrom": ("requirement", "need"),
    "allocatedTo": ("requirement", "element"),
    "verifies": ("test", "requirement"),
    "resultOf": ("evidence", "test"),
    "supports": ("evidence", "requirement"),
}


def audit(data: dict) -> dict:
    baseline = data["baseline"]
    nodes = data["nodes"]
    edges = data["edges"]
    by_id = {node["id"]: node for node in nodes}
    errors = []
    if len(by_id) != len(nodes):
        errors.append("duplicate node IDs")
    for edge in edges:
        relationship = edge["relation"]
        src, dst = edge["from"], edge["to"]
        if relationship not in ALLOWED_RELATIONS:
            errors.append(f"Unknown relationship: {relationship}")
            continue
        if src not in by_id or dst not in by_id:
            errors.append(f"Broken reference: {src} {relationship} {dst}")
            continue
        expected = ALLOWED_RELATIONS[relationship]
        actual = (by_id[src]["type"], by_id[dst]["type"])
        if actual != expected:
            errors.append(f"Invalid type for {src} {relationship} {dst}: {actual}")
    results = {}
    for requirement in (v for v in nodes if v["type"] == "requirement" and v.get("in_scope", True)):
        rid = requirement["id"]
        verified_tests = {e["from"] for e in edges if e["relation"] == "verifies" and e["to"] == rid}
        related_evidence = [e for e in nodes if e["type"] == "evidence" and
                            e.get("test_id") in verified_tests and
                            any(link["relation"] == "resultOf" and link["from"] == e["id"] and
                                link["to"] == e["test_id"] for link in edges) and
                            any(link["relation"] == "supports" and link["from"] == e["id"] and
                                link["to"] == rid for link in edges)]
        valid = [e for e in related_evidence if e.get("accepted") is True and e.get("passed") is True and
                 e.get("build") == baseline and e.get("scenario") in requirement.get("scenarios", [])]
        if valid:
            status = "COVERED"
        elif related_evidence and any(e.get("accepted") and e.get("passed") and e.get("build") != baseline for e in related_evidence):
            status = "STALE"
        else:
            status = "MISSING"
        results[rid] = status
    return {"baseline": baseline, "status": results, "schema_errors": errors}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()
    result = audit(json.loads(args.json_file.read_text(encoding="utf-8")))
    print(f"baseline: {result['baseline']}")
    for rid, status in result["status"].items():
        print(f"{rid}: {status}")
    for error in result["schema_errors"]:
        print(f"SCHEMA ERROR: {error}")
    print("No result here is a system-safety or physical verification certification.")
    if result["schema_errors"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
