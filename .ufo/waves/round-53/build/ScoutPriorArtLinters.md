Result: DONE — no surveyed linter or audit implements `alwayson.04` (dated/transient text);
`alwayson.07` has close but non-equivalent prior art (agnix `CC-MEM-018` catches the prose-mention
case only, `XP-006` flags the documented `@AGENTS.md` import, and no tool requires one canonical
rule-file name), so both kotoba checks are extensions, not duplicates, and no external tool can
serve as the counter's instrument under the frozen CLI/exit contract.

# Scout — prior art for the C2 always-on instrument (round 53, build wave)

Seat: `KotobaR53.ScoutPriorArtLinters`. Read-only in the lane; all runs in
`/fast/scratch/hyaku/kotoba-r53/ScoutPriorArtLinters` (clone of the lane at plan commit
`3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`).

## 1. Bottom line for the two boxes

| Box | Closest prior art | Same check? | Verdict |
| --- | --- | --- | --- |
| `alwayson.04` no dated or transient text | `agent-context-lint` `check:stale-dates` (year mentions older than 2 years); Claude `/doctor prompt-audit` ("outdated" content, model-judged) | No | kotoba's criterion (any date / expiry phrasing in a rule file) exists in no tool found. [INFERENCE from documented rule text, not run] `check:stale-dates` would pass all four pinned FAIL cases because 2026 is the current year; it flags *old years*, not *present dates*. |
| `alwayson.07` one canonical rule-file name or explicit redirect | agnix `CC-MEM-018` (prose mention), `XP-006` (two files, no relation note); `@tqakdev/ctxlint` `[duplication]`; JustHandled "competing rule files"; Claude `/doctor` duplicate *local* `CLAUDE.md` | Partly | Only agnix is deterministic and runnable, and its two rules split the box incorrectly: it fires on the documented `@AGENTS.md` import (expected PASS) and stays silent on two independent rule files (expected FAIL). Its findings are `info`, exit 0 even under `--strict`, so the exit contract cannot be met without a wrapper. |

Consequence for the executor: build the instrument lane-native and borrow *semantics* (prose
mention is not an import; symlink and `@AGENTS.md` are redirects), not a dependency. Shelling out
to agnix would import two wrong verdicts plus a host toolchain dependency.

## 2. Sources opened (URL, UTC access, HTTP, bytes, sha256 prefix)

| Id | URL | UTC | HTTP | Bytes | sha256 (16) |
| --- | --- | --- | --- | --- | --- |
| M | https://code.claude.com/docs/en/memory.md | 2026-10-22T20:04:40Z | 200 | 51971 | `971d75bfce7a04c2` |
| S | https://code.claude.com/docs/en/skills.md | 2026-10-22T20:13Z | 200 | 111928 | `d1359f0c64371b3f` |
| C | https://code.claude.com/docs/en/commands.md | 2026-10-22T20:13:21Z | 200 | 54225 | `80164a5bc0d09cd4` |
| L | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2026-10-22T20:15:46Z | 200 | 1070244 | `121129bcb4d33f3b` |
| A | https://raw.githubusercontent.com/agent-sh/agnix/main/README.md | 2026-10-22T20:05:14Z | 200 | 12267 | `7ec5254d90178f98` |
| AR | https://agent-sh.github.io/agnix/docs/rules/ | 2026-10-22T20:05:53Z | 200 (301 → trailing slash) | 314095 | `1d393bb00a4bd39f` |
| A18 | https://agent-sh.github.io/agnix/docs/rules/generated/cc-mem-018 | 2026-10-22T20:06:29Z | 200 | 196649 | `598d675c748e2cef` |
| A14 | https://agent-sh.github.io/agnix/docs/rules/generated/cc-mem-014 | 2026-10-22T20:06:29Z | 200 | 196989 | `47dc23084e056f1f` |
| AL | https://unpkg.com/agentlint-ai@1.1.13/README.md | 2026-10-22T20:05:58Z | 200 | 21164 | `9b856c3700c14eec` |
| AGL | https://unpkg.com/agents-lint@0.7.0/README.md | 2026-10-22T20:10:40Z | 200 | 13941 | `faee22990f8569ba` |
| CX | https://unpkg.com/@ctxlint/ctxlint@1.1.3/README.md | 2026-10-22T20:10:40Z | 200 | 13824 | `ba56ca69c69e8f66` |
| TQ | https://unpkg.com/@tqakdev/ctxlint@0.4.0/README.md | 2026-10-22T20:10:40Z | 200 | 14478 | `fa7812204484f900` |
| ACL | https://raw.githubusercontent.com/mattschaller/agent-context-lint/main/README.md | 2026-10-22T20:17:25Z | 200 | 5007 | `44a5e7d2df6bac91` |
| GAL | https://raw.githubusercontent.com/giacomo/agents-lint/main/README.md | 2026-10-22T20:17:25Z | 200 | 13560 | `548d23c6022e3561` |
| JHL | https://justhandledlabs.com/skills/agents-md-linter/ | 2026-10-22T20:17:25Z | 200 | 11764 | `5485453ac4d24eee` |
| AG | https://agents.md/ | 2026-10-22T20:10:30Z | 200 | 81690 | `06b65de901814135` |
| AGR | https://raw.githubusercontent.com/agentsmd/agents.md/main/README.md | 2026-10-22T20:12Z | 200 | 2015 | `60ec51c226560aaf` |
| — | https://tryctxlint.com/ | 2026-10-22T20:10:30Z | 000 (connect timeout, 136 s) | 0 | — |

`tryctxlint.com` is unreachable from this host; its npm package metadata was read instead
(`@tqakdev/ctxlint` 0.4.0, registry modified 2026-07-09T10:44Z). No claim below rests on the
unreached site.

## 3. Claude Code `/doctor prompt-audit` — what it checks

Docs, in three independent places (line numbers are in the fetched bytes under `/tmp`, hashes in
§2):

- `memory.md:94` — "Claude looks for problems such as instructions written for older models,
  references to files or commands that don't exist, and files that contradict each other".
- `skills.md:92` — "Flag instructions written for older models in your prompts, skills, and tool
  descriptions and propose fixes as a diff". This is the `/claude-api` subcommand table, which
  lists "v2.1.221 or later"; the changelog confirms both dates and they are not in conflict: the
  standalone subcommand was added in `## 2.1.221` (`CHANGELOG.md:4090`, heading at `:4085`:
  "Added a `prompt-audit` subcommand to the `claude-api` skill…"), and the `/doctor` wiring in
  `## 2.1.283` (`CHANGELOG.md:1741`: "audit your CLAUDE.md files, skills, agents and commands for
  prompting patterns written for older models"). `skills.md:49` and `memory.md:98` both say the
  `/doctor` form "requires Claude Code v2.1.283 or later"; host `claude --version` = `2.1.304`,
  so the command is available here.
- Scope: `memory.md:96` — "By default, the audit covers your CLAUDE.md, CLAUDE.local.md, and
  AGENTS.md files". Pass a path to narrow it.
- Current emphasis: `CHANGELOG.md:1792` — "stale paths, stale commands and contradicting
  instruction files now lead the report".
- Mechanism: `memory.md:98` — "The audit runs through the bundled `/claude-api` skill"; findings
  are "a report of findings with proposed edits" (`:94`), applied only on request.

What it does **not** do, per the same three pages: it does not flag embedded dates or expiring
statements (no "date", "dated" or "expire" check appears in `memory.md`, `skills.md`,
`commands.md`; the only "stale" tokens are paths/commands), and it does not require one canonical
rule-file name — the nearest is "files that contradict each other" and the plain `/doctor`
checkup's "local `CLAUDE.md` files that duplicate checked-in ones" (`skills.md:43`), which is a
local-vs-checked-in pair, not `AGENTS.md`-vs-`CLAUDE.md`. It is model-judged, not a
deterministic linter, and `claude doctor` in the terminal is installation diagnostics only
(`claude doctor --help`: "Check the health of your Claude Code installation").

The redirect semantics the counter pins are documented, not linted:
`memory.md:356-358` table — with both files present and no import, Claude reads "Your `CLAUDE.md`
files only"; `:442` prescribes "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it";
`:452` — "If you don't need Claude-specific content, a symlink also works"; `:436` — a prose
sentence is not a redirect: "Claude sees `AGENTS.md` only if it decides to open the file."

Size is the one always-on property Claude documents numerically: `memory.md:88` "target under 200
lines per CLAUDE.md file"; `:619` "Claude Code skips a file over 4 MiB"; `:621` warns at startup
and `/status`; `:623` the `/doctor` checkup "proposes trims for a checked-in CLAUDE.md".

Relation to kotoba: `alwayson.07` is *narrower and stricter* than prompt-audit (binary verdict on
one file-name policy, deterministic, exit-coded); `alwayson.04` has no counterpart.

## 4. agnix 0.59.0 (npm and PyPI; CLI also published on crates.io as `agnix-cli`) — rules that touch the boxes

Install shape: `npx --yes agnix` resolved 0.59.0 from
`/home/vgpnk/.npm/_npx/3e0744517887772d/node_modules/agnix` (npx cache; no global install, no
cargo/pip install performed). PyPI `agnix` is also 0.59.0 (same summary). Claims 702 rules
(`README.md:17`), "sourced from official specs, academic research, and real-world breakage
patterns" (`:42`).

Relevant rules from the reference (`AR`, categories `Claude Memory` and `cross-platform`):

- `CC-MEM-018 AGENTS.md Not Imported` (LOW, claude-code, no autofix; evidence
  `https://code.claude.com/docs/en/memory`). Invalid example: "Read AGENTS.md before making
  changes."; valid example: "@AGENTS.md" (`A18:45`).
- `XP-006 Several Tools' Instruction Files Without a Note` (LOW, best practice, community sources
  incl. the Claude memory page). Bad example: two files with clashing style rules; good example:
  "CLAUDE.md takes precedence over AGENTS.md." (`agnix explain XP-006`).
- `CC-MEM-014 Instruction File Exceeds 200 Lines` (MEDIUM, warning) — invalid example "250 lines
  of instructions" (`A14:45`).
- `CC-MEM-010 README Duplication` (MEDIUM) — content "duplicated verbatim from README.md".
- `CC-MEM-015 Always-Loaded Instructions Exceed Combined Size` (LOW).
- No dated-text rule: the only `stale`/`date` token in a rule name anywhere on the reference page
  is `GM-010 Stale experimental.memoryManager Setting` (a Gemini CLI settings rule), and no rule
  name or description mentions dates, expiry or temporal facts (grep over `AR`; the other
  `dated` hits in the raw HTML are the page's own "Last updated" footer).

Empirical run — the counter's six `alwayson.07` cases plus four dated cases and five additional
probes (`f8`–`f12`), each in its own fixture directory under
`/fast/scratch/hyaku/kotoba-r53/ScoutPriorArtLinters/priorart-fixtures`, run as
`npx --yes agnix --format json <dir>`:

| Fixture (mirrors) | agnix findings | Pinned expectation | Agreement |
| --- | --- | --- | --- |
| `f1-agents-only` (agents-only, PASS) | none | PASS | yes |
| `f2-claude-only` (claude-only, PASS) | none | PASS | yes |
| `f4-import` (`@AGENTS.md` import, PASS) | `XP-006` info | PASS | **no** (false FAIL) |
| `f5-symlink` (`CLAUDE.md -> AGENTS.md`, PASS) | none (only `PE-006` on rule style) | PASS | yes |
| `f3-both-no-import` (two rule files, FAIL) | `XP-006` info only, no `CC-MEM-018` | FAIL | **partial** (info, exit 0) |
| `f6-prose-mention` (prose mention, FAIL) | `CC-MEM-018` info + `XP-006` | FAIL | **partial** (info, exit 0) |
| `f7-dated`, `d1-iso-timestamp`, `d2-month-day`, `d3-dated-claude` (dated FAILs) | none | FAIL | **no** |
| `f8-long` (260-line `AGENTS.md`) | none | n/a (size not a box) | — |
| `f9-long-claude` (264-line `CLAUDE.md`) | `CC-MEM-014` warning | n/a | — |
| `f10-relation-note` ("AGENTS.md is the canonical rule file…") | `XP-006` still fires | n/a | — |
| `f11-precedence` ("CLAUDE.md takes precedence over AGENTS.md.") | `XP-006` cleared | n/a | — |
| `f12-prose-no-agents` (prose mention, no `AGENTS.md` on disk) | none (`CC-MEM-018` needs the second file) | n/a | — |

Exit behaviour: `--strict` did not change the exit code for `f3`/`f6` (both exit 0 with info
diagnostics). JSON shape is `{version, files_checked, diagnostics[{level, rule, file, line, …}],
summary}` — no `checks[]` array keyed by an id, which the frozen counter requires.

Reading: `CC-MEM-018` is a genuine duplicate of one *case* of `alwayson.07` (prose mention) and
`XP-006` covers the two-file *shape*, but `XP-006` treats a prose precedence note as the fix and
flags the import the vendor docs recommend, so adopting agnix's model would invert a pinned case.
Neither rule is a "canonical rule-file name" check.

## 5. Other linters surveyed

| Tool | Checks relevant to the boxes | Relation to kotoba |
| --- | --- | --- |
| `agentlint-ai` 1.1.13 (npm) | 58 checks / "51 deterministic checks on 6 core dimensions" (`AL:25`); F1 entry file exists, F6 "README.md, CLAUDE.md are auto-discovered" (`:124`), I6 "Entry file length" 60–120 lines (`:138`), I7 under 40,000 characters (`:139`), C1 "Document freshness — Stale instructions are worse than no instructions" (`:162`) | Entry-file length and budget only; "freshness" is reference rot, no date detection; no canonical-name rule. Differs. |
| `agents-lint` 0.7.0 (npm) | "Detect stale references and context rot" (`AGL:3`); path refs, npm scripts, Make targets, framework staleness, memory-file schema; "Cross-File Consistency (1 issue)" (`AGL:29`), documented in the project's GitHub README as package-manager conflict / script-role conflict (`GAL:145-148`) | Cross-file *contradiction* only; no dated text, no duplicate-file rule. Differs. |
| `@ctxlint/ctxlint` 1.1.3 (npm) | `stale-file-ref`, `stale-command`, `no-directory-tree`, `redundant-readme` = "Content that duplicates README.md (trigram overlap)" (`CX:174`), `max-lines` = "Files over 200 lines almost always contain bloat" (`:175`), `token-budget` | Size and README duplication; nothing on rule-file naming or dates. Differs. |
| `@tqakdev/ctxlint` 0.4.0 (npm; site unreachable) | `[duplication]` "Same rule maintained twice for different tools" and "Keep one canonical copy (prefer AGENTS.md)" (`TQ:64-66`); `[drift]` divergent copies; `[contradiction]`; `[load-semantics]` file "read by no tool ctxlint knows" (`:78`) | Nearest conceptual match to `alwayson.07`, but the criterion is identical rule *text* across tools, so two independent rule files pass. Differs; not run (site down, docs-only). |
| `agent-context-lint` (npm, GitHub) | `check:stale-dates` — "Year references older than 2 years" (`ACL:41`), configurable `staleDateYears`; `check:contradictions`; `check:token-budget` | Nearest to `alwayson.04` by name only: year-age heuristic, not presence of dates/expiry. Differs. |
| JustHandled Labs "AGENTS.md Linter" | "Duplicate rules, and competing rule files that should be consolidated into one AGENTS.md" (`JHL:40`); read-only; "This is heuristic" (`:44`) | Semantically the closest to `alwayson.07`, but it is a paid prompt-skill (Agensi), no code, no exit contract, and its own page disclaims proof beyond the supplied files. Differs as an instrument; no duplicate claim. |
| `agents.md` spec site + repo README | Nothing about linting, duplicate rule files or dated text; the page's only related statement is "One AGENTS.md works across many agents" (`AG:1`, single minified line; extracted text line 31). The repo README is an example `AGENTS.md`, not spec prose | No prior art; the canonical-name *premise* is stated, not checked. |

## 6. Sibling-lane and fleet scripts (read-only)

- No fleet or sibling script checks rule-file content, within the scope swept: source files
  (`*.py`, `*.sh`, `*.mjs`) under `/home/vgpnk/Projects/shokunin` excluding `.ufo`,
  `node_modules`, `target`, `corpus`, plus a name search for `*agents*`, `*alwayson*`,
  `*rulefile*` at depth 4. Files that mention `AGENTS.md` or `CLAUDE.md` are only:
  `kumitate-shokunin/scripts/cite-check.mjs:176` (lists `AGENTS.md` in a `SELF_DOCS` set of file
  names a citation check tolerates), `kotoba-shokunin/verifiers/check_alwayson_boxes.py` and
  `verifiers/verify_surfaces.py`, plus a comment in `tsukuroi-shokunin/tools/tsukuroi-census.sh:336`
  and one in `kotodama-shokunin/tools/gates/myth-consistency-gate.py:30`. None measures dates,
  size or duplicates. Scripts in other languages or non-source files were not swept.
- The in-lane precedent is manual, not executable: `corpus/knowledge/alwayson-checklist-round7.md`
  drafted the 8 boxes and applied them by hand (6/6 fleet `AGENTS.md` PASS; `~/.agents/AGENTS.md`
  FAIL on AC-1/2/4/5 with dated attestations at `:48`,`:51`). That file is the source of
  `alwayson.04`/`alwayson.07`, so the pre-round-53 state is "checklist prose only".
- Existing machinery a new instrument must also satisfy: `verifiers/verify_skill_checklist.py`
  accepts `delegated:<path>` only when the target is an *instrument* (suffix/shebang/ELF,
  `is_instrument`, line 924) and, when it advertises `--box-proof`, runs that proof
  (`delegated_box_proof`, line 985). npm CLIs (agnix and peers) are not repo files, carry no
  shebang and advertise no `--box-proof`, so they can never be the delegated target — the
  delegation must point at a repo script regardless of prior art.

## 7. Live population (observation, not the claim)

- `/home/vgpnk/Projects/shokunin` (depth 2): 18 `AGENTS.md` (17 lane files + the fleet root),
  **zero** `CLAUDE.md`. Four lane directories have no `AGENTS.md` at all (audio, game-dev-2d,
  lore, revenger) — an absence gap, not `alwayson.07`'s two-file failure.
- The one dual-file repo found under `/home/vgpnk/Projects` is `kimi-code`: `CLAUDE.md` is a
  symlink to `AGENTS.md` (124 lines each) — the sanctioned redirect, so `alwayson.07` would PASS
  it and agnix agrees (returns no duplicate/import diagnostic on the symlink fixture).
- `~/.agents/AGENTS.md` (949 B) opens with "# Operator tooling directive — 2026-10-19" at line 1
  — a live `alwayson.04` FAIL instance; it is not a Claude-discovered path (no `~/AGENTS.md`, no
  `~/.claude/CLAUDE.md`, no `~/CLAUDE.md` on this host).
- Lane `AGENTS.md` is 5 lines / 246 B (fleet template); outliers: `game-dev-3d` 74 lines,
  `kotodama` 40, `souji` 20, `kama` 6 lines but 1730 B.

## 8. Contract fit (why prior art cannot be the instrument)

The frozen counter runs `python3 -B <path> --check <box> --target <case dir> --json` and requires
exit 0 with `{"id": "<box>", "status": "PASS"}` in `checks` for PASS cases and exit 1 with `FAIL`
for FAIL cases (`verifiers/check_alwayson_boxes.py:28-42`). Observed against that:

- agnix has no `--check <box>` at all, and its `-t/--target` means *tool selector*
  (`generic|claude-code|cursor|codex|kiro`), not the case directory; it emits `diagnostics[]`,
  not `checks[]`; its `CC-MEM-018` and `XP-006` are `info` and never change the exit code, even
  with `--strict` (measured above).
- Even wrapped, agnix alone would score 1 of 6 wrong on `alwayson.07` (import case) and 4 of 4
  wrong on `alwayson.04` (no dated rule).
- `agent-context-lint`'s stale-date heuristic would pass all four pinned dated FAIL cases
  (2026 is not older than two years) — [INFERENCE from the documented rule text; not run].

So the executor's instrument must implement `alwayson.04` from scratch and re-implement
`alwayson.07` with the vendor-documented redirect semantics; prior art contributes rule vocabulary
(`AGENTS.md Not Imported`), not logic.

## 9. Gaps and what was not done

Negative-claim sweeps (Q30 shape) behind the "documents nothing" statements above:

- Claude Code has no dated-text check in its instruction tooling: `CHANGELOG.md` grepped for
  `dated|expir` (hits are prompt-cache/credential/auth fixes only; no release note adds a
  date check), the three docs pages `memory.md`, `skills.md`, `commands.md` read at the cited
  lines, and the lane corpus grepped (`prompt-audit` appears only as the unrelated
  `dispatch-prompt-audit-round7.md` artefact name).
- `agents.md` documents no linter and no duplicate-rule-file guidance: the repo has no changelog
  (`CHANGELOG.md`, `changelog.md`, `RELEASES.md` all 404 on `main`), the site has no changelog
  link, the spec page and the repo README were both fetched, and the corpus grep is empty.
- agnix has no dated-text rule at version 0.59.0: the full rule reference for that version was
  read (all categories), not sampled; npm README read; corpus grep empty. Its GitHub release
  notes were not separately swept, so a rule newer than 0.59.0 would not be visible here.

Other limits:

- `tryctxlint.com` unreachable (HTTP 000); `@tqakdev/ctxlint` was assessed from its npm README
  only, not executed (it is a 3-version package whose docs advertise cross-tool duplication).
- `agent-context-lint` and `agents-lint` were not executed (docs-only); their date rules are
  documented as year-age heuristics, so a run would not change the verdict.
- `/doctor prompt-audit` was not executed: it is a model call inside Claude Code, which the seat
  bounds forbid. Its checks are taken from three docs pages plus the changelog, not from behaviour.
- The audit's bundled instruction file (`shared/prompt-audit.md`) ships compressed inside the
  Claude binary; not decompressed (out of scope for a docs-grounded answer).
- No SOURCES row exists yet for `code.claude.com/docs/en/memory` (`grep` over
  `corpus/SOURCES.md` returns none); the provenance in §2 is ready for a wave-1 seat to write one.
- Corpus sweep for the same tools: `grep -rn -i "agnix|agentlint|ctxlint"` over `corpus/`,
  `verifiers/`, `SKILL.md` returns nothing, and no corpus file mentions `/doctor prompt-audit`
  (only unrelated `dispatch-prompt-audit-round7.md`). kotoba has never surveyed these tools.

## 10. Tooling record

- `npx --yes agnix` 0.59.0, npm/npx channel, resolved into
  `/home/vgpnk/.npm/_npx/3e0744517887772d/` — reason: run its rules read-only against 15
  fixtures to test the two boxes empirically. No global install, no pacman transaction, no
  upgrade. No model calls.

## 11. Commands (exit codes observed)

- `python3 -B verifiers/check_alwayson_boxes.py --rev 3bb0a7a3…` in the sandbox clone →
  `always-on boxes executed and discriminating 0 of 8` / `alwayson.04: not counted (disposition
  unexecuted)` / `alwayson.07: not counted (disposition unexecuted)`, exit 1.
- `npx --yes agnix --version` → `agnix 0.59.0`, exit 0.
- `for c in <15 fixtures>; npx --yes agnix --format json "$c"` → per-fixture findings as tabulated
  in §4; `--strict` rerun on `f3`,`f6`,`d1`,`d2`,`d3` → exit 0 each.
- `claude doctor --help` → usage text, exit 0 (no session, no payload).
- `claude --version` → `2.1.304 (Claude Code)`.
