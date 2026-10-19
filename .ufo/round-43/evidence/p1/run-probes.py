#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
ROOT = DRAFT.parents[3]
FROZEN = DRAFT / "compare-b1be35f.py"
CANDIDATE = DRAFT / "compare-candidate.py"
LIVE = DRAFT / "live.json"
INDEPENDENT = DRAFT / "independent.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
OUTPUT = DRAFT / "probe-results.json"
SCOPED_IDS = {
    "omp.catalogue.found",
    "omp.catalogue.matched",
    "omp.catalogue.missing_names",
    "omp.catalogue.total",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def capture(command, output):
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=300)
    if proc.returncode != 0:
        raise RuntimeError("producer failed (%s): %s" % (command[1], proc.stderr[-800:]))
    output.write_text(proc.stdout, encoding="utf-8")
    return json.loads(proc.stdout)


def harvested(live):
    return {row["check"]: row["observed"] for row in live["results"]}


def record_map(payload, channel):
    return {row["check"]: row for row in payload[channel]}


def arms(live, independent):
    values = harvested(live)
    out = {}

    expected_only = copy.deepcopy(independent)
    for cid in values:
        for channel in ("results", "rows"):
            record = record_map(expected_only, channel)[cid]
            for key in ("expected_value", "re_derived", "value", "observed"):
                record.pop(key, None)
            record["expected"] = values[cid]
        expected_only["checks"][cid] = values[cid]
    out["heldout-expected-only-full-copy"] = expected_only

    out["heldout-flat-dotted-map"] = dict(values)
    out["heldout-nested-checks-map"] = {"checks": dict(values)}
    out["heldout-nested-expected-wrapper"] = {"expected": dict(values)}
    out["heldout-nested-observations-wrapper"] = {"observations": dict(values)}
    out["heldout-wrapper-precedence-expected-over-observations"] = {
        "expected": dict(values),
        "observations": {cid: 999 for cid in values},
    }
    return out


def invoke(driver, live_path, ind_path):
    command = [
        sys.executable, str(driver),
        "--live-json", str(live_path),
        "--independent-json", str(ind_path),
        "--expect-n", "28",
        "--cwd", str(ROOT),
        "--scope-file", str(SCOPE),
        "--no-stamp", "--json",
    ]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=120)
    try:
        report = json.loads(proc.stdout)
    except ValueError:
        report = None
    return {
        "command": command,
        "exit": proc.returncode,
        "headline": report.get("headline") if report else None,
        "reason": report.get("reason") if report else None,
        "stdout_sha256": digest(proc.stdout.encode()),
        "stderr": proc.stderr.strip(),
    }


def main():
    frozen_bytes = subprocess.run(
        ["git", "show", "b1be35f:verifiers/compare_harness_independent.py"],
        cwd=ROOT, capture_output=True, check=True).stdout
    FROZEN.write_bytes(frozen_bytes)
    source = ROOT / "verifiers/compare_harness_independent.py"
    candidate_bytes = source.read_bytes()
    CANDIDATE.write_bytes(candidate_bytes)
    candidate_sha = digest(candidate_bytes)
    live = capture([sys.executable, "verifiers/verify_harness_claims.py", "--json"], LIVE)
    independent = capture(
        [sys.executable, "verifiers/verify_harness_independent.py", "--json"],
        INDEPENDENT)
    payloads = arms(live, independent)
    results = {}
    for arm_id, payload in payloads.items():
        path = DRAFT / ("arm-" + arm_id + ".json")
        path.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")
        before = invoke(FROZEN, LIVE, path)
        after = invoke(CANDIDATE, LIVE, path)
        named_scope = any(cid in after["stderr"] for cid in SCOPED_IDS)
        named_class = any(token in after["stderr"] for token in (
            "scope-out value laundering", "derived-set overflow",
            "competing value-map aliases"))
        results[arm_id] = {
            "payload_path": str(path),
            "payload_sha256": digest(path.read_bytes()),
            "before_frozen": before,
            "after_candidate_snapshot": after,
            "matched": before["exit"] == 0 and after["exit"] == 2
                       and named_scope and named_class,
        }
    control = invoke(FROZEN, LIVE, INDEPENDENT)
    after_control = invoke(CANDIDATE, LIVE, INDEPENDENT)
    worktree_sha_after = digest(source.read_bytes())
    report = {
        "replay_command": ["python3", str(Path(__file__).relative_to(ROOT))],
        "measured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                capture_output=True, text=True, check=True).stdout.strip(),
        "head_tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT,
                                     capture_output=True, text=True, check=True).stdout.strip(),
        "frozen_commit": "b1be35f9522f21c0c5b39879358a011806ab9200",
        "frozen_tree": "8bb24450a9c500c427019c7147013b4946525b09",
        "frozen_comparator_sha256": digest(frozen_bytes),
        "candidate_snapshot_path": str(CANDIDATE),
        "candidate_comparator_sha256": candidate_sha,
        "worktree_comparator_sha256_after": worktree_sha_after,
        "candidate_unchanged_during_measurement": candidate_sha == worktree_sha_after,
        "live_instrument_sha256": digest((ROOT / "verifiers/verify_harness_claims.py").read_bytes()),
        "independent_instrument_sha256": digest((ROOT / "verifiers/verify_harness_independent.py").read_bytes()),
        "scope_sha256": digest(SCOPE.read_bytes()),
        "live_payload_sha256": digest(LIVE.read_bytes()),
        "independent_payload_sha256": digest(INDEPENDENT.read_bytes()),
        "live_n": len(live["results"]),
        "independent_n": len(independent["results"]),
        "honest_control_before": control,
        "honest_control_after": after_control,
        "arms": results,
    }
    control_ok = (control["exit"] == 0 and after_control["exit"] == 0
                  and after_control["headline"] == {
                      "column": "mode-aware protocol", "joined_scope": 24,
                      "live_checks": 28, "n": 24, "total": 24})
    report["all_six_arms_closed"] = all(result["matched"] for result in results.values())
    report["honest_control_24_of_24"] = control_ok
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    for arm_id, result in results.items():
        before = result["before_frozen"]
        after = result["after_candidate_snapshot"]
        print("%s before=%d %s after=%d %s matched=%s" % (
            arm_id, before["exit"], (before["headline"] or {}).get("n"),
            after["exit"], after["stderr"][:240], result["matched"]))
    print("honest before=%d %s/%s after=%d %s/%s" % (
        control["exit"], (control["headline"] or {}).get("n"),
        (control["headline"] or {}).get("total"), after_control["exit"],
        (after_control["headline"] or {}).get("n"),
        (after_control["headline"] or {}).get("total")))
    print("results=%s sha256=%s" % (OUTPUT, digest(OUTPUT.read_bytes())))
    print("measured_at=%s head=%s tree=%s" % (
        report["measured_at_utc"], report["head"], report["head_tree"]))
    print("frozen_cmp=%s candidate_cmp=%s scope=%s" % (
        report["frozen_comparator_sha256"], report["candidate_comparator_sha256"],
        report["scope_sha256"]))
    return 0 if report["all_six_arms_closed"] and control_ok \
        and report["candidate_unchanged_during_measurement"] else 1


if __name__ == "__main__":
    sys.exit(main())
