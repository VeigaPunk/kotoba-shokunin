#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
TARGET = "032f47bd13fdff0cd2ccea5f902df9690ad09376"
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
LIVE_PRODUCER = ROOT / "verifiers/verify_harness_claims.py"
IND_PRODUCER = ROOT / "verifiers/verify_harness_independent.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
LIVE_FILE = DRAFT / "fresh-live.json"
IND_FILE = DRAFT / "fresh-independent.json"
RECEIPT = DRAFT / "fresh-join-receipt.json"
OUTPUT = DRAFT / "fresh-channel-hunts.json"
CID = "omp.offered.skills"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def run_driver(source, args):
    wrapper = (
        "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
        "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
        "{'__name__':'__main__','__file__':p})"
    )
    command = [sys.executable, "-c", wrapper, str(DRIVER), *args]
    proc = subprocess.run(command, cwd=ROOT, input=source.decode("utf-8"),
                          capture_output=True, text=True, timeout=300)
    try:
        data = json.loads(proc.stdout)
        reason = data.get("reason", "")
        headline = data.get("headline")
    except (ValueError, TypeError):
        data = None
        reason = (proc.stderr or proc.stdout).strip()[-1200:]
        headline = None
    return command, proc, data, reason, headline


def exact_value(record):
    for key in ("re_derived", "value", "observed", "expected", "expected_value"):
        if key in record:
            return record[key]
    raise ValueError("target record has no usable value")


def alternative(value):
    if isinstance(value, bool):
        return not value
    if isinstance(value, int):
        return value + 991
    if isinstance(value, float):
        return value + 991.25
    if isinstance(value, str):
        return value + "-conflict"
    if isinstance(value, list):
        return value + ["conflict"]
    if isinstance(value, dict):
        return dict(value, c2_conflict=True)
    return "c2-conflict"


def all_records(payload, cid):
    found = []
    for channel in ("results", "rows"):
        records = payload.get(channel)
        if isinstance(records, list):
            found.extend((channel, record) for record in records
                         if isinstance(record, dict) and record.get("check") == cid)
    if not found:
        raise ValueError(f"target {cid} absent from results/rows")
    return found


def make_hunts(independent):
    arms = {}

    expected_pair = copy.deepcopy(independent)
    for _channel, record in all_records(expected_pair, CID):
        chosen = exact_value(record)
        record["expected"] = chosen
        record["expected_value"] = alternative(chosen)
    arms["expected_expected_value_conflict"] = json.dumps(
        expected_pair, indent=2, sort_keys=True).encode("utf-8") + b"\n"

    lone_status = copy.deepcopy(independent)
    for _channel, record in all_records(lone_status, CID):
        record.pop("state", None)
        record["status"] = ["UNLANDED"]
    arms["status_lone_nonstring"] = json.dumps(
        lone_status, indent=2, sort_keys=True).encode("utf-8") + b"\n"

    duplicate_status = copy.deepcopy(independent)
    for channel in ("results", "rows"):
        rows = duplicate_status.get(channel)
        if not isinstance(rows, list):
            continue
        current = next((record for record in rows
                        if isinstance(record, dict) and record.get("check") == CID), None)
        if current is None:
            continue
        shadow = copy.deepcopy(current)
        shadow["status"] = "UNLANDED"
        current.setdefault("status", "DERIVED")
        rows.insert(0, shadow)
    arms["duplicate_id_status_precedence"] = json.dumps(
        duplicate_status, indent=2, sort_keys=True).encode("utf-8") + b"\n"

    nonstring_id = copy.deepcopy(independent)
    for _channel, record in all_records(nonstring_id, CID):
        record.pop("id", None)
        record["check"] = []
        record["name"] = CID
    arms["nonstring_check_alias"] = json.dumps(
        nonstring_id, indent=2, sort_keys=True).encode("utf-8") + b"\n"

    top_duplicate_payload = copy.deepcopy(independent)
    contradictory_results = copy.deepcopy(top_duplicate_payload.get("results"))
    for record in contradictory_results:
        if isinstance(record, dict) and record.get("check") == CID:
            key = next((name for name in ("re_derived", "value", "observed", "expected")
                        if name in record), None)
            if key is None:
                raise ValueError("target result has no value to mutate")
            record[key] = alternative(record[key])
            break
    honest_results = copy.deepcopy(top_duplicate_payload["results"])
    top_duplicate_payload.pop("results", None)
    tail = json.dumps(top_duplicate_payload, separators=(",", ":"), sort_keys=True)
    raw_top_duplicate = (
        "{\"results\":" + json.dumps(contradictory_results, separators=(",", ":")) +
        ",\"results\":" + json.dumps(honest_results, separators=(",", ":")) + "," + tail[1:]
    )
    parsed_duplicate = json.loads(raw_top_duplicate)
    if raw_top_duplicate.count("\"results\":") != 2 or parsed_duplicate["results"] != honest_results:
        raise ValueError("top-level duplicate results member was not constructed as intended")
    arms["duplicate_top_level_results_member"] = raw_top_duplicate.encode("utf-8") + b"\n"

    row_duplicate_payload = copy.deepcopy(independent)
    target_row = next(record for record in row_duplicate_payload["results"]
                      if isinstance(record, dict) and record.get("check") == CID)
    correct = exact_value(target_row)
    target_row["re_derived"] = "__C2_DUPLICATE_MEMBER__"
    raw_record_duplicate = json.dumps(row_duplicate_payload, separators=(",", ":"), sort_keys=True)
    marker = '"re_derived":"__C2_DUPLICATE_MEMBER__"'
    replacement = '"re_derived":' + json.dumps(alternative(correct), separators=(",", ":")) + "," + \
                  '"re_derived":' + json.dumps(correct, separators=(",", ":"))
    if marker not in raw_record_duplicate:
        raise ValueError("duplicate-record marker not found")
    raw_record_duplicate = raw_record_duplicate.replace(marker, replacement, 1)
    json.loads(raw_record_duplicate)
    arms["duplicate_record_rederived_member"] = raw_record_duplicate.encode("utf-8") + b"\n"

    extension = copy.deepcopy(independent)
    extension["extensions"] = {"results": [{"check": CID, "expected": alternative(exact_value(
        next(record for _channel, record in all_records(independent, CID))))}]}
    arms["unknown_nested_channel_carrier"] = json.dumps(
        extension, indent=2, sort_keys=True).encode("utf-8") + b"\n"
    return arms


def main():
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    comparator_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{TARGET}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    comparator_sha = sha_bytes(comparator_bytes)
    if head != TARGET or comparator_sha != "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56":
        raise RuntimeError("target commit or frozen comparator hash changed")
    source_hashes = {
        "live_producer": sha_file(LIVE_PRODUCER),
        "independent_producer": sha_file(IND_PRODUCER),
        "scope": sha_file(SCOPE),
        "worktree_comparator": sha_file(DRIVER),
    }
    captured = {}
    for name, path in (("live", LIVE_PRODUCER), ("independent", IND_PRODUCER)):
        start = datetime.now(timezone.utc).isoformat()
        proc = subprocess.run([sys.executable, "-B", str(path), "--json"], cwd=ROOT,
                              capture_output=True, text=True, timeout=300)
        end = datetime.now(timezone.utc).isoformat()
        if proc.returncode != 0:
            raise RuntimeError(f"{name} producer exit {proc.returncode}: {proc.stderr[-800:]}")
        payload = json.loads(proc.stdout)
        output_path = LIVE_FILE if name == "live" else IND_FILE
        raw = proc.stdout.encode("utf-8")
        output_path.write_bytes(raw)
        captured[name] = {
            "command": [sys.executable, "-B", str(path), "--json"],
            "started_at_utc": start,
            "finished_at_utc": end,
            "exit": proc.returncode,
            "producer_sha256": source_hashes["live_producer" if name == "live" else "independent_producer"],
            "output_path": str(output_path.relative_to(ROOT)),
            "output_sha256": sha_bytes(raw),
            "record_count": len(payload.get("results", [])) if isinstance(payload, dict) else None,
        }

    live = json.loads(LIVE_FILE.read_text(encoding="utf-8"))
    independent = json.loads(IND_FILE.read_text(encoding="utf-8"))
    if len(live.get("results", [])) != 28:
        raise RuntimeError("fresh live producer did not publish 28 results")
    for channel, record in all_records(independent, CID):
        if record.get("status") == "SCOPED_OUT":
            raise RuntimeError(f"hunt target {CID} unexpectedly scoped out in {channel}")

    def base_args(ind_path):
        return ["--live-json", str(LIVE_FILE), "--independent-json", str(ind_path),
                "--cwd", str(ROOT), "--scope-file", str(SCOPE), "--expect-n", "28",
                "--no-stamp", "--json"]

    base_command, base_proc, base_data, base_reason, base_headline = run_driver(
        comparator_bytes, base_args(IND_FILE) + ["--receipt", str(RECEIPT)])
    if base_data is None:
        raise RuntimeError("honest join returned no JSON: " + base_reason)
    base_result = {
        "command": base_command,
        "exit": base_proc.returncode,
        "reason": base_reason,
        "headline": base_headline,
        "agreement": base_data.get("agreement"),
        "receipt_path": str(RECEIPT.relative_to(ROOT)),
        "receipt_sha256": sha_file(RECEIPT) if RECEIPT.is_file() else None,
    }

    hunt_payloads = make_hunts(independent)
    arms = []
    immutable = {"live_json": sha_file(LIVE_FILE), "scope_file": sha_file(SCOPE)}
    for name, raw in sorted(hunt_payloads.items()):
        input_path = DRAFT / f"hunt-{name}.json"
        input_path.write_bytes(raw)
        before = {**immutable, "independent_json": sha_file(input_path)}
        command, proc, data, reason, headline = run_driver(
            comparator_bytes, base_args(input_path))
        after = {**immutable, "independent_json": sha_file(input_path)}
        arms.append({
            "id": name,
            "input_path": str(input_path.relative_to(ROOT)),
            "command": command,
            "independent_payload_sha256": before["independent_json"],
            "input_hashes_before": before,
            "input_hashes_after": after,
            "inputs_unchanged": before == after,
            "exit": proc.returncode,
            "headline": headline,
            "reason": reason,
            "stdout_sha256": sha_bytes(proc.stdout.encode()),
            "stderr_sha256": sha_bytes(proc.stderr.encode()),
        })

    after_hashes = {
        "live_producer": sha_file(LIVE_PRODUCER),
        "independent_producer": sha_file(IND_PRODUCER),
        "scope": sha_file(SCOPE),
        "worktree_comparator": sha_file(DRIVER),
        "frozen_comparator": sha_bytes(subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{TARGET}:verifiers/compare_harness_independent.py"],
            check=True, capture_output=True).stdout),
    }
    report = {
        "schema": "kotoba.round45.c2.fresh-channel-hunts.v1",
        "measured_at_utc": datetime.now(timezone.utc).isoformat(),
        "target": {
            "commit": head,
            "tree": tree,
            "comparator_path": "verifiers/compare_harness_independent.py",
            "frozen_comparator_sha256": comparator_sha,
            "execution": "git-show source loaded once and used for every comparator subprocess",
            "worktree_comparator_sha256_at_start": source_hashes["worktree_comparator"],
            "worktree_comparator_sha256_at_end": after_hashes["worktree_comparator"],
        },
        "sources": {
            "producer_and_scope_hashes_at_start": source_hashes,
            "producer_and_scope_hashes_at_end": after_hashes,
            "non_comparator_sources_unchanged": all(
                source_hashes[key] == after_hashes[key]
                for key in ("live_producer", "independent_producer", "scope")),
            "frozen_comparator_unchanged": after_hashes["frozen_comparator"] == comparator_sha,
            "captured_producers": captured,
            "live_json_sha256": sha_file(LIVE_FILE),
            "independent_json_sha256": sha_file(IND_FILE),
            "scope_sha256": sha_file(SCOPE),
        },
        "honest_join": base_result,
        "summary": {
            "fresh_hunt_arm_count": len(arms),
            "green_exit_0_arm_ids": [arm["id"] for arm in arms if arm["exit"] == 0],
            "nonzero_arm_ids": [arm["id"] for arm in arms if arm["exit"] != 0],
            "all_hunt_inputs_unchanged": all(arm["inputs_unchanged"] for arm in arms),
            "head_tree_unchanged": git("rev-parse", "HEAD") == head and git("rev-parse", "HEAD^{tree}") == tree,
        },
        "arms": arms,
    }
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("fresh_hunts: %d arms; exit-0=%s; honest exit=%d headline=%s" % (
        len(arms), ",".join(report["summary"]["green_exit_0_arm_ids"]),
        base_proc.returncode, base_headline))
    print("target=%s tree=%s frozen-comparator=%s worktree-start=%s end=%s" % (
        head, tree, comparator_sha, source_hashes["worktree_comparator"],
        after_hashes["worktree_comparator"]))
    print("output=%s sha256=%s" % (OUTPUT, sha_file(OUTPUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
