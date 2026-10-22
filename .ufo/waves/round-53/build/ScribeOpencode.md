Result: DONE — opencode's installed channel (1.19.4, V1) reads three always-on names — `AGENTS.md`, `CLAUDE.md` as a fallback, and a deprecated `CONTEXT.md` — and with `AGENTS.md` and `CLAUDE.md` both present it reads `AGENTS.md` only; the current docs source tree documents the opposite for OpenCode V2 (`AGENTS.md` only, no `CLAUDE.md` fallback); no `@AGENTS.md` import in rule files, three documented redirect forms, no documented or coded size limit, no rule about dated or transient content; 5 SOURCES rows drafted, 10 candidates rejected.

Round 53, wave 1 (build), C2 source basis, client opencode. Seat `KotobaR53.ScribeOpencode`. Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. The only lane file written is this report. All fetched bytes and both clones live under `/fast/scratch/hyaku/kotoba-r53/ScribeOpencode/` (`git clone` of the lane at the plan commit, with `.fetch/` for downloads and `.fetch/oc-src` for a partial clone of the vendor repo). No tool was installed or upgraded; no model call of any kind was made; no lane file was edited; the lane's Git index and jj state were not touched.

## 1. Method and fetched-byte ledger

Fetches used `curl -sS -L` with the agent's own user agent, recorded by a small `get.sh` helper that prints URL, UTC time, HTTP status, byte count and sha256 for every request. Vendor refs were pinned with read-only `git ls-remote` (the GitHub REST API refused this seat: 403, see §6). Source quotes are line numbers in the fetched bytes; for the served V1 page the same sentence also carries a line number in the pinned source file `packages/web/src/content/docs/rules.mdx`, because the served `.md` route is that file's body plus its frontmatter `description` as a leading paragraph (diff of `tail -n +7 rules.mdx` against the served text: 7 diff lines, all one added leading paragraph and one missing trailing newline).

Vendor refs at fetch time (read-only `git ls-remote`, exit 0):

```
7a6ce05d0939826aa6c8e1c481489a713b2d633f	refs/heads/2.0
4a6dacec5e4afb69f211458e08be5233c57dd307	refs/heads/dev
daf64a10034adeec50066549a2804026398642ec	refs/heads/v1
e3c4eb242585dcd77be1a867391b7c25fd47ce52	refs/tags/v1.19.3
148842ef7cb1bc34192b3fff57d0f9721ab9c801	refs/tags/v1.19.4
main: []            # refs/heads/main does not exist; every /main/ raw URL below 404s
```

| what | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| served V1 rules text | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |
| served V1 rules page | https://opencode.ai/docs/rules | 2026-10-22T20:04:44Z | 200 | 76,861 | `05a6070925ba6a0a74fe23bde1b2cc0329bf7dae8e00ba39cf373001967128e2` |
| V1 docs source, dev head | https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/packages/web/src/content/docs/rules.mdx | 2026-10-22T20:04:58Z | 200 | 6,758 | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` |
| same file at tag v1.19.4 | .../148842ef7cb1bc34192b3fff57d0f9721ab9c801/packages/web/src/content/docs/rules.mdx | 2026-10-22T20:09:57Z | 200 | 6,758 | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` (byte-identical) |
| V2 instructions source, dev head | .../4a6dacec.../services/www/src/docs/content/instructions.mdx | 2026-10-22T20:05:25Z | 200 | 5,634 | `7c767eb7433054c47549b8e28e1d934aee40e1b36fdf09d777a04062c2958895` |
| V1 loader at tag v1.19.4 | .../148842ef.../packages/opencode/src/session/instruction.ts | 2026-10-22T20:05:57Z | 200 | 8,581 | `fee79c023eae44f720d4d600f334a987ad5f7615c4a008a20c89131a92684a8f` |
| prompt assembly at tag v1.19.4 | .../148842ef.../packages/opencode/src/session/prompt.ts | 2026-10-22T20:08Z | 200 | 64,944 | `f0c5bc64c0f0e966693d4a57f7ede1e9d6e188b396152f04b55303dc75b9b768` |
| reference regex at tag v1.19.4 | .../148842ef.../packages/opencode/src/config/markdown.ts | 2026-10-22T20:08Z | 200 | 1,173 | `bcb87009e9ffc760e0e2f0878543f582b5ca7ecc67bebb2087de2467ae28cbfe` |
| V2 release notes | .../4a6dacec.../CHANGELOG.md | 2026-10-22T20:04:59Z | 200 | 50,001 | `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b` |
| site changelog route | https://opencode.ai/changelog | 2026-10-22T20:09:29Z | 200 | 88,230 | `39613fe0950e64ea88ce62cb2764179f164120a997532883b1231787527018c2` |
| release feed (V1 + V2 tags) | https://github.com/anomalyco/opencode/releases.atom | 2026-10-22T20:10:12Z | 200 | 6,758 | `5d050363ba74e9b441a41de9c81ec34b39a9df91952e1e40d720052ff3a6fe1a` |
| v1.19.4 release page | https://github.com/anomalyco/opencode/releases/tag/v1.19.4 | 2026-10-22T20:09:57Z | 200 | 194,665 | `d59579dd3450382b4101df4e67da976cb234f5ba70660c795958c8375b29bb3e` |
| V2 instructions route | https://opencode.ai/docs/instructions | 2026-10-22T20:11:24Z | 404 | 101 | (error page) |
| GitHub REST API (3 URLs) | api.github.com/repos/anomalyco/opencode… | 2026-10-22T20:04:49Z | 403 | 280 | `2282f9baf641a8417b97a1785119fd62f08e3560b50fdecfae2019fff3ae259d` |

Other read-only commands (all exit 0 unless shown): `git clone -q --depth 1 --filter=blob:none --no-checkout --branch dev https://github.com/anomalyco/opencode.git oc-src` then `git -C oc-src fetch -q --depth 1 origin tag v1.19.4`; `git -C oc-src grep -n -E "ConfigMarkdown\.files|FILE_REGEX|instructionFiles|GEMINI\.md" v1.19.4 -- packages/opencode/src packages/core/src` (6 hits: `config/markdown.ts:5,9`, `session/instruction.ts:64,124,172`, `session/prompt.ts:160`); `git -C oc-src ls-tree -r --name-only v1.19.4 | grep -i gemini` (11 hits, all model protocol code, provider test fixtures, the `prompt/gemini.txt` model prompt and two icons — none a rule-file name); `grep -c "first matching file wins" rules.html` → `1`.

## 2. Answers for opencode

### 2.1 Which always-on file names it reads

Installed channel (V1; the host's opencode 1.19.4 binary). The loader's project name array, `instruction.ts:64-68`:

```
64:    const instructionFiles = [
65:      "AGENTS.md",
66:      ...(!flags.disableClaudeCodePrompt ? ["CLAUDE.md"] : []),
67:      "CONTEXT.md", // deprecated
68:    ]
```

and the global array, `instruction.ts:60-63`, holds `path.join(global.config, "AGENTS.md")` plus `~/.claude/CLAUDE.md` behind the same flag. The served page names two of the three: `rules.mdx:81` "**Project rules**: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)" and `rules.mdx:73` for the global `~/.config/opencode/AGENTS.md`. `CONTEXT.md` appears in no documentation page this seat opened (see §3, negative N4). `GEMINI.md` appears nowhere: not in either docs page, not in the docs tree listings, and not in the v1.19.4 source — `git grep "GEMINI\.md"` over `packages/opencode/src` and `packages/core/src` returned no hit; the only `gemini`-named files in that tree are model protocol code, provider test fixtures, the `prompt/gemini.txt` model prompt and two icons.

V2 channel (the vendor's `dev` branch, which is what the site's own `/changelog` lists as v2.1.3). `instructions.mdx:42`:

> OpenCode V2 recognizes `AGENTS.md` only. It does not use `CLAUDE.md` as a fallback.

So the two live channels give opposite answers about `CLAUDE.md`, and the channel that ships as the installed 1.19.4 is the V1 one (§2.6).

### 2.2 What it does when two of them exist in one directory

V1: exactly one project-level file is read, and `AGENTS.md` wins. `rules.mdx:103`:

> The first matching file wins in each category. For example, if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used.

(served route line 98). The code agrees and shows the mechanism: the loader walks the names in array order, and the first name with any hit anywhere on the walk wins and stops the search — `instruction.ts:122-130`:

```
122:      // The first project-level match wins so we don't stack AGENTS.md/CLAUDE.md from every ancestor.
123:      if (!Flag.OPENCODE_DISABLE_PROJECT_CONFIG) {
124:        for (const file of instructionFiles) {
...
128:          if (matches.length > 0) {
129:            matches.forEach((item) => paths.add(path.resolve(item)))
130:            break
```

Two consequences worth stating plainly: a `CLAUDE.md` beside the edited file loses to an `AGENTS.md` several directories up (the search is per name, not per directory), and the global category is the same shape — one of `~/.config/opencode/AGENTS.md` or `~/.claude/CLAUDE.md` (`rules.mdx:100-101`, `instruction.ts:60-63`). Additional files only enter through the config array, `rules.mdx:131`: "All instruction files are combined with your `AGENTS.md` files."

V2: the question dissolves for `CLAUDE.md` (never read), while several `AGENTS.md` at different depths are all loaded — `instructions.mdx:19` (global file then every `AGENTS.md` from the workspace toward home) and `instructions.mdx:37`: "OpenCode combines the files and does not resolve conflicts between them."

### 2.3 Whether it honours a redirect

Three forms, none of them the Claude Code import form.

1. `@AGENTS.md` import inside a rule file: not honoured, and the page says so. `rules.mdx:137`:

> While opencode doesn't automatically parse file references in `AGENTS.md`, you can achieve similar functionality in two ways:

(served route line 132). The code matches this: the `@name` regex (`config/markdown.ts:5`, `FILE_REGEX`) is consumed by the prompt resolver (`session/prompt.ts:160`, `const files = ConfigMarkdown.files(template)`), which turns `@path` into file parts of a *prompt*, and by nothing in the rule-file loader — `instruction.ts:92` reads the file as opaque text (`readFileString`) and `instruction.ts:166` re-emits it verbatim inside `Instructions from: <path>`. The V2 page does not mention the import form at all. So for the installed client, a `CLAUDE.md` whose body is `@AGENTS.md` is inert text.

2. A config pointing at another name: honoured and documented. `rules.mdx:107-131` documents the `instructions` array (`"instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]`), relative, `~/`, absolute, glob and remote-URL forms, remote fetches at a 5 s timeout (`rules.mdx:129`); the loader implements it at `instruction.ts:135-155` (with `~/` expansion at `:138`) and the URL branch at `:158-160` with `Effect.timeout(5000)` at `:97`. V2 documents the same array at `instructions.mdx:103-128` with a resolution table.

3. A symlink: documented as a sharing mechanism, not as a precedence rule. `rules.mdx:182`:

> Share rules across projects via symlinks or git submodules

(served route line 177). Read together with §2.2, a symlink that gives `CLAUDE.md` the bytes of `AGENTS.md` is compatible with the V1 client — the client reads `AGENTS.md`, and the second name is never consulted, so no second text can drift. Nothing in either page documents a symlink as a *redirect the loader follows for a missing name*; the loader opens that path with `readFileString` (`instruction.ts:92`), which follows a link at open time — the name is still found by the walk, so a link only ever supplies the bytes of a name the walk already matched. [INFERENCE for the open-time follow; the walk and the read call are observed.]

### 2.4 Documented size limit

None, in either channel, and none in the code. `grep -n -i -E "size|limit|truncat|characters|bytes" rules.mdx` → exit 1, no output at all, so the served page carries no size or truncation vocabulary (the only time-bounded prose on it is the 5 s remote fetch timeout at `rules.mdx:129`). `instructions.mdx` has no cap either (its hits for the same pattern are `:61` nested-edit detection and `:72` the built-in date line). The loader reads the whole file (`instruction.ts:92`) and the assembler concatenates whole files (`instruction.ts:166-167`); prompt assembly spreads them in unmodified (`prompt.ts:1257-1269`). The config docs on both channels (`packages/web/src/content/docs/config.mdx:792-799`, `services/www/src/docs/content/config.mdx:442-453`) mention the `instructions` option without a size rule. The Q30 sweep for this negative is in §3 (N1).

### 2.5 Anything about dated or transient content

No rule about dated or transient *content* in a rule file, in either channel. On the V1 page the whole vocabulary is absent: `grep -n -i -E "\bdate|dated|transient|stale|status file|live-state|size|limit" rules.mdx` → exit 1, no output. The V2 page has three adjacent statements, all about opencode's own machinery rather than about the file's content: `instructions.mdx:72` "5. Built-in date and environment context" (opencode injects its own date line), `instructions.mdx:95`:

> A temporary read failure preserves the last known instructions instead of treating them as deleted.

and `instructions.mdx:61` (an edit to a nested file is not detected until a new session). The Q30 sweep is §3 (N3). One V1 detail in the same family, relevant to a *checker* rather than to the client: the client detects edits to a loaded `AGENTS.md` and re-sends it, and removing every ambient file tells the session the old instructions no longer apply (V2 `instructions.mdx:78-96`); the V1 page documents no runtime update channel — its only "update" occurrence is `/init` creating or updating the file (`rules.mdx:18`, `grep -n -i -E "update|detect|change" rules.mdx` → one hit).

### 2.6 The channel fork, stated as a finding

The vendor's docs source tree has two live rule-file pages that contradict each other, and the site currently serves the older one:

- `https://opencode.ai/docs/rules` (200) carries the V1 text, and `https://opencode.ai/docs/rules.md` equals the body of `packages/web/src/content/docs/rules.mdx`; that file is byte-identical at the round-52 pin `cdf1c200a671378458b50f9e3167405f1f326b24`, at dev head `4a6dacec…`, and at tag `v1.19.4` (`2d789f84…`).
- `services/www/src/docs/content/instructions.mdx` (the V2 docs tree, alongside `migrate-v1.mdx`) says `CLAUDE.md` is not a fallback; its route `https://opencode.ai/docs/instructions` returns 404 (101 B).
- The site changelog and the repo `CHANGELOG.md` list only V2 versions (`v2.0.26` … `v2.1.3`), so the served docs page is not a stale copy of an old site: the vendor keeps the V1 page live for the V1 channel the npm binary belongs to.
- The installed 1.19.4 release notes contain no rule-file change: the whole `v1.19.4` entry is a bundled Bun upgrade (quote in §5, row E). 1.19.4 therefore inherits the 1.19.3 rule-file behaviour, and the V1 page is the correct documentation for the installed client.

## 3. Q30 sweeps for the negatives

Each negative carries its three parts: vendor changelog or release notes, the current docs source tree (the files, not only a rendered route), and a grep of the lane corpus.

| # | negative | (a) changelog / release notes | (b) current docs source tree | (c) lane corpus |
|---|---|---|---|---|
| N1 | opencode documents no size limit for rule files | `grep -n -i -E "instruction.*(size\|limit\|truncat)\|(size\|limit\|truncat).*instruction" CHANGELOG.md` → no output (exit 1); the `size\|limit\|truncat` hits that do exist are provider output-token continuations and Gemini model items (`CHANGELOG.md:254,277,359,366,430`), none about rule files; the `v1.19.4` release-notes entry is 203 B and says only that the Bun runtime was upgraded | `rules.mdx` (both channels: the same file at dev head and at tag v1.19.4) and `instructions.mdx` carry no size rule; `config.mdx` on both trees (`:792-799`, `:442-453`) mentions `instructions` with no cap; `instruction.ts:92,166` read and concatenate whole files | `grep -rn -i -E "size limit\|truncat\|character limit\|token budget" corpus/` filtered to rule-file rows returns only skill-description truncation from rounds 8 and 9 (`corpus/knowledge/harness-router-models-round9.md:171,175`, `corpus/knowledge/opencode-offer-trace-round8.md:180`); nothing about rule files |
| N2 | opencode reads no `GEMINI.md` | `grep -c -i "GEMINI\.md" CHANGELOG.md` → `0` (exit 1); the `gemini` hits are models, voice and routing (`CHANGELOG.md:254,277,430,521`); `rel.atom` v1.19.4 body → 0 | `instructions.mdx`, `rules.mdx` → 0 occurrences; the docs tree listings contain no gemini page on either tree; the v1.19.4 code: `git grep "GEMINI\.md"` over `packages/opencode/src` and `packages/core/src` → 0 hits, and `instruction.ts:64-68` is the only definition of the name array | `grep -rn -i gemini corpus/` with `opencode` → only omp-side rows: `corpus/knowledge/instruction-surface-census-round13.md:76,93,479` credit `GEMINI.md` to omp, and `:479` already records opencode's three names as "AGENTS.md → CLAUDE.md → CONTEXT.md, first hit wins"; no row claims opencode reads `GEMINI.md` |
| N3 | opencode states no rule about dated or transient content in rule files | `grep -n -i -E "dated\|transient\|stale" CHANGELOG.md` → 4 hits, none about rule files: two are substring matches inside "updated" (`:9` Bun certificates, `:542` session layout), two unrelated (`:218` transient model-generation failures, `:462` a stale tool label) | `rules.mdx` → 0 hits for the whole vocabulary (exit 1); `instructions.mdx` → `:61`, `:72`, `:95` only, all about opencode's own date context and read-failure handling, none about the file's content | `grep -rn -i -E "dated\|transient\|stale date\|live-state" corpus/` filtered to always-on rows → `corpus/knowledge/alwayson-checklist-round7.md:30` (the lane's own dated-text finding for the host file) and `corpus/knowledge/instruction-surface-census-round13.md:473` ("dated operational notes belong in status files") — both lane rules, no vendor rule |
| N4 | opencode's docs never name `CONTEXT.md` | `grep -c -i "CONTEXT\.md" CHANGELOG.md` → 0; `rel.atom` → 0 | `rules.mdx` → 0; `instructions.mdx` → 0 (the deprecated third name exists only in code, `instruction.ts:67`) | `corpus/knowledge/instruction-surface-remeasure-round13.md:24` and `corpus/knowledge/opencode-extraction-round14.md:50,117` already carry the three-name array from the binary, including `opencode:instructions/CONTEXT.md` |

No client is recorded "silent" on the strength of a one-part sweep here; N1–N4 each carry all three parts, and the code witness on top where one exists.

## 4. Draft SOURCES rows

Column shape and vocabulary per `/home/vgpnk/Projects/shokunin/CORPUS.md:86-104` (`kind` enum, `tier` A/B/C, `status` queued/mined/rejected, `recheck` ISO date or cadence, no `|` inside a cell). `used-by` is the entry the plan names. These are drafts: the L1 integrates them, and `mined` only becomes true once `corpus/knowledge/alwayson-rule-files-round53.md` exists and cites the rows (§8).

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | opencode — Rules (served docs page) — https://opencode.ai/docs/rules | docs | A | opencode's always-on rule-file names, per-directory precedence, Claude Code fallback, and the redirect forms it documents | § Types → § Claude Code Compatibility (`rules.mdx:77-91`), § Precedence (`:95-103`), § Custom Instructions (`:107-131`), § Referencing External Files (`:135-137`, `:182`); served as https://opencode.ai/docs/rules.md (200, 6,684 B, sha256 `dfb242d9…`) and as HTML (200, 76,861 B, `05a60709…`) on 2026-10-22T20:04:44Z; the prose equals the body of `packages/web/src/content/docs/rules.mdx` at dev head 4a6dacec (`2d789f84…`), byte-identical at tag v1.19.4 | Reads `AGENTS.md` with `CLAUDE.md` as a fallback and says that with both present only `AGENTS.md` is used; documents an `instructions` config array, globs and symlinks as the redirects, and states it does not parse file references in `AGENTS.md` | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | opencode — Instructions docs source, V2 tree (anomalyco/opencode, commit in the URL) — https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/services/www/src/docs/content/instructions.mdx | docs | A | the V2 channel's always-on contract: `AGENTS.md` only, no `CLAUDE.md` fallback, several `AGENTS.md` combined with no conflict resolution, `OPENCODE_DISABLE_PROJECT_CONFIG` | § Scope (`instructions.mdx:19,37,39`), the V2 note (`:42`), § Discovery (`:45-61`), § Ordering (`:63-76`), § Updates (`:78-96`), § Configuration (`:103-128`); fetched 2026-10-22T20:05:25Z (200, 5,634 B, sha256 `7c767eb7…`); the route https://opencode.ai/docs/instructions returned 404 (101 B) at 2026-10-22T20:11:24Z, so the page is not yet served | OpenCode V2 recognizes `AGENTS.md` only and does not use `CLAUDE.md` as a fallback; every discovered `AGENTS.md` is combined in a fixed order and conflicts between them are not resolved | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | anomalyco/opencode — session/instruction.ts at tag v1.19.4 — https://raw.githubusercontent.com/anomalyco/opencode/148842ef7cb1bc34192b3fff57d0f9721ab9c801/packages/opencode/src/session/instruction.ts | code | A | the installed 1.19.4 loader: which names it reads, how a tie is broken, and that files are read whole | `instruction.ts:60-68` (global and project name arrays), `:92` (readFileString), `:122-130` (first project-level match wins, then break), `:135-155` (config `instructions`), `:158-168` (assembly); fetched 2026-10-22T20:05:57Z (200, 8,581 B, sha256 `fee79c02…`); tag v1.19.4 = 148842ef7cb1bc34192b3fff57d0f9721ab9c801 | The name array is `AGENTS.md`, `CLAUDE.md` behind the Claude Code flag, and a deprecated `CONTEXT.md`; the first name with any match on the walk wins and the rest are skipped, and the loader applies no size cap | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | opencode — Changelog, release notes (anomalyco/opencode, commit in the URL) — https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/CHANGELOG.md | docs | A | what the vendor's release notes say about rule files and the Claude Code compatibility flags (Q30 part a) | `CHANGELOG.md:309` (the `.claude` skills discovery honours the flags), `:5` (v2.1.3, 2026-10-22), `:59` (MCP instructions updates); fetched 2026-10-22T20:04:59Z (200, 50,001 B, sha256 `7c4cb740…`); the site route https://opencode.ai/changelog (200, 88,230 B, sha256 `39613fe0…`, 2026-10-22T20:09:29Z) lists the same V2 versions only | The V2 release notes carry no rule-file or `AGENTS.md` change; their only rule-file-adjacent entry honors `OPENCODE_DISABLE_CLAUDE_CODE` and `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS` for `.claude` skill discovery | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | opencode — Release notes for v1.19.4 (anomalyco/opencode, releases atom) — https://github.com/anomalyco/opencode/releases.atom | docs | A | what the vendor's release notes for the installed version say about rule files (Q30 part a) | `v1.19.4` entry, body 203 B, first item the Bun upgrade; fetched 2026-10-22T20:10:12Z (200, 6,758 B, sha256 `5d050363…`); the tag page https://github.com/anomalyco/opencode/releases/tag/v1.19.4 also 200 (194,665 B, `d59579dd…`) | The only v1.19.4 change is a bundled Bun runtime upgrade, so the installed 1.19.4 rule-file behaviour is the 1.19.3 behaviour | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |

## 5. Gate records

Every quote is ≤25 words and is located by line number in the fetched bytes. For the served V1 page both the served-route line and the pinned-source line are given, because the two are offset by five lines.

| row | URL | UTC | HTTP | bytes | sha256 | quote (≤25 words) | line |
|---|---|---|---|---|---|---|---|
| A | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9…` | "The first matching file wins in each category. For example, if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used." | served route 98; `rules.mdx:103` |
| A | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9…` | "While opencode doesn't automatically parse file references in `AGENTS.md`, you can achieve similar functionality in two ways:" | served route 132; `rules.mdx:137` |
| A | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9…` | "**Project rules**: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)" | served route 76; `rules.mdx:81` |
| A | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9…` | "Share rules across projects via symlinks or git submodules" | served route 177; `rules.mdx:182` |
| A | https://opencode.ai/docs/rules.md | 2026-10-22T20:04:44Z | 200 | 6,684 | `dfb242d9…` | "All instruction files are combined with your `AGENTS.md` files." | served route 126; `rules.mdx:131` |
| A | https://opencode.ai/docs/rules | 2026-10-22T20:04:44Z | 200 | 76,861 | `05a60709…` | "The first matching file wins in each category." (rendered HTML carries the sentence; `grep -c` → 1) | HTML bytes, one line |
| B | https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/services/www/src/docs/content/instructions.mdx | 2026-10-22T20:05:25Z | 200 | 5,634 | `7c767eb7…` | "OpenCode V2 recognizes `AGENTS.md` only. It does not use `CLAUDE.md` as a fallback." | `instructions.mdx:42` |
| B | same URL | 2026-10-22T20:05:25Z | 200 | 5,634 | `7c767eb7…` | "OpenCode combines the files and does not resolve conflicts between them." | `instructions.mdx:37` |
| B | same URL | 2026-10-22T20:05:25Z | 200 | 5,634 | `7c767eb7…` | "A temporary read failure preserves the last known instructions instead of treating them as deleted." | `instructions.mdx:95` |
| B | same URL | 2026-10-22T20:05:25Z | 200 | 5,634 | `7c767eb7…` | "Built-in date and environment context" | `instructions.mdx:72` |
| C | https://raw.githubusercontent.com/anomalyco/opencode/148842ef7cb1bc34192b3fff57d0f9721ab9c801/packages/opencode/src/session/instruction.ts | 2026-10-22T20:05:57Z | 200 | 8,581 | `fee79c02…` | "The first project-level match wins so we don't stack AGENTS.md/CLAUDE.md from every ancestor." | `instruction.ts:122` |
| C | same URL | 2026-10-22T20:05:57Z | 200 | 8,581 | `fee79c02…` | `"CONTEXT.md", // deprecated` | `instruction.ts:67` |
| D | https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/CHANGELOG.md | 2026-10-22T20:04:59Z | 200 | 50,001 | `7c4cb740…` | "Honor `OPENCODE_DISABLE_CLAUDE_CODE` and `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS` when discovering `.claude` skills." | `CHANGELOG.md:309` |
| E | https://github.com/anomalyco/opencode/releases.atom | 2026-10-22T20:10:12Z | 200 | 6,758 | `5d050363…` | "Upgraded the bundled Bun runtime to 1.4.4, which includes security fixes for Brotli, TLS, HTTP/1.1, HTTP/2, HTTP/3, WebSocket, and fetch" | `v1.19.4` entry body, bytes 19-60 of 203 |

Supporting (not row-anchoring) facts with their own locators: the Claude Code compatibility flags as shipped code, `runtime-flags.ts:23-30` (`OPENCODE_DISABLE_CLAUDE_CODE` broad, `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`, `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS`) and `flag.ts:54-55` (`OPENCODE_DISABLE_PROJECT_CONFIG`); the `@` regex, `config/markdown.ts:5`, consumed at `prompt.ts:160`; the site's `/docs/instructions` 404 (101 B) and the docs tree listings (the V2 tree has `instructions.mdx` and `migrate-v1.mdx`; the V1 tree has `rules.mdx`; neither has a gemini page).

## 6. Rejected candidates

| candidate | outcome | reason |
|---|---|---|
| https://opencode.ai/docs/instructions and its trailing-slash form | 404, 101 B / 102 B | The V2 page is not served; the source file is admitted as row B instead. |
| https://api.github.com/repos/anomalyco/opencode (and two commits-by-path queries) | 403, 280 B, three URLs, identical body sha256 | The API refused the request; there is no content to mine, and working around an access control is out of bounds for this seat. Consequence: commit pins here come from `git ls-remote`, not from the API. |
| `.../main/packages/web/src/content/docs/rules.mdx`, `.../main/services/www/.../rules.mdx`, `.../main/packages/opencode/CHANGELOG.md` | 404, 14 B each | `refs/heads/main` does not exist in the vendor repo (see §1); wrong ref. |
| https://raw.githubusercontent.com/anomalyco/opencode/v1/CHANGELOG.md | 404, 14 B | The `v1` branch carries no root changelog; the releases atom feed is admitted as row E instead. |
| `packages/web/src/content/docs/rules.mdx` at the round-52 pin `cdf1c200a671378458b50f9e3167405f1f326b24` | 200, 6,758 B, `2d789f84…` | Byte-identical to the dev-head file, so it adds no new witness; kept as a byte-identity check inside row A's anchor. |
| `packages/web/src/content/docs/config.mdx:792-799` and `services/www/src/docs/content/config.mdx:442-453` | 200 | They only repeat that an `instructions` option exists, which rows A and B already carry. |
| `packages/opencode/src/session/prompt.ts:160` and `packages/opencode/src/config/markdown.ts:5` | 200 | Opened to answer the `@` question; they witness the same claim the docs quote at `rules.mdx:137` carries, and no separate claim rests on them. Cited in §2.3 and §5, not admitted as rows. |
| `packages/opencode/src/session/system.ts` | 200 | Its MCP-instructions assembly belongs to the round-52 rows (S032-S037, S041), not to this claim. |
| Translated `rules.mdx` variants listed in the docs tree (ar, bs, da, de, es, fr, it, ja, ko, nb, pl, pt-br, ru, …) | not opened | Redundant translations of row A; opening one would add no claim-bearing fact. |
| `packages/opencode/src/session/prompt/gemini.txt` (v1.19.4) | surfaced by the GEMINI grep | It is the Gemini *model* prompt, not a rule-file name, and it is not part of the client's rule-file surface. |

## 7. Consequence for C2 (facts only; the box wording is the L1's call)

1. The counter's `import-redirect` PASS case (a `CLAUDE.md` whose body is `@AGENTS.md`) is **not** a redirect for opencode: opencode reads `AGENTS.md` and never consults the second name (`rules.mdx:103`, `instruction.ts:122-130`), and it does not parse references inside rule files (`rules.mdx:137`, `instruction.ts:92,166`). The case remains grounded for the Claude Code basis the plan names; opencode diverges, so the box sentence "or an explicit redirect" needs either a client-qualified reading or the config/symlink forms named. [INFERENCE on the wording only; the client facts are observed.]
2. The counter's `two-rule-files` FAIL case is a cross-client drift case, not an opencode failure mode: for the installed opencode, two names in one directory means only `AGENTS.md` is read, so no second text reaches the model. The drift exists because another client in the same directory reads the other name. This seat did not open Claude Code's page and does not assert its behaviour; that is `ScoutClaudeBehaviour`'s evidence, not mine. [NOT MEASURED BY THIS SEAT]
3. A third name exists in the shipped loader that no page documents: `CONTEXT.md`, marked deprecated (`instruction.ts:67`), already recorded lane-side as `opencode:instructions/CONTEXT.md` (`corpus/knowledge/opencode-extraction-round14.md:50,117`). The instrument's six cases do not exercise it; if the box is meant to be complete for the installed client, the case set is where that gap shows (the counter's cases are frozen at the plan commit, so this is a note for the L1, not a request to widen it).
4. opencode's own documented redirect forms, for whoever writes the knowledge entry: the `instructions` array (`rules.mdx:107-131`, `instructions.mdx:103-128`) and symlinks (`rules.mdx:182`). The config form is the one that survives opencode's per-name precedence, because it is additive (`rules.mdx:131`).
5. The two channels must not be mixed in one sentence: the served page documents `CLAUDE.md` fallback for the V1 channel that the installed 1.19.4 binary belongs to, while the vendor's current docs source tree documents `AGENTS.md` only for V2. Any row or entry that cites opencode without naming the channel will be false on one of them.

## 8. Limits and known gaps

- `mined` in §4 is a draft status. `/home/vgpnk/Projects/shokunin/CORPUS.md:103` defines `mined` as "cited by ≥1 path in `used-by`", and the same contract's gate at `:145-147` prints any `mined` row whose used-by path does not exist; until `corpus/knowledge/alwayson-rule-files-round53.md` exists and cites these rows, the honest status is `queued`. The L1 asked for `mined` with that `used-by`, so the rows are drafted that way and this precondition is stated rather than assumed.
- Code evidence is read from the vendor's source at tag `v1.19.4` and dev head `4a6dacec…` over HTTPS, not from the installed binary. The C1 seat's extraction reads the binary; this seat's read is a documentation-and-source witness. It agrees with the lane's own binary extraction of the same array (`corpus/knowledge/instruction-surface-remeasure-round13.md:24`, `corpus/knowledge/opencode-extraction-round14.md:50`), which is corroboration, not a second measurement.
- No commit history was enumerated for the docs paths (the API refused, §6), so "the V1 page has not moved" rests on three byte-identical pins (round-52 pin, dev head, tag v1.19.4) rather than on a history walk.
- The `@`-reference question is answered for rule files and for prompt parts. This seat did not trace every consumer of `ConfigMarkdown.files`; `git grep` over `packages/opencode/src` and `packages/core/src` at tag v1.19.4 found exactly one caller, `prompt.ts:160`.
- Nothing here measures the live always-on population, the C2 instrument, or either counter; those are other seats. No counter was run and no counter output is claimed.

## 9. Bounds compliance

Only lane file written: this report. Writes were confined to the sandbox clone `/fast/scratch/hyaku/kotoba-r53/ScribeOpencode` (lane clone at `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`, plus `.fetch/` scratch and a partial vendor clone `.fetch/oc-src` with the `v1.19.4` tag fetched). Read-only git in the lane: `git log --oneline -3`, `git rev-parse HEAD`. No lane git write, no jj command, no fleet-root or sibling-lane write, no `MANIFEST.json` or `.ufo/state` touch, no push, no pacman, no install, no model call, no headless browser, no `model` parameter and no `ask`. Messages: this report plus the seat's normal result channel only.
