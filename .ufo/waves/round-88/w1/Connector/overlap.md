# Connector — sibling overlap scan, omp root semantics surface (round 88, w1)

Read-only. Scope: each sibling lane's HEAD (`git -C <lane> grep` / `git show HEAD:`), PROVINCE.md, SKILL.md,
corpus/knowledge, corpus/lessons, corpus/SOURCES.md, plus counters under tools/, scripts/, verifiers/.
No sibling was edited. Lane heads read: kumitate 7218699c, kasegi a5e814a, kama 95ad1dbb, mori 7b3fe9d5,
kagi a916f4a, kaidoku fe1913d90, tameshi f256302b, tabi 4bea87d5, mado e4875ba5, souji 16fa821f,
tsukuroi 64f45b79, chousa 378fda82, kengaku c3f81f72, kake d838e744, kotodama d39434b3, lore 0f044aa,
revenger dcb10b9, game-dev-2d 1e033ef0, game-dev-3d 39ca397, audio f9da7ee9. Lane `kotoba` HEAD 89579c7 (round-88 freeze),
with tip 4df1e80 an ancestor (checked).

Host facts read for the overlap (not executed): `~/.local/bin/omp` is 276785328 bytes, sha256
`6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` (matches the plan); ELF magic true;
`~/.local/bin/omp.real` absent.

## Lanes with a claim about omp skill roots, the omp catalogue, or the omp ELF: 4 (match count)

absorb = no for every row. "skill-root claim" = the row states where omp (or a tool on the omp path) reads skills.

| Lane | file:line | Claim | Skill-root claim? |
|---|---|---|---|
| kumitate | `corpus/knowledge/kimi-skills-plugins.md:513-518` | "OMP skills root shares names with the Kimi root": `~/.agents/skills/*` symlinked into `ompskills/.omp/skills/*`; Kimi scans it as a second User root | yes (routed to OMP lane) |
| kumitate | `corpus/knowledge/kimi-modes-machinery.md:177,517,527` | `.omp/skills/tower` and `~/Projects/ompskills/.omp/skills/` paths (measured 2026-10-13) | yes |
| kumitate | `corpus/knowledge/omp-agent-root.md:36,146` | agent-root member `skill-descriptions.db` (0600), cited to `dirs.ts` lines 984-987 | adjacent (agent root, skill metadata) |
| kumitate | `corpus/SOURCES.md:181` (S226) | omp v18.15.0 `dirs.ts` agent-directory member names at the installed release; 21 names, lines 793-1106 | adjacent; the row text does not say whether `skills` is one of them (not verified) |
| kumitate | `SKILL.md:618`; `scripts/omp-census.mjs` | `omp-census` gate, default root `$HOME/.omp/agent` | adjacent (agent root) |
| kumitate | `corpus/knowledge/omp-installed-release-mcp-runtime.md:2,22-25,90-91,166,178-183,214,265`; `PROVINCE.md:20` | ELF claims about `~/.local/bin/omp.real` (wrapper + release binary, `omp/18.12.6`) | ELF claim; host-stale (see below) |
| kumitate | `scripts/omp-binary-probe.sh:44-61,102,120` | byte reads of wrapper and `omp.real` (`grep -a -o -F`) | ELF reader |
| kumitate | `corpus/knowledge/route-probe-cluster.md:128-131,154,311`; `scripts/probe-token-plan-shared.mjs:19-20,108-121` | `omp models <provider> --json` catalogue read | "catalogue" in the model sense only, not skill catalogue |
| kasegi | `SKILL.md:1019` | `~/Projects/bounties/.omp/{config.yml,agents/,skills/}` named a "second routing truth" | yes (project-scoped omp skills dir) |
| kasegi | `corpus/knowledge/ufo-workspaces.md:163,309`; `corpus/lessons/round-12.md:42` | `.omp/skills/ufo/SKILL.md` is a drifted untracked fork | yes |
| kama | `corpus/knowledge/consumer-registry.md:59-61,236` | `~/.omp/agent/skills/kimi-webbridge` listed as a consumer path (DEAD endpoint `127.0.0.1:10086`) | yes (path under the omp agent skills dir) |
| kama | `corpus/knowledge/consumer-registry.md:12,66,101,237-238,369,390`; `PROVINCE.md:11,199,279`; `SKILL.md:103,117` | `~/.local/bin/omp` byte-offset claims for the builtin llama-cpp default (`:1544771`), other endpoint literals; presence/absence | ELF claim (provider defaults), not skill roots |
| kama | `tools/round65-province-host-audit.py:40`; `tools/round71-province-host-claims.py:20,110` | existence-only checks of `~/.local/bin/omp` (no byte read) | ELF path, no token read |
| mori | `corpus/SOURCES.md:108` (S102) | `~/.local/bin/omp` read-only locator, sha256 pinned `85d9daf3…ccfa4` | ELF claim; pin is stale against host `6737ee24` |
| mori | `tools/mori-job-runway.py:90,114,393-420` | `mmap` over the same ELF path; regex on `maxRunningJobs` and `async.maxJobs` | ELF reader (same file, job cap, not skill roots) |
| mori | `corpus/knowledge/harness-job-capacity-r25.md:13,231` | job cap clamp in `~/.local/bin/omp` (sha `85d9daf3…`) | ELF claim, not skill roots |

Lanes checked with no omp skill-root or omp ELF claim: tameshi, tabi, mado (its `~/.pi/agent/skills/omarchy` is
pi, not omp: `corpus/knowledge/omarchy-drift-watch.md:47`), souji (`corpus/lessons/round-20.md:320` ConsumerSkill root,
not omp), chousa, kengaku, kake, kotodama, kaidoku (ELF hits are generic ELF, no omp), kagi, lore, revenger,
game-dev-2d, game-dev-3d, audio, tsukuroi. Their hits on "catalog", "selftest", "ELF" are generic.

## Counters that read the same ELF surface

- **mori `tools/mori-job-runway.py`** reads `~/.local/bin/omp` by mmap (default `--binary` = realpath of `omp`
  on PATH, which is this file). Literals: `maxRunningJobs` (host ELF count 3) and `async.maxJobs`. v2's binding
  token sets are skill-root and reader tokens. **No collision** on the tokens read.
- **kumitate `scripts/omp-binary-probe.sh`** reads `omp.real` (a different file). On this host `omp.real` is absent
  and `~/.local/bin/omp` is the ELF, not a script. [INFERENCE from reading the code, not executed]: the `BIN=` line
  search finds nothing, so the probe takes `real-unidentified` and exits 2. Host ELF count of a line-start `BIN=` is 0
  (measured). Probe literals are protocol strings. **No collision** with v2 tokens.
- **kama `tools/round65-province-host-audit.py`, `tools/round71-province-host-claims.py`**: `test -e`-style presence
  only. **No collision.**
- **kotoba's own r87 counters** (`verifiers/check_omp_root_semantics.py:85`, `verifiers/check_omp_catalogue_repro.py:104`)
  read the same path. These are the lane's own frozen controls, not siblings; v2 must keep its token sets
  disjoint from them only if it reads the same byte ranges. Recorded for ExecLiveBound.

## Host-state facts a token set must respect (measured, read-only)

- Host ELF literal counts: `agent/skills` = 2 (the reader quote at byte offset 173866338: "Load skills from .agent/skills
  and .agents/skills (project walk-up + user home)", module `packages/coding-agent/src/discovery/agents.ts`), `.omp/agent/skills` = 0,
  `skill-descriptions` = 14, `omp.real` = 0, `maxRunningJobs` = 3.
- The r87 ledger's `binary_quote` for `{cwd}/.agent/skills`, `{cwd}/.agents/skills`, `~/.agent/skills`, `~/.agents/skills`
  is the same agents.ts sentence. The sibling claims `~/.agents/skills` (kumitate) and `.omp/skills` (kasegi, kumitate)
  name these same roots, so a token that binds a root path must not be the path string alone; bind the reader quote.

## Stale sibling claims about the omp ELF (report only, absorb no)

- kumitate `PROVINCE.md:20` and `corpus/knowledge/omp-installed-release-mcp-runtime.md` describe a 1680-byte wrapper and
  `~/.local/bin/omp.real` at `omp/18.12.6`. Host: `omp.real` absent, `~/.local/bin/omp` is a 276785328-byte ELF.
  kumitate round-67 verifier-spotcheck already flagged PROVINCE:20 as stale (unlanded).
- mori `corpus/SOURCES.md:108` pins `85d9daf3…ccfa4` for `~/.local/bin/omp`; host sha is `6737ee24…`.
- kama `consumer-registry.md:101` `~/.local/bin/omp:1544771` line offsets belong to an older bundle.

## Collision verdict

No other lane's counter reads the omp ELF with a token set that overlaps the skill-root or reader tokens
v2 would bind. Two sibling counters (mori, kumitate) read the same file or path with disjoint literals. The one
real overlap is textual: the sibling `~/.agents/skills` and `.omp/skills` claims share the agents.ts roots, so v2
should bind the reader quote and not only the path. Nothing here changes the frozen predicate.
