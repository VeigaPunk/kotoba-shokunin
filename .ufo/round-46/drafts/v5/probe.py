import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
COMPARE_REL = "verifiers/compare_harness_independent.py"
COMPARE_PATH = ROOT / COMPARE_REL
SCOPE_PATH = ROOT / "verifiers/harness-independent-scope.json"
COMMIT = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
FROZEN_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
SCOPE_SHA = "fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a"
INPUT_DIR = Path(__file__).resolve().parent / "inputs"
RESULT_PATH = ROOT / ".ufo/round-46/evidence/V5/arm-matrix.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return sha(path.read_bytes())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def state():
    return {
        "at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "worktree_comparator_sha256": file_sha(COMPARE_PATH),
        "scope_sha256": file_sha(SCOPE_PATH),
    }


def write_input(name, text):
    path = INPUT_DIR / name
    raw = text.encode("utf-8")
    path.write_bytes(raw)
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(raw), "bytes": len(raw)}


def payload(results):
    return '{"results":' + results + '}\n'


def run_cli(source, live_path, independent_path, scope_path, extra=()):
    args = [
        "--live-json", str(live_path),
        "--independent-json", str(independent_path),
        "--cwd", str(ROOT),
        "--scope-file", str(scope_path),
        "--expect-n", "1",
        "--no-stamp",
        "--json",
        *extra,
    ]
    if source == "frozen-055d3b9":
        bootstrap = (
            "import subprocess; "
            f"p={str(COMPARE_PATH)!r}; "
            f"b=subprocess.check_output(['git','show',{(COMMIT + ':' + COMPARE_REL)!r}],cwd={str(ROOT)!r}); "
            "exec(compile(b,p,'exec'),{'__name__':'__main__','__file__':p})"
        )
        argv = [sys.executable, "-B", "-c", bootstrap, *args]
    elif source == "worktree":
        argv = [sys.executable, "-B", str(COMPARE_PATH), *args]
    else:
        raise ValueError(source)
    before = file_sha(COMPARE_PATH)
    proc = subprocess.run(
        argv,
        cwd=ROOT,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        capture_output=True,
        text=True,
        timeout=30,
    )
    after = file_sha(COMPARE_PATH)
    stdout_bytes = proc.stdout.encode("utf-8")
    stderr_bytes = proc.stderr.encode("utf-8")
    try:
        document = json.loads(proc.stdout) if proc.stdout.strip() else None
    except ValueError:
        document = None
    return {
        "argv": argv,
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stdout_sha256": sha(stdout_bytes),
        "stderr": proc.stderr,
        "stderr_sha256": sha(stderr_bytes),
        "json_exit": document.get("exit") if isinstance(document, dict) else None,
        "headline": document.get("headline") if isinstance(document, dict) else None,
        "reason": document.get("reason") if isinstance(document, dict) else None,
        "worktree_comparator_sha256_before": before,
        "worktree_comparator_sha256_after": after,
        "worktree_source_stable_for_invocation": before == after,
    }


def main():
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    state_before = state()
    frozen = subprocess.check_output(
        ["git", "show", f"{COMMIT}:{COMPARE_REL}"], cwd=ROOT
    )
    frozen_sha = sha(frozen)
    if frozen_sha != FROZEN_SHA:
        raise SystemExit(f"frozen comparator SHA changed: {frozen_sha}")
    if file_sha(SCOPE_PATH) != SCOPE_SHA:
        raise SystemExit("official scope SHA changed before probe")

    live_default = write_input(
        "live-control.json",
        '{"results":[{"check":"probe.value","observed":1,"verdict":"PASS","mode":"equal"}]}\n',
    )
    live_path = ROOT / live_default["path"]
    independent_control = write_input(
        "independent-control.json",
        payload('[{"check":"probe.value","re_derived":1}]'),
    )
    ordinary_mismatch = write_input(
        "independent-ordinary-mismatch.json",
        payload('[{"check":"probe.value","re_derived":999}]'),
    )
    arm_specs = [
        ("ordinary-control", live_default, independent_control, "official", (), 0, None),
        ("ordinary-value-mismatch", live_default, ordinary_mismatch, "official", (), 1, None),
        ("top-results-divergent-first-honest-last", live_default,
         write_input("ind-top-results-bad-first-good-last.json",
                     '{"results":[{"check":"probe.value","re_derived":999}],"results":[{"check":"probe.value","re_derived":1}]}\n'),
         "official", (), 0, "results"),
        ("top-results-honest-first-divergent-last", live_default,
         write_input("ind-top-results-good-first-bad-last.json",
                     '{"results":[{"check":"probe.value","re_derived":1}],"results":[{"check":"probe.value","re_derived":999}]}\n'),
         "official", (), 1, "results"),
        ("record-rederived-divergent-first-honest-last", live_default,
         write_input("ind-record-rederived-bad-first-good-last.json",
                     payload('[{"check":"probe.value","re_derived":999,"re_derived":1}]')),
         "official", (), 0, "re_derived"),
        ("record-rederived-honest-first-divergent-last", live_default,
         write_input("ind-record-rederived-good-first-bad-last.json",
                     payload('[{"check":"probe.value","re_derived":1,"re_derived":999}]')),
         "official", (), 1, "re_derived"),
        ("record-check-rogue-first-live-id-last", live_default,
         write_input("ind-record-check-rogue-first-live-last.json",
                     payload('[{"check":"rogue.value","check":"probe.value","re_derived":1}]')),
         "official", (), 0, "check"),
        ("dotted-check-map-divergent-first-honest-last", live_default,
         write_input("ind-dotted-map-bad-first-good-last.json",
                     '{"checks":{"probe.value":999,"probe.value":1}}\n'),
         "official", (), 0, "probe.value"),
        ("embedded-noisy-json-rederived-duplicate", live_default,
         write_input("ind-noisy-rederived-duplicate.json",
                     'producer log before JSON\n{"results":[{"check":"probe.value","re_derived":999,"re_derived":1}]}\ntrailing log\n'),
         "official", (), 0, "re_derived"),
        ("live-observed-divergent-first-honest-last", write_input(
             "live-observed-bad-first-good-last.json",
             '{"results":[{"check":"probe.value","observed":999,"observed":1,"verdict":"PASS","mode":"equal"}]}\n'),
         independent_control, "official", (), 0, "observed"),
        ("live-mode-positive-last", write_input(
             "live-mode-equal-first-positive-last.json",
             '{"results":[{"check":"probe.value","observed":7,"verdict":"PASS","mode":"equal","mode":"positive"}]}\n'),
         write_input("ind-positive-control.json", payload('[{"check":"probe.value","re_derived":8}]')),
         "official", (), 0, "mode"),
        ("live-mode-equal-last", write_input(
             "live-mode-positive-first-equal-last.json",
             '{"results":[{"check":"probe.value","observed":7,"verdict":"PASS","mode":"positive","mode":"equal"}]}\n'),
         write_input("ind-positive-control-reverse.json", payload('[{"check":"probe.value","re_derived":8}]')),
         "official", (), 1, "mode"),
        ("live-verdict-pass-last", write_input(
             "live-verdict-drift-first-pass-last.json",
             '{"results":[{"check":"probe.value","observed":1,"verdict":"DRIFT","verdict":"PASS","mode":"equal"}]}\n'),
         independent_control, "official", (), 0, "verdict"),
        ("live-verdict-drift-last", write_input(
             "live-verdict-pass-first-drift-last.json",
             '{"results":[{"check":"probe.value","observed":1,"verdict":"PASS","verdict":"DRIFT","mode":"equal"}]}\n'),
         independent_control, "official", (), 3, "verdict"),
        ("record-status-derived-last", live_default,
         write_input("ind-status-unlanded-first-derived-last.json",
                     payload('[{"check":"probe.value","re_derived":1,"status":"UNLANDED","status":"DERIVED"}]')),
         "official", (), 0, "status"),
        ("record-status-unlanded-last", live_default,
         write_input("ind-status-derived-first-unlanded-last.json",
                     payload('[{"check":"probe.value","re_derived":1,"status":"DERIVED","status":"UNLANDED"}]')),
         "official", (), 1, "status"),
        ("scope-file-scopeout-first-shadowed-by-empty-last", live_default,
         independent_control,
         write_input("scope-duplicate-scope-out.json",
                     '{"scope_out":{"probe.value":{"kind":"rule-in-author-scope","reason":"shadowed"}},"scope_out":{},"probe_contract":{"kind":"rule-spread-census"}}\n'),
         (), 0, "scope_out"),
        ("strict-headline-does-not-strict-parse", live_default,
         write_input("ind-strict-headline-top-results-duplicate.json",
                     '{"results":[{"check":"probe.value","re_derived":999}],"results":[{"check":"probe.value","re_derived":1}]}\n'),
         "official", ("--strict-headline",), 0, "results"),
        ("no-strict-json-cli-option", live_default, independent_control,
         "official", ("--strict-json",), 2, None),
    ]

    input_index = {"live-control": live_default, "independent-control": independent_control}
    results = []
    for name, live_rec, ind_rec, scope_choice, extra, baseline_exit, duplicate_token in arm_specs:
        scope_rec = scope_choice if isinstance(scope_choice, dict) else None
        scope_path = ROOT / scope_rec["path"] if scope_rec else SCOPE_PATH
        live_file = ROOT / live_rec["path"]
        independent_file = ROOT / ind_rec["path"]
        duplicate_path = (
            scope_path if duplicate_token == "scope_out"
            else live_file if name.startswith("live-")
            else independent_file
        )
        duplicate_occurrences = (
            duplicate_path.read_bytes().count(json.dumps(duplicate_token).encode("utf-8"))
            if duplicate_token is not None else None
        )
        for source in ("frozen-055d3b9", "worktree"):
            observed = run_cli(source, live_file, independent_file, scope_path, extra)
            expected_exit = (
                baseline_exit if source == "frozen-055d3b9"
                else 2 if duplicate_token is not None
                else baseline_exit
            )
            input_meta = {
                "live": {"path": live_rec["path"], "sha256": file_sha(live_file), "bytes": live_file.stat().st_size},
                "independent": {"path": ind_rec["path"], "sha256": file_sha(independent_file), "bytes": independent_file.stat().st_size},
                "scope": {"path": str(scope_path.relative_to(ROOT)) if scope_path.is_relative_to(ROOT) else str(scope_path),
                          "sha256": file_sha(scope_path), "bytes": scope_path.stat().st_size},
            }
            observed.update({
                "source": source,
                "arm": name,
                "expected_exit": expected_exit,
                "input_bytes": input_meta,
                "duplicate_member_token": duplicate_token,
                "duplicate_member_target": str(duplicate_path.relative_to(ROOT)),
                "raw_member_name_occurrences": duplicate_occurrences,
            })
            if duplicate_token is not None:
                observed["duplicate_member_rejected_named"] = (
                    source != "worktree"
                    or (observed["exit"] == 2 and "duplicate JSON member" in observed["stderr"])
                )
            if name == "no-strict-json-cli-option":
                observed["flag_rejected_as_unknown"] = "unrecognized arguments" in observed["stderr"]
            observed["expectation_met"] = (
                observed["exit"] == expected_exit
                and (duplicate_occurrences == 2 if duplicate_token is not None else True)
                and observed.get("duplicate_member_rejected_named", True)
                and observed.get("flag_rejected_as_unknown", True)
            )
            results.append(observed)

    state_after = state()
    frozen_after = sha(subprocess.check_output(
        ["git", "show", f"{COMMIT}:{COMPARE_REL}"], cwd=ROOT
    ))
    all_inputs = {}
    for path in sorted(INPUT_DIR.iterdir()):
        if path.is_file():
            raw = path.read_bytes()
            all_inputs[str(path.relative_to(ROOT))] = {"sha256": sha(raw), "bytes": len(raw)}
    expected_results = all(row["expectation_met"] for row in results)
    worktree_hashes = {
        row[key]
        for row in results if row["source"] == "worktree"
        for key in ("worktree_comparator_sha256_before", "worktree_comparator_sha256_after")
    }
    stable = (
        state_before["head"] == state_after["head"] == COMMIT
        and state_before["tree"] == state_after["tree"]
        and state_before["scope_sha256"] == state_after["scope_sha256"] == SCOPE_SHA
        and state_before["worktree_comparator_sha256"] == state_after["worktree_comparator_sha256"]
        and state_before["worktree_comparator_sha256"] in worktree_hashes
        and frozen_after == FROZEN_SHA
        and len(worktree_hashes) == 1
    )
    report = {
        "seat": "V5",
        "measurement": "raw duplicate JSON member arms; decoder behavior, not a claim about producer output",
        "command": "PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v5/probe.py",
        "runner_sha256": file_sha(Path(__file__).resolve()),
        "started": state_before,
        "ended": state_after,
        "frozen_comparator": {"revision": COMMIT, "sha256": frozen_sha, "sha256_after": frozen_after},
        "official_scope_sha256": SCOPE_SHA,
        "worktree_comparator_shas_observed": sorted(worktree_hashes),
        "arms_per_source": len(arm_specs),
        "invocations": len(results),
        "all_expected_exits": expected_results,
        "pinned_state_stable": stable,
        "inputs": all_inputs,
        "results": results,
    }
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "result": str(RESULT_PATH.relative_to(ROOT)),
        "arms_per_source": len(arm_specs),
        "invocations": len(results),
        "all_expected_exits": expected_results,
        "pinned_state_stable": stable,
        "worktree_comparator_shas_observed": sorted(worktree_hashes),
        "failed": [f'{r["source"]}:{r["arm"]}:{r["exit"]}!={r["expected_exit"]}' for r in results if not r["expectation_met"]],
    }, sort_keys=True))
    return 0 if expected_results and stable else 1


if __name__ == "__main__":
    raise SystemExit(main())
