#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = ROOT / ".ufo/round-46/drafts/a2"
EVIDENCE = ROOT / ".ufo/round-46/evidence/a2"
DRIVER = ROOT / ".ufo/round-46/evidence/v3/compare-1101213a.py"
LIVE = ROOT / ".ufo/round-45/evidence/h06/fresh-live.json"
INDEPENDENT = ROOT / ".ufo/round-45/evidence/h06/fresh-independent.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
CARRIER = ROOT / ".ufo/round-45/evidence/h06/carrier-spread"
PIN_HEAD = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
PIN_TREE = "e8dced184612a9738c5b8d244a0837fbd955a7da"
DRIVER_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
SCOPE_SHA = "fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a"
LIVE_SHA = "0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341"
INDEPENDENT_SHA = "eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887"
FABRICATED = "fabricated blocker: no evidence; this row is not derivable because I say so"
CID = "omp.catalogue.found"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def snapshot():
    return {
        "at_utc": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        "head": git("rev-parse", "HEAD"),
        "head_tree": git("rev-parse", "HEAD^{tree}"),
        "target_blob_sha256": hashlib.sha256(subprocess.run(
            ["git", "-C", str(ROOT), "show",
             f"{PIN_HEAD}:verifiers/compare_harness_independent.py"],
            check=True, capture_output=True).stdout).hexdigest(),
        "frozen_driver_sha256": sha(DRIVER),
        "worktree_driver_sha256": sha(ROOT / "verifiers/compare_harness_independent.py"),
        "scope_sha256": sha(SCOPE),
        "live_sha256": sha(LIVE),
        "independent_sha256": sha(INDEPENDENT),
    }


def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")


def set_probe(payload, cid, probe):
    payload["scoped_out_probes"][cid] = copy.deepcopy(probe)
    for channel in ("results", "rows"):
        for record in payload.get(channel, []):
            if isinstance(record, dict) and record.get("check") == cid:
                record["probe"] = copy.deepcopy(probe)


def set_targeted_base(payload, recomputed):
    ids = sorted(payload["scoped_out"])
    assert ids == sorted(payload["scoped_out_probes"])
    for cid in ids:
        probe = copy.deepcopy(payload["scoped_out_probes"][cid])
        probe["target"] = str(CARRIER)
        probe["observable"] = copy.deepcopy(recomputed["observable"])
        probe["kind"] = "rule-spread-census"
        set_probe(payload, cid, probe)
    return payload


def case_payloads(base, recomputed):
    valid = set_targeted_base(copy.deepcopy(base), recomputed)
    cases = {"retargeted-control": copy.deepcopy(valid)}

    reason = copy.deepcopy(valid)
    reason["scoped_out"][CID] = FABRICATED
    cases["fabricated-reason"] = reason

    evidence = copy.deepcopy(valid)
    for channel in ("results", "rows"):
        for record in evidence.get(channel, []):
            if isinstance(record, dict) and record.get("check") == CID:
                record["evidence"] = FABRICATED
    cases["fabricated-evidence"] = evidence

    bad_kind = copy.deepcopy(valid)
    selected = copy.deepcopy(bad_kind["scoped_out_probes"][CID])
    selected["kind"] = "external-authority"
    set_probe(bad_kind, CID, selected)
    cases["wrong-probe-kind"] = bad_kind

    bad_result = copy.deepcopy(valid)
    selected = copy.deepcopy(bad_result["scoped_out_probes"][CID])
    selected["observable"]["candidate_blocks"] += 1
    set_probe(bad_result, CID, selected)
    cases["wrong-probe-result"] = bad_result
    return cases


def run_case(name, payload_path):
    receipt = EVIDENCE / f"{name}.receipt.json"
    command = [sys.executable, str(DRIVER),
               "--live-json", str(LIVE),
               "--independent-json", str(payload_path),
               "--expect-n", "28", "--cwd", str(ROOT),
               "--scope-file", str(SCOPE), "--no-stamp", "--json",
               "--receipt", str(receipt)]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=180)
    stdout_path = EVIDENCE / f"{name}.stdout.json"
    stderr_path = EVIDENCE / f"{name}.stderr.txt"
    stdout_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    try:
        output = json.loads(proc.stdout)
    except ValueError:
        output = None
    return {
        "command": command,
        "exit": proc.returncode,
        "headline": output.get("headline") if isinstance(output, dict) else None,
        "reason": output.get("reason") if isinstance(output, dict) else proc.stderr.strip(),
        "scoped_out_reason": output.get("scoped_out", {}).get(CID)
        if isinstance(output, dict) else None,
        "payload_sha256": sha(payload_path),
        "stdout_sha256": sha(stdout_path),
        "stderr_sha256": sha(stderr_path),
        "receipt_sha256": sha(receipt) if receipt.is_file() else None,
    }


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    if git("rev-parse", "HEAD") != PIN_HEAD or git("rev-parse", "HEAD^{tree}") != PIN_TREE:
        raise RuntimeError("HEAD or committed tree differs from the requested 1101213a snapshot")
    frozen = subprocess.run(["git", "-C", str(ROOT), "show",
                             f"{PIN_HEAD}:verifiers/compare_harness_independent.py"],
                            check=True, capture_output=True).stdout
    if hashlib.sha256(frozen).hexdigest() != DRIVER_SHA:
        raise RuntimeError("committed comparator blob does not match 1101213a")
    for path, expected in ((DRIVER, DRIVER_SHA), (SCOPE, SCOPE_SHA),
                           (LIVE, LIVE_SHA), (INDEPENDENT, INDEPENDENT_SHA)):
        if sha(path) != expected:
            raise RuntimeError(f"pinned input changed: {path}")
    if not CARRIER.is_dir():
        raise RuntimeError("controlled in-repository carrier fixture is absent")

    spec = importlib.util.spec_from_file_location("pinned_compare", DRIVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    recomputed = module.recompute_probe({"kind": "rule-spread-census",
                                         "target": str(CARRIER)})
    if len(recomputed["observable"].get("distinct_totals") or []) < 2:
        raise RuntimeError("controlled carrier does not produce a non-vacuous rule spread")

    base = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
    payloads = case_payloads(base, recomputed)
    before = snapshot()
    inputs = {
        "scope": sha(SCOPE),
        "live": sha(LIVE),
        "independent_base": sha(INDEPENDENT),
        "carrier_files": {str(path): sha(path) for path in sorted(CARRIER.rglob("*.jsonl"))},
        "carrier_probe": recomputed,
    }
    results = {}
    for name, payload in payloads.items():
        path = DRAFT / f"{name}.independent.json"
        dump(path, payload)
        results[name] = run_case(name, path)
    after = snapshot()
    after_inputs = {
        "scope": sha(SCOPE),
        "live": sha(LIVE),
        "independent_base": sha(INDEPENDENT),
        "carrier_files": {str(path): sha(path) for path in sorted(CARRIER.rglob("*.jsonl"))},
        "carrier_probe": module.recompute_probe({"kind": "rule-spread-census",
                                                  "target": str(CARRIER)}),
    }
    if inputs != after_inputs:
        raise RuntimeError("a pinned input or carrier fixture changed during replay")
    if before["head"] != after["head"] or before["head_tree"] != after["head_tree"]:
        raise RuntimeError("HEAD or committed tree changed during replay")
    if before["target_blob_sha256"] != after["target_blob_sha256"]:
        raise RuntimeError("committed comparator blob changed during replay")
    if before["frozen_driver_sha256"] != after["frozen_driver_sha256"]:
        raise RuntimeError("frozen comparator copy changed during replay")
    if before["scope_sha256"] != after["scope_sha256"]:
        raise RuntimeError("scope file changed during replay")

    result = {
        "runner": str(Path(__file__).relative_to(ROOT)),
        "runner_sha256": sha(__file__),
        "command": "PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/a2/replay_scope_contract.py",
        "git_operations": "read-only rev-parse and show only; no write-tree/add/commit/ref operation",
        "before": before,
        "after": after,
        "inputs_unchanged": inputs == after_inputs,
        "inputs": inputs,
        "cases": results,
    }
    result_path = EVIDENCE / "scope-contract-results.json"
    dump(result_path, result)
    print(json.dumps({"result_sha256": sha(result_path),
                      "before": before, "after": after,
                      "cases": {name: {"exit": item["exit"],
                                       "headline": item["headline"],
                                       "reason": item["reason"],
                                       "scoped_out_reason": item["scoped_out_reason"]}
                                for name, item in results.items()}},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError) as exc:
        print(f"scope contract replay: ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
