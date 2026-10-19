#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
FIXTURE = ROOT / "verifiers/fixtures/compare-harness-independent/scope-file-cwd"
EVIDENCE = Path(__file__).resolve().parent
FROZEN_REV = "055d3b9"
FROZEN_SHA256 = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
RELATIVE_SCOPE = "verifiers/harness-independent-scope.json"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def materialize(value, carrier):
    if isinstance(value, dict):
        return {key: materialize(child, carrier) for key, child in value.items()}
    if isinstance(value, list):
        return [materialize(child, carrier) for child in value]
    if value == "@fixture:carrier@":
        return str(carrier)
    return value


def frozen_source():
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         f"{FROZEN_REV}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True,
    )
    digest = sha256(proc.stdout)
    if digest != FROZEN_SHA256:
        raise RuntimeError(f"frozen comparator digest mismatch: {digest}")
    return proc.stdout


def run(argv, process_cwd, label, driver=None):
    command = ([sys.executable, str(COMPARATOR)] if driver is None else
               [sys.executable, "-c", driver]) + argv
    proc = subprocess.run(command, cwd=process_cwd, capture_output=True, text=True)
    parsed = None
    try:
        parsed = json.loads(proc.stdout)
    except ValueError:
        pass
    return {
        "label": label,
        "command": command,
        "process_cwd": str(process_cwd),
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "json": parsed,
    }


def main():
    now = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                         check=True, capture_output=True, text=True).stdout.strip()
    tree = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD^{tree}"],
                          check=True, capture_output=True, text=True).stdout.strip()
    frozen = frozen_source()
    current = COMPARATOR.read_bytes()
    planted_fixture = FIXTURE / "planted-cwd"
    carrier = (FIXTURE / "carrier").resolve()
    payload = json.loads((FIXTURE / "independent.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="P1-scope-cwd-", dir=EVIDENCE) as tmp:
        tmp = Path(tmp)
        planted = tmp / "planted-cwd"
        planted_scope = planted / RELATIVE_SCOPE
        planted_scope.parent.mkdir(parents=True)
        planted_document = json.loads(
            (planted_fixture / RELATIVE_SCOPE).read_text(encoding="utf-8"))
        planted_scope.write_text(json.dumps(materialize(planted_document, carrier)),
                                 encoding="utf-8")
        independent = tmp / "independent.json"
        independent.write_text(json.dumps(materialize(payload, carrier)), encoding="utf-8")
        honest_cwd = tmp / "honest-cwd"
        scope_path = honest_cwd / RELATIVE_SCOPE
        scope_path.parent.mkdir(parents=True)
        scope_path.write_bytes((FIXTURE / "honest-scope.json").read_bytes())
        baseline_receipt = tmp / "baseline-receipt.json"
        candidate_receipt = tmp / "candidate-receipt.json"
        control_receipt = tmp / "control-receipt.json"
        common = [
            "--live-json", str((FIXTURE / "live.json").resolve()),
            "--independent-json", str(independent.resolve()),
            "--expect-n", "2",
            "--scope-file", RELATIVE_SCOPE,
            "--no-stamp", "--json",
        ]
        baseline_argv = common + ["--cwd", str(honest_cwd.resolve()),
                                  "--receipt", str(baseline_receipt)]
        driver = (
            "import hashlib,subprocess,sys\n"
            f"root={str(ROOT)!r}\n"
            f"expected={FROZEN_SHA256!r}\n"
            "source=subprocess.run(['git','-C',root,'show',"
            f"{(FROZEN_REV + ':verifiers/compare_harness_independent.py')!r}],"
            "check=True,capture_output=True).stdout\n"
            "actual=hashlib.sha256(source).hexdigest()\n"
            "if actual!=expected: raise SystemExit('frozen digest mismatch: '+actual)\n"
            f"filename={str(COMPARATOR)!r}\n"
            "exec(compile(source,filename,'exec'),"
            "{'__name__':'__main__','__file__':filename})\n"
        )
        baseline = run(baseline_argv, planted, "frozen-055d3b9", driver)

        candidate_argv = common + ["--cwd", str(honest_cwd.resolve()),
                                   "--receipt", str(candidate_receipt)]
        candidate = run(candidate_argv, planted, "worktree-candidate")
        control_argv = common + ["--cwd", str(planted.resolve()),
                                 "--receipt", str(control_receipt)]
        control = run(control_argv, planted, "planted-scope-control")

        baseline_receipt_json = (json.loads(baseline_receipt.read_text())
                                 if baseline_receipt.is_file() else None)
        candidate_receipt_json = (json.loads(candidate_receipt.read_text())
                                  if candidate_receipt.is_file() else None)
        control_receipt_json = (json.loads(control_receipt.read_text())
                                if control_receipt.is_file() else None)
        enforced_planted = planted / RELATIVE_SCOPE
        record = {
            "recorded_at_utc": now,
            "phase": sys.argv[1] if len(sys.argv) > 1 else "unspecified",
            "head": head,
            "head_tree": tree,
            "frozen_revision": FROZEN_REV,
            "frozen_comparator_sha256": sha256(frozen),
            "worktree_comparator_sha256": sha256(current),
            "fixture_sha256": {
                path.relative_to(FIXTURE).as_posix(): sha256(path.read_bytes())
                for path in sorted(FIXTURE.rglob("*")) if path.is_file()
            },
            "honest_scope_path": str(scope_path.resolve()),
            "honest_scope_sha256": sha256(scope_path.read_bytes()),
            "planted_scope_path": str(enforced_planted.resolve()),
            "planted_scope_sha256": sha256(enforced_planted.read_bytes()),
            "runs": {
                "frozen": baseline,
                "candidate": candidate,
                "planted_control": control,
            },
            "receipts": {
                "frozen": baseline_receipt_json,
                "candidate": candidate_receipt_json,
                "planted_control": control_receipt_json,
            },
            "expected": {
                "frozen_exit": 0,
                "candidate_exit": 2,
                "candidate_error_class": "laundering",
                "planted_control_exit": 0,
                "planted_control_receipt_path": str(enforced_planted.resolve()),
                "planted_control_receipt_sha256": sha256(enforced_planted.read_bytes()),
            },
        }
        print(json.dumps(record, indent=2, sort_keys=True))
        if len(sys.argv) > 2:
            Path(sys.argv[2]).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n",
                                         encoding="utf-8")


if __name__ == "__main__":
    main()
