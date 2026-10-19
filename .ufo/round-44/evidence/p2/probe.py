#!/usr/bin/env python3
import argparse
import hashlib
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FIXTURES = ROOT / "verifiers/fixtures/compare-harness-independent"
NAMES = (
    "dotted-id-top-level-map-shadow",
    "record-check-id-conflict",
    "record-re-derived-observed-conflict",
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    proc = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                          text=True, check=True)
    return proc.stdout.strip()


def run_one(comparator, name):
    case = FIXTURES / name
    live = FIXTURES / "field-shared/live.json"
    independent = case / "independent.json"
    scope = FIXTURES / "scope.json"
    argv = [
        sys.executable, str(comparator),
        "--live-json", str(live),
        "--independent-json", str(independent),
        "--cwd", str(ROOT), "--scope-file", str(scope),
        "--expect-n", "3", "--no-stamp",
    ]
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {
        "name": name,
        "argv": argv,
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "stdout_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr.encode()).hexdigest(),
        "inputs": {
            "case": sha(case / "case.json"),
            "live": sha(live),
            "independent": sha(independent),
            "scope": sha(scope),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("before", "after"))
    parser.add_argument("--comparator", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    comparator = args.comparator.resolve()
    with ThreadPoolExecutor(max_workers=len(NAMES)) as pool:
        rows = list(pool.map(lambda name: run_one(comparator, name), NAMES))
    current = ROOT / "verifiers/compare_harness_independent.py"
    record = {
        "stage": args.stage,
        "measured_at": datetime.now(timezone.utc).isoformat(),
        "head": git("rev-parse", "HEAD"),
        "head_tree": git("rev-parse", "HEAD^{tree}"),
        "worktree_status": git("status", "--short"),
        "comparator": str(comparator),
        "comparator_sha256": sha(comparator),
        "current_comparator_sha256": sha(current),
        "cases": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "stage": args.stage,
        "head": record["head"],
        "head_tree": record["head_tree"],
        "comparator_sha256": record["comparator_sha256"],
        "current_comparator_sha256": record["current_comparator_sha256"],
        "cases": [{"name": row["name"], "exit": row["exit"],
                   "stdout_sha256": row["stdout_sha256"],
                   "stderr_sha256": row["stderr_sha256"]}
                  for row in rows],
        "output": str(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
