# Blocks — C1 subsection, frame rewrite, routed item 5 row, PROVINCE bullet, gate rows

Seat ScribeSkillSectionR74 (round 74 wave 1). Nothing here is landed; the L1 is the one integration
owner. Every block below is draft text only — no lane file was edited by this seat.

Substitution contract: the three source ids are **placeholders** (`S<a>` best-practices, `S<b>`
using-scripts, `S<c>` quickstart), as the seat instruction directs. The L1 must substitute the ids it
actually appends to `corpus/SOURCES.md` before any measurement: `ExecSrcBestPracticesR74/row.md:1` already
drafts `S223` for best-practices; `ExecSrcScriptsR74/row.md` and `ExecSrcQuickstartR74/row.md` both carry
`S<next>` and both compute the next free lane id as `S223`. So two of the three ids are undecided at the
time of writing; a placeholder left in `SKILL.md` fails C1 predicate (e) by construction
(`S<a>` is not an `S###`).

---

## 1. C1 subsection — insert after `SKILL.md:198`, before the existing blank line `SKILL.md:199`

Insertion point: the current `SKILL.md` lines 190–199 are `## Compression rules` (190), blank (191), five
prose lines (192–197) and the wrapped tail `Trigger-fidelity checklist, line-budget box).` (198), blank
(199). The block goes between 198 and 199; the existing blank at 199 separates it from
`## Trigger-fidelity checklist` (200). **14 lines added, exactly the plan's C1 budget** — measured below.

```markdown

### Body craft — the specification's skill-creation guides
Body craft from the specification's own `skill-creation/` guides, one rule per
row; the entry is `corpus/knowledge/spec-skill-creation-craft-round74.md`.

| rule | source | what a skill author does |
|---|---|---|
| "Match the specificity of your instructions to the fragility of the task" | S<a> best-practices | Be prescriptive where a sequence is fragile; explain *why* where several approaches work |
| "Provide defaults, not menus" | S<a> best-practices | Name one default tool and one escape hatch, never four equal options |
| `SKILL.md` "under 500 lines and 5,000 tokens" | S<a> best-practices | Keep the body to every-run instructions and load the rest from `references/` on a stated trigger |
| `uvx ruff@0.8.0 check .` "reference it directly" | S<b> using-scripts | Call a published package at a pinned version instead of bundling a copy under `scripts/` |
| `--help` "the primary way an agent learns your script's interface" | S<b> using-scripts | Document flags and examples in `--help`; make missing input a named error, not a prompt |
| `.agents/skills/` "VS Code looks for skills in" | S<c> quickstart | Create the folder under `.agents/skills/` in the project; VS Code needs no config |
| "The same skill works in any compatible agent" | S<c> quickstart | Keep the body client-neutral, then load the same folder in a second harness |
```

Line accounting (counted on the block above): blank 1 + heading 1 + lead 2 + blank 1 + header 1 +
separator 1 + rows 7 = **14**. Rows per page 3 / 2 / 2 — clears `≥ 2` for each page. Lead-line widths
78 and 74 characters (the file's prose band is 72–81 in § Compression rules); the table rows are long
single lines like every other table in this file.

Token provenance (each token is a literal substring of the seat snapshot named, `grep -c -F`):

| token | snapshot | hits |
|---|---|---|
| `Match the specificity of your instructions to the fragility of the task` | `ExecSrcBestPracticesR74/bp-md.raw:96` | 1 |
| `Provide defaults, not menus` | `ExecSrcBestPracticesR74/bp-md.raw:127` | 1 |
| `under 500 lines and 5,000 tokens` | `ExecSrcBestPracticesR74/bp-md.raw:90` | 1 |
| `uvx ruff@0.8.0 check .` / `reference it directly` | `ExecSrcScriptsR74/snapshot.md:20` / `:13` | 1 / 1 |
| `--help` / `the primary way an agent learns your script's interface` | `ExecSrcScriptsR74/snapshot.md:254` | 3 / 1 |
| `.agents/skills/` / `VS Code looks for skills in` | `ExecSrcQuickstartR74/snapshot.md:21` | 3 / 1 |
| `The same skill works in any compatible agent` | `ExecSrcQuickstartR74/snapshot.md:17` | 1 |

Page census, this seat's independent reading (the Q45 census seat owns the declared figure): each page
carries at least two usable rule tokens — best-practices has the three above plus `Calibrating control`
(L94) and `Favor procedures over declarations` (L145); using-scripts has the two above plus
`npx eslint@9.0.0` (L90) and `bundle reusable scripts in a` (L9); quickstart has the two above plus
`one file, under 20 lines` (L44) and `Type \`/skills\`` (L55). All three pages clear `≥ 2`, so the
frozen target `N == 3` is reachable on this evidence.

Two constraints the L1 must honour for predicate (e) to count these rows:

1. Every row cites its page's id in the `source` cell — after substitution, no `S<a>`-class placeholder
   may survive.
2. The entry's rule table must carry the same tokens and locate them in the **same snapshots** the
   counter hashes (`snapshots/MANIFEST.sha256`). The seats' snapshot bytes are
   `ab9f3b60…fb41` (best-practices, 15 060 B), `2cd77271…ad1f` (using-scripts, 12 078 B),
   `7c480b44…bffb` (quickstart, 4 080 B) — re-hashed by this seat, see the report.

---

## 2. Frame sentence — `SKILL.md:23-24`, two lines out, two lines in

Observed at base (`sed -n '23,24p' SKILL.md`; the seat said lines 21-23 — the sentence actually starts at
23, line 21 being the `#` title and 22 blank):

```
A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part any router ingests — and the two harnesses here show it differently.
```

Replacement (**exactly 2 lines**, widths 73 and 80; no line-count change, so it spends none of the C1
budget):

```
A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part any router ingests — read live on omp and opencode, documented for 11.
```

The 11 is a command-backed count, not a recollection — distinct client names the lane knows from
documentation (7 per-client rows of this file's own client tables + the 4 Chinese vendors in the
round-73 Core bullet):

```
$ { grep -oE '^\| (Claude Code|Codex|VS Code|Copilot CLI|Gemini CLI|Cursor|opencode) ' SKILL.md; \
    grep -oE 'TRAE|CodeBuddy|Kimi Code|Zhipu' PROVINCE.md; } | sed -E 's/^\| //; s/ $//' | sort -u | wc -l
11
$ … | sort -u
Claude Code / CodeBuddy / Codex / Copilot CLI / Cursor / Gemini CLI / Kimi Code / opencode / TRAE /
VS Code / Zhipu
```

`opencode` is in both sets: it is one of the 11 documented clients **and** one of the two read live, so the
sentence says "documented for 11", never "11 others". `omp` is the one surface the lane reads live and no
page in the corpus documents — the sentence does not claim a page for it.

---

## 3. Routed item 5 — decision row for the cross-vendor `.agents/skills/` root

Shape copied from the nearest existing table, `SKILL.md` § Instruction surfaces, the round-52 MCP
`instructions` table `| guidance that is… | put it in | why (documented) |` (three columns: situation →
placement → documented reason). Placement: after that table's last row, before
`### Agent-definition files by client` (`SKILL.md:78`). **3 table lines + 1 blank = 4 lines**, the plan's
routed-item-5 budget.

```markdown

| decision | what the pages say | what a skill author does |
|---|---|---|
| where a skill meant for TRAE, CodeBuddy, Kimi Code or Zhipu lives | `.agents/skills/` is read by Kimi at both scopes and by TRAE only behind an explicit switch, while CodeBuddy and Zhipu name it nowhere; TRAE's own `.trae/skills/` outranks it on a name collision (S217, S220, S221; `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:26,35-36`) | Write to the vendor's own root; never ship a skill that travels only through `.agents/skills/` |
```

Grounding of each clause in the entry's own lines (not in another seat's summary):

- "read by Kimi at both scopes" — entry `:26` (Kimi row: project roots `.kimi-code/skills/`,
  `.agents/skills/`; user roots `$KIMI_CODE_HOME/skills/`, `~/.agents/skills/`) and `:36` ("Kimi reads it
  at both scopes: `~/.agents/skills/` and `.agents/skills/` (`cn-kimi-zh-skills.md:277-285`)").
- "by TRAE only behind an explicit switch" — entry `:36`, quote `在 导入设置 部分，打开 启用 .agents 技能目录
  开关。` located at `cn-trae-skills.md:389`.
- "CodeBuddy and Zhipu name it nowhere" — entry `:36` ("CodeBuddy's two pages never name it and Zhipu's
  page never does — 0 hits on each").
- "TRAE's own `.trae/skills/` outranks it on a name collision" — entry `:35`, quote
  `若你在 TRAE 内创建的技能（位于 .trae/skills/ 目录）与 .agents/skills/ 中的技能重名，系统将优先调用 .trae/skills/ 目录中的技能。`
  (`cn-trae-skills.md:375`), restated at `:38` as "an imported namespace that its own directory outranks".

The two ids `S217` (TRAE) and `S220`/`S221` (Kimi) are the entry's own committed header rows; the row
cites the entry by path and line, so the pointer survives a registry renumber.

---

## 4a. `PROVINCE.md` § Core — two round-74 bullets, appended after the round-73 bullet

Style borrowed from `PROVINCE.md:28-31` (one bullet per round, title with the round in parentheses, the
entry path, then `counted by <verifier>`). Values are placeholders for the L1's measured figures.

```markdown
- Body craft from the specification's own authoring guides (round 74, C1 depth): what `agentskills.io/skill-creation/` best-practices, using-scripts and quickstart teach about the `SKILL.md` body — calibrating control to task fragility, defaults over menus, the 500-line/5,000-token bound, pinned one-off commands instead of bundled copies, script interfaces written for an agent caller, and the `.agents/skills/` default the tutorial teaches — acted on in `SKILL.md` § Compression rules `### Body craft` and held in `corpus/knowledge/spec-skill-creation-craft-round74.md`, counted by `verifiers/check_spec_craft.py --rev <rev>` (`<<N>>` of 3 pages backed at `<<rev>>`). This is guide advice, not observed client behaviour; tier A scopes each page to its own claims.
- Sibling census re-pinned (round 74, C2 freshness): all 20 § Adjacent lanes re-read at the frozen fleet heads of `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`, each row re-passing the base `check_sibling_census.py` row checks at its pinned commit and carrying a recomputed `git diff --shortstat` delta against the round-49 pin, with `PROVINCE.md` § Adjacent carrying the same commit and classification — `corpus/knowledge/sibling-overlap-census-round74.md`, counted by `verifiers/check_sibling_reread.py --rev <rev>` (`<<N>>` of 20 rows re-pinned and re-read at `<<rev>>`). Rows are valid at their pins, not at the round end; the classification judgement stays with the wave-2 reviewers.
```

Both are written as single lines like every other Core bullet; wrapped in the file they stay inside the
allowed five.

## 4b. `SKILL.md` § Gate registry — two row texts

Shape from the last four rows (`check_author_rules.py`, `check_substrate_repin_v2.py`,
`check_tip_battery.py`, `check_cn_vendor_surfaces.py`): 8 cells, the verdict map carrying the counter's
long form and its printed figure, `--self-test` in the self-test cell, pinned values named explicitly,
write scope named, owner `kotoba`. Registry order: rows are alphabetical by filename apart from appended
round-72/73 rows; alphabetically `check_sibling_reread.py` belongs after `check_sibling_census.py`
(`SKILL.md:467`) and `check_spec_craft.py` after `check_sources_append_only.py` (`:468`). Appending both at
the end beside the round-72/73 rows is the other defensible placement — `check_gate_registry.py` compares
rows with files, so either passes if the row is well-formed; the L1 picks one and says which.

```markdown
| `verifiers/check_spec_craft.py` | gate | `python3 -B verifiers/check_spec_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-74 C1 counter (depth): committed bytes only, no network; each of `best-practices`, `using-scripts` and `quickstart` is backed when (a) `corpus/knowledge/spec-skill-creation-craft-round74.md` has one rule row for the page carrying ≥2 tokens located in its snapshot, (b) the page's `S###` is an 11-cell registry row `mined`/tier A/`agentskills.io`, opened in round 74, `used-by` naming the entry, and the registry is census-conformant, (c) the snapshot's sha256 equals its pin in `snapshots/MANIFEST.sha256`, (d) the row's 5–25-word quote is found after whitespace collapse, (e) `SKILL.md` § Compression rules `### Body craft` has ≥2 rows citing that id, each with a ≥5-word action cell and an in-snapshot token, (f) `PROVINCE.md` § Core names the entry; prints `spec craft pages backed N of 3`; counts form and sources, rule carriage is reviewer judgement | `--self-test` | in-file SELF_SHA; `.ufo/waves/round-74/snapshots/MANIFEST.sha256` | none (reads `git show <rev>:<path>`; `--self-test` writes fixture repos under `$TMPDIR`, removed) | kotoba |
| `verifiers/check_sibling_reread.py` | gate | `python3 -B verifiers/check_sibling_reread.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-74 C2 counter (freshness): each of the 20 § Adjacent lanes is re-pinned and re-read when (a) `corpus/knowledge/sibling-overlap-census-round74.md` has exactly one row for it in the round-49 shape, passing the sha256-pinned base `check_sibling_census.py` row checks at the pinned commit, (b) its commit cell equals the lane's freeze head in `receipts/sibling-heads-freeze.tsv` and that commit is an ancestor of `<rev>`, (c) its `delta` cell equals the recomputed `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`, (d) `PROVINCE.md` § Adjacent carries the same commit and classification, (e) no `none` row exists for a lane whose pinned bytes carry the whole word `kotoba`; prints `sibling rows re-pinned and re-read N of 20`; measures pin, delta, cells, quote location and the mechanical `none` rule — the classification judgement is a reviewer's | `--self-test` | in-file freeze table and base-checker sha256; `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` | none (read-only `git` against sibling repos; self-test fixtures under `$TMPDIR`, removed) | kotoba |
```

Line budget with these blocks: 570 + 14 (C1 subsection) + 2 (registry rows) + 4 (item 5) = 590 of 600,
matching the plan's stated budget; the frame rewrite is net 0.

---

## What this seat did not do

- Did not edit `SKILL.md`, `PROVINCE.md`, `corpus/SOURCES.md`, any verifier, or the staged package.
- Did not assign registry ids: `S<a>/S<b>/S<c>` must be substituted by the L1 after the three rows are
  appended (the ids were still open when this block was written).
- Did not write the C1 or C2 entries, counters or snapshots — those are the ExecSrc*, ExecCounter* and
  ExecControl* seats' deliverables.
- Did not run any gate (the scribe seat runs no measurement it then reports as a pass).
