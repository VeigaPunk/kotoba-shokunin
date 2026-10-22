Result: DONE — the host + depth-≤2 always-on surface is 5 rule files (1 host, 4 project) and exactly one sibling pair, a `CLAUDE.md` symlink; no directory holds two independent rule files; the round-7 / baseline census no longer describes this host (host file 75→14 lines, its cited lines 48/51 are gone, the 6-file lane family is now 17, and 4 top-level project files are in no prior count).

Round 53 C2 scout, seat `KotobaR53.ScoutAlwaysOnPop`, measured 2026-10-22 on the live host.
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, no lane write except this report; no installs or
upgrades were run, so there is no tooling change to record.

## Scope read from source

The checklist C2 governs is `SKILL.md:360-378`, `## Always-on constraint-file checklist (AGENTS.md-class)`,
8 unchecked boxes; box 04 is `SKILL.md:371` ("No dated or transient text"), box 07 is `SKILL.md:375-376`
("One canonical rule-file name per repo (AGENTS.md **or** CLAUDE.md, or an explicit redirect)"). All 8 boxes
share one disposition string in `verifiers/checklist-baseline.json` (checked at the working tree and at
`e78dff66` with `git show`): `unexecuted:surface = AGENTS.md/CLAUDE.md class; 7 files at round 15 (6
repo-level under ~/projects plus the host ~/.agents/AGENTS.md); the hand-applied no-dated-text box splits
6 PASS / 1 FAIL (host file lines 48 and 51); instrument is SKILL.md-scoped`.

## 1. Host-level and client config-directory files (asked list)

| Path | State | Bytes | Lines | sha256 | Symlink |
|---|---|---|---|---|---|
| `/home/vgpnk/.agents/AGENTS.md` | present | 949 | 14 | `7b06a503110ca86373c1da0daf3694d5ce57f4ae9a792dd09fcf3c4ae4b1896e` | no (regular) |
| `/home/vgpnk/.claude/CLAUDE.md` | **absent** | — | — | — | — |
| `/home/vgpnk/.codex/AGENTS.md` | **absent** | — | — | — | — |
| `/home/vgpnk/.config/opencode/AGENTS.md` | **absent** | — | — | — | — |
| `/home/vgpnk/.gemini/GEMINI.md` | **absent** (`~/.gemini` does not exist) | — | — | — | — |

`for f in ~/.agents/AGENTS.md ~/.claude/CLAUDE.md ~/.codex/AGENTS.md ~/.config/opencode/AGENTS.md
~/.gemini/GEMINI.md; do [ -e "$f" ] || [ -L "$f" ]; done` → one EXISTS, four ABSENT, exit 0.

The three client config directories exist but carry no rule file: `~/.claude/` = `.credentials.json`,
`.last-cleanup`, `agents/`, `backups/`, `cache/`, `debug/`, `plugins/`, `projects/`, `session-env/`,
`sessions/`, `settings.json`, `skills/`; `~/.config/opencode/` = `cli.json`, `opencode.json`,
`service.json`; `~/.codex/` = `config.toml`, state DBs. No rule-file reference in either client config:
`grep -n -i -E 'instruction|agents|prompt' ~/.codex/config.toml` returns exactly :69, :70
(`NODE_REPL_INSTRUCTIONS_USE_CASE_*`, shell env names) and :78 (`rea-agents@6.7.0`, an MCP package name),
and `grep -rn -i 'instruction' ~/.config/opencode/` → exit 1, no match (its `opencode.json` holds only
`$schema`, `theme`, `autoupdate`). `cli.json` holds session/tab UX settings; `service.json` holds one
`password` field — do not quote that file into lane artifacts.

Additional host-scope checks that came back empty: `~/AGENTS.md`, `~/CLAUDE.md`, `~/GEMINI.md`,
`~/CLAUDE.local.md` all absent; `~/.agent/` absent (only `~/.agents/`); `~/.copilot/copilot-instructions.md`
absent; no `.github/copilot-instructions.md` at depth ≤3 under `/home/vgpnk/Projects`.

## 2. Depth ≤ 2 under /home/vgpnk/Projects

`find . -maxdepth 2 \( -name node_modules -o -name .git \) -prune -o -type f \( -name AGENTS.md -o -name
CLAUDE.md -o -name GEMINI.md -o -name CLAUDE.local.md -o -name AGENT.md \) -print` → 4 regular files;
`-type l` over the same names → 1 symlink (`./kimi-code/CLAUDE.md`). No `GEMINI.md`, no `CLAUDE.local.md`,
no `.claude/CLAUDE.md` anywhere at depth ≤2 (`find . -maxdepth 3 -type d -name .claude` → none).

| Path | Bytes | Lines | sha256 | Mode | Tracked |
|---|---|---|---|---|---|
| `kimi-code/AGENTS.md` | 14941 | 124 | `a63198630e042e03fa97afa6b9c5d1877052d8218c02029474d5e6d782732bdc` | 644 | yes, `kimi-code` git `100644 ad06a3b3…` |
| `kimi-code/CLAUDE.md` | 9 (link string) | 124 (resolves to AGENTS.md) | `a6319863…` (same bytes, target followed) | symlink | yes, git mode `120000 47dc3e3d…` |
| `opencodeufo/AGENTS.md` | 2347 | 32 | `92b17a0d2a00d7c00d9a514973f7c2ff5c627671a6a47a2cf6908c04a0192436` | 644 | no; ignored by `/home/vgpnk/.gitignore:3 /*` (home dir is a git repo) |
| `shokunin/AGENTS.md` | 5921 | 92 | `382f28ab4e2846a94e176f67b5ea93d6c6a347997778a10ddc4c78772886eb86` | 644 | no; untracked in the fleet repo (`git ls-files --error-unmatch AGENTS.md` → exit 1, and `check-ignore` → exit 1, so not ignored either) |
| `ufo-fsd-alpha/AGENTS.md` | 18492 | 293 | `4896d671d8193a9a00a56775bad588cb28a2984a8be16cf376fe75791f05e51b` | 600 | yes, `100644 4c333bb1…` |

mtime is not evidence of edit content, but for traceability (host clock, `-0300`): host `2026-10-20 09:18`,
`kimi-code` `2026-10-15 04:45`, `opencodeufo` `2026-10-11 14:32`, `shokunin` `2026-10-22 15:12`,
`ufo-fsd-alpha` `2026-10-20 06:56`.

## 2b. Beyond the requested depth (supplement, so the lane knows the floor is bigger)

`find . -maxdepth 6 \( -name node_modules -o -name .git -o -name .venv -o -name dist -o -name build -o
-name target \) -prune -o -type f \( -name AGENTS.md -o -name CLAUDE.md -o -name GEMINI.md -o -name
CLAUDE.local.md \) -print` → **35 files, all `AGENTS.md`; zero `CLAUDE.md`, `GEMINI.md` or
`CLAUDE.local.md`; zero symlinks** (`-type f` does not follow links, so the depth-2 `kimi-code/CLAUDE.md`
link is not in this 35; a matching `-type l` pass through depth 6 prints that one link and nothing else). By top-level project: `shokunin` 20 (17 lane files + `shokunin/AGENTS.md` + 2
duplicates under `shokunin/.tower/jj-probe/{kotoba,chousa}-shokunin/`), `kimi-code` 7 (root + `apps/kimi-code`,
`apps/kimi-inspect`, `docs`, `packages/klient`, `packages/minidb`, `packages/pi-tui`), `ds4cc-marketplace` 3,
`xsnapshot` 2, `ufo-fsd-alpha` 1, `opencodeufo` 1, `kimi-shokunin` 1 (`templates/mint/AGENTS.md`, a template).
Two consequences: a lane-walking instrument double-counts the fleet's lanes through the `.tower/jj-probe`
worktrees, and the round-7 drift table's "CLAUDE.md census 18 (5/1/12)" is a much deeper (vendored) count
than this pruning allows — it is not reproducible from depth ≤6 without the pruned trees, which I did not
scan.

## 3. The one sibling pair, and its relation

`/home/vgpnk/Projects/kimi-code/` holds both names. `readlink CLAUDE.md` → `AGENTS.md`;
`readlink -f` → `/home/vgpnk/Projects/kimi-code/AGENTS.md`; `stat` type `symbolic link`, size 9.
Relationship: **symlink redirect (the PASS form of alwayson.07)**. This is the only `CLAUDE.md` on the
whole enumerated surface, so the other redirect form (`CLAUDE.md` containing an `@AGENTS.md` line) has no
live instance — and since the only `CLAUDE.md` is a link to its sibling, no enumerated file can carry an
`@AGENTS.md` import (a symlink body is the target's bytes). Independent scan for import lines in all five
rule files (`grep -cE '^[[:space:]]*@[A-Za-z0-9_./~-]+\.[A-Za-z]+'`) → 0 in each, so nothing on this
surface pulls another rule file by import.

No other enumerated directory holds a second rule-file name: `~/.agents/` (AGENTS.md only, plus `hooks/`,
`skills/`), `opencodeufo/`, `shokunin/`, `ufo-fsd-alpha/`.

## 4. Directories holding two independent rule files

**None.** Every directory on the enumerated surface holds at most one rule-file name, except
`/home/vgpnk/Projects/kimi-code/`, whose second name is a symlink to the first, not an independent file.
A live run of the box-07 check therefore cannot produce the FAIL branch from this population; the FAIL
branch is reachable only through the counter's pinned fixture case `two-rule-files`.

## 5. What omp actually loads (`~/.omp`)

Source: `omp://context-files.md` (§ Native `.omp` files, § Other supported context conventions, § Load order
and shadowing) and `omp://system-prompt-customization.md` (§ Inputs and precedence).

| Native path | State | Bytes | Lines | sha256 | Role |
|---|---|---|---|---|---|
| `~/.omp/agent/AGENTS.md` | **absent** | — | — | — | user-level context file; would be the highest-priority user file |
| `~/.omp/agent/RULES.md` | present | 995 | 14 | `beb647d0d4bba504e918ae988335a43403c6cff7033e42e75a2577e9ca0999ed` | sticky rule, always-apply, carried on every request |
| `~/.omp/APPEND_SYSTEM.md` | present | 1242 | 18 | `5c2b85a3f8149d65b060b430e06bad536ddb03bc7506507d0095f5dd89f1f104` | plain-text append to the rendered system prompt |
| `~/.omp/agent/SYSTEM.md`, `SYSTEM_TEMPLATE.md`, `APPEND_SYSTEM.md` | absent | — | — | — | — |

Consequences, straight from that doc: (a) with `~/.omp/agent/AGENTS.md` absent, the user-scope slot goes to
the next provider, and the `.agent`/`.agents` provider — enabled by default — supplies
`~/.agents/AGENTS.md`, so that file is the surviving user context file today; (b) `~/.claude/CLAUDE.md`,
`~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`, `~/.config/opencode/AGENTS.md` are *opt-in* foreign user sources,
and `~/.omp/agent/config.yml` sets no `enabledProviders` (its top-level keys are `setupVersion`,
`extendedContext`, `enabledModels`, `modelRoles`, `task`, `retry`, `dev`, `tools`, `async`, `tier`,
`textVerbosity`, `hideThinkingBlock`, `omitThinking`; `grep -n -E 'enabledProviders|disabledProviders|
contextFiles|appendSystem|systemPrompt|extra'` → exit 1, no match), so they would not load even if present;
(c) `contextFiles.extra` is unset, so no `AGENTS.local.md`-class file is discovered. No relocation is in
play either: `env | grep -E 'CLAUDE_CONFIG_DIR|COPILOT_HOME|PI_CODING_AGENT_DIR|PI_CONFIG_DIR|OMP_PROFILE|PI_PROFILE'`
→ exit 1, no match, so the default profile (`~/.omp/agent`) and the default user bases are what the rules
above describe.

Project-level native surface contributes nothing: four project `.omp` directories exist
(`ufo-fsd-alpha/.omp`, `ompskills/.omp` (empty), `gamez/dbzmon/.omp`, `shokunin/.omp`) and none contains
`AGENTS.md` or `RULES.md` (depth-3 `find` for `AGENTS.md`/`RULES.md`/`SYSTEM*.md`/`APPEND_SYSTEM.md` under
`~/.omp` returns only the two user files above).

Live confirmation that these bytes reach a running session: this session's system prompt carries the
"Tooling directive — operator, 2026-10-19 (always on, every agent)" block whose first paragraph is
`~/.omp/agent/RULES.md:3-5` verbatim, and a Godspeed block matching `~/.omp/APPEND_SYSTEM.md:1-18`
including its provenance comment. [INFERENCE] the two differ in origin only in that the prompt block also
contains a sentence "Pacman guard: all pacman transactions are PAUSED host-wide … never -Sy, -Syu, -U, -R,
downgrade, or restart a host service" that is **not** in `RULES.md` on disk (`grep -n -iE 'pause|paused'
RULES.md` → exit 1, no match; `grep -n -i 'pacman' RULES.md` → :7, :10, :13 only), so at least two divergent copies of the same
always-on directive are in circulation and a future instrument that scans for it will find the on-disk copy
older than the delivered one.

## 6. Round-7 population comparison

Round-7 population (`corpus/knowledge/alwayson-checklist-round7.md` § Application): 7 files = host
`~/.agents/AGENTS.md` **75 lines / 3781 B / FAIL AC-1,2,4,5** (dated attestations at :48, :51; procedures at
:18, :55) + `shokunin/*-shokunin/AGENTS.md` **6/6 PASS**, named as
kagi/kake/kasegi/kengaku/kumitate/kotoba by `.ufo/waves/round-21/scouts/K02.md:56` (5 lines, 244–248 B,
`tail -n +2 | md5sum` = `12a62ab90292` for all six).

Measured today:

| Item | Round 7 | 2026-10-22 | Note |
|---|---|---|---|
| host `~/.agents/AGENTS.md` | 75 L / 3781 B | **14 L / 949 B**, sha `7b06a503…`, md5 `dd64d484ac5ba6429f6b3758d30afe69` | different file; no VCS in `~/.agents` (no `.git`) so no history to diff |
| the six named lanes | 6 files | still 6 files, still 5 lines each, body md5 `12a62ab90292` | shape unchanged |
| lanes in that body family | 6 | **9** (the six above plus chousa, kaidoku, mori) | +3 |
| `shokunin/*-shokunin` dirs with AGENTS.md | 6 | **17** of 21 sibling dirs | 4 singletons (kotodama 40 L, game-dev-3d 74 L, souji 20 L, kama 6 L) + a second family of 4 (mado/tabi/tameshi/tsukuroi, body `96f7dfd1d7d3`) |
| top-level depth-≤2 project files | 0 in the census | **4** (kimi-code, opencodeufo, shokunin, ufo-fsd-alpha) | none of the four is in the round-7 or baseline population |
| distinct body hashes across the 17 nested files | n/a | 6 | `12a62ab90292`×9, `96f7dfd1d7d3`×4, then 4 singletons |

Prior scouts already recorded this family drifting while never agreeing: `round-21/scouts/G5.md:139-141`
counts 11 files at `12a62ab9…` and 3 outliers; `round-23/scouts/F3.md:115` counts 10 in the 5-line family.
My count is 9. The family count is therefore not citable across rounds — only re-measurable.

## 7. Baseline disposition comparison (`verifiers/checklist-baseline.json`)

Three mismatches between the frozen disposition and today's surface, all factual:

1. **Population.** The disposition says "7 files at round 15 (6 repo-level under ~/projects plus the host)".
   Today the same scope is 1 host + 17 nested = 18 files, and a depth-≤2 scan adds 4 more (22 distinct
   files, 23 directory entries counting the symlink).
2. **Dead line pointers.** The disposition locates the dated-text FAIL at "host file lines 48 and 51".
   `wc -l < ~/.agents/AGENTS.md` → 14; `sed -n '48p;51p' ~/.agents/AGENTS.md` prints nothing, exit 0. Those
   pointers cannot be re-checked.
3. **Same-sentence staleness in the skill.** `SKILL.md:363` still says "the 75-line host
   `~/.agents/AGENTS.md`", against 14 lines today, and `SKILL.md:362-364` still says "6/6 repo files pass".

Raw date evidence on the live surface (mechanical scan only — this is not a box verdict, and it is not the
instrument being built): ISO `YYYY-MM-DD` occurs at `~/.agents/AGENTS.md:1` ("# Operator tooling directive —
2026-10-19") and at `ufo-fsd-alpha/AGENTS.md:87`, `:139`, `:268`; zero occurrences in the three other depth-≤2
files. `grep -cE '\b(January|…|December) [0-9]{1,2}\b'` → 0 in all five. `~/.omp/agent/RULES.md:1` also
carries "2026-10-19" but it is a `RULES.md`, outside the AGENTS.md/CLAUDE.md class the boxes name.

## 8. What this means for the C2 instrument (findings, not fixes)

- Scope must be stated, because it changes the population by more than 4×: depth ≤2 + host = 5 rule files,
  1 sibling pair, 0 independent-pair directories; host + nested-lane walk = 18 files and 0 sibling pairs;
  depth-≤6 walk = 35 `AGENTS.md` files, 33 distinct rule files because 2 of the `shokunin` entries are
  `.tower/jj-probe` worktree copies of lane files; still 0 independent pairs.
- Neither the round-7 numbers nor the disposition's "7 files" can be used as a live-baseline; a live
  invocation has to enumerate at run time.
- On today's live files: box 04 has ISO-date hits at `~/.agents/AGENTS.md:1` and `ufo-fsd-alpha/AGENTS.md:87,
  :139, :268`; box 07 has one directory (kimi-code) resolvable only through symlink resolution, and the
  `@AGENTS.md` import branch has no live instance at all, so a live suite that never plants fixtures proves
  nothing about it.
- `~/.agents/AGENTS.md:5` redirects to `/home/vgpnk/.omp/agent/RULES.md`, a different file name. If box 07's
  rule is read to cover any explicit redirect, that is a live case; as pinned in the counter (AGENTS.md ↔
  CLAUDE.md only) it is out of scope.

## Confidence and remaining unknowns

- Observed directly (`stat`, `sha256sum`, `wc -l`, `readlink`, `find`, `git ls-files`, file reads): every
  path, size, line count, hash, symlink and tracking fact above.
- Observed from harness docs (`omp://context-files.md`, `omp://system-prompt-customization.md`,
  `omp://config-usage.md`): the loading and dedup rules, and the default-on/opt-in provider split.
- [INFERENCE]: that `RULES.md` is the source of the prompt's directive paragraph (verbatim match of :3-5),
  and that the extra "Pacman guard" sentence arrives from a layer I did not locate. I did not attempt to
  identify that layer; it is outside this question.
- Not resolved: which 2 of the round-21 scout's 11-file family left it (G5 says 11, F3 says 10, measured 9).
  The lane repos are git repos, so the history exists, but per-lane archaeology is not this seat's question.
- Not resolved: whether the 4 top-level project `AGENTS.md` files existed at round 7 and were simply outside
  its census. `kimi-code/AGENTS.md` is mtime 2026-10-15 and tracked in its repo, so its own history could
  answer it; the other three cannot be dated reliably (`opencodeufo` is ignored by the home repo,
  `shokunin/AGENTS.md` is untracked).
