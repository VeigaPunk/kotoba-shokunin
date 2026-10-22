# Falsify seat — MutLeverGuard (mutation test of verifiers/check_overlap_levers.py)

Verdict: HOLDS-BOUNDED

The C2 counter as landed is correct on the real tree (HEAD `59903b2` prints
"overlap levers backed 7 of 7 clients", exit 0; `--self-test` passes 22
assertions). But the instrument is not robust: 14 of 18 plausible single-defect
mutants of the script itself survive BOTH the in-memory self-test and the
real-tree `--rev` run. Several survivors would let a false "7 of 7" (or, for
the denominator mutant, a false exit 0) through. Killed: 4 (all by
`--self-test`; the real-tree run never killed one — the real data is clean, so
it only proves slack).

## Findings — mutant table (18 mutants, one per BACKED condition plus the --rev reader)

Run for each mutant `mNN.py` (copy of pristine, one defect):
`python3 -B verifiers/mNN.py --self-test` and
`python3 -B verifiers/mNN.py --rev 59903b2637689739a5b9901956301da72d0effe1`.

| # | condition mutated | defect | self-test exit | rev exit | real-tree print | verdict |
|---|---|---|---|---|---|---|
| m01 | section scoping | `if inside:` → `if True:` (table outside `## Anti-patterns` now counts) | 0 | 0 | 7 of 7 | SURVIVED |
| m02 | comment stripping | `COMMENT.sub` deleted (table in an HTML comment now counts) | 0 | 0 | 7 of 7 | SURVIVED |
| m03 | header-name parsing | `_find_table` column-header equality dropped | 0 | 0 | 7 of 7 | SURVIVED |
| m04 | held-by vocabulary | "vendor staff" added to ALLOWED_HELD_BY | 0 | 0 | 7 of 7 | SURVIVED |
| m05 | effect vocabulary | "renamed" added to ALLOWED_EFFECTS | 0 | 0 | 7 of 7 | SURVIVED |
| m06 | URL prefix | vendor-prefix check bypassed | 1 | 0 | 7 of 7 | KILLED (self-test: cross-vendor URL fixture got 7) |
| m07 | kind | "own-work" added to ALLOWED_KINDS | 0 | 0 | 7 of 7 | SURVIVED |
| m08 | tier | tier "B" accepted | 0 | 0 | 7 of 7 | SURVIVED |
| m09 | mined | `mined` check bypassed | 1 | 0 | 7 of 7 | KILLED (self-test: queued-row fixture got 7) |
| m10 | used-by exact path | `ENTRY_FILENAME` fallback dropped (strict full path only) | 0 | 0 | 7 of 7 | SURVIVED (narrowing; no false-pass risk) |
| m11 | Gate record | `rid not in gate` check bypassed | 1 | 0 | 7 of 7 | KILLED (self-test: no-Gate fixture got 7) |
| m12 | duplicate row ids | source-duplicates check bypassed | 0 | 0 | 7 of 7 | SURVIVED |
| m13 | reviewed-list membership | "disabledSkills" added to VS Code reviewed set | 0 | 0 | 7 of 7 | SURVIVED |
| m14 | exact backtick span | code-span equality relaxed to substring-in-quote | 1 | 0 | 7 of 7 | KILLED (self-test: un-backticked-key fixture got 7) |
| m15 | 25-word cap | MAX_QUOTE_WORDS 25 → 30 | 0 | 0 | 7 of 7 | SURVIVED |
| m16 | 'description' filter | description-mention check bypassed | 0 | 0 | 7 of 7 | SURVIVED |
| m17 | pinned denominator | "Codex" removed from CLIENTS | 0 | 0 | **6 of 6** (exit 0) | SURVIVED |
| m18 | --rev reader | `git show <rev>:<path>` → `git show HEAD:<path>` (rev ignored) | 0 | 0 | 7 of 7 | SURVIVED |

### Survivors that would let a false "7 of 7" through
m01, m02, m03, m04, m05, m07, m08, m12, m13, m15, m16 (permissive
weakenings: a bad world can pass the weakened check while the real tree still
prints 7 of 7); m17 (prints a false "6 of 6" with exit 0 — an exit-code-based
judge is fooled, and the claim's "7 of 7" string can never print again); m18
(`--rev <base>` would print HEAD's 7 of 7 — a direct false pass on the exact
command the claim uses, with a different revision). m10 narrows only; no false
pass.

### Why some kill-fixtures do not isolate their check (coverage gaps)
- m01/m02: section scoping and comment stripping overlap; the comment-hidden
  fixture only fails when BOTH are removed, so either defect alone is invisible.
- m12: the duplicate-source-row fixture's inserted row carries a trailing
  newline, so joining produces a blank line that truncates `parse_sources`
  before S029/S030/S031; the fixture lowers K via those three clients, and
  bypassing the duplicates gate still leaves K=4 < 7 — the assertion passes.
- m16: the "key term mentions description" fixture's term `description-term0`
  is also outside REVIEWED_LEVERS, so reviewed-membership unbacks it first; the
  description filter is never the deciding check.
- m17: `--self-test` derives its expectation from CLIENTS itself, so trimming
  CLIENTS trims the expectation; the denominator is not independently pinned in
  the test.

## Evidence

Pristine baseline (scratch clone of lane at `59903b2`; file sha256
`e871fa03d0587f3f857f730b3799d417c93a83d8ab2e34478fe0a4bf006fc9a1`, identical
to the lane's committed verifier):
- `python3 -B check_overlap_levers.py --self-test` → "0 failures / 22
  assertions", exit 0.
- `python3 -B check_overlap_levers.py --rev 59903b2637689739a5b9901956301da72d0effe1`
  → BACKED for all seven clients, "overlap levers backed 7 of 7 clients", exit 0.

Mutant runs: exit codes and prints in the table above; full outputs kept in
`/fast/scratch/hyaku/kotoba-r51/falsify/MutLeverGuard/{st,rev}_NN.out`.
Mutant hashes (sha256, `git diff`-free check): m01 8aa547eb, m02 fa9c34d8,
m03 8fc0514d, m04 d109e030, m05 a76da404, m06 8e39c09b, m07 364a33f3,
m08 8388beee, m09 ed702db9, m10 eb484933, m11 8ace4058, m12 0fd99f44,
m13 68c7cb70, m14 2f2861f5, m15 1c8546dd, m16 2a793bfa, m17 6c1d7d9d,
m18 1cc214d2. Pristine byte restored untouched: v0.py still
e871fa03... (no lane file was ever modified; the scratch clone is disposable).

No tools installed (nothing needed; policy record: none).
