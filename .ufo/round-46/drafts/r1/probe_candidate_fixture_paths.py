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
RUN = DRAFT / "run-14"
INPUTS = RUN / "inputs"
CASES = RUN / "cases"
OUTPUTS = RUN / "outputs"
FIXTURE = ROOT / "verifiers/fixtures/compare-harness-independent/scope-file-cwd"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
SOURCE = ROOT / "verifiers/compare_harness_independent.py"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def identity() -> dict:
    return {
        "at": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
        "tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT,
                             check=True, capture_output=True, text=True).stdout.strip(),
        "worktree_comparator_sha256": sha(SOURCE.read_bytes()),
    }


def run_case(name: str, process_cwd: Path, cli_cwd: Path, scope_arg: str,
             independent: Path, comparator: Path, live: Path) -> dict:
    receipt_path = OUTPUTS / f"{name}.receipt.json"
    stdout_path = OUTPUTS / f"{name}.stdout.json"
    argv = [
        sys.executable, "-B", str(comparator),
        "--live-json", str(live), "--independent-json", str(independent),
        "--scope-file", scope_arg, "--cwd", str(cli_cwd),
        "--expect-n", "2", "--no-stamp", "--json", "--receipt", str(receipt_path),
    ]
    arg_path = Path(scope_arg)
    resolved_path = (arg_path if arg_path.is_absolute() else cli_cwd / arg_path).resolve()
    enforced_sha = sha(resolved_path.read_bytes())
    proc = subprocess.run(
        argv, cwd=process_cwd, capture_output=True, text=True, timeout=120,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    stdout_bytes = proc.stdout.encode()
    result = json.loads(proc.stdout) if proc.returncode == 0 else None
    if result is not None:
        stdout_path.write_bytes(stdout_bytes)
    receipt = json.loads(receipt_path.read_text()) if receipt_path.is_file() else None
    return {
        "name": name,
        "command": argv,
        "process_cwd": str(process_cwd),
        "cli_cwd": str(cli_cwd),
        "scope_argument": scope_arg,
        "resolved_path_expected": str(resolved_path),
        "enforced_scope_sha256": enforced_sha,
        "exit": proc.returncode,
        "headline": result.get("headline") if result else None,
        "agreement": result.get("agreement") if result else None,
        "stderr": proc.stderr,
        "stdout_sha256": sha(stdout_bytes),
        "receipt_scope": receipt.get("scope_file") if receipt else None,
        "receipt_path": str(receipt_path) if receipt else None,
        "stdout_json_path": str(stdout_path) if result else None,
    }


def main() -> int:
    for path in (INPUTS, CASES, OUTPUTS):
        path.mkdir(parents=True, exist_ok=False)
    started = identity()
    comparator_bytes = SOURCE.read_bytes()
    comparator = INPUTS / "compare_candidate.py"
    comparator.write_bytes(comparator_bytes)

    live = INPUTS / "live.json"
    independent = INPUTS / "independent.json"
    honest_scope = INPUTS / "honest-scope.json"
    planted_scope = INPUTS / "planted-scope.json"
    live.write_bytes((FIXTURE / "live.json").read_bytes())
    payload = json.loads((FIXTURE / "independent.json").read_text())
    carrier = (FIXTURE / "carrier").resolve()
    raw = json.dumps(payload, sort_keys=True).replace("@fixture:carrier@", str(carrier))
    payload = json.loads(raw)
    reason = payload["scoped_out"]["a.c"]
    for record in payload["results"]:
        if record.get("check") == "a.c":
            record["evidence"] = "SCOPED_OUT: " + reason
    independent.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    honest_doc = json.loads((FIXTURE / "honest-scope.json").read_text())
    planted_doc = json.loads((FIXTURE / "scope.json").read_text())
    for document in (honest_doc, planted_doc):
        document["probe_contract"]["target"] = str(carrier)
    honest_scope.write_text(json.dumps(honest_doc, indent=2, sort_keys=True) + "\n")
    planted_scope.write_text(json.dumps(planted_doc, indent=2, sort_keys=True) + "\n")
    honest_sha, planted_sha = sha(honest_scope.read_bytes()), sha(planted_scope.read_bytes())

    process_plain = CASES / "process-plain-planted"
    process_plain_scope = process_plain / SCOPE_REL
    process_plain_scope.parent.mkdir(parents=True)
    process_plain_scope.write_bytes(planted_scope.read_bytes())
    process_file_link = CASES / "process-symlinked-file"
    process_file_scope = process_file_link / SCOPE_REL
    process_file_scope.parent.mkdir(parents=True)
    process_file_scope.symlink_to(planted_scope.resolve())
    process_dir_link = CASES / "process-symlinked-directory"
    process_dir_link.mkdir()
    (process_dir_link / "verifiers").symlink_to((process_plain / "verifiers").resolve(),
                                                   target_is_directory=True)

    cli_honest = CASES / "cli-honest-root"
    cli_honest_scope = cli_honest / SCOPE_REL
    cli_honest_scope.parent.mkdir(parents=True)
    cli_honest_scope.write_bytes(honest_scope.read_bytes())
    cli_planted = CASES / "cli-planted-root"
    cli_planted_scope = cli_planted / SCOPE_REL
    cli_planted_scope.parent.mkdir(parents=True)
    cli_planted_scope.write_bytes(planted_scope.read_bytes())
    cli_file_link = CASES / "cli-symlinked-file-root"
    cli_file_scope = cli_file_link / SCOPE_REL
    cli_file_scope.parent.mkdir(parents=True)
    cli_file_scope.symlink_to(planted_scope.resolve())
    cli_dir_link = CASES / "cli-symlinked-directory-root"
    cli_dir_link.mkdir()
    (cli_dir_link / "verifiers").symlink_to((process_plain / "verifiers").resolve(),
                                                target_is_directory=True)
    cli_root_alias = CASES / "cli-root-symlink"
    cli_root_alias.symlink_to(cli_file_link.resolve(), target_is_directory=True)
    absolute_scope_link = process_file_scope

    cases = [
        run_case("relative-arg-from-planted-process-cwd", process_plain, cli_honest,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("relative-arg-through-process-symlink-file", process_file_link, cli_honest,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("relative-arg-through-process-symlink-directory", process_dir_link, cli_honest,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("relative-arg-selects-cli-cwd-planted-scope", cli_planted, cli_planted,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("symlink-file-inside-cli-cwd", cli_file_link, cli_file_link,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("symlink-directory-inside-cli-cwd", cli_dir_link, cli_dir_link,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("symlinked-cli-cwd-root", cli_root_alias, cli_root_alias,
                 str(SCOPE_REL), independent, comparator, live),
        run_case("absolute-symlink-argument", process_plain, cli_honest,
                 str(absolute_scope_link.absolute()), independent, comparator, live),
        run_case("absolute-honest-arg-overrides-planted-cli-cwd", cli_planted, cli_planted,
                 str(honest_scope.resolve()), independent, comparator, live),
    ]
    by_name = {case["name"]: case for case in cases}
    for name in ("relative-arg-from-planted-process-cwd",
                 "relative-arg-through-process-symlink-file",
                 "relative-arg-through-process-symlink-directory",
                 "absolute-honest-arg-overrides-planted-cli-cwd"):
        case = by_name[name]
        if case["exit"] != 2 or "laundering" not in case["stderr"]:
            raise RuntimeError(f"expected honest scope rejection for {name}: {case}")
        if case["enforced_scope_sha256"] != honest_sha:
            raise RuntimeError(f"wrong scope was resolved for {name}: {case}")
    for name in ("relative-arg-selects-cli-cwd-planted-scope", "symlink-file-inside-cli-cwd",
                 "symlink-directory-inside-cli-cwd", "symlinked-cli-cwd-root",
                 "absolute-symlink-argument"):
        case = by_name[name]
        if case["exit"] != 0 or case["headline"]["n"] != 1:
            raise RuntimeError(f"expected explicit planted-scope agreement for {name}: {case}")
        if case["enforced_scope_sha256"] != planted_sha:
            raise RuntimeError(f"wrong planted scope was resolved for {name}: {case}")
        if case["receipt_scope"]["sha256"] != planted_sha:
            raise RuntimeError(f"receipt digest differs from enforced scope for {name}: {case}")
        if case["receipt_scope"]["path"] != case["resolved_path_expected"]:
            raise RuntimeError(f"receipt path differs from enforced path for {name}: {case}")

    finished = identity()
    if started["head"] != finished["head"] or started["tree"] != finished["tree"]:
        raise RuntimeError("HEAD/tree changed during candidate fixture replay")
    result = {
        "measurement": {"started": started, "finished": finished},
        "candidate": {"source": str(SOURCE), "snapshot": str(comparator),
                      "sha256": sha(comparator_bytes)},
        "fixture": {"path": str(FIXTURE),
                    "live_sha256": sha(live.read_bytes()),
                    "independent_sha256": sha(independent.read_bytes()),
                    "honest_scope_sha256": honest_sha,
                    "planted_scope_sha256": planted_sha,
                    "carrier": str(carrier)},
        "cases": cases,
    }
    result_path = OUTPUTS / "candidate-fixture-scope-path-results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "result": str(result_path), "result_sha256": sha(result_path.read_bytes()),
        "candidate_sha256": sha(comparator_bytes),
        "cases": [{"name": c["name"], "exit": c["exit"],
                   "headline": c["headline"], "receipt_scope": c["receipt_scope"]}
                  for c in cases],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
