# SC05ScorecardDrafts — round 77, wave w1 (scribe)

Date: 2026-10-27. Seat: `SC05ScorecardDrafts` (scribe, leaf; no subagents, no background jobs).
Milestone: Round 77 w1 — build + first falsifiers for C1 description-craft (sourced depth) and C2 r75 routed
repairs (consistency); counters frozen unchanged from r76.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`), base per plan
`2f675548eaad2a037a899d39247c1fd7a88aaf48`.

## Behavior

I drafted the SCORECARD.md updates and nothing else: the two round-77 axis-row clauses (depth, consistency),
the two move-log rows, and the `planned` replacement for round 78. All three sit in
`.ufo/waves/round-77/build/SC05ScorecardDrafts.scorecard-rows.md`; no lane file was edited (the L1
integrates).

Method: read `plans/round-77.md` in full, `plans/round-76.md` § C1/§ C2, `plans/round-76-addendum-1/4/5/6.md`,
the two frozen counter docstrings, `SCORECARD.md:1-60` (rubric, axes-table shape, both target rows),
`:168-181` (end of § planned), `:240-320` (move-log tail, Capabilities tail), `:460-469` (annotation tail),
the r76 build drafts (`scorecard-draft.md`, `entry-draft.md`, `skill-patch.md`, `sources-patch.md`), the r77
base receipts and the r76 snapshot set. The r76 draft was treated as an input to verify, not a source of
facts; every number it carried was re-derived or is left as a slot.

Decisions taken (stated in the draft, not silently):

- **HOLD on both scores** (depth 9, consistency 10), because the rubric's band 10 is "repeated non-author
  verification in the opposite direction" and this seat, like the lane, is the author of both counter and
  data. `Last change` cells are preserved (`60` / `15`) since no score moves; only the evidence cell gains a
  leading `**round 77 (…) —**` clause, old cell content untouched.
- **Predicate sentences are byte-copied from `plans/round-77.md:26` and `:38`** (Q26). Verified
  programmatically: each appears exactly once in the draft, verbatim, including the C2 variant
  `(r76 base \`b7f13f4…\`)` — which is not the C1 variant `(the r76 base was \`b7f13f4…\`)`.
- **No `**Round 77 completed …**` line pre-written** in § planned: the disposition is the closure's.
- **After-values, tip receipts and both control receipts are slots** (9 unique slots), because no data or
  tip measurement exists at authoring time and I ran none.

## Gates

None run by this seat, and none claimed. This is a scribe item: no build, no lint, no test, no counter run
at any tip, no mutation, no install (no tool installed; `pacman` untouched, per the paused host policy).
The gate results quoted inside the draft are **committed receipts I read**, not runs I made:

- `.ufo/waves/round-77/receipts/c1-base-2f675548….txt` → `description craft backed 0 of 6`, `exit=1`, with
  all six conjuncts `fail` and the per-conjunct reasons.
- `.ufo/waves/round-77/receipts/c2-base-2f675548….txt` → `r75 routed repairs closed 0 of 4`, `exit=1`, R1–R4
  all `open`, nine per-repair fail notes.
- `.ufo/waves/round-77/receipts/selftests-base.txt` → `0 failure(s) over 53 assertions` (C1) and
  `0 failure(s) over 27 assertions` (C2), `exit=0` each.

Read-only verification I did perform (exact commands and outputs):

```
$ sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py
cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e  verifiers/check_desc_craft.py
989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63  verifiers/check_r75_routed_repairs.py
$ git show 2f675548eaad2a037a899d39247c1fd7a88aaf48:verifiers/check_desc_craft.py | sha256sum   # and the C2 counter
cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e  -                            # (same at base)
989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63  -                            # (same at base)
$ git show ec7f853:verifiers/<counter>.py | sha256sum     # r76 freeze commit, type=commit
same two digests -> counters truly unchanged since the freeze
$ sha256sum .ufo/waves/round-76/snapshots/*.md  vs  snapshots/MANIFEST.sha256  vs  fetch-record.json
7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837  optimizing-descriptions.md (13,403 B, HTTP 200)
a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684  evaluating-skills.md
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  best-practices.md
    -> MANIFEST, fetch-record and the counter's in-file table (check_desc_craft.py:142) all agree
$ python3 -B -c "<import verifiers/check_desc_craft.py; description_measures(SKILL.md)>"
measures (clip,stripped,first): (1022, 1021, 151)     # identical at HEAD and at base 2f675548
$ awk 'NR==153' corpus/SOURCES.md  ->  used-by today = corpus/knowledge/skill-eval-artefacts-round70.md
```

## Touched surfaces

- Wrote `.ufo/waves/round-77/build/SC05ScorecardDrafts.scorecard-rows.md` (17,576 bytes).
- Wrote this report `.ufo/waves/round-77/w1/SC05ScorecardDrafts.md`.
- Nothing else. `git -C <lane> status --porcelain` shows only untracked wave files owned by other seats
  (`.ufo/waves/round-77/build/`, `.ufo/waves/round-77/receipts/E05*`, `E10*`, …); no tracked lane file, no
  index entry and no jj state was modified by me. No scratch directory was created (no clone, mirror or temp
  work was needed: every check above is a read or an in-memory compute), so there is nothing to remove. No
  fleet-repo write.

## Findings for the L1

- **F1 (input defect, r76 draft header).** `scorecard-draft.md`'s header says "at authoring time
  `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` are absent from the base tree
  and the receipts dir is empty". False against the r77 base (and against the r76 freeze): both counters are
  committed at `2f67554` with the pinned digests, and `.ufo/waves/round-77/receipts/` holds the base receipts.
  I did not carry that sentence into the draft.
- **F2 (input defect, r76 draft body).** The r76 draft wrote a completed measurement it never ran
  (`description craft backed 6 of 6`, exit 0 at `<tip>`), with the depth bullet truncated mid-word
  ("admitted at guide-…"). My draft keeps the before-value as measured and leaves the after-value as a slot.
- **F3 (Q26 asymmetry, expected but worth naming).** The frozen counter docstrings state the **r76** base
  (`b7f13f4b…`) as "base", while the r77 plan's Q26 sentence states the r77 base with the r76 base in
  parentheses. The counters may not be edited, so the SCORECARD row and the receipt label carry the plan's
  r77 sentence and the docstring carries the older form. Recorded, not repaired.
- **F4 (SCORECARD hygiene).** § planned is stale: its last `**Next:` line inside the section is
  `**Next: round 44**` (`:166`), and the file's actual last forward pointer is `**Next: round 67**` at
  `:371`, outside § planned (after § Saturation). My §3 gives the insertion point at the end of § planned
  and leaves `:371` as a record; whether to re-house it is the L1's call, not a scribe's.
- **F5 (band reasoning, disclosed limit).** The C1 row must not read as "the description now follows the
  advice": the r76 entry's own audit marks imperative phrasing **not met** and "A few sentences to a short
  paragraph" **not met** at 1,022 of 1,024 characters. I put that limit inside the depth clause so the row
  cannot be read as a compliance claim.
- **F6 (controls).** `.ufo/waves/round-77/receipts/c1-controls.txt` and `c2-controls.txt` do not exist yet
  (E01/E02 own them); the r76 control receipts were scored on an earlier counter blob (`87837d7a…`). The
  draft therefore carries slots rather than citing receipts that do not exist.

## Out of scope (untouched)

No claim data (entry, `SKILL.md` row, `SOURCES.md` cell, lesson rows), no counter edit, no SCORECARD.md
edit, no LOG/QUALITY/README edit, no snapshot or receipt write, no git/jj write, no MANIFEST/templates/
scripts/.ufo/state/.scratch/considerthese writes, no fleet-root write, no tool install, no subagent.

## Deliverables

`.ufo/waves/round-77/build/SC05ScorecardDrafts.scorecard-rows.md` — §1 depth and consistency row clauses
(HOLD, band reasoning, predicate sentences verbatim, before → slot); §2 the two move-log rows
`| 77 | depth | … | [[SLOT]] | … |` and `| 77 | consistency | … | [[SLOT]] | … |`; §3 the `**Next: round 78**`
replacement; §4 the verification table; §5 bounds and the slot list.

VERDICT: SCORECARD draft delivered for round 77 — depth 9 and consistency 10 both HOLD with band reasoning, predicate sentences byte-identical to plans/round-77.md:26 and :38, after-values/receipts as slots (no tip measurement exists), planned round-78 entry drafted; r76 draft input's false "counters absent" header and its unrun `6 of 6` claim reported as findings; no lane file, index or jj state touched.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC05ScorecardDrafts.scorecard-rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/SC05ScorecardDrafts.md
