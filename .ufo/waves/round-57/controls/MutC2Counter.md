Result: BREAKS — 35 of 96 single-point mutants of the frozen C2 counter survive its `--self-test` (for 14 of them a run showed a hollow world exiting 0), and the unmutated frozen counter scored a 50-line stub that replaces the whole verifier at 120 of 120, exit 0.

# MutC2Counter — R5 guard-mutation check of `verifiers/check_infoless_fences.py`

- **Counter under test.** `verifiers/check_infoless_fences.py` at the freeze commit `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`. The counter prints `counter sha256 b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac`. This matches `git show ee50d8fa…:verifiers/check_infoless_fences.py | sha256sum`.
- **Sandbox.** `/fast/scratch/hyaku/kotoba-r57/MutC2Counter`, HEAD `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`.
- **Raw output.** `.ufo/waves/round-57/controls/MutC2Counter.txt`, sha256 `c3c49e75…a21aa`, 1401 lines.
- **Scripts.** In the sandbox under `mut/`:
  - `driver.py` `6be349c2…`
  - `demos.py` `a3294be4…`
  - `demos2.py` `6e8a0adb…`
  - `probe124.py` `0bdfa5c0…`
  - `stub_instrument.py` `dbb86ab4…`
- **Hollow worlds.** All are sandbox commits in `/fast/scratch/hyaku/kotoba-r57/MutC2Counter`, none meant for landing:
  - sandbox `23b527aae934532e80d90c032bf60b12f2c0d38c` (J): the instrument prints nothing.
  - sandbox `715766a3653a31c50e08c3b29d3702aa13fc714f` (X): the instrument is deleted.
  - sandbox `fa4a7e4f6894663a24300ec8a6bcc152246be733` (S): the whole verifier is replaced by a character-keyed stub. The stub answers only `trigger.command_binary_resolves`. Its rule is chosen by `KOTOBA_R57_MUT_MODE`, which the counter passes through in `env`.
  - sandbox `cf660f9235ae4a3461c5a0cbaf4272a62454271c` (Y): `verifiers/verify_skill_checklist.py` is an absolute symlink to that uncommitted stub.
  - Base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` is the lane commit, with the do-nothing instrument.

## Method

The detector was `timeout 300 python3 -B -P verifiers/check_infoless_fences.py --self-test`. Runs were sequential, one process at a time. For each mutant, `driver.py`:

1. asserts that the `old` text occurs exactly once in the frozen bytes;
2. checks that the sandbox counter's sha256 is `b3dbe72f…`;
3. writes the mutant in place and runs the detector;
4. restores the exact bytes in a `finally` block and re-checks the sha256;
5. runs the same detector on the restored bytes.

A mutant is **killed** if the mutated run exits non-zero. It **survived** if it exits 0. It is **inconclusive** if the pristine or restored run fails, or a hash differs.

- **Pristine baseline.** rc=0, `self-test: 0 failure(s) over 105 assertions`, 0.15 s.
- **Every restored run.** rc=0 with the same summary line. All 96 before and after hashes equal `b3dbe72f…`. Inconclusive count: 0.
- **Sweep.** Started 2026-10-23 04:24:38 UTC; 23.4 s wall time.
- **Measured runs.** `demos.py` and `demos2.py` ran 29 full measurements, one at a time, each under `timeout 300`. Mutated counters print their own sha256, which differs from `b3dbe72f…`. Every run tagged FROZEN printed `b3dbe72f…`.

## Mutation table

"Hollow meets?" asks whether a world that skips the claimed work could exit 0 if the counter had this defect. R-numbers refer to the measured runs in the raw output. Line numbers are the first line of the mutated text in the frozen file.

| id | mutant | line | verdict | hollow meets? |
|---|---|---|---|---|
| C01–C05 | P1…P5 expectation PASS→FAIL | 108–109 | killed (`hard-negative head is a drawn token`) | — |
| C06–C10 | H1…H5 expectation FAIL→PASS | 109–110 | killed (`pass cases carry exactly one real command`) | — |
| C11 | H3 class replaced by a second H1 | 109 | killed (`every (seed, class) has 4`) | — |
| C12 | `CASES_PER_CLASS` 4→3 | 105 | killed | — |
| C13 | `DEFAULT_SEEDS` (11,22,33)→(1,2,3) | 104 | **survived** | No [INFERENCE]. Same classes and T=120 on other seeds. The summary line does not print the seeds, so the drift would not show in a receipt. |
| C14 | bash tag moved from H5 to H4 | 368 | **survived** | **Yes.** R18: the colon-skip stub scores 120/120, exit 0. Frozen counter (R15): 108/120, all 12 H4 wrong. |
| C15 | every fence rendered without an info string | 394 | **survived** | No [INFERENCE]. H5 loses its shell-tag control, but P must still be told apart from H1–H4. |
| C16 | H4 built by the H1 builder | 356 | **survived** | **Yes.** R17: colon-skip stub 120/120, exit 0. |
| C17 | H4 `--opt=a:b` → `--opt=a-b` (colon dropped) | 346 | **survived** | **Yes.** R16: colon-skip stub 120/120, exit 0. |
| C18 | H2 `ls \| x` → `ls ; x` | 334 | **survived** | **Yes.** R20: pipe-skip stub 120/120, exit 0. Frozen counter (R19): 108/120, all 12 H2 wrong. |
| C19 | `REAL_COMMANDS` made unresolvable | 118 | **survived** | No [INFERENCE]. P becomes unreachable for a correct instrument, so the counter gets stricter, not looser. |
| C20 | P1 loses its real command | 291 | killed | — |
| D01 | drop `case.head in detail` | 455 | killed (`negative on FAIL without its head`) | — |
| D02 | `case.head not in detail` | 455 | killed | — |
| D03 | hard negative `status == "FAIL"` → `status != "PASS"` | 455 | **survived** | **Yes.** R22: the colon-echo stub answers N/A with the skipped lines echoed and scores 120/120, exit 0. Frozen counter (R21): 108/120. |
| D04 | `case.head[:4] in detail` | 455 | **survived** | No new path [INFERENCE]. Echoing the fence already satisfies `head in detail`. The FAIL/PASS split is the binding constraint. |
| D05 | any case token in detail | 455 | **survived** | No new path [INFERENCE], for the same reason. At base it would only credit the 12 H3 misses caused by truncation. |
| D06 | pass-expected `== "PASS"` → `!= "FAIL"` | 454 | killed | — |
| D07 | unparseable counted correct | 450 | killed | — |
| D08 | PASS/FAIL branches swapped | 453 | killed | — |
| S01 | bad JSON → `("PASS","")` | 428 | killed | — |
| S02–S04 | non-dict document / non-list checks / non-dict entry accepted | 430, 433, 436 | killed (crash) | — |
| S05, S06 | check-id test negated / dropped | 438 | killed | — |
| S07 | non-string status accepted | 441 | killed | — |
| S08 | no matching check → `("PASS","")` | 444 | killed | — |
| S09 | detail dropped | 444 | killed | — |
| S10 | `CHECK_ID` typo (`…_resolve`) | 116 | **survived** | No [INFERENCE, not run]. The instrument would be asked for a different check id. A hollow instrument still has to tell P from H. |
| T01 | `TimeoutExpired` → `("PASS","")` | 419 | killed | — |
| T02 | `CASE_TIMEOUT` 60→600 | 114 | killed (frozen argv arm) | — |
| T03 | 70 s subprocess backstop removed | 403 | **survived** | No [INFERENCE]. Affects liveness only: a stuck instrument hangs the counter, which never exits 0. |
| T04 | backstop shortened to 1 s | 403 | **survived** | No [INFERENCE]. Stricter: slow cases become wrong. |
| T05 | `timeout 60` wrapper dropped from argv | 413 | killed | — |
| T06 | `except TimeoutExpired` → `except OSError` | 419 | killed (crash) | — |
| P01 | drop `T >= 120` | 466 | killed | — |
| P02 | drop `N == T` | 466 | killed | — |
| P03 | `>=` → `>` | 466 | killed | — |
| P04 | `and` → `or` | 466 | killed | — |
| P05 | `N >= T-1` | 466 | killed | — |
| P06 | `N == T` → `N >= T` | 466 | **survived** | No. Equivalent mutant: N ≤ T by construction in `measure()`. |
| P07 | `MIN_TOTAL` 120→12 | 113 | killed | — |
| P08 | `main`: N summed from the totals (`pair[1]`) | 906 | **survived** | **Yes.** R02: the do-nothing base instrument prints `correct 120 of 120 (pass-expected 0 of 60; hard negatives 48 of 60)`, exit 0. |
| P09 | `main`: `total = len(cases) - len(wrong)` | 905 | **survived** | No. R06 prints `48 of 48`, exit 1. `T >= 120` still forces all 120 cases correct. |
| P10 | `main`: exit code inverted | 913 | **survived** | **Yes.** R04 prints `48 of 120`, exit 0. |
| P11 | `main`: `predicate_ok(total, total)` | 913 | **survived** | **Yes.** R05 prints `48 of 120`, exit 0. |
| P12 | `measure`: `if case_correct(…)` → `if True` | 498 | **survived** | **Yes.** R03: base instrument, `120 of 120`, 0 wrong lines, exit 0. |
| P13 | `measure`: verdict negated | 498 | **survived** | **Yes.** R08: empty-output junk J scores `120 of 120`, exit 0. Frozen counter (R07): `0 of 120`. |
| P14 | `measure`: per-class total not counted | 497 | **survived** | No [INFERENCE]. Only the printed PT/HT change; N and T do not. |
| P15 | `main`: environment failure returns 0 | 900 | **survived** | **Yes.** R10: with the instrument deleted (X), exit 0 and no summary line. Frozen counter (R09): exit 2. |
| P16 | `main`: own-sha failure returns 0 | 885 | **survived** | No practical path [INFERENCE]. It needs the counter's own file to be unreadable. |
| P17 | `main`: `--rev` format guard skipped | 894 | **survived** | No [INFERENCE]. The rev must still resolve, and N and T are still judged. |
| A01 | `measure` runs the working tree, not the extracted rev | 496 | **survived** | **Yes, given an uncommitted meeting instrument.** R25: base 47c05558 (do-nothing) scores 120/120, exit 0, and still prints the base `instrument sha256 629867d1…`. What ran was the uncommitted stub in the working tree. Frozen counter (R24): 48/120. |
| A02 | archive `HEAD` instead of the rev | 192 | **survived** | **Yes, given a meeting HEAD.** R27 measured junk J with sandbox HEAD = S. It printed `measured 23b527aa…` and scored 120/120, exit 0. Frozen counter (R26): 0/120. |
| A03 | instrument sha read from the working tree | 489 | **survived** | No [INFERENCE]. N and T are unchanged; only the printed sha could misname what ran. |
| A04 | tar filter `data` → `fully_trusted` | 206 | **survived** | **Yes.** R29: Y, whose only change is a symlink, scores 120/120, exit 0. Frozen counter (R28) refuses with `tarfile.AbsoluteLinkError`, exit 1. |
| A05 | rev-parse without `^{commit}` | 177 | **survived** | No [INFERENCE]. A tree hash would be accepted, but it is still judged on N and T. |
| A06–A12 | instrument absent; archive/rev-parse return code; output shape; 40-hex; empty rev; `{7,40}` regex | 120–212 | killed | — |
| A13 | tar extracted beside the executed path | 487 | **survived** | No [INFERENCE]. Every measured run would exit 2 because the instrument is absent. |
| I01 | one shared case dir | 408 | killed | — |
| I02 | cwd = work root (not empty) | 411 | killed (`runner: empty cwd`) | — |
| I03 | one shared, initially empty cwd | 411 | **survived** | No [INFERENCE]. Each case keeps its own `--repo` and `SKILL.md`. Cross-case state carries no expectation signal. |
| I04 | `PYTHONSAFEPATH` not set in `measure` | 492 | **survived** | No. Equivalent while argv keeps `-P`; I05, which drops `-P`, is killed. |
| I05 | `-P` dropped from argv | 413 | killed | — |
| I06 | dirname not recorded as taken | 371 | **survived** | No. Equivalent at seeds 11/22/33: the `dirname unique per seed` arm passed. |
| I07 | per-case token dedupe dropped | 375 | **survived** | No. Equivalent at these seeds: `tokens distinct within a case` passed. |
| I08 | `SKILL.md` not written | 410 | killed | — |
| I09 | shuffle dropped | 385 | killed | — |
| I10 | every seed uses `Random(0)` | 364 | killed | — |
| G01–G07, G09–G12 | token shape/taken/reserved/which/exhaustion; dirname taken/exhaustion; usage conflict; `guarded` exit 2; tools; own sha | 151–476 | killed | — |
| G08 | `RESERVED` loses `let` | 131 | **survived** | No [INFERENCE]. Data only; a drawn builtin would make a hard negative stricter, not looser. |

**Totals: 96 mutants — 61 killed, 35 survived, 0 inconclusive.** Of the 35 survivors:

- **14** were shown by a run to let a hollow world exit 0: C14, C16, C17, C18, D03, P08, P10, P11, P12, P13, P15, A01, A02, A04.
- **5** are equivalent or no-path, with run, arm or construction evidence: P06 (N ≤ T by construction), P09 (R06), I04 (argv keeps `-P`; I05 killed), I06 and I07 (their arms passed).
- **16** are no-path by reasoning only, marked [INFERENCE]: C13, C15, C19, D04, D05, S10, T03, T04, P14, P16, P17, A03, A05, A13, I03, G08.

I re-ran 32 of the w0 receipt's 34 guards in equivalent form: A06–A11, G01–G07, G09–G12, S01–S04, S06–S08, D01, D06, D07, P01, P02, T01, I09 and C12. All are killed, which agrees with `w0/ExecCounterC2.md`. I did not re-run `wrong-line-status`. My D03 is a narrower variant of w0's `verdict-negative-status`, and it survives. The gaps lie outside the w0 table:

- **`main()` and `measure()`.** The self-test reaches `measure()` only through `measure: git failure raises`, which raises before the case loop. It never calls `main()`. The w0 receipt explicitly excluded `if result is None: return code`, and P15 shows that line is exploitable.
- **Class-shape and tag details.** No arm checks that H4 carries a colon inside an argument, that H2 carries ` | `, that only H5 is tagged, or what the rendered fence line is.
- **One verdict polarity.** No arm checks a hard negative answered `N/A` with the head present.

## Findings on the frozen counter itself (unmutated, sha256 `b3dbe72f…`)

1. **The frozen C2 predicate is met by a hollow instrument (R23).**
   - **World:** sandbox `fa4a7e4f6894663a24300ec8a6bcc152246be733` (`/fast/scratch/hyaku/kotoba-r57/MutC2Counter`).
   - **Command:** `KOTOBA_R57_MUT_MODE=shape timeout 300 python3 -B -P verifiers/check_infoless_fences.py --rev fa4a7e4f6894663a24300ec8a6bcc152246be733`.
   - **Output:** `counter sha256 b3dbe72f…d1ac` / `measured fa4a7e4f…` / `instrument sha256 dbb86ab4…` / `info-less fence cases correct 120 of 120 (pass-expected 60 of 60; hard negatives 60 of 60)`, exit 0, 2.3 s.
   - **How:** the commit deletes the whole checklist gate. In its place, `verify_skill_checklist.py` is a stub (`mut/stub_instrument.py`) that answers only the measured check. For info-less fences it skips three kinds of line, taken from the counter's own class shapes: lines starting with `|` or `+`; lines containing U+2500–U+257F or U+2192; and lines whose first token ends in `:`. It then checks the first word of each `|`/`;`/`&&` segment with `shutil.which`.
   - **What stops it:** only the plan's out-of-counter guard (Q33). `python3 -B -P mut/stub_instrument.py --self-test` → `ValueError: list.index(x): x not in list`, exit 1. The base instrument's `--self-test` → `0 failure(s) over 1852 assertions`, exit 0. The counter alone cannot tell a fix inside the gate from deletion of the gate.
2. **A wrapper timeout with parseable output is scored by its status.** Pristine probe (`mut/probe124.py`): an injected runner returns exit 124 (the coreutils `timeout 60` exit code) plus valid JSON. `run_case` returns `('PASS', 'ok')` and `case_correct` is True; the same holds for an H2 case with `FAIL` plus its head. Spec item 2 says "timeout = case wrong", but only the 70 s Python backstop enforces it. The arm `runner: empty output is a wrong case` uses exit 124 with empty stdout, so the 124 path is never told apart. This gives no hollow gain: timing out cannot make a status right.
3. **An absolute-symlink instrument crashes with a traceback (R28).** The run ends in an uncaught `tarfile.AbsoluteLinkError` traceback, exit 1. The docstring promises exit 2 with no traceback for environment failures, but this failure class is not in its list. It cannot be exploited, since the exit is not 0.

## Where to add must-fail arms (coverage findings only; the contract is unchanged and nothing was applied)

- **`measure()` end to end.** Feed a fake git (a `make_tar` holding a scripted instrument) or an injected runner. Assert N, T and `main`'s exit code for: all correct, one wrong, all unparseable, and an environment failure (exit 2). This kills P08–P15 and A01–A03.
- **Class details.** Pin that only H5 carries `bash`, and check the rendered fence line (C14, C15). Assert a colon inside an H4 argument and ` | ` in H2 (C16–C18).
- **Verdict polarity.** A hard negative scored `("N/A", head)` must be wrong (D03).
- **Literal pins.** Pin the values of `CHECK_ID`, `DEFAULT_SEEDS` and `REAL_COMMANDS` resolving via `shutil.which` (S10, C13, C19).
- **Plumbing arguments.** Assert the full rev in the `git archive` argv (A02), `^{commit}` in rev-parse (A05), and a refused out-of-tree symlink (A04).

## Restoration evidence

`mut/probe_and_final.txt`, at 04:29 UTC:

- the sandbox counter's sha256 is `b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac`;
- `cmp` against the frozen blob: identical;
- `--self-test` on the restored counter: `0 failure(s) over 105 assertions`, exit 0.

After `demos2.py` finished, the working-tree instrument's sha256 is again `629867d1…` and HEAD is `ee50d8fa…`; the asserts passed.

## Hygiene

- **Lane writes.** Only this report and `MutC2Counter.txt`. No git or jj writes in the lane or the fleet repo.
- **Sandbox commits.** J, X, S and Y, listed above; never pushed.
- **Processes.** Every command ran under `timeout` (300 s per run, at most 900 s per driver). Runs were sequential with no concurrency. No process was killed.
- **Tools.** No tool was installed or upgraded, and pacman was not touched.
- **Bounds.** No C1 content was written. No real fix to the C2 instrument was written: the stub is hollow and lives only in sandbox S and in `mut/`.
