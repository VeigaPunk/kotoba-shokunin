Result: HOLDS — the C2 counter prints `gate registry rows conformant 24 of 24 lane verifiers; phantom 0` with exit 0 at both claim revisions (bf65974c, 58db81c4) and its erratum-2 guard holds: all four declared self-tests are each script's own, exit 0 at bf65974c and at the tip, with a clean negative control at 7ad05d34.

Seat: KotobaR54.W2RerunC2, round-54 falsify wave, 2026-10-22.
Method: every run that executes lane code ran in my sandbox clone
`/fast/scratch/hyaku/kotoba-r54/W2RerunC2` (cloned from the lane, checked out at
58db81c4465b0e9b07ef2485b87d8970683afac6; checkouts of older revs inside the clone only).
The lane itself saw read-only git only (log, ls-tree, rev-parse, cat-file, diff).
No tools were installed or upgraded (none needed). Sources: none fetched (no network claims made).

## 1. Counter re-runs (`verifiers/check_gate_registry.py --rev <r>`)

Command per revision (cwd = sandbox clone):

    python3 -B verifiers/check_gate_registry.py --rev <full-rev>; echo rc=$?

Observed (full stdout saved as c2run-<rev>.txt in the sandbox; stderr empty in all five runs —
no `could-not-evaluate` lines):

| rev | summary line (verbatim) | exit |
|---|---|---|
| 422ffd10 (base) | `gate registry rows conformant 0 of 21 lane verifiers; phantom 0` | 1 |
| e3371548 (plan) | `gate registry rows conformant 0 of 23 lane verifiers; phantom 0` | 1 |
| b55550b9 (self-tests) | `gate registry rows conformant 0 of 23 lane verifiers; phantom 0` | 1 |
| bf65974c (C2 registry) | `gate registry rows conformant 24 of 24 lane verifiers; phantom 0` | 0 |
| 58db81c4 (tip) | `gate registry rows conformant 24 of 24 lane verifiers; phantom 0` | 0 |

Independent M ground truth (my own count, not the counter's):

    git ls-tree <rev> verifiers/ | awk '$2=="blob" && $4 ~ /\.(py|sh)$/ {n++} END{print n+0}'

gives 21 / 23 / 23 / 23 / 24 / 24 for the six revisions above (7ad05d34 = 23 as well) —
identical to the M the counter printed at every revision. The M growth is accounted for:
+2 in the plan commit e3371548 itself (the two frozen counters live in `verifiers/`),
+1 in bf65974c (`verifiers/check_sources_append_only.py` is new there:
`git diff --stat b55550b9..bf65974c -- verifiers/` shows exactly one file, 189 insertions,
0 deletions). The pre-registry runs print `no registry rows naming it: 0 (need 1)` per verifier
(e.g. c2run-422ffd1….txt line 21), consistent with "SKILL.md has no `## Gate registry`" before bf65974c.

The base before-value in the plan (`conformant 0 of 21 … phantom 0`, exit 1) reproduced exactly.
Note: the counter file does not exist at 422ffd10 (created in plan commit e3371548; `git rev-parse
422ffd10:verifiers/check_gate_registry.py` fails with "exists on disk, but not in …"), so the base
is necessarily scored by the counter from a later checkout with `--rev` — the same frozen blob
(d3e82a2b…, §2), so the measurement is the declared one.

## 2. Counter frozen (byte-identical e3371548 → tip)

    git rev-parse <rev>:verifiers/check_gate_registry.py

= `d3e82a2b914e2530cbb461ea6c9ed156503ec155` at e3371548, 7ad05d34, b55550b9, bf65974c and
58db81c4 (identical blob = identical bytes). `git diff --stat e3371548..58db81c4 --
verifiers/check_gate_registry.py` is empty (rc=0, no output). One commit touches the file in its
whole history: e3371548. Counter not widened. HOLDS.

## 3. Counter soundness spot-check (is it a real counter, not an echo?)

Read the source at the tip blob. It is substantive: universe from `git ls-tree` at the measured
rev (docstring "Universe (M)…", check_gate_registry.py:2-52); per-row conformance (kind, entry
command contains the path, verdict pairs with unique codes, gates need `0=clean`+`1=failed`,
self-test cell `none`/backticked flags occurring literally in the file bytes, pinned values
`none`/`in-file`/existing backticked paths, non-empty write scope, owner `kotoba`);
phantom = rows naming `verifiers/…` outside the universe; `return 0 if k == len(universe) and not
phantom else 1`. Its own self-test at the tip:

    python3 -B verifiers/check_gate_registry.py --self-test
    self-test: 0 failure(s) over 22 assertions
    rc=0

The discrimination observed in §1 (0 of M exit 1 before bf65974c; 24 of 24 exit 0 after) is what
the claim needs: the counter does not pass vacuously.

## 4. Erratum-2 guard at bf65974c (the four declared self-tests)

Sandbox clone checked out at bf65974c7845a06d7ef621ad998c6378ff735cd5; for each of
`box_proof_case_deletion.py`, `check_alwayson_boxes.py`, `check_callee_rename.py`,
`check_opencode_repin.py`:

    python3 -B verifiers/<script> --self-test; echo rc=$?

Observed, exit 0 all four, real in-file summaries:

    box_proof_case_deletion.py   self-test: 0 failure(s) over 10 assertions        rc=0
    check_alwayson_boxes.py      self-test PASS: counted box exit 0; missing delegate exit 1   rc=0
    check_callee_rename.py       PASS self-test robust case: strings-omp-clean.txt exit=0 finding=omp:rnplant/RNPLANT.md
                                 PASS self-test non-robust case: strings-omp-clean.txt exit=1 finding=self-test injected suppression
                                 self-test: 0 failure(s) over 2 assertions        rc=0
    check_opencode_repin.py      0 failure(s) over 2 assertions                    rc=0

Each is the script's OWN self-test — flag parsed by the script's own argparse and logic defined
in the same file (bf65974c blobs, line numbers): box_proof_case_deletion.py:225 (`add_argument("--self-test", …)`), :230 (`def self_test`), :376-378 (summary), :384 dispatch; check_alwayson_boxes.py:203, :205-208 (`return self_test()`, :96 def); check_callee_rename.py:44 (usage), :145 (`def self_test(seed)`), :217-219; check_opencode_repin.py:199, :202-203 (`return self_test()`, :87 def). The `subprocess` use inside them builds isolated fixture git repos and re-invokes the script itself — test fixtures, not delegation to another script's test. No borrowed flag: each row's declared flag `--self-test` is accepted by that script's argparse and triggers its in-file `self_test()` (a comment-only or borrowed literal would have exited 2 with an argparse error, as the negative control shows).

Registry rows agree with the guard's letter — at bf65974c, SKILL.md:
- :441 `verifiers/box_proof_case_deletion.py` — kind `gate`, self-test `` `--self-test` ``
- :442 `verifiers/check_alwayson_boxes.py` — kind `gate`, self-test `` `--self-test` ``
- :444 `verifiers/check_callee_rename.py` — kind `gate`, self-test `` `--self-test` ``
- :450 `verifiers/check_opencode_repin.py` — kind `gate`, self-test `` `--self-test` ``

No `probe` label, no borrowed flag on any of the four. Guard HOLDS.

## 5. Negative control (guard is non-vacuous) and drift

At 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39 (before b55550b9 added the self-test modes), same
sandbox, same command: all four exit 2 — matching erratum 2's "each exits 2 on `--self-test`"
(e.g. neg-box_proof_case_deletion.py.err: `box_proof_case_deletion.py: error: the following
arguments are required: --rev`). The guard can fail, and fails exactly where erratum 2 said.

At the tip 58db81c4: all four self-tests exit 0 again, and all four script blobs are identical
between bf65974c and tip (9328108d…, 871e8fba…, c903b5e0…, a3bd4038…), so no drift between the
guard revision and the tip.

## Verdicts

| attack | verdict |
|---|---|
| C2 statement at bf65974c and tip: exact string `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0, M = my independent blob count | HOLDS |
| Counter frozen at plan commit (byte-identical e3371548 → tip; no widening) | HOLDS |
| Counter discriminates (0 of 21 / 0 of 23 exit 1 before the registry; base before-value reproduced) | HOLDS |
| Counter's own `--self-test` (0 failures over 22 assertions, exit 0) | HOLDS |
| Erratum-2 guard: four own self-tests exit 0 at bf65974c, rows say `gate` + own flag, each flag is the script's own argparse | HOLDS |
| Guard non-vacuity (negative control at 7ad05d34, all exit 2) | HOLDS |

## Residual risk / verification gaps

- The counter's substring checks (self-test flag literal occurrence, entry-command substring) and
  case-insensitive row-name matching are bounded in plan erratum 2; exact flag matching is a
  later-round item because the counter is frozen (Q28). I verified genuine argparse wiring for the
  four guard scripts only; other rows' flags were not individually executed by this seat.
- Declared exit codes being actually produced, and `gate` vs `probe` being the right kind, are
  explicitly outside the counter and outside my item (other wave-2 seats run each script).
- The self-tests of `check_callee_rename.py` and `check_opencode_repin.py` declare only 2
  assertions each; their strength (can they be made to pass on a broken script?) is the mutation
  seats' scope. Identity, in-file wiring and exit 0 are what the guard requires, and those hold.
- `check_sources_append_only.py` enters the universe in bf65974c itself, the same commit that
  lands the registry; M=24 is therefore fully self-consistent at the claim revisions, but no
  revision exists where the counter scored 24-of-24 against a registry built before that verifier
  existed. [INFERENCE] Not a defect under the claim's wording (M is measured per revision), noted
  for calibration history.
