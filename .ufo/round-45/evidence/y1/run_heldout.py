#!/usr/bin/env python3
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
SOURCE = ROOT / ".ufo/round-41/evidence/v10-census-probes.py"
CLASSIFIER = ROOT / ".ufo/round-41/evidence/v10-channel-census.py"
COMPARATOR = DRAFT / "compare-032f47b.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(Path(path).read_bytes())


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def command_output(argv):
    return subprocess.run(argv, cwd=ROOT, text=True, capture_output=True,
                          check=True).stdout.strip()


def parse_output(proc):
    try:
        payload = json.loads(proc.stdout)
        return payload.get("headline"), payload.get("reason", ""), payload
    except (ValueError, TypeError):
        return None, (proc.stderr or proc.stdout).strip()[-1200:], None


def input_paths(command, process_cwd):
    paths = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in command:
            value = Path(command[command.index(flag) + 1])
            resolved = value if value.is_absolute() else process_cwd / value
            paths[flag[2:].replace("-", "_")] = resolved.resolve()
    return paths


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    pins_before = {
        "head": command_output(["git", "rev-parse", "HEAD"]),
        "tree": command_output(["git", "rev-parse", "HEAD^{tree}"]),
        "comparator_sha256": sha_file(COMPARATOR),
        "scope_sha256": sha_file(SCOPE),
    }
    live_path = DRAFT / "live-current.json"
    independent_path = DRAFT / "independent-current.json"
    live_proc = subprocess.run([sys.executable, str(ROOT / "verifiers/verify_harness_claims.py"), "--json"],
                               cwd=ROOT, text=True, capture_output=True, timeout=300)
    independent_proc = subprocess.run([sys.executable, str(ROOT / "verifiers/verify_harness_independent.py"), "--json"],
                                      cwd=ROOT, text=True, capture_output=True, timeout=300)
    if live_proc.returncode or independent_proc.returncode:
        raise RuntimeError("fresh producer capture failed: live=%d %s independent=%d %s" % (
            live_proc.returncode, live_proc.stderr[-500:],
            independent_proc.returncode, independent_proc.stderr[-500:]))
    live_path.write_text(live_proc.stdout, encoding="utf-8")
    independent_path.write_text(independent_proc.stdout, encoding="utf-8")
    live = json.loads(live_proc.stdout)
    independent = json.loads(independent_proc.stdout)

    probes = load_module("r41_v10_census_probes", SOURCE)
    probes.ROOT = ROOT
    probes.DRAFT = DRAFT
    probes.DRIVER = COMPARATOR
    probes.LIVE_FILE = live_path
    probes.IND_FILE = independent_path
    probes.CARRIER = DRAFT / "builder-carrier"
    probes.CARRIER.mkdir(parents=True, exist_ok=True)
    for name, stamp, entries in (("a.jsonl", "2026-01-01T00:00:00.000Z", 2),
                                 ("b.jsonl", "2026-02-02T00:00:00.000Z", 5)):
        rows = "\\n".join("- entry %d" % i for i in range(entries))
        (probes.CARRIER / name).write_text(
            '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\\n' %
            (stamp, rows), encoding="utf-8")
    os.utime(probes.CARRIER / "a.jsonl", (1700000000, 1700000000))
    os.utime(probes.CARRIER / "b.jsonl", (1700001000, 1700001000))
    driver = probes.load_driver()
    arms = probes.arms(driver, live, independent)
    classifier = load_module("r41_v10_channel_census", CLASSIFIER)

    results = {}
    for arm_id, case in sorted(arms.items()):
        expected = probes.run_case(driver, live, arm_id, case)
        process_cwd = Path(expected["process_cwd"])
        paths = input_paths(expected["command"], process_cwd)
        before = {key: sha_file(path) for key, path in paths.items()}
        proc = subprocess.run(expected["command"], cwd=process_cwd, text=True,
                              capture_output=True, timeout=90)
        headline, reason, parsed = parse_output(proc)
        after = {key: sha_file(path) for key, path in paths.items()}
        matched = (proc.returncode == expected["exit"]
                   and headline == expected["headline"]
                   and reason == expected["reason"]
                   and before == after)
        baseline_class = classifier.CASES[arm_id][0]
        if baseline_class == "open":
            current_class = "still-open" if proc.returncode == 0 else "closed-since-r41"
        elif baseline_class in ("control", "trust-input", "diagnostic"):
            current_class = baseline_class if proc.returncode == expected["exit"] else "control-or-diagnostic-drift"
        else:
            current_class = "closed" if proc.returncode != 0 else "reopened"
        results[arm_id] = {
            "r41_classification": baseline_class,
            "current_classification": current_class,
            "exit": proc.returncode,
            "headline": headline,
            "reason": reason,
            "matched_inprocess_outcome": proc.returncode == expected["exit"] and headline == expected["headline"] and reason == expected["reason"],
            "input_hashes_unchanged": before == after,
            "input_sha256_before": before,
            "input_sha256_after": after,
            "command": expected["command"],
            "process_cwd": str(process_cwd),
            "live_payload_sha256": sha_file(paths["live_json"]),
            "independent_payload_sha256": sha_file(paths["independent_json"]),
            "stdout_tail": proc.stdout[-1600:],
            "stderr_tail": proc.stderr[-800:],
            "subprocess_replay_matched": matched,
        }

    counts = Counter(row["current_classification"] for row in results.values())
    pins_after = {
        "head": command_output(["git", "rev-parse", "HEAD"]),
        "tree": command_output(["git", "rev-parse", "HEAD^{tree}"]),
        "comparator_sha256": sha_file(COMPARATOR),
        "scope_sha256": sha_file(SCOPE),
    }
    report = {
        "schema": "kotoba.round45.y1.heldout-hunt.v1",
        "started_at_utc": started,
        "ended_at_utc": datetime.now(timezone.utc).isoformat(),
        "pins_before": pins_before,
        "pins_after": pins_after,
        "sources": {
            "r41_census_doc_sha256": sha_file(ROOT / "corpus/knowledge/harness-independent-round41-census.md"),
            "r41_probe_generator_sha256": sha_file(SOURCE),
            "r41_arm_classifier_sha256": sha_file(CLASSIFIER),
            "r41_saved_probe_results_sha256": sha_file(ROOT / ".ufo/round-41/evidence/v10-probe-results.json"),
            "r41_saved_subprocess_replay_sha256": sha_file(ROOT / ".ufo/round-41/evidence/v10-subprocess-replay.json"),
            "scope_sha256": sha_file(SCOPE),
        },
        "fresh_producers": {
            "live_command": "python3 verifiers/verify_harness_claims.py --json",
            "live_exit": live_proc.returncode,
            "live_payload_sha256": sha_file(live_path),
            "independent_command": "python3 verifiers/verify_harness_independent.py --json",
            "independent_exit": independent_proc.returncode,
            "independent_payload_sha256": sha_file(independent_path),
            "live_result_count": len(live.get("results", [])),
            "independent_result_count": len(independent.get("results", [])),
        },
        "summary": {
            "arm_count": len(results),
            "classification_counts": dict(sorted(counts.items())),
            "still_open_ids": sorted(name for name, row in results.items() if row["current_classification"] == "still-open"),
            "reopened_ids": sorted(name for name, row in results.items() if row["current_classification"] == "reopened"),
            "all_subprocess_replays_matched": all(row["subprocess_replay_matched"] for row in results.values()),
            "all_input_hashes_unchanged": all(row["input_hashes_unchanged"] for row in results.values()),
        },
        "arms": results,
    }
    output = DRAFT / "heldout-hunt-results.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))
    print("RESULTS", output, sha_file(output))
    print("PINS", json.dumps({"before": pins_before, "after": pins_after}, sort_keys=True))
    return 0 if (len(results) == 46 and report["summary"]["all_subprocess_replays_matched"]
                 and report["summary"]["all_input_hashes_unchanged"]
                 and pins_before == pins_after) else 1


if __name__ == "__main__":
    sys.exit(main())
