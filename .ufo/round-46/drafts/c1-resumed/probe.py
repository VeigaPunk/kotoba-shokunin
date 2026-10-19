#!/usr/bin/env python3
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
EVIDENCE = ROOT / ".ufo/round-46/evidence/c1-resumed"
INPUTS = WORK / "inputs"
COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
FROZEN_REV = "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae"
FROZEN_BLOB = f"{FROZEN_REV}:verifiers/compare_harness_independent.py"
FROZEN_SHA = "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def sha(path):
    return sha_bytes(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def snapshot():
    return {
        "at_utc": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "comparator_sha256": sha(COMPARATOR),
        "frozen_sha256": sha_bytes(subprocess.run(
            ["git", "-C", str(ROOT), "show", FROZEN_BLOB], check=True,
            capture_output=True).stdout),
        "claims_sha256": sha(ROOT / ".ufo/round-46/claims.json"),
        "scope_sha256": sha(SCOPE),
        "live_source_sha256": sha(ROOT / "verifiers/verify_harness_claims.py"),
        "independent_source_sha256": sha(ROOT / "verifiers/verify_harness_independent.py"),
    }


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def write(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(raw, encoding="utf-8")
    return path


def json_file(path, value):
    return dump(path, value)


def make_carrier(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    (path / "first.jsonl").write_text(
        '{"ts":"2026-10-01T00:00:00Z","skills":"<skills>\\n- alpha\\n</skills>"}\n',
        encoding="utf-8")
    (path / "second.jsonl").write_text(
        '{"ts":"2026-10-02T00:00:00Z","skills":"<skills>\\n- alpha\\n- beta\\n</skills>"}\n',
        encoding="utf-8")
    for index, item in enumerate(sorted(path.glob("*.jsonl"))):
        os.utime(item, ns=(1_700_000_000_000_000_000 + index * 1_000_000_000,
                          1_700_000_000_000_000_000 + index * 1_000_000_000))
    return path


def run(source, name, live_path, ind_path, scope_path, cwd, process_cwd=None,
        expect_n=1, receipt=True):
    if source == "candidate":
        command = [sys.executable, "-B", str(COMPARATOR)]
    else:
        code = (
            "import hashlib,subprocess,sys; "
            f"root={str(ROOT)!r}; blob={FROZEN_BLOB!r}; "
            f"expected={FROZEN_SHA!r}; filename={str(COMPARATOR)!r}; "
            "src=subprocess.run(['git','-C',root,'show',blob],check=True,capture_output=True).stdout; "
            "actual=hashlib.sha256(src).hexdigest(); "
            "actual==expected or sys.exit('frozen comparator hash mismatch: '+actual); "
            "exec(compile(src,filename,'exec'),{'__name__':'__main__','__file__':filename})"
        )
        command = [sys.executable, "-B", "-c", code]
    command += ["--live-json", str(Path(live_path).resolve()),
                "--independent-json", str(Path(ind_path).resolve()),
                "--expect-n", str(expect_n), "--cwd", str(Path(cwd).resolve()),
                "--scope-file", str(scope_path), "--no-stamp", "--json"]
    receipt_path = EVIDENCE / f"{name}-{source}.receipt.json"
    if receipt:
        command += ["--receipt", str(receipt_path)]
    proc = subprocess.run(command, cwd=process_cwd, capture_output=True, text=True,
                          timeout=120)
    stdout_path = EVIDENCE / f"{name}-{source}.stdout.txt"
    stderr_path = EVIDENCE / f"{name}-{source}.stderr.txt"
    stdout_path.write_text(proc.stdout, encoding="utf-8")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    try:
        parsed = json.loads(proc.stdout)
    except ValueError:
        parsed = None
    receipt_data = None
    if receipt_path.is_file():
        try:
            receipt_data = json.loads(receipt_path.read_text(encoding="utf-8"))
        except ValueError:
            receipt_data = None
    return {
        "source": source,
        "command": command,
        "process_cwd": str(Path(process_cwd or ROOT).resolve()),
        "live": {"path": str(Path(live_path).resolve()), "sha256": sha(live_path)},
        "independent": {"path": str(Path(ind_path).resolve()), "sha256": sha(ind_path)},
        "scope_argument": str(scope_path),
        "exit": proc.returncode,
        "stdout_sha256": sha(stdout_path),
        "stderr_sha256": sha(stderr_path),
        "stderr": proc.stderr.strip(),
        "headline": parsed.get("headline") if isinstance(parsed, dict) else None,
        "reason": parsed.get("reason") if isinstance(parsed, dict) else None,
        "scoped_out": parsed.get("scoped_out") if isinstance(parsed, dict) else None,
        "receipt_path": str(receipt_path) if receipt_path.is_file() else None,
        "receipt": receipt_data,
    }


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    INPUTS.mkdir(parents=True, exist_ok=True)
    before = snapshot()
    if before["frozen_sha256"] != FROZEN_SHA:
        raise RuntimeError("frozen 055d3b9 comparator SHA mismatch")

    live_control = json_file(INPUTS / "live-one.json", {
        "results": [{"check": "a.b", "observed": 7, "mode": "equal", "verdict": "PASS"}]
    })
    ind_control = json_file(INPUTS / "ind-one.json", {
        "results": [{"check": "a.b", "re_derived": 7, "status": "DERIVED"}]
    })

    arms = []
    def arm(name, live, independent, scope=SCOPE, cwd=ROOT, process_cwd=None,
            expect_n=1):
        arms.append({"name": name, "live": Path(live), "independent": Path(independent),
                     "scope": Path(scope), "cwd": Path(cwd),
                     "process_cwd": Path(process_cwd) if process_cwd else None,
                     "expect_n": expect_n})

    arm("honest-one-row-control", live_control, ind_control)

    raw_dup = write(INPUTS / "duplicate-results-member.independent.json",
                    '{"results":[{"check":"a.b","re_derived":999}],'
                    '"results":[{"check":"a.b","re_derived":7}]}\n')
    arm("raw-duplicate-results-member", live_control, raw_dup)

    fixture_root = ROOT / "verifiers/fixtures/compare-harness-independent"
    for case in ("live-mode-shadow", "live-verdict-shadow", "live-summary-shadow"):
        arm(case, fixture_root / case / "live.json",
            fixture_root / case / "independent.json")

    duplicate_status_live = json_file(INPUTS / "duplicate-status.live.json", {
        "results": [{"check": "a.b", "observed": 7, "mode": "equal", "verdict": "PASS"}]
    })
    duplicate_status_ind = json_file(INPUTS / "duplicate-status.independent.json", {
        "results": [
            {"check": "a.b", "re_derived": 7, "status": "UNLANDED"},
            {"check": "a.b", "re_derived": 7, "status": "DERIVED"},
        ]
    })
    arm("duplicate-id-status-order", duplicate_status_live, duplicate_status_ind)

    carrier = make_carrier(INPUTS / "carrier")
    alternate = make_carrier(INPUTS / "alternate-carrier")
    committed_scope = {
        "scope_out": {"a.c": {"reason": "payload blocker", "kind": "rule-in-author-scope"}},
        "probe_contract": {"kind": "rule-spread-census", "target": str(carrier)},
    }
    planted_cwd = INPUTS / "planted-cwd"
    planted_scope_path = planted_cwd / "verifiers/harness-independent-scope.json"
    honest_cwd = INPUTS / "honest-cwd"
    honest_scope_path = honest_cwd / "verifiers/harness-independent-scope.json"
    json_file(planted_scope_path, committed_scope)
    json_file(honest_scope_path, {"scope_out": {},
                                  "probe_contract": {"kind": "rule-spread-census",
                                                     "target": str(carrier)}})
    scoped_live = json_file(INPUTS / "scope-live.json", {"results": [
        {"check": "a.b", "observed": 7, "mode": "equal", "verdict": "PASS"},
        {"check": "a.c", "observed": None, "mode": "equal", "verdict": "PASS"},
    ]})

    def scope_independent(reason="payload blocker", evidence="SCOPED_OUT: payload blocker", target=carrier):
        probe_module_source = COMPARATOR.read_bytes()
        namespace = {"__name__": "c1_probe_module", "__file__": str(COMPARATOR)}
        exec(compile(probe_module_source, str(COMPARATOR), "exec"), namespace)
        probe = namespace["recompute_probe"]({"kind": "rule-spread-census", "target": str(target)})
        scoped_probe = {
            "kind": "rule-spread-census", "target": str(target),
            "observable": probe["observable"],
        }
        return json_file(INPUTS / f"scope-{hashlib.sha256((reason+evidence+str(target)).encode()).hexdigest()[:10]}.independent.json", {
            "results": [
                {"check": "a.b", "re_derived": 7, "status": "DERIVED"},
                {"check": "a.c", "re_derived": None, "status": "SCOPED_OUT",
                 "reason": reason, "evidence": evidence, "probe": scoped_probe},
            ],
            "scoped_out": {"a.c": reason},
            "scoped_out_probes": {"a.c": scoped_probe},
        })

    scope_base = scope_independent()
    arm("scope-cwd-relative-path-split", scoped_live, scope_base,
        scope="verifiers/harness-independent-scope.json", cwd=honest_cwd,
        process_cwd=planted_cwd, expect_n=2)
    arm("scope-reason-drift", scoped_live,
        scope_independent(reason="fabricated reason"), scope=planted_scope_path,
        expect_n=2)
    arm("scope-evidence-drift", scoped_live,
        scope_independent(evidence="fabricated evidence"), scope=planted_scope_path,
        expect_n=2)
    arm("scope-probe-target-drift", scoped_live,
        scope_independent(target=alternate), scope=planted_scope_path,
        expect_n=2)

    results = {}
    for item in arms:
        values = {}
        for source in ("frozen", "candidate"):
            values[source] = run(
                source, item["name"], item["live"], item["independent"],
                item["scope"], item["cwd"], item["process_cwd"], item["expect_n"],
                receipt=(item["name"] == "scope-cwd-relative-path-split"),
            )
        results[item["name"]] = values

    control = run("candidate", "scope-cwd-planted-control", scoped_live, scope_base,
                  "verifiers/harness-independent-scope.json", planted_cwd,
                  planted_cwd, expect_n=2, receipt=True)
    after = snapshot()
    stable_keys = ("head", "tree", "comparator_sha256", "frozen_sha256", "claims_sha256",
                   "scope_sha256", "live_source_sha256", "independent_source_sha256")
    source_state_stable = all(before[key] == after[key] for key in stable_keys)
    report = {
        "runner": str(Path(__file__).relative_to(ROOT)),
        "runner_sha256": sha(__file__),
        "command": "PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/c1-resumed/probe.py",
        "before": before,
        "after": after,
        "source_state_stable": source_state_stable,
        "count": {"cases": len(results), "source_invocations": len(results) * 2 + 1},
        "results": results,
        "scope_cwd_planted_control": control,
    }
    result_path = EVIDENCE / "focused-arms.json"
    dump(result_path, report)
    print(json.dumps({
        "result": str(result_path.relative_to(ROOT)),
        "runner_sha256": report["runner_sha256"],
        "before": before,
        "after": after,
        "source_state_stable": source_state_stable,
        "counts": report["count"],
        "results": {name: {source: {"exit": run_result["exit"],
                                     "reason": run_result["reason"],
                                     "stderr": run_result["stderr"]}
                          for source, run_result in values.items()}
                    for name, values in results.items()},
        "scope_cwd_planted_control": {"exit": control["exit"], "reason": control["reason"]},
    }, indent=2, sort_keys=True))
    return 0 if source_state_stable else 1


if __name__ == "__main__":
    raise SystemExit(main())
