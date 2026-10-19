from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
RUN = DRAFT / "run-17"
INPUTS = RUN / "inputs"
PLANTED = RUN / "cases" / "planted-cwd"
OUTPUTS = RUN / "outputs"
BASELINE_INPUTS = DRAFT / "run-16/inputs"
BASELINE_RESULT = DRAFT / "run-03/outputs/scope-path-results.json"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
TARGET = "omp.offered.skills"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def identity() -> dict:
    return {
        "at": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
        "tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
    }


def invoke(name: str, comparator: Path, live: Path, independent: Path,
           process_cwd: Path, cli_cwd: Path) -> dict:
    receipt = OUTPUTS / f"{name}.receipt.json"
    argv = [
        sys.executable, "-B", str(comparator),
        "--live-json", str(live), "--independent-json", str(independent),
        "--scope-file", str(SCOPE_REL), "--cwd", str(cli_cwd),
        "--expect-n", "28", "--no-stamp", "--json", "--receipt", str(receipt),
    ]
    resolved = (cli_cwd / SCOPE_REL).resolve()
    proc = subprocess.run(argv, cwd=process_cwd, capture_output=True, text=True,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, timeout=180)
    output = json.loads(proc.stdout) if proc.returncode == 0 else None
    if output is not None:
        (OUTPUTS / f"{name}.stdout.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    receipt_data = json.loads(receipt.read_text()) if receipt.is_file() else None
    return {
        "name": name,
        "command": argv,
        "process_cwd": str(process_cwd),
        "cli_cwd": str(cli_cwd),
        "resolved_scope_path": str(resolved),
        "resolved_scope_sha256": sha(resolved.read_bytes()),
        "exit": proc.returncode,
        "stderr": proc.stderr,
        "headline": output.get("headline") if output else None,
        "agreement": output.get("agreement") if output else None,
        "receipt_scope": receipt_data.get("scope_file") if receipt_data else None,
        "receipt_path": str(receipt) if receipt_data else None,
    }


def main() -> int:
    for directory in (INPUTS, PLANTED / "verifiers", OUTPUTS):
        directory.mkdir(parents=True, exist_ok=False)
    started = identity()
    comparator = DRAFT / "run-14/inputs/compare_candidate.py"
    comparator_sha = sha(comparator.read_bytes())
    live = INPUTS / "live.json"
    live.write_bytes((BASELINE_INPUTS / "live.json").read_bytes())
    independent = json.loads((BASELINE_INPUTS / "independent.json").read_text())
    scope = json.loads((BASELINE_INPUTS / "scope.json").read_text())
    reason = "R1 planted-CWD closure probe; scoped value must not leave the join"
    probe = copy.deepcopy(independent["scoped_out_probes"]["omp.catalogue.found"])
    records_touched = {}
    for channel in ("results", "rows"):
        rows = independent.get(channel)
        if not isinstance(rows, list):
            continue
        matches = [row for row in rows if isinstance(row, dict) and row.get("check") == TARGET]
        if len(matches) != 1:
            raise RuntimeError(f"{channel}: expected one {TARGET}; got {len(matches)}")
        record = matches[0]
        for field in ("expected", "expected_value", "re_derived", "value", "observed"):
            if field in record:
                record[field] = None
        record["re_derived"] = None
        record["value"] = None
        record["status"] = "SCOPED_OUT"
        record["evidence"] = "SCOPED_OUT: " + reason
        record["probe"] = copy.deepcopy(probe)
        records_touched[channel] = 1
    checks = independent.get("checks")
    if not isinstance(checks, dict) or TARGET not in checks:
        raise RuntimeError(f"checks channel lacks {TARGET}")
    checks[TARGET] = None
    independent.setdefault("scoped_out", {})[TARGET] = reason
    independent.setdefault("scoped_out_probes", {})[TARGET] = copy.deepcopy(probe)
    independent_path = INPUTS / "independent-planted-scope.json"
    independent_path.write_text(json.dumps(independent, indent=2, sort_keys=True) + "\n")

    entry_template = copy.deepcopy(next(iter(scope["scope_out"].values())))
    entry_template["reason"] = reason
    scope["scope_out"][TARGET] = entry_template
    planted_scope = PLANTED / SCOPE_REL
    planted_scope.write_text(json.dumps(scope, indent=2, sort_keys=True) + "\n")
    planted_sha = sha(planted_scope.read_bytes())
    (INPUTS / "planted-scope.json").write_bytes(planted_scope.read_bytes())
    scope_base = INPUTS / "scope-base.json"
    scope_base.write_bytes((BASELINE_INPUTS / "scope.json").read_bytes())

    rejected = invoke("honest-cwd-rejects-planted", comparator, live, independent_path,
                      PLANTED, ROOT)
    accepted_control = invoke("matching-cwd-enforces-and-attests-plant", comparator, live,
                              independent_path, PLANTED, PLANTED)
    if rejected["exit"] != 2 or "laundering" not in rejected["stderr"]:
        raise RuntimeError(f"honest --cwd did not class-reject the planted row: {rejected}")
    if rejected["resolved_scope_sha256"] != sha((BASELINE_INPUTS / "scope.json").read_bytes()):
        raise RuntimeError(f"honest --cwd did not resolve to the baseline scope: {rejected}")
    if accepted_control["exit"] != 0 or accepted_control["headline"]["n"] != 23:
        raise RuntimeError(f"matching --cwd control did not accept valid planted scope: {accepted_control}")
    if accepted_control["receipt_scope"]["sha256"] != planted_sha:
        raise RuntimeError(f"matching --cwd receipt digest differs from planted scope: {accepted_control}")
    if accepted_control["receipt_scope"]["path"] != str(planted_scope.resolve()):
        raise RuntimeError(f"matching --cwd receipt path differs from resolved scope: {accepted_control}")

    finished = identity()
    if started["head"] != finished["head"] or started["tree"] != finished["tree"]:
        raise RuntimeError("HEAD/tree changed during R1 24-row closure check")
    result = {
        "measurement": {"started": started, "finished": finished},
        "candidate": {"path": str(comparator), "sha256": comparator_sha},
        "inputs": {
            "source_bundle": str(BASELINE_INPUTS),
            "live_sha256": sha(live.read_bytes()),
            "independent_clean_sha256": sha((BASELINE_INPUTS / "independent.json").read_bytes()),
            "independent_planted_scope_sha256": sha(independent_path.read_bytes()),
            "honest_scope_sha256": sha(scope_base.read_bytes()),
            "planted_scope_sha256": planted_sha,
            "target_check": TARGET,
            "updated_channels": records_touched,
        },
        "before": {
            "candidate_sha256": "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4",
            "result_path": str(BASELINE_RESULT),
            "result_sha256": sha(BASELINE_RESULT.read_bytes()),
            "relative_process_cwd_exit": 0,
            "headline": "23/23",
        },
        "after_cases": [rejected, accepted_control],
    }
    result_path = OUTPUTS / "cwd-closure-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(result_path), "result_sha256": sha(result_path.read_bytes()),
        "candidate_sha256": comparator_sha,
        "before_exit": 0, "after_planted_payload_exit": rejected["exit"],
        "after_planted_payload_error": rejected["stderr"],
        "matching_cwd_control_exit": accepted_control["exit"],
        "matching_cwd_control_headline": accepted_control["headline"],
        "receipt_scope": accepted_control["receipt_scope"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
