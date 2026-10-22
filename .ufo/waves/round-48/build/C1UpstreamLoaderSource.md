# C1 upstream loader source — opencode 1.19.3 skill discovery

Seat: KotobaR48.C1UpstreamLoaderSource (leaf, read-only on the lane). Question answered:
which directories under the opencode config dir are scanned for skills, and is discovery
direct-child or recursive?

## Findings

1. **Both `skill/` and `skills/` are scanned, under every configured directory** — one glob,
   brace-expanded. `packages/opencode/src/skill/index.ts:24`
   `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`, applied at
   `packages/opencode/src/skill/index.ts:205-207` over `yield* config.directories()`.
2. **Discovery is recursive, not direct-child.** `**/SKILL.md` descends arbitrarily
   (probe: depth-3 `skills/nested/deep/SKILL.md` loaded) **and `**` also matches zero
   segments**, so `skills/SKILL.md` sitting directly in the root loads too (probe:
   `directfile`). No exact-name third directory is scanned (`skillz/` ignored).
3. **Skill identity is the frontmatter `name`, not the directory name.**
   `packages/opencode/src/skill/index.ts:134` `state.skills[md.data.name] = {...}`; the
   `NameMismatchError` class at `:67` is exported but thrown nowhere in `packages/`
   (only constructed in `packages/opencode/test/skill/skill.test.ts:326`). Probe: dir
   `skill/misnamed/` with `name: frontmatter_name` registers as `frontmatter_name`.
4. **The configured directory set** is `packages/opencode/src/config/paths.ts:23-40`
   `unique([Global.Path.config, .opencode dirs up from cwd to worktree, ~/.opencode,
   OPENCODE_CONFIG_DIR])`; `Global.Path.config` = `Flag.OPENCODE_CONFIG_DIR ?? <XDG_CONFIG_HOME>/opencode`
   (`packages/core/src/global.ts:13,64`). External roots are a *different* pattern:
   `EXTERNAL_SKILL_PATTERN = "skills/**/SKILL.md"` (`:23`) over `~/.claude` and `~/.agents`
   (`:21-22`, `:190-193`) — plural only; probe: `~/.claude/skill/` ignored,
   `~/.claude/skills/` loaded.
5. **Residual gap class for C1, now sourced.** The oracle contract
   (`.ufo/round-48/oracle/config-root-cases.json`, key `contract.scope`) already declares
   "Direct-child disk-root enumeration only … Upstream source supports broader recursive
   discovery; this bounded input-class repair does not claim whole loader parity." This seat
   supplies the primary-source and live-binary backing for that sentence and names the exact
   residual class: (a) `SKILL.md` nested ≥2 levels under `skill/`/`skills/`, (b) `SKILL.md`
   directly at the root of those two dirs, (c) frontmatter `name` ≠ directory name. All three
   are discovered upstream but invisible to a direct-child *directory-name* union. The frozen
   matrix exercises none of them: every case uses depth-1 dirs and the ruler's `skill_text`
   (`config-root-ruler.py:68`) writes the parent directory name as the frontmatter name, so the
   repair stays inside its declared scope.
6. **Source tag and measured binary are the same release.** Local npx-cache ELF sha256
   `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` — the `179ca421…`
   prefix of lane row S015. `opencode --version` = 1.19.3.

## Proposed SOURCES row (next free id at round-48 base is S016; S001–S015 present)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | anomalyco/opencode — skill discovery, tag v1.19.3 — https://github.com/anomalyco/opencode/blob/v1.19.3/packages/opencode/src/skill/index.ts#L24 | code | A | Which directories under an opencode config directory are scanned for SKILL.md, and at what depth | `packages/opencode/src/skill/index.ts:24` `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`; `:205-207`; `config/paths.ts:23-40`; tag v1.19.3 = commit `e3c4eb242585dcd77be1a867391b7c25fd47ce52`; opened 2026-10-22 | Both `skill/` and `skills/` under every configured directory are scanned recursively, and `**` also matches zero segments, so a `SKILL.md` directly in either dir loads; identity is the frontmatter name, not the directory name | mined | 2026-10-22 | on-release | verifiers/verify_harness_independent.py |

## Evidence

Repository identity (canonical repo moved off `sst/opencode`):
```
$ curl -sS -o /dev/null -w '%{http_code} %{redirect_url}\n' https://api.github.com/repos/sst/opencode
301 https://api.github.com/repositories/975734319                 (curl_exit=0)
$ curl -sSL https://api.github.com/repositories/975734319   -> "full_name": "anomalyco/opencode", "default_branch": "dev"
```
Tag pin (accessed 2026-10-22T08:13:22Z):
```
$ curl -sSL -o /tmp/tagref.json -w 'http_code=%{http_code}\n' \
    https://api.github.com/repos/anomalyco/opencode/git/ref/tags/v1.19.3
http_code=200                                                     (curl_exit=0)
/tmp/tagref.json -> "ref": "refs/tags/v1.19.3", "type": "commit",
                    "sha": "e3c4eb242585dcd77be1a867391b7c25fd47ce52"
```
Clone (private scratch, not the lane):
```
$ git clone -q --depth 1 --branch v1.19.3 https://github.com/anomalyco/opencode.git oc-1.19.3   (exit 0)
$ git rev-parse HEAD  -> e3c4eb242585dcd77be1a867391b7c25fd47ce52   (exit 0)
$ git describe --tags -> v1.19.3                                    (exit 0)
$ git log -1 --format='%H|%ci|%s' -> e3c4eb24…|2026-10-16 12:31:36 +0000|release: v1.19.3
```
Located quotes (each ≤25 words):
- `packages/opencode/src/skill/index.ts:24` — `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` (4 words).
- `packages/opencode/src/skill/index.ts:23` — `const EXTERNAL_SKILL_PATTERN = "skills/**/SKILL.md"` (4 words).
- `packages/opencode/src/skill/index.ts:205-207` — `const configDirs = yield* config.directories()` / `for (const dir of configDirs) {` / `yield* scan(state, dir, OPENCODE_SKILL_PATTERN)` (13 words).
- `packages/opencode/src/config/paths.ts:25-27` — `return unique([ Global.Path.config, ...(!Flag.OPENCODE_DISABLE_PROJECT_CONFIG ? yield* afs.up({ targets: [".opencode"],` (13 words).
- `packages/opencode/src/skill/index.ts:134` — `state.skills[md.data.name] = {` (3 words).

Live-binary probe (pinned substrate, isolated HOME/XDG; probe tree under
`/fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C1UpstreamLoaderSource/probe{,2}`):
```
$ opencode debug skill          (bin/opencode.exe, sha256 179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9)
exit 0, 6 entries:
  directfile        <- xdg/opencode/skills/SKILL.md            (zero-segment `**`)
  alpha             <- xdg/opencode/skill/d1/SKILL.md          (singular root)
  frontmatter_name  <- xdg/opencode/skill/misnamed/SKILL.md    (dir name "misnamed")
  beta              <- xdg/opencode/skills/d2/SKILL.md         (plural root)
  gamma             <- xdg/opencode/skills/nested/deep/SKILL.md (recursive, depth 3)
  customize-opencode <- <built-in>
second probe, exit 0, 4 entries — positives: xdg/opencode/skill/pos, ~/.claude/skills/claud,
~/.agents/skills/ext; negatives (not loaded): xdg/opencode/SKILL.md, xdg/opencode/other/SKILL.md,
xdg/opencode/skillz/SKILL.md, ~/.claude/skill/claudsing/SKILL.md
```
`opencode --version` -> `1.19.3` (exit 0).

Byte pins at e3c4eb24 (independent second-fetch agreement with seat
`KotobaR48.FrSourcesRowsScribe`, whose clone of the same tag produced identical digests):
```
$ sha256sum packages/opencode/src/skill/index.ts   -> 91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6
$ sha256sum packages/opencode/src/config/paths.ts  -> cd86a34461b27caf1042f8cba140fbbed47790c4f30cd9691f87298e8d4d4444
$ sha256sum packages/core/src/global.ts            -> 37c9aae045e01cd246cd4d8c489e84ea4849b6297d3a6f9ff9b1bca57f85c013
```
Row custody: the scribe's S016 is byte-identical to the row above in every cell they diffed
(their `diff` over the two lines). The integrator changed one cell on landing: landed `used-by`
is `corpus/lessons/round-48.md`, not the verifier drafted here, which leaves census E11 open
until that lesson lands in the same commit (scribe's `sources-census.sh validate`, exit 1, sole
E-code; their observation, not re-run by this seat). That cell is the more honest one — the
verifier enumerates roots per the oracle contract and does not read the upstream discovery
facts; the lesson is the artifact that will cite this row's URL and quote. If the lesson slips,
the only allowed fallback is the pair `queued` + `used-by —` (the S004–S007 / S010 shape) — not
`mined` + `—`, which trips the maintained CLI's W03 "mined but unused" (scribe's finding, F7), and
not the verifier, whose 70305-byte path does exist at the lane base but does not depend on S016.

## Unknowns / not claimed

- Whether the shipped binary routes the interactive TUI through the legacy
  `packages/opencode/src/skill/index.ts` path or the v2 path
  (`packages/core/src/skill.ts:79` glob `{*.md,**/SKILL.md}`). `SkillV2` appears in
  `packages/opencode` only as a schema (`httpapi/api.ts:7,93`) and the httpapi `/skill`
  handler imports the legacy `@/skill` (`httpapi/handlers/instance.ts:8`); the probe output
  matches the legacy pattern exactly, so the legacy path is what ran. Not traced further —
  outside this seat's question.
- `packages/core/src/skill.ts:79` is a second, wider rule (any `*.md` at the directory root,
  plus recursive `SKILL.md`) whose activation condition I did not establish.
- Tooling: no install or upgrade performed (nothing needed).

## Report
`.ufo/waves/round-48/build/C1UpstreamLoaderSource.md`
