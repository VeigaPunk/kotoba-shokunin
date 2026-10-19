#!/usr/bin/env python3
import contextlib
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
R41_REPLAY = ROOT / ".ufo/round-45/evidence/c2/replay_r41.py"
R41_INPUT = ROOT / ".ufo/round-41/evidence/probe-results.json"
R41_CLASSIFIER = ROOT / ".ufo/round-41/evidence/v10-channel-census.py"
R45_EVIDENCE = ROOT / ".ufo/round-45/evidence/c2"
R45_FRESH = R45_EVIDENCE / "fresh-channel-hunts.json"
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
LIVE = ROOT / "verifiers/verify_harness_claims.py"
INDEPENDENT = ROOT / "verifiers/verify_harness_independent.py"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
EXPECTED_HEAD = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
EXPECTED_TREE = "e8dced184612a9738c5b8d244a0837fbd955a7da"
EXPECTED_DRIVER_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
OUTPUT = DRAFT / "v2-results.json"
REPLAY_OUTPUT = DRAFT / "r41-union-replay.json"
RECEIPT = DRAFT / "r41-replay-receipt.json"


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(path.read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def parse_response(proc):
    try:
        data = json.loads(proc.stdout)
        return data, data.get("reason", ""), data.get("headline")
    except (ValueError, TypeError):
        return None, (proc.stderr or proc.stdout).strip()[-1200:], None


def run_snapshot(source, args, cwd=ROOT):
    wrapper = (
        "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
        "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
        "{'__name__':'__main__','__file__':p})"
    )
    command = [sys.executable, "-c", wrapper, str(DRIVER), *args]
    proc = subprocess.run(command, cwd=cwd, input=source.decode("utf-8"),
                          capture_output=True, text=True, timeout=300)
    data, reason, headline = parse_response(proc)
    return command, proc, data, reason, headline


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    measured_start = datetime.now(timezone.utc).isoformat()
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    source = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{head}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    driver_sha = sha_bytes(source)
    worktree_driver_start = sha_file(DRIVER)
    if head != EXPECTED_HEAD or tree != EXPECTED_TREE:
        raise RuntimeError(f"landed target changed: {head} {tree}")
    if driver_sha != EXPECTED_DRIVER_SHA:
        raise RuntimeError(f"frozen comparator hash changed: {driver_sha}")

    replay_spec = importlib.util.spec_from_file_location("r41_replay", R41_REPLAY)
    replay = importlib.util.module_from_spec(replay_spec)
    replay_spec.loader.exec_module(replay)
    replay.TARGET = head
    replay.OUTPUT = REPLAY_OUTPUT
    replay.RECEIPT = RECEIPT
    replay_stdout = io.StringIO()
    with contextlib.redirect_stdout(replay_stdout):
        replay_exit = replay.main()
    if replay_exit != 0:
        raise RuntimeError("historical 46-arm replay failed: " + replay_stdout.getvalue())
    replay_data = json.loads(REPLAY_OUTPUT.read_text(encoding="utf-8"))
    live_shadow_ids = [
        "live-mode-positive-masks-independent-drift",
        "live-mode-split-across-row-channels",
        "live-top-level-observed-summary-divergence",
        "live-verdict-shadow-in-row-channel",
    ]
    replay_by_id = {arm["id"]: arm for arm in replay_data["arms"]}

    fresh_data = json.loads(R45_FRESH.read_text(encoding="utf-8"))
    fresh_arms = []
    immutable = {
        "live_json": sha_file(R45_EVIDENCE / "fresh-live.json"),
        "scope_file": sha_file(SCOPE),
    }
    for old_arm in fresh_data["arms"]:
        arm_id = old_arm["id"]
        path = R45_EVIDENCE / f"hunt-{arm_id}.json"
        before = {**immutable, "independent_json": sha_file(path)}
        if before["independent_json"] != old_arm["independent_payload_sha256"]:
            raise RuntimeError(f"preserved input hash differs for {arm_id}")
        args = [
            "--live-json", str(R45_EVIDENCE / "fresh-live.json"),
            "--independent-json", str(path),
            "--cwd", str(ROOT), "--scope-file", str(SCOPE),
            "--expect-n", "28", "--no-stamp", "--json",
        ]
        command, proc, data, reason, headline = run_snapshot(source, args)
        after = {**immutable, "independent_json": sha_file(path)}
        fresh_arms.append({
            "id": arm_id,
            "input_path": str(path.relative_to(ROOT)),
            "expected_round45_exit": old_arm["exit"],
            "expected_round45_target": fresh_data["target"],
            "input_sha256_before": before,
            "input_sha256_after": after,
            "inputs_unchanged": before == after,
            "command": command,
            "exit": proc.returncode,
            "reason": reason,
            "headline": headline,
            "stdout_sha256": sha_bytes(proc.stdout.encode("utf-8")),
            "stderr_sha256": sha_bytes(proc.stderr.encode("utf-8")),
        })

    live_command = f"{sys.executable} {LIVE} --json"
    independent_command = f"{sys.executable} {INDEPENDENT} --json"
    join_args = [
        "--live-cmd", live_command,
        "--independent-cmd", independent_command,
        "--cwd", str(ROOT), "--scope-file", str(SCOPE),
        "--expect-n", "28", "--no-stamp", "--json",
    ]
    join_command, join_proc, join_data, join_reason, join_headline = run_snapshot(source, join_args)
    if join_data is None:
        raise RuntimeError("live producer join returned no JSON: " + join_reason)

    replay_counts = replay_data["summary"]["landed_classification_counts"]
    r41_controls = [arm for arm in replay_data["arms"]
                    if arm["baseline_classification"] == "control"]
    r41_diagnostics = [arm for arm in replay_data["arms"]
                       if arm["baseline_classification"] == "diagnostic"]
    fresh_control = [arm for arm in fresh_arms if arm["id"] == "unknown_nested_channel_carrier"]
    no_union_regression = (
        replay_data["summary"]["all_input_hashes_unchanged"]
        and replay_data["summary"]["unexpected_open_from_baseline_closed"] == 0
        and all(arm["actual"]["exit"] == 0 for arm in r41_controls)
        and all(arm["actual"]["exit"] != 0 for arm in r41_diagnostics)
        and all(arm["inputs_unchanged"] for arm in fresh_arms)
        and len(fresh_control) == 1 and fresh_control[0]["exit"] == 2
    )
    producer_hashes = {
        "live": sha_file(LIVE),
        "independent": sha_file(INDEPENDENT),
        "scope": sha_file(SCOPE),
    }
    result = {
        "schema": "kotoba.round46.v2.c2-verification.v1",
        "measured_start_utc": measured_start,
        "measured_end_utc": datetime.now(timezone.utc).isoformat(),
        "target": {
            "head": head,
            "tree": tree,
            "comparator_path": "verifiers/compare_harness_independent.py",
            "comparator_sha256_from_git_show_head": driver_sha,
            "worktree_comparator_sha256_at_start": worktree_driver_start,
            "worktree_comparator_sha256_at_end": sha_file(DRIVER),
            "execution": "all comparator arms used the frozen git-show HEAD source bytes",
        },
        "source_inputs": {
            "claims_sha256": sha_file(ROOT / ".ufo/round-46/claims.json"),
            "r41_probe_results_sha256": sha_file(R41_INPUT),
            "r41_classifier_sha256": sha_file(R41_CLASSIFIER),
            "r45_fresh_hunt_results_sha256": sha_file(R45_FRESH),
            "live_producer_sha256": producer_hashes["live"],
            "independent_producer_sha256": producer_hashes["independent"],
            "scope_sha256": producer_hashes["scope"],
            "r45_live_capture_sha256": immutable["live_json"],
        },
        "c2_live_shadow_arms": [replay_by_id[name] for name in live_shadow_ids],
        "fresh_union_arms": fresh_arms,
        "honest_live_join": {
            "command": join_command,
            "exit": join_proc.returncode,
            "reason": join_reason,
            "headline": join_headline,
            "agreement": join_data.get("agreement"),
            "stdout_sha256": sha_bytes(join_proc.stdout.encode("utf-8")),
            "stderr_sha256": sha_bytes(join_proc.stderr.encode("utf-8")),
        },
        "union_battery": {
            "definition": "46 archived R41 arms + 7 R45 fresh C2 arms",
            "r41_arm_count": len(replay_data["arms"]),
            "r41_landed_classification_counts": replay_counts,
            "r41_unexpected_open_ids": replay_data["summary"]["unexpected_open_arm_ids"],
            "r41_input_hashes_unchanged": replay_data["summary"]["all_input_hashes_unchanged"],
            "r41_control_arms_exit_0": all(arm["actual"]["exit"] == 0 for arm in r41_controls),
            "r41_diagnostic_arms_nonzero": all(arm["actual"]["exit"] != 0 for arm in r41_diagnostics),
            "r45_fresh_arm_count": len(fresh_arms),
            "r45_control_exit_2": len(fresh_control) == 1 and fresh_control[0]["exit"] == 2,
            "all_fresh_inputs_unchanged": all(arm["inputs_unchanged"] for arm in fresh_arms),
            "no_regression": no_union_regression,
        },
        "worktree_after": {
            "head": git("rev-parse", "HEAD"),
            "tree": git("rev-parse", "HEAD^{tree}"),
            "comparator_sha256": sha_file(DRIVER),
        },
    }
    if result["worktree_after"]["head"] != head or result["worktree_after"]["tree"] != tree:
        raise RuntimeError("HEAD/tree changed during verification")
    if result["honest_live_join"]["exit"] != 0:
        raise RuntimeError("honest live join was not green: " + join_reason)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("r41 union: %d arms; classes=%s; unexpected-open=%d" % (
        len(replay_data["arms"]), json.dumps(replay_counts, sort_keys=True),
        replay_data["summary"]["unexpected_open_from_baseline_closed"]))
    print("fresh union: %d arms; exits=%s" % (
        len(fresh_arms), ",".join(f"{a['id']}={a['exit']}" for a in fresh_arms)))
    print("C2 live shadows: %s" % ",".join(
        f"{arm_id}={replay_by_id[arm_id]['actual']['exit']}" for arm_id in live_shadow_ids))
    print("honest live join: exit=%d headline=%s" % (join_proc.returncode, join_headline))
    print("no_regression=%s head=%s tree=%s comparator=%s" % (
        no_union_regression, head, tree, driver_sha))
    print("output=%s sha256=%s" % (OUTPUT.relative_to(ROOT), sha_file(OUTPUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
