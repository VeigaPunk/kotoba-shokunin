# Kb81R07ClosureLearn — r80 closure routed-defect → r81 plan mapping audit (scout, leaf)

Base `b284223105f4d106f7e8f56ed4fd296c643cda0e` (verified: `git rev-parse HEAD` in the lane).
Sources mined: `corpus/lessons/round-80-verifier-spotcheck.md` (the r80 closure spot-check, landed
at the base without an index row), `/home/vgpnk/Projects/shokunin/.ufo/reports/round-80/kotoba.md`
(the r80 closure), `plans/round-81.md` (authoritative), plus committed bytes named per finding.
Every byte claim below was re-read from the lane/fleet trees this session; commands pasted.

## 1. Routed-defect mapping — all four defects mapped, no plan gap

Closure § Routed defects (`round-80-verifier-spotcheck.md:63-68`) names exactly R80-D1..D4.

| defect | closure disposition | r81 plan mapping | verified |
|---|---|---|---|
| R80-D1 attribution (report landed via hyaku sweep under lane identity) | "record only; no lane fix possible" | correctly absent — no repair item; the plan names no attribution work, matching "record only" | `grep -n 'attribut\|R80-D' plans/round-81.md` → zero attribution hits; only D2/D4 cited |
| R80-D2 scope (stray `.ufo/wapes` at lane root) | "remove or move under `.ufo/waves/`" | **R3** (plan line 21): file moves to `.ufo/waves/round-81/dispositions/wapes.txt`, deleted from lane root; also re-mined as a Mistakes candidate + Q76 criterion (plan line 47) | `ls -la .ufo/wapes` → 594 B, untracked; `git status --porcelain` → `?? .ufo/wapes` only (plus r81 wave/plan files) |
| R80-D3 instrument (external-classification + fleet-report existence control-reachable; bind repository & report-content identity per Q75) | "bind … before reusing the C1 claim — already planned for round 81" | **R1+R2** (plan lines 19–20): report-pointer `<rev>:<path>` object resolution + `## SHONEN`/≥400 B content identity (integrity gate); `verifiers/external-commits.json` verified binding in BOTH gates; trigger line 8 names D3 "this claim" | both gates' base reds verified (§3); marker-only classification explicitly forbidden by plan text |
| R80-D4 residuals (corpus gates red: `report_dead`/`commit_unresolvable` carried at expectation 0; S230 anchor misattribution) | "a future SOURCES row must supersede it per CORPUS rule 2" | **R5** (plan line 23): S250 `supersedes S230 —` row, S230 retained append-only + **R2's manifest** binding `7bb48f21…` → `mistralai/mistral-vibe`; both hex occurrences classify `commit_external` | `git cat-file -e 7bb48f213ac677f943d5c791199ed3dddf302f00` → rc=1 in lane AND fleet root; `corpus/SOURCES.md:171-172` carry the token (S230 pi-mono anchor, S231 vibe) |

Assignment mapping confirmed exactly: D1→record-only, D2→R3, D3→R1+R2, D4→R5+manifest. **No
unmapped defect; no plan gap.**

## 2. C1 kill reasoning → strengthened design (W8–W10 → R1/R2 + controls W6–W9)

Closure C1 kill (spot-check § C1, lines 19–24): C01's three canonical worlds each printed
`6 of 6` exit 0 on the frozen amended counter — (a) real lane-created commit `56b0764e…` absent
lane/fleet masked as external by `owner/repo@`, (b) dead lane SHA in a lane-URL row →
`commit_external=3, unresolvable=0`, (c) seven-byte `marker` file at the fleet report path.
Receipts `Kb80C01C1-canonical-{lane-at,lane-url}-tipbattery.txt` +
`Kb80C01C1-canonical-fleet-marker-default.txt` exist in `.ufo/waves/round-80/build/` (listed).

Strengthened equivalents in the r81 plan (line 30), each mapped:

- r80 (a) lane-at marker → r81 **W6**: real lane-created commit + `owner/repo@` marker NOT in
  `external-commits.json` → expect `commit_unresolvable` red. R2 kills the marker-only arm.
- r80 (b) lane-URL dead hash → r81 **W7**: dead lane hash in a lane-URL row → red. Same arm.
- r80 (c) fleet marker → r81 **W8**: marker file at fleet report path → expect `report_dead`
  red. R1's content-identity arm (`## SHONEN` + ≥400 B) kills it — fleet
  `.ufo/reports/round-76/kotoba.md` is 8,128 B (a real report passes, a 7 B marker does not).
- NEW **W9**: manifest entry with no committed receipt proof → red. Guards the new binding
  surface itself — a class r80 had no counter for.

E04 read (`.ufo/waves/round-80/build/Kb80E04DeadPointer.patch`, 35 lines): adds `<rev>:<path>`
`git cat-file -e` resolution (citing repo, then fleet) inside `report_pointer_exists` + a
self-test arm. R1 keeps that resolution and *adds* content identity — strictly stronger.
E05 report read (`w1/Kb80E05GrammarFix.md`): its own residual **R1** admitted "line scope is
spoofable by construction" — the exact class W8/W9 falsified; R2's manifest supersedes the
entire marker-grammar arm, and the two live sites still classify `commit_external` with
provenance now verified. Correct strengthening, not narrowing.

## 3. Base-state verification (committed bytes)

- `receipts/tipbattery-base-dot.txt` (round-81): tail `guards 5 of 5; tip battery exit 0: 4 of 6`,
  `wall 105.9s`; six gates listed — registry/floors/checklist/correction-sweep exit 0, integrity +
  independent exit 1. Matches plan's `4 of 6` base claim.
- `verifiers/check_tip_battery.py`: `LINE_CAP = 40` at line 111; `INSTRUMENT_PINS` at line 125;
  used at 316–320,335. E6's named line set exists.
- `verifiers/external-commits.json`: absent at base (`ls` → No such file) — new file per R2.
  Wave draft `build/Kb81E03ExtManifest.json` binds `7bb48f21…` → `mistralai/mistral-vibe`,
  evidence `.ufo/waves/round-79/snapshots/S231.fetch.json` — that fetch record (tracked) pins
  the hash "by git ls-remote at 2026-10-27T21:43:03Z". `S230.fetch.json`/`S231.fetch.json` +
  manifests exist under `round-79/snapshots/` (tracked; plan calls them "r80 receipts" —
  cosmetic round naming, content correct).
- pi-mono head `bb65e3e4…` / path-touching `25cc5c7b…` verified in
  `Kb80S15FreezeShas-receipts.txt:369-377` and `Kb80S01Lesson.md:44` (M80-3). Fresh r81
  `snapshots/pi-mono-lsremote.txt` shows HEAD moved to `a9228305…` — consistent, not a conflict.
- `corpus/lessons/round-77-verifier-spotcheck.md:15` carries `HEAD:.ufo/reports/round-77/kotoba.md`
  inside the `git show` command — the `report_dead` 1 token class R1 resolves.
- Index gap verified: `corpus/README.md` coverage map has the r79 spotcheck row ("indexed
  round 80") but **no** round-80 row → `unindexed 1` confirmed; covered by R4.
- All five base DRIFT classes have a named repair: `tracked_files`/`report_total`/`unindexed`→R4,
  `report_dead`→R1, `commit_unresolvable`→R2+R5.

## 4. Discernment spot-check table carry-over

Closure table (spot-check § Discernment, 5 rows, all `agree`): S227 admit (quote verbatim
`S227-claude.md:617`, cap-exact 25 words; live page changed → snapshot-pin justified),
S246 reject (LangChain page self-states unrelated), S232 reject (0 `allowed[-_ ]tools` hits in
417,416 B), S248 queued→agree (quote verbatim line 348, tier B), C1 kill agree (three worlds at
6/6). No disagreement left unmined — M80-3/M80-4/Q75 already capture the caught signals. The
S248 row is the direct ancestor of r81's S249: same page, same line-348 quote, same 28,395 B /
`ac62c2df…` fetch identity — plan's C2 anchor is grounded in closure-verified bytes.

## 5. Grant-semantics `unprovable-but-better` → SCORECARD text

Closure ruled the r80 rider `unprovable-but-better` (spot-check line 30). Already landed in
SCORECARD: the round-80 annotation reads "form-level only, and the grant-semantics exploratory
rider is unprovable absent a named non-author review. Scores held; no depth move" — and the
"Round 81 (planned)" row already conditioned any depth adjudication on a named non-author
reviewer. **No additional SCORECARD text is required this round for that ruling**; the r81 C2 is
a different, conjunct-based predicate on a new surface (S249), not a re-adjudication of the r80
matrix. The r80 rider stays unprovable for scoring unless a named non-author review occurs — the
plan correctly does not re-litigate it.

## Flags (observations, not gaps)

- S249 reuses S248's canonical URL → expect one new W04 duplicate-URL census warning (class
  already tolerated at 31); plan doesn't name it. Cosmetic.
- Plan § R2 calls the S230/S231 fetch receipts "r80 receipts"; the tracked path is
  `round-79/snapshots/` (r79-era records re-verified r80). Cosmetic.

VERDICT: All four routed r80 defects map to repairs/dispositions in plans/round-81.md (D1 record-only correctly absent; D2→R3; D3→R1+R2 with strengthened W6–W9 controls reproducing the killing classes plus new W9; D4→R5+manifest); base-state DRIFT classes each have a named repair; the unprovable-but-better rider needs no new SCORECARD text — no plan gap found.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R07ClosureLearn.md
