from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
RUN = DRAFT / "run-03"
INPUTS = RUN / "inputs"
CASES = RUN / "cases"
OUTPUTS = RUN / "outputs"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
TARGET = "omp.offered.skills"
BASELINE = "055d3b9"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pin() -> dict:
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
        "comparator_worktree_sha256": digest(
            (ROOT / "verifiers/compare_harness_independent.py").read_bytes()
        ),
        "scope_worktree_sha256": digest((ROOT / SCOPE_REL).read_bytes()),
    }


def git_blob(revision: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{path}"], cwd=ROOT,
        check=True, capture_output=True
    ).stdout


def make_attack(clean: dict) -> dict:
    payload = copy.deepcopy(clean)
    probes = payload.get("scoped_out_probes")
    if not isinstance(probes, dict) or not probes:
        raise RuntimeError("fresh independent producer has no scoped_out_probes")
    probe_source = next(iter(probes))
    probe = copy.deepcopy(probes[probe_source])
    if not isinstance(probe, dict):
        raise RuntimeError(f"probe source {probe_source} is not an object")
    seen = 0
    for channel in ("results", "rows"):
        rows = payload.get(channel)
        if not isinstance(rows, list):
            continue
        matches = [row for row in rows if isinstance(row, dict) and row.get("check") == TARGET]
        if len(matches) != 1:
            raise RuntimeError(f"{channel}: expected one {TARGET} row; got {len(matches)}")
        record = matches[0]
        for key in ("expected", "expected_value", "re_derived", "value", "observed"):
            if key in record:
                record[key] = None
        record["re_derived"] = None
        record["value"] = None
        record["status"] = "SCOPED_OUT"
        record["probe"] = copy.deepcopy(probe)
        seen += 1
    checks = payload.get("checks")
    if not isinstance(checks, dict) or TARGET not in checks:
        raise RuntimeError(f"checks channel lacks {TARGET}")
    checks[TARGET] = None
    payload.setdefault("scoped_out", {})[TARGET] = "probe: C1 planted scope-path arm"
    payload.setdefault("scoped_out_probes", {})[TARGET] = copy.deepcopy(probe)
    if seen != 2:
        raise RuntimeError(f"expected both results and rows channels; updated {seen}")
    return payload


def run_case(name: str, proc_cwd: Path, scope_arg: str, live_path: Path,
             independent_path: Path, comparator: Path) -> dict:
    receipt_path = OUTPUTS / f"{name}.receipt.json"
    stdout_path = OUTPUTS / f"{name}.stdout.json"
    argv = [
        sys.executable, "-B", str(comparator),
        "--live-json", str(live_path),
        "--independent-json", str(independent_path),
        "--scope-file", scope_arg,
        "--cwd", str(ROOT),
        "--expect-n", "28",
        "--no-stamp", "--json",
        "--receipt", str(receipt_path),
    ]
    invoked_scope = Path(scope_arg)
    effective_path = invoked_scope if invoked_scope.is_absolute() else proc_cwd / invoked_scope
    enforced_bytes = effective_path.read_bytes()
    completed = subprocess.run(
        argv, cwd=proc_cwd, capture_output=True, text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, timeout=180,
    )
    stdout_bytes = completed.stdout.encode()
    result = None
    if completed.returncode == 0:
        result = json.loads(completed.stdout)
        stdout_path.write_bytes(stdout_bytes)
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    return {
        "name": name,
        "command": argv,
        "process_cwd": str(proc_cwd),
        "scope_argument": scope_arg,
        "scope_effective_path": str(effective_path.resolve()),
        "scope_enforced_sha256": digest(enforced_bytes),
        "returncode": completed.returncode,
        "stdout_sha256": digest(stdout_bytes),
        "stderr": completed.stderr,
        "headline": result.get("headline") if result else None,
        "agreement": result.get("agreement") if result else None,
        "scoped_out": result.get("scoped_out") if result else None,
        "receipt_scope": receipt.get("scope_file") if receipt else None,
        "receipt_path": str(receipt_path) if receipt else None,
        "stdout_json_path": str(stdout_path) if result else None,
    }


def main() -> int:
    for directory in (INPUTS, CASES, OUTPUTS):
        directory.mkdir(parents=True, exist_ok=False)
    before = pin()
    comparator = INPUTS / "compare_harness_independent.py"
    comparator_blob = git_blob(BASELINE, "verifiers/compare_harness_independent.py")
    comparator.write_bytes(comparator_blob)
    scope_blob = git_blob(BASELINE, str(SCOPE_REL))
    (INPUTS / "honest-scope.json").write_bytes(scope_blob)
    honest_sha = digest(scope_blob)
    if digest((ROOT / SCOPE_REL).read_bytes()) != honest_sha:
        raise RuntimeError("worktree scope differs from the pinned scope blob")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    producer_runs = {}
    for name, path in (
        ("live", ROOT / "verifiers/verify_harness_claims.py"),
        ("independent", ROOT / "verifiers/verify_harness_independent.py"),
    ):
        command = [sys.executable, "-B", str(path), "--json"]
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, env=env, timeout=180)
        if proc.returncode != 0:
            raise RuntimeError(f"producer {name} exit {proc.returncode}: {proc.stderr.decode()[:500]}")
        (INPUTS / f"{name}.json").write_bytes(proc.stdout)
        producer_runs[name] = {
            "command": command,
            "exit": proc.returncode,
            "stdout_sha256": digest(proc.stdout),
            "stderr_sha256": digest(proc.stderr),
        }
    live_path = INPUTS / "live.json"
    independent_path = INPUTS / "independent.json"
    clean_payload = json.loads(independent_path.read_text())
    attack_payload = make_attack(clean_payload)
    attack_path = INPUTS / "independent-planted-scope.json"
    attack_path.write_text(json.dumps(attack_payload, indent=2, sort_keys=True) + "\n")
    attack_scope = json.loads(scope_blob)
    template = copy.deepcopy(next(iter(attack_scope["scope_out"].values())))
    template["reason"] = "planted scope-path reproduction; not an authoritative scope edit"
    attack_scope["scope_out"][TARGET] = template
    attack_scope_path = INPUTS / "planted-superset-scope.json"
    attack_scope_path.write_text(json.dumps(attack_scope, indent=2, sort_keys=True) + "\n")
    attack_scope_sha = digest(attack_scope_path.read_bytes())

    plain_cwd = CASES / "plain-relative-cwd"
    plain_scope_dir = plain_cwd / "verifiers"
    plain_scope_dir.mkdir(parents=True)
    (plain_scope_dir / SCOPE_REL.name).write_bytes(attack_scope_path.read_bytes())

    file_link_cwd = CASES / "symlinked-scope-file-cwd"
    file_link_dir = file_link_cwd / "verifiers"
    file_link_dir.mkdir(parents=True)
    (file_link_dir / SCOPE_REL.name).symlink_to(attack_scope_path.resolve())

    dir_link_cwd = CASES / "symlinked-scope-directory-cwd"
    dir_link_cwd.mkdir()
    (dir_link_cwd / "verifiers").symlink_to(plain_scope_dir.resolve(), target_is_directory=True)

    symlinked_scope = file_link_dir / SCOPE_REL.name
    cases = [
        run_case("clean-24-24-control", ROOT, str(ROOT / SCOPE_REL), live_path,
                 independent_path, comparator),
        run_case("honest-scope-rejects-planted-row", ROOT, str(ROOT / SCOPE_REL), live_path,
                 attack_path, comparator),
        run_case("relative-process-cwd-planted-scope", plain_cwd, str(SCOPE_REL), live_path,
                 attack_path, comparator),
        run_case("relative-via-symlinked-scope-file", file_link_cwd, str(SCOPE_REL), live_path,
                 attack_path, comparator),
        run_case("relative-via-symlinked-scope-directory", dir_link_cwd, str(SCOPE_REL), live_path,
                 attack_path, comparator),
        run_case("absolute-symlink-scope-explicit-trust", ROOT, str(symlinked_scope.absolute()),
                 live_path, attack_path, comparator),
    ]
    for case in cases:
        if case["name"] == "clean-24-24-control":
            if case["returncode"] != 0 or case["headline"]["n"] != 24:
                raise RuntimeError(f"clean control failed: {case}")
        elif case["name"] == "honest-scope-rejects-planted-row":
            if case["returncode"] != 2 or "laundering" not in case["stderr"]:
                raise RuntimeError(f"honest scope did not class-reject planted row: {case}")
        elif case["name"] == "absolute-symlink-scope-explicit-trust":
            if case["returncode"] != 0 or case["headline"]["n"] != 23:
                raise RuntimeError(f"absolute symlink control unexpected: {case}")
            if case["receipt_scope"]["sha256"] != attack_scope_sha:
                raise RuntimeError(f"absolute symlink receipt did not hash enforced bytes: {case}")
        else:
            if case["returncode"] != 0 or case["headline"]["n"] != 23:
                raise RuntimeError(f"relative path attack did not reproduce: {case}")
            if case["receipt_scope"]["sha256"] != honest_sha:
                raise RuntimeError(f"receipt did not attest the --cwd scope: {case}")
            if case["scope_enforced_sha256"] != attack_scope_sha:
                raise RuntimeError(f"expected planted scope bytes were not enforced: {case}")

    after = pin()
    if before["head"] != after["head"] or before["tree"] != after["tree"]:
        raise RuntimeError("HEAD/tree changed during frozen probe")
    if before["scope_worktree_sha256"] != after["scope_worktree_sha256"]:
        raise RuntimeError("worktree scope file changed during frozen probe")
    output = {
        "measurement": {"started": before, "finished": after},
        "frozen_comparator": {
            "revision": BASELINE,
            "path": str(comparator),
            "sha256": digest(comparator_blob),
        },
        "frozen_scope": {"revision": BASELINE, "sha256": honest_sha},
        "producer_runs": producer_runs,
        "attack_inputs": {
            "live_sha256": digest(live_path.read_bytes()),
            "independent_clean_sha256": digest(independent_path.read_bytes()),
            "independent_planted_scope_sha256": digest(attack_path.read_bytes()),
            "planted_scope_sha256": attack_scope_sha,
            "target_check": TARGET,
            "scope_probe_copied_from": next(iter(clean_payload["scoped_out_probes"])),
        },
        "cases": cases,
    }
    result_path = OUTPUTS / "scope-path-results.json"
    result_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(result_path),
        "sha256": digest(result_path.read_bytes()),
        "frozen_comparator_sha256": digest(comparator_blob),
        "cases": [
            {"name": case["name"], "exit": case["returncode"],
             "headline": case["headline"], "receipt_scope": case["receipt_scope"],
             "enforced_sha256": case["scope_enforced_sha256"]}
            for case in cases
        ],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
