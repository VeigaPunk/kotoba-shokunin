Result: HOLDS — all three specified mechanisms remain NOT ELIGIBLE for frozen C1, but each supports an author action; “directory-scoped” must describe discovery, not promise per-file applicability or automatic unloading.

# CriticNegativeRows — prerecord review

## Scope and axes

- Reviewed the W0 census reasons, not an observed final SOURCES/entry/SKILL row. At inspection, the build directory listed only `swarm-registry.json`. Conditional BREAKS below identify wording the forthcoming rows must not introduce, not defects falsely attributed to an unwritten row.
- Primary axis: **depth** — preserve the actionable technical distinction between directory discovery and a rule's path-pattern applicability key. Also at risk: calibration/provenance (claiming more than the cited snapshot says) and operability (placement advice missing the discovery trigger).
- Frozen authority read: `verifiers/check_scoped_rules.py:11-26,72-138,155-183`; plan `plans/round-60.md:102-110,125-153`. The rule, counter, target, census eligibility and source-id assignments are unchanged by this review. HOLDS/BREAKS here describes the reviewed wording, not round admission or a canonical judgment.
- W0 evidence read: `.ufo/waves/round-60/w0/CensusCodex.md:26-46,95-113`; `CensusGeminiCLI.md:22-79,90-105`; `Censusopencode.md:25-94,127-143,168-174`.

## Per-row result

| Row | NOT ELIGIBLE / directory-discovery explanation | Page-alone author action | Smallest safe correction |
|---|---|---|---|
| Codex / S104 | **HOLDS** — a startup instruction chain selected by the root-to-current-directory walk, with `AGENTS.override.md` preferred within each directory. Not automatic discovery whenever a nested work file is touched. | Create the nested override and start Codex from that directory. | Say **startup/cwd-scoped**, and include the starting-directory requirement; do not offer placement alone as a JIT mechanism. |
| Gemini CLI / S107 | **HOLDS** — workspace/ancestor discovery plus JIT directory/ancestor discovery up to a trusted root. | [INFERENCE from the documented scan] Put `GEMINI.md` in the component directory whose guidance should be discovered when a tool accesses that area. | Say **JIT directory discovery**, not “no scoping/action,” and do not promise context is unloaded when subsequent work leaves that directory. |
| opencode / S109 | **HOLDS** — directory-based `AGENTS.md` discovery; `instructions` selects additional instruction sources, not the work files to which a rule applies. | V1 page: put project rules in project-root `AGENTS.md`; its local discovery walks upward from the current directory. V2 page expressly supports placement near the covered code and nested read/list-triggered discovery. | Keep the action within the pinned page/version. Do not attribute V2 nested discovery to the V1 snapshot, call configured globs applicability filters, or call combined guidance an override hierarchy. |

The affirmative actions do **not** make these mechanisms C1-eligible. Bare `AGENTS.md`, `AGENTS.override.md` and `GEMINI.md` fail the frozen dot-led/multi-segment token rule; AGENTS names also hit the banned `agents` segment word (`check_scoped_rules.py:75-95`). The inspected configuration examples name context/instruction sources, not a frontmatter key binding an instruction file to matching work paths. This is an exclusion from the frozen mechanism, not a claim that these clients lack useful scoped guidance.

## 1. Codex — HOLDS, with a startup/cwd boundary

Source: [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md.md), fetched bytes `codex-agents.page` in the sandbox below.

Evidence, literal excerpts from those bytes:

- `codex-agents.page:9`:
  > Codex builds an instruction chain when it starts (once per run; in the TUI this usually means once per launched session).
- `codex-agents.page:64`:
  > 2. Add overrides in nested directories when specific teams need different rules. For example, inside `services/payments/` create `AGENTS.override.md`:
- `codex-agents.page:75`:
  > 3. Start Codex from the payments directory:
- `codex-agents.page:83`:
  > Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible.

Line 12 specifies the root-to-cwd walk, the `AGENTS.override.md` / `AGENTS.md` / fallback order, and at most one file per directory. Line 13 describes nearer guidance overriding earlier guidance. These are directory-selected startup instructions, not a frontmatter path-pattern rule.

**Strongest counterexample:** [INFERENCE directly from lines 9, 12 and 83] start a run at the repository root, then ask it to inspect `services/payments/...`. Merely putting `services/payments/AGENTS.override.md` there does not establish that this run discovers it: the documented startup walk stops at the root cwd. No client invocation was made; this is a documentation counterexample, not an observed runtime test.

**Action from the page:** create `services/payments/AGENTS.override.md` for that area's different rules and start a new run from `services/payments`. Both placement and launch location are explicit, so the action need not be invented.

**Conditional BREAKS:** “Codex cannot scope instructions,” “no author action,” or “nested AGENTS automatically loads when its files are accessed.” The first two throw away the page's own action; the third substitutes Gemini/V2-opencode discovery semantics for Codex's documented startup semantics.

**Impacted axes / correction:** depth and operability. Add the startup/cwd qualifier and the launch-location clause; keep NOT ELIGIBLE and a non-key Scope key cell.

## 2. Gemini CLI — HOLDS, with discovery rather than an unloading guarantee

Source: [Provide context with GEMINI.md files](https://geminicli.com/docs/cli/gemini-md.md), fetched bytes `gemini-context.page`.

Evidence, literal excerpts:

- `gemini-context.page:31`:
  > - **Location:** When a tool accesses a file or directory, the CLI
- `gemini-context.page:32-33` (original line break and indentation retained):
  ```text
      automatically scans for `GEMINI.md` files in that directory and its
      ancestors up to a trusted root.
  ```
- `gemini-context.page:34-35` (original line break and indentation retained):
  ```text
    - **Scope:** Lets the model discover highly specific instructions for
      particular components only when they are needed.
  ```
- `gemini-context.page:15`, contiguous excerpt:
  > sends them to the model with every prompt.
- `gemini-context.page:105`:
  ```text
    "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]
  ```

Lines 13-16 say found context files are concatenated and sent with every prompt. Lines 20-21 describe the home `~/.gemini/GEMINI.md` as defaults for all projects, unlike JIT discovery. Lines 96-105 explain `context.fileName` as changing the context filename(s), not matching work paths.

**Strongest counterexample:** [INFERENCE from lines 13-16] after a component's JIT context is found, the page does not establish that moving to a different component removes it from subsequent prompts. Thus “applies only while working on that directory's files” claims more than the cited discovery mechanism supports. This review does not assert a runtime unload behavior.

**Action from the page:** [INFERENCE, not an imperative quoted from the page] place the component's `GEMINI.md` in the relevant directory below the trusted root, so the documented tool-access scan can find it. The necessary filename, placement relationship and trigger are all supplied by this page. Calling this “no author action” merely because there is no frontmatter glob key would be false.

**Conditional BREAKS:** treating all Gemini context as always-on global context; claiming directory guidance cannot be authored; treating `fileName` as an applicability glob; or promising automatic unloading. None follows from these bytes.

**Impacted axes / correction:** depth and calibration. Keep the negative C1 classification, explicitly name JIT directory/ancestor discovery, and present placement as the page-grounded action rather than inventing a matching-path key.

## 3. opencode — HOLDS, but separate V1, V2 and configured source selection

Sources: [V1 rules](https://opencode.ai/docs/rules.md), fetched as `opencode-v1.page`; [V2 instructions](https://opencode.ai/v2/docs/instructions/), fetched separately as `opencode-v2.page`. They are different documents and hashes.

V1 evidence:

- `opencode-v1.page:64`:
  > Place an `AGENTS.md` in your project root for project-specific rules. These only apply when you are working in this directory or its sub-directories.
- `opencode-v1.page:94`:
  > 1. **Local files** by traversing up from the current directory (`AGENTS.md`, `CLAUDE.md`)
- `opencode-v1.page:126`:
  > All instruction files are combined with your `AGENTS.md` files.

The example at V1 line 111 lists `CONTRIBUTING.md`, `docs/guidelines.md` and `.cursor/rules/*.md` as instruction sources; line 141 similarly lists `packages/*/AGENTS.md`. Those are globs over instruction files to combine. They do not attach a rule to a glob of work files. V1 also offers a distinct prompt-directed external-file-loading approach (`:145-179`); do not turn the directory summary into an exhaustive claim that every other conditional technique is absent.

V2 evidence:

- `opencode-v2.page:17`, first sentence:
  > Place `AGENTS.md` in the directory where its guidance should apply.
- `opencode-v2.page:45`, second sentence:
  > Reading a file or listing a directory loads any `AGENTS.md` files between that target and the workspace.
- `opencode-v2.page:35`, final sentence:
  > OpenCode combines the files and does not resolve conflicts between them.
- `opencode-v2.page:57`, first sentence:
  > Nested files are loaded nearest-first and deduplicated while their instruction entry remains in model-visible history.
- `opencode-v2.page:101`:
  > Use the `instructions` array to add files, glob patterns, or HTTP(S) URLs alongside discovered `AGENTS.md` files:

**Strongest counterexamples:**

1. **False provenance:** a row pinning V1 `/docs/rules.md` cannot cite its snapshot as evidence for V2's read/list-triggered nested discovery. V1's opened page explicitly supplies project-root placement and upward cwd discovery; the separate V2 page supplies the stronger nested-discovery statement. Using that statement without the V2 source would manufacture support.
2. **Wrong match target:** [INFERENCE from V1 :111/:126/:141 and V2 :101/:115] configuring `packages/*/AGENTS.md` selects instruction files for combination, not “apply package A's rule only while working on package A's code.” A source-file glob must not be presented as a work-file applicability key.
3. **Wrong authority/lifetime:** V2 says combined files do not resolve conflicts and nested instructions remain in history. “A nearer rule overrides broader rules,” copied from Codex, or “the rule stops applying as soon as work moves elsewhere,” is not supported here.

**Action from the page:** V1 alone supports putting project rules in root `AGENTS.md` and explains the upward cwd search. V2 alone explicitly supports placing more specific `AGENTS.md` guidance near its code and discovering it through reads/listings. The action is available, but its precise trigger must match the actual snapshot.

**Conditional BREAKS:** a blank/no-action row, a source-selection glob mislabeled as scope, V2 assertions cited to V1, or a fabricated override hierarchy.

**Impacted axes / correction:** depth plus provenance/calibration and operability. If S109 pins the V1 page, keep the V1-supported placement/cwd action and leave the V2 observations in supporting discussion unless separately sourced. If the chosen snapshot is V2, cite its own placement/discovery lines. No change to the frozen rule or eligibility is needed.

## Evidence receipts and limits

All fetched files are under:

`/fast/scratch/hyaku/kotoba-r60/CriticNegativeRows/`

Sandbox setup command (exit 0, no output):

```sh
timeout 60s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows && timeout 30s git -C /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows checkout -q b1cd64bb45eee744c4ec93be8631f1eddb28fddd
```

Each fetch ran from that sandbox using the following command shape, expanded to the URL and stem in the table (each complete command exited 0):

```sh
timeout 5s date -u && timeout 45s curl -sS -L --max-time 35 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -D STEM.headers -o STEM.page -w 'HTTP %{http_code}; final %{url_effective}; bytes %{size_download}\n' URL && timeout 5s wc -c STEM.page && timeout 5s sha256sum STEM.page && timeout 5s printf 'exit 0\n'
```

The `date -u` output for every fetch was exactly:

```text
Fri 23 Oct 2026 12:08:33 PM UTC
```

Observed outputs (final URL equaled the requested URL in each case):

| Stem | Requested/final URL | HTTP | `wc -c` / curl bytes | `sha256sum` |
|---|---|---|---|---|
| codex-agents | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 200 | 9149 / 9149 | 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e |
| gemini-context | https://geminicli.com/docs/cli/gemini-md.md | 200 | 3816 / 3816 | e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2 |
| opencode-v1 | https://opencode.ai/docs/rules.md | 200 | 6684 / 6684 | dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54 |
| opencode-v2 | https://opencode.ai/v2/docs/instructions/ | 200 | 5618 / 5618 | 56162c66b6124de0591d8b902f5e0c9dee3ca03a468985aabb64808630f5c957 |

These hashes also equal the respective W0 page hashes printed in the census reports. Actual evidence extraction used successful ranged `read` calls on the fetched files, not descriptions of the pages. No Markdown/backtick stripping or word-count assertions are used. Quotes are contiguous excerpts; omitted surrounding sentences/list prefixes remain outside the quote, not silently rewritten. For Gemini's line-31 excerpt the four indentation spaces precede the quoted bullet and are not asserted as quote content; the other multi-line Gemini excerpts preserve their shown line breaks and indentation.

Exact line-selection reproductions, provided as recipes rather than commands claimed executed here:

```sh
sed -n '9p;64p;75p;83p' /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows/codex-agents.page
sed -n '13,16p;31,35p;105p' /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows/gemini-context.page
sed -n '64p;94p;111p;126p;141p' /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows/opencode-v1.page
sed -n '17p;35p;45p;57p;101p;115p' /fast/scratch/hyaku/kotoba-r60/CriticNegativeRows/opencode-v2.page
```

Limits: no counters, measurements, self-tests, client/model calls, runtime probes or alternate judge were run. No claim of client-wide silence is made: the W0 three-leg sweeps were read, not repeated in this assignment. No lane content was edited, integrated or committed; the only lane write is this report. No sandbox commits and no tool installations/updates.

## Smallest safe disposition

Keep all three frozen NOT ELIGIBLE classifications. Give each negative row its real placement action and its own discovery trigger; do not conflate exclusion from C1 with lack of useful directory guidance. Preserve the distinction between Codex startup precedence, Gemini JIT context discovery, and opencode's version-specific discovery plus source combination. These are fixable wording/provenance issues, not grounds to alter the counter, target or census after freeze. No admission or tradeoff ruling is made by this critic.

Report: .ufo/waves/round-60/build/CriticNegativeRows.md
