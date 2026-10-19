#!/usr/bin/env python3
import copy
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd().resolve()
OUT = ROOT / ".ufo/round-46/evidence/g1/replays-final5/c2c3"
OUT.mkdir(parents=True, exist_ok=True)
LIVE_PATH = OUT / "live.json"
IND_PATH = OUT / "independent.json"
SCOPE = ROOT / "verifiers/harness-independent-scope.json"
COMPARATOR = ROOT / "verifiers/compare_harness_independent.py"
COMPARATOR_SNAPSHOT = OUT / "comparator.py"
CID = "omp.catalogue.found"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return sha_bytes(Path(path).read_bytes())


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout.strip()


def source_state():
    paths = [
        "LOG.md", "SCORECARD.md", "SKILL.md",
        "corpus/knowledge/harness-independent-round41-census.md",
        ".ufo/round-46/claims.json",
        "verifiers/compare_harness_independent.py",
        "verifiers/verify_harness_claims.py",
        "verifiers/verify_harness_independent.py",
        "verifiers/harness-independent-scope.json",
        "verifiers/floors-registry.json",
        "verifiers/baseline.json",
    ]
    return {
        "at_utc": now(),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
        "sha256": {p: sha(ROOT / p) for p in paths},
    }


def dump(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")


def json_bytes(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode()


def run_case(name, live_raw, independent_raw, expected_exit, expect_text, is_file=False):
    live_case = OUT / f"{name}.live.json"
    ind_case = OUT / f"{name}.independent.json"
    live_case.write_bytes(live_raw)
    ind_case.write_bytes(independent_raw)
    receipt = OUT / f"{name}.receipt.json"
    cmd = [sys.executable, "-c",
           "from pathlib import Path; import sys; p=Path(sys.argv.pop(1)); f=Path('verifiers/compare_harness_independent.py').resolve(); g={'__name__':'__main__','__file__':str(f)}; exec(compile(p.read_bytes(),str(f),'exec'),g)",
           str(COMPARATOR_SNAPSHOT),
           "--live-json", str(live_case), "--independent-json", str(ind_case),
           "--cwd", str(ROOT), "--scope-file", "verifiers/harness-independent-scope.json",
           "--expect-n", "28", "--no-stamp", "--json", "--receipt", str(receipt)]
    start = now()
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, timeout=90)
    end = now()
    (OUT / f"{name}.stdout").write_text(proc.stdout, encoding="utf-8")
    (OUT / f"{name}.stderr").write_text(proc.stderr, encoding="utf-8")
    combined = proc.stdout + proc.stderr
    ok = proc.returncode == expected_exit and expect_text in combined
    rec = {
        "name": name, "command": cmd, "cwd": str(ROOT),
        "started_utc": start, "ended_utc": end,
        "exit_code": proc.returncode, "expected_exit": expected_exit,
        "expected_text": expect_text, "assertion_pass": ok,
        "live_path": str(live_case.relative_to(ROOT)), "live_sha256": sha(live_case),
        "independent_path": str(ind_case.relative_to(ROOT)), "independent_sha256": sha(ind_case),
        "stdout_path": str((OUT / f"{name}.stdout").relative_to(ROOT)),
        "stdout_sha256": sha_bytes(proc.stdout.encode()),
        "stderr_path": str((OUT / f"{name}.stderr").relative_to(ROOT)),
        "stderr_sha256": sha_bytes(proc.stderr.encode()),
        "receipt_path": str(receipt.relative_to(ROOT)),
        "receipt_sha256": sha(receipt) if receipt.is_file() else None,
        "stderr": proc.stderr,
    }
    try:
        parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
    except ValueError:
        parsed = None
    if isinstance(parsed, dict):
        rec["headline"] = parsed.get("headline")
        rec["agreement"] = parsed.get("agreement")
        rec["reason"] = parsed.get("reason")
    print(f"{name}: exit={proc.returncode} expected={expected_exit} ok={ok} sha_live={rec['live_sha256']} sha_ind={rec['independent_sha256']}", flush=True)
    return rec


def raw_duplicate_member(payload, duplicate_key, duplicate_value=None):
    if duplicate_key == "results":
        rows = payload["results"]
        rest = {k: v for k, v in payload.items() if k != "results"}
        fields = [json.dumps(k, ensure_ascii=False) + ":" + json_bytes(v).decode()
                  for k, v in rest.items()]
        row_bytes = json_bytes(rows).decode()
        return ("{\"results\":" + row_bytes + ",\"results\":" + row_bytes +
                ("," + ",".join(fields) if fields else "") + "}\n").encode()
    rows = copy.deepcopy(payload["results"])
    chosen = next(i for i, row in enumerate(rows) if duplicate_key in row)
    row = rows[chosen]
    value = row[duplicate_key] if duplicate_value is None else duplicate_value
    row_members = [json.dumps(k, ensure_ascii=False) + ":" + json_bytes(v).decode()
                   for k, v in row.items() if k != duplicate_key]
    duplicate_json = json_bytes(value).decode()
    row_text = "{" + ",".join(row_members + [json.dumps(duplicate_key) + ":" + duplicate_json,
                                               json.dumps(duplicate_key) + ":" + duplicate_json]) + "}"
    row_texts = [row_text if i == chosen else json_bytes(item).decode()
                 for i, item in enumerate(rows)]
    rest = {k: v for k, v in payload.items() if k != "results"}
    fields = [json.dumps(k, ensure_ascii=False) + ":" + json_bytes(v).decode()
              for k, v in rest.items()]
    return ("{\"results\":[" + ",".join(row_texts) + "]" +
            ("," + ",".join(fields) if fields else "") + "}\n").encode()


def main():
    before = source_state()
    comparator = COMPARATOR.read_bytes()
    COMPARATOR_SNAPSHOT.write_bytes(comparator)
    snap_sha = sha(COMPARATOR_SNAPSHOT)
    live_cmd = [sys.executable, "-B", "verifiers/verify_harness_claims.py", "--json"]
    ind_cmd = [sys.executable, "-B", "verifiers/verify_harness_independent.py", "--json"]
    live_start = now()
    live = subprocess.run(live_cmd, cwd=ROOT, capture_output=True,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, timeout=120)
    live_end = now()
    LIVE_PATH.write_bytes(live.stdout)
    (OUT / "producer-live.stderr").write_bytes(live.stderr)
    ind_start = now()
    independent = subprocess.run(ind_cmd, cwd=ROOT, capture_output=True,
                                 env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, timeout=120)
    ind_end = now()
    IND_PATH.write_bytes(independent.stdout)
    (OUT / "producer-independent.stderr").write_bytes(independent.stderr)
    if live.returncode or independent.returncode:
        raise SystemExit(f"fresh producer failure: live={live.returncode}, independent={independent.returncode}")
    live_obj = json.loads(live.stdout)
    ind_obj = json.loads(independent.stdout)
    cases = []
    cases.append(run_case("control", live.stdout, independent.stdout, 0, "all checks agree, both instruments green"))

    mode = copy.deepcopy(live_obj)
    mode["modes"]["omp.offered.skills"] = "positive"
    cases.append(run_case("live-mode-shadow", json_bytes(mode), independent.stdout, 2, "live mode shadow"))
    verdict = copy.deepcopy(live_obj)
    verdict["verdicts"]["omp.offered.skills"] = "DRIFT"
    cases.append(run_case("live-verdict-shadow", json_bytes(verdict), independent.stdout, 2, "live verdict shadow"))
    summary = copy.deepcopy(live_obj)
    summary["observed"]["omp"]["template_bytes"] = summary["observed"]["omp"].get("template_bytes", 273) + 1
    cases.append(run_case("live-summary-shadow", json_bytes(summary), independent.stdout, 2, "live summary shadow"))
    dup_live = raw_duplicate_member(live_obj, "results")
    cases.append(run_case("duplicate-live-results-member", dup_live, independent.stdout, 2, "duplicate JSON member 'results'"))
    dup_ind_results = raw_duplicate_member(ind_obj, "results")
    cases.append(run_case("duplicate-independent-results-member", live.stdout, dup_ind_results, 2, "duplicate JSON member 'results'"))
    dup_ind_rederived = raw_duplicate_member(ind_obj, "re_derived")
    cases.append(run_case("duplicate-independent-re-derived-member", live.stdout, dup_ind_rederived, 2, "duplicate JSON member 're_derived'"))

    reason = copy.deepcopy(ind_obj)
    reason["scoped_out"][CID] = "fabricated blocker: not the committed reason"
    cases.append(run_case("scope-reason-drift", live.stdout, json_bytes(reason), 2, "scope reason drift"))
    evidence = copy.deepcopy(ind_obj)
    for channel in ("results", "rows"):
        row = next(row for row in evidence[channel] if row.get("check") == CID)
        row["evidence"] = "fabricated evidence contradicting the committed explanation"
    cases.append(run_case("scope-evidence-drift", live.stdout, json_bytes(evidence), 2, "scope evidence drift"))
    target = copy.deepcopy(ind_obj)
    target["scoped_out_probes"][CID]["target"] = "/tmp/g1-forged-probe-target"
    for channel in ("results", "rows"):
        next(row for row in target[channel] if row.get("check") == CID)["probe"]["target"] = "/tmp/g1-forged-probe-target"
    cases.append(run_case("scope-probe-target-drift", live.stdout, json_bytes(target), 2, "scope probe target drift"))

    after = source_state()
    manifest = {
        "started_utc": before["at_utc"], "ended_utc": after["at_utc"],
        "head": before["head"], "tree": before["tree"],
        "source_before": before["sha256"], "source_after": after["sha256"],
        "source_stable": before["head"] == after["head"] and before["tree"] == after["tree"] and before["sha256"] == after["sha256"],
        "comparator_snapshot": str(COMPARATOR_SNAPSHOT.relative_to(ROOT)),
        "comparator_sha256": snap_sha,
        "comparator_worktree_sha256_after": sha(COMPARATOR),
        "scope_sha256": sha(SCOPE),
        "producers": {
            "live": {"command": live_cmd, "started_utc": live_start, "ended_utc": live_end,
                     "exit_code": live.returncode, "stdout_sha256": sha(LIVE_PATH),
                     "stderr_sha256": sha(OUT / "producer-live.stderr")},
            "independent": {"command": ind_cmd, "started_utc": ind_start, "ended_utc": ind_end,
                            "exit_code": independent.returncode, "stdout_sha256": sha(IND_PATH),
                            "stderr_sha256": sha(OUT / "producer-independent.stderr")},
        },
        "cases": cases,
        "all_assertions_pass": all(case["assertion_pass"] for case in cases),
    }
    path = OUT / "matrix.json"
    dump(path, manifest)
    print(f"manifest={path.relative_to(ROOT)} sha256={sha(path)} stable={manifest['source_stable']} all_assertions_pass={manifest['all_assertions_pass']}")
    return 0 if manifest["all_assertions_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
