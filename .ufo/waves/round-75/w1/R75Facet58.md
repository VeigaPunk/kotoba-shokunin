# R75Facet58 — the description-thresholds header sentence: a count and a universal negative no counter reads

Seat `R75Facet58` (leaf, read-only, no delegation, no edits). Measured revision
`65a5c7a663249e0522cc49e4a148424200d9ddfe` (lane `kotoba-shokunin`, `master`; `git status --porcelain`
printed only `?? .ufo/waves/round-75/`, and `git show 65a5c7a6:SKILL.md | sha256sum` =
`sha256sum SKILL.md` = `1b2804fbab784b2c523681259f37d783238f65b2ca21c69b01a5a041bd13155f`, so committed
bytes = working tree for every file cited).

## Axes named

- **Sourced depth** — does the sentence rest on a located source the lane can re-open?
- **Calibration** — does the sentence's quantity and universality clause turn on something that can fail?

## Facet (observed)

`SKILL.md:164-166`, the header paragraph of `### Description thresholds by client`:

```
### Description thresholds by client

A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there, Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis: `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), checked by `verifiers/check_description_thresholds.py`.
```

This is the sentence a description audit reads first: it decides whether a length number is a render
guarantee. It carries four clauses — a count (`four clients state 1,024`), a universal negative (`none
documents a cut there`), a cut/budget pair (`Claude Code and Codex`), and a pointer (`omp cuts at 99`).

## Factual support (observed, true today)

The count and the negative hold against the committed table:

- `SKILL.md:172` VS Code — "`description` maximum 1024 characters"; `:173` Copilot CLI — "`description`
  max 1024 characters"; `:175` Cursor — "1,024 characters for `description`"; `:176` opencode —
  "1-1024 characters" — exactly four rows.
- Those four rows' `Past the threshold` cells all state a documented absence of a cut (`Not documented: …`,
  `Not documented;`, `No cut documented;`, `nothing:`), so "none documents a cut there" is true of the four
  named clients.
- `Claude Code` (`:170`) is "Truncated at the cap, with a startup warning" and `Codex` (`:171`) "shortens
  descriptions first", so "cut or budget the listing" holds.
- The pointer resolves: `SKILL.md:155-156` sends § Router model to
  `corpus/knowledge/anatomy-and-compression.md` § `## Moved from SKILL.md § Router model (round 72)` (`:201`),
  where `:211` still states "hard 99-char cliff" with `_8n=100`.
- Source tier: the four rows are `S055`, `S056`, `S058`, `S059` (`corpus/SOURCES.md:68,69,71,72`), tier `A`,
  kind `docs`, status `mined`, opened `2026-10-22`, `recheck: 90d` — 5 days old at this revision, so the fact
  is fresh against its own cadence. `corpus/knowledge/skill-listing-thresholds-round54.md:15-19` states the
  same count and negative ("Four clients document 1,024 characters … None of their pages documents a cut at
  that number"), and `:60-68` (§ Limits) correctly assigns the non-mechanical judgments to reviewers.

## Control weakness (observed by probe, not inferred)

The sentence names `verifiers/check_description_thresholds.py` as its check, and that counter does not read
it. Its BACKED conjuncts (`verifiers/check_description_thresholds.py:19-53`) cover the SKILL table's cells,
the entry's `## Per-client record` row, the `S###` row, the pinned host, the quote's number token and the
round-54 Gate quote; `judge()` (`:266-333`) reads `table_rows(skill, SKILL_HEADING, SKILL_HEADER)` and never
the paragraph above the table.

Measured by importing the committed instrument and calling its public `judge()` on committed bytes
(scratch `/fast/scratch/hyaku/kotoba-r75/R75Facet58/probe.py`, `SKILL.md` sha256 `1b2804fb…`):

```
base backed: (7, [])
header-'three clients': (7, [])
header-'six clients': (7, [])
negative flipped (says a cut IS documented): (7, [])
one 1024 removed from Copilot row: (6, ['Copilot CLI'])
```

So the counter's backed count stays `7 of 7` — and its printed line `description thresholds backed 7 of 7
clients` exits 0 by `:514` — with the sentence saying four clients, three clients, six clients, or the
negation of its own negative. Only a row's cell changes the count, and even then the exit code does not move:
`TARGET = 4` (`:83`) means `4 of 7`, `5 of 7` and `6 of 7` all exit 0. That insensitivity is already measured
in a committed round-54 wave artefact — `.ufo/waves/round-54/build/CriticC1Sizing.md:61` (`description
thresholds backed 4 of 7 clients  exit 0`), `:114` (`5 of 7 … exit 0`), `:117` (`4 of 7 … exit 0`) — and is
recorded nowhere in `corpus/lessons/round-54.md` (`grep -n '4 of 7\|trivial\|target' corpus/lessons/round-54.md`
printed nothing), so no QUALITY row owns the class.

A second over-acceptance survives in the same frozen token test: `NUM_RE` (`:109`) accepts any digit run, so a
threshold cell with no limit but a version label still backs its row — measured, with the four 1,024 tokens
removed from their cells, opencode stayed BACKED on `v1`/`v2`:

```
four 1024 rows tokenless -> 4 backed; failed: ['VS Code', 'Copilot CLI', 'Cursor']
```

(`.ufo/waves/round-54/build/CriticC1Sizing.md:117` recorded the same class as "world D-trivial-token": the cell
`1 skill` backed opencode.)

Rule exposure: `corpus/QUALITY.md:37` (Q26 — every clause of a statement is turned on by the counter's output or
by a cited guard whose exit code changes), `:42` (Q31 — prose describing a counter names only the cells it
reads), `:24` (Q13 — a count carries its command) and `:25` (Q14 — a negative claim carries its sweep). The
sentence's count has no command, and its Basis line attributes the whole paragraph to a counter that reads
none of it.

## Scope check (observed; the sentence's population is narrower than the lane's census)

The table holds 7 clients (`SKILL.md:170-176`). `SKILL.md:24-25` says "11 clients are mapped by documentation",
and `corpus/lessons/round-74.md:73-75` names the other four with its command: "the seven client tables plus
TRAE, CodeBuddy, Kimi Code, Zhipu". Those four are documented for skill keys in
`corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:24-27`, but that entry states no
`description`-length cap — `grep -c '1024\|1,024' corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`
printed `0`. So today the sentence is true at 11-client scope only by absence of a contrary record, not by a
sweep. `none documents a cut there` most naturally binds to the four clients just named, which is defensible;
it stops being defensible the moment a report reads it as the lane's 11-client population — and the paragraph
never prints its denominator. Note also the numerical coincidence that invites misreading: the counter's target
is 4 (`:83`) and its output `4 of 7` is a *backed* count, a different quantity from "four clients state 1,024"
(a count of 1,024-bearing cells); the same output line is green whether four, five or seven clients are backed.

## Freshness exposure

The four supporting rows carry `recheck: 90d` from `2026-10-22` (`corpus/SOURCES.md:68,69,71,72`), due
2027-01-20, so the *fact* is fresh. The *instrument's* page evidence is not: the counter's `--fetch` mode
(`verifiers/check_description_thresholds.py:50-53,260-265`) fetches live and holds no committed snapshot and
records no HTTP status, which is the form `corpus/QUALITY.md:62` (Q51) refuses as page evidence and `:86` (Q70)
would require to be pinned by snapshot sha256, registry anchor and an HTTP-200 fetch record. The round-54 Gate
(`corpus/lessons/round-54.md:25-29`) records byte sizes and sha256 digests for those pages in prose, which is a
committed record but not a snapshot the counter can hash. A vendor edit to any of the four pages therefore
moves this paragraph silently, and no receipt for the counter at this revision exists: `grep -rl 'description
thresholds backed' .ufo` returns only round-54 wave artefacts and dispatch files, no `receipts/` file.

## Concrete check / control (to build, not run, by the r75 owner)

Extend the *same* frozen counter rather than adding a second method, with two conjuncts read from committed
bytes and one scope conjunct:

- **(g) `header-count`**: the paragraph whose line starts `A documented maximum is not a render cut:` is located
  by that frozen prefix; the number word in it (a pinned word→int table) must equal the number of table rows
  whose threshold cell holds `1024`/`1,024` as a whole token. Missing prefix → exit 2, not 0.
- **(h) `no-documented-cut`**: for each of those rows, the `Past the threshold` cell must match a documented-no-cut
  form (`Not documented|No cut documented|nothing:|no truncation|no cut`) and must not match a documented-cut form
  (`Truncated at|shortened first|refused|dropped|omitted|Truncated at the cap`).
- **(i) `denominator`**: either the sentence names its four rows (or "of the seven documented here"), or the plan
  carries a sweep over the four un-tabled clients with its command (Q14); the four rows are frozen at the plan
  commit (Q28).

Two-sided arms (measured above, so the check is known able to fail in both directions):

| world | expected |
|---|---|
| committed `65a5c7a6` | `4` rows, negative green, exit 0 |
| header word `four`→`three` (equivalently `six`) | (g) red — count 4 ≠ 3 |
| one row's `1024`→`2048` | (g) red — count 3 |
| VS Code past-cell → `Truncated at the cap` | (h) red — one documented cut on a "none" sentence |
| threshold cell text reworded, number intact (`1024 characters (authoring maximum)`) | green — semantics-preserving |
| a fifth 1024 client row added **and** the word updated to `five` | green — the clause tracks the table |
| threshold cell set to `1 skill` / `capped for v1` | red — the redesign must reject the `NUM_RE` over-acceptance measured above |

Command that measures the count today (runs on committed bytes; the exact line I ran):

```
git show 65a5c7a6:SKILL.md | awk -F'|' 'NR>=169 && NR<=176 && $3 ~ /(^|[^0-9])1,?024([^0-9]|$)/ {n++} END{print n+0}'
→ 4
```

## What a described claim may say, and what it may not

- **May** (bounded, if the check lands): "At `65a5c7a6`, four of the seven documented clients state 1,024
  characters for `description`, and none of them documents a cut at it — `<counter>` conjuncts (g)+(h), exit 0."
- **May not**: any r75 description-audit headline that reads this sentence as evidence about render behaviour.
  "A documented maximum is not a render cut" is an inference, and the only render measurement in the sentence
  (`omp cuts at 99`) is a pointer to `anatomy-and-compression.md:211`, whose guard is
  `verifiers/verify_harness_claims.py` — `plans/round-74.md:31` records that script at 17 of 28 checks with 11
  DRIFT, cause attributed to a round-18 catalogue baseline. I did not run it, so whether the 99-cliff check is
  green at this revision is **unmeasured here**; a claim must not inherit it.
- **May not**: "four clients" as the lane's client population; at 11 clients the negative is unswept for TRAE,
  CodeBuddy, Kimi Code and Zhipu.

## Risks of this facet

1. The proposed (g) is a word-parse of English prose: a reword breaks it. Pin the sentence (or its prefix) at the
   plan commit and treat a missing prefix as exit 2 — never as a pass (`corpus/QUALITY.md:62`, Q51; `:86`, Q70).
2. (h)'s token list over-flags on Cursor's cell, which mentions a *warning* containing "1,024" and "cut"
   ("No cut documented; … document a warning"); the direction must be measured on that cell before data, not
   assumed (Q20/Q23: "stricter"/"looser" is a measured direction, never a label).
3. The clause is time-sensitive by construction: a vendor dropping a cap moves both the count and the negative.
   Without a committed snapshot the paragraph is only valid "as documented on 2026-10-22".
4. Landed as conjuncts on a frozen counter, this is a **second** measurement of a round-54 claim; per Q28 it must
   be reported beside the declared one, never in its place.
5. Nothing here measures whether the four pages are the right population, whether "cut or budget" is accurately
   read, or whether the render inference is true — those stay reviewer judgment (Q31).

## Environment and tooling

No installs, no pacman, no git/jj mutation, no live fetch, no model experiments. LSP was not reachable in this
seat (no LSP device exposed); all evidence is literal committed bytes at `65a5c7a6`. Scratch
`/fast/scratch/hyaku/kotoba-r75/R75Facet58/` removed on exit. `git status --porcelain` at the lane showed only
`.ufo/waves/round-75/` at this seat's start and, at its end, `.ufo/waves/round-75/` plus an untracked
`corpus/lessons/round-75.md` (1,664 B, mtime 2026-10-27 12:46) written by another seat during the wave — not
this seat's file, not used as evidence, recorded here for the parent's final sweep (Q40).

Report path: `.ufo/waves/round-75/w1/R75Facet58.md`
