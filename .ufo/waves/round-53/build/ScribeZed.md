Result: DONE — Zed documents a nine-name ordered project-instruction list and a first-match-only loader (doc and source code agree at upstream `cfb894a`), documents neither an `@`-import nor a symlink for instruction files, documents no instruction size limit, and says nothing about dated or transient content after the Q30 three-part sweep.

Seat: KotobaR53.ScribeZed (leaf scribe, no subagents dispatched). Lane repo read-only; all writes are this report plus scratch under `/fast/scratch/hyaku/kotoba-r53/ScribeZed/`.

# What Zed does (answers to the five questions)

**1. Which always-on file names it reads.** Zed Agent reads a personal file (`~/.config/zed/AGENTS.md`, `%APPDATA%\Zed\AGENTS.md` on Windows) and, per project root, the first match from a fixed nine-name list. Doc: `zed.dev/docs/ai/instructions.md:27-35` —

```
- `.rules`
- `.cursorrules`
- `.windsurfrules`
- `.clinerules`
- `.github/copilot-instructions.md`
- `AGENT.md`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
```

The same nine names are the constant `RULES_FILE_NAMES` in `crates/prompt_store/src/prompts.rs:22-32` at commit `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e`. Note `AGENT.md` (singular) is a separate, higher-priority entry from `AGENTS.md`; `GEMINI.md` is last.

**2. One or several, and two files in one directory.** One project file per worktree root, never merged, plus the personal file once: a single-root project contributes at most two files to the prompt (personal and one project), and a multi-root project contributes one project file per root (`future::join_all` over `worktree_tasks`, `agent.rs:1422-1438`). Doc: `instructions.md:25` "Project instruction files apply to the current project. Zed uses the first matching file in this list"; personal and project both reach the prompt, with `instructions.md:37` "Project instructions override personal `AGENTS.md` when they conflict". Code agrees: the loader walks the ordered list and takes `.next()` — the first entry that exists and is a file — in `crates/agent/src/agent.rs:1522-1532`, and the system prompt renders `### Personal \`AGENTS.md\`` before `### Project Rules` (`crates/agent/src/templates/system_prompt.hbs:253-274`, precedence sentence at `:266`). With two files in one directory the lower-priority one is ignored silently: no merge, no warning.

**Hazard (code-read, not executed):** the filter tests only that the entry is a file, so an **empty or stale higher-priority file wins**. A leftover empty `.rules` or `.cursorrules` suppresses a populated `AGENTS.md` (`agent.rs:1524-1532` has no emptiness check, and the text is inserted as-is, `system_prompt.hbs:273`). Six names outrank `AGENTS.md`.

**3. Redirects.**
- `@AGENTS.md` import: **not documented** (three-part sweep below) and **not implemented in the loader** — `load_worktree_rules_file` reads the file's rope, trims it, and the template inserts it verbatim (`agent.rs:1550-1558`, `system_prompt.hbs:273`); no import/include expansion exists in `crates/agent` or `crates/prompt_store`. For Zed an `@AGENTS.md` line is literal text the model may or may not act on, not a loader redirect. [INFERENCE from code; not executed against a running Zed — `zed` is not installed on this host (`command -v zed` → not found).]
- Symlink: **not documented for instruction files.** The only symlink documentation near this topic is for the skills root (`docs/src/ai/skills.md:199`, "Use a symlink if you need to point at another location"). Code: the worktree records a symlink to a regular file as a normal file (metadata follows the target: `crates/fs/src/fs.rs:1106-1117`; `EntryKind` has no symlink variant, `crates/worktree/src/worktree.rs:4028-4034`; `Entry::new` maps non-directory metadata to `EntryKind::File`, `:4156-4168`; `is_file()` is `matches!(self, EntryKind::File)`, `:4212-4214`). So a symlink named `AGENTS.md` is selected and its target's text is read. [INFERENCE from code.] A symlink does **not** redirect name choice: if `.rules` exists, the `AGENTS.md` symlink is never consulted.
- Config pointing at another name: **none.** No setting in `docs/src` names a rules-file path or alternate filename (`grep -rniE 'rules_file|instructions_file|agents_md' docs/src --include='*.md'` → no lines); `crates/agent_settings` exposes only `agent.commit_message_instructions` and `agent.commit_message_include_project_rules`, neither of which changes the loader's name list. The list is a compile-time constant.

**4. Documented size limit.** **None for instruction files.** Doc pages state none, and the loader reads in full — `crates/agent_settings/src/user_agents_md.rs:13-14`: "The file is read in full, mirroring how project rules / repo `AGENTS.md` files are loaded by the native agent today." The project loader has no cap either (`agent.rs:1515-1586`). The 50 KB cap in `docs/src/ai/skills.md:198` applies to the skills catalog, a different subsystem; it must not be quoted as an instruction-file limit.

**5. Dated or transient content.** **Nothing documented.** No doc sentence, release-note line or code path filters, expires or re-dates instruction text; the only date in the prompt is harness metadata (`pub date: String`, `crates/agent/src/templates.rs:45`), not a content rule. Q30 sweep is complete, so this is recorded as "not documented", not "not checked".

**Scope caveat (divergence from the open format).** The loader looks only at the worktree root (`worktree.entry_for_path(name)` with root-relative names, `agent.rs:1524-1527`); a nested `sub/dir/AGENTS.md` is never read, and the watcher only refreshes on those root paths plus `.agents/` (`agent.rs:1619-1629`). The agents.md convention of "closest file wins" (SOURCES row S004, still `queued`) does not apply to Zed. [INFERENCE from code.]

# Gate record

All fetches by `curl -sS -L`; times UTC, 2026-10-22.

| # | source | URL | time | HTTP | bytes | sha256 | quote (≤25 words) | location |
|---|---|---|---|---|---|---|---|---|
| G1 | Zed docs — Agent Instructions (served markdown) | https://zed.dev/docs/ai/instructions.md | 20:05:08Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` | "Project instruction files apply to the current project. Zed uses the first matching file in this list:" | `instructions.md:25` |
| G2 | same, HTML route | https://zed.dev/docs/ai/instructions | 20:05:08Z | 200 | 44,721 | `866281ea28d3a171e1fb565147357ed771d9e2b7fd763212b06659db9d24b81b` | "Instructions are always-on context for the Zed Agent." | `zed_instructions.html:143` (same sentence at `instructions.md:5` in G1; G3 source body differs only by frontmatter) |
| G3 | Zed docs source tree at `cfb894a` | https://raw.githubusercontent.com/zed-industries/zed/main/docs/src/ai/instructions.md | 20:05:08Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` | "Project instructions override personal `AGENTS.md` when they conflict." | `docs/src/ai/instructions.md:40` |
| G4 | Zed docs source tree, replaced Rules page | https://raw.githubusercontent.com/zed-industries/zed/main/docs/src/ai/rules.md | 20:05:08Z | 200 | 1,657 | `c8e775ec6a182444ae75b3805459c4a2d3069ceec1d7a038051d4af99884fce5` | "Starting in Zed v1.4.0, on-demand Rules and the Rules Library have been replaced by Skills." | `docs/src/ai/rules.md:10` |
| G5 | Zed release notes | https://zed.dev/releases | 20:05:33Z | 200 | 1,935,695 | `e17e20ab3731231541425b656047bf75864cc893a2679b59c8104bd07972f6cc` | "Agent: Added support for a global `AGENTS.md` file alongside `settings.json` for user-wide instructions" | line 519, embedded payload `169:T2985` (release v1.4.0, `published_at` 2026-05-20T18:07:56Z) |
| G6 | loader source, pinned commit | https://github.com/zed-industries/zed (sparse clone, `HEAD` = `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e`, commit time 2026-10-22T18:50:17Z) | clone run after 20:05:33Z; `git rev-parse HEAD` resolved | git object, no byte count | commit `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e` | "pub const RULES_FILE_NAMES: &[&str] = &[" (nine names follow) | `crates/prompt_store/src/prompts.rs:22-32` |
| G7 | personal-file loader | same clone | same clone | git object | same commit | "The file is read in full, mirroring how project rules / repo `AGENTS.md` files are loaded by the native agent today." | `crates/agent_settings/src/user_agents_md.rs:13-14` |

Stability: G1 re-fetched at 20:12:06Z, 200, 3,169 B, byte-identical (`7c63efe0…`). G5 re-fetched at 20:12:08Z, 200, 1,935,695 B, sha256 `508d25d54858def74e133d3164793275c2a5a3384f69bfcfe81712f1f689d0f6`: 93 differing bytes, all inside the `<meta name="sentry-trace">`/`baggage` header token; the v1.4.0 entry is unchanged at line 519. The quote above is anchored to the G5 bytes.

Other fetch results (recorded as routes, not rows): `https://zed.dev/docs/ai/rules` → 404, 142,258 B (both `.md` and HTML); `https://zed.dev/changelog` → 404, 234,797 B; `https://api.github.com/repos/zed-industries/zed/git/trees/main?recursive=1` → 403, 280 B, `API rate limit exceeded`; `https://github.com/zed-industries/zed/releases/tag/v1.4.0` → 404; `https://zed.dev/docs/llms.txt` → 200, 29,371 B, `75bc3bbd…` (index only, used to locate the live page).

# Q30 sweep (three parts, all executed)

1. **Release notes:** `https://zed.dev/releases` (G5, 519 lines, last unterminated; 1,935,695 B). Term counts in the fetched bytes: `AGENTS.md` 8, `instruction` 12, `symlink` 27, `.rules` 0, `stale` 32, `expire` 5. Every hit was inspected in context: the only instruction-file entries are the v1.4.0 note (skills, global `AGENTS.md`, "Removed the rules library and replaced it with skills support.") and a later bug fix "commit message generation not respecting instructions from global `AGENTS.md`". The 27 `symlink` hits concern the project panel, worktree scanning, `scan_symlinks`, git diffs and *skills* directories — none concerns instruction files.
2. **Current docs source tree** (not only the rendered page): clone at `cfb894a`, `git sparse-checkout add docs/src` → 1.7 MB, `docs/src/ai/{instructions,rules,skills,agents,agent-settings,agent-panel,external-agents}.md` present. `grep -rniE 'symlink|@AGENTS|import|size limit|truncat|token limit|character limit|dated|stale|transient|expire' docs/src/ai/*.md` → the only instruction-relevant symlink line is `skills.md:199` (skills root). `grep -rn 'AGENTS\.md' docs/src --include='*.md'` → 15 lines across 4 files, all prose or the G1/G4 lists. `grep -rn 'cursorrules\|clinerules\|windsurfrules' docs/src` → 6 lines, all in `instructions.md` and `rules.md`.
3. **Lane corpus:** `grep -rniIE --include='*.md' '\bzed\b' corpus` → **0 lines**; no SOURCES row S001–S042 concerns Zed. The 40 case-insensitive substring hits are incidental (`recognized`, `sized`, `normalized`). No prior lane fact about Zed instruction files exists to contradict or reuse.

Conclusion: "Zed documents nothing about `@`-imports for instructions, instruction-file symlinks, instruction size limits, or dated/transient instruction content" is a Q30-complete negative, not `not checked`.

# Draft SOURCES.md rows

Place at the end of the Registry table; ids left as `S0xx` for the L1 to assign (42 rows exist, so S043–S045). Cells contain no `|`.

| S0xx | Zed — Agent Instructions (served markdown, verified against the docs source tree) — https://zed.dev/docs/ai/instructions.md | docs | A | Which always-on instruction filenames the Zed Agent loads, in what order, and how personal and project files combine | § Personal Instructions (`instructions.md:11-21`), § Project Instructions (`:23-37`), § Instruction File Support (`:39-48`), § Migrating from Rules (`:57-63`); fetched 2026-10-22T20:05:08Z (200, 3,169 B, sha256 `7c63efe0…`), byte-identical on re-fetch 20:12:06Z; body identical to `docs/src/ai/instructions.md` at commit `cfb894a5` (frontmatter only differs) | Zed uses the first matching project instruction file from a fixed nine-name ordered list that starts `.rules`, `.cursorrules`, `.windsurfrules`, `.clinerules` and ends `CLAUDE.md`, `GEMINI.md`, and never merges two of them | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |

| S0xx | zed-industries/zed — instruction-file loader at commit `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e` — https://github.com/zed-industries/zed/tree/cfb894a5dde8ccf3fba1659164f47fdd1c024e2e | code | A | What the loader does when several recognised instruction files exist, whether imports or symlinks redirect it, whether it caps size, and where it looks for files | `crates/prompt_store/src/prompts.rs:22-32` (name list); `crates/agent/src/agent.rs:1515-1533` (first-match, file-kind filter, no emptiness test), `:1619-1629` (reload triggers); `crates/agent/src/templates/system_prompt.hbs:248-274` (personal then project, verbatim insertion); `crates/worktree/src/worktree.rs:4028-4034,4156-4168,4212-4214`; `crates/fs/src/fs.rs:1106-1117`; `crates/agent_settings/src/user_agents_md.rs:1-14`; main tip 2026-10-22T18:50:17Z, sparse clone | The loader takes only the first existing name per worktree root, reads instruction text in full with no size cap, expands no `@`-import, and — because symlink metadata follows the target — treats a symlinked instruction file as a file | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |

| S0xx | Zed — Release Notes (v1.4.0 entry, embedded payload `169:T2985`) — https://zed.dev/releases | docs | A | When the Rules library was removed and what replaced it (skills plus a global `AGENTS.md`) | v1.4.0, `published_at` 2026-05-20T18:07:56Z, payload `169:T2985` at line 519 of the fetched page; fetched 2026-10-22T20:05:33Z (200, 1,935,695 B, sha256 `e17e20ab…`); re-fetch 20:12:08Z differs only in the sentry header token (`508d25d5…`, same size) | The version that removed the Rules library in favour of Skills also introduced the user-global `AGENTS.md`, so "rules" and "instructions" name different eras of the same feature | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |

Caveat for the L1: `mined` presumes `corpus/knowledge/alwayson-rule-files-round53.md` lands with a `source:` citing these rows; that file does not exist yet (`ls corpus/knowledge | grep -i alwayson` → `alwayson-checklist-round7.md` only). If it does not land, the status must be `queued`.

# Rejected candidates

- `https://zed.dev/docs/ai/rules` and `…/rules.md` — 404 (142,258 B error page, sha256 `8047cff5…`). The route is gone; the live page is `/docs/ai/instructions`, with a repo-side stub at `docs/src/ai/rules.md`. Not a source, a dead route.
- `https://zed.dev/changelog` and `…/changelog.md` — 404 (234,797 B, `07a249d7…`). Release notes live at `/releases`; no separate changelog route exists.
- `https://api.github.com/repos/zed-industries/zed/…` — 403 rate-limit body. The docs tree was taken from the pinned clone instead; no authentication was attempted.
- `https://github.com/zed-industries/zed/releases/tag/v1.4.0` — 404. Version metadata and the note body came from `/releases`.
- Third-party restatements surfaced by search and **not opened**: `openagenticplatform.com/knowledge-base/zed`, `projects.localizethedocs.org/zed-docs-l10n/en-us/main/ai/rules.html`, `thepromptshelf.dev/blog/zed-editor-agents-md-ai-rules-setup-guide-2026/`, `automatelab.tech/blog/ai-coding/claude-md-agents-md-cursorrules/`. Tier C at best (community), not authoritative, and the vendor page plus the pinned source answer every question; a row would duplicate with less standing.
- `koriebruh/zed-mod` fork of `docs/src/ai/rules.md` — a fork of an upstream file; the upstream commit is authoritative.
- Zed's own root `.rules` (`git show HEAD:.rules`, Rust coding guidelines) — evidence of dogfooding, not a source row: it teaches nothing about the loader beyond the name list already cited.

# Findings that bear on C2 / alwayson.07 (not on the frozen counter)

- The checklist's two-name framing (`AGENTS.md` **or** `CLAUDE.md`) understates Zed's arbitration: six other names outrank both, and `AGENT.md` (singular) is a separate entry. A live-population check that only looks for `AGENTS.md`/`CLAUDE.md` would score a repo with `.cursorrules` + `AGENTS.md` as clean while Zed reads the `.cursorrules` only.
- With `AGENTS.md` and `CLAUDE.md` both present and no redirect, Zed reads `AGENTS.md` and Claude Code reads `CLAUDE.md` (the counter's own Claude Code basis) — two independent rule files in force across two clients, which is exactly what alwayson.07 forbids.
- An empty higher-priority file silently wins; an instrument for box 07 should treat a zero-byte `.rules`/`.cursorrules` as a discriminator, not as "no rule file".
- For Zed the two redirect forms the counter pins behave differently: the `@AGENTS.md` import is literal text (no loader support), while a symlink does load its target — so the knowledge entry must not generalise "a redirect works" across clients. This is knowledge-layer wording; the counter's pinned cases and expected statuses are untouched.

# Limits

- `zed` is not installed on this host, so every runtime behaviour above is [INFERENCE] from the pinned source, not an executed observation. No headless browser, no bot-challenge circumvention, no paid model call (`claude`/`codex`/`opencode`/`gemini` CLIs were not invoked), no `ask`, no `model` parameter.
- The code statements are bounded to the crates checked out at `cfb894a5` (`agent`, `agent_settings`, `project`, `prompt_store`, `worktree`, `fs`, `docs/src`). `git ls-tree -r HEAD | grep -iE 'rules|instruction'` shows no other rules-loading module outside `crates/prompt_store/src/rules_to_skills_migration.rs` (migration only) and grammar token-rule JSON, so the single loader is the one read.
- No lane file was edited. Installs: none. Host binaries unchanged.

# Touched surfaces

- Written: `.ufo/waves/round-53/build/ScribeZed.md` (this report).
- Scratch: `/fast/scratch/hyaku/kotoba-r53/ScribeZed/` — `clone/` (lane clone at `3bb0a7a3…`, `git rev-parse HEAD` printed `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`), `src/` (fetched bytes: `zed_instructions.md`, `zed_instructions.html`, `zed_src_instructions.md`, `zed_src_rules.md`, `zed_releases.html`, `zed_llms.txt`, `zed_relnotes_doc.md`), `zed/` (sparse clone at `cfb894a5`).
- Commands with outcomes: `git clone -q --filter=blob:none --depth 1 --sparse` produced a worktree whose `git rev-parse HEAD` is `cfb894a5dde8ccf3fba1659164f47fdd1c024e2e`; `git sparse-checkout set crates/agent crates/agent_settings crates/project docs/src/ai` exit 0; `git sparse-checkout add crates/prompt_store` exit 0; `git sparse-checkout add crates/worktree crates/fs` exit 0; `git sparse-checkout add docs/src` exit 0; `git show HEAD:.rules` exit 0. Lane git/jj untouched.

# Out of scope

C1 opencode 1.19.4 re-derivation, the alwayson instrument implementation and its fixtures, the corpus-integrity baseline, the MCP counter mutants, and the knowledge entry itself — all other seats. This seat supplies source facts, rows and the Gate record only.
