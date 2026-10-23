# ReviewL0Line — falsify of the round-55 kotoba L0 queue line (fleet `.ufo/l0-questions.md:117`)

Result: MIXED — every measurable claim in the filed line reproduces exactly in a sandbox (verifier stdout byte-identical to the scout's capture, the 13-change per-commit breakdown exact, all four quoted lesson/CORPUS locations verbatim, the round-53 routed-defect-3 and S061 records correct, draft=queue byte-for-byte), but the line's evidence sentence has two wording defects: it calls 542f51567 a "falsify-correction commit" when its own subject is the round-50 C1/build commit, and "the round lessons disclose only as … 'No other row moved'" overstates non-disclosure (round-50.md:103 discloses the S022 teaches correction; round-50.md:77's old→new delegation is backed by real seat-report tables).

Seat KotobaR55.ReviewL0Line (falsify reviewer, leaf; no subagents). Read-only on the lane; the only lane
file written is this report. All runs in the sandbox clone
`/fast/scratch/hyaku/kotoba-r55/ReviewL0Line` at tip `f0e6b695b746775823b65a8c45de7d50ea33e84f`
(clone + `checkout -q` per bounds; `rev-parse` confirms). Access stamp: `date -u` →
`Fri 23 Oct 2026 12:14:17 AM UTC` (first verifier run). No installs or upgrades (git, python3, coreutils
already present). No lsp device used: the checked artifacts are markdown line quotes and a Python gate whose
semantics were exercised by direct execution (stronger evidence here than static reference checks); the gate
script's identity base↔tip was pinned by sha256 below.

## 1. The verifier claim — reproduces byte-identically

- Script identity: `git show f0e5de82:verifiers/check_sources_append_only.py` vs the tip file →
  both sha256 `9f18f00ce488d687362cfa3e16df8f4fec56da9e580423a83d2bad6283998bd3`, 195 lines
  (`wc -l`). The line's "check_sources_append_only.py at f0e5de82" is the same bytes as the tip's.
- Run 1: `timeout 300 python3 -B verifiers/check_sources_append_only.py --rev f0e5de82` → **exit 1**;
  stdout 39 lines, sha256 `b1a89a1cd55ff1cf00a6dd3a00d6bf58a5ff8a514ea2f5ec71301655cee73ae1`
  (= the scout's recorded capture, ScoutL0Sources.md §2); stderr empty (sha256 `e3b0c442…`);
  summary `sources append-only breach 13 change(s) in 4 of 17 commits`. The line's quoted
  "13 change(s) in 4 of 17 commits" and "exits 1" are exact.
- Run 2 (the registered command, SKILL.md:467 at base / :466 at tip):
  `timeout 300 python3 -B verifiers/check_sources_append_only.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev f0e5de82`
  → **exit 0**, `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`.
  The line's "registered gate command is green on its pinned --base 422ffd10 range but the
  full-history scan is red" holds.

## 2. The 13 changes — per-commit breakdown exact

The 13 `breach` lines from my run (after 25 `log` lines), grouped, match the line's
"bfd5a583a S022 teaches (1); 542f51567 S019 scope/anchor/teaches and S022 scope/anchor/teaches (6);
bf109cacc S019 teaches, S022 teaches, S026 scope/teaches, S028 teaches (5)" plus the e792607e S050 edit,
with no row-removal breach:

```
breach bfd5a583a S022 teaches
breach 542f51567 S019 scope / S019 anchor / S019 teaches / S022 scope / S022 anchor / S022 teaches   (6)
breach bf109cacc S019 teaches / S022 teaches / S026 scope / S026 teaches / S028 teaches              (5)
breach e792607e8 S050 anchor
```

All are protected-cell changes in existing rows ("in-place" is right). Commit identities
(`git show -s --format='%H|%ci|%s'`, full hashes in the scout's §3 table all resolve):

| short | author date | subject (first clause) |
|---|---|---|
| bfd5a583a | 2026-10-22 08:37:22 -0300 | "round-49: falsify-wave corrections (…, S022 teaches, …)" |
| 542f51567 | ai 08:57:23 / ci 10:25:02 -0300 | "round-50: C1 description names the 9 adjacent census lanes …, S024-S029, Q26, lesson" |
| bf109cacc | 2026-10-22 10:41:42 -0300 | "round-50: falsify corrections 2 (…, S019/S022/S026/S028 cells, …)" |
| e792607e | 2026-10-22 17:45:49 -0300 | "round-53: records and falsify-wave corrections — … S052, S050 wording, …" |

## 3. Quoted locations — all verbatim at the cited lines

- `corpus/lessons/round-49.md:50-51`: "Status changes logged old→new: … No other row / moved. Rows 21 → 23" — "No other row moved." spans 50-51. ✓
- `corpus/lessons/round-50.md:76-78`: "…S019 and S022 / also gain anchor, scope and teaches text for the round-50 facts (seat reports carry each old→new cell). / No other row moved. Rows 23 → 29". ✓ (the line drops the parenthetical; see F2)
- `corpus/lessons/round-51.md:64-67`: "Contract v1 rule 2 forbids editing `teaches` in place, and a superseding / row with the same URL would add a W04 duplicate-URL warning, so the narrower cell stays…" — quoted phrase at :65, inside the cited range; the refusal context is S024, i.e. "the same edit" is fair. ✓
- `CORPUS.md:116-118` (fleet): "2. **Append-only.** Only `status`, `recheck` and `used-by` change in place, and each change / is logged old→new in the round lesson. A correction is a new row whose `teaches` opens / `supersedes S0NN —`." ✓ (line cites :116)
- All three lesson files are byte-identical between f0e5de82 and tip (`git diff --name-only` over them → empty), so the quotes hold at both revisions.

## 4. The e792607e / S061 routing claim — correct

- `corpus/lessons/round-53-verifier-spotcheck.md:192-193`: "3. **S050 in-place `anchor` edit** (`e792607e`) breaks SOURCES append-only rule 2. Record it as a correction, or ask the operator to ratify it via L0." — the filed line is literally the routed remedy for the remaining 12.
- `corpus/lessons/round-54.md:67` (§ Routed defects from the round-53 spot-check, item 3): "S050 in-place edit: S061 and M45, with `verifiers/check_sources_append_only.py` (red on `e792607e`)"; also :51-56 ("S050 (routed defect 3): not edited… M45's gate finds 12 more protected-cell changes in `bfd5a583a`, `542f51567`, `bf109cacc`; they are carried, not corrected this round") — the line's "12 earlier … carried" framing matches the lane's own record.
- S061 exists: `corpus/SOURCES.md:74` teaches opens "supersedes S050 — records the in-place anchor edit of `e792607e` as a correction…"; `corpus/lessons/round-54.md:31` records it as "correction row for the in-place S050 anchor edit of `e792607e`". ✓

## 5. Queue hygiene and draft fidelity

- Exactly one round-55 line in the queue (line 117); append-only preserved (mori r30 at :116 unchanged; :118-119 are kumitate r43 / kake r35).
- `diff` of ScoutL0Sources.md:129 (the §5 draft) against `.ufo/l0-questions.md:117` → empty, `DRAFT-QUEUE-IDENTICAL`; the integrator appended the scout's bytes without alteration. Evidence pointer `kotoba-shokunin/.ufo/waves/round-55/build/ScoutL0Sources.md` exists.

## Findings by severity

**F1 (moderate — mislabeled provenance in the filed line).** "12 changes in three round-49/50
falsify-correction commits" is wrong for 542f51567: its subject is the round-50 main/C1 **build**
commit ("round-50: C1 description names the 9 adjacent census lanes … S024-S029, Q26, lesson"), and its six
S019/S022 scope/anchor/teaches gains are new round-50 build-wave content ("for the round-50 facts",
round-50.md:77), not corrections of routed defects. Only bfd5a583a ("falsify-wave corrections") and
bf109cacc ("falsify corrections 2") are falsify-correction commits — 6 of the 12 changes each class.
The ratify-vs-correct question is unaffected, but the evidence sentence misstates the class of half
the changes. (ScoutL0Sources.md §3 itself labeled 542f51567 "round-50 C1"; the imprecision entered in §5.)

**F2 (moderate — "disclose only" overstates).** "the round lessons disclose only as cells that 'gain
anchor, scope and teaches text' with 'No other row moved'" is false for 1 of the 12 and incomplete for 6:
- round-50.md:103 (erratum table, item 14) discloses the bfd5a583a correction: "S022's 'description alone' teaches cell | the page supports less than the cell claims; **the cell was corrected** | `.ufo/waves/round-49/falsify/ReopenS022.md:11-12`" — a third disclosure form in the same cited file.
- round-50.md:77's parenthetical "(seat reports carry each old→new cell)" is real, not vestigial: `.ufo/waves/round-50/build/SrcReopenS019.md:78-81` and `SrcReopenS022.md:68-71` carry per-cell old→new tables whose new texts match my run's breach windows (e.g. S019 scope old "…nd description" → new "…nd description, and what the page says about…").
- What remains true: contract rule 2's letter ("logged old→new **in the round lesson**") is unmet for all 12 — the lesson delegates (6), qualitatively discloses without old→new (1), or is silent (5: the bf109cacc set, covered only by "No other row moved." at :78, which the same commit bf109cacc left untouched while editing round-50.md +12/−1 and SOURCES 4 rows). For those 5, detailed defect+fix text lives outside the lessons (`.ufo/waves/round-50/falsify/ReopenS019S022.md` F1-F2, `ReopenS026.md` F2-F3, `ReopenS028.md` F1) and the commit subject names the rows/cells. "Disclose only" should be narrowed to "the lessons log no old→new" — the actual rule-2 breach.

**F3 (minor — temporal nuance on the round-49 citation).** round-49.md:50-51's "No other row moved."
was written by the round-49 build landing; bfd5a583a rewrote S022's teaches later in the round and did
not touch round-49.md (`git show --stat bfd5a583a -- corpus/lessons/round-49.md corpus/SOURCES.md` →
SOURCES.md only, 1 insertion, 1 deletion). So :50-51 is a stale non-update rather than a same-commit
contradiction; the line citing it is fair, but the sequence matters for the operator's ratification.

**F4 (context, not a defect).** The commit subjects themselves name the affected cells
(bfd5a583a "S022 teaches"; bf109cacc "S019/S022/S026/S028 cells"; e792607e "S050 wording") — the line's
non-disclosure claim is scoped to the lessons and survives, but an operator doing due diligence will find
these pointers; naming them in the line would preempt a "nothing disclosed" misreading.

## Residual risk and verification gaps

- I did not re-derive the scout's per-cell byte-size column (477→641 etc.); my gate windows match its windows, and my stdout sha256 equals its recorded capture, so the windows are pinned even where sizes are not.
- I did not re-verify the scout's §1 script-lineage claims (bf65974c + cae8f2ea) — the base↔tip script hash and the observed behavior pin what the queue line needs.
- I did not run the gate's `--self-test` (not needed for any claim in the line; the wave-2 no-harm seats own gate mutations).
- 542f51567's author vs committer date differ (ai 08:57:23, ci 10:25:02 -0300); the scout's table used author dates. The filed line carries no timestamps, so nothing turns on it.
- "of 17 commits" is the gate's self-printed scan count (17 of 18 SOURCES-touching commits; creation commit skipped) — I relied on the byte-identical output rather than recounting the commit set.

## Process hygiene

Sandbox clone only; every command `timeout`-bounded (≤330 s); no process left running; no lane file written
except this report; no jj command; no installs/upgrades (nothing to record under the tooling directive);
no paid model calls; leaf seat (no subagents).
