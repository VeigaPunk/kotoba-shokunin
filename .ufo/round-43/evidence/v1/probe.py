#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
CASES = DRAFT / "cases"
FROZEN_REV = "b1be35f9522f21c0c5b39879358a011806ab9200"
DRIVER_REL = "verifiers/compare_harness_independent.py"
SCOPE_REL = "verifiers/harness-independent-scope.json"
CENSUS_REL = ".ufo/round-41/evidence/v10-channel-census.json"
HELDOUT = (
    "heldout-expected-only-full-copy",
    "heldout-flat-dotted-map",
    "heldout-nested-checks-map",
    "heldout-nested-expected-wrapper",
    "heldout-nested-observations-wrapper",
    "heldout-wrapper-precedence-expected-over-observations",
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(argv, cwd=ROOT, timeout=300):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout)


def git_text(*args):
    return run(["git", *args], timeout=60).stdout.strip()


def record_map(payload, key):
    return {r["check"]: r for r in payload[key]}


def make_cases(live, independent, scope_ids):
    live_values = {r["check"]: r["observed"] for r in live["results"]}
    ind_values = {r["check"]: r.get("value", r.get("re_derived"))
                  for r in independent["results"]}
    scored = {r["check"] for r in independent["results"]
              if r.get("status") != "SCOPED_OUT"}

    expected_only = copy.deepcopy(independent)
    for cid in scored:
        for channel in ("results", "rows"):
            record = record_map(expected_only, channel)[cid]
            for key in ("expected_value", "re_derived", "value", "observed"):
                record.pop(key, None)
            record["expected"] = live_values[cid]
        expected_only["checks"][cid] = live_values[cid]

    cases = {
        "honest": copy.deepcopy(independent),
        "heldout-expected-only-full-copy": expected_only,
        "heldout-flat-dotted-map": dict(live_values),
        "heldout-nested-checks-map": {"checks": dict(live_values)},
        "heldout-nested-expected-wrapper": {"expected": dict(live_values)},
        "heldout-nested-observations-wrapper": {"observations": dict(live_values)},
        "heldout-wrapper-precedence-expected-over-observations": {
            "expected": dict(live_values),
            "observations": {cid: 999 for cid in live_values},
        },
    }

    target = "omp.catalogue.found"
    if target not in scope_ids:
        raise RuntimeError("chosen scoped-out id is absent from committed scope")
    scoped_value = dict(live_values)
    exact_other = sum(scoped_value[cid] == value
                      for cid, value in live_values.items() if cid != target)
    if len(live_values) != 28 or len(scoped_value) != 28 or exact_other != 27:
        raise RuntimeError("own map did not carry 27 unchanged live values + 1 scoped-out value")
    cases["own-map-27-live-values-plus-scoped-out-value"] = scoped_value
    cases["own-map-extra-unknown-id"] = {**live_values, "attacker.extra": 999}
    cases["own-wrapper-expected-observations-conflict"] = {
        "expected": dict(scoped_value),
        "observations": {**scoped_value, target: False},
    }
    return cases, live_values, ind_values, scored, target


def failure_class(reason, stderr):
    text = stderr or reason or ""
    for name in ("derived-set overflow", "competing value-map aliases", "unknown checks"):
        if name in text:
            return name
    return None


def invoke(driver, live_path, independent_path, driver_sha):
    argv = [
        sys.executable, str(driver),
        "--live-json", str(live_path),
        "--independent-json", str(independent_path),
        "--cwd", str(ROOT), "--scope-file", str(ROOT / SCOPE_REL),
        "--expect-n", "28", "--no-stamp", "--json",
    ]
    proc = run(argv, timeout=300)
    try:
        report = json.loads(proc.stdout)
    except ValueError:
        report = None
    headline = report.get("headline", {}) if report else {}
    reason = report.get("reason") if report else None
    stderr_tail = proc.stderr[-1200:]
    return {
        "command": argv,
        "driver_sha256": driver_sha,
        "live_input_sha256": sha(live_path.read_bytes()),
        "independent_input_sha256": sha(independent_path.read_bytes()),
        "stdout_sha256": sha(proc.stdout.encode("utf-8")),
        "exit": proc.returncode,
        "headline": headline,
        "agreement": report.get("agreement", {}) if report else {},
        "reason": reason,
        "failure_class": failure_class(reason, stderr_tail),
        "stderr_tail": stderr_tail,
    }


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    CASES.mkdir(parents=True, exist_ok=True)
    start = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    head, tree = git_text("rev-parse", "HEAD"), git_text("rev-parse", "HEAD^{tree}")
    frozen_bytes = run(["git", "show", f"{FROZEN_REV}:{DRIVER_REL}"], timeout=60).stdout.encode()
    frozen_path = DRAFT / "compare-b1be35f.py"
    frozen_path.write_bytes(frozen_bytes)
    current_path = ROOT / DRIVER_REL
    current_bytes = current_path.read_bytes()
    current_path_snapshot = DRAFT / "compare-current-snapshot.py"
    current_path_snapshot.write_bytes(current_bytes)

    census_path = ROOT / CENSUS_REL
    census_bytes = census_path.read_bytes()
    census = json.loads(census_bytes)
    scope_path = ROOT / SCOPE_REL
    scope_bytes = scope_path.read_bytes()
    scope = json.loads(scope_bytes)
    scope_ids = set(scope["scope_out"])

    producer_cmds = {
        "live": [sys.executable, "verifiers/verify_harness_claims.py", "--json"],
        "independent": [sys.executable, "verifiers/verify_harness_independent.py", "--json"],
    }
    captures = {}
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(run, cmd): name for name, cmd in producer_cmds.items()}
        for future in as_completed(futures):
            name = futures[future]
            proc = future.result()
            if proc.returncode != 0:
                raise RuntimeError(f"{name} producer exit {proc.returncode}: {proc.stderr[-800:]}")
            captures[name] = proc
    live_path = DRAFT / "live-current.json"
    ind_path = DRAFT / "independent-current.json"
    live_path.write_text(captures["live"].stdout, encoding="utf-8")
    ind_path.write_text(captures["independent"].stdout, encoding="utf-8")
    live, independent = json.loads(captures["live"].stdout), json.loads(captures["independent"].stdout)
    cases, live_values, ind_values, scored, scoped_target = make_cases(live, independent, scope_ids)
    if len(live_values) != 28 or len(ind_values) != 28 or scored != set(live_values) - scope_ids:
        raise RuntimeError("fresh producers did not reproduce the 28/24/4 shape")

    payload_paths = {}
    for name, payload in cases.items():
        path = CASES / f"{name}.json"
        path.write_text(json.dumps(payload, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        payload_paths[name] = path

    drivers = {
        "before_frozen_b1be35f": (frozen_path, sha(frozen_bytes)),
        "after_current_snapshot": (current_path_snapshot, sha(current_bytes)),
    }
    jobs = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for name, path in payload_paths.items():
            for version, (driver, driver_sha) in drivers.items():
                jobs[(name, version)] = pool.submit(invoke, driver, live_path, path, driver_sha)
        results = {key: future.result() for key, future in jobs.items()}

    historical_arms = {item["id"]: item for item in census.get("arms", [])}
    historical = {}
    for name in HELDOUT:
        item = historical_arms.get(name, {})
        historical[name] = {
            "classification": item.get("classification"),
            "exit": item.get("actual", {}).get("exit"),
            "headline": item.get("actual", {}).get("headline"),
            "input_sha256": item.get("input_sha256_before"),
        }

    current_after = current_path.read_bytes()
    report = {
        "schema": "kotoba.round43.v1-c1-heldout-map-verification.v1",
        "measured_at_utc": start,
        "head": head,
        "head_tree": tree,
        "worktree_status_at_capture": git_text("status", "--short", "--untracked-files=all").splitlines(),
        "frozen": {
            "revision": FROZEN_REV,
            "tree": "8bb24450a9c500c427019c7147013b4946525b09",
            "git_show_command": ["git", "show", f"{FROZEN_REV}:{DRIVER_REL}"],
            "sha256": sha(frozen_bytes),
            "bytes": len(frozen_bytes),
        },
        "current_snapshot": {
            "source_path": DRIVER_REL,
            "sha256_at_capture": sha(current_bytes),
            "bytes": len(current_bytes),
            "sha256_after_probe": sha(current_after),
            "stable_during_probe": sha(current_after) == sha(current_bytes),
            "snapshot_path": str(current_path_snapshot),
        },
        "scope": {"path": SCOPE_REL, "sha256": sha(scope_bytes), "scope_out_ids": sorted(scope_ids)},
        "historical_census": {
            "path": CENSUS_REL,
            "sha256": sha(census_bytes),
            "source_replay_sha256": census.get("source", {}).get("sha256"),
            "source_head": census.get("source", {}).get("frozen_head"),
            "source_tree": census.get("source", {}).get("frozen_tree"),
            "source_comparator_sha256": census.get("source", {}).get("comparator_sha256"),
            "heldout_arms": historical,
        },
        "producers": {
            name: {
                "command": producer_cmds[name],
                "exit": captures[name].returncode,
                "stdout_sha256": sha(captures[name].stdout.encode("utf-8")),
                "file_sha256": sha((live_path if name == "live" else ind_path).read_bytes()),
                "records": len(json.loads(captures[name].stdout).get("results", [])),
            }
            for name in producer_cmds
        },
        "own_27_plus_1_definition": {
            "scope_out_id": scoped_target,
            "total_ids": len(cases["own-map-27-live-values-plus-scoped-out-value"]),
            "other_values_matching_live_observations": 27,
            "scoped_out_value_source": "current live producer observed value for the named SCOPED_OUT id",
        },
        "cases": {
            name: {
                "payload_path": str(path),
                "payload_sha256": sha(path.read_bytes()),
                "before_frozen_b1be35f": results[(name, "before_frozen_b1be35f")],
                "after_current_snapshot": results[(name, "after_current_snapshot")],
            }
            for name, path in payload_paths.items()
        },
    }

    def check(label, value, details):
        return {"label": label, "pass": bool(value), "details": details}

    closure = [check("honest input remains 24/24 exit 0 on frozen bytes",
                     results[("honest", "before_frozen_b1be35f")]["exit"] == 0 and
                     results[("honest", "before_frozen_b1be35f")]["headline"].get("n") == 24 and
                     results[("honest", "before_frozen_b1be35f")]["headline"].get("total") == 24,
                     results[("honest", "before_frozen_b1be35f")]),
               check("honest input remains 24/24 exit 0 on current snapshot",
                     results[("honest", "after_current_snapshot")]["exit"] == 0 and
                     results[("honest", "after_current_snapshot")]["headline"].get("n") == 24 and
                     results[("honest", "after_current_snapshot")]["headline"].get("total") == 24,
                     results[("honest", "after_current_snapshot")])]
    for name in HELDOUT:
        actual = results[(name, "after_current_snapshot")]
        closure.append(check(f"{name} fails closed, class-named, exit 2",
                             actual["exit"] == 2 and bool(actual["failure_class"]), actual))
    for name in ("own-map-27-live-values-plus-scoped-out-value",
                 "own-map-extra-unknown-id", "own-wrapper-expected-observations-conflict"):
        actual = results[(name, "after_current_snapshot")]
        closure.append(check(f"{name} fails closed, class-named, exit 2",
                             actual["exit"] == 2 and bool(actual["failure_class"]), actual))
    report["closure_assertions"] = closure
    report["closure_green"] = all(item["pass"] for item in closure)
    output = DRAFT / "probe-results.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for name in cases:
        before = results[(name, "before_frozen_b1be35f")]
        after = results[(name, "after_current_snapshot")]
        bh, ah = before["headline"], after["headline"]
        print(f"{name}: frozen={before['exit']} {bh.get('n')}/{bh.get('total')} "
              f"({before['reason']}); current={after['exit']} {ah.get('n')}/{ah.get('total')} "
              f"({after['reason'] or after['stderr_tail']})")
    print(f"HEAD={head} TREE={tree} captured={start}")
    print(f"FROZEN_SHA256={sha(frozen_bytes)} CURRENT_SHA256={sha(current_bytes)} "
          f"CURRENT_STABLE={report['current_snapshot']['stable_during_probe']} "
          f"SCOPE_SHA256={sha(scope_bytes)}")
    print(f"CENSUS_SHA256={sha(census_bytes)} LIVE_SHA256={sha(live_path.read_bytes())} "
          f"INDEPENDENT_SHA256={sha(ind_path.read_bytes())}")
    print(f"RESULT={output} SHA256={sha(output.read_bytes())} "
          f"CLOSURE_GREEN={report['closure_green']}")
    return 0 if report["closure_green"] else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError) as exc:
        print(f"v1-probe: ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
