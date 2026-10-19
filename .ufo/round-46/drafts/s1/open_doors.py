#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRIVER = ROOT / "verifiers/compare_harness_independent.py"
EVIDENCE = ROOT / ".ufo/round-46/evidence/s1"
OUTPUT = EVIDENCE / "open-doors.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return sha(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True).stdout.decode().strip()


def run(source, source_sha, name, live, independent):
    live = Path(live).resolve()
    independent = Path(independent).resolve()
    scope = (ROOT / "verifiers/harness-independent-scope.json").resolve()
    inputs = {"live": file_sha(live), "independent": file_sha(independent),
              "scope": file_sha(scope)}
    args = ["--live-json", str(live), "--independent-json", str(independent),
            "--expect-n", "28", "--cwd", str(ROOT), "--scope-file", str(scope),
            "--no-stamp", "--json"]
    wrapper = ("import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
               "s=sys.stdin.read(); exec(compile(s,p,'exec'), "
               "{'__name__':'__main__','__file__':p})")
    command = [sys.executable, "-c", wrapper, str(DRIVER), *args]
    proc = subprocess.run(command, cwd=ROOT, input=source.decode("utf-8"),
                          capture_output=True, text=True, timeout=120)
    try:
        result = json.loads(proc.stdout)
        reason = result.get("reason", "")
        headline = result.get("headline")
    except (ValueError, TypeError):
        result = None
        reason = (proc.stderr or proc.stdout).strip()
        headline = None
    after = {"live": file_sha(live), "independent": file_sha(independent),
             "scope": file_sha(scope)}
    return {
        "id": name,
        "source_sha256": source_sha,
        "argv": args,
        "inputs_sha256_before": inputs,
        "inputs_sha256_after": after,
        "inputs_unchanged": inputs == after,
        "exit": proc.returncode,
        "reason": reason,
        "headline": headline,
        "stdout_sha256": sha(proc.stdout.encode()),
        "stderr_sha256": sha(proc.stderr.encode()),
    }


def main():
    started = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    current_bytes = DRIVER.read_bytes()
    current_sha = sha(current_bytes)
    frozen_bytes = subprocess.run(
        ["git", "-C", str(ROOT), "show",
         "055d3b9:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    frozen_sha = sha(frozen_bytes)
    h11 = ROOT / ".ufo/round-45/evidence/h11/census-inputs"
    c2 = ROOT / ".ufo/round-45/evidence/c2"
    h06 = ROOT / ".ufo/round-45/evidence/h06"
    cases = [
        ("duplicate_top_level_results_member", c2 / "fresh-live.json",
         c2 / "hunt-duplicate_top_level_results_member.json"),
        ("duplicate_record_rederived_member", c2 / "fresh-live.json",
         c2 / "hunt-duplicate_record_rederived_member.json"),
    ]
    live_ids = [
        "live-mode-positive-masks-independent-drift",
        "live-mode-split-across-row-channels",
        "live-top-level-observed-summary-divergence",
        "live-verdict-shadow-in-row-channel",
    ]
    cases.extend((name, h11 / f"live-arm-{name}.json", h11 / f"arm-{name}.json")
                 for name in live_ids)
    probe_ids = [
        "scoped-out-reason-and-evidence-drift",
        "record-probe-fallback-reads-results-only",
        "record-probe-shadowed-by-top-level-map",
        "unmatched-extra-scoped-out-probe",
    ]
    cases.extend((name, h06 / "fresh-live.json", h11 / f"arm-{name}.json")
                 for name in probe_ids)
    cases.extend([
        ("fresh-fabricated-reason-evidence", h06 / "fresh-live.json",
         h06 / "fresh-fabricated-reason-evidence-independent.json"),
        ("fresh-payload-target-unconstrained-by-scope", h06 / "fresh-live.json",
         h06 / "fresh-uncommitted-probe-target-independent.json"),
    ])
    rows = []
    for source_name, source_bytes, source_hash in (
            ("frozen-055d3b9", frozen_bytes, frozen_sha),
            ("worktree-candidate", current_bytes, current_sha)):
        for name, live, independent in cases:
            row = run(source_bytes, source_hash, name, live, independent)
            row["source"] = source_name
            rows.append(row)
    current_after_sha = file_sha(DRIVER)
    result = {
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
        "head": head,
        "head_tree": tree,
        "frozen_source": {"command": "git show 055d3b9:verifiers/compare_harness_independent.py",
                          "sha256": frozen_sha},
        "candidate_source": {"path": "verifiers/compare_harness_independent.py",
                             "sha256_at_start": current_sha,
                             "sha256_at_end": current_after_sha,
                             "stable_during_run": current_sha == current_after_sha},
        "case_count": len(cases),
        "runs": rows,
    }
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                      encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT.relative_to(ROOT)),
                      "case_count": len(cases), "source_sha256": current_sha,
                      "source_stable": current_sha == current_after_sha,
                      "head": head, "tree": tree}, sort_keys=True))


if __name__ == "__main__":
    main()
