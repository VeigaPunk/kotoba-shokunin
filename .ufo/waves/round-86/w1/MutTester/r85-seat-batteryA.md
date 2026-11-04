# r85 MutTester seat — mutation battery A on the amended C1 counter (b9ee5484)

Out-of-wave seat, revived by a mis-addressed dispatch. Scope: battery A only, on
`verifiers/check_omp_catalogue_repro.py` as amended by
`b9ee5484a139c4428a2d53e572868abe86844821` (addendum 1; `plans/round-86-addendum-1.md`;
counter sha256 `39a014f2…`, self-test 46 assertions). Production files were read, never written.

## Method

* Frozen detector: `git -C <lane> show b9ee5484:verifiers/check_omp_catalogue_repro.py` →
  sha256 `39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520` (identical to the
  lane working-tree file at run time).
* The copy is placed at `<scratch>/repo/verifiers/check_omp_catalogue_repro.py` so the counter's
  `REPO = HERE.parent` resolves inside the scratch clone and the self-test's synthetic worlds
  (under `TMPDIR`, outside `<scratch>/repo`) keep G2 clean. A copy outside that shape fails four
  arms spuriously (G2 "resolves inside" the counter's own REPO) — a harness artefact, not a defect.
* Detector command, identical for pristine and every mutant:
  `TMPDIR=<scratch>/tmp python3 -B <scratch>/repo/verifiers/check_omp_catalogue_repro.py --self-test`
* One single-point mutant at a time, applied by exact string replacement (anchor asserted unique),
  run, then the pristine bytes rewritten and the sha256 re-verified before the next mutant.

Pristine: exit 0, `0 failure(s) over 46 assertions`.

## Table A — 26 single-point mutants (killed = the self-test fails)

| mutant | removes | observed | verdict |
|---|---|---|---|
| `A01-g1-disabled` | G1 no-echo guard call | 4 failure(s) over 46 assertions (FAIL echo forgery exit 1; FAIL echo forgery G1 FAIL) | killed |
| `A02-g2-disabled` | G2 provenance guard call | 6 failure(s) over 46 assertions (FAIL provenance exit 1; FAIL provenance G2 FAIL) | killed |
| `A03-g3-pin-dropped` | G3 fixture-pin test | 2 failure(s) over 46 assertions (FAIL fixture pin exit 1; FAIL fixture pin G3 FAIL) | killed |
| `A04-g3-total-dropped` | G3 entry-count (TOTAL) test | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A05-g4-disabled` | G4 roots guard call | 16 failure(s) over 46 assertions (FAIL w_noledger exit 1; FAIL w_noledger G4 FAIL) | killed |
| `A06-threshold-dropped` | the 205 (TARGET) threshold | 6 failure(s) over 46 assertions (FAIL empty roots exit 1; FAIL wrong floor exit 1) | killed |
| `A07-hide-emptied` | the whole default hide list | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A08-scratch-emptied` | the default scratch list | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A09-ctime-dropped` | the post-render mtime/ctime test | 2 failure(s) over 46 assertions (FAIL post-render file exit 1; FAIL post-render file G2 FAIL) | killed |
| `A10-g4-quote-location-dropped` | G4 quote-located-in-ELF test | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A11-g4-pattern-match-always-true` | G4 root-matches-a-pattern test | 2 failure(s) over 46 assertions (FAIL w_otherroot exit 1; FAIL w_otherroot G4 FAIL) | killed |
| `A12-cache-precedence-swapped` | cache-row precedence over the preview | 4 failure(s) over 46 assertions (FAIL good world exit 0; FAIL good world 3 of 3) | killed |
| `A13-render-compare-stripped` | exact render equality (loosened to strip()) | 0 failure(s) over 46 assertions — not-exploited (masked by the preview reference check) | survived |
| `A14-dir-name-dropped` | the parent-side dir-name check | 1 failure(s) over 46 assertions (FAIL one-path forgery dir-name MISS) | killed |
| `A15-desc-in-file-dropped` | the parent-side desc-in-file check | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A16-key-reference-dropped` | the parent-side omp_key reference check | 0 failure(s) over 46 assertions — not-exploited (no forgery path) | survived |
| `A17-preview-reference-dropped` | the parent-side preview reference check | 4 failure(s) over 46 assertions (FAIL wrong floor exit 1; FAIL wrong floor below 3) | killed |
| `A18-pattern-first-segment-wildcard-dropped` | _pattern_problem first-segment wildcard branch | 0 failure(s) over 46 assertions — not-exploited (another branch still refuses it) | survived |
| `A19-pattern-dot-wildcard-dropped` | _pattern_problem dot-segment wildcard branch | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A20-pattern-no-dot-dropped` | _pattern_problem no-dot-directory branch | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A21-pattern-quote-names-dot-dropped` | _pattern_problem quote-names-the-dot-segment branch | 2 failure(s) over 46 assertions (FAIL w_quotemiss exit 1; FAIL w_quotemiss G4 FAIL) | killed |
| `A22-pattern-no-directory-dropped` | _pattern_problem empty-pattern branch | 0 failure(s) over 46 assertions — regression-not-forgery | survived |
| `A23-rebind-widened` | the narrow rebind allowlist (binds all of ~/.omp back) | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A24-unshare-net-dropped` | the network namespace | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A25-clearenv-dropped` | the cleared environment | 0 failure(s) over 46 assertions — EXPLOITED | survived |
| `A26-unshare-pid-dropped` | the pid namespace | 0 failure(s) over 46 assertions — EXPLOITED | survived |

11 killed, 15 survived.

## Table B — survivors: does a real world exploit the removed check?

Paired run, same world, pristine copy vs mutant copy. `EXPLOITED` = the mutant accepts a forgery
the pristine counter refuses.

| survivor | exploit world | pristine | mutant |
|---|---|---|---|
| `A04-g3-total-dropped` | 205-entry fixture (TOTAL 215) scores as if complete | `{"rc": 1, "lines": ["guard G3 fixture FAIL (1): fixture sha256 x entries 205", "omp catalogue lines reproduced 205 of 20` | `{"rc": 0, "lines": ["guard G3 fixture PASS", "omp catalogue lines reproduced 205 of 205"]}` |
| `A07-hide-emptied` | module lists ~/.omp/logs (Sentinel-3 request dumps carry all 215 renders) | `"/probe--1"` | `"/probe-16524"` |
| `A08-scratch-emptied` | forged SKILL.md files written under the scratch tree reproduce renders | `{"rc": 1, "lines": ["guard G2 provenance FAIL (2): alpha: /fast/scratch/hyaku/kotoba-r86/MutTester/expl/wtmp/w-gzmz0xdi/` | `{"rc": 0, "lines": ["guard G2 provenance PASS", "omp catalogue lines reproduced 2 of 2"]}` |
| `A10-g4-quote-location-dropped` | ledger cites an invented quote that names the dot directory | `{"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: quote not located in the omp binary ('\".fakeclient\" is th` | `{"rc": 0, "lines": ["guard G4 roots PASS", "omp catalogue lines reproduced 2 of 2"]}` |
| `A13-render-compare-stripped` | module preview differs from the reference only by whitespace | `{"rc": 1, "lines": ["MISS beta preview-differs-from-reference", "omp catalogue lines reproduced 1 of 2"]}` | `{"rc": 1, "lines": ["MISS beta preview-differs-from-reference", "omp catalogue lines reproduced 1 of 2"]}` |
| `A15-desc-in-file-dropped` | module returns out-of-band descriptions while the files carry decoys | `{"rc": 1, "lines": ["MISS alpha desc-not-in-file", "MISS beta desc-not-in-file", "omp catalogue lines reproduced 0 of 2"` | `{"rc": 0, "lines": ["omp catalogue lines reproduced 2 of 2"]}` |
| `A16-key-reference-dropped` | module's omp_key is not the reference port (cache lookup lost) | `{"rc": 1, "lines": ["MISS alpha key-differs-from-reference", "MISS beta key-differs-from-reference", "omp catalogue line` | `{"rc": 0, "lines": ["omp catalogue lines reproduced 2 of 2"]}` |
| `A18-pattern-first-segment-wildcard-dropped` | ledger row '*' with quote 'loadSkillsFromDir(".fakeclient")-QUOTE' | `{"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: pattern '*' has a wildcard in its first segment", "omp cata` | `{"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: pattern '*' names no literal dot-directory", "omp catalogue` |
| `A19-pattern-dot-wildcard-dropped` | ledger row '/fast/scratch/hyaku/kotoba-r86/MutTester/expl/wtmp/w-91v3op6u/.*/skills' with quote 'loadSkillsFromDir(".*")-QUOTE' | `{"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: pattern '/fast/scratch/hyaku/kotoba-r86/MutTester/expl/wtmp` | `{"rc": 0, "lines": ["guard G4 roots PASS", "omp catalogue lines reproduced 2 of 2"]}` |
| `A20-pattern-no-dot-dropped` | ledger row '/fast/scratch/hyaku/kotoba-r86/MutTester/expl/wtmp/w-91v3op6u/plain/skills' with quote 'loadSkillsFromDir(".fakeclient")-QUOTE' | `{"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: pattern '/fast/scratch/hyaku/kotoba-r86/MutTester/expl/wtmp` | `{"rc": 0, "lines": ["guard G4 roots PASS", "omp catalogue lines reproduced 2 of 2"]}` |
| `A22-pattern-no-directory-dropped` | pattern '/' reaches _pattern_problem with no segments | `{"result": "pattern '/' names no directory", "guard_g4": {"rc": 1, "lines": ["guard G4 roots FAIL (3): ledger line 2: pa` | `{"raised": "IndexError", "detail": "list index out of range", "guard_g4": {"raised": "IndexError", "detail": "list index` |
| `A23-rebind-widened` | module lists ~/.omp/logs under the widened allowlist | `"/probe--1"` | `"/probe-16524"` |
| `A24-unshare-net-dropped` | connect to a local listener from inside the sandbox | `"/net-0"` | `"/net-1"` |
| `A25-clearenv-dropped` | read a parent environment variable inside the sandbox | `"/env-0"` | `"/env-1"` |
| `A26-unshare-pid-dropped` | count /proc pids inside the sandbox | `"/proc-2"` | `"/proc-2771"` |

## Named counter defects (survivors), by class

**Self-test coverage defects — load-bearing check, no assertion covers it (11).**
Removing or breaking each lets a real forgery through while the self-test still prints
`0 failure(s) over 46 assertions`:

1. `A04` G3's `len(entries) == TOTAL` test — a 205-entry fixture scores as a complete catalogue
   (`guard G3 fixture FAIL (1): … entries 205` → `PASS`, exit 0).
2. `A07` the `~/.omp` entry of `default_hide()` — the sandboxed module lists `~/.omp/logs`
   (`/probe--1` → `/probe-16524`; Sentinel-3's request dumps carry the renders).
3. `A08` `default_scratch()` — forged SKILL.md files under the scratch tree reproduce renders
   (G2 `resolves inside` FAIL → PASS, exit 0).
4. `A10` G4's quote-located-in-ELF test — an invented quote that names the dot directory is
   accepted (`quote not located in the omp binary` → `guard G4 roots PASS`, exit 0).
5. `A15` `predict`'s desc-in-file test — a module returning out-of-band descriptions while the
   files carry decoys reproduces 2 of 2, exit 0 (pristine: `desc-not-in-file`, 0 of 2).
6. `A19` `_pattern_problem`'s dot-wildcard branch — `…/.*/skills` with the quote
   `loadSkillsFromDir(".*")-QUOTE` is accepted (pristine: `has a wildcard in a dot-directory
   segment`).
7. `A20` `_pattern_problem`'s no-dot branch — a root with no dot-directory (`…/plain/skills`) is
   accepted (pristine: `names no literal dot-directory`).
8. `A23` the narrow `default_rebind()` — widening it to `~/.omp` binds the whole hidden tree back
   (`/probe--1` → `/probe-16524`): the allowlist, not the hide list, is what keeps `~/.omp` out.
9. `A24` `--unshare-net` — the sandboxed module connects to a local listener (`/net-0` → `/net-1`).
10. `A25` `--clearenv` — the sandboxed module reads a parent environment variable
    (`/env-0` → `/env-1`).
11. `A26` `--unshare-pid` — the sandboxed module sees host pids (`/proc-2` → `/proc-2771`).

**Uncovered but not forgeable (3).** `A13` exact render equality → `strip()`: unreachable — the
parent-side preview reference check rejects any whitespace-variant preview first (pristine and
mutant both read `MISS beta preview-differs-from-reference`, 1 of 2). `A16` the `omp_key` reference
check: the parent derives the key itself, so the module's key value never reaches a render and
dropping the check cannot move N (mutant 2 of 2, exit 0); it only stops testing that the module
ports omp 18.15.0 `A(e)`. `A18` the first-segment wildcard branch: the `*` row is still refused by
the no-dot branch (`names no literal dot-directory`) — defence in depth.

**Robustness regression (1).** `A22` the empty-pattern branch: pattern `/` is reachable through
`guard_g4` (non-empty first cell), and without the branch `_pattern_problem` raises
`IndexError: list index out of range` — a traceback instead of the clean
`pattern '/' names no directory` refusal.

**Killed and therefore asserted (11).** G1 no-echo, G2 provenance and the ctime test, G3's pin
test, G4's guard call, its root-match test and its quote-names-the-dot branch, the 205 threshold,
cache precedence, the dir-name check, the preview reference check.

## Reproduction

Mutant runs: the command above, with the copy rewritten per row; each row's exit status and failure
lines are in Table A, and the pristine sha256 was re-verified after every mutant (all restorations
equal to `39a014f2…`). Exploit rows: the pristine and mutant copies were loaded as modules and their own
`score()` / `run_module()` called on one synthetic world (`TOTAL=TARGET=2`, root
`<world>/.fakeclient/skills`, ledger quote `loadSkillsFromDir(".fakeclient")-QUOTE` located in a
synthetic ELF blob; the A04 world uses 205 entries with `TOTAL=215, TARGET=205`).

## Bounds

* This battery mutates the counter, not the candidate model. The counter's own self-test is the
  detector, so a survivor names a missing assertion, not a present production bug.
* `A07`/`A23` count entries under `~/.omp/logs` on this host (16,5xx); the absolute number moves
  with the host's log volume — the invariant is hidden (`-1`) vs a positive count.
* The exploit worlds are synthetic (2–205 entries, synthetic ELF blob), not the 215-entry fixture;
  they show each check's load-bearing role, not a score against the real catalogue.

## Cleanup

Scratch (`/fast/scratch/hyaku/kotoba-r86/MutTester`) deleted after this report was written. No tool
installed or upgraded. No production file, no lane file outside this report, and no
`/home/vgpnk/.local/bin` path was written.
