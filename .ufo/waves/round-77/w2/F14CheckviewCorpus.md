# F14CheckviewCorpus — r77 w2: corpus baseline & integrity gate falsification

Seat: leaf reviewer, round-77 wave 2. Attacked item: the landed r77 tip's corpus
baseline (`verifiers/corpus-baseline.json`) and the two corpus integrity gates
(`verify_corpus_integrity.py`, `verify_corpus_independent.py`), plus the frozen
C1/C2 counter pins and base receipts the freeze commit carries.

Axes I worked: depth, consistency, calibration, freshness, operability.

Environment: no tools installed (none needed); pacman untouched; no LSP server
answers for Python in this session, so all checks are text/execution checks on
named bytes (recorded per protocol). Scratch: /fast/scratch/hyaku/kotoba-r77/
F14CheckviewCorpus (the item prose says F14ReviewCorpus; the roster id and the
Report trailer say F14CheckviewCorpus — I used the latter for both), shared
clone of the lane, `git rev-parse --show-toplevel` asserted before every
worktree mutation; scratch removed before yield.

## Findings by severity

### 1. BLOCKER — claim data is not committed at the r77 tip

- Lane HEAD = `6523aced1ee0ebe07dca996213bdc645a6acbd1e` ("round-77: freeze plan,
  base receipts"). `git diff --name-status 2f675548..6523ace` = exactly 5 files:
  `plans/round-77.md` + 4 receipts (c1-base, c2-base, census-before,
  selftests-base). Nothing else.
- `git status --porcelain` shows 35 entries, all `??` untracked, all under
  `.ufo/waves/round-77/` (build/, w1/, w2/, receipts/, dispatch JSONs). No
  tracked lane file is modified.
- Consequence: at the tip both counters still read red — I re-ran them:
  - `python3 -B verifiers/check_desc_craft.py --rev 6523aced...` →
    `description craft backed 0 of 6`, exit=1 (same 6 per-conjunct failure lines
    as the committed c1-base receipt; also reproduced at base `2f675548`, exit=1).
  - `python3 -B verifiers/check_r75_routed_repairs.py --rev 6523aced... --work
    <scratch>/work` → `r75 routed repairs closed 0 of 4`, exit=1 (same 9 detail
    lines as the committed c2-base receipt; also at base `2f675548`, exit=1).
- C1 and C2 are therefore NOT landed; the w2 dispatch premise "attack the landed
  tip" is executable only for the freeze landing (pins + base receipts), not for
  the claims. Per the dispatch I report this as a blocker rather than scoring
  w1 scratch evidence as landed. Minimal repair: L1 lands landing-order steps 2–3
  (controls, then data + R76-D4 index/baseline) before any w2 verdict is scored;
  w2 reviewers re-run against the new tip.

### 2. CONFIRMED DEFECT (landed state, plan-disclosed) — both corpus gates red at the tip; R76-D4 un-landed

In a clean shared clone at `6523ace` (worktree = HEAD):

- `python3 -B verifiers/verify_corpus_integrity.py` → exit=1, 4 DRIFT:
  - `corpus.index.tracked_files: observed=146 expected=144`
  - `corpus.index.unindexed: observed=2` —
    `corpus/lessons/round-75-verifier-spotcheck.md`,
    `corpus/lessons/round-76-verifier-spotcheck.md`
  - `corpus.pointers.report_total: observed=102 expected=99`
  - `corpus.pointers.commit_total: observed=44 expected=43`
- `python3 -B verifiers/verify_corpus_independent.py` → exit=1 (unindexed is a
  zero-mode DRIFT; independent instrument agrees).
- Delta attribution: tracked +2 = the two closure-owned spot-checks (added at
  `b7f13f4` r75 closure and `2f67554` r76 closure, both without index rows);
  report pointers +3 = 2 in the r75 spot-check (`.ufo/reports/round-75/kotoba.md`
  ×2) + 1 in the r76 spot-check (`round-76/kotoba.md`); commit citations +1.
- This is exactly R76-D4 as routed by `corpus/lessons/round-76-verifier-spotcheck.md`
  §5 and disclosed in `plans/round-77.md` landing order step 3 ("index +
  baseline"). Not a plan contradiction: the repair is drafted but un-landed, and
  until it lands the plan's own base battery claim ("both exit 0 after the
  repair") is future tense, not fact. The w1 receipt
  `receipts/E06EntryVerify.corpus-integrity-with-entry.txt` honestly records the
  same red state with the draft data applied (`tracked_files: 148`, exit=1).

### 3. MINOR (w1 draft, operability) — refresh_baseline.sh dry-run always exits 3

`E10GateRepair.refresh_baseline.sh --dry-run` prints the correct old→new lines
(`tracked_files 144 -> 146`, `report_total 99 -> 102`, `commit_total 43 -> 44`,
"baseline untouched") and then fails its own post-condition —
"the re-recorded baseline does not read green (exit 1)" — because the
post-condition gate run executes even though nothing was written. Observed:
`dry-run-exit=3` on a tree whose real run then succeeded. Minimal repair: skip
the post-condition block when `dry_run=1` (or print "post-condition skipped
(dry-run)"). Harms no other axis: the real write path is fail-closed and
unaffected; defect is confined to the preview mode of a w1 draft file.

### 4. Repair path verified end-to-end (positive, with the fix the L1 must replicate)

In my clone: applied `build/E10GateRepair.readme-index-rows.patch` (clean apply,
adds the two index rows with the "indexed round 77" wording), then ran the
refresh script for real: preconditions held (toplevel assert, no untracked
corpus files, zero-mode clean), it wrote baseline 146/102/44 with
`measured_against.head 6523ace` and note key, and post-write I re-ran both gates
independently: integrity `9/9 checks pass`, exit=0; independent exit=0.
Guidance for the L1: at step 3 the same refresh must run on the FINAL data tree
(entry + lesson included, i.e. the 148-tracked world of E06's receipt) — the
script refuses (exit 2) over untracked corpus files or zero-mode drift, so all
new corpus files need their index rows in the same landing; it cannot be
recorded over drift, which is the correct behavior.

### 5. Frozen-counter integrity (positive)

- `git show HEAD:verifiers/check_desc_craft.py | sha256sum` =
  `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` (pin ✓);
  `check_r75_routed_repairs.py` = `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`
  (pin ✓); worktree blobs identical.
- Self-tests re-run in my clone: C1 `0 failure(s) over 53 assertions`, exit=0;
  C2 `0 failure(s) over 27 assertions`, exit=0 — matches
  `receipts/selftests-base.txt` byte-for-byte on the tail lines.
- Base receipts reproduce exactly (commands, measured-rev, failure lines, count
  lines, exit=1).

### 6. Cross-checks of w1 receipts (verify, don't trust)

- `receipts/E10GateRepair.gates.txt` base section lists the same 2 unindexed
  files and drift counts I measured at the tip — agrees with my run.
- `build/E04R2Receipt.gates-at-base-2f675548.txt`: integrity exit=1,
  independent exit=1 — agrees with my measurement at that rev (both spot-checks
  present). Its `gates-at-tip` exit=0/exit=0 is the r75-final-tip (`ac9f2951`,
  R2's measured rev) context, where the spot-checks do not yet exist; consistent
  with the baseline, not a contradiction of finding 2.
- `receipts/census-before.txt`: census ends `kotoba ok`, exit=0, with the known
  W04 duplicate-url warning set (incl. S213) — matches the plan.
- `SKILL.md`: 590 lines at the tip, zero diff vs base — within the ≤600 budget.

## Residual risk and verification gaps

- I did not run the full no-harm battery at a data-carrying tree (E12 owns the
  battery; the corpus-gate slice is covered here). I did not attack entry
  content, quotes, or the S213 page freshness (F03/S01/S02/F05 own those); my
  C1/C2 runs at the tip prove red-ness, not data correctness.
- The landing is live while I audited: `build/E10GateRepair.gates.txt` moved to
  `receipts/` mid-session. Findings are pinned to HEAD `6523ace`; if steps 2–3
  land, findings 1–2 must be re-checked at the new tip.
- No lane files were written; no git/jj mutation anywhere outside my scratch
  clone (worktree patch + baseline rewrite in the clone only; clone removed).

Report-file name note: the item prose names `F14ReviewCorpus.md`; the roster id
and the Report trailer name `F14CheckviewCorpus.md` — this file uses the trailer
name.

VERDICT: Landed r77 tip is honest (counter pins, self-tests and base receipts all reproduce; corpus-gate red state exactly as R76-D4 routed) but NO claim data is committed — C1/C2 remain 0-of-6/0-of-4 red at the tip; L1 must land steps 2–3 (controls, data + index/baseline repair, refresh re-run on the final tree) before w2 verdicts, and fix the refresh script's dry-run exit-3 defect.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F14CheckviewCorpus.md
