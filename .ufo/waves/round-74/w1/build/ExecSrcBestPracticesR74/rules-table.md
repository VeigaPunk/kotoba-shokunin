# Best practices for skill creators — 13 rules an author acts on

Source: https://agentskills.io/skill-creation/best-practices.md (200, 15 060 B,
sha256 `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41`, fetched
2026-10-25). Line numbers are `snapshot.md` lines (= the fetched `.md` bytes
verbatim; L1-L4 is the site's injected "Documentation Index" blockquote plus a blank
line; the body starts at L5, the `description` blockquote at L7).
Every quote was verified as a literal substring after whitespace collapse only
(`' '.join(q.split()) in ' '.join(snapshot.split())` → 13/13 OK, `tok` counts from
the same snapshot).

Section headings, with levels exactly as the page has them: `## Spending context
wisely` (L48), `### Add what the agent lacks, omit what it knows` (L52), `### Design
coherent units` (L80), `### Aim for moderate detail` (L84), `### Structure large
skills with progressive disclosure` (L88), `## Calibrating control` (L94), `###
Match specificity to fragility` (L98), `### Provide defaults, not menus` (L127), `###
Favor procedures over declarations` (L145), `## Patterns for effective instructions`
(L163), `### Gotchas sections` (L167), `### Templates for output format` (L189),
`### Checklists for multi-step workflows` (L214), `### Validation loops` (L229), `###
Plan-validate-execute` (L247), `### Bundling reusable scripts` (L266).

| # | section (quote line) | quote (literal) | rule tokens | action |
|---|---|---|---|---|
| 1 | § Calibrating control, intro (L96) | "Match the specificity of your instructions to the fragility of the task." | `fragility`, `prescriptiveness` | grade each part's prescriptiveness by how fragile its step is, not by taste |
| 2 | § Structure large skills with progressive disclosure (L90) | "recommends keeping `SKILL.md` under 500 lines and 5,000 tokens" | `SKILL.md`, `references/` | cap the body at 500 lines and 5,000 tokens; move detail into `references/` |
| 3 | § Structure large skills with progressive disclosure (L92) | "Read `references/api-errors.md` if the API returns a non-200 status code" | `references/api-errors.md`, `non-200` | attach each side file to the condition that should load it |
| 4 | § Match specificity to fragility (L111) | "when operations are fragile, consistency matters, or a specific sequence must be followed" | `migrate.py`, `--verify` | write the exact command where the sequence is fragile |
| 5 | § Match specificity to fragility (L122) | "Do not modify the command or add additional flags." | `migrate.py`, `--backup` | state the prohibition next to the pinned command |
| 6 | § Provide defaults, not menus (L129) | "When multiple tools or approaches could work, pick a default and mention alternatives briefly" | `pdfplumber`, `pdf2image` | name one default tool; the alternative is an escape hatch |
| 7 | § Favor procedures over declarations (L147) | "A skill should teach the agent *how to approach* a class of problems" | `references/schema.yaml`, `_id` | write the method steps that generalize, not the one answer |
| 8 | § Add what the agent lacks, omit what it knows (L54) | "Focus on what the agent *wouldn't* know without your skill" | `pdfplumber`, `project-specific` | cut what the agent already knows; keep conventions and edge cases |
| 9 | § Aim for moderate detail (L86) | "Concise, stepwise guidance with a working example tends to outperform exhaustive documentation." | `stepwise`, `exhaustive` | prefer steps plus one working example over an edge-case encyclopedia |
| 10 | § Gotchas sections (L169) | "The highest-value content in many skills is a list of gotchas" | `WHERE deleted_at IS NULL`, `soft deletes` | collect environment facts that defy assumptions as a named gotchas list |
| 11 | § Gotchas sections (L183) | "Keep gotchas in `SKILL.md` where the agent reads them before encountering the situation." | `SKILL.md`, `gotchas` | keep gotchas in the body, not in a reference file |
| 12 | § Validation loops (L231) | "Instruct the agent to validate its own work before moving on." | `validate.py`, `output/` | end a workflow with run-validator, fix, re-run until it passes |
| 13 | § Plan-validate-execute (L249) | "For batch or destructive operations, have the agent create an intermediate plan in a structured format" | `field_values.json`, `validate_fields.py` | for destructive batches write a plan file and validate it against a source of truth |

Rows 4 and 5 are the two halves of one rule (be prescriptive where fragile: the
command, then the prohibition); merge them if exactly 12 rows are wanted (the
assignment asks for 8-12, so a 12-row entry drops row 5 or rows 4+5 into one).

## Dropped bytes, named

- Row 1: the preceding sentence "Not every part of a skill needs the same level of prescriptiveness." (L96) is outside the quote; the quote is the page's own self-contained second sentence.
- Row 2: the link `The [specification](...#progressive-disclosure)` before "recommends" is outside the quote; the quote starts at "recommends" and stops before the em dash that opens the gloss "just the core instructions the agent needs on every run".
- Row 3: the double quotes the page wraps around the example instruction are outside the quote, as is the continuation "is more useful than a generic see references/ for details".
- Row 4: the bold markers around "Be prescriptive" (L111) are outside the quote; the quote begins at "when" and stops before the colon.
- Row 7: the page writes `*how to approach*` with emphasis asterisks — the quote keeps them (they are in the bytes) and stops after "class of problems"; the closing `*` and the clause "not *what to produce* for a specific instance" are outside the quote.
- Row 8: same, `*wouldn't*` keeps its asterisks; the colon-and-list that follows is outside the quote.
- Row 10: the em-dash gloss "environment-specific facts that defy reasonable assumptions" is outside the quote.
- Rows 6, 9, 11, 12, 13: nothing dropped inside the quote; rows 6 and 13 continue after a comma, row 9 ends at its full stop.

## Absent from this page (observed, 0 hits)

- `uvx`, `pipx`, `npx`, `bunx`: 0 occurrences (`grep -cE 'uvx|pipx|npx|bunx' snapshot.md` → 0). The one-off-command and package-runner rules live on `using-scripts` (S236), not here — the entry must not cite this page for them.
- `description` as a body rule: 1 line only (L277, a link to the description guide). This page states the *body* craft; description/trigger rules stay with S213.
