import hashlib
import json
import pathlib
import subprocess
from datetime import datetime, timezone

repo = pathlib.Path(__file__).resolve().parents[4]
evidence = repo / ".ufo/round-44/evidence/p3"
source_paths = [
    "verifiers/verify_surfaces.py",
    "verifiers/fixtures/surfaces/strings-omp-newcallees.txt",
    "verifiers/surfaces-baseline.json",
    "corpus/knowledge/instruction-surface-census-round13.md",
    "verifiers/baseline.json",
    "verifiers/check_substrate_pins.py",
    "verifiers/check_assertion_floors.py",
    "verifiers/floors-registry.json",
]
commands = [
    ["python3", "verifiers/verify_surfaces.py"],
    ["python3", "verifiers/verify_surfaces.py", "--self-test"],
    ["python3", "verifiers/check_substrate_pins.py"],
    ["python3", "verifiers/check_substrate_pins.py", "--self-test"],
    ["python3", "verifiers/check_assertion_floors.py", "--repo", str(repo)],
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(*args):
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()

def source_hashes():
    return {path: sha(repo / path) for path in source_paths}

def binary_state():
    path = pathlib.Path("/home/vgpnk/.local/bin/omp")
    stat = path.stat()
    return {"path": str(path), "sha256": sha(path), "mtime_ns": stat.st_mtime_ns}

start_state = {"captured_at_utc": datetime.now(timezone.utc).isoformat(),
               "head": git("rev-parse", "HEAD"), "tree": git("rev-parse", "HEAD^{tree}"),
               "sources": source_hashes(), "binary": binary_state(),
               "status": git("status", "--short", "--untracked-files=all")}
results = []
for command in commands:
    started = datetime.now(timezone.utc).isoformat()
    before = source_hashes()
    proc = subprocess.run(command, cwd=repo, capture_output=True, text=True)
    ended = datetime.now(timezone.utc).isoformat()
    after = source_hashes()
    results.append({"command": command, "started_utc": started, "ended_utc": ended,
                    "exit_code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                    "stdout_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
                    "stderr_sha256": hashlib.sha256(proc.stderr.encode()).hexdigest(),
                    "source_sha256_before": before, "source_sha256_after": after,
                    "sources_stable": before == after})
end_state = {"captured_at_utc": datetime.now(timezone.utc).isoformat(),
             "head": git("rev-parse", "HEAD"), "tree": git("rev-parse", "HEAD^{tree}"),
             "sources": source_hashes(), "binary": binary_state(),
             "status": git("status", "--short", "--untracked-files=all")}
report = {"start_state": start_state, "results": results, "end_state": end_state}
out = evidence / "after-results.json"
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
summary = {"path": str(out.relative_to(repo)), "sha256": sha(out),
           "head": start_state["head"], "tree": start_state["tree"],
           "sources_stable_during_all_runs": all(r["sources_stable"] for r in results),
           "binary_stable": start_state["binary"] == end_state["binary"],
           "results": [{"command": r["command"], "exit_code": r["exit_code"],
                        "started_utc": r["started_utc"], "ended_utc": r["ended_utc"],
                        "stdout_sha256": r["stdout_sha256"], "stdout": r["stdout"],
                        "sources_stable": r["sources_stable"]} for r in results]}
print(json.dumps(summary, indent=2, sort_keys=True))
if not summary["sources_stable_during_all_runs"] or not summary["binary_stable"]:
    raise SystemExit(1)
if any(result["exit_code"] != 0 for result in results):
    raise SystemExit(1)
