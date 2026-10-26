---
seat: R75Facet50
round: 75
lane: kotoba
mode: read-only research (no lane edit, no commit, no spawn, no live fetch, no install)
measured-at: 2026-10-27
measured-rev: 65a5c7a663249e0522cc49e4a148424200d9ddfe
---

# R75Facet50 — `SKILL.md:176`: the opencode description row cites vendor code at two tags, and neither citation is resolvable or checkable from this lane

Seat `R75Facet50` (leaf; read-only; no delegation, no edits, no live fetch, no installs, no git/jj mutation).
`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`;
`git status --porcelain` → only `?? .ufo/waves/round-75/`.
Named axes: **depth** (a claim asserted beyond its committed evidence base) and **calibration**
(what the section's counter can and cannot fail on). Operability is reported as the control's cost, nothing more.

## Facet under audit

`SKILL.md:176`, the **opencode** row of `### Description thresholds by client` (heading `SKILL.md:164`; header
`SKILL.md:168` = `client | documented threshold | past the threshold | action`). Cells 3 and 4, verbatim:

> nothing: no cut, truncation, warning or refusal — both shipped trees print the whole string into
> `<available_skills>` (v1.19.4 `skill/index.ts:332`, v2.1.3 `skill/instructions.ts:21`)

Two of the seven rows rest their "Past the threshold" cell on vendor **code** rather than a documentation page —
the Gemini CLI row (`SKILL.md:174`, held by another seat this wave) and this one. The opencode row is the only
one that pins **two tags of the same artifact** (v1.19.4 and v2.1.3) and names a rendered element
(`<available_skills>`); `SKILL.md:166`/`:168` are cited here only as context, never as my claim.

## What the sentence asserts, clause by clause

| # | clause | kind |
|---|---|---|
| C1 | "both shipped trees print the whole string" — no slice, cut or filter at render | code fact, two tags |
| C2 | "into `<available_skills>`" — the element both renderers emit | code fact, two tags |
| C3 | v1.19.4 `skill/index.ts:332`; v2.1.3 `skill/instructions.ts:21` | citation, resolvability |
| C4 | "nothing: no cut, truncation, warning or refusal" | absence claim (Q14 class) |
| C5 | threshold `1-1024` | docs quote (S059) |

## Observations

**O1 — the bytes the row describes are not in this repo; only digests are.** The round-54 seat recorded both
files with full paths and sha256 in committed wave reports:

- `.ufo/waves/round-54/build/Srcopencode.md:25` — v1.19.4, tag `148842ef7cb1bc34192b3fff57d0f9721ab9c801`,
  `packages/opencode/src/skill/index.ts` (11,843 B, sha256 `91dce57f…`): "`:332` renders
  `    <description>${skill.description}</description>` and `:344` renders `- **${skill.name}**: ${skill.description}` in the compact form".
- `.ufo/waves/round-54/build/Srcopencode.md:26` — v2.1.3, tag `bb25a2f4a3f3f04d7c344bec0c0574ea3510b3b1`:
  "`packages/core/src/skill/instructions.ts:21` renders `    <description>${skill.description}</description>`
  inside `<available_skills>`".
- `.ufo/waves/round-54/build/Srcopencode.md:55` — the fetch table row: URL, `200`, 4,089 B,
  sha256 `ee6b644ca849292f68fdfae7c6ab1d3f02b46e9050757ff4a7cb976199ccc60e`.
- `.ufo/waves/round-54/build/Srcopencode.md:170-172` — the bytes lived at
  `/fast/scratch/hyaku/kotoba-r54/Srcopencode/` (clones `oc-v2.1.3`, `oc-v1.19.4`).

`ls /fast/scratch/hyaku/kotoba-r54/` → `No such file or directory`. No copy of either file is committed:
`git ls-files | grep -E 'instructions\.ts$|[Ss]kill/index\.ts$'` prints nothing, and
`git ls-tree -d 65a5c7a .ufo/waves/round-54/` lists only `build` and `falsify` (no `snapshots/`). So C1–C3 are
re-derivable today only from the seat's own prose.

**O2 — the v1 half is corroborated twice; the v2 half once, by the same seat lineage.** v1: the entry
`corpus/knowledge/skill-listing-thresholds-round54.md:18` ("`:332,344` print it whole") and the falsify seat
`.ufo/waves/round-54/falsify/W2Srcopencode.md:19` ("interpolates it whole in the verbose `<available_skills>`
renderer (`skill/index.ts:39,53-57,332` … `:344`)"). v2: only
`.ufo/waves/round-54/falsify/W2CriticDepth.md:94-95` — "v2.1.3 likewise (`oc-v2-instr.ts:21`)" — with no line
text quoted. The element name for v2 appears in the build seat's prose (`Srcopencode.md:26`), not in a quoted
code line. So C2's v2 half is a **seat reading**, not an observed string in committed bytes.

**O3 — no registry row covers either code citation.** `grep -c 'instructions\.ts' corpus/SOURCES.md` → `0`;
`grep -c 'skill/index\.ts' corpus/SOURCES.md` → `1` (S016, tag **v1.19.3**, not v1.19.4). The two rows the
section's intro cites for opencode (S059 the served v1 page, S064 the V2 page) are documentation, and S059's own
row says "vendor documentation, not a measurement of enforcement" (`corpus/SOURCES.md:72`).

**O4 — the citation path in the row is not resolvable as written, and the same file already carries the
resolvable form.** `SKILL.md:538-540` names the same client as "upstream `github.com/sst/opencode` (dev)" and
writes the full path `packages/opencode/src/skill/index.ts:321-343`; the row writes `skill/index.ts:332`. For v2
the package prefix is `packages/core/src/` (`Srcopencode.md:55`), and the sibling resolution a reader would try
first — `v2.1.3/packages/opencode/src/skill/instructions.ts` — answered **404** at the same tag
(`.ufo/waves/round-54/falsify/W2CriticDepth.md:57`: "A first try at
`v2.1.3/packages/opencode/src/skill/instructions.ts` answered 404 (wrong package; the seat's path is
`packages/core`)"). The two files the one cell cites resolve under **different package roots** at the same tag —
`packages/opencode/src/skill/index.ts` (entry `:18`) and `packages/core/src/skill/instructions.ts`
(`Srcopencode.md:55`) — and the cell names neither. That is exactly the shape `SKILL.md:267-269` bans: "any other
root must be named in the file … bare basenames that exist under multiple roots fail".

**O5 — the executed half of that box never sees these tokens.** `verifiers/verify_skill_checklist.py:1665-1690`
(`check_citation_resolves`) evaluates only subjects produced by `citation_subjects`, i.e. tokens that start with
`CITATION_ROOTS` (this repo's `corpus/`, `verifiers/`, `opencode/`, `.ufo/` prefixes and `../`). `skill/index.ts`
starts with none of them, so the checklist reports N/A-or-clean on the row — reproduced by the checklist's own
message "(a token counts when it starts with …)".

**O6 — the gate that is cited for the section reads none of C1–C3.** `verifiers/check_description_thresholds.py`
docstring `:3-57` lists the conjuncts (table row, number token, entry row, `S###` shape, host, quote, lesson
Gate). In `judge()` (`:266-334`) the row is read as `sr[1]` (threshold cell) and `sr[3]` (action cell) only;
`sr[2]` — the cell under audit — is never indexed. Measured at the tip:

```
python3 -B verifiers/check_description_thresholds.py --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe
  → "description thresholds backed 7 of 7 clients", exit 0
```

Sandbox arms (`/fast/scratch/hyaku/kotoba-r75/R75Facet50/`, four files materialised from
`git show 65a5c7a:<path>`; `--root` was used because `--rev` would need a mutated commit):

| arm | mutation to `SKILL.md:176` | observed |
|---|---|---|
| honest | none | `description thresholds backed 7 of 7 clients` |
| M1 | `skill/instructions.ts:21` → `…:9999` | `7 of 7`, opencode `BACKED` |
| M2 | `skill/instructions.ts` → `skill/no-such-file.ts` | `7 of 7`, opencode `BACKED` |
| M3 | delete `1-1024` from the threshold cell, keep "v1 docs page; the v2 page" | `7 of 7`, opencode `BACKED` |
| M4 | delete every digit from the threshold cell | `opencode     no SKILL.md threshold cell has no number`; `description thresholds backed 6 of 7 clients`; **exit 0** |

**O7 — M3 passes because the number conjunct counts version digits.** `:281` is
`tokens = NUM_RE.findall(sr[1])` with `NUM_RE = r"\d[\d,]*(?:\.\d+)?%?"` (`:109`); `has_token` (`:245-250`) accepts
a token when the next character is not a digit or `%`. Measured directly against the module:

```
tokens = NUM_RE.findall('characters (v1 docs page; the v2 page says it enforces no maximum)')  → ['1', '2']
has_token('`description` must be 1-1024 characters.', ['1', '2'])                              → True
```

so a cell that states no threshold at all still satisfies "the row's threshold cell holds at least one number
token", because `v1`/`v2` are digits and the `1` of `1-1024` matches ahead of the hyphen. The gate's pass
condition is `TARGET = 4` (`:83`; docstring `:57` "Exit 0 iff the counted value is at least TARGET (4)"), so M4's
`6 of 7` is green as well: three of seven rows could go red without the gate moving.

## Assessment against the audit's four criteria

- **Factual support.** C5 holds (S059 quote, `.ufo/waves/round-54/falsify/` re-read it). C1 and C2 hold for
  v1 in committed *reports quoting the code line*. C1/C2 for v2 rest on one seat's prose plus a sha256, with the
  bytes deleted (O1) and no snapshot; by the lane's own evidence pattern (`FETCH-LOG.tsv` + `snapshots/` +
  `MANIFEST.sha256`, `.ufo/waves/round-74/snapshots/`) this row is a step below the r74 standard.
- **Falsifiability.** Of the five clauses, a committed instrument can turn on C5 only (with the M3 caveat) —
  C1–C3 cannot fail any gate today, measured twice (M1, M2). C4 is not turned on by anything either: the section's
  counter never reads the cell (O6), and every occurrence of the absence vocabulary in it is a self-test fixture
  or a git-refusal diagnostic (`grep -n -iE 'truncat|shorten|refus' verifiers/check_description_thresholds.py` →
  14 hits at `:120`, `:348`, `:352`, `:361`, `:391-392`, `:435-456`), none of which reads a skill's rendered output.
- **Scope.** "both shipped trees" names two specific tags; the lane's own pinned host substrate is a third,
  newer one — `verifiers/baseline.json:16` (round 72): "opencode v2.1.4 (`/home/vgpnk/.opencode/bin/opencode`,
  `opencode --version` = opencode v2.1.4, sha256 `ca9b3ee2…`)". The sentence is bounded to its two tags — it says
  nothing about the installed v2.1.4, which this seat did not measure for the cut — and the fetch record itself
  already flagged that "which tag counts as 'current' is not settled by those pages" (`Srcopencode.md:26`).
- **Control weakness.** Three, all measured rather than argued: the cell is unread (O6), the one conjunct that
  would touch a number is satisfiable by version digits (O7), and the gate's target is 4 of 7 (O6/M4). The
  citation box that would catch O4 executes only repo-rooted tokens (O5).

## Adjacent paragraph, reported because it supplies this row's version premise (not my facet object)

`SKILL.md:536-539` states: "opencode — npm `opencode-ai` 1.19.3 since round 47 (the `~/.local/bin/opencode` npx
wrapper; … ; the round-8/18 `~/.opencode/bin` install is gone)". Observed 2026-10-27:

```
readlink -f $(which opencode)                 → /home/vgpnk/.opencode/bin/opencode
opencode --version                            → opencode v2.1.4
stat /home/vgpnk/.local/bin/opencode          → No such file or directory
sha256sum /home/vgpnk/.opencode/bin/opencode  → ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
python3 -B verifiers/check_substrate_pins.py  → PASS opencode_binary_sha256: ca9b3ee2…
```

The pin at `verifiers/baseline.json:10` holds against the live binary, while the shipped § Sources line describes
the opposite install. No gate compares `SKILL.md` prose with `baseline.json`, so a green substrate pin and a false
prose line coexist. Reported here as one line of context; it is not part of this facet's claim and is not
counted in it.

## Concrete check / control (design only — nothing created this round)

Object: every code citation in § Description thresholds by client (cells 2–4). Predicate, per token:

- **(a) root named.** A token matches
  `github.com|raw.githubusercontent.com/<owner>/<repo>@<tag> packages/<pkg>/…/<file>:<line>`, or it is covered by
  a row of a frozen sidecar `verifiers/fixtures/description-code-citations.tsv` with the same five fields.
- **(b) bytes committed.** The sidecar pins bytes, sha256, HTTP status 200 and fetch date; the bytes sit under
  `.ufo/waves/<round>/snapshots/` and their sha256 equals the sidecar and any `corpus/SOURCES.md` anchor.
- **(c) line says what the claim says.** The cited line's text contains the interpolation form the cell asserts
  (`<description>${…}</description>` for C1/C2).
- **(d) number conjunct is exact.** Replace `NUM_RE.findall` on the threshold cell with a whole-cell match of a
  version-free number (`(?<!v)\b\d[\d,]*(?:\.\d+)?%?\b` on a cell with `v\d` stripped), so M3 fails.
- **(e) target equals rows.** Target = 7 (or the honest count) so a drop from 7 to 6 turns the gate red, not 4.

Self-test arms the check must carry: unrooted token → FAIL; line moved by one → FAIL; the 404 sibling package
(`packages/opencode/src/skill/instructions.ts`) → FAIL; snapshot digest ≠ sidecar → FAIL; honest row → PASS.

**Red-before, runnable today, offline (commands as executed):**

1. `grep -c 'instructions\.ts' corpus/SOURCES.md` → `0` (no registry row for the v2 citation).
2. sidecar absent → the new check would read `could-not-evaluate` on the row. A reviewer reading today, by
   inspection of the two tokens, is `root-named 0 of 2`: neither `skill/index.ts:332` nor
   `skill/instructions.ts:21` names a repository or a package root (no tool prints this figure; it is a reading).
3. M1 and M2 above read `7 of 7` on the existing counter — the gap the new check closes.

**Expected post-state:** `2 of 2` once the cell reads, for example,
`anomalyco/opencode@v2.1.3 packages/core/src/skill/instructions.ts:21` with a committed snapshot; `1 of 2` if only
the v1 half is pinned. If only one can be pinned, C3's headline must shrink to that half (Q26) rather than keep
"both shipped trees".

**Bounded headline a later round could claim:** "every code citation in the description-threshold table names its
repo, tag and package path, and its cited line is committed and digest-pinned (K of K)". Not claimable: that the
cell's *reading* of that line is right — that stays reviewer judgment (Q31), as the existing counter already says.

## Limits and risks

- **No live fetch this round.** The 404 and the v2 line text are re-read as committed report prose
  (`.ufo/waves/round-54/`), not re-fetched bytes; both dates are 2026-10-22. Nothing here re-opens the tag.
- **Sandbox mode.** M1–M4 are `--root` runs over four files materialised with `git show`; `main()` feeds the same
  texts to `judge()` for `--rev` (`:479-487`), so the blindness transfers — that transfer is code-read, labelled
  as inference, and was not run on a commit because a mutated commit is a git mutation this seat may not make.
- **Host binary is v2.1.4, not v2.1.3.** The only v2.1.4 observation made here is that the element name survives:
  `grep -a -o -E 'available_skills.{0,240}' /home/vgpnk/.opencode/bin/opencode` →
  `["<available_skills>",...cn(H),"</available_skills>"]`. That is version-labelled and does not stand in for
  the cited tag.
- **Not measured by this seat:** the docs-side absence sweep (C4) and the Cursor/Claude Code rows; an absence
  claim needs its own sweep (Q14) and a target above the reachable population (Q45).
- Scratch used: `/fast/scratch/hyaku/kotoba-r75/R75Facet50/` (four files, one mutated `SKILL.md`); removed after
  the measurement. No tool installed; no lane file written.
