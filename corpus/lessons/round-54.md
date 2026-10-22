# Round 54 — lessons (kotoba, hyaku campaign, attempt 1)

Base `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`; plan and frozen counters `e33715486a45a4a857b64c30e6b695f7995858b8`;
errata `d051ec40225a2cf330e45348eaf755a9877f5745` (times), `3b2535d28f2665fc4931f02ae58bae7ca01b0c9f` (C2),
`90cae9af3db5fc213b1a62162912d9ed8f5c68e9` (C1), each before the content it bounds. Claims: C1 depth (description
thresholds by client; the learning and sourced claim), C2 consistency (gate registry rows). Seat reports:
`.ufo/waves/round-54/build/` (40 seats) and `.ufo/waves/round-54/falsify/`.

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M45 | `append-only-breach` | `corpus/SOURCES.md` rows were rewritten in place across commits. `CORPUS.md:116` (contract v1 rule 2) lets only `status`, `recheck` and `used-by` change in place and requires a correction to be a new row opening `supersedes S0NN —`. Routed instance: `e792607e` rewrote S050's `anchor` cell, "…at commit `cfb894a5`…" → "…at zed-industries/zed@`cfb894a5`…", to clear the lane gate's `commit_unresolvable` reading; the round-53 lesson discloses it and names the rule (`corpus/lessons/round-53.md:43-46`) and the outside spot-check routed it (`corpus/lessons/round-53-verifier-spotcheck.md:192`). The same scan finds 12 more protected-cell changes in 3 earlier commits, none filed as a breach: `bfd5a583a` S022 `teaches`; `542f51567` S019 `scope`, `anchor`, `teaches` and S022 `scope`, `anchor`, `teaches`; `bf109cacc` S019 `teaches`, S022 `teaches`, S026 `scope`, `teaches`, S028 `teaches` — 13 changes in 4 of 16 commits from the file's creation to `7ad05d34`. Round 49's summary says "No other row" moved (`corpus/lessons/round-49.md:50`); round 50's says the cells "gain anchor, scope and teaches text" and "No other row moved" (`corpus/lessons/round-50.md:76-78`), which discloses the cells as an ordinary gain; round 51 refused the same edit and cited the rule (`corpus/lessons/round-51.md:65`). | none — no criterion governs SOURCES.md history and no instrument reads it: no verifier runs `git rev-list` or `git log` (nine read a revision's bytes with `git show`, most in the `git(repo, "show", …)` form that a literal `grep 'git show'` misses, which first gave four; none compares a row against its parent; falsify `W2CriticLesson`), `scripts/sources-census.sh` makes 0 `git` calls, and the corpus's one append-only test records "no removed row" from a `git diff` piped through `grep` for removed lines (`corpus/lessons/round-52-verifier-spotcheck.md:30`), which flags every in-place change as a removed line, permitted `status`/`used-by` moves included (`55973a20`: 2, `a78fec1ff`: 8), so it cannot separate a protected-cell rewrite from a permitted one, and was run on round 52's range only (corrected by `W2CriticLesson`; first written "cannot tell a rewritten row from an appended one") | `verifiers/check_sources_append_only.py` (landed `bf65974c`, byte-identical to the seat draft, 189 lines, sha256 `d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`): walks `--base..--rev`, parses every registry row at each commit and its parent, exits 1 on a protected-cell change or a dropped row. Arms: red `--base 55973a20 --rev e792607e` → `breach e792607e8 S050 anchor: …at commit \`cfb894a5\`… -> …at zed-industries/zed@\`cfb894a5\`…`, `1 change(s) in 1 of 1 commits`, exit 1; green `--base 55973a20 --rev e792607e^` → clean, exit 0; green on a populated range that edits the file `--base 34cfffbb --rev 55973a20` → 4 commits scanned, 0 changes, exit 0; `--self-test` → 0 failure(s) over 14 assertions, including a must-fail `anchor in place` arm. Landed without a disposition of the 12 earlier changes: they are carried (§ Rows touched) and go to the operator as an L0 question (ratify, or one superseding row each); until then the gate is red from the file's root (`--rev 58db81c4` → `13 change(s) in 4 of 17 commits`, exit 1) and its registry entry command pins `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`. Registry row added (M 23 → 24). |
| M46 | `overclaim` (times) | The round-54 plan `e3371548` stated its before-values were measured at 21:30Z–21:32Z; its own committer time is 21:12:08Z and the runs were at 21:08–21:11Z (`.ufo/waves/round-54/build/ScribeMistake.md` § 2.2). The L1 wrote the times ahead of the clock. | Q19 (re-measure before-values) — it binds the values, not the stamps; no gate reads plan times | Erratum `d051ec40` before any content. Fix as practice: the L1 pastes the `date -u` line printed with each before-run instead of typing a time. Not shown able to fail mechanically, so it is recorded, not counted as a fix. |
| M47 | `unregistered-gate` | Four gates had no self-test (`box_proof_case_deletion.py`, `check_alwayson_boxes.py`, `check_callee_rename.py`, `check_opencode_repin.py`: each exits 2 on `--self-test` at `7ad05d34`), against PROTOCOL.md § Gate standard Self-test; the lane had no registry, so no one compared. Found by seats `RegCheckCalleeRename`, `RegBoxProofCaseDeletion`, `RegCheckAlwaysonBoxes`, `RegCheckOpencodeRepin` and critic `CriticC2Sizing`. | none before round 54 | Self-tests landed `b55550b9` (judging unchanged); `verifiers/check_gate_registry.py` now fails a `gate` row with `none` self-test (shown able to fail: its self-test arm `gate with self-test none` expects the row rejected, and the round-54 sandbox run of the honest pre-patch registry printed 19 of 23, `CriticC2Sizing`). Its flag test is a substring test (CriticC2Sizing, ReviewCounters F5), so a borrowed flag still passes; the plan's erratum 2 guard covers the four rows. |

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S053 | https://code.claude.com/docs/en/skills.md | 2026-10-22T21:15:56Z | 111,928 B, `d1359f0c…` | "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" | `skills.md:389` | SrcClaudeCode |
| S054 | https://learn.chatgpt.com/docs/build-skills.md | 2026-10-22T21:15:49Z | 11,035 B, `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" | `build-skills.md:38-39` | SrcCodex |
| S055 | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T21:15:47Z | 22,871 B, `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` | "help Copilot decide when to load the skill. Maximum 1024 characters." | `agent-skills.md:148` | SrcVSCode |
| S056 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T21:18:03Z | 461,944 B, sha256 c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | SrcCopilotCLI |
| S057 | https://geminicli.com/docs/cli/skills-best-practices.md | 2026-10-22T21:16:27Z | 3,257 B, sha256 612c3b83… | "Metadata (name + description): Always in context (~100 words)." | `skills-best-practices.md:24` | SrcGeminiCLI |
| S058 | https://cursor.com/docs/release-notes.md | 2026-10-22T21:19:23Z | 301,193 B, sha256 fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd | "Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters" | `release-notes.md:122` | SrcCursor |
| S059 | https://opencode.ai/docs/skills.md | 2026-10-22T21:15:53Z | 5,365 B, `f10ced73971c…` | "`description` must be 1-1024 characters." | `skills.md:72` | Srcopencode |
| S060 | google-gemini/gemini-cli `docs/cli/gemini-md.md` at `451a02ff` (raw), re-opened at main and on the served docs page | 2026-10-22T21:16:17Z (main 21:16:21Z; served 21:16:26Z, re-fetched 21:17:28Z) | pinned 200, 3,807 B, sha256 `d00eeaef…`; served 200, 3,816 B, sha256 `e5fbfd6d…` | "To specify a different name or a list of names, use the `context.fileName` property." (14 words); `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` (4 words); "You can break down large `GEMINI.md` files into smaller, more manageable components by importing content from other files using the `@file.md` syntax." (22 words) | `gemini-md.md:97-98`, `:105`, `:73-74`; default at `:3`, `:96` | ScribeS046Fix |
| S061 | https://zed.dev/docs/ai/instructions.md | 2026-10-22T21:16:10Z (source tree re-fetched 21:16:44Z; 8-character form 21:17:27Z) | 3,169 B, `7c63efe0…` (source 3,256 B, `1bc6e312…`) | "Project instruction files apply to the current project. Zed uses the first matching file in this list:" | `instructions.md:25` | ScribeS050Fix; correction row for the in-place S050 anchor edit of `e792607e` |
| S062 | https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md | 2026-10-22T21:19:52Z | 1,070,244 B, `121129bc…` | "raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions are truncated" | `CHANGELOG.md:6409`, § 2.1.105 | SrcClaudeCode |
| S063 | https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-10-22T21:16:19Z | 136,297 B, `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` | "Token budget for the available-skills catalog. Defaults to 2% of the model's context window. Explicit values are capped at `10000` tokens." | `config-reference.md:378` | SrcCodex |
| S064 | https://opencode.ai/v2/docs/skills | 2026-10-22T21:16:53Z | 32,694 B, `243e88907fcb…` | "V2 currently does not enforce this pattern, the 1–64 character recommendation, a match between `name` and the directory, or a maximum description length." | `services/www/src/docs/content/skills.mdx:160` | Srcopencode |

### Rejected (opened this round, not admitted)

| source | opened | reason | flip |
|---|---|---|---|
| `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills.md` | 2026-10-22T21:06Z (L1 screen) | HTTP 404, 502 B: no page at that route, so nothing to quote | a live route for the concept page |
| `https://cursor.com/changelog.md` | 2026-10-22 (seat `SrcCursor`, F5) | served HTML with 0 bytes of "skill"; the skill-limit sentence is on `release-notes.md:122` (S058) instead, so this route would record a false silence | server-rendered changelog entries |
| GitHub Copilot CLI plugin reference, `cli-plugin-reference.md:195,349` `Max 1024 chars` (seat `SrcCopilotCLI`) | 2026-10-22 | the caps are on plugin manifest and marketplace metadata, not on a skill's `description`; admitting them would count a number in another sense (`plans/round-54.md` erratum 3) | a page that ties the plugin cap to skill descriptions |

### Rows touched (old → new)

- S046 (round-53 spot-check routed defect 2): `used-by` `corpus/knowledge/alwayson-rule-files-round53.md` →
  `corpus/knowledge/alwayson-rule-files-round53.md, corpus/lessons/round-54.md`; status `mined` → `mined`; recheck
  unchanged. S060 supersedes S046's `teaches` cell only: the pinned bytes and the served page say "To specify a
  different name or a list of names, use the `context.fileName` property." and contain no "replaces"
  (`grep -o -i replac` → 0 hits on both; seat `ScribeS046Fix`).
- S050 (routed defect 3): not edited. Commit `e792607e` rewrote S050's `anchor` cell in place ("… at commit
  `cfb894a5` (frontmatter only differs)" → "… at zed-industries/zed@`cfb894a5` (frontmatter only differs)"),
  which contract rule 2 does not allow; S061 records the correction append-only and bounds its teach to a
  17-word quote; the parenthetical "frontmatter only differs" is false (the served page also adds a navigation
  line, seat `ScribeS050Fix`) and stays in S050 as a recorded, unfixed cell. M45's gate finds 12 more
  protected-cell changes in `bfd5a583a`, `542f51567`, `bf109cacc`; they are carried, not corrected this round.
- New IDs: seat drafts `S053b`, `S054b`, `S059b` were renumbered S062, S063, S064 (the contract's id is `S` and
  three or more digits).

## Routed defects from the round-53 spot-check

1. Drift sentinel: this round works the Frontier row *Per-render consumption* and makes no freshness claim and no
   claim on `verify_surfaces.py` or the checklist/always-on row. Recorded for the closure: round 53's C1 was the
   third consecutive freshness claim on `verify_surfaces.py`, and the round-51/52 tie-break reading (adjacency)
   was reversed in round 53 without a note.
2. S046 "replaces": S060 (above).
3. S050 in-place edit: S061 and M45, with `verifiers/check_sources_append_only.py` (red on `e792607e`).
4. Gate registry rows: C2, `SKILL.md` § Gate registry (24 rows at `bf65974c`).
5. Tip runs committed with revisions: `.ufo/waves/round-54/build/ExecTipRuns.md` (corpus integrity, independent,
   floors, checklist, finding delta with base pinned to `422ffd10`, at `7ad05d34` and at `b38c32a0`; floors at
   `b38c32a0` show `surfaces 175/175`). `LOG.md` gains the missing `e5355a62`.
6. `baseline.json` `opencode_round53_note` cites `strings -n 4 <binary> | sha256sum` (reproduces `2d72d83f…`)
   instead of the deleted scratch dump: `fed56863`, no pin value changed.
7. Carried as listed by the closure.
