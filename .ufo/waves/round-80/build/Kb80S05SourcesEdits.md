# Kb80S05SourcesEdits — SOURCES.md edit text (round 80, w1)

Scope: `corpus/SOURCES.md` only. Three parts: (1) the S226–S231 `used-by` old→new cells, (2) the
S232+ rows from this round's negative sweep, in exact 11-cell census schema, (3) the `## Search log`
prose note. Plus the old→new log lines the round lesson must carry (SOURCES rule 2).

Base: lane `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Row count before: 157
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 157). Highest id before:
S231. New ids claimed: **S244–S248** (S244–S247 rejected, S248 queued). The negative-sweep seat
`Kb80R01NegSweep` publishes 12 id-free client-keyed records; the census ledger seat
`Kb80S16CensusLog` has already recorded that block as S232–S243, so these five rows are numbered
after it and the two sets do not collide. If the ledger renumbers the 12, shift this block by the
same offset; do not renumber only part of it.

Counter conjunct this edit must satisfy: the C2 counter's (b) conjunct, read from the only copy that
exists at this hour — `.ufo/waves/round-79/build/check_allowed_tools.py`, `registry_problems()`:

```python
listed = [c.strip() for c in row[10].split(",")]
if ENTRY not in listed:
    notes.append(f"{sid}: used-by {row[10].strip()!r} does not list {ENTRY}")
```

with `ENTRY` = `corpus/knowledge/allowed-tools-surfaces-round80.md` in the round-80 bytes. So the
cell is **comma-separated**, and each item is a repo-relative path that must exist on disk (the
census's E11 resolves every comma item of a `mined` row's `used-by`). A `+`-joined cell satisfies
neither. (The published round-80 counter was absent from `.ufo/waves/round-80/build/` when this file
was written — derived from the r79 draft, as the seat spec permits; the `ENTRY` path is the one the
plan and the seat spec name.)

---

## 1. S226–S231 — `used-by` old → new (only cell 11 changes; no other cell)

Old cell (exact, all six rows): `corpus/lessons/round-79.md`
New cell (exact, all six rows): `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md`

| id | line at base | old cell 11 | new cell 11 |
|---|---|---|---|
| S226 | 167 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |
| S227 | 168 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |
| S228 | 169 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |
| S229 | 170 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |
| S230 | 171 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |
| S231 | 172 | `corpus/lessons/round-79.md` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` |

Mechanical form: the six base lines all end in the byte sequence
`| mined | 2026-10-27 | 90d | corpus/lessons/round-79.md |`
(measured: `grep -c "corpus/lessons/round-79.md |$" corpus/SOURCES.md` → 6, on lines 167–172 only).
Replace that 18-character cell with the new cell; nothing else on the line moves. The result of each
line is the base line with its final cell substituted, and no other byte differs.

Preconditions for E11 to clear on these six rows: both `corpus/knowledge/allowed-tools-surfaces-round80.md`
(C2 entry seat) and `corpus/lessons/round-80.md` (lesson seat) must be present in the tree that is
validated. If either is not yet landed, apply part 1 only after it is — a `mined` row naming an
absent path is an E11 finding, not a warning.

## 2. New rows

Insert directly after the S231 row (base line 172), before the blank line that closes `## Registry`.
All five rows are 11 cells; no cell contains `|`; `anchor` cells carry the fetch record; `opened` is
this round's date.

```text rows
| S244 | Cline — Skills — https://docs.cline.bot/customization/skills | docs | C | Whether Cline's skills page documents the allowed-tools frontmatter field | § How Skills Work, progressive-loading table; fetched 2026-10-27, HTTP 200, 228466 B, sha256 ef602792f4d2074678eadcd39f1d506d604dbed4bbee69df05865792e6c57fdc; tag-stripped text 73303 chars with 0 hits of allowed[-_ ]tools; located quote "Metadata Always (at startup) ~100 tokens per skill name and description from YAML frontmatter" | REJECTED: the page's frontmatter contract is name and description only, and neither raw nor tag-stripped bytes carry the field; flip: a page revision naming the field's value syntax or effect | rejected | 2026-10-27 | 90d | corpus/lessons/round-80.md |
| S245 | Windsurf — Cascade Skills — https://docs.windsurf.com/windsurf/cascade/skills | docs | C | Whether Windsurf Cascade's skills page documents the allowed-tools frontmatter field | § Required Frontmatter Fields; fetched 2026-10-27, HTTP 200, 471336 B, sha256 a7e33f3a12363a33fd96e26e6a26e1d1f412dfc1c2a18d2715eb64f22f7cb85b; tag-stripped text 301227 chars with 0 hits of allowed[-_ ]tools; located quote "name : Unique identifier for the skill (displayed in UI and used for @-mentions) description : Brief explanation shown to the model" | REJECTED: the required-frontmatter section names name and description only, and neither raw nor tag-stripped bytes carry the field; flip: a page revision adding the field to the required or optional list | rejected | 2026-10-27 | 90d | corpus/lessons/round-80.md |
| S246 | LangChain — Deep Agents: Skills — https://docs.langchain.com/oss/python/deepagents/skills | docs | C | Whether the Deep Agents skills page documents allowed-tools behavior of its own | § Add tools to skills; fetched 2026-10-27, HTTP 200, 2085218 B, sha256 dfaa7d2bd9a1fabf245bdc9e4b2a61a4ea2bf002a9de497cbae3d945c5ad6b52; located quote "They are unrelated to the spec’s allowed-tools field, which pre-approves tools rather than adding them" | REJECTED: the field appears only in a contrast sentence that disclaims the page's own metadata.include_tools feature, so no allowed-tools behavior is stated; flip: a revision giving the field its own syntax or effect paragraph | rejected | 2026-10-27 | 90d | corpus/lessons/round-80.md |
| S247 | anthropics/claude-code — Issue #18737, docs inconsistency in SKILL.md allowed-tools support — https://github.com/anthropics/claude-code/issues/18737 | community | C | Whether a user-filed docs-inconsistency report grounds allowed-tools semantics | § Current Documentation in the issue body; fetched 2026-10-27, HTTP 200, 327421 B, sha256 7774040f99f84da2b9f26ab7dc0c78973388c84e9e11eabf041a51e2b8c15688; located quote "The allowed-tools frontmatter field in SKILL.md is only supported when using Claude Code CLI directly."; the cited platform.claude.com/docs/en/agent-sdk/skills route served an application shell at fetch (200, 433168 B, sha256 6da45f95307f63ac3eac7fead5ea27af10b0cd46839ed6e76e4143d1aa1f26cb), so the quoted sentence could not be re-verified against page text | REJECTED: a reporter's quotation of a docs sentence, not vendor documentation, and the cited page could not be re-fetched as text this round; it stands as a conflict lead only; flip: a maintainer reply, or page bytes carrying the sentence | rejected | 2026-10-27 | 90d | corpus/lessons/round-80.md |
| S248 | Claude Code — Agent SDK: Agent Skills — https://code.claude.com/docs/en/agent-sdk/skills.md | docs | B | What the Claude Agent SDK page states about the SKILL.md allowed-tools frontmatter field in SDK sessions | § Pre-approve tools for skills (line 348) and the grant note (line 389); fetched 2026-10-27, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2; located quotes "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option" and "The list pre-approves the named tools rather than restricting the others." | The page states that in SDK sessions the frontmatter field pre-approves the listed tools, as does the allowedTools query option, that managed settings can override both, and that the list pre-approves rather than restricts — a documented surface outside the frozen six, held queued | queued | 2026-10-27 | 90d | — |
```

Notes on the rejected rows: each is a page **opened this round** whose bytes and fetch record are in
`Kb80S05-fetches.txt` and copied under this directory as `Kb80S05-<slug>` files. S235's `kind` is
`community` because the source is a user-filed issue, not vendor documentation (community is never
tier A; tier is C here anyway).

## 3. `## Search log` note

Insert as the last bullet of `## Search log`, immediately before the `## Leads (unopened)` heading.

```text searchlog
- **2026-10-27 — round-80 allowed-tools negative sweep (C2 frontier step).** Question: which further
  client or vendor pages that mention, or plausibly cover, the `allowed-tools` skill-frontmatter field
  fail the C2 documentation conjuncts, and which such pages does the registry already carry? Where:
  the six C2 surface pages were re-opened by the round-80 ReopenSix seat; this sweep opened nine
  pages — Cline Skills (`docs.cline.bot/customization/skills`), Windsurf Cascade Skills
  (`docs.windsurf.com/windsurf/cascade/skills`), LangChain Deep Agents Skills
  (`docs.langchain.com/oss/python/deepagents/skills`), the Claude Agent SDK skills page
  (`code.claude.com/docs/en/agent-sdk/skills.md`), anthropics/claude-code issue #18737, the Cursor
  skills route (`cursor.com/docs/context/skills`), the platform.claude.com Agent SDK route, and two
  registry-carried pages re-checked for the field (opencode `opencode.ai/docs/skills.md`, Gemini CLI
  `geminicli.com/docs/cli/skills/`). Identified 9; screened 9; included 1 (S248, queued); rejected 4
  (S244–S247); excluded 2 as already carried by the registry (opencode → S024/S039/S059/S207; Gemini
  CLI → S029); excluded 2 application shells (cursor.com/docs/context/skills, 490061 B, and
  platform.claude.com/docs/en/agent-sdk/skills served as .md, 433168 B: HTML app markup with no page
  text, so no negative claim is made from either). Token sweep per page: `grep -oiE
  'allowed[-_ ]?tools|allowedTools'` over raw bytes and over tag-stripped visible text; both counts
  are 0 for every excluded or rejected page except LangChain (6 raw and 6 text-view, all in the
  contrast paragraph) and issue #18737 (58 raw, 13 text-view, the surplus being page chrome and the
  reporter's quotation recorded in S247). Byte counts and sha256 are in
  `.ufo/waves/round-80/build/Kb80S05-fetches.txt`. Finding kept as a semantics note, not a row: the
  opencode served page states "Unknown frontmatter fields are ignored" — a client statement that no
  grant follows from an unknown field, relevant to the grant-semantics rider. Stop rationale: the
  four rejections and the one queued row exhaust this round's claim; no other opened page carries
  bytes that would change the form claim.
```

## 4. Lesson log lines (SOURCES rule 2 — old→new per row)

For `corpus/lessons/round-80.md` § Gate, appended by the lesson seat; the round-80 frontier step
re-opened all six rows (ReopenSix) and moved `used-by` to the round-80 entry:

```text lessonlog
- S226 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
- S227 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
- S228 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
- S229 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
- S230 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
- S231 used-by: `corpus/lessons/round-79.md` → `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-80.md` (re-opened 2026-10-27)
```

## 5. Validation (run 2026-10-27, receipts in `Kb80S05-validation.txt`)

Applied in a scratch clone at base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`
(`/fast/scratch/hyaku/kotoba-r80/Kb80S05SourcesEdits/clone`), plus two **placeholder** files
(`corpus/knowledge/allowed-tools-surfaces-round80.md`, `corpus/lessons/round-80.md`) that exist only
to satisfy the census's E11 path test and are **not** in the patch.

| check | command | result |
|---|---|---|
| census validate | `scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md` | **exit 0**, `ok`; 24 W04 warnings, all baseline (S018, S227, S229–S231, …), none naming S244–S248 |
| E11 is real | same command with both used-by targets removed | **exit 1**, 12 `E11` lines (two paths × six rows) |
| conjunct (b) red-before | draft counter's `registry_problems()`, `ENTRY=corpus/knowledge/allowed-tools-surfaces-round80.md`, base SOURCES.md | 6 of 6 fail: `used-by 'corpus/lessons/round-79.md' does not list …` |
| conjunct (b) after | same harness, edited SOURCES.md | **0 of 6 fail**, exit 0 |
| rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 157 → **162** |
| 11-cell shape | `awk -F'|' … NF!=13` | **0** malformed rows; each new row NF=13 |
| duplicate ids | frozen census awk | prints nothing |
| enums / tier inflation | frozen census awk | prints nothing |
| mined used-by paths exist | frozen census awk + `[ -e ]` loop | prints nothing (with the placeholders) |

Patch: `Kb80S05SourcesEdits.patch` (one file, `+36 −6`), generated with `--src-prefix=a/
--dst-prefix=b/`, `git apply --check` **exit 0** on a fresh base clone and `git apply` **exit 0**;
the applied result hashes `e9ebf9a374837ab1c88cea0793cf1823aaf750ca42dae9618207cf2daa852a10`
(416 lines). Re-run after the search-log note's count wording was corrected: census **exit 0**,
conjunct (b) **0 of 6**, patch applies clean (see the receipt's last section). Only `corpus/SOURCES.md` is touched; the placeholders and the harness scripts stay in
scratch.

Known limits: (a) the placeholders are stubs, so this validation proves the row arithmetic and the
census/conjunct behaviour, not the content of the C2 entry or the lesson; (b) the published round-80
counter was absent when this file was written, so conjunct (b) was exercised through the r79 draft —
the code path it reads (`row[10].split(",")`) is the same one the plan names; (c) `corpus/SOURCES.md`
carries a base structural defect outside this edit: two column-0 lines that begin
`## Leads (unopened)\`` (base lines 229 and 232, prose that lost its bullet) and a duplicated
`## Leads (unopened)` block (base 260 and 302, with a 2026-10-23 search-log note stranded after the
first one). The new note is inserted before the first *exact* `## Leads (unopened)` heading, i.e.
after all search-log prose; the defect is reported, not repaired (append-only record, outside this
seat's scope).

## 6. Fetch receipts

`Kb80S05-fetches.txt` lists url, curl status+bytes, sha256, raw token hits, tag-stripped token hits.
Raw pages are copied beside it as `Kb80S05-<slug>` (opencode and Gemini pages included because they
were opened this round for the duplicate check).

## 7. Addendum — post-publication checks (2026-10-27, after the census seat measured this patch)

- **The published counter is the r79 draft, byte for byte.** I verified it myself:
  `.ufo/waves/round-80/build/check_allowed_tools.py` and `.ufo/waves/round-79/build/check_allowed_tools.py`
  both hash `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`, and the round-80 copy
  still carries `TARGET = 5` (line 188), `ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"`
  (line 190) and the headline `allowed-tools surfaces backed {n} of {TOTAL}` (line 2268). The round-80
  frozen predicate is `documented N of 6`, exit 0 iff N == 6, ENTRY = the round-80 entry — so the
  published bytes do **not** yet implement C2's frozen claim, and the gap is three edits, not one
  rebind: `TARGET` 5 → 6, `ENTRY` → the round-80 entry, and the printed headline
  `backed` → `documented` (plus its self-test strings). Until those land, the round-80 freeze sha256
  must still read `74e067cc…`, i.e. the counter is not yet frozen as the plan's bytes. My
  conjunct-(b) harness rebound `ENTRY` by hand and therefore says nothing about `TARGET` or the
  headline; the (b) code path itself is the one quoted in § 0.
- **Census-after, reported by `Kb80E12Census` (not re-run by me):** census validate exit 0, `ok`,
  174 rows in both the explicit-dir and lane-label forms, 31 W04 (7 new, all "duplicate url across
  scopes", a warning class that does not change exit status), tier A 135 unchanged, B 21 → 22,
  C 1 → 17; statuses mined 149 unchanged, queued 7 → 8, rejected 1 → 17. The same tree with the two
  used-by targets removed gives 12 E11 findings and exit 1, as in § 5.
- **Two row texts now exist for the sweep.** The ledger/census seat publishes 12 rows numbered
  S232–S243 (their patch `Kb80E12Census-S232-S243.patch` applies over mine) and these five are
  S244–S248; the ranges do not collide, and the L1 must pick one 12-row text for the final tree.

## 8. C1 `commit_unresolvable` audit (verified on primary bytes, 2026-10-27)

Triggered by the instruments auditor's broadcast (`Kb80V03Instruments`) and corroborated by the
battery runner (`Kb80E10Battery`). I verified every claim myself; receipt
`Kb80S05-c1-blocker-audit.txt`, gate JSONs `Kb80S05-gate-{int,ind}-{base,after}.json`.

- **Locations agree with the auditor.** At 398cbe1 both corpus gates read `commit_unresolvable=2`,
  detail `corpus/SOURCES.md:171` and `:172`, both `7bb48f213ac677f943d5c791199ed3dddf302f00`
  (`commit_total 46`, `commit_quoted_excluded 6`). `451a02ff` and `cfb894a5` appear only in
  `commit_quoted_detail` (`corpus/lessons/round-54-verifier-spotcheck.md:147`, `round-53.md:44`,
  `round-54.md:13`), i.e. quoted context, never unresolvable — as the auditor says, and contrary to
  the plan's § Trigger sentence, which names those two as the unresolvable tokens.
- **The hex's owner is mistral-vibe, not pi-mono.** `api.github.com/repos/mistralai/mistral-vibe/commits/7bb48f21…`
  → 200; `api.github.com/repos/badlogic/pi-mono/commits/7bb48f21…` → 422 "No commit found for SHA";
  `…/pi-mono/commits/main` → `85c2ee3e761e…`, `…/mistral-vibe/commits/main` → `7bb48f21…`. The live
  pages still hash to the rows' own pins (pi-mono skills 4793 B = `5b980552…`; mistral-vibe README
  77634 B = `fc48a5db…`). So S231 (mistral-vibe) records the commit correctly and S230 (pi-mono)
  records mistral-vibe's commit against `badlogic/pi-mono`, where it does not exist.
- **Consequence for the grammar repair (reported, not adjudicated).** A line-scope "explicit
  third-repository citation" class would turn both lines green while S230 still asserts a false
  attribution: it classifies a row-content defect as if it were a resolution-set fact. The auditor's
  "do not rewrite the rows (M45)" instruction and this finding point in opposite directions; the L1
  must choose between a correction row for S230 and a grammar class, or both.
- **This seat's patch is neutral on that accounting.** With `Kb80S05SourcesEdits.patch` applied, both
  gates still read `commit_total 46`, `commit_unresolvable 2`, same two detail lines — my rows' 64-hex
  strings are sha256 pins, not commit citations, and my edit neither adds nor clears a token. Anchor
  cells were not touched (used-by only).

### 8a. Erratum text (the anchor cell is not edited this round; the lesson carries it)

For `corpus/lessons/round-80.md`, append-only:

```text erratum
- S230 anchor erratum (round-80): the row says pi-mono `main` "resolved to `badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00`", but the row's own fetch record `.ufo/waves/round-79/snapshots/S230.fetch.json` (fetched 2026-10-27T21:41:14Z) records main at fetch as `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` (path blob sha1 `19d2bf28910ce49caaaf4dde86d1e96330ca7b31`). `7bb48f21…` is mistral-vibe's commit and is recorded correctly by `S231.fetch.json` (2026-10-27T21:41:26Z). Measured again this round: api.github.com answers 422 "No commit found for SHA" for `badlogic/pi-mono/commits/7bb48f21…` and 200 for `mistralai/mistral-vibe/commits/7bb48f21…`; pi-mono's main head today is `85c2ee3e761e…`, so the cited hash is neither the fetch-time head nor the current head of pi-mono. The row's page bytes are right (4793 B, sha256 `5b980552…`, unchanged today); only the commit citation is wrong.
```

### 8b. The msaf Q70 conflict (measured, counter seat's)

I reproduced the entry seat's finding on the counter's own bytes rather than relaying it:
`text_view("S229-msaf.html", …)` yields 1550 lines with exactly one `allowed-tools` occurrence (index 95),
and the first `#`-prefixed line is index 168 — `# Auto-approve load_skill and read_skill_resource, but
not run_skill_script.`, a Python comment in a code sample, not a heading. The draft's
`quote_location()` takes `first_head = next(i for i, l in enumerate(lines) if l.startswith("#"))` and
rejects `idx <= first_head + 1` (lines 893-895), so with the single occurrence at 95 no admissible quote
exists. That is a counter heuristic defect on an HTML text view; the fix belongs to the counter seat.
