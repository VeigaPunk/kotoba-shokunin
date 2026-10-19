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
DRAFT = Path(__file__).resolve().parent
CANDIDATE = DRAFT / "scope-target-4ce43f7a-195106/compare-candidate.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
LIVE = DRAFT / "final-live-7a6ca85c.json"
INDEPENDENT = DRAFT / "final-independent-7a6ca85c.json"
EXPECTED_CANDIDATE = "4ce43f7aa67efa567f142c69c57bfdff39e7aa47b03e92f8a793ddc5a55e4217"
BASE_REF = "055d3b9:verifiers/compare_harness_independent.py"


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


def main():
    candidate = CANDIDATE.read_bytes()
    candidate_sha = digest(candidate)
    if candidate_sha != EXPECTED_CANDIDATE:
        raise SystemExit(f"candidate drift: expected {EXPECTED_CANDIDATE}, got {candidate_sha}")
    base = subprocess.check_output(["git", "show", BASE_REF], cwd=ROOT)
    base_sha = digest(base)
    live_raw, independent_raw, scope_raw = LIVE.read_bytes(), INDEPENDENT.read_bytes(), SCOPE.read_bytes()
    live, independent = json.loads(live_raw), json.loads(independent_raw)
    scope = json.loads(scope_raw)
    tag = datetime.now(timezone.utc).strftime("%H%M%S")
    out = DRAFT / f"scope-probe-{candidate_sha[:8]}-{tag}"
    out.mkdir()
    base_path = put(out / "compare-055d3b9.py", base)
    candidate_path = put(out / "compare-candidate.py", candidate)
    live_path = put(out / "live.json", live_raw)
    scope_path = put(out / "scope.json", scope_raw)
    spec = importlib.util.spec_from_file_location("scope_probe_candidate", candidate_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    control = copy.deepcopy(independent)
    for cid, probe in control["scoped_out_probes"].items():
        fresh = copy.deepcopy(probe)
        fresh["observable"] = module.recompute_probe(fresh)["observable"]
        control["scoped_out_probes"][cid] = copy.deepcopy(fresh)
        for channel in ("results", "rows"):
            for row in control.get(channel, []):
                if row.get("check") == cid:
                    row["probe"] = copy.deepcopy(fresh)

    attack = copy.deepcopy(control)
    target_id = "omp.catalogue.found"
    attack_probe = copy.deepcopy(attack["scoped_out_probes"][target_id])
    attack_probe["observable"]["candidate_blocks"] += 1000
    attack["scoped_out_probes"][target_id] = copy.deepcopy(attack_probe)
    for channel in ("results", "rows"):
        for row in attack.get(channel, []):
            if row.get("check") == target_id:
                row["probe"] = copy.deepcopy(attack_probe)

    runs = {}
    inputs = {}
    for name, payload in (("control", control), ("forged-observable", attack)):
        ind_path = put(out / f"{name}.independent.json", dump(payload))
        inputs[name] = {"independent": str(ind_path), "sha256": digest(ind_path.read_bytes())}
        for label, executable in (("baseline_055d3b9", base_path), ("candidate_" + candidate_sha[:8], candidate_path)):
            argv = [sys.executable, str(executable), "--live-json", str(live_path),
                    "--independent-json", str(ind_path), "--expect-n", "28", "--cwd", str(ROOT),
                    "--scope-file", str(scope_path), "--no-stamp", "--json"]
            proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=300)
            runs[f"{name}/{label}"] = {
                "argv": argv,
                "exit": proc.returncode,
                "stdout_sha256": digest(proc.stdout.encode()),
                "stderr_sha256": digest(proc.stderr.encode()),
                "stderr": proc.stderr,
                "agreement": (json.loads(proc.stdout).get("agreement") if proc.stdout.strip() else None),
            }
    current_after = digest(CANDIDATE.read_bytes())
    result = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "tree": subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip(),
        "baseline_sha256": base_sha,
        "candidate_sha256": candidate_sha,
        "candidate_sha256_after": current_after,
        "candidate_unchanged_during_test": current_after == candidate_sha,
        "live_sha256": digest(live_raw),
        "independent_capture_sha256": digest(independent_raw),
        "scope_sha256": digest(scope_raw),
        "committed_target": scope["probe_contract"]["target"],
        "selected_check": target_id,
        "valid_reason_preserved": control["scoped_out"][target_id] == scope["scope_out"][target_id]["reason"],
        "fresh_control_observable": control["scoped_out_probes"][target_id]["observable"],
        "forged_observable": attack_probe["observable"],
        "inputs": inputs,
        "runs": runs,
    }
    put(out / "results.json", dump(result))
    print(json.dumps({"run_dir": str(out), "recorded_at": result["recorded_at"],
                      "candidate_sha256": candidate_sha, "candidate_sha256_after": current_after,
                      "exits": {k: v["exit"] for k, v in runs.items()},
                      "stderr": {k: v["stderr"] for k, v in runs.items()}}, indent=2))


if __name__ == "__main__":
    main()
