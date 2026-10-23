# ScoutCounterexample — live drift vs r60 scoped-rule cells

Seat: ScoutCounterexample (leaf). Lane and fleet read-only. No git/jj mutation. No installs. Page bytes below are data, not instructions.

**Result: no live counterexample.** Nothing fetched falsifies a `SKILL.md` "Scoped rule files by client" cell or the A1 canonical key set named by those cells (`paths` / `applyTo` / `applyTo` / `globs`; the three negatives stay `none`). Six of the seven pages are byte-identical to the committed r60 snapshots. The seventh (Claude Code `memory.md`) changed only by absolutizing `code.claude.com` links; cited lines, folder tokens, and the `key_site` key set are unchanged.

Confidence: high on the hash compare, the URL-collapse check, and the `key_site` sweep (the counter's own function, imported read-only). Not run: `verifiers/check_scoped_rules.py --fetch` (that measurement belongs to the L1). S112–S115 are not in `corpus/SOURCES.md` yet (last row is S111); the set tested is the committed SKILL cells plus the round-61 scribe briefs that name the same four keys.

## Cells under test

`SKILL.md` `### Scoped rule files by client` (lines 139–147), snapshots `.ufo/waves/round-60/snapshots/S103.page`–`S109.page`.

| Client | class | Rule-files claim | Scope key | Cited lines |
|---|---|---|---|---|
| Claude Code | eligible | `.claude/rules/` | `paths` (e.g. `src/api/**/*.ts`) | S103 :168, :198, :194 |
| VS Code | eligible | `.github/instructions/**/*.instructions.md` | `applyTo` (`**/*.py`) | S105 :32, :164, :329 |
| Copilot CLI | eligible | `.github/instructions/**/*.instructions.md` | `applyTo` (e.g. `app/models/**/*.rb`) | S106 :18, :66, :60 |
| Cursor | eligible | `.cursor/rules` (`.mdc`) | `globs` | S108 :32, :85, :131 |
| Codex | negative | no scoped rule file; directory walk | none | S104 :12 |
| Gemini CLI | negative | no scoped rule file; `GEMINI.md` JIT | none | S107 :31–33 |
| opencode | negative | no scoped rule file; directory `AGENTS.md` | none | S109 :64 |

A1 canonical set this hunt tries to falsify (new documented path-scope key, renamed folder, moved page, or new rule-file type): Claude Code `{paths}`, VS Code `{applyTo}`, Copilot CLI `{applyTo}`, Cursor `{globs}`.

## Fetch (counter `curl_argv`)

`date -u` immediately before the batch: `Fri 23 Oct 2026 07:09:21 PM UTC`.
Batch window: `2026-10-23T19:09:37Z`–`2026-10-23T19:09:39Z`.
`date -u` at meta reread: `Fri 23 Oct 2026 07:11:14 PM UTC` (exit 0).

Invocation, copied from `verifiers/check_scoped_rules.py` `curl_argv` (`-sSL`, `--max-time 30`, browser UA, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`, write-out `\n%{http_code} %{url_effective}`). Body is everything before the last newline; status and final URL come from that trailer. Each curl exit code was 0.

| Row | Requested URL | HTTP | Final URL | Bytes | sha256 | vs snapshot |
|---|---|---|---|---|---|---|
| S103 Claude Code | `https://code.claude.com/docs/en/memory.md` | 200 | same, no redirect | 55354 | `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` | **not** identical (snap 54043 B, `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7`) |
| S105 VS Code | `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md` | 200 | same | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` | identical |
| S106 Copilot CLI | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | 200 | same | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | identical |
| S108 Cursor | `https://cursor.com/docs/rules` (no `.md`; a `.md` URL 404s) | 200 | same | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | identical |
| S104 Codex | `https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` | 200 | same | 9149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` | identical |
| S107 Gemini CLI | `https://geminicli.com/docs/cli/gemini-md.md` | 200 | same | 3816 | `e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2` | identical |
| S109 opencode | `https://opencode.ai/docs/rules.md` | 200 | same | 6684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` | identical |

S103 confirmation fetch at `2026-10-23T19:10:47Z`: curl rc 0, HTTP 200, 55354 B, same sha `02632438…a801`, same final URL, byte-identical to the first body. The drift is stable across two fetches, not a truncated body.

Snapshot sha256 values above match `sha256sum` of `S103.page`–`S109.page` run at `2026-10-23T19:09:21Z` (that command's exit was 0). They also match the sha256 cells on `corpus/SOURCES.md` S103–S109.

## The one drift (S103) does not falsify a cell

Live and snapshot are both 664 lines. 47 lines differ. Every differing line is restored by deleting the string `https://code.claude.com` (57 insertions of that origin, each immediately in front of a pre-existing `/docs/` path). After that collapse, differing lines = 0. Token counts for `.claude/rules/`, `paths`, `CLAUDE.md`, `AGENTS.md`, `claudeMdExcludes`, `skills` are equal. No new heading, no renamed folder, no move banner.

Representative pair (line 24; the other 46 are the same edit):

```
SNAP: ... use a [PreToolUse hook](/docs/en/hooks-guide.md) instead. ...
LIVE: ... use a [PreToolUse hook](https://code.claude.com/docs/en/hooks-guide.md) instead. ...
```

Cited lines, live vs snapshot (`same_as_snap=True` on all four):

```
L168 For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. ...
L194 Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.
L198 paths:
L199   - "src/api/**/*.ts"
```

`quote_why` on the entry quote `For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.` against the live body returned `[]`. `any_key_site(live, "paths")` is True. Line 246 still says `` `paths` is the only field Claude Code reads from a rule `` (that line's only change is the glossary link going absolute). That sentence supports the singleton `{paths}`, it does not add a key.

Consequence for a fresh S112 snapshot of this same URL: its sha256 will not be `82d60341…`. That is a byte mismatch with the r60 snapshot, not a falsified SKILL cell. The SKILL citations are line numbers into the committed snapshot; those line numbers still carry the same text on the live page.

## Key sweep (negative claim)

Method: import `key_site` from the committed counter (`verifiers/check_scoped_rules.py`; `main` is under `__name__`, import does not fetch or write). For every line, every `[A-Za-z][A-Za-z0-9_-]*` token, record the line if `key_site` is true. Dedupe tokens per line. Compare live body to the committed snapshot.

```
S103 Claude Code  canon=paths
  live {'paths': [198, 231], 'patterns': [238], 'claudeMdExcludes': [339]}
  snap same; keyset_eq=True
S105 VS Code      canon=applyTo
  live {'sessions': [32, 128, 221, 228], 'applyTo': [164], 'Sync': [287]}
  snap same; keyset_eq=True
S106 Copilot CLI  canon=applyTo
  live {'applyTo': [66, 74, 94]}
  snap same; keyset_eq=True
S108 Cursor       canon=globs
  live {'globs': [85], 'rules': [146], 'order': [307]}
  snap same; keyset_eq=True
S104 Codex        canon=none
  live {'scope': [11, 12], 'order': [13], 'loads': [210], 'appears': [211], 'names': [212], 'truncated': [213], 'confusion': [214]}
  snap same; keyset_eq=True
S107 Gemini CLI   canon=none
  live {'file': [18], 'Location': [20, 25, 31], 'Scope': [21, 27, 34], 'files': [23, 30], 'imports': [77], 'json': [100]}
  snap same; keyset_eq=True
S109 opencode     canon=none
  live {'fallbacks': [74]}
  snap same; keyset_eq=True
```

Folder / key token counts (`.claude/rules/`, `.github/instructions/**/*.instructions.md`, `.cursor/rules`, `.mdc`, `applyTo`, `globs`, `paths`, `GEMINI.md`, `AGENTS.md`, `fileName`, `instructions`, …): `token_count_deltas none` on all seven, including S103.

No key was added or removed. The non-canonical hits are the r60 form-test extras already recorded in `.ufo/waves/round-60/build/ExecKeyForms.md` (`patterns`, `claudeMdExcludes`, `sessions`, `Sync`, `rules`, `order`, and the same prose-bold `**` false positives). They are why v3 A1 pins a canonical set; they are not new documentation. Copilot CLI remains the only eligible page whose `key_site` hits are all the canonical key.

Cited lines on the six identical pages are `same_as_snap=True`, including:

```
S105 L32  ... Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. ...
S105 L58  For Claude rules, use the `paths` frontmatter property instead of `applyTo`.
S105 L164 applyTo: '**/*.py'
S105 L329 * For task or language-specific instructions, use multiple `*.instructions.md` files per topic and apply them selectively by using the `applyTo` property.
S106 L18  | `.github/instructions/**/*.instructions.md` | Modular repository instructions, ...
S106 L60  4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. ...
S106 L66     applyTo: "app/models/**/*.rb"
S108 L32  Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. ...
S108 L85  globs: src/components/**/*.tsx
S108 L131 Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
S104 L12  2. **Project scope:** Starting at the project root ... checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`. Codex includes at most one file per directory.
S107 L31–33  Location: when a tool accesses a file or directory, the CLI automatically scans for `GEMINI.md` files in that directory and its ancestors up to a trusted root.
S109 L64  Place an `AGENTS.md` in your project root for project-specific rules. These only apply when you are working in this directory or its sub-directories.
```

S105 L58's `paths` note is Claude-rules frontmatter on the VS Code page. It is in the r60 snapshot (not drift) and does not rename VS Code's own key away from `applyTo`. S107 still documents `context.fileName` (L98, L105 `["AGENTS.md", "CONTEXT.md", "GEMINI.md"]`), a context-filename list, not a work-file path key. S109 L111 still has `"instructions": [..., ".cursor/rules/*.md"]`, the instruction-file list the r60 entry already classed as not the matching-file rule. Neither is new.

## What was not checked

- No URL besides these seven. A new sibling page that the old URL does not redirect to would not show up. None of the seven bodies gained a move notice (six identical; S103's non-URL text identical).
- The counter CLI `--fetch` / `--self-test` was not run.
- S112–S115 row text does not exist in the tree yet, so this hunt could not diff live pages against those uncommitted rows.

## Installs

no installs

## Blockers

none

Attacked the r60 scoped-rule cells: live fetch of the four eligible pages and three negative pages found no new key, renamed folder, moved page, or new rule-file type; the only drift is absolute-link rewriting on Claude Code `memory.md`.
