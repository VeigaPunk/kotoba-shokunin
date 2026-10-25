# Anatomy & compression

Observed across 16 files, 2026-09-28. Line counts from `wc -l`.

## Observed size distribution

| File | Lines | Shape class |
|------|-------|-------------|
| godspeed | 18 | deferral-only (body = "read directive.md verbatim") |
| xbrd-ask | 68 | lane table + protocol |
| bailian-finetune, bailian-sandbox | 75 | workflow + routing |
| sekhmet-l3 | 94 | env blocks + flag table |
| bailian-model-recommend | 111 | staged procedure |
| bailian-web-search | 120 | routing workflow + fallback classes |
| bailian-cli | 132 | hub routing tables |
| bailian-protocol | 152 | shared consent protocol |
| ufo (opencode) | 161 | invariants + dispatch contract |
| bailian-gen | 121 | intent→command table + examples |
| bailian-managed-agent | 196 | IaC workflow |
| bailian-train-deploy | 200 | longest procedure: 7 numbered steps |
| wwkd | 233 | posture skill: principles + phases + refusals |
| omarchy | 392 | largest; config-location tables + task recipes |

Source: `wc -l ~/.agents/skills/*/SKILL.md ~/.config/opencode/skills/ufo/SKILL.md`.

## Claim — ~600 lines is a split trigger, not a norm

wwkd principle 8 states "~600 lines per module" (`wwkd/SKILL.md` L64–66).
No surveyed file exceeds 392. Interpretation (opinion): the bound fires as a
*split* signal — decision surface stays in SKILL.md, depth moves to
`reference/`/`assets/` — long before 600. bailian-cli keeps flag docs in
`reference/<group>.md` generated from CLI source and instructs "do not guess
flags — use the reference files or `--help`."

## Claim — bodies mostly assume activation succeeded (2 of 16 restate)

Sweep: `grep -n 'When to use\|何时使用\|适用场景' */SKILL.md` over the 16-file
survey set (run 2026-09-28). Most hits are intent→command routing tables
(`When to use which command` in bailian-cli/finetune/gen) — legitimate body
content, not a restated trigger. Two genuine counterexamples:

- `bailian-model-recommend` L16–24 `## 适用场景` lists the same trigger
  phrases its frontmatter 触发词 carries.
- `bailian-docs-llm-wiki` L16–35 `## 何时使用` / `## 何时不要使用` restates
  both activation conditions and anti-triggers in the body.

Refined rule (opinion): trigger content in the body is usually dead weight —
but where a router is imperfect, a body-level restatement acts as a
second-layer correction net. Whether that redundancy pays is unmeasured (no
activation telemetry); treat it as optional hardening, not an error.

## Claim — command blocks carry their own env setup

sekhmet-l3 live-wave block exports `CODEX_BIN` / sources env file before the
command; bailian skills state `bl auth status` as a prerequisite step rather
than embedding auth in every block. Runnable-as-pasted is the bar.

## Claim — depth files keep SKILL.md flat

Pattern: `reference/<group>.md` per command group (bailian-cli hub),
`assets/*.md` for procedures (setup, issue-reporting, video post-processing),
`models/*.jsonl` for data (model-recommend). SKILL.md holds the pointer line
plus the fallback (`bl <cmd> --help`) — never a copy.

## Compression rules — moved from `SKILL.md` (round 15)

The six rules, verbatim as they stood in `SKILL.md` before the round-15
line-budget move (the file was 675 lines at pre-registration commit `63ceba7`;
`SKILL.md` now keeps a five-line summary plus this pointer).

1. **Spend tokens in the description; save tokens in the body.** The description
   is always loaded — density there has the highest leverage. The body loads only
   on activation, but still competes with the task context.
2. **Depth moves to files, not prose.** Hub skills point to `reference/<group>.md`
   and `bl <cmd> --help` instead of duplicating flag docs ("do not guess flags" —
   bailian-cli). One authoritative home per fact; the skill keeps the pointer.
3. **Command blocks verbatim-copyable.** Env setup first, then the command
   (sekhmet-l3 live-wave block). No placeholders that require guessing the shape.
4. **Failure signatures inline.** Pitfalls earn their lines only when they carry
   the observed symptom: zsh `status` readonly-variable trap, 404 deploy
   propagation delay, `--learning-rate` must be string `"3e-4"` not number
   (bailian-train-deploy 反幻觉清单). "Be careful" without a signature is noise.
5. **Never restate the trigger in the body.** The body assumes activation
   succeeded; "when to use this skill" paragraphs in the body are dead weight —
   move them to the description.
6. **~600-line module bound.** wwkd principle 8: fits in one file, one screen,
   single-sitting readable. Largest observed production skill: omarchy at 392
   lines. Past ~600 lines, split: decision surface stays in SKILL.md, depth goes
   to `reference/` / `assets/` with a pointer line. Gods-eye rule: if you can't
   hold the whole file while editing it, the reader can't either (heuristic, not
   measured).

## Moved from SKILL.md § Decision tables (round 57)

Verbatim from `SKILL.md` § Decision tables — when to use one at `01312a77`
lines 203–217 (round 57 line-budget move, 15 lines; the moved block's sha256 is
unchanged by the move, checked before and after — receipt in the round-57
build report).

## Decision tables — when to use one

| Situation | Table? | Evidence |
|-----------|--------|----------|
| Intent → command/route mapping | Yes: `Intent | Command | Notes` | bailian-cli "When to use which command" |
| Request classification with different actions | Yes: `Class | Pattern | Action` | bailian-protocol 4-class consent table |
| Flag → effect reference | Yes: `Flag | Effect` | sekhmet-l3 |
| Ordered pipeline | No — numbered steps or ASCII chain | bailian-finetune 7-step chain |
| One conditional | No — one sentence | — |

Table rule: every row must contain an **action cell** (command, route, named
fallback, or verdict) — it need not be the last column; a trailing
Source/Evidence column is allowed only when an action cell exists earlier in
the row. A table with no action column at all is documentation, not a
decision surface, and must not be presented as one.

## Moved from SKILL.md § Skill-file anatomy (round 58)

Verbatim from `SKILL.md` § Skill-file anatomy at `3de87aad` lines 58–76 (round 58
line-budget move, 19 lines; the moved block's sha256 is unchanged by the move,
checked before and after — receipt in the round-58 build report).

## Skill-file anatomy

Observed load order, top to bottom. A file that inverts this order (procedures
before scope, examples before decision tables) reads worse under activation
pressure.

| # | Section | Function | Exemplar |
|---|---------|----------|----------|
| 0 | Frontmatter | Trigger index; the only always-loaded bytes | all |
| 1 | H1 + role statement | What this skill is, in one line | wwkd L16–24 |
| 2 | Prerequisite gate | Fail-closed dependency check before any action | bailian-cli "CRITICAL — MUST read bailian-protocol" |
| 3 | Decision surface | Tables/protocols that route the request | bailian-protocol class table; sekhmet-l3 flag table |
| 4 | Procedures | Numbered steps, copy-pasteable command blocks | bailian-finetune steps 1–7 |
| 5 | Boundaries | Refusals, anti-triggers, hand-offs | wwkd "Refusals"; bailian-train-deploy 反触发表 |
| 6 | References | Cited sources, relative links to depth files | wwkd "Source Excerpts"; bailian `reference/` links |

Not every file needs every section. godspeed is 18 lines: frontmatter + one
deferral ("Read `directive.md` … apply verbatim") + one invocation note. Anatomy
is a checklist of *available* organs, not a mandatory skeleton.

## Moved from SKILL.md § Sources — production skill files (round 59)

Verbatim from `SKILL.md` § Sources bullets 2–15 at `67b68e0f` lines 482–509
(round 59 line-budget move, 28 lines; the moved block's sha256
`9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8` is unchanged by
the move, checked before and after — receipt in
`.ufo/waves/round-59/build/ExecBudgetMove.md`).

### Production skill files studied

- `~/.agents/skills/wwkd/SKILL.md` — posture-skill anatomy: principles, phased
  protocol, refusals, quoted source excerpts.
- `~/.agents/skills/godspeed/SKILL.md` — minimal always-on skill (18 lines);
  deferral pattern.
- `~/.agents/skills/sekhmet-l3/SKILL.md` — ops-skill anatomy: env blocks, smoke
  gate, flag table.
- `~/.agents/skills/xbrd-ask/SKILL.md` — lane table, advisory protocol, epistemic
  constraints.
- `~/.agents/skills/bailian-protocol/SKILL.md` — consent decision table,
  classification with actions.
- `~/.agents/skills/bailian-cli/SKILL.md` — hub/routing tables, soft hand-offs,
  `metadata.requires.bins`.
- `~/.agents/skills/bailian-train-deploy/SKILL.md` — 反触发表, 反幻觉清单,
  numbered end-to-end procedure, failure signatures.
- `~/.agents/skills/bailian-model-recommend/SKILL.md` — implicit-intent triggers,
  sibling boundary arbitration.
- `~/.agents/skills/bailian-web-search/SKILL.md`, `bailian-gen/SKILL.md`,
  `bailian-finetune/SKILL.md` — routing workflows, consent short-forms.
- `~/.agents/skills/bailian-docs-llm-wiki/SKILL.md` — layered depth trees
  (wiki/models/raw), quality-score fallback, grep/jq query recipes.
- `~/.agents/skills/bailian-managed-agent/SKILL.md` — plan-before-apply
  guardrail, secrets-never-in-preview rules.
- `~/.agents/skills/bailian-sandbox/SKILL.md` — operational-boundary section,
  credential-redaction defaults.
- `~/.agents/skills/omarchy/SKILL.md` — largest observed file (392 lines);
  safety-rule callouts, config-location tables.
- `~/.config/opencode/skills/ufo/SKILL.md` — invariant lists (I1–I10), load-order
  with fail-closed resolution, dispatch contract.

## Moved from SKILL.md § Sources — host surfaces (round 60)

Verbatim from `SKILL.md` § Sources at `31092dc6` lines 509–521 (round 60 line-budget move, 13 lines, replaced by a
2-line pointer; the moved block's sha256 `20766162d5617f04ec566813d617182674fa5135ef8390f551c67f84c0482e4c` is the same before and after the move:
`git show 31092dc6:SKILL.md | sed -n 509,521p | sha256sum` and, while this section is the file's last, `tail -n 13 corpus/knowledge/anatomy-and-compression.md | sha256sum`).

- `~/.config/opencode/agents/*.md` (historical: 18 files, 14–197 lines; absent on this host as of 2026-10-23) — agent-definition
  surface: roster frontmatter (`subagents`, `cascade`, `permission_mode`),
  negative routing (`NOT …` family in 11/18 — round-6 audit corrected
  round-4's 7), shared godspeed preamble in 14/18 (doubled in
  mutation-tester.md), stale dated `cascade_note` and missing `name:` key
  in ufo.md, `aaron` bin declared-but-absent in scout.md.
- `~/.config/opencode/command/*.md` (3 files, 10–13 lines) — command surface:
  pointer-then-rules idiom, `agent:` delegation key, `$ARGUMENTS`.
- CLAUDE.md files: `find ~ -maxdepth 6 -iname 'claude.md' -not -path
  '*/node_modules/*'` → 18 hits at round-7 recount (5 operator-authored, 1
  dispatch template, 12 vendored/cache); loader strings in both harness
  binaries (9 opencode / 17 omp) but 0 captured injections — seventh surface
  class, cold channel.

## Moved from SKILL.md § Router model (round 72)

Moved verbatim to free lines for four author-facing boxes and five gate-registry rows (SKILL.md was 600 of 600 lines; `File ≤ 600 lines` is an executed box). The heading stays in SKILL.md with a pointer. Body (SKILL.md lines 150-204 at `c69711ee`) sha256 `7aa505aadb970057cf7cbcfd0c9ca0414fbbbda701b50060043e61f41df738bb` (`sed -n '150,204p' SKILL.md | sha256sum` at that revision).

Two harnesses consume skills here, and neither shares the other's catalogue
tag, render, or offer gate. Read the harness's own artifacts before predicting
a render — a rule proven on omp is wrong on opencode.

| Harness | Catalogue tag | Description render | Offer gate (action) | Failure mode |
|---------|---------------|--------------------|---------------------|--------------|
| omp | `<skills>` (ELF template) | `cache.get(key) ?? previewSkillDescription` — cached LLM line, else deterministic truncator (`_8n=100`; first sentence if ≥40 chars, else last-space cut + `…`); hard 99-char cliff | Ship the dir under an omp discovery root (`~/.agents/skills`, `~/.omp/agent/skills`, `~/.claude/skills`, project walk-up) and front-load the capability + WHEN into the first ≤99 chars | Trigger material past offset 99 or in sentence 2 renders as nothing (all 13 observed `Triggers:`/反触发/`Excludes` clauses lost) |
| opencode | `<available_skills>` (`fmt(list,{verbose:true})`) | Full `description` byte-for-byte + `<location>` in the system-prompt catalogue; no truncation, no cache (the TUI skill list collapses whitespace only) | Define `description` and a frontmatter `name:`; leave the `skill` permission enabled; if a same-name duplicate exists, do not rely on which copy wins | Missing `description` is filtered out of the catalogue; a denied `skill` permission omits the whole block; duplicate names are last-parsed-wins under unbounded parse concurrency (round-9 re-verify: first-scanned-wins was wrong) |

Check before predicting: on omp read the cache db
(`sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from
skill_descriptions;"`) **and** the newest *catalogue-bearing* `<skills>` block —
mtime order is not a selection rule: the newest session file
(`~/.omp/agent/sessions/<project-slug>/<ts>/<Agent>.jsonl`) may carry no
`<skills>` block (round-8 box-3 cold run's B1), so take the two fields the verifier already resolves:
`python3 verifiers/verify_harness_claims.py --json` → `omp.catalogue_path` /
`omp.catalogue_timestamp`. The catalogue freezes at session start, so db coverage
is time-varying; on opencode read the global roots and
`grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log`.

### Run the verifier instead of re-typing the recipe

`python3 verifiers/verify_harness_claims.py` recomputes this whole table from
live state against `verifiers/baseline.json` and exits non-zero on drift —
**28 checks**: the omp key prefix read out of the ELF
(`omp.elf.template_sha256`, 273 B), `keys_reproduced` per offered skill under the
style-aware salt, cache-miss/truncation count, the newest captured `<skills>`
block matched line-by-line against the cache, offered vs dangling skill dirs,
name==folder, unmodelled YAML scalar forms (excluded, never guessed), opencode
`init count` max vs root-union+builtin, `<available_skills>` hits, per-root
duplicate split, `skill`-permission allow lines. Exit 0 agree / 1 drift
/ 2 environment unreadable / 3 no baseline; `--self-test` falsifies the script's
own truncator + block-scalar model. Cite this file for any harness number rather
than a hand-run recipe, and update the baseline only with a LOG entry naming the
mechanism that moved. Model + gaps: `corpus/knowledge/harness-verifier-round10.md`.

`python3 verifiers/verify_skill_checklist.py` executes this file's own checklist:
**11 checks** (`checklist.box_map_complete` + the eight boxes marked
`(executed: …)` below + `trigger.no_xml_tag`, bound to no box since round 47 +
`governance.citation_resolves` over the two root governance files), each fail-closed on fixtures, `evaluated N` per check,
exit 0/1/2/3 (`3` = box map missing, unparseable, or bound elsewhere).
`verifiers/checklist-baseline.json` maps **all 41 boxes** (8 executed, 2
delegated, 31 unexecuted with reason) by text hash, so drift FAILs. The two
delegated boxes are the dispatch-prompt fidelity boxes `dispatch.04` and
`dispatch.08`, run by `verifiers/verify_dispatch_prompts.py` (its
`--box-proof` prints `boxes proven 2` only when both boxes are delegated there
and each of its six named conjuncts has an isolated must-fail case, judged on
observed statuses; the checklist gate runs `--box-proof` only when the
delegate's `--help` output contains the flag text (a substring test) — a probe that times out, cannot
execute or does not show the flag is reported PASS with "not run", so the gate
fails open there, and a relative `--map` run from another directory gives a
false red and non-UTF-8 `--help` output crashes the gate
(`.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1–F5, carried); the
unsubstituted-variable clause, the `≤` equality boundary, the legacy-state
arm and a non-digit round folder have no fixture yet). Limits and ceilings: `corpus/knowledge/checklist-execution-round17.md`.
