# Round 69 — plan (hyaku run 6, lane kotoba, attempt 1)

Frozen before any wave seat scored any claim. Base lane tip (branch `master`):
`a5f7459f99bb27bf697e9438362e75ac5833eca8` (`jj-lane.sh state` → `local=a5f7459f… remote=a5f7459f…
ahead=0 behind=0`; the tip is the r68 closure's spot-check commit, authored `protocol-shokunin`).

Round shape: **two v1 waves** (policy `scripts/hyaku/ufo-wave-policy.json`, band 32–64): wave 1
build + first falsifiers; wave 2 falsify only if wave 1 yields ≥32 distinct attack items, else one
residual `task` call of ≤8 reviewer/critic seats. The L1 holds the canonical §3 planner seat (the
validator rejects `planner`); the planning data-walk rides the wave-1 connector and scout items.

**Inherited state.** `git status --porcelain` lists 24 lane-authored round-68 wave paths (10
modified seat logs/drafts, 14 untracked seat reports, drafts, controls and the seat-results file)
— routed defect R68-7, worked by C2. One of them, `.ufo/waves/round-68/w1/controls/c2falsify-clone/`,
is a 269 MB git clone (it carries its own `.git`): it is control scratch, and it is the M109 class
(an untracked working-tree artefact left undisclosed) recurring one round after its capture.
The watchdog log shows no `lane-dead-no-report kotoba round=69` line: no earlier attempt.

## Claim declarations (this round declares 3)

### C1 — depth (the lane's lowest owned axis), sourced, assimilation — skill name-collision precedence

**Axis:** `depth` (owned, 9). **Surface:** what clients document about a skill NAME COLLISION —
which of two same-named skills wins, or that names must be unique. The lane holds no such ground:
`corpus/knowledge/` has no precedence entry, the coverage map has no row for it, and
`corpus/README.md` § Coverage map's round-58 note leaves "precedence between a command and a
same-named skill" unheld. Theme taken from `/home/vgpnk/Projects/shokuknow/merge/kotoba/`
(staged `skill-paths-and-precedence.md` and `skill-source-precedence-round7.md`, folded into one
lane entry per the package's adopt checklist item 6), re-grounded in-round under CORPUS.md rule 1.

**Frozen predicate (the same sentence in this plan, in the counter's docstring and in the receipt):**

```
python3 -B verifiers/check_skill_precedence.py --rev <rev>  ->  prints "skill precedence backed N of 5", exit 0 when N == 5
```

Conjuncts that keep it non-vacuous: at the base it prints `skill precedence backed 0 of 5`, exit 1
(`controls/C1-base.txt`); the junk-entry control (provenance trio, a quote and an index row but no
`source:` lines) prints `0 of 5`, exit 1 (`controls/C1-junk-control.txt`); `--self-test` kills one
broken world per conjunct; `--fetch` finds each located quote on its live page.

**Counter semantics (frozen with this plan; sha256 recorded in the plan commit's receipt).** For
`corpus/knowledge/skill-name-precedence-round69.md`: the entry opens with its provenance trio
(Q12) naming exactly five ids; each id resolves to an 11-cell `mined` row opened `2026-10-25`
whose `used-by` names the entry and whose `source` cell is in the entry's `source:` line; each row's
anchor carries a ≤25-word located quote that the entry carries; exactly one per-client table row
per id carries that quote with a client and a rule cell; the five rows name five distinct clients;
the entry is indexed in the coverage map. A missing entry is a content verdict (exit 1); an
unreadable environment is exit 2.

**The five clients (L1 data-walk at round start, `/tmp` fetches, 2026-10-25):** Roo Code
(`docs.roocode.com/features/skills`: native root "higher priority" than the shared root; project
over global), Amp (`ampcode.com/docs/customize/skills`: "Local skills mask repository skills with
the same name"), Deep Code (`deepcode.vegamo.cn/en/docs/configuration/agent-skills`: "only the
highest-priority one is kept"), Junie (`junie.jetbrains.com/docs/agent-skills.html`: project-level
takes precedence, user-level ignored), opencode (`opencode.ai/docs/skills`: "Ensure skill names are
unique across all locations" — a uniqueness rule, not a precedence rule). Wave-1 scouts re-open
each; a source whose rule does not survive re-opening is a miss, never a substitution after data.

**Bound (named before data).** Documentary evidence, not observed client behaviour; the counter
reads the measured revision's own bytes (Q33). No band move claimed; depth stays 9 pending the
closure.

### C2 — consistency (calibration sub-axis) — the eight routed r68 repairs

**Axis:** `consistency` (owned, 10). **Routed cause:** `corpus/lessons/round-68-verifier-spotcheck.md`
§ Routed defects R68-1 … R68-8 (hyaku closure; never edited by the lane).

**Frozen predicate (three conjuncts):**

```
python3 -B verifiers/check_r68_routed_repairs.py --rev <rev>  ->  prints "r68 routed defects closed 8 of 8", exit 0
python3 -B verifiers/verify_corpus_integrity.py               ->  prints "9/9 checks pass", exit 0
python3 -B verifiers/verify_corpus_independent.py --json      ->  exit 0
```

**Before (base, `controls/C2-base.txt`, `controls/C2-base-integrity.txt`):** `r68 routed defects
closed 0 of 8`, exit 1; the primary gate `6/9 checks pass`, exit 1 (`tracked_files 125≠124`,
`unindexed 1`, `report_total 87≠85`). Cheapest control — commit the round-68 wave paths and one
index row, nothing else — stays `0 of 8`, exit 1 (`controls/C2-cheap-control.txt`).

**Repairs, one per defect (D-numbers are the counter's).** D1/R68-1: re-capture the nine r68
receipts under `.ufo/waves/round-69/recapture/` with a printed `measured-rev:` and `exit=` line,
run in a `/tmp` shared clone at the revision each measures. D2/R68-2: the self-test re-capture at
`9b72edb0`. D3/R68-3: `check_r67_routed_repairs.py` classifies a missing records file as a content
verdict AND stops running `git checkout <rev> -- corpus verifiers` in the lane (it wrote the lane's
index and working tree; found at round start) — measured from a sandbox at the r68 base (`0 of 4`,
exit 1) and tip (`4 of 4`, exit 0), with the base receipt committed. D4/R68-4: the round-69 Gate
names the removed bytes (S200 `<code>`, S202 `**`). D5/R68-5: a supersede row for S201 quoting the
approval sentence, named by the r68 entry in an appended amendment. D6/R68-6: mistake row + a new
`QUALITY.md` criterion. D7/R68-7: each of the 24 paths committed, or dispositioned as removed (the
clone). D8/R68-8: the coverage-map row and a baseline re-record taken from the gate's own
`--no-baseline --json` measurement.

**Bound.** D4 and D6 are presence floors (disclosed in the counter); D1's receipts are re-runs of
recorded commands, and their faithfulness rests on the recorded command lines.

### C3 — coverage (advisory, 8.5) — the r67 and r68 areas enter `PROVINCE.md` § Core

**Axis:** `coverage`. **Surface:** `PROVINCE.md` § Core, the list of ground the lane governs. The
r68 closure: "`PROVINCE.md` § Core is untouched this round (carried to 69)"; the r67 authority
ladder and the r68 client trust gates sit in `corpus/knowledge/` with counters but are not named in
§ Core.

**Frozen predicate:**

```
python3 -B verifiers/check_province_core.py --rev <rev>  ->  prints "province core rows 2 of 2", exit 0
```

Base `0 of 2`, exit 1 (`controls/C3-base.txt`); cheapest control — Core bullets naming only the
entry paths — `0 of 2`, exit 1 (`controls/C3-cheap-control.txt`). The counter requires § Frontier
and § Adjacent byte-identical to the base. **Causal separability:** C3 counts only the r67/r68
areas, which exist at the base; it does not depend on C1 or C2.

## Frontier step (§2b)

Curate `corpus/SOURCES.md` (rows only after opening this round; Gate records URL, access date,
≤25-word located quote); census before (`controls/census-before.txt`, exit 0, 16 W04) and after;
mine ≥1 mistake into `corpus/lessons/round-69.md` § Mistakes (candidates at round start: the R68-6
wrong refusal reason; the r67 counter's git write in the lane; the 269 MB clone recurrence of M109);
C1 is the sourced claim.

## Item 10 — assimilation

One theme (skill name-collision precedence), one lane entry folded from two staged entries.
Collision check run at round start with the 0–3-space pattern: 128 registry ids, 188 staged ids,
0 collisions; guard proved non-vacuous (`assimilation/guard-proof/`: an indented `  | S203 |` row
collides under the 0–3-space pattern, 0 under the column-zero pattern). Adopted ids continue the
lane registry from S203; each staged row is re-pointed by document (URL), never by arithmetic, and
the renumber map lands in the lesson. Quarantine slice (13 rows, `assimilation/quarantine-slice`):
the register's `S185` (Roo Code, quote `Skill locations`) and `S172` (Junie) are this theme's rows
and are hand-checked this round before any Roo/Junie row is appended. Scratch transform +
`sources-census.sh validate --file` exit 0 before the first registry append. ≥1 admit and ≥1
reject recorded. considerthese: at most one still-unimplemented proposal from
`considerthese/2026-10-24.md`.

## Round mechanics

Lane commits only through `scripts/hyaku/jj-lane.sh`; report last through
`scripts/hyaku/fleet-commit.sh --as kotoba`. Seats never mutate the fleet repo, a sibling lane, the
lane's jj state or Git index; seat writes stay under `.ufo/waves/round-69/`. Tool installs only
under `/home/vgpnk/.omp/agent/RULES.md`; all pacman transactions are paused host-wide.
