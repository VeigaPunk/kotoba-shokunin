# ExecModel — round 86 w1 (C1 freshness): omp 18.15.0 catalogue model

Seat: ExecModel (leaf). Files written in the lane: `verifiers/verify_harness_claims.py`,
`verifiers/omp-skill-roots.tsv` (uncommitted, for the L1 to integrate), plus receipts under
`.ufo/waves/round-86/w1/ExecModel/` (`score.txt`, `CANDIDATE_READY`, `cli-after.txt`).

## Result

Scratch clone of `b9ee5484a139c4428a2d53e572868abe86844821` (addendum-1 counter, sha256
`39a014f2…4520`) + the two candidate files, commit `903bd78e18c0dbb6d4013d9726d89dbe7c190bcd`:

    guard G1 no-echo PASS
    guard G2 provenance PASS
    guard G3 fixture PASS
    guard G4 roots PASS
    omp catalogue lines reproduced 215 of 215
    exit=0

No MISS lines. Before: base `83 of 215`, G4 FAIL, exit 1 (132 `not-discovered`).
`verify_harness_claims.py --self-test`: before `0 failure(s) over 10 assertions`, after
`0 failure(s) over 34 assertions` (exit 0). Main CLI (`--cwd /home/vgpnk/Projects/shokunin`):
base module `16/28 checks pass`, exit 1; candidate `16/28 checks pass`, exit 1 — the same 12
DRIFT ids (round-13 baseline, pre-existing); no crash, no new DRIFT row. Receipts:
`ExecModel/cli-base.txt`, `ExecModel/cli-after.txt`.

Candidate sha256: `verify_harness_claims.py` `bd793b6c…0ab7`, `omp-skill-roots.tsv` `36021309…7800`.

## What the 18.15.0 source says (offsets are byte offsets into `/home/vgpnk/.local/bin/omp`, sha256 `6737ee24…7b0f`)

The catalogue is `Dp` in `extensibility/skills.ts` (~177,496,0xx): it loads the `skills`
capability (`kn(zl.id, …)`) from every registered provider and keeps an item when the gate `ue`
passes. Gate (177,499,2xx–177,499,8xx): `enableCodexUser: R = false`, `enableClaudeUser: k = false`,
`enableClaudeProject = true`, `enablePiUser/PiProject/AgentsUser/AgentsProject = true`; claude/codex
user fall back to `zi(provider)`, which is false for opt-in providers in `me`
(capability/index.ts 172,770,7xx: `codex: true`, `claude: true`, `opencode: true`, …); any other
*user* level goes through `zi` (true for non-opt-in providers), every project level is `true`.
This host's `config.yml` has no `skills.*`/extensions/plugin settings (grep), so defaults hold.

Providers for `skills` (priority) and the roots they read:

| provider | prio | roots | source |
|---|---|---|---|
| native (`Or`) | 100 | `<dir>/.omp/skills` for cwd→git root (home excluded); `~/.omp/agent/skills` | `T7`: `dir: fr.join(k, Ou.projectDir, "skills")` @173,819,979, `dir: fr.join(we(), "skills")` @173,820,135; description `Native OMP configuration from ~/.omp and .omp/` @173,814,318 |
| skillshare | 95 | `skills.lock.json` store under `~/.omp/agent` (absent on host) | discovery/skillshare.ts `Y4t` — not modelled (no lock) |
| omp-plugins (`xo`) | 90 | `<pkg>/skills` of each installed omp plugin | see chain below |
| claude (`wi`) | 80 | `.claude/skills` cwd→git root; user root opt-in (off) | `Zte` @173,840,164; `Load skills from .claude/skills/*/SKILL.md` @173,847,159 |
| agent-plugins (`eb`) | 75 | `skills/` of agent-plugins.org packages (root `plugin.json`) from the Claude/omp plugin registries | discovery/agent-plugins.ts; the 4 Claude registry plugins have no root `plugin.json` → none |
| agents (`Yo`) | 70 | `.agent/skills`, `.agents/skills` cwd→git root (home excluded) + `~/.agent/skills`, `~/.agents/skills` | `var y1 = [".agent", ".agents"];` @173,864,226; `Load skills from .agent/skills and .agents/skills (project walk-up + user home)` @173,866,320 |
| codex (`Qr`) | 70 | `.codex/skills` (cwd); `~/.codex/skills` opt-in (off) | `mre` @173,882,077; `Load skills from ~/.codex/skills and .codex/skills/` @173,887,155 |
| opencode (`Io`) | 55 | `.opencode/skills` (cwd); `~/.config/opencode/skills` opt-in (off) | `Bre` @173,903,087; quote @173,905,684 |
| github (`Qo`) | 30 | `.github/skills` (cwd) | `sie`; quote @173,911,210 |
| managed (`sl`) | 5 | `~/.omp/agent/managed-skills` (only names nobody else has) | `M7`; quote @173,820,704 |

Per-root scan `Ba` (discovery/helpers.ts ~172,790,2xx): skips entries starting with `.`
(@172,791,566), takes dir/symlink entries holding `SKILL.md`, names the skill by frontmatter
`name` trimmed else the directory (@172,790,973), skips names with a path separator.

Host falsification of the opt-in reading: `~/.codex/skills/kimi-webbridge`, `~/.claude/skills/
{claude-red,kimi-webbridge,learned,synced}` exist and are **absent** from the 215-line catalogue;
the 4 Claude-registry plugins (`superpowers`, `frontend-design`, …) are absent too.

### omp-plugins chain (the 132 previously missing names) — the `var Gh = ".omp";` ledger row

1. `var Gh = ".omp";` @166,884,553 (packages/utils/src/dirs.ts); `function qh() { return
   process.env.PI_CONFIG_DIR || Gh; }` (PI_CONFIG_DIR unset).
2. `$o(p)`: `return h.join(p, qh(), "plugins");` @166,892,383 → `~/.omp/plugins`.
3. `eD` (extensibility/plugins/loader.ts): `const R = yo.join(u, "node_modules");` @173,767,148;
   `const U = yo.join(u, "omp-plugins.lock.json");` @173,767,575; candidates = package.json deps ∪
   lock keys, undeclared entries kept only if `node_modules/<name>` is a symlink;
   `const ue = oe.omp || oe.pi;` @173,768,743; `if (he && !he.enabled) {` @173,768,871;
   `UQ` calls `const k = await eD(R, x, "user");` @173,769,583.
4. `X9` (discovery/omp-extension-roots.ts) with `var bC = "merge";` @173,772,524 adds `XQ` →
   `AP` (the `eD` list) to the extension roots.
5. `uie` (discovery/omp-plugins.ts): `const p = await vd(u, "skills");` @173,914,848 then
   `dir: Zo.join(R.path, "skills"),` @173,914,936; provider `var wd = 90;` @173,914,660.

Host: `~/.omp/plugins/omp-plugins.lock.json` enables `ecc-pi-core` (symlink →
`~/.ecc/pi/core`, `package.json` `"pi": {"skills": ["./skills"]}`) and `unreal-engine-skills-omp`
(`"omp"` manifest, no `skills/`). `ecc-pi-core/skills` holds exactly the 132 names; the other
83 are `~/.agents/skills` (incl. symlinks `omarchy`, `tower`, `shokunin`, `ufo`, `swarm`). No
name occurs in both roots, so omp's namespacing (`u0e`) never fires here.

No ELF line holds `.omp` together with `plugins` (all 168 `.omp` occurrences scanned); under
addendum-1 the row cites the constant (L1 accepted). ReviewerRoots judges it.

## Model changes (`verifiers/verify_harness_claims.py`)

- `WALKUP_REL` = `.omp/skills`, `.claude/skills`, `.agent/skills`, `.agents/skills`,
  `.codex/skills`, `.opencode/skills`, `.github/skills` (priority order). cwd only: the fleet
  root is a git root, where every walk-up is cwd itself.
- `USER_ROOTS` = `~/.omp/agent/skills`, `omp_plugin_skill_roots(~/.omp/plugins)`,
  `~/.agent/skills`, `~/.agents/skills`, `~/.omp/agent/managed-skills`. Dropped
  `~/.config/opencode/skills` and `~/.claude/skills` (opt-in, off).
- New `omp_plugin_skill_roots` ports `eD` (JS truthiness for `oe.omp || oe.pi` and
  `he && !he.enabled`). When neither `package.json` nor the lock is readable but
  `node_modules` is — the counter's sandbox hides `~/.omp` and binds back only
  `plugins/node_modules` — it takes every package with a manifest (omp would take none);
  on the host the registry decides. Same result here (both host plugins are enabled).
- `discover_skills`: signature unchanged, first root wins; now skips `.`-entries, names by
  frontmatter `name` (fallback directory), drops names with `/` or `\`. No fixture skill has
  frontmatter name ≠ directory.
- `preview` **changed**: 18.15.0 `dnt` (@178,770,368: `const c = o >= E ? r.slice(0,
  o).trimEnd() : r;`) cuts at the last space only when it sits at index ≥ 40, else keeps the
  whole 99-char slice; the lane cut at any space (and at 98 chars when none). No fixture line
  hit the difference. `omp_key` unchanged (`A`: sha256(prompt‖0‖name‖0‖desc)); constants
  k=100, E=40, T=160, _=12 confirmed @178,768,2xx.
- `parse_frontmatter` untouched (all 215 files parse; every description reproduces).
- `name_matches_folder` now compares frontmatter name to the SKILL.md's directory (the key
  is now the frontmatter name). Stale `A8n/H7s/ldl` names and the 2026-09-28 note replaced.
- Self-test: 10 → 34 assertions (dnt branches incl. last space at 39/40/45, root lists,
  `Ba` rules, first-root-wins, dangling, plugin registry/lock/no-registry worlds).

## Findings

- F1: base model missed omp 18.15.0's omp-plugin skill roots (132/215 lines).
- F2: base `preview` deviated from `dnt` on the last-space branch (no fixture impact).
- F3: base `USER_ROOTS` listed two roots 18.15.0 does not read by default
  (`~/.claude/skills`, `~/.config/opencode/skills`); `~/.omp/agent/skills` does not exist on
  this host.
- F4: the newest live catalogue (22:31:02Z, after the freeze render 21:55:22Z) also lists 215;
  the CLI's `catalogue_matched` 35/215 is the old "every line is cached" check the plan names
  as the mined mistake (180 lines are previews, not cache rows).

## Risks

- Lengths are Python code points; omp uses UTF-16 units. Checked: 0 of the 215 descriptions
  carry an astral character, 0 divergences against a UTF-16 port.
- First-root-wins ≠ omp's `u0e` namespacing for differing same-name skills (`<ns>/<name>`);
  equal on this host (no cross-root name collision).
- Not modelled: skillshare lock store, `skills.customDirectories`, configured `extensions:`,
  project-scope plugins, `enabled: false` frontmatter, `requireDescription` for native/plugins
  (none present on this host).
- Sandbox fallback in `omp_plugin_skill_roots` would over-include a lock-disabled plugin when
  the registry is hidden.

Tools installed/updated: none.
