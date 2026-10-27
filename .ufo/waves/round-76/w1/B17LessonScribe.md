# Seat B17LessonScribe — round 76, wave w1

Seat: `B17LessonScribe`, scribe (leaf, no subagents). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base `b7f13f4b39cbd43076a85568adca763a6f674e7a`; lane tip observed while drafting
`eab64394dba08a47f6797a2e23719be14675b44b` (HEAD moved twice during the seat: `7eed80e` addendum,
`eab6439` role mix). Assignment: draft `corpus/lessons/round-76.md` to
`.ufo/waves/round-76/build/lesson-draft.md`; report only.

## Delivered

`.ufo/waves/round-76/build/lesson-draft.md` — 221 lines, 21,726 bytes, 3,053 words, sha256
`b5a86a91b19359d6692e0f4a0f51483dcda40c8f53da6cc5174d2cf4a640d9ba` (final, after peer review — § 6).
Five sections: `## Gate` (line 26), `## Mistakes` (112), `## Routed defects` (123), `## Round honesty` (180,
an extra section on the r73/r74 precedent), `## Status changes` (207). Content: S213 re-open record with URL,
access date and a 10-word located quote; one admit and two rejects plus the r75 reject reversed; proposals
1/2/4/5 declined with reasons; assimilation none with the staged-package refusal; six mistake rows (M76-1, a
slice off-by-one, a vacuous red-before, a reference-drift, and M76-5/M76-6 from the validated dispatch);
R1–R4 dispositions, D1–D5 states, one forward route; S213 `used-by` logged old→new.

## 1. Measurements this seat took (commands, observed output, exit code)

### 1.1 The render quartet — 1022 clip / 1021 stripped / 151 first sentence, block lines 4–18

`python3 -B` over `git show <rev>:SKILL.md`, slice `lines[:index("---",1)]` joined with `"\n"` plus a
trailing newline, `yaml.safe_load(...)["description"]`:

```
65a5c7a6 clip=1022 stripped=1021 bare-slice=1021 first-sentence=151 block=4-18
ac9f2951 clip=1022 stripped=1021 bare-slice=1021 first-sentence=151 block=4-18
b7f13f4b clip=1022 stripped=1021 bare-slice=1021 first-sentence=151 block=4-18
4de12b61 clip=1022 stripped=1021 bare-slice=1021 first-sentence=151 block=4-18
```

`bare-slice` is `s[:s.index("\n---",4)]`, which drops the folded scalar's clip newline: **that is the
1021/1022 boundary** (M76-2 in the lesson, § 3 F-4 below). Exit 0.

### 1.2 The Gate quote is verbatim, page-unique, after the first heading, 10 words

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ Q='A few sentences to a short paragraph is usually right'
$ for f in optimizing-descriptions evaluating-skills best-practices; do printf '%s\t%s\n' "$f" "$(grep -c -F -- "$Q" .ufo/waves/round-76/snapshots/$f.md)"; done
optimizing-descriptions	1
evaluating-skills	0
best-practices	0
$ grep -n -F -- "$Q" .ufo/waves/round-76/snapshots/optimizing-descriptions.md | cut -c1-40
28:* **Keep it concise.** A few sentence
$ python3 -c "print('words',len('$Q'.split()))"
words 10
```

First page heading is line 5 (`# Optimizing skill descriptions`), so line 28 is after it. Exit 0.

### 1.3 Snapshot digests and manifest

```
$ sha256sum .ufo/waves/round-76/snapshots/*.md
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  .ufo/waves/round-76/snapshots/best-practices.md
a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684  .ufo/waves/round-76/snapshots/evaluating-skills.md
7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837  .ufo/waves/round-76/snapshots/optimizing-descriptions.md
$ cd .ufo/waves/round-76/snapshots && sha256sum -c MANIFEST.sha256
optimizing-descriptions.md: OK
evaluating-skills.md: OK
best-practices.md: OK
exit=0
```

My own independent `curl -sS` of the URL on 2026-10-27 returned HTTP 200, 13,403 bytes, sha256
`7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` — the same digest as the snapshot and
`fetch-record.json`. **Operability note (F-6):** `sha256sum -c MANIFEST.sha256` fails from the repo root
(`FAILED open or read`, exit 1) because the manifest lists bare filenames; it passes from the snapshot
directory. Not a defect in the bytes, a cwd contract; B26's receipt already cd's.

### 1.4 Fixture: what the S213 `used-by` append does to `check_skill_evals_v2.py` and to the census

A `git clone --shared` of the lane at `b7f13f4` under
`/fast/scratch/hyaku/kotoba-r76/B17LessonScribe/fx` (`git rev-parse --show-toplevel` asserted the fixture
path before any write), one `edit` of S213's `used-by` cell to B14's verbatim new text, one fixture commit
`7e37c1d` (`git -c user.name=fixture … commit`), row still `NF=13`.

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_skill_evals_v2.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a; echo exit=$?
measured-rev: b7f13f4b39cbd43076a85568adca763a6f674e7a
skill eval artefacts verified 2 of 10
  SKILL.md: 0 rendered lines name the entry + S211/S212/S213 (want exactly 1; 1 name the path, 1 rejected)
exit=1

$ python3 -B verifiers/check_skill_evals_v2.py --repo <fixture> --rev 7e37c1d; echo exit=$?
measured-rev: 7e37c1d
skill eval artefacts verified 1 of 10
  SKILL.md: 0 rendered lines name the entry + S211/S212/S213 (want exactly 1; 1 name the path, 1 rejected)
  F7: S213 used-by != corpus/knowledge/skill-eval-artefacts-round70.md (exact match required)
  A10: census validate --file non-zero at --rev
exit=1

$ cd <fixture> && bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md; echo exit=$?
… 20 × W04 …
file	E11	S213 missing used-by corpus/knowledge/description-craft-round76.md
exit=1
```

F7's condition is `verifiers/check_skill_evals_v2.py:288` (`if row[10].strip() != ENTRY:`). Both
consequences are in the lesson (M76-4 and § Status changes' landing constraint) and in § 3 below.

## 2. Gates

| Check | State |
|---|---|
| Lesson carries the five required sections | pass (section list above) |
| `## Gate` has URL + access date + ≤25-word located quote from the snapshot | pass (§ 1.2; 10 words, line 28, page-unique) |
| Admit ≥1 and reject ≥1 recorded | pass (one admit, two rejects, one r75 reject reversed) |
| Proposals 1/2/4/5 declined with reasons | pass (Gate, four bullets) |
| Assimilation none with the staged-package refusal reason | pass (Gate) |
| `## Mistakes` rows carry class/evidence/captured-by/fix | pass (6 rows, 5 pipes each) |
| R1–R4 dispositions, D1–D5 states, forward route | pass |
| S213 `used-by` old→new logged | pass (verbatim cells from B14) |
| Table integrity (pipe count per row) | pass (`awk gsub` → 5 pipes on all 8 table lines) |
| `check_desc_craft.py` / `check_r75_routed_repairs.py` run | **not run — neither file existed in the tree at write time** (`ls verifiers/ | grep -E 'desc_craft|r75_routed'` empty). Not claimed as green. |
| No-harm battery at tip | **not run by this seat** (main-agent verification per the seat contract); the plan's post-state battery and its receipt are other seats'. |
| Lane file beyond the two named draft paths | none written |

## 3. Findings (for the integrator; verbatim conflicts kept for the canonical judge)

**F-1 `F7` exact-match vs the append-only registry (new, routed to r77).** Verified in § 1.4: the append
that C1 (e) requires moves `check_skill_evals_v2.py` from `2 of 10` to `1 of 10` (exit 1 both ways — a red
counter moving red-er, not a green→red regression), with `F7: S213 used-by !=
corpus/knowledge/skill-eval-artefacts-round70.md (exact match required)`. The plan's no-harm list does not
name this counter; the lesson's M76-4 does, and routes the fix.

**F-2 C1 (a) vs `CORPUS.md` rule 2 — resolved before data by addendum 1.** B14 reported verbatim:
"plan C1(a) says the optimizing-descriptions digest must equal 'the digest recorded in the S213 row's anchor
update', and S213's anchor currently carries no sha256 … so (a) is unsatisfiable via used-by alone", and
"CORPUS.md rule 2 permits in-place change of status/recheck/used-by only". `plans/round-76-addendum-1.md`
(committed `7eed80e9`) withdraws the clause and pins the digest in four homes, the fourth being the lesson's
`## Gate`. The lesson records the withdrawal and does not claim an anchor change.

**F-3 The plan's wave-shape numbers do not match the dispatch (M76-5, M76-6).** Measured from
`.ufo/waves/round-76/w1-spec.json`: 64 seats = executor 15, scribe 10, reviewer 10, scout 10, critic 6,
mutation-tester 4, simplifier 3, revenger 3, sentinel 2, connector 1 → attack 22 of 64 = 34.4%. The plan's
§ Wave shape says "30 build + 34 attack (attack share 53%)" and budgets `labrat` 4 + `sonic` 1, which the
dispatch validator refuses (`unknown_role`; 0 such seats in the spec). The lesson's claim line states the
dispatched mix, and both rows are in `## Mistakes`.

**F-4 B21RevMethod's window sum is arithmetically wrong; the lesson does not propagate it.** `w1/B21RevMethod.md`
§ 2 states the r75 window measured "372 of 1022" characters. Its own printed lengths are `14,76,78,73,79,72`,
which sum to **392** (`14+76+78+73+79+72`), as B08's notes also state. The lesson's M76-1 row says 392 and
names B21's 372 as a mis-sum; that is the only correction I made to another seat's text.

**F-5 Wave timing left five attack reports without a subject.** `A01RevQuoteLocate`, `A02RevHashChain`,
`A17CritAudit` and `A34ScoutReceipts` inspected an empty `build/` (or absent receipts) and returned
blocked/incomplete rather than verdicts; `A11MutRedBefore` ran the counters from a base checkout and got
`can't open file …: [Errno 2] No such file or directory`, exit 2 ×4, INCONCLUSIVE. The lesson records this
in `## Round honesty` and M76-3; these five are not counted as falsification evidence either way, and the
re-runs are the integration's.

**F-6 `MANIFEST.sha256` is cwd-relative** (§ 1.3): a reader running `sha256sum -c` from the lane root sees
three FAILED lines. Worth one clause in the counter docstring or the receipt.

**F-7 Landed-state caveat (honesty).** At write time these were drafts or absent, so every disposition in
the lesson is the round's *intended* landing, each tied to the artifact and counter arm that will read it:
`verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` (absent), `receipts/r1-folded-render.txt`
and `receipts/noharm-at-tip.txt` (absent), `.ufo/waves/round-76/w2-registry-note.md` (draft at
`build/w2-registry-note.md`), the R1 correction in `corpus/lessons/round-75.md` and the Q74/M76-1 rows
(drafts at `build/B08-*.diff`), the entry (`build/entry-draft.md`), LOG § Round 75/74 and § Round 76
(`build/log-draft.md`), SCORECARD (`build/scorecard-draft.md`). The integrator must confirm each before the
lesson is read as closing anything.

## 4. Touched surfaces

Wrote, inside the lane only:
- `.ufo/waves/round-76/build/lesson-draft.md` (new)
- `.ufo/waves/round-76/w1/B17LessonScribe.md` (this file)

Read-only elsewhere. No git/jj write of any kind in the lane (no add/commit/stash/checkout); git was used
read-only (`log`, `show`, `status`, `diff`). No lane source, `LOG.md`, `SCORECARD.md`, `MANIFEST.json`,
`templates/`, `scripts/`, `.ufo/state/`, `.scratch/`, `considerthese/` or counter file was modified.

Scratch: `/fast/scratch/hyaku/kotoba-r76/B17LessonScribe` (clone + fixture) created and **removed**;
`test -e` on it returns 1 (absent). All its numbers are transcribed above, not cited to the dead path.

Installs: **none** (no tool, package or binary installed: `python3`, `git`, `curl`, `sha256sum`, `awk`,
`jq` already present). Nothing was run under `pacman`.

## 5. Out of scope / not done

Not applied the lesson, not written any C1/C2 artifact, not edited `round-75.md`/`QUALITY.md`/`SOURCES.md`/
`LOG.md`/`SCORECARD.md`/`SKILL.md`/counters/floors/receipts, not run the ordered no-harm battery, not
re-run siblings' checks to decorate this report, not committed or pushed anything.

## 6. Revisions after peer review (drafts changed while this seat ran)

- **B15Simplifier (O2)** measured the entry against the *revised* `build/entry-draft.md`: 5 rule rows, no
  `## The admitted rules` heading, worked example read at `:184`–`:188` (not `:179`–`:190`). My Gate's entry
  sentence was stale on all three counts; it now says five quotes in the opening rule table, the four
  principles at `:25`–`:28` plus the unnamed-context rule, the `:184`–`:188` reading, and the entry's Q62
  section. **Freshness note (F-8):** a lesson drafted against a sibling artifact that is still being revised
  goes stale silently; the Gate should be re-read against the entry as landed, not as first seen.
- **B15Simplifier (O2, second half) / Q11.** The claims preamble was a fourth copy of the plan, LOG and
  SCORECARD text; it is now 10 lines naming the two claims, the two counters, the freeze, and pointers to
  `plans/round-76.md` § Base battery, `LOG.md` § Round 76 and the SCORECARD annotation. The wave mix now
  appears once, in M76-6, where it is evidence.
- **B15Simplifier (minor).** M76-6 now names its taxonomy in the sentence that prints the number, and states
  the alternatives that make the row checkable: the plan's own attack list with the `attack-simplifier` seats
  gives 25/64 = 39.1%, and the dispatch's A/B seat-name prefixes split 36/28 — neither is the plan's 34/53%.
- **B08LessonDrafts (IRC, two messages).** Adopted: Q74's third clause verbatim ("clip 1,022 / stripped
  1,021, the convention named beside the number"), the addendum rev `7eed80e9` for the convention, the 392
  window sum with B21's 372 named as a mis-sum, and B21's class slug `layout-window-counted-as-value` for
  M76-1. Declined: B08's 5-column Mistakes shape (this lesson follows round-75's 4-column
  `class | evidence pointer | captured-by | fix`, per the seat spec).
- **L1 addendum (`7eed80e9`).** C1 (a)'s anchor-digest clause is recorded as withdrawn and the digest's four
  homes are stated; the render-length convention is cited wherever the number appears.
- **B15Simplifier final result.** O2/O3/O5 confirmed taken against the final bytes; B15's own size headline
  was corrected to a per-disposition figure (+30% against round 74: 13.75 vs 10.6 lines per disposition), so
  this lesson is over precedent per disposition by about a third, not by the raw line count. Its revision of
  `build/skill-patch.md` also moved the patch from +5 to +3 lines (593, not 595); the lesson's Round honesty
  now prints 593 and 7 lines of margin. O4 concerns the R1 correction in `corpus/lessons/round-75.md` (B08's
  artifact), not this lesson, and stays conditional on the absent counter.

## 7. Operator-visible limits of this report

No frozen counter has been executed against the tip (both were absent when this seat wrote). Everything in
§ 2 marked *not run* is unverified rather than passed, and the lesson's R1–R4/D2–D4 dispositions are
drafts-plus-counter-arms, not observed landings (F-7).

VERDICT: lesson draft delivered at `.ufo/waves/round-76/build/lesson-draft.md` (221 lines, sha256
`b5a86a91b193…`) with Gate/Mistakes/Routed defects/Status changes plus a Round honesty section; 6 mistake
rows; R1–R4 and D1–D5 disposed and one forward route opened; S213 used-by old→new recorded verbatim from
B14. Executed by this seat: the render quartet at four revisions, the Gate quote check, the snapshot digest
and manifest check, and the fixture's two registry consequences (evals v2 2 of 10 → 1 of 10 exit 1; census
E11 exit 1). Not executed: both frozen counters (absent at write time) and the tip no-harm battery.
