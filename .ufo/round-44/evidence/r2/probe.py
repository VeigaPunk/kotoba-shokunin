#!/usr/bin/env python3
import copy
import contextlib
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = ROOT / ".ufo/round-44/drafts/r2"
EVIDENCE = ROOT / ".ufo/round-44/evidence"
EVIDENCE.mkdir(parents=True, exist_ok=True)
(DRAFT / "tmp").mkdir(parents=True, exist_ok=True)

COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
SURFACES = ROOT / "verifiers/verify_surfaces.py"
PINS = ROOT / "verifiers/check_substrate_pins.py"
BASELINE = ROOT / "verifiers/baseline.json"
SURFACE_BASELINE = ROOT / "verifiers/surfaces-baseline.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
INVENTORY = ROOT / "corpus/knowledge/instruction-surface-census-round13.md"
OMP = Path("/home/vgpnk/.local/bin/omp")
OPENCODE = Path("/home/vgpnk/.opencode/bin/opencode")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          capture_output=True).stdout


def git_text(*args):
    return git(*args).decode("utf-8", "replace").strip()


def snapshot():
    paths = (COMPARATOR, SURFACES, PINS, BASELINE, SURFACE_BASELINE, SCOPE,
             ROOT / ".ufo/round-44/claims.json")
    return {
        "at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="microseconds"),
        "head": git_text("rev-parse", "HEAD"),
        "head_tree": git_text("rev-parse", "HEAD^{tree}"),
        "tracked_diff": git_text("diff", "--name-only"),
        "staged_diff": git_text("diff", "--cached", "--name-only"),
        "tracked_diff_sha256": sha(git("diff", "--binary")),
        "staged_diff_sha256": sha(git("diff", "--cached", "--binary")),
        "sha256": {str(p.relative_to(ROOT)): sha_file(p) for p in paths},
    }


def capture(argv, cwd=ROOT, timeout=300):
    p = subprocess.run(argv, cwd=str(cwd), capture_output=True, timeout=timeout)
    return {
        "argv": [str(a) for a in argv],
        "cwd": str(cwd),
        "exit": p.returncode,
        "stdout": p.stdout.decode("utf-8", "replace"),
        "stderr": p.stderr.decode("utf-8", "replace"),
        "stdout_sha256": sha(p.stdout),
        "stderr_sha256": sha(p.stderr),
    }


def write_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data),
            "sha256": sha(data)}


def write_json(path, value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    return write_bytes(path, raw)


def summarized_process(record):
    out = record["stdout"]
    try:
        payload = json.loads(out)
    except ValueError:
        payload = None
    summary = {k: payload.get(k) for k in ("exit_code", "pass", "fail") if payload is not None and k in payload}
    if payload is not None and isinstance(payload.get("agreement"), dict):
        summary["agreement"] = {k: payload["agreement"].get(k) for k in (
            "n_agree_protocol", "n_agree_strict", "n_adjudicated", "n_scoped_out",
            "n_disagree", "n_uncovered", "n_unknown", "total")}
        summary["headline"] = payload.get("headline")
        summary["secondary_agree"] = payload.get("secondary_agree")
    if payload is not None and isinstance(payload.get("checks"), list):
        summary["checks"] = payload["checks"]
    summary["exit"] = record["exit"]
    summary["stderr"] = record["stderr"]
    summary["stdout_sha256"] = record["stdout_sha256"]
    summary["stderr_sha256"] = record["stderr_sha256"]
    return summary


start = snapshot()
claims_path = ROOT / ".ufo/round-44/claims.json"
claims_sha = sha_file(claims_path)

frozen_comparator = git("show", "6fbbff5:verifiers/compare_harness_independent.py")
frozen_comparator_path = EVIDENCE / "r2-compare-harness-independent-6fbbff5.py"
frozen_comparator_input = write_bytes(frozen_comparator_path, frozen_comparator)
current_comparator_before = sha_file(COMPARATOR)
current_comparator = COMPARATOR.read_bytes()
current_comparator_after = sha_file(COMPARATOR)
if current_comparator_before != current_comparator_after or sha(current_comparator) != current_comparator_after:
    raise RuntimeError("current comparator changed while its candidate snapshot was frozen")
current_comparator_sha = sha(current_comparator)
current_comparator_path = EVIDENCE / ("r2-compare-candidate-" + current_comparator_sha[:12] + ".py")
current_comparator_input = write_bytes(current_comparator_path, current_comparator)

frozen_surfaces = git("show", "6fbbff5:verifiers/verify_surfaces.py")
frozen_surfaces_path = EVIDENCE / "r2-verify-surfaces-6fbbff5.py"
frozen_surfaces_input = write_bytes(frozen_surfaces_path, frozen_surfaces)
frozen_surfaces_text = frozen_surfaces.decode("utf-8")
old_callee = "(?:Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj)"
new_callee = "(?:Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)"
if frozen_surfaces_text.count(old_callee) != 1:
    raise RuntimeError("frozen surfaces source no longer has one exact OMP callee pattern")
calibrated_text = frozen_surfaces_text.replace(old_callee, new_callee, 1)
old_shape = "(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj)(<v>, <group>, \"<file>.md\")"
new_shape = "(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(<v>, <group>, \"<file>.md\")"
if calibrated_text.count(old_shape) != 1:
    raise RuntimeError("frozen surfaces callee-shape description did not match exactly")
calibrated_text = calibrated_text.replace(old_shape, new_shape, 1)
calibrated_surfaces_path = EVIDENCE / "r2-verify-surfaces-candidate-I5-Gl-Mo.py"
calibrated_surfaces_input = write_bytes(calibrated_surfaces_path, calibrated_text.encode())

live_rec = capture([sys.executable, "verifiers/verify_harness_claims.py", "--json"])
ind_rec = capture([sys.executable, "verifiers/verify_harness_independent.py", "--json"])
if live_rec["exit"] != 0 or ind_rec["exit"] != 0:
    raise RuntimeError("fresh producer failed; refusing to score mutated payloads")
live_bytes = live_rec["stdout"].encode()
ind_bytes = ind_rec["stdout"].encode()
live_path = EVIDENCE / "r2-live-claims.json"
ind_path = EVIDENCE / "r2-independent.json"
live_input = write_bytes(live_path, live_bytes)
ind_input = write_bytes(ind_path, ind_bytes)
live_payload = json.loads(live_bytes)
ind_payload = json.loads(ind_bytes)

records_present = [k for k in ("results", "rows") if isinstance(ind_payload.get(k), list)]
if set(records_present) != {"results", "rows"} or not isinstance(ind_payload.get("checks"), dict):
    raise RuntimeError("fresh independent producer no longer has the expected records + map channels")
first_cid = ind_payload["results"][0]["check"]


def mutate_records(payload, fn):
    for channel in ("results", "rows"):
        fn(payload[channel][0])


arms = {}
arm = copy.deepcopy(ind_payload)
arm[first_cid] = "SHADOW: top-level dotted-id conflicts with record channels"
arms["top-level-dotted-shadow"] = arm

arm = copy.deepcopy(ind_payload)
mutate_records(arm, lambda r: r.update(id="rogue.id.alias"))
arms["check-id-conflict"] = arm

arm = copy.deepcopy(ind_payload)
mutate_records(arm, lambda r: r.update(name="rogue.name.alias"))
arms["check-name-conflict"] = arm

arm = copy.deepcopy(ind_payload)
def id_name_conflict(record):
    cid = record.pop("check")
    record["id"] = cid
    record["name"] = "rogue.name.alias"
mutate_records(arm, id_name_conflict)
arms["id-name-conflict"] = arm

arm = copy.deepcopy(ind_payload)
mutate_records(arm, lambda r: r.update(check_id="rogue.check_id.alias"))
arms["fourth-check_id-field"] = arm

arm = copy.deepcopy(ind_payload)
mutate_records(arm, lambda r: r.update(observed="CONFLICT: observed differs from re_derived"))
arms["re_derived-observed-conflict"] = arm

arm = copy.deepcopy(ind_payload)
mutate_records(arm, lambda r: r.update(value="CONFLICT: value differs from re_derived"))
arms["re_derived-value-conflict"] = arm

arm = copy.deepcopy(ind_payload)
arm["checks"][first_cid] = "CONFLICT: map differs from row channels"
arms["checks-map-divergence-control"] = arm

arm_paths = {}
for name, payload in arms.items():
    path = EVIDENCE / ("r2-independent-arm-" + name + ".json")
    arm_paths[name] = write_json(path, payload)

scope_sha = sha_file(SCOPE)
compare_sources = {
    "frozen-6fbbff5": str(frozen_comparator_path),
    "candidate-snapshot": str(current_comparator_path),
}

commands = {}
for source_name, source_path in compare_sources.items():
    commands[source_name] = {}
    for arm_name, input_record in arm_paths.items():
        argv = [sys.executable, source_path,
                "--live-json", str(live_path),
                "--independent-json", str(ROOT / input_record["path"]),
                "--cwd", str(ROOT), "--scope-file", str(SCOPE),
                "--expect-n", "28", "--no-stamp", "--json"]
        record = capture(argv)
        commands[source_name][arm_name] = {
            "argv": record["argv"], "cwd": record["cwd"],
            "input_sha256": input_record["sha256"],
            "exit": record["exit"],
            "stdout_sha256": record["stdout_sha256"],
            "stderr_sha256": record["stderr_sha256"],
            "summary": summarized_process(record),
        }

base_control = {}
for source_name, source_path in compare_sources.items():
    argv = [sys.executable, source_path, "--live-json", str(live_path),
            "--independent-json", str(ind_path), "--cwd", str(ROOT),
            "--scope-file", str(SCOPE), "--expect-n", "28", "--no-stamp", "--json"]
    record = capture(argv)
    base_control[source_name] = {
        "argv": record["argv"], "cwd": record["cwd"],
        "exit": record["exit"], "stdout_sha256": record["stdout_sha256"],
        "stderr_sha256": record["stderr_sha256"], "summary": summarized_process(record),
    }

surfaces_before_argv = [sys.executable, str(frozen_surfaces_path),
                        "--repo", str(ROOT), "--baseline", str(SURFACE_BASELINE),
                        "--inventory", str(INVENTORY), "--omp-binary", str(OMP),
                        "--opencode-binary", str(OPENCODE), "--json"]
surfaces_after_argv = [sys.executable, str(calibrated_surfaces_path),
                       "--repo", str(ROOT), "--baseline", str(SURFACE_BASELINE),
                       "--inventory", str(INVENTORY), "--omp-binary", str(OMP),
                       "--opencode-binary", str(OPENCODE), "--json"]
surfaces_before = capture(surfaces_before_argv)
surfaces_after = capture(surfaces_after_argv)

pins_before = capture([sys.executable, str(PINS), "--baseline", str(BASELINE), "--json"])

omp_stat = OMP.stat()
mtime_ns = omp_stat.st_mtime_ns
secs, nanos = divmod(mtime_ns, 1_000_000_000)
stamp = dt.datetime.fromtimestamp(secs, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + ".%09d+00:00" % nanos
repin_candidate = json.loads(BASELINE.read_text(encoding="utf-8"))
repin_candidate["measured_against"]["omp_binary_sha256"] = sha_file(OMP)
repin_candidate["measured_against"]["omp_binary_mtime"] = stamp
repin_path = EVIDENCE / "r2-baseline-scratch-repin.json"
repin_input = write_json(repin_path, repin_candidate)
pins_after = capture([sys.executable, str(PINS), "--baseline", str(repin_path), "--json"])

sys.path.insert(0, str(ROOT / "verifiers"))
import verify_surfaces as surface_module

dump_proc = subprocess.run(["strings", "-n", "4", str(OMP)], check=True,
                           capture_output=True, timeout=600)
dump_bytes = dump_proc.stdout
dump = dump_bytes.decode("utf-8", "replace")
generic = re.compile(
    r'(?<![A-Za-z0-9_$])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*'
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
constants = surface_module.constant_table(dump)
loader_calls = []
for m in generic.finditer(dump):
    group = m.group(2) or constants.get(m.group(3), "<unresolved-var:%s>" % m.group(3))
    snippet = dump[max(0, m.start() - 30):min(len(dump), m.end() + 30)]
    loader_calls.append({"callee": m.group(1), "raw_group": m.group(2) or m.group(3),
                         "group": group, "file": m.group(4), "snippet": snippet})
actual_pairs = sorted({(c["group"], c["file"]) for c in loader_calls})
actual_ids = sorted("omp:%s/%s" % pair for pair in actual_pairs)
classes = surface_module.load_baseline(SURFACE_BASELINE)
declared_ids = sorted(e["class_id"] for e in classes
                      if e["harness"] == "omp" and e["context_kind"] == "loader-group")
old_ids = sorted("omp:%s/%s" % pair for pair in surface_module.extract_classes(dump, "omp"))

history = {
    "baseline_path_history": git_text("log", "--all", "--format=%h %ad %s",
                                       "--date=iso-strict", "--", "verifiers/baseline.json"),
    "current_omp_sha_git_search": git_text("log", "--all", "-S" + sha_file(OMP),
                                            "--format=%h %ad %s", "--date=iso-strict", "--", "."),
    "embedded_release_lines": [line for line in dump.splitlines()
                               if "## [18.12.2] - 2026-10-18" in line],
    "embedded_version_lines": [line for line in dump.splitlines()
                               if "18.12.2" in line and "version" in line.lower()][:6],
}

end = snapshot()

result = {
    "round": 44,
    "seat": "R2",
    "claims_sha256": claims_sha,
    "measurement": {"start": start, "end": end,
                    "stable_head_tree": start["head"] == end["head"] and start["head_tree"] == end["head_tree"],
                    "stable_tracked_diff": start["tracked_diff"] == end["tracked_diff"] and start["staged_diff"] == end["staged_diff"] and start["tracked_diff_sha256"] == end["tracked_diff_sha256"] and start["staged_diff_sha256"] == end["staged_diff_sha256"],
                    "stable_sources": start["sha256"] == end["sha256"]},
    "inputs": {
        "frozen_comparator": frozen_comparator_input,
        "candidate_comparator": current_comparator_input,
        "current_comparator_sha256": current_comparator_sha,
        "frozen_surfaces": frozen_surfaces_input,
        "candidate_surfaces": calibrated_surfaces_input,
        "live": live_input,
        "independent": ind_input,
        "live_n": len((live_payload.get("results") or [])),
        "independent_n": len((ind_payload.get("results") or [])),
        "scope_sha256": scope_sha,
        "arm_payloads": arm_paths,
    },
    "c2": {"candidate_source_path": current_comparator_input["path"],
           "candidate_source_sha256": current_comparator_sha,
           "frozen_source_commit": "6fbbff5:verifiers/compare_harness_independent.py",
           "frozen_source_sha256": frozen_comparator_input["sha256"],
           "base_control": base_control, "arms": commands},
    "c3": {
        "surfaces_before_frozen": {"argv": surfaces_before["argv"],
                                    "exit": surfaces_before["exit"],
                                    "stdout_sha256": surfaces_before["stdout_sha256"],
                                    "stderr_sha256": surfaces_before["stderr_sha256"],
                                    "summary": summarized_process(surfaces_before)},
        "surfaces_after_candidate": {"argv": surfaces_after["argv"],
                                      "exit": surfaces_after["exit"],
                                      "stdout_sha256": surfaces_after["stdout_sha256"],
                                      "stderr_sha256": surfaces_after["stderr_sha256"],
                                      "summary": summarized_process(surfaces_after)},
        "pins_before": {"argv": pins_before["argv"], "exit": pins_before["exit"],
                        "stdout_sha256": pins_before["stdout_sha256"],
                        "stderr_sha256": pins_before["stderr_sha256"],
                        "summary": summarized_process(pins_before)},
        "pins_after_scratch_repin": {"argv": pins_after["argv"], "exit": pins_after["exit"],
                                     "input": repin_input,
                                     "stdout_sha256": pins_after["stdout_sha256"],
                                     "stderr_sha256": pins_after["stderr_sha256"],
                                     "summary": summarized_process(pins_after)},
        "omp_binary": {"path": str(OMP), "size": omp_stat.st_size,
                       "mtime_ns": mtime_ns, "sha256": sha_file(OMP),
                       "strings_bytes": len(dump_bytes), "strings_sha256": sha(dump_bytes),
                       "candidate_call_count": len(loader_calls),
                       "candidate_unique_pair_count": len(actual_pairs),
                       "candidate_ids": actual_ids,
                       "baseline_loader_group_ids": declared_ids,
                       "candidate_id_parity": actual_ids == declared_ids,
                       "current_allowlist_ids": old_ids,
                       "calls": loader_calls,
                       "resolved_constants": {k: constants.get(k) for k in
                                               sorted({c["raw_group"] for c in loader_calls
                                                       if c["raw_group"] not in {"gemini", "github", "opencode", "windsurf"}})},
                       "version_18_12_2_present": "18.12.2" in dump},
        "git_and_binary_provenance": history,
        "scope_limit": "surface candidate and scratch repin only; production verifier and baseline unchanged",
    },
}

out_path = EVIDENCE / "r2-adversarial-results.json"
write_json(out_path, result)
print(json.dumps({"results_path": str(out_path.relative_to(ROOT)),
                  "results_sha256": sha_file(out_path),
                  "measurement": result["measurement"],
                  "c2_base": {k: v["summary"] for k, v in base_control.items()},
                  "c2_arms": {s: {a: {"exit": v["exit"], "summary": v["summary"]}
                                  for a, v in rows.items()} for s, rows in commands.items()},
                  "c3_surfaces_before": result["c3"]["surfaces_before_frozen"]["summary"],
                  "c3_surfaces_after": result["c3"]["surfaces_after_candidate"]["summary"],
                  "c3_pins_before": result["c3"]["pins_before"]["summary"],
                  "c3_pins_after": result["c3"]["pins_after_scratch_repin"]["summary"],
                  "omp_binary": {k: result["c3"]["omp_binary"][k] for k in
                                 ("size", "mtime_ns", "sha256", "strings_bytes", "strings_sha256",
                                  "candidate_call_count", "candidate_unique_pair_count",
                                  "candidate_ids", "baseline_loader_group_ids", "candidate_id_parity",
                                  "current_allowlist_ids", "version_18_12_2_present")},
                  "git_and_binary_provenance": history}, indent=2, sort_keys=True))
