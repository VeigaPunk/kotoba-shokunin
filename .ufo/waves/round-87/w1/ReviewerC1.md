# ReviewerC1 — attack C1's four conjuncts (round 87, w1)

Seat: ReviewerC1 (non-author). Everything below was derived before or independently of the
executors' files: my own ELF scan (`recon_*.py` → `receipts/recon_*.out`), my own conjunct
implementation (`indep_root_semantics.py`), and my own scratch clone
(`/fast/scratch/hyaku/kotoba-r87/ReviewerC1/repo`, `--shared` clone, commits only there).
Reviewed bytes (lane worktree, untracked; no `COUNTERS_READY`/`LEDGER_READY` ever appeared —
reviewed what exists after the 45-minute poll expired):

- `verifiers/check_omp_root_semantics.py` sha256 `dca21dee7432defc…99a11d5c` (29 975 B, 20:34)
- `verifiers/omp-skill-roots-semantics.tsv` sha256 `65590472569fc3b9…b77475cb` (1 939 B, 20:29)
- omp ELF sha256 `6737ee2415555a36…49ccb7b0f` (matches the plan pin; S2 PASS everywhere)

## 0. Addendum-1 effect on this review

The frozen plan says "13 rows / 13 patterns / `N of 13`"; I measured the round-86 ledger at base
`223ae62` before opening any executor file: **12 data rows** (`… | tail -n +2 | wc -l` → 12;
awk enumeration in the transcript). Addendum-1 (`512126b`, committed before any candidate score)
corrects the denominator to 12 and keeps the target "every row grounded" (11 of 12 is still
exit 1 — not a narrowed target). I therefore report both readings: the frozen counter's observed
`N of 13` and the addendum's `N of 12`. A corrected denominator changes no attack verdict below.

## 1. Independent per-row table (real ledger, same committed bytes, same ELF)

My implementation vs the frozen counter, row by row (offsets are the quote's first occurrence;
both implementations located identical offsets):

| # | root_pattern | module cell | mine | frozen counter |
|---|---|---|---|---|
| 1 | `{cwd}/.omp/skills` | builtin.ts | GROUND | GROUND @173819979 |
| 2 | `{cwd}/.claude/skills` | claude.ts | GROUND | GROUND @173840364 |
| 3 | `{cwd}/.agent/skills` | agents.ts | GROUND | GROUND @173865724 |
| 4 | `{cwd}/.agents/skills` | agents.ts | GROUND | GROUND @173865724 |
| 5 | `{cwd}/.codex/skills` | codex.ts | GROUND | GROUND @173879095 |
| 6 | `{cwd}/.opencode/skills` | helpers.ts | GROUND | GROUND @172785704 |
| 7 | `{cwd}/.github/skills` | helpers.ts | GROUND | GROUND @172785704 |
| 8 | `~/.omp/agent/skills` | builtin.ts | GROUND | GROUND @173820135 |
| 9 | `~/.omp/plugins/node_modules/*/skills` | omp-plugins.ts | GROUND | GROUND @173914936 |
| 10 | `~/.agent/skills` | agents.ts | GROUND | GROUND @173865523 |
| 11 | `~/.agents/skills` | agents.ts | GROUND | GROUND @173865523 |
| 12 | `~/.omp/agent/managed-skills` | managed-skills.ts | GROUND | GROUND @173809938 |

Mine: `omp root semantics grounded 12 of 12`, guards S1/S2/S3 PASS, exit 0.
Counter: `omp root semantics grounded 12 of 13`, `note:` 12 patterns vs denominator 13, exit 1.
The two implementations agree on every row; they differ only on the denominator (finding F2).

Base reading, run from the lane (`--rev 223ae62…`): `omp root semantics grounded 0 of 13`,
exit 1, `semantics ledger: … absent at the revision` — matches the FROZEN plan sentence; the
addendum's corrected base sentence (`0 of 12`) is **not** what the counter prints (F2).
Counter `--self-test` independently reproduced: `0 failure(s) over 35 assertions`, exit 0.

## 2. Attack worlds (each a one-cell mutation of the real ledger, committed in my scratch clone, scored on the FROZEN counter, never edited)

| world | conjunct | observed (frozen counter) | observed (addendum denom.) | verdict |
|---|---|---|---|---|
| base223-lane | — | 0 of 13, exit 1 | (0 of 12) | base ✓ |
| world_real | all | 12 of 13, exit 1, all rows GROUND | 12 of 12, exit 0 | rows sound; exit gated by denominator (F2) |
| W1a-docjoin-line | 2 | 11 of 13, exit 1; row 1 FAIL "sits on no ELF line carrying a path-join token" | 11 of 12 | **refused** |
| W1b-docquote-bare | 2 (+3) | 11 of 13, exit 1; row 1 FAIL (doc line; first occ @114486488 precedes every header, min header @166865730) | 11 of 12 | **refused** |
| W2-wrongmodule | 3 | 12 of 13, exit 1; **row 5 GROUND with `module='coding-agent/src/discovery/claude.ts'`** while the quote is codex.ts's `return Xr.join(u.cwd, ".codex");` | 12 of 12, exit 0 | **ADMITTED** |
| W4-dotdot | 1 (+S3, 4) | 11 of 13, exit 1; row 1 FAIL (pattern ≠ r86 row 1; `{cwd}/` rest not a plain relative path; S3 detail) | 11 of 12 | **refused** |
| W5-fabricated | 2 | 11 of 13, exit 1; row 9 FAIL "reader_quote not located in the omp ELF" | 11 of 12 | **refused** |
| W6-linespan-degenerate (extra) | 2 impl. | 11 of 13, exit 1; row 9 FAIL — see F4 | 11 of 12 | **refused** (this ELF) |
| W3-bound (probe, no ledger) | 4 | `bound_grounded('{cwd}/…', FULL_CHAIN)` → False: "`{cwd}/` expansion reaches /.omp/skills ($HOME or above)"; frozen chain passes | — | **refused** |

W3 matcher detail (`receipts/probe-bound.out`): `matches_row` refuses `/home/u/proj/sub/../.omp/skills`
(a `..` candidate that **normalizes onto the legitimate row-1 root**), `/home/u/proj/sub/../sub/.omp/skills`
and `/home/u/../u/.omp/skills`; a clean candidate matches; `~/` rows stay grounded. The counter's
self-test arm `w_bound` (score with `FULL_CHAIN`) leaves exactly the five `~/` rows grounded — refusal works.

My independent scorer agrees with the counter on every world at row level
(`receipts/worlds-indep-real.txt` vs `receipts/worlds-summary.txt`).

## 3. Findings (by severity)

- **F2 (defect, blocks the claim; owner ExecSemantics).** The committed counter (sha `dca21dee…`)
  still carries `TOTAL = 13`, the frozen sentence `… grounded N of 13`, and
  `ok = grounded == TOTAL`. The real round-86 ledger has 12 patterns, so `grounded` can never
  reach 13: **the counter cannot exit 0 even with every row grounded** — observed:
  `world_real` prints 12 GROUND rows, S3 PASS, then `12 of 13`, `exit=1`. Addendum-1 § A1.1
  requires the corrected sentence (`N of 12`, exit 0 iff N == 12) "in the counter's docstring…
  and in every receipt"; the docstring still says 13 and the base reading prints `0 of 13`
  (addendum: `0 of 12`). The addendum's own re-run control `w_honest` (12 grounded rows →
  12 of 12, exit 0) would FAIL on this counter as committed. Per the L1's routing this is
  ExecSemantics' to fix; recorded here because it is the state at the reviewed hash.
- **F3 (admitted world — bounds the claim; conjunct 3).** W2-wrongmodule: the frozen conjunct 3
  checks only that `// packages/<module>` occurs and the quote's first occurrence lies after the
  header's last occurrence. It never checks that the quoted code belongs to the named module:
  codex's reader grounded as `claude.ts` (12 of 12, exit 0 under the addendum denominator). The
  real ledger leans on the same weakness for rows 6 and 7, which both cite the shared
  `helpers.ts` line `return d.join(e.cwd, r.projectDir, n);` — provider-agnostic code naming no
  opencode/github-specific literal. Within the frozen predicate this is admissible; the
  per-provider meaning therefore rests on the round-86 roots review, not on this counter.
- **F4 (latent implementation defect — refused in this ELF).** Conjunct 2's `elf_line` bounds the
  "line" to ±LINE_SPAN (8192). A quote ≥ 8192 B from any newline degenerates to the whole-ELF
  slice, which contains unrelated `join(`/`resolve(` tokens: at function level
  `reader_grounded('/$bunfs/root/chunks/daemon-ceq4bv7m.js') → True` (pure bun-virtual-fs path
  metadata, no join token in the string; receipt in the transcript). Not exploitable in a full
  row today: every tail-zone string also occurs early in the string table (conjunct 3's
  first-occurrence rule then refuses — first occ @112.7 M < min header @166.9 M), and strings
  with > 8 occurrences are shielded by `occurrences(limit=8)`. I searched the newline-free tail
  (3 000+ printable runs) for a constructible full-row world: none exists in this ELF (0
  late-only candidates). Residual risk for future ELFs or quote choices.
- **F1 (adjudicated, for the record).** Plan denominator 13 vs 12 measured rows — resolved by
  addendum-1 before any candidate score; my independent measurement confirms 12.

## 4. Verification gaps and residual risk

- The executors' files are untracked worktree bytes; the markers `COUNTERS_READY`/`LEDGER_READY`
  never appeared within the polling window. My review pins the exact hashes above; if
  ExecSemantics amends the counter (the L1 says the denominator fix is theirs), the F2 state may
  already be stale — re-run `--rev <rev>` + `--self-test` at the new hash before integrating.
- My worlds commit the counter+ledger bytes into the scratch clone and run it there (S1
  exercised via `git show` of those commits); the L1's integration commit in the lane may differ
  only by commit id, not bytes (hashes pinned).
- Conjunct 4 is scored on the frozen synthetic chain inside the counter (`chain=FROZEN_CHAIN`
  default); I probed it directly rather than through a ledger world (a ledger cannot change the
  chain), plus the counter's own `w_bound` self-test arm.

## 5. Verdict

**C1 conjuncts: bounded by conjunct 3 (module attribution is ordering-only — W2 admitted at row
level) — and the committed counter cannot reach its own target (TOTAL=13 vs a 12-pattern
ledger; addendum-1's corrected predicate is not implemented in the counter at sha `dca21dee…`).**
Conjuncts 1, 2 and 4 refused every forgery world thrown at them (doc lines with window tokens,
bare doc quotes, `..` patterns and `..` candidates normalizing onto legitimate roots, fabricated
absent quotes, HOME-reaching expansions); the honest ledger grounds 12 of 12 rows under the
corrected predicate.
