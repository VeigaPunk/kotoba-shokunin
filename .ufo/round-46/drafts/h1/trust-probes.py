#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
EVIDENCE = REPO / ".ufo/round-46/evidence/H1-trust-boundary.json"
COMPARATOR = REPO / "verifiers/compare_harness_independent.py"
LIVE_PRODUCER = REPO / "verifiers/verify_harness_claims.py"
IND_PRODUCER = REPO / "verifiers/verify_harness_independent.py"
SCOPE = REPO / "verifiers/harness-independent-scope.json"
TARGET = "omp.elf.template_bytes"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    return digest(path.read_bytes())


def git(*args):
    proc = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, check=True)
    return proc.stdout.strip()


def capture_producer(path, command):
    proc = subprocess.run(command, cwd=REPO, capture_output=True, timeout=300)
    path.write_bytes(proc.stdout)
    return {
        "command": command,
        "exit": proc.returncode,
        "stdout_sha256": digest(proc.stdout),
        "stderr_sha256": digest(proc.stderr),
    }


def target_row(payload, channel):
    rows = payload.get(channel)
    if not isinstance(rows, list):
        raise AssertionError(f"missing {channel} record list")
    return next(row for row in rows if row.get("check") == TARGET)


def write_json(path, value):
    payload = (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()
    path.write_bytes(payload)
    return digest(payload)


def set_independent_value(payload, value):
    changed = []
    for channel in ("results", "rows"):
        rows = payload.get(channel)
        if isinstance(rows, list):
            row = next(item for item in rows if item.get("check") == TARGET)
            for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                if key in row:
                    row[key] = value
                    changed.append(f"{channel}.{key}")
    checks = payload.get("checks")
    if isinstance(checks, dict) and TARGET in checks:
        checks[TARGET] = value
        changed.append("checks[check]")
    if len(changed) < 2:
        raise AssertionError(f"independent channels not all found/changed: {changed}")
    return changed


def run_case(name, live_path, ind_path, argv_base):
    cmd = [*argv_base, "--live-json", str(live_path), "--independent-json", str(ind_path)]
    before = {"live": file_digest(live_path), "independent": file_digest(ind_path), "scope": file_digest(SCOPE)}
    proc = subprocess.run(cmd, cwd=REPO, capture_output=True, timeout=300)
    after = {"live": file_digest(live_path), "independent": file_digest(ind_path), "scope": file_digest(SCOPE)}
    try:
        report = json.loads(proc.stdout)
    except (ValueError, UnicodeDecodeError):
        report = None
    return {
        "id": name,
        "command": cmd,
        "exit": proc.returncode,
        "reason": report.get("reason") if isinstance(report, dict) else proc.stderr.decode(errors="replace"),
        "headline": report.get("headline") if isinstance(report, dict) else None,
        "agreement": report.get("agreement") if isinstance(report, dict) else None,
        "live_input_sha256": before["live"],
        "independent_input_sha256": before["independent"],
        "scope_sha256": before["scope"],
        "input_hashes_unchanged": before == after,
        "stdout_sha256": digest(proc.stdout),
        "stderr_sha256": digest(proc.stderr),
    }


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    tracked_status_before = {
        "worktree_diff_empty": subprocess.run(["git", "diff", "--quiet"], cwd=REPO).returncode == 0,
        "index_diff_empty": subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO).returncode == 0,
    }
    source_start = {str(path.relative_to(REPO)): file_digest(path)
                    for path in (COMPARATOR, LIVE_PRODUCER, IND_PRODUCER, SCOPE)}

    live_path = DRAFT / "live-base.json"
    ind_path = DRAFT / "independent-base.json"
    producer_runs = {
        "live": capture_producer(live_path, [sys.executable, "-B", str(LIVE_PRODUCER), "--json"]),
        "independent": capture_producer(ind_path, [sys.executable, "-B", str(IND_PRODUCER), "--json"]),
    }
    if producer_runs["live"]["exit"] != 0 or producer_runs["independent"]["exit"] != 0:
        raise SystemExit("producer command failed; captured its exit and stderr hash in no result")
    live_base, ind_base = json.loads(live_path.read_bytes()), json.loads(ind_path.read_bytes())
    live_row = target_row(live_base, "results")
    old_live = live_row["observed"]
    old_ind = target_row(ind_base, "results").get("re_derived", target_row(ind_base, "results").get("value"))
    if not (isinstance(old_live, int) and not isinstance(old_live, bool) and old_ind == old_live):
        raise AssertionError(f"target is not an equal integer control: live={old_live!r}, ind={old_ind!r}")

    argv_base = [sys.executable, "-B", str(COMPARATOR), "--cwd", str(REPO),
                 "--scope-file", str(SCOPE), "--expect-n", "28", "--no-stamp", "--json"]
    cases = []
    cases.append(run_case("honest-producer-control", live_path, ind_path, argv_base))

    ind_drift = copy.deepcopy(ind_base)
    changed_fields = set_independent_value(ind_drift, old_live + 1)
    ind_drift_path = DRAFT / "independent-template-bytes-plus-one.json"
    ind_drift_sha = write_json(ind_drift_path, ind_drift)
    live_positive = copy.deepcopy(live_base)
    target_row(live_positive, "results")["mode"] = "positive"
    live_positive_path = DRAFT / "live-template-bytes-positive.json"
    live_positive_sha = write_json(live_positive_path, live_positive)
    cases.append(run_case("caller-positive-mode-masks-independent-plus-one", live_positive_path,
                          ind_drift_path, argv_base))

    live_mode_split = copy.deepcopy(live_positive)
    live_mode_split["rows"] = copy.deepcopy(live_mode_split["results"])
    target_row(live_mode_split, "rows")["mode"] = "equal"
    live_mode_split_path = DRAFT / "live-mode-split-positive-results-equal-rows.json"
    live_mode_split_sha = write_json(live_mode_split_path, live_mode_split)
    cases.append(run_case("mode-conflict-across-live-row-channels", live_mode_split_path,
                          ind_drift_path, argv_base))

    live_verdict_split = copy.deepcopy(live_base)
    live_verdict_split["rows"] = copy.deepcopy(live_verdict_split["results"])
    target_row(live_verdict_split, "rows")["verdict"] = "DRIFT"
    live_verdict_split_path = DRAFT / "live-verdict-split-pass-results-drift-rows.json"
    live_verdict_split_sha = write_json(live_verdict_split_path, live_verdict_split)
    cases.append(run_case("verdict-conflict-across-live-row-channels", live_verdict_split_path,
                          ind_path, argv_base))

    live_summary = copy.deepcopy(live_base)
    live_summary["observed"]["omp"]["template_bytes"] = old_live + 1
    live_summary_path = DRAFT / "live-top-level-observed-summary-plus-one.json"
    live_summary_sha = write_json(live_summary_path, live_summary)
    cases.append(run_case("top-level-observed-summary-conflicts-with-row", live_summary_path,
                          ind_path, argv_base))

    live_value_split = copy.deepcopy(live_base)
    live_value_split["rows"] = copy.deepcopy(live_value_split["results"])
    target_row(live_value_split, "rows")["observed"] = old_live + 1
    live_value_split_path = DRAFT / "live-row-value-channel-conflict-control.json"
    live_value_split_sha = write_json(live_value_split_path, live_value_split)
    cases.append(run_case("observed-value-conflict-across-live-row-channels", live_value_split_path,
                          ind_path, argv_base))

    source_end = {str(path.relative_to(REPO)): file_digest(path)
                  for path in (COMPARATOR, LIVE_PRODUCER, IND_PRODUCER, SCOPE)}
    if source_start != source_end or git("rev-parse", "HEAD") != head or git("rev-parse", "HEAD^{tree}") != tree:
        raise SystemExit("source/HEAD/tree changed during test; do not treat this run as pinned")
    if any(not case["input_hashes_unchanged"] for case in cases):
        raise SystemExit("a comparator invocation changed a captured input")

    result = {
        "schema": "kotoba.round46.h1.producer-trust.v1",
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python3 -B .ufo/round-46/drafts/h1/trust-probes.py",
        "target": {"head": head, "head_tree": tree, "tracked_status_before": tracked_status_before,
                   "source_sha256_start": source_start, "source_sha256_end": source_end},
        "producer_runs": producer_runs,
        "producer_payload_sha256": {"live": file_digest(live_path), "independent": file_digest(ind_path)},
        "scope_sha256": file_digest(SCOPE),
        "case_inputs": {
            "positive_live": {"path": str(live_positive_path.relative_to(REPO)), "sha256": live_positive_sha},
            "independent_plus_one": {"path": str(ind_drift_path.relative_to(REPO)), "sha256": ind_drift_sha,
                                      "changed_aliases": changed_fields},
            "mode_split_live": {"path": str(live_mode_split_path.relative_to(REPO)), "sha256": live_mode_split_sha},
            "verdict_split_live": {"path": str(live_verdict_split_path.relative_to(REPO)), "sha256": live_verdict_split_sha},
            "summary_live": {"path": str(live_summary_path.relative_to(REPO)), "sha256": live_summary_sha},
            "value_split_live_control": {"path": str(live_value_split_path.relative_to(REPO)), "sha256": live_value_split_sha},
        },
        "target_check": TARGET,
        "target_values": {"observed": old_live, "independent_control": old_ind,
                          "independent_plus_one": old_live + 1},
        "cases": cases,
    }
    EVIDENCE.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence": str(EVIDENCE.relative_to(REPO)),
                      "evidence_sha256": file_digest(EVIDENCE),
                      "head": head, "tree": tree, "source_sha256": source_start,
                      "target_values": result["target_values"], "cases": cases}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
