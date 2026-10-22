HOLDS-BOUNDED — applies to C1's content guard `verifiers/check_sibling_census.py` at judged commit
`c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`: every named content check is enforced (6 of the 8
mandated mutants are killed by `--self-test`), the live command exits 0 with
`rows 20 verified 20` / `province rows 20 matched 20`, and the declared after-value (20 classified,
pinned rows in PROVINCE.md § Adjacent) measures 20. The bound: the guard's self-test leaves four
mutation points uncovered (M2, M7, M9, M10), one of which (M7) is a fail-open exit-code mapping, and
the ±2 quote window is load-bearing for 9 of the 20 live rows while no test bounds it.

## Findings

- **F1 (holds, 6 killed).** Quote existence (M1), heading-line refusal (M3), lane-set equality
  with the fleet directories (M4), PROVINCE classification comparison (M5), PROVINCE commit
  comparison (M6), and empty-quote-cell rejection (M8) each produce a `--self-test` failure, so
  the guard really enforces them. The live command exits 0 under every one of these mutants
  (the live census is correct), so none of them is a live-data defect.
- **F2 (survivor, fail-open — M7).** The CLI exit code is not tested with a failing census.
  Mutating `return 1 if result["failures"] else 0` to
  `return 1 if (result["failures"] and result["verified"] == result["rows"]) else 0` leaves
  `--self-test` at `0 failure(s) over 39 assertions` (exit 0). Exposure: a census whose quote was
  mutated → pristine exit 1, mutant exit 0 while still printing `FAIL …` and `rows 1 verified 0`.
  A guard that reports false content and then exits 0 is a fail-open path.
- **F3 (survivor — M2).** `LINE_TOLERANCE = 2` → `1000000` (whole-file window) leaves
  `--self-test` at 0 failures (exit 0) and the live command at exit 0. Exposure: a row citing
  `SKILL.md:3` whose quote is at line 26 → pristine exit 1 (`quote not found at SKILL.md:3
  (+/-2 lines)`), mutant exit 0 (`rows 1 verified 1`). The tolerance is not pinned by any arm,
  and it is load-bearing on the live data (F6), so this is a live-relevant gap, not a cosmetic one.
- **F4 (survivor — M9).** `extract_adjacent_section` returning the whole file instead of the
  `## Adjacent` body leaves `--self-test` at 0 failures (exit 0). Exposure: a PROVINCE.md whose
  `## Adjacent` section holds a bare-name list while another section holds a stale 4-column table
  → pristine exit 1 (`holds no lane table … a bare-name list is not a table`), mutant exit 0
  (`province rows 1 matched 1`). The "only the `## Adjacent` section is read" contract is untested.
- **F5 (survivor — M10).** Dropping the census-side classification-vocabulary check
  (`classification not in CLASSIFICATIONS`) leaves `--self-test` at 0 failures (exit 0).
  Exposure: a census row classified `maybe` with a matching PROVINCE row → pristine exit 1
  (`classification 'maybe' is not one of contested/adjacent/none`), mutant exit 0. Cross-agreement
  between census and PROVINCE is the only consistency the guard checks, so a bogus vocabulary
  agreed on both sides passes.
- **F6 (live-data, bounded).** The ±2 window is load-bearing: with `LINE_TOLERANCE = 0` the live
  command exits 1 with 9 of 20 rows unverified (audio, game-dev-3d, kotodama, mori, revenger,
  souji, tabi, tameshi, tsukuroi — their quoted description wraps onto the next line). So the
  cited `scope quote at` line points at the start of a wrapped description, and the guard's
  multi-line window is what finds it. Nothing in the self-test says how wide that window may get.
- **F7 (in-flight lane bytes, informational).** The uncommitted lane repair (`CriticC1Landed`,
  `git diff HEAD -- verifiers/check_sibling_census.py`) adds mechanical-column re-derivation and
  five new self-test arms, but leaves `LINE_TOLERANCE = 2` (line 107), the exit-code rule
  (line 698), `extract_adjacent_section`'s `return body` (line 554) and the
  `classification not in CLASSIFICATIONS` check (line 461) exactly as judged. F2–F5 therefore
  survive that repair too.

## Evidence

Scratch: `/fast/scratch/hyaku/kotoba-r49/falsify/MutCensusGuard/repo` (private clone of the lane at
`c48793d`). Verifier sha256 before any mutation and after every restore:
`8889d2190e300710042c238c6618343b5b1527f7ef901683ef1bbc536b3c8ddc` (identical every time;
`git status --porcelain` empty at the end).

Baseline (pristine bytes):
- `python3 -B verifiers/check_sibling_census.py --self-test` → `self-test: 0 failure(s) over 39 assertions`, exit 0
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, exit 0
- `awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md | grep -cE '^\| (audio|…|tsukuroi) \| (contested|adjacent|none) \| [0-9a-f]{40} \|'` → `20`, exit 0

Mutants (each applied in place, self-test + live run, then `git checkout --` restore + sha256):
| # | mutation | `--self-test` | live command |
|---|---|---|---|
| M1 | quote-existence check dropped (`if not found:` → accept, keep heading refusal) | exit 1 (3 assertion failures) | exit 0 |
| M2 | `LINE_TOLERANCE = 2` → `1000000` | exit 0 — SURVIVED | exit 0 |
| M3 | heading-line refusal dropped | exit 1 (2 failures) | exit 0 |
| M4 | lane-set equality dropped | exit 1 (2 failures) | exit 0 |
| M5 | PROVINCE classification comparison dropped | exit 1 (2 failures) | exit 0 |
| M6 | PROVINCE commit comparison dropped | exit 1 (2 failures) | exit 0 |
| M7 | exit code accepts `rows N verified M` with M<N | exit 0 — SURVIVED | exit 0 |
| M8 | rows with an empty quote cell skipped (empty-cell list excludes `quote`; empty quote `continue`s) | exit 1 (2 failures) | exit 0 |
| M9 | `## Adjacent` section isolation dropped (`return lines`) | exit 0 — SURVIVED | exit 0 |
| M10 | census classification-vocabulary check dropped | exit 0 — SURVIVED | exit 0 |

Supporting probe (not a mutant): `LINE_TOLERANCE = 0` → live exit 1, `rows 20 verified 11`
(9 rows need the window; see F6).

Exposure fixtures (private fixture fleet `/fast/scratch/hyaku/kotoba-r49/falsify/MutCensusGuard/exposure/fleet/alpha-shokunin`,
commit `abb0f597d7428b8abb0cae4b811dd5e5a52254ee`, quote at SKILL.md line 26):
- E1 `exposure/e1_census.md` (cites `SKILL.md:3`, quote at line 26): pristine exit 1; under M2 exit 0 (`rows 1 verified 1`)
- E2 `exposure/e2_census.md` (mutated quote): pristine exit 1 (`rows 1 verified 0`); under M7 exit 0 (still prints `FAIL row 1 … quote not found`)
- E3 `exposure/e3_census.md` + `exposure/e3_PROVINCE.md` (Adjacent = bare list, stale table in `## Archive`): pristine exit 1 (`holds no lane table`); under M9 exit 0 (`province rows 1 matched 1`)
- E4 `exposure/e4_census.md` + `exposure/e4_PROVINCE.md` (classification `maybe` on both sides): pristine exit 1 (`classification 'maybe' is not one of contested/adjacent/none`); under M10 exit 0 (`province rows 1 matched 1`)

Restoration: after each mutant the verifier was restored with `git -C repo checkout --
verifiers/check_sibling_census.py`; sha256 after every restore =
`8889d2190e300710042c238c6618343b5b1527f7ef901683ef1bbc536b3c8ddc`; the final restored run
reproduces the baseline (`self-test: 0 failure(s) over 39 assertions` exit 0; live exit 0).

Lane hygiene: no file in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was created, edited or
deleted except this report; no git/jj write command was run in the lane, the fleet root or any
sibling lane; the clone was created with `git clone -q` and left at `c48793d`.

Tooling: none installed or upgraded (stock `python3`, `git`, `awk`, `grep` only).
