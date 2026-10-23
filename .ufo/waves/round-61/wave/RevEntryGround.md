# RevEntryGround — r60 entry cell-by-cell snapshot audit (kotoba round 61, wave)

- Seat: kotoba-r61-wave-RevEntryGround · Date: 2026-10-23 (all commands run 2026-10-23, see `date -u` pasted per block)
- Target: `corpus/knowledge/scoped-rules-round60.md` (base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`)
- Against: `.ufo/waves/round-60/snapshots/S103.page` … `S109.page` (plus the census/recensus files the entry cites, committed under `.ufo/waves/round-60/w0/` and `w0b/`)
- Method: fixed-string grep evidence per cell (grep tool, literal patterns) + a byte-exact Python checker (`/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-RevEntryGround/check_entry.py`, scratch — untrusted, cited only via its pasted output) that extracts the entry's four table rows verbatim and does plain substring/prefix containment against the cited snapshot lines, including the S106 space-run and `&#124;` unescape. No lane/fleet/jj/git mutation (only read-only `git show`); no dispatch.

## Verdict

**No drifting cell.** All four table Quote cells occur byte-verbatim at exactly the snapshot lines the entry's Quote-shaping section documents; every backticked Rule-files token occurs verbatim on those same lines; every inline snapshot anchor I checked lands on a line supporting its claim; all census/recensus spans cited by the entry exist and say what the entry says they say; all seven snapshot sha256 values match `corpus/SOURCES.md` and are byte-identical at the base rev. Two low-severity anchor-precision notes (below), neither touching a quoted span.

## 1. The four Quote cells (the ground v3 must not regress)

### S103 — documented shaping: "contiguous prefix of `S103.page:168` through `directory.`; backticks kept; no bytes removed"

Cell: `For larger projects, you can organize instructions into multiple files using the \`.claude/rules/\` directory.`

Grep evidence (literal pattern incl. escaped metacharacters), tool output:

```
*168|For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain. Rules can also be [scoped to specific file paths](#path-specific-rules), so they only load into context when Claude works with matching files, reducing noise and saving context space.
```

Byte-exact: `[PASS] S103 cell is verbatim prefix of S103.page:168 :: len=108` — the cell is exactly the line prefix (108 bytes), line continues ` This keeps…`. Prefix shaping as documented. **OK.**

### S105 — documented shaping: "contiguous slice of `S105.page:32` (the second sentence of the line); backticks kept; no bytes removed"

Cell: `Targeted instructions can use \`.github/instructions/**/*.instructions.md\` or Markdown files in \`.claude/rules\`.`

Grep evidence — first attempt with the fully escaped pattern (contains `**`) returned "No matches found"; re-run as plain substring, tool output:

```
*32|> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.
```

Byte-exact: `[PASS] S105 cell occurs verbatim in S105.page:32 :: idx=127`; `[PASS] S105 cell is second sentence (line prefix before cell ends with '`CLAUDE.md`. ') :: prefix_tail=' `CLAUDE.md`. '`; `[PASS] S105 cell sentence-ends in snapshot right after cell` (next chars ` The`). Slice shaping as documented; independent corroboration: `CensusVSCode.md` ("Quote (line 32)") derives the identical 10-word quote. **OK.**

### S106 — documented shaping: "contiguous slice of the table row `S106.page:18` from the token's opening backtick through `locations`; the source's run of spaces is kept and its one table pipe is written `&#124;` … (the counter unescapes it); no other bytes changed"

Cell (raw, as written in the entry): `` `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations ``

Grep evidence — escaped pattern failed (same `**` tool quirk), plain substring, tool output:

```
*18|| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |
```

Byte-exact: `[PASS] S106 cell (after single &#124;->| unescape) occurs verbatim in S106.page:18`; `[PASS] S106 space run between backtick and pipe preserved :: entry_spaces=14 snapshot_spaces=14`; `[PASS] S106 cell ends at 'standard locations' and snapshot continues 'but not intermediate'`; `[PASS] S106 cell has exactly one &#124; escape`. Counter support for the documented unescape: `verifiers/check_scoped_rules.py:935-938`:

```
935| def page_plain(s: str) -> str:
936|     """The v1.3 `_plain` without its final lower-casing: case is preserved."""
937|     s = html.unescape(s)
938|     s = re.sub(r"[`*_]", "", s)
```

`html.unescape` at line 937 does turn `&#124;` back into `|` before matching — the documented shaping site is real in the committed counter. Slice/truncation shaping as documented. **OK.**

### S108 — documented shaping: "contiguous prefix of `S108.page:32` through `version-controlled.`; backticks kept; no bytes removed"

Cell: `Project rules live in \`.cursor/rules\` as \`.mdc\` files and are version-controlled.`

Grep evidence (literal pattern), tool output:

```
*32|Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.
```

Byte-exact: `[PASS] S108 cell is verbatim prefix of S108.page:32 :: len=81`. Prefix shaping as documented. **OK.**

Rule-files column tokens on the same cited lines: `[PASS] Rule-files S103 '.claude/rules/' occurs in :168` · `[PASS] Rule-files S105 '.github/instructions/**/*.instructions.md' occurs in :32` · `[PASS] Rule-files S106 token occurs in :18` · `[PASS] Rule-files S108 '.cursor/rules' occurs in :32`.

## 2. Checker transcript (command + result + exit + date)

Command: `python3 -B /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-RevEntryGround/check_entry.py` (cwd `kotoba-shokunin`), exit code line and clock pasted from the run:

```
### 1. TABLE QUOTE CELLS (byte-exact vs documented snapshot line)
[PASS] S103 cell is verbatim prefix of S103.page:168 :: len=108
[PASS] S105 cell occurs verbatim in S105.page:32 :: idx=127
[PASS] S105 cell is second sentence (line prefix before cell ends with '`CLAUDE.md`. ') :: prefix_tail=' `CLAUDE.md`. '
[PASS] S106 cell (after single &#124;->| unescape) occurs verbatim in S106.page:18
[PASS] S106 space run between backtick and pipe preserved :: entry_spaces=14 snapshot_spaces=14
[PASS] S106 cell ends at 'standard locations' and snapshot continues 'but not intermediate'
[PASS] S106 cell has exactly one &#124; escape
[PASS] S108 cell is verbatim prefix of S108.page:32 :: len=81
[PASS] Rule-files S103 '.claude/rules/' occurs in :168
[PASS] Rule-files S105 '.github/instructions/**/*.instructions.md' occurs in :32
[PASS] Rule-files S106 token occurs in :18
[PASS] Rule-files S108 '.cursor/rules' occurs in :32
### SUMMARY
FAILS: none
EXIT=0
Fri 23 Oct 2026 07:19:06 PM UTC
```

(First run of the checker reported one FAIL on the S105 "second sentence" predicate — that was my checker's own index arithmetic (`find` start vs end), not an entry defect; predicate corrected, rerun above. Both transcripts retained in scratch.)

## 3. Inline anchors, claim by claim (snapshot lines dumped and read)

| Entry claim (cell) | Cited | Snapshot line content | Verdict |
|---|---|---|---|
| "a `paths` rule loads only when Claude works with matching files" | S103 :168 | "…only load into context when Claude works with matching files…" | OK |
| "rules without `paths` load at launch" / "`.claude/CLAUDE.md` is a separate, launch-loaded file" | S103 :188 | "Rules without [`paths` frontmatter](…) are loaded at launch with the same priority as `.claude/CLAUDE.md`." | OK |
| "YAML frontmatter `paths` takes the matching file patterns" | S103 :194,198-199 | :194 "…scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns." ; :198-199 `paths:` / `- "src/api/**/*.ts"` | OK |
| "`~/.claude/rules/` as a user-level rules directory" / "path-scoped rules can be in either" | S103 :273,640 | :273 "Personal rules in `~/.claude/rules/` apply to every project…" ; :640 "[Path-scoped rules](…) in your project's `.claude/rules/` or in `~/.claude/rules/`" | OK |
| "automatically attaches an `applyTo` instruction when its pattern matches files being changed" | S105 :105 | "VS Code automatically attaches files with an `applyTo` pattern that matches the files being changed. The agent can also load an instructions file on demand when its `description` matches the current task." | OK |
| "loading an instruction on demand when its `description` matches the task" | S105 :27,105,164 | :105 carries the sentence; :27 is the harness-table Copilot row (token row, not description); :164 is `applyTo: '**/*.py'` (the `description` example line is :163) | OK, see Low-1 / Info-2 |
| "Local-harness note also lists `CLAUDE.md`" / "project-wide" / "targeted files" | S105 :24,32,64 | :32 note lists `.github/copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md` + targeted files; :64 "…use `.github/copilot-instructions.md` for project-wide guidance."; **:24 is a blank line** | OK except dead anchor :24 — see Low-1 |
| "includes a path-specific instruction only when `applyTo` matches a file it is working with" | S106 :32 | "Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with…" | OK |
| "repository-wide `.github/copilot-instructions.md` is a separate scope" | S106 :17 | "\| `.github/copilot-instructions.md` \| Repository-wide instructions, discovered in the standard locations. \|" | OK |
| "`applyTo` makes them conditional on the file Copilot CLI is working with" | S106 :18,32,66 | :32 is the condition; :66 is the `applyTo: "app/models/**/*.rb"` frontmatter example; :18 is the table row (file identity) | OK (bundle) |
| "auto-attaches a `globs` rule when a matching file is in context" | S108 :68 | "\| `false` \| — \| provided \| Auto-attached when a matching file is in context. \|" | OK |
| "always-apply, description-selected, and manual rule types" | S108 :65-70 | :67-70 behavior table (Always included / Auto-attached / description-pulled / @-mention); phrasing is verbatim from `CensusCursor.md:20` which itself points at snapshot lines 65–70 | OK |
| "`globs` supplies a path pattern" | S108 :85 | `globs: src/components/**/*.tsx` (example frontmatter) | OK |
| "Codex walks instruction files by directory… at most one file per directory" | S104 :12 | "…walks down to your current working directory… checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names… includes at most one file per directory." | OK |
| "user-home default plus workspace/ancestor and just-in-time directory discovery" | S107 :20-35,38-40 | :20-21 `~/.gemini/GEMINI.md` "Provides default instructions for all your projects"; :20-35 global/workspace/JIT sections; :38-40 land on the footer-cue sentence + "### Example `GEMINI.md` file" heading | OK (:38-40 loose — Info-3) |
| "`fileName` setting names context filenames" | S107 :94-108 | :98 "`context.fileName` property." ; :105 `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` | OK |
| "project-directory rules and a global file" | S109 :64,68 | :64 "…only apply when you are working in this directory or its sub-directories." ; :68 "global rules in a `~/.config/opencode/AGENTS.md` file… applied across all opencode sessions." | OK |

## 4. Census / re-census spans cited by the entry (committed, not snapshots)

- `CensusVSCode.md:133-139` ("Other printed paths (not the chosen token)") — present; lists `.github/instructions` variants, `.github/copilot-instructions.md`, `~/.copilot/instructions`, `.claude/rules`, `*.instructions.md`; none establishes a VS Code user-home rule folder → supports the entry's "does not establish … limit of the evidence" sentence. OK.
- `CensusCodex.md:28-46` — directory-walk quote (`agents-md.body:12`) + "No frontmatter on this page. Fallback names are a filename list in config.toml …, not a path-pattern key." OK.
- `CensusCodex.md:48-93` — "Rejected candidate A — ~/.codex/rules/ (command execpolicy)", experimental (`rules.body:7`), match target is a command prefix (`rules.body:61` "defines the command prefix to match"). Entry's "`pattern` matches command prefixes, not instruction-file paths" OK. The parenthetical "census's second fetch https://learn.chatgpt.com/docs/agent-configuration/rules.md, which is not a committed round-60 snapshot" is supported: `CensusCodex.md:12` records `rules.body` from exactly that URL, and `.ufo/waves/round-60/snapshots/` contains only `S103.page`–`S109.page` — no rules snapshot committed. OK.
- `CensusCodex.md:95-100` — "AGENTS.md is one segment and does not start with a dot" (Rejected candidate B). Entry's "one segment and not dot-led" OK.
- `CensusCursor.md:20` — contains verbatim "always-apply, description-selected, and manual rules (lines 65–70)". `:65-76` — action line (`globs` scope, line 131) and "not a key site" notes; no default-for-missing-globs statement, no user-level folder. Supports both Cursor-bullet limit sentences. OK.
- `CensusGeminiCLI.md:66-88` — scope-key failure on `context.fileName`/`fileName`, "No Action line tells a rule author to attach a path pattern", docs-tree search counts (`.gemini/rules` 0, `applyTo` 0, `globs:` 0). Supports "no path-pattern key and no action line". OK.
- `Censusopencode.md:73-86` — "Near-miss key `instructions` (not a scope key)"; "the globs choose instruction files to load with `AGENTS.md`, not paths of files the agent is working on" — entry paraphrases this almost verbatim. OK.
- `RecensusCopilotCLI.md:115` — "Personal `~/.copilot/instructions/` applied to every session. No token, `any_key_site(applyTo)` False" on `cli-config-dir-reference.md`; and `corpus/SOURCES.md` S106 row confirms the assigned snapshot URL is `…/customize-copilot/add-custom-instructions.md` — the entry's parenthetical is exact. OK.

## 5. Ground integrity (front-matter claims)

All seven snapshot sha256 values are recorded in `corpus/SOURCES.md` (lines 115-121) and the working-tree snapshots hash to them; the files are also byte-identical at the base rev. Command: `for n in 103 … 109; do git show f3246d1493b60ea1c0d947a19c39f9e08e92f326:.ufo/waves/round-60/snapshots/S$n.page | sha256sum; done; date -u` (read-only):

```
S103 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  -
S104 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e  -
S105 a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  -
S106 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  -
S107 e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2  -
S108 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  -
S109 dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54  -
Fri 23 Oct 2026 07:18:52 PM UTC
```

Checker cross-check: `[PASS] S103…S109 snapshot sha256 recorded in SOURCES.md` (7/7). These are also the values the committed counter checks (it reads snapshots via `git show <rev>:<path>` as bytes and requires sha256 equality, `verifiers/check_scoped_rules.py:147-150`), so v3 measuring against this ground inherits verified bytes.

## Findings by severity

**High:** none. **Medium:** none.

**Low-1 — dead anchor S105 :24 (entry bullet "VS Code (S105)… Local-harness note also lists `CLAUDE.md` [S105 :24,32,64]").** `S105.page:24` is a blank line (line 23 is "Use an instruction format supported by the selected harness."; the Harness table is :25-29, Copilot row :27 — `CensusVSCode.md:21` also anchors the token row at "Line 27"). The claim itself is fully supported by :27/:32/:64 in the same bundle, and no Quote cell is affected, but v3 (or any re-verification keyed on that anchor) should not treat :24 as evidence. Drift class: anchor precision only.

**Info-2 — S105 :164 anchors `applyTo: '**/*.py'` while the `description` example line is :163** ([S105 :27,105,164] bundle for "description matches the task"; the on-demand sentence itself is :105 only; `CensusVSCode.md` scope-key section anchors K=`applyTo` at L=164, so the bundle is census-consistent). No action needed; do not tighten to :163 without also checking the census's own anchoring convention.

**Info-3 — S107 :38-40 lands on the footer-cue sentence + example heading** (entry bundle [S107 :20-35,38-40]; the JIT discovery content is inside :20-35; `SOURCES.md` anchors S107 at `:13-35` and `:94-108`). Loose but same passage; harmless.

**Tooling observation (filed to report_issue):** the grep tool returned "No matches found" for two fully-escaped literal patterns containing `\*\*` on lines where the text exists verbatim (`S105.page:32`, `S106.page:18`); identical plain-substring patterns matched. Evidence above; the byte-exact checker (plain containment, stronger than `grep -F`) is the authoritative proof for those two cells.

## Residual risk / verification gaps

- I did not run `verifiers/check_scoped_rules.py` (that measurement belongs to the L1/v3 lane); "the counter unescapes it" is verified by reading the committed code (`:937 html.unescape`), not by executing the counter.
- Live-page equality (`--fetch`) not re-checked here; ground claim is about committed snapshots, which are hash-pinned at base and in SOURCES.md.
- Census files under `w0/`/`w0b/` were checked at the entry's cited ranges only, not exhaustively.

---
Installs: no installs (pacman guard respected; no tool installed or upgraded).
Blockers: none.
Attacked: the r60 scoped-rules entry — 4/4 Quote cells + all Rule-files tokens byte-verbatim at their documented snapshot lines, all snapshot/census anchors checked, sha256 ground pinned at base; 1 low-severity dead anchor found (S105 :24), no drifting cell.
