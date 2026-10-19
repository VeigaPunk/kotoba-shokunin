import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
LIVE_PATH = DRAFT / "live.json"
IND_PATH = DRAFT / "independent.json"
SCOPE_PATH = ROOT / "verifiers/harness-independent-scope.json"
COMPARATORS = {
    "frozen-6fbbff5": DRAFT / "compare-6fbbff5.py",
    "frozen-worktree-a2bf": DRAFT / "compare-worktree-a2bf.py",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def dump_input(name, payload):
    path = DRAFT / f"input-{name}.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def main():
    live = json.loads(LIVE_PATH.read_text(encoding="utf-8"))
    original = json.loads(IND_PATH.read_text(encoding="utf-8"))
    live_values = {r["check"]: r["observed"] for r in live["results"]}
    committed = set(json.loads(SCOPE_PATH.read_text(encoding="utf-8"))["scope_out"])

    rows_only = copy.deepcopy(original)
    rows_only.pop("results", None)

    expected_only = copy.deepcopy(rows_only)
    for record in expected_only["rows"]:
        cid = record["check"]
        record["expected"] = None if cid in committed else live_values[cid]
        for key in ("re_derived", "expected_value", "value", "observed"):
            record.pop(key, None)
    expected_only["checks"] = {
        cid: (None if cid in committed else live_values[cid])
        for cid in expected_only["checks"]
    }

    scoped_value = copy.deepcopy(rows_only)
    scoped_id = "omp.catalogue.found"
    scoped_live_value = live_values[scoped_id]
    for record in scoped_value["rows"]:
        if record["check"] == scoped_id:
            record["expected"] = scoped_live_value
            for key in ("re_derived", "expected_value", "value", "observed"):
                record.pop(key, None)
    scoped_value["checks"][scoped_id] = scoped_live_value

    extra_id = "attacker.extra.record_map"
    extra = copy.deepcopy(rows_only)
    extra["rows"].append({"check": extra_id, "expected": 1, "status": "DERIVED"})
    extra["checks"][extra_id] = 1

    nested_expected = copy.deepcopy(original)
    nested_expected.pop("results", None)
    nested_expected["expected"] = copy.deepcopy(nested_expected["checks"])

    map_missing = copy.deepcopy(rows_only)
    map_missing["checks"][extra_id] = 1

    cases = [
        ("honest-control-results-rows-checks", original),
        ("honest-control-rows-checks", rows_only),
        ("expected-only-records-rows-plus-checks", expected_only),
        ("scoped-out-value-record-plus-checks-map", scoped_value),
        ("extra-id-record-plus-checks-map", extra),
        ("record-plus-nested-expected-map", nested_expected),
        ("rows-plus-checks-map-membership-split", map_missing),
    ]

    report = {
        "started_at": stamp(),
        "root": str(ROOT),
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
                                capture_output=True, text=True).stdout.strip(),
        "tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, check=True,
                                 capture_output=True, text=True).stdout.strip(),
        "probe_sha256": sha(Path(__file__)),
        "live_input": {"path": str(LIVE_PATH.relative_to(ROOT)), "bytes": LIVE_PATH.stat().st_size,
                       "sha256": sha(LIVE_PATH)},
        "independent_input": {"path": str(IND_PATH.relative_to(ROOT)),
                              "bytes": IND_PATH.stat().st_size, "sha256": sha(IND_PATH)},
        "scope_file": {"path": str(SCOPE_PATH.relative_to(ROOT)), "sha256": sha(SCOPE_PATH)},
        "committed_scoped_ids": sorted(committed),
        "comparators": {name: {"path": str(path.relative_to(ROOT)), "sha256": sha(path)}
                        for name, path in COMPARATORS.items()},
        "runs": [],
    }

    for case_name, payload in cases:
        input_path = dump_input(case_name, payload)
        input_record = {"case": case_name, "path": str(input_path.relative_to(ROOT)),
                        "bytes": input_path.stat().st_size, "sha256": sha(input_path)}
        for comparator_name, comparator in COMPARATORS.items():
            argv = [sys.executable, str(comparator), "--live-json", str(LIVE_PATH),
                    "--independent-json", str(input_path), "--expect-n", "28",
                    "--cwd", str(ROOT), "--scope-file", str(SCOPE_PATH),
                    "--no-stamp", "--json"]
            started = stamp()
            proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=120)
            ended = stamp()
            try:
                parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
            except ValueError:
                parsed = None
            run = {
                **input_record,
                "comparator": comparator_name,
                "comparator_sha256": sha(comparator),
                "started_at": started,
                "ended_at": ended,
                "argv": argv,
                "exit": proc.returncode,
                "stdout_bytes": len(proc.stdout.encode("utf-8")),
                "stdout_sha256": hashlib.sha256(proc.stdout.encode("utf-8")).hexdigest(),
                "stderr_bytes": len(proc.stderr.encode("utf-8")),
                "stderr_sha256": hashlib.sha256(proc.stderr.encode("utf-8")).hexdigest(),
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            }
            if parsed is not None:
                run["headline"] = parsed.get("headline")
                run["agreement"] = parsed.get("agreement")
                run["reason"] = parsed.get("reason")
            report["runs"].append(run)

    report["ended_at"] = stamp()
    output = DRAFT / "record-map-probe-results.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "report": str(output.relative_to(ROOT)),
        "report_sha256": sha(output),
        "probe_sha256": report["probe_sha256"],
        "head": report["head"],
        "tree": report["tree"],
        "live_sha256": report["live_input"]["sha256"],
        "independent_sha256": report["independent_input"]["sha256"],
        "runs": [{"case": r["case"], "comparator": r["comparator"], "exit": r["exit"],
                  "agreement": r.get("agreement"), "error": r["stderr"].strip()}
                 for r in report["runs"]],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
