#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
ROOT = DRAFT.parents[4]
RESULTS = DRAFT / "probe-results.json"
OUT = DRAFT / "subprocess-replay.json"
REPLAY_RECEIPT = DRAFT / "cwd-replay-receipt.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_paths(command, process_cwd):
    paths = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in command:
            value = Path(command[command.index(flag) + 1])
            resolved = value if value.is_absolute() else process_cwd / value
            paths[flag[2:].replace("-", "_")] = resolved.resolve()
    return paths


def main():
    source = json.loads(RESULTS.read_text(encoding="utf-8"))
    arms = []
    for arm_id, expected in sorted(source["arms"].items()):
        command = list(expected["command"])
        if "--receipt" in command:
            command[command.index("--receipt") + 1] = str(REPLAY_RECEIPT)
        process_cwd = Path(expected["process_cwd"])
        inputs = input_paths(command, process_cwd)
        before = {key: sha(path) for key, path in inputs.items()}
        completed = subprocess.run(command, cwd=process_cwd, text=True,
                                   capture_output=True, timeout=90)
        try:
            response = json.loads(completed.stdout)
            headline = response.get("headline")
            reason = response.get("reason", "")
        except (ValueError, TypeError):
            headline = None
            reason = (completed.stderr or completed.stdout).strip()[-1200:]
        after = {key: sha(path) for key, path in inputs.items()}
        matched = (completed.returncode == expected["exit"]
                   and headline == expected.get("headline")
                   and reason == expected["reason"]
                   and before == after)
        arms.append({
            "id": arm_id,
            "command": command,
            "process_cwd": str(process_cwd),
            "driver_cwd_arg": expected["driver_cwd_arg"],
            "scope_file_arg": expected["scope_file_arg"],
            "inputs_sha256_before": {key: value for key, value in before.items()},
            "inputs_sha256_after": {key: value for key, value in after.items()},
            "expected": {
                "exit": expected["exit"],
                "headline": expected.get("headline"),
                "reason": expected["reason"],
            },
            "actual": {
                "exit": completed.returncode,
                "headline": headline,
                "reason": reason,
                "stderr_tail": completed.stderr[-400:],
            },
            "matched": matched,
        })
    report = {
        "schema": "kotoba.round41.v10.subprocess-replay.v1",
        "replayed_at_utc": datetime.now(timezone.utc).isoformat(),
        "frozen_head": source["head"],
        "frozen_tree": source["tree"],
        "comparator_sha256": source["comparator_sha256"],
        "live_payload_sha256": source["live_payload_sha256"],
        "independent_payload_sha256": source["independent_payload_sha256"],
        "scope_sha256": source["scope_sha256"],
        "process_count": len(arms),
        "matched_count": sum(arm["matched"] for arm in arms),
        "mismatches": [arm["id"] for arm in arms if not arm["matched"]],
        "arms": arms,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("subprocess_replay: %d/%d matched; output=%s" % (
        report["matched_count"], report["process_count"], OUT))
    if report["mismatches"]:
        print("mismatches: " + ", ".join(report["mismatches"]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
