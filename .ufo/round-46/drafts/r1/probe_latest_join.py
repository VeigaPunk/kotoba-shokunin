from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
RUN = DRAFT / "run-16"
INPUTS = RUN / "inputs"
OUTPUTS = RUN / "outputs"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    return sha(path.read_bytes())


def identity() -> dict:
    return {
        "at": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
        "tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
        "comparator_worktree_sha256": file_sha(ROOT / "verifiers/compare_harness_independent.py"),
        "live_producer_sha256": file_sha(ROOT / "verifiers/verify_harness_claims.py"),
        "independent_producer_sha256": file_sha(ROOT / "verifiers/verify_harness_independent.py"),
        "scope_worktree_sha256": file_sha(ROOT / "verifiers/harness-independent-scope.json"),
    }


def main() -> int:
    for path in (INPUTS, OUTPUTS):
        path.mkdir(parents=True, exist_ok=False)
    before = identity()
    candidate_source = DRAFT / "run-14/inputs/compare_candidate.py"
    candidate_bytes = candidate_source.read_bytes()
    candidate = INPUTS / "compare_candidate.py"
    candidate.write_bytes(candidate_bytes)
    scope_bytes = (ROOT / "verifiers/harness-independent-scope.json").read_bytes()
    scope = INPUTS / "scope.json"
    scope.write_bytes(scope_bytes)
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    producers = {}
    for name, filename in (
        ("live", "verify_harness_claims.py"),
        ("independent", "verify_harness_independent.py"),
    ):
        command = [sys.executable, "-B", str(ROOT / "verifiers" / filename), "--json"]
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, env=env, timeout=180)
        if proc.returncode != 0:
            raise RuntimeError(f"producer {name} exit {proc.returncode}: {proc.stderr.decode()[:500]}")
        out_path = INPUTS / f"{name}.json"
        out_path.write_bytes(proc.stdout)
        producers[name] = {"command": command, "exit": proc.returncode,
                           "stdout_sha256": sha(proc.stdout),
                           "stderr_sha256": sha(proc.stderr)}

    receipt_path = OUTPUTS / "ordinary-join.receipt.json"
    argv = [
        sys.executable, "-B", str(candidate),
        "--live-json", str(INPUTS / "live.json"),
        "--independent-json", str(INPUTS / "independent.json"),
        "--scope-file", str(scope), "--cwd", str(ROOT),
        "--expect-n", "28", "--no-stamp", "--json", "--receipt", str(receipt_path),
    ]
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, env=env, timeout=180)
    parsed = json.loads(proc.stdout) if proc.returncode == 0 else None
    if parsed is not None:
        (OUTPUTS / "ordinary-join.json").write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    after = identity()
    if before["head"] != after["head"] or before["tree"] != after["tree"]:
        raise RuntimeError("HEAD/tree changed during ordinary join")
    if before["scope_worktree_sha256"] != after["scope_worktree_sha256"]:
        raise RuntimeError("worktree scope changed during ordinary join")
    result = {
        "measurement": {"started": before, "finished": after},
        "candidate": {"path": str(candidate), "source_sha256": sha(candidate_bytes)},
        "scope_snapshot_sha256": sha(scope_bytes),
        "producer_runs": producers,
        "command": argv,
        "exit": proc.returncode,
        "stderr": proc.stderr,
        "stdout_sha256": sha(proc.stdout.encode()),
        "headline": parsed.get("headline") if parsed else None,
        "agreement": parsed.get("agreement") if parsed else None,
        "receipt_scope": receipt.get("scope_file") if receipt else None,
        "errors": parsed is None,
    }
    result_path = OUTPUTS / "ordinary-join-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"result": str(result_path), "result_sha256": sha(result_path.read_bytes()),
                      "candidate_sha256": sha(candidate_bytes), "exit": proc.returncode,
                      "headline": result["headline"], "agreement": result["agreement"],
                      "receipt_scope": result["receipt_scope"], "stderr": proc.stderr},
                     indent=2, sort_keys=True))
    return 0 if proc.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
