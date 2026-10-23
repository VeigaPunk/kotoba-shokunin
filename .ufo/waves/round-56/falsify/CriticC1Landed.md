Result: MIXED — C1 at c22fdd39 meets the frozen v1.3 predicate (7 of 7; new ground 3, exit 0) with substantive new ground (0 base hits for .github/agents, .gemini/agents, .cursor/agents both outside and inside .ufo/) and a byte-exact SKILL.md line-budget move (sha256 73497d2a…), but two rows' quotes/tokens (opencode S078 and Gemini CLI S076) were shaped to counter mechanics rather than the page, corpus/README.md § Coverage map omits the new C1 files (unindexed=3 in verify_corpus_integrity.py), and lowest-axis compliance holds under the owned-axis reading (depth 9) only.

## 1. Frozen-predicate verification (`7 of 7; new ground 3`) and declared reason

**Verdict: HOLDS.** C1 at `c22fdd390e10623209024c9bbc2fa86b0cdfc333` verifies on the frozen v1.3 counter (`verifiers/check_agent_definitions.py`, committed at `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8` before any C1 content existed; sha256 `2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47`, unchanged at `c22fdd39`) for the declared reason.

- **Sandbox setup and counter runs** (cwd `/fast/scratch/hyaku/kotoba-r56/CriticC1Landed`, cloned from `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at `c22fdd390e10623209024c9bbc2fa86b0cdfc333`):
  ```text
  $ timeout 30 python3 -B verifiers/check_agent_definitions.py --self-test
  self-test: 0 failure(s) over 99 assertions
  SELFTEST_EXIT=0

  $ timeout 60 python3 -B verifiers/check_agent_definitions.py --rev c22fdd390e10623209024c9bbc2fa86b0cdfc333 --fetch; echo "EXIT=$?"
  agent-definition locations found on the live page 7 of 7; new ground 3
  Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
  Codex        BACKED token=.codex/agents/ norm=.codex/agents found=yes base_count=5
  VS Code      BACKED token=.github/agents norm=.github/agents found=yes base_count=0
  Copilot CLI  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
  Gemini CLI   BACKED token=.gemini/agents/*.md norm=.gemini/agents found=yes base_count=0
  Cursor       BACKED token=.cursor/agents/ norm=.cursor/agents found=yes base_count=0
  opencode     BACKED token=.opencode/agents norm=.opencode/agents found=yes base_count=10
  EXIT=0
  ```
- **Independent live-page re-fetch** (ordinary `curl -sSL --max-time 30`, saved under `/fast/scratch/hyaku/kotoba-r56/CriticC1Landed/fetches/S072.md`–`S078.md`):
  Every row's URL returned HTTP 200 and reproduced the exact byte count and SHA-256 recorded in `corpus/SOURCES.md:85-91` and `corpus/lessons/round-56.md:14-20`:
  - `S072` (`https://code.claude.com/docs/en/agent-sdk/subagents.md`): `Fri 23 Oct 2026 03:11:21 AM UTC`, HTTP 200, 41,461 B, sha256 `5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315`.
  - `S073` (`https://developers.openai.com/codex/subagents.md` → `https://learn.chatgpt.com/docs/agent-configuration/subagents.md`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 22,907 B, sha256 `e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f`.
  - `S074` (`https://code.visualstudio.com/docs/agent-customization/custom-agents.md`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 15,714 B, sha256 `8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f`.
  - `S075` (`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 8,379 B, sha256 `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2`.
  - `S076` (`https://geminicli.com/docs/core/subagents.md`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 23,614 B, sha256 `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db`.
  - `S077` (`https://cursor.com/docs/subagents.md`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 27,660 B, sha256 `264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668`.
  - `S078` (`https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/agents.mdx`): `Fri 23 Oct 2026 03:11:22 AM UTC`, HTTP 200, 8,779 B, sha256 `6cca5b0a5a88387e94177d9c13d2e539fb710d69b2298ca6d44b9bc465c8b57a`.

---

## 2. Substantiveness of `new ground 3` (outside `.ufo/` and inside `.ufo/`)

**Verdict: HOLDS.** All three counted new-ground forms — `.github/agents`, `.gemini/agents`, and `.cursor/agents` — are completely absent at base `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41` both **outside `.ufo/`** and **inside `.ufo/`**.

- **Exact git-grep check at `b0b7140b` (outside `.ufo/` and inside `.ufo/`) and at pre-build freeze `e02f5f5d` (inside `.ufo/`):**
  ```text
  $ for p in ".github/agents" ".gemini/agents" ".cursor/agents" ".github/agent" ".gemini/agent" ".cursor/agent" ".vscode/agents" ".copilot/agents"; do
      git --no-optional-locks grep -n -i -F -e "$p" b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- . ':!.ufo'; echo "$p outside .ufo @ b0b7140b: exit=$?"
      git --no-optional-locks grep -n -i -F -e "$p" b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- .ufo; echo "$p inside .ufo @ b0b7140b: exit=$?"
    done
  .github/agents outside .ufo @ b0b7140b: exit=1
  .github/agents inside .ufo @ b0b7140b: exit=1
  .gemini/agents outside .ufo @ b0b7140b: exit=1
  .gemini/agents inside .ufo @ b0b7140b: exit=1
  .cursor/agents outside .ufo @ b0b7140b: exit=1
  .cursor/agents inside .ufo @ b0b7140b: exit=1
  .github/agent outside .ufo @ b0b7140b: exit=1
  .github/agent inside .ufo @ b0b7140b: exit=1
  .gemini/agent outside .ufo @ b0b7140b: exit=1
  .gemini/agent inside .ufo @ b0b7140b: exit=1
  .cursor/agent outside .ufo @ b0b7140b: exit=1
  .cursor/agent inside .ufo @ b0b7140b: exit=1
  .vscode/agents outside .ufo @ b0b7140b: exit=1
  .vscode/agents inside .ufo @ b0b7140b: exit=1
  .copilot/agents outside .ufo @ b0b7140b: exit=1
  .copilot/agents inside .ufo @ b0b7140b: exit=1
  ```
- **What is inside `.ufo/` at `b0b7140b` vs `e02f5f5d`:**
  - At `b0b7140b` inside `.ufo/`:
    - `.github/agents`, `.gemini/agents`, `.cursor/agents` (and their singulars, plus `.vscode/agents` and `.copilot/agents`): **0 hits (exit 1)**. No prior round's scout, build, or falsify report in `.ufo/` ever named these three directories.
    - `.claude/agents`: 22 lines across 9 files in `.ufo/` — 2 lines genuinely name Claude Code's `.claude/agents/` subagent directory (`.ufo/waves/round-50/build/SrcClaudeSubagents.md:49` and `.ufo/waves/round-50/falsify/CriticFrontierSweep.md:55`), and 20 lines are `.claude/AGENTS.md` always-on fixtures/reports in `.ufo/waves/round-53/`. Outside `.ufo/` at `b0b7140b`, all 3 hits are `.claude/AGENTS.md` case collisions (`corpus/knowledge/alwayson-rule-files-round53.md:25`, `verifiers/verify_alwayson.py:22,77`).
    - `.codex/agents`: 25 lines across 18 files in `.ufo/`, all `~/.codex/AGENTS.md` or `~/.codex/AGENTS.override.md` (rounds 21, 44, 47, 53); outside `.ufo/` at `b0b7140b`, all 5 hits are `~/.codex/AGENTS.md` / `.codex/AGENTS.md` case collisions (`LOG.md:484`, `alwayson-rule-files-round53.md:82`, `instruction-surface-census-round13.md:98`, `instruction-surface-remeasure-round13.md:63,65`). Thus Codex's standalone TOML `.codex/agents/` directory is also substantively new to the lane's corpus even though case-insensitive matching against `AGENTS.md` conservatively bars it from `G`.
    - `.opencode/agents`: 4 lines in `.ufo/` (`.ufo/round-21/scouts/G5.md:123` `.opencode/agents/` and 3 `.opencode/AGENTS.md` lines in `.ufo/waves/round-47/`); outside `.ufo/` at `b0b7140b`, 10 hits (`verifiers/checklist-baseline.json:100-148` ×9 and `instruction-surface-remeasure-round13.md:63`).
  - At `e02f5f5d` inside `.ufo/`: `.github/agents`, `.gemini/agents`, and `.cursor/agents` occur only inside round 56's own pre-freeze control wave (`.ufo/waves/round-56/controls-call.json`, `CtlC1DoNothingJunk.{md,txt}`, `CtlC1Fabricated.{md,txt}`, `CtlC1RealNoForm.{md,txt}`, `C1-v12-rescore.txt`).
  - VS Code (`.github/agents`) and Copilot CLI (`.github/agents/`) both normalise to `.github/agents` and are deduplicated by `ground = len({n for n, c in counts.items() if c == 0})` (`verifiers/check_agent_definitions.py:1136`), contributing 1 to `G`, plus `.gemini/agents` (1) and `.cursor/agents` (1) = `new ground 3`.

---

## 3. Rows whose token or quote was tuned to the counter rather than the page

**Verdict: MIXED (two concrete counterexamples where quote/token selection was shaped by counter mechanics; neither invalidates `F >= 5, G >= 2`).**

### Counterexample 3a — `opencode` row (`SKILL.md:109`, `corpus/knowledge/agent-definition-files-round56.md:27,33-34`, `corpus/lessons/round-56.md:20,23-24`, `corpus/SOURCES.md:91`)
- **What landed:**
  - `SKILL.md:109` & `agent-definition-files-round56.md:27` location token: `.opencode/agents` (no trailing slash, whereas `SOURCES.md:91` `teaches` writes `.opencode/agents/`).
  - Quote (`agent-definition-files-round56.md:27`, `lessons/round-56.md:20`):
    `"A nested path becomes part of the agent ID: text .opencode/agents/team/reviewer.md → team/reviewer"` (`agents.mdx:41-44`).
- **Evidence of counter-tuning from sandbox git history (`/fast/scratch/hyaku/kotoba-r56/Srcopencode`):**
  In `Srcopencode`'s initial commit `469b73d57d1a0c31955f37cbd7d9e5e9ebc62c25`, the location token was `.opencode/agents/` and the quote was taken from the primary `## Locations` definition at `agents.mdx:33-38`:
  `"Save Markdown agents globally for all projects or inside a project: text ~/.config/opencode/agents/<name>.md .opencode/agents/<name>.md"`
  That run failed `--fetch` (`opencode BACKED token=.opencode/agents/ norm=.opencode/agents found=no`, `Srcopencode.md:50`) because `check_agent_definitions.py` strips `<[A-Za-z][^>]*>` as HTML tags on the fetched page (`norm_page`, `:699`) while preserving angle brackets on the quote side (`norm`, `:691-693`), making any verbatim quote containing `<name>` from a raw `.mdx` file impossible to match (`found_on_page = False`).
  In commit `84b6e10a0794ea82de37baad94358af505357cd4` (`sandbox: fix opencode C1 quote for fetch`), `Srcopencode`:
  1. Switched to `agents.mdx:41-44`, stripped the ```` ``` ```` code-fence markers, and kept the fence's info string `text` as a bare word in the quote (`"...agent ID: text .opencode/agents/team/reviewer.md..."`) because `_plain()` (`:686`) strips backticks from ```` ```text ```` on the page, leaving `text` between `ID:` and `.opencode/agents/team/reviewer.md` in `norm_page(page_text)`. Removing `text` from the quote fails `--fetch`:
     ```text
     S078 landed_with_text: found_on_page=True
     S078 without_text_infostring: found_on_page=False
     S078 loc_block_with_<name>: found_on_page=False
     ```
  2. Dropped the trailing `/` from `.opencode/agents/` → `.opencode/agents` so the token matches `.opencode/agents/team/reviewer.md` before `/team` at a right segment boundary (`check_agent_definitions.py:726`).
- **Impacted axes:** calibration / consistency (the quote is disclosed in `agent-definition-files-round56.md:33-34`, so it is not fabrication, but the token and quote are artifacts of `norm_page()` on fenced `.mdx`). Even if `opencode` were excluded from `F`, `F = 6 >= 5` and `G = 3 >= 2` still hold (`opencode` has `base_count=10`, contributing `0` to `G`).
- **Smallest safe correction:** Keep the disclosure in `agent-definition-files-round56.md:33-34` (or align `SOURCES.md:91` and `SKILL.md:109` on whether the trailing slash is written); no counter edit.

### Counterexample 3b — `Gemini CLI` row (`SKILL.md:107`, `corpus/knowledge/agent-definition-files-round56.md:25,31-33`, `corpus/lessons/round-56.md:18,22-23`)
- **What landed:**
  - `SKILL.md:107` and `agent-definition-files-round56.md:25` list the **project-level** path `.gemini/agents/*.md` in the Location cell, but the Quote cell quotes only line 324 (`fetches/S076.md:324`):
    `"2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)"`
- **Why it was tuned to the counter:**
  In `fetches/S076.md:320-324`:
  ```markdown
  Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You
  can place them in:

  1.  **Project-level:** `.gemini/agents/*.md` (Shared with your team)
  2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)
  ```
  Line 323 alone (`1.  **Project-level:** \`.gemini/agents/*.md\` (Shared with your team)`) has no `agent`/`subagent` word outside `.gemini/agents/*.md` (`outside_agent=False` at `check_agent_definitions.py:571`). Line 324 has `(Personal agents)` at the end (`outside_agent=True`), and passes the raw-token check (`check_agent_definitions.py:573`) only because `.gemini/agents/*.md` is a substring of `~/.gemini/agents/*.md` after `~/`. Thus the Quote cell in `agent-definition-files-round56.md:25` witnesses the user-level path (`~/.gemini/agents/*.md`), not the project-level path (`.gemini/agents/*.md`) in its own Location cell.
- **Verification of untuned alternatives on the same page (`fetches/S076.md:320-324`):**
  ```text
  S076 proj_only (:323): words=7 hit=('.gemini/agents/*.md', 23, 42) outside_agent=False raw_ok=True found_on_page=True
  S076 proj_with_intro (:320-323): words=23 hit=('.gemini/agents/*.md', 119, 138) outside_agent=True raw_ok=True found_on_page=True
  S076 both_bullets (:323-324): words=12 hit=('.gemini/agents/*.md', 23, 42) outside_agent=True raw_ok=True found_on_page=True
  S076 landed_user_only (:324): words=5 hit=('~/.gemini/agents/*.md', 20, 41) outside_agent=True raw_ok=True found_on_page=True
  ```
- **Impacted axes:** calibration / consistency (scope mismatch between the Location cell and Quote cell).
- **Smallest safe correction:** Replace the S076 quote in `corpus/knowledge/agent-definition-files-round56.md:25` and `corpus/lessons/round-56.md:18` (and update `:1` / `:31-33` anchor to `subagents.md:323-324`) with the 12-word two-bullet quote `"1.  **Project-level:** \`.gemini/agents/*.md\` (Shared with your team) 2.  **User-level:** \`~/.gemini/agents/*.md\` (Personal agents)"`, which directly witnesses `.gemini/agents/*.md` and passes `check_agent_definitions.py`.

### Other rows checked (no tuning defect)
- **VS Code (`S074`, `SKILL.md:105`, `agent-definition-files-round56.md:23`):** On `fetches/S074.md:108,128`, VS Code's own documentation writes the workspace directory as `.github/agents` **without** a trailing slash (`| Workspace | \`.github/agents\` folder |`, `such as \`.github/agents\` and \`~/.copilot/agents\``); `.github/agents/` with a trailing slash is `False` under `token_at_boundary` on `S074.md`. Because `cells()` in `check_agent_definitions.py:254` splits naively on `|`, the markdown table row at `custom-agents.md:108` cannot sit inside the entry's table cell; `SrcVSCode` quoted the example sentence at `custom-agents.md:63` (`"For example, save this planning agent as \`.github/agents/planner.agent.md\`. It uses read-only tools to research a task and return a plan:"`), which is verbatim prose on the page. (If a non-example prose quote is preferred, `custom-agents.md:128` `"Prefer native harness folders, such as \`.github/agents\` and \`~/.copilot/agents\`, over custom search locations."` is 13 words and also passes `check_agent_definitions.py`.)
- **Claude Code (`S072`, `SKILL.md:103`, `agent-definition-files-round56.md:21,29-30`):** Because `S026` (`code.claude.com/docs/en/sub-agents`) was already a base SOURCES row at `b0b7140b`, `SrcClaudeCode` cited the Agent SDK subagents page (`code.claude.com/docs/en/agent-sdk/subagents.md:17`, S072) for the `.claude/agents/` path quote while explicitly attributing the file schema (`name`, `description`, `tools`, `model`) to `S026`. Disclosed in both `SKILL.md:103` and `agent-definition-files-round56.md:1,29-30`.
- **Copilot CLI (`S075`, `SKILL.md:106`, `lessons/round-56.md:33`):** L1 explicitly rejected `ScoutAgentSpec.md:236-238`'s suggestion to lead Copilot CLI's cell with user-level `~/.copilot/agents/` (which would have tuned the cell to raise `G` from 3 to 4), keeping project-level `.github/agents/` first across all seven rows.

---

## 4. Axis fit (`depth`) and lowest-owned-axis compliance

**Verdict: MIXED (fits `depth` and is the lowest *owned* axis, but not the lowest *overall* axis).**

- **Why C1 is `depth`:** `PROVINCE.md:13` already owns agent-definition craft and `SKILL.md:304-349` already carries the 9-box opencode checklist. `SKILL.md:97-110` (`### Agent-definition files by client`) and `corpus/knowledge/agent-definition-files-round56.md` add verifiable, source-backed technical detail on where each of the seven clients stores agent definitions, how their file formats and frontmatter schemas diverge (Codex standalone TOML with required `name`, `description`, `developer_instructions` and `features.* = false` vs Markdown with YAML frontmatter; required vs optional `name`; `tools` vs `readonly` vs `permissions`), and why the opencode checklist cannot be applied directly to the other six clients. Both pre-integration defects raised in `CriticC1Rows.md` (the wrong Cursor Action `"Apply checklist to Cursor subagents"` and `ScribeC1Frame.md`'s placement of the new heading inside `## Agent-definition fidelity checklist`) were corrected before `c22fdd39` landed.
- **Lowest owned axis vs all axes:** At base `b0b7140b` (`SCORECARD.md:3,26-34`), kotoba's owned axes are **depth (9)** and **consistency (10)**, so **depth (9) is the lowest owned axis**. However, the advisory axes **freshness (8)** and **adjacency (8.0)** are lower than 9, and fleet `.ufo/l0-questions.md:84` (whether `AXES.md`'s lowest non-retired axis requirement ranges over advisory axes) remains open (`SCORECARD.md:343`, `corpus/lessons/round-47-verifier-spotcheck.md:41`). C1 meets the lowest-owned-axis reading only.

---

## 5. Harm check: `SKILL.md` line-budget move, checklist box hashes, and corpus gates

**Verdict: MIXED (the `SKILL.md` line-budget move and 9 agentdef boxes are byte-exact, but `corpus/README.md` § Coverage map omits the new C1 files at `c22fdd39`, leaving `verify_corpus_integrity.py` red with `unindexed=3`).**

- **`SKILL.md` moved block SHA-256 (`b0b7140b` `SKILL.md:157-175` vs `c22fdd39` `corpus/knowledge/render-mechanism-round7.md:100-118`):**
  ```text
  $ git --no-optional-locks show b0b7140b5a7cf8a50f13989ee6285fc8ee245c41:SKILL.md | sed -n '157,175p' | sha256sum
  73497d2a0440ba83ade05e3fca022eb1f615890de42a6d03d67bdd648375a109  -
  $ git --no-optional-locks show c22fdd390e10623209024c9bbc2fa86b0cdfc333:corpus/knowledge/render-mechanism-round7.md | sed -n '100,118p' | sha256sum
  73497d2a0440ba83ade05e3fca022eb1f615890de42a6d03d67bdd648375a109  -
  $ diff -u <(git --no-optional-locks show b0b7140b5a7cf8a50f13989ee6285fc8ee245c41:SKILL.md | sed -n '157,175p') <(git --no-optional-locks show c22fdd390e10623209024c9bbc2fa86b0cdfc333:corpus/knowledge/render-mechanism-round7.md | sed -n '100,118p'); echo "DIFF_EXIT=$?"
  DIFF_EXIT=0
  ```
- **Nine agent-definition fidelity checklist boxes (`b0b7140b` `SKILL.md:308-353` vs `c22fdd39` `SKILL.md:304-349`):**
  ```text
  $ git --no-optional-locks show b0b7140b5a7cf8a50f13989ee6285fc8ee245c41:SKILL.md | sed -n '308,353p' | sha256sum
  0d23bcd80dbc401e40cd119949428802913a2da1ba92a4ff59107d741013b409  -
  $ git --no-optional-locks show c22fdd390e10623209024c9bbc2fa86b0cdfc333:SKILL.md | sed -n '304,349p' | sha256sum
  0d23bcd80dbc401e40cd119949428802913a2da1ba92a4ff59107d741013b409  -
  AGENTDEF_DIFF_EXIT=0
  ```
- **Line budget, gate registry, surfaces, and SOURCES append-only (`b0b7140b..c22fdd39`):**
  - `SKILL.md` is 596 lines (`trigger.line_budget` PASS: `596 lines within budget 600`; `checklist.box_map_complete` PASS: `41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)`).
  - `python3 -B verifiers/check_gate_registry.py --rev c22fdd390e10623209024c9bbc2fa86b0cdfc333` → `gate registry rows conformant 28 of 28 lane verifiers; phantom 0`, exit 0.
  - `python3 -B verifiers/verify_surfaces.py --json` → `pass: 7, fail: 0`, exit 0.
  - `python3 -B verifiers/check_sources_append_only.py --base b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 --rev c22fdd390e10623209024c9bbc2fa86b0cdfc333` → `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`, exit 0.
- **Defect found — `corpus/README.md` § Coverage map (`corpus/README.md:7-88`) omits the new C1 entry and round-56 lesson (plus `lessons/round-55-verifier-spotcheck.md`):**
  ```text
  $ timeout 30 python3 -B verifiers/verify_corpus_integrity.py; echo "CORPUS_INT_EXIT=$?"
  corpus.index    tracked=87 unindexed=3 stale=0 missing=0  (102 FILE-column patterns over 86 md files)
             unindexed: corpus/knowledge/agent-definition-files-round56.md
             unindexed: corpus/lessons/round-55-verifier-spotcheck.md
             unindexed: corpus/lessons/round-56.md
  DRIFT   corpus.index.tracked_files: observed=87 expected=81
  DRIFT   corpus.index.unindexed: observed=3 expected=0 / empty
  ...
  CORPUS_INT_EXIT=1
  ```
  `verify_corpus_independent.py` reports the identical `corpus.index.unindexed` DRIFT (`observed=3`, exit 1). Note that even in the lane's uncommitted working-tree diff (`corpus/README.md:136-143`), `knowledge/agent-definition-files-round56.md` is mentioned only inside a `## Frontier` note paragraph, whereas both corpus verifiers scan only the `File` column of the `## Coverage map` table (`corpus/README.md:7-88`).
  - **Impacted axes:** consistency / operability (corpus index gate).
  - **Smallest safe correction:** Add index rows for `lessons/round-55-verifier-spotcheck.md`, `knowledge/agent-definition-files-round56.md`, and `lessons/round-56.md` to the `## Coverage map` table in `corpus/README.md` (and update `verifiers/corpus-baseline.json` + `check_gate_finding_delta.py` if part of the round's close-out).

## Tooling and hygiene

- No tools were installed or upgraded.
- No paid model calls, client CLIs, or headless browsers were invoked.
- Only this report was written in the lane (`.ufo/waves/round-56/falsify/CriticC1Landed.md`); all probes and fetches ran inside `/fast/scratch/hyaku/kotoba-r56/CriticC1Landed` with no sandbox commits created and no lingering background processes.

Report: .ufo/waves/round-56/falsify/CriticC1Landed.md
