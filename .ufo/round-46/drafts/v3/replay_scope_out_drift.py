#!/usr/bin/env python3
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / ".ufo/round-46/evidence/v3"
WORKTREE_DRIVER = ROOT / "verifiers/compare_harness_independent.py"
DRIVER = OUT / "compare-1101213a.py"
PIN_HEAD = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
PIN_TREE = "e8dced184612a9738c5b8d244a0837fbd955a7da"
TARGET_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
LIVE_SOURCE = ROOT / "verifiers/verify_harness_claims.py"
IND_SOURCE = ROOT / "verifiers/verify_harness_independent.py"
LIVE = OUT / "fresh-live.json"
RAW_BASE = OUT / "fresh-independent-raw.json"
BASE = OUT / "fresh-independent-normalized.json"
NORMAL_CARRIER = OUT / "carrier-normalized"
TARGET_CARRIER = OUT / "carrier-unconstrained"
CID = "omp.catalogue.found"
FABRICATED = "fabricated blocker: no evidence; this row is not derivable because I say so"


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
        "index_tree": git("write-tree"),
        "status": git("status", "--short", "--untracked-files=all"),
        "target_comparator_sha256": sha(DRIVER),
        "worktree_comparator_sha256": sha(WORKTREE_DRIVER),
        "live_producer_sha256": sha(LIVE_SOURCE),
        "independent_producer_sha256": sha(IND_SOURCE),
        "scope_sha256": sha(SCOPE),
    }


def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def find_row(payload, channel, cid):
    rows = payload.get(channel)
    if not isinstance(rows, list):
        raise RuntimeError(f"payload has no {channel} row list")
    return next(row for row in rows if row.get("check") == cid)


def make_carrier(path, entries, stamps, mtimes):
    path.mkdir(parents=True, exist_ok=True)
    files = []
    for index, (name, count, stamp, mtime) in enumerate(
            zip(("a.jsonl", "b.jsonl"), entries, stamps, mtimes)):
        block = "\n".join(f"- entry-{index}-{i}" for i in range(count))
        payload = {"stamp": stamp, "text": f"<skills>\n{block}\n</skills>"}
        target = path / name
        target.write_text(json.dumps(payload, separators=(",", ":")) + "\n",
                          encoding="utf-8")
        ns = int(mtime * 1_000_000_000)
        os.utime(target, ns=(ns, ns))
        files.append(target)
    if len(list(path.glob("*.jsonl"))) != 2:
        raise RuntimeError(f"carrier {path} must contain exactly two JSONL files")
    return path.resolve(), files


def make_probe(module, carrier):
    probe = {"kind": "rule-spread-census", "target": str(carrier)}
    probe["observable"] = module.recompute_probe(probe)["observable"]
    return probe


def replace_probe(payload, cid, probe):
    payload.setdefault("scoped_out_probes", {})[cid] = json.loads(json.dumps(probe))
    for channel in ("results", "rows"):
        find_row(payload, channel, cid)["probe"] = json.loads(json.dumps(probe))


def differing_paths(left, right, path="$" ):
    if isinstance(left, dict) and isinstance(right, dict):
        out = []
        for key in sorted(set(left) | set(right)):
            child = f"{path}.{key}"
            if key not in left or key not in right:
                out.append(child)
            else:
                out.extend(differing_paths(left[key], right[key], child))
        return out
    if isinstance(left, list) and isinstance(right, list):
        out = []
        for index in range(max(len(left), len(right))):
            child = f"{path}[{index}]"
            if index >= len(left) or index >= len(right):
                out.append(child)
            else:
                out.extend(differing_paths(left[index], right[index], child))
        return out
    return [] if left == right else [path]


def capture_producer(name, source, output_path):
    command = [sys.executable, str(source.relative_to(ROOT)), "--json"]
    started = utc_now()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=900)
    ended = utc_now()
    output_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path = OUT / f"{name}.stderr.txt"
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    try:
        payload = json.loads(proc.stdout)
        parsed = isinstance(payload, dict)
        parse_error = None
    except ValueError as exc:
        payload, parsed, parse_error = None, False, str(exc)
    return {
        "command": command,
        "cwd": str(ROOT),
        "started_at_utc": started,
        "ended_at_utc": ended,
        "exit": proc.returncode,
        "source_sha256": sha(source),
        "stdout_path": str(output_path.relative_to(ROOT)),
        "stdout_sha256": sha(output_path),
        "stderr_path": str(stderr_path.relative_to(ROOT)),
        "stderr_sha256": sha(stderr_path),
        "parsed_json_object": parsed,
        "parse_error": parse_error,
    }, payload


def capture_inputs(reason_path, evidence_path, target_path, carrier_files):
    paths = [LIVE, RAW_BASE, BASE, reason_path, evidence_path, target_path,
             SCOPE, DRIVER, LIVE_SOURCE, IND_SOURCE]
    return {
        "files": {str(path.relative_to(ROOT)): sha(path) for path in paths},
        "probe_carrier_files": {
            str(path.relative_to(ROOT)): {
                "sha256": sha(path), "mtime_ns": path.stat().st_mtime_ns,
            }
            for path in carrier_files
        },
    }


def classify_case(exit_code, reason):
    if exit_code == 0:
        return "accepted-residual"
    if exit_code == 2 and CID in reason and any(
            token in reason.lower() for token in ("false blocker", "laundering")):
        return "class-named"
    return "other-or-unrelated-failure"


def run_case(name, independent_path):
    receipt = OUT / f"{name}.receipt.json"
    command = [sys.executable, str(DRIVER),
               "--live-json", str(LIVE),
               "--independent-json", str(independent_path),
               "--expect-n", "28", "--cwd", str(ROOT),
               "--scope-file", "verifiers/harness-independent-scope.json",
               "--no-stamp", "--json", "--receipt", str(receipt)]
    started = utc_now()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=180)
    ended = utc_now()
    stdout_path = OUT / f"{name}.stdout.json"
    stderr_path = OUT / f"{name}.stderr.txt"
    stdout_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    try:
        data = json.loads(proc.stdout)
    except ValueError:
        data = None
    reason = data.get("reason", "") if isinstance(data, dict) else proc.stderr.strip()
    return {
        "command": command,
        "started_at_utc": started,
        "ended_at_utc": ended,
        "exit": proc.returncode,
        "classification": classify_case(proc.returncode, reason),
        "headline": data.get("headline") if isinstance(data, dict) else None,
        "agreement": data.get("agreement") if isinstance(data, dict) else None,
        "reason": reason,
        "scoped_out_reason": data.get("scoped_out", {}).get(CID)
        if isinstance(data, dict) else None,
        "independent_path": str(independent_path.relative_to(ROOT)),
        "independent_sha256": sha(independent_path),
        "live_sha256": sha(LIVE),
        "stdout_path": str(stdout_path.relative_to(ROOT)),
        "stdout_sha256": sha(stdout_path),
        "stderr_path": str(stderr_path.relative_to(ROOT)),
        "stderr_sha256": sha(stderr_path),
        "receipt_path": str(receipt.relative_to(ROOT)),
        "receipt_sha256": sha(receipt) if receipt.is_file() else None,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if git("rev-parse", "HEAD") != PIN_HEAD:
        raise RuntimeError("HEAD differs from the requested 1101213a snapshot")
    if git("rev-parse", "HEAD^{tree}") != PIN_TREE:
        raise RuntimeError("HEAD tree differs from the requested 1101213a snapshot")
    target_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         f"{PIN_HEAD}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True,
    ).stdout
    if hashlib.sha256(target_bytes).hexdigest() != TARGET_SHA:
        raise RuntimeError("HEAD comparator bytes differ from the requested 1101213a target")
    DRIVER.write_bytes(target_bytes)
    if sha(DRIVER) != TARGET_SHA:
        raise RuntimeError("frozen comparator copy differs from requested 1101213a target")
    before = snapshot()
    if before["scope_sha256"] != "fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a":
        raise RuntimeError("scope file differs from the R45 pinned input")

    spec = importlib.util.spec_from_file_location("frozen_comparator_1101213a", DRIVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load frozen comparator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    normal_path, normal_files = make_carrier(
        NORMAL_CARRIER, [2, 5],
        ["2026-02-02T00:00:00.000Z", "2026-01-01T00:00:00.000Z"],
        [1760000000, 1760000010])
    target_path, target_files = make_carrier(
        TARGET_CARRIER, [3, 7],
        ["2026-02-02T00:00:00.000Z", "2026-01-01T00:00:00.000Z"],
        [1760000100, 1760000110])
    normal_probe = make_probe(module, normal_path)
    target_probe = make_probe(module, target_path)
    if normal_probe["observable"]["distinct_totals"] != [2, 5]:
        raise RuntimeError(f"normalized carrier lacks [2,5] spread: {normal_probe}")
    if target_probe["observable"]["distinct_totals"] != [3, 7]:
        raise RuntimeError(f"target carrier lacks [3,7] spread: {target_probe}")

    capture_specs = (("fresh-live", LIVE_SOURCE, LIVE),
                     ("fresh-independent-raw", IND_SOURCE, RAW_BASE))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(capture_producer, *args) for args in capture_specs]
        captured = [future.result() for future in futures]
    producer_meta = {capture_specs[i][0]: captured[i][0]
                     for i in range(len(capture_specs))}
    live_payload, raw_payload = captured[0][1], captured[1][1]
    capture_errors = []
    for name, payload in zip(("fresh-live", "fresh-independent-raw"),
                             (live_payload, raw_payload)):
        item = producer_meta[name]
        if item["exit"] != 0:
            capture_errors.append(f"{name} exited {item['exit']}")
        if not item["parsed_json_object"]:
            capture_errors.append(f"{name} did not produce a JSON object")
    if capture_errors:
        raise RuntimeError("producer capture failure: " + "; ".join(capture_errors))

    scope = json.loads(SCOPE.read_text(encoding="utf-8"))
    committed = sorted(scope["scope_out"])
    if sorted(raw_payload.get("scoped_out", {})) != committed:
        raise RuntimeError("fresh producer scope-out set differs from the committed scope file")
    for cid in committed:
        fresh_probe = raw_payload.get("scoped_out_probes", {}).get(cid)
        if not isinstance(fresh_probe, dict):
            raise RuntimeError(f"fresh producer omitted probe for {cid}")
        replace_probe(raw_payload, cid, normal_probe)
    dump(BASE, raw_payload)
    base = json.loads(BASE.read_text(encoding="utf-8"))

    reason_payload = json.loads(json.dumps(base))
    reason_payload["scoped_out"][CID] = FABRICATED
    reason_path = OUT / "fabricated-reason.independent.json"
    dump(reason_path, reason_payload)

    evidence_payload = json.loads(json.dumps(base))
    for channel in ("results", "rows"):
        find_row(evidence_payload, channel, CID)["evidence"] = FABRICATED
    evidence_path = OUT / "fabricated-evidence.independent.json"
    dump(evidence_path, evidence_payload)

    target_payload = json.loads(json.dumps(base))
    replace_probe(target_payload, CID, target_probe)
    target_input_path = OUT / "unconstrained-probe-target.independent.json"
    dump(target_input_path, target_payload)

    input_paths = (reason_path, evidence_path, target_input_path)
    carrier_files = normal_files + target_files
    inputs_before = capture_inputs(*input_paths, carrier_files)
    cases = {
        "honest-control": run_case("honest-control", BASE),
        "fabricated-reason": run_case("fabricated-reason", reason_path),
        "fabricated-evidence": run_case("fabricated-evidence", evidence_path),
        "unconstrained-probe-target": run_case(
            "unconstrained-probe-target", target_input_path),
    }
    inputs_after = capture_inputs(*input_paths, carrier_files)
    after = snapshot()

    diff_paths = {
        "fabricated-reason": differing_paths(base, reason_payload),
        "fabricated-evidence": differing_paths(base, evidence_payload),
        "unconstrained-probe-target": differing_paths(base, target_payload),
    }
    control = cases["honest-control"]
    control_green = (
        control["exit"] == 0
        and control["headline"] == {"column": "mode-aware protocol", "n": 24,
                                    "total": 24, "joined_scope": 24,
                                    "live_checks": 28}
        and control["agreement"] == {
            "n_agree_protocol": 24, "n_agree_strict": 20,
            "n_adjudicated": 4, "n_disagree": 0,
            "n_unadjudicated": 0, "n_provisional": 0,
            "n_uncovered": 0, "n_unknown": 0, "n_scoped_out": 4,
            "total": 24,
        }
    )
    source_hashes_stable = all(
        before[key] == after[key]
        for key in ("live_producer_sha256", "independent_producer_sha256"))
    inputs_unchanged = inputs_before == inputs_after
    git_state_stable = all(before[key] == after[key]
                           for key in ("head", "head_tree", "index_tree"))
    frozen_comparator_stable = (
        before["target_comparator_sha256"] == TARGET_SHA
        and after["target_comparator_sha256"] == TARGET_SHA)
    scope_stable = before["scope_sha256"] == after["scope_sha256"]
    arm_outputs_parse = all(cases[name]["headline"] is not None for name in cases)
    expected_diffs = {
        "fabricated-reason": [f"$.scoped_out.{CID}"],
        "fabricated-evidence": [
            f"$.results[{next(i for i, r in enumerate(base['results']) if r['check'] == CID)}].evidence",
            f"$.rows[{next(i for i, r in enumerate(base['rows']) if r['check'] == CID)}].evidence",
        ],
    }
    diffs_isolated = all(diff_paths[name] == paths
                         for name, paths in expected_diffs.items())
    result_index = next(i for i, row in enumerate(base["results"])
                        if row["check"] == CID)
    rows_index = next(i for i, row in enumerate(base["rows"])
                      if row["check"] == CID)
    target_paths = {
        f"$.scoped_out_probes.{CID}.target",
        f"$.results[{result_index}].probe.target",
        f"$.rows[{rows_index}].probe.target",
    }
    allowed_probe_prefixes = target_paths | {
        f"$.scoped_out_probes.{CID}.observable",
        f"$.results[{result_index}].probe.observable",
        f"$.rows[{rows_index}].probe.observable",
    }
    target_diffs = set(diff_paths["unconstrained-probe-target"])
    target_only_probe = (
        bool(target_diffs)
        and target_paths <= target_diffs
        and all(any(path == prefix or path.startswith(prefix + ".")
                    or path.startswith(prefix + "[")
                    for prefix in allowed_probe_prefixes)
                for path in target_diffs)
    )
    checks = {
        "baseline_green_24_of_24": control_green,
        "producer_source_hashes_stable": source_hashes_stable,
        "replay_inputs_unchanged": inputs_unchanged,
        "head_tree_index_stable": git_state_stable,
        "frozen_comparator_sha_stable": frozen_comparator_stable,
        "scope_sha_stable": scope_stable,
        "all_cli_outputs_parse": arm_outputs_parse,
        "reason_and_evidence_mutations_isolated": diffs_isolated,
        "probe_target_arm_changes_only_target_observable": target_only_probe,
        "all_probe_recomputations_valid": True,
    }
    checks["all_probe_recomputations_valid"] = all(
        module.recompute_probe(probe)["observable"] == probe["observable"]
        for payload in (base, target_payload)
        for cid in committed
        for probe in [payload["scoped_out_probes"][cid]])
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "runner": str(Path(__file__).relative_to(ROOT)),
        "runner_sha256": sha(__file__),
        "runner_command": "PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v3/replay_scope_out_drift.py",
        "measurement_started_at_utc": before["at_utc"],
        "measurement_finished_at_utc": after["at_utc"],
        "head_pin": PIN_HEAD,
        "tree_pin": PIN_TREE,
        "comparator_sha256_pin": TARGET_SHA,
        "scope_sha256_pin": before["scope_sha256"],
        "before": before,
        "after": after,
        "producer_captures": producer_meta,
        "normalization": {
            "disclosure": "Fresh independent rows and reasons were retained, but each committed scope-out probe was regenerated against the deterministic lane-local [2,5] carrier. The target arm changes only omp.catalogue.found's probe target and recomputes its observable against a second lane-local [3,7] carrier.",
            "raw_independent_path": str(RAW_BASE.relative_to(ROOT)),
            "raw_independent_sha256": sha(RAW_BASE),
            "normalized_independent_path": str(BASE.relative_to(ROOT)),
            "normalized_independent_sha256": sha(BASE),
            "normal_probe": normal_probe,
            "target_probe": target_probe,
            "normal_carrier_files": {
                str(path.relative_to(ROOT)): {"sha256": sha(path),
                                               "mtime_ns": path.stat().st_mtime_ns}
                for path in normal_files
            },
            "target_carrier_files": {
                str(path.relative_to(ROOT)): {"sha256": sha(path),
                                               "mtime_ns": path.stat().st_mtime_ns}
                for path in target_files
            },
        },
        "mutation_diff_paths": diff_paths,
        "inputs_unchanged": inputs_unchanged,
        "input_hashes_before": inputs_before,
        "input_hashes_after": inputs_after,
        "checks": checks,
        "failures": failures,
        "cases": cases,
    }
    result_path = OUT / "scope-out-drift-results.json"
    dump(result_path, result)
    print(json.dumps({
        "result_path": str(result_path.relative_to(ROOT)),
        "result_sha256": sha(result_path),
        "checks": checks,
        "failures": failures,
        "before": before,
        "after": after,
        "cases": {name: {"exit": value["exit"],
                          "classification": value["classification"],
                          "headline": value["headline"],
                          "reason": value["reason"],
                          "scoped_out_reason": value["scoped_out_reason"]}
                  for name, value in cases.items()},
    }, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError) as exc:
        print(f"scope-out drift replay: ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
