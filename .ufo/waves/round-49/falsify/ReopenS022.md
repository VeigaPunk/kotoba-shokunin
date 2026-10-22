# Falsify seat — ReopenS022 (source row S022, `code.claude.com/docs/en/skills`)

**Verdict: HOLDS-BOUNDED** — S022's fetch bytes, sha256, four line anchors, lesson-Gate quote, census
quotes, negative sweeps, tier and scope cells all reproduce; two bounded wording defects are named
below (teaches cell "description alone"; scope cell misses the listing-budget rule), and neither
overturns the census's "no tie-break for two matching descriptions" nor the 20-row classification.
Judged commit `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`; scratch clone at that commit.

## Findings

### F1 (bounded defect, row teaches cell) — "description alone" is not what the page says
The row's teaches opens: "Claude picks a skill by its `description` alone". The page supports only
the weaker clause after the dash ("the `description` is the field Claude uses to decide whether a
skill applies", `skills.md:389`). Against "alone":
- `skills.md:390` — `when_to_use` | No | "Additional context for when Claude should invoke the
  skill, such as trigger phrases or example requests. Appended to `description` in the skill
  listing and counts toward the 1,536-character cap."
- `skills.md:1207` — "The listing always contains every skill name, but if you have many skills,
  Claude Code drops some descriptions to fit the listing's character budget".
- `skills.md:1213` — low-priority entries can be set to `"name-only"` "so they list without a
  description".
- The row's own second clause contradicts it: a name clash "is settled by origin" (`skills.md:198-202`),
  not by description.
Impact: the dash-clause is verbatim-supported; the absolute "alone" is not, and it is internally
inconsistent with the row. The census inherits only the defensible form ("The description is the
matching input"), so C1's argument does not rest on the bad word.

### F2 (bounded defect, row scope cell) — documented selection rule the sweep cannot see
Scope says the row covers "How Claude Code decides which of several available skills to use".
`skills.md:1207-1213` (§ Skill descriptions are cut short) documents a real selection mechanism:
the budget "scales at 1% of the model's context window" and overflow "drops descriptions starting
with the skills you invoke least, so the skills you use most keep their full text". That decides
which of several skills remain matchable, by invocation frequency rather than by description text.
It is a listing-priority rule, not a tie-break between two matching descriptions — so the census's
negative ("Neither page states a tie-break rule for two descriptions that both match") survives —
but the row's scope cell omits it, and no sweep token (`arbitrat`, `tie-?break`, `ambigu`,
`overlap`) can detect it. Bounded: the census consequence "the only arbitration a skill author
controls is the text of each description" stays defensible because `when_to_use` is also author
text, but `skillOverrides` visibility is a second author control it does not name.

### F3 (premise correction, not a row defect) — tier definitions are not at the top of SOURCES.md
`corpus/SOURCES.md:1-11` holds no tier legend (header prose and the registry table only). The
definitions live at `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-30` (kind enum :24-25; tier-inflation
/ enum census :77-78). Checked there, not at the lane file top.

### F4 (evidence limitation) — "byte-identical to the round-48 fetch" is sha-record corroboration only
The round-48 record `.ufo/waves/round-48/build/C2ClaudeDocs.md:104` holds the same sha
`cdfcb0df9307…114cd456` for the `.md` route, but the round-48 bytes were not retained, so identity
rests on that recorded hash, not on re-hashing prior bytes.

## What holds (each observed this run)

- **Fetch, `.md` route.** `curl -sS -o skills.md … https://code.claude.com/docs/en/skills.md` →
  HTTP 200, 111,557 B, sha256 `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456`,
  at 2026-10-22T11:25:53Z. Row records 200, 111557 B, `cdfcb0df…` → match.
- **Fetch, HTML route.** `…/docs/en/skills` → HTTP 200, 1,233,129 B, sha256
  `102195341251387cee65e8d8f47809878c3c118a12f53fff64bea966a6c42ee2`, `redirect_url` empty. Row
  records 1233129 B, `10219534…`, "did not redirect" → match. The exact 389 sentence appears twice
  in the HTML (body plus duplicate), so "serves the same prose" holds.
- **Anchors.** `365: ### Frontmatter reference` → 389 is the `description` table row; `100: ### Create
  your first skill` → 114 inside it (next heading 123); `196: ### Resolve skills that share a name`
  with 198 the origin paragraph; `1171: ## Troubleshooting` → `1190: ### Skill triggers too often`
  through 1195. All four anchor strings in the row are correct at this revision.
- **Lesson Gate quote** (`corpus/lessons/round-49.md:39`): "What the skill
  does and when to use it. Claude uses this to decide when to apply the skill." — verbatim at
  `skills.md:389`, 19 words (≤25).
- **Census quotes** (`corpus/knowledge/sibling-overlap-census-round49.md`): same 389 sentence, 19
  words, verbatim; and `skills.md:198` "When two skills share a directory or file name, where each
  one came from decides which one `/name` runs." — verbatim including the code ticks, 19 words. Both
  present in the census and in the fetched file modulo markdown line wrap.
- **Negative sweeps on the fetched `.md`** (both `grep -cEi` and `grep -oEi | wc -l`):
  `arbitrat` 0, `tie-?break` 0, `ambigu` 0, `overlap` 0. Matches the row's "→ 0 each" and the
  census's restatement. On the HTML the only `overlap` hits (2) are CSS/markup ("the panels overlap
  again" inside a stylesheet comment), not document prose.
- **Wider arbitration probe** (mine, not in the row): `more than one` 0, `both match` 0, `first
  match` 0, `highest priority` 0, `most specific` 0; `decides which` 2 and `which one runs` 1 are the
  name/session rules at 154, 198, 200. No description-overlap arbitration rule exists in the bytes.
- **Tier and scope cells.** kind `docs` ∈ enum; tier `A` allowed for "official docs" under the
  contract's scoped-A definition (26-29); community-never-A not triggered; status `mined` ∈ enum;
  scope is a claim-scoped topic with the vendor/measurement disclaimer. Conform.
- **Registry shape.** `S022` row `NF=13`, 23 rows, duplicate-id list empty (`awk` + `uniq -d`).
- **C1 guard, private clone at `c48793d`:** `python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → exit 0,
  "rows 20 verified 20", "province rows 20 matched 20"; `PROVINCE.md` § Adjacent lists 20 lanes.
  Guard passes with the S022 row as landed.

## Residual unknowns
- S023's census quotes (`overview.md:59` and the "matches your request against" sentence) were not
  re-opened — out of this row's scope, another seat owns S023.
- The row's `recheck: 90d` was not audited against any rule; the contract fixes no numeric default.

## Tooling
No installs or upgrades. Fetches by `curl` (system), hashing/checks by coreutils `sha256sum`, `wc`,
`grep`, `awk`, `python3 -B`; scratch at `/fast/scratch/hyaku/kotoba-r49/falsify/ReopenS022/`.
