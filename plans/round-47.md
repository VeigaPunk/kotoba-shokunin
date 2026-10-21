# kotoba round 47 — plan (L1 MoriR22R, reused idle agent; Main spawn job-capped)

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (branch `master`, jj-colocated lane).
Before measurements: `.ufo/waves/round-47/before/SUMMARY.md` (raw outputs beside it).
Frozen substrate snapshot (read-only): `/fast/scratch/kotoba-r47/shared/` — `bin/omp-18.12.5`
(sha256 `fdbc8136…`), `bin/opencode-1.19.3` (sha256 `179ca421…`), `strings -n 4` dumps, `SHA256SUMS`.

## Starting point

SCORECARD `## planned` → "Next: round 47" (C1 freshness re-pin, C2 operability description
XML-tag rule, C3 capability sources curation). The planned before-values went stale before the
round began: omp moved 18.12.3 → 18.12.5 (sha `fdbc8136…`, mtime 2026-10-21 03:30 -03) and the
pinned opencode path `/home/vgpnk/.opencode/bin/opencode` no longer exists — opencode is now an
npx wrapper (`~/.local/bin/opencode` → `opencode-ai` 1.19.3, ELF in the npx cache). Planned C3
(capability) is replaced by a calibration claim on two gates red at BASE; the SOURCES workflow
still runs as the frontier step.

## Claims (distinct axes, causally separable)

- **C1 — freshness (lowest non-retired axis, 8.0; tie with adjacency):** re-derive the
  instruction-surface extraction and re-pin the substrate for omp 18.12.5 and opencode 1.19.3.
  Before: `verify_surfaces.py` exit 2 (opencode binary missing; with the 1.19.3 binary passed
  explicitly 4 PASS / 3 FAIL — omp vacuity 0/8 loader classes, OC-1/OC-4/OC-6 match nothing);
  `check_substrate_pins.py` exit 2, 3/3 pins failed. After target: surfaces 7/7 exit 0 and pins
  3/3 exit 0 at the default resolution, with extraction rules re-derived (not copied) and every
  class that no longer exists re-verdicted with its sweep, never silently dropped (Q09, Q14).
  Count: `python3 -B verifiers/verify_surfaces.py --json`; `python3 -B verifiers/check_substrate_pins.py`.
- **C2 — operability (8.5), sourced on S003 re-opened this round:** a semantic frontmatter check
  — the `description` value carries no XML tag — lands in `verifiers/verify_skill_checklist.py`
  with discriminating fixtures, and this lane's own description loses its `<skills>` token.
  Before: `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` → 1, no check. After: 0, live
  check PASS, `--self-test` rejects the planted-tag mutation and keeps every tag-free control
  green (Q05, Q18).
- **C3 — calibration (8.5):** records match repo state — the governance citation gate learns a
  pinned, fail-closed erratum registry for recorded absences (LOG.md:2111 cites a runner whose
  absence the line itself records), and the corpus index covers the integrator-written
  `corpus/lessons/round-46-verifier-spotcheck.md`. Before: checklist `--json` 9 PASS / 1 FAIL;
  `verify_corpus_integrity.py --json` 2 DRIFT; `verify_corpus_independent.py --json` 1 DRIFT.
  After: 10/10 (11/11 with C2), 0 DRIFT, 0 DRIFT.

## Not claimed (named)

- `verify_harness_claims.py` 21/28 at BASE: three host skills appeared (`create-toolset`,
  `unreal-mcp`, `unreal-skill`); cache rows absent for them. Root-caused this round, recorded as
  Q09 debt unless a re-derivation (not a copy of observed values) is shown.
- r46 spot-check residuals (mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`,
  payload-selectable committed scope-outs, the printed C1 counting command exit 2): carried; each
  gets a why-not line in the report.

## Waves

Wave 1 build (64–100) → wave 2 falsify (64–100), total ≤ 200. L1 holds the planner seat and is
the sole production integrator; seats write reports/patches only.

## Replacement coordinator note (KotobaR47-2, after the host crash)

The coordinator above died with the host session while wave 1 ran. The replacement kept
the three claims and their after-targets unchanged and integrated from the 72 wave-1
reports that survived (20 seats died without a report; named in `LOG.md` § Round 47). One
addition inside C3's scope: the fault harness planter fix (`ExecFaultBaseline`), because
the corpus index move otherwise leaves `verifiers/fault_injection_corpus.sh` red on a
pre-existing planter defect. A post-crash falsification wave (wave 2) attacks the landed
tree.
