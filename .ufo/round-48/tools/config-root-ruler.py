#!/usr/bin/env python3
"""Parent-owned invocation only: real independent CLI on a literal frozen matrix.

This is a ruler, not the candidate implementation. It never imports lane code,
reads default host substrates, executes opencode, changes VCS, or cleans scratch.
Exit 0: all target cases and controls meet the frozen contract; 1: measured
contract failure; 2: custody/setup/CLI failure (not a behavioral verdict).
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or not value or any(p in (".", "..") for p in value.split("/")):
        raise ValueError("non-owned relative input path")
    return path


def files_digest(root: Path) -> dict[str, str]:
    return {str(p.relative_to(root)): digest(p.read_bytes())
            for p in sorted(root.rglob("*")) if p.is_file()}


def skill_text(name: str, description: str) -> str:
    return f"---\nname: {name}\ndescription: {description}\n---\n\n# {name}\n"


def materialize(root: Path, case: dict, inputs: dict) -> dict[str, Path]:
    home = root / "home"
    config = home / ".config/opencode"
    agents = home / ".agents/skills"
    carrier = root / "carrier"
    for directory in (config, agents, carrier, root / "tmp",
                      home / ".local/share", home / ".cache"):
        directory.mkdir(parents=True, exist_ok=True)
    template = inputs["template_utf8"].encode("utf-8")
    omp = root / "omp.synthetic"
    omp.write_bytes(b"\x7fELF" + b"\0" * 16 + template + b"\0" * 8)
    db = root / "skill-descriptions.db"
    with sqlite3.connect(db) as connection:
        connection.execute("CREATE TABLE skill_descriptions (key TEXT PRIMARY KEY, description TEXT NOT NULL)")
        for name, description in inputs["agents"].items():
            directory = agents / name
            directory.mkdir()
            (directory / "SKILL.md").write_text(skill_text(name, description), encoding="utf-8")
            key = digest(template + b"\0" + name.encode() + b"\0" + description.encode())
            connection.execute("INSERT INTO skill_descriptions VALUES (?, ?)",
                               (key, f"Use {name} in one line."))
    (config / "opencode.json").write_text(json.dumps(inputs["config_json"]) + "\n", encoding="utf-8")
    for name in case["config_files"]:
        path = config / relative(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(skill_text(path.parent.name, "Configured skill.") if path.name == "SKILL.md"
                        else "Not a skill definition.\n", encoding="utf-8")
    for entry in case["extra_inputs"]:
        if entry.startswith("directory:"):
            name = entry.removeprefix("directory:")
            path = (config / relative(name.removeprefix("config/"))
                    if name.startswith("config/") else root / relative(name))
            path.mkdir(parents=True, exist_ok=True)
        else:
            path = root / relative(entry)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(skill_text(path.parent.name, "Logged skill."), encoding="utf-8")
    log = root / "oc.log"
    sources = []
    for entry in case["log_sources"]:
        path = (config / relative(entry.removeprefix("config/"))
                if entry.startswith("config/") else root / relative(entry))
        sources.append(f'sources="[directory:{path}]"\n')
    log.write_text("".join(sources), encoding="utf-8")
    return {"home": home, "config": config, "agents": agents,
            "carrier": carrier, "omp": omp, "db": db, "log": log}


def unique_members(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON member: " + key)
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError("non-finite JSON constant: " + value)


def coherent_channels(text: str) -> tuple[dict, dict]:
    document = json.loads(text, object_pairs_hook=unique_members,
                          parse_constant=reject_constant)
    known = {"results", "checks", "rows", "landed", "unlanded",
             "scoped_out", "scoped_out_probes", "alternatives"}
    if not isinstance(document, dict) or set(document) != known:
        raise ValueError("missing or unknown published consumer channel")
    values = document["checks"]
    if not isinstance(values, dict) or any(not isinstance(key, str) for key in values):
        raise ValueError("checks must be the published flat id/value map")
    channels = {}
    for name in ("results", "rows"):
        rows = document[name]
        if not isinstance(rows, list):
            raise ValueError(name + " must be a record list")
        channel_values = {}
        channel_statuses = {}
        allowed = ({"check", "re_derived", "value", "status", "probe"}
                   if name == "results" else {"check", "value", "status", "evidence", "probe"})
        required = {"check", "value", "status"} | ({"re_derived"} if name == "results" else set())
        for row in rows:
            if not isinstance(row, dict) or set(row) - allowed or required - set(row):
                raise ValueError(name + " has a missing or unknown record field")
            key = row["check"]
            if not isinstance(key, str) or key in channel_values:
                raise ValueError(name + " has a non-string or duplicate check id")
            if not isinstance(row["status"], str):
                raise ValueError(name + " has a non-string status")
            value = json.dumps(row["value"], sort_keys=True)
            if name == "results" and value != json.dumps(row["re_derived"], sort_keys=True):
                raise ValueError(name + " value/re_derived type or value split: " + key)
            channel_values[key] = value
            channel_statuses[key] = row["status"]
        if set(channel_values) != set(values):
            raise ValueError(name + " check-id membership split")
        for key, value in values.items():
            if json.dumps(value, sort_keys=True) != channel_values[key]:
                raise ValueError(name + "/checks type or value split: " + key)
        channels[name] = channel_statuses
    if channels["results"] != channels["rows"]:
        raise ValueError("results/rows status split")
    return values, channels["results"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--consumer-sha256", required=True)
    parser.add_argument("--oracle", type=Path, required=True)
    parser.add_argument("--oracle-sha256", required=True)
    parser.add_argument("--scratch", type=Path, required=True)
    parser.add_argument("--baseline-receipt", type=Path)
    parser.add_argument("--baseline-sha256")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        raise ValueError("revision must be the actual full immutable Git commit")
    oracle_bytes = args.oracle.read_bytes()
    if digest(oracle_bytes) != args.oracle_sha256:
        raise ValueError("oracle_sha256 mismatch")
    oracle = json.loads(oracle_bytes)
    if oracle["schema"] != "kotoba-configured-root-oracle-v1":
        raise ValueError("unexpected oracle schema")
    source_command = ["git", "-C", str(args.repo.resolve()), "show",
                      args.revision + ":" + oracle["consumer"]]
    source_run = subprocess.run(source_command, capture_output=True, check=True)
    source_bytes = source_run.stdout
    if digest(source_bytes) != args.consumer_sha256:
        raise ValueError("consumer_sha256 mismatch")
    baseline = None
    if args.baseline_receipt:
        raw = args.baseline_receipt.read_bytes()
        if not args.baseline_sha256 or digest(raw) != args.baseline_sha256:
            raise ValueError("baseline receipt hash mismatch")
        baseline = json.loads(raw)
        if (baseline["revision"] != oracle["base_revision"] or
                baseline["oracle_sha256"] != args.oracle_sha256):
            raise ValueError("baseline receipt revision/oracle mismatch")
    elif args.baseline_sha256:
        raise ValueError("baseline hash without baseline receipt")
    if args.revision != oracle["base_revision"] and args.baseline_receipt is None:
        raise ValueError("non-BASE revision requires the committed before receipt")
    scratch = args.scratch.resolve()
    if not str(scratch).startswith("/fast/scratch/"):
        raise ValueError("scratch must be one new parent-owned /fast/scratch child")
    scratch.mkdir(parents=True, exist_ok=False)
    consumer = scratch / "consumer.py"
    consumer.write_bytes(source_bytes)
    outcomes = []
    failed = []
    mismatches = []
    errors = []
    target = oracle["target_check"]
    baseline_cases = {c["id"]: c for c in baseline["cases"]} if baseline else {}
    control_values = None
    control_statuses = None
    current = None
    remaining = [case["id"] for case in oracle["cases"]]
    try:
        for case in oracle["cases"]:
            remaining.remove(case["id"])
            current = {"id": case["id"], "state": "unsettled", "process_exit_observed": False}
            root = scratch / case["id"]
            root.mkdir()
            paths = materialize(root, case, oracle["inputs"])
            before = files_digest(root)
            argv = [sys.executable, "-B", str(consumer), "--json",
                    "--omp-binary", str(paths["omp"]),
                    "--agents-root", str(paths["agents"]),
                    "--skill-db", str(paths["db"]),
                    "--oc-log", str(paths["log"]),
                    "--oc-config", str(paths["config"]),
                    "--catalogue-carrier", str(paths["carrier"])]
            environment = {"PATH": "/usr/bin:/bin", "HOME": str(paths["home"]),
                           "XDG_CONFIG_HOME": str(paths["home"] / ".config"),
                           "XDG_DATA_HOME": str(paths["home"] / ".local/share"),
                           "XDG_CACHE_HOME": str(paths["home"] / ".cache"),
                           "TMPDIR": str(root / "tmp"), "LC_ALL": "C.UTF-8",
                           "PYTHONDONTWRITEBYTECODE": "1"}
            current.update({"argv": argv, "cwd": str(root), "environment": environment,
                            "inputs_before": before,
                            "expected_target_count": case["expected_target_count"],
                            "predicted_base_count": case["expected_base_count"]})
            run = subprocess.run(argv, cwd=root, env=environment, capture_output=True, timeout=30)
            (root / "stdout.json").write_bytes(run.stdout)
            (root / "stderr.txt").write_bytes(run.stderr)
            after = files_digest(root)
            after.pop("stdout.json", None)
            after.pop("stderr.txt", None)
            record = current
            record.update({"exit": run.returncode, "process_exit_observed": True,
                           "inputs_after": after, "stdout_sha256": digest(run.stdout),
                           "stderr_sha256": digest(run.stderr), "streams_complete": True})
            if run.returncode != oracle["expected_cli_exit_every_case"] or before != after:
                errors.append(case["id"] + ": CLI/input custody")
                record.update({"error": "CLI exit or synthetic input mutation", "state": "unevaluable"})
                outcomes.append(record)
                current = None
                continue
            try:
                values, statuses = coherent_channels(run.stdout.decode("utf-8"))
            except (ValueError, TypeError, KeyError) as error:
                errors.append(case["id"] + ": consumer channels: " + str(error))
                record.update({"error": "unevaluable consumer channels: " + str(error),
                               "state": "unevaluable"})
                outcomes.append(record)
                current = None
                continue
            record.update({"checks": values, "statuses": statuses})
            if target in values:
                value = values[target]
                record.update({"observed_count": value, "target_state": "observed",
                               "target_met": type(value) is int and value == case["expected_target_count"],
                               "base_prediction_met": type(value) is int and value == case["expected_base_count"]})
            else:
                mismatches.append(case["id"] + ": frozen target check id missing")
                record.update({"target_state": "missing", "target_met": False,
                               "base_prediction_met": False})
            if control_values is None:
                control_values, control_statuses = values, statuses
            if (len(values) != 28 or set(values) != set(control_values) or
                    statuses != control_statuses or
                    list(statuses.values()).count("DERIVED") != 24 or
                    list(statuses.values()).count("SCOPED_OUT") != 4):
                mismatches.append(case["id"] + ": original check/status population changed")
            for key in control_values:
                if key != target and json.dumps(values.get(key), sort_keys=True) != json.dumps(control_values[key], sort_keys=True):
                    mismatches.append(case["id"] + ": non-target value changed: " + key)
            if baseline:
                old = baseline_cases[case["id"]]
                if old.get("statuses") != statuses or set(old.get("checks", {})) != set(values):
                    mismatches.append(case["id"] + ": baseline population changed")
                for key in values:
                    if key != target and json.dumps(old["checks"].get(key), sort_keys=True) != json.dumps(values[key], sort_keys=True):
                        mismatches.append(case["id"] + ": baseline non-target changed: " + key)
            if not record["target_met"]:
                failed.append(case["id"])
            record["state"] = "observed"
            outcomes.append(record)
            current = None
    except subprocess.TimeoutExpired as error:
        errors.append(current["id"] + ": timeout; current case unsettled, remaining cases not observed")
        current.update({"failure": "timeout", "streams_complete": False})
        for name, data in (("stdout", error.stdout), ("stderr", error.stderr)):
            if data is None:
                current[name + "_capture"] = "unavailable, not an observed empty stream"
            else:
                raw = data if isinstance(data, bytes) else data.encode("utf-8")
                path = root / ("stdout.json" if name == "stdout" else "stderr.txt")
                path.write_bytes(raw)
                current[name + "_partial_sha256"] = digest(raw)
                current[name + "_partial_path"] = str(path)
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        errors.append((current["id"] if current else "case loop") + ": unsettled: " + str(error))
        if current is not None:
            current.update({"failure": type(error).__name__, "grading_complete": False})
    try:
        consumer_after = digest(consumer.read_bytes())
        if consumer_after != digest(source_bytes):
            errors.append("consumer source changed")
    except OSError as error:
        consumer_after = None
        errors.append("consumer source custody unavailable: " + str(error))
    receipt = {"schema": "kotoba-configured-root-measurement-v1", "revision": args.revision,
               "recorded_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "consumer": oracle["consumer"], "consumer_sha256_before": digest(source_bytes),
               "consumer_sha256_after": consumer_after,
               "source_command": source_command, "oracle_sha256": args.oracle_sha256,
               "ruler_sha256": digest(Path(__file__).read_bytes()),
               "baseline_receipt_sha256": args.baseline_sha256,
               "cases": outcomes, "current_unsettled": current,
               "remaining_not_observed": remaining,
               "target_failures": failed, "behavioral_mismatches": mismatches,
               "evaluation_errors": errors,
               "expected_before_target_failures": oracle["expected_before_target_failures"],
               "scope": oracle["contract"],
               "verdict": "could-not-evaluate" if errors else "failed" if failed or mismatches else "clean"}
    (scratch / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"receipt": str(scratch / "receipt.json"), "settled_cases": len(outcomes),
                      "current_unsettled": current["id"] if current else None,
                      "remaining_not_observed": remaining, "target_failures": failed,
                      "behavioral_mismatches": mismatches, "evaluation_errors": errors,
                      "verdict": receipt["verdict"]}, sort_keys=True))
    return 2 if errors else 1 if failed or mismatches else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print("CONFIG_ROOT_RULER: could-not-evaluate: " + str(error), file=sys.stderr)
        raise SystemExit(2)
