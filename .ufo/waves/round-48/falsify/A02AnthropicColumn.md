# A02AnthropicColumn — S019 (Anthropic docs) column, round-48 falsify

Seat: KotobaR48.A02AnthropicColumn, 2026-10-22. Leaf seat, no delegation. No tools installed
or upgraded. Read-only on the lane except this file; fetched bytes live in
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A02AnthropicColumn/`.

## Verdict

- S019 column of `corpus/knowledge/frontmatter-rule-authorities-round48.md`: **CONFIRMED** —
  every quote, line number, and "not stated" sweep checks out against today's bytes.
- SOURCES.md S019 row (supersedes S003): **CONFIRMED** on all three supersedence reasons.
- One **DEFECT (low)** on the drift characterization, shared by the entry header and the
  S019 row: "copy edits only, every rule line unchanged" / "the rule lines are unchanged" is
  false at the byte level for three rule-bearing lines (257, 1140, 1150). No rule's content
  changed; the landed sentence still overstates.

## Freshness (re-opened live)

| url | when (UTC) | bytes | sha256 |
|---|---|---|---|
| platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | 2026-10-22T08:52:06Z, `curl -fsSL` exit 0 (HTTP 200) | 42,169 | `f0a5d61b67123a31…` |
| platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md | same run | 21,840 | `7913d4556c014c6b…` |
| agentskills.io/specification.md (cross-ref for supersedes) | same run | 7,608 | `9a67de89132948b2…` |

All three match the hashes recorded in the entry header / SOURCES rows (S019 `f0a5d61b…`,
overview per `C2ClaudeDocs.md` evidence table, S018 `9a67de89…`). Round-47's bytes are archived
in-lane at `.ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md`:
sha256 `727f3fa1168eb1c3…`, 42,028 B — exactly the values the entry cites for round 47.

Located quotes (each ≤25 words, at today's line numbers): bp.md:153 "Maximum 64 characters";
bp.md:156 "Cannot contain reserved words: \"anthropic\", \"claude\""; bp.md:206 "Always write in
third person"; bp.md:257 "Keep the `SKILL.md` body under 500 lines for optimal performance.";
overview.md:215 "Must contain only lowercase letters, numbers, and hyphens"; spec.md:237 "Keep
your main `SKILL.md` under 500 lines."

## Cell-by-cell (S019 column)

| cell | claim | result |
|---|---|---|
| name length | "Maximum 64 characters" (bp.md:153) | CONFIRMED verbatim at 153 |
| name charset | "Must contain only lowercase letters, numbers, and hyphens" (bp.md:154) | CONFIRMED at 154; restated bp.md:172, overview.md:215 |
| name equals directory | not stated (b) | CONFIRMED: sweep pattern 0 hits in bp.md and overview.md (exit 1); my wider `grep -niE 'director\|folder'` over bp.md hits only 275/459/1053/1057/1071, none a rule |
| consecutive hyphens | not stated (`grep -niE consecutive` → 0) | CONFIRMED: 0 hits in both pages |
| description length | "Must be non-empty", "Maximum 1,024 characters" (bp.md:160-161) | CONFIRMED at 160 and 161 respectively |
| XML tags | "Cannot contain XML tags" for name and description (bp.md:155,162) | CONFIRMED at 155 (name) and 162 (description) |
| third person | "Always write in third person" (bp.md:206) | CONFIRMED at 206 |
| reserved words | "Cannot contain reserved words: \"anthropic\", \"claude\"" (bp.md:156) | CONFIRMED at 156; examples at bp.md:191 |
| unknown top-level fields | not stated (`grep -niE 'unknown field\|unrecognized'` → 0) | CONFIRMED: 0 hits in both pages |
| body length | "under 500 lines for optimal performance" (bp.md:257) | CONFIRMED at 257; restated bp.md:1140, checklist bp.md:1150 |

Anchor headings all exist in today's bytes: `## Skill structure` (bp.md:146), `### Writing
effective descriptions` (bp.md:201), `### Progressive disclosure patterns` (bp.md:251). The
entry's recheck command logic verified on the spec: `grep -c 'Must match the parent directory
name' spec.md` → 1 today.

## Drift claim — DEFECT (low)

`diff` old→new: exit 1, 62 change records, all `c` (in-place), 79/79 lines, both files 1,191
lines — no insertions/deletions, so all cited line numbers are stable across both shas.

But the change records include `257,259c257,259`, `1140c1140`, `1150c1150` — the three 500-line
rule statements:

- old bp.md:257 `* Keep SKILL.md body under 500 lines for optimal performance` → new
  `* Keep the `SKILL.md` body under 500 lines for optimal performance.` (article, backticks,
  period added)
- old bp.md:1140 `Keep SKILL.md body under 500 lines…` → new `Keep the `SKILL.md` body under
  500 lines…` (same class)
- old bp.md:1150 checklist bullet `* [ ] SKILL.md body is under 500 lines` → new with backticks

So "every rule line unchanged" (entry header) and "the rule lines are unchanged" (SOURCES S019
anchor) are literally false: the very line the body-length cell quotes changed bytes since the
round-47 sha. The rule content is identical everywhere — 153-162, 206, 1133-1134 are
byte-identical (absent from all change records) — so no cell, quote, or teaching is wrong
against today's bytes; only the drift sentence overstates. Root: `C2ClaudeDocs.md` F2 says "the
… 500-line sentence [is] byte-identical at both shas", contradicting its own later evidence
line "only 500-line backtick/punctuation lines" changed. Suggested repair wording: "no rule's
content changed; copy edits (backticks/article/period) touched three rule-bearing lines
(257, 1140, 1150)".

## SOURCES.md S019 row (teaches supersedes S003)

All three supersedence reasons verified against live bytes:

1. "the 500-line body rule is not Anthropic-only: the open spec states it too (S018 §
   Progressive disclosure)" — spec.md:237 sits under `## Progressive disclosure` (heading
   spec.md:229); hash matches S018's `9a67de89…`.
2. "Anthropic-only … the no-XML-tags rule on both `name` and `description`" — `grep -niEc
   'angle\|xml' spec.md` → 0 (exit 1); skills-ref/packager/Codex columns consistent with the
   entry's table.
3. reserved words "anthropic"/"claude" and the third-person rule — no other tabled authority
   states them; bp.md:156 and bp.md:206 are the only statements among the opened sources.

S003's own row (SOURCES.md:16) keeps its now-known-wrong "an Anthropic-only rule the open spec
lacks" with status `mined` and no superseded marker. That matches the registry's established
convention (S018 supersedes S001, S020 supersedes S010, S021 supersedes S013 — superseded rows
are left untouched, the new row carries the correction), so not scored as a round-48 defect.

## Residual risk / verification gaps

- S019 `recheck: 90d` while the page's `.md` endpoint demonstrably moved within one day
  (2026-10-21 → 2026-10-22). The 90d matches every other docs-tier row, and the anchor records
  the churn, but a hash-equality recheck of this URL will false-alarm roughly daily; the
  entry's fail-closed re-fetch-and-compare pattern is the workable one.
- I verified the Anthropic column only; the skills-ref/packager/Codex/lane columns were not
  re-run (other seats' targets). The "Anthropic-only" claims were spot-checked against the
  spec bytes and the entry's own table, not against re-run validators.
- Round-47 bytes exist only as the retained wave-dir copy (in-lane); if that file is ever
  garbage-collected, the drift claim loses its evidence base.
- Client runtime behavior (what Claude Code actually enforces, the 256-character name refusal)
  is recorded in `C2ClaudeDocs.md` F3/F4 but has no SOURCES row; the entry's Limits paragraph
  describes this faithfully ("not yet opened into source rows").
