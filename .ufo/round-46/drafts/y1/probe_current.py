#!/usr/bin/env python3
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
HEAD = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
COMPARATOR_REL = "verifiers/compare_harness_independent.py"
EXPECTED_COMPARATOR_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
FROZEN = DRAFT / "compare-055d3b9.py"
EVIDENCE = ROOT / ".ufo/round-45/evidence"
LIVE = EVIDENCE / "h11/live-current.json"
INDEPENDENT = EVIDENCE / "h11/independent-current.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    path = Path(path)
    return sha_bytes(path.read_bytes()) if path.is_file() else None


def tree_hash(path):
    path = Path(path)
    if not path.is_dir():
        return None
    items = []
    for child in sorted(p for p in path.rglob("*") if p.is_file()):
        items.append((child.relative_to(path).as_posix(), sha_file(child)))
    return sha_bytes(json.dumps(items, separators=(",", ":")).encode())


def snapshot():
    def git(*args):
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
    return {
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "comparator_worktree_sha256": sha_file(ROOT / COMPARATOR_REL),
        "scope_sha256": sha_file(SCOPE),
        "status": git("status", "--short"),
        "tracked_diff_exit": subprocess.run(["git", "diff", "--quiet"], cwd=ROOT).returncode,
        "index_diff_exit": subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode,
    }


def possible_targets(payload_path):
    try:
        payload = json.loads(Path(payload_path).read_text(encoding="utf-8"))
    except Exception:
        return {}
    targets = set()
    def walk(value):
        if isinstance(value, dict):
            target = value.get("target")
            if isinstance(target, str) and target.startswith("/"):
                p = Path(target)
                try:
                    p.relative_to(ROOT)
                except ValueError:
                    pass
                else:
                    targets.add(p)
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)
    walk(payload)
    return {str(p): tree_hash(p) for p in sorted(targets)}


def run_case(case_id, live_path, independent_path, process_cwd, scope_arg,
             scope_hash_paths, receipt_path=None):
    inputs = {str(Path(live_path)): sha_file(live_path),
              str(Path(independent_path)): sha_file(independent_path)}
    inputs.update({str(Path(p)): sha_file(p) for p in scope_hash_paths if Path(p).is_file()})
    target_hashes = possible_targets(independent_path)
    cmd = [sys.executable, "-B", str(FROZEN),
           "--live-json", str(Path(live_path).resolve()),
           "--independent-json", str(Path(independent_path).resolve()),
           "--expect-n", "28", "--cwd", str(ROOT),
           "--scope-file", scope_arg, "--no-stamp", "--json"]
    if receipt_path:
        cmd += ["--receipt", str(receipt_path)]
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(cmd, cwd=process_cwd, text=True, capture_output=True)
    finished = datetime.now(timezone.utc).isoformat()
    try:
        output = json.loads(proc.stdout)
    except Exception:
        output = None
    unchanged = {p: sha_file(p) for p in inputs}
    record = {
        "id": case_id,
        "started_utc": started,
        "finished_utc": finished,
        "argv": cmd,
        "process_cwd": str(Path(process_cwd).resolve()),
        "repo_cwd": str(ROOT),
        "scope_argument": scope_arg,
        "inputs_before_sha256": inputs,
        "inputs_after_sha256": unchanged,
        "inputs_unchanged": inputs == unchanged,
        "target_tree_sha256": target_hashes,
        "exit": proc.returncode,
        "headline": output.get("headline") if isinstance(output, dict) else None,
        "agreement": output.get("agreement") if isinstance(output, dict) else None,
        "disagreements": output.get("disagreements") if isinstance(output, dict) else None,
        "stdout_sha256": sha_bytes(proc.stdout.encode()),
        "stderr": proc.stderr.strip(),
        "stderr_sha256": sha_bytes(proc.stderr.encode()),
        "receipt_sha256": sha_file(receipt_path) if receipt_path else None,
    }
    return record


def main():
    raw = subprocess.check_output(["git", "show", f"{HEAD}:{COMPARATOR_REL}"], cwd=ROOT)
    FROZEN.write_bytes(raw)
    frozen_sha = sha_bytes(raw)
    if frozen_sha != EXPECTED_COMPARATOR_SHA:
        raise SystemExit(f"frozen comparator digest mismatch: {frozen_sha}")
    if sha_file(LIVE) != "0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341":
        raise SystemExit("live capture digest mismatch")
    if sha_file(INDEPENDENT) != "eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887":
        raise SystemExit("independent capture digest mismatch")

    h11 = EVIDENCE / "h11/census-inputs"
    s1 = EVIDENCE / "s1"
    planted = EVIDENCE / "h11/planted-cwd"
    h06 = EVIDENCE / "h06"
    start = snapshot()
    records = []
    records.append(run_case(
        "honest-live-join", LIVE, INDEPENDENT, ROOT,
        "verifiers/harness-independent-scope.json", [SCOPE],
        DRAFT / "honest-live-receipt.json"))
    scope_attack = s1 / "relative-scope-null-isolation.json"
    planted_scope = planted / "verifiers/harness-independent-scope.json"
    records.append(run_case(
        "scope-file-relative-planted-cwd", LIVE, scope_attack, planted,
        "verifiers/harness-independent-scope.json", [SCOPE, planted_scope],
        DRAFT / "scope-planted-cwd-receipt.json"))
    records.append(run_case(
        "scope-file-relative-honest-cwd-control", LIVE, scope_attack, ROOT,
        "verifiers/harness-independent-scope.json", [SCOPE],
        DRAFT / "scope-honest-cwd-receipt.json"))

    live_arms = [
        "live-mode-positive-masks-independent-drift",
        "live-mode-split-across-row-channels",
        "live-top-level-observed-summary-divergence",
        "live-verdict-shadow-in-row-channel",
    ]
    for arm in live_arms:
        live_input = h11 / f"live-arm-{arm}.json"
        records.append(run_case(arm, live_input, INDEPENDENT, ROOT,
                               str(SCOPE), [SCOPE]))

    for case_id, independent_input in [
        ("duplicate-raw-top-level-results", s1 / "top-level-duplicate-results.json"),
        ("duplicate-raw-record-re_derived", s1 / "duplicate-record-rederived.json"),
        ("scoped-out-reason-evidence-drift", h06 / "fresh-fabricated-reason-evidence-independent.json"),
        ("scoped-out-probe-target-drift", h06 / "fresh-uncommitted-probe-target-independent.json"),
    ]:
        records.append(run_case(case_id, LIVE, independent_input, ROOT,
                               str(SCOPE), [SCOPE]))

    end = snapshot()
    result = {
        "measurement_started_utc": records[0]["started_utc"],
        "measurement_finished_utc": records[-1]["finished_utc"],
        "claim_file_sha256": sha_file(ROOT / ".ufo/round-46/claims.json"),
        "frozen_revision": HEAD,
        "frozen_tree": subprocess.check_output(["git", "rev-parse", f"{HEAD}^{{tree}}"], cwd=ROOT, text=True).strip(),
        "frozen_comparator_sha256": frozen_sha,
        "comparator_copy": str(FROZEN.relative_to(ROOT)),
        "source_at_start": start,
        "source_at_end": end,
        "live_capture_sha256": sha_file(LIVE),
        "independent_capture_sha256": sha_file(INDEPENDENT),
        "scope_sha256": sha_file(SCOPE),
        "records": records,
    }
    (DRAFT / "probe-current-results.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "frozen_comparator_sha256": frozen_sha,
        "start": result["source_at_start"],
        "end": end,
        "records": [{"id": r["id"], "exit": r["exit"], "headline": r["headline"],
                     "agreement": r["agreement"], "stderr": r["stderr"],
                     "inputs_unchanged": r["inputs_unchanged"]} for r in records],
        "result_sha256": sha_file(DRAFT / "probe-current-results.json"),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
