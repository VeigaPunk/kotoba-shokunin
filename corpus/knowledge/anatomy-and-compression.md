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
