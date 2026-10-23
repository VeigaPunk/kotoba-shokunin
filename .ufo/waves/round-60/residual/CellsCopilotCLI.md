Result: HOLDS — Copilot CLI: all three cells of SKILL.md:144 say what S106 says, the entry row's quote is byte-exact against `S106.page:18` under its one declared pipe escape, and the quote counts 10 words.

Seat `CellsCopilotCLI` · revision audited `7b80ae80cda69a95b6fc90879395113a99a57912` · 2026-10-23 · lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only; every read below is of committed tip bytes — the lane working tree is dirty only in `PROVINCE.md`, `SHONEN.md`, `corpus/README.md` plus untracked round-60 artifacts, none of them an audited file; `git --no-optional-locks rev-parse master` → `7b80ae8…`, `git --no-optional-locks diff --stat 7b80ae8… master` → empty).

Evidence base: committed snapshot `.ufo/waves/round-60/snapshots/S106.page`, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`, 8,730 B (`sha256sum` + `wc -c`, exit 0) — byte-identical to the sha256 and byte count recorded in `corpus/SOURCES.md` row S106 and the Gate row `corpus/lessons/round-60.md:13` (fetched 2026-10-23T12:08:47Z, HTTP 200).

## Row audited — SKILL.md:144

```
| Copilot CLI | `.github/instructions/**/*.instructions.md` (modular repository instruction files, S106 :18) | `applyTo` (e.g. `app/models/**/*.rb`, S106 :66) | Create a path-specific instruction file with an `applyTo` glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60). |
```

Citations in the row: `S106 :18`, `S106 :66`, `S106 :60` — all three resolve to real lines of the committed snapshot (byte-exact pastes below).

## Cell 1 — Rule files: `.github/instructions/**/*.instructions.md` (modular repository instruction files, S106 :18) — HOLDS

Cited line, bytes from the committed snapshot (repr):

```
S106.page:18 = '| `.github/instructions/**/*.instructions.md`              | Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         |'
```

- The token is the Location-column entry of the page's "Types of custom instructions" table (`S106.page:13-22`) for "Modular repository instructions" — a named location, not an example file. The page's example files are `NAME.instructions.md` (`S106.page:58`).
- The page binds that location to matching-file scope: `S106.page:11` — "Modular instruction files (those matching `*.instructions.md`) are path-specific—a file with an `applyTo` value applies only to matching files."
- The page also names a user-level modular location `$HOME/.copilot/instructions/**/*.instructions.md` (`S106.page:16`). The row names the repository one; the knowledge entry's per-client note (`corpus/knowledge/scoped-rules-round60.md`, Copilot CLI bullet) records the user-level folder separately as applying across sessions, citing `RecensusCopilotCLI.md:115`. No defect: the scoped-rule row carries the location whose matching-path behavior the page states.

## Cell 2 — Scope key: `applyTo` (e.g. `app/models/**/*.rb`, S106 :66) — HOLDS

Cited lines, bytes:

```
S106.page:32 = 'Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with. An instruction file that you disable using `/instructions` is not included.'
S106.page:66 = '   applyTo: "app/models/**/*.rb"'
```

- `applyTo` is the key the page states limits the file to matching files (`:11` "applies only to matching files"; `:32` "included only when their `applyTo` value matches a file that Copilot CLI is working with"). The cited example line `:66` is exactly `applyTo: "app/models/**/*.rb"`.
- Not a wrong key: the only other frontmatter key the page documents is `excludeAgent` (`S106.page:88,99`), and it excludes agent runtimes ("code-review" / "cloud-agent"), not files. `alwaysApply` and `description` never occur anywhere in S106 (case-insensitive grep over all 110 lines: no hit; "frontmatter" occurs only at `:60`, `:70`, `:88`, `:99` around those two keys). There is no `name` frontmatter key on this page.

## Cell 3 — Action — HOLDS (two cosmetic notes; no correction required)

Cited line, bytes:

```
S106.page:60 = '4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.'
```

- The Action's second clause — "use glob syntax to specify the files or directories the instructions apply to" — is the cited line's own instruction ("Use glob syntax to specify what files or directories the instructions apply to"); only "what"→"the" differs. Not inverted, not invented.
- The Action's first clause — "Create a path-specific instruction file with an `applyTo` glob" — summarizes the same documented procedure: section heading `S106.page:52` "## Creating path-specific custom instructions", create the `.github/instructions` directory `:54`, create `NAME.instructions.md` files `:58`, add the `applyTo` frontmatter `:60`. The SOURCES row S106 scopes exactly this section ("§ Creating path-specific custom instructions (`:52-60`)"). Nothing the page does not say; no meaning inverted.
- Note 1 (citation span, minor): the first clause rests on `:52-58` in addition to `:60`; the single-line anchor under-covers it. The operative glob-syntax sentence is on `:60`, so the plan's A1 Action test is satisfied; I record the span as a note, not a defect.
- Note 2 (layout, cosmetic): the row ends `(S106 :60).` with the period after the citation, while sibling rows keep it inside (e.g. SKILL.md:141 `…apply only when matching specified patterns. (S103 :194)`).
- Exact corrected cell, offered only if the L1 wants the span tightened (semantic content unchanged):

```
| Copilot CLI | `.github/instructions/**/*.instructions.md` (modular repository instruction files, S106 :18) | `applyTo` (e.g. `app/models/**/*.rb`, S106 :66) | Create a path-specific instruction file with an `applyTo` glob; use glob syntax to specify the files or directories the instructions apply to (S106 :52-60) |
```

## Entry row quote — byte-exact; 10 words

- The entry table row (`corpus/knowledge/scoped-rules-round60.md`, the single `| Copilot CLI |` row) has Quote cell:

```
`.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations
```

  Compared against the committed snapshot blob: it is the contiguous slice of `S106.page:18` from the token's opening backtick through `locations`, with exactly one declared shaping step — the table pipe written `&#124;` — and the source's run of spaces kept. Program comparison over `git show` blobs: `BYTE-EXACT (after declared pipe-escape only): True` (exit 0; no other byte differs, lengths equal).
- The shaping note in the entry ("Quote shaping (per row)", S106 bullet) declares precisely this transformation, and the Gate row `corpus/lessons/round-60.md:13` records the same quote with the declared pipe escape. All three artifacts agree with the snapshot bytes.
- Word count: `wc -w` on the Quote cell → `10` (identical whether the pipe is escaped or not). No word count is stated for this quote in the entry, the Gate row, or `plans/round-60.md` (swept all three for "word"/"wc -w"; the only stated word-count items in the plan concern the round-59 Gemini 29-vs-25 correction and the M86 lesson class). The stated bound that applies is the plan's quote rule "6–25 words" (`plans/round-60.md:82`) — 10 is inside it, the quote contains the token case-sensitively, and it matches `(rules?|instructions?)` outside the token span ("Modular repository instructions, discovered…"). M86 (a stated count must carry its command) is not triggered: no count is stated for this quote.

## Corroboration of the knowledge entry's Copilot CLI note

Its citations `[S106 :18,32,66]` and `[S106 :17]` all resolve: `:18` types-table row (pasted above), `:32` applyTo-match sentence (pasted above), `:66` example (pasted above), `:17` = `| \`.github/copilot-instructions.md\` … | Repository-wide instructions, discovered in the standard locations. |` — the separate repository-wide scope the note names. No anchor error.

## Residual risk and verification gaps

- I audited the committed snapshot, not the live page: no re-fetch was run this seat. Freshness rests on the round-60 fetch record (2026-10-23T12:08:47Z, HTTP 200, 8,730 B, sha256 `00e45ea5…`), which the snapshot matches byte-for-byte; a docs edit after that fetch would not be visible here. The plan's reject table records the `enterprise-cloud@latest` rendering (8,826 B) as rejected, consistent with the base-page choice.
- Per the plan's own limit (`plans/round-60.md:62-64`): a cell built from the cited line's words can still invert meaning, and that reading belongs to the Cells seats — this report is that semantic reading; the counter v2 (frozen sha `ca2585a4…`) was not run by this seat and is supporting evidence only (Erratum E2).
- The `paths`-style always/description/manual typology check (Claude Code/Cursor rows) is out of my scope; for Copilot CLI the page documents no such alternative rule types — the only per-file selector is `applyTo` and the only other frontmatter key is `excludeAgent`.
- No tool was installed or upgraded by this seat; all commands were read-only (`git --no-optional-locks`, `sha256sum`, `wc`, `grep` tool, python over `git show` blobs) with `timeout` caps.
