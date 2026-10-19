#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
EVIDENCE = ROOT / ".ufo/round-41/evidence"
SOURCE = EVIDENCE / "probe-results.json"
CENSUS_MAP = EVIDENCE / "v10-channel-census.py"
DRIVER_PATH = ROOT / "verifiers/compare_harness_independent.py"
TARGET = "032f47bd13fdff0cd2ccea5f902df9690ad09376"
RECEIPT = DRAFT / "cwd-replay-receipt.json"
OUTPUT = DRAFT / "r41-replay-landed.json"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def load_cases():
    spec = importlib.util.spec_from_file_location("r41_channel_census", CENSUS_MAP)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CASES


def input_paths(command, process_cwd):
    paths = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag not in command:
            continue
        value = Path(command[command.index(flag) + 1])
        resolved = value if value.is_absolute() else process_cwd / value
        paths[flag[2:].replace("-", "_")] = resolved.resolve()
    return paths


def main():
    root_head = git("rev-parse", "HEAD")
    root_tree = git("rev-parse", "HEAD^{tree}")
    source_bytes = SOURCE.read_bytes()
    source = json.loads(source_bytes)
    source_arms = source["arms"]
    cases = load_cases()
    if len(source_arms) != 46 or set(source_arms) != set(cases):
        raise ValueError("r41 source arm inventory does not match its 46-arm classifier")
    if root_head != TARGET:
        raise ValueError(f"expected target HEAD {TARGET}, found {root_head}")

    driver_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{TARGET}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    driver_sha = sha_bytes(driver_bytes)
    worktree_driver_sha = sha_file(DRIVER_PATH)
    source_sha = sha_bytes(source_bytes)
    source_map_sha = sha_file(CENSUS_MAP)
    wrapper = (
        "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
        "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
        "{'__name__':'__main__','__file__':p})"
    )
    arms = []
    for arm_id, expected in sorted(source_arms.items()):
        original = list(expected["command"])
        args = original[2:]
        if "--receipt" in args:
            args[args.index("--receipt") + 1] = str(RECEIPT)
        process_cwd = Path(expected["process_cwd"])
        paths = input_paths(args, process_cwd)
        before = {key: sha_file(path) for key, path in paths.items()}
        command = [sys.executable, "-c", wrapper, str(DRIVER_PATH), *args]
        proc = subprocess.run(command, cwd=process_cwd, input=driver_bytes.decode("utf-8"),
                              capture_output=True, text=True, timeout=120)
        after = {key: sha_file(path) for key, path in paths.items()}
        try:
            response = json.loads(proc.stdout)
            headline = response.get("headline")
            reason = response.get("reason", "")
        except (ValueError, TypeError):
            headline = None
            reason = (proc.stderr or proc.stdout).strip()[-1200:]
        baseline_class = cases[arm_id][0]
        if baseline_class == "open":
            landed_class = "open" if proc.returncode == 0 else "closed"
        elif baseline_class == "closed":
            landed_class = "unexpected-open" if proc.returncode == 0 else "closed"
        elif baseline_class == "diagnostic":
            landed_class = "diagnostic" if proc.returncode != 0 else "accepted-diagnostic"
        elif baseline_class == "trust-input":
            landed_class = "trust-input"
        else:
            landed_class = "control"
        arms.append({
            "id": arm_id,
            "baseline_classification": baseline_class,
            "landed_classification": landed_class,
            "channel": cases[arm_id][1],
            "finding": cases[arm_id][2],
            "command": command,
            "process_cwd": str(process_cwd),
            "inputs_sha256_before": before,
            "inputs_sha256_after": after,
            "inputs_unchanged": before == after,
            "expected": {"exit": expected["exit"], "headline": expected.get("headline"),
                         "reason": expected["reason"]},
            "actual": {"exit": proc.returncode, "headline": headline, "reason": reason,
                       "stdout_sha256": sha_bytes(proc.stdout.encode()),
                       "stderr_sha256": sha_bytes(proc.stderr.encode()),
                       "stderr_tail": proc.stderr[-500:]},
        })

    counts = Counter(arm["landed_classification"] for arm in arms)
    report = {
        "schema": "kotoba.round45.c2.r41-landed-replay.v1",
        "measured_at_utc": datetime.now(timezone.utc).isoformat(),
        "target": {
            "commit": root_head,
            "tree": root_tree,
            "comparator_path": "verifiers/compare_harness_independent.py",
            "comparator_git_blob_sha256": driver_sha,
            "comparator_worktree_sha256_at_start": worktree_driver_sha,
            "worktree_matches_target_bytes_at_start": worktree_driver_sha == driver_sha,
            "execution": "one git-show source snapshot executed via python -c for every arm; comparator worktree file was not executed",
        },
        "inputs": {
            "r41_probe_results": str(SOURCE.relative_to(ROOT)),
            "r41_probe_results_sha256": source_sha,
            "r41_source_head": source.get("head"),
            "r41_source_tree": source.get("tree"),
            "r41_channel_classifier_sha256": source_map_sha,
            "captured_live_sha256": source.get("live_payload_sha256"),
            "captured_independent_sha256": source.get("independent_payload_sha256"),
            "committed_scope_sha256": source.get("scope_sha256"),
        },
        "summary": {
            "arm_count": len(arms),
            "baseline_open_arm_count": sum(arm["baseline_classification"] == "open" for arm in arms),
            "landed_open_arm_count": counts["open"],
            "unexpected_open_from_baseline_closed": counts["unexpected-open"],
            "landed_classification_counts": dict(sorted(counts.items())),
            "open_arm_ids": [arm["id"] for arm in arms if arm["landed_classification"] == "open"],
            "unexpected_open_arm_ids": [arm["id"] for arm in arms if arm["landed_classification"] == "unexpected-open"],
            "all_input_hashes_unchanged": all(arm["inputs_unchanged"] for arm in arms),
            "all_processes_completed": len(arms) == 46,
        },
        "arms": arms,
        "worktree_state_after": {
            "head": git("rev-parse", "HEAD"),
            "tree": git("rev-parse", "HEAD^{tree}"),
            "comparator_worktree_sha256": sha_file(DRIVER_PATH),
        },
    }
    if report["worktree_state_after"]["head"] != root_head or report["worktree_state_after"]["tree"] != root_tree:
        raise RuntimeError("HEAD/tree changed during the replay")
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("r41_replay: %d arms, baseline-open=%d, landed-open=%d, unexpected-open=%d, counts=%s" % (
        report["summary"]["arm_count"], report["summary"]["baseline_open_arm_count"],
        report["summary"]["landed_open_arm_count"],
        report["summary"]["unexpected_open_from_baseline_closed"],
        report["summary"]["landed_classification_counts"]))
    print("target=%s tree=%s comparator=%s worktree-comparator-start=%s end=%s" % (
        root_head, root_tree, driver_sha, worktree_driver_sha,
        report["worktree_state_after"]["comparator_worktree_sha256"]))
    print("output=%s sha256=%s" % (OUTPUT, sha_file(OUTPUT)))
    return int(not report["summary"]["all_input_hashes_unchanged"])


if __name__ == "__main__":
    sys.exit(main())
