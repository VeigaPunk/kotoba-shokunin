# Kb80S09SkillRule — seat report (kotoba round 80, w1)

Date 2026-10-27. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Leaf seat, no subagents, no background jobs.
Freeze discipline: drafts only; the L1 integrates and is the only committer. Nothing of mine is applied to the lane.

## Behavior

Produced the three things the seat names:

1. **Author-facing rule line** for `allowed-tools` — one physical line, 920 chars, naming all six surfaces
   (Open specification, Claude Code, Factory, Microsoft Agent Framework, pi, Mistral Vibe), in the round-74 body-craft
   register (rule first, authorities inline with `S###` ids, action last), carrying the entry path
   `corpus/knowledge/allowed-tools-surfaces-round80.md`, and stating the four assigned readings plus the consequence:
   *"a skill that does is wrong on at least one client"*.
2. **Gate-registry row** for `verifiers/check_allowed_tools.py` — one line, 1373 chars, 8 cells, kind `gate`,
   `0=clean, 1=failed, 2=could-not-evaluate`, `--self-test`, pinned values `in-file SELF_SHA` +
   `.ufo/waves/round-79/snapshots/MANIFEST.sha256`, owner `kotoba`, describing the round-80 counter's headline
   (`allowed-tools surfaces documented N of 6`), its generator-world score (`generator world: M of 6`, Q71/Q74) and the
   exit predicate (N == 6 plus the tree conjuncts).
3. **Placement rationale** — `## Frontmatter craft — the trigger surface`, one blank line + the rule line after the
   `Portability floor` paragraph (base line 162), with four rejected sections argued in the deliverable.

Drafted in a scratch clone, measured there, and transcribed into the deliverable; the deliverable's two paste blocks
re-hash to the exact bytes measured in the clone (920-char rule `6468c797…`, 1373-char row `4bf7b71b…`).

## Gates I ran (each verdict is the command's own exit status, never a pipeline's)

| command (from the fixture clone at the base bytes + my two blocks) | value | exit |
|---|---|---|
| `python3 -B verifiers/check_gate_registry.py --rev HEAD --json` | `conformant 61 of 63; phantom 0`; my row `conformant true, why []` | 1 |
| `… --rev HEAD~1` (pristine base) | `conformant 60 of 62; phantom 0`; same two failures | 1 |
| `python3 -B verifiers/verify_skill_checklist.py --repo . --check trigger.line_budget` | `PASS … 593 lines within budget 600` | (in run 4) |
| `… --check trigger.citation_resolves` (entry stub present) | only `line 583: '../.ufo/reports/round-7/kotoba.md'` unresolved | 1 |
| `python3 -B verifiers/check_cn_vendor_surfaces.py --rev HEAD` | `4 of 4`; `registry home ok` | 0 |
| `python3 -B verifiers/check_spec_craft.py --rev HEAD` and `--rev HEAD~1` | `0 of 3`, identical both revs (`SOURCES.md` census conjunct) | 1 |
| conjunct-(g) harness (`skill_rule_ok`, `registry_home_ok`, 5 negative controls) | rule `True`, row `True`, 6 surfaces, 8 cells; all 5 controls `False` | 0 |

The registry delta is exactly one conformant row and one lane verifier; the two remaining failures are
`check_desc_craft.py` and `check_r75_routed_repairs.py` — the two rows `Kb79E01Registry.patch` carries — both at base
and at the fixture tip, so my row moved nothing they own.

Line budget: base 590 → fixture 593 (+2 rule line and its blank, +1 row); with E01's two rows the file is 595 ≤ 600.

## Touched surfaces

- Lane: **none**. Wrote only `.ufo/waves/round-80/build/Kb80S09SkillRule.md`,
  `.ufo/waves/round-80/build/Kb80S09SkillRule.patch`, `.ufo/waves/round-80/build/Kb80S09SkillRule-receipts.txt` and this
  report. No lane git index, jj state, tracked file, `SKILL.md`/`PROVINCE.md`/`verifiers/` edit.
- Scratch: `$S/clone` (git clone --shared of the lane at base, own user.name/email, asserted toplevel), `$S/tmp`,
  `$S/harness.py`; removed before yielding.
- Fleet root, sibling lanes, `/home/vgpnk/Projects/shokuknow`: untouched. No pacman, no network fetch, no tool install.

## Out of scope (other seats' deliverables, not mine)

- `corpus/knowledge/allowed-tools-surfaces-round80.md` — the entry (E09/E08). Both my pointers resolve only once it
  lands; that is the conjunct-(g) target, not a row defect.
- `verifiers/check_allowed_tools.py` round-80 bytes (E07) and the L1's `SELF_SHA` freeze.
- The three registry rows as a patch set (E01) — my row is a fallback, and the lane must hold exactly one.
- `PROVINCE.md` § Core bullet (`Kb80S10Province`), `corpus/README.md` coverage row (`Kb80S08ReadmeRows`), SOURCES
  census rows (`Kb80S16CensusLog`), `.ufo/waves/round-79/snapshots/MANIFEST.sha256` itself (entry seats).
- C1 (tip battery, erratum E5, the five repairs) and every claim after-value: not measured, not scored here.

## Findings

1. **The field is new to `SKILL.md`.** `grep -c 'allowed-tools' <base>:SKILL.md` → `0`, so both blocks are additions;
   nothing existing is reworded, and the compiler reads a subject list that had no entry.
2. **One physical line is the right carrier.** Conjunct (g) is a line predicate (`ENTRY in line and
   surfaces_named(line) >= 3`); a per-client table would cost 9 lines and still need the entry path on one row.
3. **The row is conformant, and the pin is load-bearing.** `.ufo/waves/round-79/snapshots/MANIFEST.sha256` does not
   exist at base `398cbe1` (the six `S22x` snapshots were added by the freeze commit `c2f69d4`); the entry seats must
   commit the manifest with the entry. Without it this row reds `check_gate_registry.py` ("pinned path … does not
   exist") **and** the counter's own `MANIFEST` constant is dead — the two must land in one commit.
4. **A blank line silently detaches a table row.** My first insertion left a blank line above the row; `registry_rows()`
   ends the table at the first empty line, so the row would have vanished from the gate's view while looking right to a
   reader. Fixed and re-verified (row is now directly after the `check_sibling_reread` row). Integration check:
   `grep -c '^| \`verifiers/check_allowed_tools.py\`' SKILL.md` must print `1`, and the row must have no blank line
   above it.
5. **One row only.** `Kb79E01Registry.patch` carries two rows, **not** the third the plan describes; `Kb80E01Registry`
   had published nothing at draft time (build dir absent, then no `Kb80E01*` file; seat status "running"), so I derived
   the row myself from the plan's § C2 freeze and the r79 draft counter. If E01's patch lands with a
   `check_allowed_tools.py` row, **keep E01's and drop mine** — two rows read `registry rows naming it: 2 (need 1)`.
6. **The published round-80 counter is the r79 draft, byte for byte.** `.ufo/waves/round-80/build/check_allowed_tools.py`
   ≡ `.ufo/waves/round-79/build/check_allowed_tools.py` (sha256 `74e067cc…`): `ENTRY` still points at the round-79
   entry, `TARGET = 5`, `BASE_REV = b10bcbc6…`, headline `allowed-tools surfaces backed N of 6`, world line
   `script-only world: M of 6`. On my blocks those bytes read `skill_rule_ok → False` (wrong entry path) and
   `registry_home_ok → True`; rebound in memory to `…round80.md`, `True` with 6 surfaces and 8 cells. Conjunct (g)
   therefore passes **only once E07 republishes** with the round-80 `ENTRY`, the `documented` / `generator world:`
   labels and an exit predicate at `N == 6` — otherwise my row's description cell describes the plan, not the bytes
   (freshness defect, and E07's, not mine to repair).
7. **My texts carry no commit token, so the grammar class cannot reach them.** Sweep over all four artifacts:
   `7bb48f21` = 0 hits and `owner/repo@<hex>` = 0 hits in every file. The hex-citation hazard `Kb80E10Battery` reports
   lives in the C2 entry (`allowed-tools-surfaces-round80.md`, the mistral-vibe commit sentence) — E09's line, not my
   row or rule line, and my patch adds 0 instrument lines (3 `SKILL.md` lines), so it spends none of the 21-line
   grammar budget the battery's arithmetic leaves.
8. **`check_spec_craft.py` is red in a shared clone at both revs** (`0 of 3`, `corpus/SOURCES.md is not
   census-conformant at HEAD` and at `HEAD~1`). Identical before and after my lines → environmental/pre-existing, not
   caused by and not fixed by this seat.
9. **Citation resolution isolates to the entry.** With the entry stubbed, the only unresolved pointer in `SKILL.md` is
   the base line 583 `../.ufo/reports/round-7/kotoba.md` (a `../` hop needing the fleet root, absent under scratch
   root). Every pointer I add — the entry path twice and the manifest once — resolves in that run.
10. **Own defect, reported:** my first base extraction wrote `/fast/scratch/skill-base.md`, outside my scratch dir,
   because a shell `||` fallback fired after the redirect succeeded. Removed immediately (`ls` → absent); no tracked,
   lane or fleet file implicated. No other write left my assigned paths.

## Artifact paths

- `.ufo/waves/round-80/build/Kb80S09SkillRule.md` — deliverable: both paste blocks, clause→snapshot-line table,
  measured conformance, E01 diff rule, placement rationale, landing constraints, limits.
- `.ufo/waves/round-80/build/Kb80S09SkillRule.patch` — fallback only: `SKILL.md` +3 lines (two hunks), sha256
  `9ad16e05cf43460c230ee7acf5d7f86fc43c8f1c5182df6595060fdd53906a4c`. Do not apply alongside E01's row.
- `.ufo/waves/round-80/build/Kb80S09SkillRule-receipts.txt` — commands, exit statuses, selected output, snapshot digests.
- `.ufo/waves/round-80/w1/Kb80S09SkillRule.md` — this report.

VERDICT: rule line (920 chars, 6 surfaces, entry-cited) and the single `check_allowed_tools.py` gate row (8 cells, 1373 chars) are drafted, byte-verified in a base clone, and pass conjunct (g) plus `check_gate_registry.py` (61 of 63, phantom 0, five negative controls fail as required); placed in `## Frontmatter craft`; E01's duplicate-row rule and the round-79 `MANIFEST.sha256` landing constraint are named.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S09SkillRule.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S09SkillRule.patch /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S09SkillRule-receipts.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80S09SkillRule.md
