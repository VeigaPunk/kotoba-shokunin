# ScoutTipReds — the three carried red gates of the tip battery (round-98 w1)

Seat: `ScoutTipReds` (read-only scout; no lane edits, no patch, no READY file).
Question: for each red gate of `verifiers/check_tip_battery.py` at
`63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`, record the exact failing lines and exit code,
find the cause (check id, file:line, introducing round/commit), classify it
(a) stale baseline/pin the lane can re-record honestly, (b) real content defect,
(c) gate defect, and give the minimal fix with a falsifiable before→after and the
do-nothing control that would NOT meet it.

Method: a fleet-shaped sandbox clone of the lane at the freeze commit
(`git clone --shared --no-checkout`, checkout `63cd48d9`, every fleet-root entry
including dotfiles symlinked next to it), the gates run from the sandbox root, and
`check_tip_battery.py --repo <sandbox> --rev 63cd48d9 --fleet /home/vgpnk/Projects/shokunin`
for the official reading. Read-only git (`log -S`, `blame`, `show`, `ls-tree`) for the
introducing commits. A second sandbox was used for the fix experiments; the lane was
never written.

## 1. Base reading (exact)

`python3 -B verifiers/check_tip_battery.py --repo . --rev 63cd48d9 --fleet /home/vgpnk/Projects/shokunin`
→ rc 1:

```
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.5s
gate verifiers/check_assertion_floors.py exit 0 wall 221.5s
gate verifiers/verify_skill_checklist.py exit 1 wall 2.1s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.3s
gate verifiers/verify_corpus_independent.py exit 1 wall 1.0s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 3 of 6
```

Per-gate, same sandbox:

- `verify_skill_checklist.py` rc 1 — 10 PASS, **1 FAIL** in the fleet-shaped sandbox
  (`FAIL governance.citation_resolves: evaluated 1642 — correction LOG.md:2621 SCORECARD.md:158
  '.ufo/reports/round-60/kotoba.md': names no live red subject; LOG.md:2881: '...before-tip-battery-win-dot.txt'
  does not resolve; LOG.md:2947: same; LOG.md:2958: '.ufo/reports/round-82/kotoba.md' does not resolve
  … (+14 more); 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s)
  excused, 3 recorded correction(s) excused`). Full 18-entry list in
  `ScoutTipReds/governance-failures-base.txt`. A **bare clone** (fleet root not symlinked)
  additionally reds `trigger.citation_resolves` on `../.ufo/reports/round-7/kotoba.md`
  (line 590) — a measurement artifact, not a lane defect; the counter builds the
  fleet-shaped sandbox and does not see it.
- `verify_corpus_integrity.py` rc 1 — `4/9 checks pass; DRIFT: corpus.index.tracked_files,
  corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total,
  corpus.pointers.commit_unresolvable`; observed 201/165/71/7/1 vs expected 172/127/59/0/0.
- `verify_corpus_independent.py` rc 1 — its own derivation: `unindexed=7 DRIFT`,
  `commit_unresolvable=1 DRIFT`; the three count rows are `observe … INFO` (it does **not**
  read `verifiers/corpus-baseline.json`).

## 2. Cause per gate

### 2.1 `verify_skill_checklist.py` / `governance.citation_resolves` (18 bad entries = 1 pinned-row problem + 17 live entries, 16 unique subjects)

| # | subject | cause | class |
|---|---|---|---|
| 1 | `correction LOG.md:2621 SCORECARD.md:158 …: names no live red subject` + `SCORECARD.md:161 '.ufo/reports/round-60/kotoba.md'` | the frozen `GOVERNANCE_CORRECTIONS` row pins the round-60 row at `SCORECARD.md:158`; round 82 (**747a07c**, 2026-11-01) inserted 3 lines above it, so the row is at **161**. The LOG.md:2621 notice itself is unchanged (append-only). | (a) stale pin |
| 2 | `LOG.md:2881` `…before-tip-battery-win-dot.txt` | round 82 (**747a07c**) cites a receipt name that never existed; round 83 (**84c2963**) appended the correction notice at `LOG.md:2947` naming `before-tip-battery-win.txt`, but no `GOVERNANCE_CORRECTIONS` row was added and the horizon (`2723`) is below 2947. | (a) missing pin |
| 3 | `LOG.md:2947` same token | the correction notice itself names the stale token in backticks, so it is a live dead subject; the gate's meta-finding exclusion needs double quotes on the token's own line. | (a) missing pin |
| 4 | `LOG.md:2958`, `SCORECARD.md:186` `.ufo/reports/round-82/kotoba.md`; `SCORECARD.md:204` round-83; `SCORECARD.md:222`, `LOG.md:3360`, `SCORECARD.md:646` round-84 `kama`; `LOG.md:3353`, `LOG.md:3561` `.ufo/watchdog.log`; `LOG.md:3512` `.ufo/l0-questions.md`; `SCORECARD.md:531` round-81 (×2) | repo-rooted `.ufo/...` citations of files that exist at the **fleet** root (`../.ufo/...`); the lane's own convention (round-57/58/59 rows, and the round-65 correction rows) is the `../` hop. Introduced by 747a07c (r82), 84c2963/d84c7c8 (r83), 462d240 (r84), d1c0318 (r87), 010d3b8 (r92), 38361a2 (r97). | (b) content |
| 5 | `SCORECARD.md:527` `.ufo/wapes` | typo for `.ufo/waves`; introduced at **23e838c** (round-81 record, 2026-10-28). | (b) content |
| 6 | `SCORECARD.md:538` `verifiers/check_description_render.py` | the round-85 counter was removed at **47085c8** (round-85: "quarantine killed unsafe C1 experiment and remove active gate"); the bytes live at `.ufo/waves/round-85/frozen/check_description_render.py`. | (b) content |
| 7 | `SCORECARD.md:529` `corpus/lessons/round-80-verifier-spotcheck.md:30,37` | the file exists; `strip_token_dressing` (verify_skill_checklist.py:1079-1084) strips `file.md:42` and `file.md:42-45` but not the comma list `:30,37`, so the whole token is tested as a path. The gate's own docstring says a line anchor does not change the path. | (c) gate defect |

Timeline (receipt `timeline.txt`): the checklist gate is **green at the round-81 base
`b2842231`** (0 bad) and **red at the round-81 record `23e838c`** (4 bad), then grows
monotonically: 747a07c 8, 84c2963 10, d84c7c8 11, 462d240 12, 43ae91c 13, ff4bf3f 13,
801dd9b 17, 693be9c 17, 63cd48d9 18. So "red since round 96" is not the record: the gate
has been red since **round 81's record commit**, and round 82 added the pinned-row drift.

### 2.2 `verify_corpus_integrity.py` (4/9)

- `corpus.index.tracked_files` 201 ≠ 172, `corpus.pointers.report_total` 165 ≠ 127,
  `corpus.pointers.commit_total` 71 ≠ 59 — **stale baseline**: `verifiers/corpus-baseline.json`
  was last re-recorded at **ff4bf3f** (round-87, head `e03f9e2`); rounds 88–97 added corpus
  files without a re-record. Class **(a)**.
- `corpus.index.unindexed` = 7 — the round-91…97 `-verifier-spotcheck.md` files have no
  coverage-map row in `corpus/README.md` (rows exist for r80–r90). Counts per rev
  (`unindexed-timeline.txt`): r88 1, r89 0, r90 3, r91 0, r92 1, r93 2, r94 3, r95 4,
  r96 5, r97 6, freeze 7 — cumulative since round 92. Class **(b)**.
- `corpus.pointers.commit_unresolvable` = 1 — `corpus/lessons/round-81.md:8`:
  `commit \`8b1cc1b00a9322cd8e231d87e015e1d75d20adc1\``, a dead-clone test commit absent
  from lane and fleet; `verifiers/external-commits.json` pins only `7bb48f21…` (a real
  third-repo commit), so the token is not external. Class **(b)** (or a new exemption class,
  see F4).

### 2.3 `verify_corpus_independent.py` (rc 1)

Same two zero-mode defects (7 unindexed, 1 unresolvable commit). It is an independent
implementation and does **not** compare the equal-mode counts (they print `INFO`), so the
baseline re-record does not affect it. Class **(b)** only.

## 3. Minimal fix (measured in the scratch sandbox; lane untouched)

1. `corpus/README.md`: append 7 coverage-map rows for `lessons/round-91…97-verifier-spotcheck.md`.
2. `corpus/lessons/round-81.md:8`: write the hash in the quoted form (`commit "8b1cc1b…"`)
   so both gates classify it as context. `commit_total` then reads 70, not 71.
3. `verifiers/corpus-baseline.json`: re-record the three equal-mode expectations to the
   observed 201/165/70 from `--no-baseline --json` **after** step 1–2.
4. `verifiers/verify_skill_checklist.py`: re-pin row 2621 `SCORECARD.md 158 → 161`; add 14
   correction rows for the remaining subjects; raise `GOVERNANCE_CORRECTIONS_HORIZON` to the
   new notice line; extend `strip_token_dressing` to `^(.+\.\w+):\d+(?:[,-]\d+)*$`.
5. `LOG.md`: append one correction notice naming each stale → corrected pair (stale tokens
   double-quoted so the notice line adds no live subjects; corrected tokens backticked so
   they resolve).
6. `verifiers/check_tip_battery.py`: admit the new `verify_skill_checklist.py` blob
   (`fe472e8696bcf209fb671f56e1e3dd4d3f913fbf` for this exact fix) in `INSTRUMENT_PINS`.

Measured after (receipt `fix-measured.txt`):

```
verify_skill_checklist rc 0  PASS governance.citation_resolves: evaluated 1640 — … 18 recorded correction(s) excused
verify_skill_checklist --self-test rc 0  0 failure(s) over 1864 assertions
verify_corpus_integrity  rc 0  9/9 checks pass
verify_corpus_independent rc 0  exit 0
tip-battery guards 5 of 5 at the fix rev (with the pin admission)
tip battery exit 0: 6 of 6, rc 0 (fix rev 795059aa, receipt tip-battery-fix.txt;
  registry 0, floors 0 wall 250.3s, checklist 0, integrity 0, independent 0, sweep 0)
```

Do-nothing / partial controls (receipt `controls.txt`), each NOT meeting the after:

| control | reading |
|---|---|
| base `63cd48d9` | checklist rc 1, 18 bad; integrity 4/9; independent rc 1; battery 3 of 6 |
| checklist regex-only | rc 1, **17** bad |
| checklist re-pin-only | rc 1, **16** bad |
| checklist all rows + notice, no regex fix | rc 1, **1** bad (`:30,37`) |
| checklist all rows + regex, no notice | rc 1, **29** bad (rows fail: past horizon/absent + 14 live) |
| corpus content-only (no baseline) | integrity 6/9 rc 1 (3 equal drifts); independent rc 0 |
| corpus baseline-only, re-recorded to the unfixed 201/165/71 | integrity 7/9 rc 1 (unindexed + commit_unresolvable); independent rc 1 |
| corpus baseline-only, re-recorded to the post-fix 201/165/70 but content reverted | integrity 6/9 rc 1 (unindexed, commit_total, commit_unresolvable) — shows the baseline must be taken after the content fix |
| checklist fix without the `INSTRUMENT_PINS` admission | `FAIL instrument-pin: … blob fe472e86… is not a pinned blob` |

## 4. Findings

- **F1 (timeline understated).** The round-97 closure says the three reds are "carried from
  round 96" (spot-check lines 149, 205) — true as far as it goes, but the onset is much
  earlier. `verify_skill_checklist` has been red since round-81's record commit `23e838c`
  (2026-10-28); the corpus pair has been red at every measured rev since at least the
  round-81 base `b2842231`, with a best reading of 8/9 at the round-87 baseline re-record
  `ff4bf3f` (only `commit_unresolvable`), and a re-drift from round 88. The item's framing
  "red since round 96" is therefore a lower bound, not the onset.
- **F2 (fleet-shaped sandbox is load-bearing).** In a bare clone `trigger.citation_resolves`
  fails on `../.ufo/reports/round-7/kotoba.md` and `report_dead` reads 1; with the fleet
  root's `.ufo` symlinked both pass. The counter builds the fleet-shaped sandbox correctly;
  a direct lane run or a bare-clone run over-reports the red set.
- **F3 (instrument disagreement).** The corpus gates resolve `.ufo/...` lane-first then
  fleet-root (round-66 note), while the checklist gate requires repo-root resolution and the
  `../` hop. 11 unique subjects (12 entries; `SCORECARD.md:531` carries the token twice) are
  the same citation class the corpus gates accept; the lane's written convention is the
  `../` form, so the content is wrong, but the inconsistency is a gate-design finding.
- **F4 (fragile line pins).** A correction row pins a line number in a mutable governance
  file; round 82's 3-line insertion above line 158 broke the round-65 row. A token+file
  locator (or an append-only offset) would survive insertions; the current design re-breaks
  on any insertion above a pinned row.
- **F5 (`:30,37` gate defect).** `strip_token_dressing` documents "a citation may carry a
  line anchor (`file.md:42`)", but only accepts `:N` and `:N-M`; the comma list `:N,M` is a
  false red. One-line regex fix; the gate's self-test still passes (1864 assertions).
- **F6 (normalized red).** From round 92 the lane's landing no-harm rule accepts "the base
  DRIFT set" as a conjunct (LOG round-92), so the corpus red never heals; the zero-mode
  expectations are not re-recordable, only fixable.
- **F7 (pin admission is load-bearing).** Editing `verify_skill_checklist.py` re-reds the
  battery's `instrument-pin` guard unless the new blob is admitted in
  `check_tip_battery.py`; measured both ways.
- **F8 (timeout risk).** `check_assertion_floors.py` takes ~220 s against the 280 s
  `GATE_TIMEOUT_S`; round-94's landing battery already recorded `exit none wall 280.0s
  (timeout after 280 s)`. A landing run on a loaded host can read 5 of 6 without any gate
  being red.
- **F9 (baseline ordering).** The round-81 quote fix moves `commit_total` 71 → 70; a
  baseline re-record taken before the content fix re-reds `commit_total` (measured).

## 5. Remaining unknowns

- Whether the lane will edit `corpus/lessons/round-81.md` (a historical lesson) or instead
  add a new exemption class for absent-by-construction test-world commits; the one-line
  quote is the minimal fix, the exemption class is the record-preserving alternative.
- The full tip battery at the fix rev is measured: `guards 5 of 5; tip battery exit 0: 6 of 6`,
  rc 0 (`tip-battery-fix.txt`), so the six-file fix set is sufficient in the scratch clone.
- Whether the round-98 landing will spend an instrument-pin admission on
  `verify_skill_checklist.py`; the fix cannot green the checklist gate without it.

## 6. Receipts

`ScoutTipReds/`: `tip-battery-base.txt`, `gate-checklist-base.txt`,
`gate-integrity-base.txt`, `gate-independent-base.txt`, `governance-failures-base.txt`,
`timeline.txt`, `unindexed-timeline.txt`, `controls.txt`, `fix-measured.txt`,
`tip-battery-fix.txt`.
