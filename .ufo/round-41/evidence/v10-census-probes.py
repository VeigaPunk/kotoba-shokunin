#!/usr/bin/env python3
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
DRIVER = DRAFT / "compare-b1be35f.py"
LIVE_FILE = DRAFT / "live-b1be35f.json"
IND_FILE = DRAFT / "independent-b1be35f.json"
CARRIER = DRAFT / "builder-carrier"
SCOPE_REL = "verifiers/harness-independent-scope.json"
TARGET_ID = "omp.offered.skills"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load_driver():
    spec = importlib.util.spec_from_file_location("cmp_frozen_b1be35f", DRIVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capture():
    frozen = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "b1be35f:verifiers/compare_harness_independent.py"],
        capture_output=True, check=True).stdout
    DRIVER.write_bytes(frozen)
    live = subprocess.run(
        [sys.executable, str(ROOT / "verifiers/verify_harness_claims.py"), "--json"],
        cwd=ROOT, capture_output=True, text=True, timeout=300)
    independent = subprocess.run(
        [sys.executable, str(ROOT / "verifiers/verify_harness_independent.py"), "--json"],
        cwd=ROOT, capture_output=True, text=True, timeout=300)
    if live.returncode or independent.returncode:
        raise RuntimeError("producer capture failed: live=%d %s independent=%d %s" % (
            live.returncode, live.stderr[-500:], independent.returncode,
            independent.stderr[-500:]))
    LIVE_FILE.write_text(live.stdout, encoding="utf-8")
    IND_FILE.write_text(independent.stdout, encoding="utf-8")
    CARRIER.mkdir(parents=True, exist_ok=True)
    for name, stamp, entries in (("a.jsonl", "2026-01-01T00:00:00.000Z", 2),
                                 ("b.jsonl", "2026-02-02T00:00:00.000Z", 5)):
        rows = "\\n".join("- entry %d" % i for i in range(entries))
        (CARRIER / name).write_text(
            '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' %
            (stamp, rows), encoding="utf-8")
    os.utime(CARRIER / "a.jsonl", (1700000000, 1700000000))
    os.utime(CARRIER / "b.jsonl", (1700001000, 1700001000))
    return {
        "head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                               capture_output=True, text=True, check=True).stdout.strip(),
        "tree": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD^{tree}"],
                               capture_output=True, text=True, check=True).stdout.strip(),
        "comparator_sha256": sha(frozen),
        "comparator_live_sha256": sha((ROOT / "verifiers/compare_harness_independent.py").read_bytes()),
        "live_instrument_sha256": sha((ROOT / "verifiers/verify_harness_claims.py").read_bytes()),
        "independent_instrument_sha256": sha((ROOT / "verifiers/verify_harness_independent.py").read_bytes()),
        "live_payload_sha256": sha(LIVE_FILE.read_bytes()),
        "independent_payload_sha256": sha(IND_FILE.read_bytes()),
        "scope_sha256": sha((ROOT / SCOPE_REL).read_bytes()),
        "scope_worktree_sha256": sha((ROOT / SCOPE_REL).read_bytes()),
        "registry_worktree_sha256": sha((ROOT / "verifiers/floors-registry.json").read_bytes()),
        "guard_worktree_sha256": sha((ROOT / "verifiers/check_assertion_floors.py").read_bytes()),
        "tracked_status": subprocess.run(["git", "-C", str(ROOT), "status", "--short"],
                                         capture_output=True, text=True, check=True).stdout.strip().splitlines(),
        "captured_at_utc": subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                                           capture_output=True, text=True,
                                           check=True).stdout.strip(),
        "live_exit": live.returncode,
        "independent_exit": independent.returncode,
    }


def load_inputs():
    driver = load_driver()
    live = json.loads(LIVE_FILE.read_text(encoding="utf-8"))
    independent = json.loads(IND_FILE.read_text(encoding="utf-8"))
    return driver, live, independent


def id_map(records, key):
    return {record["check"]: record for record in records[key]}


def scored_ids(payload):
    return [r["check"] for r in payload["results"]
            if r.get("status") != "SCOPED_OUT"]


def probe_at(driver, target):
    observable = driver.recompute_probe({"kind": "rule-spread-census",
                                        "target": str(target)})["observable"]
    return {"kind": "rule-spread-census", "target": str(target),
            "observable": observable}


def replace_probe(payload, driver, target):
    for cid in list(payload.get("scoped_out_probes", {})):
        payload["scoped_out_probes"][cid] = probe_at(driver, target)
    for channel in ("results", "rows"):
        for record in payload.get(channel, []):
            if record.get("status") == "SCOPED_OUT" and isinstance(record.get("probe"), dict):
                record["probe"] = probe_at(driver, target)


def refresh_original_probes(payload, driver):
    for cid, probe in list(payload.get("scoped_out_probes", {}).items()):
        if isinstance(probe, dict) and isinstance(probe.get("target"), str):
            payload["scoped_out_probes"][cid] = probe_at(driver, probe["target"])
    for channel in ("results", "rows"):
        for record in payload.get(channel, []):
            probe = record.get("probe")
            if isinstance(probe, dict) and isinstance(probe.get("target"), str):
                record["probe"] = probe_at(driver, probe["target"])


def harvested(live):
    return {r["check"]: r["observed"] for r in live["results"]}


def row_mutation(payload, cid, change):
    for channel in ("results", "rows"):
        for record in payload[channel]:
            if record.get("check") == cid:
                change(record)


def change_all_value_channels(payload, cid, value):
    for channel in ("results", "rows"):
        for record in payload[channel]:
            if record.get("check") == cid:
                if "re_derived" in record:
                    record["re_derived"] = value
                record["value"] = value
    if cid in payload.get("checks", {}):
        payload["checks"][cid] = value


def add_committed_scope(payload, driver, scope_path):
    cid = TARGET_ID
    obs = harvested(json.loads(LIVE_FILE.read_text(encoding="utf-8")))[cid]
    row_mutation(payload, cid, lambda record: record.update(status="SCOPED_OUT"))
    payload.setdefault("scoped_out", {})[cid] = "probe-only author rule"
    payload.setdefault("scoped_out_probes", {})[cid] = probe_at(driver, CARRIER)
    row_mutation(payload, cid, lambda record: record.update(
        value=obs, re_derived=obs,
        probe=probe_at(driver, CARRIER)))
    scope = json.loads(scope_path.read_text(encoding="utf-8"))
    scope["scope_out"][cid] = {"kind": "rule-in-author-scope",
                                "reason": "probe-only author rule"}
    scope_path.parent.mkdir(parents=True, exist_ok=True)
    scope_path.write_text(json.dumps(scope, indent=2) + "\n", encoding="utf-8")


def arms(driver, live, original):
    values = harvested(live)
    names = scored_ids(original)
    out = {}

    def arm(name, mutate=lambda p: None, *, scope=None, cwd=None, receipt=None,
            live_payload=None):
        payload = copy.deepcopy(original)
        refresh_original_probes(payload, driver)
        mutate(payload)
        out[name] = {"payload": payload, "scope": scope, "process_cwd": cwd,
                     "receipt": receipt, "live_payload": live_payload}

    arm("control")

    def f2_notderived(p):
        for cid in names:
            row_mutation(p, cid, lambda r, v=values: r.update(
                expected=v[r["check"]], re_derived="NOT DERIVED", value="NOT DERIVED"))
            p["checks"][cid] = values[cid]
    arm("r1-f2-expected-not-derived", f2_notderived)

    def f3_rows(p):
        id_map(p, "rows")[TARGET_ID]["value"] = 999
    arm("r1-f3-rows-shadow", f3_rows)

    def a7_checks(p):
        p["checks"][TARGET_ID] = 999
    arm("v1-a7-checks-shadow", a7_checks)

    def rows_missing(p):
        p["rows"] = [r for r in p["rows"] if r["check"] != TARGET_ID]
    arm("f3-rows-missing", rows_missing)

    def consistent_disagreement(p):
        change_all_value_channels(p, TARGET_ID, 999)
    arm("f3-consistent-value-disagreement", consistent_disagreement)

    def status_unlanded(p):
        row_mutation(p, TARGET_ID, lambda r: r.update(status="UNLANDED"))
    arm("status-primary-unlanded", status_unlanded)

    def state_shadow(p):
        row_mutation(p, TARGET_ID, lambda r: r.update(state="UNLANDED"))
    arm("x2-state-shadow", state_shadow)

    def nonstring_status_shadow(p):
        row_mutation(p, TARGET_ID, lambda r: r.update(status=None, state="UNLANDED"))
    arm("status-nonstring-hides-state", nonstring_status_shadow)

    def meta(p):
        p["landed"] = 0
        p["unlanded"] = sorted(r["check"] for r in p["results"])
        p["provisional"] = sorted(r["check"] for r in p["results"])
        p["alternatives"] = {TARGET_ID: {"value": 999, "why": "fabricated"}}
    arm("top-level-status-and-alternatives", meta)

    def expected_only(p):
        for cid in names:
            for channel in ("results", "rows"):
                record = id_map(p, channel)[cid]
                for key in ("expected_value", "re_derived", "value", "observed"):
                    record.pop(key, None)
                record["expected"] = values[cid]
            p["checks"][cid] = values[cid]
    arm("heldout-expected-only-full-copy", expected_only)

    def expected_value_shadow(p):
        row_mutation(p, TARGET_ID, lambda r: r.update(
            expected=values[TARGET_ID], expected_value=999))
    arm("heldout-expected-value-secondary-shadow", expected_value_shadow)

    def derived_key_shadow(p):
        id_map(p, "results")[TARGET_ID]["value"] = 999
    arm("heldout-rederived-vs-value-shadow", derived_key_shadow)

    def observed_key_shadow(p):
        id_map(p, "results")[TARGET_ID]["observed"] = 999
    arm("heldout-observed-key-shadow", observed_key_shadow)

    def id_alias_shadow(p):
        row_mutation(p, TARGET_ID, lambda r: r.update(id="forged.id", name="forged.name"))
    arm("heldout-id-alias-conflict", id_alias_shadow)

    def duplicate_value(p):
        for channel in ("results", "rows"):
            records = p[channel]
            original_record = copy.deepcopy(id_map(p, channel)[TARGET_ID])
            original_record["re_derived"] = 999
            original_record["value"] = 999
            records.append(original_record)
    arm("t1-duplicate-id-divergent-copy", duplicate_value)

    def duplicate_status(p):
        for channel in ("results", "rows"):
            record = copy.deepcopy(id_map(p, channel)[TARGET_ID])
            record["status"] = "UNLANDED"
            p[channel].insert(0, record)
    arm("heldout-duplicate-id-status-shadow", duplicate_status)

    def map_control(p):
        p["rows"] = {r["check"]: r["value"] for r in p["rows"]}
    arm("row-map-agreeing-control", map_control)

    def map_shadow(p):
        p["rows"] = {r["check"]: r["value"] for r in p["rows"]}
        p["rows"][TARGET_ID] = 999
    arm("row-map-divergent", map_shadow)

    def string_shadow(p):
        id_map(p, "rows")[TARGET_ID]["value"] = str(values[TARGET_ID])
    arm("w1-stringified-rows", string_shadow)

    def results_map(p):
        p["results"] = {r["check"]: r.get("re_derived", r.get("value"))
                         for r in p["results"]}
    arm("results-dotted-map-control", results_map)

    def results_map_shadow(p):
        results_map(p)
        p["results"][TARGET_ID] = 999
    arm("results-dotted-map-divergent", results_map_shadow)

    def checks_list(p):
        p["checks"] = [{"id": cid, "value": value}
                        for cid, value in p["checks"].items()]
    arm("checks-record-list-control", checks_list)

    def checks_list_shadow(p):
        checks_list(p)
        next(r for r in p["checks"] if r["id"] == TARGET_ID)["value"] = 999
    arm("checks-record-list-divergent", checks_list_shadow)

    def scoped_value(p):
        cid = "omp.catalogue.total"
        change_all_value_channels(p, cid, 999)
    arm("w1-scoped-row-carries-value", scoped_value)

    def scoped_reason(p):
        cid = "omp.catalogue.total"
        p["scoped_out"][cid] = "not the committed reason"
        row_mutation(p, cid, lambda r: r.update(evidence="fabricated record evidence"))
    arm("scoped-out-reason-and-evidence-drift", scoped_reason)

    def target_redirect(p):
        replace_probe(p, driver, CARRIER)
    arm("r1-f4-payload-chosen-probe-target", target_redirect)

    def record_probe_shadow(p):
        cid = "omp.catalogue.total"
        false_probe = {"kind": "rule-spread-census", "target": str(CARRIER),
                       "observable": {"session_files": 0}}
        row_mutation(p, cid, lambda r: r.update(probe=false_probe))
    arm("record-probe-shadowed-by-top-level-map", record_probe_shadow)

    def record_probe_fallback_shadow(p):
        p.pop("scoped_out_probes", None)
        cid = "omp.catalogue.total"
        false_probe = {"kind": "rule-spread-census", "target": str(CARRIER),
                       "observable": {"session_files": 0}}
        for record in p["rows"]:
            if record.get("check") == cid:
                record["probe"] = false_probe
    arm("record-probe-fallback-reads-results-only", record_probe_fallback_shadow)

    def extra_probe(p):
        p["scoped_out_probes"]["forged.extra"] = {
            "kind": "unknown", "target": "/definitely/not/a/carrier"}
    arm("unmatched-extra-scoped-out-probe", extra_probe)

    def scope_uncommitted(p):
        cid = TARGET_ID
        p["scoped_out"][cid] = "probe-only author rule"
        p["scoped_out_probes"][cid] = probe_at(driver, CARRIER)
        row_mutation(p, cid, lambda r: r.update(
            status="SCOPED_OUT", value=values[cid], re_derived=values[cid],
            probe=probe_at(driver, CARRIER)))
    arm("scope-uncommitted-extra-row", scope_uncommitted)

    planted = DRAFT / "planted-cwd"
    planted_scope = planted / SCOPE_REL
    planted_scope.parent.mkdir(parents=True, exist_ok=True)
    if (ROOT / SCOPE_REL).is_file():
        shutil.copyfile(ROOT / SCOPE_REL, planted_scope)
    payload_scope = copy.deepcopy(original)
    refresh_original_probes(payload_scope, driver)
    add_committed_scope(payload_scope, driver, planted_scope)
    out["r1-f3-prime-scope-file-cwd"] = {
        "payload": payload_scope, "scope": SCOPE_REL,
        "process_cwd": planted, "receipt": DRAFT / "cwd-receipt.json"}
    out["r1-f3-prime-scope-file-honest-cwd-control"] = {
        "payload": payload_scope, "scope": SCOPE_REL,
        "process_cwd": ROOT, "receipt": None}
    out["scope-file-caller-selected-absolute"] = {
        "payload": payload_scope, "scope": planted_scope,
        "process_cwd": ROOT, "receipt": None}

    def scope_missing(p):
        p.pop("scoped_out", None)
    arm("scoped-out-record-without-map", scope_missing)

    def remove_uncovered(p):
        p["results"] = [r for r in p["results"] if r["check"] != TARGET_ID]
        p["rows"] = [r for r in p["rows"] if r["check"] != TARGET_ID]
        p["checks"].pop(TARGET_ID, None)
    arm("headline-uncovered-count", remove_uncovered)

    def expected_wrapper(p):
        values_map = harvested(live)
        p.clear()
        p["expected"] = values_map
    arm("heldout-nested-expected-wrapper", expected_wrapper)

    def wrappers_conflict(p):
        values_map = harvested(live)
        p.clear()
        p["expected"] = values_map
        p["observations"] = {cid: 999 for cid in values_map}
    arm("heldout-wrapper-precedence-expected-over-observations", wrappers_conflict)

    def observations_wrapper(p):
        p.clear()
        p["observations"] = harvested(live)
    arm("heldout-nested-observations-wrapper", observations_wrapper)

    def flat_map(p):
        p.clear()
        p.update(harvested(live))
    arm("heldout-flat-dotted-map", flat_map)

    def nested_map(p):
        p.clear()
        p["checks"] = harvested(live)
    arm("heldout-nested-checks-map", nested_map)

    def independent_drift(p):
        change_all_value_channels(p, TARGET_ID, 999)
    arm("live-mode-equal-with-independent-drift", independent_drift)

    live_positive = copy.deepcopy(live)
    id_map(live_positive, "results")[TARGET_ID]["mode"] = "positive"
    arm("live-mode-positive-masks-independent-drift", independent_drift,
        live_payload=live_positive)

    live_mode_split = copy.deepcopy(live_positive)
    live_mode_split["rows"] = copy.deepcopy(live_mode_split["results"])
    id_map(live_mode_split, "rows")[TARGET_ID]["mode"] = "equal"
    arm("live-mode-split-across-row-channels", independent_drift,
        live_payload=live_mode_split)

    live_summary = copy.deepcopy(live)
    live_summary["observed"]["omp"]["offered_skills"] = 999
    arm("live-top-level-observed-summary-divergence", live_payload=live_summary)

    live_verdict_split = copy.deepcopy(live)
    live_verdict_split["rows"] = copy.deepcopy(live_verdict_split["results"])
    id_map(live_verdict_split, "rows")[TARGET_ID]["verdict"] = "DRIFT"
    arm("live-verdict-shadow-in-row-channel", live_payload=live_verdict_split)

    return out


def run_case(driver, live, name, case):
    live_payload = case.get("live_payload")
    live_path = LIVE_FILE
    if live_payload is not None:
        live_path = DRAFT / ("live-arm-" + name + ".json")
        live_path.write_text(json.dumps(live_payload, indent=1, sort_keys=True) + "\n",
                             encoding="utf-8")
    ind_path = DRAFT / ("arm-" + name + ".json")
    ind_path.write_text(json.dumps(case["payload"], indent=1, sort_keys=True) + "\n",
                        encoding="utf-8")
    scope = case["scope"] or str(ROOT / SCOPE_REL)
    argv = ["--live-json", str(live_path), "--independent-json", str(ind_path),
            "--cwd", str(ROOT), "--scope-file", str(scope), "--no-stamp", "--json"]
    if case["receipt"]:
        argv += ["--receipt", str(case["receipt"])]
    process_cwd = case["process_cwd"] or ROOT
    previous = Path.cwd()
    stdout = io.StringIO()
    stderr = io.StringIO()
    try:
        os.chdir(process_cwd)
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exit_code = driver.main(argv)
    finally:
        os.chdir(previous)
    out_text, err_text = stdout.getvalue(), stderr.getvalue()
    try:
        meta = json.loads(out_text)
        reason = meta.get("reason", "")
        headline = meta.get("headline")
    except (ValueError, IndexError):
        meta = None
        reason = (err_text or out_text).strip()[-800:]
        headline = None
    return {
        "exit": exit_code,
        "reason": reason,
        "headline": headline,
        "stdout": out_text[-2500:],
        "stderr": err_text[-1200:],
        "live_payload_sha256": sha(live_path.read_bytes()),
        "independent_payload_sha256": sha(ind_path.read_bytes()),
        "command": [sys.executable, str(DRIVER), *argv],
        "process_cwd": str(process_cwd),
        "driver_cwd_arg": str(ROOT),
        "scope_file_arg": str(scope),
        "receipt_file": str(case["receipt"]) if case["receipt"] else None,
        "receipt": json.loads(case["receipt"].read_text()) if case["receipt"] and case["receipt"].is_file() else None,
    }


def main():
    meta = capture()
    driver, live, independent = load_inputs()
    meta["payload_top_level_keys"] = sorted(independent)
    meta["live_top_level_keys"] = sorted(live)
    meta["independent_results_fields"] = sorted(independent["results"][0])
    meta["independent_rows_fields"] = sorted(independent["rows"][0])
    meta["live_results_fields"] = sorted(live["results"][0])
    case_map = arms(driver, live, independent)
    results = {}
    for name, case in case_map.items():
        results[name] = run_case(driver, live, name, case)
    meta["arms"] = {name: {k: v for k, v in result.items() if k not in ("stdout", "stderr")}
                    for name, result in results.items()}
    meta["stdout_stderr"] = {name: {"stdout": r["stdout"], "stderr": r["stderr"]}
                             for name, r in results.items()}
    out = DRAFT / "probe-results.json"
    out.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for name, result in results.items():
        print("%-48s exit=%s headline=%s reason=%s" % (
            name, result["exit"],
            (result["headline"] or {}).get("n") if result["headline"] else "-",
            result["reason"][:180]))
    print("RESULTS", out)
    print("HEAD", meta["head"], "TREE", meta["tree"])
    print("COMPARATOR", meta["comparator_sha256"], "LIVE", meta["comparator_live_sha256"])
    print("PAYLOADS", meta["live_payload_sha256"], meta["independent_payload_sha256"])
    print("CAPTURED", meta["captured_at_utc"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
