#!/usr/bin/env python3
"""Run one Round 46 C1 scope-file CWD arm against a selected comparator."""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

FROZEN_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
COMMITTED_SHA = "ccf41c23d2c766124b27f60653508cd1590aa625cbf8afd8da68b56f7b5bc04d"
WORKTREE_SHA = "778b367e5e5f94fc90132f4070aec3e2395b26914a1d0a50a188558c55cff332"
SCOPE_REL = Path("verifiers/harness-independent-scope.json")
SNAPSHOT_HOME = Path("/var/tmp/kotoba-r46-home")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return digest(Path(path).read_bytes())


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


def prepare(root, scratch, committed_comparator):
    data = scratch / "scope-cwd"
    carrier = data / "carrier"
    carrier.mkdir(parents=True, exist_ok=True)
    files = (
        ("first.jsonl", '{"ts":"2026-10-01T00:00:00Z","skills":"<skills>\\n- alpha\\n</skills>"}\n'),
        ("second.jsonl", '{"ts":"2026-10-02T00:00:00Z","skills":"<skills>\\n- alpha\\n- beta\\n</skills>"}\n'),
    )
    for name, text in files:
        (carrier / name).write_text(text, encoding="utf-8")
    for index, path in enumerate(sorted(carrier.glob("*.jsonl"))):
        stamp = 1_700_000_000_000_000_000 + index * 1_000_000_000
        os.utime(path, ns=(stamp, stamp))

    module = {"__name__": "c1_probe_module", "__file__": str(committed_comparator)}
    source = Path(committed_comparator).read_bytes()
    exec(compile(source, str(committed_comparator), "exec"), module)
    probe = module["recompute_probe"]({"kind": "rule-spread-census",
                                        "target": str(carrier.resolve())})
    scoped_probe = {"kind": "rule-spread-census", "target": str(carrier.resolve()),
                    "observable": probe["observable"]}
    live = write_json(data / "live.json", {"results": [
        {"check": "a.b", "observed": 7, "mode": "equal", "verdict": "PASS"},
        {"check": "a.c", "observed": None, "mode": "equal", "verdict": "PASS"},
    ]})
    independent = write_json(data / "independent.json", {
        "results": [
            {"check": "a.b", "re_derived": 7, "status": "DERIVED"},
            {"check": "a.c", "re_derived": None, "status": "SCOPED_OUT",
             "reason": "payload blocker", "evidence": "SCOPED_OUT: payload blocker",
             "probe": scoped_probe},
        ],
        "scoped_out": {"a.c": "payload blocker"},
        "scoped_out_probes": {"a.c": scoped_probe},
    })
    committed = json.loads((root / SCOPE_REL).read_text(encoding="utf-8"))
    planted = json.loads(json.dumps(committed))
    planted["scope_out"]["a.c"] = {"kind": "rule-in-author-scope",
                                    "reason": "payload blocker"}
    planted["probe_contract"] = {"kind": "rule-spread-census",
                                  "target": str(carrier.resolve())}
    planted_cwd = data / "planted-cwd"
    planted_scope = write_json(planted_cwd / SCOPE_REL, planted)
    base_keys = set(committed["scope_out"])
    planted_keys = set(planted["scope_out"])
    if not base_keys < planted_keys or "a.c" in base_keys:
        raise RuntimeError("planted scope is not a strict superset of committed scope rows")
    if len(probe["observable"].get("distinct_totals", [])) < 2:
        raise RuntimeError("probe carrier is vacuous")
    return {
        "live": live, "independent": independent, "carrier": carrier,
        "planted_cwd": planted_cwd, "planted_scope": planted_scope,
        "base_scope_keys": sorted(base_keys), "planted_scope_keys": sorted(planted_keys),
        "extra_scope_keys": sorted(planted_keys - base_keys),
        "probe_observable": probe["observable"],
    }


def classify_stderr(text):
    error = re.search(r"compare_harness_independent: ERROR:\s*([A-Za-z][A-Za-z0-9_-]*)", text)
    if error:
        return error.group(1)
    return "receipt-notice" if text.strip().startswith("receipt:") else ("none" if not text.strip() else "other")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worktree", type=Path, required=True)
    parser.add_argument("--scratch", type=Path, default=Path("/tmp/kotoba-r46-c1b"))
    parser.add_argument("--comparator", type=Path, required=True)
    parser.add_argument("--source", choices=("frozen", "committed", "worktree"), required=True)
    parser.add_argument("--arm", choices=("planted-relative", "absolute-control"), required=True)
    parser.add_argument("--committed-source", type=Path, default=None)
    args = parser.parse_args()
    os.environ["HOME"] = str(SNAPSHOT_HOME)
    root, scratch = args.worktree.resolve(), args.scratch.resolve()
    comparator = args.comparator.resolve()
    committed_comparator = (args.committed_source.resolve() if args.committed_source
                            else root / "verifiers/compare_harness_independent.py")
    actual_sha = file_sha(comparator)
    expected_sha = {"frozen": FROZEN_SHA, "committed": COMMITTED_SHA,
                    "worktree": WORKTREE_SHA}[args.source]
    if actual_sha != expected_sha:
        raise RuntimeError(f"{args.source} comparator SHA mismatch: {actual_sha}")
    if file_sha(committed_comparator) != COMMITTED_SHA:
        raise RuntimeError("committed source is not the pinned HEAD comparator bytes")

    inputs = prepare(root, scratch, committed_comparator)
    process_cwd = inputs["planted_cwd"].resolve()
    scope_argument = ("verifiers/harness-independent-scope.json"
                      if args.arm == "planted-relative"
                      else str(inputs["planted_scope"].resolve()))
    if args.arm == "absolute-control" and args.source == "frozen":
        raise RuntimeError("the absolute-path control requires the committed-after implementation")
    receipt_path = scratch / "receipts" / f"{args.source}-{args.arm}.receipt.json"
    argv = [sys.executable, "-B", str(comparator),
            "--live-json", str(inputs["live"].resolve()),
            "--independent-json", str(inputs["independent"].resolve()),
            "--expect-n", "2", "--cwd", str(root),
            "--scope-file", scope_argument, "--no-stamp", "--json",
            "--receipt", str(receipt_path.resolve())]

    enforced = Path(scope_argument)
    if not enforced.is_absolute():
        enforced = process_cwd / enforced if args.source == "frozen" else root / enforced
    enforced = enforced.resolve()
    hash_before = file_sha(enforced)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["HOME"] = str(SNAPSHOT_HOME)
    proc = subprocess.run(argv, cwd=process_cwd, env=env, capture_output=True, timeout=300)
    stdout_path = scratch / "raw" / f"{args.source}-{args.arm}.stdout"
    stderr_path = scratch / "raw" / f"{args.source}-{args.arm}.stderr"
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stdout_path.write_bytes(proc.stdout)
    stderr_path.write_bytes(proc.stderr)
    stderr = proc.stderr.decode("utf-8", errors="replace").strip()
    try:
        report = json.loads(proc.stdout.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        report = None
    receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.is_file() else None
    receipt_scope = receipt.get("scope_file") if isinstance(receipt, dict) else None
    if args.source == "frozen" and not Path(scope_argument).is_absolute():
        expected_receipt_scope = {"path": scope_argument, "sha256": file_sha(root / scope_argument)}
    else:
        expected_receipt_scope = {"path": str(enforced), "sha256": file_sha(enforced)}
    result = {
        "source": args.source, "arm": args.arm,
        "comparator_path": str(comparator), "comparator_sha256": actual_sha,
        "argv": argv, "process_cwd": str(process_cwd), "cwd_argument": str(root),
        "comparator_home": str(SNAPSHOT_HOME),
        "probe_rederivation_home": str(SNAPSHOT_HOME),
        "scope_argument": scope_argument, "exit": proc.returncode,
        "stderr_class": classify_stderr(stderr), "stderr": stderr,
        "stderr_sha256": digest(proc.stderr), "stdout_sha256": digest(proc.stdout),
        "stdout_path": str(stdout_path), "stderr_path": str(stderr_path),
        "receipt_path_requested": str(receipt_path.resolve()),
        "receipt_emitted": receipt is not None,
        "receipt_sha256": file_sha(receipt_path) if receipt is not None else None,
        "receipt_scope": receipt_scope,
        "receipt_scope_expected_if_not_emitted": expected_receipt_scope,
        "enforced_file": {"path": str(enforced), "sha256_before": hash_before,
                          "sha256_after": file_sha(enforced)},
        "report": ({"head": report.get("head"), "exit": report.get("exit"),
                    "reason": report.get("reason"), "headline": report.get("headline"),
                    "agreement": report.get("agreement")} if isinstance(report, dict) else None),
        "input_sha256": {"live": file_sha(inputs["live"]),
                          "independent": file_sha(inputs["independent"])},
        "planted_scope": {
            "path": str(inputs["planted_scope"].resolve()),
            "sha256": file_sha(inputs["planted_scope"]),
            "base_scope_out_keys": inputs["base_scope_keys"],
            "planted_scope_out_keys": inputs["planted_scope_keys"],
            "extra_scope_out_keys": inputs["extra_scope_keys"],
            "strict_superset": True,
            "probe_observable": inputs["probe_observable"],
        },
    }
    result_path = scratch / "results" / f"{args.source}-{args.arm}.json"
    write_json(result_path, result)
    result["result_path"] = str(result_path)
    result["result_sha256"] = file_sha(result_path)
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
