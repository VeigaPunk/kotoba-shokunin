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

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
CANDIDATE = DRAFT / "scope-probe-4ce43f7a-194756/compare-candidate.py"
EXPECTED_CANDIDATE = "4ce43f7aa67efa567f142c69c57bfdff39e7aa47b03e92f8a793ddc5a55e4217"
BASE_REF = "055d3b9:verifiers/compare_harness_independent.py"
LIVE = DRAFT / "final-live-7a6ca85c.json"
INDEPENDENT = DRAFT / "final-independent-7a6ca85c.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def put(path, data):
    if isinstance(data, str):
        data = data.encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def dump(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode()


def sync_probe(payload, cid, probe, reason):
    payload["scoped_out"][cid] = reason
    payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(probe)
    for channel in ("results", "rows"):
        for row in payload.get(channel, []):
            if row.get("check") == cid:
                row["probe"] = copy.deepcopy(probe)
                row["evidence"] = "SCOPED_OUT: " + reason


def main():
    candidate_data = CANDIDATE.read_bytes()
    candidate_sha = digest(candidate_data)
    if candidate_sha != EXPECTED_CANDIDATE:
        raise SystemExit(f"frozen candidate drift: expected {EXPECTED_CANDIDATE}, got {candidate_sha}")
    base_data = subprocess.check_output(["git", "show", BASE_REF], cwd=ROOT)
    base_sha = digest(base_data)
    live_raw, independent_raw, scope_raw = LIVE.read_bytes(), INDEPENDENT.read_bytes(), SCOPE.read_bytes()
    independent, scope = json.loads(independent_raw), json.loads(scope_raw)
    cid = "omp.catalogue.found"
    committed_reason = scope["scope_out"][cid]["reason"]
    committed_evidence = "SCOPED_OUT: " + committed_reason
    tag = datetime.now(timezone.utc).strftime("%H%M%S")
    out = DRAFT / f"scope-target-{candidate_sha[:8]}-{tag}"
    out.mkdir()
    base_path = put(out / "compare-055d3b9.py", base_data)
    candidate_path = put(out / "compare-candidate.py", candidate_data)
    live_path = put(out / "live.json", live_raw)
    scope_path = put(out / "scope.json", scope_raw)
    spec = importlib.util.spec_from_file_location("scope_target_candidate", candidate_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    control = copy.deepcopy(independent)
    for scope_id, probe in control["scoped_out_probes"].items():
        fresh = copy.deepcopy(probe)
        fresh["observable"] = module.recompute_probe(fresh)["observable"]
        reason = scope["scope_out"][scope_id]["reason"]
        sync_probe(control, scope_id, fresh, reason)

    carrier = out / "uncommitted-probe-carrier"
    carrier.mkdir()
    for name, stamp, count, mtime in (("a.jsonl", "2026-01-01T00:00:00.000Z", 1, 1700000000),
                                      ("b.jsonl", "2026-02-02T00:00:00.000Z", 4, 1800000000)):
        block = "\n".join(f"- entry {index}" for index in range(count))
        path = carrier / name
        path.write_text(json.dumps({"stamp": stamp, "text": f"<skills>{block}\n</skills>"}) + "\n",
                        encoding="utf-8")
        os.utime(path, (mtime, mtime))

    redirected = copy.deepcopy(control)
    redirected_probe = copy.deepcopy(redirected["scoped_out_probes"][cid])
    redirected_probe["target"] = str(carrier.resolve())
    redirected_probe["observable"] = module.recompute_probe(redirected_probe)["observable"]
    sync_probe(redirected, cid, redirected_probe, committed_reason)

    runs, inputs = {}, {}
    for name, payload in (("honest-control", control), ("valid-reason-retargeted-probe", redirected)):
        independent_path = put(out / f"{name}.independent.json", dump(payload))
        inputs[name] = {"independent": str(independent_path), "sha256": digest(independent_path.read_bytes())}
        for label, executable in (("baseline_055d3b9", base_path),
                                  ("candidate_" + candidate_sha[:8], candidate_path)):
            argv = [sys.executable, str(executable), "--live-json", str(live_path),
                    "--independent-json", str(independent_path), "--expect-n", "28", "--cwd", str(ROOT),
                    "--scope-file", str(scope_path), "--no-stamp", "--json"]
            proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)
            runs[f"{name}/{label}"] = {
                "argv": argv,
                "exit": proc.returncode,
                "stdout_sha256": digest(proc.stdout.encode()),
                "stderr_sha256": digest(proc.stderr.encode()),
                "stderr": proc.stderr,
                "agreement": json.loads(proc.stdout).get("agreement") if proc.stdout.strip() else None,
            }

    result = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "runner_sha256": digest(Path(__file__).read_bytes()),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "tree": subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip(),
        "baseline_sha256": base_sha,
        "candidate_sha256": candidate_sha,
        "candidate_snapshot_sha256_after": digest(candidate_path.read_bytes()),
        "live_sha256": digest(live_raw),
        "independent_capture_sha256": digest(independent_raw),
        "scope_sha256": digest(scope_raw),
        "selected_check": cid,
        "committed_target": scope["probe_contract"]["target"],
        "redirected_target": redirected_probe["target"],
        "valid_reason": redirected["scoped_out"][cid] == committed_reason,
        "valid_evidence_in_every_record_channel": all(
            row.get("evidence") == committed_evidence
            for channel in ("results", "rows")
            for row in redirected.get(channel, []) if row.get("check") == cid),
        "honest_observable": control["scoped_out_probes"][cid]["observable"],
        "recomputed_redirected_observable": redirected_probe["observable"],
        "inputs": inputs,
        "runs": runs,
    }
    put(out / "results.json", dump(result))
    print(json.dumps({"run_dir": str(out), "recorded_at": result["recorded_at"],
                      "runner_sha256": result["runner_sha256"], "candidate_sha256": candidate_sha,
                      "exits": {key: value["exit"] for key, value in runs.items()},
                      "stderr": {key: value["stderr"] for key, value in runs.items()}}, indent=2))


if __name__ == "__main__":
    main()
