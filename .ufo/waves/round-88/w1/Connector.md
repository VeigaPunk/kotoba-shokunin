# Connector — round 88 w1 — sibling overlap (read-only)

Detail: `.ufo/waves/round-88/w1/Connector/overlap.md`. Marker: `.ufo/waves/round-88/w1/CONNECTOR_READY` (content `4`).

## Match count

4 sibling lanes state a claim about omp skill roots, the omp catalogue or the omp ELF: kumitate, kasegi, kama, mori.
Each claim is reported; none is absorbed (absorb = no).

## Per-lane

- **kumitate** — yes, skill-root claims: `corpus/knowledge/kimi-skills-plugins.md:513-518` (OMP skills root shares
  names with the Kimi root, `~/.agents/skills` → `ompskills/.omp/skills`); `corpus/knowledge/kimi-modes-machinery.md:177,517,527`.
  ELF claims: `corpus/knowledge/omp-installed-release-mcp-runtime.md`, `scripts/omp-binary-probe.sh` (reads `omp.real`).
  Adjacent: `corpus/knowledge/omp-agent-root.md:36,146`, `corpus/SOURCES.md:181` (S226, dirs.ts at v18.15.0).
- **kasegi** — yes: `SKILL.md:1019` (`~/Projects/bounties/.omp/skills/` second routing truth);
  `corpus/knowledge/ufo-workspaces.md:163,309`.
- **kama** — yes, one skill path: `corpus/knowledge/consumer-registry.md:61,236` (`~/.omp/agent/skills/kimi-webbridge`).
  ELF claims (provider defaults, not skill roots): `consumer-registry.md:101`, `PROVINCE.md:11,199,279`, `SKILL.md:103,117`.
- **mori** — ELF claims, not skill roots: `corpus/SOURCES.md:108` (S102, sha `85d9daf3…`), `tools/mori-job-runway.py`
  (mmap of the same file; regex on `maxRunningJobs` / `async.maxJobs`), `corpus/knowledge/harness-job-capacity-r25.md:13,231`.
- No match: tameshi, tabi, mado (pi, not omp), souji, chousa, kengaku, kake, kotodama, kaidoku, kagi, lore, revenger,
  game-dev-2d, game-dev-3d, audio, tsukuroi.

## Counter collision

- mori `tools/mori-job-runway.py` reads the same ELF surface with literals `maxRunningJobs` and `async.maxJobs`.
  No token overlap with v2's skill-root or reader tokens. No collision.
- kumitate `scripts/omp-binary-probe.sh` reads `omp.real`, a different file. Absent on this host.
- kama `tools/round65-province-host-audit.py:40`, `tools/round71-province-host-claims.py:20,110`: existence checks only.
- Lane's own r87 counters read the same path (`verifiers/check_omp_root_semantics.py:85`,
  `verifiers/check_omp_catalogue_repro.py:104`). They are the frozen controls, not siblings.

## Measured host facts (read-only, not executed)

- `~/.local/bin/omp`: 276785328 B, sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`, ELF magic true
  (matches the plan). `~/.local/bin/omp.real`: absent.
- Literal counts in the ELF: `agent/skills` 2 (offset 173866338, the agents.ts reader quote "Load skills from .agent/skills
  and .agents/skills (project walk-up + user home)"); `.omp/agent/skills` 0; `skill-descriptions` 14; `omp.real` 0;
  `maxRunningJobs` 3.
- Lane HEAD 89579c7 (round-88 freeze); tip 4df1e80 is an ancestor.

## Findings

1. A binding token built from the path `.omp/agent/skills` would match zero bytes in the host ELF. The reader quote is
   `.agent/skills` / `.agents/skills`. Bind the reader quote, not the path alone.
2. Stale sibling claims about the omp ELF: kumitate PROVINCE.md:20 and its runtime note (`omp.real` wrapper, 18.12.6);
   mori S102 sha pin `85d9daf3…` (host `6737ee24…`); kama `omp:1544771` offsets. Reported only.
3. [INFERENCE] kumitate's probe on this host takes `real-unidentified` and exits 2 (code read, not run).

## Risks

- The sibling `~/.agents/skills` / `.omp/skills` claims share roots with the v2 reader quote. A future cross-lane
  claim could contradict a v2 root row. No edit made.
- No sibling file was edited. Nothing here changes the frozen predicate or the kill rule.
