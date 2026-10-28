# Kb80S12AssimDisp — assimilation disposition text (round 80, build output)

> Source of per-row evidence: this seat ran the reads itself. The w1 scout reports
> (`w1/Kb80R06ShokuknowSlice.md`, `w1/Kb80K03Considerthese.md`) were **absent** at read time
> (`.ufo/waves/round-80/w1/` held only `swarm-registry.json`), so every verdict below is derived
> here from the register, the lane bytes and live fetches dated 2026-10-27. Nothing was copied
> from a peer.

## 1. Quarantine — the campaign's absent-defect register, kotoba slice

Derived read-only, per the round prompt §6.10 (data rows only — lane cell, round cell, id cell):

```
A=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/assimilation
R=/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ \
  {print $4, $5}' "$R" > "$A/quarantine-slice"
```

**13 rows** (every line carries an S-id): 7 `payload-absent`, 6 `unreachable`. Every cited source
was re-opened live this round (2026-10-27) before a verdict; the register itself and every
campaign file stayed unread-only, unedited.

| id | class | cited source | fetched 2026-10-27 | verdict |
|---|---|---|---|---|
| S151 | payload-absent | agentskills.io/skill-creation/optimizing-descriptions.md | 200, markdown | **refused as a quotation** — the register's span is lane prose, not page text; the 37–44 / +37.8 figure is on no page this round fetched |
| S167 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | 200, markdown | **refused** — span is a lane note *about* S002 ("The lane holds this page as S002…"), not a source quotation |
| S168 | payload-absent | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | 200, md suffix | **refused** — span `section:` is a heading-fold artifact; the page carries the 56% non-invocation sentence verbatim |
| S172 | payload-absent | junie.jetbrains.com/docs/agent-skills.html | 200, native | **refused as a quotation, fact located** — wording absent; the fact is present in Troubleshooting: "if a project-level and a user-level skills have the same name, the user-level skill will be skipped" (17 words) |
| S176 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | 200, markdown | **refused** — span is lane prose about the three-tier table; the page's own heading is "The core principle: progressive disclosure" |
| S180 | payload-absent | web.archive.org/web/2026/…/coding-agents?hl=ja | 200, ja page | **refused verbatim** — the live heading is "Gemini エージェント スキルをインストールする"; `スキルのインストール` alone is absent |
| S185 | payload-absent | docs.roocode.com/features/skills | 200, redirects roocodeinc.github.io | **refused verbatim** — no `Skill locations` heading remains; the page has "Choose a location" and "Skill Discovery", and S203 already anchors a present heading |
| S169 | unreachable | ai.google.dev/gemini-api/docs/coding-agents | 200, native | **reachable this round** — no quote was ever recorded, so it stays unverifiable *as a quote*; the class ("could not be fetched") no longer holds |
| S236 | unreachable | skills.sh/docs | 200 ("Documentation") | **reachable this round** — same reading as S169 |
| S237 | unreachable | skills.sh/audits | 200 ("Security Audits") | **reachable this round** — same |
| S238 | unreachable | code.claude.com/docs/en/security.md | 200, markdown | **reachable this round** — same |
| S239 | unreachable | skills.sh/agent | 200 ("Agents") | **reachable this round** — same |
| S243 | unreachable | skills.sh/docs/api | 200 ("API Reference") | **reachable this round** — same |

**Verdict count: 13 rows — 0 adopted, 7 refused as quotations, 6 reachable-but-unverifiable (no
recorded quote), 0 entries left `unreachable`.** Adoption stays closed: no row is appendable this
round, and nothing from the register entered any lane file. Flip condition per row: for a
`payload-absent` row, the row may be admitted only after the located anchor is written into the
row in the lane's own words (S172 is the one row whose flip is already evidenced: the fact is on
the page, the quoted wording is not); for an `unreachable` row, the source being fetchable does
not admit it — a quote must first be located and recorded.

### Id-space drift — the slice does not resolve against the lane registry

No row of the slice exists in the lane's registry, and the cited documents mostly do:

```
$ for id in S151 S167 S168 S172 S176 S180 S185 S169 S236 S237 S238 S239 S243; do
    printf '%s ' "$id"; grep -cE "^ {0,3}\|[[:space:]]*${id}[[:space:]]*\|" corpus/SOURCES.md; done
→ 0 for all 13 ids
$ sed -n '13,173p' corpus/SOURCES.md | grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' | wc -l   → 157
→ the registry's ids run S001–S124 (minus S092, S116), then S129, then S198–S231;
   74 ids absent below S232: S092, S116, S125–S128, S130–S197
   (python3 set-difference of S001..S231 against the file's ids)
```

Four of the seven `payload-absent` documents are already held under current ids — S213/S210
(optimizing-descriptions), S002 (adding-skills-support), S206 (junie), S203 (roocode) — and three
(vercel blog, skills.sh×4, code.claude security) are held nowhere (`grep -c 'vercel.com/blog'
corpus/SOURCES.md` → 0; `grep -c 'skills\.sh'` → 0; `grep -c
'code.claude.com/docs/en/security'` → 0). This is the §6.10 mass-id-drift case: the register's
kotoba ids are pre-renumber ids. Adoption therefore has nothing to repair *by id* and keeps
closed; a future round re-anchors **by document**, never by arithmetic.

**Alias hazard, recorded not repaired.** The lane's round-80 negative sweep appends new rejection
rows "ids from S232" (plan § Frontier). The register's stale ids S236–S239 and S243 sit inside
that same number space, so once the sweep lands ≥ 4 new rows, `S236` will name a new rejection row
to anyone reading the register, and the register's quarantined skills.sh row to anyone reading the
lesson. Any later quarantine pass must key on (lane, cited URL), not on the id alone.

### Finding for the frontier owner (not a quarantine row, not repaired here)

The lane's own S206 quotes "the project-level skill takes precedence and the user-level skill is
ignored." (11 words). The Junie page as fetched 2026-10-27 (`meta-built-on:
2026-10-27T08:16:42`) carries instead "…the user-level skill will be skipped." The page was
rebuilt today, so this is page drift after S206's opening date, not fabrication at the time —
but by the frontier step's own re-open rule the S206 quote cell no longer matches its page and
belongs on the round-80 re-open list. Reported; NOT edited (S206 is a corpus row and this seat
writes no lane file outside `build/`).

## 2. `merge/kotoba/` — nothing appended; collision arithmetic re-derived

Read-only package: `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` (188 rows,
ids S203–S390, contiguous, no duplicates). Nothing was staged, transformed or appended.

```
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort > reg-ids     # 157
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' $P/merge/kotoba/SOURCES.append.md | grep -oE 'S[0-9]+' | sort > staged-ids  # 188
$ comm -12 reg-ids staged-ids > collisions
reg_ids=157 staged_ids=188 collisions=29
collisions = S203 S204 S205 S206 S207 S208 S209 S210 S211 S212 S213 S214 S215 S216 S217 S218 S219 S220
             S221 S222 S223 S224 S225 S226 S227 S228 S229 S230 S231
```

29 collisions (S203–S231, exactly the lane's newest 29 registry rows) — the package cannot be
appended without renumbering, and renumbering would have to be by document (the id follows its
URL), which is the r77 S04 disposition unchanged. So: **nothing appended, arithmetic re-derived,
29/29 collisions, same reading as r77.**

Guard proof (the 0–3-space extractor must catch an indented row; a column-zero-only pattern must
not), run on scratch fixtures under `/fast/scratch/hyaku/kotoba-r80/Kb80S12AssimDisp/`:

```
fixture: | id | source |\n| S001 | x |\n  | S210 | indented row colliding with staged |
0-3-space pattern  → fixture_ids = S001 S210 | collisions with staged = 1 (S210)
^\|-only pattern   → fixture_ids = S001      | collisions = 0
```

The 0–3-space pattern catches the indented collision; the column-zero-only pattern false-greens
it. The guard is sound and this lane's first append under §10 must use the 0–3-space form.
Scratch removed after the run (`trap 'rm -rf'`; `scratch_removed=0`).

## 3. `considerthese/` proposals 2–5 (proposal 1 was dispositioned r79)

Source of record: `considerthese/2026-10-26.md` § Self-improvement suggestions (operator-authored,
never edited). None is implemented this round; each line carries the measure the proposal names.

- **P2 — move `## Gate registry` out of `SKILL.md` into `verifiers/REGISTRY.md`.** Measured
  today: the section spans `SKILL.md:445-513`, **24,897 B of a 78,647 B file (31.7 %)** — 11 B
  below the proposal's 24,908 B and still a third of the file; `wc -lc SKILL.md` → 590 lines /
  78,647 B. Open, and it is the payment for P1's byte ceiling.
- **P3 — land the page round 74 rejected, then audit kotoba's own description.** The premise does
  not hold: the rejected staged entry's source is `optimizing-descriptions.md`, which the lane
  already holds as **S213** (and S210 before it) — round 74 refused it for duplicate URL, not for
  unavailability. The audit half measures: the description YAML-parses to **1,021 characters of
  the 1,024 cap (3 chars headroom)**; its first sentence is **151 characters** against the
  ~99-char omp render cliff the proposal names. Open; the page cannot be "landed" again, so the
  proposal should be restated as the audit alone.
- **P4 — do not close a round before its falsify wave runs; mark it `provisional` in
  `SCORECARD.md`.** Measured: `grep -c -i provisional SCORECARD.md` → **2**, at `SCORECARD.md:126`
  (round 51) and `:365` (round 47) — the marker exists nowhere else, and round 74, the round the
  proposal names, closes as admitted with the missing wave recorded in prose only
  (`SCORECARD.md:467`: "Round 74 wave 2 … generated and validated but not dispatched"). Open;
  nothing in the round-80 closure rule changes it.
- **P5 — a per-round evidence budget.** Measured: `.ufo/` = **175,428,954 B of a 244,774,284 B
  working tree (71.7 %)** (`du -sb`), and the 2026-10-23→2026-10-27 window alone is **3,715 files,
  597,617 insertions, 3,089 deletions over 132 commits**
  (`git log --since=2026-10-23 --until=2026-10-27 --numstat`). The proposal's own figures
  (1,587 files / ~275k lines) are a narrower window and are not contradicted — the tree has grown
  since. Operator-owned budget: recorded, not acted on.

Proposals 2–5 stay open; none may be smuggled into a frozen claim (plan § C1/C2 are frozen), and
none is used here as evidence for anything above.

## Findings (for the round-80 lesson `## Gate`)

1. 13/13 quarantined ids do not resolve in the lane registry; the register's kotoba ids are
   pre-renumber. Key quarantine passes on (lane, URL).
2. The register's `payload-absent` spans for S151/S167/S176 are lane prose harvested out of row
   cells by the campaign's quote extractor, not page text — a register-side extraction class, not
   lane fabrication. S168's `section:` is a heading-fold artifact of the same kind.
3. S206's quoted sentence is no longer on its page as of 2026-10-27 (page rebuilt today; the page
   now says "the user-level skill will be skipped").
4. Future id aliasing: new lane rejection rows start at S232 and will collide with the register's
   stale S236–S239/S243.
