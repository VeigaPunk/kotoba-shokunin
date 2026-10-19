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
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
LIVE_SOURCE = OUT / "final-live-7a6ca85c.json"
IND_SOURCE = OUT / "final-independent-7a6ca85c.json"
BASE_REF = "055d3b9:verifiers/compare_harness_independent.py"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(path.read_bytes())


def put(path, data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def jb(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def run(argv):
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)


def set_value(payload, cid, value):
    n = 0
    for channel in ("results", "rows"):
        for row in payload.get(channel, []) or []:
            if isinstance(row, dict) and row.get("check") == cid:
                for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                    if key in row:
                        row[key] = copy.deepcopy(value)
                        n += 1
    checks = payload.get("checks")
    if isinstance(checks, dict) and cid in checks:
        checks[cid] = copy.deepcopy(value)
        n += 1
    if not n:
        raise RuntimeError(f"no independent value changed for {cid}")


def replace_probe(payload, cid, probe):
    payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(probe)
    for channel in ("results", "rows"):
        for row in payload.get(channel, []) or []:
            if isinstance(row, dict) and row.get("check") == cid:
                row["probe"] = copy.deepcopy(probe)


def main():
    base_data = subprocess.check_output(["git", "show", BASE_REF], cwd=ROOT)
    base_sha = sha(base_data)
    candidate_data = DRIVER.read_bytes()
    candidate_sha = sha(candidate_data)
    tag = candidate_sha[:8]
    dest = OUT / f"final-adversarial-{tag}"
    if dest.exists():
        raise SystemExit(f"refusing to reuse {dest}")
    dest.mkdir()
    inp = dest / "inputs"
    inp.mkdir()
    base_path = put(dest / "compare-055d3b9.py", base_data)
    candidate_path = put(dest / "compare-current.py", candidate_data)
    live_raw = LIVE_SOURCE.read_bytes()
    ind_raw = IND_SOURCE.read_bytes()
    live = json.loads(live_raw)
    independent = json.loads(ind_raw)
    scope_raw = SCOPE.read_bytes()
    scope_obj = json.loads(scope_raw)
    live_copy = put(dest / "live-capture.json", live_raw)
    ind_copy = put(dest / "independent-capture.json", ind_raw)
    scope_copy = put(dest / "scope.json", scope_raw)
    cid = "oc.log.skills_rescan_max"
    if cid not in {r["check"] for r in live["results"]}:
        raise RuntimeError("live target row missing")
    target_row = next(r for r in live["results"] if r["check"] == cid)
    drift_value = int(target_row["observed"]) + 999
    cases = []

    def add(name, live_bytes, ind_bytes, expect_n=28, scope_bytes=None):
        lp = put(inp / f"{name}.live.json", live_bytes)
        ip = put(inp / f"{name}.independent.json", ind_bytes)
        sp = scope_copy if scope_bytes is None else put(inp / f"{name}.scope.json", scope_bytes)
        case = {"name": name, "expect_n": expect_n, "inputs": {
            "live": str(lp), "independent": str(ip), "scope": str(sp),
            "sha256": {"live": digest(lp), "independent": digest(ip), "scope": digest(sp)}}, "runs": {}}
        for label, executable in (("before_055d3b9", base_path), ("candidate_" + tag, candidate_path)):
            argv = [sys.executable, str(executable), "--live-json", str(lp),
                    "--independent-json", str(ip), "--expect-n", str(expect_n),
                    "--cwd", str(ROOT), "--scope-file", str(sp), "--no-stamp", "--json"]
            proc = run(argv)
            parsed = None
            try:
                parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
            except ValueError:
                pass
            case["runs"][label] = {
                "argv": argv,
                "exit": proc.returncode,
                "stdout_sha256": sha(proc.stdout.encode()),
                "stderr_sha256": sha(proc.stderr.encode()),
                "agreement": parsed.get("agreement") if isinstance(parsed, dict) else None,
                "reason": parsed.get("reason") if isinstance(parsed, dict) else None,
                "stderr": proc.stderr,
            }
        cases.append(case)

    # Live C2 controls and shadows over the actual current producer shape.
    add("honest-current-producer-control", live_raw, ind_raw)
    ind_drift = copy.deepcopy(independent)
    set_value(ind_drift, cid, drift_value)
    live_drift = copy.deepcopy(live)
    next(r for r in live_drift["results"] if r["check"] == cid)["mode"] = "positive"
    add("live-mode-row-shadow-vs-mirror", jb(live_drift), jb(ind_drift))

    live_summary = copy.deepcopy(live)
    path = live_summary["summary_paths"][cid]
    live_summary["observed"][path[0]][path[1]] = drift_value
    add("live-summary-path-shadow", jb(live_summary), ind_raw)

    live_bad_verdict = copy.deepcopy(live)
    next(r for r in live_bad_verdict["results"] if r["check"] == cid)["verdict"] = []
    add("live-nonstring-verdict", jb(live_bad_verdict), ind_raw)

    # A same-channel duplicate row with a last-positive mode still launders if
    # the producer summary and metadata maps are all omitted together.
    live_optout = copy.deepcopy(live_drift)
    for key in ("observed", "modes", "verdicts", "summary_paths"):
        live_optout.pop(key, None)
    add("live-summary-and-mirror-optout", jb(live_optout), jb(ind_drift))

    duplicate_rows = copy.deepcopy(live["results"])
    idx = next(i for i, row in enumerate(duplicate_rows) if row["check"] == cid)
    first = copy.deepcopy(duplicate_rows[idx])
    first["mode"] = "equal"
    last = copy.deepcopy(first)
    last["mode"] = "positive"
    duplicate_rows[idx:idx + 1] = [first, last]
    live_dupe = copy.deepcopy(live)
    live_dupe["results"] = duplicate_rows
    live_dupe["modes"][cid] = "positive"
    add("live-same-id-mode-duplicate", jb(live_dupe), jb(ind_drift))

    # Raw duplicate-member controls: a duplicate key below the nested value object.
    add("raw-nested-duplicate-value", b'{"results":[{"check":"sample.value","observed":{"nested":999},"mode":"equal","verdict":"PASS"}]}\n',
        b'{"results":[{"check":"sample.value","expected":{"nested":1,"nested":999},"re_derived":{"nested":999},"status":"DERIVED"}]}\n',
        1, jb({"scope_out": {}}))

    # Scope-out adversarial C3: exact committed reason/evidence, but target changed
    # to a small attacker-written carrier whose structural census recomputes.
    scope_id = "omp.catalogue.found"
    committed_reason = scope_obj["scope_out"][scope_id]["reason"]
    spec = importlib.util.spec_from_file_location("compare_probe", candidate_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    carrier = inp / "uncommitted-probe-carrier"
    carrier.mkdir()
    for name, stamp, count, mtime in (("a.jsonl", "2026-01-01T00:00:00.000Z", 1, 1700000000),
                                      ("b.jsonl", "2026-02-02T00:00:00.000Z", 4, 1800000000)):
        block = "\n".join(f"- entry {i}" for i in range(count))
        path_file = carrier / name
        path_file.write_text(json.dumps({"stamp": stamp, "text": f"<skills>{block}\n</skills>"}) + "\n", encoding="utf-8")
        os.utime(path_file, (mtime, mtime))
    redirected = {"kind": scope_obj["probe_contract"]["kind"], "target": str(carrier.resolve())}
    redirected["observable"] = module.recompute_probe(redirected)["observable"]
    redirected_ind = copy.deepcopy(independent)
    redirected_ind["scoped_out"][scope_id] = committed_reason
    for channel in ("results", "rows"):
        for row in redirected_ind.get(channel, []) or []:
            if row.get("check") == scope_id and "evidence" in row:
                row["evidence"] = committed_reason
    replace_probe(redirected_ind, scope_id, redirected)
    add("scopeout-committed-reason-fabricated-target", live_raw, jb(redirected_ind))

    fabricated = copy.deepcopy(redirected_ind)
    fake_probe = copy.deepcopy(redirected)
    fake_probe["observable"]["candidate_blocks"] += 1000
    replace_probe(fabricated, scope_id, fake_probe)
    add("scopeout-committed-reason-fabricated-observable", live_raw, jb(fabricated))

    reason_drift = copy.deepcopy(redirected_ind)
    reason_drift["scoped_out"][scope_id] = "valid-looking but fabricated blocker explanation"
    for channel in ("results", "rows"):
        for row in reason_drift.get(channel, []) or []:
            if row.get("check") == scope_id and "evidence" in row:
                row["evidence"] = "fabricated evidence conflicting with the committed entry"
    add("scopeout-reason-evidence-drift", live_raw, jb(reason_drift))

    record_shadow = copy.deepcopy(redirected_ind)
    bad_record = copy.deepcopy(redirected)
    bad_record["observable"]["candidate_blocks"] += 1000
    for channel in ("results", "rows"):
        for row in record_shadow.get(channel, []) or []:
            if row.get("check") == scope_id and "probe" in row:
                row["probe"] = copy.deepcopy(bad_record)
    add("scopeout-false-record-probe-shadow", live_raw, jb(record_shadow))

    current_end = digest(DRIVER)
    tree_before = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    result = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "head": run(["git", "rev-parse", "HEAD"]).stdout.strip(),
        "tree": tree_before,
        "baseline_ref": BASE_REF,
        "baseline_sha256": base_sha,
        "candidate_sha256": candidate_sha,
        "candidate_sha256_after": current_end,
        "candidate_unchanged_during_test": candidate_sha == current_end,
        "producer_sha256": {"live": digest(ROOT / "verifiers/verify_harness_claims.py"),
                             "independent": digest(ROOT / "verifiers/verify_harness_independent.py")},
        "capture_sha256": {"live": digest(live_copy), "independent": digest(ind_copy)},
        "scope_sha256": digest(SCOPE),
        "selected_live": {"check": cid, "observed": target_row["observed"], "skew_value": drift_value},
        "selected_scopeout": {"check": scope_id, "reason_sha256": sha(committed_reason.encode()),
                               "contract_target": scope_obj["probe_contract"].get("target")},
        "cases": cases,
    }
    put(dest / "results.json", json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"run_dir": str(dest), "recorded_at": result["recorded_at"],
                      "head": result["head"], "tree": tree_before, "baseline_sha256": base_sha,
                      "candidate_sha256": candidate_sha, "candidate_sha256_after": current_end,
                      "candidate_unchanged_during_test": result["candidate_unchanged_during_test"],
                      "exits": {c["name"]: {k: v["exit"] for k, v in c["runs"].items()} for c in cases}}, indent=2))


if __name__ == "__main__":
    main()
