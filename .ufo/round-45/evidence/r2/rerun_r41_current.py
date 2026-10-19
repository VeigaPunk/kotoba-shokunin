import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = Path(__file__).resolve().parent
DRAFT.mkdir(parents=True, exist_ok=True)
SOURCE = ROOT / ".ufo/round-41/evidence/v10-census-probes.py"
COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
COMPARATOR_SHA = "13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def frozen_source(rev, output):
    raw = subprocess.run(
        ["git", "-C", str(ROOT), "show", f"{rev}:verifiers/compare_harness_independent.py"],
        check=True, capture_output=True).stdout
    output.write_bytes(raw)
    return {"revision": rev, "path": str(output.relative_to(ROOT)),
            "bytes": len(raw), "sha256": sha(raw)}

def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

landed_bytes = subprocess.run(
    ["git", "-C", str(ROOT), "show", "032f47b:verifiers/compare_harness_independent.py"],
    check=True, capture_output=True).stdout
if sha(landed_bytes) != COMPARATOR_SHA:
    raise SystemExit("git show 032f47b comparator is not the registered landed 13b6d791 source")
worktree_comparator_sha_at_start = sha(COMPARATOR.read_bytes())

source_info = {
    "r44_dispatch": frozen_source("6881ce3", DRAFT / "compare-r44-dispatch-6881ce3.py"),
    "landed": frozen_source("032f47b", DRAFT / "compare-landed-032f47b.py"),
}
if source_info["landed"]["sha256"] != COMPARATOR_SHA:
    raise SystemExit("git show 032f47b comparator differs from the claimed landed SHA")

probes = import_file("v10_census_probes", SOURCE)
probes.ROOT = ROOT
probes.DRAFT = DRAFT
probes.DRIVER = DRAFT / "compare-r41-b1be35f.py"
probes.LIVE_FILE = DRAFT / "live-b1be35f.json"
probes.IND_FILE = DRAFT / "independent-b1be35f.json"
probes.CARRIER = DRAFT / "builder-carrier"

def load_landed():
    return import_file("compare_landed_032f47b", DRAFT / "compare-landed-032f47b.py")

probes.load_driver = load_landed
probes.main()
results_path = DRAFT / "probe-results.json"
results = json.loads(results_path.read_text(encoding="utf-8"))
if len(results.get("arms", {})) != 46:
    raise SystemExit(f"expected 46 census arms, got {len(results.get('arms', {}))}")
results["stdout_stderr"] = {}
results["comparison_sources"] = source_info
results["landed_comparator_sha256"] = COMPARATOR_SHA
results["fresh_replay_started_at_utc"] = datetime.now(timezone.utc).isoformat()
results_path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")

census = import_file("v10_channel_census", ROOT / ".ufo/round-41/evidence/v10-channel-census.py")
static_cases = census.CASES
arms = results["arms"]
replays = {}
receipt_paths = {}
for source_key, source in source_info.items():
    source_path = ROOT / source["path"]
    records = []
    for arm_id, arm in sorted(arms.items()):
        command = list(arm["command"])
        command[1] = str(source_path)
        if "--receipt" in command:
            i = command.index("--receipt") + 1
            command[i] = str(DRAFT / f"receipt-{source_key}-{arm_id}.json")
            receipt_paths[arm_id] = command[i]
        inputs = {}
        for flag in ("--live-json", "--independent-json", "--scope-file"):
            if flag not in command:
                continue
            value = Path(command[command.index(flag) + 1])
            resolved = value if value.is_absolute() else Path(arm["process_cwd"]) / value
            inputs[flag[2:].replace("-", "_")] = resolved.resolve()
        before = {key: sha(path.read_bytes()) for key, path in inputs.items()}
        proc = subprocess.run(command, cwd=arm["process_cwd"], capture_output=True,
                              text=True, timeout=120)
        try:
            payload = json.loads(proc.stdout)
            headline, reason = payload.get("headline"), payload.get("reason", "")
        except (ValueError, TypeError):
            headline, reason = None, (proc.stderr or proc.stdout).strip()[-1200:]
        after = {key: sha(path.read_bytes()) for key, path in inputs.items()}
        records.append({
            "id": arm_id,
            "argv": command,
            "process_cwd": arm["process_cwd"],
            "input_sha256_before": before,
            "input_sha256_after": after,
            "inputs_unchanged": before == after,
            "exit": proc.returncode,
            "headline": headline,
            "reason": reason,
            "stderr_tail": proc.stderr[-600:],
            "matches_landed_generation": (source_key != "landed" or
                (proc.returncode == arm["exit"] and headline == arm.get("headline")
                 and reason == arm["reason"])),
        })
    replays[source_key] = records

classification = {}
for arm_id, arm in arms.items():
    base_class, channel, finding = static_cases[arm_id]
    before = replays["r44_dispatch"][[x["id"] for x in replays["r44_dispatch"]].index(arm_id)]
    after = replays["landed"][[x["id"] for x in replays["landed"]].index(arm_id)]
    if base_class in ("control", "diagnostic", "trust-input"):
        current_class = base_class
    elif after["exit"] == 0:
        current_class = "open"
    else:
        current_class = "closed"
    classification[arm_id] = {
        "r41_class": base_class,
        "channel": channel,
        "r44_exit": before["exit"],
        "landed_exit": after["exit"],
        "landed_headline": after["headline"],
        "landed_reason": after["reason"],
        "current_class": current_class,
        "finding": finding,
    }

summary = {}
for source_key, records in replays.items():
    summary[source_key] = {
        "arm_count": len(records),
        "exit_counts": dict(sorted(Counter(str(r["exit"]) for r in records).items())),
        "input_mutations": [r["id"] for r in records if not r["inputs_unchanged"]],
        "landed_generation_mismatches": [r["id"] for r in records if not r["matches_landed_generation"]],
    }
counts = Counter(row["current_class"] for row in classification.values())
output = {
    "schema": "kotoba.round45.r2.heldout-census-replay.v1",
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                           check=True, capture_output=True, text=True).stdout.strip(),
    "tree": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD^{tree}"],
                           check=True, capture_output=True, text=True).stdout.strip(),
    "current_comparator_sha256": sha(COMPARATOR.read_bytes()),
    "scope_sha256": sha((ROOT / "verifiers/harness-independent-scope.json").read_bytes()),
    "sources": source_info,
    "r41_inputs": {
        "generator": str(SOURCE.relative_to(ROOT)),
        "generator_sha256": sha(SOURCE.read_bytes()),
        "historical_probe_results_sha256": sha((ROOT / ".ufo/round-41/evidence/v10-probe-results.json").read_bytes()),
        "historical_census_sha256": sha((ROOT / ".ufo/round-41/evidence/v10-channel-census.json").read_bytes()),
        "fresh_live_sha256": sha(probes.LIVE_FILE.read_bytes()),
        "fresh_independent_sha256": sha(probes.IND_FILE.read_bytes()),
        "fresh_probe_results_sha256": sha(results_path.read_bytes()),
    },
    "summary": summary,
    "landed_classification_counts": dict(sorted(counts.items())),
    "classification": classification,
    "replays": replays,
}
output_path = DRAFT / "census-replay.json"
output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"output": str(output_path.relative_to(ROOT)),
                  "output_sha256": sha(output_path.read_bytes()),
                  "head": output["head"], "tree": output["tree"],
                  "comparator": output["current_comparator_sha256"],
                  "summary": summary,
                  "landed_classification_counts": output["landed_classification_counts"],
                  "open_ids": sorted(k for k, v in classification.items()
                                      if v["current_class"] == "open")},
                 indent=2, sort_keys=True))
