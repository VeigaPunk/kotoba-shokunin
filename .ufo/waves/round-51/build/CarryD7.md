# CarryD7 — round-51 build seat (routed defect D7: carried items)

**Result: OPEN ×7 — every D7 item is still open at base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`; I reproduced the two C2 laundering arms and three crash paths at base bytes, so they are confirmed, not merely re-read.** Calibration note: the round-50 bound "two crash paths" undercounts — three are confirmable at base and a fourth (subprocess timeout/`OSError`) remains unrun.

Seat `KotobaR51.CarryD7` (UFO-FSD scout, leaf, no delegation), 2026-10-22. Lane read-only except this
report; every mutation is in `/fast/scratch/hyaku/kotoba-r51/build/CarryD7/lane` (clone at `43ca0bfb`,
branches `probe-base 1da5e22`, `probe-dup c3c766a`, `probe-twin 617bb63`, `probe-advb 89f6a71`). No jj
command anywhere; no git write outside the clone.

## Why the round-50 numbers still describe the base bytes (one command)

    git diff --stat 956ee1676e4c18480bce8ac3993541462be76e11 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 -- verifiers/
    → verifiers/corpus-baseline.json | 5 +++--   (1 file changed; exit 0)

So the instrument, driver and guard the round-50 seats measured are the base files:
`box_proof_case_deletion.py` sha256 `e09a402f…` (equal to `git show 956ee:… | sha256sum`),
`verify_dispatch_prompts.py` `de960271…` (equals `MutBoxProofCode`'s restoration digest),
`check_sibling_census.py` `2f9d8a88…` (equals `MutGuardCode`'s pristine digest).

## Item-by-item re-confirmation

| # | item | base state | open? |
|---|---|---|---|
| 1 | C2 driver laundered by duplicate-id or unlabelled twins | `attempt()` filters `and c.get("id") == cid` (line 285), `pool = must_fail or holders` (308). Duplicate-id twin → `killed 6 of 6`, exit 0, while deleting one twin alone → `boxes proven 2`, exit 0. Stripped label + unlabelled twin → `--in-place` `killed 6 of 6` exit 0 (the sixth kill is the N/A case); default mode crashes | **open**, reproduced |
| 2 | kill test is a stderr substring | `named = any(name and name in stderr for name in names)` (line 205), whole-stderr, any line. An instrument that fails on any reduced manifest and names all six conjuncts on stderr → `killed 6 of 6`, `controls killed 2 of 2`, `na killed 1 of 1`, exit 0 | **open**, reproduced |
| 3 | crash paths | (a) unknown rev: `tarfile.open` (131) runs before the git return-code check (141) and only `DriverError` is caught (239) → `tarfile.ReadError: empty file`, exit 1, no `ERROR` line. (b) malformed manifest: `read_manifest` (254) is outside the `try` → uncaught `DriverError: cannot parse …`, exit 1. (c) duplicate work directory: `work = tmpdir / ("fixtures-%s" % cid)` (288) → `FileExistsError: … 'fixtures-d08-missing-state'`, exit 1, no `killed` line | **open**, (a)(b)(c) reproduced; `ReviewDriver` F5 (timeout/`OSError`) still unrun |
| 4 | 7 of 17 instrument mutants survive the driver | `return 0 if killed == 6 else 1` (344); `controls killed` / `na killed` are printed and never read. Survivors M09, M10, M12, M13, M14, M16, M17 = 7 of 17 | **open** (bytes identical) |
| 5 | 11 of 28 census-guard mutants survive the self-test | guard self-test prints `self-test: 0 failure(s) over 68 assertions`, exit 0 (the `MutGuardCode` baseline); survivors reported with shown behaviour differences for F2–F7 | **open** (bytes identical) |
| 6 | `box_proof_case_deletion.py` absent from `verifiers/floors-registry.json` | `grep -c box_proof_case_deletion verifiers/floors-registry.json` → `0` (exit 1); registry `instrument_total` 11 over 11 rows; no script, gate or CI file invokes the driver (`grep -rln … --include='*.py' --include='*.sh' --include='*.json'` → the driver and four round-50 wave specs only) | **open** |
| 7 | four `FloorsRegister` arms F30–F33 unapplied | `grep -c F30 verifiers/check_assertion_floors.py` → 0; guard self-test `0 failure(s) over 150 assertions` (the patch's count is 169); no arm exercises the `sibling_census` registry row. The round-50 patch still exists and `git apply --check /fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/patch.diff` → exit 0 at base | **open** (patch ready) |

## Reproductions at base (verbatim outputs)

- `probe-dup c3c766a` (append a second `d04-stem` entry, nothing else):
  `python3 -B verifiers/box_proof_case_deletion.py --rev HEAD --repo .` → `killed 6 of 6`, exit 0.
  Falsifier on the same revision: fixtures copy with exactly one `d04-stem` removed →
  `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json --fixtures <copy>`
  → `boxes proven 2`, exit 0. So "deleting any one of the 6 must-fail cases exits 1" is false for that manifest.
- `probe-twin 617bb63` (strip `expect_conjunct`/`expect_conjunct_status` from `d08-above-state`, add unlabelled `d08-above-twin`):
  default mode → `FileExistsError` traceback at `shutil.copytree` (line 288), exit 1, no `killed` line;
  `--in-place` → `case d08-missing-state (round_le_latest_dispatched): exit 1 killed` … `killed 6 of 6`, exit 0;
  falsifier: fixtures copy without `d08-above-state` (twin kept) → `boxes proven 2`, exit 0.
- `probe-advb 89f6a71` (instrument returns 1 with six `no isolated must-fail case for conjunct <name>` stderr lines whenever the manifest holds fewer than 9 cases):
  intact → `boxes proven 2`, exit 0; driver → `killed 6 of 6`, `controls killed 2 of 2`, `na killed 1 of 1`, exit 0.
  The driver cannot separate a conjunct-specific failure from a generic one (this is `ReviewDriver` F1's advB, reconfirmed).
- `probe-base` → `--rev 0000…0` → `tarfile.ReadError: empty file`, exit 1; and with manifest `{"cases": [` →
  `DriverError: cannot parse /tmp/…/manifest.json (Expecting value: line 2 column 1 (char 12))`, exit 1.

## Carry lines

- **CARRY D7.1 — C2 driver laundering (duplicate-id / unlabelled twins).** Open at `43ca0bfb` because `attempt()` deletes every entry sharing the id and the conjunct pool falls back to `must_fail or holders`; both arms reproduce a false `killed 6 of 6`. Fixing needs the counter to exit 2 when the manifest carries duplicate ids or a deletion would remove more than one entry, and to drop the `or holders` fallback so an unlabelled conjunct prints `survived (absent)`.
- **CARRY D7.2 — substring kill test.** Open because a kill is scored by `name in stderr` over all of stderr; an instrument with a generic or hash-pin failure passes with 6 of 6. Fixing needs the driver to require the instrument's own per-case problem line (`box-proof: <box>: no isolated must-fail case for conjunct <name>`) with the box id on the same line, and a pre-scoring twin-then-delete probe through the CLI so an instrument that fails on any manifest change is refused before a count is printed.
- **CARRY D7.3 — crash paths (three, not two).** Open: unknown rev, malformed manifest and the duplicate work-directory all exit 1 with a traceback and no `ERROR … not measurable` line. Fixing needs the git return code checked (or `git cat-file -e <rev>^{commit}`) before `tarfile.open`, `read_manifest` moved inside the `DriverError` handler or `main`'s body wrapped after export, one work directory per attempt (counter index), and `subprocess.TimeoutExpired`/`OSError` handled in `run_box_proof` (still unrun, `ReviewDriver` F5).
- **CARRY D7.4 — 7 of 17 instrument mutants survive the driver.** Open: the counter's exit code reads only `killed == 6`; control and N/A deletion counts are printed and ignored (M09, M10, M17), and the observation rule plus the `EnvError` arm have no counter arm (M12, M13, M14, M16). Fixing needs the exit code to gate `controls_killed`/`na_killed` and two discriminating CLI arms, an unreadable-fixture probe for the `EnvError` path, and the `MutBoxProofCode` table rerun as a floor.
- **CARRY D7.5 — 11 of 28 census-guard mutants survive the self-test.** Open: the guard's battery never asserts the semicolon split (K2), the `NOT` rule (M3/M4), the `route` marker (M2), `any` vs `all` (M6), the value-end rule for a column-0 non-comment line (S2), or that the non-`none` set cannot silently become empty (C4, a vacuous pass). Fixing needs those fixture arms, then the `sibling_census` floor re-measured at the landing tree (68 at base) and re-bumped in all carriers in the same change.
- **CARRY D7.6 — the C2 counter is unregistered.** Open: the registry has 11 classes and no row for `box_proof_case_deletion.py`, and nothing imports or runs it, so a broken counter fails no gate. Fixing needs a `--self-test` on the driver that prints `N failure(s) over M assertions` (it has none today), a registry row (path + floor), the same row in `EXPECTED_INSTRUMENTS` and `INSTRUMENTS`, the guard docstring's floor list, and `instrument_total` 11 → 12.
- **CARRY D7.7 — `FloorsRegister` arms F30–F33 unapplied.** Open: the guard's self-test is 150 assertions at base and no arm exercises the `sibling_census` registry row, so a half-bump of the newest row would pass silently. Fixing needs the round-50 patch applied (`git apply --check` exit 0 at base; `check_assertion_floors.py` +110/−2, registry `floors_guard` 150 → 169), the `sibling_census` floor taken from the landing tree, and the guard rerun to `169 assertions` with 11 × PASS.

## SCORECARD § planned "Next: round 51" — round-48/49 candidates and status

`SCORECARD.md:122` names four candidates. Three trace to rounds 48–49:

| candidate | origin | state at base | open? |
|---|---|---|---|
| omp 18.12.6 re-pin (open Q09 debt; new callees `Kl`, `Ho`, `bq`, an `S$` rebind) | round 48 (`Q09` first recorded as debt in `SCORECARD.md:112` "Next: round 49") | `python3 -B verifiers/check_substrate_pins.py` → `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`, exit 1 (installed sha256 `85d9daf3…`, pin `fdbc8136…`) | open, and claimed this round as C1 (build seat `PinsRepin`) |
| v2 configured-root oracle (R5) | round 49 (`.ufo/waves/round-49/build/R5Disposition.md`) | `grep -rln 'configured-root-oracle-v2'` → `R5Disposition.md`, `CarryD6.md`, `ReviewR6Carry.md` only; `.ufo/round-50/oracle` absent — no frozen v2 file | open; no round-51 claim covers it, so it stays open |
| R1's no-name fallback | round 49 (`MutR1Keying`, carried by `CarryD6`) | `sha256sum verifiers/verify_harness_independent.py` → `54f9c95b…`, the digest `CarryD6` recorded, so the bytes are unchanged; the skip-vs-bounded-divergence decision is still open | open; not claimed this round |

The fourth candidate (`CriticC1Sizing` G3, a pinned owner phrase per `adjacent` row) is a round-50
item, not 48/49: `grep -c -i 'owner.phrase' PROVINCE.md` → 0, and no round-51 claim adds one. Open.

## Findings for the integrator

1. **The round-50 bound is accurate but one short on crash paths.** Three are reproducible at base
   (unknown rev, malformed manifest, duplicate work directory); `ReviewDriver` recorded two. Carrying
   "three" (with F5 unrun) is honest; carrying "two" would be a bound narrower than the measured set.
2. **The laundering arms are reproducibility-only risks today.** The landed manifest has 9 unique ids and
   one label per conjunct, so `killed 6 of 6` at base is genuine (`control: exit 0 boxes proven 2` in all
   my runs). The defect is future-tense: a later manifest edit can produce a false green with no gate
   noticing (D7.6).
3. **D7.7 is the cheapest item to close** — the patch applies cleanly at base and only needs the
   `sibling_census` floor read from the landing tree.
4. **Do not fold D7.4 and D7.6 together.** Registering the driver without a `--self-test` cannot be
   floored; the self-test is a prerequisite for the registry row, not a follow-up.

## Evidence (commands, exit codes)

    git -C lane checkout -q 43ca0bfb…                          → HEAD 43ca0bfb…, status 0 lines
    git -C lane diff --stat 956ee167… 43ca0bfb… -- verifiers/  → 1 file (corpus-baseline.json), exit 0
    sha256sum verifiers/box_proof_case_deletion.py             → e09a402f…, exit 0
    git show 956ee167…:verifiers/box_proof_case_deletion.py | sha256sum → e09a402f…, exit 0
    python3 -B verifiers/check_sibling_census.py --self-test    → 0 failure(s) over 68 assertions, exit 0
    python3 -B verifiers/check_assertion_floors.py --self-test  → 0 failure(s) over 150 assertions, exit 0
    grep -c box_proof_case_deletion verifiers/floors-registry.json → 0, exit 1
    python3 -c 'registry: instrument_total 11, 11 rows, no box_proof row'  → exit 0
    grep -rln box_proof_case_deletion --include='*.py' … --exclude-dir=.git . → driver + 4 wave specs, exit 0
    git apply --check /fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/patch.diff → exit 0
    git apply --stat  …                                        → check_assertion_floors.py +110/−2, floors-registry.json 2 lines
    driver on probe-dup c3c766a                                → killed 6 of 6, exit 0
    box proof on dup copy minus one d04-stem                   → boxes proven 2, exit 0
    driver (default) on probe-twin 617bb63                     → FileExistsError traceback, exit 1
    driver --in-place on probe-twin 617bb63                    → killed 6 of 6, exit 0
    box proof on twin copy minus d08-above-state               → boxes proven 2, exit 0
    driver on probe-advb 89f6a71                               → killed 6 of 6, controls 2 of 2, na 1 of 1, exit 0
    driver --rev 0000…0                                        → tarfile.ReadError, exit 1
    driver on malformed manifest                               → DriverError traceback, exit 1
    python3 -B verifiers/check_substrate_pins.py               → DRIFT 2/3, exit 1
    ls .ufo/round-50/oracle                                     → No such file or directory, exit 2
    sha256sum verifiers/verify_harness_independent.py          → 54f9c95b…, exit 0
    grep -c -i 'owner.phrase' PROVINCE.md                       → 0, exit 1

Tools installed or upgraded: none (python3 3.14.8 and git already present). Unrun: `ReviewDriver` F5
(subprocess timeout path), `MutBoxProofCode` M01–M17 rerun, `MutGuardCode` mutant rerun (bytes identical,
so both tables are cited, not re-executed).
