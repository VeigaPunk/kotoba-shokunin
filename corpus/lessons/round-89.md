# Round 89 — kotoba (Linux host, omp 18.15.0): lesson

Author: KotobaR89 (L1). Three scribe seats (ScribeEntry-19, ScribeLesson-50, ScribeSources-26) left no landed
corpus output in the wave directory (`.ufo/waves/round-89/w1/`; ScribeSources left receipts only); the L1 wrote
the knowledge entries, the registry rows, the index rows and this lesson itself. That is a seat-death
disclosure, not a claim that the seats landed work.
Round: 89, plan `plans/round-89.md` (draft `43fc784`), addendum `plans/round-89-addendum-1.md`.
Base: `a5b3b15c00b1de5db321e4226a0a7db17340e605`. Freeze: `FREEZE-REV` (filled by the L1 at the freeze commit).
Tip: `TIP-REV` (filled by the L1 at the landing commit).

## Gate

Candidates considered, with the decision and the reason:

- **S258** — Nosek et al., "The preregistration revolution", PNAS 2018, opened at `pmc.ncbi.nlm.nih.gov/articles/PMC5856500/`
  (the DOI resolved to PMCID PMC5856500 through the NCBI idconv API). **Admitted** as tier A, scoped to the
  preregistration-before-data principle and the confirmatory/exploratory distinction. Access date 2026-11-05;
  sha256 `ee0d0560901a0e65c6b8079e2eaf1d79c049c74597ce3f374b4e19bce0ba51f9` (196,972 B). Located quote, HTML line 1451
  (§Preregistration Distinguishes Prediction and Postdiction, 17 words): "Preregistration of an analysis plan is
  committing to analytic steps without advance knowledge of the research outcomes." Second located quote, HTML line
  1472 (§Challenge 5: Many Experiments, 15 words): "researchers can achieve confirmatory research via replication.
  All initial experiments are treated as exploratory research." Re-opened by the critic seat (CriticFalsify § 4), who
  matched both lines and the sha256 against `.ufo/waves/round-89/w1/ScoutSource/s258.html`.
- **S258 route (a)** — `pmc.ncbi.nlm.nih.gov/articles/PMC5813543/` (the assignment's route). **Rejected** as a
  source: HTTP 200 but a different article (STKR1/SnRK1, 307,298 B, sha256 `20574435…`). Flip: a PMC route that serves
  the paper's own bytes (the PMC5856500 route supersedes it).
- **S258 routes (b) and (c)** — the publisher and the DOI redirect. **Rejected** on HTTP 403 (bot block), no bytes used.
- **S259** — the round-88 spot-check bytes at `a5b3b15c…`, lines 73 and 74 (routed defects 3 and 4). **Admitted**
  as own-work, tier A, scoped to the round-88 requirement record. Verified by the critic seat: line 73 quote is
  20 words by the scout's count and **18 by `wc -w`**; the line-74 quote is 9 words by the scout's count and **8 by
  `wc -w`** (both still ≤25; the scout miscounted — see Mistakes row 2 for the count-without-command class).
- **Considerthese proposal 2** (`considerthese/2026-10-26.md`, move the gate registry out of `SKILL.md`). **Not taken**:
  PROTOCOL.md §Gate standard makes `SKILL.md` the registry home and the L0 question `kotoba | round-73` (line 174) is
  unanswered. Flip: an operator ruling that a pointer registry is conformant.
- **Considerthese proposals 3 and 5** (land the description page round 74 rejected; per-round evidence budget).
  **Not taken**: neither fits the claim cap beside the two routed successors; carried to a later round.
- **Assimilation of `/home/vgpnk/Projects/shokuknow/merge/kotoba/`**. **Rejected** this round: 55 staged ids collide
  with the lane registry (`.ufo/waves/round-89/assimilation/collisions`, re-derived with the 0-3-space guard; open L0
  `kotoba | round-88`). Flip: the operator's renumber-or-retire ruling.

Per-entry gates for the two knowledge entries: `freeze-gate-round89.md` admitted (grounded in S258, S259; inference
labelled); `instance-d5-round89.md` admitted (grounded in S259; bounds stated).

Spot-check result: **pending** — the non-author closure samples one admit and one reject from this gate.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `landing`: a filed round report was rewritten in place (round 88: `5306df4` filed a 199-line report; `d6c5ec57` replaced it with a 104-line report, so the filed bytes changed) | `corpus/lessons/round-88-verifier-spotcheck.md` routed defect 1; `git log --format='%h %s' -- .ufo/reports/round-88/kotoba.md` | none — no criterion or helper refuses a second commit to a filed report path | criterion Q81 appended to `corpus/QUALITY.md` (a filed report is immutable; corrections land as appended errata). Shown able to fail: `grep -c '^| Q81 ' corpus/QUALITY.md` prints 0 at `a5b3b15c` and 1 after this round; the rewrite pattern is caught by the fleet-commit history of `.ufo/reports/round-88/kotoba.md` (two commits, two different blobs) |
| `attribution`: the round-88 lesson's parenthetical named "MERGE-REPORT.md, 188 rows"; 188 is the row count of `SOURCES.append.md` (MERGE-REPORT.md has 155 lines, 113 table lines) | `corpus/lessons/round-88-verifier-spotcheck.md` routed defect 5; `wc -l` of both files in `shokuknow/merge/kotoba/` (read-only) | Q76 (a count names the artifact it counts) — existed, not consulted when the round-88 lesson was written | this lesson names both counts with their files and commands: `wc -l MERGE-REPORT.md` → 155; `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' SOURCES.append.md` → 188. The round-88 wording is not rewritten (append-only); this row is the correction |

Found, not mined as a class of its own: the freeze-gate and D5 instruments were first drafted with an unsatisfiable
or exit-only control (the critic's N6/N7) and a dirty-tree receipt path (N5). Both are recorded as pre-score
amendments in `plans/round-89-addendum-1.md` and the critic's attack file, not as lesson rows.

## Sources

- **S258** — Nosek et al., PNAS 2018; URL `https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/`; access 2026-11-05;
  sha256 `ee0d0560901a0e65c6b8079e2eaf1d79c049c74597ce3f374b4e19bce0ba51f9`; located quotes HTML lines 1451 and 1472
  (above). Tier A scoped. Status `mined`; used-by `corpus/knowledge/freeze-gate-round89.md`.
- **S259** — own-work; locator `git -C …/kotoba-shokunin show a5b3b15c00b1de5db321e4226a0a7db17340e605:corpus/lessons/round-88-verifier-spotcheck.md`;
  sha256 `236aa5172442fc7d5dbb860c59997f339883be82a9647b188f1bb84298215cfd`; lines 73–74. Status `mined`; used-by both
  round-89 knowledge entries.

## Assimilation: none

`/home/vgpnk/Projects/shokuknow/merge/kotoba/` was re-read (read-only). Collisions: reg 183 ids, staged 188 ids,
collisions 55 (`.ufo/waves/round-89/assimilation/collisions`). CORPUS.md rule 2 is append-only, so adoption needs the
renumber-or-retire ruling first (L0 `kotoba | round-88`). No row was appended from the package.

## Considerthese

Read `considerthese/2026-10-26.md` (proposals only; not acted on). One proposal per round may be taken; this round took
none for the reasons in § Gate. The round-88 proposal 4 → Q80 (attack seat required) was applied in this round's wave:
attack seats `ReviewerFreezeGate`, `ReviewerD5Gate`, `CriticFalsify`, `MutTesterGates` — each with output present in
`.ufo/waves/round-89/w1/`.

## Seat record (this round)

- Wave `r89-w1`, 12 seats, validated under policy v1 (band 8–16). WAVE-DONE received; `r89-w1-results.json` carries
  `output: null` for every seat with the note "orchestrator kernel restarted mid-wave"; the seat outputs were read from
  the wave directory instead.
- Landed seat output: ScoutSource (S258/S259 records), ExecFreezeGate (gate + fixtures + floors row), ExecD5Gate (v3 gate),
  ExecCtlWorlds (five controls + equivalence + v2-blindness receipts), ReviewerFreezeGate, ReviewerD5Gate, CriticFalsify,
  MutTesterGates, Connector (`.ufo/waves/round-89/w1/Connector.md`).
- Not landed: ScribeEntry-19, ScribeLesson-50 (no output directory); ScribeSources-26 (receipts only, no rows). The L1
  performed their work and says so here.
