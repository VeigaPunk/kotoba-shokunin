Result: DONE — agents.md documents exactly one always-on file name (`AGENTS.md`, at the repository root), nearest-file precedence between `AGENTS.md` files at different depths, and exactly three redirect forms (a symlink beside a renamed old name, an Aider `read:` key, a Gemini CLI `context.fileName` key); it states no size limit, no dated-text rule, and never names `CLAUDE.md`, `GEMINI.md` or an `@AGENTS.md` import; two SOURCES rows drafted, four candidates rejected.

Round 53, wave 1 (build), C2 source basis. Seat `KotobaR53.ScribeAgentsMdSpec`. Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. The only lane file written is this report. All fetched or cloned bytes live in `/fast/scratch/hyaku/kotoba-r53/ScribeAgentsMdSpec/` (`fetch/` for downloads, `repo/` and `repo-full/` for clones). No tool was installed or upgraded; no model call of any kind was made; the lane, its Git index and its jj state were not touched.

## 1. Method

`https://agents.md/` is a single-page Next.js site; its own repository `agentsmd/agents.md` renders it. Because the deployed page is one HTML line, every quote is pinned twice: a byte offset in the fetched HTML, and a line number in the pinned source file at commit `d001185d792eb6402a58e4cbef1c228b309ec25d` (the `main` tip at fetch time, 38 commits of history). Each quoted string was located in the deployed bytes with `bytes.find()` and in the source with `cat -n`; both locations are given. Where the source wraps a file name in a `<code>` element, the quote renders it in backticks; the words are unchanged.

Commands, all with observed output:

```
curl -sS -o agentsmd.html -w 'HTTP %{http_code} bytes %{size_download}\n' https://agents.md/
HTTP 200 bytes 81690                     # 2026-10-22T20:04:34Z
sha256sum agentsmd.html                   # 06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979
curl -sS -o agentsmd2.html https://agents.md/   # 2026-10-22T20:06:48Z
HTTP 200 bytes 81690 ; sha256 identical   # byte-stable across the two fetches
git clone -q --depth 1 https://github.com/agentsmd/agents.md repo
git -C repo rev-parse HEAD                # d001185d792eb6402a58e4cbef1c228b309ec25d
git clone -q --filter=blob:none https://github.com/agentsmd/agents.md repo-full
git -C repo-full rev-list --count HEAD    # 38
```

## 2. Answers

### 2.1 Which always-on file names it reads

agents.md is a format page, not a runtime, so "reads" here means "specifies". The page specifies one name and one location. `components/HowToUseSection.tsx:10-11`:

> Create an AGENTS.md file at the root of the repository.

(`Hero.tsx:20-33`, the same claim in framing: "A simple, open format for guiding coding agents, used by over 60k open-source projects.") The only other name anywhere on the site is the singular pre-existing name `AGENT.md`, which the FAQ treats as a retired name to be migrated away from (2.3). Absence checks, all run over the whole 38-commit tree and the deployed bytes: `grep -c -i claude fetch/agentsmd.html` → `0`; `grep -ri claude repo-full --exclude-dir=.git | wc -l` → `0`; `grep -rn 'GEMINI.md' repo-full | wc -l` → `0`; `grep -rn '@AGENTS' repo-full | wc -l` → `0`; `grep -rn -i -E 'cursorrules|copilot-instructions|CONVENTIONS\.md|\.rules' repo-full` → no output. The compatibility marquee (`CompatibilitySection.tsx:14-142`) lists 23 agents (Codex, Amp, Jules, Cursor, Factory, RooCode, Aider, Gemini CLI, goose, Kilo Code, opencode, Phoenix, Zed, Semgrep, Warp, GitHub Copilot coding agent, VS Code, Ona, Devin, Windsurf, UiPath, Augment Code, Junie) and no Claude entry; the section title is "One AGENTS.md works across many agents" (`:330`).

**Consequence for C2:** agents.md supports the box's `AGENTS.md` half only. It does not support the `or CLAUDE.md` clause, the `claude-only` PASS case, or the import form.

### 2.2 Two of them in one directory

The page distinguishes two cases and answers only the first.

Different depths (monorepo): the nearest file wins. `HowToUseSection.tsx:35-38`:

> Agents automatically read the nearest file in the directory tree, so the closest one takes precedence and every subproject can ship tailored instructions.

The FAQ repeats the rule with chat precedence. `FAQSection.tsx:18-21`:

> The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.

Two different names in one directory (`AGENTS.md` beside `CLAUDE.md`): not stated. See the Q30 sweep in §3. The page's nearest-file rule is scoped to `AGENTS.md` files; it is not a rule about two clients' rule files sitting side by side. One adjacent fact is on the page: its own migration advice installs a second *name* as a symlink, i.e. a redirect rather than a second file (2.3).

### 2.3 Redirects (symlink, import, config pointing at another name)

Three redirect forms are documented, and none of them is an import. The migration FAQ, `FAQSection.tsx:36`:

> Rename existing files to AGENTS.md and create symbolic links for backward compatibility:

with the command at `:40` — `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`. That is a symlink from the old name to `AGENTS.md`, not from another tool's name.

Two config redirects follow. `FAQSection.tsx:54-58`: "Configure Aider to use AGENTS.md in `.aider.conf.yml`:" with the line `read: AGENTS.md`. `FAQSection.tsx:72-80`: "Configure Gemini CLI to use AGENTS.md in `.gemini/settings.json`:" with

```
{ "context": { "fileName": "AGENTS.md" }, }
```

There is no `@AGENTS.md` import form on the site: `@AGENTS` occurs zero times in the deployed bytes and zero times in the 38-commit tree. **Consequence for C2:** the counter's `symlink-redirect` PASS case is grounded here; the `import-redirect` PASS case is not — it rests on Claude Code's memory documentation alone, as the plan already states.

### 2.4 Size limit

Not documented. The page's own position is only that no fields are required (`FAQSection.tsx:13-16`):

> No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide.

No byte, token, line or truncation rule appears in the source tree: `grep -rn -i -E '\b(limit|token|kb|kilobyte|megab|max(imum)? size|truncat|large file)\b' --include='*.tsx' --include='*.ts' --include='*.md' .` returns four hits, all Next.js rate-limit comments in `pages/index.tsx:39,59,84,157` (`:84` is the word "token" in "access token"); the four `truncat` hits in the deployed HTML at offsets 56,283 / 57,804 / 59,352 / 60,920 are the CSS class `truncate` on repository-card titles. See the Q30 sweep in §3.

### 2.5 Dated or transient content

No rule against it. The page's only maintenance statement is `FAQSection.tsx:27-30`:

> Absolutely. Treat AGENTS.md as living documentation.

**Consequence for C2:** `alwayson.04` ("No dated or transient text") has no support from agents.md. That box's rule comes from the checklist text and the round-7 observed evidence; the counter's FAIL cases are the instrument's parsing decisions, not a vendor rule. Do not cite agents.md in the box-04 provenance.

### 2.6 What the page says about its own governance

`AboutSection.tsx:20-32`: "AGENTS.md is now stewarded by the Agentic AI Foundation under the Linux Foundation." That is stewardship, not a rule about files; it is recorded so no seat re-derives it from the GitHub owner name.

## 3. Q30 sweep (three parts) for each negative

The negatives are (a) no second always-on name, (b) no size limit, (c) no rule for two different names in one directory, (d) no `@`-import. Each sweep used the same three parts.

1. **Changelog or release notes.** No changelog exists to read: `git -C repo-full log --all --name-only --pretty=format: -- '*CHANGELOG*'` → no paths in 38 commits; `git ls-remote --tags https://github.com/agentsmd/agents.md | wc -l` → `0`; `https://github.com/agentsmd/agents.md/releases` → 200, 174,171 B, sha256 `e4a9f4da…`, page contains "There aren't any releases"; `https://agents.md/CHANGELOG.md` → 404, 3,795 B, sha256 `acb61c58…`; `https://raw.githubusercontent.com/agentsmd/agents.md/main/CHANGELOG.md` → 404, 14 B, sha256 `d5558cd4…`. There is no release-notes artifact, so part 1 returns "the vendor publishes none", not "unchecked".
2. **Current docs source tree.** Full clone at `d001185d…` (38 commits, `main` tip). The site is `pages/index.tsx` plus eleven components and five icon components, one route; the greps in 2.1 and 2.4 were run over the whole tree, not only the rendered page. The rendered page is byte-identical to a second fetch and carries every quoted sentence, so the pinned tree is the tree that renders it.
3. **Lane corpus grep.** `grep -rn -i 'agents\.md' corpus/` → 120 hits, of which exactly two concern this site: `corpus/SOURCES.md:17` (row S004) and `corpus/lessons/round-46.md:66` (the S004 fetch row). Neither attributes a second file name, a size cap or an import form to agents.md. The nearest lane text, `corpus/knowledge/agents-md-and-dispatch-surfaces.md:31-32`, is marked "Craft implication (opinion)" and claims only that bytes are paid every session — no vendor limit. `corpus/knowledge/claude-md-surface.md:36-38` records a dual-name collision risk from the lane's own census, not from agents.md.

So all four negatives are recorded as **not documented**, each with the three parts above, not as "silent".

## 4. Draft SOURCES rows (exact column shape; S-number left as S0xx)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | AGENTS.md — open format site — https://agents.md/ | spec | A | The open AGENTS.md convention: canonical file name and location, nearest-file precedence in monorepos, and the redirect forms the page documents for other tools (format page, not a measurement of any client) | `HowToUseSection.tsx:10-11` (root file), `:35-38` (nested, nearest wins), `FAQSection.tsx:18-21` (conflict rule), `:13-16` (no required fields), `:27-30` ("living documentation"), `:31-48` (migration symlink), `:49-66` (Aider `read:`), `:67-88` (Gemini CLI `context.fileName`); live page fetched 2026-10-22T20:04:34Z (200, 81,690 B, sha256 `06b65de9…`), byte-identical on re-fetch 20:06:48Z; the round-46 record of the same URL carries `e3a5b9a4…`, so the fetched bytes are not stable across builds while the conflict sentence is unchanged verbatim | supersedes S004 — the canonical name is `AGENTS.md` at the repository root and a nested `AGENTS.md` wins for its subtree, with explicit user chat prompts above both; the only redirect forms the page shows are a symlink beside a renamed old name (`mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`) and two client config keys that point a tool at the name (Aider `read: AGENTS.md`, Gemini CLI `context.fileName`); it states no size limit, no dated-text rule, and never names CLAUDE.md, GEMINI.md or an `@`-import | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | agentsmd/agents.md — site source at commit d001185d — https://github.com/agentsmd/agents.md/tree/d001185d792eb6402a58e4cbef1c228b309ec25d | code | A | The page source that renders https://agents.md/, supplying the line-anchored quotes and the absence sweep behind the page's name, precedence, redirect and size statements | `components/FAQSection.tsx:11-89` (sha256 `f8840671…`), `components/HowToUseSection.tsx:5-41` (`ea4b43e1…`), `components/CompatibilitySection.tsx:14-142` (`925aa7df…`), `components/Hero.tsx:20-33`, `components/WhySection.tsx:56-60`, `components/AboutSection.tsx:20-32`; cloned 2026-10-22T20:05Z at HEAD `d001185d…` (38 commits, one page route); no CHANGELOG file in any commit, 0 tags, releases page "There aren't any releases" (fetched 20:10:51Z, 200, 174,171 B, sha256 `e4a9f4da…`) | The prose the live page shows is present verbatim in these source lines; the compatibility marquee names 23 agents and no Claude; the tree contains no second always-on file name and no size or truncation rule, so a name or cap the page does not mention is not documented anywhere in the site's own source | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |

Notes for the L1: both rows are `tier A` by the registry's own usage for a live primary format page and its pinned source (`S004` page, `S016`/`S041` source pins); `90d` matches S004's recheck cadence and the page's lack of releases or tags. Row 1 supersedes S004 (same URL, S004 was `queued` and never re-opened, and its teach cell carried only the conflict sentence); row 2 is new. If the L1 prefers one row per URL, merge row 2's anchor text into row 1 and keep the tree hash. Append-only: the L1 appends both rows; this seat writes only this report.

## 5. Rejected candidates

| candidate | why rejected |
|---|---|
| `Technical_Charter.pdf` in the same repository (229,296 B, sha256 `f4f2a02a…`) | It is the Linux Foundation / Agentic AI Foundation charter. `pdftotext -layout` → 354 lines; a grep for `preced`, `closest`, `near`, `monorepo`, `nest`, `limit`, `size`, `token`, `CLAUDE`, `GEMINI`, `symlink`, `alias`, `import`, `redirect`, `AGENT.md`, `conflict`, `scope` matches only governance clauses (lines 16, 20, 25, 133, 171-172, 229). It carries no rule about file names, precedence, redirects or size. |
| The repository's own `AGENTS.md` | It is an instance of the format (Next.js instructions for this site), not the format's authority. Opening it confirms nothing about the convention. |
| The 23 outbound links in the compatibility marquee (aider.chat, Gemini CLI github, opencode docs, zed, warp, …) | Each is another client's page, not an agents.md statement; several are other seats' targets this round. Opening them here would double-count and is out of this seat's slice. |
| GitHub issues / PR discussions of `agentsmd/agents.md` | Not opened; they are not the vendor's documentation and a claim about the format must rest on the page or its source. Recorded as unopened, not as absent. |

## 6. Gate record

| URL | accessed (UTC) | status | bytes | sha256 | quote (≤25 words) | location |
|---|---|---|---|---|---|---|
| https://agents.md/ | 2026-10-22T20:04:34Z | 200 | 81,690 | `06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979` | "The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything." | deployed HTML single line, byte offset 66,581; same sentence `components/FAQSection.tsx:20` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Agents automatically read the nearest file in the directory tree, so the closest one takes precedence and every subproject can ship tailored instructions." | offset 63,989; `HowToUseSection.tsx:38` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Create an AGENTS.md file at the root of the repository." | offset 62,799; `HowToUseSection.tsx:10-11` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Rename existing files to AGENTS.md and create symbolic links for backward compatibility:" | offset 67,467; `FAQSection.tsx:36`; command `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md` at offset 71,464 / `:40` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Configure Aider to use AGENTS.md in `.aider.conf.yml`:" | offset 71,752; `FAQSection.tsx:54`; value `read: AGENTS.md` at offset 75,726 / `:58` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Configure Gemini CLI to use AGENTS.md in `.gemini/settings.json`:" | offset 75,977 (76,024 for the file name); `FAQSection.tsx:72-80`; JSON `{"context": {"fileName": "AGENTS.md"},}` at offset 79,964, key `fileName` at 79,993 |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide." | offset 66,285; `FAQSection.tsx:15` |
| https://agents.md/ (same fetch) | 2026-10-22T20:04:34Z | 200 | — | — | "Absolutely. Treat AGENTS.md as living documentation." | offset 67,214; `FAQSection.tsx:29` |
| https://agents.md/ (re-fetch) | 2026-10-22T20:06:48Z | 200 | 81,690 | `06b65de9…` (identical) | — | byte-stable, ETag `vt6j5odein1r0m` |
| https://raw.githubusercontent.com/agentsmd/agents.md/main/README.md | 2026-10-22T20:04:42Z | 200 | 2,015 | `60ec51c226560aaf2c49a0b8a2452c8cf24459c37a816764979dc917076c7afb` | "AGENTS.md is a simple, open format for guiding coding agents." | `readme.md:5` |
| https://github.com/agentsmd/agents.md (clone) | 2026-10-22T20:05Z | clone | — | commit `d001185d792eb6402a58e4cbef1c228b309ec25d` | — | 38 commits; `FAQSection.tsx` sha256 `f884067162ad6b4a629904664f8ffe93bce92296b05ac971027176dbf1eb1e32` |
| https://github.com/agentsmd/agents.md/tree/d001185d… | 2026-10-22T20:08:51Z | 200 | 290,205 | — | — | source listing |
| https://github.com/agentsmd/agents.md/releases | 2026-10-22T20:10:51Z | 200 | 174,171 | `e4a9f4da40340bdc62699583d2afc42893a2bafbf0702fece7daaa5445cde8f6` | "There aren't any releases" | absence of release notes |
| https://agents.md/CHANGELOG.md | 2026-10-22T20:10:51Z | 404 | 3,795 | `acb61c58a61ca70595400e480d47cee4cea90f54a28303289e72ebaf5f68d6a8` | — | absence |
| https://raw.githubusercontent.com/agentsmd/agents.md/main/CHANGELOG.md | 2026-10-22T20:10:51Z | 404 | 14 | `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed` | — | absence |
| `git ls-remote --tags https://github.com/agentsmd/agents.md` | 2026-10-22T20:08:52Z | exit 0 | 0 refs | — | — | no tags, so no release-notes surface |

## 7. Limits and what this does not establish

- The page-vs-source identity is established sentence by sentence for every quote above plus the framing strings in §2.1, not by a whole-page diff: the deployed HTML has no sourcemap or commit marker, so "the live page is rendered from exactly `d001185d`" is `[INFERENCE]` from those matching strings and the one-page route.
- The hash difference against the round-46 S004 record (`e3a5b9a4…` vs `06b65de9…`) is recorded as a byte difference only. The round-46 row does not say how its bytes were fetched (raw HTML or reader text), so whether the page's *content* changed is `[INFERENCE]` and is not claimed.
- This seat did not open Claude Code's memory documentation; the `@AGENTS.md` import and the "reads CLAUDE.md only with both present" behaviour remain grounded there (plan § C2, `verifiers/check_alwayson_boxes.py` docstring), not here. agents.md neither supports nor contradicts them.
- Nothing here measures a client's loader. agents.md states a convention; whether any given binary follows it is out of this slice.
- Not checked (recorded, not swept): GitHub issues/PRs of `agentsmd/agents.md`; the `dkundel/logo-handling` and `remove-unused-package-lock` branches.

## 8. Findings for the C2 build

1. `alwayson.07`'s four PASS cases are not equally sourced. `agents-only` and `symlink-redirect` are grounded in agents.md; `import-redirect` and `claude-only` are grounded in Claude Code's memory documentation (plus the box text). A provenance line that cites agents.md for all four would be a Q23 mis-attribution.
2. `two-rule-files` FAIL is a lane policy ("one canonical name … or an explicit redirect"), not an agents.md statement; agents.md is silent on `AGENTS.md` beside `CLAUDE.md` in one directory. `prose-mention` FAIL is the frozen counter's own parsing rule (a redirect must be a machine form — its docstring says "A prose mention of AGENTS.md is not an import"), which the delegated instrument must implement; the box text does not say it.
3. `alwayson.04` has no support from agents.md. Its only freshness sentence is "living documentation", which argues for updating the file, not for stripping dates.
4. The page's own migration recommendation is a redirect (`ln -s AGENTS.md AGENT.md`), which is a concrete worked example the instrument's symlink case mirrors; the counter's symlink case points the other way (`CLAUDE.md` → `AGENTS.md`), the same shape with the names reversed.
5. S004 is now stale in its fetch hash and thin in its teach cell; row 1 above supersedes it, and the round-46 gate row (`corpus/lessons/round-46.md:66`) stays as the audit trail.
