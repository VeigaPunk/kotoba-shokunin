#!/usr/bin/env python3
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import types
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
R41_SOURCE = ROOT / ".ufo/round-41/evidence/probe-results.json"
R41_CLASSIFIER = ROOT / ".ufo/round-41/evidence/v10-channel-census.py"
R41_GENERATOR = ROOT / ".ufo/round-41/evidence/v10-census-probes.py"
R45_FRESH_RUNNER = ROOT / ".ufo/round-45/evidence/c2/fresh_hunts.py"
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
LIVE = ROOT / "verifiers/verify_harness_claims.py"
INDEPENDENT = ROOT / "verifiers/verify_harness_independent.py"
HEAD_SCOPE_ROOT = DRAFT / "head-scope-root"
SCOPE = HEAD_SCOPE_ROOT / "verifiers/harness-independent-scope.json"
EXPECTED_HEAD = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
EXPECTED_TREE = "e8dced184612a9738c5b8d244a0837fbd955a7da"
EXPECTED_DRIVER_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
EXPECTED_SCOPE_SHA = "fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a"
LIVE_CAPTURE = DRAFT / "fresh-live.json"
IND_CAPTURE = DRAFT / "fresh-independent.json"
OUTPUT = DRAFT / "v2-results-head-scope.json"
RECEIPT = DRAFT / "r41-fresh-receipt.json"
CARRIER = DRAFT / "probe-carrier"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def duplicate_members(raw):
    duplicates = Counter()

    def collect(pairs):
        counts = Counter(key for key, _value in pairs)
        duplicates.update({key: count - 1 for key, count in counts.items() if count > 1})
        return dict(pairs)

    json.loads(raw.decode("utf-8"), object_pairs_hook=collect)
    return dict(sorted(duplicates.items()))


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def produce(path, head, *args):
    relative = path.relative_to(ROOT).as_posix()
    source = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{head}:{relative}"],
        check=True, capture_output=True).stdout
    wrapper = (
        "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
        "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
        "{'__name__':'__main__','__file__':p})"
    )
    command = [sys.executable, "-B", "-c", wrapper, str(path), *args]
    start = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(command, cwd=ROOT, input=source.decode("utf-8"),
                          capture_output=True, text=True, timeout=300)
    end = datetime.now(timezone.utc).isoformat()
    if proc.returncode != 0:
        raise RuntimeError(f"producer failed ({path.name}): {proc.returncode}: {proc.stderr[-800:]}")
    raw = proc.stdout.encode("utf-8")
    return raw, {"command": command, "started_at_utc": start,
                 "finished_at_utc": end, "exit": proc.returncode,
                 "source_sha256_from_git_show_head": sha_bytes(source),
                 "sha256": sha_bytes(raw)}


def frozen_module(source):
    module = types.ModuleType("v2_frozen_comparator")
    module.__file__ = str(DRIVER)
    exec(compile(source.decode("utf-8"), str(DRIVER), "exec"), module.__dict__)
    return module


def run_snapshot(source, args, cwd):
    wrapper = (
        "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
        "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
        "{'__name__':'__main__','__file__':p})"
    )
    command = [sys.executable, "-c", wrapper, str(DRIVER), *args]
    proc = subprocess.run(command, cwd=cwd, input=source.decode("utf-8"),
                          capture_output=True, text=True, timeout=300)
    try:
        data = json.loads(proc.stdout)
        reason, headline = data.get("reason", ""), data.get("headline")
    except (ValueError, TypeError):
        data = None
        reason, headline = (proc.stderr or proc.stdout).strip()[-1200:], None
    return command, proc, data, reason, headline


def prepare_carrier():
    CARRIER.mkdir(parents=True, exist_ok=True)
    for name, stamp, entries, mtime in (
        ("a.jsonl", "2026-01-01T00:00:00.000Z", 2, 1700000000),
        ("b.jsonl", "2026-02-02T00:00:00.000Z", 5, 1700001000),
    ):
        rows = "\\n".join(f"- entry {i}" for i in range(entries))
        path = CARRIER / name
        path.write_text(
            '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' % (stamp, rows),
            encoding="utf-8")
        os.utime(path, (mtime, mtime))


def run_generated_arm(source, live, name, case, index):
    live_path = LIVE_CAPTURE
    if case.get("live_payload") is not None:
        live_path = DRAFT / f"live-arm-{name}.json"
        live_path.write_text(json.dumps(case["live_payload"], indent=1,
                                        sort_keys=True) + "\n", encoding="utf-8")
    ind_path = DRAFT / f"arm-{name}.json"
    ind_path.write_text(json.dumps(case["payload"], indent=1,
                                   sort_keys=True) + "\n", encoding="utf-8")
    scope = case["scope"] or str(SCOPE)
    cwd = case["process_cwd"] or HEAD_SCOPE_ROOT
    args = ["--live-json", str(live_path), "--independent-json", str(ind_path),
            "--cwd", str(HEAD_SCOPE_ROOT), "--scope-file", str(scope), "--expect-n", "28",
            "--no-stamp", "--json"]
    if case["receipt"]:
        args += ["--receipt", str(case["receipt"])]
    scope_path = Path(scope)
    if not scope_path.is_absolute():
        scope_path = cwd / scope_path
    tracked = {"live": live_path, "independent": ind_path, "scope": scope_path}
    if case["receipt"]:
        tracked["receipt"] = Path(case["receipt"])
    before = {key: sha_file(path) for key, path in tracked.items() if path.is_file()}
    command, proc, data, reason, headline = run_snapshot(source, args, cwd)
    after = {key: sha_file(path) for key, path in tracked.items() if path.is_file()}
    expected_class = index.CASES[name][0]
    if expected_class == "open":
        classification = "open" if proc.returncode == 0 else "closed"
    elif expected_class == "closed":
        classification = "unexpected-open" if proc.returncode == 0 else "closed"
    elif expected_class == "diagnostic":
        classification = "diagnostic" if proc.returncode != 0 else "accepted-diagnostic"
    elif expected_class == "trust-input":
        classification = "trust-input"
    else:
        classification = "control"
    return {
        "id": name,
        "baseline_classification": expected_class,
        "landed_classification": classification,
        "channel": index.CASES[name][1],
        "finding": index.CASES[name][2],
        "process_cwd": str(cwd),
        "command": command,
        "input_paths": {key: str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
                        for key, path in tracked.items()},
        "input_sha256_before": before,
        "input_sha256_after": after,
        "inputs_unchanged": before == after,
        "exit": proc.returncode,
        "headline": headline,
        "reason": reason,
        "stdout_sha256": sha_bytes(proc.stdout.encode("utf-8")),
        "stderr_sha256": sha_bytes(proc.stderr.encode("utf-8")),
        "stderr_tail": proc.stderr[-500:],
    }


def run_fresh_c2_arm(source, live_path, path, name, raw):
    duplicate_names = duplicate_members(raw)
    expected_duplicate = {
        "duplicate_top_level_results_member": {"results": 1},
        "duplicate_record_rederived_member": {"re_derived": 1},
    }.get(name)
    if expected_duplicate is not None and duplicate_names != expected_duplicate:
        raise RuntimeError(f"{name} raw duplicate members differ: {duplicate_names}")
    path.write_bytes(raw)
    args = ["--live-json", str(live_path), "--independent-json", str(path),
            "--cwd", str(HEAD_SCOPE_ROOT), "--scope-file", str(SCOPE), "--expect-n", "28",
            "--no-stamp", "--json"]
    before = {"live": sha_file(live_path), "independent": sha_file(path),
              "scope": sha_file(SCOPE)}
    command, proc, data, reason, headline = run_snapshot(source, args, HEAD_SCOPE_ROOT)
    after = {"live": sha_file(live_path), "independent": sha_file(path),
             "scope": sha_file(SCOPE)}
    duplicate_outcome = None
    if expected_duplicate is not None:
        duplicate_outcome = (
            "class-named" if proc.returncode == 2 and "duplicate json member" in reason.lower()
            else "accepted-last-member-wins" if proc.returncode == 0
            else "nonzero-without-duplicate-class")
    return {
        "id": name,
        "input_path": str(path.relative_to(ROOT)),
        "raw_duplicate_members": duplicate_names,
        "duplicate_outcome": duplicate_outcome,
        "input_sha256_before": before,
        "input_sha256_after": after,
        "inputs_unchanged": before == after,
        "command": command,
        "exit": proc.returncode,
        "reason": reason,
        "headline": headline,
        "stdout_sha256": sha_bytes(proc.stdout.encode("utf-8")),
        "stderr_sha256": sha_bytes(proc.stderr.encode("utf-8")),
    }


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    measured_start = datetime.now(timezone.utc).isoformat()
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    source = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{head}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    scope_source = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{head}:verifiers/harness-independent-scope.json"],
        check=True, capture_output=True).stdout
    driver_sha = sha_bytes(source)
    scope_sha = sha_bytes(scope_source)
    worktree_driver_start = sha_file(DRIVER)
    if (head, tree, driver_sha) != (EXPECTED_HEAD, EXPECTED_TREE, EXPECTED_DRIVER_SHA):
        raise RuntimeError(f"landed target changed: {head} {tree} {driver_sha}")
    if scope_sha != EXPECTED_SCOPE_SHA:
        raise RuntimeError(f"landed scope changed: {scope_sha}")

    HEAD_SCOPE_ROOT.mkdir(parents=True, exist_ok=True)
    SCOPE.parent.mkdir(parents=True, exist_ok=True)
    SCOPE.write_bytes(scope_source)
    live_raw, live_meta = produce(LIVE, head, "--json")
    ind_raw, ind_meta = produce(INDEPENDENT, head, "--json")
    LIVE_CAPTURE.write_bytes(live_raw)
    IND_CAPTURE.write_bytes(ind_raw)
    live, independent = json.loads(live_raw), json.loads(ind_raw)
    driver = frozen_module(source)
    classifier = load_module("v10_channel_census", R41_CLASSIFIER)
    generator = load_module("v10_census_probes", R41_GENERATOR)
    generator.CASES = classifier.CASES
    generator.DRAFT = DRAFT
    generator.DRIVER = DRIVER
    generator.LIVE_FILE = LIVE_CAPTURE
    generator.IND_FILE = IND_CAPTURE
    generator.CARRIER = CARRIER
    generator.ROOT = ROOT
    generator.SCOPE_REL = "verifiers/harness-independent-scope.json"
    generator.TARGET_ID = "omp.offered.skills"
    prepare_carrier()

    raw_scope = independent.get("scoped_out_probes", {})
    probe_preflight = []
    for cid, probe in raw_scope.items():
        recomputed = driver.recompute_probe(probe)
        probe_preflight.append({"check": cid,
                                "target": probe.get("target"),
                                "declared_matches_now": probe.get("observable") == recomputed["observable"],
                                "observable": recomputed["observable"]})
    if not all(entry["declared_matches_now"] for entry in probe_preflight):
        raise RuntimeError("fresh producer capture and comparator probe census disagree")

    cases = generator.arms(driver, live, independent)
    if len(cases) != 46 or set(cases) != set(generator.CASES):
        raise RuntimeError("fresh R41 union generator does not match the 46-arm census")
    planted_scope = DRAFT / "planted-cwd" / generator.SCOPE_REL
    planted_data = json.loads(scope_source.decode("utf-8"))
    planted_data.setdefault("scope_out", {})[generator.TARGET_ID] = {
        "kind": "rule-in-author-scope", "reason": "probe-only author rule"}
    planted_scope.parent.mkdir(parents=True, exist_ok=True)
    planted_scope.write_text(json.dumps(planted_data, indent=2) + "\n", encoding="utf-8")
    cases["r1-f3-prime-scope-file-honest-cwd-control"]["process_cwd"] = HEAD_SCOPE_ROOT
    r41_results = []
    for index, (name, case) in enumerate(sorted(cases.items())):
        r41_results.append(run_generated_arm(source, live, name, case, generator))

    c2_generator = load_module("r45_fresh_hunts", R45_FRESH_RUNNER)
    c2_inputs = c2_generator.make_hunts(independent)
    c2_results = []
    for name, raw in sorted(c2_inputs.items()):
        path = DRAFT / f"fresh-hunt-{name}.json"
        c2_results.append(run_fresh_c2_arm(source, LIVE_CAPTURE, path, name, raw))

    join_args = ["--live-json", str(LIVE_CAPTURE),
                 "--independent-json", str(IND_CAPTURE),
                 "--cwd", str(HEAD_SCOPE_ROOT), "--scope-file", str(SCOPE),
                 "--expect-n", "28", "--no-stamp", "--json"]
    join_command, join_proc, join_data, join_reason, join_headline = run_snapshot(
        source, join_args, HEAD_SCOPE_ROOT)
    if join_data is None:
        raise RuntimeError("live producer join returned no JSON: " + join_reason)
    agreement = join_data.get("agreement", {})
    if (join_proc.returncode != 0 or join_headline is None
            or join_headline.get("n") != 24 or join_headline.get("total") != 24
            or agreement.get("n_agree_protocol") != 24
            or agreement.get("total") != 24 or agreement.get("n_disagree") != 0):
        raise RuntimeError(f"honest live join was not protocol 24/24: {join_reason}")

    driver._PROBE_CACHE.clear()
    post_scope = json.loads(IND_CAPTURE.read_text(encoding="utf-8")).get("scoped_out_probes", {})
    probe_postflight = []
    for cid, probe in post_scope.items():
        recomputed = driver.recompute_probe(probe)
        probe_postflight.append({"check": cid,
                                 "target": probe.get("target"),
                                 "still_matches": probe.get("observable") == recomputed["observable"],
                                 "observable": recomputed["observable"]})

    live_shadow_ids = [
        "live-mode-positive-masks-independent-drift",
        "live-mode-split-across-row-channels",
        "live-top-level-observed-summary-divergence",
        "live-verdict-shadow-in-row-channel",
    ]
    by_r41 = {arm["id"]: arm for arm in r41_results}
    by_c2 = {arm["id"]: arm for arm in c2_results}
    counts = Counter(arm["landed_classification"] for arm in r41_results)
    controls = [arm for arm in r41_results if arm["baseline_classification"] == "control"]
    diagnostics = [arm for arm in r41_results if arm["baseline_classification"] == "diagnostic"]
    fresh_control = by_c2.get("unknown_nested_channel_carrier")
    no_regression = (
        len(r41_results) == 46 and len(c2_results) == 7
        and not any(arm["landed_classification"] == "unexpected-open" for arm in r41_results)
        and not any(arm["landed_classification"] == "accepted-diagnostic" for arm in r41_results)
        and all(arm["exit"] == 0 for arm in controls)
        and all(arm["exit"] != 0 for arm in diagnostics)
        and all(arm["inputs_unchanged"] for arm in r41_results + c2_results)
        and fresh_control is not None and fresh_control["exit"] == 2
        and all(entry["still_matches"] for entry in probe_postflight)
    )
    if sha_file(SCOPE) != scope_sha:
        raise RuntimeError("frozen HEAD scope changed during replay")
    source_hashes = {
        "live_producer": live_meta["source_sha256_from_git_show_head"],
        "independent_producer": ind_meta["source_sha256_from_git_show_head"],
        "scope": sha_file(SCOPE),
        "worktree_scope_excluded": sha_file(ROOT / "verifiers/harness-independent-scope.json"),
        "claims": sha_file(ROOT / ".ufo/round-46/claims.json"),
    }
    result = {
        "schema": "kotoba.round46.v2.c2-verification-fresh.v1",
        "measured_start_utc": measured_start,
        "measured_end_utc": datetime.now(timezone.utc).isoformat(),
        "target": {
            "head": head,
            "tree": tree,
            "comparator_path": "verifiers/compare_harness_independent.py",
            "comparator_sha256_from_git_show_head": driver_sha,
            "worktree_comparator_sha256_at_start": worktree_driver_start,
            "worktree_comparator_sha256_at_end": sha_file(DRIVER),
            "execution": "all comparator subprocesses loaded one immutable git-show HEAD source snapshot",
            "scope_root": str(HEAD_SCOPE_ROOT.relative_to(ROOT)),
            "scope_root_sha256_from_head_blob": scope_sha,
        },
        "sources": {
            "r41_probe_results_sha256": sha_file(R41_SOURCE),
            "r41_classifier_sha256": sha_file(R41_CLASSIFIER),
            "r41_generator_sha256": sha_file(R41_GENERATOR),
            "r45_fresh_runner_sha256": sha_file(R45_FRESH_RUNNER),
            "round46_claims_sha256": source_hashes["claims"],
            "live_producer_sha256": source_hashes["live_producer"],
            "independent_producer_sha256": source_hashes["independent_producer"],
            "scope_sha256": source_hashes["scope"],
            "scope_sha256_from_git_show_head": scope_sha,
            "worktree_scope_sha256_excluded": source_hashes["worktree_scope_excluded"],
            "scope_path": str(SCOPE.relative_to(ROOT)),
            "planted_scope": {
                "path": str(planted_scope.relative_to(ROOT)),
                "head_base_sha256": scope_sha,
                "sha256_after_intentional_extra_row": sha_file(planted_scope),
                "extra_scope_out_id": generator.TARGET_ID,
            },
            "fresh_captures": {"live": live_meta, "independent": ind_meta},
        },
        "probe_preflight": probe_preflight,
        "probe_postflight": probe_postflight,
        "r41_union_arms": r41_results,
        "c2_live_shadow_arms": [by_r41[name] for name in live_shadow_ids],
        "fresh_c2_union_arms": c2_results,
        "c2_raw_duplicate_arms": [
            by_c2["duplicate_top_level_results_member"],
            by_c2["duplicate_record_rederived_member"],
        ],
        "honest_live_join": {
            "inputs": "fresh captures from the exact HEAD producer source bytes",
            "command": join_command,
            "exit": join_proc.returncode,
            "reason": join_reason,
            "headline": join_headline,
            "agreement": join_data.get("agreement"),
            "stdout_sha256": sha_bytes(join_proc.stdout.encode("utf-8")),
            "stderr_sha256": sha_bytes(join_proc.stderr.encode("utf-8")),
        },
        "union_battery": {
            "definition": "46 regenerated R41 recipes + 7 regenerated R45 C2 hunts using fresh producer captures",
            "r41_count": len(r41_results),
            "r41_classification_counts": dict(sorted(counts.items())),
            "r41_baseline_closed_became_open": [arm["id"] for arm in r41_results
                                                  if arm["landed_classification"] == "unexpected-open"],
            "r41_controls_exit_0": all(arm["exit"] == 0 for arm in controls),
            "r41_diagnostics_nonzero": all(arm["exit"] != 0 for arm in diagnostics),
            "r41_all_inputs_unchanged": all(arm["inputs_unchanged"] for arm in r41_results),
            "fresh_c2_count": len(c2_results),
            "fresh_unknown_extension_control_exit_2": fresh_control is not None and fresh_control["exit"] == 2,
            "fresh_all_inputs_unchanged": all(arm["inputs_unchanged"] for arm in c2_results),
            "probe_snapshot_stable_through_run": all(entry["still_matches"] for entry in probe_postflight),
            "no_regression": no_regression,
        },
        "worktree_after": {
            "head": git("rev-parse", "HEAD"),
            "tree": git("rev-parse", "HEAD^{tree}"),
            "comparator_sha256": sha_file(DRIVER),
        },
    }
    if (result["worktree_after"]["head"], result["worktree_after"]["tree"]) != (head, tree):
        raise RuntimeError("HEAD/tree changed during fresh verification")
    if sha_file(SCOPE) != scope_sha:
        raise RuntimeError("frozen HEAD scope changed during fresh verification")
    if join_proc.returncode != 0:
        raise RuntimeError("honest live join was not green: " + join_reason)
    if not no_regression:
        raise RuntimeError("union battery detected a regression or unstable input")
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("R41 regenerated union: %d arms; classes=%s; baseline-closed->open=%d" % (
        len(r41_results), json.dumps(dict(sorted(counts.items())), sort_keys=True),
        len(result["union_battery"]["r41_baseline_closed_became_open"])))
    print("C2 live shadows: %s" % ",".join(
        f"{name}={by_r41[name]['exit']}" for name in live_shadow_ids))
    print("R45 regenerated union: %d arms; exits=%s" % (
        len(c2_results), ",".join(f"{a['id']}={a['exit']}" for a in c2_results)))
    print("honest live join: exit=%d headline=%s" % (join_proc.returncode, join_headline))
    print("probe stable=%s no_regression=%s" % (
        all(entry["still_matches"] for entry in probe_postflight), no_regression))
    print("head=%s tree=%s frozen_comparator=%s worktree_comparator_start=%s end=%s" % (
        head, tree, driver_sha, worktree_driver_start, result["target"]["worktree_comparator_sha256_at_end"]))
    print("output=%s sha256=%s" % (OUTPUT.relative_to(ROOT), sha_file(OUTPUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
