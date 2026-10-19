import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
COMPARATOR = WORK / "compare-055d3b9.py"
LIVE_PATH = WORK / "live-base.json"
IND_PATH = WORK / "independent-base.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
RESULT_PATH = WORK / "probe-results.json"
CHECK_ID = "omp.elf.template_bytes"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def state():
    def git(*args):
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                           text=True, check=True).stdout.strip()

    return {
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "comparator": sha(COMPARATOR),
        "worktree_comparator": sha(ROOT / "verifiers/compare_harness_independent.py"),
        "live_source": sha(ROOT / "verifiers/verify_harness_claims.py"),
        "independent_source": sha(ROOT / "verifiers/verify_harness_independent.py"),
        "scope": sha(SCOPE),
    }


def row_inputs():
    live = json.loads(LIVE_PATH.read_text(encoding="utf-8"))
    independent = json.loads(IND_PATH.read_text(encoding="utf-8"))
    live_row = copy.deepcopy(next(row for row in live["results"]
                                  if row["check"] == CHECK_ID))
    ind_row = copy.deepcopy(next(row for row in independent["results"]
                                 if row["check"] == CHECK_ID))
    return live_row, ind_row, copy.deepcopy(live["observed"])


def input_pair(live_row, ind_row, **live_fields):
    live = {"results": [live_row], **live_fields}
    independent = {"results": [ind_row]}
    return live, independent


def run_case(name, live, independent, expect_exit, expect_text="", expect_n=1):
    live_path = WORK / f"{name}-live.json"
    ind_path = WORK / f"{name}-independent.json"
    live_path.write_text(json.dumps(live, indent=2, sort_keys=True) + "\n",
                         encoding="utf-8")
    ind_path.write_text(json.dumps(independent, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    argv = [sys.executable, str(COMPARATOR), "--live-json", str(live_path),
            "--independent-json", str(ind_path), "--expect-n", str(expect_n), "--cwd",
            str(ROOT), "--scope-file", "verifiers/harness-independent-scope.json",
            "--no-stamp", "--json"]
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=120)
    combined = proc.stdout + proc.stderr
    passed = proc.returncode == expect_exit and expect_text in combined
    parsed = None
    if proc.stdout.strip():
        try:
            payload = json.loads(proc.stdout)
            parsed = {
                "headline": payload.get("headline"),
                "agreement": payload.get("agreement"),
                "live": payload.get("live"),
                "exit": payload.get("exit"),
                "reason": payload.get("reason"),
            }
        except ValueError:
            pass
    return {
        "name": name,
        "argv": argv,
        "cwd": str(ROOT),
        "live_json": {"path": str(live_path), "sha256": sha(live_path)},
        "independent_json": {"path": str(ind_path), "sha256": sha(ind_path)},
        "expected_exit": expect_exit,
        "expected_text": expect_text,
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "parsed": parsed,
        "assertion_pass": passed,
    }


def main():
    before = state()
    cases = []
    live_row, ind_row, observed_summary = row_inputs()
    cases.append(run_case(
        "one-row-control", *input_pair(copy.deepcopy(live_row), copy.deepcopy(ind_row)),
        0, '"total": 1'))

    row = copy.deepcopy(live_row)
    row.update({"observed": 7, "expected": 7, "mode": "equal", "verdict": "PASS"})
    ind = copy.deepcopy(ind_row)
    ind.update({"value": 7, "re_derived": 7})
    live, independent = input_pair(row, ind, checks={CHECK_ID: 8})
    cases.append(run_case("checks-map-observation-implies-drift-vs-pass",
                          live, independent, 2, "channel divergence"))

    live, independent = input_pair(
        copy.deepcopy(row), copy.deepcopy(ind),
        checks={CHECK_ID: {"observed": 7, "mode": "equal", "verdict": "DRIFT"}})
    cases.append(run_case("checks-map-verdict-object-vs-pass",
                          live, independent, 2, "channel divergence"))

    live_row, ind_row, observed_summary = row_inputs()
    live_row.update({"observed": 7, "expected": 7, "mode": "positive", "verdict": "PASS"})
    ind_row.update({"value": 999, "re_derived": 999})
    shadow = copy.deepcopy(live_row)
    shadow["mode"] = "equal"
    live, independent = input_pair(live_row, ind_row, checks=[shadow])
    cases.append(run_case("checks-row-mode-shadow-masks-drift",
                          live, independent, 0, '"total": 1'))

    live_row, ind_row, observed_summary = row_inputs()
    live_row.update({"observed": 7, "expected": 7, "mode": "positive", "verdict": "PASS"})
    ind_row.update({"value": 999, "re_derived": 999})
    live, independent = input_pair(
        live_row, ind_row, modes={CHECK_ID: "equal"})
    cases.append(run_case("top-level-mode-shadow-masks-drift",
                          live, independent, 0, '"total": 1'))

    live_row, ind_row, observed_summary = row_inputs()
    live_row.update({"observed": 7, "expected": 7, "mode": "equal", "verdict": "PASS"})
    ind_row.update({"value": 999, "re_derived": 999})
    shadow = copy.deepcopy(live_row)
    shadow["mode"] = "positive"
    live, independent = input_pair(live_row, ind_row, checks=[shadow])
    cases.append(run_case("primary-equal-shadow-positive-does-not-rescue",
                          live, independent, 1, CHECK_ID))

    live_row, ind_row, observed_summary = row_inputs()
    live_row.update({"observed": 7, "expected": 7, "mode": "equal", "verdict": "PASS"})
    ind_row.update({"value": 7, "re_derived": 7})
    live, independent = input_pair(live_row, ind_row,
                                   observed=observed_summary)
    live["observed"]["omp"]["template_bytes"] = 999
    cases.append(run_case("observed-summary-diverges-from-row",
                          live, independent, 0, '"total": 1'))

    live_row, ind_row, _summary = row_inputs()
    live_row.update({"observed": 7, "expected": 7, "mode": "equal", "verdict": "PASS"})
    ind_row.update({"value": 7, "re_derived": 7})
    live, independent = input_pair(
        live_row, ind_row, verdicts={CHECK_ID: "DRIFT"})
    cases.append(run_case("top-level-verdict-map-shadow",
                          live, independent, 0, '"total": 1'))

    after = state()
    result = {
        "measured_at": datetime.now(timezone.utc).isoformat(),
        "head": before["head"],
        "tree": before["tree"],
        "comparator_snapshot": str(COMPARATOR),
        "comparator_sha256": before["comparator"],
        "worktree_comparator_sha256": before["worktree_comparator"],
        "producer_sources": {
            "live_sha256": before["live_source"],
            "independent_sha256": before["independent_source"],
        },
        "scope_sha256": before["scope"],
        "producer_captures": {
            "live_sha256": sha(LIVE_PATH),
            "independent_sha256": sha(IND_PATH),
        },
        "runner_sha256": sha(__file__),
        "before_state": before,
        "after_state": after,
        "state_unchanged": all(before[key] == after[key] for key in (
            "head", "tree", "comparator", "live_source", "independent_source", "scope")),
        "case_count": len(cases),
        "assertions_passed": sum(case["assertion_pass"] for case in cases),
        "cases": cases,
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                           encoding="utf-8")
    print(json.dumps({
        "result": str(RESULT_PATH),
        "head": before["head"],
        "tree": before["tree"],
        "comparator_sha256": before["comparator"],
        "state_unchanged": result["state_unchanged"],
        "assertions_passed": result["assertions_passed"],
        "case_count": result["case_count"],
        "cases": [{"name": case["name"], "exit": case["exit"],
                   "parsed": case["parsed"], "stderr": case["stderr"],
                   "assertion_pass": case["assertion_pass"]} for case in cases],
    }, indent=2, sort_keys=True))
    return 0 if result["state_unchanged"] and all(
        case["assertion_pass"] for case in cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
