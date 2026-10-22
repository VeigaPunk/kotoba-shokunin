Result: DONE — Codex reads exactly one instruction file per directory, chosen by name as `AGENTS.override.md` → `AGENTS.md` → `project_doc_fallback_filenames` (default `[]`, so `CLAUDE.md` and `GEMINI.md` are never read); it documents no `@AGENTS.md` import and no symlink rule for rule files, caps the combined text at `project_doc_max_bytes` (32 KiB default), and states no dated/transient rule; seven SOURCES rows drafted, nine candidates excluded with reasons.

Round 53, wave 1 (build), C2 source basis. Seat `KotobaR53.ScribeCodex`. Target client: OpenAI Codex (CLI + the shared instruction loader). Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Nothing in the lane was written except this file; every fetched byte lives under `/fast/scratch/hyaku/kotoba-r53/ScribeCodex/`. No tool was installed or upgraded (none was needed); no model call of any kind was made; no Codex binary was executed.

## 1. Method and route

All sources were opened with plain `curl -sSL -o <file> -w '%{http_code} %{size_download}'` from `/fast/scratch/hyaku/kotoba-r53/ScribeCodex/src/` and hashed with `sha256sum`; quotes are against those bytes, with line numbers in the fetched file. Fetch times are the shell's `date -u` at the fetch (`2026-10-22T20:08:31Z`–`20:08:33Z` for the Gate table; the wider sweep ran `20:05`–`20:08Z`). Every admitted page returned 200, and each page's sha256 was identical between the sweep fetch and the Gate fetch, so no source moved during the run (Q10).

The routes the brief named behave like this (all `curl` with `-L`, 2026-10-22T20:05Z):

| probe | result |
|---|---|
| `https://developers.openai.com/codex/guides/agents-md.md` | 308 → `https://learn.chatgpt.com/docs/agent-configuration/agents-md.md`, 200, 9,149 B — the page |
| `https://developers.openai.com/codex/agents-md.md` | 308 → `https://learn.chatgpt.com/docs/agents-md.md`, 404 (9 B) |
| `https://developers.openai.com/codex/config-reference.md` | 308 → `https://learn.chatgpt.com/docs/config-file/config-reference.md`, 200, 136,297 B |
| `https://developers.openai.com/codex/config.md` | 308 → `https://learn.chatgpt.com/docs/config.md`, 404 (9 B) |

The `.md` forms exist (the bare 308 body is 15 B, i.e. the redirect stub), but only at the paths the site's own index names. `https://learn.chatgpt.com/llms.txt` (200, 33,447 B, sha256 `fc7b20ea…`) is the complete documentation index: 196 `.md` links, of which 191 return 200 (5 are 404: `docs.md`, `guides/best-practices.md`, `resources.md`, `guides/build-ai-native-engineering-team.md`, `videos.md`). I fetched all 196 into `docsall/` (6.0 MB) and grepped them as one corpus; that corpus is the documentation leg of every sweep in §4.

The site's authoring source is not public: the page HTML carries no edit link (only `github.com/openai/openai-cookbook` appears, `agents-md.html`, 200, 409,154 B), and `openai/codex`'s own `docs/` tree holds three-line pointers, not page content (`docs/agents_md.md`, 126 B: "For information about AGENTS.md, see [this documentation](https://developers.openai.com/codex/guides/agents-md)."). So the docs-source-tree leg below is the client repo's `docs/` tree at a pinned commit plus the full live corpus; the site source itself is recorded as not publicly reachable, not as absent.

## 2. Answers

### 2.1 Which always-on file names it reads

`agents-md.md` (9,149 B, sha256 `9d1f87a2…`) § How Codex discovers guidance, `:9`:

> Codex builds an instruction chain when it starts (once per run; in the TUI this usually means once per launched session).

(21 words.) The name list is closed and ordered, `:12`:

> In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`.

(18 words.) Global scope, `:11`:

> Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`.

(10 words.) And `:11` again: "Codex uses only the first non-empty file at this level." (10 words.)

The fallback list defaults empty. `config-sample.md` (34,474 B, sha256 `626f16ae…`), § Project Documentation Controls, `:286`:

> Ordered fallbacks when AGENTS.md is missing at a directory level. Default: []

(12 words; the assignment `project_doc_fallback_filenames = []` is `:288`.) Therefore the names Codex reads out of the box are **`AGENTS.override.md` and `AGENTS.md`**, in `~/.codex` (or `$CODEX_HOME`) and in each directory from the project root down to the cwd. `CLAUDE.md` and `GEMINI.md` are not read: `:159` closes the set —

> Filenames not on this list are ignored for instruction discovery.

(10 words.) `GEMINI.md` occurs **0 times** in the 191-page corpus; `CLAUDE.md` occurs only as a migration input (§2.3).

### 2.2 When two of them exist in one directory

One wins, by order, and the loser is dropped rather than merged. `:12`, second sentence:

> Codex includes at most one file per directory.

(8 words.) The page's own example tree marks the loser, `:104-105`: `AGENTS.md` with the comment "Ignored because an override exists" (5 words). Across directories the survivors are concatenated, `:13`:

> Codex concatenates files from the root down, joining them with blank lines.

(12 words.) Later files override earlier ones because they appear later in the prompt (`:13`).

So for `AGENTS.md` + `CLAUDE.md` in one repo root, the answer is not "combine" and not "nearest wins": Codex reads `AGENTS.md`, and `CLAUDE.md` is not a candidate at all. For `AGENTS.md` + `AGENTS.override.md`, the override wins and `AGENTS.md` is ignored. The documented order with a configured list is spelled out at `:159`:

> Now Codex checks each directory in this order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`.

(12 words.)

### 2.3 Does it honour a redirect

The levers Codex documents are a config-supplied name list and a fixed override name; neither is a pointer from inside another file. **No, the file-content form is not honoured; there is no documented `@AGENTS.md` import.**

- **Config pointing at another name — yes, and it is the documented lever.** `:147`: "add it to the fallback list so Codex treats it like an instructions file" (14 words). `config-advanced.md` (54,760 B, sha256 `6180e9e2…`), § Project instructions discovery, `:773`: "additional filenames to try when `AGENTS.md` is missing at a directory level" (12 words). Two bounds: the fallback is consulted only when `AGENTS.md` is missing, so an existing `AGENTS.md` shadows it; and an entry is a *filename*, not a path — the loader warns and drops any entry containing a separator (§2.6, code `:288`).
- **`AGENTS.override.md` — yes, as a precedence slot, not as a pointer.** It is a second fixed name in every directory, not a file that names another file (`:12`, `:64`; and `git-worktrees.md:152` for the worktree copy).
- **`@AGENTS.md` inside `CLAUDE.md` — not honoured and not documented.** `grep -rn '@AGENTS\|@import' docsall/` over all 191 pages returns 0 hits, and the loader reads the selected file's bytes verbatim with no line scanning (code `:150-169`, §2.6). The `@` mechanism Codex does document is a *composer* one — `prompting.md:389`: "You can use `@` in the composer to insert file paths from the workspace, or `/mention` to attach a specific file." (21 words) — which attaches context to a prompt and says nothing about expanding a directive inside a rule file.
- **Symlink — not documented for rule files, allowed by the loader.** `symlink` appears in 4 of 191 pages, none about instruction files: `build-skills.md:149` ("Codex supports symlinked skill folders…", 8 words, skills only), `environments/git-worktrees.md:152` (§2.6), `windows/wsl.md` (I/O performance on `/mnt/c`), and `codex-manual.md`, which is the compiled duplicate of the other three. The source comment is explicit, `codex-rs/core/src/agents_md.rs:190`: "directory, inclusive. Symlinks are allowed." (5 words.) Consequence, marked `[INFERENCE]` from that comment: a symlink **named `AGENTS.md`** pointing at `CLAUDE.md` is read; a symlink **named `CLAUDE.md`** pointing at `AGENTS.md` is never examined, because the name is not a candidate. So the symlink redirect works in one direction only, and only if the canonical name is the symlink.
- **`CLAUDE.md` is imported once, not read each run.** `import.md` (5,364 B, sha256 `34893c4d…`), `:5-6` (one sentence over a line wrap): "Use the import flow to bring instructions, settings, skills, plugins, projects, and recent work from another agent" (17 words); `:8`: "Codex CLI can import from **Claude Code** or **Cursor**." (9 words.) The API-level operation names the file move exactly, `app-server.md` (102,656 B, sha256 `f879715b…`), § Detect and import external agent config, `:1868`:

  > Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.

  (5 words.) That is a migration that writes `AGENTS.md`, not a runtime redirect.

### 2.4 Documented size limit

Yes, one, and it ships with a default. `:15`:

> Codex skips empty files and stops adding files once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB by default).

(22 words.) The sample config states the same number, `config-sample.md:282`: "Max bytes from AGENTS.md to embed into first-turn instructions. Default: 32768" (11 words; `project_doc_max_bytes = 32768` at `:284`). The remedy the docs give is to raise the knob or split the text across nested directories (`:15`, `:213`).

**Verbatim conflict, reported as-is.** `config-advanced.md:772` describes the same knob per file — "how much to read from each `AGENTS.md` file" (8 words) — while `agents-md.md:15` calls it a combined limit. The loader (`agents_md.rs:68`, `:150-161`) decrements one `remaining` counter across all files and truncates the file that crosses it, i.e. a single cumulative budget: the guide's "combined" wording matches the code, the advanced page's "each" wording does not. Reported for the canonical judge; I did not resolve it into a single sentence.

### 2.5 Dated or transient content

**No rule.** No page states that always-on text must be undated, dated, or free of transient status. `grep -n -i 'stale\|dated\|expire' gate-agents-md.md` returns three lines — `:157` and `:212` only because "updated" contains "dated" — and the only content-shaped one is `:206` ("If instructions look stale, restart Codex…"), which is about the per-run cache, not content. The closest content guidance is durability, in `customization/overview.md` (9,482 B, sha256 `e4f466bb…`):

- `:21` — "`AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work." (18 words.)
- `:23` — "Use it for the rules you want Codex to follow every time in a repo" (15 words.)
- `:32` — "Codify recurring review feedback, put guidance in the closest directory where it applies" (13 words.)

The transient lever Codex documents is a file, not a dating convention, `agents-md.md:47`:

> Use `~/.codex/AGENTS.override.md` when you need a temporary global override without deleting the base file.

(14 words.) So a temporary rule has a documented home (the override file), while dated text inside a durable file has no rule either way. Consequence for C2: alwayson.04 stays a lane craft rule (Q23); Codex supplies only the weaker "durable / every time / recurring" wording, and that wording is usable as the box's stated spirit, not as its test.

### 2.6 Two reach facts the instrument does not yet carry

- **An empty `AGENTS.md` blocks a fallback in the same directory.** The candidate loop returns the first path whose metadata says `is_file` (`agents_md.rs:254`), and only afterwards the read loop drops whitespace-only files (`:169`) without consulting the next candidate. The docs say "missing" for fallbacks (`config-advanced.md:773`) and "skips empty files" for the cap (`agents-md.md:15`), so the code is consistent with the config wording but the guide's sentence reads as if the search continues. `[INFERENCE]` from the code at the pin; not measured on a binary.
- **`AGENTS.override.md` is copied into managed worktrees, and the copy is automatic.** `environments/git-worktrees.md:152`: "Codex automatically copies an ignored `AGENTS.override.md` into local managed worktrees" (10 words). A local override therefore travels into the worktree whether or not the repo lists it in `.worktreeinclude`. Opened as a cross-check, not rowed (one line, secondary to S0xx row 1).

## 3. Bearing on the C2 counter (operability)

Counter: `verifiers/check_alwayson_boxes.py` at `3bb0a7a3`; the plan pins alwayson.07's PASS set as "4 PASS cases including the `@AGENTS.md` import and the symlink redirect".

| Counter case | Codex evidence | Effect |
|---|---|---|
| `alwayson.07` `import-redirect` (`CLAUDE.md` holds `@AGENTS.md`) | 0 hits for `@AGENTS`/`@import` in 191 pages; loader reads bytes verbatim (`agents_md.rs:150-169`) | **This PASS case is Claude Code's rule, not Codex's.** Codex never reads the file holding the import, so the redirect is invisible to it. The instrument must name Claude Code as the authority for this case (Q20/Q23) and the knowledge entry must not say "clients honour `@AGENTS.md`" |
| `alwayson.07` `symlink-redirect` | not documented for rule files; code comment allows symlinks (`:190`) | single-sourced on Claude Code in the docs; Codex corroborates only at source level and only for a symlink at the canonical name. A `CLAUDE.md` → `AGENTS.md` symlink is *not* a Codex redirect |
| `alwayson.07` `two-rule-files` | one file per directory, name-ordered (`agents-md.md:12`, `:159`) | for Codex this is not ambiguity: `AGENTS.md` wins and `CLAUDE.md` is not read. If the instrument fails a repo for carrying both, say the failure is a cross-client portability one (Q20), not a Codex load error |
| `alwayson.07` `prose-mention` → FAIL | an import would have to be a documented form; prose is not one | consistent with Codex |
| `alwayson.07` "one canonical rule-file name or an explicit redirect" | documented redirects: config `project_doc_fallback_filenames`, `AGENTS.override.md`, a symlink at the canonical name | a repo whose redirect is `@AGENTS.md` inside `CLAUDE.md` is redirected for Claude Code and **un-redirected** for Codex — the box's verdict is client-scoped |
| `alwayson.04` all four dated/transient FAIL cases | no vendor dating rule (§2.5) | keep the box rule lane-authored in the instrument's detail string (Q20/Q23) |

Practical route for the C2 instrument: it can keep Claude Code as the declared authority for the import and symlink cases, and should add Codex as the counter-witness that the same file pair is *silent* rather than ambiguous for a name-priority client. Two clients now disagree by design on co-existing files (Copilot CLI combines them, `ScribeCopilotCli.md` §2.2; Codex takes one), so a PASS/FAIL that does not name the client is a portability verdict.

## 4. Q30 sweeps for the negatives

Three negatives are asserted above: (a) no `@AGENTS.md`/import expansion, (b) no documented symlink behaviour for rule files, (c) no dating rule. Each names three legs.

**Changelog / release notes.** `openai/codex` `CHANGELOG.md` at `main` (200, 330 B, sha256 `c8458f99…`) is a pointer — "The changelog can be found on the [releases page](https://github.com/openai/codex/releases)." (9 words) — plus one unreleased bullet. `https://github.com/openai/codex/releases.atom` (200, 6,046 B, sha256 `80dafdc7…`) carries the 10 most recent entries; every `<content>` is a one-line title (e.g. "Release 0.164.0-alpha.12"), so there is no per-release prose to search, and `grep -io 'fallback\|symlink\|AGENTS'` over the feed returns nothing. The releases HTML page (200, 387,794 B, sha256 `c6972b2e…`) is a JS shell with no release prose. The vendor's product release notes that do carry prose are `docs/whats-new.md` (200, 62,433 B, sha256 `b250b91…`): one `AGENTS.md` hit, `:1086-1087` "automatic discovery of `AGENTS.md`, skills, and `config.toml`" (7 words; line wrap joined), about which folder the desktop app scans — nothing about imports, symlinks or dating. Scope limit: the atom covers the latest 10 releases only; I did not page through earlier release pages.

**Current docs source tree.** The site content source is not public (§1). Used instead: the client repo's `docs/` tree at pinned commit `8eaf5fd115f036d207be236009938261758e30f2` (`docs/agents_md.md` 126 B `56f5b602…`, `docs/config.md` 726 B `745768b4…`, both pointers to the live pages; the tree listing at that commit also shows `skills.md` and `example-config.md`, not opened), the site's complete index `llms.txt`, and a full-text grep of all 191 fetched pages. Results: `@AGENTS`/`@import` → 0 hits; `symlink|symbolic link` → 4 pages, none about instruction files; `GEMINI` → 0 hits; `CLAUDE.md` → 2 pages, both the migration action; `dated|expire|stale` in instruction prose → only the cache sentence.

**Lane corpus.** From the lane root, 2026-10-22: `grep -rn 'project_doc' corpus/` → 0 hits; `grep -rn 'AGENTS\.override' corpus/` → 0 hits; `grep -rn '@AGENTS\|@import' corpus/` → 0 hits; `grep -rn 'GEMINI' corpus/` → 7 hits, all the rival-name class in the always-on checklist and the round-13 census, none about Codex; the only "dated/transient" string is the box's own text, `corpus/knowledge/alwayson-checklist-round7.md:16` ("dates, expiring facts → status files"), which is lane-authored craft. No corpus row contradicts §2.

Verdicts: the import negative and the dating negative are complete sweeps. The symlink negative is recorded as **not checked** in the strict Q30 sense — the documentation says nothing, and the only positive statement is a source comment, so I do not upgrade Codex to "documents symlinked rule files".

## 5. Drafted SOURCES.md rows

Column shape copied from `corpus/SOURCES.md` § Registry (11 columns; no `|` inside a cell). `S0xx` is a placeholder for the next unused number. `used-by` is the path the assignment names; see §7.1.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | OpenAI Learn — Custom instructions with AGENTS.md — https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | docs | A | Codex's always-on instruction-file discovery: the filename order per directory, what happens when several exist, the redirect levers the docs name, and the documented size cap (vendor documentation for Codex; not a measurement of any installed CLI) | § How Codex discovers guidance (`agents-md.md:9-15`), § Create global guidance (`:47`), § Customize fallback filenames (`:145-159`), § Troubleshoot discovery issues (`:210-213`); fetched 2026-10-22T20:08:31Z (200, 9,149 B, sha256 `9d1f87a2…`); route `https://developers.openai.com/codex/guides/agents-md.md` → 308 → this URL, the path `docs/agents_md.md:3` names | In each directory from the project root down, Codex checks `AGENTS.override.md`, then `AGENTS.md`, then `project_doc_fallback_filenames` names, and includes at most one file; filenames not on that list are ignored, and the combined text stops at `project_doc_max_bytes` (32 KiB default) | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | OpenAI Learn — Configuration sample (config.toml reference) — https://learn.chatgpt.com/docs/config-file/config-sample.md | docs | A | The documented defaults for the two instruction-discovery knobs and the root marker they pair with (vendor documentation for Codex; not a measurement of any CLI) | § Project Documentation Controls (heading `config-sample.md:278`; comment `:282`, `project_doc_max_bytes = 32768` `:284`, comment `:286`, `project_doc_fallback_filenames = []` `:288`, `project_root_markers` `[".git"]` `:292`); § Instruction Overrides (`:120`, `developer_instructions` injects before `AGENTS.md`); fetched 2026-10-22T20:08:31Z (200, 34,474 B, sha256 `626f16ae…`) | The fallback list ships empty and the byte cap ships at 32,768, so `CLAUDE.md`/`GEMINI.md` are read only if a repo adds them by name; discovery walks up to the `.git` root marker by default | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | OpenAI Learn — Configuration advanced — https://learn.chatgpt.com/docs/config-file/config-advanced.md | docs | A | What the two instruction-discovery knobs do at a directory level, and the page's per-file wording of the byte cap (vendor documentation for Codex; not a measurement of any CLI) | § Project instructions discovery (`config-advanced.md:768-773`, knob list `:772-773`); fetched 2026-10-22T20:08:31Z (200, 54,760 B, sha256 `6180e9e2…`) | The fallback list is consulted only "when `AGENTS.md` is missing at a directory level", so a fallback name never outranks an existing `AGENTS.md`; the page describes the byte knob per file where the guide and the loader make it a combined budget | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | OpenAI Learn — Customization overview — https://learn.chatgpt.com/docs/customization/overview.md | docs | A | The content guidance Codex gives for an always-on file: durability, locality and recurring feedback (vendor documentation for Codex; not a measurement of any CLI) | § AGENTS Guidance (`customization/overview.md:19-45`: `:21`, `:23`, `:30`, `:32`, `:44-45`); fetched 2026-10-22T20:08:31Z (200, 9,482 B, sha256 `e4f466bb…`) | `AGENTS.md` is described as durable guidance for rules that apply "every time in a repo", updated by codifying recurring review feedback; the docs state no rule about dated or transient text | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | OpenAI Learn — Import from another agent — https://learn.chatgpt.com/docs/import.md | docs | A | How Codex takes over another client's always-on file: a one-time migration, not a run-time read (vendor documentation for Codex; not a measurement of any CLI) | § Import from another agent (`import.md:5-8`), § Import in Codex CLI (`:44-55`, availability limits `:52-55`); fetched 2026-10-22T20:08:32Z (200, 5,364 B, sha256 `34893c4d…`) | Codex CLI's `/import` migrates setup from Claude Code or Cursor once, so a `CLAUDE.md` reaches Codex only by being copied into Codex's own files, never by being loaded beside `AGENTS.md` | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | OpenAI Learn — App server (Codex app-server API) — https://learn.chatgpt.com/docs/app-server.md | docs | A | The API-level migration action that names the rival instruction file and its destination (vendor documentation for the app-server surface; not a measurement of any CLI) | § Detect and import external agent config (`app-server.md:1853-1900`, `AGENTS_MD` item `:1867-1868`, import call `:1880-1888`); fetched 2026-10-22T20:08:32Z (200, 102,656 B, sha256 `f879715b…`) | The migration item for an instruction file is literally "Import .../CLAUDE.md to .../AGENTS.md" with a `source` label, i.e. Codex resolves the rival name by copying it into `AGENTS.md` rather than by reading it | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | openai/codex — `codex-rs/core/src/agents_md.rs` at commit 8eaf5fd1 — https://raw.githubusercontent.com/openai/codex/8eaf5fd115f036d207be236009938261758e30f2/codex-rs/core/src/agents_md.rs | code | A | What the Codex instruction loader does with the candidate list: order, one-file-per-directory selection, symlink handling, path-syntax rejection, verbatim read and truncation (source at one commit; not a measurement of a shipped binary) | constants `:43-45`; discovery `:240-262` (`metadata.is_file` `:254`); `candidate_filenames` `:269-292` (`:274-275`, rejected-entry warning `:288`, dedup `:291`); read/truncate/empty-skip `:150-169`; doc comment `:189-190`; commit `8eaf5fd115f036d207be236009938261758e30f2` (main tip, 2026-10-22); fetched 2026-10-22T20:08:32Z (200, 20,104 B, sha256 `97427a87…`) | Discovery probes `AGENTS.override.md`, `AGENTS.md` then configured names and returns the first path that is a file, so exactly one file per directory is read; symlinks are allowed; a fallback entry containing a separator is ignored; the text is read verbatim (no import expansion) and truncated at the remaining byte budget | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |

### 5.1 Rejected candidates

| candidate | reason |
|---|---|
| `https://learn.chatgpt.com/docs/config-file/config-reference.md` (200, 136,297 B, sha256 `fe48af08…`, 20:05:05Z) | Opened, not rowed: its two entries (`:1273-1281`) say only "Maximum bytes read from `AGENTS.md` when building project instructions" and "Additional filenames to try when `AGENTS.md` is missing", i.e. the same two facts as row 3 with no default value. A row would duplicate row 3 for this scope (Q11 sizing). Flip: if the reference gains the defaults or a distinct rule. |
| `https://raw.githubusercontent.com/openai/codex/8eaf5fd115f036d207be236009938261758e30f2/docs/agents_md.md` (200, 126 B, sha256 `56f5b602…`) | Three-line pointer to the live page, no rule content — the same reason round 47 rejected the three-line spec pointer. Used as route provenance in row 1's anchor; not rowed. |
| `https://github.com/openai/codex/releases.atom` (200, 6,046 B, sha256 `80dafdc7…`) and `https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md` (200, 330 B, sha256 `c8458f99…`) | The changelog file is a pointer to the releases page and the feed's entries are one-line titles with no prose (`grep -io 'fallback\|symlink\|AGENTS'` → 0 hits), so neither carries a teachable sentence; a row would cite an artifact that states nothing. Kept as the changelog leg of §4. |
| `https://learn.chatgpt.com/docs/whats-new.md` (200, 62,433 B, sha256 `b250b915…`) | Product release notes with exactly one `AGENTS.md` line (`:1087`, desktop multi-folder discovery), which serves no claim here. Sweep witness only. |
| `https://learn.chatgpt.com/docs/build-skills.md` (200, 11,035 B, sha256 `ed6e324f…`) | The page is already **S021** (byte-identical hash `ed6e324f…` to the round-48/52 fetch). My only use is the symlink sentence at `:149`, which is scoped to skill folders; a second row would duplicate S021 and mis-scope its teach. Recorded as a cross-check in §2.3. |
| `https://learn.chatgpt.com/docs/agent-configuration/rules.md` (200, 6,783 B) | Opened, rejected as out of class: `.rules` files gate command approval (`prefix_rule`), not instruction text, and are read from config layers, not from the repository root. Not an always-on instruction surface. |
| `https://learn.chatgpt.com/docs/agents-md.md` (404, 9 B), `https://learn.chatgpt.com/docs/config.md` (404, 9 B) | Guessed developer-site routes that the redirect lands on as 404s; the canonical paths are `agent-configuration/agents-md.md` and `config-file/*`. A stale-path probe, no content. |
| `https://agents.md/` | Not opened by me this round; already queued as S004 and no claim of mine rests on it. Not admitted, not rejected on content. |
| `https://code.claude.com/docs/en/memory.md` | Out of my target client. The plan names it as C2's basis and assigns it to another wave-1 seat; I neither opened nor cited it, and every Claude Code statement above comes from the plan's own summary, marked as such. |

## 6. Gate record

| source | URL | UTC | HTTP | bytes | sha256 | quote | line |
|---|---|---|---|---|---|---|---|
| AGENTS.md guide | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 2026-10-22T20:08:31Z | 200 | 9,149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` | "In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`." | `agents-md.md:12` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Codex includes at most one file per directory." | `:12` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`." | `:11` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Codex uses only the first non-empty file at this level." | `:11` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Codex concatenates files from the root down, joining them with blank lines." | `:13` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Codex skips empty files and stops adding files once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB by default)." | `:15` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Filenames not on this list are ignored for instruction discovery." | `:159` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Now Codex checks each directory in this order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`." | `:159` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "add it to the fallback list so Codex treats it like an instructions file" | `:147` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Use `~/.codex/AGENTS.override.md` when you need a temporary global override without deleting the base file." | `:47` |
| AGENTS.md guide | same | same | 200 | 9,149 | same | "Ignored because an override exists" (FileTree comment on `AGENTS.md`) | `:105` |
| Config sample | https://learn.chatgpt.com/docs/config-file/config-sample.md | 2026-10-22T20:08:31Z | 200 | 34,474 | `626f16aed15a7c4906b5cfee22ec6f04d38fd5455f358a03b5f30342cf505d44` | "Max bytes from AGENTS.md to embed into first-turn instructions. Default: 32768" | `config-sample.md:282` |
| Config sample | same | same | 200 | 34,474 | same | "Ordered fallbacks when AGENTS.md is missing at a directory level. Default: []" | `:286` |
| Config sample | same | same | 200 | 34,474 | same | "Additional user instructions are injected before AGENTS.md. Default: unset." | `:120` |
| Config advanced | https://learn.chatgpt.com/docs/config-file/config-advanced.md | 2026-10-22T20:08:31Z | 200 | 54,760 | `6180e9e23da85dd2db17d47f59c719787c2bdf20fa95a9b41479183ab9337a3e` | "how much to read from each `AGENTS.md` file" | `config-advanced.md:772` |
| Config advanced | same | same | 200 | 54,760 | same | "additional filenames to try when `AGENTS.md` is missing at a directory level" | `:773` |
| Customization overview | https://learn.chatgpt.com/docs/customization/overview.md | 2026-10-22T20:08:31Z | 200 | 9,482 | `e4f466bb13521bc8d4e193962192c45319d5abc0cb58875d4a7eed2a9f9a20d6` | "`AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work." | `customization/overview.md:21` |
| Customization overview | same | same | 200 | 9,482 | same | "Use it for the rules you want Codex to follow every time in a repo" | `:23` |
| Customization overview | same | same | 200 | 9,482 | same | "Codify recurring review feedback, put guidance in the closest directory where it applies" | `:32` |
| Import | https://learn.chatgpt.com/docs/import.md | 2026-10-22T20:08:32Z | 200 | 5,364 | `34893c4daf7be033d4313dc188b3b0e5b89c11f2899d5a3e3cdbe8108f31fac7` | "Use the import flow to bring instructions, settings, skills, plugins, projects, and recent work from another agent" (line wrap joined) | `import.md:5-6` |
| Import | same | same | 200 | 5,364 | same | "Codex CLI can import from **Claude Code** or **Cursor**." | `:8` |
| App server | https://learn.chatgpt.com/docs/app-server.md | 2026-10-22T20:08:32Z | 200 | 102,656 | `f879715bb0d440db60b71e7a5bfe1258d045520feabe3fc6b11847100c8d064b` | "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md." | `app-server.md:1868` |
| Loader source | https://raw.githubusercontent.com/openai/codex/8eaf5fd115f036d207be236009938261758e30f2/codex-rs/core/src/agents_md.rs | 2026-10-22T20:08:32Z | 200 | 20,104 | `97427a870741b904a3f3c143f5990eaaa65b5bfa99ddac1808b2980052b5fc78` | "directory, inclusive. Symlinks are allowed." | `agents_md.rs:190` |
| Loader source | same | same | 200 | 20,104 | same | "ignoring project_doc_fallback_filenames entry that is not a filename" | `:288` |
| Docs index | https://learn.chatgpt.com/llms.txt | 2026-10-22T20:08:32Z | 200 | 33,447 | `fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943` | "Build with the Codex CLI, IDE extension, and cloud automation to speed up development." — index preamble; 196 `.md` links extracted, 191 live | `llms.txt:3` |
| Release feed | https://github.com/openai/codex/releases.atom | 2026-10-22T20:08:32Z | 200 | 6,046 | `80dafdc7bf500475a78391f29f77c8ed5839cfba0825f4d283792ecd287e6eea` | "Release 0.164.0-alpha.12" (entry body; no prose) | `:8-19` |
| Changelog pointer | https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md | 2026-10-22T20:08:33Z | 200 | 330 | `c8458f99de91a4b4b9682ecb72c396f0d08c03c51a657759e1239c3a14c697d5` | "The changelog can be found on the [releases page]" | `CHANGELOG.md:1` |
| Docs source pointer | https://raw.githubusercontent.com/openai/codex/8eaf5fd115f036d207be236009938261758e30f2/docs/agents_md.md | 2026-10-22T20:08:33Z | 200 | 126 | `56f5b6026b15fad40fe8b1f6f8910b9fccdf66da3b39dd943c91877e2299619e` | "For information about AGENTS.md, see [this documentation]" | `:3` |
| Product notes | https://learn.chatgpt.com/docs/whats-new.md | 2026-10-22T20:08:33Z | 200 | 62,433 | `b250b91542c15a0e8733d8f5a7ce2d33a6729f6a725663cebf8af331f6074c16` | "automatic discovery of `AGENTS.md`, skills, and `config.toml`" (line wrap joined) | `whats-new.md:1086-1087` |
| Prompting page (cross-check) | https://learn.chatgpt.com/docs/prompting.md | 20:05Z sweep | 200 | 22,794 | `c43142cb5c847afb5a2292abe9260667e9001563dceb4e48c0550809e10306f2` | "You can use `@` in the composer to insert file paths from the workspace, or `/mention` to attach a specific file." | `prompting.md:389` |
| Worktree page (cross-check) | https://learn.chatgpt.com/docs/environments/git-worktrees.md | 20:05Z sweep | 200 | 12,831 | `a664bda957392d9128c5fc58b661b1c5cc7a5d034838552ca95bf4b18f6875b5` | "Codex automatically copies an ignored `AGENTS.override.md` into local managed worktrees" | `git-worktrees.md:152` |
| Skills page (cross-check) | https://learn.chatgpt.com/docs/build-skills.md | 20:05Z sweep | 200 | 11,035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` | "Codex supports symlinked skill folders and follows the symlink target when scanning these locations." | `build-skills.md:149` |
| Full manual (duplicate render) | https://learn.chatgpt.com/docs/codex-manual.md | 20:05Z sweep | 200 | 3,150,484 | `c31bdc04a59d09b94add87a0db00753b11b6305aa7ea1e60aa8562c79c0cb73c` | — (restates `agents-md.md` at `:26920`, `:26923`; used only to confirm the rules repeat) | `codex-manual.md:26920` |
| Route probe | https://developers.openai.com/codex/guides/agents-md.md | 2026-10-22T20:05Z | 308 → 200 | 15 B stub → 9,149 | not hashed (stub) | — | — |
| Route probe | https://learn.chatgpt.com/docs/agents-md.md | 2026-10-22T20:05Z | 404 | 9 | not hashed | — | — |
| Route probe | https://learn.chatgpt.com/docs/config.md | 2026-10-22T20:05Z | 404 | 9 | not hashed | — | — |

Every quote is byte-exact in the named file and ≤25 words; the two FileTree/index entries are labelled as such rather than presented as prose.

## 7. Findings, limits, out of scope

1. **Row status is contingent.** `status: mined` requires the `used-by` path to exist. `corpus/knowledge/alwayson-rule-files-round53.md` does **not** exist at base (`ls corpus/knowledge/ | grep -i alwayson` lists `alwayson-checklist-round7.md` only). If that entry is not landed, all seven rows must be written `queued`, not `mined`, and the census would then find new rows with no use.
2. **The `@AGENTS.md` PASS case in alwayson.07 is not Codex's rule.** Codex documents no file-content import and its loader does not expand one. The case is sound only under Claude Code's authority; under Codex the same repo layout is un-redirected. The instrument's detail string should name the client whose rule makes the case pass, and the knowledge entry should not generalise it (Q20/Q23). This is the sharpest cross-client conflict found this round; the Copilot CLI report reached the same conclusion from the other side (that client does honour `@`-relative imports).
3. **The symlink redirect is direction-sensitive.** Codex reads a symlink named `AGENTS.md` (loader comment) and never reads one named `CLAUDE.md` (name not in the candidate list, default fallback `[]`). An instrument that treats "a symlink exists between the two names" as sufficient will pass a layout Codex cannot see. No client documentation states symlink behaviour for rule files — this stays a source-level fact, not a vendor rule.
4. **Doc-vs-doc conflict on the byte cap, reported verbatim.** `agents-md.md:15` "combined size" and `config-advanced.md:772` "from each `AGENTS.md` file" describe the same knob differently; the loader implements one cumulative budget (`agents_md.rs:68`, `:150-161`). The guide matches the code; the advanced page does not. Not resolved here.
5. **An empty `AGENTS.md` shadows a fallback in the same directory** (`agents_md.rs:254` selects on existence, `:169` then drops whitespace-only text). `[INFERENCE]` from the code at the pin; the docs say "missing" for fallbacks and "skips empty files" for the cap, so the behaviour is undocumented rather than contradicted.
6. **Codex's transient lever is a file, not a convention.** alwayson.04 has no Codex basis; the closest documented lever is `AGENTS.override.md` for temporary global changes (`:47`) and the automatic copy of that override into managed worktrees (`git-worktrees.md:152`). The box rule stays lane-authored.
7. **Docs-site source is not public.** The Q30 docs-source-tree leg is the client repo's `docs/` (pointers) plus the complete live index and a 191-page full-text grep, not the site's authoring tree. Recorded as a scope limit on every negative above; the symlink negative is still capped at "not checked" despite the corpus grep, because the only positive statement is code.
8. **Release-notes coverage is partial.** The atom feed exposes the latest 10 entries only, all with one-line bodies, and the repo changelog is a pointer. Older release prose was not paged through.
9. **Not measured, by construction.** I ran no instrument, no counter, no gate and no build; no Codex binary was executed; nothing about a shipped version's behaviour is claimed. The loader statements are source at commit `8eaf5fd1` (main tip 2026-10-22), not a binary measurement.
10. **Evidence locations.** Fetched bytes, hash table and fetch log: `/fast/scratch/hyaku/kotoba-r53/ScribeCodex/src/` (`gate-*.md`, `codex-agents-md.md`, `codex-agents_md.rs`, `meta.tsv`, `fetchlog.txt`, `urls.txt`, `docsall/` with 196 files, `agents-md.html`, `codex-releases.html`, `tree.html`, `tree-docs.html`). The sandbox clone path in the bounds was not created: this seat wrote no code and needed no checkout.

Out of scope, deliberately untouched: C1 (opencode 1.19.4 re-derivation and re-pin), the routed repairs (corpus-integrity baseline, self-test arms, MCP counter mutants), every `verifiers/` file, `corpus/SOURCES.md` itself, and the Claude Code, opencode, Gemini CLI, Copilot, Cursor, agents.md and omp rows owned by other seats.
