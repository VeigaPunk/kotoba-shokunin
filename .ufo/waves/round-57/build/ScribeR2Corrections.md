Result: DONE — R2 corrections are drafted as append-only notes; no counted quote or SOURCES cell is changed.

# Scope and revision

The read-only command `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` exited 0 and printed current HEAD `27af04a7ed8cee74291fd8237f5c73c43243ce02`. The following command returned exit 0 with no diff, establishing that the three cited surfaces have identical bytes at the assigned work revision and the observed HEAD:

```text
timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --quiet 01312a77e36317feb6e961aba77841ddab1225ca 27af04a7ed8cee74291fd8237f5c73c43243ce02 -- SKILL.md corpus/knowledge/agent-definition-files-round56.md corpus/lessons/round-56.md
exit 0 (no output)
```

The line references below are therefore for `01312a77e36317feb6e961aba77841ddab1225ca`. I read the round-56 spot-check §2 and §7 R2, both requested falsifier findings, the three target surfaces, `corpus/QUALITY.md`, and the lesson correction precedents. I made no product, lesson, SOURCES, or verifier edits; this report is the only deliverable written.

# Findings and proposed text

## 1. S076 — Gemini CLI quote note

**Evidence.** `corpus/lessons/round-56-verifier-spotcheck.md:107-122,217-228` routes the note and prefers the project-line quote. `ReopenS076S077.md:179-190` (Finding 3) records that the knowledge entry at `corpus/knowledge/agent-definition-files-round56.md:25,35-37` quotes the user-level line (`subagents.md:324`) while the project path is at `:323`. The re-open receipt at `ReopenS076S077.md:29-39` records `https://geminicli.com/docs/core/subagents.md`, HTTP 200, 23,614 bytes, SHA-256 `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db`, opened `2026-10-23T03:07:42Z`. `:186-188` gives the byte-exact project and user lines and the 24-word `:320-323` alternative.

**Old → corrected wording** (the quoted text below is note text, not the counted table quote):

- `corpus/knowledge/agent-definition-files-round56.md:35-37`
  - Old: `S076's quote is the user-level line; the project-level line `.gemini/agents/*.md` is the line before it (`subagents.md:323`) and holds no agent word.`
  - New: `S076's recorded quote at `subagents.md:324` is the user-level path and directly witnesses `~/.gemini/agents/*.md`; it supports the project token `.gemini/agents/*.md` only by substring matching. The project path is stated at `:323`; the 24-word span at `:320-323` directly witnesses it and is preferable if a later round elects to replace the counted quote.`
- `corpus/lessons/round-56.md:23-24`
  - Old: `S076's quote is the user-level line (the project line :323 holds no agent word);`
  - New: `S076's recorded quote at `subagents.md:324` directly states the user-level path; the project token `.gemini/agents/*.md` is supported only through substring matching. The project path itself is at `:323`; the direct 24-word span `:320-323` is preferable if a later round changes the counted quote.`

**Append-only action:** Do not rewrite the historical lesson. In the current knowledge entry, preserve the old note and append this correction within its existing `Quote notes:` paragraph at `corpus/knowledge/agent-definition-files-round56.md:39` (the blank line before `## Findings`):

```text
Round-57 correction (R2): S076's recorded quote at `subagents.md:324` is the user-level path and directly states `~/.gemini/agents/*.md`; it supports the project token `.gemini/agents/*.md` only by substring matching. The project path is at `:323`; the 24-word span `:320-323` directly witnesses it and is preferable if a later round elects to replace the counted quote.
```

The suggested future quote is not a request to change the S076 quote cell now. The entry table (`:25`) and round-56 Gate quote (`round-56.md:18`) remain byte-for-byte unchanged.

## 2. S078 — opencode quote note

**Evidence.** `ReopenS078.md:51-64` (F4) establishes that the recorded quote in `agent-definition-files-round56.md:27,37-38` and `round-56.md:20,24-25` combines prose at `agents.mdx:41`, the fence info string `text` at `:43`, and the body at `:44`. Backticks are stripped and whitespace is collapsed, including the spaces around `→`; therefore the phrase “the body of a fenced example” is incomplete and `text` is a fence label, not prose. `ReopenS078.md:106-113` records the pinned source fetch at `https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/agents.mdx`: HTTP 200, 8,779 bytes, SHA-256 `6cca5b0a5a88387e94177d9c13d2e539fb710d69b2298ca6d44b9bc465c8b57a`, opened `2026-10-23T03:09:20Z`. Its exact source lines are reproduced at `:160-177`.

**Old → corrected wording** (note text only):

- `corpus/knowledge/agent-definition-files-round56.md:37-38`
  - Old: `S078's quote is the body of a fenced example whose info string `text` stays in the quote; the fence markers were removed (`Srcopencode`).`
  - New: `S078's recorded quote is normalized from the prose lead-in at `agents.mdx:41`, the fence info string `text` at `:43`, and the example body at `:44`; normalization strips backticks and collapses whitespace, including the spaces around `→`. It is not solely the example body, and `text` is a fence label, not prose.`
- `corpus/lessons/round-56.md:24-25`
  - Old: `S078's quote is a fenced example whose info string `text` stays and whose fence markers were removed.`
  - New: `S078's recorded quote combines prose at `agents.mdx:41`, the fence info string `text` at `:43`, and the example body at `:44`; backticks are stripped and whitespace is folded. It is not just the example body, and `text` is a fence label, not prose.`

Append this sentence to the same existing `Quote notes:` paragraph in `corpus/knowledge/agent-definition-files-round56.md:39`, after the S076 correction above; retain its old note as history:

```text
S078's recorded quote combines the prose lead-in at `agents.mdx:41`, the fence info string `text` at `:43`, and the example body at `:44`; normalization strips backticks and folds whitespace, so the quote is not solely the example body and `text` is a fence label, not prose.
```

The S078 quote cells at `agent-definition-files-round56.md:27` and `round-56.md:20` remain unchanged.

## 3. The round-56 lesson is a historical record

Do not edit `corpus/lessons/round-56.md`. `corpus/lessons/round-12.md:57-60` explicitly says per-round lessons are records; `corpus/lessons/round-50.md:80-86` says the round-49 lesson is append-only and its erratum belongs in a later lesson. Round 56 itself uses `## Corrections to round 55` at `corpus/lessons/round-56.md:69-78`, confirming the later-lesson correction pattern. Append the following to the round-57 lesson under `## Corrections to round 56`:

```markdown
## Corrections to round 56 (R2 — quote provenance)

- **S076 (Gemini CLI).** The quote recorded in `corpus/lessons/round-56.md:18` and `corpus/knowledge/agent-definition-files-round56.md:25` is the user-level location at `subagents.md:324`; it directly states `~/.gemini/agents/*.md` and supports the project token `.gemini/agents/*.md` only through substring matching. The project location is explicitly at `:323`. The 24-word span at `:320-323` directly witnesses the project location and is preferable if a later round elects to replace the counted quote. The quote cells are unchanged by this correction.
- **S078 (opencode).** The quote recorded in `corpus/lessons/round-56.md:20` and `corpus/knowledge/agent-definition-files-round56.md:27` is normalized from prose at `agents.mdx:41`, the fence info string `text` at `:43`, and the example body at `:44`; normalization strips backticks and folds whitespace, including the spaces around `→`. It is not solely the example body, and `text` is a fence label, not prose. The quote cells are unchanged by this correction.
```

This text preserves the past Gate record and reports the corrected provenance without rewriting any counted quote.

## 4. `SKILL.md:109` — singular `agent/` clause

**Old → new** (replace only the clause in the opencode location cell):

- Old: `singular `agent/` still loads per a 2026-01-17 docs commit`
- New: `V2 still discovers legacy directories: “V1 agent files may use `agent/`, `agents/`, `mode/`, or `modes/`. V2 still discovers all four directories.” (OpenCode V2 migration guide, `migrate-v1.mdx:486`, pinned at `anomalyco/opencode@4e0bc522`.)`

The source is the re-opened pinned migration page `https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/migrate-v1.mdx`; `ReopenS078.md:138-142` records HTTP 200, 20,805 bytes, SHA-256 `f3d42b36cec1b498d19543b32e72a069e006ee2a4a6884e548ce3a9408fd78a0`, opened `2026-10-23T03:10:00Z`. The page's `:486` text is: `V1 agent files may use `agent/`, `agents/`, `mode/`, or `modes/`. V2 still discovers all four directories.` The source supports discovery of the legacy directory, but does not support the `2026-01-17` date; drop that date. No new SOURCES row or protected cell is proposed.

# Quality, gates, scope, and limits

- **Append-only decision:** keep `round-56.md` unchanged and put its correction in the round-57 lesson. Append correction wording to the knowledge entry rather than deleting its old note. No SOURCES protected cell or counted quote cell is altered.
- **Q29 integration gate:** `corpus/QUALITY.md:40` requires corrections of falsified/superseded claims in `SKILL.md` and knowledge entries to be registered in `verifiers/check_correction_sweep.py` in the same commit, with the sweep green before the round report. The current `check_correction_sweep.py:10-18` defines the stale/declared-block rule and requires new claims as new registry rows. This scribe drafted no registry row and ran no sweep; the integrator must register the applicable stale phrase(s) with the declared correction and run the gate if these proposed changes are applied.
- **Checks:** no tests, verifier, counter, or new source-fetch command was run. The only shell commands and results are the read-only revision checks above. Source fetch metadata is taken from the existing falsifier receipts, not newly claimed execution by this scribe. Static `read` inspection of the pinned migration page showed the quoted text; its recorded fetch metadata is in `ReopenS078.md`.
- **Behavior:** documentation provenance/calibration only; no product behavior or C1 predicate changes.
- **Touched surface:** `.ufo/waves/round-57/build/ScribeR2Corrections.md` only.
- **Out of scope / unchanged:** `corpus/SOURCES.md`; all counted S076/S078 quote cells in the entry and Gate; `corpus/lessons/round-56.md`; verifiers other than the noted future Q29 registry requirement; all other R1–R8 defects.
- **Known limit:** the 24-word S076 project-level quote is reported as a candidate from the committed falsifier; this report does not replace or re-score the counted quote.

# Artifact

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/build/ScribeR2Corrections.md`
