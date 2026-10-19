#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
EVIDENCE = ROOT / ".ufo/round-41/evidence"
COMPARATOR = DRAFT / "compare-032f47b.py"
PRE_COMPARATOR = DRAFT / "compare-6881ce3.py"
LIVE_FILE = DRAFT / "live-current.json"
IND_FILE = DRAFT / "independent-current.json"
RESULTS = DRAFT / "heldout-replay.json"
SCOPE_REL = "verifiers/harness-independent-scope.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_capture(path, command):
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                            timeout=300)
    if result.returncode:
        raise RuntimeError("%s failed (%d): %s" %
                           (command[1], result.returncode, result.stderr[-1000:]))
    path.write_text(result.stdout, encoding="utf-8")
    json.loads(result.stdout)
    return sha(path)


def main():
    started = datetime.now(timezone.utc).isoformat()
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    worktree_comparator_sha = sha(ROOT / "verifiers/compare_harness_independent.py")
    landed_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "032f47b:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    COMPARATOR.write_bytes(landed_bytes)
    landed_blob_sha = hashlib.sha256(landed_bytes).hexdigest()
    landed_sha = sha(COMPARATOR)
    dispatch_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "6881ce3:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    PRE_COMPARATOR.write_bytes(dispatch_bytes)
    pre_sha = sha(PRE_COMPARATOR)
    if landed_sha != landed_blob_sha:
        raise RuntimeError("frozen comparator copy differs from landed 032f47b blob")

    source_hashes = {
        path.name: sha(path) for path in (
            EVIDENCE / "v10-census-probes.py",
            EVIDENCE / "v10-channel-census.py",
            EVIDENCE / "v10-probe-results.json",
            EVIDENCE / "v10-subprocess-replay.json",
            EVIDENCE / "v10-channel-census.json",
            ROOT / "corpus/knowledge/harness-independent-round41-census.md",
            ROOT / "verifiers/harness-independent-scope.json",
            ROOT / "verifiers/verify_harness_claims.py",
            ROOT / "verifiers/verify_harness_independent.py",
        )
    }
    legacy_probe = load_module("v10_probe_r45", EVIDENCE / "v10-census-probes.py")
    census = load_module("v10_census_r45", EVIDENCE / "v10-channel-census.py")
    historic = json.loads((EVIDENCE / "v10-channel-census.json").read_text())
    old_replay = json.loads((EVIDENCE / "v10-subprocess-replay.json").read_text())
    historic_arms = {item["id"]: item for item in historic["arms"]}
    old_outcomes = {item["id"]: item for item in old_replay["arms"]}

    legacy_probe.ROOT = ROOT
    legacy_probe.DRAFT = DRAFT
    legacy_probe.DRIVER = COMPARATOR
    legacy_probe.LIVE_FILE = LIVE_FILE
    legacy_probe.IND_FILE = IND_FILE
    legacy_probe.CARRIER = DRAFT / "builder-carrier"
    driver = legacy_probe.load_driver()
    legacy_probe.CARRIER.mkdir(parents=True, exist_ok=True)
    for name, stamp, entries in (("a.jsonl", "2026-01-01T00:00:00.000Z", 2),
                                 ("b.jsonl", "2026-02-02T00:00:00.000Z", 5)):
        rows = "\\n".join("- entry %d" % index for index in range(entries))
        carrier = legacy_probe.CARRIER / name
        carrier.write_text('{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' %
                           (stamp, rows), encoding="utf-8")
        os.utime(carrier, (1700000000 if name == "a.jsonl" else 1700001000,) * 2)

    live_sha = run_capture(LIVE_FILE, [sys.executable, "-B",
        str(ROOT / "verifiers/verify_harness_claims.py"), "--json"])
    independent_sha = run_capture(IND_FILE, [sys.executable, "-B",
        str(ROOT / "verifiers/verify_harness_independent.py"), "--json"])
    live = json.loads(LIVE_FILE.read_text())
    independent = json.loads(IND_FILE.read_text())
    cases = legacy_probe.arms(driver, live, independent)
    expected_ids = set(census.CASES)
    if set(cases) != expected_ids or len(cases) != 46:
        raise RuntimeError("r41 arm set mismatch: generated=%d missing=%s extra=%s" %
                           (len(cases), sorted(expected_ids - set(cases)),
                            sorted(set(cases) - expected_ids)))
    if set(historic_arms) != expected_ids or set(old_outcomes) != expected_ids:
        raise RuntimeError("archived r41 census/replay ID sets do not match generator")

    inputs = {}
    for name, case in sorted(cases.items()):
        live_path = LIVE_FILE
        if case.get("live_payload") is not None:
            live_path = DRAFT / ("live-arm-" + name + ".json")
            live_path.write_text(json.dumps(case["live_payload"], indent=1,
                                            sort_keys=True) + "\n")
        ind_path = DRAFT / ("arm-" + name + ".json")
        ind_path.write_text(json.dumps(case["payload"], indent=1,
                                       sort_keys=True) + "\n")
        process_cwd = Path(case["process_cwd"] or ROOT)
        scope_arg = case["scope"] or str(ROOT / SCOPE_REL)
        scope_path = Path(scope_arg)
        if not scope_path.is_absolute():
            scope_path = process_cwd / scope_path
        inputs[name] = {
            "live": live_path,
            "independent": ind_path,
            "scope": scope_path,
            "cwd": process_cwd,
            "receipt": case["receipt"],
        }

    stages = (("r44-dispatch-6881ce3", PRE_COMPARATOR, pre_sha),
              ("landed-032f47b", COMPARATOR, landed_sha))
    replay = {stage: {} for stage, _, _ in stages}
    for stage, comparator, comparator_sha in stages:
        for name, case in sorted(cases.items()):
            files = inputs[name]
            live_path, ind_path, scope_path = files["live"], files["independent"], files["scope"]
            before = {"comparator": sha(comparator), "live": sha(live_path),
                      "independent": sha(ind_path), "scope": sha(scope_path)}
            command = [sys.executable, "-B", str(comparator),
                       "--live-json", str(live_path),
                       "--independent-json", str(ind_path),
                       "--cwd", str(ROOT), "--scope-file", str(case["scope"] or ROOT / SCOPE_REL),
                       "--no-stamp", "--json"]
            if files["receipt"]:
                receipt_path = DRAFT / (stage + "-cwd-receipt.json")
                command += ["--receipt", str(receipt_path)]
            process = subprocess.run(command, cwd=files["cwd"], text=True,
                                     capture_output=True, timeout=90)
            try:
                response = json.loads(process.stdout)
                headline = response.get("headline")
                reason = response.get("reason", "")
            except (ValueError, TypeError):
                headline = None
                reason = (process.stderr or process.stdout).strip()[-1200:]
            after = {"comparator": sha(comparator), "live": sha(live_path),
                     "independent": sha(ind_path), "scope": sha(scope_path)}
            if before != after:
                raise RuntimeError("input/source changed during %s/%s" % (stage, name))
            previous_class = historic_arms[name]["classification"]
            nonadversarial = {"control", "trust-input", "diagnostic"}
            current_class = ("open" if process.returncode == 0 and
                             previous_class not in nonadversarial else
                             previous_class if previous_class in nonadversarial else "closed")
            replay[stage][name] = {
                "r41_classification": previous_class,
                "r41_exit": old_outcomes[name]["actual"]["exit"],
                "classification": current_class,
                "command": command,
                "process_cwd": str(files["cwd"]),
                "driver_cwd_arg": str(ROOT),
                "scope_file_arg": str(case["scope"] or ROOT / SCOPE_REL),
                "input_sha256_before": before,
                "input_sha256_after": after,
                "exit": process.returncode,
                "headline": headline,
                "reason": reason,
                "stderr_tail": process.stderr[-500:],
            }

    counts = {}
    open_ids = {}
    for stage, results in replay.items():
        labels = [item["classification"] for item in results.values()]
        counts[stage] = {label: labels.count(label) for label in sorted(set(labels))}
        open_ids[stage] = sorted(name for name, result in results.items()
                                 if result["classification"] == "open")
    final_sha = sha(COMPARATOR)
    if final_sha != landed_sha or sha(PRE_COMPARATOR) != pre_sha:
        raise RuntimeError("comparator source changed during held-out replay")
    final_tree = git("rev-parse", "HEAD^{tree}")
    report = {
        "schema": "kotoba.round45.c1.heldout-replay.v1",
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "head": head,
        "tree": tree,
        "tree_after": final_tree,
        "comparator_sha256": {"r44_dispatch": pre_sha, "landed_032f47b": landed_sha},
        "worktree_comparator_sha256_at_start": worktree_comparator_sha,
        "landed_commit_blob_sha256": landed_blob_sha,
        "r41_sources_sha256": source_hashes,
        "fresh_payload_sha256": {"live": live_sha, "independent": independent_sha,
                                  "scope": sha(ROOT / SCOPE_REL)},
        "r41_arm_count": len(cases),
        "r41_baseline_open_count": sum(
            item["classification"] == "open" for item in historic_arms.values()),
        "arm_ids_equal_across_generator_and_r41_record":
            set(cases) == set(historic_arms) == set(old_outcomes),
        "classification_counts": counts,
        "still_open_ids": open_ids,
        "all_per_arm_inputs_unchanged": all(
            item["input_sha256_before"] == item["input_sha256_after"]
            for stage_results in replay.values() for item in stage_results.values()),
        "arms": replay,
    }
    RESULTS.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("r41 arms: %d/46; r41 baseline open: %d" %
          (len(cases), report["r41_baseline_open_count"]))
    for stage in replay:
        print("%s: counts=%s open=%s" % (stage, counts[stage], open_ids[stage]))
    print("result=%s sha256=%s" % (RESULTS, sha(RESULTS)))
    print("head=%s tree=%s comparator=%s" % (head, tree, final_sha))
    return 0


if __name__ == "__main__":
    sys.exit(main())
