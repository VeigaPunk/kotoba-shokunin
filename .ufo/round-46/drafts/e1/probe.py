#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = ROOT / ".ufo/round-46/drafts/e1"
EVIDENCE = ROOT / ".ufo/round-46/evidence"
COMPARATOR = DRAFT / "compare-055d3b9.py"
OFFICIAL_SCOPE = ROOT / "verifiers/harness-independent-scope.json"
LIVE_SOURCE = ROOT / ".ufo/round-41/evidence/live-b1be35f.json"
IND_SOURCE = ROOT / ".ufo/round-41/evidence/independent-b1be35f.json"
EXPECTED = {
    "head": "055d3b9a3f7eb28d13452a0d26853ef4feabf2ae",
    "tree": "e8dced184612a9738c5b8d244a0837fbd955a7da",
    "comparator": "1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4",
    "scope": "fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a",
    "live": "0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341",
    "independent": "eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_value(*args):
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def tree_state():
    return {"head": git_value("rev-parse", "HEAD"), "tree": git_value("rev-parse", "HEAD^{tree}")}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def current_pins():
    pins = {
        "head": git_value("rev-parse", "HEAD"),
        "tree": git_value("rev-parse", "HEAD^{tree}"),
        "comparator": digest(COMPARATOR),
        "scope": digest(OFFICIAL_SCOPE),
        "live": digest(LIVE_SOURCE),
        "independent": digest(IND_SOURCE),
    }
    return pins


def dotted_map_digest(values):
    raw = json.dumps(values, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main():
    DRAFT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    initial = current_pins()
    if initial != EXPECTED:
        raise SystemExit("input/source pin changed before probe: " + json.dumps(initial, sort_keys=True))

    live = json.loads(LIVE_SOURCE.read_text(encoding="utf-8"))
    independent = json.loads(IND_SOURCE.read_text(encoding="utf-8"))
    official_scope = json.loads(OFFICIAL_SCOPE.read_text(encoding="utf-8"))
    scope_ids = sorted(official_scope["scope_out"])
    live_ids = {row["check"] for row in live["results"]}
    live_values = {row["check"]: row["observed"] for row in live["results"]}
    probe_source = next(
        row["probe"] for row in independent["results"]
        if row.get("check") == "omp.catalogue.found"
    )

    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("e1_comparator", COMPARATOR)
    comparator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(comparator)
    fresh_probe = {"kind": "rule-spread-census", "target": probe_source["target"]}
    fresh_probe["observable"] = comparator.recompute_probe(fresh_probe)["observable"]

    def refresh_scope_probes(payload):
        payload = copy.deepcopy(payload)
        for cid in payload.get("scoped_out", {}):
            for channel in ("results", "rows"):
                record = next(row for row in payload[channel] if row["check"] == cid)
                record["probe"] = copy.deepcopy(fresh_probe)
            payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(fresh_probe)
        return payload

    independent = refresh_scope_probes(independent)
    fresh_baseline_path = write_json(DRAFT / "fresh-probe-baseline-independent.json", independent)

    def scope_variant(name, document):
        return write_json(DRAFT / f"{name}-scope.json", document)

    def independent_variant(name, document):
        return write_json(DRAFT / f"{name}-independent.json", document)

    def add_scope_row(document, cid, reason):
        document["scope_out"][cid] = {"kind": "rule-in-author-scope", "reason": reason}
        return document

    def set_all_scoped_rows_derived(payload):
        payload = copy.deepcopy(payload)
        for cid in scope_ids:
            value = live_values[cid]
            for channel in ("results", "rows"):
                record = next(row for row in payload[channel] if row["check"] == cid)
                record["re_derived"] = value
                record["value"] = value
                record["status"] = "DERIVED"
                record.pop("probe", None)
            payload["checks"][cid] = value
        payload.pop("scoped_out", None)
        payload.pop("scoped_out_probes", None)
        payload["landed"] = len(live_ids)
        return payload

    def scope_out_new_row(payload, cid, reason):
        payload = copy.deepcopy(payload)
        for channel in ("results", "rows"):
            record = next(row for row in payload[channel] if row["check"] == cid)
            record["re_derived"] = None
            record["value"] = None
            record["status"] = "SCOPED_OUT"
            record["probe"] = copy.deepcopy(fresh_probe)
        payload["checks"][cid] = None
        payload.setdefault("scoped_out", {})[cid] = reason
        payload.setdefault("scoped_out_probes", {})[cid] = copy.deepcopy(fresh_probe)
        return payload

    empty_scope = copy.deepcopy(official_scope)
    empty_scope["scope_out"] = {}
    unknown_contract = copy.deepcopy(official_scope)
    unknown_contract["probe_contract"]["kind"] = "e1-not-an-enum-kind"
    unknown_contract_empty = copy.deepcopy(empty_scope)
    unknown_contract_empty["probe_contract"]["kind"] = "e1-not-an-enum-kind"

    extra_missing = copy.deepcopy(official_scope)
    add_scope_row(extra_missing, "omp.elf.template_bytes", "E1 row intentionally omitted from independent payload")
    missing_payload = copy.deepcopy(independent)
    missing_id = "omp.elf.template_bytes"
    missing_payload["results"] = [row for row in missing_payload["results"] if row["check"] != missing_id]
    missing_payload["rows"] = [row for row in missing_payload["rows"] if row["check"] != missing_id]
    missing_payload["checks"].pop(missing_id)

    extra_unknown = copy.deepcopy(official_scope)
    add_scope_row(extra_unknown, "e1.absent.from.live.and.payload", "inert unknown scope-file row")

    forged_metadata = copy.deepcopy(official_scope)
    claimed_set = sorted(scope_ids + ["e1.fabricated.not-in-scope-out"])
    forged_metadata["committed_set"] = claimed_set
    forged_metadata["committed_set_sha256"] = dotted_map_digest(claimed_set)

    widened_scope = copy.deepcopy(official_scope)
    widened_id = "omp.offered.skills"
    add_scope_row(widened_scope, widened_id, "fabricated caller-selected scope row for the E1 trust-boundary test")
    widened_set = sorted(widened_scope["scope_out"])
    widened_scope["committed_set"] = widened_set
    widened_scope["committed_set_sha256"] = dotted_map_digest(widened_set)
    widened_payload = scope_out_new_row(independent, widened_id, widened_scope["scope_out"][widened_id]["reason"])

    cases = [
        ("official-control", LIVE_SOURCE, fresh_baseline_path, OFFICIAL_SCOPE),
        ("scope-row-live-but-absent-from-payload", LIVE_SOURCE,
         independent_variant("scope-row-live-but-absent-from-payload", missing_payload),
         scope_variant("scope-row-live-but-absent-from-payload", extra_missing)),
        ("scope-row-absent-from-live-and-payload", LIVE_SOURCE, fresh_baseline_path,
         scope_variant("scope-row-absent-from-live-and-payload", extra_unknown)),
        ("unknown-probe-contract-with-active-rows", LIVE_SOURCE, fresh_baseline_path,
         scope_variant("unknown-probe-contract-with-active-rows", unknown_contract)),
        ("empty-scope-with-payload-scope-outs", LIVE_SOURCE, fresh_baseline_path,
         scope_variant("empty-scope-with-payload-scope-outs", empty_scope)),
        ("empty-scope-no-payload-scope-outs", LIVE_SOURCE,
         independent_variant("empty-scope-no-payload-scope-outs", set_all_scoped_rows_derived(independent)),
         scope_variant("empty-scope-no-payload-scope-outs", empty_scope)),
        ("unknown-probe-contract-empty-scope", LIVE_SOURCE,
         independent_variant("unknown-probe-contract-empty-scope", set_all_scoped_rows_derived(independent)),
         scope_variant("unknown-probe-contract-empty-scope", unknown_contract_empty)),
        ("fabricated-committed-set-metadata", LIVE_SOURCE, fresh_baseline_path,
         scope_variant("fabricated-committed-set-metadata", forged_metadata)),
        ("fabricated-committed-set-with-valid-probe", LIVE_SOURCE,
         independent_variant("fabricated-committed-set-with-valid-probe", widened_payload),
         scope_variant("fabricated-committed-set-with-valid-probe", widened_scope)),
    ]

    results = []
    for name, live_path, independent_path, scope_path in cases:
        receipt_path = DRAFT / f"{name}-receipt.json"
        stdout_path = DRAFT / f"{name}-stdout.json"
        stderr_path = DRAFT / f"{name}-stderr.txt"
        argv = [
            sys.executable, str(COMPARATOR),
            "--live-json", str(live_path),
            "--independent-json", str(independent_path),
            "--expect-n", str(len(live_ids)),
            "--cwd", str(ROOT),
            "--scope-file", str(scope_path),
            "--no-stamp", "--json", "--receipt", str(receipt_path),
        ]
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, env=env, timeout=120)
        stdout_path.write_text(proc.stdout, encoding="utf-8")
        stderr_path.write_text(proc.stderr, encoding="utf-8")
        try:
            report = json.loads(proc.stdout) if proc.stdout.strip() else None
        except ValueError:
            report = None
        receipt = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else None
        results.append({
            "case": name,
            "argv": argv,
            "process_cwd": str(ROOT),
            "returncode": proc.returncode,
            "stdout_file": str(stdout_path.relative_to(ROOT)),
            "stdout_sha256": digest(stdout_path),
            "stderr_file": str(stderr_path.relative_to(ROOT)),
            "stderr_sha256": digest(stderr_path),
            "live_input": {"path": str(live_path.relative_to(ROOT)), "sha256": digest(live_path)},
            "independent_input": {"path": str(independent_path.relative_to(ROOT)), "sha256": digest(independent_path)},
            "scope_input": {"path": str(scope_path.relative_to(ROOT)), "sha256": digest(scope_path)},
            "receipt_file": str(receipt_path.relative_to(ROOT)) if receipt is not None else None,
            "receipt_sha256": digest(receipt_path) if receipt is not None else None,
            "receipt_scope_sha256_matches_input": bool(
                receipt and receipt.get("scope_file", {}).get("sha256") == digest(scope_path)
            ),
            "report": {
                "headline": report.get("headline"),
                "agreement": report.get("agreement"),
                "exit": report.get("exit"),
                "reason": report.get("reason"),
            } if isinstance(report, dict) else None,
            "receipt_committed_set": receipt.get("scope_locks", {}).get("committed_set") if receipt else None,
        })

    finished = datetime.now(timezone.utc).isoformat()
    final = current_pins()
    if final != EXPECTED:
        raise SystemExit("source/tree changed during probe: " + json.dumps({"initial": initial, "final": final}, sort_keys=True))
    result = {
        "seat": "E1",
        "started_at_utc": started,
        "finished_at_utc": finished,
        "source_pins": initial,
        "live_check_ids_n": len(live_ids),
        "official_scope_ids": scope_ids,
        "probe_kind": fresh_probe["kind"],
        "probe_observable": fresh_probe["observable"],
        "committed_set_digest_scheme": "sha256 of UTF-8 JSON sorted-list bytes, compact separators",
        "cases": results,
        "source_pins_unchanged": initial == final,
    }
    out = EVIDENCE / "E1-scope-edge-results.json"
    write_json(out, result)
    print(json.dumps({"result": str(out.relative_to(ROOT)), "sha256": digest(out), "cases": [
        {"case": row["case"], "returncode": row["returncode"], "headline": row["report"]["headline"] if row["report"] else None,
         "agreement": row["report"]["agreement"] if row["report"] else None,
         "reason": row["report"]["reason"] if row["report"] else None}
        for row in results
    ], "source_pins_unchanged": initial == final}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
