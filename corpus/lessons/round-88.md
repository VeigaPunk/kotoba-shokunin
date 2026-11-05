# Round 88 — kotoba (Linux host, omp 18.15.0): lesson

Author: ScribeLesson (round-88 wave `r88-w1`, scribe seat, kotoba lane).
Round: 88, plan `plans/round-88.md` (frozen at `89579c7`).
Base: `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (C2 red-set reference base).
Tip: `4df1e8005016c75390a5e06b209462df58c95918`.

Claim status (C1, C2, forged worlds, gate controls) is recorded with its receipts in the LOG.md round-88 entry, not restated here.

## Gate

Candidates considered:

- **S257** — omp v18.15.0 `packages/coding-agent/src/discovery/agents.ts`, the project walk-up bound (plan § C1, sourced claim). **Admitted.** URL `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts`; access date `2026-11-05`; sha256 `976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e` (12313 B, 330 lines). Located quote, line 149, 7 words: `if (current === (ctx.repoRoot ?? ctx.home)) break;`. Source: `.ufo/waves/round-88/w1/ScoutUpstream/SOURCE_ROW.md` (the scout's fetch; this seat did not re-fetch the page).
- **Considerthese proposal 4** (`considerthese/2026-10-26.md:18`, "don't close a round before its falsify wave runs"). **Admitted**, mined as criterion Q80 in `corpus/QUALITY.md`.
- **Considerthese proposal 3** (land the description page round 74 rejected, then audit the skill's own description). **Carried, not landed**: no S-row, no `SKILL.md` change this round.
- **Considerthese proposals 2 and 5** (move the gate registry out of `SKILL.md`; per-round evidence budget). **Not taken** this round: no seat item covers them.
- **R87-D7** (LOG.md:3315 reads C2 "verified, `5 of 5`" while the tip reads `4 of 5`). **Admitted** as the round's one Mistakes row.
- **`/home/vgpnk/Projects/shokuknow/merge/kotoba/`** (assimilation). **Rejected**: its id space collides with S256 and no staged theme matches this round's ground (see § Assimilation).
- **Literal sweep `grep -n '5 of 5' LOG.md | grep 'C2'`** for R87-D7. **Rejected as the fix's sweep**: it matches seven LOG.md lines (2481, 2510, 2582, 2715, 2849, 2852, 3315), so it cannot turn green after an append-only annotation. The committed `.ufo/waves/round-88/receipts/mistake-sweep.sh` is used instead; it looks for a later `supersedes LOG.md:<n>` token.
- **Annotating line 3315 in place.** **Rejected**: LOG.md is append-only.
- **Quoting the stale sentence verbatim in the correction entry.** **Rejected** after it was tried: the sweep then counted the quote as a second unannotated stale line (`stale=2 unannotated=1`, exit 1). The quote was reworded to a form the sweep does not match before commit.

Status and used-by changes to existing rows: none. S257 is a new row with status `mined`, opened `2026-11-05`, used-by `corpus/knowledge/omp-root-semantics-round88.md` (written by the ScribeEntry seat; the census check E11 reads that path and is pending until it lands).

Spot-check result: pending — non-author closure

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Stale verdict in a closure line: a record states a counter's tip result as a prior measurement (`verified, 5 of 5`) and no check compares the record with the tip reading | LOG.md:3315 reads `verified, 5 of 5`; tip reads `r86 routed defects closed 4 of 5`, exit 1, in `.ufo/waves/round-88/receipts/before-C2-tip.txt`; the later attempt-2 paragraph at LOG.md:3358 already reads `4 of 5` | none | appended correction entry `### Round 88 — R87-D7 correction` in LOG.md naming `supersedes LOG.md:3315`; sweep `.ufo/waves/round-88/receipts/mistake-sweep.sh` red before (`mistake-sweep-before.txt`: `UNANNOTATED stale line 3315`, `stale=1 unannotated=1`, exit 1) and green after (seat run: `stale=1 unannotated=0`, exit 0; the L1 runs the committed receipt) |
| A frozen discrimination control was written into the freeze and never executed before the freeze commit: C2's `w_added_red` expects FAIL via the name-level monotone test, which cannot see a new instance of an already-red check. The self-test fails (`1 failure(s) over 16 assertions`) only after data. Separately, the C1 counter was repaired after its first scored reading (`0 of 12`, disclosed in `plans/round-88-addendum-3.md` A3.1), which the frozen kill rule forbids. | `plans/round-88.md` § C2 (control list) and § Errata E2; `.ufo/waves/round-88/w1/ExecMonotoneD5.md` F1; `plans/round-88-addendum-3.md` A3.1; `.ufo/waves/round-88/w1/ExecLiveBound/` | none | the freeze must run every control and refuse the freeze on an expectation the predicate cannot satisfy; the first candidate-score timestamp must be recorded and a counter edit after it refused. Not yet shown able to fail: the self-test's red arm `w_added_red` is the only evidence; a freeze gate with a deliberately wrong control is routed to round 89 and is not claimed as a fix this round. |

**L1 disposition (plans/round-88-l1-disposition.md):** C1 killed under the frozen kill rule; C2 not verified; round not admitted. The settlement entry's ruling in LOG.md ("not a candidate score") is not adopted by the L1.

## Considerthese

- **Proposal 4 → Q80.** Appended to `corpus/QUALITY.md`: "a round whose wave has no attack seat (reviewer, critic, mutation-tester) closes provisional, not admitted; the round lesson names the attack seats." Cites this lesson and `considerthese/2026-10-26.md:18`. Round 88's attack seats, by the plan's set: `ReviewerC1`, `ReviewerC2`, `CriticFalsify` (each has output under `.ufo/waves/round-88/w1/` at write time) and `MutTesterV2` (named in the plan; no output directory on disk at write time). Under Q80 the round closes provisional until the L1 settles it.
- **Proposal 3 — carried, not landed** (see § Gate).

## Sources

- **S257** — omp 18.15.0 agent-dirs walk-up module. URL `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/agents.ts` (tag `v18.15.0`; the upstream commit of the tag is recorded in the S257 row, not here; HTTP 200); access date `2026-11-05`; sha256 `976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e`; located quote (line 149): `if (current === (ctx.repoRoot ?? ctx.home)) break;`. Status `mined`; tier A; kind `code`; recheck `on-release`. The row itself is owned by the ScribeSources seat (`corpus/SOURCES.md`).

## Assimilation: none

`/home/vgpnk/Projects/shokuknow/merge/kotoba/` (MERGE-REPORT.md, 188 rows) exists, but its id space collides with S256 and no staged theme matches this round's C1/C2 ground. No adoption starts this round (plan § Frontier).
