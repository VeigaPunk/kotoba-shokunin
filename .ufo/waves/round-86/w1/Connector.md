# Connector — round 86 w1 (scoped findings)

Full table: `.ufo/waves/round-86/w1/Connector/overlap.md`. Read-only seat. Base model only: ExecModel's `CANDIDATE_READY` was absent when this was written.

## Findings
1. **Siblings:** no collision with C1. Only kumitate (Kimi loader, the `~/.agents/skills` symlink substrate, and the `skill-descriptions.db` member mode, `PROVINCE.md:16`) and kengaku (`<available_skills>` share of a bench prompt) hit. tameshi, kagi, kama and chousa have 0 hits.
2. **Staged package:** 0 of 87 staged entries mention omp, so nothing contradicts 18.15.0. omp's source **confirms** the cross-vendor `.agents/skills` convention the staged entries describe:
   - `agents.ts`: `var y1 = [".agent", ".agents"]`, walk-up to `repoRoot ?? home`, user home plus the WSL profile.
   - It **extends** them with the singular `.agent/skills`, per-root enable switches, and `cfgSkillsCustomDirectories`.
3. **Assimilation (next round):** `skill-paths-and-precedence.md`, plus an omp row from source in the round-69 precedence table (provider priorities: native 100 … `.agents` 70 … github 30, managed 5). The dedupe direction is not yet located.
4. **considerthese 2026-10-26:** none of #1–#5 is implemented by r86. #3 is half done: the page landed in r85, but the description audit is still open. C1 adds one registry row to `SKILL.md` (#1 and #2 move slightly the wrong way) and re-grounds the 99-char cliff that #3 uses.
5. **no-absorb:** the `~/.agents/skills` provenance and layout, and the `~/.omp/agent` member modes, are kumitate's.

## Connector move (one bounded proposal)
**Evidence:**
- 23 of the 83 base-discovered fixture names sit under two or more omp-read roots (`~/.claude/skills` and `~/.agents/skills`; `omarchy` also under `~/.codex/skills`). All 23 resolve to byte-identical SKILL.md bodies.
- omp gives `.claude` priority 80 and `.agents` priority 70 [INFERENCE: higher wins].
- G4 (`check_omp_catalogue_repro.py:150-152`) matches the *offered* path's root against any located pattern. G2 (`:308`) resolves realpaths.

**Move:** ExecModel's ledger and model should attribute each colliding name to the provider omp ranks first (`.claude/skills` before `.agents/skills`), not to whichever root it scans first. The ledger row for each root should quote that root's own provider string (e.g. `Load skills from .agent/skills and .agents/skills (project walk-up + user home)`, `Load skills from .claude/skills/*/SKILL.md`), so the reviewer can check meaning and not just location.

**Axes:** freshness (the claim's attribution fidelity) +. N is unchanged, because the bodies are identical. No harm to the frozen counter, which stays unedited.

**Risks:**
- Precedence is invisible to the counter while the bodies are identical. A wrong attribution passes G4, so only the reviewer seat can catch it.
- Because `~/.agents/skills/*` are mostly symlinks into `~/Projects/ompskills/.omp/skills`, a realpath-based root in the model would match no `~/.agents/skills` pattern and fail G4. The model must emit the scanned (unresolved) path.

**Verification:** the reviewer re-runs the 23-name collision check, and confirms that omp's dedupe direction is located in the ELF before the attribution is claimed.

The 132 missing names were not found under `~/.claude`, `~/.omp`, `~/.codex` or `~/.config` by a dirname probe (`api-design`, `bengali-nlp`: 0 paths). The remaining candidate roots are the plugin, Skillshare and extension providers. That search is ExecModel's, not this seat's.
