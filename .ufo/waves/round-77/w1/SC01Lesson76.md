# SC01Lesson76 — `corpus/lessons/round-76.md` draft (kotoba round 77, w1, scribe)

Base: lane `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (freeze). Deliverable is a **draft**; nothing was written into
`corpus/`, and no lane file outside `.ufo/waves/round-77/build/` was touched.

## Deliverable

`.ufo/waves/round-77/build/SC01Lesson76.round-76.md` — 154 lines, sha256
`e111ef4f8b609d4b93defd449e4ef752ee41a37cb0f077574bcda34455d28e64` (the bytes the final W1 world measured),
landing target `corpus/lessons/round-76.md`.
`.ufo/waves/round-77/build/SC01Lesson76.counter-receipts.txt` — every command, revision, exit status and output below.

Structure (R76-D2's requirements plus C1's (a)/(e)):

- **First paragraph** states the file is the round-76 lesson **written in round 77**, names R76-D2 and the closure's CD2,
  and bounds itself: "no axis moves with this file".
- **`## Gate`** (single heading, extracted by the counter's own `_gate_section` at 5,498 B / 59 lines):
  - S213 access record — URL `https://agentskills.io/skill-creation/optimizing-descriptions.md`, snapshot
    `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (13,403 B, 196 lines, sha256 `7cc54fbb…bfd837`), that
    digest in four places (MANIFEST, fetch record with HTTP 200 at `2026-10-27T16:57:56Z`, the counter's table, this
    Gate), **access date 2026-10-27** (the fetch-record date), and three independent re-opens (S01Reopen1 curl,
    S02Reopen2 urllib, this seat's own fetch).
  - Located quote, 10 words, `:28` after the page's first heading (line 5), `grep -F -c` = 1 / 0 / 0 across the three
    snapshots (page-unique, not site chrome).
  - Admit (four rules at the r74 S223–S225 guide-advice level; acted on in `SKILL.md` § Body craft; the lane's own
    `description` measured at `2f675548` = 1022 clip / 1021 stripped, first sentence 151, by the counter's
    `description_measures`).
  - Reject held (trigger-rate protocol is instructions, not a run), Reject refused (staged `spec-description-trigger-discipline.md`,
    CORPUS rule 1), Reversed (the r75 Gate's "materially shorter" candidate), candidates/declined with reasons for
    considerthese 2026-10-26 proposals **1–5** (3 taken, 1/2/4/5 declined: baseline-map change · Q67 L0 question ·
    closure procedure · operator fleet policy), Assimilation: none.
- **`## Spot-check`** — the closure's §3 table carried as recorded (agree / agree / agree-with-caveat / —), explicitly
  "not re-judged here", pointing at `corpus/lessons/round-76-verifier-spotcheck.md`.
- **`## Mistakes`** — six rows, classes only from the CORPUS/mistakes vocabulary:
  `M76-1 number-drift` (folded-scalar read as six frontmatter lines: 14/76/78/73/79/72 = 392 of 1022, reproduced here),
  `M76-3 vacuous` (the red-before probe exited 2 on a missing file), `M76-5 scope`, `M76-6 number-drift` (53% vs 22/64),
  **`M76-7 attribution`** (the `| tail` capture — the required row; `base-battery.txt:2-6`/`:7-11` plus the three r76
  diagnoses and the r54 recurrence), **`M76-8 landing`** (the required R76-D1 stray-path commit, still in `HEAD`).
  A closing note drops the draft's M76-2 (subsumed by M76-1's convention) and M76-4 (see below) with the read that dropped them.
- **`## Routed defects`** — R1–R4 recorded **un-landed** at `6ce2724`, re-routed as R76-D3 = round 77's C2; D2/D3 prepared
  but un-landed; D4 landed (floors 250 / 47 in `floors-registry.json:65-73`); D5 conditional; R76-D1 open; R76-D5's
  52-vs-64 gap.
- **`## Status changes`** — S213 `used-by` old → new with **both concrete values**, the same-commit constraint and the
  census `E11` failure when they split, and "no other cell changes".

## Gate conformance (what the frozen counter reads)

| conjunct | requirement | draft |
|---|---|---|
| (a) | lesson `## Gate` carries URL, an access date matching `fetch-record.json`, a ≤25-word quote located after the first heading, and the optimizing-descriptions digest | all four present; counter prints `(a) snapshot chain: pass` |
| (e) | S213's `used-by` lists the entry **and** the old→new change is logged in the lesson | logged with both values, comma+space exactly as `OLD_USED_BY` expects; counter prints `(e) registry: pass` |

## Verification (frozen bytes, scratch clone, gate's own exit status)

`verifiers/check_desc_craft.py` sha256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` — equals the plan's pin.

| world | rev | result |
|---|---|---|
| W0 red-before, no lesson | `2f675548` | `description craft backed 0 of 6`, exit 1 — `(a) corpus/lessons/round-76.md is not committed` |
| W1 draft + used-by append | `d1de60a` | **(a) pass, (e) pass**, `2 of 6`, exit 1; (b)/(c)/(d)/(f) fail only for the absent entry/SKILL row |
| W2 digest → 64 zeros | `1d79e10` | (a) fail `names no digest`, `1 of 6` |
| W3 every `2026-10-27` → `2026-10-20` | `55a7478` | (a) fail `access date … does not match the fetch record date`, `1 of 6` |
| W4 quote replaced by a best-practices-only sentence | `4012834` | (a) fail `no <=25-word quote located`, `1 of 6` |
| W5 old→new log stripped | `aa5895b` | (e) fail `does not log the old->new used-by change`, (a) still pass, `1 of 6` |
| counter `--self-test` | frozen blob | `0 failure(s) over 53 assertions`, exit 0 |

So (a) and (e) are **load-bearing**, not presence floors: four independent mutations each turn exactly the mutated
conjunct red while the other one stays green.

S213 re-open by this seat: HTTP 200, 13,403 B, 196 lines, sha256 `7cc54fbb…bfd837`, `cmp` against the committed snapshot
exit 0, quote count 1. Third open of the round; S01/S02's records agree.

## Defects found in the inputs (the drafts were treated as inputs, not evidence)

1. **Q74 and Q75 are not landed.** The r76 lesson draft cites Q74 as "added this round in `corpus/QUALITY.md`";
   `corpus/QUALITY.md` at `2f675548` ends at **Q73** (`grep -o 'Q7[0-9]' | sort -u` → Q71 Q72 Q73), and the Q74 row exists
   only as `.ufo/waves/round-76/build/B08-q74-quality-row.diff`. The Q75 row is a round-77 draft
   (`.ufo/waves/round-77/build/SC03QualityRows.quality-rows.md`). Both fix cells say so; a lesson row is not a guard.
2. **The draft's F7 row (M76-4) does not reproduce.** It claims `check_skill_evals_v2.py` pins S213's `used-by` to one
   path and that an append turns it red. The delivered blob at `:289-292` splits the cell on commas and tests membership,
   and the message the draft quotes (`S213 used-by != …`) does not occur (`grep -c` → 0). Not carried; recorded in the
   lesson's dropped-rows note. (The append is safe against that counter — confirmed by (e) passing beside it.)
3. **The draft's receipt line refs were off by one** (`base-battery.txt:3-7` / `:9-11`). Line 2 is the integrity header,
   3–5 the JSON tail, 6 `exit=0`; line 7 the independent-gate header, 8–10 the tail, 11 `exit=0`. Corrected to
   `:2-6` / `:7-11` (caught by seat `SC03QualityRows`, verified against `cat -n`).
4. **The draft presented R1–R4 as closed.** At `6ce2724` the frozen counter reads `0 of 4` with `R1: open … R4: open`, and
   `r1-folded-render.txt` / `w2-registry-note.md` are un-committed `build/` drafts. The lesson records them un-landed and
   re-routed.
5. **The (e) arm is weaker than it reads.** It accepts a paragraph that merely contains the words `old` and `new` beside
   the entry path; the W5 control only failed after the `OLD_USED_BY` token and the phrase "new entry" were also removed.
   My paragraph names both concrete values, so the count is not affected, but a reviewer should know the arm's shape.
6. **The spot-check's `.ufo/l0-questions.md:174` does not resolve in the lane.** No such file exists in the lane repo; the
   question is the fleet root's `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:174` (kotoba round-73, the registry-move
   item). The lesson cites the fleet path and says why.
7. **Draft rows not carried:** M76-2 (slice off-by-one) is subsumed by M76-1's clip/stripped convention; M76-4 per item 2.

Cheap checks behind the lesson's own sentences, all re-run rather than relayed: `scripts/sources-census.sh validate
--file corpus/SOURCES.md` in the W1 world prints `E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`
and exits 1 (the Status-changes claim); the counter's `description_measures` returns `(1022, 1021, 151)` at `65a5c7a`,
`ac9f295`, `b7f13f4b`, `4de12b61` and `2f675548` (the Reversed paragraph); `SKILL.md` at `2f675548` is 590 lines /
78,647 B; `corpus/SOURCES.md` holds 151 `| S<id>` rows.

## Coordination

`SC03QualityRows` anchors Q74 on § Mistakes **M76-1** and Q75 on **M76-7**. I confirmed both IDs, supplied the exact row
ids and the "not landed" caveat, and — on their pointer set — added the r54 recurrence
(`.ufo/waves/round-54/falsify/W2CriticLesson.md:87`, "that is `tail`'s exit code, not the counter's") and the three r76
diagnoses to M76-7. All five pointers they listed resolve at `6523ace` (each line read).

## Out of scope / open

- **Index row** for the lesson in `corpus/README.md` (`verify_corpus_integrity.py` treats unindexed lesson files as red);
  R76-D4's job, L1 integration.
- **No lane byte edited**; the S213 `used-by` append exists only in the scratch clone. `git status --porcelain` in the lane
  shows only untracked `.ufo/waves/round-77/…` items (mine and siblings').
- **R76-D1 stray tree still present** at the base: `kotoba-shokukin/` holds two files (r75's `R75Facet48.md` and r76's
  `A18ScoutSnapshot.md`); removal is a lane commit, not mine.
- Lesson is a draft: the counter's `(a)`/`(e)` cannot be claimed for the lane until the L1 lands it with the same commit
  as the `used-by` append.

## Tooling

No installs and no upgrades. Nothing created or modified in any PATH directory; pacman not invoked.

## Scratch

`/fast/scratch/hyaku/kotoba-r77/SC01Lesson76` (shared clone + 7 output files) — removed before yield; the outputs are
reproduced verbatim in `SC01Lesson76.counter-receipts.txt`.

VERDICT: Draft `corpus/lessons/round-76.md` is complete for R76-D2 and turns the frozen C1 counter's (a) and (e) green (2 of 6, with four mutations each isolating one conjunct red), while recording r76's own repair landing state as un-landed rather than closed; three r76-draft claims (Q74 landed, F7 exact-match pin, R1–R4 closed) do not reproduce and are corrected or dropped.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC01Lesson76.round-76.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC01Lesson76.counter-receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/SC01Lesson76.md
