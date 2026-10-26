# PROVINCE Scope Audit of Assimilation Candidates Against Sibling Lanes (Seat ConnScopeSiblings)

## Verdict

- `chinese-client-skill-surfaces.md`: **admit** (with document-level S-id renumbering to clear collision with committed rows S203–S216).
- `client-surface-census-extension.md`: **refuse** (staged ids S205–S208 collide with committed rows in `corpus/SOURCES.md`; Qwen Code is outside C1's declared four-vendor scope; contains editorial spec commentary).
- `skill-craft-rules-from-chinese-vendors.md`: **admit-pointer-only** (contains measured capability effects belonging to `kengaku-shokunin`; staged S215 collides; distillable into `SKILL.md` checklist rules in a future round).
- `trae-build-vs-translation-axis.md`: **refuse** (core thesis is comparative research methodology owned by `chousa-shokunin`; the single craft root `~/.trae/skills/` is already held in Entry 1).
- `translation-drift-across-vendors.md`: **refuse** (thesis is documentation translation drift and citation hygiene owned by `chousa-shokunin`; interop settings belong in a client interop census).
- `skill-body-authority-and-context-placement.md`: **admit-pointer-only** (pure Kotoba core craft on context slotting, but refused as an independent file for Round 73 due to un-opened Western dependency S222 and C1 scope boundaries).

**Evaluation of the expectation ("At most the first entry is expected to be admitted"):**
I **agree** with the operational boundary for Round 73 wave 1: exactly one entry (`chinese-client-skill-surfaces.md`) should be admitted as a new committed corpus file. However, I **disagree** with any inference that `skill-body-authority-and-context-placement.md` is out-of-province or generic: context-window placement (`system prompt` vs `task` slot vs on-demand) is 100% Kotoba Core (`PROVINCE.md:12, 28`). Its exclusion from this round is purely round-gating (unopened S222 and C1 predicate scope), not sibling-province collision.

---

## 1. Sibling Lane Province Boundaries (Located Primary Evidence)

Kotoba governs prompt and skill craft (`PROVINCE.md:12, 28`). Five adjacent sibling lanes bound this work:

### 1.1 kengaku-shokunin (LLM/model research & evaluation)
- **Kotoba reading:** `sed -n '60p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md`
  > `| kengaku | adjacent | 1f3b0f1ec41ec297130e8944ff97968d32324632 | LLM and model research and evaluation (route telemetry is marked absent since 2026-10-15 in kengaku's own SKILL.md:3); kengaku keeps measured capability effects of prompt format, kotoba owns the craft rules (kengaku description, SKILL.md:3)...`
- **Kengaku reading:** `sed -n '30,32p' /home/vgpnk/Projects/shokunin/kengaku-shokunin/PROVINCE.md`
  > `prompt- and skill-craft rules, render/trigger behaviour — this lane keeps the *measured* effect of prompt format on capability and hands the reusable craft implication out.` (24 words; dropped: `- **kotoba:** `).
- **Kengaku SKILL:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kengaku-shokunin/SKILL.md`
  > `kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)` (11 words; dropped: surrounding description text).
- **Boundary rule:** Kengaku owns benchmarks, empirical accuracy comparisons, and measured capability effects. Kotoba owns prescriptive authoring rules, discovery roots, frontmatter schemas, and trigger checklists.

### 1.2 kake-shokunin (Web properties & publishing)
- **Kake PROVINCE:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kake-shokunin/PROVINCE.md`
  > `**Domain:** web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys` (12 words, byte-exact).
- **Kake SKILL:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kake-shokunin/SKILL.md`
  > `description: Domain specialist — web properties & publishing — scopes ds4cc.com, kimi.page/pro mirrors, Pages deploys. Rank: shonen.` (15 words, byte-exact).
- **Boundary rule:** Kake owns publisher-side placement, deploy pipelines, and hosted web properties. It does not own client-side agent configurations or IDE discovery paths.

### 1.3 kumitate-shokunin (Orchestration & dispatch tooling)
- **Kumitate PROVINCE:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kumitate-shokunin/PROVINCE.md`
  > `**Domain:** orchestration & tooling — scopes OMP task/hub, ufo-fsd scripts & runtime` (11 words, byte-exact).
- **Kumitate routing:** `sed -n '28p' /home/vgpnk/Projects/shokunin/kumitate-shokunin/PROVINCE.md`
  > `Prompt and skill craft → kotoba. Research method → chousa.` (9 words; dropped: `- Local model serving and endpoints → kama. `).
- **Boundary rule:** Kumitate owns agent dispatch runtimes, OMP task harnesses, and substrate paths (`~/.kimi-code/` runtime binaries). Kotoba owns prompt wording, skill frontmatter, and skill directory discovery conventions.

### 1.4 kotodama-shokunin (Linguistic-cultural worldbuilding)
- **Kotodama PROVINCE:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kotodama-shokunin/PROVINCE.md`
  > `**Domain:** linguistic-cultural worldbuilding (言霊, kotodama — the coupling` (7 words; dropped: of word and world-spirit...).
- **Kotodama refusals:** `sed -n '19,20p' /home/vgpnk/Projects/shokunin/kotodama-shokunin/PROVINCE.md`
  > `general source-research method (chousa); web publishing (kake); prompt/skill craft (kotoba).` (10 words; dropped: `(game-dev-2d/3d); `).
- **Kotodama SKILL:** `sed -n '3p' /home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md`
  > `Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin)...` (14 words; dropped: rest of frontmatter description).
- **Boundary rule:** Kotodama refuses prompt/skill craft by name. It owns fictional worldbuilding linguistics, naming systems, and costume terminology.

### 1.5 chousa-shokunin (Deep-research method)
- **Chousa PROVINCE:** `sed -n '3p' /home/vgpnk/Projects/shokunin/chousa-shokunin/PROVINCE.md`
  > `**Domain:** deep-research method (調査) — the reusable craft of source research.` (10 words, byte-exact).
- **Chousa ownership:** `sed -n '5,6p' /home/vgpnk/Projects/shokunin/chousa-shokunin/PROVINCE.md`
  > `**Owns:** question framing; source hierarchy (primary / secondary / aggregator / unsourced); citation chaining and hop resolution; claim-vs-source verification;` (16 words; dropped: search-strategy taxonomy...).
- **Chousa SKILL:** `sed -n '8,10p' /home/vgpnk/Projects/shokunin/chousa-shokunin/SKILL.md`
  > `Domain: the reusable METHOD of source research — how a question is framed, which sources outrank which, how a citation chain is followed` (22 words; dropped: `, and how a claim is verified...`).
- **Kotoba PROVINCE:** `sed -n '52p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md`
  > `| chousa | adjacent | 6c5eb1466f2b8abbd3de576389037f435016d07b | deep-research method; kotoba cites it, never re-derives it (corpus/QUALITY.md: claim admission stays here, the research method stays chousa's) |`
- **Boundary rule:** Chousa owns source hierarchy, comparative citation methods, and verification of translation fidelity. Kotoba cites research findings but never absorbs or re-derives the research method itself.

---

## 2. Audit of the Six Staged Candidate Entries

Candidate directory: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/`

### 2.1 `chinese-client-skill-surfaces.md`
- **Sources cited:** S214 (ByteDance TRAE), S216/S217 (Tencent CodeBuddy), S218/S219 (Moonshot Kimi Code), S221 (Zhipu AI).
- **Domain analysis:**
  - **Kotoba craft:** Core client skill surface ground (`PROVINCE.md:12, 22-25` and `plans/round-73.md:48-51`). Documents project-level and user-level discovery roots, frontmatter key divergence, case sensitivity traps (`allowedTools` vs `allowed-tools`), and progressive description-based routing across four vendors.
  - **Sibling overlap:** Zero collision with sibling provinces. Kengaku keeps capability numbers; Kumitate keeps runtime binaries; Kotodama and Chousa refuse prompt/skill craft.
- **Surviving craft rules:**
  1. Discovery root mappings: TRAE (`.trae/skills/`, `~/.trae-cn/skills/`, `~/.trae/skills/`), CodeBuddy (`.codebuddy/skills/`, `~/.codebuddy/skills/`), Kimi Code (`.kimi-code/skills/`, `.agents/skills/`, `$KIMI_CODE_HOME/skills/`), Zhipu AI managed agents.
  2. Scope precedence: Project-level skill directories take precedence over user-level skill directories on name collision.
  3. Shared discovery root: `.agents/skills/` is supported cross-vendor (TRAE via toggle with `.trae/skills/` winning collisions; Kimi as a first-class group).
  4. Routing surface mechanics: All four vendors treat `description` as the routing surface and scan brief descriptions prior to loading full skill bodies.
  5. Frontmatter compatibility trap: CodeBuddy uses hyphenated `allowed-tools` whereas Qwen Code expects camelCase `allowedTools` and silently drops `allowed-tools` without warning; Kimi CLI tolerates camelCase, kebab-case, and snake_case (`whenToUse`, `disableModelInvocation`).
- **Non-surviving text:** Lines 41–43 (negative market commentary on Japanese client searches; belongs in search log/lesson).
- **Verdict:** **admit** (as `chinese-vendor-skill-surfaces-round73.md`).
- **Located reason:** Implements declared Round 73 C1 coverage claim on client skill surfaces (`plans/round-73.md:48-56`).
- **Flip condition:** Cited sources fail live reopening, or package S-ids (S214, S216–S219, S221) are not renumbered to avoid colliding with committed rows `S214`–`S216`.

### 2.2 `client-surface-census-extension.md`
- **Sources cited:** S205, S206, S207, S208 (Qwen Code Agent Skills docs in EN/ZH/JA and blog update 2026-02-09).
- **Domain analysis:**
  - **Kotoba craft:** Covers Qwen Code discovery roots (`~/.qwen/skills/`, `.qwen/skills/`) and frontmatter keys (`priority`, `paths`, `user-invocable`, `disable-model-invocation`, `hooks`).
  - **Sibling / Governance overlap:**
    - Citing blog post S208 for release history violates Chousa source hierarchy (`chousa-shokunin/PROVINCE.md:5-6`: primary documentation over promotional narrative).
    - Lines 54–57 carry editorial specification commentary ("strongest available argument that the open specification's frontmatter has an unfinished section..."), which is governance opinion, not actionable craft.
  - **ID Collision:**
    - Command: `sed -n '146,149p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`
    - Observed: `S205` is Deep Code, `S206` is Junie, `S207` is opencode, `S208` is Microsoft Agent Framework. Staged IDs collide with committed rows.
- **Surviving craft rules:**
  1. Frontmatter keys: `priority` (sort order in `/skills`), `paths` (glob list gating model discovery until touched), `user-invocable: false` (hides from slash commands), `disable-model-invocation: true` (hides from model auto-invocation), `hooks` (deterministic PreToolUse enforcement).
  2. Discovery roots: `~/.qwen/skills/`, `.qwen/skills/`, `~/.agents/skills/`, `skills.directories`.
  3. Precedence: project > personal > extension > bundled on name collisions.
  4. Compatibility trap: `allowedTools` (camelCase) required; `allowed-tools` silently ignored.
- **Verdict:** **refuse**.
- **Located reason:**
  1. Staged IDs S205–S208 directly collide with committed rows in `corpus/SOURCES.md:146-149`.
  2. Outside Round 73's declared C1 scope: C1 binds four vendors (TRAE, CodeBuddy, Kimi Code, Zhipu), excluding Qwen Code (`plans/round-73.md:48-51`).
  3. Contains editorial spec commentary rather than strictly bounded craft.
- **Flip condition:** Re-opened under a dedicated Qwen Code coverage round with fresh S-ids (e.g. S217+), blog post S208 replaced by primary docs, and lines 54–57 stripped.

### 2.3 `skill-craft-rules-from-chinese-vendors.md`
- **Sources cited:** S215 (TRAE best practices), S216 (CodeBuddy IDE best practices), S218 (Kimi CLI best practices).
- **Domain analysis:**
  - **Kotoba craft:** Checklist authoring rules (naming <=64 chars, description <=1024 chars, body <=500 lines, single-level reference nesting, TOC for >100 lines).
  - **Sibling overlap:**
    - Lines 35–38 cite: "with the wave-1 measured result that focused skills of at most three modules outperform larger bundles, and with the Zhejiang University finding that the same skill can help some configurations and hurt others."
    - Sibling collision with `kengaku-shokunin/PROVINCE.md:30-32` and `PROVINCE.md:138`: "measured capability effects of prompt format stay here; reusable craft implications route out". Citing benchmark performance lift and academic capability findings absorbs Kengaku ground into Kotoba.
  - **ID Collision:** Staged S215 collides with committed S215 (`pi-mono coding agent`, `corpus/SOURCES.md:155`).
- **Surviving craft rules:**
  1. Mechanical limits: Skill name 1–64 chars (lowercase/digits/hyphens); description 1–1024 chars; SKILL.md body <= 500 lines.
  2. Reference discipline: Limit reference nesting to 1 level (no A -> B -> C chains); provide a Table of Contents for any reference file exceeding 100 lines.
  3. Scope boundaries: Explicitly specify both positive and negative trigger boundaries (`Use this skill when:` and `Do NOT use this skill when:`).
  4. Freedom-of-guidance ladder: Match instruction specificity to task fragility (principles vs templates vs executable scripts).
  5. Failure strategies: Author explicit `On Failure:` branches to prevent model improvisation.
- **Verdict:** **admit-pointer-only**.
- **Located reason:** Contains unowned benchmark/capability assertions belonging to `kengaku-shokunin` (`PROVINCE.md:30-32`), collides on S215, and exceeds the C1 four-vendor root/placement predicate (`plans/round-73.md:63-76`).
- **Flip condition:** Excise Zhejiang University and benchmark performance claims, renumber S215, and distill surviving rules into `SKILL.md` § Trigger-fidelity checklist in a future depth round.

### 2.4 `trae-build-vs-translation-axis.md`
- **Sources cited:** S225 (`docs.trae.ai/ide/skills?_lang=en`), S226 (`docs.trae.ai/ide/skills`).
- **Domain analysis:**
  - **Sibling ownership:**
    - The entire entry is a comparative research methodology treatise: how to differentiate translation drift from product build divergence across international vs domestic distributions.
    - Belongs to `chousa-shokunin`: `chousa-shokunin/PROVINCE.md:3, 5-6` ("Domain: deep-research method (調査)... citation chaining and hop resolution; claim-vs-source verification").
    - Kotoba's own `PROVINCE.md:52` explicitly mandates: "deep-research method; kotoba cites it, never re-derives it".
  - **Redundancy:** The single craft datum (the `~/.trae/skills/` international vs `~/.trae-cn/skills/` domestic root) is already captured in `chinese-client-skill-surfaces.md:21`.
- **Surviving craft rules:**
  1. Root mapping: Domestic TRAE documents `~/.trae-cn/skills/`; international TRAE documents `~/.trae/skills/`.
- **Verdict:** **refuse**.
- **Located reason:** The entry re-derives research methodology for documentation comparison, which is explicitly refused by Kotoba (`PROVINCE.md:6, 52`) and owned by `chousa-shokunin` (`PROVINCE.md:3-8`). Its lone craft fact is already incorporated into Entry 1.
- **Flip condition:** Cannot flip to admit as an independent Kotoba knowledge entry; research method findings route to `chousa-shokunin`.

### 2.5 `translation-drift-across-vendors.md`
- **Sources cited:** S218 (Kimi CLI GitHub docs), S219 (Kimi Code CLI Chinese docs).
- **Domain analysis:**
  - **Sibling ownership:**
    - Focuses on documentation drift between English and Chinese pages and deduces a citation discipline rule: "diff every translation against its original before citing it... Two vendors is enough to refuse citing a translation alone".
    - Belongs to `chousa-shokunin` (`PROVINCE.md:3, 5-8`). Citation verification discipline is research method.
  - **Substrate overlap:**
    - Mentions `~/.kimi-code/` paths, which are governed at the substrate level by `kumitate-shokunin/PROVINCE.md:14`.
- **Surviving craft rules:**
  1. Discovery roots: Kimi Code CLI English documentation records cross-client interop roots `~/.claude/skills/`, `~/.codex/skills/`, and `~/.config/agents/skills/`.
  2. Interop configuration: Kimi CLI documents `merge_all_available_skills: true` (default), loading and merging brand directories with precedence `kimi > claude > codex`.
  3. Path discrepancy: Domestic documentation specifies `.kimi-code/skills/` and `~/.kimi-code/skills/` (via `$KIMI_CODE_HOME`), while GitHub English documentation specifies `.kimi/skills/` and `~/.kimi/skills/`.
- **Verdict:** **refuse**.
- **Located reason:** Thesis is documentation translation drift and citation hygiene, which is Chousa's domain (`chousa-shokunin/PROVINCE.md:3-8`). S218/S219 are already cited in Entry 1 for craft discovery roots.
- **Flip condition:** Cannot flip to admit as a standalone knowledge entry; report translation-checking method to `chousa-shokunin`. Interop settings can be admitted as an addendum row in `chinese-client-skill-surfaces.md`.

### 2.6 `skill-body-authority-and-context-placement.md`
- **Sources cited:** S218 (Kimi CLI), S219 (Kimi Code CLI), S221 (Zhipu AI), S222 (Claude Code docs), S214 (TRAE), S216 (CodeBuddy).
- **Domain analysis:**
  - **Kotoba craft:** Core Kotoba craft! Directly addresses where a skill body is placed in LLM context slots (system prompt vs task slot vs on-demand user prompt) and instruction authority laddering.
  - Matches `PROVINCE.md:12` (`SKILL.md` anatomy and compression) and `PROVINCE.md:28` ("Instruction-authority ladder (round 67): what a skill body may assert and at whose authority level").
  - Sibling check: No sibling claims context slot architecture. Kengaku evaluates models; Kumitate schedules tasks; Chousa verifies sources. Context slotting is prompt/skill craft.
- **Surviving craft rules:**
  1. Instruction tiering: A skill body is never a privileged instruction; skill metadata may be promoted to system prompt (Kimi), body may be promoted to task slot (Claude Code `context: fork`), or kept on-demand (Zhipu).
  2. Scope injection: Kimi Code CLI injects skill metadata into the system prompt grouped by origin scope (`Project > User > Extra > Built-in`).
  3. Context window economics: Rules are persistently injected into context for the entire session; skills load on-demand, making skills the appropriate tool for task-specific instructions.
  4. Invocation nesting cap: Kimi CLI caps nested skill invocations at 3.
- **Verdict:** **admit-pointer-only**.
- **Located reason:** Although 100% Kotoba Core on domain grounds, it cannot be admitted as an independent file in Round 73 because:
  1. It introduces S222 (`https://code.claude.com/docs/en/skills.md`), an unopened Western client source outside C1's 4-vendor scope (`plans/round-73.md:48-51`).
  2. S-id collisions exist for S214 and S216.
  3. Admitting a second file would add a second README row and risk expanding the C1 counter scope.
- **Flip condition:** Renumber S-ids, open and pin S222 under an instruction-authority/placement round, and admit as `corpus/knowledge/skill-body-authority-and-context-placement-roundXX.md`.

---

## 3. Synthesis and Assessment of the One-Entry Admission Expectation

The prompt states: *"At most the first entry is expected to be admitted; say if you disagree and why."*

### Operational Assessment: AGREE
From an operational and verification standpoint for Round 73 wave 1, **exactly one entry** (`chinese-client-skill-surfaces.md`) should be admitted:
1. **Predicate constraint:** C1's frozen predicate (`plans/round-73.md:59-76`) specifically checks `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` and binds four vendors. Admitting further files would fail C1's one-row-per-vendor structure and increase registry weight.
2. **Provenance & ID collisions:** Entries 2 and 3 collide with committed rows S205–S208 and S215 in `corpus/SOURCES.md`. Entry 6 relies on S222 (Claude Code), which has not been opened, pinned, or ledgered in this round.
3. **Domain boundaries:** Entries 4 and 5 are comparative research methodology and translation drift studies owned by `chousa-shokunin` (`PROVINCE.md:3, 5-8`).

### Substantive Assessment: DISAGREE with Scope Characterization
I **disagree** with any presumption that `skill-body-authority-and-context-placement.md` (Entry 6) is excluded because it lacks craft relevance or belongs to another lane:
- The distinction between system prompt injection, task slot promotion, and on-demand tool retrieval is **central to Kotoba's Core** (`PROVINCE.md:28`).
- Entry 6 is excluded from landing this round **strictly due to procedural and source constraints** (unopened source S222, S-id collisions, and C1 predicate bounds), not province mismatch.

---

## 4. UFO-FSD Connector: Bounded Proposal

### Evidence
1. **Zhipu root token vulnerability in Entry 1:**
   In `chinese-client-skill-surfaces.md:24`, the vendor table lists `uploaded package` as Zhipu AI's root. In the actual primary documentation snapshot (`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecSrcZhipu/snapshot.md:83`), the English string `uploaded package` never appears. The snapshot states:
   `运行目录为 /workspace/skills/<目录名>/，按需读取`
   If the token in the admitted table is `uploaded package`, C1's frozen predicate (`plans/round-73.md:68-70`: backticked tokens must occur word-bounded in the committed snapshot) will **FAIL** on Zhipu.
2. **Entry 6 placement insight for Zhipu:**
   `skill-body-authority-and-context-placement.md:38` extracts Zhipu's exact placement rule: `"Agent 先读名称与描述，再按任务读取正文和配套资料，不必每次把整套方法塞进 system prompt"` (`snapshot.md:25-28, 83`).
   C1's predicate explicitly permits: `"at least one root or placement token and at least two keys"`.
3. **C2 description budget constraint:**
   `round-73-addendum-1.md` binds C2 to `check_own_description.py`, requiring `len(D) <= 1024` while maintaining 9 adjacent sibling clauses. Currently, `SKILL.md` description has 1021 characters (3 characters headroom). Admitting multiple files would force additional documentation in `SKILL.md`, threatening the byte budget.

### Affected Axes
- `coverage` (8.5; C1 — four Chinese-vendor skill surfaces)
- `depth` (9; C2 — SKILL.md's own description obeys trigger rule)
- `consistency` (10; C3 — tip battery counter agreement)

### Proposed Move
**Synthesize Zhipu's runtime path `/workspace/skills/` as its root token and `按需读取` (read on-demand) as its placement token directly into the C1 draft `chinese-vendor-skill-surfaces-round73.md`, while maintaining the strict one-entry admission boundary (refusing Entry 6 as an independent file).**

Specifically:
- In the admitted vendor table for Zhipu AI, format the row as:
  `| Zhipu AI | managed agents (S<<id>>) | `/workspace/skills/` | `按需读取` | `name`, `description`, `type:zai`, `type:custom` |`
- All backticked tokens (`/workspace/skills/`, `按需读取`, `type:zai`, `type:custom`) exist verbatim and word-bounded in the fetched snapshot `ExecSrcZhipu/snapshot.md` (lines 79, 83).
- This captures Entry 6's placement architecture without admitting Entry 6 or opening S222, preventing a C1 verification failure on Zhipu and preserving the C2 line/byte budget.

### Risks
1. **Tokenizer delimiter handling:** `check_cn_vendor_surfaces.py` must handle slash-delimited paths (`/workspace/skills/`) as valid tokens without stripping bounding slashes.
2. **Snapshot hash integrity:** The tokens must be validated against `snapshots/MANIFEST.sha256` pinned bytes for Zhipu (`b20e45c7ff...`).

### Verification
1. Run C1 counter draft over the synthesized row:
   `python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>`
   Confirm output prints `vendor skill surfaces backed 4 of 4` with Zhipu passing on `/workspace/skills/` and `按需读取`.
2. Confirm C2 description length remains `<= 1024` with zero frontmatter line count delta:
   `python3 -B verifiers/check_own_description.py --rev <rev>`
   `git diff --numstat <base> <rev> -- SKILL.md` (inserted - deleted == 0 in frontmatter).
3. Confirm no sibling lane PROVINCE is violated and no unowned capability claims are absorbed.
