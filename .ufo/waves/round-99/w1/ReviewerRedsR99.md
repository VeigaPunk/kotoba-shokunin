# ReviewerRedsR99 — C2 patch laundering review (round-99 w1)

Seat: `ReviewerRedsR99` (reviewer; writes only this report + receipts under `ReviewerRedsR99/`).

## Assignment

Wait for `ExecRedsR99_READY`, then review `.ufo/waves/round-99/w1/ExecRedsR99/ExecRedsR99.patch`
against `plans/round-99.md` § C2 and the `carried-reds.py` header. For every appended
`GOVERNANCE_CORRECTIONS` row and the LOG.md notice line: is the subject genuinely stale (dead at
b53e209), is the corrected token the truth (same artefact the original context means), or is it an
excuse silencing a real defect (round-70 precedent: M118 / QUALITY Q64 — the LOG.md:2678 row that
"corrected" a removed directory to the record of its removal; withdrawn). Also: coverage-map rows
real index entries; round-81.md:8 quoting meaning-preserving; baseline re-record equal-mode and
after the content fix; checklist diff data-only; battery diff pins-only. Run the counter on the
candidate (b53e209 + ExecRedsR99.patch) and each gate directly.

## Laundering criteria applied (from corpus/lessons M118, QUALITY Q64, M87-1)

- Q64: an append-only correction row replaces a cited token with the address of the **same
  artefact**; a token naming something that no longer exists anywhere is a recorded absence —
  never "corrected" to the record of its removal to green a gate.
- M87-1: a historical lesson is never rewritten to green a gate. Exception here is plan-authorized
  and narrow: round-81.md **line 8 hash quoting only**, meaning unchanged (plan § C2 honest route).
- Round-70 precedent: a row is laundering if the corrected token names a *record about* the subject
  rather than the artefact itself.

## Expected honest shape (from round-98 ScoutTipReds, receipts copied to `ReviewerRedsR99/`)

18 bad governance entries = 1 stale pin (LOG.md:2621 → SCORECARD.md 158→161) + repo-rooted
`.ufo/...` citations (files live at fleet root, `../` convention) + `.ufo/wapes` typo (SCORECARD:527)
+ removed counter address (SCORECARD:538, bytes at `.ufo/waves/round-85/frozen/`) + `:30,37`
line-anchor gate defect (F5 — fixed as a correction row this round, regex fix routed) + 2 missing
pins for LOG.md:2881/2947 (`before-tip-battery-win-dot.txt` → `before-tip-battery-win.txt`).
Corpus: 7 coverage rows (r91–r97 spotchecks) + 1 row for round-99.md (ScribeCorpusR99's file),
round-81.md:8 hash quoted, baseline re-record after content fix, one pin admission for the new
checklist blob, horizon raised to the new notice line.

## Status

- [10:56] Scratch clone at b53e209 created and verified (`rev-parse --show-toplevel` = scratch repo).
  Receipts copied (c2-base, five ctl receipts, round-98 ScoutTipReds report + 3 receipts).
  Polling for ExecRedsR99_READY (120 s interval, ≤75 min). No READY file as of ~11:00.
- [11:00] Base-state verification done (all against b53e209 bytes):

### Per-subject truth check at base (governance-failures-base.txt, 18 entries / 16 subjects)

| subject (file:line token) | verified at base | corrected token resolves? | verdict |
|---|---|---|---|
| LOG.md:2621 row pins SCORECARD.md:158 `.ufo/reports/round-60/kotoba.md` | row at verify_skill_checklist.py (2621, sha 6836c34a…, "SCORECARD.md", 158); token actually lives at SCORECARD.md:161 ("Report `.ufo/reports/round-60/kotoba.md`", confirmed by grep); 3-line insertion in r82 moved it | `../.ufo/reports/round-60/kotoba.md` EXISTS fleet-root (11849 B) | stale pin, fix = subject-line move 158→161, the ONLY base-row field the counter allows to move |
| LOG.md:2881 + LOG.md:2947 `before-tip-battery-win-dot.txt` | backticked token on both lines; round-83 notice at ~2947 already names the supersession; file `-dot.txt` MISSING in lane; `before-tip-battery-win.txt` EXISTS (2282 B) | `.ufo/waves/round-82/receipts/before-tip-battery-win.txt` ✓ | genuine dead name-drift; corrected token is the same artefact the round-83 notice names |
| LOG.md:2958, SCORECARD.md:186 `.ufo/reports/round-82/kotoba.md`; SCORECARD.md:204 round-83; SCORECARD.md:222 round-84; LOG.md:3360 + SCORECARD.md:646 `.ufo/reports/round-84/kama.md`; SCORECARD.md:161/531 round-60/round-81 | bare repo-rooted tokens on the verified lines; contexts say "Report …" / "landed on the fleet repo" / "fleet report"; all six reports EXIST at fleet root (10.8–26 KB) | `../.ufo/reports/...` ✓ (bounded ../ hop, the lane's written convention, same as base rows 2619/2620) | repo-rooted citation of fleet artefacts; corrected token = same artefact, real address |
| LOG.md:3353, 3561 `.ufo/watchdog.log` | fleet driver log contexts ("lane-dead-no-report … relaunch") | `../.ufo/watchdog.log` EXISTS (297 KB) | same class as base row 2620 |
| LOG.md:3512 `.ufo/l0-questions.md` | L0 question context | `../.ufo/l0-questions.md` EXISTS (230 KB) | same class |
| SCORECARD.md:527 `.ufo/wapes` | line says: `**R3** .ufo/wapes (594 B probe output …) → .ufo/waves/round-81/dispositions/wapes.txt` — the sentence itself names the artefact's address | `.ufo/waves/round-81/dispositions/wapes.txt` EXISTS (594 B, size matches) | typo'd name whose artefact exists; correction is name-drift repair, NOT removal laundering (contrast M118: there the artefact existed nowhere) |
| SCORECARD.md:529 `…round-80-verifier-spotcheck.md:30,37` | file exists (72 lines); :30/:37 real content lines (read raw); token dead only because `strip_token_dressing` lacks the `:N,M` form (F5) | `corpus/lessons/round-80-verifier-spotcheck.md` ✓ | gate-dressing false red; plan authorizes correction row + routes the regex fix; NOT a content fix |
| SCORECARD.md:538 `verifiers/check_description_render.py` | frozen predicate line: `python3 -B verifiers/check_description_render.py --rev <rev>`; counter removed from verifiers/ in r85 | `.ufo/waves/round-85/frozen/check_description_render.py` EXISTS (28 KB) | address of the same (quarantined) artefact; correction keeps the record navigable |

Gate mechanics confirmed by reading verify_skill_checklist.py: correction rows excuse `(sfile, sline, stale)`
iff the notice line is ≤ min(horizon, len(log_lines)), sha256-pinned, contains BOTH tokens verbatim,
the subject is still live+red, stale does not resolve, corrected resolves. Appended notice lines must
double-quote stale tokens (backticks do NOT exclude a token from live-subject treatment — LOG.md:2947
is the live counter-example) or the notice itself would add new live reds. GOVERNANCE_ERRATA block and
GOVERNANCE_ERRATA_HORIZON (line 400) are outside the data-only allowance and must not move.

- [11:20] `ExecRedsR99.patch` appeared 11:10 (23,016 B); applied clean (`git apply --check` OK) on my
  scratch clone at b53e209 → candidate `adce43d3166d30112e88bd6f6f1cf8346cd609a0`. Scope: exactly the
  6 owned files (LOG.md +21, corpus/README.md +9, round-81.md 1 line, check_tip_battery.py pins-only,
  corpus-baseline.json 3 equal counts, verify_skill_checklist.py corrections data only).

### Byte-level verification (my script `verify_bytes.py`, all PASS)

- Checklist data-only: `GOVERNANCE_CORRECTIONS` block + `GOVERNANCE_CORRECTIONS_HORIZON = 3601` line
  removed from base and HEAD bytes → remainder **byte-identical**. GOVERNANCE_ERRATA untouched.
- Battery pins-only: `INSTRUMENT_PINS` block removed → remainder **byte-identical**; new pin
  `b6280c684b300ba313f1fc6a06655471e1c7142e` == `git rev-parse <cand>:verifiers/verify_skill_checklist.py`
  (confirmed at battery line 171); all three earlier checklist blobs kept.
- All 16 new correction rows (LOG.md notice lines 3586–3601): sha256 of each line matches the row
  digest, and each row's stale + corrected token appears verbatim on its pinned line.
- LOG.md: exactly one appended notice block (21 lines, 3581–3601), signed `ExecRedsR99`; horizon
  3601 = last notice line = LOG.md length. Stale tokens double-quoted (excluded from live subjects);
  corrected tokens backticked and all resolve (verified existence earlier).
- round-81.md: exactly one changed line (8), transformation confined to backticks→double quotes
  around `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`; hash and sentence otherwise identical →
  meaning-preserving as the plan requires.
- corpus-baseline.json: only the three `equal` expects (172→203, 127→174, 59→72) + the note; all six
  `zero` modes/expects unchanged. NOTE: the note discloses the record tree as "base b53e209 +
  candidate patches in order ExecRedsR99, ScribeCorpusR99, ExecArmsR99" — i.e. the LANDING tree, not
  the ExecReds-only candidate my item names. `measured_against.head` metadata still says e03f9e2
  (round-87) and `as_of` 2026-11-04 — stale historical metadata, cosmetic only (the gate reads
  `checks`). Baseline-vs-candidate drift expected on my item's candidate; L1 re-records at
  integration per the wave protocol.
- README rows: 8 spot-check rows r91–r98 (all 8 files exist; r91–r97 row facts match the file heads I
  read; r98 row base `a33f262f` matches the round-98 LOG entry) + 1 row for `lessons/round-99.md`
  that honestly discloses it is indexed "before the file lands" (ScribeCorpusR99's patch does not
  exist yet at 11:20).

### Candidate measurement (11:30)

- Counter on the ExecReds-only candidate (`adce43d3…`), fleet-shaped sandbox:
  `C2 carried reds green 1 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` →
  `C2-PREDICATE-UNMET` rc 1. Detail:
  - checklist **GREEN**: `PASS governance.citation_resolves: evaluated 1651 — 1651 token(s) resolve;
    10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused,
    19 recorded correction(s) excused`; 11 PASS lines, 0 FAIL/N/A. Arithmetic coherent: 17 live red
    entries excused (16 rows + re-pinned 2621; SCORECARD:531's double entry excused by one row),
    16 new backticked corrected tokens become resolving subjects (1652 − 17 + 16 = 1651).
    Self-test held at 1864 (floor 1864) — the appended data rows break no self-test arm.
  - integrity 7/9: the ONLY drifts are `corpus.index.stale_patterns` + `corpus.index.missing_paths`,
    both `corpus/README.md:209: lessons/round-99.md` — the row indexing ScribeCorpusR99's
    not-yet-landed lesson, disclosed in the row text itself. All three `equal` counts (203/174/72)
    match observed on this tree (verified with `--no-baseline --json`: tracked 203, report 174,
    commit 72, report_dead 0, commit_unresolvable 0) — the recorded baseline is a true observation
    of the ExecReds-only tree.
  - independent: same two DRIFTs, same single site (`README:209`); report_dead 0,
    commit_unresolvable 0 — the round-81 quoting fix and the 8 spotcheck rows work in both gates.
  - battery: `guards 5 of 5; tip battery exit 0: 4 of 6` (floors 202.8 s, inside timeout).
  - verdict so far: **no laundering found**. The two residual reds are the wave-anticipated coupling
    to ScribeCorpusR99's file; they heal when `corpus/lessons/round-99.md` lands. For the L1: at the
    landing the equal counts will drift (+1 tracked file; pointer deltas from the lesson/S281 row) —
    the planned integration re-record covers this.
### Landing measurement (11:48) — base b53e209 + ExecRedsR99 + ScribeCorpusR99 + ExecArmsR99 = `aab1ed61…`

- Counter: `C2 carried reds green 2 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` →
  `C2-PREDICATE-UNMET` rc 1, with:
  - checklist **GREEN** (identical reading: 1651 evaluated, 19 corrections excused, 11 PASS lines);
  - corpus_independent **GREEN** (exit 0) — the moment round-99.md lands, stale/missing heal and
    every zero-mode passes (report_dead 0, commit_unresolvable 0);
  - corpus_integrity 7/9, the only DRIFTs `corpus.index.tracked_files` +
    `corpus.pointers.report_total` — the equal-count baseline drift, observed exactly:
    tracked_files 204 (recorded 203; +1 = `corpus/lessons/round-99.md`), report_total 176
    (recorded 174; +2 pointers from the lesson/SOURCES content), commit_total 72 (recorded 72,
    unchanged). Every zero-mode expectation passes at the landing.
  - battery `guards 5 of 5; tip battery exit 0: 5 of 6` (floors 185.1 s).
- The residual integrity red is precisely the wave-anticipated integration step: the L1 re-records
  the baseline at integration (203→204, 174→176, 72 unchanged — measured here). Nothing in the
  ExecReds patch needs to change for that; the patch's own numbers are honest observations of the
  tree it was recorded on.

## Verdict

**No laundering found.** Every appended GOVERNANCE_CORRECTIONS row and the LOG.md notice pass the
Q64/M118 test:

1. All 16 new rows' stale subjects are genuinely dead at b53e209 (verified file-by-file: the
   `-dot` receipt is absent, the bare `.ufo/` tokens resolve only at the fleet root, `.ufo/wapes`
   exists nowhere, `verifiers/check_description_render.py` is removed from the lane, the `:30,37`
   token fails only on gate dressing) — none is a live artefact being silenced.
2. Every corrected token is the address of the same artefact the original context means — for
   `.ufo/wapes` and `-dot.txt` the correcting sentence itself names the target; for the report
   classes the `../` hop is the lane's written convention (base rows 2619/2620 are the precedent);
   for `check_description_render.py` the frozen round-85 bytes exist at the named archive path.
   No row "corrects" a subject to a record about its removal (the M118 move) — the two
   recorded-absence mechanisms (GOVERNANCE_ERRATA, K69-11 row 2723) are untouched.
3. No real defect is silenced: the F5 `:30,37` gate defect remains a routed defect (fixed here only
   as a correction row, exactly as plan § C2 prescribes); the repo-rooted-citation content class is
   genuinely fixed by giving the true addresses; the mined-mistake fix (QUALITY criterion on the
   no-harm rule) is the plan's own routing, not this patch's to make.
4. Coverage-map rows are real index entries: 8 rows describe files that exist with facts matching
   the files' own heads (tips/bases/reports verified for r91–r97; r98 base matches the LOG entry);
   the 9th row forward-references `lessons/round-99.md` with that fact disclosed in the row text.
5. round-81.md:8 is meaning-preserving (hash identical, quoting only) and is the plan-authorized
   exception to M87-1, confined to exactly line 8.
6. The baseline re-record is equal-mode only (same three `equal` keys; all six `zero` modes
   byte-identical) and taken after the content fix — proven by the gate reading 7/9 with the equal
   counts matching observed values on the patched tree, zero modes passing everywhere.
7. The checklist change is data-only and the battery change pins-only (byte-strip equality both);
   the new pin is exactly the new checklist blob; the counter's four frozen conjuncts all read OK
   at both candidates; guards 5 of 5 at both.

C2-PREDICATE status: the ExecReds-only candidate reads `green 1 of 3` (checklist green; integrity +
independent red solely on the disclosed `lessons/round-99.md` forward-reference), the full landing
candidate reads `green 2 of 3` (checklist + independent green; integrity red solely on the equal-count
baseline drift 203→204 / 174→176, commit 72 unchanged) — both reds are the documented L1 integration
re-record, not patch defects. Nothing here rescues a counter or weakens a gate.

## Findings (non-blocking)

- F-R1 (minor, accuracy): the baseline note's record-tree description ("base b53e209 + candidate
  patches in order ExecRedsR99, ScribeCorpusR99, ExecArmsR99") does not match where its three equal
  counts were observed — they match the base+ExecReds-only tree exactly (gate-proven), while a
  landing tree would read 204/176/72. The numbers are honest; the description is off by the sibling
  files that had not landed when the note was written.
- F-R2 (cosmetic): correction row 3593 duplicates the re-pinned base row 2621's excused key
  (SCORECARD.md:161); the gate dedupes (19 distinct excused keys over 20 rows). No effect.
- F-R3 (cosmetic): `corpus-baseline.json` `as_of` (2026-11-04) and `measured_against.head`
  (e03f9e2, round-87) were not refreshed by the re-record; the gate reads only `checks`, and the
  note discloses the round-99 re-record. Historical-metadata hygiene for the L1's re-record.
- F-R4 (protocol): `ExecRedsR99_READY` had not been written by ~11:52 (patch stable since 11:10;
  reviewed from the patch bytes). If the READY file appears later, its sha256 should be checked
  against `ExecRedsR99.patch` — my review binds to the patch bytes at
  `w1/ExecRedsR99/ExecRedsR99.patch` as of 11:10–11:52.

## Verification gaps

- The round-97 spotcheck row's `tip 1d44bd82` and the r98 row's `tip f5181e0f` were not re-derived
  against the lane history (low value: index truthfulness established by file existence + head
  facts; the row cites the closure's own stated tip).
- The true L1 landing (after its baseline re-record) was not measured — no L1 commit exists yet;
  the predicted post-re-record reading (9/9, all three gates green, counter MET) is arithmetic from
  the measured zero/equal observations, not a counter run.

Scratch `/fast/scratch/hyaku/kotoba-r99/ReviewerRedsR99` removed after receipt copy. No installs
were made (stdlib Python only; no pacman, no uv, no downloads). Only PIDs started by this seat were
used (two counter runs, sequential); none left running.




