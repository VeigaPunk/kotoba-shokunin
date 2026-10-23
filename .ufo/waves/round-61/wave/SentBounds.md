# Round 61 — bounds audit / SentBounds

## Scope and disposition

I inspected the bounds relevant to my seat and wrote only this report. I did not edit lane/fleet/sibling files, `.ufo/state`, a Git index, or jj state; did not dispatch or invoke another runtime; and installed nothing. I read the round plan, the r60 spot-check §7–§8, the r60 v2 controls and ExecKeyForms evidence, the C2 base receipt, and the lane helper source in the fleet tree. The requested fleet/lane status reads were run. I did not run a post-wave audit or any `jj op log` command: this wave is already active, no pre-wave bounds receipt was supplied, and an op log alone cannot authenticate that an operation came from the helper.

## Findings

### Medium — No pre-wave baseline makes status drift non-attributable

**Exploit path.** A seat (or unrelated concurrent actor) can create a fleet-root file, alter runtime state, modify a sibling checkout, or leave lane worktree changes; a post-wave `status` listing shows the result but cannot establish whether it predated dispatch. Conversely, a file already dirty at the baseline can mask a later write to the same path. The fleet has many existing dirty/untracked paths in this capture, and the lane already has three wave report files.

**Evidence.** At `2026-10-23T19:11:32Z` (date captured with `date -u '+%Y-%m-%dT%H:%M:%SZ'`, exit 0), the specified read-only status commands returned the following. These are captured outputs, not proof of who wrote any path.

Command: `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all`  
Exit: `0`

```text
 M .scratch/goal-20261023-hyaku-24h.md
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
 M .ufo/waves/hyaku/PHASE5.md
 M scripts/hyaku/hyaku.env
?? .omp/mcp.json
?? .ufo/reports/round-29/kama.md
?? .ufo/reports/round-36/mori.md
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? 0
?? AGENTS.md
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/__pycache__/append-closure.cpython-314.pyc
?? scripts/hyaku/__pycache__/wave-live.cpython-314.pyc
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? wb2.html
?? write
?? xc.xml
```

Command: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain=v1 --untracked-files=all`  
Exit: `0`

```text
?? .ufo/waves/round-61/wave/ScribeC3.md
?? .ufo/waves/round-61/wave/ScribeShonen.md
?? .ufo/waves/round-61/wave/ScribeSkillReg.md
```

The three lane paths are report-shaped and may be expected seat output; this status alone does not establish their author. The fleet paths likewise cannot be attributed by porcelain. In particular, the fleet `.ufo/state/*` and `.ufo/watchdog.log` modifications are visible but are **not** evidence that this seat wrote them.

**Impact.** A post-only check can report current drift but cannot distinguish a seat violation from pre-existing/operator activity. It cannot certify the entire interval since dispatch without a frozen pre-wave snapshot of fleet status, lane status, runtime-file bytes, sibling HEADs/statuses, and the initial jj operation ID.

**Smallest remediation.** Before a wave, the L1 should commit a baseline receipt containing those exact values, plus the explicit allowed lane paths (L1 integration paths and each seat's declared report path). Post-wave, compare against that receipt; never treat current `git status` as author attribution.

### High — `jj op log` does not prove helper provenance

**Exploit path.** A seat directly invokes a mutating jj command in the lane instead of using `scripts/hyaku/jj-lane.sh`. The resulting jj operation is present in the operation history, but the operation record does not establish which executable/process invoked jj. A direct command can produce the same class of operation as the helper, so merely seeing an operation description is not evidence it came from the helper.

**Evidence.** The lane helper source `/home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh` validates scope/identity and performs `jj file track`, `metaedit`, `commit`, and `bookmark set` (lines 654–715); its only durable per-lane state use shown in the source is the helper lock under `$HOME/.local/state/shokunin-hyaku` (lines 133–142). A targeted search of that helper for `log`, `op log`, and `STATE` found no operation-provenance ledger. The helper's user-facing `landed <hash>` contract establishes remote landing, not the caller of each jj transaction. No `jj op log` was run in this assignment.

**Impact.** An op-log review can find suspicious/new jj operations, but cannot honestly classify all of them as “from helper” versus “not from helper.” A helper-only claim based on descriptions, commit identity, or timestamps is fabricated provenance.

**Smallest remediation.** For this round, enumerate new jj op IDs and mark origin unverified unless there is independent helper-invocation evidence. For future rounds, have the trusted L1/orchestrator record each helper invocation and returned landed hash in a precommitted receipt, including the before/after op IDs and exact helper path/hash/argv; compare the operation interval to those receipts. A receipt produced only by a seat-controlled process is not independent provenance.

## L1 integration audit script text

The following is the proposed two-phase, read-only-after-capture audit. `capture` must run **before dispatch** and its JSON must be frozen by the L1. `audit` requires a newline-delimited `allowed-lane-paths.txt` containing only exact lane-relative report paths and paths actually landed by the L1. The script compares changes against the baseline; it treats runtime and sibling drift as findings, not proof of actor. New jj ops are always emitted as `UNVERIFIED_ORIGIN` because the current helper does not attest them. The current round has no supplied pre-wave baseline, so this script cannot retroactively certify earlier changes.

```python
#!/usr/bin/env python3
# bounds_audit.py capture BASELINE.json
# bounds_audit.py audit BASELINE.json allowed-lane-paths.txt
# Read-only wrt Git/jj. Run capture before seat dispatch; freeze its output.
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

FLEET = Path("/home/vgpnk/Projects/shokunin")
LANE = FLEET / "kotoba-shokunin"
BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"


def cmd(args):
    return subprocess.run(args, check=True, stdout=subprocess.PIPE).stdout


def git_status(repo):
    raw = cmd(["git", "-C", str(repo), "status", "--porcelain=v1",
               "--untracked-files=all", "-z", "--no-renames"])
    result = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        # With --no-renames, porcelain-v1 -z records are `XY SP path NUL`.
        result[os.fsdecode(item[3:])] = os.fsdecode(item[:2])
    return result


def runtime_files():
    # Include fleet and lane runtime trees plus watchdog files, including ignored files.
    roots = [FLEET / ".ufo/state", LANE / ".ufo/state",
             FLEET / ".ufo/watchdog.log", LANE / ".ufo/watchdog.log"]
    found = {}
    for root in roots:
        key = str(root)
        found[key] = "present" if root.exists() or root.is_symlink() else "missing"
        paths = [root]
        if root.is_dir() and not root.is_symlink():
            paths.extend(sorted(root.rglob("*")))
        for path in paths:
            rel = str(path)
            if path.is_symlink():
                data = os.fsencode(os.readlink(path))
                found[rel] = "symlink:" + hashlib.sha256(data).hexdigest()
            elif path.is_file():
                found[rel] = "file:" + hashlib.sha256(path.read_bytes()).hexdigest()
            elif path.is_dir():
                found[rel] = "directory"
            elif not path.exists():
                found[rel] = "missing"
    return found


def sibling_state():
    result = {}
    for repo in sorted(FLEET.glob("*-shokunin")):
        if not repo.is_dir() or repo == LANE:
            continue
        top = Path(os.fsdecode(cmd(["git", "-C", str(repo), "rev-parse",
                                   "--show-toplevel"]).rstrip(b"\n"))).resolve()
        if top != repo.resolve():
            raise RuntimeError(f"not a repository root: {repo} -> {top}")
        head = os.fsdecode(cmd(["git", "-C", str(repo), "rev-parse", "HEAD"]).strip())
        result[str(repo)] = {"head": head, "status": git_status(repo)}
    return result


def jj_ops():
    raw = cmd(["jj", "--ignore-working-copy", "--repository", str(LANE),
               "op", "log", "--no-graph", "--limit", "1000",
               "-T", 'id.short() ++ "\\t" ++ description ++ "\\n"'])
    rows = []
    for line in raw.decode("utf-8", "replace").splitlines():
        op_id, sep, description = line.partition("\t")
        if sep:
            rows.append({"id": op_id, "description": description})
    if not rows:
        raise RuntimeError("jj op log returned no parseable rows")
    return rows


def snapshot():
    branch_tip = os.fsdecode(cmd(["git", "-C", str(LANE), "rev-parse", BASE]).strip())
    ops = jj_ops()
    return {
        "base": branch_tip,
        "fleet_status": git_status(FLEET),
        "lane_status": git_status(LANE),
        "runtime": runtime_files(),
        "siblings": sibling_state(),
        "jj_op_head": ops[0]["id"],
    }


def changed_paths(before, after):
    return sorted(path for path in set(before) | set(after)
                  if before.get(path) != after.get(path))


def main():
    if len(sys.argv) < 3:
        raise SystemExit("usage: bounds_audit.py capture BASELINE.json | audit BASELINE.json allowed-lane-paths.txt")
    mode, baseline_path = sys.argv[1], Path(sys.argv[2])
    if mode == "capture":
        baseline_path.write_text(json.dumps(snapshot(), indent=2, sort_keys=True) + "\n")
        print(f"captured baseline: {baseline_path}")
        return 0
    if mode != "audit" or len(sys.argv) != 4:
        raise SystemExit("usage: bounds_audit.py audit BASELINE.json allowed-lane-paths.txt")

    before = json.loads(baseline_path.read_text())
    allowed = {line.strip() for line in Path(sys.argv[3]).read_text().splitlines()
               if line.strip() and not line.lstrip().startswith("#")}
    now = snapshot()
    failures = 0

    fleet_delta = changed_paths(before["fleet_status"], now["fleet_status"])
    for path in fleet_delta:
        print(f"FLEET_DRIFT {path}: {before['fleet_status'].get(path)!r} -> {now['fleet_status'].get(path)!r}")
        failures += 1
    if not fleet_delta:
        print("FLEET_STATUS unchanged")

    lane_delta = changed_paths(before["lane_status"], now["lane_status"])
    for path in lane_delta:
        if path in allowed:
            print(f"LANE_ALLOWED {path}: {before['lane_status'].get(path)!r} -> {now['lane_status'].get(path)!r}")
        else:
            print(f"LANE_DRIFT_OUTSIDE_L1_PATHS {path}: {before['lane_status'].get(path)!r} -> {now['lane_status'].get(path)!r}")
            failures += 1
    if not lane_delta:
        print("LANE_STATUS unchanged")

    runtime_delta = changed_paths(before["runtime"], now["runtime"])
    for path in runtime_delta:
        print(f"RUNTIME_WRITE_OR_REMOVAL {path}: {before['runtime'].get(path)!r} -> {now['runtime'].get(path)!r}")
        failures += 1
    if not runtime_delta:
        print("RUNTIME_STATE unchanged")

    sibling_delta = changed_paths(before["siblings"], now["siblings"])
    for path in sibling_delta:
        print(f"SIBLING_REPO_DRIFT {path}")
        failures += 1
    if not sibling_delta:
        print("SIBLING_REPOS unchanged")

    ops = jj_ops()
    new_ops = []
    for op in ops:
        if op["id"] == before["jj_op_head"]:
            break
        new_ops.append(op)
    else:
        raise RuntimeError("baseline jj op ID is not in the current op log (truncated or rewritten)")
    for op in new_ops:
        print(f"UNVERIFIED_ORIGIN jj-op {op['id']} {op['description']}")
    if new_ops:
        print("JJ_HELPER_PROVENANCE NOT PROVABLE from op log alone; reconcile against independent helper receipts")
        failures += 1
    else:
        print("JJ_OP_LOG no operations after baseline")

    print(f"bounds audit findings={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

**Interpretation / limits of the script:** an unchanged baseline path does not prove no write occurred and was restored before audit; a changed path does not identify its writer. The sibling scan covers immediate `*-shokunin` repositories under the fleet root. `jj op log` enumeration is an anomaly detector only: current helper evidence is insufficient for automatic helper-origin attribution. Do not call an audit with no frozen pre-dispatch baseline a clean pass.

## Verification actually performed

- `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all` — output pasted above; exit 0; date captured 2026-10-23T19:11:32Z.
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain=v1 --untracked-files=all` — output pasted above; exit 0; date captured 2026-10-23T19:11:32Z.
- No other audit commands, builds, tests, linters, jj commands, or installations were run.

Installs: no installs  
Blockers: no pre-wave status/runtime/sibling/jj-op baseline was supplied, and current helper behavior does not provide independent per-op provenance; a complete historical seat-bounds pass cannot be claimed from this snapshot.  
Produced: a scoped bounds findings report and a two-phase read-only audit script proposal for L1 integration.
