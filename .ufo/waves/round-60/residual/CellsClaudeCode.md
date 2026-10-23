Result: HOLDS — Claude Code: every cell of the SKILL.md row says what its cited S103 snapshot line says, `paths` is the page's matching-file key (not `description`/`name`/`alwaysApply`/`excludeAgent`), `.claude/rules/` is the page's rule folder, and the entry quote is byte-exact against `S103.page:168` at 14 words.

# Claude Code row — semantic re-read (seat CellsClaudeCode)

- Target: `SKILL.md` § `### Scoped rule files by client` (SKILL.md:135), Claude Code row at SKILL.md:141, data commit `7b80ae80cda69a95b6fc90879395113a99a57912`.
- Lane tip: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master` → `7b80ae80cda69a95b6fc90879395113a99a57912` (tip == data commit).
- Snapshot integrity: `git show 7b80ae8:.ufo/waves/round-60/snapshots/S103.page | sha256sum` → `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` (664 lines); equals the sha256 recorded in `corpus/SOURCES.md` row S115 (`S103 … sha256 82d6034…bb6e7`, fetched 2026-10-23T12:08:16Z, HTTP 200, 54,043 B).
- LSP note: this surface is markdown prose; no language server answers `.md` files here (no `lsp` device in this seat's inventory), so all caller/definition checks are byte-exact `git show` comparisons, recorded as such — no grep output is offered as semantic proof.

The row under review (SKILL.md:141, first table of the section, header SKILL.md:139):

```
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194) |
```

## Cell 1 — Rule files: `` `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) ``

Cited line, `git show 7b80ae8:.ufo/waves/round-60/snapshots/S103.page` line 168:

> For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain. Rules can also be [scoped to specific file paths](#path-specific-rules), so they only load into context when Claude works with matching files, reducing noise and saving context space.

- Token is the folder, not an example file: line 168 names `.claude/rules/` as a **directory** for organizing instructions into multiple files; line 176 says "Place markdown files in your project's `.claude/rules/` directory"; the scoped-rule section (`#### Path-specific rules`, line 192) sits inside this same rules organization. The path is dot-led with ≥ 2 segments (`.claude` + `rules`), well-formed per the counter's token rule (plans/round-60.md:74-75).
- "multi-file instructions" ⇔ "organize instructions into multiple files" — match. "scoped to matching files" ⇔ "scoped to specific file paths … only load into context when Claude works with matching files" — match, no inversion, no extra claim.
- Corroboration that scoping is a property of rules *in this folder*: line 188 "Rules without [`paths` frontmatter](#path-specific-rules) are loaded at launch with the same priority as `.claude/CLAUDE.md`" — i.e. the launch-loaded fallback is the no-`paths` rule in the same directory.

**Ruling: HOLDS.**

## Cell 2 — Scope key: `` `paths` (e.g. `src/api/**/*.ts`, S103 :198) ``

Cited lines, same snapshot, lines 198–199 (frontmatter block opened at line 196):

```
198: paths:
199:   - "src/api/**/*.ts"
```

Defining line 194 (the cell's semantics):

> Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.

- K = `paths` is the key that limits the rule to matching files: line 194 says scoping to specific files happens "using YAML frontmatter with the `paths` field", and line 188 makes `paths` the discriminator between launch-loaded and conditional rules. The page nowhere offers `description`, `name`, `alwaysApply`, or `excludeAgent` as a matching-file key for Claude Code (those names belong to Cursor's other rule types, S108; the counter's forged-key forms such as `sessions` pass no Claude Code cell here). Not a printed-but-wrong name.
- Citation precision: the key stands in key form on the cited line 198 (`paths:` with empty value); the example value `src/api/**/*.ts` is on the next line 199. Under the plan's A1 scope-key conjunct this is exactly the anticipated shape (plans/round-60.md:54-58: value empty → first nonblank among the next 3 lines, beginning with `-` or a quote, first token containing `*`). The entry's per-client note cites the block as "[S103 :168,194,198-199]", so the entry itself cites both lines. The cell's claim is true of the cited block; no inverted or unsupported meaning.

**Ruling: HOLDS** (precision note: the "e.g." glob sits on :199, one line below the cited :198, inside the same frontmatter block; the entry cites 198-199 jointly).

## Cell 3 — Action: "Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)"

Cited line 194 (pasted above):

> Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.

- "Scope rules to specific files using YAML frontmatter" ⇔ "Rules can be scoped to specific files using YAML frontmatter with the `paths` field" — match (the cell omits the field name, which the Scope key cell supplies; no contradiction).
- "apply only when matching specified patterns" ⇔ "only apply when Claude is working with files matching the specified patterns" — match. The line's "only" is preserved, not inverted, and the line carries no negation that could be flipped. No claim beyond the line (nothing about load priority, nesting, or `--setting-sources`).
- A1 word-overlap framing (plans/round-60.md:61-64) acknowledges a cell can share the line's words yet invert it; read semantically this cell does not.

**Ruling: HOLDS.**

## Entry row quote — byte-for-byte and word count

Entry `corpus/knowledge/scoped-rules-round60.md` line 15:

```
| Claude Code | `.claude/rules/` | S103 | For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. |
```

- Byte-for-byte: the Quote cell equals the prefix of `S103.page:168` through `directory.` exactly (Python compare of the entry cell vs the snapshot prefix → `byte-equal: True`; also a strict prefix of the full line). Backticks around `.claude/rules/` kept, no bytes removed — matches the entry's own shaping note ("contiguous prefix of `S103.page:168` through `directory.`; backticks kept; no bytes removed", entry line 35).
- Word count: `printf '%s' 'For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.' | wc -w` → `14` (exit 0). The stated bound is 6–25 words (plans/round-60.md:82); 14 is within it, and the quote contains the token `.claude/rules/` case-sensitively and the word "instructions" outside the token, satisfying the counter's backed-row shape.
- Token identity: entry Rule-files token `.claude/rules/` == SKILL row token; source S103 is a tier-A docs row on the client's pinned host opened 2026-10-23 (corpus/SOURCES.md S103 row).

## Verdict

| Cell | Citation | Snapshot says | Ruling |
|---|---|---|---|
| Rule files `.claude/rules/` (multi-file, scoped to matching files) | S103 :168 | folder for multiple instruction files; rules there can be scoped so they load only for matching files | HOLDS |
| Scope key `paths` (e.g. `src/api/**/*.ts`) | S103 :198 (value :199) | `paths` field scopes rules to matching file patterns; without it rules load at launch (:188, :194) | HOLDS |
| Action "Scope rules … YAML frontmatter; apply only when matching specified patterns." | S103 :194 | same sentence, same meaning, negation preserved | HOLDS |
| Entry quote | S103 :168 | byte-equal prefix through `directory.`; `wc -w` → 14 (bound 6–25) | HOLDS |

No BREAKS or MIXED cells; no corrected cell required.

## Residual risk and verification gaps

- [INFERENCE] The snapshot is treated as a faithful capture of `https://code.claude.com/docs/en/memory.md` (SOURCES records HTTP 200, 54,043 B, sha256, fetched 2026-10-23T12:08:16Z); I verified the committed blob's sha256 against the SOURCES row but did not re-fetch the live page — live drift after 2026-10-23 would not show here.
- The counter itself is supporting evidence only (attempt-1 erratum E2: two v2 controls met it with forged provenance); this ruling rests on the line-level re-read above, not on counter output, which this seat did not run.
- Scope-key precision noted above: the "e.g." value lives on :199 while the cell cites :198; harmless under A1's key-form reading and the entry's joint :198-199 citation, but a future tightening could require citing the value line too.
- No runtime check: whether Claude Code actually loads these files per the page is outside documentation scope and explicitly not held (entry § Not held).
