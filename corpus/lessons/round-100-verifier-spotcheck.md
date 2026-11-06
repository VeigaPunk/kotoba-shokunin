author: hyaku closure (non-author integrator, @m_zfl)

# Round 100 verifier spot-check (non-author closure of kotoba round 100)

This closes lane-round kotoba r100. Round base `7b449a637c03d9b4c43a81b4df37cb38c2ea89ee` (the
round-99 spot-check commit); lane tip `3ded52e71eaae0c4eb87e9095453326edcd8069d`. Report:
`.ufo/reports/round-100/kotoba.md` in the fleet repo. The reviewer did not author the round and
changes no lane-authored file. No lane gate or lane counter was executed (PROTOCOL § Gate standard,
Closure consequence): gate and counter verdicts below are verified from committed receipts, and
each one says so. The reviewer ran the plain measurements (git/grep/wc/sha256/curl/census/a
standalone `re` probe of the two regex lines) itself on 2026-11-06.

Driver digest (copied from `.ufo/watchdog.log`, which can change):

```
2026-11-06T12:08:46-03:00 launch kotoba round=100 pgid=4071777 driver=hyaku-inline attempt=1
2026-11-06T13:43:08-03:00 complete kotoba round=100; hyaku-inline attempt=1
```

## Step-1 conformance

- **Report.**
  - Fleet commit `bbf28f9207c8a7c0ff0eddf39aa8bf3891268865`, author
    `kotoba-shokunin <kotoba@shokunin.local>`, committed 13:42:35-03:00.
  - That is after the last lane commit `3ded52e7` (13:41:27) and before the `complete` line
    (13:43:08). Its author date (12:57:40) precedes the landing; the report body cites `3ded52e7`,
    which did not exist then, so the author date is the colocated working-copy timestamp, not a
    filing time. Note only.
  - `## SHONEN` heading present once, 4 lines, one per box, all `[~]`.
- **Hashes.** For each of `d1e1170d…`, `03a98eb7…`, `8a650a48…`, `50c3ff5a…`, `3ded52e7…` and the
  base `7b449a63…`: `git cat-file -t` → `commit`; `git merge-base --is-ancestor <h> master` → true.
  `git log 7b449a63..3ded52e7` lists exactly those five round commits, all authored by
  `kotoba-shokunin`.
- **Pushed and clean.**
  - `jj-lane.sh state` → `state branch=master local=3ded52e7… remote=3ded52e7… ahead=0 behind=0
    head=detached tracked=0 untracked=0`.
  - `git status --porcelain` → empty.
  - `git ls-remote origin refs/heads/master` → `3ded52e71eaae0c4eb87e9095453326edcd8069d`.
- **Prompt.** `.ufo/prompts/kotoba-round-100.md` is committed by the lane identity (`ade1893a`).
  A `diff` of its lines 1–140 against `kimi-shokunin/templates/round-prompt.md` (after substituting
  `{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`) shows only the repo-path and `{{AXES}}` placeholder
  substitutions. §§ 1, 2, 2b, 3, 4, 5 are verbatim and the hyaku addendum § 6 starts at line 141.
  The prompt carries the template contract.
- **Conformance notes** (status-neutral):
  - **N1.** The planner seat was again held by the L1 because the wave validator rejects the
    `planner` role (disclosed; a validator gap for the operator, not lane debt).
  - **N2.** A seat left `ExecAnchorR100/` in the scratch dir; the L1 removed it (disclosed). Nothing
    was left in the lane root.
  - **N3.** `versions.html` (a Read the Docs "version not found" page, 12:35) sits untracked in the
    fleet root; the lane disclaims it with a 0-mention sweep. Unattributed; operator to clear.

## Claims

### C1 — depth: the dispatch-prompt checker's self-test kills the six frozen survivors t01..t06

Re-measured by the reviewer (plain git/grep over committed bytes):

- `git diff -U0 7b449a63 8a650a48 -- verifiers/verify_dispatch_prompts.py | grep '^@@'` →
  `@@ -1783,0 +1784,144 @@ def self_test() -> int:`: one insert-only hunk of 144 lines inside
  `self_test()`. `git diff 7b449a63 3ded52e7 -- verifiers/verify_dispatch_prompts.py | grep -c
  '^-[^-]'` → `0`; production code unchanged. Agrees with `receipts/landing/identity.txt`.
- `grep -oE 'r100-t[0-9]{2}'` over that diff → exactly `r100-t01`..`r100-t06`.
- The arms reach the named surfaces: 24 added lines mention `main(`, `run_checks(`, `EnvError`,
  `read_text`, `is_dir` or `exit_code`.
- The instruments are frozen: blob ids of `verifiers/fixtures/round-100/selftest-kills.py`
  (`40a33ea9…`) and `anchor-lists.py` (`bf6aa5da…`) are equal at `d1e1170d`, `8a650a48` and
  `3ded52e7`.

Evidence-verified (committed receipts; the counter was not run):

- **Before.** `receipts/redbefore-c1-base.txt` (added in the freeze `03a98eb7`, before the
  landing): `C1 targets killed 0 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment
  decoys held 6 of 6; code decoys held 6 of 6` → `C1-PREDICATE-UNMET`, `rc=1`; `--rules v5` same.
- **After.** `receipts/landing/c1-v62.txt` (`# rev: 8a650a48…`): `C1 targets killed 6 of 6 (run
  errors 0); …; comment decoys held 6 of 6; code decoys held 6 of 6` → `C1-PREDICATE-MET`, `rc=0`;
  `c1-rulesv5.txt` same.
- **Carried kill rules at the landing.** `r95c1` 3/3, `r96c1` 11/11, `r97c1` 13/13, `r98c1` 9/9,
  `r99c1` 12/12, all `PREDICATE-MET rc=0`.
- **Self-test.** `receipts/landing/dp-selftest.txt` (rev `8a650a48`): `0 failure(s) over 168
  assertions`, `rc=0` (154 → 168). `dp-boxproof.txt`: `boxes proven 2`, `rc=0`.

**Verdict: depth `improved`.** Values match the report: 0 → 6 of 6 at the frozen landing revision.
MutTesterDispatchR100's 13 of 16 new surviving mutants are disclosed and routed; they do not
falsify the frozen predicate.

### C2 — consistency (calibration sub-axis): comma-list line anchors read as anchors

Re-measured by the reviewer:

- **The fix line is the frozen admitted change.** `git diff 7b449a63 8a650a48 --
  verifiers/verify_skill_checklist.py | grep -E '^[-+].*re\.match'` →
  `-    m = re.match(r"^(.+\.\w+):\d+(-\d+)?$", tok)` /
  `+    m = re.match(r"^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$", tok)`. The only other deletions are the
  4-line `GOVERNANCE_CORRECTIONS` row `(3598, …, "SCORECARD.md", 529,
  "corpus/lessons/round-80-verifier-spotcheck.md:30,37", …)`; hunks: `@@ -493,4 +492,0`,
  `@@ -1148 +1144`, `@@ -2787,0 +2784,79 @@ def self_test()`. Battery: one appended pin
  `94d11c7a…`, earlier pins kept.
- **The regex behaves as documented.** A standalone `re.match` probe (old / new): `a.md:30,37`
  False/True; `a.md:5-9,12` False/True; `a.md:30` True/True; `a.md:30,,37`, `a.md:30,abc`,
  `a.md:5-` False/False. The live subject `SCORECARD.md:529` at the tip carries
  `corpus/lessons/round-80-verifier-spotcheck.md:30,37`, and that file has 72 lines.
- **What made the landing red.** `git show 8a650a48:LOG.md | sed -n 3619p` → `- **Wave
  r100-w1:** … reports in .ufo/waves/round-100/w1/.`; `git ls-tree -r --name-only 8a650a48 --
  .ufo/waves/round-100/w1 | wc -l` → `0`, and at `50c3ff5a` → `113`. `git diff --stat 8a650a48
  3ded52e7` touches only `.ufo/waves/round-100/**`, `LOG.md` (+6) and `SCORECARD.md` (+2); no
  `verifiers/` byte changes after the landing.

Evidence-verified (receipts; the gates and counter were not run):

- **Before.** `receipts/c2-base.txt` (freeze `03a98eb7`): `C2 mismatches 8 of 28; gate GREEN;
  self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok` → UNMET `rc=1`.
- **Controls.** p1, f1–f5 (freeze) all `C2-PREDICATE-UNMET rc=1`; p1 reads `mismatches 0 of 28`,
  f2 is refused by `revert mutant SURVIVED` alone, as the plan requires.
- **At the landing `8a650a48`** (`receipts/landing/c2.txt`, `# rev: 8a650a48…`): `C2 mismatches 0
  of 28; gate RED; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery FAIL` →
  **`C2-PREDICATE-UNMET` `rc=1`**; red line `gate FAIL governance.citation_resolves: … LOG.md:3619:
  '.ufo/waves/round-100/w1/' does not resolve`; `battery.txt`: `tip battery exit 0: 5 of 6`, `rc=1`.
- **At the record tip `50c3ff5a`** (`c2-record-tip.txt`): `… gate GREEN; … battery ok` →
  `C2-PREDICATE-MET` `rc=0`; `battery-record-tip.txt`: `6 of 6`, `rc=0`.

**Ruling: the landing revision binds; C2 does not verify.** The frozen plan
(`plans/round-100.md:102` target `anchor-lists.py <landing rev>`; `:129` kill rule "unmet if the
landing reading is not `C2-PREDICATE-MET` rc 0") names the landing reading, the lane's own table
names `8a650a48` as the landing, and its own receipt at that revision reads UNMET. The record tip
turns MET only by committing the evidence the landing's LOG line cited — a post-landing repair the
frozen kill rule does not admit. Precedent: kotoba r98 closure (MANIFEST rounds[1416]), C2 unmet at
the landing reading as frozen → honest stop. The surface improvement is real and persists at the
tip (8 → 0 mismatches, correction row retired, tip battery 6 of 6), but it is not credited to this
claim. **consistency: `unchanged`** (no verified move at the binding revision; no regression at the
tip).

### No harm

- `git diff 7b449a63 3ded52e7 -- SCORECARD.md` adds three paragraphs (Round 100 axis annotations,
  After round 100, the C2 reading disclosure); 0 deleted lines, no score cell changed.
- Deleted / added non-blank lines over the round: `LOG.md` 0/12 (3612 → 3628 lines),
  `SCORECARD.md` 0/3, `corpus/README.md` 0/2, `corpus/QUALITY.md` 0/1, `corpus/SOURCES.md` 0/4.
- `SKILL.md`, `PROVINCE.md`, `knowledge/` untouched (`git diff --stat` empty).
- The landing-commit red was healed at the record tip with data only; at the tip every gate the
  battery runs exits 0. No owned axis is harmed.

| axis | verdict |
|---|---|
| depth | improved |
| consistency | unchanged |
| coverage | unchanged |
| operability | unchanged |
| freshness | unchanged |
| calibration | unchanged |
| adjacency | unchanged |

**Round verdict: not admitted — `rejected-honest-stop`** (C2 did not verify at its frozen binding
revision; no axis harmed). The lane reported both readings and left the ruling to the closure.

## Discernment spot-check (`corpus/lessons/round-100.md` § Gate)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S282 Python pathlib (`release/3.15.2`) | admit (tier A, mined; supersedes S276) | `curl -sS -L https://docs.python.org/release/3.15.2/library/pathlib.html` → `200 270630`; sha256 `090f3b03b648c271f4d810f0c37a51b2b54ebbdaa8130466d695e836e7a399ca`; `sed -n 1362,1367p`, `1323,1326p` | agree | Byte count and digest equal the Gate's access record. Lines 1364–1366 read "False will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a directory." (22 words, after folding the code span); the `exists` contrast at 1325–1326 is present. The pair is exactly what makes `t04-dircheck-exists` a real defect. The release pin over the rolling `/3/` alias is the correct repair. |
| Sphinx `literalinclude :lines:` | reject (not rowed) | `curl -sS -L https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html` → `200 170372`; sha256 `2c4152a6…f2b` (differs from both recorded digests); `sed -n 1419,1422p` | agree | Line 1421 carries `:lines:` "line numbers (comma separated numbers)" split over code spans, as quoted. A third distinct digest at the same byte count confirms the per-response rotation the Gate reports. A doc-build inclusion filter is not the authority for a repo citation-anchor convention, and the lane's own `SKILL.md`/`QUALITY.md` usage already grounds the form. |

- **Newly written SOURCES row re-opened.** S285 ptrace(2): `curl` → `200 104833`, sha256
  `69cd309e…bd35`, equal to the Gate record and to S279's. `sed -n 1513,1520p` shows step (4) with
  "the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target
  process" at 1518–1520 (16 words ≤ 25). S282's quote (22 words, `wc -w`) also verified above.
  All four new rows' `teaches` open `supersedes S0NN —`; rows `grep -cE` 207 → 211; malformed rows
  (`NF!=13`) 0.
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba` → `rc=0`, 35 `W04` (34 before + S285's shared URL), no
  other finding, last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`.

## Trend verdicts

- **expansion: unchanged.** `knowledge/` untouched; the four rows re-pin existing grounds.
- **quality: improved.** C1 verified (six more frozen behaviours killed, production bytes
  unchanged), and three rolling-alias rows (S253, S270, S276) are superseded by digest-stable
  release-pinned rows, plus S279 by a full-conjunction quote, with no admitted entry failing its
  re-check.
- **discernment: improved.** Both sampled gate decisions (one admit, one reject) agree on re-open;
  six pre-data controls including a positive control were committed; post-freeze counter holes and
  the landing-commit UNMET were disclosed rather than folded into the tip reading.

## Routed defects (the lane fixes these next round)

1. **Landing order.** Mistake 2 (`governance-cell-cites-uncommitted-wave-evidence`) cost C2: commit
   cited wave evidence with or before the line that cites it, and run the sandboxed checklist gate
   on the exact landing tree before the landing commit. The C2 surface change now on master may
   only be credited by a future round's own frozen claim, never by re-reading round 100.
2. **v7 counter for g11/g16** — carried from round 98 (third deferral; CriticClaimR100 D3).
3. **C1 survivors.** 13 of 16 MutTesterDispatchR100 mutants survive (state/fleet substrate paths,
   the `--json` payload's pass/fail/na fields).
4. **anchor-lists v1 holes F1–F3** (MutTesterAnchorR100): source-sniffing arm, `SELFTEST_RE`
   window past `self_test`, code-computed pin. Any reuse needs conjuncts refusing them.
5. **Rejected-row taste record (advisory).** The Sphinx rejection lives only in the lesson; a
   `rejected` S286 row would keep it in the registry (contract v1 `status`).
6. **Seat hygiene** (N2): seats must clean their own scratch dirs.

## Operator note (promotion is operator-owned)

All four SHONEN boxes stay `[~]`. To this non-author, box 1 (the checklist gate reads 11 PASS at the
tip, evidence-verified from `receipts/landing/c2-record-tip.txt`) and box 4 (`PROVINCE.md`
unchanged; ConnectorOverlapR100 Part 2) appear checkable from outside. The reviewer neither writes
nor recommends a promotion here.
