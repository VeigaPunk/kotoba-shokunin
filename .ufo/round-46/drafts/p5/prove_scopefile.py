#!/usr/bin/env python3
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ARTIFACT_DIR = Path(__file__).resolve().parent
PATCH_PATH = ARTIFACT_DIR / "scopefile-parse-time-absolute.patch"
RESULT_PATH = ARTIFACT_DIR / "scopefile-proof.json"
BASE_REF = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
BASE_TREE = "e8dced184612a9738c5b8d244a0837fbd955a7da"
BASE_SOURCE = "verifiers/compare_harness_independent.py"
EXPECTED_SOURCE_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
RELATIVE_SCOPE = "verifiers/harness-independent-scope.json"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def import_driver(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(driver_path, process_cwd, inputs, receipt_path=None, cwd_arg=None):
    cwd_arg = cwd_arg or ROOT
    argv = [
        sys.executable,
        str(driver_path),
        "--live-json", str(inputs["live"]),
        "--independent-json", str(inputs["independent"]),
        "--expect-n", "2",
        "--cwd", str(cwd_arg),
        "--scope-file", RELATIVE_SCOPE,
        "--no-stamp",
    ]
    if receipt_path is not None:
        argv += ["--receipt", str(receipt_path)]
    proc = subprocess.run(
        argv,
        cwd=process_cwd,
        capture_output=True,
        text=True,
        timeout=120,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    return {
        "argv": argv,
        "process_cwd": str(process_cwd),
        "cwd_arg": str(cwd_arg),
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "receipt": json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt_path is not None and receipt_path.is_file()
        else None,
    }


def run_self_test(driver_path):
    proc = subprocess.run(
        [sys.executable, str(driver_path), "--self-test"],
        cwd=driver_path.parent.parent,
        capture_output=True,
        text=True,
        timeout=300,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    lines = proc.stdout.splitlines()
    return {
        "exit": proc.returncode,
        "summary": next((line for line in lines if line.startswith("self-test:")), ""),
        "failures": [line for line in lines if "FAILED:" in line],
        "stdout_sha256": sha256(proc.stdout.encode("utf-8")),
        "stderr": proc.stderr,
    }


def main():
    started = datetime.now(timezone.utc).isoformat()
    head_start = git("rev-parse", "HEAD")
    tree_start = git("rev-parse", "HEAD^{tree}")
    claims_sha_start = sha256((ROOT / ".ufo/round-46/claims.json").read_bytes())
    live_source_sha_start = sha256((ROOT / BASE_SOURCE).read_bytes())
    assert head_start == BASE_REF, ("unexpected HEAD", head_start)
    assert tree_start == BASE_TREE, ("unexpected committed tree", tree_start)

    frozen = subprocess.run(
        ["git", "show", f"{BASE_REF}:{BASE_SOURCE}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    assert sha256(frozen) == EXPECTED_SOURCE_SHA, sha256(frozen)
    patch_bytes = PATCH_PATH.read_bytes()

    with tempfile.TemporaryDirectory(prefix="p5-scope-proof-", dir=ARTIFACT_DIR) as tmp:
        work = Path(tmp)
        before_root = work / "before"
        after_root = work / "after"
        before_driver = before_root / BASE_SOURCE
        after_driver = after_root / BASE_SOURCE
        before_driver.parent.mkdir(parents=True)
        after_driver.parent.mkdir(parents=True)
        before_driver.write_bytes(frozen)
        after_driver.write_bytes(frozen)

        patch_result = subprocess.run(
            ["patch", "--batch", "--forward", "-p1"],
            cwd=after_root,
            input=patch_bytes.decode("utf-8"),
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert patch_result.returncode == 0, patch_result.stdout + patch_result.stderr
        patched_bytes = after_driver.read_bytes()
        fixture_archive = subprocess.run(
            [
                "git", "archive", BASE_REF,
                "verifiers/fixtures/compare-harness-independent",
                "verifiers/harness-independent-scope.json",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        for test_root in (before_root, after_root):
            with tarfile.open(fileobj=io.BytesIO(fixture_archive), mode="r:") as archive:
                archive.extractall(path=test_root, filter="data")
        before_self_test = run_self_test(before_driver)
        after_self_test = run_self_test(after_driver)
        expected_self_test = "self-test: 0 failure(s) over 255 assertions"
        assert before_self_test["exit"] == 0 and before_self_test["summary"] == expected_self_test, before_self_test
        assert after_self_test["exit"] == 0 and after_self_test["summary"] == expected_self_test, after_self_test

        inputs_root = work / "inputs"
        cwd_root = work / "cwd-root"
        frozen_scope_path = cwd_root / RELATIVE_SCOPE
        frozen_scope_path.parent.mkdir(parents=True)
        frozen_scope_bytes = subprocess.run(
            ["git", "show", f"{BASE_REF}:{RELATIVE_SCOPE}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        ).stdout
        frozen_scope_path.write_bytes(frozen_scope_bytes)
        honest_scope_sha = sha256(frozen_scope_bytes)
        planted_cwd = inputs_root / "planted-cwd"
        planted_scope_path = planted_cwd / RELATIVE_SCOPE
        carrier = inputs_root / "carrier"
        planted_scope_path.parent.mkdir(parents=True)
        carrier.mkdir(parents=True)

        first = carrier / "a.jsonl"
        last = carrier / "z.jsonl"
        first.write_text(
            '{"stamp":"2026-01-01T00:00:00.000Z","text":"<skills>\n- a\n- b\n</skills>"}\n',
            encoding="utf-8",
        )
        last.write_text(
            '{"stamp":"2026-02-02T00:00:00.000Z","text":"<skills>\n- a\n- b\n- c\n- d\n- e\n</skills>"}\n',
            encoding="utf-8",
        )
        now = 1_800_000_000
        os.utime(first, (now + 20, now + 20))
        os.utime(last, (now + 10, now + 10))
        observable = {
            "session_files": 2,
            "files_with_skills_block": 2,
            "candidate_blocks": 2,
            "distinct_totals": [2, 5],
            "rule_totals": {
                "newest-mtime": 2,
                "newest-iso-stamp": 5,
                "first-in-scan-order": 2,
                "last-in-scan-order": 5,
                "newest-nonempty": 2,
            },
        }
        probe = {
            "kind": "rule-spread-census",
            "target": str(carrier.resolve()),
            "observable": observable,
        }
        planted_scope = {
            "schema": "kotoba-harness-independent-scope-v1",
            "probe_contract": {"kind": "rule-spread-census"},
            "scope_out": {
                "a.out": {
                    "kind": "rule-in-author-scope",
                    "reason": "P5 isolated relative-path proof row",
                }
            },
        }
        planted_scope_path.write_text(
            json.dumps(planted_scope, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        live_path = inputs_root / "live.json"
        live_path.write_text(
            json.dumps(
                {
                    "results": [
                        {"check": "a.in", "observed": 1, "verdict": "PASS", "mode": "equal"},
                        {"check": "a.out", "observed": 1, "verdict": "PASS", "mode": "equal"},
                    ]
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        valid_live_path = inputs_root / "live-valid.json"
        valid_live_path.write_text(
            json.dumps(
                {
                    "results": [
                        {"check": "a.in", "observed": 1, "verdict": "PASS", "mode": "equal"},
                        {"check": "b.in", "observed": 1, "verdict": "PASS", "mode": "equal"},
                    ]
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        independent_path = inputs_root / "independent.json"
        independent_path.write_text(
            json.dumps(
                {
                    "results": [
                        {"check": "a.in", "expected": 1, "status": "DERIVED"},
                        {
                            "check": "a.out",
                            "expected": None,
                            "status": "SCOPED_OUT",
                            "probe": probe,
                        },
                    ],
                    "scoped_out": {"a.out": "P5 isolated relative-path proof row"},
                    "scoped_out_probes": {"a.out": probe},
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        valid_independent_path = inputs_root / "independent-valid.json"
        valid_independent_path.write_text(
            json.dumps(
                {
                    "results": [
                        {"check": "a.in", "expected": 1, "status": "DERIVED"},
                        {"check": "b.in", "expected": 1, "status": "DERIVED"},
                    ]
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        input_hashes = {
            "live": sha256(live_path.read_bytes()),
            "live_valid": sha256(valid_live_path.read_bytes()),
            "independent": sha256(independent_path.read_bytes()),
            "independent_valid": sha256(valid_independent_path.read_bytes()),
            "honest_scope": sha256(frozen_scope_path.read_bytes()),
            "planted_scope": sha256(planted_scope_path.read_bytes()),
            "carrier_a": sha256(first.read_bytes()),
            "carrier_z": sha256(last.read_bytes()),
        }
        honest_scope_sha = input_hashes["honest_scope"]
        planted_scope_sha = input_hashes["planted_scope"]
        assert honest_scope_sha != planted_scope_sha

        before_module = import_driver(before_driver, "p5_before_driver")
        after_module = import_driver(after_driver, "p5_after_driver")
        original_cwd = os.getcwd()
        try:
            os.chdir(planted_cwd)
            before_relative_read = before_module.load_scope_file(RELATIVE_SCOPE)[0]
            try:
                after_module.load_scope_file(RELATIVE_SCOPE)
                after_relative_read = {"accepted": True, "error": None}
            except after_module.CompareError as exc:
                after_relative_read = {"accepted": False, "error": str(exc)}
        finally:
            os.chdir(original_cwd)

        before_receipt_path = work / "before-receipt.json"
        after_receipt_path = work / "after-receipt.json"
        before_attack = run_case(
            before_driver, planted_cwd,
            {"live": live_path, "independent": independent_path},
            before_receipt_path, cwd_arg=cwd_root,
        )
        after_attack = run_case(
            after_driver, planted_cwd,
            {"live": live_path, "independent": independent_path},
            after_receipt_path, cwd_arg=cwd_root,
        )
        before_honest_control = run_case(
            before_driver, cwd_root,
            {"live": live_path, "independent": independent_path}, cwd_arg=cwd_root,
        )
        after_honest_control = run_case(
            after_driver, cwd_root,
            {"live": live_path, "independent": independent_path}, cwd_arg=cwd_root,
        )
        before_valid_receipt_path = work / "before-valid-receipt.json"
        after_valid_receipt_path = work / "after-valid-receipt.json"
        before_valid_control = run_case(
            before_driver, planted_cwd,
            {"live": valid_live_path, "independent": valid_independent_path},
            before_valid_receipt_path, cwd_arg=cwd_root,
        )
        after_valid_control = run_case(
            after_driver, planted_cwd,
            {"live": valid_live_path, "independent": valid_independent_path},
            after_valid_receipt_path, cwd_arg=cwd_root,
        )

        before_receipt = before_attack["receipt"]
        assert before_attack["exit"] == 0 and "agreement: 1/1" in before_attack["stdout"]
        assert after_attack["exit"] == 2 and "laundering" in after_attack["stderr"]
        assert before_receipt["scope_file"]["path"] == RELATIVE_SCOPE
        assert before_receipt["scope_file"]["sha256"] == honest_scope_sha
        assert after_attack["receipt"] is None
        assert before_valid_control["exit"] == 0 and "agreement: 2/2" in before_valid_control["stdout"]
        assert after_valid_control["exit"] == 0 and "agreement: 2/2" in after_valid_control["stdout"]
        before_valid_receipt = before_valid_control["receipt"]
        after_valid_receipt = after_valid_control["receipt"]
        assert before_valid_receipt["scope_file"]["path"] == RELATIVE_SCOPE
        assert before_valid_receipt["scope_file"]["sha256"] == honest_scope_sha
        assert after_valid_receipt["scope_file"]["path"] == str(frozen_scope_path.resolve())
        assert after_valid_receipt["scope_file"]["sha256"] == honest_scope_sha
        assert before_honest_control["exit"] == 2 and "laundering" in before_honest_control["stderr"]
        assert after_honest_control["exit"] == 2 and "laundering" in after_honest_control["stderr"]
        assert sorted(before_relative_read) == ["a.out"]
        assert not after_relative_read["accepted"] and "absolute" in after_relative_read["error"]

        proof = {
            "artifact": "P5 parse-time absolute scope path proof",
            "command": "PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/p5/prove_scopefile.py",
            "started_at_utc": started,
            "finished_at_utc": datetime.now(timezone.utc).isoformat(),
            "base": {
                "ref": BASE_REF,
                "tree": BASE_TREE,
                "source": BASE_SOURCE,
                "source_sha256": sha256(frozen),
                "claims_sha256": claims_sha_start,
            },
            "patch": {
                "path": str(PATCH_PATH.relative_to(ROOT)),
                "sha256": sha256(patch_bytes),
                "apply_exit": patch_result.returncode,
                "apply_stdout": patch_result.stdout,
                "apply_stderr": patch_result.stderr,
                "candidate_source_sha256": sha256(patched_bytes),
            },
            "self_test": {
                "command": "python3 -B compare_harness_independent.py --self-test",
                "self_test_inputs_archive_sha256": sha256(fixture_archive),
                "before": before_self_test,
                "after": after_self_test,
            },
            "invocation": {
                "live": "frozen JSON fixture; --live-json",
                "independent": "frozen JSON attack fixture with a recomputable scope-out; --independent-json",
                "cwd_arg": str(cwd_root),
                "scope_arg": RELATIVE_SCOPE,
                "scope_source": f"git show {BASE_REF}:{RELATIVE_SCOPE}",
                "expect_n": 2,
                "input_sha256": input_hashes,
                "honest_scope_sha256": honest_scope_sha,
                "attacker_planted_scope_path": str(planted_scope_path.resolve()),
                "resolved_scope_path_under_cwd": str(frozen_scope_path.resolve()),
            },
            "red_before": {
                "exit": before_attack["exit"],
                "stdout": before_attack["stdout"],
                "stderr": before_attack["stderr"],
                "receipt_scope_path": before_receipt["scope_file"]["path"],
                "receipt_scope_sha256": before_receipt["scope_file"]["sha256"],
                "path_digest_matches_enforced": (
                    before_receipt["scope_file"]["path"] == str(planted_scope_path.resolve())
                    and before_receipt["scope_file"]["sha256"] == planted_scope_sha
                ),
            },
            "green_after": {
                "exit": after_attack["exit"],
                "stdout": after_attack["stdout"],
                "stderr": after_attack["stderr"],
                "class_named_rejection": "laundering" in after_attack["stderr"],
                "receipt_written": after_attack["receipt"] is not None,
            },
            "valid_join_control": {
                "before_exit": before_valid_control["exit"],
                "before_stdout": before_valid_control["stdout"],
                "before_receipt_scope_path": before_valid_receipt["scope_file"]["path"],
                "before_receipt_scope_sha256": before_valid_receipt["scope_file"]["sha256"],
                "after_exit": after_valid_control["exit"],
                "after_stdout": after_valid_control["stdout"],
                "after_receipt_scope_path": after_valid_receipt["scope_file"]["path"],
                "after_receipt_scope_sha256": after_valid_receipt["scope_file"]["sha256"],
                "after_receipt_matches_resolved_scope": (
                    after_valid_receipt["scope_file"]["path"] == str(frozen_scope_path.resolve())
                    and after_valid_receipt["scope_file"]["sha256"] == honest_scope_sha
                ),
            },
            "relative_resolution_check": {
                "before_direct_loader_accepted": sorted(before_relative_read) == ["a.out"],
                "after_direct_loader_accepted": after_relative_read["accepted"],
                "after_error": after_relative_read["error"],
            },
            "honest_scope_control": {
                "before_exit": before_honest_control["exit"],
                "before_stderr": before_honest_control["stderr"],
                "after_exit": after_honest_control["exit"],
                "after_stderr": after_honest_control["stderr"],
            },
            "interpretation": (
                "The draft normalizes --scope-file once after parsing, against the resolved --cwd, "
                "then requires absolute paths in the loader and receipt. The planted-CWD scope "
                "attack flips from exit 0 to class-named laundering exit 2; a valid join remains "
                "2/2 and its receipt names/hashes the resolved honest scope."
            ),
            "worktree_context": {
                "HEAD_start": head_start,
                "tree_start": tree_start,
                "HEAD_end": git("rev-parse", "HEAD"),
                "tree_end": git("rev-parse", "HEAD^{tree}"),
                "live_comparator_sha256_start": live_source_sha_start,
                "live_comparator_sha256_end": sha256((ROOT / BASE_SOURCE).read_bytes()),
            },
        }
        assert proof["red_before"]["path_digest_matches_enforced"] is False
        assert proof["green_after"]["exit"] == 2
        assert proof["green_after"]["class_named_rejection"] is True
        assert proof["green_after"]["receipt_written"] is False
        assert proof["valid_join_control"]["before_exit"] == 0
        assert proof["valid_join_control"]["after_exit"] == 0
        assert proof["valid_join_control"]["after_receipt_matches_resolved_scope"] is True
        assert proof["worktree_context"]["HEAD_end"] == BASE_REF
        assert proof["worktree_context"]["tree_end"] == BASE_TREE
        RESULT_PATH.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(proof, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
