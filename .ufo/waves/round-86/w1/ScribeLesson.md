# ScribeLesson — round 86 w1 report

Seat: ScribeLesson (scribe, leaf). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base `e5d966b51494f4177868ad5f46806a204783ef6c`, freeze `ecfad51fe3f24540a6d67d2b54920929c7b83041`.
No git/jj write in the lane; no tool installed or upgraded (none needed; pacman untouched).

## Files written

- `corpus/lessons/round-86.md` (new): intro + C1 verbatim, § Gate (S255, census before,
  `census after: <L1>`, rows added/touched, controls K0/K1/K2/S with receipt sha256),
  § Mistakes (M86-1 + criterion proposal + base fails it), § Routed defects D1–D7.
- `corpus/lessons/round-85.md`: appended `## Correction, round 86` (D1, D4, D5);
  `git diff --numstat` → `33 0`.
- `LOG.md`: appended `## Round 86` (claim, intake, mistake, routed defects);
  `git diff --numstat` → `52 0` (zero deletions).
- Receipts: `.ufo/waves/round-86/w1/ScribeLesson/census-base-file.txt`,
  `census-mid-round.txt`, `harness-base-catalogue.txt`.

## Evidence (commands run by this seat, observed)

- `git diff 1c8f37e cfcb9a4 -- corpus/README.md | grep -c '^+| '` → `9`
- `git show cfcb9a4:LOG.md | wc -l` → `3235`; `… | grep -n '^## Round 85'` → `3088:`
- `git cat-file -s cfcb9a4:corpus/SOURCES.md` → `202884`
- `grep -c '^MISS' .ufo/waves/round-86/receipts/c1-K0-base.txt` → `132`; `grep -c 'not-discovered'` → `132`; `grep -c 'render-differs'` → `0`
- `sha256sum .ufo/waves/round-86/receipts/*` → K0 `ec418646…`, K1 `03974275…`, K2 `cfdfa951…`, self-test `ea77630f…`, census `5564711e…`, D6 `cd3d5917…`
- `git log -S 'must byte-equal a cached description' -- verifiers/verify_harness_claims.py` → `abef8aa 2026-09-28 round-10: …`
- `python3 -B verifiers/verify_harness_claims.py` (TMPDIR=scratch) → `16/28 checks pass`, `omp.catalogue.total: observed=215 expected=7`, `omp.catalogue.matched: observed=15 expected=7`, rc=1
- census `--root` now → exit 1, 33 W04 + `E11 S255 missing used-by verifiers/omp-skill-roots.tsv`
- census `--file` on `git show e5d966b:corpus/SOURCES.md` → 33 W04 (+249 E11 path-resolution artefacts)

## Findings

1. **Census receipt is a digest.** `receipts/census-round-start.txt` holds 2 W04 rows, not 33;
   the plan's "33 W04" is not re-derivable from the cited receipt (re-derived on base bytes: 33).
2. **Census currently red (mid-round).** S255's `used-by` names `verifiers/omp-skill-roots.tsv`,
   absent until ExecModel lands; the census `--root` form exits 1 (E11) until then.
3. **"~30 rounds" not re-derivable.** The premise sentence has stood since round 10 (`abef8aa`),
   76 rounds / 37 days; when it became false is unmeasured. The lesson does not adopt "~30".
4. **Q77 already drafted** (uncommitted) in `corpus/QUALITY.md` by someone else, citing M86-1;
   the lesson's mistake id matches it.
5. Live catalogue check picks a newer catalogue (22:14:32.885Z) than the frozen fixture
   (21:55:22.890Z); both 215 lines.
6. **Counter changed after freeze (conflict for the judge, verbatim).** Addendum 1
   (`b9ee548`, counter sha256 `2390eec2…` → `39a014f2…`) landed after `ecfad51` and before
   any candidate was scored; the plan's kill rule lists "the counter, its fixture or its pins
   changed after this freeze". Recorded in the lesson and LOG; not judged.
7. **The old check is blind to model correctness**: with ExecModel's 215-of-215 candidate,
   `verify_harness_claims.py` still reads `16/28 checks pass` (`omp.catalogue.matched:
   observed=35 expected=7`, `ExecModel/cli-after.txt`) — same verdict as the base. Added to M86-1.

## Risks

- After value, census after and the D3/D7 artefacts are L1-owned placeholders (`<L1>` / `<L1 fills>`).
- The census stays exit 1 (`E11 S255 … omp-catalogue-model-round86.md`) until ScribeEntry's entry exists.
- The candidate reading is ExecModel's (`ExecModel/score.txt`), not re-scored by this seat.

## Candidate

`CANDIDATE_READY` appeared on the 7th check (~12 min): scratch commit `903bd78e…` on `b9ee548`,
amended counter `39a014f2…`, G1–G4 PASS, `omp catalogue lines reproduced 215 of 215`, exit 0.
Worktree `verify_harness_claims.py` / `omp-skill-roots.tsv` sha256 match it (`bd793b6c…`, `36021309…`).
