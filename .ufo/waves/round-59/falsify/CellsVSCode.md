Result: MIXED — both Events spans and every Hook config/Action citation are supported for the Copilot harness; the entry's quote-shaping note misidentifies the next table row as a heading.

# Scope and evidence identity

Seat: `KotobaR59.CellsVSCode`. Review only: `SKILL.md:129`, the VS Code entry row at `corpus/knowledge/hook-files-round59.md:25`, its note at `:40-43`, and its quote-shaping description at `:63-64`, all at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`. Axis: **depth** (actionable, accurately scoped source detail). Provenance wording also affects calibration; this report does not judge C1 or the round.

Opened the committed S098 page, then its numbered snapshot. Source URL: https://code.visualstudio.com/docs/agent-customization/hooks.md . Snapshot: `.ufo/waves/round-59/snapshots/S098.page`.

Local snapshot review time, command `timeout 30s date -u`, exit 0:

```text
Fri 23 Oct 2026 09:53:18 AM UTC
```

The original fetch metadata is **inherited evidence**, not a fresh HTTP observation by this seat: `corpus/SOURCES.md:110` records 2026-10-23T09:35:04Z, HTTP 200, 15,152 B, sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08`. No network request or runtime hook was run here.

Read-only identity commands, both exit 0, from the lane root:

```sh
timeout 30s git --no-optional-locks rev-parse c63ccc6823e1f6a8577acbb43d19551eadbbee9a:SKILL.md c63ccc6823e1f6a8577acbb43d19551eadbbee9a:corpus/knowledge/hook-files-round59.md c63ccc6823e1f6a8577acbb43d19551eadbbee9a:corpus/SOURCES.md c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/S098.page
timeout 30s git --no-optional-locks hash-object -- SKILL.md corpus/knowledge/hook-files-round59.md corpus/SOURCES.md .ufo/waves/round-59/snapshots/S098.page
```

Each produced the same four lines, in the displayed path order. Thus the numbered local reads describe the assigned commit, not an unpinned later edit:

```text
70f4b46868f35d81e62632bfbab82f6958eba981
d38e14e9b0e38b1ee5376ec5f67871a01ff182d5
0da26d94d31e7cff82fbdc2fe329474240153aa1
74d0bf5838fe7b69c643eac9626639fcc7ae48b8
```

`timeout 30s sha256sum .ufo/waves/round-59/snapshots/S098.page`, exit 0:

```text
98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08  .ufo/waves/round-59/snapshots/S098.page
```

`timeout 30s wc -c .ufo/waves/round-59/snapshots/S098.page`, exit 0:

```text
15152 .ufo/waves/round-59/snapshots/S098.page
```

# Events: HOLDS

Every backticked span in this row's Events cell is ruled below. These are events used as events, not merely identifiers found elsewhere on the page. S098:126 labels the column `Copilot event`.

| Span | Ruling | Exact cited page line |
|---|---|---|
| `preToolUse` | **event** | S098:130, reproduced below |
| `sessionStart` | **event** | S098:128, reproduced below |

S098:130:

```text
| Inspect or make a decision about a tool call | `preToolUse` |
```

S098:128:

```text
| Add context when a session starts or resumes | `sessionStart` |
```

The SKILL order `:130, :128` and the entry note's reversed order `:128,130` both map to the right names. No span is ruled `not an event`; no semantic Events correction is required.

# Hook config and Action: HOLDS within documented scope

The following quotations are contiguous byte-exact source text; no Markdown bytes inside the selections were stripped or normalized. Each quotation is at most 25 words.

1. **Repository-shared `.github/hooks/*.json`: supported.** SKILL's `S098 :58-62` includes the decisive line 59; the entry's `hooks.md:59` is exact:

   ```text
   | Automation shared with a repository | `.github/hooks/*.json` at the repository root |
   ```

2. **Personal sources: supported.** Within the same cited range, S098:58 says:

   ```text
   User hook files in `~/.copilot/hooks/`
   ```

3. **Settings sources: supported.** S098:60 says:

   ```text
   | Hooks alongside other personal or repository settings | An inline `hooks` map in a supported Copilot settings file |
   ```

4. **Plugin sources: supported.** S098:61 links:

   ```text
   [Agent plugins](/docs/agents/reference/agent-plugin-reference.md#hooks-in-plugins)
   ```

5. **Agent-scoped sources exist: supported, not an assertion that every converted agent works.** S098:62 says:

   ```text
   [Agent-scoped hooks](#agent-scoped-hooks), with a current limitation for converted plugin agents
   ```

   The cell and entry assert existence, not universal execution. The limitation matters: S098:163 describes conversion omitting the hooks field from plugin-provided agents; :165 says to retain the original definition and not broaden it into a repository-wide workaround. An unconditional claim that all plugin-agent hooks execute would be overstated, but that claim is not in this row.

6. **Preview: supported.** SKILL's `S098 :4` and the entry's `:4,11` resolve correctly. S098:4 is:

   ```text
   # Configure agent hooks in Visual Studio Code (Preview)
   ```

   S098:11 contains:

   ```text
   The VS Code hooks experience is in Preview.
   ```

   The remainder of line 11 distinguishes individual provider implementations' status and release schedules. The cell does not claim all providers are Preview.

7. **Configuration and scripts are executable code; review before use: supported.** Both artifacts' `:202` citation is exact:

   ```text
   > Hook configuration and scripts are executable code. Review them before use, including hooks bundled in plugins or stored in a shared repository.
   ```

All parenthetical S098 references in the scoped row and per-client note have therefore been checked: `:58-62`, `:130`, `:128`, `:4`, `:202`, `hooks.md:59`, `:4,11`, and `:128,130`. None is unsupported or points at the wrong lines.

# Strongest scope counterexample: not a universal VS Code contract

S098:22 says:

```text
Other session targets use their own hook implementations:
```

Its :24-30 table directs Claude and Codex targets to their own references and distinguishes old Local hooks. The source registry already preserves this boundary in `corpus/SOURCES.md:110`; the short SKILL row and entry note do not explicitly repeat it. A reader choosing VS Code's Claude target cannot infer the Copilot config/event contract merely from the editor name.

**Assessment:** the cited claims hold for the Copilot harness. The page does not establish those same claims for every VS Code Session Target. Treating the row as universal would be an overstatement, not a different event ruling. Smallest safe hardening: add `Copilot harness;` to the existing Hook config parenthetical and start the entry note's first claim with `For the Copilot harness,`. Keep the client key `VS Code`, path, Events spans, quotes, and frozen counter unchanged.

# Concrete entry defect: BREAKS quote-structure description

`corpus/knowledge/hook-files-round59.md:63` calls S098:59-60 “a table row and the next heading.” The exact next line is the **settings table row**, reproduced in item 3 above, not a heading. The entry's quote at :25 borrows its trailing `Hooks` from that adjacent row. Folding :59-60 to spaces and encoding the three literal pipe bytes explains the recorded fragment; it does not make :60 a heading.

This is a **fixable provenance-description defect**, not a false location claim or a reason to change the frozen predicate. Smallest correction: replace `a table row and the next heading` with `two consecutive table rows` at entry :63. Keep the quoted bytes and the stated folding/pipe encoding unchanged. The repo-shared location is independently supported by :59, so this correction does not remove the row's substantive support.

# No-harm after-column and limits

- After the two narrow wording corrections above, both true event names, every location/status/security citation, the path token, and the vendor/runtime-test distinction remain unchanged.
- No evidence here warrants changing the counter, targets, row rule, lane identity, or source authority. Frozen `TARGET = 4`, `NEW_TARGET = 5` were read at `verifiers/check_hook_files.py:253-254`.
- Read-only command `timeout 30s git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:verifiers/check_hook_files.py | timeout 30s sha256sum`, exit 0, printed `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -`.
- No counter, mutation, build, test, linter, formatter, hook command, or alternate runtime was executed. No sandbox was needed for read-only inspection. Only this report was written; lane artifacts were not edited. Tools installed or updated: none.

Report: `.ufo/waves/round-59/falsify/CellsVSCode.md`
