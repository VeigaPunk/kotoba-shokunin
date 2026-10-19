#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
RUNS = OUT / "hunt-20261019T1630Z-r2"
BASE_REF = "055d3b9:verifiers/compare_harness_independent.py"
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
CAPTURE_LIVE = OUT / "live.json"
CAPTURE_IND = OUT / "independent.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(path.read_bytes())


def run(argv, cwd=ROOT):
    return subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=300)


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    path.write_bytes(data)
    return path


def json_bytes(payload):
    return (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def set_ind_value(payload, cid, value):
    changed = 0
    for channel in ("results", "rows", "checks"):
        raw = payload.get(channel)
        if isinstance(raw, list):
            for record in raw:
                if isinstance(record, dict) and record.get("check", record.get("id", record.get("name"))) == cid:
                    keys = [key for key in ("expected", "expected_value", "re_derived", "value", "observed") if key in record]
                    for key in keys:
                        record[key] = copy.deepcopy(value)
                        changed += 1
        elif isinstance(raw, dict) and cid in raw:
            raw[cid] = copy.deepcopy(value)
            changed += 1
    for channel in ("expected", "re_derived", "observations"):
        raw = payload.get(channel)
        if isinstance(raw, dict) and cid in raw:
            raw[cid] = copy.deepcopy(value)
            changed += 1
    if changed == 0:
        raise RuntimeError(f"no independent value found for {cid}")
    return changed


def mutate_record(payload, cid, mutate):
    results = payload.get("results")
    for i, record in enumerate(results or []):
        if isinstance(record, dict) and record.get("check") == cid:
            mutate(record)
            return i
    raise RuntimeError(f"live result not found: {cid}")


def replace_probe(payload, cid, probe):
    payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(probe)
    for channel in ("results", "rows"):
        for record in payload.get(channel, []) or []:
            if isinstance(record, dict) and record.get("check") == cid and "probe" in record:
                record["probe"] = copy.deepcopy(probe)


def main():
    if RUNS.exists():
        raise SystemExit(f"refusing to reuse existing evidence dir: {RUNS}")
    RUNS.mkdir(parents=True)
    inputs = RUNS / "inputs"
    inputs.mkdir()

    head_before = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    tree_before = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    current_before = DRIVER.read_bytes()
    current_sha_before = sha(current_before)
    baseline = subprocess.check_output(["git", "show", BASE_REF], cwd=ROOT)
    baseline_sha = sha(baseline)
    current_path = write(RUNS / "compare-current.py", current_before)
    baseline_path = write(RUNS / "compare-055d3b9.py", baseline)
    current_after_snapshot = DRIVER.read_bytes()
    current_sha_after_snapshot = sha(current_after_snapshot)

    live_raw = CAPTURE_LIVE.read_bytes()
    ind_raw = CAPTURE_IND.read_bytes()
    live = json.loads(live_raw)
    independent = json.loads(ind_raw)
    live_copy = write(RUNS / "live-capture.json", live_raw)
    ind_copy = write(RUNS / "independent-capture.json", ind_raw)
    scope_raw = SCOPE.read_bytes()
    scope_copy = RUNS / "scope.json"
    write(scope_copy, scope_raw)
    scope_obj = json.loads(scope_raw)
    live_rows = live["results"]
    ind_rows = independent["results"]
    live_by_id = {row["check"]: row for row in live_rows}
    ind_by_id = {row["check"]: row for row in ind_rows}
    cid = "oc.log.skills_rescan_max"
    if cid not in live_by_id or cid not in ind_by_id:
        raise RuntimeError(f"selected probe ID unavailable: {cid}")
    observed = live_by_id[cid]["observed"]
    if not isinstance(observed, (int, float)) or isinstance(observed, bool):
        raise RuntimeError(f"expected numeric observation for {cid}: {observed!r}")
    mismatch_value = int(observed) + 999
    baseline_modes = {row["check"]: row.get("mode") for row in live_rows}
    if baseline_modes[cid] != "equal":
        raise RuntimeError(f"expected equal-mode target, got {baseline_modes[cid]!r}")

    cases = []

    def add_case(name, live_data, ind_data, expected_n=28, scope_data=None):
        live_path = inputs / f"{name}.live.json"
        ind_path = inputs / f"{name}.independent.json"
        write(live_path, live_data)
        write(ind_path, ind_data)
        scope_path = scope_copy if scope_data is None else inputs / f"{name}.scope.json"
        if scope_data is not None:
            write(scope_path, scope_data)
        case = {
            "name": name,
            "expect_n": expected_n,
            "live_path": str(live_path),
            "independent_path": str(ind_path),
            "scope_path": str(scope_path),
            "input_sha256": {
                "live": digest(live_path),
                "independent": digest(ind_path),
                "scope": digest(scope_path),
            },
            "runs": {},
        }
        for label, executable in (("before_055d3b9", baseline_path), ("candidate_snapshot", current_path)):
            argv = [sys.executable, str(executable), "--live-json", str(live_path),
                    "--independent-json", str(ind_path), "--expect-n", str(expected_n),
                    "--cwd", str(ROOT), "--scope-file", str(scope_path), "--no-stamp", "--json"]
            proc = run(argv)
            parsed = None
            if proc.stdout.strip():
                try:
                    parsed = json.loads(proc.stdout)
                except ValueError:
                    pass
            case["runs"][label] = {
                "argv": argv,
                "exit": proc.returncode,
                "stdout_sha256": sha(proc.stdout.encode("utf-8")),
                "stderr_sha256": sha(proc.stderr.encode("utf-8")),
                "headline": parsed.get("headline") if isinstance(parsed, dict) else None,
                "agreement": parsed.get("agreement") if isinstance(parsed, dict) else None,
                "reason": parsed.get("reason") if isinstance(parsed, dict) else None,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            }
        cases.append(case)
        return case

    # Caller-supplied live verdict fields are currently retained only when strings.
    live_drift = copy.deepcopy(live)
    mutate_record(live_drift, cid, lambda row: row.__setitem__("verdict", "DRIFT"))
    add_case("live-verdict-drift-control", json_bytes(live_drift), ind_raw)
    live_bad_verdict = copy.deepcopy(live)
    mutate_record(live_bad_verdict, cid, lambda row: row.__setitem__("verdict", []))
    add_case("live-nonstring-verdict-shadow", json_bytes(live_bad_verdict), ind_raw)

    # A known mode shadow is re-run, with an equal-mode red control.
    ind_skew = copy.deepcopy(independent)
    set_ind_value(ind_skew, cid, mismatch_value)
    live_equal = copy.deepcopy(live)
    mutate_record(live_equal, cid, lambda row: row.__setitem__("mode", "equal"))
    add_case("live-positive-mode-shadow-control", json_bytes(live_equal), json_bytes(ind_skew))
    live_positive = copy.deepcopy(live)
    mutate_record(live_positive, cid, lambda row: row.__setitem__("mode", "positive"))
    add_case("live-positive-mode-shadow", json_bytes(live_positive), json_bytes(ind_skew))

    # New within-channel side channel: duplicate IDs keep the value equal, but
    # parse_live() takes the last mode/verdict while _channel_maps() checks only values/status.
    live_dup = copy.deepcopy(live)
    target_index = mutate_record(live_dup, cid, lambda row: row.__setitem__("mode", "equal"))
    first = copy.deepcopy(live_dup["results"][target_index])
    last = copy.deepcopy(first)
    last["mode"] = "positive"
    last["verdict"] = "PASS"
    live_dup["results"][target_index:target_index + 1] = [first, last]
    add_case("live-same-channel-duplicate-mode", json_bytes(live_dup), json_bytes(ind_skew))

    # Also replay an ignored top-level live summary/verdict/mode channel.
    live_summary = copy.deepcopy(live_positive)
    live_summary["summary"] = {"exit": 1, "agreement": "0/28", "reason": "DRIFT"}
    live_summary["modes"] = {cid: "equal"}
    live_summary["verdicts"] = {cid: "DRIFT"}
    add_case("live-top-level-shadow-maps", json_bytes(live_summary), json_bytes(ind_skew))

    # Existing raw duplicates: duplicate top-level results and record re_derived.
    attacker_rows = copy.deepcopy(independent["results"])
    for row in attacker_rows:
        if row.get("check") == cid:
            row["re_derived"] = mismatch_value
            row["value"] = mismatch_value
    rest = {key: value for key, value in independent.items() if key != "results"}
    raw_top_dup = ("{\"results\": " + json.dumps(attacker_rows, ensure_ascii=False, separators=(",", ":"))
                   + ", \"results\": " + json.dumps(independent["results"], ensure_ascii=False, separators=(",", ":"))
                   + ", " + json.dumps(rest, ensure_ascii=False, separators=(",", ":"))[1:-1] + "}\n")
    add_case("raw-duplicate-top-level-results", live_raw, raw_top_dup.encode("utf-8"))

    ind_pretty = json.dumps(independent, indent=2, ensure_ascii=False)
    start = ind_pretty.find(f'"check": "{cid}"')
    hit = re.search(r'("re_derived"\s*:\s*)-?\d+', ind_pretty[start:])
    if start < 0 or hit is None:
        raise RuntimeError("unable to build duplicate per-record re_derived payload")
    key_start = start + hit.start(1)
    value_end = start + hit.end()
    raw_record_dup = (ind_pretty[:key_start] + hit.group(1) + str(mismatch_value)
                      + ",\n        " + hit.group(1) + str(ind_by_id[cid]["re_derived"])
                      + ind_pretty[value_end:] + "\n").encode("utf-8")
    add_case("raw-duplicate-record-rederived", live_raw, raw_record_dup)

    # New deeper nested duplicate: duplicate a key inside a JSON object value,
    # below results[0].expected, rather than duplicating a row/top-level member.
    synthetic_live = b'{"results":[{"check":"sample.value","observed":{"nested":999},"verdict":"PASS","mode":"equal"}]}\n'
    synthetic_ind = b'{"results":[{"check":"sample.value","expected":{"nested":1,"nested":999},"re_derived":{"nested":999},"status":"DERIVED"}]}\n'
    empty_scope = json_bytes({"scope_out": {}})
    add_case("raw-duplicate-nested-value-member", synthetic_live, synthetic_ind,
             expected_n=1, scope_data=empty_scope)

    # Scope-out reason/evidence drift: non-empty prose is accepted without comparison
    # to the committed reason; the probe itself is otherwise unchanged.
    scoped_id = "omp.catalogue.found"
    committed_reason = scope_obj["scope_out"][scoped_id]["reason"]
    drifted_reason = copy.deepcopy(independent)
    drifted_reason["scoped_out"][scoped_id] = "valid reason: this blocker is inside the harness boundary, not the substrate"
    for channel in ("results", "rows"):
        for row in drifted_reason.get(channel, []) or []:
            if row.get("check") == scoped_id and "evidence" in row:
                row["evidence"] = "fabricated evidence: the committed probe does not support this statement"
    add_case("scope-out-reason-evidence-drift", live_raw, json_bytes(drifted_reason))

    # Fabricated observable at the committed target must fail, even with the exact
    # committed reason. The altered field is deliberately made far from recomputation.
    spec = importlib.util.spec_from_file_location("compare_probe", current_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    original_probe = independent["scoped_out_probes"][scoped_id]
    actual_observable = module.recompute_probe(original_probe)["observable"]
    fake_probe = copy.deepcopy(original_probe)
    fake_probe["observable"] = copy.deepcopy(actual_observable)
    fake_probe["observable"]["candidate_blocks"] += 1000
    fake_payload = copy.deepcopy(independent)
    fake_payload["scoped_out"][scoped_id] = committed_reason
    replace_probe(fake_payload, scoped_id, fake_probe)
    add_case("scope-out-fabricated-probe-result", live_raw, json_bytes(fake_payload))

    # A valid recomputation over a payload-selected, planted carrier is still
    # accepted: the committed contract pins kind, but not the carrier target.
    carrier = inputs / "fabricated-carrier"
    carrier.mkdir()
    for name, stamp, n, mtime in (("a.jsonl", "2026-01-01T00:00:00.000Z", 1, 1700000000),
                                  ("b.jsonl", "2026-02-02T00:00:00.000Z", 4, 1800000000)):
        block = "\\n".join(f"- entry {i}" for i in range(n))
        path = carrier / name
        path.write_text('{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' % (stamp, block), encoding="utf-8")
        os.utime(path, (mtime, mtime))
    planted_probe = {
        "kind": scope_obj["probe_contract"]["kind"],
        "target": str(carrier.resolve()),
    }
    planted_probe["observable"] = module.recompute_probe(planted_probe)["observable"]
    planted_payload = copy.deepcopy(independent)
    planted_payload["scoped_out"][scoped_id] = committed_reason
    replace_probe(planted_payload, scoped_id, planted_probe)
    add_case("scope-out-valid-reason-planted-probe-target", live_raw, json_bytes(planted_payload))

    # Probe-channel split: top-level canonical probe is recomputed, but a false
    # record-local probe is silently shadowed when the top-level map is non-empty.
    split_payload = copy.deepcopy(independent)
    split_payload["scoped_out"][scoped_id] = committed_reason
    bad_record_probe = copy.deepcopy(original_probe)
    bad_record_probe["observable"] = copy.deepcopy(actual_observable)
    bad_record_probe["observable"]["candidate_blocks"] += 1000
    for channel in ("results", "rows"):
        for row in split_payload.get(channel, []) or []:
            if row.get("check") == scoped_id and "probe" in row:
                row["probe"] = copy.deepcopy(bad_record_probe)
    add_case("scope-out-false-record-probe-shadowed", live_raw, json_bytes(split_payload))

    head_after = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    tree_after = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    current_sha_end = digest(DRIVER)
    meta = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "head": head_before,
        "tree_before": tree_before,
        "tree_after": tree_after,
        "head_after": head_after,
        "current_comparator_sha_before_snapshot": current_sha_before,
        "current_comparator_sha_after_snapshot": current_sha_after_snapshot,
        "current_comparator_sha_after_tests": current_sha_end,
        "baseline_ref": BASE_REF,
        "baseline_comparator_sha256": baseline_sha,
        "candidate_snapshot_sha256": current_sha_after_snapshot,
        "scope_sha256": sha(scope_raw),
        "producer_sources": {
            "live": digest(ROOT / "verifiers/verify_harness_claims.py"),
            "independent": digest(ROOT / "verifiers/verify_harness_independent.py"),
        },
        "capture_sha256": {"live": digest(live_copy), "independent": digest(ind_copy)},
        "selection": {"check": cid, "observed": observed, "independent_after_attack": mismatch_value,
                      "committed_scope_reason_sha256": sha(committed_reason.encode("utf-8"))},
        "stable_snapshot": current_sha_before == current_sha_after_snapshot,
        "source_unchanged_during_tests": current_sha_end == current_sha_after_snapshot,
        "tree_unchanged": tree_before == tree_after,
        "cases": cases,
    }
    write(RUNS / "results.json", json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "run_dir": str(RUNS),
        "recorded_at": meta["recorded_at"],
        "head": head_before,
        "tree": tree_before,
        "baseline_sha256": baseline_sha,
        "candidate_sha256": current_sha_after_snapshot,
        "candidate_stable": meta["stable_snapshot"],
        "candidate_unchanged_during_tests": meta["source_unchanged_during_tests"],
        "capture_sha256": meta["capture_sha256"],
        "case_exits": {case["name"]: {rev: runinfo["exit"] for rev, runinfo in case["runs"].items()} for case in cases},
    }, indent=2))


if __name__ == "__main__":
    main()
