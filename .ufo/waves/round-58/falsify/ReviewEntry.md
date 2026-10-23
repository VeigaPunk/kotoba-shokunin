Result: MIXED — every row, quote and citation in `corpus/knowledge/command-files-round58.md` verifies against byte-identical re-fetched sources, but the row-rule prose contradicts the Gemini row it describes, and two provenance claims ("no other byte is changed", "every quote is copied from the fetched bytes") are false as written.

Seat: ReviewEntry. Target: `corpus/knowledge/command-files-round58.md` at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` (unchanged at tip `8e52f064`; the tip adds only `.ufo/waves/round-58/C1-measure.txt`, `noharm-tip.txt`, and 3 `corpus/README.md` rows — `git diff --stat` confirms).

## Verification method

Re-fetched all eight cited URLs on 2026-10-23 into `/fast/scratch/hyaku/kotoba-r58/ReviewEntry/src/` (`date -u`: `Fri 23 Oct 2026 08:28:31 AM UTC`; all HTTP 200). Every sha256 is byte-identical to the seat-recorded hash: S089 `6b070e87…` (SrcClaudeCode), S090 `d6f7cf8d…` (SrcCodex), S091 `4ad1b2bc…` (SrcVSCode), S093 `8f3295e8…` (SrcGeminiCLI), S094 `7ceb6578…` + supporting `customize-cursor.md` `9ae0878d…` (SrcCursor), S095 `dda6bba0…` (Srcopencode), S028 `d0d362cc…` (SrcCopilotCLI). The seat reports' quoted bytes and fetch metadata are therefore reproduced, not just asserted. Counter behaviour cited from `verifiers/check_command_files.py` (frozen at `3de87aad`, read at content rev). Frozen rule/census cited from `plans/round-58.md:24-71`.

## Findings by severity

### F1 — Row-rule prose contradicts the Gemini row it claims to describe (correctness; the entry misstates its own applied rule)

Entry :23-25: the Command files cell leads with "**the project folder where both a project and a user folder exist**, else the only one documented". S093 (`custom-commands.md:8-17`, my fetched bytes) names **both**: user `~/.gemini/commands/` (:12) and project `<your-project-root>/.gemini/commands/` (:14-16). The Gemini row (:38) leads with the **user** folder `~/.gemini/commands/`. Under the stated rule the cell would lead `.gemini/commands` (project form). The row actually follows the frozen census token — `plans/round-58.md:61` records Gemini's eligible token as `~/.gemini/commands/` — so the table is right and the prose is wrong. opencode *does* lead project (:40), so the rule holds for exactly the one client where it happens to coincide with the census pick. The stated rule also fails to cover VS Code: its user location is not a folder at all ("Your user data (specific to your VS Code profile)", `prompt-files.md:26`), yet `.github/prompts` is neither "the project folder where both exist" nor "the only one documented". Correction text for L1: name the real rule — the census-recorded eligible token for the client, the page's named user-writable folder. Q26-adjacent: the rule's headline asserts a selection the table does not apply.

### F2 — "no other byte is changed" is false for the VS Code quote (provenance accuracy)

Entry :29-30: "the VS Code quote spans a Markdown table (`prompt-files.md:21-25`), so its table pipes are written as `&#124;` to keep them inside one cell — **no other byte is changed**". The source span :21-25 is five lines; every newline byte inside the quoted span — after `files.`, after each table row, plus the blank line :22 — was folded to a single space. The seat report discloses this correctly ("line breaks are collapsed to spaces", `SrcVSCode.md:6`); the entry's claim is contradicted by its own evidence. The stored quote is not a byte-substring of the fetched page (it is a whitespace-normalised one — sufficient for the counter, whose `page_plain` folds whitespace, `check_command_files.py:824-829`, but not what the sentence claims). Correction: "...`&#124;` to keep them inside one cell, and the line breaks in the span are folded to spaces".

### F3 — "every quote is copied from the fetched bytes" overstates; two more quote-shapings are undisclosed (provenance accuracy, same sentence group)

Entry :28: "every quote is copied from the fetched bytes". Two of the six row quotes carry stripped source bytes the notes never mention:
- S089 (:35): the fetched line begins `* **Command files**:…` (`slash-commands.md:172`); the stored quote drops the leading `* ` list-marker bytes. Disclosed in `SrcClaudeCode.md:14`, absent from the entry (the seat called it outside-the-quote trimming; either way the blanket "copied" claim needs it named).
- S093 (:38): source `custom-commands.md:12-13` reads `These commands\n    are available` — the newline plus four-indent bytes were folded to one space. The note only says the quote "keeps the page's list marker `1.` and bold markers" (:30); it is silent on the fold. (`SrcGeminiCLI.md:6` discloses it.)
After F2, 3 of 6 quotes carry an undisclosed whitespace/marker transformation; two are disclosed in seat reports but not propagated into the note that claims byte fidelity.

### F4 — Lead "invokes by typing `/name`" over-generalises for the admitted population (Q26 calibration; minor)

Entry :9: a custom command "is a file the user writes once and invokes by typing `/name`". Codex invokes `/prompts:draftpr` (`custom-prompts.md:34`, and the entry's own bullet :47 records it); Gemini namespaced commands are `/dir:name` (`custom-commands.md:29-31`). The generic `/name` holds for Claude Code, VS Code, Cursor, opencode. The row bullets carry the correct per-client form, so the damage is a lead sentence claiming a uniform invocation the table itself refines. Same colour: "the model does not choose it from a description, the user types it" (:10-11) — the typed half is sourced on every page (S090:10 "require explicit invocation"; S091:40; S094b:31; S095:32), but no command page states the no-description-selection contrast; that half is corpus skill-knowledge, not S###-sourced. Defensible as a surface definition; strictly, beyond these pages' evidence.

### F5 — Minor citation imprecisions (lowest)

- :50-51 `${input:…}` cited `:69-70`; the syntax is documented on line 70 only (`prompt-files.md:70`); line 69 is the unrelated `#tool:` sentence. In-range but padded.
- :51 "user-level files live in the profile folder" — the page says "Your user data (specific to your VS Code profile)" (:26), explicitly not a filesystem path (SrcVSCode.md:8). "Profile folder" is a fair but slightly load-bearing paraphrase.
- :55 Cursor bullet: `(customize-cursor.md:31, supporting page in the S094 row)` — `customize-cursor.md` supports "Markdown files … workflow" (:31, verified) but never names `.cursor/commands` (grep: no `.cursor` string on the page); the "in the project folder" half is only `deeplinks.md:54`. The parenthetical does call it "supporting", so this is placement ambiguity rather than an error.
- :64-68 Limits Q31 bullet enumerates what the counter reads but omits that `--fetch`/G also reads base-revision blobs (`git ls-tree -r -z` + `cat-file`, `.ufo/` skipped — `check_command_files.py:944-961,1041`). The enumeration is presented as complete ("reads the … cells, this table, the SOURCES rows and the lesson `## Gate`, and with `--fetch` the live page"); one sentence more would close it. Otherwise Q31-clean: it names only cells the code parses and correctly flags `What a file sets` as unread (`:782-784` confirms the action cell is word-counted only).

### F6 — Spillover observation (not in my file; reported because it touches the row my file describes)

`SKILL.md:116` Copilot CLI Command files cell contains a backticked span — `` `:456` `` in the citation "(S028 `:456`)". The seat design required **no** backticked span in that cell (`SrcCopilotCLI.md:9`: "The `Command files` cell deliberately contains no backticked span"), because the counter takes the first backtick as the token (`check_command_files.py:762-764`). `:456` is malformed → Copilot stays outside K and "6 of 6" stands, but the row is one plausible future edit (a backticked path-shaped string) away from entering K and failing — and it contradicts the recorded design intent. For the L1's row-owner.

## Per-sentence-group verdicts (sourced by which S###)

| Group (entry lines) | Verdict | Evidence |
|---|---|---|
| Front matter `source:` (:2) | OK | Lists exactly the 7 used sources; correctly drops the `S092`/`cli-command-reference` that `ScribeEntry.md`'s draft front matter carried. |
| `verified-at`, `recheck` (:3-4) | OK | All fetches 2026-10-23 (seat UTC + my re-fetch); recheck matches frozen invocation (`plans/round-58.md:32`). |
| Lead definition (:9-11) | Mostly OK | Naming verified (S091 title/`prompt.md`, S090 title); `/name` and description-contrast over-general — F4. |
| "records … opened on 2026-10-23; vendor documentation, no client was run" (:11-13) | OK | Byte-identical re-fetch; S028 re-opened 2026-10-23 per `SrcCopilotCLI.md:38`. |
| "Three clients point authors … to skills" (:15-18) | OK | S089:17 (merged, prefer skill — fuller quote than :172), S090:5-8, S091:17. Residual: Cursor's help page also documents `/migrate-to-skills` (`SrcCursor.md:18`) — outside S094's pages, so the count as enumerated holds. |
| Claude "older format/still works" (:15-16) | OK* | Verbatim substring at `slash-commands.md:172` minus `* ` marker — see F3. |
| Copilot "no command folder of its own" (:18-21) | OK* | Quote verbatim at `s028.md:456` (inside ASCII box); `com.github.copilot/commands/` is Agent Plugins 1.0-only (:154-164) = plugin path. The absence claim rests on the W0/SrcCopilotCLI sweep; that sweep's docs-source-tree leg is admittedly partial (served routes, not the repo tree — `SrcCopilotCLI.md:26`), so `documents no own folder` carries a small evidence gap, within tolerance. |
| Row rule (:23-27) | BREAKS | F1 — prose contradicts the Gemini row; also chronology clause ✓ (rule fixed in `8db2070`, targets frozen `3de87aa`, rows written `46b4a70`; "census before targets" ✓ `plans/round-58.md:52`). |
| "already named in this corpus" (:27) | OK | `instruction-surface-census-round13.md:102-103` names `.github/prompts/` and `~/.codex/prompts`; matches frozen G accounting (`plans/round-58.md:65-68`). |
| Quote notes (:28-31) | BREAKS | F2, F3 — byte-fidelity claims contradicted by seat disclosures. The opencode `Accept: text/markdown` note (:31) verified: plain GET → `text/html`, `Accept: text/markdown` → `text/markdown` (my curl, 2026-10-23); frozen `fetch()` sends only `User-Agent` (`check_command_files.py:914-915`), so the pinned-URL choice is necessary and correct. |
| Table rows (:35-40) | OK | All six quotes verified against my byte-identical fetches at the cited lines (S089:172, S090:62, S091:21-25, S093:12-13, S094:54, S095:21); tokens on-page; each row leads the folder its page names. |
| Per-client bullets (:44-59) | OK | Claude :450/:378/:402-403 all verified verbatim; Codex :10/:18,34/:40-41/:42 verified; VS Code :35/:39-44/:40/:70 verified; Gemini :41-42/:45-53/:25-27/:58-67/:8-17 verified; Cursor verified modulo F5 cite placement + both pages grep-clean of any file frontmatter/argument schema; opencode :28/:37/:99/:21 verified. |
| Limits (:63-68) | OK | No-run honesty consistent; precedence clause matches S028:456 (the only command-vs-skill precedence stated); Q31 bullet verified against counter code modulo F5 base-blob omission. |

## Residual risk and verification gaps

- The F1 row-rule defect is prose-only; no measured cell changes, C1 predicate unaffected (the counter never reads the rule paragraph). F2/F3 are likewise provenance-note defects: the stored quotes still satisfy `found_on_page` (its `page_plain` folds the very whitespace the notes failed to disclose) — the seats' `True` probes are unaffected.
- I verified seat `True` claims by reproducing identical page bytes and confirming each quote/token occurs at the cited line; I did not re-run `found_on_page` myself (no counter execution needed — the byte identity plus seat transcripts is the evidence; [INFERENCE] that normalization behaves as the seats measured is backed by `page_plain`/`norm_page` code reading).
- Cursor user-level commands: neither fetched page names one; the entry correctly claims only what the pages say.
- No tools installed. All lane access read-only; fetches landed in `/fast/scratch/hyaku/kotoba-r58/ReviewEntry/src/`; this report is the only lane file written.
