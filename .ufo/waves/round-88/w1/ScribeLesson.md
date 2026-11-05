# ScribeLesson — scoped findings (round-88 w1, kotoba lane)

Scope: `corpus/lessons/round-88.md`, `corpus/QUALITY.md` (Q80 only), `LOG.md` (append only), R87-D7 correction, this seat's summary. Base `223ae62424f8ab1eb365d733eb648d6228ddd7e8`, tip `4df1e8005016c75390a5e06b209462df58c95918`.

## Done

- Lesson written with provenance, `## Gate` (S257 admitted from `ScoutUpstream/SOURCE_ROW.md`, sha256 `976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e`, 7-word located quote, `Spot-check result: pending — non-author closure`), `## Mistakes` (R87-D7, captured-by none), `## Considerthese` (proposal 4 → Q80, proposal 3 carried), `## Sources` (S257), `## Assimilation: none`.
- Q80 appended to `corpus/QUALITY.md` (line 99), citing `considerthese/2026-10-26.md:18`.
- R87-D7 correction appended to `LOG.md` (3374–3377, `supersedes LOG.md:3315`). Sweep `receipts/mistake-sweep.sh`: before `stale=1 unannotated=1` exit 1; after `stale=1 unannotated=0` exit 0.
- Round-88 LOG entry appended (3379–3390), recording the two claims with their observed state and controls by command name.

## Findings

1. **C1 not measured by its owner.** `C1_READY` and `FORGERY_READY` never appeared in the 45-minute window (2640 s). `w1/ExecLiveBound/` absent; `w1/ExecForgeryWorlds/` empty. The v2 counter file exists (sha256 `506a2ba9…4b9beb`) with no receipt. The only forged-world numbers are reviewer receipts (`ReviewerC1/receipts/indep_C1_worlds.txt`: `10, 10, 9, 9` of 12, exit 1) and the r87 control on the same revisions (`12 of 12`, exit 0). The "forged-world rejection 4 of 4" milestone has no owning receipt.
2. **C2 counter fails its own control.** `check_r86_routed_repairs_v2.py --self-test` → `1 failure(s) over 16 assertions`, exit 1, arm `w_added_red` (`ExecMonotoneD5/receipts.txt` §1). The added red under an already-DRIFT name passes D5 (§3, `w_added`). Cause: monotone compares name sets only. Tip reads `5 of 5`, exit 0, but the frozen controls do not pass, so C2 is not admitted by its own predicate.
3. **Handoff contract violated.** `C2_READY` (06:04) holds the predicate sentence and an `F1 disclosed` note in place of a sha256, written while the self-test was red. The handoff rule says it is written only after the self-test passes. Treated as not-ready; reported, not repaired.
4. **Location dependence of the integrity gate.** The lane tip reads 5 reds in the plan's frozen table; ExecMonotoneD5's scratch clone of the same commit reads 6 (adds `corpus.pointers.report_dead`). `CriticFalsify` C2-S5 records the same effect. The tip red set is not a stable count across checkouts.
5. **Silencing and re-recording attacks pass the v2 gate.** `CriticFalsify/attacks.md` C2-S2 (in-place silencing passes (i) and (ii)) and C2-S3 (`corpus-baseline.json` re-record heals three reds) are not covered by the frozen controls. Reported for the L1; not in the LOG as verified.
6. **Sweep wording in the seat item does not match the committed sweep.** The literal `grep -n '5 of 5' LOG.md | grep 'C2'` matches seven lines (2481, 2510, 2582, 2715, 2849, 2852, 3315) and cannot go green after an append-only annotation. The committed `mistake-sweep.sh` (looks for `supersedes LOG.md:<n>`) is the one that turns green; used in the lesson and the LOG entry.
7. **Self-introduced sweep failure, corrected before commit.** The first correction draft quoted the stale sentence verbatim; the sweep then reported `stale=2 unannotated=1` (exit 1). The quote was reworded (LOG.md 3376). Also corrected my integrity sentence (LOG.md 3385). Both are my own uncommitted appended lines; no other record was edited.
8. **Attack seats.** `ReviewerC1`, `ReviewerC2`, `CriticFalsify` have output on disk; `MutTesterV2` has no output directory at write time. Q80 applies to the round at closure, not at this write.

## Not done / out of scope

- S257 row in `corpus/SOURCES.md`: owned by ScribeSources. The census E11 check on `used-by` is pending until `corpus/knowledge/omp-root-semantics-round88.md` lands (ScribeEntry).
- The L1 runs the committed sweep receipts and the no-harm battery; this seat did not run any counter, census or integrity gate.
- The S257 sha256 and quote are the scout's record; not re-fetched by this seat.

## Tooling

No installs or updates by this seat.

## Scratch

`/fast/scratch/hyaku/kotoba-r88/ScribeLesson/` created and removed at yield.
