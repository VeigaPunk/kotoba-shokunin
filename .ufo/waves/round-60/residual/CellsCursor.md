Result: HOLDS — Cursor: all three cells match their cited snapshot lines (`.cursor/rules` is the documented project-rules folder, `globs` is the matching-file key, the action restates line 131 exactly), and the entry quote is byte-identical at 11 words.

# Semantic re-read — SKILL.md § Scoped rule files by client, Cursor row

Revision: `7b80ae80cda69a95b6fc90879395113a99a57912` (= lane `master`, `git rev-parse master` → `7b80ae80cda69a95b6fc90879395113a99a57912`, exit 0). All snapshot lines below pasted verbatim from
`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 7b80ae80cda69a95b6fc90879395113a99a57912:.ufo/waves/round-60/snapshots/S108.page | sed -n '<L>p'` (exit 0 every call).
Source row: `corpus/SOURCES.md:120` — S108 = Cursor Docs — Rules, https://cursor.com/docs/rules, fetched 2026-10-23T12:09:11Z, HTTP 200, 17,403 B, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`.

The row under review (`SKILL.md:147` at the revision):

```
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) | `globs` (example `src/components/**/*.tsx`, S108 :85) | Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131) |
```

## Cell 1 — Rule files: `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) — HOLDS

Cited line `S108.page:32`:

> Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.

Ruling: HOLDS. The token `.cursor/rules` is the folder the page names as the home of project rules ("live in"), not an example rule file; the `.mdc` file type is stated on the same line, so the parenthetical "project rule folder for `.mdc` files" adds nothing the line does not say. The same line also says these rules are "scoped using path patterns" (among other modes), so the folder is where the path-scoped rule kind lives.

## Cell 2 — Scope key: `globs` (example `src/components/**/*.tsx`, S108 :85) — HOLDS

Cited line `S108.page:85` (inside the example frontmatter block "Auto-attached by file pattern", `S108.page:83-86`; line 86 is `alwaysApply: false`):

> globs: src/components/**/*.tsx

Supporting context, behavior table header and rows `S108.page:65,67-70`:

> | `alwaysApply` | `description` | `globs`  | Behavior                                                         |
> | `true`        | —             | —        | Always included. Globs and description are ignored.              |
> | `false`       | —             | provided | Auto-attached when a matching file is in context.                |
> | `false`       | provided      | omitted  | Agent reads the description and pulls the rule in when relevant. |
> | `false`       | omitted       | omitted  | Included only when you `@`-mention the rule in chat.             |

Ruling: HOLDS. `globs` is the key whose presence (with `alwaysApply: false`) limits the rule to matching files — "Auto-attached when a matching file is in context" (line 68) — which is exactly the matching-file class the section header defines. It is not `description` (line 69: the agent pulls the rule by relevance, no path matching), not `alwaysApply` (line 67: `true` means always included and "Globs and description are ignored"), not `name`, and the table names no `excludeAgent` key (header line 65 lists only `alwaysApply | description | globs | Behavior`). The example value `src/components/**/*.tsx` is byte-verbatim from line 85.

## Cell 3 — Action: "Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)" — HOLDS

Cited line `S108.page:131` (under "### Glob pattern examples", `S108.page:129`):

> Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.

Ruling: HOLDS. The cell is byte-for-byte identical to line 131 (Python `snap[130] == cell_text` → True, exit 0; no whitespace or backtick difference). No inverted meaning and no claim beyond the line: the line says exactly that `globs` scopes a rule to files/directories and that multiple patterns are comma-separated. ("§ Glob pattern examples" also matches `corpus/SOURCES.md:130-131`.)

## Entry-row quote — byte-for-byte and word count — HOLDS

Knowledge entry `corpus/knowledge/scoped-rules-round60.md:17`, Quote cell:

> Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.

Checks (Python against the committed snapshot, exit 0):
- It is a contiguous prefix of `S108.page:32` ending at `version-controlled.`: `startswith` → True; the remainder of the line is ` They are scoped using path patterns, invoked manually, or included based on relevance.` — no bytes removed, backticks kept, matching the entry's shaping note ("contiguous prefix of `S108.page:32` through `version-controlled.`; backticks kept; no bytes removed").
- Entry cell == snapshot prefix byte-identical: True.
- `wc -w` → `11` (command: `wc -w /tmp/q.txt` → `11 /tmp/q.txt`, exit 0). The stated constraint is the plan's quote rule "6–25 words" (`plans/round-60.md:82`); no other word count is stated for this quote anywhere in the plan, lesson (`corpus/lessons/round-60.md:15`), or the entry itself (`git grep "11 words\|words" <rev> -- plans/round-60.md corpus/lessons/round-60.md corpus/knowledge/scoped-rules-round60.md | grep -i "cursor\|11 word"` → no match, exit 1). 11 is within 6–25: no `word-count-without-command`-style defect (lesson M86) applies here.

## Cross-checks of the entry prose against the same snapshot

- Intro: "Cursor auto-attaches a `globs` rule when a matching file is in context [S108 :68]" — matches line 68 verbatim. HOLDS.
- Intro: "Cursor documents always-apply, description-selected, and manual rule types alongside path-scoped rules [S108 :65-70]" — matches lines 67–70 (always included; auto-attach on matching file; description-pulled; `@`-mention manual). HOLDS.
- Per-client note: "Project rules are in `.cursor/rules`; `globs` supplies a path pattern, and matching files are auto-attached when in context [S108 :32,68,85]" — all three lines support it. HOLDS.

## Residual risk and verification gaps

- I ruled the committed snapshot, not the live page; live-page drift is out of scope for this cell check (fetch provenance recorded at `corpus/SOURCES.md:120`).
- The counter (`verifiers/check_scoped_rules.py` v2) was not re-run; per erratum E2 its output is supporting evidence only, and this ruling rests on the semantic re-read above.
- The entry's claim that no user-level Cursor rules folder is identified by the census was not re-opened (outside my three cells); it is phrased as a limit of the evidence, not an existence claim.
