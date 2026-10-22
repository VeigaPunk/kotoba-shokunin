Result: HOLDS — every cell of the `verifiers/check_gate_registry.py` registry row survives re-run, source read, and mutation probes; no corrected row text needed.

# Scope

Attack on the SKILL.md `## Gate registry` row for `verifiers/check_gate_registry.py` as landed at
`bf65974c7845a06d7ef621ad998c6378ff735cd5` (row text at `SKILL.md:448` in that commit, `SKILL.md:462` at
tip `58db81c4465b0e9b07ef2485b87d8970683afac6`; `git show` of both revisions confirms the row text is
byte-identical):

`| `verifiers/check_gate_registry.py` | gate | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |`

All execution in sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2RowCheckGateRegistry` (cloned from the
lane, checked out at `58db81c4`; two throwaway commits made only inside the sandbox and then abandoned —
the lane was never touched; `git status --porcelain` in the sandbox after final checkout: empty).

# Cell-by-cell verdicts

## Name — `verifiers/check_gate_registry.py` — HOLDS
Blob exists at `bf65974c` and at tip (it is in the `ls-tree` universe; the counter's own OK line names
it). Cell spelled identically to the path; `judge()` found exactly one matching row (a `mine != 1`
report would have printed `registry rows naming it: N`, observed only for the 21 unregistered files at
base `422ffd10`, not for this file).

## Kind — `gate` — HOLDS
PROTOCOL.md § Gate standard (`/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md:390-392`):
a gate "reads surfaces, compares them against expected values persisted in its own repo, and returns a
verdict. A tool that cannot fail is a probe." This script can fail and does: exit 1 observed at base
(`conformant 0 of 21`, below) and under the phantom probe (`phantom 1`, below). It is also the round's
declared C2 counter (`plans/round-54.md:39-44`). `gate` is the right kind.

## Entry command — `python3 -B verifiers/check_gate_registry.py --rev <rev>` — HOLDS
Ran exactly as declared (read-only: three `git` reads — `ls-tree`/`show`/`cat-file -e`,
`verifiers/check_gate_registry.py:71-99`; no writes found, see Write scope; no network; ~1 s).

- `--rev bf65974c…` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, EXIT=0.
- `--rev 58db81c4…` (tip) → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, EXIT=0.
- `--rev 422ffd10…` (base) → `gate registry rows conformant 0 of 21 lane verifiers; phantom 0`, EXIT=1 —
  matches the plan's recorded before-value (`plans/round-54.md:42-44`).

## Verdict map — `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS
- `0`: `main()` returns 0 iff `k == len(universe) and not phantom` (`:307`); observed at landed rev and
  tip. Meaning "clean" is real — no findings.
- `1`: `main()` returns 1 on any nonconformant row or any phantom (`:307`); `self_test()` returns 1 on
  assertion failures (`:269`). Observed at base rev and in the phantom probe. Meaning "failed" is real.
- `2`: `main()` returns 2 on `RuntimeError`/`UnicodeDecodeError`/`OSError` from `Tree` reads
  (`:284-294`, stderr line `could-not-evaluate: …`) and argparse `ap.error()` exits 2 (`:280`,`:283`).
  Observed: `--rev deadbeef…` → `could-not-evaluate: git ls-tree failed: fatal: not a tree object`,
  EXIT=2; no `--rev` → usage + `error: --rev is required`, EXIT=2; `--self-test --rev HEAD` → usage
  error, EXIT=2. Meaning "could-not-evaluate" is real.
- No produced code missing: `sys.exit(main())` (`:311`) yields only {0,1,2}; argparse adds 2 (`error`)
  and 0 (`-h`). Short registry rows cannot crash the run — `registry_rows()` pads every row to 8 cells
  (`:137`, `c + [""] * (len(HEADER) - len(c))`), and my sandbox commit replacing this row with a 3-cell
  truncated row was judged nonconformant (`conformant 23 of 24`, EXIT=1), not a traceback. Phantom rows
  are detected and force exit 1 even at K=M (`:197-199`,`:307`): sandbox commit adding
  `verifiers/zz_phantom.py` row → `PHANTOM verifiers/zz_phantom.py` + `phantom 1`, EXIT=1.
  Residual (informative only, no break): SIGINT→130 and `BrokenPipeError`→1 are the only
  non-{0,1,2}-mapped outcomes; 130 is covered by the registry preface rule "an undeclared nonzero code
  reads as could-not-evaluate" (`SKILL.md:450-451`); `-h`→0 falls on `0=clean` (argparse convention,
  shared by every argparse-based row in this table — not a defect this row can fix without intercepting
  `-h`).

## Self-test — `--self-test` — HOLDS
The flag is the script's own self-test: argparse flag at `:276` dispatches to in-file `self_test()`
(`:203-269`), which exercises `judge()`/`registry_rows()` over 22 in-memory fixtures asserting expected
per-verifier verdicts and phantom lists against committed literals (independent of recomputation — the
expected values are hard-coded tuples, not re-derived). Ran: `python3 -B verifiers/check_gate_registry.py
--self-test` → `self-test: 0 failure(s) over 22 assertions`, EXIT=0. Not a nested call, not usage text;
no writes (pure in-memory `judge` calls — sandbox working tree clean afterward). Nuance vs. PROTOCOL
`:398-399` ("asserting both the exit code and a stable expected finding-id"): the assertions are on
verdict outcomes (conformant lists/phantom lists), which *are* stable finding-ids; `main()`'s exit-code
mapping is one line (`:307`) and not directly invoked. Recorded as observation; the row cell itself
(flag spelling) is accurate.

## Pinned values — `in-file` — HOLDS
`in-file` is true and the values are actually read as expected values: `HEADING`/`HEADER` (`:60-62`) pin
the registry section and header shape used by `registry_rows()` (`:118-132`); `KINDS`, `CLASSES` (via
`PAIR_RE`), `OWNER` (`:63-66`) pin allowed cell vocabulary checked in `judge_row()` (`:144`,`:148`,`:180`);
the self-test's expected tuples (`:229-266`) pin judge behavior. Gate rule "a `gate` may not say `none`"
(docstring `:34`) satisfied.

## Write scope — `none` — HOLDS
Full read of the source: no `open(`, `.write(`, `tempfile`, `mkdir`, `remove`, `shutil`, `unlink`
anywhere (grep over the file: no matches). Subprocess surface is `git()` (`:71-72`) invoked only with
`ls-tree`, `show`, `cat-file -e` (`:82`,`:95`,`:99`) — read-only plumbing. `-B` suppresses `__pycache__`.
Sandbox `git status --porcelain` after all runs: empty. `none` is exact.

## Owner — `kotoba` — HOLDS
Matches the pinned `OWNER = "kotoba"` (`:65`,`:180`) and the lane.

# Attacks run and results

| Attack | Result |
|---|---|
| Run entry command at landed rev `bf65974c` | `conformant 24 of 24 … phantom 0`, exit 0 — HOLDS |
| Run entry command at tip `58db81c4` | `conformant 24 of 24 … phantom 0`, exit 0 — HOLDS |
| Run entry command at base `422ffd10` | `conformant 0 of 21 … phantom 0`, exit 1 — before-value reproduced |
| Run `--self-test` | `0 failure(s) over 22 assertions`, exit 0 — genuine in-file self-test |
| Bad rev `deadbeef…` | `could-not-evaluate: git ls-tree failed…`, exit 2 |
| Missing `--rev`; `--self-test --rev` combo | argparse usage error, exit 2 (both) |
| Truncate this row to 3 cells (sandbox commit) | judged nonconformant, `23 of 24`, exit 1 — no crash (rows padded at `:137`) |
| Insert phantom row `verifiers/zz_phantom.py` (sandbox commit) | `PHANTOM` line, `phantom 1`, exit 1 even at K=M |
| `-h` | exit 0 (argparse convention; maps onto declared `0=clean` — observation only) |
| `--json` tail | JSON then summary line — consistent with sibling counters' shape; not a row defect |
| Write-scope sweep | grep for write calls: none; sandbox tree clean after runs |
| Frozen-counter check | counter body byte-identical at `e33715486a` plan commit and tip (Q28): `git diff e33715486a45a4a857b64c30e6b695f7995858b8 58db81c4 -- verifiers/check_gate_registry.py` produced no output |

# Residual risk / verification gaps

- The verdict map cannot distinguish "script crashed" from "verdict failed" for `BrokenPipeError`
  (exit 1 on truncated stdout). Environmental, unobserved in practice; shared by every lane verifier.
- `--rev` accepts moving refs at runtime (e.g. `HEAD` resolved fine in probes); the registry preface's
  "full hash, never a moving ref" is a usage convention the script does not enforce. Documentation-level
  only; no row cell claims otherwise.
- The self-test asserts judge outcomes, not `main()`'s literal exit-code return — see the Self-test
  cell note. PROTOCOL-strict reading only; the row makes no claim beyond the flag spelling.

# Proposed corrected row

None — no cell breaks.

# Install log

No tools installed; stock `python3` and `git` sufficed.
