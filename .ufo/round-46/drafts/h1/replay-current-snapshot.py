#!/usr/bin/env python3
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
COMPARATOR = REPO / "verifiers/compare_harness_independent.py"
LIVE_PRODUCER = REPO / "verifiers/verify_harness_claims.py"
IND_PRODUCER = REPO / "verifiers/verify_harness_independent.py"
SCOPE = REPO / "verifiers/harness-independent-scope.json"
LEGACY_LIVE = DRAFT / "live-base.json"
TARGET = "omp.elf.template_bytes"
WRAPPER = (
    "import sys; p=sys.argv[1]; sys.argv=[p]+sys.argv[2:]; "
    "s=sys.stdin.buffer.read(); "
    "exec(compile(s,p,'exec'), {'__name__':'__main__','__file__':p})"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    return digest(path.read_bytes())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()


def write_json(path, value):
    body = (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()
    path.write_bytes(body)
    return digest(body)


def live_target_record(payload):
    for channel in ("results", "rows", "checks"):
        rows = payload.get(channel) if isinstance(payload, dict) else None
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and row.get("check") == TARGET:
                    return row
    raise AssertionError("live target row missing")


def set_independent_target(payload, value):
    changed = []
    for channel in ("results", "rows", "checks"):
        rows = payload.get(channel) if isinstance(payload, dict) else None
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and row.get("check", row.get("id", row.get("name"))) == TARGET:
                    for key in ("expected", "expected_value", "re_derived", "value", "observed"):
                        if key in row:
                            row[key] = value
                            changed.append(f"{channel}.{key}")
        elif isinstance(rows, dict) and TARGET in rows:
            rows[TARGET] = value
            changed.append(f"{channel}[check]")
    for channel in ("expected", "expected_value", "re_derived", "observations"):
        values = payload.get(channel) if isinstance(payload, dict) else None
        if isinstance(values, dict) and TARGET in values:
            values[TARGET] = value
            changed.append(f"{channel}[check]")
    if not changed:
        raise AssertionError("independent target has no writable value aliases")
    return changed


def run_case(name, live_path, ind_path, comparator_source, comparator_sha, args):
    before = {"live": file_digest(live_path), "independent": file_digest(ind_path),
              "scope": file_digest(SCOPE)}
    command = [sys.executable, "-B", "-c", WRAPPER, str(COMPARATOR), *args,
               "--live-json", str(live_path), "--independent-json", str(ind_path)]
    proc = subprocess.run(command, cwd=REPO, input=comparator_source,
                          capture_output=True, timeout=300)
    after = {"live": file_digest(live_path), "independent": file_digest(ind_path),
             "scope": file_digest(SCOPE)}
    try:
        output = json.loads(proc.stdout)
    except (ValueError, UnicodeDecodeError):
        output = None
    return {
        "id": name,
        "command": command,
        "exit": proc.returncode,
        "reason": output.get("reason") if isinstance(output, dict)
        else proc.stderr.decode(errors="replace"),
        "headline": output.get("headline") if isinstance(output, dict) else None,
        "agreement": output.get("agreement") if isinstance(output, dict) else None,
        "comparator_sha256": comparator_sha,
        "inputs_before": before,
        "inputs_unchanged": before == after,
        "stdout_sha256": digest(proc.stdout),
        "stderr_sha256": digest(proc.stderr),
    }


def main():
    started = datetime.now(timezone.utc).isoformat()
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    comparator_source = COMPARATOR.read_bytes()
    comparator_sha = digest(comparator_source)
    comparator_snapshot = DRAFT / "current-comparator-snapshot.py"
    comparator_snapshot.write_bytes(comparator_source)
    source_pins = {str(path.relative_to(REPO)): file_digest(path)
                   for path in (LIVE_PRODUCER, IND_PRODUCER, SCOPE)}
    scope_sha = file_digest(SCOPE)

    live_path = DRAFT / "current-live-capture.json"
    independent_path = DRAFT / "current-independent-capture.json"
    producer_runs = {}
    for label, source_path, output_path in (
        ("live", LIVE_PRODUCER, live_path),
        ("independent", IND_PRODUCER, independent_path),
    ):
        proc = subprocess.run([sys.executable, "-B", str(source_path), "--json"],
                              cwd=REPO, capture_output=True, timeout=300)
        output_path.write_bytes(proc.stdout)
        producer_runs[label] = {
            "command": [sys.executable, "-B", str(source_path), "--json"],
            "exit": proc.returncode,
            "stdout_sha256": digest(proc.stdout),
            "stderr_sha256": digest(proc.stderr),
        }
        if proc.returncode != 0:
            raise SystemExit(f"{label} producer failed: {proc.stderr.decode(errors='replace')}")
    live_base = json.loads(live_path.read_bytes())
    independent_base = json.loads(independent_path.read_bytes())
    observed = live_target_record(live_base)["observed"]
    independent_row = next(row for row in independent_base.get("results", [])
                           if row.get("check") == TARGET)
    independent_value = next((independent_row[key] for key in
                               ("re_derived", "value", "expected", "expected_value", "observed")
                               if key in independent_row), None)
    if not (isinstance(observed, int) and not isinstance(observed, bool)
            and independent_value == observed):
        raise AssertionError(f"target control differs: live={observed!r} independent={independent_value!r}")

    args = ["--cwd", str(REPO), "--scope-file", str(SCOPE), "--expect-n", "28",
            "--no-stamp", "--json"]
    cases = []
    cases.append(run_case("current-producer-control", live_path, independent_path,
                          comparator_source, comparator_sha, args))
    cases.append(run_case("legacy-capture-without-current-mirrors", LEGACY_LIVE,
                          independent_path, comparator_source, comparator_sha, args))

    for name, mutation in (
        ("row-mode-disagrees-with-modes-map", "row-mode"),
        ("modes-map-disagrees-with-row", "mode-map"),
        ("row-verdict-disagrees-with-verdicts-map", "row-verdict"),
        ("verdicts-map-disagrees-with-row", "verdict-map"),
        ("summary-value-disagrees-with-row", "summary-value"),
        ("summary-path-does-not-point-to-row-value", "summary-path"),
    ):
        payload = copy.deepcopy(live_base)
        if mutation == "row-mode":
            live_target_record(payload)["mode"] = "positive"
        elif mutation == "mode-map":
            payload["modes"][TARGET] = "positive"
        elif mutation == "row-verdict":
            live_target_record(payload)["verdict"] = "DRIFT"
        elif mutation == "verdict-map":
            payload["verdicts"][TARGET] = "DRIFT"
        elif mutation == "summary-value":
            payload["observed"]["omp"]["template_bytes"] = observed + 1
        elif mutation == "summary-path":
            payload["summary_paths"][TARGET] = ["omp", "template_sha256"]
        path = DRAFT / f"current-{mutation}.json"
        write_json(path, payload)
        cases.append(run_case(name, path, independent_path, comparator_source,
                              comparator_sha, args))

    redirected_summary = copy.deepcopy(live_base)
    redirected_summary["observed"]["omp"]["template_bytes"] = observed + 1
    redirected_summary["observed"]["omp"]["caller_shadow"] = observed
    redirected_summary["summary_paths"][TARGET] = ["omp", "caller_shadow"]
    redirected_summary_path = DRAFT / "current-redirected-summary-path.json"
    write_json(redirected_summary_path, redirected_summary)
    cases.append(run_case("caller-redirects-summary-path-to-coherent-decoy",
                          redirected_summary_path, independent_path, comparator_source,
                          comparator_sha, args))

    coherent_live = copy.deepcopy(live_base)
    live_target_record(coherent_live)["mode"] = "positive"
    coherent_live["modes"][TARGET] = "positive"
    coherent_live_path = DRAFT / "current-coherent-positive-live.json"
    write_json(coherent_live_path, coherent_live)
    drift_independent = copy.deepcopy(independent_base)
    changed_independent = set_independent_target(drift_independent, observed + 1)
    drift_independent_path = DRAFT / "current-independent-plus-one.json"
    write_json(drift_independent_path, drift_independent)
    cases.append(run_case("coherently-rewritten-positive-mode-and-independent-plus-one",
                          coherent_live_path, drift_independent_path, comparator_source,
                          comparator_sha, args))

    current_pins = {str(path.relative_to(REPO)): file_digest(path)
                    for path in (COMPARATOR, LIVE_PRODUCER, IND_PRODUCER, SCOPE)}
    if current_pins.get("verifiers/compare_harness_independent.py") != comparator_sha:
        raise SystemExit("comparator changed during snapshot replay")
    if {key: current_pins[key] for key in source_pins} != source_pins:
        raise SystemExit("producer or scope source changed during snapshot replay")
    if git("rev-parse", "HEAD") != head or git("rev-parse", "HEAD^{tree}") != tree:
        raise SystemExit("HEAD/tree changed during snapshot replay")
    if not all(case["inputs_unchanged"] for case in cases):
        raise SystemExit("a comparison changed an input")

    result = {
        "schema": "kotoba.round46.h1.current-snapshot.v1",
        "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": "python3 -B .ufo/round-46/drafts/h1/replay-current-snapshot.py",
        "target": {"head": head, "head_tree": tree, "comparator_sha256": comparator_sha,
                   "comparator_snapshot": str(comparator_snapshot.relative_to(REPO)),
                   "producer_source_sha256": source_pins, "scope_sha256": scope_sha,
                   "source_pins_unchanged": True},
        "producer_runs": producer_runs,
        "producer_payload_sha256": {"live": file_digest(live_path),
                                    "independent": file_digest(independent_path)},
        "legacy_live_payload_sha256": file_digest(LEGACY_LIVE),
        "target_check": TARGET,
        "target_values": {"observed": observed, "independent_control": independent_value,
                          "independent_plus_one": observed + 1},
        "independent_changed_value_aliases": changed_independent,
        "cases": cases,
    }
    output = REPO / ".ufo/round-46/evidence/H1-trust-boundary-current-snapshot.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence": str(output.relative_to(REPO)),
                      "evidence_sha256": file_digest(output),
                      "target": result["target"], "producer_runs": producer_runs,
                      "target_values": result["target_values"], "cases": cases},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
