#!/usr/bin/env python3
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
COMPARATOR = REPO / "verifiers/compare_harness_independent.py"
SOURCE_REF = "055d3b9:verifiers/compare_harness_independent.py"
PRIOR = REPO / ".ufo/round-46/evidence/H1-trust-boundary.json"
OUT = REPO / ".ufo/round-46/evidence/H1-trust-boundary-pinned-head.json"
WRAPPER = (
    "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
    "s=sys.stdin.buffer.read(); "
    "exec(compile(s,p,'exec'), {'__name__':'__main__','__file__':p})"
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()


def file_sha(path):
    return sha(path.read_bytes())


def main():
    started = datetime.now(timezone.utc).isoformat()
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    source = subprocess.check_output(["git", "show", SOURCE_REF], cwd=REPO)
    source_sha = sha(source)
    if head != "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae" or \
            tree != "e8dced184612a9738c5b8d244a0837fbd955a7da" or \
            source_sha != "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4":
        raise SystemExit("frozen HEAD/source pins differ from the registered baseline")

    prior = json.loads(PRIOR.read_text(encoding="utf-8"))
    cases = []
    for old in prior["cases"]:
        live_path = Path(old["command"][old["command"].index("--live-json") + 1])
        ind_path = Path(old["command"][old["command"].index("--independent-json") + 1])
        scope_path = Path(old["command"][old["command"].index("--scope-file") + 1])
        before = {"live": file_sha(live_path), "independent": file_sha(ind_path), "scope": file_sha(scope_path)}
        args = old["command"][old["command"].index("--cwd"):]
        command = [sys.executable, "-B", "-c", WRAPPER, str(COMPARATOR), *args]
        proc = subprocess.run(command, cwd=REPO, input=source, capture_output=True, timeout=300)
        after = {"live": file_sha(live_path), "independent": file_sha(ind_path), "scope": file_sha(scope_path)}
        try:
            report = json.loads(proc.stdout)
        except (ValueError, UnicodeDecodeError):
            report = None
        cases.append({
            "id": old["id"],
            "command": command,
            "exit": proc.returncode,
            "reason": report.get("reason") if isinstance(report, dict) else proc.stderr.decode(errors="replace"),
            "headline": report.get("headline") if isinstance(report, dict) else None,
            "agreement": report.get("agreement") if isinstance(report, dict) else None,
            "live_input_sha256": before["live"],
            "independent_input_sha256": before["independent"],
            "scope_sha256": before["scope"],
            "input_hashes_unchanged": before == after,
            "stdout_sha256": sha(proc.stdout),
            "stderr_sha256": sha(proc.stderr),
        })

    if git("rev-parse", "HEAD") != head or git("rev-parse", "HEAD^{tree}") != tree:
        raise SystemExit("HEAD/tree changed during replay")
    source_end = subprocess.check_output(["git", "show", SOURCE_REF], cwd=REPO)
    if sha(source_end) != source_sha:
        raise SystemExit("frozen Git blob changed during replay")
    if not all(case["input_hashes_unchanged"] for case in cases):
        raise SystemExit("a replay changed an input")

    result = {
        "schema": "kotoba.round46.h1.pinned-live-trust.v1",
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python3 -B .ufo/round-46/drafts/h1/replay-pinned-head.py",
        "target": {"source_ref": SOURCE_REF, "head": head, "head_tree": tree,
                   "comparator_sha256": source_sha,
                   "live_producer_sha256": prior["target"]["source_sha256_start"]["verifiers/verify_harness_claims.py"],
                   "independent_producer_sha256": prior["target"]["source_sha256_start"]["verifiers/verify_harness_independent.py"]},
        "captured_producer_inputs": prior["producer_payload_sha256"],
        "prior_observation_source_sha256": prior["target"]["source_sha256_start"]["verifiers/compare_harness_independent.py"],
        "replayed_input_artifacts": prior["case_inputs"],
        "cases": cases,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence": str(OUT.relative_to(REPO)), "evidence_sha256": file_sha(OUT),
                      "target": result["target"], "cases": cases}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
