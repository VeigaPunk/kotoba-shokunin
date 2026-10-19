#!/usr/bin/env python3
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd().resolve()
EVIDENCE = ROOT / ".ufo/round-46/evidence/g1/final5"
DRAFTS = ROOT / ".ufo/round-46/drafts/g1"
EVIDENCE.mkdir(parents=True, exist_ok=True)
DRAFTS.mkdir(parents=True, exist_ok=True)


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_value(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()


def sources():
    paths = {ROOT / name for name in ("LOG.md", "SCORECARD.md", "SKILL.md", ".ufo/round-46/claims.json", "corpus/knowledge/harness-independent-round41-census.md")}
    for root in (ROOT / "verifiers", ROOT / "corpus"):
        if root.exists():
            paths.update(path for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
    return {str(path.relative_to(ROOT)): digest(path) for path in sorted(paths) if path.is_file()}


def snapshot():
    return {
        "at_utc": utc_now(),
        "head": git_value("rev-parse", "HEAD"),
        "tree": git_value("rev-parse", "HEAD^{tree}"),
        "source_sha256": sources(),
    }


runs = []
started = utc_now()


def run(name, argv, stdout_rel, stderr_rel):
    before = snapshot()
    start = utc_now()
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(argv, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = utc_now()
    stdout_path = ROOT / stdout_rel
    stderr_path = ROOT / stderr_rel
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)
    stdout_path.write_bytes(result.stdout)
    stderr_path.write_bytes(result.stderr)
    after = snapshot()
    rec = {
        "name": name,
        "argv": argv,
        "cwd": str(ROOT),
        "started_utc": start,
        "ended_utc": end,
        "exit_code": result.returncode,
        "stdout_path": str(stdout_path.relative_to(ROOT)),
        "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
        "stderr_path": str(stderr_path.relative_to(ROOT)),
        "stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
        "head_before": before["head"],
        "head_after": after["head"],
        "tree_before": before["tree"],
        "tree_after": after["tree"],
        "source_sha256_before": before["source_sha256"],
        "source_sha256_after": after["source_sha256"],
        "sources_stable": before["source_sha256"] == after["source_sha256"] and before["head"] == after["head"] and before["tree"] == after["tree"],
    }
    runs.append(rec)
    print(f"{name}: exit={result.returncode} stable={rec['sources_stable']} stdout_sha256={rec['stdout_sha256']}", flush=True)
    return rec


start_snapshot = snapshot()
live_json = DRAFTS / "live-final5.json"
ind_json = DRAFTS / "independent-final5.json"
base = "verifiers/"
run("live-harness-claims", ["python3", base + "verify_harness_claims.py", "--json"], str(live_json.relative_to(ROOT)), ".ufo/round-46/evidence/g1/final5/live-harness-claims.stderr")
run("live-harness-independent", ["python3", base + "verify_harness_independent.py", "--json"], str(ind_json.relative_to(ROOT)), ".ufo/round-46/evidence/g1/final5/live-harness-independent.stderr")
run("live-corpus-integrity", ["python3", base + "verify_corpus_integrity.py", "--json"], ".ufo/round-46/evidence/g1/final5/corpus-integrity.json", ".ufo/round-46/evidence/g1/final5/live-corpus-integrity.stderr")
run("live-corpus-independent", ["python3", base + "verify_corpus_independent.py", "--json"], ".ufo/round-46/evidence/g1/final5/corpus-independent.json", ".ufo/round-46/evidence/g1/final5/live-corpus-independent.stderr")
run("live-surfaces", ["python3", base + "verify_surfaces.py", "--json"], ".ufo/round-46/evidence/g1/final5/surfaces.json", ".ufo/round-46/evidence/g1/final5/live-surfaces.stderr")
run("live-checklist", ["python3", base + "verify_skill_checklist.py", "--json"], ".ufo/round-46/evidence/g1/final5/checklist.json", ".ufo/round-46/evidence/g1/final5/live-checklist.stderr")
run("live-substrate-pins", ["python3", base + "check_substrate_pins.py", "--json"], ".ufo/round-46/evidence/g1/final5/substrate-pins.json", ".ufo/round-46/evidence/g1/final5/live-substrate-pins.stderr")
run("live-comparator-join", ["python3", base + "compare_harness_independent.py", "--live-json", str(live_json), "--independent-json", str(ind_json), "--cwd", str(ROOT), "--scope-file", "verifiers/harness-independent-scope.json", "--expect-n", "28", "--no-stamp", "--json", "--receipt", str(EVIDENCE / "live-join.receipt.json")], ".ufo/round-46/evidence/g1/final5/live-join.json", ".ufo/round-46/evidence/g1/final5/live-comparator-join.stderr")
run("live-assertion-floors", ["python3", base + "check_assertion_floors.py", "--repo", str(ROOT)], ".ufo/round-46/evidence/g1/final5/assertion-floors.stdout", ".ufo/round-46/evidence/g1/final5/live-assertion-floors.stderr")

for name, script in (
    ("harness-claims", "verify_harness_claims.py"),
    ("corpus-integrity", "verify_corpus_integrity.py"),
    ("corpus-independent", "verify_corpus_independent.py"),
    ("surfaces", "verify_surfaces.py"),
    ("checklist", "verify_skill_checklist.py"),
    ("substrate-pins", "check_substrate_pins.py"),
    ("harness-independent", "verify_harness_independent.py"),
    ("comparator", "compare_harness_independent.py"),
    ("assertion-floors", "check_assertion_floors.py"),
):
    run("selftest-" + name, ["python3", base + script, "--self-test"], f".ufo/round-46/evidence/g1/final5/selftest-{name}.stdout", f".ufo/round-46/evidence/g1/final5/selftest-{name}.stderr")

end_snapshot = snapshot()
manifest = {
    "started_utc": started,
    "ended_utc": utc_now(),
    "pre_snapshot": start_snapshot,
    "post_snapshot": end_snapshot,
    "runs": runs,
    "all_sources_stable": all(r["sources_stable"] for r in runs),
}
manifest_path = EVIDENCE / "gate-battery.json"
manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"manifest={manifest_path.relative_to(ROOT)} sha256={digest(manifest_path)} all_sources_stable={manifest['all_sources_stable']}")
