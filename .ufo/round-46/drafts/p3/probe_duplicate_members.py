#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[4]
COMPARATOR = "verifiers/compare_harness_independent.py"
FIXTURES = ROOT / "verifiers/fixtures/compare-harness-independent"
CASE_NAMES = (
    "duplicate-independent-results-member",
    "duplicate-independent-re-derived-member",
    "duplicate-live-results-member",
)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_value(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=("git", "worktree"), required=True)
    parser.add_argument("--revision", default="055d3b9")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    source = (subprocess.check_output(
        ["git", "show", f"{args.revision}:{COMPARATOR}"], cwd=ROOT
    ) if args.source == "git" else (ROOT / COMPARATOR).read_bytes())
    head_before = git_value("rev-parse", "HEAD")
    tree_before = git_value("rev-parse", "HEAD^{tree}")
    draft_dir = Path(__file__).resolve().parent
    out = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "source": args.source,
        "revision": args.revision if args.source == "git" else None,
        "comparator_path": COMPARATOR,
        "comparator_sha256": sha256(source),
        "head_before": head_before,
        "tree_before": tree_before,
        "runner_sha256": sha256(Path(__file__).read_bytes()),
        "cases": [],
    }
    with tempfile.TemporaryDirectory(prefix="probe-", dir=draft_dir) as tmp:
        script = Path(tmp) / "compare_harness_independent.py"
        script.write_bytes(source)
        for name in CASE_NAMES:
            case_dir = FIXTURES / name
            case = json.loads((case_dir / "case.json").read_text(encoding="utf-8"))
            live_path = (case_dir / case["live"]).resolve()
            independent_path = (case_dir / case["independent"]).resolve()
            scope_path = FIXTURES / case.get("scope", "scope.json")
            command = [
                sys.executable, "-B", str(script),
                "--cwd", str(ROOT),
                "--live-json", str(live_path),
                "--independent-json", str(independent_path),
                "--scope-file", str(scope_path),
                "--expect-n", str(case["expect_n"]),
                "--no-stamp",
            ]
            proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            combined = proc.stdout + proc.stderr
            expected_exit = 0 if args.source == "git" else case["expect"]["exit"]
            expected_named = [] if args.source == "git" else case["expect"]["named"]
            ok = (proc.returncode == expected_exit
                  and all(token in combined for token in expected_named)
                  and "Traceback" not in combined)
            out["cases"].append({
                "name": name,
                "case_sha256": sha256((case_dir / "case.json").read_bytes()),
                "live_path": str(live_path),
                "live_sha256": sha256(live_path.read_bytes()),
                "independent_path": str(independent_path),
                "independent_sha256": sha256(independent_path.read_bytes()),
                "scope_sha256": sha256(scope_path.read_bytes()),
                "command": command,
                "exit": proc.returncode,
                "expected_exit": expected_exit,
                "expected_named": expected_named,
                "ok": ok,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            })
    out["head_after"] = git_value("rev-parse", "HEAD")
    out["tree_after"] = git_value("rev-parse", "HEAD^{tree}")
    out["recorded_at_end"] = datetime.now(timezone.utc).isoformat()
    result_path = args.out if args.out.is_absolute() else ROOT / args.out
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"source={args.source} comparator_sha256={out['comparator_sha256']}")
    print(f"head={head_before} tree={tree_before}")
    for result in out["cases"]:
        print(f"{result['name']}: exit={result['exit']} expected={result['expected_exit']} ok={result['ok']} case_sha256={result['case_sha256']} live_sha256={result['live_sha256']} independent_sha256={result['independent_sha256']}")
    print(f"result={result_path} sha256={sha256(result_path.read_bytes())}")
    return 0 if all(result["ok"] for result in out["cases"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
