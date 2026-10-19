#!/usr/bin/env python3
import copy
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
COMMIT = "6881ce31912cf52982de733d18d25e7ab7aae5c4"


def stamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_hash(path):
    return digest(Path(path).read_bytes())


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args]).decode().strip()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(command, cwd=ROOT):
    proc = subprocess.run(command, cwd=str(cwd), capture_output=True, text=True, timeout=300)
    return proc.returncode, proc.stdout, proc.stderr


def record_map(payload):
    rows = payload.get("results", payload.get("rows", payload.get("checks")))
    if not isinstance(rows, list):
        raise RuntimeError("independent producer did not publish a results/rows list")
    values = payload.get("checks")
    if not isinstance(values, dict):
        raise RuntimeError("independent producer did not publish its checks map")
    return rows, values


def main():
    replay = "--replay" in sys.argv[1:]
    start = stamp()
    if git("rev-parse", "HEAD") != COMMIT:
        raise RuntimeError("HEAD moved from the pinned C1 snapshot")

    comparator = OUT / "compare-head.py"
    scope = OUT / "scope-head.json"
    if not replay:
        comparator.write_bytes(subprocess.check_output(
            ["git", "-C", str(ROOT), "show", f"{COMMIT}:verifiers/compare_harness_independent.py"]
        ))
        scope.write_bytes(subprocess.check_output(
            ["git", "-C", str(ROOT), "show", f"{COMMIT}:verifiers/harness-independent-scope.json"]
        ))
        for name, command in (
            ("live-capture.json", [sys.executable, str(ROOT / "verifiers/verify_harness_claims.py"), "--json"]),
            ("independent-capture.json", [sys.executable, str(ROOT / "verifiers/verify_harness_independent.py"), "--json"]),
        ):
            code, stdout, stderr = run(command)
            (OUT / name).write_text(stdout, encoding="utf-8")
            (OUT / name.replace(".json", ".stderr.txt")).write_text(stderr, encoding="utf-8")
            if code != 0:
                raise RuntimeError(f"producer {command} exited {code}: {stderr[-500:]}")
    else:
        for path in (comparator, scope, OUT / "live-capture.json", OUT / "independent-capture.json"):
            if not path.is_file():
                raise RuntimeError(f"replay input missing: {path}")

    live_bytes = (OUT / "live-capture.json").read_bytes()
    ind_bytes = (OUT / "independent-capture.json").read_bytes()
    live = json.loads(live_bytes)
    independent = json.loads(ind_bytes)
    scope_doc = json.loads(scope.read_bytes())
    live_rows = live.get("results")
    if not isinstance(live_rows, list):
        raise RuntimeError("live producer did not publish results list")
    live_values = {row["check"]: row["observed"] for row in live_rows}
    rows, checks = record_map(independent)
    committed = set(scope_doc["scope_out"])
    if len(live_values) != 28:
        raise RuntimeError(f"expected the current 28-check live set, got {len(live_values)}")

    expected_only = copy.deepcopy(independent)
    copied_checks = {
        cid: (None if cid in committed else live_values[cid])
        for cid in checks
    }
    expected_only["checks"] = copy.deepcopy(copied_checks)
    for channel in ("results", "rows"):
        for row in expected_only.get(channel, []):
            cid = row.get("check", row.get("id", row.get("name")))
            value = copied_checks[cid]
            for key in ("expected_value", "re_derived", "value", "observed"):
                row.pop(key, None)
            row["expected"] = value

    cases = {}
    cases["honest-mixed-results-checks"] = copy.deepcopy(independent)
    cases["expected-only-results-checks"] = expected_only

    rows_under_expected = copy.deepcopy(expected_only)
    rows_under_expected["rows"] = rows_under_expected.pop("results")
    rows_under_expected.pop("checks", None)
    rows_under_expected["expected"] = copy.deepcopy(copied_checks)
    cases["rows-plus-expected-map"] = rows_under_expected

    scope_map_only = copy.deepcopy(expected_only)
    scoped_id = sorted(committed)[0]
    scope_map_only["checks"][scoped_id] = live_values[scoped_id]
    cases["scoped-out-value-only-in-checks-map"] = scope_map_only

    map_extra = copy.deepcopy(expected_only)
    for channel in ("results", "rows"):
        map_extra[channel] = [row for row in map_extra[channel]
                              if row.get("check", row.get("id", row.get("name"))) not in committed]
    cases["24-records-plus-28-checks-keys"] = map_extra

    nested = copy.deepcopy(expected_only)
    nested["rows"] = nested.pop("results")
    nested["checks"] = {"checks": copy.deepcopy(copied_checks)}
    cases["rows-plus-one-level-deep-checks-map"] = nested

    cases_dir = OUT / "arms"
    cases_dir.mkdir(exist_ok=True)
    for name, payload in cases.items():
        save_json(cases_dir / f"{name}.json", payload)

    run_records = []
    for name in cases:
        ind_path = cases_dir / f"{name}.json"
        argv = [
            sys.executable, str(comparator),
            "--live-json", str(OUT / "live-capture.json"),
            "--independent-json", str(ind_path),
            "--expect-n", "28",
            "--cwd", str(ROOT),
            "--scope-file", str(scope),
            "--no-stamp", "--json",
        ]
        code, stdout, stderr = run(argv)
        stdout_path = cases_dir / f"{name}.stdout.txt"
        stderr_path = cases_dir / f"{name}.stderr.txt"
        stdout_path.write_text(stdout, encoding="utf-8")
        stderr_path.write_text(stderr, encoding="utf-8")
        try:
            report = json.loads(stdout)
        except ValueError:
            report = None
        run_records.append({
            "name": name,
            "argv": argv,
            "exit": code,
            "independent_sha256": file_hash(ind_path),
            "stdout_sha256": file_hash(stdout_path),
            "stderr_sha256": file_hash(stderr_path),
            "headline": report.get("headline") if report else None,
            "agreement": report.get("agreement") if report else None,
            "reason": report.get("reason") if report else None,
            "stderr": stderr.strip(),
        })

    end = stamp()
    manifest = {
        "probe": "X1 record/map composition matrix",
        "started_at_utc": start,
        "finished_at_utc": end,
        "command": f"python3 {Path(__file__).resolve()}" + (" --replay" if replay else ""),
        "root": str(ROOT),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "worktree_status": git("status", "--short"),
        "comparison_mode": "git-show frozen comparator bytes at HEAD",
        "comparator_source": f"git show {COMMIT}:verifiers/compare_harness_independent.py",
        "comparator_sha256": file_hash(comparator),
        "scope_source": f"git show {COMMIT}:verifiers/harness-independent-scope.json",
        "scope_sha256": file_hash(scope),
        "producer_commands": {
            "live": f"python3 verifiers/verify_harness_claims.py --json (cwd {ROOT})",
            "independent": f"python3 verifiers/verify_harness_independent.py --json (cwd {ROOT})",
        },
        "producer_sha256": {
            "live": file_hash(ROOT / "verifiers/verify_harness_claims.py"),
            "independent": file_hash(ROOT / "verifiers/verify_harness_independent.py"),
        },
        "captures": {
            "live": {"path": str(OUT / "live-capture.json"), "bytes": len(live_bytes), "sha256": digest(live_bytes), "checks": len(live_values)},
            "independent": {"path": str(OUT / "independent-capture.json"), "bytes": len(ind_bytes), "sha256": digest(ind_bytes), "records": len(rows), "check_keys": len(checks)},
        },
        "scope_out_ids": sorted(committed),
        "cases": run_records,
    }
    save_json(OUT / "probe-results.json", manifest)
    print(json.dumps({
        "started_at_utc": start,
        "finished_at_utc": end,
        "head": manifest["head"],
        "tree": manifest["tree"],
        "comparator_sha256": manifest["comparator_sha256"],
        "scope_sha256": manifest["scope_sha256"],
        "live_capture_sha256": digest(live_bytes),
        "independent_capture_sha256": digest(ind_bytes),
        "cases": [{"name": item["name"], "exit": item["exit"], "headline": item["headline"], "agreement": item["agreement"], "reason": item["reason"], "stderr": item["stderr"]} for item in run_records],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
