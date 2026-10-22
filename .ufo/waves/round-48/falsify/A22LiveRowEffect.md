# Round 48 falsify — A22 live-row effect (depth)

Seat: `KotobaR48.A22LiveRowEffect` (leaf scout). Host: linux 7.2.11-arch1-1, x64.
Target claim: "on this host the live row is unchanged" for `oc.roots.names_plus_builtin`
(build-wave `C1LiveJoinEffect` finding 1, restated for the landed C2 commit).
Question asked: does `verifiers/verify_harness_independent.py --json` (default arguments)
produce the same `oc.roots.names_plus_builtin` value at base `75f671b` and landed `d1ae458`?

## Verdict

**CONFIRMED — no defect.** `oc.roots.names_plus_builtin` = **10 at both revisions**, default
arguments, exit 0 at both. All **28/28** check values are identical; row status `DERIVED` at
both; `unlanded = []`, `landed = 24` at both. The only target-row field that changed is the
evidence wording (base `(1 configured dirs present: none)` → landed `(1 present) and the
configured --oc-config roots (present: none)`), which the build report already declares.

The identity is **host-contingent, not vacuous**: the landed code path is live and does add
configured-root names when they exist (controlled probe: base 10 → landed 12, same host
substrates). On this host both configured roots are absent, so the union is a no-op.

## Method (private clones, default arguments only)

- `git clone -q <lane> /fast/scratch/hyaku/kotoba-r48-a2/seats2/A22LiveRowEffect/{base,landed}`;
  `base` @ `75f671b109d8eddd0d64c1429bd6379fe577175a`, `landed` @
  `d1ae45830235c38320b31032b57a8323cbf90b17`; both worktrees clean (`git status --porcelain` 0 lines).
- Verifier blob at base `06322fc5b0231d9bdc6cb4128c336cc5f1d53597`, at landed
  `134f756eb482cae2467218357349f9c1ba256cd6` (files sha256 `872993f8…` / `d67b1b6e…`).
- Runs: `python3 {base,landed}/verifiers/verify_harness_independent.py --json` → exit **0 / 0**,
  zero stderr bytes. Artifacts: `base.json` sha256 `93a04e2263d474f7876838f64d4153f59cbc11faf91c83a187d68716e49730be`,
  `landed.json` sha256 `1226ef898cfebb153ad769eeba1acf33aab6dd9a8221298b79e9050c6daa0fb5`
  (whole-file hashes differ because the four scoped-out catalogue probes carry live-session
  counters; see Determinism).
- No tool installs or updates; no writes outside `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A22LiveRowEffect/`
  and this report.

## Values at both revisions (base = landed for all 28)

| check | value |
|---|---|
| omp.elf.template_bytes | 273 |
| omp.elf.template_sha256 | c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51 |
| omp.db.rows | 17 |
| omp.db.rows_wellformed | 14 |
| omp.offered.skills | 10 |
| omp.offered.dangling | 0 |
| omp.cache.keys_reproduced | 7 |
| omp.cache.misses | 3 |
| omp.descriptions.over_cliff | 10 |
| omp.names.mismatches | 0 |
| omp.descriptions.missing | 0 |
| omp.descriptions.unmodelled | 3 |
| omp.cache.verified_skills | 7 |
| omp.catalogue.found | null (SCOPED_OUT at both) |
| omp.catalogue.total | null (SCOPED_OUT at both) |
| omp.catalogue.matched | null (SCOPED_OUT at both) |
| omp.catalogue.missing_names | null (SCOPED_OUT at both) |
| oc.log.init_count_max | 0 |
| oc.log.available_skills_hits | 0 |
| oc.log.skills_rescan_max | 3 |
| oc.log.init_count_monotone | [] |
| oc.log.skills_tag_hits | 0 |
| **oc.roots.names_plus_builtin** | **10** |
| oc.dup.roots_both_sided | 0 |
| oc.dup.onesided_roots | 0 |
| oc.permission.skill_lines | 0 |
| oc.permission.skill_allow | 0 |
| oc.roots.plugins_cache | 0 |

## Default `--oc-config` and configured roots on this host

- Default is `DEFAULT_OC_CONFIG = Path("/home/vgpnk/.config/opencode")` at both revisions
  (base line 127/1315, landed line 127/1482; identical string and identical argparse default).
- `/home/vgpnk/.config/opencode` exists (dir) and contains only `cli.json`, `opencode.json`,
  `service.json`.
- `/home/vgpnk/.config/opencode/skill` → does not exist; `/home/vgpnk/.config/opencode/skills` →
  does not exist (`ls` ENOENT for both; `.exists()`/`.is_dir()` false for both).

## Independent recount of the 10 (why the union is a no-op here)

Recount script over the same live substrates (read-only, run from the landed clone):
agents root `/home/vgpnk/.agents/skills` has 10 entries, all with `SKILL.md`, names =
`create-toolset, godspeed, omarchy, reverse-engineer-anything, shokunin, swarm, tower, ufo,
unreal-mcp, unreal-skill`. The opencode log (`/home/vgpnk/.local/share/opencode/log/opencode.log`,
mtime 2026-10-20 07:52, static across all runs) names six `directory:` roots; only
`/home/vgpnk/Projects/opencodeufo/.opencode/skills` exists, whose `SKILL.md` children are
`shokunin, tower` — both already in the agents-root set. Union = 10, matching the row.
(Note the log also names `~/.config/opencode/{skill,skills}`; both are absent.)

## Mechanism probe (definition is live; identity is host-contingent)

Same clones, same log/db/agents defaults, only `--oc-config` pointed at a scratch config holding
`skill/alpha-probe` and `skills/beta-probe` with `SKILL.md`:
`--oc-config probe-cfg` → base **10** (`probe-base.json` sha256 `df714929…`), landed **12**
(`probe-landed.json` sha256 `11b95ae8…`), exit 0 / 0. Landed evidence reads
`configured --oc-config roots (present: skill, skills)`. So the landed enumeration fires; the
live value stays 10 solely because this host has neither root. Base's evidence under the probe
still mislabels those config dirs as "configured dirs present" while ignoring them — an
evidence-text quirk the landed commit fixes; it does not affect any value.

## Determinism

- Reruns with default arguments: base 10, landed 10 again; the whole `checks` map is identical to
  the first run at each revision (`base rerun checks identical: true`, `landed rerun checks
  identical: true`; `rerun-base.json` sha256 `ceb4a9a4…`, `rerun-landed.json` `282d4107…`).
- Whole-row objects are not byte-stable run-to-run: base-vs-base-rerun and landed-vs-landed-rerun
  each differ in exactly the four `omp.catalogue.*` scoped-out probe blocks (live session tree
  mutates under `~/.omp/agent/sessions`). Comparison across commits differs in those same four
  probes plus the target row's evidence string. This is live-host drift, not a commit effect; the
  `checks` channel (the values) is stable at 28/28. Any "unchanged" gate must compare `checks`,
  not the file hash.

## Remaining unknowns / risks (not defects for this item)

- Producer/join side not re-run here (live producer reading 12 vs independent 10 is the known
  routed disagreement; separate seat's scope). This report only adjudicates the independent row.
- On a host where `--oc-config/skill` or `/skills` exists with unlogged names, the live independent
  value rises above 10 while the frozen join compares this row `equal`; the unchanged-live-row
  statement is therefore true for this host's substrate only, and the instrument will re-read it
  every run.
