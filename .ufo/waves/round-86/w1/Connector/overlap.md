# Round 86 w1 — Connector overlap scan (read-only)

Seat: Connector. This scan used only read-only reads: `git grep`/`git show` at sibling HEADs, files under `shokuknow/merge/kotoba`, the lane at base `e5d966b`, and python `mmap`+`re` over `/home/vgpnk/.local/bin/omp` (18.15.0, not copied). Nothing was written outside this directory and `../Connector.md`.
ExecModel's `CANDIDATE_READY` was absent when this was written, so every statement here is about the **base** model. This item does not depend on the candidate.

## 1. Sibling lanes: omp skill discovery / catalogue-rendering knowledge

Command, run at each lane's committed HEAD:
`git -C <lane> grep -n -E 'skills>|USER_ROOTS|\.agents/skills|skill-descriptions' HEAD -- SKILL.md 'corpus/knowledge/*'`. I also ran a second sweep for `loadSkills|cfgSkills|skillsCustomDirectories|\.omp/skills|\.claude/skills|\.codex/skills|\.pi/` over SKILL.md, PROVINCE.md and corpus/knowledge.

| lane @HEAD | file:line | what it holds | collision with r86 C1? |
|---|---|---|---|
| kumitate `8e4ea5f6` | `SKILL.md:556` | The **Kimi** resolution order. Kimi user skills are symlinks into `~/Projects/myskills` and `~/.agents/skills` | **no**: this is Kimi's loader, not omp's `<skills>` catalogue |
| kumitate | `corpus/knowledge/kimi-skills-plugins.md:465,481,486` | Kimi scans `~/.kimi-code/skills` plus `~/.agents/skills` as User roots, merges them by name, and the kimi-code root wins | **no** (Kimi). It is adjacent: it is the same `~/.agents/skills` directory that C1's ledger will cite for omp |
| kumitate | `corpus/knowledge/kimi-skills-plugins.md:513-518` | "OMP skills root shares names with the Kimi root… `~/.agents/skills/*` mostly symlinks into `ompskills/.omp/skills/*` … → **OMP/host-plane lane**" (a cross-domain item, "report, do not absorb") | **no** (it routes away and makes no omp loader claim). It is relevant to C1's G2, see Risks |
| kumitate | `corpus/knowledge/kimi-modes-machinery.md:183-186,516,527` | Byte sizes and symlink targets of `~/.agents/skills/{swarm,tower}` | **no** (substrate facts, not a discovery rule) |
| kumitate | `corpus/knowledge/omp-agent-root.md:36` (also `:102`, `:146`) | `skill-descriptions.db` is a depth-1 member of `~/.omp/agent`, mode 0600, `dirs.ts lines 984-987` (v18.12.6) | **no**. kumitate owns the member's **name, kind and mode** (readdir+lstat only, `PROVINCE.md:16`). C1's counter reads the db's **rows** inside its fixture. Different facets of the same file, and no claim in common |
| kumitate | `PROVINCE.md:20` | Owns the "OMP harness contract (task batch, agent hub, **agent discovery**)" | **no**. It covers agent discovery, not skill discovery, and `PROVINCE.md:32` routes "Prompt and skill craft → kotoba" |
| kengaku `88651a72` | `corpus/knowledge/bench-arena-round7-scaffold-ablation.md:19` | An `<available_skills>` catalogue accounts for 94 % of a ~12K-char bench system message (18 skills) | **no**. This is a capability-effect measurement on a bench scaffold, not omp's render rule |
| tameshi `d10a9c66` | — | 0 hits on either sweep | no |
| kagi `f6d93c5b` | — | 0 hits | no |
| kama `3ff23da3` | — | 0 hits | no |
| chousa `9fcfb70b` | — | 0 hits | no |

Result: no sibling lane holds omp's **skill** discovery roots or the `<skills>` render rule (`k=100`, `E=40`, `T=160`, `_=12`, key). C1 collides with nothing. The one adjacency is kumitate's pair of facts: the `~/.agents/skills` symlink substrate and the `skill-descriptions.db` member mode.

## 2. Staged package `shokuknow/merge/kotoba/` (read-only)

`grep -l -w -i -E 'omp|oh-my-pi'` over all 87 staged knowledge files matches **0 files**. No staged entry asserts anything about **omp's** roots, so there is nothing for 18.15.0 to *contradict*. The entries that bear on client discovery roots in general are below. All 4 are absent from the lane at `e5d966b` (`git ls-tree` count 0).

| staged entry:line | assertion | omp 18.15.0 source (ELF) |
|---|---|---|
| `client-frontmatter-and-discovery-divergence.md:41-51` | "the cross-vendor root is the common denominator". Deep Code interleaves native and `.agents/skills` ranks, Junie can switch the default roots off, Kiro has no `.agents` root | **Confirms and extends** to omp. `packages/coding-agent/src/discovery/agents.ts`: `var y1 = [".agent", ".agents"];` and the provider `"Load skills from .agent/skills and .agents/skills (project walk-up + user home)"` (ELF off. 173866306). `V9` walks up from cwd to `repoRoot ?? home` and skips `home` itself. `z9` takes the user home, plus the WSL `%USERPROFILE%`. Like Junie, omp has off switches: `cfgSkillsEnableAgentsProject` / `cfgSkillsEnableAgentsUser` (settings export, off. 192158351) |
| `client-surface-census-extension.md:40-45` | Qwen Code reads `~/.agents/skills/` and `.agents/skills/` without configuration and has a `skills.directories` setting | **Analogue confirmed**. omp has the same pair and also `cfgSkillsCustomDirectories` (off. 192158351). omp additionally reads the singular `.agent/skills`, which no staged entry records |
| `skill-paths-and-precedence.md:55-66` | Four precedence rules. "the one that has looked at it solved it by preferring its own directory" | **Consistent** [INFERENCE on direction]. omp registers 11 skill providers with priorities: native `"Native OMP configuration from ~/.omp and .omp/"` `Ko = 100`, Skillshare `95`, extension sub-discovery `90`, `.claude/skills` `cl = 80`, agent-plugins `75`, `.agent(s)/skills` `Vu = 70`, Claude marketplace `70`, codex `70`, opencode `55`, `.github/skills` `30`, managed-skills `5`. That makes omp's own root the highest. I did **not** locate the dedupe code, so "higher priority wins" is unverified |
| `spec-script-craft-rules.md:24-32`, `client-loading-and-distribution-models.md:13,57` | The spec teaches `.agents/skills/` as the cross-client default | Confirmed for omp (above). omp also reads the vendor roots `.claude`, `.codex`, `.opencode` and `.github`, so it is a multi-vendor reader, not only an `.agents` reader |

**Assimilation candidate (next round, not r86):** stage `skill-paths-and-precedence.md` and add **omp as a source-located precedence row** to the lane's round-69 table (`corpus/knowledge/skill-name-precedence-round69.md`, five doc-sourced clients, no omp row; `SKILL.md:295-298` box "precedence order on four of the five cited clients"). Why:
- omp is the only client the lane can read *from source*. Its provider-priority list above is tier-A, whereas the other five rows are documentation.
- On this host, 23 fixture names exist under more than one omp-read root (`~/.claude/skills` with `~/.agents/skills`; `omarchy` also under `~/.codex/skills`), so a live collision case exists.

Why not this round:
- The frozen C1 surface excludes precedence.
- All 23 colliding copies are byte-identical (resolved realpath bodies, 23 identical, 0 differing), so precedence cannot move C1's N in either direction.
- The dedupe direction is not yet source-located.

## 3. considerthese `2026-10-26.md`: proposals still unimplemented at base `e5d966b`

| # | proposal | status at base (evidence) | does C1 change it? |
|---|---|---|---|
| 1 | Byte ceiling (≤70 KB) and a 200-char max-line check | **open**. `SKILL.md` is 599 lines, 84,917 B (larger than the 78,569 B the note complained about), with 136 lines over 200 chars. No byte or line-length gate exists, only `--max-lines` (`verify_skill_checklist.py:2750`) | Not implemented by C1. The plan's no-harm row expects `check_gate_registry` 66→67, which **adds** a registry row to `SKILL.md` and moves #1 slightly the wrong way |
| 2 | Move `## Gate registry` to `verifiers/REGISTRY.md` | **open**. The heading is still at `SKILL.md:448`, `check_gate_registry.py:21,354` still reads SKILL.md, and no `REGISTRY.md` exists. Plan `round-86.md:113-114`: blocked on L0 `round-73` | Not implemented. The +1 row grows the section the proposal wants moved |
| 3 | Land `spec-description-trigger-discipline.md`, then audit kotoba's own description | **half**. The page's source landed as `corpus/knowledge/description-trigger-discipline-round85.md` (S213, r85). The audit/fix is **open**: the description is 1,023 of 1,024 chars and its first sentence is 153 chars against the 99-char render cliff | Not changed. C1 re-derives the render cliff from the 18.15.0 source (`k=100`), so it re-confirms the cliff #3 measures against, without touching the description |
| 4 | Close as "provisional" when the falsify wave is not dispatched | **open**. No such rule found (`git grep` for "provisional until" / "closes as provisional" in SCORECARD/PROTOCOL/SKILL: 0 hits) | Not changed. r86 runs strict attack seats, sentinel and revenger in w1 |
| 5 | Per-round evidence budget | **open**. `.ufo` is 331M (the note recorded 203 MB). No cap rule found | Not changed. The C1 fixture/receipts add a little |

Confirmed: r86 implements **none** of proposals 1–5. C1 nudges #1 and #2 by one registry row in the wrong direction, and it re-grounds the cliff that #3's audit would use.

## 4. no-absorb

**no-absorb:** kotoba must not claim the `~/.omp/agent` member inventory, or the layout and symlink provenance of `~/.agents/skills` → `ompskills/.omp/skills`. kumitate owns both (`PROVINCE.md:16`; `kimi-skills-plugins.md:513-518` routes the `.omp/skills` layout to the OMP/host-plane owner). C1's ledger may cite `~/.agents/skills` as a root **omp reads**, quoting the ELF. It must not assert who populates that directory, what links into it, or `skill-descriptions.db`'s mode or permissions.
