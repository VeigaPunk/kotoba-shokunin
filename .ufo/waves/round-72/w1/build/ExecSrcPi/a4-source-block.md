# S263 (pi coding agent — Skills) — append-ready source block for the A4 rung rule

Seat ExecSrcPi, round 72 wave 1. Read-only opening of the staged row S263. The L1 is the only
integration owner; this file is a draft, not an edit. Every quote below was pasted from
`sed -n '<L>p'` on the snapshot, not retyped.

## 1. Snapshot pins (committed evidence for C1(d))

| file | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-72/snapshots/S263-pi-skills.md` | 4 793 | `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5` |
| `.ufo/waves/round-72/snapshots/S263-pi-docs-skills.html` | 60 383 | `1e9de5d74c7f2fe210c96786ed4950e38ffb5eb4d1a6a33ec48bea16327d438e` |
| `.ufo/waves/round-72/snapshots/S263-support-pi-extensions.md` | 29 010 | `60241267684aa60e724867aabfc88ae663b3984d24dd648438afe9cb637d2378` |
| `.ufo/waves/round-72/snapshots/S263-support-pi-prompt-templates.md` | 2 490 | `ad5113cce0d05ef0ac77b3c71f9ebe41ea68c072275f9273b9616e4924feda42` |

Pin file: `.ufo/waves/round-72/snapshots/S263.sha256` (four `sha256  name` lines).

Upstream pin: GitHub contents API `packages/coding-agent/docs/skills.md?ref=main` →
blob `19d2bf28910ce49caaaf4dde86d1e96330ca7b31`, size 4 793, `download_url`
`https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md`.
Last commit touching the path: `25cc5c7bf4cb` 2026-09-22T14:48:19Z (31 commits touch the path;
newest is that one).

## 2. Row draft (11 cells, lane header order `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`)

```
| S<next-free> | pi coding agent (pi-mono, now earendil-works/pi) — Skills — https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md | docs | B | the pi coding agent's own skill surface, tier=B as one vendor's implementation; scoped to what this file states about the skill/prompt/executable boundary and the resident index, no claim about any other client | the "# Skills" heading: the preamble sentence at snapshot line 3 and the decision sentence at line 5, both before "## Create a skill"; snapshot `.ufo/waves/round-72/snapshots/S263-pi-skills.md` 4 793 B sha256 `5b980552…` (blob `19d2bf28…`, main, fetched 2026-10-25, HTTP 200); the rendered route https://pi.dev/docs/latest/skills serves both sentences verbatim (7-sentence parity probe) | located quote "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point." (22 words) — the middle rung bounded from below by a prompt template and from above by an executable integration point; the same file states the resident index at line 43 (names, descriptions and paths in the system prompt, bodies on demand) | mined | 2026-10-25 | 90d — re-fetch the raw file and confirm the line-3 and line-5 sentences are unchanged | corpus/knowledge/resident-index-and-rungs-round72.md |
```

`used-by` must be the A4 entry path (`corpus/knowledge/resident-index-and-rungs-round72.md`) for
C1(b) to hold. The staged row S263's `used-by` cell names
`corpus/knowledge/skill-vs-always-on-boundary.md`; if the L1 admits the staged entry under that
name instead, swap the cell — but then the A4 entry name in the plan (C1(d)) has to move with it.

## 3. Entry `source:` line (lane convention `source: S### — <name> — <url> — <anchor> — located quote "…"`)

```
source: S<next-free> — pi coding agent (pi-mono) — https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/skills.md — the "# Skills" heading, the decision sentence before "## Create a skill" (snapshot line 5) — located quote "Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point."
```

## 4. Quote-cell candidates for A4 (each 5–25 words, verbatim, word-bounded, one occurrence)

| # | line | words | quote |
|---|---|---|---|
| a | 5 | 22 | `Use a skill when a workflow needs more context than a prompt template but does not need a new executable integration point.` |
| b | 45 | 11 | `This keeps detailed guidance out of context until it is needed.` |
| c | 43 | 17 | `Pi scans configured skill locations and adds each skill’s name, description, and path to the system prompt.` |

Line 43 carries U+2019 in `skill’s`; lines 3, 5, 45, 65, 85 are pure ASCII. If an ASCII
normalization is used anywhere, name it (Q42/Q56).

## 5. What the A4 token set (`prompt`, `always-on`, `skill`, `index`) gets from this page

- `prompt` — line 5, verbatim ("a prompt template").
- `skill` — line 1/3/5, verbatim.
- `index` — the mechanism is stated at line 43 (names, descriptions, paths resident in the system
  prompt; bodies on demand) although the word "index" itself does not occur (`grep -c index` = 0).
- `always-on` — **not on this page**: `grep -c 'AGENTS.md'` = 0, `grep -ci 'always-on\|always on'` = 0.
  The always-on clause of A4 must rest on S262 (Factory) or the corpus's own rung text, not on pi.

## 6. Do not carry the "MCP" gloss into the entry

`grep -ci mcp` on the snapshot = 0. pi's own definition of its third rung lives in the sibling doc
`docs/extensions.md` line 3:

```
Extensions are TypeScript modules that add executable behavior to Pi. Use one when a workflow needs tools, commands, event handlers, model providers, session state, or terminal UI rather than instructions alone.
```

and the lower rung in `docs/prompt-templates.md` line 3:

```
Prompt templates turn Markdown files into reusable `/` commands. Use one when you want to reuse the same prompt without adding executable behavior or a larger set of supporting instructions.
```

Three parallel "Use one when…" sentences across three files is the strongest available form of the
rung statement. Quote the executable rung as "executable behavior" / "executable integration
point"; "MCP-style" is the corpus's inference, and pi's own MCP status changed on 2026-09-29
(`https://earendil.com/posts/you-said-no-mcp/`), seven days after the last edit to `skills.md`.

## 7. Integration constraints observed in the live tree (for the L1, not an edit)

- `SKILL.md` is 600 lines / 72 688 B (`wc -l -c SKILL.md`), the ceiling; a new box needs lines freed first.
- `verifiers/checklist-baseline.json` pins 41 boxes by text hash, 15 of them in
  `Trigger-fidelity checklist` (dispositions: 8 executed, 4 delegated, 29 unexecuted). Adding the
  four A4 boxes requires new `box_id`s, hashes and `box_total` in the same change, or
  `verify_skill_checklist.py` FAILs.
- `verifiers/check_assertion_floors.py` reads `checklist observed=1862 floor=1862` at base; a box
  add moves the observed count and the floor must move in step (`floors-registry.json` BUMP-IN-STEP RULE).
