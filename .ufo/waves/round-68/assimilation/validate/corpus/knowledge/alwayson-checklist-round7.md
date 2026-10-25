# Always-on constraint-file checklist + self-audit results — round 7

Sourced 2026-09-28 (round 7), L2 lanes `PlanAgentsChecklist` (drafted the
AGENTS.md checklist, applied to 7 files) and `RevSkillAudit` (applied the
13-item trigger-fidelity checklist verbatim to kotoba's own SKILL.md).
Lane artifacts: `/tmp/kotoba-r7/planner-agents-checklist.md`,
`/tmp/kotoba-r7/reviewer-skill.md`.

## AGENTS.md fidelity checklist (AC- items, drafted + applied)

1. **Constraint-only content** — durable rules/prohibitions/boundaries; no
   history, status, rationale prose.
2. **No how-to procedures** — no multi-step sequences or command recipes; a
   single durable required outcome may remain.
3. **No trigger/dispatch material** — no routing or activation conditions.
4. **No dated/transient text** — dates, expiring facts → status files.
5. **Terse imperative style** — short independently actionable rules.
6. **Template-family consistency** — copied families keep identical shared
   body; per-file substitutions only where declared (e.g. repo-name heading).
7. **Single owner for rule-file names** — check repo root for both
   `AGENTS.md` + `CLAUDE.md`; one canonical owner or explicit redirect.
8. **Justified size bound** — local default = the 5-line repo template; any
   expansion must be distinct constraints needed every session.

## Application: 6/6 shokunin AGENTS.md PASS; host file FAILS

| File | Result |
|---|---|
| `shokunin/*-shokunin/AGENTS.md` ×6 | PASS (P* on AC-2: the LOG-append obligation is a required outcome, not a procedure) |
| `~/.agents/AGENTS.md` (75 lines, 3781 B) | **FAIL** AC-1/2/4/5: carries procedures (`Load and obey ~/.agents/godspeed-core/directive.md` :18; `Run the-janitor tac-check` :55), dated text (:48,:51 = 2026-09-06 attestations), narrative posture paragraphs |

**Correction landed in SKILL.md** from this audit: the round-1 claim
"host-level `~/.agents/AGENTS.md` … zero procedures" was wrong — the file
carries two procedures and dated attestations. Also corrected: the six repo
files are *shape*-identical, not byte-identical (six distinct md5s; shared
body under differing first-line repo names — proven by hashing lines 2+).

## Self-audit: 13-item checklist on this repo's SKILL.md

**7/13 clean, 4 fails, 1 N/A, 1 ambiguous.** Fails resolved same-round:

| Item | Verdict | Disposition |
|---|---|---|
| 4 sibling arbitration | FAIL (strict) | Cured: `description` now names the 5 sibling `*-shokunin` skills + arbitration note. Also exposed a blind spot: siblings aren't in omp discovery roots at all (see `render-mechanism-round7.md`). |
| 6 fail-closed prereqs | FAIL (strict) | Partially cured: declared `metadata.requires.bins` (md5sum/diff/find are recipes *inside* evidence prose — added citation-form carve-out to the item). |
| 8 runnable commands | FAIL | Cured: the `diff kake-round-4.md kasegi-round-4.md` inline command now names its base dir. |
| 10 citation bases | FAIL | Cured: bare prompt filenames and `opencode.json` refs now carry their roots. |
| 9 failure signatures | AMBIGUOUS | Checklist wording fixed: "failure claim" now defined (any warning/dominant-failure label/causal claim needs a signature *or* a design-guidance marker). |

Meta-wording adopted: item 4 now requires naming concrete siblings **or**
stating `N/A — no overlapping sibling exists`.

## Standing cross-domain queue (sentinel re-verify, round 7)

All unchanged since round 5/6 (`/tmp/kotoba-r7/sentinel-siblings.md`):
- 5/5 sibling SKILL.md descriptions still `Domain specialist — scopes X`
  (0/5 triggers, 0/5 anti-triggers, 0/5 arbitration clauses).
- `ufo.md`: `name:` absent + `cascade_note` now **60 days** stale
  (`until 2026-08-29`, line 7).
- `mutation-tester.md` godspeed preamble still doubled (:15,:41).
- `scout.md:38` `aaron` still absent from PATH.
- Mint-template producer: **no owner found** — nothing in MANIFEST.json,
  scripts/, or `.ufo/waves/round-1.json` produces the SKILL description
  template; routing fix requires integrator assignment (connector lane).

## Drift table (critic re-count, round 7)

| Claim | Old | Now | Verdict |
|---|---|---|---|
| godspeed preamble in agent defs | 14/18 | 14/18 (md5 c91c0d66…) | stable |
| mutation-tester double preamble | 2 | 2 | stable |
| `NOT ` negative routing | 11/18 | 11/18 | stable |
| CLAUDE.md census | 16 (5/1/10) | **18 (5/1/12)** | drifted +2 vendored |
| loader strings opencode/omp | 9/17 | 9/17 | stable |
| compression warns | 10191 | **10681** | drifted +490 (live log) |
| opencode.db skill histogram | 415/11/g239 | same | stable |
| session_init records | 3837 | **3911** | drifted +74 |
