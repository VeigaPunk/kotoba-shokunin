Result: DONE — opencode 1.19.4 changes no instruction-loading source versus 1.19.3; the two failing C1 rules lost their anchors to a rebuild that renamed minified helper aliases (`fn`→`l`, `Key`→`Wr`), so the delta is artifact churn, not a behaviour change.

# C1 provenance — what changed between opencode-ai 1.19.3 and 1.19.4

Seat: KotobaR53.ScoutOcRelease (leaf, no dispatch). All network opens 2026-10-22 after 20:04Z.
Scratch: `/fast/scratch/hyaku/kotoba-r53/ScoutOcRelease/` (tag clones, dumps, fetches, sandbox lane clone at `repo/`).
No tool installs, no upgrades, no model calls. Lane read-only; the only lane write is this report file.

## 1. Answer

**The tag-to-tag source delta contains no instruction-loading change.** Between `v1.19.3`
(commit `e3c4eb242585dcd77be1a867391b7c25fd47ce52`, 2026-10-16T12:31:36Z) and `v1.19.4`
(`148842ef7cb1bc34192b3fff57d0f9721ab9c801`, 2026-10-22T13:03:27Z) exactly 48 files differ —
46 modified, 2 added — and none of them is under `packages/opencode/src/`:

- 30 `package.json` manifests (release-version sync),
- 11 build/CI/dependency files (`bun.lock`, `bunfig.toml`, `flake.*`, `nix/*`, two Dockerfiles, three `.github/*` files),
- 2 build scripts (`packages/cli/script/build.ts`, `packages/opencode/script/build.ts`) and 1 patch file,
- 2 test/story files (`packages/opencode/test/plugin/openai-ws.test.ts`, `packages/session-ui/src/components/timeline-playground.stories.tsx`),
- added: `packages/ui/bunfig.toml`, `packages/ui/test/solid-jsx.ts`.

The instruction-loading sources are byte-identical at both tags:

| file | sha256 at v1.19.3 and v1.19.4 |
|---|---|
| `packages/opencode/src/session/instruction.ts` | `fee79c023eae44f720d4d600f334a987ad5f7615c4a008a20c89131a92684a8f` |
| `packages/opencode/src/tool/read.ts` | `afec8294965cbd9b9e29d3453b682164f0ecdba26574ebc048e9ba21af209c68` |
| `packages/core/src/instruction-context.ts` | `fde78e0e5b5457d7290b832a435f29b033f770e0cae981f3d1eac22672a57e57` |
| `packages/core/src/system-context/builtins.ts` | `a5907c811772e7e93aab23884593f2e93348cca3c1cb8c3b41b0268c0a8d275e` |
| `packages/opencode/src/session/system.ts` | `7257f0660202d3e5d7ef86ee48cb4e51d5d0aa67703c274b8eb840b8ae307bbc` |
| `packages/opencode/src/session/llm/request.ts` | `90077551a9a46e11a37f44279c584832918d722c0ba0407ff8cad8d3437dd0de` |
| `packages/opencode/src/session/prompt.ts` | `f0c5bc64c0f0e966693d4a57f7ede1e9d6e188b396152f04b55303dc75b9b768` |
| `packages/web/src/content/docs/rules.mdx` | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` |

Verified by `cmp -s` on shallow clones of both tags (`git clone --depth 1 --branch v1.19.3|v1.19.4`),
both `IDENTICAL`. File-set delta computed by walking both trees and hashing every file:
`changed=46, added=2`; `diff -rq src-1.19.3/packages src-1.19.4/packages` agrees.

**Why the C1 rules fail, measured on the dumps.** The verifier's rules anchor on the *minified
helper alias* in front of the quoted name. The 1.19.4 rebuild reallocated those aliases:

| anchor | 1.19.3 dump hits | 1.19.4 dump hits |
|---|---|---|
| `fn("Instruction.resolve")` | 1 | **0** |
| `l("Instruction.resolve")` | 0 | 1 |
| `fn("ReadTool.execute")` | 1 | **0** |
| `l("ReadTool.execute")` | 0 | 1 |
| `Key.make("core/instructions")` | 1 | **0** |
| `Wr.make("core/instructions")` | 0 | 1 |
| `targets:["AGENTS.md"]` | 1 | 1 |
| `InstructionContext.observe` | 1 | 1 |
| `system-context-builtins` | 1 | 1 |
| `<system-reminder>` | 15 | 13 |
| `("Instruction.resolve")` | 1 | 1 |
| `("ReadTool.execute")` | 1 | 1 |
| `make("core/instructions")` | 1 | 1 |
| `fn("` (whole dump) | 120 | 2 |
| `Key.make(` (whole dump) | 12 | 6 |
| `l("` (whole dump) | 413 | 493 |

So OC-4 (`fn("Instruction.resolve")` + `fn("ReadTool.execute")` + `<system-reminder>`) loses two
of its three anchors and OC-6 (`InstructionContext.observe` + `Key.make("core/instructions")` +
`targets:["AGENTS.md"]` + `system-context-builtins`) loses one of four, while the quoted-name
arguments all remain present and unique. The two dumps are `strings -n 4` of the pinned ELFs (74,137,746 B for 1.19.4;
67,839,091 B for the 1.19.3 platform binary `179ca421…`, same bytes S015 pinned).

The chunk at each anchor shows the same code shape under renamed identifiers, e.g. the resolve walk
(`while(...startsWith(...))`, `dirname`, `claims` set) and the read-tool wrap. Source confirms the
behaviour is unchanged: `instruction.ts:179` `const resolve = Effect.fn("Instruction.resolve")(function* (`
along the same `systemPaths`/`globUp` path (`instruction.ts:81-87`, `:123-129`), and `read.ts:300`
`const loaded = yield* instruction.resolve(ctx.messages, filepath, ctx.messageID)` with
`read.ts:356` wrapping the loaded text in `<system-reminder>`. OC-6's source is
`instruction-context.ts:20` `const key = SystemContext.Key.make("core/instructions")`, `:40`
`const observe = Effect.fn("InstructionContext.observe")(function* ()`, `:51` `targets: ["AGENTS.md"]`,
composed in `system-context/builtins.ts:47` `name: "system-context-builtins"`, `:49` `deps: [… InstructionContext.node …]`.

**Why the rebuild moved aliases.** The release is a toolchain bump: root `package.json:7`
`"packageManager": "bun@1.3.14"` → `"bun@1.4.4"`, `packages/containers/bun-node/Dockerfile:7`
`ARG BUN_VERSION=1.3.14` → `1.4.4`, `packages/opencode/package.json:81`
`"@ff-labs/fff-bun": "0.9.4"` → `"0.10.5"`, and the release note names only the runtime upgrade.
`[INFERENCE]` The alias reallocation is caused by the Bun 1.3.14 → 1.4.4 bundler/minifier emitting
different local names for the same source (the dependency bump changes bundle content too, which
also perturbs name allocation). I did not rebuild the source with either Bun version, so the
attribution to the bundler is inference, not measurement. No behaviour change is claimed or observed
anywhere: no instruction source moved, and the anchor's quoted names are unchanged.

## 2. Verdict: refactor, not behaviour change

Evidence for "refactor":
1. Zero instruction-loading source files changed (hashes above; zero `packages/opencode/src/**`
   paths in the 48-file delta).
2. The only changes beyond manifests and toolchain pins are a musl native-package install fix in
   `packages/opencode/script/build.ts:141` (compare diff line 992), one websocket test expectation
   (`packages/opencode/test/plugin/openai-ws.test.ts`), and a storybook playground update.
3. The compiled instruction chunks carry the same literals and the same walk/wrap logic; only
   single-letter helper aliases moved, while the quoted argument strings are unchanged and unique.

Evidence against a behaviour change: none found. `[INFERENCE]` A Bun runtime upgrade could in
principle alter JS semantics, but nothing in the release note or the source delta claims or shows it.

## 3. Counter reproduction (honest before-state)

Sandbox clone `/fast/scratch/hyaku/kotoba-r53/ScoutOcRelease/repo` at the plan commit
`3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` (cloned from the lane, Git env unset).

```
$ python3 -B repo/verifiers/check_opencode_repin.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302
opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
exit=1
```

Per-rule detail (`python3 -B repo/verifiers/verify_surfaces.py --json --repo repo --opencode-strings oc-1.19.4.strings`, exit 1):

```
surfaces.opencode_extract FAIL :: declared opencode class(es) produced by no rule:
  opencode:instruction-context/AGENTS.md, opencode:read-hook/instructions;
  rule(s) matched nothing: OC-4 (owns opencode:read-hook/instructions; missing
  fn("Instruction.resolve") + fn("ReadTool.execute") + <system-reminder>);
  OC-6 (owns opencode:instruction-context/AGENTS.md; missing InstructionContext.observe +
  Key.make("core/instructions") + targets:["AGENTS.md"] + system-context-builtins)
```

All other checks PASS (`literal_present`, `no_uncovered_class`, `table_parity`,
`literal_parity`, `kind_parity`, `excluded_reason`).

Pin failure (`python3 -B repo/verifiers/check_substrate_pins.py --json`, exit 1): PASS 2, FAIL 1 —
`opencode_binary_sha256` expected `179ca421…` (1.19.3), observed `538fcb1b…` (1.19.4). The pin lives
at `verifiers/baseline.json:10`; omp's sha and mtime pins PASS.

Host artifact identity, confirmed end to end:
`sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`
→ `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, 214,522,032 B,
mtime `2026-10-22 14:50:30.116162200 -0300` (= 17:50:30Z). The published platform tarball
`opencode-linux-x64-1.19.4.tgz` extracts to the identical sha256 and size, so the npx file is the
registry artifact, not a local rebuild.

What the fix seat needs (observation only, this seat does not edit):
- OC-4/OC-6 anchors should stop naming the minified alias: `("Instruction.resolve")`,
  `("ReadTool.execute")` and `make("core/instructions")` each occur exactly once in both dumps,
  while `fn("` dropped 120→2 and `Key.make(` 12→6. Any re-anchor must keep the rule fail-closed and
  the mutation-tester's planted-name/extra-string arms must still kill.
- `verifiers/baseline.json:10` needs the 1.19.4 sha; the stale prose at `verify_surfaces.py:562`
  ("now runs npm `opencode-ai` 1.19.3 (npx cache, sha `179ca421…`)") and the round-47 note in
  `surfaces-baseline.json:3` describe the old measurement.

## 4. Provenance / fetch log

All fetches `curl -sSL` on 2026-10-22, times UTC, sha256 over the fetched bytes.

| artifact | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| opencode-ai 1.19.4 version doc | https://registry.npmjs.org/opencode-ai/1.19.4 | 20:13:07Z | 200 | 2,021 | `7aace4ba41a5bb0866c9a4312218d367e74227f47769fd707956ef83d5538dd8` |
| opencode-ai 1.19.3 version doc | https://registry.npmjs.org/opencode-ai/1.19.3 | 20:13:07Z | 200 | 2,020 | `817ecab7509c87ed5fbfb845be44492c39f1d224b88e859cceb623c4b0390131` |
| opencode-ai packument | https://registry.npmjs.org/opencode-ai | 20:13:07-08Z | 200 | 25,052,130 | `0552c76d72f6a33891ab88ac5d029a05fb98eb4a4e6f74fa937c678af6718216` |
| opencode-linux-x64 packument | https://registry.npmjs.org/opencode-linux-x64 | 20:13:08Z | 200 | 17,962,684 | `5498c7c33ec0237e07db6289c4ee3db9361a3b9666f67c691ddbc65c4dd913e8` |
| release page v1.19.4 (HTML) | https://github.com/anomalyco/opencode/releases/tag/v1.19.4 | 20:13:08-09Z | 200 | 194,684 | `2a0622b569b7b7ba167cab11cb5912302916a24f74d10d6130d4e14142ea18b4` |
| releases atom feed | https://github.com/anomalyco/opencode/releases.atom | 20:13:09Z | 200 | 6,758 | `5d050363ba74e9b441a41de9c81ec34b39a9df91952e1e40d720052ff3a6fe1a` |
| compare page (HTML) | https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4 | 20:13:09-10Z | 200 | 267,746 | `6df70c1197aecf78cc43572f342b9b66fa4a6c348c25fe3784b030644ff4a5d3` |
| compare diff | https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff | 20:13:10Z | 200 | 66,868 | `a6a680aec87f4b274dae4d088115f15503275d52846a35827aee1faf91130863` |
| rules.mdx at v1.19.4 | https://raw.githubusercontent.com/anomalyco/opencode/148842ef7cb1bc34192b3fff57d0f9721ab9c801/packages/web/src/content/docs/rules.mdx | 20:13:10-11Z | 200 | 6,758 | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` |
| rules.mdx at dev HEAD `4a6dacec…` | https://raw.githubusercontent.com/anomalyco/opencode/4a6dacec5e4afb69f211458e08be5233c57dd307/packages/web/src/content/docs/rules.mdx | 20:13:11Z | 200 | 6,758 | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` |
| live docs page | https://opencode.ai/docs/rules.md | 20:13:11-12Z | 200 | 6,684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |
| platform tarball 1.19.3 | https://registry.npmjs.org/opencode-linux-x64/-/opencode-linux-x64-1.19.3.tgz | 20:13:12Z | 200 | 60,356,012 | `71d67513eb4078a7ff8eb96806b1d5edcd6533a72b311409b2e88bad4188dac6` |
| platform tarball 1.19.4 | https://registry.npmjs.org/opencode-linux-x64/-/opencode-linux-x64-1.19.4.tgz | 20:13:12-13Z | 200 | 79,146,075 | `dca7b06bbb4e4a1ab3681b799cd328057b356d9399e8e47336cf53b7ae658d0d` |

The release HTML and compare HTML re-hash differently across two opens (dynamic tokens in GitHub's
shell: 194,664→194,684 B; 267,746 B both times) while the diff and atom bytes are stable. The
rendered rules page (6,684 B) differs from `rules.mdx` (6,758 B); `[INFERENCE]` the difference is the
build stripping the frontmatter block, which I did not verify against the site build.

Registry timestamps: `opencode-ai@1.19.4` published `2026-10-22T13:03:43.704Z`;
`opencode-linux-x64@1.19.4` published `2026-10-22T13:08:54.454Z`; `@1.19.3` at
`2026-10-16T12:32:00.280Z` / `12:32:02.564Z`. `gitHead` is absent/null in both version docs
(`npm view opencode-ai@1.19.4 time gitHead` exit 0 prints the time map; no gitHead field), so the npm
side gives publish times only; the commit identity comes from the tags.

Repository identity: `https://github.com/sst/opencode` answers `HTTP/2 301` with
`location: https://github.com/anomalyco/opencode` (20:10:20Z). `git ls-remote --tags` resolves
`refs/tags/v1.19.3` → `e3c4eb24…` and `refs/tags/v1.19.4` → `148842ef…` (exit 0); default branch is
`dev` at `4a6dacec5e4afb69f211458e08be5233c57dd307` (2026-10-22T15:56:44-04:00).

**Compare-view caveat.** GitHub's compare is merge-base based, not a pure tag-tree diff: 28 manifest
hunks read `"version": "1.19.2"` on the base side, while the v1.19.3 tag tree reads `1.19.3` for the
manifests checked (`packages/opencode/package.json:3`, `packages/app/package.json`,
`packages/cli/package.json`). Its 48-entry file set matches the tag-tree delta (46 changed + 2 added,
verified by hashing both trees), and its instruction-file verdict matches, but byte-identity claims
in this report rest on the two tag trees, not on the compare view.

## 5. Verbatim quotes (≤25 words each; line numbers in the fetched bytes)

- Release note, `releases.atom:27` (text after HTML-unescape): "Upgraded the bundled Bun runtime to
  1.4.4, which includes security fixes for Brotli, TLS, HTTP/1.1, HTTP/2, HTTP/3, WebSocket, and fetch".
- Build comment, `compare.diff:992`: "Bun 1.4.4 skips native packages for the other libc by default,
  but the musl targets need them."
- Dependency bump, `compare.diff:138-139`: `-        "@ff-labs/fff-bun": "0.9.4",` /
  `+        "@ff-labs/fff-bun": "0.10.5",`.
- Toolchain pin, tag tree `package.json:7` (1.19.3 and 1.19.4 respectively):
  `"packageManager": "bun@1.3.14"` / `"packageManager": "bun@1.4.4"`.
- Rules docs, `rules-v1.19.4.mdx:103`: "The first matching file wins in each category. For example,
  if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used."
- Rules docs, `rules-v1.19.4.mdx:81`: "**Project rules**: `CLAUDE.md` in your project directory
  (used if no `AGENTS.md` exists)".
- Rules docs, `rules-v1.19.4.mdx:131`: "All instruction files are combined with your `AGENTS.md` files."
- Rules docs, `rules-v1.19.4.mdx:159`: "use your Read tool to load it on a need-to-know basis".
- Read-tool wrap, `tool/read.ts:356`: "`\n\n<system-reminder>\n${loaded.map((item) => item.content).join("\n\n")}\n</system-reminder>`".

Docs source location: `packages/web/src/content/docs/rules.mdx` is still the live path at dev HEAD
`4a6dacec…` (raw fetch 200, identical bytes to the v1.19.4 tag copy). The round-52 `services/www/…`
path (S041) does not exist at this commit: a fetch of
`services/www/src/docs/content/rules.mdx` at `4a6dacec…` returned 404 (14 B, sha256 `d5558cd4…`).
`[INFERENCE]` S041's path came from a different branch/commit than dev HEAD today.

## 6. SOURCES row draft (S-number left as S0xx)

| S0xx | anomalyco/opencode — release v1.19.4 tag delta and release note (sst/opencode answers 301 to anomalyco/opencode) — https://github.com/anomalyco/opencode/compare/v1.19.3...v1.19.4.diff | code | A | What moved in the opencode artifact between the two npm releases the host's opencode re-pin measures, and whether any instruction-loading source moved | `compare.diff:1-1238` (48 entries, sha256 `a6a680ae…`); no path under `packages/opencode/src/`; `packages/opencode/script/build.ts:141` Bun 1.4.4 native-package comment; `packages/opencode/package.json:81` `@ff-labs/fff-bun` 0.9.4→0.10.5; root `package.json:7` bun@1.3.14→bun@1.4.4; release note `releases.atom:27`; tags v1.19.3 `e3c4eb24…` (2026-10-16T12:31:36Z), v1.19.4 `148842ef…` (2026-10-22T13:03:27Z); the compare view is merge-base based (28 manifest hunks read 1.19.2 before), so the tag trees are the byte-identity authority | The 1.19.4 delta changes no instruction-loading source: `session/instruction.ts` `fee79c02…`, `tool/read.ts` `afec8294…`, `core/src/instruction-context.ts` `fde78e0e…` and `system-context/builtins.ts` `a5907c81…` hash identically at both tags, and the release note names only a Bun 1.4.4 runtime upgrade; the bundle's renamed helpers (`fn(` 120→2 hits, `Key.make(` 12→6, while `("Instruction.resolve")` and `make("core/instructions")` stay at one hit each) are rebuild churn, not a loader change | mined | 2026-10-22 | on-release | .ufo/waves/round-53/build/ScoutOcRelease.md, plans/round-53.md § C1 |

## 7. Remaining unknowns

- Which exact change reallocated the minifier aliases (Bun 1.3.14→1.4.4 bundler versus the
  `@ff-labs/fff-bun` 0.9.4→0.10.5 bundle content). Not measured; would need building the v1.19.3
  tree under Bun 1.4.4 and the v1.19.4 tree under Bun 1.3.14.
- Whether Bun 1.4.4 changes observable runtime semantics for these code paths. No source or release
  claim of a behaviour change; not measured.
- The opencode 2.x channel (`v2.1.3`, 2026-10-22T12:45:27Z, ten minutes before v1.19.4) is a
  different release line and is not part of C1; nothing here measures it.
- One dump token (`<system-reminder>`) dropped 15→13 hits across the rebuild with no source change;
  this is consistent with bundled-literal layout churn but I did not locate the removed occurrences
  (no behaviour difference is claimed from the count alone).
