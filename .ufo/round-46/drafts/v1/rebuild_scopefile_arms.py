#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
LIVE = DRAFT / "fresh-live.json"
LIVE_SCOPE = DRAFT / "scope-live-projection.json"
INDEPENDENT = DRAFT / "fresh-independent.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
TARGET = "omp.offered.skills"


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return digest_bytes(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_probe_module(path):
    spec = importlib.util.spec_from_file_location("scope_probe_comparator", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_scope_files(carrier, module):
    scope_doc = json.loads(SCOPE.read_text(encoding="utf-8"))
    probe = {"kind": "rule-spread-census", "target": str(carrier.resolve())}
    scope_doc["probe_contract"]["target"] = probe["target"]
    probe["observable"] = module.recompute_probe(probe)["observable"]
    if probe["observable"].get("distinct_totals") != [1, 4]:
        raise RuntimeError(f"planted carrier did not produce distinct totals [1, 4]: {probe['observable']}")
    scope_doc["scope_out"][TARGET] = {
        "kind": "rule-in-author-scope",
        "reason": "V1 planted-cwd path-resolution probe; null value and recomputed structural evidence",
    }
    return scope_doc, probe


def build_payload(probe):
    payload = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
    reason = "V1 planted-cwd path-resolution probe; null value and recomputed structural evidence"
    for cid in payload["scoped_out"]:
        payload["scoped_out_probes"][cid] = probe
        for channel in ("results", "rows"):
            for record in payload[channel]:
                if record.get("check") == cid:
                    record["probe"] = probe
    matches = 0
    for record in payload["results"]:
        if record.get("check") == TARGET:
            record.update({"re_derived": None, "value": None, "status": "SCOPED_OUT",
                           "evidence": "SCOPED_OUT: " + reason, "probe": probe})
            matches += 1
    for record in payload["rows"]:
        if record.get("check") == TARGET:
            record.update({"value": None, "status": "SCOPED_OUT",
                           "evidence": "SCOPED_OUT: " + reason, "probe": probe})
            matches += 1
    if TARGET not in payload["checks"]:
        raise RuntimeError(f"fresh independent capture has no {TARGET} check")
    payload["checks"][TARGET] = None
    matches += 1
    if matches != 3:
        raise RuntimeError(f"expected to update three row channels, updated {matches}")
    payload["scoped_out"][TARGET] = reason
    payload["scoped_out_probes"][TARGET] = probe
    return payload


def run_arm(driver, label, process_cwd, scope_arg, live_path, independent_path,
            receipt_path, expected_scope):
    process_cwd = Path(process_cwd).resolve()
    scope_arg = str(scope_arg)
    argv = [
        sys.executable, str(driver),
        "--live-json", str(live_path.resolve()),
        "--independent-json", str(independent_path.resolve()),
        "--expect-n", "28",
        "--cwd", str(ROOT),
        "--scope-file", scope_arg,
        "--no-stamp", "--json",
        "--receipt", str(receipt_path.resolve()),
    ]
    receipt_path.unlink(missing_ok=True)
    proc = subprocess.run(argv, cwd=str(process_cwd), capture_output=True,
                          text=True, timeout=300)
    receipt = None
    if receipt_path.is_file():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    enforced_path = Path(scope_arg)
    if not enforced_path.is_absolute():
        enforced_path = process_cwd / enforced_path
    enforced_path = enforced_path.resolve()
    enforced_sha = digest(enforced_path)
    receipt_path_field = receipt.get("scope_file", {}).get("path") if receipt else None
    receipt_sha = receipt.get("scope_file", {}).get("sha256") if receipt else None
    recorded_path = None
    if receipt_path_field:
        path_value = Path(receipt_path_field)
        if not path_value.is_absolute():
            path_value = Path(receipt.get("driver_cwd", "")) / path_value
        recorded_path = path_value.resolve()
    path_matches = recorded_path == enforced_path if recorded_path is not None else False
    digest_matches = receipt_sha == enforced_sha
    report = None
    try:
        report = json.loads(proc.stdout) if proc.stdout.strip() else None
    except ValueError:
        report = None
    if label == "planted-cwd-relative":
        acceptable = ((proc.returncode == 2 and "laundering" in proc.stderr.lower())
                      or (proc.returncode == 0 and path_matches and digest_matches))
    elif label == "honest-cwd-relative-control":
        acceptable = proc.returncode == 2 and "laundering" in proc.stderr.lower()
    else:
        acceptable = (proc.returncode == 0 and path_matches and digest_matches
                      and report is not None
                      and report.get("headline", {}).get("n") == 23
                      and report.get("headline", {}).get("total") == 23)
    return {
        "arm": label,
        "argv": argv,
        "process_cwd": str(process_cwd),
        "scope_argument": scope_arg,
        "expected_scope_path": str(expected_scope.resolve()),
        "expected_scope_sha256": digest(expected_scope),
        "enforced_scope_path": str(enforced_path),
        "enforced_scope_sha256": enforced_sha,
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "receipt_path": str(receipt_path.resolve()),
        "receipt_sha256": digest(receipt_path) if receipt_path.is_file() else None,
        "receipt": receipt,
        "receipt_resolved_scope_path": str(recorded_path) if recorded_path else None,
        "receipt_scope_sha256": receipt_sha,
        "receipt_path_matches_enforced": path_matches,
        "receipt_digest_matches_enforced": digest_matches,
        "receipt_attests_enforced_file": path_matches and digest_matches,
        "headline": report.get("headline") if report else None,
        "agreement": report.get("agreement") if report else None,
        "acceptable_for_arm": acceptable,
    }


def main():
    if not LIVE.is_file() or not INDEPENDENT.is_file():
        raise RuntimeError("fresh producer captures are missing")
    live_payload = json.loads(LIVE.read_text(encoding="utf-8"))
    independent_payload = json.loads(INDEPENDENT.read_text(encoding="utf-8"))
    if len(live_payload.get("results", [])) != 28 or len(independent_payload.get("results", [])) != 28:
        raise RuntimeError("fresh captures do not each carry the expected 28 result rows")

    start = {
        "at_utc": stamp(),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "comparator_worktree_sha256": digest(COMPARATOR),
        "scope_sha256": digest(SCOPE),
        "live_capture_sha256": digest(LIVE),
        "independent_capture_sha256": digest(INDEPENDENT),
        "live_instrument_sha256": digest(ROOT / "verifiers/verify_harness_claims.py"),
        "independent_instrument_sha256": digest(ROOT / "verifiers/verify_harness_independent.py"),
    }
    frozen = subprocess.run(
        ["git", "-C", str(ROOT), "show", "055d3b9:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True,
    ).stdout
    frozen_path = DRAFT / "compare-frozen-055d3b9.py"
    frozen_path.write_bytes(frozen)
    candidate = COMPARATOR.read_bytes()
    candidate_path = DRAFT / "compare-candidate-at-start.py"
    candidate_path.write_bytes(candidate)
    planted_cwd = DRAFT / "planted-cwd"
    planted_scope_path = planted_cwd / "verifiers/harness-independent-scope.json"
    planted_scope_path.parent.mkdir(parents=True, exist_ok=True)
    carrier = DRAFT / "carrier"
    carrier.mkdir(exist_ok=True)
    (carrier / "a.jsonl").write_text(
        '{"stamp":"2026-01-01T00:00:00.000Z","text":"<skills>\\n- a\\n</skills>"}\n',
        encoding="utf-8",
    )
    (carrier / "b.jsonl").write_text(
        '{"stamp":"2026-02-02T00:00:00.000Z","text":"<skills>\\n- a\\n- b\\n- c\\n- d\\n</skills>"}\n',
        encoding="utf-8",
    )
    os.utime(carrier / "a.jsonl", (1700000000, 1700000000))
    os.utime(carrier / "b.jsonl", (1800000000, 1800000000))
    probe_module = load_probe_module(candidate_path)
    scope_doc, probe = make_scope_files(carrier, probe_module)
    superset_scope = DRAFT / "superset-scope.json"
    write_json(superset_scope, scope_doc)
    write_json(planted_scope_path, scope_doc)
    attack_path = DRAFT / "planted-scope-independent.json"
    write_json(attack_path, build_payload(probe))

    variants = {
        "frozen-055d3b9": frozen_path,
        "candidate-at-start": candidate_path,
    }
    arm_definitions = [
        ("planted-cwd-relative", planted_cwd, "verifiers/harness-independent-scope.json", planted_scope_path),
        ("honest-cwd-relative-control", ROOT, "verifiers/harness-independent-scope.json", SCOPE),
        ("superset-scope-relative-control", ROOT,
         str(superset_scope.relative_to(ROOT)), superset_scope),
        ("absolute-planted-path", planted_cwd, str(planted_scope_path.resolve()), planted_scope_path),
    ]
    arms = []
    for variant, driver in variants.items():
        for arm, process_cwd, scope_arg, expected_scope in arm_definitions:
            receipt_path = DRAFT / f"{variant}-{arm}-receipt.json"
            result = run_arm(
                driver, arm, process_cwd, scope_arg, LIVE, attack_path,
                receipt_path, expected_scope,
            )
            result["comparator_variant"] = variant
            result["comparator_sha256"] = digest(driver)
            if arm == "planted-cwd-relative" and variant == "frozen-055d3b9":
                result["expected_outcome_met"] = (
                    result["exit"] == 0
                    and not result["receipt_attests_enforced_file"]
                    and result["headline"] is not None
                    and result["headline"].get("n") == 23
                    and result["headline"].get("total") == 23
                )
            else:
                result["expected_outcome_met"] = result["acceptable_for_arm"]
            arms.append(result)

    honest_receipt_path = DRAFT / "honest-live-join-receipt.json"
    honest_receipt_path.unlink(missing_ok=True)
    honest_argv = [
        sys.executable, str(candidate_path),
        "--expect-n", "28", "--cwd", str(ROOT),
        "--scope-file", "verifiers/harness-independent-scope.json",
        "--no-stamp", "--json", "--receipt", str(honest_receipt_path.resolve()),
    ]
    honest_proc = subprocess.run(honest_argv, cwd=str(ROOT), capture_output=True,
                                  text=True, timeout=600)
    honest_report = json.loads(honest_proc.stdout) if honest_proc.stdout.strip() else None
    honest_receipt = (json.loads(honest_receipt_path.read_text(encoding="utf-8"))
                      if honest_receipt_path.is_file() else None)
    honest = {
        "argv": honest_argv,
        "process_cwd": str(ROOT),
        "exit": honest_proc.returncode,
        "stdout": honest_proc.stdout,
        "stderr": honest_proc.stderr,
        "report": honest_report,
        "receipt": honest_receipt,
        "receipt_sha256": digest(honest_receipt_path) if honest_receipt_path.is_file() else None,
        "passed_24_of_24": bool(
            honest_proc.returncode == 0 and honest_report
            and honest_report.get("headline", {}).get("n") == 24
            and honest_report.get("headline", {}).get("total") == 24
            and honest_report.get("agreement", {}).get("n_disagree") == 0
            and honest_report.get("agreement", {}).get("n_uncovered") == 0
            and honest_report.get("agreement", {}).get("n_unknown") == 0
        ),
    }
    end = {
        "at_utc": stamp(),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "comparator_worktree_sha256": digest(COMPARATOR),
        "scope_sha256": digest(SCOPE),
        "source_and_tree_stable": (
            start["head"] == git("rev-parse", "HEAD")
            and start["tree"] == git("rev-parse", "HEAD^{tree}")
            and start["comparator_worktree_sha256"] == digest(COMPARATOR)
            and start["scope_sha256"] == digest(SCOPE)
        ),
    }
    result_doc = {
        "generated_at_utc": stamp(),
        "task": "Round 46 V1 C1 scope-file cwd resolution verification",
        "pinned_frozen_source": {
            "git_show": "055d3b9:verifiers/compare_harness_independent.py",
            "sha256": digest(frozen_path),
            "candidate_byte_identical": digest(frozen_path) == digest(candidate_path),
        },
        "candidate_snapshot": {
            "path": str(candidate_path.relative_to(ROOT)),
            "sha256": digest(candidate_path),
            "source_worktree_path": str(COMPARATOR.relative_to(ROOT)),
        },
        "capture_commands": [
            "PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_claims.py --json",
            "PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_independent.py --json",
        ],
        "inputs": {
            "live": {"path": str(LIVE.relative_to(ROOT)), "sha256": digest(LIVE), "rows": len(live_payload["results"])},
            "independent": {"path": str(INDEPENDENT.relative_to(ROOT)), "sha256": digest(INDEPENDENT), "rows": len(independent_payload["results"])},
            "attack_independent": {"path": str(attack_path.relative_to(ROOT)), "sha256": digest(attack_path)},
            "official_scope": {"path": str(SCOPE.relative_to(ROOT)), "sha256": digest(SCOPE), "ids": sorted(json.loads(SCOPE.read_text(encoding="utf-8"))["scope_out"])},
            "superset_scope": {"path": str(superset_scope.relative_to(ROOT)), "sha256": digest(superset_scope), "ids": sorted(scope_doc["scope_out"])},
            "carrier": {"path": str(carrier.relative_to(ROOT)), "files": {p.name: digest(p) for p in sorted(carrier.glob("*.jsonl"))}, "probe": probe},
        },
        "start": start,
        "end": end,
        "arms": arms,
        "honest_live_join": honest,
        "summary": {
            "arm_count": len(arms),
            "expected_arm_outcome_count": sum(1 for arm in arms if arm["expected_outcome_met"]),
            "all_expected_arm_outcomes": all(arm["expected_outcome_met"] for arm in arms),
            "honest_24_of_24": honest["passed_24_of_24"],
            "baseline_planted_attack_reproduced": next(a["expected_outcome_met"] for a in arms if a["comparator_variant"] == "frozen-055d3b9" and a["arm"] == "planted-cwd-relative"),
            "candidate_planted_path_fail_closed": next(a["exit"] == 2 and "laundering" in a["stderr"].lower() for a in arms if a["comparator_variant"] == "candidate-at-start" and a["arm"] == "planted-cwd-relative"),
            "candidate_planted_relative_receipt_written": next(a["receipt"] is not None for a in arms if a["comparator_variant"] == "candidate-at-start" and a["arm"] == "planted-cwd-relative"),
        },
    }
    output = DRAFT / "scopefile-arm-results.json"
    write_json(output, result_doc)
    print(json.dumps({
        "result": str(output.relative_to(ROOT)),
        "result_sha256": digest(output),
        "candidate_sha256": digest(candidate_path),
        "frozen_sha256": digest(frozen_path),
        "source_and_tree_stable": end["source_and_tree_stable"],
        "summary": result_doc["summary"],
        "arms": [{"variant": a["comparator_variant"], "arm": a["arm"], "exit": a["exit"],
                  "receipt_attests_enforced": a["receipt_attests_enforced_file"],
                  "expected_outcome_met": a["expected_outcome_met"]} for a in arms],
        "honest": {"exit": honest_proc.returncode,
                   "headline": honest_report.get("headline") if honest_report else None,
                   "agreement": honest_report.get("agreement") if honest_report else None,
                   "passed_24_of_24": honest["passed_24_of_24"]},
    }, indent=2, sort_keys=True))
    if not end["source_and_tree_stable"]:
        raise SystemExit("source/tree changed during measurement")
    if not honest["passed_24_of_24"]:
        raise SystemExit("honest 24/24 join did not pass")
    if any(not arm["expected_outcome_met"] for arm in arms):
        raise SystemExit("one or more scope-file arms missed its before/after outcome")


if __name__ == "__main__":
    main()
