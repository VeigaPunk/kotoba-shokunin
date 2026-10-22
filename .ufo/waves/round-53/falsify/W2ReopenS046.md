Result: MIXED — the S046 anchor re-opens byte-identical (200, 3,807 B, sha256 `d00eeaef…`) and its three cited doc sections say what the row cites them for, but the row's teaches clause "a string or list in `context.fileName` replaces the name" is contradicted by the pinned client code, which appends the configured names to `GEMINI.md` so the default keeps loading, and the knowledge entry cites `memoryDiscovery.ts:430` (a path sort) for the both-load behaviour.

# W2ReopenS046 — re-open of SOURCES row S046 (Gemini CLI GEMINI.md docs, pinned commit)

Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc` (branch `master`). Read-only in the lane; I made no join to the C1 or C2 counters; this seat attacks only the source row and the knowledge entry that rests on it.

## 0. Judged cells, and a working-tree caveat

`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `c775d6823bfca8f0de8c0874032a954438b38edc` (exit 0). The working tree carries post-floors edits by other seats (`git diff --stat HEAD -- corpus/SOURCES.md corpus/knowledge/alwayson-rule-files-round53.md` → 3 and 23 changed lines: S052 added, other clients' cells revised). None of those edits touches my target cells, confirmed by hashing the judged blob against the working copy:

| cell | at `c775d68` | working copy | equal |
|---|---|---|---|
| `corpus/SOURCES.md:59` (S046 row) | `c704a3ff6582f30137a23c870ab0965c4b30d5abad7ea56c94f3c8aad3cf4f25` | same | yes |
| `corpus/knowledge/alwayson-rule-files-round53.md:28` (Gemini CLI row) | `ca9939a8684c4daa73db4d02f43c648929514d4ea5137ecfd994faeedcae4d52` | same | yes |

So every quote below is the judged text. The round-53 lesson (`corpus/lessons/round-53.md`) is **not** in `c775d68` (`git show c775d68:corpus/lessons/round-53.md` → `fatal: path … exists on disk, but not in …`); its Gate row for S046 is a working-tree artifact and is treated as informational only (O3).

## 1. Re-open receipt and anchor-cell comparison

Opened by ordinary `curl` (no browser, no challenge bypass). Two independent fetches, plus a fresh fetch of the branch tip for the same path.

| fetch | UTC | status | bytes | sha256 | content-type |
|---|---|---|---|---|---|
| A: the row's URL | 2026-10-22T20:36:37Z | 200 | 3,807 | `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf` | not captured |
| B: the row's URL, re-fetch (`-D` headers) | 2026-10-22T20:40:26Z | 200 | 3,807 | same full digest | `text/plain; charset=utf-8`, `cache-control: max-age=300`, server `date: Thu, 22 Oct 2026 20:40:26 GMT` |
| C: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md` | 2026-10-22T20:40:26Z | 200 | 3,807 | same full digest (`diff -q` → no output, exit 0) | — |

URL fetched: `https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/docs/cli/gemini-md.md` (no redirect; the `-w` output was `HTTP 200 bytes 3807`).

| row element (`corpus/SOURCES.md:59`) | row value | observed 2026-10-22 | verdict |
|---|---|---|---|
| fetch receipt | `fetched 2026-10-22T20:10:20Z (200, 3,807 B, sha256 d00eeaef…)` | two fetches today: 200, 3,807 B, `d00eeaef22453de4…` | exact match |
| file length | implied 3,807 B | `wc -c` → 3807; `wc -l` → 116 | match |
| committed pin | `451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1` in the URL | `curl …/commit/<sha>.patch` → HTTP 200, 38,174 B; header `From 451a02ff…`, `Date: Thu, 22 Oct 2026 19:07:09 +0000` | commit exists in the vendor repo; date matches the wave-1 seat's recorded commit time |
| freshness of the rule | row is pinned, recheck 2027-01-20 | `main`'s copy of the same path is byte-identical today | the pinned text is current main text, not stale-but-pinned |
| status field | `mined`; used-by `corpus/knowledge/alwayson-rule-files-round53.md` | `git cat-file -e c775d68:corpus/knowledge/alwayson-rule-files-round53.md` → exit 0 | used-by exists at the judged revision |
| registry validity | tier `A`, kind `docs`, id unique | `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0; only pre-existing W04 warnings for S018/S019/S021, no E-code for S046 | valid row |
| recheck cadence | opened 2026-10-22, recheck 2027-01-20 | 90 days | matches the lane's 90d cadence |

Local bytes kept at `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS046/` (`gemini-md.md`, `pin_recheck.md`, `main_gemini_md.md`, and the corroborating files below).

## 2. Per-line verification

Quotes are verbatim, ≤25 words; line numbers are lines of the fetched 3,807-byte file.

### 2.1 SOURCES row S046 locators and taught clauses

| locator / clause | what the row claims it supports | verbatim evidence | verdict |
|---|---|---|---|
| `gemini-md.md:13-36` (§ Understand the context hierarchy) | context files are loaded hierarchically; the default name is `GEMINI.md` | `:13-15` "It loads various context files from several locations, concatenates the contents of all found files, and sends them to the model with every prompt."; the file name appears at `:20` "`~/.gemini/GEMINI.md`" and `:25` "The CLI searches for `GEMINI.md` files in your configured" | HOLDS for what the row cites the section for |
| `gemini-md.md:71-92` (§ Modularize context with imports) | an `@file.md` import pulls content in | `:73-75` "You can break down large `GEMINI.md` files into smaller, more manageable components by importing content from other files using the `@file.md` syntax." | HOLDS; "pulls another file's bytes in" is a paraphrase — the page says "importing content", it does not say "bytes" |
| `gemini-md.md:94-106` (§ Customize the context file name) | the default name, the name-or-list setting, the example | `:96-97` "While `GEMINI.md` is the default filename, you can configure this in your `settings.json` file."; `:97-98` "To specify a different name or a list of names, use the `context.fileName` property."; `:105` `"fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` | HOLDS for default / name-or-list / example. The word "replaces" is the row's own — see D1 |
| teaches: "Context files default to `GEMINI.md`" | default name | `:3` "Context files, which use the default name `GEMINI.md`, are a powerful feature"; code `DEFAULT_CONTEXT_FILENAME = 'GEMINI.md'` (`packages/core/src/tools/memoryTool.ts:11`) | HOLDS |
| teaches: "a string or list in `context.fileName` replaces the name" | setting semantics | the page says "a different name or a list of names", never that the default stops being read; the pinned loader appends (D1) | BREAKS |
| teaches: "an `@file.md` import pulls another file's bytes in" | import semantics | `:73-75` above; `docs/reference/memport.md` at the same pin (6,382 B, `eb2737b4…`) documents the import processor | HOLDS as a paraphrase |

The row's citation ranges are slightly loose but no claim depends on a clipped line: `:13-36` omits the heading at `:11` and the section's last two lines (the footer cue at `:37-38`), and the word "default" for the file name is stated at `:3` and `:96` rather than inside `:13-36` — but `:96` is inside the row's third locator, so the taught default is anchored; `:94-106` stops before the example's outer `}` and closing fence (`:107-108`). See O1.

### 2.2 `corpus/knowledge/alwayson-rule-files-round53.md` locators for S046

| locator | what the entry claims | verbatim evidence | verdict |
|---|---|---|---|
| `:1` source header — S046 `:71-106` | imports and file-name span | both sections above are inside `:71-106`; the default-name sentence is at `:96`, also inside | HOLDS |
| `:28` names column — `gemini-md.md:94-106` | `GEMINI.md` by default; the setting takes a name or a list; the example | `:96-98`, `:105` above | HOLDS |
| `:28` both-files column — `memoryDiscovery.ts:430` | "only configured names are read; when both are configured, both load" | `packages/core/src/utils/memoryDiscovery.ts:430` is `return unique.sort();` — a path sort; the claimed behaviour is at `:470` "const geminiMdFilenames = getAllGeminiMdFilenames();" and `:485-500`, where every configured name is probed (`:486` `geminiMdFilenames.map(async (filename) => {`, `:496-498` filter non-null, `:500` `upwardPaths.unshift(...foundPathsInDir);`) | BREAKS as to the pointer (D2); the claim itself is true |
| `:28` both-files column — wording "only configured names are read" | which names are read | true of the probed list, but the list always retains `GEMINI.md` after any `context.fileName` value (D1/D3), so it is incomplete for a repo that ships `GEMINI.md` | HOLDS narrowly / incomplete (D3) |
| `:28` redirect column — `gemini-md.md:71-92` | `@file.md` imports | `:73-75` above | HOLDS |
| `:28` redirect column — "a symlink redirect is not documented" | negative on symlinks | `grep -n -i "symlink\|symbolic\|link" gemini-md.md` → no output, exit 1; same grep over `memport.md` and `configuration.md` at the pin → no output, exit 1; the client-wide sweep (changelog arm, docs-tree arm, lane-corpus arm) is in `.ufo/waves/round-53/build/ScribeGemini.md` § 3 | HOLDS as a page-scoped negative; the client-wide sweep exists in the seat report but is not named in the cell, and its lane-corpus arm grepped `GEMINI.md` terms, not "symlink" (O2) |
| `:60` — `memory-management.md:117-118` | Gemini CLI's only stale-content advice | at the pin: 200, 4,541 B, `3d745a89d9f455a458af2561002612270628ce6acb4af8364b4d1f614d32ff9c`; `:117-118` "Periodically check your `GEMINI.md` files to remove outdated" / "rules." | HOLDS the quote; no SOURCES row exists for this file (D4) |
| `:53` — "(S046, S047, S048, S050)" for "`GEMINI.md` … a further name" | GEMINI.md is a name a repository may need to cover | `:3`, `:96` | HOLDS |

## 3. Defects

### D1 — the row's "replaces the name" is contradicted by the pinned loader (Medium)

`corpus/SOURCES.md:59` teaches "a string or list in `context.fileName` replaces the name". The page does not say that: `gemini-md.md:96-98` says "To specify a different name or a list of names, use the `context.fileName` property", and its own example (`:105`) lists `GEMINI.md` alongside the other two names. At the same pinned commit the loader **appends** the configured names to the current list, which starts as the default:

- `packages/core/src/tools/memoryTool.ts:11` `export const DEFAULT_CONTEXT_FILENAME = 'GEMINI.md';`
- `:14-16` the module starts with that single name: "It defaults to DEFAULT_CONTEXT_FILENAME but can be extended by setGeminiMdFilename."
- `:18-19` the setter's own docstring: "Adds one or more filenames to the current context filenames."
- `:22-49` `setGeminiMdFilename` builds `next` from the new names, then `:39-41` adds every current name back: "for (const filename of current) { next.add(filename); }".
- `memoryTool.test.ts:21-27` pins the behaviour: the test is named "appends to currentGeminiMdFilename when a valid new name is provided" and expects `[newName, DEFAULT_CONTEXT_FILENAME]`.
- `packages/cli/src/config/config.ts:623-624` calls that setter when the setting is present (`if (settings.context?.fileName) { setServerGeminiMdFilename(settings.context.fileName);`); the replacing helper `resetGeminiMdFilename` is only called in the else branch, `:627`, when no `context.fileName` is set. `packages/core/src/config/config.ts:1416-1417` also calls the additive setter.

Consequence: with `context.fileName: ["AGENTS.md"]`, the probed name list is `["AGENTS.md", "GEMINI.md"]`, so a repository's `GEMINI.md` still loads (project discovery enumerates the whole list: `memoryDiscovery.ts:470`, `:485-500`; the global directory does the same at `:317-339`). The only place the first name wins is `getGlobalMemoryFilePath()` (`memoryTool.ts:76-81`, `:90-92`), which returns the first entry of the list. So "replaces" is at best half true (the global write/read-back path) and false for the project-level discovery the always-on checklist is about. The row converts the page's "a different name" into a behavioural claim the pinned client does not implement.

Fix: put the page's words in the teaches cell ("a different name or a list of names") and carry the append fact as a separate, code-cited clause (`memoryTool.ts:22-49`; test `memoryTool.test.ts:21-27`), or keep the row documentation-only and move the behaviour into the entry's Gemini cell.

### D2 — the entry's `memoryDiscovery.ts:430` pointer names a sort, not the both-load check (Low)

`corpus/knowledge/alwayson-rule-files-round53.md:28` cites `memoryDiscovery.ts:430` for "only configured names are read; when both are configured, both load". Line 430 of the pinned file (sha256 `f7c1123381d9326a7ce04ce54f3e0980140e791ba2fe5c2f22602a8f67ef23a5`, 21,318 B — the same bytes the wave-1 seat recorded) is `return unique.sort();` inside `getEnvironmentMemoryPaths`. The cited claim's support is at `:470` (the configured-name list) and `:485-500` (every configured name probed and kept). The claim is true; the pointer is wrong by 55 lines and a function. Fix: cite `memoryDiscovery.ts:470, 485-500` (the wave-1 seat's own § 2.2 does).

### D3 — the entry's Gemini "both files" cell omits that the default name is never dropped (Low–Medium)

Because of D1, "only configured names are read" is true of the probed list but the list always includes `GEMINI.md` once `context.fileName` is set. For the box's purpose (which rule set a repository's clients read), a repository that ships `GEMINI.md` keeps that file in play even when a user configures `AGENTS.md`; only `resetGeminiMdFilename` (no setting path) removes it. The entry's § What follows item 4 ("`GEMINI.md` … a further name a repository may need to cover") is directionally right but understates it: at this pin, `GEMINI.md` is read by default and also by every configured list. Fix: add the append fact to the cell with the code cites from D1.

### D4 — `memory-management.md:117-118` is cited with no SOURCES row (Low)

The entry (line 60) cites the Gemini CLI tutorial for the stale-content advice and the quote/line verify at the pin (200, 4,541 B, `3d745a89…`). But the file has no row in `corpus/SOURCES.md` (`grep -n "memory-management" corpus/SOURCES.md` → no output), and the entry's own `source:` header lists only S043–S051 plus S004/S019, so a cited source is outside the registry the entry claims. The plan's Frontier step says "SOURCES: rows for every always-on source opened this round", and the wave-1 seat drafted a row for this file. Fix: add the row (or fold the citation into a rowed source with the located line).

## 4. Observations (not defects against `c775d68`)

- **O1 (cosmetic):** the row's ranges clip the section headings/last lines (`:13-36` vs section `:11-38`; `:94-106` vs section `:94-108`). No taught clause depends on a clipped line, and `:105` (the example's `fileName` line) is inside `:94-106`.
- **O2 (sweep naming):** the Gemini symlink negative is page-scoped and true, but the cell does not name its Q30 sweep (unlike the Codex cell's "0 hits over 191 pages, `ScribeCodex.md` § 4"). The swept seat report has all three arms; its lane-corpus arm grepped `GEMINI.md`/`context.fileName` terms, not the negative's term. I ran the missing term in the lane: `grep -rn -i "symlink" corpus | grep -i "gemini"` → only the entry's own line 28, i.e. nothing contradicts the negative.
- **O3 (working tree, outside the judged revision):** the lesson Gate row for S046 (`corpus/lessons/round-53.md:21-26`, working tree only) gives the URL as "google-gemini/gemini-cli `docs/cli/gemini-md.md` at `451a02ff` (raw)" — a locator, not a URL — and its table has no status column. The SOURCES row carries the full URL and 200, so access evidence is complete in the registry.

## 5. What I did not check

- I did not run the Gemini CLI (no installed binary; model calls are out of bounds). The append behaviour is read from the pinned source and its committed unit test, not from a live client run.
- I did not clone the whole gemini-cli docs tree; the client-wide symlink negative rests on the wave-1 seat's three-arm sweep, corroborated by my zero-hit greps of `gemini-md.md`, `memport.md` and `configuration.md` at the pin.
- I did not re-verify rows S043–S052 or any C1/C2 counter; those are other seats' items.
- The `main` fetch proving the pin is current is one point in time (2026-10-22T20:40Z); `main` can move after this report.

## 6. Commands and exits actually run

- `date -u +%Y-%m-%dT%H:%M:%SZ` → `2026-10-22T20:36:37Z`, `2026-10-22T20:40:26Z`.
- `curl -sS -o gemini-md.md -w 'HTTP %{http_code} bytes %{size_download} …' https://raw.githubusercontent.com/…/451a02ff…/docs/cli/gemini-md.md` → `HTTP 200 bytes 3807`, exit 0; `sha256sum` → `d00eeaef22453de4…`; `wc -c` → `3807`, `wc -l` → `116`.
- Second fetch with `-D` → `HTTP 200 bytes 3807`, exit 0, same sha; headers `content-type: text/plain; charset=utf-8`, `cache-control: max-age=300`, `date: Thu, 22 Oct 2026 20:40:26 GMT`.
- `curl …/google-gemini/gemini-cli/main/docs/cli/gemini-md.md` → `MAIN HTTP 200 bytes 3807`; `diff -q gemini-md.md main_gemini_md.md` → no output, `diff_exit=0`.
- `curl -sS -o commit.patch -w 'HTTP %{http_code} bytes %{size_download}' https://github.com/google-gemini/gemini-cli/commit/451a02ff….patch` → `HTTP 200 bytes 38174`; head shows `From 451a02ff…` and `Date: Thu, 22 Oct 2026 19:07:09 +0000`. (The GitHub API commit endpoint answered 403, rate limit; the patch route was used instead.)
- Fetches at the same pin with digests matching the wave-1 seat: `memoryDiscovery.ts` 21,318 B `f7c11233…`; `memoryTool.ts` 2,922 B `af2a33a1…`; `memoryTool.test.ts` 2,410 B; `packages/cli/src/config/config.ts` 40,094 B; `packages/core/src/config/config.ts` 135,234 B `db2fbf52…`; `configuration.md` 102,685 B `4b86e73e…`; `memport.md` 6,382 B `eb2737b4…`; `memory-management.md` 4,541 B `3d745a89…`.
- `grep -n -i "symlink\|symbolic\|link" gemini-md.md` → no output, exit 1; same over `memport.md` and `configuration.md` → exit 1.
- In the lane (read-only): `git rev-parse HEAD` → `c775d682…`; `git show c775d68:corpus/SOURCES.md | sed -n '59p' | sha256sum` = `sed -n '59p' corpus/SOURCES.md | sha256sum` = `c704a3ff…`; the Gemini-row equivalent = `ca9939a8…`; `git cat-file -e c775d68:corpus/knowledge/alwayson-rule-files-round53.md` → exit 0; `git show c775d68:corpus/lessons/round-53.md` → fatal (not in that commit).
- `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0; output `kotoba W04 S018…`, `W04 S019…`, `W04 S021…` (pre-existing), `kotoba ok`.
- No install or upgrade was needed; nothing was installed or changed on the host. No git or jj write was made in the lane; no counter was run.

## 7. Bounds note

Scratch work was first written to `/tmp/s046probe/` (a deviation from the seat-scratch rule) and then copied to the assigned directory `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS046/`, which now holds every fetched byte and the patch file. No lane file was written except this report; no Git index, jj state, fleet file or sibling lane was touched.
