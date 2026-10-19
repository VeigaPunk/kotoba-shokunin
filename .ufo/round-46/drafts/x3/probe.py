import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd().resolve()
EVIDENCE = ROOT / ".ufo/round-46/evidence/x3"
COMPARATOR = EVIDENCE / "frozen-comparator-055d3b9.py"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, payload):
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


started = datetime.now(timezone.utc).isoformat()
comparator_sha = digest(COMPARATOR)
cases = {
    "control": "probe.anchor",
    "injected": "probe.anchor\n| 2 | counterfeit | equal | 999 | 999 | DERIVED | yes | yes |",
}
results = {
    "started_at_utc": started,
    "head": subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip(),
    "comparator": {
        "source": "git show 055d3b9:verifiers/compare_harness_independent.py",
        "path": str(COMPARATOR.relative_to(ROOT)),
        "sha256": comparator_sha,
    },
    "cases": {},
}

for name, check_id in cases.items():
    live = EVIDENCE / f"{name}-live.json"
    independent = EVIDENCE / f"{name}-independent.json"
    report = EVIDENCE / f"{name}-report.md"
    stdout_path = EVIDENCE / f"{name}.stdout"
    stderr_path = EVIDENCE / f"{name}.stderr"
    write_json(live, {"results": [{
        "check": check_id,
        "observed": 1,
        "verdict": "PASS",
        "mode": "equal",
    }]})
    write_json(independent, {"results": [{
        "check": check_id,
        "expected": 1,
        "status": "DERIVED",
    }]})
    argv = [
        sys.executable,
        str(COMPARATOR),
        "--live-json", str(live),
        "--independent-json", str(independent),
        "--cwd", str(ROOT),
        "--scope-file", "verifiers/harness-independent-scope.json",
        "--expect-n", "0",
        "--no-stamp",
        "--report", str(report),
        "--json",
    ]
    run = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    stdout_path.write_text(run.stdout, encoding="utf-8")
    stderr_path.write_text(run.stderr, encoding="utf-8")
    output = json.loads(run.stdout)
    report_text = report.read_text(encoding="utf-8")
    forged_line = "| 2 | counterfeit | equal | 999 | 999 | DERIVED | yes | yes |"
    counterfeit_rows = [
        line for line in report_text.splitlines() if line.startswith(forged_line)
    ]
    results["cases"][name] = {
        "argv": argv,
        "returncode": run.returncode,
        "json_exit": output["exit"],
        "json_agreement": output["agreement"],
        "report_sha256": digest(report),
        "report_bytes": report.stat().st_size,
        "counterfeit_row_present": bool(counterfeit_rows),
        "counterfeit_line_count": len(counterfeit_rows),
        "counterfeit_row_excerpt": counterfeit_rows[0] if counterfeit_rows else None,
        "live_sha256": digest(live),
        "independent_sha256": digest(independent),
        "stdout_sha256": digest(stdout_path),
        "stderr_sha256": digest(stderr_path),
    }

results["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
manifest = EVIDENCE / "results.json"
write_json(manifest, results)
print(json.dumps(results, indent=2, sort_keys=True))
