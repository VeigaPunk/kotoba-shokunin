# W2ReopenS051 — re-open SOURCES row S051 (opencode v1.19.3…v1.19.4 tag delta)

Result: MIXED — every substantive claim in S051 reproduces on a fresh fetch today (48 entries, sha256
`a6a680ae…`, 1238 lines, no `packages/opencode/src/` path, all four cited line numbers, both tag shas and
dates, both loader-file hash prefixes, and every bundle hit count), but one number in the anchor cell is off
by one, one hit-count label omits the quote character its own number depends on, and the release-note anchor
is a line number in a rolling feed that already carries 15-line shifts per release.

Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc`. Row bytes at that revision hash
`835c6c12b10712dfb8b9dd541204c0ce9d63441944fe252f11e6f5a56940ef71` and are identical in the lane working
tree (same sha256; `git show c775d68:corpus/SOURCES.md | sed -n 64p`). The row landed in
`55973a20ac728f7b11ac8de518620ba128c13afa` and is unchanged through `c775d68`; it is absent at `aeed0890`
and earlier. Sandbox clone: `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS051/{lane,oc}`.

## 1. Fetch receipts (all ordinary curl, no browser, no challenge bypass)

| artifact | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| compare diff | `https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff` | 2026-10-22T20:36:44Z→20:36:45Z | 200 | 66,868 | `a6a680aec87f4b274dae4d088115f15503275d52846a35827aee1faf91130863` |
| compare diff (re-fetch) | same | 2026-10-22T20:42:22Z | 200 | 66,868 | `a6a680ae…630863`, `cmp -s` byte-identical |
| release atom | `https://github.com/anomalyco/opencode/releases.atom` | 2026-10-22T20:36:53Z→20:36:54Z | 200 | 6,758 | `5d050363ba74e9b441a41de9c81ec34b39a9df91952e1e40d720052ff3a6fe1a` |
| release tag page | `…/releases/tag/v1.19.4` | 2026-10-22T20:41:45Z | 200 | 194,684 | not hashed |
| sst redirect | `https://github.com/sst/opencode/compare/v1.19.3...v1.19.4.diff` | 2026-10-22T20:41:44Z | 301 → `https://github.com/anomalyco/opencode/…` | 0 | — |
| root `package.json` @v1.19.3 | raw.githubusercontent…/v1.19.3/package.json | 2026-10-22T20:37:0xZ (batch start 20:37:14Z) | 200 | 6,052 | `564e182ea9f962fe4ac148b2c93f6679b38cecd62d81abf6b51f5a2a88e03262` |
| root `package.json` @v1.19.4 | …/v1.19.4/package.json | same batch; re-fetched 2026-10-22T20:43:42Z, 200, 6,076 B, sha256 `889a89bf…f7288`, `cmp -s` identical | 200 | 6,076 | `889a89bf4b914323e7af206a854bd400d30395f04c377afbbfd65042f15f7288` |
| `packages/opencode/package.json` @v1.19.3 | raw… | same batch | 200 | 5,268 | `f26b884353a34f771ed960e4042363f7843d0fb0a822feca84adce37d18aab22` |
| `packages/opencode/package.json` @v1.19.4 | raw… | same batch | 200 | 5,269 | `9825647d55cdbc693e2965048e448b21540a1d290023b31a3af8b1d5da0fede5` |
| `packages/opencode/script/build.ts` @v1.19.3 | raw… | same batch | 200 | 7,289 | `37362ba0ff8f0d82a917970a648fc79a4d35264a2fa405ca126e918a967563f9` |
| `packages/opencode/script/build.ts` @v1.19.4 | raw… | same batch | 200 | 7,422 | `a9936f1f84bbcb0f084c50d18a9025708508a4c07da598aa96925b47aa030d5e` |
| npm `opencode-ai` metadata | `https://registry.npmjs.org/opencode-ai` | 2026-10-22T20:37:40Z | 200 | 25,052,130 | not hashed |
| npm `opencode-linux-x64` metadata | `https://registry.npmjs.org/opencode-linux-x64` | 2026-10-22T20:38:03Z | 200 | 17,962,684 | not hashed |
| npm 1.19.3 platform tarball | `…/opencode-linux-x64/-/opencode-linux-x64-1.19.3.tgz` | 2026-10-22T20:38:15Z | 200 | 60,356,012 | `71d67513eb4078a7ff8eb96806b1d5edcd6533a72b311409b2e88bad4188dac6` |
| npm 1.19.4 platform tarball | `…/opencode-linux-x64-1.19.4.tgz` | 2026-10-22T20:38:35Z | 200 | 79,146,075 | `dca7b06bbb4e4a1ab3681b799cd328057b356d9399e8e47336cf53b7ae658d0d` |

Extracted binaries and dumps (mine, built here, not borrowed):

- `pkg193/package/bin/opencode` sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` (186,013,824 B) — equals the 1.19.3 bytes pinned by S015 `179ca421…`.
- `pkg194/package/bin/opencode` sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7` (214,522,032 B) — equals `verifiers/baseline.json` `measured_against.opencode_binary_sha256` and the plan's C1 host sha. So the npm tarballs ARE the two artifacts the re-pin measures.
- `strings -n 4` dumps (GNU binutils 2.47): `mine-1.19.3.strings` 67,839,091 B sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`, `mine-1.19.4.strings` 74,137,746 B sha256 `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`. Both are byte-identical to the dumps the wave-1 seats used (`/fast/scratch/hyaku/kotoba-r53/ScoutOcRelease/oc-1.19.{3,4}.strings`), so the counts below are reproduced on independently rebuilt files.

No installs or upgrades were made; nothing to record under the tooling directive.

## 2. Per-cell verdicts

### 2a. Source cell (URL + name) — HOLDS
- `https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff` → 200, 66,868 B, sha256 `a6a680ae…`; a second fetch at 20:42:22Z is byte-identical (`cmp -s`, exit 0). Determinism holds.
- "sst/opencode answers 301 to anomalyco/opencode": `curl -D` shows `HTTP 301` with `location: https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff`. Holds.

### 2b. Anchor cell — BREAKS on one number, HOLDS on the rest
| anchor element | verdict | evidence |
|---|---|---|
| `compare.diff:1-1238` | HOLDS | `wc -l -c cmp.diff` → 1238 66868; last byte is `0a` (file ends at line 1238) |
| 48 entries | HOLDS | `grep -c '^diff --git '` → 48; and `git diff --name-only v1.19.3 v1.19.4` in a blobless clone of both tags → 48 paths, `comm -3` between the compare path list and the tag-tree path list → empty (sets identical) |
| sha256 `a6a680ae…` | HOLDS | full sha above, twice |
| no path under `packages/opencode/src/` | HOLDS | `grep -c 'packages/opencode/src/' cmp.diff` → 0; `grep -c '^packages/opencode/src/' treedelta.txt` → 0. (Only `src/` path in the whole delta is `packages/session-ui/src/components/timeline-playground.stories.tsx`; the cell's narrow wording is therefore correct, a broader "no src path" claim would not be) |
| `packages/opencode/script/build.ts:141` Bun 1.4.4 comment | HOLDS | `git show v1.19.4:packages/opencode/script/build.ts \| sed -n 141p` → `// Bun 1.4.4 skips native packages for the other libc by default, but the musl targets need them.`; the compare hunk adds exactly that line |
| `packages/opencode/package.json:81` `@ff-labs/fff-bun` 0.9.4→0.10.5 | HOLDS | line 81 = `"@ff-labs/fff-bun": "0.10.5"` at v1.19.4 and `"0.9.4"` at v1.19.3; compare hunks at cmp.diff:870-871 and :976-977 |
| root `package.json:7` bun@1.3.14→bun@1.4.4 | HOLDS | line 7 = `"packageManager": "bun@1.4.4"` (v1.19.4) vs `"bun@1.3.14"` (v1.19.3) |
| release note `releases.atom:27` | HOLDS today, volatile (see D3) | atom line 27 = `<li>Upgraded the bundled Bun runtime to 1.4.4, which includes … security fixes … HTTP/2, HTTP/3, WebSocket, and <code>fetch</code>, and updates root certificates to NSS 3.131.1.</li>` |
| tags v1.19.3 `e3c4eb24…` 2026-10-16T12:31:36Z, v1.19.4 `148842ef…` 2026-10-22T13:03:27Z | HOLDS | `git ls-remote --tags` → `e3c4eb242585dcd77be1a867391b7c25fd47ce52 refs/tags/v1.19.3`, `148842ef7cb1bc34192b3fff57d0f9721ab9c801 refs/tags/v1.19.4` (lightweight refs, no `^{}` line); `git log -1 --format=%cI` → `2026-10-16T12:31:36Z` and `2026-10-22T13:03:27Z`, exact |
| "the compare view is merge-base based" | HOLDS | `git merge-base v1.19.3 v1.19.4` → `60c9be092129745688bb3c3a752affc6cbd66ede` (2026-10-16T11:37:51Z, "chore: generate"); `merge-base --is-ancestor v1.19.3 v1.19.4` → NO |
| "(28 manifest hunks read 1.19.2 before)" | **BREAKS** | the compare diff removes `-  "version": "1.19.2"` 29 times, in 29 distinct manifests and 29 distinct hunks (28 under `packages/`, plus `sdks/vscode/package.json`); the tag trees read `"version": "1.19.3"` → `"1.19.4"` for the same file (`git show v1.19.3:packages/console/app/package.json` line 3 = `"1.19.3"`) |

### 2c. Teaches cell — HOLDS on substance, two wording defects
| element | verdict | evidence |
|---|---|---|
| `session/instruction.ts` `fee79c02…` identical at both tags | HOLDS | raw fetch 200 / 8,581 B at both tags, sha256 `fee79c023eae44f720d4d600f334a987ad5f7615c4a008a20c89131a92684a8f` both; git blob `7f593550…` both |
| `tool/read.ts` `afec8294…` | HOLDS | 13,126 B, sha256 `afec8294965cbd9b9e29d3453b682164f0ecdba26574ebc048e9ba21af209c68` both; blob `678ed445…` both |
| `core/src/instruction-context.ts` `fde78e0e…` | HOLDS | 3,611 B, sha256 `fde78e0e5b5457d7290b832a435f29b033f770e0cae981f3d1eac22672a57e57` both; blob `492fa420…` both |
| `system-context/builtins.ts` `a5907c81…` | HOLDS (hash), path base ambiguous (D4) | real path `packages/core/src/system-context/builtins.ts`; sha256 `a5907c811772e7e93aab23884593f2e93348cca3c1cb8c3b41b0268c0a8d275e` both; blob `b8b50577…` both. `packages/opencode/src/system-context/builtins.ts` is 404 at both tags |
| "no instruction-loading source moved" | HOLDS | all four loaders are outside the 48-path delta entirely; the only `packages/core/` path in it is `packages/core/package.json` |
| "the release note names only a Bun 1.4.4 runtime upgrade" | HOLDS | the v1.19.4 atom entry (lines 19-33) has exactly one change item: `<h2>Core</h2><h3>Improvements</h3>` and one `<li>` naming Bun 1.4.4 plus the security-fix and NSS-cert consequences of that upgrade |
| `fn(` 120→2 | **BREAKS as written**, holds for `fn("` (D1) | line counts on my dumps: `grep -c 'fn('` → 192→103; `grep -c 'fn("'` → 120→2; occurrences `grep -o 'fn('` → 1179→180 |
| `Key.make(` 12→6 | HOLDS as a distinct-string count; not as an occurrence count (D1) | `grep -c 'Key.make('` → 12→6; `grep -oF 'Key.make(' \| wc -l` → 18→10 |
| `("Instruction.resolve")` one hit each | HOLDS | lines 1→1, occurrences 1→1 |
| `make("core/instructions")` one hit each | HOLDS | lines 1→1, occurrences 1→1 |
| "renamed helpers are rebuild churn, not a loader change" | HOLDS | the anchor-row table reproduces exactly on my dumps (`fn("Instruction.resolve")` 1→0, `l("Instruction.resolve")` 0→1, `fn("ReadTool.execute")` 1→0, `l("ReadTool.execute")` 0→1, `Key.make("core/instructions")` 1→0, `Wr.make("core/instructions")` 0→1, `l("` 413→493, `<system-reminder>` 15→13), and the source files themselves are byte-identical |

### 2d. Registry cells — HOLDS
- `status` = `mined`, `opened` = 2026-10-22, `recheck` = `on-release`: consistent with a tag published 2026-10-22T13:03:27Z and mined today. Nothing falsifiable beyond that; the row did not exist at `e78dff66`, `3bb0a7a3`, `5e5336c4`, `aeed0890`, and appeared at `55973a20`.
- `used-by` = `corpus/knowledge/instruction-surface-census-round13.md`: the note cites S051 at line 572 and repeats the two-to-three-point provenance (no `packages/opencode/src/` path, release note = Bun runtime only 1.3.14→1.4.4, renamed wrappers = rebuild of unchanged source). Holds.
- Registry parses: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok`, with only the pre-existing W04 duplicate-url warnings (S018, S019, S021; no S051 diagnostic).

## 3. Defects and severity

- **D1 (LOW) — hit-count label and unstated metric, teaches cell.** The cell writes `` `fn(` 120→2 hits ``. Under the literal pattern `fn(` the dump gives 192→103 distinct strings or 1179→180 occurrences; the 120→2 pair is the `fn("` count (the build report's own table labels it `fn("`). The neighbouring `Key.make(` 12→6 pair only reproduces as *distinct strings* (occurrences are 18→10), and the row never states that it counts distinct strings. A reader reproducing the cell literally gets a different number. Fix: write `` `fn("` 120→2 (distinct strings, `strings -n 4`) ``.
- **D2 (LOW) — off-by-one in the anchor cell.** "28 manifest hunks read 1.19.2 before": measured 29 (28 under `packages/`, plus `sdks/vscode/package.json`). The caveat's substance is right and in fact stronger than stated (v1.19.3 is not an ancestor of v1.19.4; the merge base is `60c9be09`, 2026-10-16T11:37:51Z). Fix: 29, or "28 under `packages/`".
- **D3 (MEDIUM, freshness-specific) — the release-note anchor is a line number in a rolling feed, and it is the only anchor in the row with no URL and no fetch receipt.** Today line 27 is exact. But the feed's newest entry is already `v2.1.3` (2026-10-22T12:45:27Z, atom lines 8-18) above the `v1.19.4` entry (lines 19-33), i.e. the feed interleaves two release series and pushes every entry down by ~15 lines per new release; and the `v1.19.4` entry's own `<updated>` (13:03:41Z) is *later* than `v2.1.3`'s (12:45:27Z) yet sits below it, so feed position is not even the `<updated>` order. [INFERENCE] the first v2.1.4/v1.19.5/… release moves the cited line, silently making `releases.atom:27` point at unrelated text. Unlike S046-S050, the row carries no `fetched <UTC> (200, N B, sha256 …)` receipt for the atom, and the atom's own URL exists only inside the anchor text. Fix: cite `https://github.com/anomalyco/opencode/releases/tag/v1.19.4` (200 confirmed) or the entry `<id>`, and add the receipt: 2026-10-22T20:36:53Z, 200, 6,758 B, sha256 `5d050363…`.
- **D4 (LOW) — three path bases in one clause, teaches cell.** `session/instruction.ts` and `tool/read.ts` are relative to `packages/opencode/src/`; `core/src/instruction-context.ts` is relative to `packages/`; `system-context/builtins.ts` is relative to `packages/core/src/`. Resolving the last under the first base is a 404. Fix: print the four paths in full, or state the bases.
- **D5 (INFO) — no instrument pins this row.** `grep -rn "S051\|compare.diff\|releases.atom" verifiers/` → no hits; `sources-census.sh validate` checks format and duplicate URLs only. The row's numbers are prose checked by a seat, not a counter, so D1-D2 have no automatic backstop.
- **D6 (INFO) — used-by retarget.** The wave-1 draft (`ScoutOcRelease.md:216`) carried `used-by = .ufo/waves/round-53/build/ScoutOcRelease.md, plans/round-53.md § C1`; the landed row replaced it with the census note. Chain of custody survives because the census note itself cites `ScoutOcRelease.md`, but the row no longer points at the report holding the measurement table.

No severity above MEDIUM; nothing here weakens C1's own statement, which the plan already bounds to the counter's printed line.

## 4. Reproduction (sandbox, all commands run there)

```
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin lane && git -C lane checkout -q c775d68…   # exit 0
curl -sSL -o cmp.diff 'https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff'          # 200, 66868 B
sha256sum cmp.diff                     # a6a680aec87f4b274dae4d088115f15503275d52846a35827aee1faf91130863
wc -l cmp.diff ; grep -c '^diff --git ' cmp.diff ; grep -c 'packages/opencode/src/' cmp.diff          # 1238 ; 48 ; 0 (exit 1)
git clone --filter=blob:none --no-checkout --depth 1 --branch v1.19.4 https://github.com/anomalyco/opencode oc
git -C oc fetch --depth 1 origin refs/tags/v1.19.3:refs/tags/v1.19.3
git -C oc diff --name-only v1.19.3 v1.19.4 | wc -l                                                   # 48
git -C oc merge-base v1.19.3 v1.19.4                                                                 # 60c9be09…
curl -sSL -o releases.atom https://github.com/anomalyco/opencode/releases.atom                       # 200, 6758 B
grep -n '' releases.atom | sed -n 27p                                                                # the Bun 1.4.4 <li>
curl -sSLO https://registry.npmjs.org/opencode-linux-x64/-/opencode-linux-x64-1.19.{3,4}.tgz
tar -xzf oc-1.19.3.tgz -C pkg193 ; tar -xzf oc-1.19.4.tgz -C pkg194
sha256sum pkg193/package/bin/opencode pkg194/package/bin/opencode                                    # 179ca421… ; 538fcb1b…
strings -n 4 pkg193/package/bin/opencode > mine-1.19.3.strings ; … pkg194 … > mine-1.19.4.strings
grep -c 'fn("' mine-1.19.3.strings mine-1.19.4.strings                                               # 120 ; 2
grep -c 'fn('   mine-1.19.3.strings mine-1.19.4.strings                                              # 192 ; 103
grep -c 'Key.make(' mine-1.19.3.strings mine-1.19.4.strings                                          # 12 ; 6
```

Remaining unknowns: none for the row's cells as written, other than D3's future-dated volatility, which no
fetch today can settle.
