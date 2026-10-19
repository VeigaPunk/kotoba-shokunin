import copy
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
ROOT = DRAFT.parents[3]
SOURCE = ROOT / ".ufo/round-41/evidence/probe-results.json"
COMPARATOR = DRAFT / "compare-13b6d791.py"
RECEIPT = DRAFT / "cwd-replay-receipt.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def input_paths(command, process_cwd):
    paths = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in command:
            value = Path(command[command.index(flag) + 1])
            resolved = value if value.is_absolute() else process_cwd / value
            paths[flag[2:].replace("-", "_")] = resolved.resolve()
    return paths


def main():
    source_bytes = SOURCE.read_bytes()
    archived = json.loads(source_bytes)
    original_arms = archived["arms"]
    comparator_sha = sha(COMPARATOR)
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    captured_at = datetime.now(timezone.utc).isoformat()
    arms = {}

    for arm_id, original in sorted(original_arms.items()):
        command = list(original["command"])
        command[1] = str(COMPARATOR)
        if "--receipt" in command:
            command[command.index("--receipt") + 1] = str(RECEIPT)
        process_cwd = Path(original["process_cwd"])
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
        arms[arm_id] = {
            **original,
            "command": command,
            "process_cwd": str(process_cwd),
            "driver_cwd_arg": original["driver_cwd_arg"],
            "scope_file_arg": original["scope_file_arg"],
            "exit": completed.returncode,
            "headline": headline,
            "reason": reason,
            "initial_inputs_sha256_before": before,
            "initial_inputs_sha256_after": after,
            "initial_inputs_unchanged": before == after,
        }
        print(f"{arm_id:48s} exit={completed.returncode} "
              f"headline={(headline or {}).get('n', '-')} reason={reason[:150]}")

    result = {
        **archived,
        "arms": arms,
        "head": head,
        "tree": tree,
        "comparator_sha256": comparator_sha,
        "current_comparator_sha256": comparator_sha,
        "archived_probe_results_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "archived_comparator_sha256": archived.get("comparator_sha256"),
        "captured_at_utc": captured_at,
        "replay_target": "git show 032f47bd:verifiers/compare_harness_independent.py", 
    }
    if sha(COMPARATOR) != comparator_sha or git("rev-parse", "HEAD") != head or git("rev-parse", "HEAD^{tree}") != tree:
        raise RuntimeError("HEAD, tree, or comparator changed during candidate outcome capture")
    if not all(arm["initial_inputs_unchanged"] for arm in arms.values()):
        raise RuntimeError("one or more input files changed during candidate outcome capture")
    output = DRAFT / "probe-results.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"candidate_outcomes: {len(arms)} arms; output={output}")
    print(f"HEAD {head} TREE {tree} COMPARATOR {comparator_sha} CAPTURED {captured_at}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
