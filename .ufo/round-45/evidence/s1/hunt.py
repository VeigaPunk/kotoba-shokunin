import concurrent.futures
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
INPUTS = DRAFT / "inputs"
RECEIPTS = DRAFT / "receipts"
COMPARATOR_REL = "verifiers/compare_harness_independent.py"
BASE_REF = "6881ce3"
LANDED_REF = "032f47b"
BASE_SHA = "d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d"
LANDED_SHA = "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56"
TARGET = "omp.offered.skills"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return digest(Path(path).read_bytes())


def git_text(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout.strip()


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_output(proc):
    try:
        parsed = json.loads(proc.stdout)
    except (TypeError, ValueError):
        parsed = None
    return {
        "exit": proc.returncode,
        "headline": parsed.get("headline") if isinstance(parsed, dict) else None,
        "agreement": parsed.get("agreement") if isinstance(parsed, dict) else None,
        "reason": ((parsed.get("reason") if isinstance(parsed, dict) else None)
                   or proc.stderr.strip()[-1200:] or proc.stdout.strip()[-1200:]),
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "stdout_sha256": digest(proc.stdout.encode("utf-8")),
        "stderr_sha256": digest(proc.stderr.encode("utf-8")),
    }


def run(argv, cwd, timeout=120):
    started = stamp()
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    ended = stamp()
    result = parse_output(proc)
    result["started_at_utc"] = started
    result["ended_at_utc"] = ended
    result["argv"] = [str(value) for value in argv]
    result["process_cwd"] = str(cwd)
    return result


def make_comparator(ref, name, expected_sha):
    data = subprocess.run(["git", "show", f"{ref}:{COMPARATOR_REL}"], cwd=ROOT,
                          check=True, capture_output=True).stdout
    actual_sha = digest(data)
    if actual_sha != expected_sha:
        raise RuntimeError(f"{ref} comparator SHA mismatch: {actual_sha}")
    path = DRAFT / "comparators" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def command_input_hashes(argv, cwd):
    output = {}
    for flag in ("--live-json", "--independent-json", "--scope-file"):
        if flag in argv:
            value = Path(argv[argv.index(flag) + 1])
            path = (value if value.is_absolute() else Path(cwd) / value).resolve()
            output[flag[2:].replace("-", "_")] = {"path": str(path), "sha256": file_sha(path)}
    return output


def run_saved_arm(arm_id, expected, driver):
    argv = list(expected["command"])
    argv[1] = str(driver)
    if "--receipt" in argv:
        receipt = RECEIPTS / f"r41-{arm_id}.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        argv[argv.index("--receipt") + 1] = str(receipt)
    cwd = Path(expected["process_cwd"])
    hashes_before = command_input_hashes(argv, cwd)
    result = run(argv, cwd)
    hashes_after = command_input_hashes(argv, cwd)
    result.update({
        "arm_id": arm_id,
        "baseline_classification": expected.get("classification"),
        "expected_exit_frozen_r41": expected["exit"],
        "input_hashes_before": hashes_before,
        "input_hashes_after": hashes_after,
        "input_hashes_unchanged": hashes_before == hashes_after,
    })
    return result


def encode_object_pairs(pairs):
    return "{" + ",".join(json.dumps(key, ensure_ascii=False) + ":" + value
                         for key, value in pairs) + "}"


def encode_duplicate_record(payload, target):
    root_pairs = []
    for key, value in payload.items():
        if key != "results":
            root_pairs.append((key, json.dumps(value, ensure_ascii=False, separators=(",", ":"))))
            continue
        records = []
        for record in value:
            if record.get("check") != target or "re_derived" not in record:
                records.append(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
                continue
            record_pairs = []
            for field, field_value in record.items():
                if field == "re_derived":
                    record_pairs.append((field, json.dumps(999999)))
                record_pairs.append((field, json.dumps(field_value, ensure_ascii=False,
                                                        separators=(",", ":"))))
            records.append(encode_object_pairs(record_pairs))
        root_pairs.append((key, "[" + ",".join(records) + "]"))
    return encode_object_pairs(root_pairs)


def arm_record_json(payload, target, output):
    divergent = copy.deepcopy(payload["results"])
    for record in divergent:
        if record.get("check") == target:
            for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                if key in record:
                    record[key] = 999999
            record.setdefault("re_derived", 999999)
    pairs = [("results", json.dumps(divergent, ensure_ascii=False, separators=(",", ":")))]
    for key, value in payload.items():
        pairs.append((key, json.dumps(value, ensure_ascii=False, separators=(",", ":"))))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(encode_object_pairs(pairs) + "\n", encoding="utf-8")


def arm_nested_extensions(payload, target):
    changed = copy.deepcopy(payload)
    changed["extensions"] = {
        "diagnostics": {
            "payload": {
                "channels": {
                    "results": [{"check": target, "expected": 999999, "re_derived": 999999}],
                    "rows": [{"check": target, "expected": 999999, "re_derived": 999999}],
                    "checks": {target: 999999},
                }
            }
        }
    }
    return changed


def arm_expected_alias(payload, live_values):
    changed = copy.deepcopy(payload)
    for channel in ("results", "rows"):
        for record in changed.get(channel, []):
            if record.get("check") == TARGET:
                record["expected"] = live_values[TARGET]
                record["expected_value"] = 999999
    return changed


def arm_status(payload, value, with_state=False):
    changed = copy.deepcopy(payload)
    for channel in ("results", "rows"):
        for record in changed.get(channel, []):
            if record.get("check") == TARGET:
                record["status"] = value
                if with_state:
                    record["state"] = "UNLANDED"
    return changed


def arm_nonstring_id_alias(payload):
    changed = copy.deepcopy(payload)
    for channel in ("results", "rows"):
        for record in changed.get(channel, []):
            if record.get("check") == TARGET:
                record["check"] = []
                record["name"] = TARGET
    return changed


def arm_extra_null_map(payload):
    changed = copy.deepcopy(payload)
    changed.setdefault("checks", {})["r45.attacker.extra"] = None
    return changed


def arm_null_scope_row(payload, planted_payload):
    changed = copy.deepcopy(payload)
    probe = next(record["probe"] for record in planted_payload["results"]
                 if record.get("check") == TARGET)
    for channel in ("results", "rows"):
        for record in changed.get(channel, []):
            if record.get("check") == TARGET:
                record["status"] = "SCOPED_OUT"
                record["evidence"] = "probe-only author rule"
                record["probe"] = copy.deepcopy(probe)
                for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                    if key in record:
                        record[key] = None
    changed.setdefault("checks", {})[TARGET] = None
    changed.setdefault("scoped_out", {})[TARGET] = "probe-only author rule"
    changed.setdefault("scoped_out_probes", {})[TARGET] = copy.deepcopy(probe)
    return changed


def arm_summary_only(payload):
    changed = copy.deepcopy(payload)
    changed["landed"] = 0
    changed["unlanded"] = [TARGET]
    changed["alternatives"] = {TARGET: {"value": 999999, "why": "fabricated summary"}}
    return changed


def cli_args(driver, live_path, independent_path, scope_path, expect_n=28):
    return [sys.executable, str(driver), "--live-json", str(live_path),
            "--independent-json", str(independent_path), "--expect-n", str(expect_n),
            "--cwd", str(ROOT), "--scope-file", str(scope_path), "--no-stamp", "--json"]


def run_fresh_arm(name, path, description, driver_name, driver, live_path,
                  scope_path, expected_n=28):
    argv = cli_args(driver, live_path, path, scope_path, expected_n)
    result = run(argv, ROOT)
    result.update({
        "case": name,
        "description": description,
        "comparator": driver_name,
        "comparator_sha256": file_sha(driver),
        "independent_input": str(path),
        "independent_sha256": file_sha(path),
        "live_input": str(live_path),
        "live_sha256": file_sha(live_path),
        "scope_input": str(scope_path),
        "scope_sha256": file_sha(scope_path),
    })
    return result


def run_scope_case(name, driver_name, driver, live_path, independent_path,
                   scope_arg, process_cwd):
    argv = [sys.executable, str(driver), "--live-json", str(live_path),
            "--independent-json", str(independent_path), "--expect-n", "28",
            "--cwd", str(ROOT), "--scope-file", str(scope_arg), "--no-stamp", "--json"]
    cwd = Path(process_cwd)
    result = run(argv, cwd)
    scope_path = Path(scope_arg)
    scope_path = (scope_path if scope_path.is_absolute() else cwd / scope_path).resolve()
    result.update({
        "case": name,
        "comparator": driver_name,
        "comparator_sha256": file_sha(driver),
        "live_sha256": file_sha(live_path),
        "independent_sha256": file_sha(independent_path),
        "scope_argument": str(scope_arg),
        "resolved_scope_path": str(scope_path),
        "scope_sha256": file_sha(scope_path),
    })
    return result


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    INPUTS.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    start = {
        "timestamp_utc": stamp(),
        "head": git_text("rev-parse", "HEAD"),
        "tree": git_text("rev-parse", "HEAD^{tree}"),
        "status": git_text("status", "--short"),
        "worktree_comparator_sha256": file_sha(ROOT / COMPARATOR_REL),
        "scope_sha256": file_sha(ROOT / "verifiers/harness-independent-scope.json"),
    }
    base = make_comparator(BASE_REF, "compare-6881ce3.py", BASE_SHA)
    landed = make_comparator(LANDED_REF, "compare-032f47b.py", LANDED_SHA)
    if file_sha(landed) != LANDED_SHA:
        raise RuntimeError("the git-show landed comparator does not match the requested 13b6d791 source")

    source_path = ROOT / ".ufo/round-41/evidence/probe-results.json"
    old_census_path = ROOT / ".ufo/round-41/evidence/v10-channel-census.json"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    old_census = json.loads(old_census_path.read_text(encoding="utf-8"))
    if len(source["arms"]) != 46 or old_census["summary"]["arm_count"] != 46:
        raise RuntimeError("the saved R41 census inputs do not contain exactly 46 arms")
    classes = {arm["id"]: arm["classification"] for arm in old_census["arms"]}
    if set(classes) != set(source["arms"]):
        raise RuntimeError("R41 replay and channel census arm ID sets differ")
    saved_arms = {}
    for arm_id, record in source["arms"].items():
        expected = dict(record)
        expected["classification"] = classes[arm_id]
        saved_arms[arm_id] = expected
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        replay = list(pool.map(lambda item: run_saved_arm(item[0], item[1], landed),
                               sorted(saved_arms.items())))
    replay.sort(key=lambda item: item["arm_id"])
    replay_counts = {}
    for item in replay:
        label = str(item["exit"])
        replay_counts[label] = replay_counts.get(label, 0) + 1
    still_open = [item["arm_id"] for item in replay
                  if item["baseline_classification"] == "open" and item["exit"] == 0]
    closed_open = [item["arm_id"] for item in replay
                   if item["baseline_classification"] == "open" and item["exit"] != 0]
    newly_green = [item["arm_id"] for item in replay
                   if item["baseline_classification"] in ("closed", "diagnostic")
                   and item["exit"] == 0]
    controls_green = [item["arm_id"] for item in replay
                      if item["baseline_classification"] == "control" and item["exit"] == 0]
    trust_input_green = [item["arm_id"] for item in replay
                         if item["baseline_classification"] == "trust-input" and item["exit"] == 0]
    replay_report = {
        "generated_at_utc": stamp(),
        "command_basis": "python3 .ufo/round-41/evidence/v10-replay-probes.py inputs replayed as subprocesses with only argv[1] replaced by git-show 032f47b comparator; per-arm saved process cwd and all input args preserved; --receipt redirected under this draft",
        "root": str(ROOT),
        "head_at_start": start["head"],
        "tree_at_start": start["tree"],
        "head_at_end": git_text("rev-parse", "HEAD"),
        "tree_at_end": git_text("rev-parse", "HEAD^{tree}"),
        "comparator_target": {
            "ref": LANDED_REF,
            "source_sha256": file_sha(landed),
            "worktree_sha256_start": start["worktree_comparator_sha256"],
            "worktree_sha256_end": file_sha(ROOT / COMPARATOR_REL),
        },
        "frozen_baseline": {"ref": BASE_REF, "source_sha256": file_sha(base)},
        "scope_sha256": start["scope_sha256"],
        "r41_replay_source": {"path": str(source_path.relative_to(ROOT)),
                               "sha256": file_sha(source_path),
                               "frozen_comparator_sha256": source["comparator_sha256"]},
        "r41_static_census": {"path": str(old_census_path.relative_to(ROOT)),
                               "sha256": file_sha(old_census_path),
                               "original_classification_counts": old_census["summary"]["classification_counts"]},
        "summary": {
            "arm_count": len(replay),
            "actual_exit_counts": replay_counts,
            "original_open_count": old_census["summary"]["classification_counts"]["open"],
            "still_green_originally_open": len(still_open),
            "formerly_open_now_nonzero": len(closed_open),
            "originally_closed_or_diagnostic_now_green": len(newly_green),
            "control_arms_exit0": len(controls_green),
            "trust_input_arms_exit0": len(trust_input_green),
            "all_input_hashes_unchanged": all(item["input_hashes_unchanged"] for item in replay),
            "all_arm_ids_unique": len({item["arm_id"] for item in replay}) == 46,
        },
        "still_open_original_arms": still_open,
        "formerly_open_now_nonzero": closed_open,
        "originally_closed_or_diagnostic_now_green": newly_green,
        "control_arms_exit0": controls_green,
        "trust_input_arms_exit0": trust_input_green,
        "arms": replay,
    }
    write_json(DRAFT / "census-current-replay.json", replay_report)

    live_path = INPUTS / "live-current.json"
    independent_path = INPUTS / "independent-current.json"
    live_proc = subprocess.run([sys.executable, str(ROOT / "verifiers/verify_harness_claims.py"), "--json"],
                               cwd=ROOT, capture_output=True, text=True, timeout=300)
    independent_proc = subprocess.run([sys.executable, str(ROOT / "verifiers/verify_harness_independent.py"), "--json"],
                                     cwd=ROOT, capture_output=True, text=True, timeout=300)
    live_path.write_text(live_proc.stdout, encoding="utf-8")
    independent_path.write_text(independent_proc.stdout, encoding="utf-8")
    if live_proc.returncode or independent_proc.returncode:
        raise RuntimeError(f"fresh producer capture failed: live={live_proc.returncode} independent={independent_proc.returncode}")
    live = json.loads(live_path.read_text(encoding="utf-8"))
    independent = json.loads(independent_path.read_text(encoding="utf-8"))
    live_values = {record["check"]: record["observed"] for record in live["results"]}
    if TARGET not in live_values:
        raise RuntimeError(f"fresh live capture lacks {TARGET}")
    scope_path = ROOT / "verifiers/harness-independent-scope.json"
    planted_scope_arm = json.loads(
        (ROOT / ".ufo/round-41/evidence/arm-r1-f3-prime-scope-file-cwd.json")
        .read_text(encoding="utf-8"))
    null_scope_payload = arm_null_scope_row(independent, planted_scope_arm)
    null_scope_input = INPUTS / "relative-scope-null-isolation.json"
    write_json(null_scope_input, null_scope_payload)
    planted_cwd = ROOT / ".ufo/round-41/evidence/planted-cwd"
    planted_scope_path = planted_cwd / "verifiers/harness-independent-scope.json"
    cases = {}

    def add(name, payload, description, paired=True):
        path = INPUTS / f"{name}.json"
        if isinstance(payload, str):
            path.write_text(payload, encoding="utf-8")
        else:
            write_json(path, payload)
        cases[name] = {"path": path, "description": description, "paired": paired}

    add("expected-expected_value-conflict", arm_expected_alias(independent, live_values),
        "same record carries expected equal to live and a conflicting expected_value", True)
    add("lone-nonstring-status", arm_status(independent, ["UNLANDED"]),
        "single non-string status with no state field", True)
    add("nonstring-status-state-conflict", arm_status(independent, ["UNLANDED"], True),
        "non-string status plus contradictory state=UNLANDED", True)
    add("extra-null-map-key", arm_extra_null_map(independent),
        "record channels plus a null-valued checks key absent from records and committed scope", True)
    add("coherent-record-map-null-scopeouts", independent,
        "fresh producer record/map control with committed scope-out nulls", True)
    add("check_id-ignored", {
        **copy.deepcopy(independent),
    }, "unknown check_id field control; record-level mutation added below", True)
    check_id_path = cases["check_id-ignored"]["path"]
    check_id_payload = copy.deepcopy(independent)
    for channel in ("results", "rows"):
        for record in check_id_payload.get(channel, []):
            if record.get("check") == TARGET:
                record["check_id"] = "rogue.check_id.alias"
    write_json(check_id_path, check_id_payload)
    add("top-level-summary-only", arm_summary_only(independent),
        "contradictory landed/unlanded/alternatives summaries without uncontracted fields", True)
    add("nonstring-check-name-alias", arm_nonstring_id_alias(independent),
        "non-string check field is ignored in favor of the matching name alias", True)
    add("nested-extension-shadow", arm_nested_extensions(independent, TARGET),
        "conflicting channel-shaped fields under unknown extensions subtree", True)
    add("top-level-duplicate-results", "", "duplicate top-level results member: divergent first, honest last", True)
    arm_record_json(independent, TARGET, cases["top-level-duplicate-results"]["path"])
    duplicate_record = INPUTS / "duplicate-record-rederived.json"
    duplicate_record.write_text(encode_duplicate_record(independent, TARGET) + "\n", encoding="utf-8")
    cases["duplicate-record-rederived"] = {
        "path": duplicate_record,
        "description": "duplicate results-record re_derived member: conflicting first, honest last",
        "paired": True,
    }
    live_nested = arm_nested_extensions(live, TARGET)
    live_nested_path = INPUTS / "live-nested-extension-shadow.json"
    write_json(live_nested_path, live_nested)
    cases["live-nested-extension-shadow"] = {
        "path": independent_path,
        "description": "live payload has nested extensions shadow; independent input remains honest",
        "paired": False,
        "live_path": live_nested_path,
    }

    fixture_root = ROOT / "verifiers/fixtures/compare-harness-independent"
    fixture_cases = []
    for fixture_name in ("record-map-24-control", "record-map-24-composition"):
        folder = fixture_root / fixture_name
        case = json.loads((folder / "case.json").read_text(encoding="utf-8"))
        live_fixture = (folder / case["live"]).resolve()
        scope_fixture = (folder / case["scope"]).resolve()
        carrier_fixture = (folder / case["probe_carrier"]).resolve()
        ind_source = (folder / case["independent"]).read_text(encoding="utf-8")
        materialized = ind_source.replace("@fixture:carrier@", str(carrier_fixture))
        if "@fixture:carrier@" in materialized:
            raise RuntimeError(f"unmaterialized fixture marker in {fixture_name}")
        ind_fixture = INPUTS / f"{fixture_name}-independent.json"
        ind_fixture.write_text(materialized, encoding="utf-8")
        fixture_cases.append({
            "name": fixture_name,
            "live_path": live_fixture,
            "independent_path": ind_fixture,
            "scope_path": scope_fixture,
            "case_sha256": file_sha(folder / "case.json"),
            "fixture_independent_sha256": file_sha(folder / case["independent"]),
            "materialized_independent_sha256": file_sha(ind_fixture),
            "paired": True,
        })

    expected_only_source = source["arms"]["heldout-expected-only-full-copy"]
    expected_only_diff = run_saved_arm("heldout-expected-only-full-copy", expected_only_source, base)
    expected_only_diff["comparator"] = "6881ce3 frozen baseline"
    expected_only_diff_after = run_saved_arm("heldout-expected-only-full-copy", expected_only_source, landed)
    expected_only_diff_after["comparator"] = "032f47b landed comparator"
    scope_differentials = {}
    for arm_id in ("r1-f3-prime-scope-file-cwd", "scope-file-caller-selected-absolute"):
        before = run_saved_arm(arm_id, source["arms"][arm_id], base)
        after = run_saved_arm(arm_id, source["arms"][arm_id], landed)
        scope_differentials[arm_id] = {"before_6881ce3": before, "after_032f47b": after}
    scope_isolation = []
    for driver_name, driver in (("6881ce3", base), ("032f47b", landed)):
        scope_isolation.append(run_scope_case(
            "relative-scope-null-isolation", driver_name, driver, live_path,
            null_scope_input, "verifiers/harness-independent-scope.json", planted_cwd))
        scope_isolation.append(run_scope_case(
            "absolute-scope-null-isolation", driver_name, driver, live_path,
            null_scope_input, planted_scope_path, ROOT))
        scope_isolation.append(run_scope_case(
            "relative-scope-null-honest-cwd-control", driver_name, driver,
            live_path, null_scope_input, "verifiers/harness-independent-scope.json", ROOT))

    fresh_work = []
    drivers = [("6881ce3", base), ("032f47b", landed)]
    for case_name, case in sorted(cases.items()):
        for driver_name, driver in (drivers if case["paired"] else [("032f47b", landed)]):
            live_arg = case.get("live_path", live_path)
            fresh_work.append((case_name, case, driver_name, driver, live_arg, scope_path))
    for fixture in fixture_cases:
        for driver_name, driver in drivers:
            fresh_work.append((fixture["name"], fixture, driver_name, driver,
                               fixture["live_path"], fixture["scope_path"]))
    def execute_fresh(item):
        name, case, driver_name, driver, live_arg, scope_arg = item
        path = case.get("path", case.get("independent_path"))
        return run_fresh_arm(name, path, case.get("description", name), driver_name,
                             driver, live_arg, scope_arg)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        fresh_results = list(pool.map(execute_fresh, fresh_work))
    fresh_results.sort(key=lambda item: (item["case"], item["comparator"]))

    outputs = {}
    for proc_name, proc in (("live", live_proc), ("independent", independent_proc)):
        outputs[proc_name] = {"exit": proc.returncode,
                              "stdout_sha256": digest(proc.stdout.encode("utf-8")),
                              "stderr": proc.stderr[-1200:]}
    fresh_report = {
        "generated_at_utc": stamp(),
        "command_basis": "fresh verify_harness_claims.py --json and verify_harness_independent.py --json captures; each arm invoked with python3 <frozen comparator> --live-json ... --independent-json ... --expect-n 28 --cwd <repo> --scope-file <scope> --no-stamp --json",
        "head_at_start": start["head"],
        "tree_at_start": start["tree"],
        "head_at_end": git_text("rev-parse", "HEAD"),
        "tree_at_end": git_text("rev-parse", "HEAD^{tree}"),
        "worktree_comparator_sha256_start": start["worktree_comparator_sha256"],
        "worktree_comparator_sha256_end": file_sha(ROOT / COMPARATOR_REL),
        "frozen_comparators": {"6881ce3": file_sha(base), "032f47b": file_sha(landed)},
        "scope_sha256": file_sha(scope_path),
        "fresh_capture": {
            "live": {**outputs["live"], "path": str(live_path.relative_to(ROOT)),
                     "sha256": file_sha(live_path)},
            "independent": {**outputs["independent"], "path": str(independent_path.relative_to(ROOT)),
                            "sha256": file_sha(independent_path)},
            "live_instrument_sha256": file_sha(ROOT / "verifiers/verify_harness_claims.py"),
            "independent_instrument_sha256": file_sha(ROOT / "verifiers/verify_harness_independent.py"),
        },
        "r41_expected_only_differential": {
            "input_sha256": expected_only_source["independent_payload_sha256"],
            "before": expected_only_diff,
            "after": expected_only_diff_after,
        },
        "r41_scope_differentials": scope_differentials,
        "null_value_scope_isolation": {
            "input_path": str(null_scope_input.relative_to(ROOT)),
            "input_sha256": file_sha(null_scope_input),
            "planted_scope_sha256": file_sha(planted_scope_path),
            "runs": scope_isolation,
        },
        "fixture_differentials": [
            {key: str(value) if isinstance(value, Path) else value
             for key, value in fixture.items()}
            for fixture in fixture_cases
        ],
        "summary": {
            "fresh_case_count": len(cases) + len(fixture_cases),
            "subprocess_count": len(fresh_results) + 2,
            "differential_case_count": len([x for x in fresh_results if x["comparator"] == "6881ce3"]),
            "all_invoked": len(fresh_results) == len(fresh_work),
        },
        "results": fresh_results,
    }
    write_json(DRAFT / "fresh-channel-hunt.json", fresh_report)

    final = {
        "timestamp_utc": stamp(),
        "head": git_text("rev-parse", "HEAD"),
        "tree": git_text("rev-parse", "HEAD^{tree}"),
        "status": git_text("status", "--short"),
        "worktree_comparator_sha256": file_sha(ROOT / COMPARATOR_REL),
        "scope_sha256": file_sha(scope_path),
    }
    summary = {
        "replay_output": str((DRAFT / "census-current-replay.json").relative_to(ROOT)),
        "replay_output_sha256": file_sha(DRAFT / "census-current-replay.json"),
        "fresh_output": str((DRAFT / "fresh-channel-hunt.json").relative_to(ROOT)),
        "fresh_output_sha256": file_sha(DRAFT / "fresh-channel-hunt.json"),
        "start": start,
        "final": final,
        "r41_open_count": len(still_open),
        "r41_closed_from_open_count": len(closed_open),
        "r41_unexpected_green_count": len(newly_green),
        "r41_exit_counts": replay_counts,
        "r41_still_open_ids": still_open,
        "fresh_cases": len(cases) + len(fixture_cases),
        "fresh_runs": len(fresh_results) + 2,
        "scope_isolation_runs": len(scope_isolation),
    }
    write_json(DRAFT / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
