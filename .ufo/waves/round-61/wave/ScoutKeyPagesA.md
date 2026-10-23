# ScoutKeyPagesA — canonical frontmatter-key pages

Seat `kotoba-r61-wave-ScoutKeyPagesA`. Read-only hunt. No lane file written except this report. No git/jj mutation. No dispatch. Registry checked: `corpus/SOURCES.md` (S001–S111). Round-60 census practice followed: no `/de/` or `/ja/` locale copies, no `enterprise-cloud@latest` alias, no changelog or nav page as a candidate.

A URL is **unopened** here only when that exact URL string is absent from `corpus/SOURCES.md`. A duplicate is returned only as a declared re-open of S043, S047, S048, or S049.

## Result

| Client | Candidate | Registry | What the page enumerates |
|---|---|---|---|
| Claude Code `paths` | `https://code.claude.com/docs/en/claude-directory.md` | **unopened** | `rules/*.md` frontmatter fields are exactly `` `paths` `` (one table cell) |
| Claude Code `paths` | `https://code.claude.com/docs/en/memory.md` | **re-open of S043** (also already S103; bytes drifted) | prose: `` `paths` is the only field `` plus a one-row field table |
| VS Code / Copilot `applyTo` | `https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide.md` | **unopened** | VS Code tab: frontmatter keywords `` `applyTo` `` and `` `excludeAgent` ``; `applyTo:` takes a glob |
| VS Code / Copilot `applyTo` | `https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md` | **unopened** | GitHub.com (not the IDE): same two keywords; `applyTo:` takes a glob. Not the enterprise alias |
| Cursor `globs` | `https://cursor.com/docs/rules` | **re-open of S049**, and byte-identical to already-opened S108 | names the three fields `alwaysApply`, `description`, `globs`; `globs:` takes a path |
| Cursor `globs` | no second candidate | — | the typed field table is already S088 (see below). No unopened cursor.com page in `llms.txt` lists the set |

No closed field table for `applyTo` was found on an unopened URL. The three-field VS Code table (`name`, `description`, `applyTo`) is already S105, which is not S047. S047's `.md` URL is HTTP 404 today.

## Claude Code — `paths`

### 1. Unopened — Explore the .claude directory

URL: `https://code.claude.com/docs/en/claude-directory.md`

Listed in `https://code.claude.com/docs/llms.txt` (HTTP 200, 63682 B, final URL unchanged). Not in `corpus/SOURCES.md` (grep `claude-directory` → no match). English `/docs/en/` path, not a locale copy. How-to/reference page, not a changelog.

Fetch (`date -u` immediately before the batch: `Fri 23 Oct 2026 07:11:10 PM UTC`; response `date: Fri, 23 Oct 2026 19:11:10 GMT`; `content-type: text/markdown; charset=utf-8`; script exit 0, curl did not fail):

```
curl -sSL --max-time 40 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -D claude-directory.hdr -o claude-directory.body -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective} redir=%{num_redirects} ctype=%{content_type}\n' \
  'https://code.claude.com/docs/en/claude-directory.md'
```

```
http=200 bytes=31144 final=https://code.claude.com/docs/en/claude-directory.md redir=0 ctype=text/markdown; charset=utf-8
sha256 1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14
```

Grounding lines (this fetch). Heading `## Frontmatter fields by file` is line 84. The rule row is line 94. Line 90 is the skill row, which also contains `paths` among many other fields — that is not the rule set.

```
86|Skills, command files, subagents, output styles, and rules read their configuration from YAML [frontmatter](https://code.claude.com/docs/en/glossary.md#frontmatter) at the top of the file, and each accepts its own set of fields. This table lists the field names for each file and links to the reference that describes them.
88|| File | Frontmatter fields | Reference |
90|| `skills/<name>/SKILL.md` | `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility` | [Skill frontmatter](https://code.claude.com/docs/en/skills.md#frontmatter-reference) |
94|| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |
```

The rule frontmatter set on this page is the single name `paths`. The link target is the S043 URL plus `#rules-frontmatter-reference`.

Not used as a second unopened candidate: `https://code.claude.com/docs/en/large-codebases.md` (HTTP 200, 35669 B, sha256 `d41576eed15d2393913d0b4dcd52e5a794920358b820237610967860cdc06f70`, same batch, exit 0). Line 116 mentions a rule's `` `paths:` `` glob in a comparison table. It does not list the field set.

### 2. Declared re-open of S043 — How Claude remembers your project

URL: `https://code.claude.com/docs/en/memory.md` — byte-identical URL to S043 and to S103. Declared re-open, not a new open.

Fetch (`date -u`: `Fri Oct 23 07:13:23 PM UTC 2026`; response `date: Fri, 23 Oct 2026 19:13:23 GMT`; `content-type: text/markdown`; curl exit 0):

```
curl -sSL --max-time 40 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -D claude-memory.hdr -o claude-memory.body -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective} redir=%{num_redirects}\n' \
  'https://code.claude.com/docs/en/memory.md'
```

```
http=200 bytes=55354 final=https://code.claude.com/docs/en/memory.md redir=0
sha256 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
```

S103 recorded HTTP 200, 54043 B, sha256 `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` at 2026-10-23T12:08:16Z. This fetch is **not** those bytes (55354 vs 54043; sha differs). Both bodies are 664 lines. A line diff against the committed snapshot `.ufo/waves/round-60/snapshots/S103.page` shows 47 differing lines. Line 250 (the `` `paths` `` table row) is unchanged. Line 246 differs only in the glossary link (`https://code.claude.com/docs/en/glossary.md#frontmatter` now, `/docs/en/glossary.md#frontmatter` in S103). The only-field sentence is still on line 246.

```
244|#### Rule frontmatter reference
246|Configure a rule with YAML [frontmatter](https://code.claude.com/docs/en/glossary.md#frontmatter) between `---` markers at the top of the file. `paths` is the only field Claude Code reads from a rule; any other field is ignored without an error. Claude Code removes the frontmatter before loading the rule into context.
248|| Field | Required | Description |
250|| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

[INFERENCE] For A1, the canonical Claude Code **rule** key set grounded on these two pages is `{paths}`. `patterns` and `claudeMdExcludes` are not in that set. `paths` on a skill file is a different file class (directory line 90). This seat did not run the counter.

## VS Code / Copilot — `applyTo`

### 1. Unopened — IDE how-to, VS Code tab

URL: `https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide.md`

Not in `corpus/SOURCES.md` (grep `add-repository-instructions-in-your-ide` → no match). Path is `/en/`, not `enterprise-cloud@latest`, not `/de/` or `/ja/`. Not the CLI how-to (that URL is S048 / S106).

Fetch (same 07:11:10 PM UTC batch; response `date: Fri, 23 Oct 2026 19:11:10 GMT`; `content-type: text/markdown; charset=utf-8`; `content-length: 46556`; curl exit 0):

```
curl -sSL --max-time 40 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -D gh-ide.hdr -o gh-ide.body -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective} redir=%{num_redirects} ctype=%{content_type}\n' \
  'https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide.md'
```

```
http=200 bytes=46556 final=https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide.md redir=0 ctype=text/markdown; charset=utf-8
sha256 9d76ff1414cca75440157d253ccdfd83848daacd77f27ec9bec6cc482adfb59b
```

The markdown is a multi-tool article. The VS Code copy is lines 5–196 (`<!-- START VS CODE TAB -->` at line 5, `<!-- end of VS Code tab -->` at line 196). Visual Studio starts at line 198 and repeats the same key later (line 252). Ground the VS Code tab, not the later copy.

```
62|4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.
68|   applyTo: "app/models/**/*.rb"
90|5. Optionally, to prevent the file from being used by either Copilot cloud agent or Copilot code review, add the `excludeAgent` keyword to the frontmatter block. Use either `"code-review"` or `"cloud-agent"`.
96|   applyTo: "**"
97|   excludeAgent: "code-review"
```

Line 68 is key form `applyTo:` with value token `app/models/**/*.rb` (contains `*`). The two frontmatter keywords this tab names are `applyTo` and `excludeAgent`. There is no Field/Required/Description table on this page.

### 2. Unopened — GitHub.com how-to (not the IDE, not the enterprise alias)

URL: `https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md`

Not in `corpus/SOURCES.md` (grep `add-repository-instructions` → no match). This is the `/en/` article. Round-60 rejected only the `enterprise-cloud@latest` rendering of a Copilot how-to; this fetch did not use that host prefix. Title line 1 is `Adding repository custom instructions for GitHub Copilot`. Line 7 sends IDE setup to candidate 1. Line 146 limits path-specific instructions on GitHub.com to Copilot cloud agent and Copilot code review.

Fetch (`date -u`: `Fri Oct 23 07:14:08 PM UTC 2026`; curl exit 0):

```
curl -sSL --max-time 40 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -D gh-web-repo.hdr -o gh-web-repo.body -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective} redir=%{num_redirects}\n' \
  'https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md'
```

```
http=200 bytes=22858 final=https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md redir=0
sha256 c29d67f0a342f2ae8de6bda04b8c7e7ce9a1341d61eaffdeee9a4fc8c9ced635
```

```
146|> Currently, on GitHub.com, path-specific custom instructions are only supported for Copilot cloud agent and Copilot code review.
154|4. At the start of the file, create a frontmatter block containing the `applyTo` keyword. Use glob syntax to specify what files or directories the instructions apply to.
160|   applyTo: "app/models/**/*.rb"
182|5. Optionally, to prevent the file from being used by either Copilot cloud agent or Copilot code review, add the `excludeAgent` keyword to the frontmatter block. Use either `"code-review"` or `"cloud-agent"`.
188|   applyTo: "**"
189|   excludeAgent: "code-review"
```

### Not a candidate — S047 re-open fails; S105 already holds the field table

S047 URL `https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md` (`date -u` `Fri Oct 23 07:14:08 PM UTC 2026`, curl exit 0):

```
http=404 bytes=9 final=https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md redir=0
sha256 0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5
```

Body is the nine bytes `Not Found`. Not used.

Already opened, not returned as a new URL: S105 `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md`. Committed snapshot `.ufo/waves/round-60/snapshots/S105.page` lines 148–164 are the closed table (`name`, `description`, `applyTo`) and the example `applyTo: '**/*.py'`. That table does **not** name `excludeAgent`. The two unopened GitHub how-tos do. [INFERENCE] A canonical key set copied only from S105 would omit `excludeAgent`; a set copied only from the how-tos would omit `name` and `description`. This seat did not decide the set.

Also fetched and rejected as enumerations (HTTP 200, no `applyTo` / frontmatter field table): concepts page `…/prompting-and-context/custom-instructions.md` (14669 B, sha256 `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933`, 07:13:23 PM UTC); support matrix `…/reference/custom-instructions-support.md` (14612 B, sha256 `90150f5a25f493640b9a52da6ac0a363ece8ece13429bd2c6c4e5ebb0c44e814`); cheat sheet `…/reference/customization-cheat-sheet.md` (10699 B, sha256 `25f43326fb38833208df14cc9d9f6a72bf182f0785bf5b2a86748953a0fc3b25`, names the path-specific file glob but not the frontmatter key); VS Code learn page `https://code.visualstudio.com/learn/customizations/2-instructions.md` (6726 B, sha256 `2d842e6b67e5b82b36ec51542a1026b85cef16b0a79d0e9bea2de3444d6f22e7`). CLI how-to left as S048/S106; not re-opened.

## Cursor — `globs`

### 1. Declared re-open of S049 — live rules page (already S108)

S049's recorded URL is `https://cursor.com/docs/rules.md`. That URL is **404** today (`date -u` `Fri Oct 23 07:13:22 PM UTC 2026`, curl exit 0, `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`):

```
http=404 bytes=389 final=https://cursor.com/docs/rules.md redir=0
sha256 4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1
```

Head: `# Page not found`. Same 404 body for `https://cursor.com/docs/reference/plugins.md` and for `https://cursor.com/docs/reference/rules` (the last fetched 07:14:10 PM UTC, 389 B, same sha256, exit 0, `Accept: text/markdown`).

The page `llms.txt` links as `https://cursor.com/docs/rules.md` is served, with `Accept: text/markdown`, at `https://cursor.com/docs/rules`. That URL is already S108, whose row says it re-opens S049. Same bytes as S108's recorded sha256 and as committed snapshot `.ufo/waves/round-60/snapshots/S108.page`.

Fetch (`date -u` `Fri Oct 23 07:13:22 PM UTC 2026`; response `date: Fri, 23 Oct 2026 19:11:10 GMT`; `content-type: text/markdown; charset=utf-8`; `x-matched-path: /api/raw`; curl exit 0):

```
curl -sSL --max-time 40 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' \
  -D cursor-rules.hdr -o cursor-rules.body -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective} redir=%{num_redirects}\n' \
  'https://cursor.com/docs/rules'
```

```
http=200 bytes=17403 final=https://cursor.com/docs/rules redir=0
sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
```

```
63|Under the hood, the three frontmatter fields interact to determine when a rule is included:
65|| `alwaysApply` | `description` | `globs`  | Behavior                                                         |
85|globs: src/components/**/*.tsx
```

Line 65 names the three fields. Line 85 is key form `globs:` with value `src/components/**/*.tsx`. Alias rejected: `https://cursor.com/docs/context/rules` with the same Accept header returned `http=200 bytes=17403 final=https://cursor.com/docs/rules redir=1` and the same sha256 (07:13:23 PM UTC, curl exit 0). That is the redirect round-60 already refused.

### 2. No unopened second URL

`https://cursor.com/llms.txt` (HTTP 200, 24815 B, fetched 07:09:50 PM UTC) lists one rules article, `https://cursor.com/docs/rules.md`, plus help `https://cursor.com/help/customization/rules.md` (already S052). It does not list a separate rules-frontmatter reference. Probing `https://cursor.com/docs/reference/rules` 404'd (above).

Already opened, not a new candidate: S088's document. Registered URL `https://cursor.com/docs/reference/plugins.md` is the 404 above. The unsuffixed URL returns S088's recorded sha256 (`3bbf36f3…`, SOURCES row `3bbf36f3320382adb68509aa758e2e764…`):

```
curl … -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' 'https://cursor.com/docs/reference/plugins'
http=200 bytes=30324 final=https://cursor.com/docs/reference/plugins redir=0
sha256 3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204
```

`date -u` `Fri Oct 23 07:13:22 PM UTC 2026`, curl exit 0, `content-type: text/markdown`. Field table:

```
184|### Rule frontmatter fields
188|| `description` | string          | Brief description of what the rule does                                         |
189|| `alwaysApply` | boolean         | If `true`, rule applies to all files. If `false`, rule is available on request. |
190|| `globs`       | string or array | File patterns the rule applies to (e.g., `"**/*.ts"`)                           |
```

This is the typed enumeration. It is S088, not an unopened URL and not a re-open of S049. Not proposed as a new row.

[INFERENCE] The Cursor rule frontmatter set named on the live rules page and on S088 is `{description, alwaysApply, globs}`. `globs` is the path key. `rules` and `order`, which round-60 `ExecKeyForms` saw pass a form check, are not in that set.

## Census rejections (this seat)

- Locale copies (`/de/`, `/ja/`) not requested.
- `enterprise-cloud@latest` not requested. The GitHub.com candidate uses `/en/`.
- `https://cursor.com/docs/context/rules` redirects to the base rules page (alias).
- `https://cursor.com/docs/rules.md` and `https://cursor.com/docs/reference/plugins.md` are 404. `llms.txt` still prints the `.md` forms.
- Changelog, release notes, and nav/index pages were not used as candidates. `llms.txt` indexes were used only to choose URLs.

## Installs

no installs

## Blockers

none

Produced: five measured candidate URLs (three unopened, two declared re-opens) for the per-client scoped-rule frontmatter key set, plus the S088/S105 already-opened tables those new pages do not replace.
