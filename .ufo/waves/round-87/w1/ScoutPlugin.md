# ScoutPlugin — the plugin registry branch and C1's new source row (round 87, w1)

Seat: ScoutPlugin (leaf, read-only outside `.ufo/waves/round-87/w1/ScoutPlugin/`).
Host: Linux `7.2.11-arch1-1`, omp 18.15.0, ELF `/home/vgpnk/.local/bin/omp`
sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`.
All ELF offsets are byte offsets of the first match (python `mmap` + `re`, no copy into the lane).

Receipts: `ScoutPlugin/registry.txt`, `ScoutPlugin/SOURCE_RECORD.txt`, `ScoutPlugin/skill-size.txt`.

## 1. The plugin registry branch (round-86 CF3/P4)

### What omp reads under `~/.omp/plugins/`

The directory is small: `find ~/.omp/plugins -maxdepth 4` yields **6 entries** (2 dirs, 2 files,
2 symlinks). Following the symlinks (`find -L`) yields **175 entries** at depth 4 and 132 `SKILL.md`
at depth 5.

| file | reader (ELF quote @offset) | role |
|---|---|---|
| `~/.omp/plugins` | `function $o(p)` @166892325 → `return c.rootSubdir("plugins", "data");` @166892424 (module `// packages/utils/src/dirs.ts` @166884479) | the registry root itself |
| `~/.omp/plugins/node_modules` | `function Pu(p)` @166892466; `const R = yo.join(u, "node_modules");` @173767148 | package dir |
| `~/.omp/plugins/package.json` | `function i_(p)` @166892525; `const F = yo.join(u, "package.json");` @173767259 | declared dependencies |
| `~/.omp/plugins/omp-plugins.lock.json` | `function VV(p)` @166892584; `const U = yo.join(u, "omp-plugins.lock.json");` @173767575 | installed/enabled set |
| `~/.omp/plugins/node_modules/<pkg>/package.json` | `const re = yo.join(R, te, "package.json");` @173768431; `const ue = oe.omp \|\| oe.pi;` @173768743; `if (he && !he.enabled) {` @173768871 | package manifest + `omp`/`pi` key + lock `enabled` gate |
| `~/.omp/plugins/node_modules/<pkg>/skills/*/SKILL.md` | `dir: Zo.join(R.path, "skills"),` @173914936 (module `// packages/coding-agent/src/discovery/omp-plugins.ts` @173914407); `const c = d.join(s, S.name, "SKILL.md");` @172791679 | the skills root, one level deep |

Enumerator: `async function eD(u, p, x)` @173767117 in
`// packages/coding-agent/src/extensibility/plugins/loader.ts` @173766331. It short-circuits to `[]`
when `node_modules` is absent, reads `package.json` for `dependencies`, reads the lock for
`plugins`, skips a lock entry not declared in `dependencies` unless the package is symlinked, and
skips a package whose lock entry says `enabled: false`.
`plugin-overrides.json` is read project-level only (`tD` → `Pm("plugin-overrides.json", { user: false, cwd: u })`,
@173766757); it is not a file under `~/.omp/plugins/`.

### Which of them the round-86 hide list would hide

Hide list (`check_omp_catalogue_repro.py:250-257`): `~/.omp`, `/home/vgpnk/Projects/shokunin`,
`/fast/scratch`, `/tmp`, `/var/tmp`, `/dev/shm`, `/run/user`. Rebind
(`default_rebind`, lines 260-263): `~/.omp/plugins/node_modules`, `~/.omp/agent/skills` — the second
does not exist on this host, so `run_module`'s `if r.is_dir()` skips it.

Probed by running exactly that wrap (`bwrap --ro-bind / / … --tmpfs … --ro-bind <node_modules>`):

```
VISIBLE /home/vgpnk/.omp
VISIBLE /home/vgpnk/.omp/plugins
HIDDEN  /home/vgpnk/.omp/plugins/package.json
HIDDEN  /home/vgpnk/.omp/plugins/omp-plugins.lock.json
VISIBLE /home/vgpnk/.omp/plugins/node_modules
VISIBLE /home/vgpnk/.omp/plugins/node_modules/ecc-pi-core/package.json
VISIBLE /home/vgpnk/.omp/plugins/node_modules/ecc-pi-core/skills
VISIBLE /home/vgpnk/.omp/plugins/node_modules/unreal-engine-skills-omp/package.json
VISIBLE /home/vgpnk/.ecc/pi/core/skills
HIDDEN  /home/vgpnk/Projects/shokunin/.omp
glob_count=132
bwrap rc=0
```

So the hide list removes exactly the **two registry manifests** — `package.json` and
`omp-plugins.lock.json`, both direct children of `~/.omp/plugins/` — while the rebound
`node_modules` (a symlink to `/home/vgpnk/.ecc/pi/core`, outside `~/.omp`) keeps every package
manifest and every `SKILL.md` visible. CF3 is therefore precise and P4 is forced: inside the wrap
`eD` sees `package.json` ENOENT → `dependencies []`, lock ENOENT → `{}`, i.e. omp's own enumeration
yields **zero** plugin packages, while the 132 skill files are still there. A model scored in that
sandbox must carry a non-omp fallback (walk `node_modules/*/package.json`), which is exactly the
branch the round-86 review scored and named P4.

### Does the registry root still yield 132?

```
$ ls -d ~/.omp/plugins/node_modules/*/skills/*/SKILL.md | wc -l           -> 132
$ … | awk -F/ '{print $(NF-1)}' | sort -u | wc -l                          -> 132
registry SKILL.md: 132 unique: 132
in fixture catalogue: 132 | registry-only: 0 | fixture-only: 83
```

The round-86 review's 132 reproduces exactly and is a subset of the 215-entry fixture
(`verifiers/fixtures/omp-catalogue-r86/catalogue.json`); the remaining 83 come from the other
non-empty root (`~/.agents/skills`), unchanged. One plugin package
(`unreal-engine-skills-omp`) contributes 0 skills (it ships `hooks/` + `vendor/`, no `skills/`).

## 2. C1's new source row (`SOURCE_RECORD.txt`)

Module: `packages/coding-agent/src/discovery/omp-plugins.ts` (ELF header @173914407, before the
reader @173914936 — the same ordering C1's `module` conjunct requires).

```
url    https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-plugins.ts
tag    v18.15.0 of https://github.com/can1357/oh-my-pi  (the tag answered; default branch not read)
status 200   bytes 15362   sha256 4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4
quote  line 70: dir: path.join(root.path, "skills"),
ELF    the bundle is minified, so the exact line's counterpart is @173914936
       dir: Zo.join(R.path, "skills"),
       byte-identical anchor in both: "Sub-discovery (skills, hooks, tools, commands, rules, prompts,
       .mcp.json) inside extension packages" (upstream line 46, ELF @114492956)
```

Secondary fetches recorded in the same file: `extensibility/plugins/loader.ts` (200, 17785 B,
sha256 `d759c466…`), `discovery/omp-extension-roots.ts` (200, 15648 B, sha256 `9f673afe…`).
Fidelity: 13 of the 31 string literals ≥ 6 chars in the fetched module occur inside the ELF module
region; the absent 18 are import specifiers and template placeholders.

## 3. `SKILL.md` size (for the L1's considerthese item)

`skill-size.txt`: **600 lines, 86416 bytes, 156 lines over 120 chars, 86 lines over 300 chars,
longest line 1170 (line 521)** — identical at the worktree and at base `223ae62`. The plan's
"within the 600-line budget" is therefore already at the ceiling: any added row needs a matching
removal, or the budget sentence needs re-reading.

## 4. Findings for the L1 / closure

1. **CF3/P4 is a counter property, not an omp property.** The sandbox hides `package.json` and
   `omp-plugins.lock.json` only; the skill files it scores are visible. A round-87 counter that
   keeps this hide list keeps forcing a non-omp fallback branch, so any claim resting on the
   round-86 catalogue counter still scores the fallback. If round 87 wants the registry branch
   scored, the rebind set must include `~/.omp/plugins` (or the hide list must spare the two
   manifests) — that is a counter change, i.e. a new counter, not an edit to the frozen one.
2. **The registry is symlink-borne.** `~/.omp/plugins/node_modules` holds two symlinks and no real
   directories; the 132 skills live in `/home/vgpnk/.ecc/pi/core/skills`. Any model that resolves
   the registry by scanning real directories under `node_modules` sees nothing; the path must go
   through the symlink, as omp's `existsSync` + `Bun.file` path does.
3. **`omp-plugins.lock.json` is the only enable/disable authority.** `enabled: false` in the lock
   removes a package even when it is declared in `package.json` and symlinked (`if (he && !he.enabled)`
   @173768871); no other file under `~/.omp/plugins/` gates it.
4. **The source row's quote is a code quote, but not byte-identical to the ELF** — the ELF is a
   minified bun bundle. ScribeSources should carry the code quote and the byte-identical
   description anchor, as `SOURCE_RECORD.txt` records; claiming the exact upstream line occurs in
   the ELF would be false.

## 5. Gaps

- `ScoutElf`'s `ELF_MAP.tsv` had not appeared in `.ufo/waves/round-87/w1/` while this seat worked;
  the module identification above is independent (ELF header scan of 3131 `// packages/…` headers,
  then the reader's offset within the `discovery/omp-plugins.ts` region).
- The project-level plugin branch (`<cwd>/.omp/omp-plugins.lock.json` via `Jl(u)` @173769599) was
  not exercised: the project `.omp` is hidden by the same wrap and no project lock exists on this
  host.
- No counter was run: this seat is read-only on `verifiers/`; C1's and C2's counters belong to
  ExecSemantics/ExecRepairs.
