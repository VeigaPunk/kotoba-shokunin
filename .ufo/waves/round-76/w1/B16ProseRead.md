# B16ProseRead — prose read of the round-76 build drafts

Seat: `B16ProseRead` (scribe, leaf). Round 76, wave `w1`, lane `kotoba-shokunin`.
Base `b7f13f4b39cbd43076a85568adca763a6f674e7a`; lane HEAD `4de12b61f75c73e3675ef0e422cc2be0f7da8960` throughout.
**Report only.** No lane file, build draft, verifier, counter, index or git/jj state was written by this seat; the one write is this report. Leaf bounds honoured: no subagent dispatch, no background job, no install, no pacman.

VERDICT: drafts read and recomputed — four claims still false or contradictory as written (F-02, F-04, F-06/F-08, F-09), one cross-draft number conflict still open (F-05), two table-shape defects (F-09, F-10), one new ordering defect in the D2/D3 patch pair (F-17), plus nits. Two defects I first recorded (the entry's false `:17` cross-reference and the lesson's "eight quotes") were fixed by their seats while I was reading — recorded below as resolved, with the check that re-proves them.

## Reading state (drafts were being revised while read)

Two drafts changed three times and four changed once during this read; this report is pinned to these hashes (re-hash before landing; any difference means the finding must be re-checked, not assumed):

```
6e55b5d2a55a9b644bd1267d7c071ac5cfbc85f2a901231e7c141da936908bf8  B08-m76-1-round-76-row.md
9e75f8f2131c9e6daacb03ce1becf22f583a6fea6acfc3ff6f02990325694d73  B08-notes.md
6cbe0e14dacef4589be5ee97d6c20ac108b8b633da6748b023e4abda834c3044  B08-q74-quality-row.diff
94ae0d6832e19aed374e0c3015390e0508dca72062cd879cdaf770a8b10f4279  B08-r1-round-75-correction.diff
0d87f87ed3fa2a0b4792c5fa96626a076507a39cb0083792a18f1bf12473454a  B08-verify.txt
bf7840ffdfc8b901dd5b6b33981a9984a45a921521b841b6890c7c5c789175ad  B10RepairD2D3.D2-log-round74.md
95315e8299ac7c9b5a2f49ecd6ada9aee66f28b790f64cc76145177bc8a4c89b  B10RepairD2D3.D3-r49-forward-pointer.md
60b9e410615e2a474d154105df0dcafebe21196e8a42fc02173a74683eccf75d  B10RepairD2D3.formA.patch
01afc7d7b302832e188d0d96e6bac4adc8b46f1cafd3cea0b8dda816257977c9  B10RepairD2D3.formB.patch
21ad9bfe7d73c67b8c93f29cc8cc3059e3d2b54b5e91495abfac6838061d391d  B10RepairD2D3.measurements.txt
caf84c403c589e71510b742db82a5db064023a2b0ff4a5352a444b11b8627a1e  check_receipt_revs.sh   (shell; header read only)
b0204b127edb39570597976c75ec1f5997b0a9326cd64df4deb43a604e454274  entry-draft.md
341ed317d3f310cc7213dfba9d5be4bcbe358166c96e616ba38e17b130d60965  lesson-draft.md   (B/F-05, F-06, F-04, F-19, F-20 re-proved at this hash)
39a18eeeca37ca95a969c8889cc10d306387c8fe62e673623bd7c779a86ff6dc  log-draft.md      (F-05, F-11, F-15, F-17 log-placement re-proved at this hash)
e7dc6330b1bbcdc678feb303856c22a19a6c53a43bddd477c244ec58809839ad  quotes-s213.md
88833414d38cae5fd75ff33edec78d306ea5ab6ef4685e53390a5e117dedddf4  scorecard-draft.md
bbef13cbb15fbd540fa3e342c79c7b914622ceecd52bf1a78b2798f7ee2c0dda  skill-patch.md
d963274c15d648b7366f601b46a54e805cb2b39897c0bdf0bb7d418467760392  sources-patch.md
a3c1e399acc928056aaa8edf7cee88ee09255fc993497159b873a3e25e370f9c  w2-registry-note.md
```

Also observed in the working tree at read time (not mine, not committed): `M verifiers/floors-registry.json`, `M verifiers/check_assertion_floors.py` — D4's two floor rows being applied (`check_spec_craft.py` now present in the registry JSON). Untracked: the whole round-76 wave dir.

## Gates run by this seat (recomputations from bytes; no claim counter run)

`verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` do **not** exist at my read, so I ran neither and claim no claim-counter output.

| check | result |
|---|---|
| 13 located quotes in `quotes-s213.md` — verbatim, stated line, word count, occurrences, page-uniqueness vs the two other snapshots | **0 problems**; #9 `A few sentences…` 10 w @28, #12 16 w @159, #13 7 w @157 |
| the draft's "page does not state" sweeps (11 patterns) | **0 hits each**; `front` only in `frontmatter` (9, 173) |
| entry rule-table quotes (5 rows) at `:25/:26/:27/:27/:28` | **all verbatim, all on their line, page-unique**, 9/13/7/17/10 words |
| entry `tokens` cells (5) | **all verbatim, occurrence 1** |
| rendered description at `b7f13f4` | **1022 clip / 1021 stripped**, first sentence **151**, words **148**, sentences **7**, quoted spans **108**, Triggers sentence **149**, anti-trigger sentence **153**, headroom **2** — every audit number reproduces |
| same render at `65a5c7a`, `ac9f295`, `4de12b6` | **1022** at all four |
| r75 window arithmetic | `3:14 4:76 5:78 6:73 7:79 8:72` (sum 392); raw block `4–18` = `1037`; 1037−30+14 = 1021, +1 clip = 1022 — the R1/Q74/M76-1 arithmetic reproduces |
| R3 note's five command blocks (`jq`, `test -e`×2, `git log --diff-filter=A`, `git status`) | **all reproduce** — sha256 `e4ce0f6d…`, `d118a3b`, `has_report_field:false`, 64/64/0/64, 63 `.md` + `swarm-registry.json`, both `test -e` → 1 — **except** the contrast clause (F-02) |
| LOG anchors | **2810 lines**, `w2 falsify results pending` once at 2810, §74 at 2801, §75 at 2805, single trailing newline |
| dispatch role census (`w1-dispatch.json`) | **15/10/10/10/6/4/3/3/2/1 = 64**; `sonic` 0/0; `labrat` 0 roles / 15 prompt mentions; `A`-prefixed names 36 |
| S213 row edit (`sources-patch.md`) | **810 ch / 814 B / NF 13**; `used-by` = cells[11]; insert 47 ch → **857 / 861 / NF 13** |
| cross-references cited by drafts | `frontmatter-rule-authorities-round48.md:44` ✓; spotcheck `:63`/`:72`/`:77` ✓; `plans/round-75.md:15` ✓; `frontmatter-trigger-surface.md` §12 at 150–155 (quote spans **153–154**) |
| D2 commit facts (both B10 patches) | `d5aebcf` message, author `kotoba-shokunin`, `2026-10-25 23:16:44 -0300`, **394 files** — exact |
| D3 cited line ranges in the r49 entry | `:43` `## Classification rule`, `:246` `## Round 50: precedence…`, `:416` `## Round 51 status…`, file 466 lines — exact; counts `10 adjacent, 10 none, 0 contested` (round 49 `9/11/0`) exact |
| **D3 no-harm (Q72 post-state)** | r49 entry + the D3 append vs the base entry, through `check_sibling_census.py --province`: **byte-identical output, 16 FAIL lines, `province rows 20 matched 4`, exit 1 in both** — the append is census-neutral |
| lane's own description readers | `check_sibling_census.description_of(SKILL.md)` → **1021**, confirming the entry's "contested convention" note |
| `burden of triggering` provenance | 0 in `spec-skill-creation-craft-round74.md`, 0 in `frontmatter-trigger-surface.md`, 0 files lane-wide |

## Findings

Severity: **B** false as written; **C** two artifacts disagree; **S** shape; **N** nit.

### B — must be fixed before landing

**F-02 (B) — `w2-registry-note.md`: "unlike sibling seats `R75Attack08`, `R75Attack13`, `R75Attack51`, …, which do" is false — no results entry in the file has a `report` field.**
Measured: `jq '[.results[]|select(has("report"))]|length' .ufo/waves/round-75/w2-results.json` → **0**; `.results[0]|keys` → `["agent","name","note","output"]`; all three named seats read `has_report:false`. The clause contradicts the note's own excerpt (`has_report_field:false`) two lines above it, and this is the artifact R3's counter reads.
Fix: "no results entry in this file carries a top-level `report` field; the report path appears only inside the seat's embedded verdict prose." Everything else in the note reproduced byte-for-byte.

**F-04 (C→B) — `lesson-draft.md:117` M76-1 row: `(w1/B21RevMethod.md §2–§4, whose "372" mis-sums its own five printed lengths)` misreads the cited report.**
`w1/B21RevMethod.md:70` derives it: "76+78+73+79+72 = 378 raw, minus 10 indent chars = 368, plus 4 join spaces = **372 value characters**". 372 is that window folded, not a claimed sum; the five printed lengths sum to 378 (`awk` confirms). As written the lesson repeats the very error class it records (a number detached from its stated method), inside the row that files the mistake.
Fix: strike the parenthetical, or "whose 372 is the same window folded (378 raw − 10 indent + 4 joins)".

**F-09 (S→B for the row's English) — `skill-patch.md` Pin 1: the row is 447 chars / 65 words (neighbours 164–260 chars), and its first cell is ungrammatical.**
Measured now: row length **447**, 65 words, 3 cells; base § Body craft rows 211–216 = 260, 224, 228, 193, 172, 164 chars. The draft's own note now states 447/65 honestly, but justifies it as "the row keeps the six existing § Body craft rows' dense one-line form and adds no padding" — it keeps the one-line *form*, and it exceeds the widest neighbour by 187 characters (72 %).
First cell, verbatim: `write the description as an imperative about the goal, not the mechanics, and err pushy` — "and err pushy" is not English, and the page's own phrase (already quoted in the same row) is `Err on the side of being pushy`.
Fix: `write the description as an imperative about user intent, and err on the side of being pushy`; trim the action cell to the two fragments conjunct (c) needs plus one consequence clause.

### C — conflicts (one owner must settle; report verbatim for the judge)

**F-05 (C) — tip line count: `593`/`+3` (patch) vs `595`/`+5` (log, lesson).**
`skill-patch.md:7` "Net delta: **+3 lines → 593** (1 rule row, 2 registry rows)"; `:11` anchors `rule row line 217`, `registry rows 514–515` (consistent with +3 from base anchors I measured: rows 211–216, last registry row 512). `log-draft.md:35` "base 590, planned 595"; `log-draft.md:119` "590 → 595 planned (+5: 1 preamble wrap, 1 rule row, 2 registry rows, rounded by the wrap)" — that decomposition sums to 4; `lesson-draft.md:203` "the C1 patch adds 5 lines (595), leaving 5 lines of margin". Either the two downstream drafts take the new figure or the preamble pin must be restored.

**F-06 (C) — R2's measured revision: `b7f13f4` (lesson) vs `ac9f295` (log F2).**
`lesson-draft.md:137` "names the r75 tip `b7f13f4…` on its first line"; `log-draft.md` F2 "the spot-check asks for a receipt at the **r75** final tip (`ac9f295…`)". Ancestry measured: `git log --oneline ac9f295..b7f13f4` → `b7f13f4` only, so `ac9f295` is r75's landing tip and `b7f13f4` its closure commit. The frozen sentence ("names the tip revision on its first line") does not choose; the counter must, and both drafts must say the same.

**F-08 (C, contract) — `sources-patch.md` still presents conjunct (a)'s anchor clause as open; `plans/round-76-addendum-1.md` closes it.**
Addendum: "(a) … equal to the digest recorded in the S213 row's anchor update" is **withdrawn**, replaced by four pins. `sources-patch.md` CF-1 still lays out options (i)/(ii)/(iii) without citing the addendum, and option (i) (anchor-cell edit) is the one that would redden the append-only gate 18 → 19 and break rule 2.
Fix: one line — "resolved by `plans/round-76-addendum-1.md`: option (iii) is the adopted reading".

**F-17 (C, new) — the D2/D3 patch pair ships two mutually exclusive forms whose placement differs in consequence.**
`formA` inserts the D2 bullet inside § Round 74 (before `## Round 75`); `formB` appends a new `## Round 74 correction (append-only, routed D2)` section **after** § Round 75, so the LOG's chronological heading order becomes 71,72,73,74,75,**74-correction**,76 once the round-76 entry lands. `formA` preserves chronology but shifts every line after 2804 by +4, which stales `log-draft.md`'s placement facts ("§ Round 75 spans lines 2805–2810", "`LOG.md` ends at line 2810", "append immediately after `LOG.md:2810`") — the counter's ordering test is index-based, so the contract survives, but the draft's line numbers do not. Both forms also say "every commit **this round** put on `master`" inside a round-76 edit of a round-74 record — "that round" is the unambiguous word.
Pick one form and restate the log draft's placement facts as strings, not line numbers.

**F-18 (C, resolved-in-flight) — the entry's `:17` cross-reference and the lesson's "eight quotes" were both false at my first read and both were fixed by their seats before I finished.**
First-read text: `entry-draft.md` "… is four principles … (`:17`, already in the lane's `spec-skill-creation-craft-round74.md` and `frontmatter-trigger-surface.md`)" — false, `grep` finds the sentence in neither file (0/0). Current `entry-draft.md:7` reads "(`:17`)" with the parenthetical gone; the grammar defect **remains** ("§ Writing effective descriptions is four principles").
First-read `lesson-draft.md`: "carries eight such located quotes (§ The admitted rules)" — the entry has five and had no such heading. Current `lesson-draft.md:42` reads "carries five such located quotes in its opening rule table" ✓.
Re-prove after any further edit: `grep -c '^| optimizing-descriptions' entry-draft.md` → 5, `grep -n '^## ' entry-draft.md` → 4 headings.

### S — table shape (measured against the neighbours)

**F-10 (S) — the pinned source cell is the only one in § Body craft carrying a repository path.**
`S213 optimizing-descriptions; `corpus/knowledge/description-craft-round76.md`` vs neighbours `S223 best-practices`, `S224 quickstart`, `S225 using-scripts`. The path is there because conjunct (c) reads the row alone — legitimate — but the semicolon reads as two sources. If the counter searches the whole row, move the path to the action cell's tail and keep the source cell in house form; if it reads the source cell only, keep it and say so (the patch note does).

**Positive (no action).** The two new § Gate registry rows are 8-cell in file order (`Name | Kind | Entry command | Verdict map | Self-test | Pinned values | Write scope | Owner`), `gate` kind, backticked path first, verdict cell `0=clean, 1=failed, 2=could-not-evaluate — round-76 C<N> counter (<axis>): …`, `--self-test`, plausible pinned values, `none (read-only); --self-test fixture repos under $TMPDIR (removed)`, `kotoba` — the shape of the r73/r74 rows. No stray pipes in either row; the header and separator are untouched; all 19 checklist boxes untouched. `check_spec_craft.py` counts only rows citing S223/S224/S225 (`:690`), so the new S213 row cannot disturb its 3 of 3. The Q74 row appended by `B08-q74-quality-row.diff` is 5 cells like Q73, and the R1 correction diff is append-only with the superseded row indented so it cannot re-enter the `## Mistakes` table.

### N — nits

**F-11 (N)** `log-draft.md:6` "Nothing here is a measurement of a tip that has not run" — double negative that says the opposite; write "Nothing here reports a tip measurement that has not been run."
**F-12 (N)** `entry-draft.md` action cells: "a description that needs the full character allowance is a finding, not a fit" (no referent for "fit") and "a missed context costs the whole skill" (elliptical); say the consequence.
**F-13 (N)** `sources-patch.md` cites `check_skill_evals_v2.py:289` for `if row[10].strip() != ENTRY:` (the `if` is **288**) and `check_spec_craft.py:691` for `if ENTRY not in listed:` (the `if` is **690**).
**F-14 (N)** `scorecard-draft.md` writes "Measured: … at `<tip>`" for arms not yet run, and attributes "census exit 0, 151 rows" to `.ufo/waves/round-76/base-battery/base-battery.txt`, which carries no census lines (the census line is in `receipts/census-before.txt`).
**F-15 (N)** Both paste-ready LOG blocks still carry `<tip>`, `<freeze>`, `<land-*>`, `<lines-at-tip>`, `<tip-rev>`; add the implied gate after pasting — `grep -n '<[a-z][a-z0-9-]*>' LOG.md` expecting no hit outside code spans.
**F-16 (N)** `lesson-draft.md` asserts D2/D3/D4 "landed"; at my read D4's rows are uncommitted working-tree edits and the D2/D3 patches are still drafts. True on landing if they land — false at tip if any slips; the sentence needs to move to § Round honesty in that case.
**F-19 (N)** `quotes-s213.md` quote #11 (`enforces a hard limit of 1024 characters.`) begins lowercase mid-sentence; fine as a located fragment, but name it "fragment" where it is tabulated so a reader does not take it for a sentence.
**F-20 (N)** `lesson-draft.md:42` "the four principles at `:25`–`:28` plus the unnamed-context rule" — the unnamed-context row is a split of the `:27` bullet, so "four principles plus one split row" is the accurate form.

## Conflicts reported verbatim

1. `lesson-draft.md:137`: "names the r75 tip `b7f13f4b39cbd43076a85568adca763a6f674e7a` on its first line" vs `log-draft.md` F2: "asks for a receipt at the **r75** final tip (`ac9f29510d3914a6edb97c8dbdb3445cab9141de`)".
2. `skill-patch.md:7`: "**+3 lines → 593** (1 rule row, 2 registry rows)" vs `log-draft.md:119`: "590 → 595 planned (+5: 1 preamble wrap, 1 rule row, 2 registry rows…)" vs `lesson-draft.md:203`: "the C1 patch adds 5 lines (595)".
3. `plans/round-76.md:64`: "64 seats — 30 build + 34 attack (attack share 53%)" vs `plans/round-76-addendum-1.md`: "22/64 = 34.4%" vs commit `4de12b6`: "34% attack share" — now recorded as M76-6 in the lesson ("42 build + 22 attack = 34.4%", consistent with my dispatch census); the plan sentence itself is unreconciled.
4. `w2-registry-note.md`: "no top-level `report` field (unlike sibling seats … which do)" vs `jq '[.results[]|select(has("report"))]|length'` → `0`.
5. `sources-patch.md` CF-1: "(a) cannot be reached through `used-by` alone … Options (i)/(ii)/(iii)" vs `plans/round-76-addendum-1.md`: "That clause is **withdrawn** … pinned in four places instead".

## Out of scope (recorded, not done)

- Did not run either frozen counter (absent); no red/green receipt claimed.
- Did not fetch the live pages; quote checks use the three pinned snapshots only (digests match `MANIFEST.sha256` and `fetch-record.json`).
- Did not rebuild `sources-patch.md`'s append-only "18 breaches in 8 of 44 commits" or its extensionless-URL 344 074 B body; did not review `check_receipt_revs.sh` as prose.
- Did not read the w1 seat reports as prose beyond `B21RevMethod.md` §2–§4 and the `B26FetchRecheck`/`A24ScoutFresh` references (I verified the snapshot digest, not those reports' text).
- No scratch dir was created (all recomputation in-process except one `/tmp/b16` census comparison, removed with `rm -rf`); nothing to clean.

## Artefacts

- This report: `.ufo/waves/round-76/w1/B16ProseRead.md`.
- Inputs: `.ufo/waves/round-76/build/*` (hashes above), `.ufo/waves/round-76/snapshots/*`, `.ufo/waves/round-76/receipts/{census-before,d4-selftests,fetch-recheck,receipt-revs,description-audit-4de12b61…}.txt`, `.ufo/waves/round-76/{w1-spec.json,w1-dispatch.json}`, `plans/round-76.md`, `plans/round-76-addendum-1.md`, `SKILL.md`, `LOG.md`, `SCORECARD.md`, `corpus/SOURCES.md`, `corpus/QUALITY.md`, `corpus/lessons/round-75.md`, `corpus/lessons/round-75-verifier-spotcheck.md`, `corpus/knowledge/{spec-skill-creation-craft-round74,frontmatter-trigger-surface,frontmatter-rule-authorities-round48,skill-listing-thresholds-round54,sibling-overlap-census-round49,sibling-overlap-census-round74}.md`, `.ufo/waves/round-75/w2-results.json`, `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md`, `verifiers/{check_spec_craft,check_skill_evals_v2,check_sibling_census,check_sibling_reread,verify_harness_claims}.py`.
- No receipt produced; this seat produces a report, not a counter arm.
