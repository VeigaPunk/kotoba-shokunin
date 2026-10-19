#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
BASE_REF = "055d3b9:verifiers/compare_harness_independent.py"
PRIOR = OUT / "hunt-20261019T1630Z-r2" / "inputs"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(path.read_bytes())


def run(argv):
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)


def put(path, data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def jb(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def main():
    head = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    tree = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    current_bytes = DRIVER.read_bytes()
    current_sha = sha(current_bytes)
    base_bytes = subprocess.check_output(["git", "show", BASE_REF], cwd=ROOT)
    base_sha = sha(base_bytes)
    tag = current_sha[:8]
    dest = OUT / f"final-{tag}"
    if dest.exists():
        raise SystemExit(f"refusing to reuse {dest}")
    dest.mkdir()
    inp = dest / "inputs"
    inp.mkdir()
    current_path = put(dest / "compare-current.py", current_bytes)
    base_path = put(dest / "compare-055d3b9.py", base_bytes)
    if digest(DRIVER) != current_sha:
        raise SystemExit("comparator changed while snapshotting")
    live_orig_path = PRIOR / "live-positive-mode-shadow.live.json"
    ind_orig_path = PRIOR / "live-positive-mode-shadow.independent.json"
    live_orig = json.loads(live_orig_path.read_bytes())
    ind_orig = json.loads(ind_orig_path.read_bytes())
    scope_path = put(dest / "scope.json", SCOPE.read_bytes())
    cases = []

    def add(name, live, ind, expect_n=28, scope=None):
        live_path = put(inp / f"{name}.live.json", live)
        ind_path = put(inp / f"{name}.independent.json", ind)
        test_scope = scope_path if scope is None else put(inp / f"{name}.scope.json", scope)
        record = {
            "name": name,
            "live": str(live_path),
            "independent": str(ind_path),
            "scope": str(test_scope),
            "expect_n": expect_n,
            "sha256": {"live": digest(live_path), "independent": digest(ind_path), "scope": digest(test_scope)},
            "runs": {},
        }
        for label, exe in (("before_055d3b9", base_path), ("candidate_" + tag, current_path)):
            argv = [sys.executable, str(exe), "--live-json", str(live_path),
                    "--independent-json", str(ind_path), "--expect-n", str(expect_n),
                    "--cwd", str(ROOT), "--scope-file", str(test_scope), "--no-stamp", "--json"]
            proc = run(argv)
            parsed = None
            try:
                parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
            except ValueError:
                pass
            record["runs"][label] = {
                "argv": argv,
                "exit": proc.returncode,
                "stdout_sha256": sha(proc.stdout.encode()),
                "stderr_sha256": sha(proc.stderr.encode()),
                "reason": parsed.get("reason") if isinstance(parsed, dict) else None,
                "agreement": parsed.get("agreement") if isinstance(parsed, dict) else None,
                "stderr": proc.stderr,
            }
        cases.append(record)

    # C2 live input: mode-positive drift is green only because mirrors can be
    # opted out of by removing the top-level observed summary carrier entirely.
    positive_live = copy.deepcopy(live_orig)
    positive_ind = ind_orig
    add("live-positive-full-summary", jb(positive_live), jb(positive_ind))
    no_summary = copy.deepcopy(positive_live)
    no_summary.pop("observed", None)
    no_summary.pop("modes", None)
    no_summary.pop("verdicts", None)
    no_summary.pop("summary_paths", None)
    add("live-positive-summary-removed", jb(no_summary), jb(positive_ind))
    empty_summary = copy.deepcopy(positive_live)
    empty_summary["observed"] = {}
    empty_summary.pop("modes", None)
    empty_summary.pop("verdicts", None)
    empty_summary.pop("summary_paths", None)
    add("live-positive-summary-empty", jb(empty_summary), jb(positive_ind))

    nonstring = copy.deepcopy(no_summary)
    for row in nonstring["results"]:
        if row["check"] == "oc.log.skills_rescan_max":
            row["verdict"] = []
    add("live-nonstring-verdict-no-summary", jb(nonstring), jb(positive_ind))

    duplicate_mode = json.loads((PRIOR / "live-same-channel-duplicate-mode.live.json").read_bytes())
    duplicate_mode.pop("observed", None)
    add("live-duplicate-mode-no-summary", jb(duplicate_mode), jb(positive_ind))

    # New nested JSON duplicate control, exercising the current strict decoder.
    empty_scope = jb({"scope_out": {}})
    synthetic_live = b'{"results":[{"check":"sample.value","observed":{"nested":999},"verdict":"PASS","mode":"equal"}]}\n'
    synthetic_ind = b'{"results":[{"check":"sample.value","expected":{"nested":1,"nested":999},"re_derived":{"nested":999},"status":"DERIVED"}]}\n'
    add("raw-duplicate-nested-value-member", synthetic_live, synthetic_ind, 1, empty_scope)

    # Minimal, consistent single-row scope-out world to isolate C3's probe trust.
    cid = "omp.scope.test"
    reason = "committed blocker: selection is authored outside the substrate"
    scope_obj = {"probe_contract": {"kind": "rule-spread-census"},
                 "scope_out": {cid: {"kind": "rule-in-author-scope", "reason": reason}}}
    scope_bytes = jb(scope_obj)
    scope_obj_path = put(inp / "scope-probe-contract.json", scope_bytes)
    carrier = inp / "fabricated-carrier"
    carrier.mkdir()
    for name, stamp, n, mtime in (("a.jsonl", "2026-01-01T00:00:00.000Z", 1, 1700000000),
                                  ("b.jsonl", "2026-02-02T00:00:00.000Z", 4, 1800000000)):
        lines = "\\n".join(f"- entry {i}" for i in range(n))
        p = carrier / name
        p.write_text(json.dumps({"stamp": stamp, "text": f"<skills>{lines}\\n</skills>"}) + "\n", encoding="utf-8")
        os.utime(p, (mtime, mtime))

    spec = importlib.util.spec_from_file_location("candidate_probe", current_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    probe = {"kind": "rule-spread-census", "target": str(carrier.resolve())}
    probe["observable"] = module.recompute_probe(probe)["observable"]
    live_scope = {"observed": {}, "results": [{"check": cid, "observed": 5, "mode": "equal", "verdict": "PASS"}]}

    def scoped_payload(reason_text, probe_top, probe_record=None):
        rec_probe = probe_record if probe_record is not None else probe_top
        row = {"check": cid, "expected": None, "re_derived": None, "value": None,
               "status": "SCOPED_OUT", "probe": copy.deepcopy(rec_probe)}
        row_channel = {"check": cid, "value": None, "status": "SCOPED_OUT",
                       "evidence": "the scoped row is not derived blind",
                       "probe": copy.deepcopy(rec_probe)}
        return {
            "results": [row],
            "rows": [row_channel],
            "checks": {cid: None},
            "scoped_out": {cid: reason_text},
            "scoped_out_probes": {cid: copy.deepcopy(probe_top)},
        }

    good_ind = scoped_payload(reason, probe)
    add("scope-planted-valid-probe-target", jb(live_scope), jb(good_ind), 1, scope_bytes)

    fake_probe = copy.deepcopy(probe)
    fake_probe["observable"]["candidate_blocks"] += 1000
    fake_ind = scoped_payload(reason, fake_probe)
    add("scope-fabricated-observable-valid-reason", jb(live_scope), jb(fake_ind), 1, scope_bytes)

    reason_drift_ind = scoped_payload("valid but noncanonical scope-out explanation", probe)
    reason_drift_ind["rows"][0]["evidence"] = "fabricated evidence contradicting the committed explanation"
    add("scope-reason-evidence-drift", jb(live_scope), jb(reason_drift_ind), 1, scope_bytes)

    record_shadow_ind = scoped_payload(reason, probe, fake_probe)
    add("scope-false-record-probe-shadowed-by-map", jb(live_scope), jb(record_shadow_ind), 1, scope_bytes)

    head_after = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    tree_after = run(["git", "rev-parse", "HEAD^{tree}"]).stdout.strip()
    end_sha = digest(DRIVER)
    result = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "head": head,
        "tree_before": tree,
        "tree_after": tree_after,
        "head_after": head_after,
        "baseline_ref": BASE_REF,
        "baseline_sha256": base_sha,
        "candidate_sha256": current_sha,
        "candidate_sha256_after": end_sha,
        "candidate_unchanged_during_run": end_sha == current_sha,
        "scope_sha256": digest(SCOPE),
        "live_capture_sha256": digest(live_orig_path),
        "independent_capture_sha256": digest(ind_orig_path),
        "cases": cases,
    }
    put(dest / "results.json", json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "run_dir": str(dest),
        "recorded_at": result["recorded_at"],
        "head": head,
        "tree": tree,
        "baseline_sha256": base_sha,
        "candidate_sha256": current_sha,
        "candidate_sha256_after": end_sha,
        "candidate_unchanged_during_run": result["candidate_unchanged_during_run"],
        "exits": {c["name"]: {k: v["exit"] for k, v in c["runs"].items()} for c in cases},
    }, indent=2))


if __name__ == "__main__":
    main()
