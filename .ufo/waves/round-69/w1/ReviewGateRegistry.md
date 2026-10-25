# ReviewGateRegistry — round-69 wave 1 (gate registry rows + flag match)

Seat: `L1Kotoba69-2.ReviewGateRegistry` (reviewer, leaf). Read-only w.r.t. the lane; all executions ran in
`/tmp` sandbox clones. No lane file, index or jj state was touched; the only lane write is this report.

## Required measurement

Command (sandbox clone of the lane, `git clone --shared` → `/tmp/r69-review-gateregistry`):

```
python3 -B verifiers/check_gate_registry.py --rev <rev>
```

| rev | what it is | stdout tail | exit |
|---|---|---|---|
| `a238989a96cb0d2b939679126b832d75b861ca6e` | lane branch tip (`master`; the round-69 plan commit, child of base `a5f7459f`) | `gate registry rows conformant 46 of 49 lane verifiers; phantom 0` | 1 |
| `e845832b6892f71ff33ee84603aafe2643ea6a99` | `refs/jj/keep/…` snapshot of the L1 draft; parent `a238989`; its `SKILL.md` is byte-identical to the lane working tree (`sha256 e4c65d1695f40534a7c669305cee0c22d1287f1edbf748c7341543bb3f27ba3d`) | `gate registry rows conformant 49 of 49 lane verifiers; phantom 0` | 0 |

**Count: 49 of 49, phantom 0, exit 0 — reproduced exactly, but only at `e845832`, not at the branch tip.**
At the branch tip the gate prints **46 of 49, exit 1** and names exactly the three new verifiers with
`registry rows naming it: 0 (need 1)`. `git diff HEAD -- SKILL.md` is exactly three added table rows
(lines 517–519). The rows exist only as uncommitted working-tree content (and in the jj keep-snapshot);
no branch carries them (`git branch -a --contains e845832` → empty; `git show-ref | grep e845832` →
`refs/jj/keep/…` only).

Re-verified independently of any committed state: a synthetic sandbox commit carrying only the
working-tree `SKILL.md` (`d16dfd6`) also gives `49 of 49 … phantom 0`, exit 0 — so the 3-row diff is the
entire delta between 46/49 and 49/49.

## Rows in SKILL.md § Gate registry

Header at line 463 (`## Gate registry`), table header at 469, 49 `verifiers/` rows; the three new rows
are 517 `check_skill_precedence.py`, 518 `check_r68_routed_repairs.py`, 519 `check_province_core.py`
(table ends before `## Sources`). Each parsed to 8 cells by the counter's own `cells()`/`registry_rows()`
and judged conformant:

| row | kind | verdict map | self-test | pinned | write scope | owner |
|---|---|---|---|---|---|---|
| `check_skill_precedence.py` | gate | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; `--fetch` reads the network | kotoba |
| `check_r68_routed_repairs.py` | gate | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temporary sandbox clones under `$TMPDIR` (removed) | kotoba |
| `check_province_core.py` | gate | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |

No duplicate rows (the counter requires exactly one row per name); no phantom row (phantom 0).

## Flag match: row text vs argparse — 0 mismatches

Script blobs are byte-identical at `a238989`, `e845832` and the working tree, so this comparison is
revision-stable (`sha256` prefix: C1 `9c7965…`, C2 `320254…`, C3 `c85f9d…`).

| script | row's flags | argparse `add_argument` strings | verdict |
|---|---|---|---|
| `check_skill_precedence.py` | `--rev` (entry), `--self-test` (self-test), `--fetch` (write scope) | `--rev`, `--repo`, `--fetch`, `--self-test` | **match** — every named flag exists; none invented |
| `check_r68_routed_repairs.py` | `--rev`, `--self-test` | `--rev`, `--repo`, `--self-test` | **match** — row names no `--fetch`, script accepts none |
| `check_province_core.py` | `--rev`, `--self-test` | `--rev`, `--repo`, `--self-test` | **match** — same |

`--repo` is accepted by all three and omitted from the rows; the registry does not require it, and its
default (`verifiers/..`) is compatible with the entry commands as written. `--fetch` is real
(`action="store_true"`) and its body performs only `urllib.request.urlopen` reads; it is additionally
gated to run only when the five conjuncts already hold (`check_skill_precedence.py:388`), a detail the
row does not state but does not contradict.

## Non-vacuity (own falsifications, sandbox only)

| probe | result |
|---|---|
| `check_gate_registry.py --self-test` | `self-test: 0 failure(s) over 28 assertions`, exit 0 |
| C3 row's self-test cell rewritten to `--selftest` (no handler) | `48 of 49 … phantom 0`, exit 1, `self-test flag --selftest lacks an exact handler` |
| ghost row `verifiers/check_ghost69.py` inserted in the table | `49 of 49 lane verifiers; phantom 1`, exit 1, `PHANTOM verifiers/check_ghost69.py` |
| universe recount (`git ls-tree` blobs under `verifiers/`, `.py`/`.sh`) | 49 at both revisions; no new verifier file in the working tree |

Both arms the assignment depends on (flag-handler check, phantom count) bite for these rows; 49/49 is
not an empty table passing vacuously.

## Findings

### P1 — the three rows are uncommitted; the gate fails at the lane branch tip
`master` = `a238989` → 46/49, exit 1. Only `refs/jj/keep/e845832…` (not a branch) carries the rows.
Evidence: `git show HEAD:SKILL.md | grep -cE 'check_(skill_precedence|r68_routed_repairs|province_core)'` → 0;
working tree → 3; `git diff HEAD -- SKILL.md` → `1 file changed, 3 insertions(+)`.
**Action:** the closure commit must include `SKILL.md` (three rows). Until it does, the round's own
registry gate reads 46/49 at any branch tip, and the assignment's expected string is unreachable.

### P2 — the C1 row's "5 of 5 at the measured rev" is not true at the only revision carrying the row
`corpus/knowledge/skill-name-precedence-round69.md` is untracked and absent from every commit, including
`e845832` (`git cat-file -e e845832:corpus/knowledge/skill-name-precedence-round69.md` → rc 128).
`check_skill_precedence.py --rev e845832` → `skill precedence backed 0 of 5`, exit 1. Consequently the
counter's `--self-test` at a clean checkout of either revision exits 2 (`selftest setup failed: the entry
is not present in the working tree`), because the honest world is read from `--repo`'s **working tree**,
not from `--rev`. With the entry present in a `/tmp` mirror of the working tree the self-test is sound
(`0 failure(s) over 18 assertions`; `PASS honest world: backed 5 of 5`). The registry gate cannot see
this (it checks handler presence only, by design), but the row's self-test cell is not reproducible from
a revision today.

### P3 — C1 write-scope cell understates writes, and `--self-test` leaks its worlds
Cell says `none; --fetch reads the network`, but the counter writes under `$TMPDIR`:
`_materialize` into `tempfile.TemporaryDirectory` (auto-removed, `check_skill_precedence.py:385`) and
`_world` via `tempfile.mkdtemp` with **no cleanup** (`:279`). Measured: one successful self-test run
(mine, 07:18:22) left 18 `k69-prec-world-*` directories; `find /tmp -maxdepth 1 -name 'k69-prec-world-*'
-newermt '2026-10-25 06:00' | wc -l` = **528** — one per assertion, accumulated across today's runs. Its
sibling C2 row discloses `$TMPDIR (removed)`; C1 should match that granularity, and the leaked worlds are
the one place the disclosure matters. Not a registry conformance failure (write scope only needs to be
non-empty), but it is a consistency defect in the same table. I did not delete the accumulated worlds:
sibling seats are running the same counter concurrently.

### Verified accurate (no finding)
- C3 `none (read-only)`: the counter only runs `git show`/`git rev-parse`, no writes.
- C2 `$TMPDIR (removed)`: `tempfile.TemporaryDirectory` + `git clone --shared` in its `--rev` path.
- `pinned values: in-file` for all three: C1 `TOTAL=5`; C2 `TOTAL=8`, `R68_BASE`, `R69_BASE`; C3 `BASE`, `TOTAL`.
- Verdict maps: each script returns 2 on `EnvError` (and argparse returns 2 on usage errors), 0/1 as declared.

## Residual risk / verification gaps

- The registry gate is structural: it never runs a verifier and does not prove exit statuses (its own
  docstring, Q31). I ran the three entry commands in the sandbox: C1 `0 of 5` exit 1 at both revs; C2
  `0 of 8` exit 1 at `a238989` and `1 of 8` exit 1 at `e845832`; C3 `0 of 2` exit 1 at `a238989` and
  `2 of 2` exit 0 at `e845832` — every observed code is one the rows declare, but closing those claims is
  the C1/C2/C3 seats' scope, not this one.
- `--fetch` was **not** exercised (network); only its argparse presence and read-only body were checked.
- No revision exists that carries both the three rows and the C1 entry, so 49/49 and C1's 5/5 could not
  be observed at one rev.
- Sandbox `/tmp/r69-review-gateregistry` and `/tmp/r69-c1-world` were removed after measurement; recreate
  with `git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/r69-review-gateregistry`.

## Verdict

Registry rows and flags: **conformant, 49 of 49, phantom 0, exit 0** at the draft snapshot `e845832`
(and at a sandbox commit of the working-tree `SKILL.md`); **0 flag mismatches** for
`--rev`/`--self-test`/`--fetch`. The one blocking consistency item is P1: the three rows are not committed
on the branch tip, so the same command prints 46 of 49 and exits 1 there.
