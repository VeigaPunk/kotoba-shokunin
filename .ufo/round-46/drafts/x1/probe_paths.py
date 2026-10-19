#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
COMPARATOR = ROOT / "verifiers" / "compare_harness_independent.py"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return sha(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n",
                    encoding="utf-8")


def committed_scope(path, include_row=True, marker=""):
    row = {"kind": "rule-in-author-scope", "reason": "scope fixture"}
    value = {
        "schema": "kotoba-harness-independent-scope-v1",
        "probe_contract": {"kind": "rule-spread-census"},
        "scope_out": {"a.b": row} if include_row else {},
    }
    if marker:
        value["fixture_marker"] = marker
    write_json(path, value)


def main():
    started = datetime.now(timezone.utc).isoformat()
    baseline_rev = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
    baseline_blob = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         baseline_rev + ":verifiers/compare_harness_independent.py"],
        capture_output=True, check=True,
    ).stdout
    baseline_sha = sha(baseline_blob)
    head_before = git("rev-parse", "HEAD")
    tree_before = git("rev-parse", "HEAD^{tree}")
    worktree_source_before = file_sha(COMPARATOR)
    worktree_before = git("status", "--porcelain=v1")

    with tempfile.TemporaryDirectory(prefix="x1-paths-", dir=Path(__file__).resolve().parent) as temp:
        base = Path(temp)
        frozen_comparator = base / "compare_harness_independent.py"
        frozen_comparator.write_bytes(baseline_blob)
        spec = importlib.util.spec_from_file_location("round46_comparator", frozen_comparator)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        carrier = base / "carrier"
        carrier.mkdir()
        for name, stamp, entries, mtime in (
            ("a.jsonl", "2026-01-01T00:00:00.000Z", 1, 1_700_000_000),
            ("b.jsonl", "2026-02-02T00:00:00.000Z", 4, 1_700_000_002),
        ):
            block = "\n".join("- entry %d" % index for index in range(entries))
            path = carrier / name
            path.write_text(json.dumps({"stamp": stamp, "text": "<skills>\n" + block + "\n</skills>"}) + "\n",
                            encoding="utf-8")
            os.utime(path, (mtime, mtime))
        probe_result = module.recompute_probe({"kind": "rule-spread-census", "target": str(carrier)})
        probe = {"kind": "rule-spread-census", "target": str(carrier),
                 "observable": probe_result["observable"]}
        live = base / "live.json"
        independent = base / "independent.json"
        write_json(live, {"results": [{"check": "a.b", "observed": 1,
                                        "verdict": "PASS", "mode": "equal"}]})
        row = {"check": "a.b", "expected": None, "re_derived": None,
               "value": None, "status": "SCOPED_OUT", "probe": probe}
        write_json(independent, {
            "results": [row],
            "rows": [dict(row)],
            "checks": {"a.b": None},
            "scoped_out": {"a.b": "fixture blocker"},
            "scoped_out_probes": {"a.b": probe},
        })

        outside = base / "outside"
        outside.mkdir()
        external_scope = outside / "planted.json"
        committed_scope(external_scope, include_row=True, marker="outside")
        honest_scope = outside / "honest.json"
        committed_scope(honest_scope, include_row=False, marker="honest")

        link_file = base / "scope-link.json"
        link_file.symlink_to(external_scope)
        target_dir = base / "scope-target-dir"
        target_dir.mkdir()
        dir_scope = target_dir / "scope.json"
        committed_scope(dir_scope, include_row=True, marker="symlink-dir")
        link_dir = base / "scope-dir-link"
        link_dir.symlink_to(target_dir, target_is_directory=True)

        process_cwd = base / "process-cwd"
        cwd_root = base / "report-cwd"
        rel = Path("verifiers") / "harness-independent-scope.json"
        planted_relative = process_cwd / rel
        honest_relative = cwd_root / rel
        planted_relative.parent.mkdir(parents=True)
        honest_relative.parent.mkdir(parents=True)
        committed_scope(planted_relative, include_row=True, marker="process-cwd")
        committed_scope(honest_relative, include_row=False, marker="cwd-receipt")

        def run_case(name, scope_arg, process_dir, cwd_arg, enforced_path, receipt_path):
            receipt_path = Path(receipt_path)
            argv = [
                sys.executable, str(frozen_comparator),
                "--live-json", str(live),
                "--independent-json", str(independent),
                "--expect-n", "1",
                "--cwd", str(cwd_arg),
                "--scope-file", str(scope_arg),
                "--no-stamp", "--json",
                "--receipt", str(receipt_path),
            ]
            proc = subprocess.run(argv, cwd=process_dir, capture_output=True,
                                  text=True, timeout=120)
            report = json.loads(proc.stdout) if proc.stdout.strip() else {}
            receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else {}
            resolved_enforced = Path(enforced_path).resolve()
            receipt_scope = receipt.get("scope_file", {})
            return {
                "case": name,
                "argv": argv,
                "process_cwd": str(process_dir),
                "cwd_arg": str(cwd_arg),
                "scope_arg": str(scope_arg),
                "exit": proc.returncode,
                "headline": report.get("headline"),
                "n_scoped_out": report.get("agreement", {}).get("n_scoped_out"),
                "committed_set_in_receipt": receipt.get("scope_locks", {}).get("committed_set"),
                "enforced_path_argument_resolves_to": str(resolved_enforced),
                "enforced_scope_sha256": file_sha(resolved_enforced),
                "receipt_scope_path": receipt_scope.get("path"),
                "receipt_scope_sha256": receipt_scope.get("sha256"),
                "receipt_matches_enforced_bytes": receipt_scope.get("sha256") == file_sha(resolved_enforced),
                "stderr": proc.stderr.strip(),
            }

        results = [
            run_case("absolute-symlinked-scope-file", link_file, ROOT, ROOT,
                     link_file, base / "receipt-link-file.json"),
            run_case("scope-file-through-symlinked-directory", link_dir / "scope.json", ROOT, ROOT,
                     dir_scope, base / "receipt-link-dir.json"),
            run_case("relative-scope-arg-process-cwd-vs--cwd", str(rel), process_cwd, cwd_root,
                     planted_relative, base / "receipt-cwd-split.json"),
            run_case("absolute-scope-outside-repo", external_scope, ROOT, ROOT,
                     external_scope, base / "receipt-outside.json"),
        ]
        input_hashes = {"live": file_sha(live), "independent": file_sha(independent)}

    finished = datetime.now(timezone.utc).isoformat()
    print(json.dumps({
        "started_at": started,
        "finished_at": finished,
        "baseline_revision": baseline_rev,
        "head_before": head_before,
        "tree_before": tree_before,
        "head_after": git("rev-parse", "HEAD"),
        "tree_after": git("rev-parse", "HEAD^{tree}"),
        "baseline_comparator_sha256_before": baseline_sha,
        "baseline_comparator_sha256_after": sha(baseline_blob),
        "worktree_comparator_sha256_before": worktree_source_before,
        "worktree_comparator_sha256_after": file_sha(COMPARATOR),
        "runner_sha256": file_sha(__file__),
        "worktree_status_before": worktree_before,
        "worktree_status_after": git("status", "--porcelain=v1"),
        "probe_observable": probe["observable"],
        "input_sha256": input_hashes,
        "results": results,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
