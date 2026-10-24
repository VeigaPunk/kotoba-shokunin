# ScoutCorpusCount — corpus count reconciliation (round 66, w1)

Seat: scout (leaf; no dispatch). Read-only measurement; no production edits.
Observed tip: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` ("round-66 verifier spot-check (integrator, hyaku): non-author admit/reject"). Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`.

## Independent counts (commands + values)

- `git ls-files corpus/ | wc -l` → **119** (tip working index)
- `git ls-tree -r --name-only HEAD corpus/ | wc -l` → **119** (committed tip tree, index agrees)
- `git ls-files corpus/ | grep -c '\.md$'` → **118** corpus Markdown files; `grep -cv '\.md$'` → **1** (`corpus/knowledge/sibling-citation-routing-round16.json`)
- `git ls-tree -r --name-only 11385e04… corpus/ | wc -l` → **116** at pinned base (115 `.md` + 1 `.json`)
- `git status --porcelain -- corpus/` → empty; `git ls-files -m corpus/` → 0, `git ls-files -o corpus/` → 0 (all 119 committed; no pending corpus file)
- `git diff --name-status 11385e04..HEAD -- corpus/` → A `corpus/knowledge/fleet-commit-resolution-round66.md`, A `corpus/lessons/round-66.md`, A `corpus/lessons/round-66-verifier-spotcheck.md`; M QUALITY/README/SOURCES. **Three** newly tracked files, not two.

## Reconciliation to `verifiers/corpus-baseline.json`

- Baseline `checks.corpus.index.tracked_files.expect = 118`; `round66_rerecord` note: "116 -> 118 (the round-66 lesson and C2 knowledge entry, both indexed)", measured at `daedcdf` via `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`; receipt `receipts/C2-reconcile-measure.txt` confirms tracked=118, unindexed=0, report_total=79, commit_total=37.
- Per-commit: `git ls-tree -r --name-only <rev> corpus/ | wc -l` gives 118 at `daedcdf`, `4119647`, `fc1b71e`, `9e75e73`, and **119** at tip `2a8eba5`.
- **Accounted-for exactly:** the baseline's "exactly two" is the two lane-authored files (`lessons/round-66.md`, `knowledge/fleet-commit-resolution-round66.md`) landed in `daedcdf`; both indexed in `corpus/README.md` (rows 122, 123). The third file, `corpus/lessons/round-66-verifier-spotcheck.md` (11137 B, closure/integrator-authored), landed after re-record at `2a8eba5`; `grep -n round-66-verifier-spotcheck corpus/README.md` → 0 rows, consistent with the r46–r65 pattern of indexing the closure spot-check next round.

## Live gate at observed tip (read-only run)

`python3 -B verifiers/verify_corpus_integrity.py` → **exit 1**:
`corpus.index tracked=119 unindexed=1 stale=0 missing=0 (136 FILE-column patterns over 118 md files)`; `corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0`.
`--json` verdicts: DRIFT on tracked_files (119 vs 118), unindexed (1 vs 0, named file `corpus/lessons/round-66-verifier-spotcheck.md`), report_total (82 vs 79), commit_total (38 vs 37); PASS on report_dead, commit_unresolvable, commit_nonhash, stale_patterns, missing_paths. The spotcheck's `commit `1154d57a9ebb…`` (line 11) resolves via the r66 lane→fleet hop, keeping `commit_unresolvable=0`.

## Findings

1. Counts are internally consistent: base 116 + 2 lane-authored = 118 (baseline correct for its measurement revision `daedcdf`), + 1 closure spot-check = 119 at tip.
2. The round-66 lesson + C2 knowledge entry account for exactly two newly tracked corpus files; the third is outside their D2 scope (post-landing `2a8eba5`).
3. Calibration gap (observation, not a scored claim): the frozen C2 predicate says `verify_corpus_integrity.py` "must exit 0 at the final lane tree"; at the observed tip it exits 1 with 4 DRIFT rows, all attributable to the unindexed r66 spot-check. README has no r66 spot-check row; baseline `as_of` predates `2a8eba5`.

## Gaps / notes

- `git status` shows ` M .ufo/waves/round-66/w1/swarm-registry.json` — modified wave artifact, outside `corpus/`, not counted.
- No lane gate was re-run against the pinned base; C2-before control (`controls/C2-before.txt`) already records the base state. Only the tip was measured live.
- No tools installed this run (pacman pause observed; nothing needed).
