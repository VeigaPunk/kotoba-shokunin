# W2ReopenS045 — re-open of SOURCES row S045 (opencode Rules docs)

Result: MIXED — the S045 anchor re-opens byte-identical to every recorded status, byte count and digest, and four of its five
line ranges say what the row claims; but the row's scope cell asserts a "per-directory precedence" the page does not state and
the v1.19.4 loader does not implement, and `rules.mdx:182` is cited as a redirect form when the page lists symlinks only as a
sharing mechanism.

Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc` (branch `master`), read-only. I made no join to the C1/C2 counters;
this seat attacks only the source row and the knowledge entry that rests on it.

## 1. Re-open receipt (independent fetch, 2026-10-22)

| route | UTC | status | bytes | sha256 | content-type | server `date` |
|---|---|---|---|---|---|---|
| https://opencode.ai/docs/rules.md | 2026-10-22T20:39:07Z–20:39:08Z | 200 | 6,684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` | text/plain; charset=utf-8 | Thu, 22 Oct 2026 20:39:08 GMT |
| https://opencode.ai/docs/rules | 2026-10-22T20:39:08Z–20:39:09Z | 200 | 76,861 | `05a6070925ba6a0a74fe23bde1b2cc0329bf7dae8e00ba39cf373001967128e2` | text/html | Thu, 22 Oct 2026 20:39:09 GMT |
| https://opencode.ai/docs/rules/ (trailing slash) | 2026-10-22T20:36:34Z | 200 | 76,861 | same HTML bytes (`cmp` not run on this alias) | text/html | — |

Byte stability: a second full fetch at 20:37:59Z produced the same two digests and `cmp` reported equality for both files
(`md stable`, `html stable`, exit 0). So the row's recorded bytes are reproducible today, not a one-off.

### Anchor cell comparison (row `corpus/SOURCES.md:58` vs this fetch)

| row cell element | row value | observed | verdict |
|---|---|---|---|
| `.md` status / bytes | 200 / 6,684 B | 200 / 6,684 | exact match |
| `.md` sha256 | `dfb242d9…` | `dfb242d9a8c0…` | exact prefix match |
| HTML status / bytes | 200 / 76,861 B | 200 / 76,861 | exact match |
| HTML sha256 | `05a60709…` | `05a6070925ba…` | exact prefix match |
| mdx at dev head `4a6dacec` | sha256 `2d789f84…` | 6,758 B, `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` | exact match |
| "byte-identical at tag v1.19.4" | asserted | tag fetch 6,758 B, same sha `2d789f84…` | holds |
| "prose equals the body" of `rules.mdx` | asserted | served `.md` == mdx lines 6–188, one trailing newline apart (6,684 B vs 6,685 B; first differing char: none) | holds |
| dev head still `4a6dacec` | "at dev head 4a6dacec" | `refs/heads/dev` now `cd1861d9d8ed09aad38720efdb5e6518b6afe28`; `rules.mdx` at that head is still `2d789f84…` | no source drift; the head moved, the file did not |

Tag identity also re-checked read-only: `git ls-remote --tags https://github.com/anomalyco/opencode.git refs/tags/v1.19.4`
→ `148842ef7cb1bc34192b3fff57d0f9721ab9c801` (exit 0), matching the S051 row; `v1.19.3` → `e3c4eb24…`, also matching.

Local files kept under `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS045/`: `rules.md`, `rules.html`, `f_0303ee59` (mdx at
`4a6dacec`), `f_510dff39` (mdx at v1.19.4), `f_c3f4060d` (`instruction.ts` at v1.19.4), `fsutil.ts`.

## 2. Per-line verification

Quotes are verbatim, ≤25 words, line numbers are `packages/web/src/content/docs/rules.mdx` at `4a6dacec` (= v1.19.4, same sha).
Served `.md` line = mdx line − 5 (frontmatter block); the offset was checked on every quote.

### 2.1 SOURCES row S045 locators

| locator | what the row claims it supports | verbatim evidence | verdict |
|---|---|---|---|
| `rules.mdx:77-91` (§ Types → § Claude Code Compatibility) | `CLAUDE.md` as a Claude Code compatibility fallback | `:79` "For users migrating from Claude Code, OpenCode supports Claude Code's file conventions as fallbacks:"; `:81` "**Project rules**: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)" | HOLDS |
| `rules.mdx:95-103` (§ Precedence) | with both present only `AGENTS.md` is used | `:103` "The first matching file wins in each category. For example, if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used." | HOLDS for the taught fact (see D1 for the row's scope wording) |
| `rules.mdx:107-131` (§ Custom Instructions) | `instructions` config array, globs, additive | `:116` `"instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]`; `:131` "All instruction files are combined with your `AGENTS.md` files." | HOLDS |
| `rules.mdx:135-137` (§ Referencing External Files) | it does not parse file references in `AGENTS.md` | `:137` "While opencode doesn't automatically parse file references in `AGENTS.md`, you can achieve similar functionality in two ways:" | HOLDS |
| `rules.mdx:182` (§ Referencing External Files, benefits list) | "documents … symlinks as the redirects" | `:182` "- Share rules across projects via symlinks or git submodules" | BREAKS as a redirect claim; HOLDS only as a mention of symlinks as a sharing mechanism (D2) |

### 2.2 `corpus/knowledge/alwayson-rule-files-round53.md` locators for S045

| locator | what the entry claims | verbatim evidence | verdict |
|---|---|---|---|
| `rules.mdx:77-103` (`:1` source header) | fallback plus precedence span | spans `:77-91` and `:95-103`, both above | HOLDS |
| `rules.mdx:77-91` (`:27`, names column) | `AGENTS.md`, with `CLAUDE.md` as a Claude Code compatibility fallback | `:81` quote above | HOLDS |
| `rules.mdx:95-103` + loader `instruction.ts:122-130` at v1.19.4 (`:27`, both-files column) | "precedence is per name, first name with any hit wins" | `:103` quote above; `instruction.ts:122` "The first project-level match wins so we don't stack AGENTS.md/CLAUDE.md from every ancestor."; `:124` `for (const file of instructionFiles) {`, `:126` `findUp(file, ctx.directory, ctx.worktree)`, `:128-130` `if (matches.length > 0) { … break }` | HOLDS (the loop order + break is exactly name-order-first) |
| `rules.mdx:107-131` (`:27`, redirect column) | `instructions` array is additive | `:131` quote above | HOLDS |
| `rules.mdx:135-137` (`:27`, `:49`) | `@` references in a rule file are not parsed | `:137` quote above (page says `AGENTS.md`; entry generalises to "rule file" — low risk, same loaded text) | HOLDS |
| `rules.mdx:182` (`:27` redirect column, `:45` item 2) | symlinks are a redirect form the client documents / a `CLAUDE.md` symlink to `AGENTS.md` | `:182` quote above | BREAKS as "documents a redirect": the bullet is one item in "This approach allows you to:" and states a sharing mechanism, not loader behaviour (D2) |

Independent fetch of the loader: `https://raw.githubusercontent.com/anomalyco/opencode/v1.19.4/packages/opencode/src/session/instruction.ts`
→ 200, 8,581 B, sha256 `fee79c023eae44f720d4d600f334a987ad5f7615c4a008a20c89131a92684a8f` — the same size and digest the wave-1
seat recorded (`build/ScribeOpencode.md:27`). The cited lines exist in those bytes and say what is quoted.

## 3. Defects

**D1 — scope cell: "per-directory precedence" is not what the page says or the loader does. Low.**
Target: `corpus/SOURCES.md:58`, `scope` cell (fed by the knowledge entry's precedence line).
The page's precedence is per *name* within a category (`rules.mdx:99` "Local files by traversing up from the current
directory (`AGENTS.md`, `CLAUDE.md`)"; `:103` "The first matching file wins in each category"), not nearest-directory-first.
The installed loader walks names in array order and stops at the first name with any hit (`instruction.ts:124-130`), so a
`CLAUDE.md` beside the edited file loses to an `AGENTS.md` several directories up. The lane's own seat report says this in
words: `build/ScribeOpencode.md:79` "a `CLAUDE.md` beside the edited file loses to an `AGENTS.md` several directories up (the
search is per name, not per directory)". The knowledge entry is right ("precedence is per name"); only the registry `scope`
cell misleads, and it is the cell a later reader uses to decide what the source covers. Suggested fix (L1): replace
"per-directory precedence" with "per-name precedence and the project/global/Claude-Code category order".

**D2 — `rules.mdx:182` is over-read in both files. Low.**
Targets: `corpus/SOURCES.md:58` `teaches` cell ("documents an `instructions` config array, globs and symlinks as the
redirects") and `corpus/knowledge/alwayson-rule-files-round53.md:27` redirect column plus `:45` item 2 (S045 `:182` cited for
a `CLAUDE.md`-symlink redirect).
`rules.mdx:182` says "Share rules across projects via symlinks or git submodules" — a benefit bullet about sharing files, in
a list introduced by "This approach allows you to:". Nothing on the page says a symlink is followed when a rule file is
loaded, nor that a `CLAUDE.md` symlink to `AGENTS.md` is a redirect. The seat report itself draws the same line:
`build/ScribeOpencode.md:95` "A symlink: documented as a sharing mechanism, not as a precedence rule" and `:99` "Nothing in
either page documents a symlink as a *redirect the loader follows for a missing name*". The behavioural claim is not harmed —
the entry's Limits section records the measurement (`:74` "a `CLAUDE.md` symlink to `AGENTS.md` → `AGENTS.md` once") — but
the citation asserts documentation the page does not contain, and the C2 PASS case named "symlink-redirect"
(`verifiers/verify_alwayson.py:419`) inherits the framing. Suggested fix: in the row, say symlinks are documented for sharing,
not as a redirect; in the entry, keep `:182` for "symlinks named as a sharing mechanism" and let the measurement carry the
follow behaviour.

**G1 — gap: the deprecated third name `CONTEXT.md` is missing from the "names read" record. Low.**
Target: `corpus/knowledge/alwayson-rule-files-round53.md:27` names column.
The v1.19.4 loader's project array is `["AGENTS.md", "CLAUDE.md" (flag-gated), "CONTEXT.md" // deprecated]`
(`instruction.ts:64-68`), and the entry cites that same file (at `:122-130`) without the array. The row is not false — the
served page never mentions `CONTEXT.md` (regex `CONTEXT` over `rules.md` and `rules.mdx`: no hit, `grep` exit 1) — but the
entry presents the installed client as a two-name reader. The seat report already records it (`build/ScribeOpencode.md:53`,
and the S0xx row at `:143`). A reader of the entry could conclude a `CONTEXT.md`-only repository reads nothing. Suggested
fix: one clause in the names cell, sourced to `instruction.ts:64-68`, plus a note that the instrument does not check it
(the entry's item 4 already lists third names outside the check).

**G2 — observation, not a defect: the loader stacks same-name ancestors. Info.**
`systemPaths` adds every match returned by `findUp` for the winning name (`instruction.ts:129`), and `findUp` pushes every
existing ancestor file up to the worktree root (`packages/core/src/fs-util.ts:154-166`, fetched at v1.19.4, 10,690 B, sha256
`8deaf7c7b809425da81315019b79d9044592eead53a066e6263886a9c11bf860`). So several `AGENTS.md` files load together, while the
inline comment at `instruction.ts:122` ("so we don't stack") and the page's `rules.mdx:103` ("The first matching file wins in
each category") both read as one file. No kotoba sentence asserts the one-file reading, so this is a vendor divergence worth
a sentence in the entry, not a defect in the row.

## 4. What this receipt does not establish

- The original access at `2026-10-22T20:04:44Z` cannot be replayed; it is corroborated by the wave-1 seat's recorded digests
  (`build/ScribeOpencode.md:22-25`, identical sha256 values) and by today's byte-identical refetch.
- No vendor docs history walk: the "page has not moved" reading rests on three byte-identical pins (round-52 pin per the
  seat report, dev head now, tag v1.19.4), not on a commit history.
- The installed opencode 1.19.4 binary was not run here; the measured client behaviour is the seat's
  (`build/ScoutOpencodeBehaviour.md`) and the entry's Limits section, not this seat's.
- Other clients (S043, S044, S046–S051) and the C1/C2 counters were not touched.

## 5. Commands (exit codes as observed)

- `date -u` → `2026-10-22T20:39:07Z` (final receipt batch).
- `curl -sS -L -D … -w 'code=%{http_code} bytes=%{size_download} …' https://opencode.ai/docs/rules.md` → `code=200 bytes=6684 ctype=text/plain; charset=utf-8`, exit 0; `sha256sum` → `dfb242d9a8c0…`
- `curl … https://opencode.ai/docs/rules` → `code=200 bytes=76861 ctype=text/html`, exit 0; `sha256sum` → `05a6070925ba…`
- `curl … https://opencode.ai/docs/rules/` → `200 76861 text/html`, exit 0
- second batch at 20:37:59Z: both digests unchanged; `cmp rules.md rules.md.2` → exit 0 `md stable`; `cmp rules.html rules.html.2` → exit 0 `html stable`
- `curl … raw.githubusercontent.com/anomalyco/opencode/4a6dacec/packages/web/src/content/docs/rules.mdx` → 200, 6,758 B, `2d789f84…`, exit 0
- `curl … /v1.19.4/packages/web/src/content/docs/rules.mdx` → 200, 6,758 B, same sha, exit 0
- `curl … /v1.19.4/packages/opencode/src/session/instruction.ts` → 200, 8,581 B, `fee79c02…`, exit 0
- `curl … /v1.19.4/packages/core/src/fs-util.ts` → 200, 10,690 B, `8deaf7c7…`, exit 0
- `curl … /dev/…/rules.mdx` and `/master/…/rules.mdx` → 200, 6,758 B, `2d789f84…` each, exit 0; `/main/…` → 404
- `git ls-remote --tags https://github.com/anomalyco/opencode.git refs/tags/v1.19.4 refs/tags/v1.19.3` → `148842ef…` and `e3c4eb24…`, exit 0; `git ls-remote --symref … HEAD` → `ref: refs/heads/dev`, `cd1861d9…`, exit 0
- comparison: `diff -u <(mdx lines 6-188) rules.md` → exit 1, sole hunk is `\ No newline at end of file`; python3 check → `equal ignoring one trailing newline: True`, `len diff 1`
- HTML text check after `html.unescape`: "used if no" ×2, "Claude Code Compatibility" heading present, the `’`-apostrophe
  rendering of `:79` present; symbols `grep` for the ASCII apostrophe form returns 0 only because of entity escaping
- lane reads: `grep -n "S045" corpus/SOURCES.md corpus/knowledge/alwayson-rule-files-round53.md corpus/lessons/round-53.md` (read-only);
  the lesson's Gate quote (`corpus/lessons/round-53.md:25`) is the `rules.mdx:103` sentence verbatim and its byte/digest cells agree

Hygiene: no installs, no pacman, no model call, no `ask`, no headless browser, no lane Git or jj write, no subagent, no push.
Writes: this report plus scratch under `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS045/`. Tool version: `curl` and
`git ls-remote`/`diff`/`sha256sum` as shipped on the host; no tool was installed or upgraded for this seat.
