Result: DONE — Claude Code reads the CLAUDE.md family and reads AGENTS.md only when no counting CLAUDE.md exists, honours `@AGENTS.md` and symlink redirects, skips a rule file over 4 MiB, treats `GEMINI.md` only as a one-time `/import gemini` copy, and has two drafted SOURCES rows (S043, S044) with Gate quotes, alwayson.07 being fully vendor-grounded while alwayson.04 is only directionally supported.

Round 53, wave 1 (build), C2 source basis. Seat `KotobaR53.ScribeClaudeCode`. Target client: Claude Code. Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Leaf seat: no subagents, no lane writes except this file, no git/jj writes anywhere, no model calls. No tool was installed or upgraded; nothing was needed.

Axes: coverage — all six C2 questions answered from fetched bytes with line-numbered quotes; operability — six of six alwayson.07 cases attributable to this client, zero of six alwayson.04 cases (the date rule is lane craft).

## 1. Method and fetch log

Every source was opened with plain `curl -sS -o <file> -w '...'`, from `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/`, then hashed with `sha256sum`. All successful fetches exited 0 and printed the status/byte line below. Quoting is against the fetched bytes; line numbers are lines in the fetched file, not the rendered page.

| local file | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| `memory.md` | https://code.claude.com/docs/en/memory.md | 2026-10-22T20:04:43Z | 200 | 51,971 | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` |
| `changelog.md` | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2026-10-22T20:04:46Z | 200 | 1,070,244 | `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` |
| `llms.txt` | https://code.claude.com/docs/llms.txt | 2026-10-22T20:05:13Z | 200 | 63,682 | `b7064ac53215f39ad3b8cb20f1a63dba5334f6fcb7efd8e789c55fa634e3d4c0` |
| `llms-full.txt` | https://code.claude.com/docs/llms-full.txt | 2026-10-22T20:05:28Z | 200 | 9,614,681 | `1a5816202ca5cb4378a2ea8afad80d1d0102e83fe387096ffe0ca89f80fe563a` |
| `repo.html` | https://github.com/anthropics/claude-code/tree/main | 2026-10-22T20:07:46Z | 200 | 314,089 | `77a889bcf3652965ccf869c325a2b7aeb9eae3fce07022fdf35e0e72bf7af94c` |
| `README.md` | https://raw.githubusercontent.com/anthropics/claude-code/main/README.md | 2026-10-22T20:10:01Z | 200 | 2,873 | `aa0d8b80ac083e1591be0789273f447058cc9187b4331634a5614155da27778d` |
| `gh-contents.json` | https://api.github.com/repos/anthropics/claude-code/contents/ | 2026-10-22T20:05:28Z | 403 | 280 | `2282f9baf641a8417b97a1785119fd62f08e3560b50fdecfae2019fff3ae259d` |

Commands run (exit codes):

- `curl ... https://code.claude.com/docs/en/memory.md` → exit 0, `HTTP 200 bytes 51971`.
- `curl ... https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` → exit 0, `HTTP 200 bytes 1070244`.
- `curl ... llms.txt` → exit 0, `HTTP 200 bytes 63682`; `llms-full.txt` → exit 0, `HTTP 200 bytes 9614681`.
- `curl ... https://api.github.com/repos/anthropics/claude-code/contents/` → curl exit 0, body `API rate limit exceeded` at HTTP 403. A follow-up `python3` one-liner that assumed a JSON array exited 1 (`TypeError: string indices must be integers`); the 403 body was then read directly. The API route is recorded as unavailable, not as a check.
- `ls /home/vgpnk/Projects/shokunin/SOURCES-CONTRACT-v1.md` → exit 2 (no such file). The contract was then read where `corpus/SOURCES.md` points: fleet `CORPUS.md:79-126`.
- `grep -c '^| S0' corpus/SOURCES.md` → 42 rows, last `S042`; proposed ids are `S043` and `S044`.

`memory.md` carries `last-modified: Thu, 22 Oct 2026 20:04:43 GMT` equal to the fetch time, so its revision identity is the sha256, not the header. The changelog was fetched from `main` (mutable branch tip): no commit pin is recorded because the GitHub API listing was rate-limited (403); re-fetch and compare `121129bc…`.

## 2. Answers

### 2.1 Which always-on file names Claude Code reads

The page's enumeration, with line numbers in `memory.md`:

- **Project, either name:** `./CLAUDE.md` or `./.claude/CLAUDE.md` (`:61`, `:70`); `CLAUDE.local.md` loads alongside and is appended after `CLAUDE.md` (`:123`, `:144`).
- **AGENTS.md branch:** `AGENTS.md` when no CLAUDE.md-class file counts (`:356`); `.claude/AGENTS.md` also loads at session start (`:375`); `AGENTS.md` files in directories above the working directory load at launch too (`:375`).
- **User:** `~/.claude/CLAUDE.md` (`:60`).
- **Managed:** `/etc/claude-code/CLAUDE.md` on Linux/WSL, `/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS, `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows (`:59`, `:293-295`); or inline content from the managed-settings `claudeMd` key (`:301`).
- **Rules:** `.claude/rules/*.md`; without `paths` frontmatter they load at launch with the same priority as `.claude/CLAUDE.md` (`:188`).
- **Explicitly not read:** "**Not read**: `AGENTS.local.md`, `AGENTS.override.md`, or anything under a `.agents/` directory" (`:378`).
- **Auto memory (different class):** `MEMORY.md`, first 200 lines or 25KB (`:547`), is not a user rule file.

The page's own framing at `:352`: "a repository already set up for other coding agents works without adding a `CLAUDE.md`" (15 words).

**GEMINI.md:** not among the names read at session start anywhere in the fetched bytes; the only Gemini path documented is `/import gemini`, covered in §2.6 and the Q30 sweep in §4.

### 2.2 Two of them in one directory

Default behaviour, verbatim (`memory.md:356-357`):

- `:356` — "An `AGENTS.md`, and no `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it | Your `AGENTS.md`"
- `:357` — "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it | Your `CLAUDE.md` files only"

So with both present and no import, the AGENTS.md content is **not** read: one rule file is live and the other is dead weight for this client. `CLAUDE.local.md` counts for that check (`:370`), and adding one stops Claude reading `AGENTS.md` (`:382`). `~/.claude/CLAUDE.md`, the managed CLAUDE.md and `.claude/rules/` do not count and keep loading alongside (`:371`).

Two CLAUDE.md-class files in one directory are both read and concatenated, not overridden; `CLAUDE.local.md` is appended after `CLAUDE.md` (`:144`). The page does not state a precedence between `./CLAUDE.md` and `./.claude/CLAUDE.md` when both exist; it lists either as the project location (`:61`, `:70`) — observed absence, not a vendor negative.

### 2.3 Redirects honoured

- **`@AGENTS.md` import — yes.** The table row at `:358`: "A `CLAUDE.md` that already imports `AGENTS.md` | Your `CLAUDE.md`, with `AGENTS.md` included through the import". The mechanism is the general import syntax at `:102`: "CLAUDE.md files can import additional files using `@path/to/import` syntax." The section at `:442` names the cross-tool case and the exact file shape: put "an `@AGENTS.md` import in a `CLAUDE.md` next to it", Claude-specific text below the import, and Claude reads the imported file first. Imports are expanded at launch, so they do not reduce context cost (`:88`, `:102`). Deduplication: "Keeping the import never makes Claude read `AGENTS.md` twice" (`:435`), and in both-files mode Claude Code "skips an `AGENTS.md` it has already loaded" (`:391`).
- **Symlink — yes.** `:452` "If you don't need Claude-specific content, a symlink also works", with `:455` `ln -s AGENTS.md CLAUDE.md`. The old-workaround section: "Either way Claude reads the content once" (`:437`). Documented costs: the Edit and Write tools refuse to write through the symlink and redirect Claude to the target (`:460`); on Windows use the import instead, because a committed symlink may check out as a plain text file unless `core.symlinks` is enabled (`:461`).
- **Config — not an arbitrary-name redirect.** `Project instructions` takes four modes: `claude-md-or-agents-md` (default), `claude-md-and-agents-md`, `claude-md`, `managed-only` (`:390-393`), set with `/config` (`:386`) or `pluginConfigs["cc-plugin-agents-md@builtin"].options.instructionFiles` (`:395-407`). `claudeMdExcludes` skips files by path or glob (`:333`, `:346`). The managed `claudeMd` key injects content directly (`:301`; settings-reference text at `llms-full.txt:33806`, `:33812` says it is honoured in managed/policy settings only). No documented setting takes an alternate rule-file *name*: arbitrary files enter only through `@path` imports or symlinks. That absence is stated in the Q30 sweep (§4), not as vendor silence.
- **Prose is not a redirect.** `:436`: "Claude sees `AGENTS.md` only if it decides to open the file", where the sentence tells Claude in words to read it; the docs' fix is to replace the sentence with an `@AGENTS.md` import. This is the exact basis for the counter's `prose-mention` FAIL case.

### 2.4 Documented size limit

- Hard skip: "Files over 200 lines consume more context and may reduce adherence. Claude Code skips a file over 4 MiB." (`:619`); "Claude Code loads a CLAUDE.md file of up to 4 MiB in full and skips a larger file." (`:551`).
- Recommendation: "target under 200 lines per CLAUDE.md file" (`:88`).
- Warnings: "If one of your instruction files is over the recommended length, you see a warning at startup and when you run `/status`" (`:621`), plus a combined-limit warning; "Each CLAUDE.md, rules file, and `@path` import counts as a separate file" (`:621`).
- Unstated: whether the 4 MiB skip applies to `AGENTS.md`. The page names "a CLAUDE.md file"; extending it to AGENTS.md is [INFERENCE]. Do not claim it.
- Different, do not conflate: auto memory `MEMORY.md` loads first 200 lines or 25KB (`:547`); rule `paths` expansion has a 1,000-pattern / 4 MiB budget (`:238`), not a file-size cap.

### 2.5 Dated or transient content

No page states a rule against dated text, and the fetched bytes contain no "transient", "live state" or "status file" wording. What the vendor does document:

- `:51` — 'Keep it to facts Claude should hold in every session: build commands, conventions, project layout, "always do X" rules'; multi-step procedures or part-of-codebase content belong in a skill or path-scoped rule.
- `:90` — review the files "periodically to remove outdated or conflicting instructions".
- `:94` — `/doctor prompt-audit` finds "instructions written for older models, references to files or commands that don't exist, and files that contradict each other".

Consequence for C2: the "facts held in every session" line and the stale-instruction audit support box 04's *direction*, but the dated-text prohibition ("dates and live-state go to status files") is lane craft, grounded at `corpus/knowledge/alwayson-checklist-round7.md:16` and its FAIL example at `:30`. The instrument must not cite Claude Code for the date rule (Q20/Q23). The version-number PASS control ("Python 3.12") has no vendor basis either: it is the lane's discriminator against date-shaped strings.

### 2.6 Operability mapping for the frozen C2 counter

`verifiers/check_alwayson_boxes.py` pins six cases per box. Against the fetched bytes:

- **alwayson.07 — all six cases attributable.** `agents-only` PASS (`:356`); `claude-only` PASS (`:40`, "Claude reads them at the start of every session", `:70`); `import-redirect` PASS (`:358`, `:442`, `:435`; the case's file shape mirrors the doc example at `:444-450`); `symlink-redirect` PASS (`:452`, `:455`, `:437`); `two-rule-files` FAIL (`:357`, `:368` — the second name is not read); `prose-mention` FAIL (`:436`).
- **alwayson.04 — none of the six cases attributable to this client.** Only `:51`, `:90`, `:94` above. The counter's docstring does not claim otherwise (it sources only "the redirect forms and the both-files behaviour"), which matches §2.3-§2.2; the knowledge entry should say the same.
- The counter docstring's clause "so two independent rule files are read by different clients" is not in S043: Claude Code's page says only what *Claude Code* reads. The clause is defensible from other rows (opencode's priority list, Copilot CLI combining them) but must not be quoted to Claude Code. `AGENTS.md` itself is described only as what "other coding agents" use (`:352`).

## 3. Draft SOURCES rows

Column shape copied from `corpus/SOURCES.md:11` (11 columns). Ids are proposals: the registry holds 42 rows at base, last `S042`. Status `mined`, used-by names the planned round-53 entry; the entry is not on disk yet, so the citation resolves only after it lands. `recheck` is the date the brief asked for (90 days); for S044 the natural cadence would be `on-release`, and `recheck` is an in-place-mutable cell (fleet `CORPUS.md` rule 2).

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S043 | Claude Code — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Which always-on instruction files Claude Code reads (CLAUDE.md family, AGENTS.md, rules), which name wins when both exist, the documented redirect forms, and documented size handling (vendor documentation, not a measurement of the client binary) | § AGENTS.md table (memory.md:354-358), § When Claude Code reads AGENTS.md (:368-378), § Choose which instruction files load (:388-393), § Share one file with other coding tools (:440-452), § My CLAUDE.md is too large (:617-619); fetched 2026-10-22T20:04:43Z, HTTP 200, 51,971 B, sha256 971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff | With both AGENTS.md and CLAUDE.md present and no import, Claude Code reads CLAUDE.md only; an `@AGENTS.md` import and a CLAUDE.md symlink are the two documented redirects; a file over 4 MiB is skipped | mined | 2026-10-22 | 2027-01-20 | corpus/knowledge/alwayson-rule-files-round53.md |
| S044 | Claude Code — changelog (anthropics/claude-code, main) — https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | docs | A | When Claude Code gained AGENTS.md reading and which session types gained it later (vendor release notes, not a measurement of the client binary) | § 2.1.277 (changelog.md:2223-2225), § 2.1.281 (:1921, :2060); fetched 2026-10-22T20:04:46Z, HTTP 200, 1,070,244 B, sha256 121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49; main-branch tip at fetch time, re-fetch by sha256 | AGENTS.md support landed in 2.1.277 (reads AGENTS.md instead when no CLAUDE.md) and 2.1.281 extended it to Bedrock, Vertex, Foundry, LLM gateways and telemetry-disabled sessions | mined | 2026-10-22 | 2027-01-20 | corpus/knowledge/alwayson-rule-files-round53.md |

### Gate record

- **S043** — https://code.claude.com/docs/en/memory.md, opened 2026-10-22T20:04:43Z, HTTP 200, 51,971 B, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. Quote (`memory.md:357`): "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it | Your `CLAUDE.md` files only". Supporting quotes: `:356` (AGENTS.md only when none counts), `:358` (import case), `:364` ("Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later."), `:368` (default rule), `:378` (Not read list), `:391` (both-files order and dedupe), `:436` ("Claude sees `AGENTS.md` only if it decides to open the file"), `:437` ("Either way Claude reads the content once."), `:442` (import shape), `:452` and `:455` (symlink), `:619` (200 lines / 4 MiB skip), `:88` (200-line target), `:90` and `:94` (outdated instructions), `:51` (facts held every session), `:102` (import syntax), `:301` (managed inline `claudeMd`), `:333` (`claudeMdExcludes`), `:473` (import appends a one-time copy to CLAUDE.md).
- **S044** — https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md, opened 2026-10-22T20:04:46Z, HTTP 200, 1,070,244 B, sha256 `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49`. Quote (`changelog.md:2225`): 'Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in `/config`' (21 words). Quote (`:2060`): "Changed AGENTS.md support to also work on Amazon Bedrock, Google Vertex AI, Microsoft Foundry, LLM gateways, and sessions with telemetry disabled" (21 words). The changelog top at fetch time is `## 2.1.308` (`:3`), so both entries are historical, and the memory page's v2.1.277 floor (`:364`) is consistent with `:2225`.

## 4. Q30 sweep for the negatives

The negatives in this report are: (a) `GEMINI.md` is not an always-on name, (b) no config key names an alternate rule file, (c) `./CLAUDE.md` vs `./.claude/CLAUDE.md` precedence is unstated. Each leg:

1. **Vendor changelog / release notes.** `CHANGELOG.md` (`main`, 20:04:46Z, 1,070,244 B, `121129bc…`, 9,372 lines). Greps: `GEMINI.md` 0; `gemini` (case-insensitive) 0; `instructionFiles` 0; `claudeMd` 2, both unrelated to an alternate name (`:3141` managed `claudeMd` approval, `:3659` `claudeMdExcludes` and symlinked rules). `AGENTS.md` 4 hits: the two entries above, a symlink fix (`:1002`) and a subdirectory attachment fix (`:1080`).
2. **Current docs.** The vendor publishes no docs source tree: the public repo root tree (https://github.com/anthropics/claude-code/tree/main, 20:07:46Z, 200, 314,089 B, `77a889bc…`) lists `.claude-plugin`, `.devcontainer`, `examples`, `.github`, `mods`, `plugins`, `Script`, `scripts`, `.vscode` — no `docs/` directory; the README (20:10:01Z, 200, 2,873 B, `aa0d8b80…`, `:9`, `:17`) sends readers to code.claude.com. Substitute sweep: the vendor's complete current docs export `llms-full.txt` (20:05:28Z, 200, 9,614,681 B, `1a581620…`, 121,692 lines). Greps: `GEMINI.md` 0; `gemini` 2, both the `/import` command row (`llms-full.txt:59879`) and `/init`'s offer to carry Gemini CLI configuration over with `/import` (`:59880`); `AGENTS.local.md` 1 (the "not read" bullet); `claudeMd`/`instructionFiles` only as in S043 plus the settings reference (`:33806`, `:33812`, `:90942`). The page index `llms.txt` (20:05:13Z, 200, 63,682 B, `b7064ac5…`) carries no AGENTS.md-specific page; the memory page is the page, linked twice.
3. **Lane corpus.** `grep -rn -i "gemini\.md" corpus/ SKILL.md` → 7 hits, all omp/provider-side classes: `corpus/knowledge/instruction-surface-census-round13.md:76`, `:93`, `:146-147`, `:348`, `:479`, and `corpus/knowledge/instruction-surface-remeasure-round13.md:38`. None claims Claude Code reads it. `corpus/knowledge/claude-md-surface.md` records only the host's loader strings and a cold surface, no AGENTS.md precedence.

Disposition: (a) is stated positively from the vendor's name enumeration and the all-pages absence, with the Gemini path documented as a migration; (b) rests on the closed mode list (`:390-393`) plus the all-pages settings grep; (c) is recorded merely as unstated in the opened page — no client-level negative is claimed. No `silent` label is used. The literal docs-source-tree leg is unavailable (no published tree), which is recorded here rather than hidden; if the L1 counts that as an incomplete Q30 sweep, the negative stays "not checked" and none of the positive quotes above change.

## 5. Rejected candidates

- **`https://code.claude.com/docs/llms-full.txt`** (20:05:28Z, 200, 9,614,681 B, `1a581620…`) — sweep-only, not a row: it re-renders the pages S043 already cites (its `llms-full.txt:33509` is the same memory page), its synthetic line numbers are not stable anchors, and it teaches only the absence counts recorded in §4.
- **`https://code.claude.com/docs/llms.txt`** (20:05:13Z, 200, 63,682 B, `b7064ac5…`) — navigation index; no rule text; confirms there is no separate AGENTS.md page.
- **`https://github.com/anthropics/claude-code/tree/main`** (20:07:46Z, 200, 314,089 B, `77a889bc…`) — public repo root; no `docs/` tree; used only as the Q30 tree check.
- **`https://raw.githubusercontent.com/anthropics/claude-code/main/README.md`** (20:10:01Z, 200, 2,873 B, `aa0d8b80…`) — points at the docs; no always-on content.
- **`https://api.github.com/repos/anthropics/claude-code/contents/`** (20:05:28Z, 403, 280 B, `2282f9ba…`) — rate-limited; not a source, not a check.
- **Claude Code settings-reference / commands pages individually** — not opened on their own; their text was read inside the all-pages export and is cited only for the `claudeMd` and `/import` facts above. A row would need its own canonical-page open with sha256.
- **GEMINI CLI docs** — out of this seat's client; not opened, not a candidate row.

## 6. Limits and observations for the integrator

- These are vendor-documentation statements, not a measurement of any installed Claude Code binary. No Claude Code CLI was run (no paid model call, and no version/help introspection was needed). Whether the loader in a shipped build behaves as documented is not measured here.
- The counter's instrument contract is other seats' work; this report only shows that the six alwayson.07 cases have vendor text behind them and that the six alwayson.04 cases do not.
- The 4 MiB skip is documented for "a CLAUDE.md file"; applying it to AGENTS.md is [INFERENCE], not a quote.
- The `/import gemini` channel is documented in the all-pages export (`llms-full.txt:59879-59880`) and explained by memory.md `:473`: it "appends a one-time copy of instruction files such as `AGENTS.md` to the matching `CLAUDE.md`". It is a migration action, not an always-on read; it does not make GEMINI.md a canonical name, but it is the reason the knowledge entry should say "not an always-on name", not "not read at all".
- The changelog was fetched from a mutable branch tip; `121129bc…` is the recorded identity. The GitHub API could not pin the commit (403 rate limit).
- The SOURCES rows are drafts; no registry row, lesson, knowledge entry, counter, baseline or fixture was edited by this seat. The `used-by` path is the planned entry `corpus/knowledge/alwayson-rule-files-round53.md`, which is not yet on disk.
- Fetched bytes for every value above are under `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/` (`memory.md`, `changelog.md`, `llms.txt`, `llms-full.txt`, `repo.html`, `README.md`, `gh-contents.json`, and the `headers-*.txt` files). Scratch is not evidence; the values in §1 and §3 are the record.
