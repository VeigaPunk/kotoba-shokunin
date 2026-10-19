import contextlib
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
ROOT = DRAFT.parents[3]
EVIDENCE = ROOT / ".ufo/round-46/evidence/S2"
R41 = ROOT / ".ufo/round-41/evidence"
R40 = ROOT / ".ufo/round-40/evidence"
R44 = ROOT / ".ufo/round-44/evidence"
R45 = ROOT / ".ufo/round-45/evidence"
COMPARATOR_REL = "verifiers/compare_harness_independent.py"
EXPECTED_COMPARATORS = {
    "r41-b1be35f": "1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76",
    "r44-dispatch-6881ce3": "d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d",
    "r45-landed-032f47b": "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56",
    "head-055d3b9": "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4",
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return digest(Path(path).read_bytes())


def committed_sha(path):
    relative = Path(path).resolve().relative_to(ROOT).as_posix()
    committed = digest(git("show", f"HEAD:{relative}", binary=True))
    actual = sha_file(path)
    if actual != committed:
        raise RuntimeError(f"worktree differs from HEAD for {relative}: {actual} != {committed}")
    return actual


def git(*args, binary=False):
    result = subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                            capture_output=True, text=not binary)
    return result.stdout if binary else result.stdout.strip()


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def frozen_comparator(ref, label):
    data = git("show", f"{ref}:{COMPARATOR_REL}", binary=True)
    actual = digest(data)
    if actual != EXPECTED_COMPARATORS[label]:
        raise RuntimeError(f"comparator pin mismatch for {label}: {actual}")
    path = EVIDENCE / "drivers" / f"{label}.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def input_paths(command, cwd):
    paths = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in command:
            arg = Path(command[command.index(flag) + 1])
            paths[flag[2:].replace("-", "_")] = (arg if arg.is_absolute() else cwd / arg).resolve()
    return paths


def parse_compare(proc):
    try:
        payload = json.loads(proc.stdout)
        return payload.get("headline"), payload.get("reason", ""), payload
    except (ValueError, TypeError):
        return None, (proc.stderr or proc.stdout).strip()[-1200:], None


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay_census(source, census_module, drivers, scope_snapshot):
    reports = {}
    for label, driver in drivers.items():
        started = stamp()
        arms = []
        for arm_id, expected in sorted(source["arms"].items()):
            command = list(expected["command"])
            command[1] = str(driver)
            if "--scope-file" in command:
                command[command.index("--scope-file") + 1] = str(scope_snapshot)
            if "--receipt" in command:
                receipt = EVIDENCE / "receipts" / f"{label}-{arm_id}.json"
                receipt.parent.mkdir(parents=True, exist_ok=True)
                command[command.index("--receipt") + 1] = str(receipt)
            cwd = Path(expected["process_cwd"])
            paths = input_paths(command, cwd)
            before = {key: sha_file(path) for key, path in paths.items()}
            proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=120,
                                  env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            headline, reason, payload = parse_compare(proc)
            after = {key: sha_file(path) for key, path in paths.items()}
            unchanged = before == after
            saved_inputs_match = (
                before.get("independent_json") == expected.get("independent_payload_sha256")
                and before.get("live_json") == expected.get("live_payload_sha256")
            )
            scope_pin_matches = before.get("scope_file") == source["scope_sha256"]
            baseline_output_match = (
                proc.returncode == expected["exit"]
                and headline == expected.get("headline")
                and reason == expected["reason"]
            )
            matched = (unchanged and saved_inputs_match and scope_pin_matches
                       and (label != "r41-b1be35f" or baseline_output_match))
            origin_class, channel, finding = census_module.CASES[arm_id]
            if origin_class == "open":
                observed_class = "still-open" if proc.returncode == 0 else "closed-on-target"
            elif origin_class == "closed":
                observed_class = "closed" if proc.returncode != 0 else "unexpected-green"
            else:
                observed_class = origin_class
            arms.append({
                "id": arm_id,
                "baseline_classification": origin_class,
                "channel": channel,
                "finding": finding,
                "command": command,
                "process_cwd": str(cwd),
                "driver_cwd_arg": expected["driver_cwd_arg"],
                "scope_file_arg": str(scope_snapshot),
                "exit": proc.returncode,
                "headline": headline,
                "reason": reason,
                "stdout_sha256": digest(proc.stdout.encode("utf-8")),
                "stderr_sha256": digest(proc.stderr.encode("utf-8")),
                "inputs_sha256_before": before,
                "inputs_sha256_after": after,
                "input_hashes_unchanged": unchanged,
                "saved_live_and_independent_hashes_match": saved_inputs_match,
                "saved_scope_hash_matches_r41_pin": scope_pin_matches,
                "matches_r41_saved_result": baseline_output_match if label == "r41-b1be35f" else None,
                "matched": matched,
                "observed_classification": observed_class,
                "actual": {"exit": proc.returncode, "headline": headline,
                           "reason": reason, "stderr_tail": proc.stderr[-400:]},
                "stderr_tail": proc.stderr[-600:],
            })
        exit_counts = dict(sorted(Counter(str(row["exit"]) for row in arms).items()))
        class_counts = dict(sorted(Counter(row["observed_classification"] for row in arms).items()))
        replay_path = EVIDENCE / f"{label}-r41-replay.json"
        replay = {
            "schema": "kotoba.round46.s2.r41-exact-payload-replay.v1",
            "started_at_utc": started,
            "finished_at_utc": stamp(),
            "head": git("rev-parse", "HEAD"),
            "tree": git("rev-parse", "HEAD^{tree}"),
            "driver_label": label,
            "driver_sha256": sha_file(driver),
            "r41_source_sha256": sha_file(R41 / "probe-results.json"),
            "r41_baseline_census_sha256": sha_file(R41 / "v10-channel-census.json"),
            "frozen_head": source["head"],
            "frozen_tree": source["tree"],
            "comparator_sha256": sha_file(driver),
            "live_payload_sha256": source["live_payload_sha256"],
            "independent_payload_sha256": source["independent_payload_sha256"],
            "scope_sha256": source["scope_sha256"],
            "scope_snapshot_sha256": sha_file(scope_snapshot),
            "r41_recorded_frozen_head": source["head"],
            "r41_recorded_frozen_tree": source["tree"],
            "r41_recorded_frozen_comparator_sha256": source["comparator_sha256"],
            "arm_count": len(arms),
            "process_count": len(arms),
            "matched_count": sum(row["matched"] for row in arms),
            "mismatches": [row["id"] for row in arms if not row["matched"]],
            "all_inputs_unchanged": all(row["input_hashes_unchanged"] for row in arms),
            "all_saved_live_and_independent_hashes_match": all(
                row["saved_live_and_independent_hashes_match"] for row in arms),
            "all_saved_scope_hashes_match_r41_pin": all(
                row["saved_scope_hash_matches_r41_pin"] for row in arms),
            "exit_counts": exit_counts,
            "classification_counts": class_counts,
            "still_open_original_ids": [row["id"] for row in arms
                                         if row["observed_classification"] == "still-open"],
            "unexpected_green_ids": [row["id"] for row in arms
                                      if row["observed_classification"] == "unexpected-green"],
            "arms": arms,
        }
        write_json(replay_path, replay)
        census_module.SOURCE = replay_path
        census_path = EVIDENCE / f"{label}-r41-channel-census.json"
        census_module.OUTPUT = census_path
        capture = io.StringIO()
        census_error = None
        try:
            with contextlib.redirect_stdout(capture):
                census_rc = census_module.main()
        except ValueError as exc:
            census_rc = 1
            census_error = f"{type(exc).__name__}: {exc}"
        census_result = None
        if census_error is None:
            census_result = json.loads(census_path.read_text(encoding="utf-8"))
            census_record = {
                "exit": census_rc,
                "status": "generated",
                "output": str(census_path.relative_to(ROOT)),
                "output_sha256": sha_file(census_path),
                "summary": census_result["summary"],
                "validation": census_result["validation"],
                "stdout": capture.getvalue().strip(),
            }
        else:
            census_record = {
                "exit": census_rc,
                "status": "refused-invalid-replay",
                "error": census_error,
                "output": None,
                "output_sha256": None,
                "stdout": capture.getvalue().strip(),
            }
        replay["census_replay"] = census_record
        write_json(replay_path, replay)
        reports[label] = {
            "path": str(replay_path.relative_to(ROOT)),
            "sha256": sha_file(replay_path),
            "arm_count": len(arms),
            "matched_count": replay["matched_count"],
            "all_inputs_unchanged": replay["all_inputs_unchanged"],
            "saved_hashes_match": replay["all_saved_live_and_independent_hashes_match"],
            "all_scope_hashes_match_r41_pin": replay["all_saved_scope_hashes_match_r41_pin"],
            "baseline_output_match_count": sum(row["matches_r41_saved_result"] is True for row in arms),
            "exit_counts": exit_counts,
            "classification_counts": class_counts,
            "census_status": census_record["status"],
            "census_output_sha256": census_record["output_sha256"],
            "census_validation": census_result["validation"] if census_result else None,
            "census_error": census_error,
        }
    return reports


def run_union_c1_c2(union_module, drivers, scope_snapshot):
    live_path = R41 / "live-b1be35f.json"
    independent_path = R41 / "independent-b1be35f.json"
    expected_live = "0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341"
    expected_independent = "eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887"
    committed_sha(live_path)
    committed_sha(independent_path)
    head_scope = git("show", "HEAD:verifiers/harness-independent-scope.json", binary=True)
    if digest(head_scope) != sha_file(scope_snapshot):
        raise RuntimeError("R40 union scope snapshot differs from the committed HEAD scope")
    if sha_file(live_path) != expected_live or sha_file(independent_path) != expected_independent:
        raise RuntimeError("R40 union captured inputs do not match the cited producer pins")
    live = json.loads(live_path.read_text(encoding="utf-8"))
    independent = json.loads(independent_path.read_text(encoding="utf-8"))
    report = {
        "schema": "kotoba.round46.s2.union-battery-safe-subset.v1",
        "started_at_utc": stamp(),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "source_sha256": sha_file(R40 / "union-battery.py"),
        "live_input_sha256": sha_file(live_path),
        "independent_input_sha256": sha_file(independent_path),
        "scope_sha256": sha_file(scope_snapshot),
        "scope_head_blob": git("rev-parse", "HEAD:verifiers/harness-independent-scope.json"),
        "worktree_scope_sha256": sha_file(ROOT / "verifiers/harness-independent-scope.json"),
        "worktree_floors_guard_sha256": sha_file(ROOT / "verifiers/check_assertion_floors.py"),
        "floors_guard_head_blob": git("rev-parse", "HEAD:verifiers/check_assertion_floors.py"),
        "floors_guard_committed_sha256": digest(
            git("show", "HEAD:verifiers/check_assertion_floors.py", binary=True)),
        "drivers": {},
        "C3": {
            "status": "not rerun",
            "reason": "the committed run_c3 helper executes git init and git add in each temporary world; the lane forbids Git add/mutation",
            "prior_committed_record": str((ROOT / ".ufo/round-45/scouts/S2.md").relative_to(ROOT)),
            "prior_report_sha256": sha_file(ROOT / ".ufo/round-45/scouts/S2.md"),
        },
    }
    source_scope_sha = sha_file(scope_snapshot)
    for label, driver in drivers.items():
        wrapper = EVIDENCE / "drivers" / f"union-{label}-scoped.py"
        wrapper.write_text("\n".join([
            "import os, sys",
            f"driver = {str(driver)!r}",
            f"scope = {str(scope_snapshot)!r}",
            "os.execv(sys.executable, [sys.executable, driver, *sys.argv[1:], '--scope-file', scope])",
            "",
        ]), encoding="utf-8")
        work = EVIDENCE / "union" / label / "work"
        work.mkdir(parents=True, exist_ok=False)
        c1 = union_module.run_c1(ROOT, independent, live, work, wrapper)
        join_argv = [sys.executable, str(driver), "--live-json", str(live_path),
                     "--independent-json", str(independent_path), "--cwd", str(ROOT),
                     "--scope-file", str(scope_snapshot), "--json"]
        before = {"live": sha_file(live_path), "independent": sha_file(independent_path),
                  "scope": sha_file(scope_snapshot)}
        join = subprocess.run(join_argv, cwd=ROOT, text=True, capture_output=True, timeout=300,
                              env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        after = {"live": sha_file(live_path), "independent": sha_file(independent_path),
                 "scope": sha_file(scope_snapshot)}
        headline, reason, payload = parse_compare(join)
        report["drivers"][label] = {
            "driver_sha256": sha_file(driver),
            "scope_injecting_wrapper_sha256": sha_file(wrapper),
            "C1": c1,
            "LIVE_JOIN": {"command": join_argv, "exit": join.returncode,
                          "headline": headline, "reason": reason,
                          "stdout_sha256": digest(join.stdout.encode("utf-8")),
                          "stderr_sha256": digest(join.stderr.encode("utf-8")),
                          "inputs_sha256_before": before, "inputs_sha256_after": after,
                          "inputs_unchanged": before == after,
                          "inputs_match_R41_pins": before == {
                              "live": expected_live, "independent": expected_independent,
                              "scope": source_scope_sha}},
        }
    guard_source_repo = EVIDENCE / "union" / "head-055d3b9-guard-source"
    guard_source = guard_source_repo / "verifiers/check_assertion_floors.py"
    guard_source.parent.mkdir(parents=True, exist_ok=True)
    guard_source.write_bytes(git("show", "HEAD:verifiers/check_assertion_floors.py", binary=True))
    c2_work = EVIDENCE / "union" / "head-055d3b9-c2" / "work"
    c2_work.mkdir(parents=True, exist_ok=False)
    report["C2_head_guard"] = union_module.run_c2(guard_source_repo, c2_work)
    report["finished_at_utc"] = stamp()
    out = EVIDENCE / "union-battery-safe-subset.json"
    write_json(out, report)
    return {"path": str(out.relative_to(ROOT)), "sha256": sha_file(out),
            "drivers": {key: {"driver_sha256": val["driver_sha256"],
                              "C1_exits": {row["arm"]: row["exit"] for row in val["C1"]},
                              "join": val["LIVE_JOIN"]}
                        for key, val in report["drivers"].items()},
            "C2_exits": {row["arm"]: row["exit"] for row in report["C2_head_guard"]},
            "C3": report["C3"]}


def run_record_map_fixtures(drivers):
    fixture_base = Path("verifiers/fixtures/compare-harness-independent")
    stage_root = EVIDENCE / "record-map-head-tree"
    fixture_names = ("record-map-24-control", "record-map-24-composition")
    head_pins = {}
    for fixture_name in fixture_names:
        fixture_rel = fixture_base / fixture_name
        for relative in git("ls-tree", "-r", "--name-only", "HEAD", "--", str(fixture_rel)).splitlines():
            data = git("show", f"HEAD:{relative}", binary=True)
            destination = stage_root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            head_pins[relative] = {"blob": git("rev-parse", f"HEAD:{relative}"),
                                   "sha256": digest(data)}
    fixture_root = stage_root / fixture_base
    result_rows = []
    expected_materialized_hashes = {
        "record-map-24-control": "f4437143dd0892e7b1736a55893c98cb29f97543bc3aa2a940d888863d1b9adf",
        "record-map-24-composition": "1656893090d5d51ba675691551306ea90fecf4e2a9dad208ad648200b9243afb",
    }
    for fixture_name in fixture_names:
        folder = fixture_root / fixture_name
        case_path = folder / "case.json"
        case = json.loads(case_path.read_text(encoding="utf-8"))
        live_path = (folder / case["live"]).resolve()
        scope_path = (folder / case["scope"]).resolve()
        independent_source_path = folder / case["independent"]
        carrier_rel = Path(os.path.normpath((fixture_base / fixture_name / case["probe_carrier"]).as_posix()))
        carrier_path = ROOT / carrier_rel
        carrier_files = sorted(path for path in carrier_path.rglob("*") if path.is_file())
        carrier_pins = {}
        for carrier_file in carrier_files:
            relative = carrier_file.relative_to(ROOT).as_posix()
            head_data = git("show", f"HEAD:{relative}", binary=True)
            if sha_file(carrier_file) != digest(head_data):
                raise RuntimeError(f"worktree carrier differs from HEAD: {relative}")
            carrier_pins[str(carrier_file.relative_to(carrier_path))] = digest(head_data)
        staged_sources = {
            "case": case_path.relative_to(stage_root).as_posix(),
            "live": live_path.relative_to(stage_root).as_posix(),
            "scope": scope_path.relative_to(stage_root).as_posix(),
            "independent_fixture_source": independent_source_path.relative_to(stage_root).as_posix(),
        }
        source_hashes = {key: sha_file(stage_root / relative)
                         for key, relative in staged_sources.items()}
        if any(source_hashes[key] != head_pins[relative]["sha256"]
               for key, relative in staged_sources.items()):
            raise RuntimeError(f"staged HEAD fixture pin mismatch: {fixture_name}")
        independent_source = independent_source_path.read_text(encoding="utf-8")
        materialized = independent_source.replace("@fixture:carrier@", str(carrier_path))
        if "@fixture:carrier@" in materialized:
            raise RuntimeError(f"fixture marker remains in {fixture_name}")
        independent_path = EVIDENCE / "record-map-inputs" / f"{fixture_name}-independent.json"
        independent_path.parent.mkdir(parents=True, exist_ok=True)
        independent_path.write_text(materialized, encoding="utf-8")
        if sha_file(independent_path) != expected_materialized_hashes[fixture_name]:
            raise RuntimeError(f"materialized fixture hash mismatch for {fixture_name}: {sha_file(independent_path)}")
        before = {**source_hashes, "materialized_independent": sha_file(independent_path),
                  "carrier": carrier_pins}
        for driver_label, driver in drivers.items():
            argv = [sys.executable, str(driver), "--live-json", str(live_path),
                    "--independent-json", str(independent_path), "--expect-n", str(case["expect_n"]),
                    "--cwd", str(ROOT), "--scope-file", str(scope_path), "--no-stamp", "--json"]
            proc = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True, timeout=120,
                                  env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
            headline, reason, payload = parse_compare(proc)
            after = {**{key: sha_file(stage_root / relative)
                        for key, relative in staged_sources.items()},
                     "materialized_independent": sha_file(independent_path),
                     "carrier": {str(path.relative_to(carrier_path)): sha_file(path)
                                 for path in carrier_files}}
            combined = proc.stdout + proc.stderr
            expect = case["expect"]
            expectation_met = (proc.returncode == expect["exit"]
                               and all(text in combined for text in expect["named"])
                               and all(text not in combined for text in expect["absent"]))
            result_rows.append({
                "fixture": fixture_name,
                "case_sha256": source_hashes["case"],
                "fixture_independent_source_sha256": source_hashes["independent_fixture_source"],
                "materialized_independent_sha256": sha_file(independent_path),
                "fixture_head_blob_pins": {key: head_pins[relative]
                                            for key, relative in staged_sources.items()},
                "carrier_head_sha256": carrier_pins,
                "driver": driver_label,
                "driver_sha256": sha_file(driver),
                "argv": argv,
                "process_cwd": str(ROOT),
                "exit": proc.returncode,
                "headline": headline,
                "reason": reason,
                "stdout_sha256": digest(proc.stdout.encode("utf-8")),
                "stderr_sha256": digest(proc.stderr.encode("utf-8")),
                "inputs_before": before,
                "inputs_after": after,
                "inputs_unchanged": before == after,
                "expect": expect,
                "expectation_met": expectation_met,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            })
    report = {"schema": "kotoba.round46.s2.record-map-fixture-replay.v1",
              "started_at_utc": stamp(), "head": git("rev-parse", "HEAD"),
              "tree": git("rev-parse", "HEAD^{tree}"), "runs": result_rows,
              "all_inputs_unchanged": all(row["inputs_unchanged"] for row in result_rows),
              "all_expectations_met": all(row["expectation_met"] for row in result_rows),
              "fixture_head_pins": head_pins}
    out = EVIDENCE / "record-map-fixture-replay.json"
    write_json(out, report)
    return {"path": str(out.relative_to(ROOT)), "sha256": sha_file(out),
            "all_expectations_met": report["all_expectations_met"],
            "runs": [{"fixture": row["fixture"], "driver": row["driver"],
                      "exit": row["exit"], "headline": row["headline"],
                      "reason": row["reason"], "inputs_unchanged": row["inputs_unchanged"],
                      "expectation_met": row["expectation_met"],
                      "materialized_sha256": row["materialized_independent_sha256"]}
                     for row in result_rows]}


def run_g1():
    dump = R44 / "omp-live-18.12.2-strings.txt"
    probe_source = R44 / "g1/probe-call-shapes.py"
    baseline = ROOT / "verifiers/surfaces-baseline.json"
    committed_sha(dump)
    committed_sha(probe_source)
    committed_sha(baseline)
    current_worktree_verifier = ROOT / "verifiers/verify_surfaces.py"
    current_data = git("show", "HEAD:verifiers/verify_surfaces.py", binary=True)
    if sha_file(current_worktree_verifier) != digest(current_data):
        raise RuntimeError("worktree surfaces verifier differs from committed HEAD")
    historical_data = git("show", "6881ce3:verifiers/verify_surfaces.py", binary=True)
    historical_sha = digest(historical_data)
    current_sha = digest(current_data)
    if historical_sha != "e6b3e1bcdb4a1661c9f320b1488a477406722aad8417a0f90efe3077bf0ca223":
        raise RuntimeError(f"historical surfaces verifier pin mismatch: {historical_sha}")
    if current_sha != "9fa10d44848a9ff7e9d516125beafe501d62d3df7dbcb777dd13fef074d69657":
        raise RuntimeError(f"HEAD surfaces verifier pin mismatch: {current_sha}")
    verifier_paths = {}
    for label, data in (("verify-surfaces-6881ce3.py", historical_data),
                        ("verify-surfaces-head-055d3b9.py", current_data)):
        path = EVIDENCE / "g1" / label
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        verifier_paths[label] = path
    probe_sha = sha_file(probe_source)
    dump_sha = sha_file(dump)
    baseline_sha = sha_file(baseline)
    outputs = {}
    for label, verifier_path in verifier_paths.items():
        surfaces = load_module(verifier_path, "verify_surfaces")
        sys.modules["verify_surfaces"] = surfaces
        probe = load_module(probe_source, f"g1_probe_{label.replace('-', '_')}")
        probe.DUMP = dump
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            probe.main()
        text = capture.getvalue()
        outputs[label] = {"verifier_sha256": sha_file(verifier_path),
                          "probe_sha256": probe_sha,
                          "dump_sha256": dump_sha,
                          "baseline_sha256": baseline_sha,
                          "output_sha256": digest(text.encode("utf-8")),
                          "output": text}
    binary = Path("/home/vgpnk/.local/bin/omp")
    binary_before = sha_file(binary)
    version = subprocess.run([str(binary), "--version"], capture_output=True, text=True, timeout=30)
    stat = subprocess.run(["stat", "-c", "mtime=%y size=%s", str(binary)],
                          capture_output=True, text=True, check=True)
    strings_proc = subprocess.run(["strings", "-n", "4", str(binary)],
                                  capture_output=True, timeout=300)
    strings_sha = digest(strings_proc.stdout)
    strings_equal = strings_proc.returncode == 0 and strings_sha == dump_sha and strings_proc.stdout == dump.read_bytes()
    binary_after = sha_file(binary)
    gate = subprocess.run([sys.executable, "-B", "verifiers/verify_surfaces.py", "--json"],
                          cwd=ROOT, capture_output=True, text=True, timeout=300,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    self_test = subprocess.run([sys.executable, "-B", "verifiers/verify_surfaces.py", "--self-test"],
                               cwd=ROOT, capture_output=True, text=True, timeout=300,
                               env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    committed_sha(current_worktree_verifier)
    report = {
        "schema": "kotoba.round46.s2.g1-strings-census.v1",
        "measured_at_utc": stamp(),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "committed_dump": str(dump.relative_to(ROOT)),
        "committed_dump_sha256": dump_sha,
        "probe_source": str(probe_source.relative_to(ROOT)),
        "probe_source_sha256": probe_sha,
        "baseline_sha256": baseline_sha,
        "historical_verifier": {"ref": "6881ce3", "sha256": historical_sha},
        "head_verifier": {"ref": "HEAD", "sha256": current_sha},
        "probe_results": outputs,
        "binary": {"path": str(binary), "sha256_before": binary_before,
                   "sha256_after": binary_after, "version_exit": version.returncode,
                   "version_stdout": version.stdout.strip(), "stat": stat.stdout.strip(),
                   "strings_command": "strings -n 4 /home/vgpnk/.local/bin/omp",
                   "fresh_strings_exit": strings_proc.returncode,
                   "fresh_strings_bytes": len(strings_proc.stdout),
                   "fresh_strings_sha256": strings_sha,
                   "fresh_equals_committed_dump": strings_equal},
        "current_gate": {"command": "python3 -B verifiers/verify_surfaces.py --json",
                         "exit": gate.returncode, "stdout_sha256": digest(gate.stdout.encode()),
                         "stderr_sha256": digest(gate.stderr.encode()), "stdout": gate.stdout,
                         "stderr": gate.stderr},
        "current_self_test": {"command": "python3 -B verifiers/verify_surfaces.py --self-test",
                              "exit": self_test.returncode,
                              "stdout_sha256": digest(self_test.stdout.encode()),
                              "stderr_sha256": digest(self_test.stderr.encode()),
                              "stdout": self_test.stdout, "stderr": self_test.stderr},
    }
    out = EVIDENCE / "g1-strings-census.json"
    write_json(out, report)
    return {"path": str(out.relative_to(ROOT)), "sha256": sha_file(out),
            "committed_dump_sha256": dump_sha, "probe_source_sha256": probe_sha,
            "historical_probe_sha256": outputs["verify-surfaces-6881ce3.py"]["output_sha256"],
            "head_probe_sha256": outputs["verify-surfaces-head-055d3b9.py"]["output_sha256"],
            "binary_sha256": binary_before, "binary_stable": binary_before == binary_after,
            "fresh_strings_sha256": strings_sha, "fresh_equals_committed_dump": strings_equal,
            "gate_exit": gate.returncode, "self_test_exit": self_test.returncode}


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    temp_root = EVIDENCE / "tmp"
    temp_root.mkdir(exist_ok=True)
    os.environ["TMPDIR"] = str(temp_root)
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    started = stamp()
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    source_hashes = {
        ".ufo/round-41/evidence/probe-results.json": committed_sha(R41 / "probe-results.json"),
        ".ufo/round-41/evidence/v10-channel-census.json": committed_sha(R41 / "v10-channel-census.json"),
        ".ufo/round-41/evidence/v10-replay-probes.py": committed_sha(R41 / "v10-replay-probes.py"),
        ".ufo/round-41/evidence/v10-channel-census.py": committed_sha(R41 / "v10-channel-census.py"),
        ".ufo/round-41/evidence/compare-b1be35f.py": committed_sha(R41 / "compare-b1be35f.py"),
        ".ufo/round-40/evidence/union-battery.py": committed_sha(R40 / "union-battery.py"),
        ".ufo/round-44/evidence/g1/probe-call-shapes.py": committed_sha(R44 / "g1/probe-call-shapes.py"),
        ".ufo/round-44/evidence/omp-live-18.12.2-strings.txt": committed_sha(R44 / "omp-live-18.12.2-strings.txt"),
        "verifiers/surfaces-baseline.json": committed_sha(ROOT / "verifiers/surfaces-baseline.json"),
        "verifiers/compare_harness_independent.py (worktree)": sha_file(ROOT / COMPARATOR_REL),
        "verifiers/check_assertion_floors.py (worktree)": sha_file(ROOT / "verifiers/check_assertion_floors.py"),
    }
    expected_current_blob = git("rev-parse", f"HEAD:{COMPARATOR_REL}")
    source = json.loads((R41 / "probe-results.json").read_text(encoding="utf-8"))
    scope_data = git("show", f"{source['head']}:verifiers/harness-independent-scope.json", binary=True)
    if digest(scope_data) != source["scope_sha256"]:
        raise RuntimeError("R41 historical scope snapshot does not match the recorded source pin")
    scope_snapshot = EVIDENCE / "drivers" / "r41-scope-1c79e86.json"
    scope_snapshot.parent.mkdir(parents=True, exist_ok=True)
    scope_snapshot.write_bytes(scope_data)
    source_hashes["R41 committed scope snapshot"] = digest(scope_data)
    source_hashes["R41 scope worktree at start"] = sha_file(ROOT / "verifiers/harness-independent-scope.json")
    census_module = load_module(R41 / "v10-channel-census.py", "r41_v10_channel_census")
    drivers = {
        "r41-b1be35f": R41 / "compare-b1be35f.py",
        "r44-dispatch-6881ce3": frozen_comparator("6881ce3", "r44-dispatch-6881ce3"),
        "r45-landed-032f47b": frozen_comparator("032f47b", "r45-landed-032f47b"),
        "head-055d3b9": frozen_comparator("HEAD", "head-055d3b9"),
    }
    for label, driver in drivers.items():
        actual = sha_file(driver)
        if actual != EXPECTED_COMPARATORS[label]:
            raise RuntimeError(f"driver SHA mismatch for {label}: {actual}")
    if source["comparator_sha256"] != EXPECTED_COMPARATORS["r41-b1be35f"]:
        raise RuntimeError("saved R41 replay comparator pin differs from recorded source")
    census = replay_census(source, census_module, drivers, scope_snapshot)
    union_module = load_module(R40 / "union-battery.py", "r40_union_battery")
    union = run_union_c1_c2(union_module, {
        "r44-dispatch-6881ce3": drivers["r44-dispatch-6881ce3"],
        "r45-landed-032f47b": drivers["r45-landed-032f47b"],
        "head-055d3b9": drivers["head-055d3b9"],
    }, scope_snapshot)
    fixtures = run_record_map_fixtures({
        "r44-dispatch-6881ce3": drivers["r44-dispatch-6881ce3"],
        "r45-landed-032f47b": drivers["r45-landed-032f47b"],
        "head-055d3b9": drivers["head-055d3b9"],
    })
    g1 = run_g1()
    summary = {
        "schema": "kotoba.round46.s2.evidence-verification.v1",
        "started_at_utc": started,
        "finished_at_utc": stamp(),
        "head": head,
        "tree": tree,
        "head_comparator_blob": expected_current_blob,
        "head_comparator_sha256": EXPECTED_COMPARATORS["head-055d3b9"],
        "source_hashes_at_start": source_hashes,
        "r41_exact_saved_payload_replays": census,
        "r40_union_safe_subset": union,
        "r44_record_map_fixture_replay": fixtures,
        "r44_g1_strings_census": g1,
        "worktree_comparator_sha256_at_end": sha_file(ROOT / COMPARATOR_REL),
        "worktree_floors_guard_sha256_at_end": sha_file(ROOT / "verifiers/check_assertion_floors.py"),
        "head_at_end": git("rev-parse", "HEAD"),
        "tree_at_end": git("rev-parse", "HEAD^{tree}"),
        "status_at_end": git("status", "--short"),
    }
    write_json(EVIDENCE / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
