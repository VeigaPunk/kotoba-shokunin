#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
ROOT = DRAFT.parents[3]
EVIDENCE = ROOT / ".ufo/round-45/evidence/h11"
HELPER = ROOT / ".ufo/round-41/evidence/v10-census-probes.py"
CENSUS = ROOT / ".ufo/round-41/evidence/v10-channel-census.py"
BASELINE_CENSUS = ROOT / ".ufo/round-41/evidence/v10-channel-census.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
DISPATCH_DRAFT = DRAFT / "compare-r44-dispatch-6881ce3.py"
LANDED_DRAFT = DRAFT / "compare-landed-032f47b.py"
DISPATCH = EVIDENCE / DISPATCH_DRAFT.name
LANDED = EVIDENCE / LANDED_DRAFT.name
EXPECTED_DISPATCH_SHA = "d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d"
EXPECTED_LANDED_SHA = "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56"
TARGET_ID = "omp.offered.skills"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def git_show(ref):
    return subprocess.run(["git", "-C", str(ROOT), "show", ref],
                          capture_output=True, check=True).stdout


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def promote(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    if sha_file(source) != sha_file(destination):
        raise RuntimeError(f"promotion hash mismatch: {source} -> {destination}")
    return destination


def under(path, root):
    try:
        return Path(path).resolve().relative_to(root.resolve())
    except ValueError:
        return None


def run_producer(script, label):
    proc = subprocess.run([sys.executable, str(ROOT / script), "--json"],
                          cwd=ROOT, capture_output=True, text=True, timeout=300,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if proc.returncode:
        raise RuntimeError(f"{label} producer exited {proc.returncode}: {proc.stderr[-1000:]}")
    return proc.stdout.encode("utf-8"), proc


def parse_output(proc):
    try:
        payload = json.loads(proc.stdout)
        return payload.get("headline"), payload.get("reason", ""), payload
    except (ValueError, TypeError):
        return None, (proc.stderr or proc.stdout).strip()[-1200:], None


def run_comparison(driver, live_path, independent_path, expect_n, scope_arg,
                   process_cwd, receipt_path=None):
    command = [
        sys.executable, str(driver),
        "--live-json", str(live_path),
        "--independent-json", str(independent_path),
        "--expect-n", str(expect_n),
        "--cwd", str(ROOT),
        "--scope-file", str(scope_arg),
        "--no-stamp", "--json",
    ]
    if receipt_path:
        command += ["--receipt", str(receipt_path)]
    scope_path = Path(scope_arg)
    if not scope_path.is_absolute():
        scope_path = Path(process_cwd) / scope_path
    before = {
        "live_json": sha_file(live_path),
        "independent_json": sha_file(independent_path),
        "scope_file": sha_file(scope_path),
    }
    proc = subprocess.run(command, cwd=process_cwd, capture_output=True,
                          text=True, timeout=300,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    after = {
        "live_json": sha_file(live_path),
        "independent_json": sha_file(independent_path),
        "scope_file": sha_file(scope_path),
    }
    headline, reason, payload = parse_output(proc)
    return {
        "command": command,
        "process_cwd": str(process_cwd),
        "exit": proc.returncode,
        "headline": headline,
        "reason": reason,
        "stderr_tail": proc.stderr[-1000:],
        "input_sha256_before": before,
        "input_sha256_after": after,
        "input_hashes_unchanged": before == after,
        "output_payload": payload,
    }


def main():
    started = datetime.now(timezone.utc).isoformat()
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    for source, destination, expected in (
        (DISPATCH_DRAFT, DISPATCH, EXPECTED_DISPATCH_SHA),
        (LANDED_DRAFT, LANDED, EXPECTED_LANDED_SHA),
    ):
        if sha_file(source) != expected:
            raise RuntimeError(f"unexpected frozen comparator bytes: {source}")
        promote(source, destination)

    head_before = git("rev-parse", "HEAD")
    tree_before = git("rev-parse", "HEAD^{tree}")
    dirty_comparator_before = sha_file(ROOT / "verifiers/compare_harness_independent.py")
    source_pins = {
        "head": head_before,
        "tree": tree_before,
        "dispatch_commit": git("rev-parse", "6881ce3"),
        "dispatch_tree": git("rev-parse", "6881ce3^{tree}"),
        "landed_commit": git("rev-parse", "032f47b"),
        "landed_tree": git("rev-parse", "032f47b^{tree}"),
        "dispatch_comparator_sha256": sha_file(DISPATCH),
        "landed_comparator_sha256": sha_file(LANDED),
        "working_tree_comparator_sha256_before": dirty_comparator_before,
        "scope_sha256": sha_file(SCOPE),
        "independent_instrument_sha256": sha_file(ROOT / "verifiers/verify_harness_independent.py"),
        "live_instrument_sha256": sha_file(ROOT / "verifiers/verify_harness_claims.py"),
        "census_generator_sha256": sha_file(HELPER),
        "census_taxonomy_sha256": sha_file(CENSUS),
        "r41_baseline_census_sha256": sha_file(BASELINE_CENSUS),
    }

    live_bytes, live_proc = run_producer("verifiers/verify_harness_claims.py", "live")
    independent_bytes, independent_proc = run_producer(
        "verifiers/verify_harness_independent.py", "independent")
    live_draft = DRAFT / "live-current.json"
    independent_draft = DRAFT / "independent-current.json"
    live_draft.write_bytes(live_bytes)
    independent_draft.write_bytes(independent_bytes)
    live_path = promote(live_draft, EVIDENCE / live_draft.name)
    independent_path = promote(independent_draft, EVIDENCE / independent_draft.name)
    live = json.loads(live_bytes)
    independent = json.loads(independent_bytes)

    helper = load_module(HELPER, "kotoba_r41_v10_h11_helper")
    helper.DRAFT = DRAFT
    helper.ROOT = ROOT
    helper.DRIVER = LANDED
    helper.LIVE_FILE = live_draft
    helper.IND_FILE = independent_draft
    helper.CARRIER = DRAFT / "builder-carrier"
    helper.CARRIER.mkdir(parents=True, exist_ok=True)
    for index, (name, stamp, entries) in enumerate((
        ("a.jsonl", "2026-01-01T00:00:00.000Z", 2),
        ("b.jsonl", "2026-02-02T00:00:00.000Z", 5),
    )):
        rows = "\\n".join("- entry %d" % i for i in range(entries))
        (helper.CARRIER / name).write_text(
            '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' % (stamp, rows),
            encoding="utf-8")
        os.utime(helper.CARRIER / name, (1700000000 + index * 1000,
                                         1700000000 + index * 1000))
    driver = helper.load_driver()
    census = load_module(CENSUS, "kotoba_r41_v10_h11_census")
    base_census = json.loads(BASELINE_CENSUS.read_text(encoding="utf-8"))
    baseline_ids = {row["id"] for row in base_census["arms"]}

    case_map = helper.arms(driver, live, independent)
    if set(case_map) != set(census.CASES) or set(case_map) != baseline_ids or len(case_map) != 46:
        raise RuntimeError(
            f"R41 arm set mismatch: generated={len(case_map)}, census={len(census.CASES)}, "
            f"baseline={len(baseline_ids)}")

    planted_draft = DRAFT / "planted-cwd"
    planted_evidence = EVIDENCE / "planted-cwd"
    if planted_draft.exists():
        for path in sorted(planted_draft.rglob("*")):
            if path.is_file():
                promote(path, planted_evidence / path.relative_to(planted_draft))

    arm_results = {}
    for name, case in sorted(case_map.items()):
        independent_draft_path = DRAFT / f"arm-{name}.json"
        write_json(independent_draft_path, case["payload"])
        independent_path_arm = promote(
            independent_draft_path, EVIDENCE / "census-inputs" / independent_draft_path.name)
        live_payload = case.get("live_payload")
        if live_payload is None:
            live_path_arm = live_path
        else:
            live_draft_path = DRAFT / f"live-arm-{name}.json"
            write_json(live_draft_path, live_payload)
            live_path_arm = promote(
                live_draft_path, EVIDENCE / "census-inputs" / live_draft_path.name)

        scope_case = case.get("scope")
        if scope_case:
            scope_arg = str(scope_case)
            scope_abs = Path(scope_arg)
            if scope_abs.is_absolute():
                rel = under(scope_abs, DRAFT)
                if rel is not None:
                    scope_arg = str(EVIDENCE / rel)
        else:
            scope_arg = str(SCOPE)

        process_cwd = case.get("process_cwd") or ROOT
        process_cwd = Path(process_cwd)
        cwd_rel = under(process_cwd, DRAFT)
        if cwd_rel is not None:
            process_cwd = EVIDENCE / cwd_rel
        receipt = case.get("receipt")
        if receipt:
            receipt = Path(receipt)
            receipt_rel = under(receipt, DRAFT)
            if receipt_rel is not None:
                receipt = EVIDENCE / receipt_rel

        run = run_comparison(
            LANDED, live_path_arm, independent_path_arm, 28, scope_arg,
            process_cwd, receipt_path=receipt)
        origin_class, channel, finding = census.CASES[name]
        if origin_class == "open":
            observed_class = "still-open" if run["exit"] == 0 else "closed-on-landed"
        elif origin_class == "closed":
            observed_class = "closed" if run["exit"] != 0 else "unexpected-green"
        else:
            observed_class = origin_class
        arm_results[name] = {
            "r41_baseline_class": origin_class,
            "channel": channel,
            "baseline_finding": finding,
            "landed_class": observed_class,
            "exit": run["exit"],
            "headline": run["headline"],
            "reason": run["reason"],
            "stderr_tail": run["stderr_tail"],
            "command": run["command"],
            "process_cwd": run["process_cwd"],
            "scope_file_arg": scope_arg,
            "live_input_sha256": sha_file(live_path_arm),
            "independent_input_sha256": sha_file(independent_path_arm),
            "input_sha256_before": run["input_sha256_before"],
            "input_sha256_after": run["input_sha256_after"],
            "input_hashes_unchanged": run["input_hashes_unchanged"],
        }
        print(f"census {name:48s} exit={run['exit']} {observed_class}: {run['reason'][:120]}")

    scope_doc = json.loads(SCOPE.read_text(encoding="utf-8"))
    scoped_ids = set(scope_doc["scope_out"])
    live_rows = [r for r in live["results"] if r["check"] not in scoped_ids]
    if len(live_rows) != 24:
        raise RuntimeError(f"targeted dotted-map harness expected 24 rows, got {len(live_rows)}")
    target_live_draft = DRAFT / "target-live-24.json"
    write_json(target_live_draft, {"results": live_rows})
    target_live = promote(target_live_draft, EVIDENCE / target_live_draft.name)
    check_map = {r["check"]: r["observed"] for r in live_rows}
    if TARGET_ID not in check_map:
        raise RuntimeError(f"target id absent from in-scope live set: {TARGET_ID}")
    drift_map = copy.deepcopy(check_map)
    drift_map[TARGET_ID] = 999
    target_inputs = {
        "bare-map-control": check_map,
        "bare-map-contradiction": drift_map,
        "checks-plus-nested-expected-conflict": {
            "checks": check_map,
            "expected": drift_map,
        },
        "checks-plus-flat-top-level-map-conflict": {
            **check_map,
            "checks": check_map,
        },
    }
    target_inputs["checks-plus-flat-top-level-map-conflict"][TARGET_ID] = 999
    target_input_paths = {}
    for name, payload in target_inputs.items():
        draft_path = DRAFT / f"target-{name}.json"
        write_json(draft_path, payload)
        target_input_paths[name] = promote(draft_path, EVIDENCE / "target-inputs" / draft_path.name)

    target_results = {}
    for version, comparator in (("r44-dispatch-6881ce3", DISPATCH),
                                ("landed-032f47b-13b6d791", LANDED)):
        for name, ind_path in target_input_paths.items():
            run = run_comparison(comparator, target_live, ind_path, 24, str(SCOPE), ROOT)
            target_results[f"{version}/{name}"] = {
                "comparator_sha256": sha_file(comparator),
                "live_input_sha256": sha_file(target_live),
                "independent_input_sha256": sha_file(ind_path),
                "exit": run["exit"],
                "headline": run["headline"],
                "reason": run["reason"],
                "stderr_tail": run["stderr_tail"],
                "command": run["command"],
                "process_cwd": run["process_cwd"],
                "input_sha256_before": run["input_sha256_before"],
                "input_sha256_after": run["input_sha256_after"],
                "input_hashes_unchanged": run["input_hashes_unchanged"],
            }
            print(f"hunt {version}/{name}: exit={run['exit']} {run['reason'][:180]}")

    counts = {}
    for result in arm_results.values():
        key = result["landed_class"]
        counts[key] = counts.get(key, 0) + 1
    still_open = sorted(name for name, result in arm_results.items()
                        if result["landed_class"] == "still-open")
    unexpected_green = sorted(name for name, result in arm_results.items()
                              if result["landed_class"] == "unexpected-green")
    live_records = len(live["results"])
    independent_records = len(independent.get("results", []))
    ended = datetime.now(timezone.utc).isoformat()
    current_worktree_comparator_after = sha_file(ROOT / "verifiers/compare_harness_independent.py")
    pins_after = {
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "working_tree_comparator_sha256_after": current_worktree_comparator_after,
        "scope_sha256_after": sha_file(SCOPE),
        "independent_instrument_sha256_after": sha_file(ROOT / "verifiers/verify_harness_independent.py"),
        "live_instrument_sha256_after": sha_file(ROOT / "verifiers/verify_harness_claims.py"),
    }
    census_report = {
        "schema": "kotoba.round45.h11.r41-census-replay.v1",
        "started_at_utc": started,
        "finished_at_utc": ended,
        "tree_state_before": source_pins,
        "tree_state_after": pins_after,
        "producer_capture": {
            "live_command": f"python3 verifiers/verify_harness_claims.py --json",
            "live_exit": live_proc.returncode,
            "live_sha256": sha_bytes(live_bytes),
            "live_results_n": live_records,
            "independent_command": f"python3 verifiers/verify_harness_independent.py --json",
            "independent_exit": independent_proc.returncode,
            "independent_sha256": sha_bytes(independent_bytes),
            "independent_results_n": independent_records,
        },
        "baseline": {
            "source_path": str(BASELINE_CENSUS.relative_to(ROOT)),
            "source_sha256": sha_file(BASELINE_CENSUS),
            "arm_count": len(base_census["arms"]),
            "open_count": base_census["summary"]["classification_counts"]["open"],
            "open_ids": sorted(row["id"] for row in base_census["arms"]
                                if row["classification"] == "open"),
        },
        "landed_summary": {
            "arm_count": len(arm_results),
            "classification_counts": dict(sorted(counts.items())),
            "still_open_count": len(still_open),
            "still_open_ids": still_open,
            "unexpected_green_count": len(unexpected_green),
            "unexpected_green_ids": unexpected_green,
            "all_input_hashes_unchanged": all(r["input_hashes_unchanged"]
                                               for r in arm_results.values()),
            "arm_set_matches_r41_baseline": set(arm_results) == baseline_ids,
        },
        "arms": arm_results,
    }
    write_json(EVIDENCE / "census-replay-13b6d791.json", census_report)

    hunt_report = {
        "schema": "kotoba.round45.h11.dotted-map-hunt.v1",
        "started_at_utc": started,
        "finished_at_utc": ended,
        "tree_state": source_pins,
        "target": TARGET_ID,
        "target_value_observed": check_map[TARGET_ID],
        "live_24_sha256": sha_file(target_live),
        "test_definitions": {
            "bare-map-control": "24-key top-level dotted map is the whole independent payload; values match the in-scope live rows",
            "bare-map-contradiction": "same bare map with " + TARGET_ID + " changed to 999; must be a comparison disagreement, not a shadow pass",
            "checks-plus-nested-expected-conflict": "checks map matches live, nested expected map changes " + TARGET_ID + " to 999",
            "checks-plus-flat-top-level-map-conflict": "checks map matches live, flat dotted top-level " + TARGET_ID + " is 999",
        },
        "scope": "24 in-scope live rows; the four committed scope-outs are excluded from this isolated shape test, so no map-shape result is confounded by scope-out handling",
        "results": target_results,
    }
    write_json(EVIDENCE / "dotted-map-hunt.json", hunt_report)

    for name, path in (
        ("replay_h11.py", Path(__file__).resolve()),
        ("census-generator-v10.py", HELPER),
        ("census-taxonomy-v10.py", CENSUS),
    ):
        promote(path, EVIDENCE / name)

    print(f"census-replay: {len(arm_results)}/46; classes={dict(sorted(counts.items()))}; "
          f"still_open={len(still_open)}; unexpected_green={len(unexpected_green)}")
    print(f"evidence: {EVIDENCE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
