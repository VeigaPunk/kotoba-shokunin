# ConnClaimOverlap — round-72 wave-1 cross-claim contention map

**Verdict:** C1 (depth), C2 (freshness) and C3 (consistency) are pairwise separable for verification **except** that C3's landing is causally downstream of C1 and C2 in one place (gate-registry rows naming the two new counters), and C3 owns the *last-writer* re-record of the shared corpus numbers. Recommended landing order: **C1 → C2 → C3**, each landing self-contained on the shared numbers (see table). One non-separable pair is demonstrated by command below; all other pairs verify on a tree lacking the other claim.

## Shared files / numbers the three landings touch

| File | C1 (depth) | C2 (freshness) | C3 (consistency) |
|---|---|---|---|
| `SKILL.md` | adds 4 boxes in § Trigger-fidelity checklist (currently 15 boxes, `verifiers/checklist-baseline.json` section count; SKILL.md:253 heading) + frees lines; must update the count sentence at SKILL.md:259 ("Eight of the fifteen boxes") | — | adds 5 `## Gate registry` rows (SKILL.md:464; 51 rows now, universe 53 → 56) |
| `SKILL.md` memory budget | **shared number:** ≤600 lines (executed box `trigger.<line_budget>`, base 600/600 in `receipts/base-battery.txt:41`) | — | same 600-line cap; 5 registry rows consume ~5–7 lines |
| `verifiers/checklist-baseline.json` | adds 4 box entries + `box_total` 41→45 (required: `checklist.box_map_complete` is MULTISET parity, `verify_skill_checklist.py:50`, fixtures `map-extra-entry`/`map-missing-entry` at :2078/:2080) | — | read-only input of its own gate `verify_skill_checklist.py` |
| `verifiers/corpus-baseline.json` | its new entry + README index row shift observed `tracked_files`, `report_total`, `commit_total` | its Frontier-row rewrite may shift pointer counts (watch) | re-records expectations; absorbs all prior corpus mutations (base drifts in `receipts/base-outputs/verify_corpus_integrity.out:22-26`) |
| `corpus/README.md` | new index row for `corpus/knowledge/resident-index-and-rungs-round72.md` | § Frontier "Loader-rule freshness" row (`corpus/README.md:149`) | index row for `corpus/lessons/round-71-verifier-spotcheck.md` (unindexed 1: `receipts/base-outputs/verify_corpus_integrity.out:3`) |
| `corpus/SOURCES.md` | appends opened rows (S248/S254–S256/S261–S264 staged; collisions S203–S213 in `.ufo/waves/round-72/assimilation/collisions`); append-only gate `check_sources_append_only.py` | — | — |
| `verifiers/floors-registry.json` | — | keeps `surfaces` floor 175 (self-test assertion count must not drop) | keeps `checklist` floor 1862 (self-test assertion count must not drop) |
| `verifiers/verify_skill_checklist.py` | — | — | live-governance self-test arm (verify_skill_checklist.py:2519-2525) expects "only LOG.md:2678 red"; live now PASS (2 recorded absences excused) → self-test failure (`receipts/base-outputs/check_assertion_floors.out:5`) |
| `verifiers/verify_skill_checklist.py` (guarded) | — | — | C3 must stay ≤40 added lines across the six battery instruments; also `verify_corpus_integrity.py`/`verify_corpus_independent.py`/`check_gate_registry.py`/`check_correction_sweep.py` |
| `verifiers/baseline.json`, `verifiers/surfaces-baseline.json`, new `verifiers/census-removals.json` | — | re-pins omp path (`omp.real`), opencode v2.1.4 sha, OC-1…OC-6 rules, removal ledger | row pins in `## Gate registry` must name existing paths at rev (`check_gate_registry.py:39-41`) |
| `PROVINCE.md` | § Core bullet optional; § Frontier/§ Adjacent must stay byte-identical (check_province_core.py no-harm conjunct) | no edit expected (surface is `corpus/README.md` § Frontier) | no edit expected |
| `.ufo/waves/round-72/snapshots/` | new sha256-pinned snapshots for A4 quotes | — | — |

## Pairwise separability

### C1 × C2 — separable (order-free)
No shared file except `corpus/README.md` in disjoint sections (index row vs § Frontier row). C1's counter (`check_author_rules.py`) reads SKILL.md boxes, SOURCES.md rows, the entry, snapshots; C2's counter (`check_substrate_repin_v2.py`) reads pins, surfaces baseline, ledger. Neither gate reads the other's artifacts. Order either; C3 needs both counters to exist before its registry rows.

### C1 × C3 — separable for verification, ordered for green intermediates
C3's six gates include `verify_skill_checklist.py` and `verify_corpus_integrity.py`/`verify_corpus_independent.py`; C1's landing supplies the checklist-baseline entries and the corpus index row those gates read. C1 can verify without C3 (its predicate does not read the Gate registry). C3 cannot be verified on a tree where C1's boxes exist unregistered (verify_skill_checklist FAILs: `map-extra-entry`) or C1's entry is unindexed (corpus DRIFT). Therefore: **C1 before C3**: and C1's landing should carry its own `checklist-baseline.json` update + README row + corpus-baseline re-record so the intermediate state is green.

### C2 × C3 — separable for verification, C3 last
C2's counter runs `verify_surfaces.py`/`check_substrate_pins.py` at their own default paths and recomputes the ledger; it never reads the six battery gates. C3's gates never read pin/ledger files. Shared surface: `corpus/README.md` (Frontier row vs index rows) and the final corpus-baseline re-record. Recommended order: C2 before C3 so C3's re-record absorbs any pointer-count shift C2's Frontier row introduces (unobserved until the draft; watch item).

### C3 ← C1 + C2 — NOT separable (the only non-separable pair)
C3's declared landing adds five `## Gate registry` rows: two for existing unregistered scripts (`check_r69_routed_repairs_v2.py`, `check_skill_evals_v2.py`) and three for the new counters (`check_author_rules.py` [C1], `check_substrate_repin_v2.py` [C2], `check_tip_battery.py` [C3]). The universe grows 53 → 56; a row naming a script that does not exist at rev is a PHANTOM row (check_gate_registry.py:45-48) and a missing row leaves the registry at 51/56 → exit 1. C3's gate therefore cannot pass unless C1's and C2's counter scripts already exist at the rev.

**Command showing it** (intermediate rev with C1+C2 counters, no C3 rows):
```
$ python3 -B verifiers/check_gate_registry.py --rev <rev-with-C1-C2-counters>
verifiers/check_author_rules.py            no registry rows naming it: 0 (need 1)
verifiers/check_substrate_repin_v2.py      no registry rows naming it: 0 (need 1)
gate registry rows conformant 54 of 56 lane verifiers; phantom 0
```
Observed equivalent at base (receipts/base-outputs/check_gate_registry.out:30,39,54):
```
verifiers/check_r69_routed_repairs_v2.py     no registry rows naming it: 0 (need 1)
verifiers/check_skill_evals_v2.py            no registry rows naming it: 0 (need 1)
gate registry rows conformant 51 of 53 lane verifiers; phantom 0
```
Conversely, C1 and C2 predicates have no dependence on C3 (their counters do not read the Gate registry), so the non-separability is one-directional.

## Conflict table (file | claim A edit | claim B edit | order)

| File | Claim A edit | Claim B edit | Order |
|---|---|---|---|
| `SKILL.md` | C1: 4 boxes in § Trigger-fidelity checklist (~15 lines, tail lines; free lines first) | C3: 5 Gate-registry rows (~5–7 lines) | C1 then C3; C1 frees ≥ C3's row budget (600-line cap shared) |
| `SKILL.md:259` | C1: "Eight of the fifteen" → executed count after 4 new boxes (19 boxes) | — | within C1 |
| `verifiers/checklist-baseline.json` | C1: +4 entries, box_total 45 | C3 reads only | C1 must land its baseline update before C3's `verify_skill_checklist.py` gate runs |
| `verifiers/corpus-baseline.json` | C1: re-record after its entry+row | C3: final re-record after its index row (+ C2 Frontier shifts) | C1 → C2 → C3; C3 is last writer |
| `corpus/README.md` | C1: index row (new entry) | C2: § Frontier row write; C3: index row (r71 spotcheck) | disjoint sections; any order, but C3's final re-record covers all |
| `corpus/SOURCES.md` | C1: append staged rows (collision-free ids) | — | — |
| `verifiers/floors-registry.json` | — | C2: keep surfaces ≥175 | C3: keep checklist ≥1862 | no floor lowers; each claim keeps its instrument's assertion count |
| `verifiers/verify_skill_checklist.py` | — | — | C3: rewrite live-governance arm (:2519-2525) | within C3; ≤40 added lines across six instruments |
| `verifiers/baseline.json` / `surfaces-baseline.json` / `census-removals.json` | — | C2: re-pin + ledger | — | C2 before C3 registry rows pin census-removals.json |
| `PROVINCE.md` | C1 optional § Core bullet | none | none | § Frontier/Adjacent byte-identity preserved |

## Risks / watch items (no command run; observed states)

1. **r71 non-author spotcheck vs byte-identical guard** — C3's planned fix touches `corpus/lessons/round-71-verifier-spotcheck.md` (unindexed; two `commit_nonhash` tokens at lines 90 and 120: `955ffd5d…`, `fb6a28ee…`; `receipts/base-outputs/verify_corpus_integrity.out:14-15`). The C3 counter's own guard says non-author `*-verifier-spotcheck.md` files are byte-identical to base. The counter draft must either exempt the round-71 file (it is the round's own record, written by the closure) or fix the nonhash tokens via quoted-context exclusion; otherwise the guard and the fix contradict. [INFERENCE: exact exemption set is a C3-counter draft decision; not observable before the draft exists.]
2. **C2 Frontier-row pointer count** — whether the rewritten Loader-rule freshness row changes `report_total`/`commit_total` is unobserved until the draft; C3's final re-record absorbs it if it does.
3. **Census row count** — C1's SOURCES.md append shifts the row count (139 at base, `receipts/census-before.txt`); the no-harm census `validate` runs at the measured tip and the receipts are re-committed by the L1. No gate conflict observed.
4. **A4 snapshot state** — C1 requires committed, sha256-pinned snapshots under `.ufo/waves/round-72/snapshots/`; missing/tampered → exit 2. Not a cross-claim file.

## Tooling record
No tools installed or upgraded (read-only analysis; standard `git`/`python3`/`sed`/`grep` only).
