# Critic — round 86 W1 shortcut worlds against the C1 counter (Q71 disclosure)

Seat `Critic`. Each world was a scratch commit in a `git clone --shared` of the lane, and each
was scored by the lane counter:
`TMPDIR=$S python3 -B <lane>/verifiers/check_omp_catalogue_repro.py --repo $S/repo --rev <hash> --work $S/work-<tag>`.

- **Frozen counter** (freeze `ecfad51f`, counter sha256 `2390eec2…6514`): runs 19:16–19:19 on 2026-11-04. They came before
  addendum-1 (`b9ee548`, 19:27:14). Receipts: `receipts/<world>.txt`.
- **Amended counter** (addendum-1 `b9ee5484…`, counter sha256 `39a014f2…4520`, printed in every
  receipt): runs from 19:34. Receipts: `receipts/a1-<world>.txt`.

Generators, root lists, ledgers, module diffs and digests are in `worlds/` (`gen.py`, `alias.py`,
`dotfilter.py`, `reduce.py`, `score.sh`, `module-digests.txt`).

**How the brute world finds roots (it never reads omp's discovery code).**
`find /home/vgpnk -path /home/vgpnk/Projects/shokunin -prune -o -name SKILL.md -print` returned
5882 hits. A root is the grandparent of every SKILL.md whose parent-directory name is a fixture
name. That gives 107 roots covering 214 of 215 names. `omarchy` comes only through the
`~/.agents/skills/omarchy` symlink, and that root is already in the list. First match wins.

**The dot-brute variant, built for the amended G4.**
- `alias.py` adds one level of symlink aliases: a `find -type l` over HOME returned 613,683
  links; any link whose target is a root, or an ancestor of one, yields an alias root.
- `dotfilter.py` keeps a root only if its dot segments (`.x`) can be quoted from **some**
  printable ELF run of 12 or more characters that contains all of them. The ELF is used as an
  opaque string pool, and the meaning of the run is ignored.
- `reduce.py` keeps one alias per real directory, the one with the fewest path components.
- The result is 39 roots, each with its own ledger row, e.g. `~/.agents/skills<TAB>app.agents.hub`,
  `~/.omp/plugins/node_modules/ecc-pi-core/skills<TAB>Authenticate via the provider keys/OAuth
  state already configured under ~/.omp.`, and
  `~/.local/share/omp-gamedev/unity-technologies-skills/skills<TAB>String.prototype.localeCompare
  requires that |this| not be null or undefined`.

## Frozen counter (`ecfad51f`)

| world (receipt) | roots | ledger | N of 215 | G1 | G2 | G3 | G4 | exit |
|---|---|---|---|---|---|---|---|---|
| W-brute (a) `brute-a-noledger` | 107, find order | none | **141** | PASS | PASS | PASS | FAIL absent | **1** |
| W-brute (b) `brute-b-fragledger` | same | 107 rows, pattern = root, quote = any ELF string with a path fragment (`skills from .agent/skills and .agents/skills`, `Load skills from .claude/skills/*/SKILL.md`, `om ~/.codex/skills and .codex/skills/`, else `: archive has no SKILL.md`) | **141** | PASS | PASS | PASS | PASS | **1** |
| W-brute (c) `brute-c-wildledger` | same | 1 row `*` + `: archive has no SKILL.md` | 141 | PASS | PASS | PASS | PASS | 1 |
| W-alpha (a) `alpha-a-noledger` | 107, alphabetical | none | **143** | PASS | PASS | PASS | FAIL absent | **1** |
| W-alpha (b) `alpha-b-fragledger` | same | fragment ledger | **143** | PASS | PASS | PASS | PASS | **1** |
| W-cover (a) `cover-a-noledger` | 107, by coverage desc | none | 215 | PASS | PASS | PASS | FAIL absent | 1 |
| W-cover (c) `cover-c-wildledger` | same | `*` | **215** | PASS | PASS | PASS | PASS | **0** |
| W-base+1 (a) `baseplus1-a-noledger` | base 4 + `~/.ecc/pi/core/skills` (132 of 132 base misses; tied with 2 `.zcode` copies) | none | 215 | PASS | PASS | PASS | FAIL absent | 1 |
| W-base+1 (b) `baseplus1-b-fragledger` | same | 5 fragment rows | **215** | PASS | PASS | PASS | PASS | **0** |
| W-base+1 (c) `baseplus1-c-wildledger` | same | `*` | 215 | PASS | PASS | PASS | PASS | 0 |
| tie `baseplus1-zcache-b` / `baseplus1-zmarket-b` | base 4 + a `.zcode` copy | fragment | 215 / 215 | PASS | PASS | PASS | PASS | 0 / 0 |
| runner-up `baseplus1-eccskills-b` | base 4 + `~/.ecc/skills` (131) | fragment | 214 | PASS | PASS | PASS | PASS | 0 |
| **cheapest** `cheapest-zcode-1line-wild` | base + **1 appended line** `~/.zcode/cli/plugins/marketplaces/ecc/pi/core/skills` | 2 lines: header + `*<TAB>: archive has no SKILL.md` | **215** | PASS | PASS | PASS | PASS | **0** |
| reference `ref-pluginroot-noledger` | base 4 + `~/.omp/plugins/node_modules/ecc-pi-core/skills` | none | 215 | PASS | PASS | PASS | FAIL absent | 1 |

The 141 and 143 worlds lose 74 and 72 lines to `render-differs`: first match wins picks a
translated or forked copy (`docs/ja-JP`, `.kiro`, …).

The cheapest world was reported to KotobaR86 as F1 and became addendum-1 (K3).

## Amended counter (addendum-1, `b9ee5484`)

| world (receipt `a1-…`) | N of 215 | G1 | G2 | G3 | G4 | exit |
|---|---|---|---|---|---|---|
| W-brute (a) no ledger | **141** | PASS | PASS | PASS | FAIL absent | **1** |
| W-brute (b) fragment ledger | **141** | PASS | PASS | PASS | FAIL (204): quote does not name `.local` | **1** |
| W-brute (c) `*` | 141 | PASS | PASS | PASS | FAIL (142): wildcard in first segment | 1 |
| W-alpha (a) no ledger | **143** | PASS | PASS | PASS | FAIL absent | **1** |
| W-alpha (b) fragment ledger | **143** | PASS | PASS | PASS | FAIL (165): quote does not name `.claude` | **1** |
| W-cover (c) `*` | 215 | PASS | PASS | PASS | FAIL (216) | 1 |
| W-base+1 (b) `~/.ecc` + fragment | 215 | PASS | PASS | PASS | FAIL (135): quote does not name `.omp` | 1 |
| cheapest-zcode `*` (= K3) | 215 | PASS | PASS | PASS | FAIL (216) | 1 |
| **W-dotbrute find order** (39 roots, 39 junk-quote rows) | **212** | PASS | PASS | PASS | **PASS** | **0** |
| **W-dotbrute alphabetical** | **214** | PASS | PASS | PASS | **PASS** | **0** |
| **W-dotbrute coverage order** | **215** | PASS | PASS | PASS | **PASS** | **0** |
| W-dotbrute coverage, no ledger | 215 | PASS | PASS | PASS | FAIL absent | 1 |
| **cheapest-a1** `baseplus1-plugin-anyquote`: base + 1 line `~/.omp/plugins/node_modules/ecc-pi-core/skills`; ledger 3 rows `~/.omp/*<TAB>Authenticate via the provider keys/OAuth state already configured under ~/.omp.`, `~/.agents/skills<TAB>app.agents.hub`, `~/.claude/skills<TAB>.claude.json` | **215** | PASS | PASS | PASS | **PASS** | **0** |
| same, no ledger | 215 | PASS | PASS | PASS | FAIL absent | 1 |
| **W-candidate** (`903bd78` content: module sha256 `bd793b6c…`, ledger `36021309…`, copied from the lane working tree; digests equal `CANDIDATE_READY`) | **215** | PASS | PASS | PASS | PASS | **0** |

Under the amended counter the 141 world splits its 74 misses into 64 `render-differs` and 10
`preview-differs-from-reference` (amendment 3).

Where the dot-brute lines come from (host-side `discover_skills` on the same roots):
- **cover order:** 132 from `~/.omp/plugins/node_modules/ecc-pi-core/skills` and 83 from
  `~/.agents/skills`. These are the same two roots and counts as the candidate.
- **alpha order:** 131 plus 83, and 1 from an `~/.config/OpenBot/…` root.
- **find order:** 131 + 43, plus 23 from `~/.local/share/omp-gamedev/unity-technologies-skills/skills`,
  8 from `…/omp-gamedev/blender-claude-plugin/skills`, and 3 + 3 + 1 + 1 from `~/.config/OpenBot/…`,
  1 from `…/omp-gamedev/unity-mcp/.claude/skills`, 1 from `~/.local/share/devin/…`.

ELF hits: `omp-gamedev` 0, `OpenBot` 0, `zcode` 0, `.ecc` 0. `~/.omp/agent/config.yml` has no
`extensions`, `skill` or `customDirectories` key. The source packet has no row for any of these
roots.

## Answers

**(a) Does a world that never read omp's discovery source reach the target?**
- **Frozen counter: yes.** W-cover with the 1-row `*` ledger reaches 215, exit 0. W-base+1 with
  located but unrelated quotes also reaches 215, exit 0. With no ledger, every world fails G4
  only.
- **Amended counter: yes, still.** The dot-brute world reaches 215 (coverage order), 214
  (alphabetical) or **212 (find order)**, all with G1–G4 PASS and exit 0. Its ledger rows quote
  ELF runs that only spell the dot segment (`app.agents.hub`, `.claude.json`,
  `String.prototype.localeCompare …` for `.local`).
- The find-order world takes about 41 of its 212 lines from roots that omp 18.15.0 does not read
  (`~/.local/share/omp-gamedev/…`, `~/.config/OpenBot/…`, `~/.local/share/devin/…`; 0 ELF hits,
  no packet row). It still clears 205.
- The plain brute (141) and W-alpha (143) worlds stay below 205 under every ledger.

**(b) Cheapest world that reaches the target.**
- **Frozen counter:** the base module plus 1 appended line (a `.zcode` mirror omp never names)
  and a 2-line ledger (`*`). Result: 215, exit 0.
- **Amended counter:** the base module plus 1 appended line,
  `~/.omp/plugins/node_modules/ecc-pi-core/skills`, and a 3-row ledger whose quotes say nothing
  about discovery. Result: 215, exit 0.
- All 132 base misses sit in one plugin directory. One root is the whole delta, and any
  `.omp`-spelling ELF string satisfies G4 for it.

**(c) Does the candidate name a root the brute world needs but omp does not read? No.**
- The candidate's 215 lines come from exactly 2 roots: 132 from
  `~/.omp/plugins/node_modules/ecc-pi-core/skills` and 83 from `~/.agents/skills`.
- Both carry source-packet rows: omp-plugins, rows 36–48 (`dir: Zo.join(R.path, "skills"),`,
  `const R = yo.join(u, "node_modules");`); agents user, row 75 (`skills.enableAgentsUser`
  default true).
- The brute needs no root outside the candidate's set. The cover-order dot-brute uses the
  identical pair.
- The candidate drops `~/.claude/skills`, `~/.config/opencode/skills` and `~/.codex/skills`,
  consistent with packet rows 58 and 79 (user roots are opt-in, default false).
- The candidate also names roots that contribute **0** fixture lines, so the counter does not
  exercise them: `~/.agent/skills`, `~/.omp/agent/managed-skills`, `~/.omp/agent/skills` (empty),
  the `unreal-engine-skills-omp` plugin, and the 7-entry `WALKUP_REL`. Inside the sandbox the
  fleet tree is tmpfs.

## Findings

- F1 (frozen; fixed by addendum-1 amendment 1) — G4 accepted the pattern `*`. Receipt
  `cheapest-zcode-1line-wild.txt`.
- **F5 (amended; open) — G4's dot-directory rule checks spelling, not reading.** A quote passes
  if it contains the dot segment anywhere: `app.agents.hub` for `.agents`, `.claude.json` for
  `.claude`, `…localeCompare…` for `.local`. Under this rule a 39-root brute search that never
  read omp's loaders reaches 212–215 with exit 0, including the find-order world, which serves
  about 41 lines from roots omp does not read.
- **F6 (amended; open) — N cannot separate the candidate from the brute world.** The
  coverage-order dot-brute and the candidate produce the same root-to-name attribution
  (132 + 83) and the same N=215. The only discriminator is whether each ledger quote is the loader
  code, which is ReviewerRoots' judgement. The plan already states this residual bound, so this
  is a tradeoff and not a counter defect. But it means **C1's N carries no evidence of source
  derivation by itself**.
- **F7 (amended; design tension) — G4 now penalises the most meaningful quotes.** The loader
  lines that actually make omp read the plugin root (`dir: Zo.join(R.path, "skills"),`,
  `const R = yo.join(u, "node_modules");`) do not contain `.omp`, so the dot rule rejects them.
  It pushes ledgers toward generic name strings (`var Gh = ".omp";`, which the candidate uses).
- F4 (both) — the session cwd `/home/vgpnk/Projects/shokunin` is tmpfs inside bwrap, so
  `WALKUP_REL` roots always yield 0. Project discovery is unscored, and a model may list
  anything there at no cost.
- Candidate note — `omp_plugin_skill_roots` has a sandbox-only branch: with no readable registry
  it takes every package with a manifest. The counter's sandbox hides `~/.omp/plugins/package.json`
  and the lock, so the counter scores that fallback and never the registry logic that models omp.
  On this host both give the same two plugin roots (lock: `ecc-pi-core` true,
  `unreal-engine-skills-omp` true; package.json deps empty, both `node_modules` entries symlinks).
  The match holds only because the host is in that state.

**Smallest safe correction** (needs a further addendum or the next freeze; this seat patches
nothing):
1. Score attribution, not only N. Require each reproduced name's root to match a ledger row
   whose quote is drawn from the packet's located loader lines. In practice, pin a whitelist of
   loader-quote offsets (module path plus offset from ScoutRootsSource) instead of "any located
   string containing the dot segment".
2. Bind back `~/.omp/plugins/{package.json,omp-plugins.lock.json}` so that the candidate's
   registry branch is the one scored.

Without (1), the reviewer judgement in the kill rule is the only defence against F5 and F6.
ReviewerRoots should check every candidate ledger row against the packet quote, not against
spelling.

## Risks

- The brute search ran `find` without `-L`. A `find -L` run hit its 600 s timeout on symlink
  loops and was discarded. The alias pass covers one level of symlinks only.
- "omp does not read `omp-gamedev` / `OpenBot` / `.zcode` / `.ecc` directly" rests on 0 ELF hits,
  the absence of any packet row, and no `extensions` key in config.yml. [INFERENCE] I did not
  trace this at omp runtime.
- The candidate was scored from the lane working-tree files (content equal to `903bd78` by sha256),
  not from ExecModel's scratch commit object.
