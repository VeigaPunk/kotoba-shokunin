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
