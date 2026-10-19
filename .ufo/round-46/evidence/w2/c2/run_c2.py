#!/usr/bin/env python3
"""Replay registered round-46 C2 payload arms against one comparator snapshot."""
import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def set_independent_value(payload, check_id, value):
    changed = 0
    for channel in ("results", "rows"):
        for row in payload.get(channel, []) or []:
            if isinstance(row, dict) and row.get("check") == check_id:
                for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                    if key in row:
                        row[key] = copy.deepcopy(value)
                        changed += 1
    checks = payload.get("checks")
    if isinstance(checks, dict) and check_id in checks:
        checks[check_id] = copy.deepcopy(value)
        changed += 1
    if not changed:
        raise RuntimeError(f"no independent value changed for {check_id}")


def duplicate_top_level_results(payload):
    if not isinstance(payload, dict) or "results" not in payload:
        raise RuntimeError("independent input has no top-level results member")
    members = []
    for key, value in payload.items():
        members.append(json.dumps(key, ensure_ascii=False) + ":" + compact(value))
        if key == "results":
            members.append(json.dumps(key, ensure_ascii=False) + ":" + compact(value))
    return ("{" + ",".join(members) + "}\n").encode("utf-8")


def duplicate_record_rederived(payload):
    rows = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(rows, list):
        raise RuntimeError("independent input has no results list")
    target_index = next((i for i, row in enumerate(rows)
                         if isinstance(row, dict) and "re_derived" in row), None)
    if target_index is None:
        raise RuntimeError("independent results has no re_derived record")

    def dump(value, path=()):
        if isinstance(value, dict):
            members = []
            for key, child in value.items():
                if path == ("results", target_index) and key == "re_derived":
                    members.append(json.dumps(key, ensure_ascii=False) + ":null")
                members.append(json.dumps(key, ensure_ascii=False) + ":" + dump(child, path + (key,)))
            return "{" + ",".join(members) + "}"
        if isinstance(value, list):
            return "[" + ",".join(dump(child, path + (i,)) for i, child in enumerate(value)) + "]"
        return compact(value)

    return (dump(payload) + "\n").encode("utf-8")


def stderr_class(stderr):
    text = stderr.strip()
    if not text:
        return "none"
    first = text.splitlines()[0]
    if "duplicate JSON member" in first:
        match = re.search(r"duplicate JSON member '([^']+)'", first)
        return "duplicate JSON member '" + (match.group(1) if match else "unknown") + "'"
    for name in ("mode", "verdict", "summary"):
        if f"live {name} shadow" in first:
            return f"live {name} shadow"
    if "live metadata missing" in first:
        return "live metadata missing"
    if "false blocker" in first:
        return "false blocker"
    if "ERROR:" in first:
        return first.split("ERROR:", 1)[1].strip()
    return first


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("comparator", help="comparator Python file to replay")
    parser.add_argument("--label", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--live", required=True)
    parser.add_argument("--independent", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--inputs-dir", required=True)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    comparator = Path(args.comparator).resolve()
    inputs_dir = Path(args.inputs_dir).resolve()
    inputs_dir.mkdir(parents=True, exist_ok=True)
    live_bytes = Path(args.live).read_bytes()
    independent_bytes = Path(args.independent).read_bytes()
    scope_bytes = Path(args.scope).read_bytes()
    live_base = json.loads(live_bytes)
    independent_base = json.loads(independent_bytes)
    check_id = "oc.log.skills_rescan_max"

    producer_live_row = next((r for r in live_base.get("results", [])
                              if isinstance(r, dict) and r.get("check") == check_id), None)
    producer_independent_row = next((r for r in independent_base.get("results", [])
                                     if isinstance(r, dict) and r.get("check") == check_id), None)
    if (producer_live_row is None or not isinstance(producer_live_row.get("observed"), (int, float))
            or isinstance(producer_live_row.get("observed"), bool)):
        raise RuntimeError(f"numeric live row missing for {check_id}")
    if producer_independent_row is None or "re_derived" not in producer_independent_row:
        raise RuntimeError(f"independent re_derived row missing for {check_id}")
    observed = producer_live_row["observed"]
    skew = observed + 999
    if int(skew) != skew:
        raise RuntimeError("selected live value did not yield an integer skew")
    skew = int(skew)
    original_mode = producer_live_row.get("mode")
    if not isinstance(original_mode, str):
        raise RuntimeError("selected live row has no string mode")
    alternate_mode = "positive" if original_mode != "positive" else "zero"
    summary_path = live_base["summary_paths"][check_id]
    summary_value = live_base["observed"][summary_path[0]][summary_path[1]]
    test_live = {
        "observed": {summary_path[0]: {summary_path[1]: copy.deepcopy(summary_value)}},
        "results": [copy.deepcopy(producer_live_row)],
        "modes": {check_id: original_mode},
        "verdicts": {check_id: producer_live_row["verdict"]},
        "summary_paths": {check_id: copy.deepcopy(summary_path)},
    }
    test_independent = {"results": [copy.deepcopy(producer_independent_row)]}
    base_live_bytes = encoded(test_live)
    base_independent_bytes = encoded(test_independent)

    cases = []

    def add(name, live_data, independent_data, expect_n=1):
        live_path = inputs_dir / f"{name}.live.json"
        independent_path = inputs_dir / f"{name}.independent.json"
        scope_path = inputs_dir / f"{name}.scope.json"
        live_path.write_bytes(live_data)
        independent_path.write_bytes(independent_data)
        scope_path.write_bytes(scope_bytes)
        argv = [sys.executable, str(comparator), "--live-json", str(live_path),
                "--independent-json", str(independent_path), "--expect-n", str(expect_n),
                "--cwd", str(repo), "--scope-file", str(scope_path), "--no-stamp", "--json"]
        proc = subprocess.run(argv, cwd=repo, capture_output=True, text=True, timeout=300)
        parsed = None
        try:
            parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
        except ValueError:
            pass
        agreement = parsed.get("agreement") if isinstance(parsed, dict) else None
        headline = parsed.get("headline") if isinstance(parsed, dict) else None
        cases.append({
            "name": name,
            "expect_n": expect_n,
            "argv": argv,
            "input_sha256": {
                "live": sha(live_path.read_bytes()),
                "independent": sha(independent_path.read_bytes()),
                "scope": sha(scope_path.read_bytes()),
            },
            "exit": proc.returncode,
            "stderr_class": stderr_class(proc.stderr),
            "stderr_first_line": proc.stderr.strip().splitlines()[0] if proc.stderr.strip() else "",
            "stdout_sha256": sha(proc.stdout.encode("utf-8")),
            "agreement": agreement,
            "headline": headline,
            "reason": parsed.get("reason") if isinstance(parsed, dict) else None,
        })

    # Four live shadow cases from the registered R2 matrix. The one-row
    # projection is taken from fresh producer output so volatile scoped-out
    # census probes cannot mask the C2 parser outcomes.
    independent_drift = copy.deepcopy(test_independent)
    set_independent_value(independent_drift, check_id, skew)
    independent_drift_bytes = encoded(independent_drift)

    live_mode = copy.deepcopy(test_live)
    next(r for r in live_mode["results"] if r.get("check") == check_id)["mode"] = alternate_mode
    add("live-mode-row-shadow-vs-mirror", encoded(live_mode), independent_drift_bytes, 1)

    live_summary = copy.deepcopy(test_live)
    live_summary["observed"][summary_path[0]][summary_path[1]] = skew
    add("live-summary-path-shadow", encoded(live_summary), base_independent_bytes, 1)

    live_bad_verdict = copy.deepcopy(test_live)
    next(r for r in live_bad_verdict["results"] if r.get("check") == check_id)["verdict"] = []
    add("live-nonstring-verdict", encoded(live_bad_verdict), base_independent_bytes, 1)

    live_duplicate = copy.deepcopy(test_live)
    duplicate_rows = copy.deepcopy(live_duplicate["results"])
    index = next(i for i, r in enumerate(duplicate_rows) if r.get("check") == check_id)
    first = copy.deepcopy(duplicate_rows[index])
    first["mode"] = original_mode
    last = copy.deepcopy(first)
    last["mode"] = alternate_mode
    duplicate_rows[index:index + 1] = [first, last]
    live_duplicate["results"] = duplicate_rows
    live_duplicate["modes"][check_id] = alternate_mode
    add("live-same-id-mode-duplicate", encoded(live_duplicate), independent_drift_bytes, 1)

    # R2's side-channel opt-out: skew the independent target and leave only the
    # live row's positive mode as the adjudication input.
    live_optout = copy.deepcopy(test_live)
    next(r for r in live_optout["results"] if r.get("check") == check_id)["mode"] = "positive"
    for key in ("observed", "modes", "verdicts", "summary_paths"):
        live_optout.pop(key, None)
    add("live-summary-and-mirror-optout", encoded(live_optout), independent_drift_bytes, 1)

    # Raw duplicate JSON members on the independent side. Using a committed
    # scope file with a single derived row avoids unrelated scope-out probes.
    add("raw-duplicate-top-level-results", base_live_bytes,
        duplicate_top_level_results(test_independent), 1)
    add("raw-duplicate-record-rederived", base_live_bytes,
        duplicate_record_rederived(test_independent), 1)

    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    except (OSError, subprocess.SubprocessError):
        head = None
    result = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "label": args.label,
        "head": head,
        "repo": str(repo),
        "comparator": str(comparator),
        "comparator_sha256": sha(comparator.read_bytes()),
        "source_sha256": {"live": sha(live_bytes), "independent": sha(independent_bytes),
                          "scope": sha(scope_bytes)},
        "selected_live": {"check": check_id, "observed": observed, "independent_skew": skew,
                          "original_mode": original_mode, "shadow_mode": alternate_mode},
        "cases": cases,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
