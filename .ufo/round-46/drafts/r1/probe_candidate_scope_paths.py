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
PRIOR = DRAFT / "run-03" / "inputs"
RUN = DRAFT / "run-04"
INPUTS = RUN / "inputs"
CASES = RUN / "cases"
OUTPUTS = RUN / "outputs"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
TARGET = "omp.offered.skills"
SOURCE = ROOT / "verifiers/compare_harness_independent.py"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def identity() -> dict:
    return {
        "at": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
            capture_output=True, text=True
        ).stdout.strip(),
        "tree": subprocess.run(
            ["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, check=True,
            capture_output=True, text=True
        ).stdout.strip(),
        "worktree_comparator_sha256": sha(SOURCE.read_bytes()),
    }


def run_case(name: str, process_cwd: Path, cli_cwd: Path, scope_arg: str,
             independent: Path, comparator: Path, live: Path) -> dict:
    receipt_path = OUTPUTS / f"{name}.receipt.json"
    stdout_path = OUTPUTS / f"{name}.stdout.json"
    argv = [
        sys.executable, "-B", str(comparator),
        "--live-json", str(live),
        "--independent-json", str(independent),
        "--scope-file", scope_arg,
        "--cwd", str(cli_cwd),
        "--expect-n", "28", "--no-stamp", "--json",
        "--receipt", str(receipt_path),
    ]
    arg_path = Path(scope_arg)
    resolved_path = (arg_path if arg_path.is_absolute() else cli_cwd / arg_path).resolve()
    enforced_sha = sha(resolved_path.read_bytes())
    proc = subprocess.run(
        argv, cwd=process_cwd, capture_output=True, text=True, timeout=180,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    output = None
    stdout_bytes = proc.stdout.encode()
    if proc.returncode == 0:
        output = json.loads(proc.stdout)
        stdout_path.write_bytes(stdout_bytes)
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    return {
        "name": name,
        "command": argv,
        "process_cwd": str(process_cwd),
        "cli_cwd": str(cli_cwd),
        "scope_argument": scope_arg,
        "resolved_path_expected": str(resolved_path),
        "resolved_scope_sha256": enforced_sha,
        "exit": proc.returncode,
        "headline": output.get("headline") if output else None,
        "agreement": output.get("agreement") if output else None,
        "stderr": proc.stderr,
        "stdout_sha256": sha(stdout_bytes),
        "receipt_scope": receipt.get("scope_file") if receipt else None,
        "receipt_path": str(receipt_path) if receipt else None,
        "stdout_json_path": str(stdout_path) if output else None,
    }


def main() -> int:
    for path in (INPUTS, CASES, OUTPUTS):
        path.mkdir(parents=True, exist_ok=False)
    before = identity()
    comparator_blob = SOURCE.read_bytes()
    comparator = INPUTS / "compare_candidate.py"
    comparator.write_bytes(comparator_blob)
    comparator_sha = sha(comparator_blob)
    live = PRIOR / "live.json"
    clean_ind = PRIOR / "independent.json"
    attack_ind = PRIOR / "independent-planted-scope.json"
    planted_scope = PRIOR / "planted-superset-scope.json"
    if not all(path.is_file() for path in (live, clean_ind, attack_ind, planted_scope)):
        raise RuntimeError("the pinned r46 R1 input bundle is incomplete")
    planted_sha = sha(planted_scope.read_bytes())

    process_plain = CASES / "plain-process-cwd"
    plain_verifiers = process_plain / "verifiers"
    plain_verifiers.mkdir(parents=True)
    (plain_verifiers / SCOPE_REL.name).write_bytes(planted_scope.read_bytes())

    process_file_link = CASES / "process-cwd-symlink-file"
    process_file_verifiers = process_file_link / "verifiers"
    process_file_verifiers.mkdir(parents=True)
    (process_file_verifiers / SCOPE_REL.name).symlink_to(planted_scope.resolve())

    process_dir_link = CASES / "process-cwd-symlink-directory"
    process_dir_link.mkdir()
    (process_dir_link / "verifiers").symlink_to(plain_verifiers.resolve(), target_is_directory=True)

    cwd_file_link = CASES / "cli-cwd-symlink-file"
    cwd_file_verifiers = cwd_file_link / "verifiers"
    cwd_file_verifiers.mkdir(parents=True)
    (cwd_file_verifiers / SCOPE_REL.name).symlink_to(planted_scope.resolve())

    cwd_dir_link = CASES / "cli-cwd-symlink-directory"
    cwd_dir_link.mkdir()
    (cwd_dir_link / "verifiers").symlink_to(plain_verifiers.resolve(), target_is_directory=True)

    absolute_symlink = process_file_verifiers / SCOPE_REL.name
    cases = [
        run_case("clean-24-24", ROOT, ROOT, str(ROOT / SCOPE_REL), clean_ind, comparator, live),
        run_case("honest-scope-rejects-plant", ROOT, ROOT, str(ROOT / SCOPE_REL), attack_ind, comparator, live),
        run_case("relative-plant-in-process-cwd", process_plain, ROOT, str(SCOPE_REL), attack_ind, comparator, live),
        run_case("symlink-file-in-process-cwd", process_file_link, ROOT, str(SCOPE_REL), attack_ind, comparator, live),
        run_case("symlink-dir-in-process-cwd", process_dir_link, ROOT, str(SCOPE_REL), attack_ind, comparator, live),
        run_case("symlink-file-under-cli-cwd", cwd_file_link, cwd_file_link, str(SCOPE_REL), attack_ind, comparator, live),
        run_case("symlink-dir-under-cli-cwd", cwd_dir_link, cwd_dir_link, str(SCOPE_REL), attack_ind, comparator, live),
        run_case("absolute-symlink-argument", ROOT, ROOT, str(absolute_symlink.absolute()), attack_ind, comparator, live),
    ]
    for case in cases:
        name = case["name"]
        if name == "clean-24-24":
            if case["exit"] != 0 or case["headline"]["n"] != 24:
                raise RuntimeError(f"candidate clean control failed: {case}")
        elif name in ("honest-scope-rejects-plant", "relative-plant-in-process-cwd",
                      "symlink-file-in-process-cwd", "symlink-dir-in-process-cwd"):
            if case["exit"] != 2 or "laundering" not in case["stderr"]:
                raise RuntimeError(f"candidate failed to reject planted payload via {name}: {case}")
        else:
            if case["exit"] != 0 or case["headline"]["n"] != 23:
                raise RuntimeError(f"candidate explicit scope path unexpected for {name}: {case}")
            if not case["receipt_scope"] or case["receipt_scope"]["sha256"] != planted_sha:
                raise RuntimeError(f"candidate receipt did not attest resolved scope for {name}: {case}")
            if case["receipt_scope"]["path"] != case["resolved_path_expected"]:
                raise RuntimeError(f"candidate receipt path differs from resolved enforced path: {case}")

    after = identity()
    if before["head"] != after["head"] or before["tree"] != after["tree"]:
        raise RuntimeError("HEAD/tree changed during candidate replay")
    result = {
        "measurement": {"started": before, "finished": after},
        "candidate": {"source_path": str(SOURCE), "snapshot_path": str(comparator),
                      "snapshot_sha256": comparator_sha},
        "inputs": {
            "source_bundle": str(PRIOR),
            "live_sha256": sha(live.read_bytes()),
            "independent_clean_sha256": sha(clean_ind.read_bytes()),
            "independent_planted_scope_sha256": sha(attack_ind.read_bytes()),
            "planted_scope_sha256": planted_sha,
            "target_check": TARGET,
        },
        "cases": cases,
    }
    result_path = OUTPUTS / "candidate-scope-path-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(result_path),
        "result_sha256": sha(result_path.read_bytes()),
        "candidate_sha256": comparator_sha,
        "cases": [{"name": c["name"], "exit": c["exit"],
                   "headline": c["headline"], "receipt_scope": c["receipt_scope"]}
                  for c in cases],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
