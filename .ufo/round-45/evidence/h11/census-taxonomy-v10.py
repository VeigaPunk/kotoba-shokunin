#!/usr/bin/env python3
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

DRAFT = Path(__file__).resolve().parent
SOURCE = DRAFT / "subprocess-replay.json"
OUTPUT = DRAFT / "channel-census.json"
EXPECTED_ARM_COUNT = 46

CASES = {
    "checks-record-list-control": ("control", "record-channels", "Consistent list-channel control accepted."),
    "checks-record-list-divergent": ("closed", "record-channel-divergence", "Divergent checks/results values for one id rejected with exit 2."),
    "control": ("control", "baseline-join", "Unmutated baseline join accepted."),
    "f3-consistent-value-disagreement": ("closed", "value-disagreement", "Consistent independent value disagrees with live observation; exit 1 reports the disagreement."),
    "f3-rows-missing": ("closed", "record-channel-membership", "An id present in checks but absent from rows is rejected with exit 2."),
    "headline-uncovered-count": ("diagnostic", "headline-accounting", "The missing row is rejected, but headline.live_checks is 29 while the captured live payload has 28 checks."),
    "heldout-duplicate-id-status-shadow": ("open", "status-consistency", "A duplicate id with an earlier UNLANDED status and later DERIVED status is accepted with exit 0."),
    "heldout-expected-only-full-copy": ("open", "expected-value-source", "A complete copied expected-value map is accepted without proving independent derivation."),
    "heldout-expected-value-secondary-shadow": ("open", "value-key-alias", "A conflicting expected_value=999 shadow beside value=7 is accepted with exit 0."),
    "heldout-flat-dotted-map": ("open", "alternate-value-map", "A flat dotted-id map carrying copied values is accepted with exit 0."),
    "heldout-id-alias-conflict": ("open", "identity-alias", "Conflicting id/name aliases are accepted alongside the check identity."),
    "heldout-nested-checks-map": ("open", "alternate-value-map", "A nested checks map carrying copied values is accepted with exit 0."),
    "heldout-nested-expected-wrapper": ("open", "alternate-value-wrapper", "A nested expected-value wrapper is accepted as an independent payload."),
    "heldout-nested-observations-wrapper": ("open", "alternate-value-wrapper", "A nested observations wrapper is accepted as an independent payload."),
    "heldout-observed-key-shadow": ("open", "value-key-alias", "A conflicting observed=999 shadow beside value/re_derived=7 is accepted with exit 0."),
    "heldout-rederived-vs-value-shadow": ("open", "value-channel-consistency", "A results record with re_derived=7 and value=999 is accepted with exit 0."),
    "heldout-wrapper-precedence-expected-over-observations": ("open", "wrapper-precedence", "Conflicting expected=7 and observations=999 wrapper maps are accepted with exit 0."),
    "live-mode-equal-with-independent-drift": ("closed", "live-mode-comparison", "An equal-mode live row with independent drift is reported as exit 1 disagreement."),
    "live-mode-positive-masks-independent-drift": ("open", "live-mode-comparison", "A caller-supplied positive live mode masks independent value drift and returns exit 0."),
    "live-mode-split-across-row-channels": ("open", "live-mode-channel-consistency", "Conflicting live modes split across results/rows are accepted with exit 0."),
    "live-top-level-observed-summary-divergence": ("open", "live-summary-consistency", "Divergent top-level observed/summary content is ignored while row channels return exit 0."),
    "live-verdict-shadow-in-row-channel": ("open", "live-verdict-consistency", "A conflicting verdict shadow in a live row channel is accepted with exit 0."),
    "r1-f2-expected-not-derived": ("closed", "expected-versus-derivation", "A harvested expected value cannot override explicit NOT DERIVED; rejected with exit 2."),
    "r1-f3-prime-scope-file-cwd": ("open", "scope-file-resolution", "The relative scope file resolves from planted process CWD, returns 0 at 23/23, and the receipt digest is inconsistent with that selected file."),
    "r1-f3-prime-scope-file-honest-cwd-control": ("closed", "scope-file-resolution", "The same relative scope argument from the honest repo CWD rejects the uncommitted scope-out with exit 2."),
    "r1-f3-rows-shadow": ("closed", "record-channel-divergence", "A divergent rows value hidden beside checks/results is rejected with exit 2."),
    "r1-f4-payload-chosen-probe-target": ("open", "probe-target-binding", "Payload-selected probe target is recomputed and the altered input is accepted with exit 0."),
    "record-probe-fallback-reads-results-only": ("open", "probe-channel-completeness", "A record probe carried only in results is accepted; the probe channels are not reconciled."),
    "record-probe-shadowed-by-top-level-map": ("open", "probe-target-binding", "A top-level probe map shadows a record probe target and the payload is accepted with exit 0."),
    "results-dotted-map-control": ("control", "record-channel-format", "Consistent dotted results-map control accepted."),
    "results-dotted-map-divergent": ("closed", "record-channel-divergence", "A divergent dotted results-map value is rejected with exit 2."),
    "row-map-agreeing-control": ("control", "record-channel-format", "Consistent row-map control accepted."),
    "row-map-divergent": ("closed", "record-channel-divergence", "A divergent row-map value is rejected with exit 2."),
    "scope-file-caller-selected-absolute": ("trust-input", "scope-file-trust-boundary", "An explicitly caller-selected absolute scope file is accepted; this tests the caller-chosen trust input, not bypass of the selected file."),
    "scope-uncommitted-extra-row": ("closed", "scope-set-membership", "A payload scope-out absent from the committed scope set is rejected with exit 2."),
    "scoped-out-reason-and-evidence-drift": ("open", "scope-record-integrity", "Changed scoped-out reason/evidence is accepted with exit 0."),
    "scoped-out-record-without-map": ("closed", "scope-channel-membership", "SCOPED_OUT record statuses missing from the scoped_out map are rejected with exit 2."),
    "status-nonstring-hides-state": ("open", "status-consistency", "A non-string status shadows state=UNLANDED and is accepted with exit 0."),
    "status-primary-unlanded": ("closed", "unlanded-status", "An explicit primary UNLANDED status yields exit 1 and is not counted as a green join."),
    "t1-duplicate-id-divergent-copy": ("closed", "duplicate-id-values", "Two values for one duplicated results id are rejected with exit 2."),
    "top-level-status-and-alternatives": ("open", "top-level-metadata", "Fabricated top-level alternatives/status metadata is not reconciled with row data and the payload returns exit 0."),
    "unmatched-extra-scoped-out-probe": ("open", "probe-channel-membership", "An unmatched extra scoped-out probe target is accepted with exit 0."),
    "v1-a7-checks-shadow": ("closed", "record-channel-divergence", "A checks-channel shadow divergent from results is rejected with exit 2."),
    "w1-scoped-row-carries-value": ("open", "scoped-out-value", "A SCOPED_OUT row carrying a value is accepted with exit 0."),
    "w1-stringified-rows": ("closed", "record-value-type", "A stringified row value disagrees with the integer checks value and is rejected with exit 2."),
    "x2-state-shadow": ("open", "status-consistency", "state=UNLANDED alongside status=DERIVED is accepted with exit 0."),
}

CLASS_MEANINGS = {
    "open": "The adversarial payload was accepted by the frozen comparator (actual exit 0).",
    "closed": "The attempted inconsistency was rejected or reported as a disagreement (actual exit nonzero).",
    "control": "A baseline or structurally consistent control was accepted; this is not an adversarial pass.",
    "diagnostic": "The arm rejected the input but exposed a separate reporting/counting defect.",
    "trust-input": "The caller explicitly selected the input path; acceptance characterizes that trust boundary, not a bypass of the selected file.",
}


def main():
    source_bytes = SOURCE.read_bytes()
    source = json.loads(source_bytes)
    arms = source.get("arms")
    if not isinstance(arms, list):
        raise ValueError("subprocess replay arms must be a list")

    arm_ids = [arm["id"] for arm in arms]
    if len(arm_ids) != len(set(arm_ids)):
        raise ValueError("subprocess replay contains duplicate arm ids")
    source_ids = set(arm_ids)
    case_ids = set(CASES)
    missing = sorted(source_ids - case_ids)
    extra = sorted(case_ids - source_ids)
    if missing or extra or len(arm_ids) != EXPECTED_ARM_COUNT:
        raise ValueError(f"arm set mismatch: missing={missing}, extra={extra}, count={len(arm_ids)}")
    if not all(arm.get("matched") for arm in arms):
        raise ValueError("one or more subprocess arms failed to reproduce saved output")
    if source.get("matched_count") != EXPECTED_ARM_COUNT or source.get("process_count") != EXPECTED_ARM_COUNT:
        raise ValueError("subprocess replay does not report 46/46 matches")

    results = []
    for arm in sorted(arms, key=lambda item: item["id"]):
        classification, channel, finding = CASES[arm["id"]]
        results.append({
            "id": arm["id"],
            "classification": classification,
            "channel": channel,
            "finding": finding,
            "reproducer": {
                "argv": arm["command"],
                "process_cwd": arm["process_cwd"],
                "driver_cwd_arg": arm["driver_cwd_arg"],
                "scope_file_arg": arm["scope_file_arg"],
            },
            "actual": arm["actual"],
            "input_sha256_before": arm["inputs_sha256_before"],
            "input_sha256_after": arm["inputs_sha256_after"],
            "input_hashes_unchanged": arm["inputs_sha256_before"] == arm["inputs_sha256_after"],
        })

    counts = Counter(result["classification"] for result in results)
    report = {
        "schema": "kotoba.round41.v10.channel-census.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": SOURCE.name,
            "sha256": hashlib.sha256(source_bytes).hexdigest(),
            "frozen_head": source["frozen_head"],
            "frozen_tree": source["frozen_tree"],
            "comparator_sha256": source["comparator_sha256"],
            "live_payload_sha256": source["live_payload_sha256"],
            "independent_payload_sha256": source["independent_payload_sha256"],
            "scope_sha256": source["scope_sha256"],
        },
        "classifications": CLASS_MEANINGS,
        "summary": {
            "arm_count": len(results),
            "classification_counts": dict(sorted(counts.items())),
            "source_replay_matched_count": source["matched_count"],
        },
        "validation": {
            "expected_arm_count": EXPECTED_ARM_COUNT,
            "source_arm_count": len(arm_ids),
            "classified_arm_count": len(results),
            "arm_ids_unique": len(arm_ids) == len(set(arm_ids)),
            "arm_set_equal": source_ids == case_ids == {result["id"] for result in results},
            "missing_classifications": missing,
            "extra_classifications": extra,
            "all_source_arms_replayed": all(arm.get("matched") for arm in arms),
            "all_input_hashes_unchanged": all(result["input_hashes_unchanged"] for result in results),
        },
        "arms": results,
    }
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("channel_census: %d/%d arms classified; counts=%s; output=%s" % (
        len(results), EXPECTED_ARM_COUNT, dict(counts), OUTPUT))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"channel_census: ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
