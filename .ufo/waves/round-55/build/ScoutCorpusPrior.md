# ScoutCorpusPrior — C1 new-ground baseline at f0e5de82 (round 55, build wave)

Result: DONE — baseline inventory complete; `/skill-name`, `$skill-name`, `$skill-creator` and
`activate_skill` occur 0 times in the whole base haystack (new-ground eligible), while `/skills`
and `skill tool` already occur at base, so rows whose matched token is exactly one of those can
never be new ground.

All commands were read-only (`git grep` / `git show` / `git rev-parse` against `f0e5de82` in the
lane checkout; no sandbox execution was needed). The only lane write is this report. No counter was
run, no lane code was executed, nothing was installed or upgraded, no process was left running.

## 0. Haystack and rule (read from the frozen counter, not assumed)

- Counter: `verifiers/check_explicit_invocation.py`. Docstring: NEW GROUND = "its matched token
  occurs 0 times in `SKILL.md` and 0 times in every `corpus/knowledge/*.md` file at BASE
  (`git show BASE:<path>`, fixed-string)", implemented as
  `new_ground()` = `token not in base_skill and all(token not in t for t in base_know)` —
  a case-sensitive substring test over the token matched in the SKILL.md form cell.
- Haystack reader `base_texts()` uses `git_ls(BASE, "corpus/knowledge")`, i.e.
  `git ls-tree --name-only` (non-recursive) with a `.md` filter.
- Verified at base: `git rev-parse f0e5de82^{commit}` → `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`
  (exit 0); `git ls-tree --name-only f0e5de82 corpus/knowledge/ | wc -l` → 42, of which
  `grep -c '\.md$'` → 41 (the single non-md, `sibling-citation-routing-round16.json`, is outside
  the counter's haystack); `git show f0e5de82:SKILL.md | wc -l` → 599.

## 1. Places at base that already state an explicit skill-invocation form

Command (the plan's): `git grep -n -E '\$skill|/skill|@skill|activate_skill|slash command|invoke'
f0e5de82 -- SKILL.md corpus/knowledge/` → exit 0, 128 matching lines. Most are path/URL noise
(`~/.agents/skills/…`, `.claude/skills/…`, `docs/*/skills.md` URLs, `skill-descriptions.db`,
`skills-ref`, a `skills/skill-creator/scripts/` URL path). The lines that state a client's form:

Seven-client rows (client | exact token | path:line | what the line says):

| Claude Code | `/name` | SKILL.md:433 | "description out of Claude's context, `/name` still works" (overlap-levers turn-off row) |
| Claude Code | `/name` | corpus/knowledge/skill-overlap-levers-round51.md:23 | "the user can still run `/name`" (quote of S022, skills.md:393) |
| Claude Code | `/name` | corpus/knowledge/sibling-overlap-census-round49.md:31 | "where each one came from decides which one `/name` runs" (S022, skills.md:198) |
| Cursor | `/skills` | SKILL.md:190 | "the skill still loads and `/skills` shows a yellow warning count" |
| Cursor | `/skills` | corpus/knowledge/skill-listing-thresholds-round54.md:45 | "the release notes place it in the `/skills` warning set" (S058, release-notes.md:122) |
| Gemini CLI | `/skills disable <name>` | SKILL.md:435 | token cell of the disable-command row (S029) |
| Gemini CLI | `/skills disable <name>` | corpus/knowledge/skill-overlap-levers-round51.md:25 | "`/skills disable <name>`: Prevents a specific skill from being used." (S029, skills.md:94) |
| Gemini CLI | `/skills disable <name>` / `/skills disable` | corpus/knowledge/skill-overlap-levers-round51.md:96, :114 | same lever restated |
| Codex | `$skill` | corpus/knowledge/skill-overlap-levers-round51.md:26 | "explicit `$skill` invocation still works." (S021, build-skills.md:218) |
| opencode | `/<name>` | corpus/knowledge/instruction-surface-census-round13.md:475 | "Opt-in: user invokes `/<name>`" — `opencode/command/*.md` command files (row also names `$ARGUMENTS`) |
| opencode | `skill tool` (prose) | corpus/knowledge/opencode-offer-trace-round8.md:89, :141, :143 | transcript text about opencode's `skill` tool ("Use the skill tool to load a skill …") |

Outside the seven, but their tokens sit in the new-ground haystack and can block a token's
new-ground status for any client:

| omp | `skill://`, `/skill:` | corpus/knowledge/skill-overlap-levers-round51.md:82 | "still reachable by `skill://` and `/skill:`" |
| omp | `skill://<name>`, `skill://X`, `skill:<name>` | corpus/knowledge/skill-activation-telemetry.md:20, :66–70 | prompt template "you MUST read `skill://<name>` before proceeding"; slash counts |
| omp/opencode sessions | `/skill:godspeed`, `/ufo` | corpus/knowledge/trigger-miss-proxy-round6.md:15, :86 | "slash-command tokens stripped … these are invocation verbs" |
| omp | `/wwkd` | corpus/knowledge/frontmatter-trigger-surface.md:7–8, :90; corpus/knowledge/render-mechanism-round7.md:43, :83 | literal invocation strings in wwkd frontmatter / observed triggers |
| opencode | `/init` | corpus/knowledge/instruction-surface-census-round13.md:276, :362; corpus/knowledge/instruction-surface-remeasure-round13.md:23, :28 | `/init` command prompt template (not a skill form) |

- No VS Code- or Copilot CLI-attributed form token appears anywhere in the searched surface: the
  given grep (128 lines, exit 0) and a backticked-sigil sweep
  (`` git grep -n -E '`[/$@#][A-Za-z<]' f0e5de82 -- SKILL.md corpus/knowledge/ ``, exit 0) both
  return none. The sweep's `@` hits are context-file imports (`@AGENTS.md`), npm scopes
  (`@opencode/Instruction`) and dressing (`@commit`); its only `#` hit is a code fragment
  (`#o()`, harness-verifier-round10.md:61).
- Token-less statements worth knowing: SKILL.md:434 (opencode "still loadable by exact name");
  corpus/knowledge/skill-overlap-levers-round51.md:48 (Claude picks by directory — implicit, no token).

## 2. Fixed-string counts for the six candidate tokens

Method: `git grep -o --no-color -F -e <token> f0e5de82 -- SKILL.md corpus/knowledge/`, per-file
counts via `awk -F: '{print $2}' | sort | uniq -c`. Occurrence counts (not line counts),
case-sensitive — the same substring semantics as the counter's `in` test.

| token | at base | per-file counts (occurrences) |
|---|---|---|
| `/skill-name` | ABSENT | 0 in SKILL.md and all 41 knowledge `.md` files (`git grep` exit 1, NO-MATCH) |
| `$skill-name` | ABSENT | 0 everywhere (NO-MATCH) |
| `$skill-creator` | ABSENT | 0 everywhere (NO-MATCH) |
| `/skills` | PRESENT | SKILL.md 22; knowledge: skill-overlap-levers-round51.md 13, opencode-offer-trace-round8.md 12, harness-router-models-round9.md 9, harness-verifier-round10.md 9, frontmatter-trigger-surface.md 8, instruction-surface-census-round13.md 8, skill-selection-rules-round50.md 7, frontmatter-rule-authorities-round48.md 6, render-mechanism-round7.md 6, sibling-description-rewrites-round8.md 4, fail-closed-and-anti-patterns.md 3, skill-activation-telemetry.md 3, agents-md-and-dispatch-surfaces.md 2, anatomy-and-compression.md 2, checklist-execution-round15.md 2, harness-system-prompt.md 1, sibling-overlap-census-round49.md 1, skill-listing-thresholds-round54.md 1; 0 elsewhere |
| `activate_skill` | ABSENT | 0 everywhere (NO-MATCH) |
| `skill tool` | PRESENT | opencode-offer-trace-round8.md 3 (lines 89, 141, 143); 0 elsewhere (case-insensitive: the same 3) |

Verdicts for the L1:

- Never new ground, whatever the row or quote: `/skills`, `skill tool`.
- New-ground eligible (0 occurrences at base): `/skill-name`, `$skill-name`, `$skill-creator`,
  `activate_skill`. Eligibility only — each still needs its client's documented form, a new tier-A
  `mined` SOURCES row on a pinned host, the 3–25-word quote and the live-page fetch.
- `skill tool` also cannot satisfy TOKEN_RE (space; no sigil; no `_`), so a form cell spelled that
  way is not backed at all — opencode's `skill` tool needs a differently shaped token to count.

## 3. Adjacent tokens the L1 may otherwise reach for (all PRESENT at base → not new ground verbatim)

- `$skill`: 2 (skill-overlap-levers-round51.md:26) — Codex's documented form is already at base.
- `/name`: 4 (SKILL.md:433; skill-overlap-levers-round51.md:23; sibling-overlap-census-round49.md:31;
  opencode-offer-trace-round8.md:43, the last inside a `</name>` XML tag) — Claude Code's documented
  form is already at base.
- `/skills disable`: 4 (SKILL.md:435; skill-overlap-levers-round51.md:25, :96, :114).
- `/<name>`: 7 (harness-router-models-round9.md:131; instruction-surface-census-round13.md:475, :498;
  opencode-offer-trace-round8.md:175–177; skill-activation-telemetry.md:20) — a mix of path roots and
  the opencode command row.
- `skill://` 3 (skill-activation-telemetry.md:20, :66; skill-overlap-levers-round51.md:82);
  `/skill:` 2 (skill-overlap-levers-round51.md:82; trigger-miss-proxy-round6.md:15).
- `/wwkd` 6; `/ufo` 47 (31 outside `sibling-citation-routing-round16.json`, 16 inside it);
  `/init` 4.
- `/skill-creator` 1 (frontmatter-rule-authorities-round48.md:126, inside a raw.githubusercontent URL
  path `…/skills/skill-creator/scripts/quick_validate.py`) — note `/skill-creator` ≠ `$skill-creator`.
- `/skill` (the plan's short pattern): 30 in SKILL.md and 118 across 21 knowledge files, so a bare
  `/skill` token is not new ground either.
- `@skill`: 0 everywhere.

## 4. Evidence (commands, exit codes, observed output)

- `git rev-parse f0e5de82^{commit}` → `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c` (exit 0).
- `git show f0e5de82:SKILL.md | wc -l` → `599`.
- `git ls-tree --name-only f0e5de82 corpus/knowledge/ | wc -l` → `42`; same piped through
  `grep -c '\.md$'` → `41`.
- Given grep → exit 0, 128 matching lines; only the §1 rows state a form (rest are paths/URLs).
- Six-token count loop → outputs exactly as tabulated in §2; the four ABSENT rows each printed
  `NO-MATCH` (git grep exit 1) rather than an empty file list.
- Second loop (`$skill`, `skill://`, `/skill:`, `/<name>`, `/skills disable`, `@skill`) →
  `$skill` 2 in skill-overlap-levers-round51.md; `skill://` 2+1; `/skill:` 1+1; `/<name>` 1+2+3+1;
  `/skills disable` 3+1; `@skill` NO-MATCH.
- Third loop (`/skill-creator`, `/name`, `/wwkd`, `/ufo`, `/init`, `/skill`) → counts in §3.
- Sigil sweep `git grep -n --no-color -E '`[/$@#][A-Za-z<]' f0e5de82 -- SKILL.md corpus/knowledge/`
  → exit 0 (this is where SKILL.md:433, the Claude Code `/name` row, surfaced).

## 5. Limits / unknowns

- The predicate itself was not run here (running the counter executes lane code, outside a
  read-only baseline item): no C1 value is claimed.
- Counts are substring counts — a token embedded in a path, URL or XML tag counts (e.g. `/skills`
  inside `.claude/skills`, `/name` inside `</name>`), exactly as the counter's `in` test would.
- The `sibling-citation-routing-round16.json` hits (`$VAR`, `/home/…`, `$OUT_DIR`) are outside the
  counter's `.md` haystack and contribute 0 to all six candidate tokens (verified: it appears in
  none of the six per-file count lists).
- Whether any of the eligible-but-vacant spellings (`/skill-name`, `$skill-name`, `$skill-creator`,
  `activate_skill`) is actually a documented form for a client on its pinned host is not answered
  here; that is this wave's sourcing work, not baseline.