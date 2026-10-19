#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
R41 = ROOT / ".ufo/round-41/evidence"
DRIVER_REL = "verifiers/compare_harness_independent.py"
DISPATCH_REV = "6881ce31912cf52982de733d18d25e7ab7aae5c4"
LANDED_REV = "032f47bd13fdff0cd2ccea5f902df9690ad09376"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
TARGET = "omp.catalogue.found"
FABRICATED = "fabricated blocker: no evidence; this row is not derivable because I say so"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return sha(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True).stdout


def git_text(*args):
    return git(*args).decode().strip()


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")


def load_driver(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def input_paths(command, process_cwd):
    result = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in command:
            value = Path(command[command.index(flag) + 1])
            result[flag[2:].replace("-", "_")] = (value if value.is_absolute()
                                                        else process_cwd / value).resolve()
    return result


def extract_result(proc):
    try:
        data = json.loads(proc.stdout)
        return data, data.get("reason", ""), data.get("headline")
    except (ValueError, TypeError):
        return None, (proc.stderr or proc.stdout).strip()[-1500:], None


def classify(source_class, exit_code):
    if source_class in ("open", "closed"):
        if exit_code == 0:
            return "open"
        return "closed"
    if source_class == "control":
        return "control" if exit_code == 0 else "red-control"
    if source_class == "diagnostic":
        return "diagnostic-open" if exit_code == 0 else "diagnostic-rejected"
    if source_class == "trust-input":
        return "trust-input" if exit_code == 0 else "trust-input-rejected"
    return "unclassified"


def replay_r41(snapshot_name, driver_path, arms, classifications, prior_replay):
    results = []
    prior_by_id = {arm["id"]: arm for arm in prior_replay["arms"]}
    with tempfile.TemporaryDirectory(prefix=f".{snapshot_name}-", dir=OUT) as scratch:
        for name, arm in sorted(arms.items()):
            command = list(arm["command"])
            command[1] = str(driver_path)
            if "--receipt" in command:
                command[command.index("--receipt") + 1] = str(
                    Path(scratch) / f"{name}.receipt.json")
            cwd = Path(arm["process_cwd"])
            paths = input_paths(command, cwd)
            before = {key: file_sha(path) for key, path in paths.items()}
            completed = subprocess.run(command, cwd=cwd, capture_output=True,
                                       text=True, timeout=120)
            after = {key: file_sha(path) for key, path in paths.items()}
            data, reason, headline = extract_result(completed)
            source_class = classifications[name][0]
            expected_inputs = prior_by_id[name].get("inputs_sha256_before", {})
            results.append({
                "id": name,
                "source_class_r41": source_class,
                "classification": classify(source_class, completed.returncode),
                "channel": classifications[name][1],
                "exit": completed.returncode,
                "headline": headline,
                "reason": reason,
                "command": command,
                "process_cwd": str(cwd),
                "input_sha256_before": before,
                "input_sha256_after": after,
                "inputs_unchanged": before == after,
                "matches_r41_input_hashes": not expected_inputs or before == expected_inputs,
                "stdout_sha256": sha(completed.stdout.encode()),
                "stderr_sha256": sha(completed.stderr.encode()),
                "result_keys": sorted(data) if isinstance(data, dict) else None,
            })
    counts = Counter(item["classification"] for item in results)
    return {
        "arm_count": len(results),
        "classification_counts": dict(sorted(counts.items())),
        "all_inputs_unchanged": all(item["inputs_unchanged"] for item in results),
        "all_r41_input_hashes_match": all(item["matches_r41_input_hashes"]
                                           for item in results),
        "arms": results,
    }


def carrier(path, counts):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    stamps = ["2026-01-01T00:00:00.000Z", "2026-02-02T00:00:00.000Z"]
    for index, (stamp, count) in enumerate(zip(stamps, counts)):
        text = "<skills>\n" + "\n".join(
            f"- entry-{index}-{i}" for i in range(count)) + "\n</skills>"
        (path / f"session-{index}.jsonl").write_text(
            json.dumps({"stamp": stamp, "text": text}) + "\n",
            encoding="utf-8")
        mtime = 1700000000 + index * 1000
        os.utime(path / f"session-{index}.jsonl", (mtime, mtime))
    return path.resolve()


def make_probe(driver, target):
    base = {"kind": "rule-spread-census", "target": str(target)}
    base["observable"] = driver.recompute_probe(base)["observable"]
    return base


def replace_probe(payload, cid, probe):
    payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(probe)
    for channel in ("results", "rows"):
        rows = payload.get(channel)
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and row.get("check") == cid:
                    row["probe"] = copy.deepcopy(probe)


def find_record(payload, channel, cid):
    for row in payload.get(channel, []):
        if isinstance(row, dict) and row.get("check") == cid:
            return row
    raise KeyError(f"{channel} has no row {cid}")


def run_fresh_case(name, payload, live_path, driver_path, scope_path, scope_sha):
    independent_path = OUT / f"fresh-{name}-independent.json"
    stdout_path = OUT / f"fresh-{name}-stdout.json"
    stderr_path = OUT / f"fresh-{name}-stderr.txt"
    receipt_path = OUT / f"fresh-{name}-receipt.json"
    write_json(independent_path, payload)
    command = [sys.executable, str(driver_path),
               "--live-json", str(live_path),
               "--independent-json", str(independent_path),
               "--expect-n", "28", "--cwd", str(ROOT),
               "--scope-file", str(scope_path), "--no-stamp", "--json",
               "--receipt", str(receipt_path)]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=180)
    stdout_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    data, reason, headline = extract_result(proc)
    return {
        "exit": proc.returncode,
        "headline": headline,
        "reason": reason,
        "command": command,
        "scope_path": str(scope_path),
        "scope_sha256": scope_sha,
        "independent_sha256": file_sha(independent_path),
        "live_sha256": file_sha(live_path),
        "stdout_sha256": file_sha(stdout_path),
        "stderr_sha256": file_sha(stderr_path),
        "receipt_sha256": file_sha(receipt_path) if receipt_path.is_file() else None,
        "scoped_out_result": data.get("scoped_out") if isinstance(data, dict) else None,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    started = utc()
    head = git_text("rev-parse", "HEAD")
    tree = git_text("rev-parse", "HEAD^{tree}")
    current_worktree_driver_sha = file_sha(ROOT / DRIVER_REL)
    scope_sha = file_sha(SCOPE)
    claim_sha = file_sha(ROOT / ".ufo/round-45/claims.json")

    dispatch_bytes = git("show", f"{DISPATCH_REV}:{DRIVER_REL}")
    landed_bytes = git("show", f"{LANDED_REV}:{DRIVER_REL}")
    dispatch_sha, landed_sha = sha(dispatch_bytes), sha(landed_bytes)
    dispatch_path = OUT / "dispatch-6881ce3.py"
    landed_path = OUT / "landed-032f47b.py"
    dispatch_path.write_bytes(dispatch_bytes)
    landed_path.write_bytes(landed_bytes)
    if landed_sha != "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56":
        raise RuntimeError(f"unexpected landed blob sha: {landed_sha}")

    probe_results_path = R41 / "probe-results.json"
    prior_replay_path = R41 / "subprocess-replay.json"
    census_path = R41 / "v10-channel-census.json"
    probe_results = json.loads(probe_results_path.read_text())
    prior_replay = json.loads(prior_replay_path.read_text())
    old_census = json.loads(census_path.read_text())
    census_module_path = R41 / "v10-channel-census.py"
    spec = importlib.util.spec_from_file_location("r41_channel_census", census_module_path)
    census_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(census_module)
    classifications = census_module.CASES
    arms = probe_results["arms"]
    if (len(arms) != 46 or len(prior_replay["arms"]) != 46
            or old_census["summary"]["classification_counts"].get("open") != 25
            or set(arms) != set(classifications)):
        raise RuntimeError("r41 source census is not the pinned 46-arm / 25-open set")

    dispatch = replay_r41("dispatch", dispatch_path, arms, classifications, prior_replay)
    landed = replay_r41("landed", landed_path, arms, classifications, prior_replay)
    landed_by_id = {arm["id"]: arm for arm in landed["arms"]}
    dispatch_by_id = {arm["id"]: arm for arm in dispatch["arms"]}
    changed = []
    for name in sorted(arms):
        before, after = dispatch_by_id[name], landed_by_id[name]
        if (before["exit"], before["headline"], before["reason"]) != (
                after["exit"], after["headline"], after["reason"]):
            changed.append({"id": name, "dispatch_exit": before["exit"],
                            "dispatch_headline": before["headline"],
                            "dispatch_reason": before["reason"],
                            "landed_exit": after["exit"],
                            "landed_headline": after["headline"],
                            "landed_reason": after["reason"]})
    replay_summary = {
        "started_at_utc": started,
        "finished_at_utc": utc(),
        "snapshot": {
            "head": head,
            "tree": tree,
            "round45_claim_sha256": claim_sha,
            "dispatch_commit": DISPATCH_REV,
            "dispatch_blob_sha256": dispatch_sha,
            "landed_commit": LANDED_REV,
            "landed_blob_sha256": landed_sha,
            "worktree_driver_sha256_at_start": current_worktree_driver_sha,
            "scope_sha256": scope_sha,
        },
        "sources": {
            "probe_results_sha256": file_sha(probe_results_path),
            "subprocess_replay_sha256": file_sha(prior_replay_path),
            "channel_census_sha256": file_sha(census_path),
            "r41_arm_count": len(arms),
            "r41_open_count": old_census["summary"]["classification_counts"]["open"],
        },
        "dispatch_replay": dispatch,
        "landed_replay": landed,
        "dispatch_to_landed_outcome_changes": changed,
    }
    write_json(OUT / "r41-replay.json", replay_summary)

    live_path = OUT / "fresh-live.json"
    independent_path = OUT / "fresh-independent.json"
    live_cmd = [sys.executable, str(ROOT / "verifiers/verify_harness_claims.py"), "--json"]
    ind_cmd = [sys.executable, str(ROOT / "verifiers/verify_harness_independent.py"), "--json"]
    live_source_sha = file_sha(ROOT / "verifiers/verify_harness_claims.py")
    independent_source_sha = file_sha(ROOT / "verifiers/verify_harness_independent.py")
    live_proc = subprocess.run(live_cmd, cwd=ROOT, capture_output=True, text=True,
                               timeout=300)
    ind_proc = subprocess.run(ind_cmd, cwd=ROOT, capture_output=True, text=True,
                              timeout=300)
    if live_proc.returncode != 0 or ind_proc.returncode != 0:
        raise RuntimeError("fresh producer capture failed: live=%s %s; independent=%s %s" % (
            live_proc.returncode, live_proc.stderr[-500:], ind_proc.returncode,
            ind_proc.stderr[-500:]))
    live_path.write_text(live_proc.stdout, encoding="utf-8")
    independent_path.write_text(ind_proc.stdout, encoding="utf-8")
    live_payload = json.loads(live_proc.stdout)
    independent_payload = json.loads(ind_proc.stdout)
    if file_sha(ROOT / "verifiers/verify_harness_claims.py") != live_source_sha:
        raise RuntimeError("live producer source changed during capture")
    if file_sha(ROOT / "verifiers/verify_harness_independent.py") != independent_source_sha:
        raise RuntimeError("independent producer source changed during capture")

    normal_command = [sys.executable, str(landed_path),
                      "--live-json", str(live_path),
                      "--independent-json", str(independent_path),
                      "--expect-n", "28", "--cwd", str(ROOT),
                      "--scope-file", str(SCOPE), "--no-stamp", "--json",
                      "--receipt", str(OUT / "fresh-current-join-receipt.json")]
    normal = subprocess.run(normal_command, cwd=ROOT, capture_output=True,
                            text=True, timeout=300)
    (OUT / "fresh-current-join.json").write_text(normal.stdout, encoding="utf-8")
    (OUT / "fresh-current-join.stderr.txt").write_text(normal.stderr, encoding="utf-8")
    normal_data, normal_reason, normal_headline = extract_result(normal)

    driver = load_driver(landed_path, "frozen_landed_compare")
    spread_carrier = carrier(OUT / "carrier-spread", [2, 5])
    flat_carrier = carrier(OUT / "carrier-flat", [3, 3])
    spread_probe = make_probe(driver, spread_carrier)
    flat_probe = make_probe(driver, flat_carrier)
    if len(spread_probe["observable"]["distinct_totals"]) < 2:
        raise RuntimeError("spread carrier did not create a rule spread")

    hunts = {}
    reason_mutant = copy.deepcopy(independent_payload)
    reason_mutant["scoped_out"][TARGET] = FABRICATED
    for channel in ("results", "rows"):
        row = find_record(reason_mutant, channel, TARGET)
        row["evidence"] = FABRICATED
    hunts["fabricated-payload-reason-and-evidence"] = run_fresh_case(
        "fabricated-reason-evidence", reason_mutant, live_path, landed_path,
        SCOPE, scope_sha)

    target_mutant = copy.deepcopy(independent_payload)
    replace_probe(target_mutant, TARGET, spread_probe)
    hunts["payload-target-unconstrained-by-scope-file"] = run_fresh_case(
        "uncommitted-probe-target", target_mutant, live_path, landed_path,
        SCOPE, scope_sha)

    false_scope_mutant = copy.deepcopy(independent_payload)
    replace_probe(false_scope_mutant, TARGET, flat_probe)
    hunts["same-total-probe-claims-row-out-of-scope"] = run_fresh_case(
        "derivable-flat-probe", false_scope_mutant, live_path, landed_path,
        SCOPE, scope_sha)

    derivable_mutant = copy.deepcopy(independent_payload)
    derived_id = "omp.offered.skills"
    derivable_reason = "fabricated scope-out for a row independently derived in this payload"
    derivable_probe = copy.deepcopy(spread_probe)
    for channel in ("results", "rows"):
        row = find_record(derivable_mutant, channel, derived_id)
        row["status"] = "SCOPED_OUT"
        row["evidence"] = derivable_reason
        row["probe"] = copy.deepcopy(derivable_probe)
    derivable_mutant.setdefault("scoped_out", {})[derived_id] = derivable_reason
    derivable_mutant.setdefault("scoped_out_probes", {})[derived_id] = derivable_probe
    hunts["already-derived-uncommitted-row-scoped-out"] = run_fresh_case(
        "derived-row-scope-out", derivable_mutant, live_path, landed_path,
        SCOPE, scope_sha)

    carries_value = copy.deepcopy(independent_payload)
    carried_id = "omp.catalogue.total"
    live_rows = {row["check"]: row["observed"] for row in live_payload["results"]}
    carried_value = live_rows[carried_id]
    for channel in ("results", "rows"):
        row = find_record(carries_value, channel, carried_id)
        row["re_derived"] = carried_value
        row["value"] = carried_value
        row["evidence"] = "fabricated evidence claims this scoped row is derivable"
    carries_value["checks"][carried_id] = carried_value
    hunts["committed-scope-row-carries-observed-value"] = run_fresh_case(
        "scoped-row-carries-derived-value", carries_value, live_path, landed_path,
        SCOPE, scope_sha)

    alternate_scope_path = OUT / "alternate-valid-kind-fabricated-reason-scope.json"
    alternate_scope = json.loads(SCOPE.read_text(encoding="utf-8"))
    alternate_scope["scope_out"][TARGET]["kind"] = "external-authority"
    alternate_scope["scope_out"][TARGET]["reason"] = FABRICATED
    write_json(alternate_scope_path, alternate_scope)
    alternate_sha = file_sha(alternate_scope_path)
    alternate_payload = copy.deepcopy(reason_mutant)
    hunts["caller-selected-valid-kind-fabricated-scope-entry"] = run_fresh_case(
        "caller-selected-fabricated-scope-entry", alternate_payload, live_path,
        landed_path, alternate_scope_path, alternate_sha)

    report = {
        "started_at_utc": started,
        "finished_at_utc": utc(),
        "snapshot": replay_summary["snapshot"],
        "producer_capture": {
            "live_command": live_cmd,
            "live_exit": live_proc.returncode,
            "live_source_sha256": live_source_sha,
            "live_payload_sha256": file_sha(live_path),
            "independent_command": ind_cmd,
            "independent_exit": ind_proc.returncode,
            "independent_source_sha256": independent_source_sha,
            "independent_payload_sha256": file_sha(independent_path),
        },
        "honest_join": {
            "command": normal_command,
            "exit": normal.returncode,
            "headline": normal_headline,
            "reason": normal_reason,
            "stdout_sha256": file_sha(OUT / "fresh-current-join.json"),
            "receipt_sha256": file_sha(OUT / "fresh-current-join-receipt.json")
            if (OUT / "fresh-current-join-receipt.json").is_file() else None,
            "protocol": normal_data.get("agreement") if isinstance(normal_data, dict) else None,
            "scoped_out": normal_data.get("scoped_out") if isinstance(normal_data, dict) else None,
        },
        "fresh_probe_inputs": {
            "spread_target": str(spread_carrier),
            "spread_observable": spread_probe["observable"],
            "flat_target": str(flat_carrier),
            "flat_observable": flat_probe["observable"],
            "committed_probe_contract": json.loads(SCOPE.read_text())["probe_contract"],
            "committed_scope_target_binding": "no target path appears in the committed scope entries or probe_contract",
        },
        "fresh_hunts": hunts,
        "final_hashes": {
            "comparator_worktree_sha256": file_sha(ROOT / DRIVER_REL),
            "scope_sha256": file_sha(SCOPE),
            "live_source_sha256": file_sha(ROOT / "verifiers/verify_harness_claims.py"),
            "independent_source_sha256": file_sha(ROOT / "verifiers/verify_harness_independent.py"),
        },
        "worktree_status_at_end": git_text("status", "--short"),
    }
    write_json(OUT / "fresh-hunts.json", report)
    print("r41 replay dispatch:", dispatch["classification_counts"])
    print("r41 replay landed:", landed["classification_counts"])
    print("dispatch-to-landed changed outcomes:", len(changed))
    print("honest join:", normal.returncode, normal_headline, normal_reason)
    for name, item in hunts.items():
        print(f"{name}: exit={item['exit']} headline={item['headline']} reason={item['reason'][:180]}")
    print("evidence:", OUT / "r41-replay.json", OUT / "fresh-hunts.json")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, subprocess.SubprocessError, ValueError, KeyError, TypeError) as exc:
        print(f"hunt_scoped_out: ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
