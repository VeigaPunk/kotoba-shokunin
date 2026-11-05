# ReviewC1R87 — w3 independent re-implementation of C1 (read-only)

Seat: reviewer, round-87 w3. Item: re-implement the four C1 conjuncts from
`plans/round-87.md` § C1 only, without importing or pre-reading the frozen counter
`verifiers/check_omp_root_semantics.py`, score all 12 rows at the lane tip
`760e1c5edfdefb4767420f711d08f669952de013`, and diff per-row verdicts against the
counter's `row NN GROUND` lines. No counter defect may be edited in this wave.

## States measured (all read-only)

| check | observed |
|---|---|
| lane tip | `git rev-parse master` → `760e1c5edfdefb4767420f711d08f669952de013` (matches the seat spec; the w3 L1's attempt-2 append is still worktree-only) |
| ELF | sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` — equals the pinned build |
| counter drift freeze→tip | `diff` of `show 87ab1cb9...:verifiers/check_omp_root_semantics.py` vs `show 760e1c5e...:verifiers/check_omp_root_semantics.py` → identical; sha `6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922` matches the c1-instrument-freeze pin |
| frozen counter run | `python3 -B verifiers/check_omp_root_semantics.py --rev 760e1c5e` → `omp root semantics grounded 12 of 12`, all guard S1/S2/S3 PASS, `exit=0` (receipt `counter_c1_tip.txt`) |
| C2 frozen counter run | `python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e` → `r86 routed defects closed 4 of 5`, `exit=1` (D5(iii) red-set exact-match fails because `report_dead` healed — known assignment context) |

## My re-implementation

`reimpl.py` (in this seat dir, 159 lines) — written from the plan's C1 section only,
before any read of the counter's source. Independent coverage:

- guards S1 (both ledgers read from `git show 760e1c5e:...` committed bytes, never the
  worktree) and S2 (ELF pin asserted via hashlib).
- conjunct 1: semantics `root_pattern` must equal the round-86 ledger row at the same
  index, no `..` segment anywhere, no `*?[` in the first segment after stripping the
  `{cwd}/` or `~/` prefix.
- conjunct 2: `reader_quote` ≥ 12 chars, located as raw bytes in the ELF, with a
  bounded (8192-B) newline-window line that carries one of `join(`, `.join(`,
  `resolve(`, `path.join`.
- conjunct 3: `// packages/<module>` occurs in the ELF and the reader quote's first
  occurrence offset precedes the header's **last** occurrence (strict "<" refusal,
  mirroring the frozen "first occurrence lies after that header's last occurrence").
- conjunct 4: `{cwd}/` rows expand only over the frozen chain
  (`/home/u/proj/sub`, `/home/u/proj`); any expansion at or above `$HOME` (`/home/u`)
  fails; both frozen `..` probe candidates (`/home/u/proj/sub/../sub/.probe/skills`,
  `/home/u/../u/.probe/skills`) must fail to match after normalization.

Run: `python3 reimpl.py` → `reimpl grounded 12 of 12`, S1/S2 PASS, per-row 12× GROUND.
Receipt: `reimpl_out.txt`.

## Verdict diff (reimpl vs frozen counter)

`verdicts_diff.txt`: **disagreements: none** — all 12 rows: same verdict (GROUND),
same module, same reader-quote offset (e.g. row 9
`'~/.omp/plugins/node_modules/*/skills'` `@173914936`, row 1 `@173819979`,
row 5 `@173879095`, rows 6/7 `@172785704`, rows 10/11 `@173865523`).

**C1 independently corroborated at the tip: 12 of 12, exit 0, no observable drift
between the frozen counter and a from-plan re-implementation.**

## Independence audit (what this re-implementation shares with the counter)

Written from the same plan text (same predicate, same frozen token list
`JOIN_TOKENS`, same frozen chain, same 12-row denominator) and reading the **same
ELF** — not an independent ground-truth that the ELF itself is what maps these roots.
What the re-implementation adds: (a) the counter's implementation is pinned to the
one in `87ab1cb9` (verified byte-identical to tip); (b) the from-plan derivation
sealed the same four predicates with no free parameter — my own choice of 8192-B
line bound and of probe paths matched the counter exactly (not read in advance).

Not covered: no adversarial mutant was scored (interaction bound); specifically the
w3 L1's own mutants and Q79 control live under `.ufo/waves/round-87/w3/l1/` and were
not re-run here.

## C2 state at the tip (measured, not re-opened)

`python3 -B verifiers/check_r86_routed_repairs.py --rev 760e1c5e` → `4 of 5`, exit 1;
D5(iii) refuses the exact red-set match because the fleet-root kama report
(`.ufo/reports/round-84/kama.md`) landed at fleet commit `5b052020a13b37340c1054286d65b2514c7133d5`
and healed `report_dead` — the lane's committed bytes did not change (D5(i)/(ii) blobs
`4620a63` round-87 C2-final receipt, spot-check blob `ae3f49a`/`315c0ec` unchanged from
base at tip — verified via `rev-parse <rev>:<path>`).

No counter-defect edits were made; per the bounds this finding is routed, not repaired.

files_written:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-87/w3/ReviewC1R87/reimpl.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-87/w3/ReviewC1R87/reimpl_out.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-87/w3/ReviewC1R87/counter_c1_tip.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-87/w3/ReviewC1R87/verdicts_diff.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-87/w3/ReviewC1R87.md (this report)
