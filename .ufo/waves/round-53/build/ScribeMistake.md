Result: DONE — drafted lesson row M41 (`stale-baseline`) for round 52's un-re-recorded corpus baseline, with a finding-set delta check shown red at `0c9180a6` (`commit_total` new) and green after a defect-2-shaped re-record; candidate (b) yielded no unmined error strong enough to rank above it.

## 1. Candidate choice (calibration)

Both candidates were swept. **(a) chosen.** (b) produced one imprecise sentence (F3 below) that no claim turns on, and it concerns the same gate as (a).

(a) Round 52 left `verifiers/corpus-baseline.json` un-re-recorded after its own corpus files landed. Measured, pointer-rich, and its "why nothing caught it" is demonstrable at instrument level (§4, §5).

(b) Disagreements or overclaims in `corpus/lessons/round-52-verifier-spotcheck.md` (the closure) or `.ufo/reports/round-52/kotoba.md` (the round). I re-measured every statement bearing on the corpus gate plus the spot-check's no-harm block: all hold except F3. Nothing there outranks (a).

Dedupe against the lessons already mined. M36 is a superseded claim left standing in a sibling file (fixed by a registry of superseded phrases). M39 is prose describing a counter wider than its code. M40 is an unrun check recorded as passed. M41 is none of these: a **persisted expectation set that no rule binds to the tree it grades**, sitting inside a gate whose exit code cannot express "new finding", so the round's own no-harm test — exit-code equality — reported it as harmless while it happened.

## 2. Measurements (each revision's own instrument, its own baseline)

Run in the sandbox clone, one worktree per revision (`git worktree add`), 2026-10-22:

```
python3 -B wt-c8579a4c/verifiers/verify_corpus_integrity.py --repo wt-c8579a4c   → exit 1
  5/9 checks pass; DRIFT tracked_files 73/72, unindexed 1, report_total 47/46, report_dead 3
python3 -B wt-0c9180a6/verifiers/verify_corpus_integrity.py --repo wt-0c9180a6   → exit 1
  5/9 checks pass; DRIFT tracked_files 75/72, report_total 47/46, report_dead 3, commit_total 31/30
python3 -B wt-e78dff66/verifiers/verify_corpus_integrity.py --repo wt-e78dff66   → exit 1
  4/9 checks pass; DRIFT tracked_files 76/72, unindexed 1, report_total 49/46, report_dead 5, commit_total 31/30
```

Same pass count at round-52 base and head, different finding set: `unindexed` resolved (1 → 0), `commit_total` new (30 → 31). At the round-53 base the count drops to 4/9, and `unindexed_detail = ['corpus/lessons/round-52-verifier-spotcheck.md']` — the closure's own file, landed after the baseline's last record.

`report_dead_detail` at `e78dff66` is five repo-relative fleet-report pointers, all inside closure spot-checks: `round-48` (2), `round-51` (1), `round-52` (2). That matches the plan's "5 fleet-report pointers".

The 31st citation: exactly one new `commit` citation token appears between `c8579a4c` and `0c9180a6` — the token `4c003a4b` at `corpus/knowledge/mcp-server-instructions-round52.md:75` (round 52's plan-commit citation inside its own new knowledge entry). My tokenizer counts 35 → 36 instances where the gate prints 30 → 31, so the two exclude different shapes; the location is an inspection of the only new token, not arithmetic on the gate's number.

## 3. Drafted row (the lesson table's exact shape, paste-ready)

```markdown
| M41 | `stale-baseline` | The corpus baseline was not re-recorded after round 52's own files landed, and the lane's no-harm test could not see it. Each revision's own gate: `c8579a4c` 5/9 pass, DRIFT `tracked_files` 73/72, `unindexed` 1, `report_total` 47/46, `report_dead` 3; `0c9180a6` 5/9 pass, DRIFT `tracked_files` 75/72, `report_total` 47/46, `report_dead` 3, `commit_total` 31/30 — same pass count, changed set (`unindexed` fixed, `commit_total` new). The new citation is the token `4c003a4b` at `corpus/knowledge/mcp-server-instructions-round52.md:75`. The round's report (`.ufo/reports/round-52/kotoba.md:89-90`) and LOG.md:2437 read the constant count as no-harm ("5 of 9, the same count as base" in the report; the same count in parentheses at LOG.md:2437) and carried the re-record; the lesson's routed-defect queue (`corpus/lessons/round-52.md:100-116`) never lists it, so only the outside closure routed it (`corpus/lessons/round-52-verifier-spotcheck.md:125`). The lane's own falsify seat had the cause and set it aside: "does not flip the gate's exit (still 1) so it is not a \"harm\" by the stated criterion" (`.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md:79`). The baseline's `notes` log ends at `round50_entry` (`verifiers/corpus-baseline.json:64`) although the last expectation change is `59903b2` (round 51), which moved two `expect` values and added no note. At the round-53 base `e78dff66` the gate reads 4/9 with five DRIFTs; `unindexed` is `corpus/lessons/round-52-verifier-spotcheck.md`. | `none` — no criterion or gate binds the baseline's expectations to the tree they grade, and the round's no-harm test is exit-code equality (`.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md:79`; the closure repeats it, `round-52-verifier-spotcheck.md:92`; PROTOCOL.md:380 defines the gate's verdict as `0` clean, `1` failed), which a new finding inside an already-red gate never moves. PROTOCOL.md:393 states the principle ("a gate grades the tree it runs on") and `verifiers/verify_corpus_integrity.py:103` states it for this baseline ("the baseline is a property of the tree being checked"), but neither is enforced; rounds 48-51 re-recorded by practice only (LOG.md:2374, :2396). Q01-Q31 contain no baseline-freshness or finding-delta criterion. | `verifiers/check_gate_finding_delta.py`: runs the gate as it stands at each revision and exits 1 when head has a DRIFT check id base did not. Shown able to fail: `python3 -B verifiers/check_gate_finding_delta.py --repo <clone> --base c8579a4c --head 0c9180a6` → `new: corpus.pointers.commit_total`, exit 1; control `--base c8579a4c --head c8579a4c` → `new: none`, exit 0; green after a re-record of the shape routed defect 2 asks for: `--base e78dff66 --head 81d3e5a` → `new: none; resolved 3`, exit 0; `--self-test` 0 failures over 9 assertions. Rule it grounds: no-harm for a red gate is a finding-set comparison, never an exit code or a pass count (Q32, drafted; number [INFERENCE]). Limit: detects a missing re-record, not a fitted one, so the re-record diff must still name each moved `expect` and its cause in `notes` — review work, not instrumented here. |
```

## 4. The fix, shown able to fail

Script: `/fast/scratch/hyaku/kotoba-r53/ScribeMistake/verifiers/check_gate_finding_delta.py`, 171 lines, sha256 `1c41414eff46bdf7850963c98535c09a86f90bde1764da18f92159ad6853f41a` (full text in the appendix; it was written and run only in my sandbox clone — the lane was not touched).

It extracts each revision with `git archive`, gives the extracted tree a temporary Git index (`git read-tree` into `GIT_INDEX_FILE`, under the system temp), runs **that tree's own** gate with that tree's own baseline, and compares the DRIFT ids. Nothing in the clone's index or working tree is written.

Arms run, 2026-10-22:

| arm | command | observed | exit |
|---|---|---|---|
| red (the mistake) | `--repo . --base c8579a4c --head 0c9180a6` | `base drift 4, head drift 4` / `new: corpus.pointers.commit_total` / `resolved: corpus.index.unindexed` | 1 |
| control | `--repo . --base c8579a4c --head c8579a4c` | `new: none` / `resolved: none` | 0 |
| green after | `--repo . --base e78dff66 --head sim-rerecord` (`81d3e5a`) | `base drift 5, head drift 2` / `new: none` / `resolved: tracked_files, commit_total, report_total` | 0 |
| self-test | `--self-test` | `self-test: 0 failure(s) over 9 assertions` | 0 |

The green arm is a simulation: `81d3e5a` is a commit in my sandbox clone at `e78dff66` that changes exactly the three `expect` values the round-53 re-record must move (`tracked_files` 76, `report_total` 49, `commit_total` 31) and nothing else. It does not contain the sibling resolver patch (`ExecCorpusIntegrity.patch`), so its head still carries `unindexed` and `report_dead`; those are red at base too, so they are not new. With that patch integrated the head set only shrinks, so the same command stays green. **[INFERENCE]** — the real round-53 head does not exist yet.

Why red here and green after, in one line: the check asks whether a finding appeared that the baseline did not have; the re-record is the act that makes the baseline the landed tree's property, and after it no equal-mode DRIFT can appear that the base did not already carry.

## 5. Why no gate or rule caught it before the report

1. The gate cannot say it. `verify_corpus_integrity.py:1325` is `return 1 if drift else 0`; there is no carried/new distinction, so exit 1 means the same thing for a finding that predates the round and one it introduced.
2. The no-harm test is exit equality, applied explicitly. `ExecGateMatrix.md:79` writes the cause and the dismissal in one paragraph: it did not re-record, and "does not flip the gate's exit (still 1) so it is not a \"harm\" by the stated criterion". The closure used the same test (`round-52-verifier-spotcheck.md:92`, "no exit flip").
3. The aggregate could not move either. The report printed "5 of 9, the same count as base" (`kotoba.md:89`) and LOG.md:2437 printed the same count in parentheses. A constant pass count over a changed set is the one number that hides this class.
4. The fault harness is blind for the same reason: `fault_injection_corpus.sh` exits 1 at base and head because the lane corpus is already red (`ExecGateMatrix.md:75`).
5. No rule binds the baseline. PROTOCOL.md:393 states the principle; `verify_corpus_integrity.py:103` states it for this file; Q01-Q31 hold no baseline-freshness or finding-delta criterion; rounds 48-51 re-recorded by convention (`LOG.md:2374`, `:2396`), which nothing enforces.
6. The lane's own queue dropped it. The report and LOG carried the re-record in prose, and the lesson's routed-defect queue (`corpus/lessons/round-52.md:100-116`) does not list it; only the outside closure did (`round-52-verifier-spotcheck.md:125`, defect 2). The round-53 plan then reconstructed it from the closure, not from the lane.

## 6. Findings

- **F1 — measured, the row's core.** Base and head of round 52 read the same 5/9 with different finding sets; `commit_total` appears only at head (30/30 → 31/30). Commands and outputs in §2. Pointer: row M41.
- **F2 — the new citation.** One new `commit` citation token, `4c003a4b` at `corpus/knowledge/mcp-server-instructions-round52.md:75`. Pointer: §2.
- **F3 — imprecise in the round's own record (not mined, too weak for a row).** `.ufo/reports/round-52/kotoba.md:89-90` and `LOG.md:2437` attribute the `tracked_files` drift to "this round's new files and pointers"; at the round's own base `c8579a4c` the gate already read `tracked_files` 73 against `expect` 72, so one of the three excess files predates the round (the round added two, 73 → 75). The closure repeated the set change without noting the pre-existing drift either (`round-52-verifier-spotcheck.md:69-72`). No claim turns on it. Routed as an observation for the L1, not as M41-adjacent text to correct.
- **F4 — the baseline's audit trail is short by one round.** `verifiers/corpus-baseline.json` `notes` ends at `round50_entry` (`:64`), yet the last expectation change is `59903b2` (round 51), which moved `tracked_files` 69 → 72 and `report_total` 44 → 46 with no note. The file cannot say when it was recorded, and a review of a re-record has nothing to diff against. This is the reason the row's fix keeps "name each moved `expect` and its cause" as review work.
- **F5 — the lane knew the cause.** `ExecGateMatrix.md:79` names it and calls it low severity for the exit-code reason; `:23` shows the gate row with `commit_total` bolded at head. Nothing in the round's lesson or queue promotes it.
- **F6 — the round-53 base is worse, not equal.** 4/9 with five DRIFTs at `e78dff66`, versus 5/9 at both round-52 revisions; the extra DRIFT is `unindexed` = the round-52 closure file. This is the ping-pong the plan routes around: each closure lands a corpus file after the round's re-record.
- **F7 — spot-check statements I re-measured and confirm.** "5 of 9 at both base and head" (true, §2); "`unindexed` was fixed" (true, 1 → 0); "`commit_total` is new" (true, 30/30 → 31/30); "the only self-test change is a rise, `surfaces` 119 → 129" and "floor 129" (`verify_surfaces.py --self-test` → `0 failure(s) over 119 assertions` at `c8579a4c`, `... over 129` at `0c9180a6`, exit 0 both; `floors-registry.json:42` floor 129). No disagreement found.
- **F8 — the sibling repair does not close the gap.** `.ufo/waves/round-53/build/ExecCorpusIntegrity.md` resolves the five fleet-report pointers and indexes the closure file, and leaves `corpus-baseline.json` unchanged, deferring the re-record to the L1 ("re-record the corpus baseline last"). The delta check is what makes "last" checkable; without it the next closure file restarts the same cycle.

## 7. Calibration and limits

- Verified by running: the three gate runs (§2), the probe's four arms (§4), `verify_surfaces.py --self-test` at two revisions, `floors-registry.json` floor, `git log/show` reads for `59903b2` and the baseline notes.
- **[INFERENCE]**: that Q32 is the next criterion number (Q31 is the last row of `corpus/QUALITY.md`); that the real round-53 head will be green under the delta check (only the simulation commit was measured).
- Not run, and therefore not claimed: the C1 opencode re-pin counter, the C2 always-on counter, `check_assertion_floors.py`, `fault_injection_corpus.sh`, the sibling `ExecCorpusIntegrity.patch` (not integrated), any harness or census command. I did not re-measure the round-52 claims beyond the corpus gate and the surfaces no-harm figures above.
- The row does not claim the baseline was *wrong*; the expectations were stale relative to the tree, which is the class. The measurable difference between "stale" and "correct after a re-record" is exactly what the delta check reports.
- No quote over 25 words was taken from any fetched page; no network source was opened for this item (all evidence is in the lane or the fleet report tree).

## 8. Surfaces

- Written: this report only (`.ufo/waves/round-53/build/ScribeMistake.md`).
- Sandbox: `/fast/scratch/hyaku/kotoba-r53/ScribeMistake` (clone at `3bb0a7a3`), worktrees `wt-c8579a4c`, `wt-0c9180a6`, `wt-e78dff66`, `wt-sim` (branch `sim-rerecord`, commit `81d3e5a`), and the probe `verifiers/check_gate_finding_delta.py`. No jj command was run; no install or upgrade was made.
- Lane cleanliness, checked with `git status --porcelain` after writing this report: the only path I created is this report, under an untracked `.ufo/waves/round-53/` tree. The same command also shows five modified tracked files I did not touch — `corpus/README.md`, `verifiers/check_mcp_instructions.py`, `verifiers/verify_corpus_independent.py`, `verifiers/verify_corpus_integrity.py`, `verifiers/verify_surfaces.py` — plus untracked `verifiers/fixtures/surfaces/strings-omp-unresolved-group.txt`. They are other seats' work, not mine, and they mean the lane working tree is **not** the tree my numbers describe: every measurement in §2 and §4 ran on revision trees extracted from the sandbox clone at `3bb0a7a3`.
- Out of scope, and unchanged by me: the counters (`check_opencode_repin.py`, `check_alwayson_boxes.py`, `verify_corpus_integrity.py`, `corpus-baseline.json`), `corpus/lessons/round-53.md` (absent at the time of writing), the QUALITY table, the sibling patches. The row is a draft for the L1 to place; the probe is a sandbox artifact for the L1 to lift or reject.

## Appendix — the probe as run

```python
#!/usr/bin/env python3
"""Report a gate's finding-set delta between two revisions.

Why: a gate that is already red at base cannot report a new defect by exit
code. Round 52 read `verify_corpus_integrity.py` as "5 of 9, the same count as
base" while its DRIFT set changed (unindexed resolved, commit_total new), so
nothing in the lane's no-harm checks saw the new finding.

This instrument runs the gate as it stands *at each revision* (that tree's own
instrument against that tree's own baseline, per PROTOCOL § Gate standard
"Two evidences": a gate grades the tree it runs on) and compares the DRIFT
check ids. Exit 1 when head has a DRIFT id base did not have.

    python3 -B verifiers/check_gate_finding_delta.py --repo <clone> \
        --base c8579a4c --head 0c9180a6 [--json] [--self-test]

Exit codes: 0 no new finding, 1 new finding, 2 environment unreadable.

Scope, stated so the number is readable: it detects a *missing* re-record. It
cannot detect a dishonest re-record that writes the observed value into the
baseline's `expect`; that stays a review of the re-record diff.
"""

import argparse
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

PY = sys.executable


def delta(base, head):
    """Pure model: (new, resolved) from two sets of finding ids."""
    return sorted(set(head) - set(base)), sorted(set(base) - set(head))


def findings(tree, gate, env=None):
    proc = subprocess.run(
        [PY, "-B", str(tree / gate), "--repo", str(tree), "--json"],
        capture_output=True, text=True, env=env,
    )
    if proc.returncode not in (0, 1) or not proc.stdout.strip():
        print(f"could not evaluate {tree}: exit {proc.returncode}: {proc.stderr.strip()}",
              file=sys.stderr)
        raise SystemExit(2)
    doc = json.loads(proc.stdout)
    red = [r["check"] for r in doc["results"] if r["verdict"] != "PASS"]
    return sorted(red), proc.returncode


def extract(repo, rev, dest):
    """Extract a revision's files without .git; links are skipped (corpus/ has none)."""
    archive = subprocess.run(
        ["git", "-C", str(repo), "archive", rev], capture_output=True, check=True,
    )
    with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
        members = [m for m in tar.getmembers() if not (m.issym() or m.islnk())]
        tar.extractall(dest, members=members)
    return dest


def revision_env(repo, rev, index, tree):
    """Env that makes `git -C tree` read `rev`'s index and the clone's objects.

    Writes only the temp index: the clone's index and working tree are untouched.
    """
    env = dict(os.environ)
    env.update({
        "GIT_DIR": str((repo / ".git").resolve()),
        "GIT_WORK_TREE": str(tree),
        "GIT_INDEX_FILE": str(index),
    })
    subprocess.run(
        ["git", "-C", str(repo), "read-tree", rev],
        capture_output=True, check=True, env=env,
    )
    return env


def run(repo, base, head, gate, as_json):
    with tempfile.TemporaryDirectory(prefix="finding-delta.") as tmp:
        tmp = Path(tmp)
        btree = extract(repo, base, tmp / "base")
        htree = extract(repo, head, tmp / "head")
        benv = revision_env(repo, base, tmp / "base.index", btree)
        henv = revision_env(repo, head, tmp / "head.index", htree)
        bset, bcode = findings(btree, gate, benv)
        hset, hcode = findings(htree, gate, henv)
    new, resolved = delta(bset, hset)
    if as_json:
        print(json.dumps({
            "base": {"rev": base, "drift": bset, "exit": bcode},
            "head": {"rev": head, "drift": hset, "exit": hcode},
            "new": new, "resolved": resolved,
        }, indent=1, sort_keys=True))
        return 1 if new else 0
    print(f"gate finding delta {base} -> {head}: base drift {len(bset)}, head drift {len(hset)}")
    print(f"  new: {', '.join(new) if new else 'none'}")
    print(f"  resolved: {', '.join(resolved) if resolved else 'none'}")
    print(f"finding delta: new {len(new)}, resolved {len(resolved)}")
    return 1 if new else 0


def self_test():
    failures = []

    def eq(label, got, want):
        if got != want:
            failures.append(f"{label}: got {got!r}, want {want!r}")

    eq("delta/identical", delta(["a", "b"], ["a", "b"]), ([], []))
    eq("delta/new", delta(["a"], ["a", "b"]), (["b"], []))
    eq("delta/resolved", delta(["a", "b"], ["b"]), ([], ["a"]))
    eq("delta/mixed", delta(["a", "b"], ["b", "c"]), (["c"], ["a"]))
    eq("delta/empty-base", delta([], []), ([], []))

    # exit-code arm over two synthetic trees whose stub gate prints a fixed set
    with tempfile.TemporaryDirectory(prefix="finding-delta-selftest.") as tmp:
        root = Path(tmp)
        for name, ids in (("base", ["a"]), ("head", ["a", "b"]), ("same", ["a"])):
            tree = root / name
            (tree / "verifiers").mkdir(parents=True)
            (tree / "verifiers/gate.py").write_text(
                "import json, sys\n"
                f"print(json.dumps({{'results': [{{'check': i, 'verdict': 'DRIFT'}} for i in {ids!r}]\n"
                f"                     + [{{'check': 'ok', 'verdict': 'PASS'}}]}}))\n"
                "sys.exit(1)\n"
            )
        stub = Path("verifiers/gate.py")

        def stub_findings(tree):
            return findings(tree, stub)

        eq("arm/new-finding-red", delta(stub_findings(root / "base")[0], stub_findings(root / "head")[0]),
           (["b"], []))
        eq("arm/no-new-finding", delta(stub_findings(root / "base")[0], stub_findings(root / "same")[0]),
           ([], []))
        red_exit = 1 if delta(stub_findings(root / "base")[0], stub_findings(root / "head")[0])[0] else 0
        green_exit = 1 if delta(stub_findings(root / "base")[0], stub_findings(root / "same")[0])[0] else 0
        eq("arm/exit-red", red_exit, 1)
        eq("arm/exit-green", green_exit, 0)

    print(f"self-test: {len(failures)} failure(s) over 9 assertions")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=False, default=".")
    ap.add_argument("--base")
    ap.add_argument("--head")
    ap.add_argument("--gate", default="verifiers/verify_corpus_integrity.py")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.base or not args.head:
        ap.error("--base and --head are required")
    return run(Path(args.repo).resolve(), args.base, args.head, Path(args.gate), args.json)


if __name__ == "__main__":
    sys.exit(main())
```
