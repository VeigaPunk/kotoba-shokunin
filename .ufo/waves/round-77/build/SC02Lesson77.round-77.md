<!-- BUILD DRAFT — seat SC02Lesson77 (kotoba round 77, wave w1). Landing target `corpus/lessons/round-77.md`.
     The L1/integrator drops this comment, fills every `[[SLOT: ...]]` marker, and lands the file after claim data.
     Nothing below is claim data: every number and path was read from the r77 freeze commit 6523ace or from the
     r76 wave artifacts named beside it. Red-before evidence: `.ufo/waves/round-77/build/SC02Lesson77.red-before.txt`. -->

---
author: kotoba L1 (hyaku run 10, round 77, attempt 1)
date: 2026-10-27
round: 77
lane: kotoba
---

# Round 77 lessons — kotoba

Claims (frozen in `plans/round-77.md` at `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; both counters unchanged
from the r76 freeze and re-hashed at 6523ace — `verifiers/check_desc_craft.py` sha256
`cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`, `verifiers/check_r75_routed_repairs.py`
sha256 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`): **C1 depth (sourced)** —
`python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed 6 of 6`; **C2 consistency
(calibration sub-axis)** — `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed
repairs closed 4 of 4`. Red at base, receipts committed at 6523ace: C1 `description craft backed 0 of 6`, exit 1
(`.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`); C2 `r75 routed repairs
closed 0 of 4`, exit 1 (`.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`).
Final-tip values: [[SLOT: C1 and C2 measured values at the final tip, each with the receipt path whose first line names that same revision]].

## Gate

### S213 re-opened this round (two independent seats)

S213 — `https://agentskills.io/skill-creation/optimizing-descriptions.md` — is an existing row (registry table,
`corpus/SOURCES.md:153`; status `mined`, recheck `90d`, `used-by` a single entry at base). The plan re-opens it
**by two independent seats** and requires a digest that matches the pinned `7cc54fbb…bd837`; any differing digest
stops C1 until a new, pre-data addendum re-pins it. Each seat records URL, access date, a ≤25-word located quote
and the sha256 of the bytes it fetched.

- [[SLOT: S01Reopen1 — access date, HTTP status, sha256 of the fetched bytes, the ≤25-word located quote with its line and its page-unique check]]
- [[SLOT: S02Reopen2 — the same five fields, independently]]
- [[SLOT: digest verdict — both values against the pinned 7cc54fbb…bd837 and against each other; on disagreement: C1 stopped and the addendum that re-pins it]]

### Decisions taken this round

**Admit.** [[SLOT: each admit, its reason, and the evidence pointer (entry / counter conjunct / seat report)]]

**Reject.** [[SLOT: each reject, the reason grounded on an observed fact, the flip that would reverse it, and the evidence pointer]]

Carried by `plans/round-77.md` § Trigger, not re-argued: considerthese proposals 1, 2, 4 and 5 stay declined
with the r76 reasons. Those reasons are recorded in `plans/round-76.md` § Trigger and in the r76 closure's §3 —
**not** in a round-76 lesson Gate: `corpus/lessons/round-76.md` is absent at the r77 base
(`git cat-file -e 6523ace:corpus/lessons/round-76.md` exits 128; `ls corpus/lessons/round-76*.md` prints only the
spot-check file). [[SLOT: after the r76 lesson lands, the file+line where each decline reason is now recorded, or that the decline still stands with no lesson record]]

**considerthese mined: proposal 3** (`considerthese/2026-10-26.md:17`, "Land the page round 74 rejected, then use
it on the skill's own description") — C1's motivation again: admit the description-writing half of S213 at the
r74 S223–S225 guide-advice level and turn it on kotoba's own `description`. The page's size figures in that
proposal are historical, not a round baseline: the r75 lesson records them as `stale-premise`
(`corpus/lessons/round-75.md` § Mistakes), and the render convention the counters measure is fixed by
`plans/round-76-addendum-1.md` (clip-preserving 1022 characters, stripped 1021 at the r75 tip).
[[SLOT: what the mined proposal actually produced, and the reconciliation of its 1,021 figure with the clip-1022 convention — C2's R1 correction is the governing record]]

### Census

Before: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
→ `kotoba ok`, 20 W04 duplicate-URL warnings, `exit=0` (`.ufo/waves/round-77/receipts/census-before.txt`,
committed at 6523ace; the last two lines of that file are the `kotoba ok` line and `exit=0`).
After: [[SLOT: the same command at the final tip — row count, warning set, and the command's own exit status]]

### Rows touched (old → new)

S213 `used-by` at 6523ace, measured: `corpus/knowledge/skill-eval-artefacts-round70.md` (single member; 12th cell
of the row). [[SLOT: S213 used-by new value as landed, with the commit that carries it — expected form: the r70 path plus `, corpus/knowledge/description-craft-round76.md` as an exact comma-delimited member (addendum 2 §4)]]
[[SLOT: every other row changed in place (allowed cells only: status, recheck, used-by), old → new, or "no other row"]]

## Mistakes

Two rows, one per mistake — CORPUS.md: "One row per mistake." Both mine step-1 conformance defects of the
**round-76 non-author closure** (`corpus/lessons/round-76-verifier-spotcheck.md` §1, CD1 and CD2). Neither was
mined before: the file that owed them, `corpus/lessons/round-76.md`, has never existed. The red-before column
names the command, the state it reads at the r77 base, and the receipt that holds the bytes; CORPUS.md:179 makes
a fix count only once it is shown able to fail.

| id | class | evidence pointer | captured-by | fix | red-before, and the green-after with the fix as only delta |
|---|---|---|---|---|---|
| M77-1 | landing | CD2, `corpus/lessons/round-76-verifier-spotcheck.md:26`: the plan says the declined-proposal reasons are "recorded in the round-76 lesson Gate" and the lesson does not exist. Measured at 6523ace: `git cat-file -e 6523ace:corpus/lessons/round-76.md` exits 128 while both `plans/round-76.md` and `plans/round-77.md` name the path, and the frozen C1 counter fails conjunct (a) with `corpus/lessons/round-76.md is not committed at the measured revision` (`.ufo/waves/round-77/receipts/.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`) | none for "a plan's promised artefact exists at the round's tip"; nearest are Q65 (a plan's promised landing is checked — arithmetically, on the SKILL.md budget, not for existence) and Q60 (the `git cat-file -e` existence mechanism, scoped to a citation-with-revision, not a forward promise); sweep in `build/SC02Lesson77.red-before.txt` §4 | Run a check over the round's own plan in the no-harm battery: every `corpus/**.md` path the plan names must exist at the measured revision. The check measures existence only (Q26); that the lesson carries a real `## Gate` and `## Mistakes` stays C1 (a)/(e) and the closure's judgement | `build/SC02Lesson77.red-before.txt` §3: at 6523ace the check exits 1 naming `corpus/lessons/round-76.md` and `corpus/knowledge/description-craft-round76.md` (9 plan-named paths, `exit=1`); its lesson arm (3 paths) turns `exit=0` in the sandbox commit `a0c4762f…` once a file exists at the named path — existence only, labelled fixture |
| M77-2 | reference-drift | CD1, `corpus/lessons/round-76-verifier-spotcheck.md:25`: the recovery commit added a typo'd root. Measured at 6523ace: three tracked paths — `.ufo/waves/round-76/w1/A18ScoutSnapshot.md` and `kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` are byte-identical (both sha256 `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb`), and `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` is the **only** copy of that seat report (its declared path `.ufo/waves/round-75/w1/R75Facet48.md` exits 128), against the r75 lesson's own row claiming it was "Copied byte-exact to the same relative lane path" (`corpus/lessons/round-75.md:12`) **and** the r75 closure's endorsement of that recovery — `corpus/lessons/round-75-verifier-spotcheck.md:44` reads "Misroot `R75Facet48` recovered: `git diff --numstat` carries `22 0 kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md`; `git ls-tree -r ac9f295…` confirms it" — the numstat line it cites contains the typo path, so the closure checked the tree against the diff's own spelling instead of the declared seat path | Q49 partially — it bounds seat-report lane-locality and the final misroot sweep, but the sweep in both rounds looked outside the lane, and no row bounds the lane tree's own top-level entries; none for a lane-internal typo root or for "a lesson's own recorded fix path resolves" | Restore `R75Facet48.md` to `.ufo/waves/round-75/w1/R75Facet48.md` (bytes equal, sha256 `a419cc6f…fdd9`) **before** removing the typo root (Q22 custody: it is the only copy), then `git rm -r kotoba-shokukin`; add check1 to the no-harm battery — the tracked top-level entries must equal the lane's declared roots (pinned allowlist, Q28; a legitimate new root needs a ledger arm, Q73 pattern); strike R76-D1's "removed" in favour of the measured tree state | `build/SC02Lesson77.red-before.txt` §2: at 6523ace check1 exits 1 printing `kotoba-shokukin` and naming both files; at the sandbox commit `a0c4762f…` it exits 0 with fix A as the only delta |
| [[SLOT: id, e.g. M77-3]] | [[SLOT: class — CORPUS.md vocabulary: vacuous / survivor / stale-premise / reference-drift / number-drift / scope / attribution / landing / provider]] | [[SLOT: evidence pointer — file:line plus the command and its measured value]] | [[SLOT: the QUALITY.md criterion or protocol rule that should have caught it, with the line, or `none` after a shown grep]] | [[SLOT: the fix, named by its mechanism]] | [[SLOT: red-before command, its non-clean output and exit, and the commit or receipt holding it]] |

[[SLOT: further mistake rows this round adds from its own waves — one row per mistake, same six cells]]

Follow-up this table owes (append-only, not a rewrite): the r75 lesson's misroot row names a lane-relative path
the tree never carried, and its fix text is contradicted by `ac9f295` and by 6523ace; the r75 closure's line 44
endorses the same recovery. The closure file is outside the lane's edit rights (its header: written by the hyaku
closure, never edited here), so the correction has to live in a lane-owned file — `corpus/lessons/round-75.md` as
an appended correction, or this lesson, naming `round-75-verifier-spotcheck.md:44`.
[[SLOT: whether `corpus/lessons/round-75.md` gets an appended correction for that row, and the commit — it must not disturb C2 R1's appended M75-1 correction in the same file]]
`plans/round-77.md` § Trigger currently lists R76-D1 as "stray `kotoba-shokukin/` path removed" while the r77
base carries it; the sentence is false of the base it names. It becomes true only by the restore+delete landing —
not by the sentence.
[[SLOT: the landing commit that makes R76-D1 true of the tip (restore to `.ufo/waves/round-75/w1/`, then drop `kotoba-shokukin/`), with its candidate diff — or, if it does not land, the disclosure that the base record and the R76-D1 sentence stay in conflict]]

## Spot-check

Owed to the non-author closure (LEARNING.md: at least one admit and one reject, each re-opened by a reviewer who
is not the lane). The lane does not fill this section.

[[SLOT: per-claim re-derivation by the non-author closure, with the commands it ran and the receipts]]
[[SLOT: discernment sample — at least one admit and one reject, each with the source re-opened and the reviewer's agree/disagree]]
[[SLOT: verdict — admitted / not admitted / honest stop — and every axis unchanged or moved, with the reason]]
[[SLOT: any defect the closure routes to the next round]]
