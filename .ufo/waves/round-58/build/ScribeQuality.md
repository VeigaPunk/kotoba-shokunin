Result: BREAKS — Three QUALITY rows and frozen-revision falsifiers are drafted, but an exploratory self-test run used an unpinned default temporary directory before compliant reruns.

# Scope and provenance

Draft only for `corpus/QUALITY.md`; no lane QUALITY or lesson file was edited. The rows below preserve the existing five-column table and place the lesson entry plus falsifier command in `grounded in`; `supersedes` remains `—` because these rows replace no existing criterion.

The build dispatch asks for the R1 withdrawal annotation, the C2 two-sided mutation rule, and the R4 successful `main()` path. I read `corpus/QUALITY.md:1-11,54-60`, `plans/round-58.md:13,16,75-95`, both frozen counter sources, the proposed M70–M73 lesson text (`.ufo/waves/round-58/build/ScribeMistakes.md:14,16,20`), and the R1/R4/C2 build reports. The execution sandbox was cloned and checked out at `3de87aad29e960c95ed35840442f424c48c29729`:

```sh
timeout 900s bash -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; mkdir -p /fast/scratch/hyaku/kotoba-r58/ScribeQuality && git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/ScribeQuality && git -C /fast/scratch/hyaku/kotoba-r58/ScribeQuality checkout -q 3de87aad29e960c95ed35840442f424c48c29729'
```

Exit 0; no output. Test temporary directories for the final two behavioral runs were pinned under `/fast/scratch/hyaku/kotoba-r58/ScribeQuality/.tmp`.

# Proposed QUALITY rows (verbatim)

```markdown
| Q46 | A counter whose claim is withdrawn carries an explicit in-row `claim withdrawn` annotation and states there that it is no longer a claim gate; the registry's syntactic `gate` kind alone cannot restore the withdrawn claim. | verifier registry rows for withdrawn claims | M70 `withdrawn-counter-kept-as-gate` (proposed `corpus/lessons/round-58.md` § Mistakes; `.ufo/waves/round-58/build/ScribeMistakes.md:14`); `grep -c 'check_infoless_fences.py.*claim withdrawn.*not a claim gate' SKILL.md` (0, exit 1 at `3de87aad29e960c95ed35840442f424c48c29729`). | — |
| Q47 | A mutation-kill claim reports and gates both sides: every declared mutant is killed and every semantics-preserving equivalent rewrite survives; a snapshot-only self-test that kills equivalents is rejected even when it kills every mutant. | mutation-sweep predicates and mutation-kill claims | M73 `correction-sweep-arms-weak` (proposed `corpus/lessons/round-58.md` § Mistakes; `.ufo/waves/round-58/build/ScribeMistakes.md:20`); `python3 -B verifiers/check_sweep_mutants.py --rev 3de87aad29e960c95ed35840442f424c48c29729` (4/11 mutants killed, 5/5 equivalents survived, exit 1); snapshot control `.ufo/waves/round-58/controls/CtlC2Snapshot.md:61-80` (11/11 killed, 0/5 equivalents survived, exit 1). | — |
| Q48 | A counter's self-test exercises its public `main()` on a valid satisfying fixture and requires exit 0 plus the exact measured output; helper-only checks and failure-only calls do not cover the successful measurement path. | verifier self-tests for scored behavior | M71 `self-test-no-successful-main-path` (proposed `corpus/lessons/round-58.md` § Mistakes; `.ufo/waves/round-58/build/ScribeMistakes.md:16`); `TMPDIR=/fast/scratch/hyaku/kotoba-r58/ScribeQuality/.tmp timeout 900s python3 -B -c 'import importlib.util,pathlib; p=pathlib.Path("verifiers/check_command_files.py"); s=importlib.util.spec_from_file_location("check_command_files",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); old=m.main; armed=[True]; m.main=lambda a=None: (armed.__setitem__(0,False) or 1) if armed[0] and a and "--fetch" in a and m.TARGET==2 else old(a); raise SystemExit(m.self_test())'` (two R4 failures, exit 1 at `3de87aad29e960c95ed35840442f424c48c29729`). | — |
```

# Executed falsifiers and outcomes

All final commands below ran in `/fast/scratch/hyaku/kotoba-r58/ScribeQuality`, checked out at the frozen commit. The R1 grep reads the checked-out `SKILL.md`; the mutation counter is pinned explicitly with `--rev`; the R4 command mutates only the imported module's in-memory `main` binding so the self-test's first satisfying `--fetch` call returns 1. It does not edit the counter.

### Q46 — withdrawal annotation

```sh
timeout 900s grep -c 'check_infoless_fences.py.*claim withdrawn.*not a claim gate' SKILL.md
```

```text
0
exit code: 1
```

### Q47 — both mutation sides

```sh
TMPDIR=/fast/scratch/hyaku/kotoba-r58/ScribeQuality/.tmp timeout 900s python3 -B verifiers/check_sweep_mutants.py --rev 3de87aad29e960c95ed35840442f424c48c29729
```

```text
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
exit code: 1
```

The separate snapshot-only control is cited but was not run by this seat: `.ufo/waves/round-58/controls/CtlC2Snapshot.md:61-80` records `sweep mutants killed 11 of 11; equivalents survived 0 of 5`, exit 1. This is a record-only counter because C2 was withdrawn before data, not a C2 claim.

### Q48 — successful `main()` path must be testable

```sh
TMPDIR=/fast/scratch/hyaku/kotoba-r58/ScribeQuality/.tmp timeout 900s python3 -B -c 'import importlib.util,pathlib; p=pathlib.Path("verifiers/check_command_files.py"); s=importlib.util.spec_from_file_location("check_command_files",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); old=m.main; armed=[True]; m.main=lambda a=None: (armed.__setitem__(0,False) or 1) if armed[0] and a and "--fetch" in a and m.TARGET==2 else old(a); raise SystemExit(m.self_test())'
```

```text
FAIL R4: the satisfying world exits 0: got 1, expected 0
FAIL R4: the exact found line is printed: got False, expected True
self-test: 2 failure(s) over 244 assertions
exit code: 1
```

# Finding: R1 plan/lesson route conflicts with the frozen registry counter

The frozen plan says R1 is “registry row re-labelled `probe` with the withdrawal reason (build wave)” (`plans/round-58.md:13`). The proposed M70 text repeats: “round 58 relabels the `SKILL.md` gate-registry row as `probe` and records the withdrawal reason” (`ScribeMistakes.md:14`). The R1 executor reports the opposite constraint verbatim:

> “That remedy is rejected by the frozen counter: a `probe` is rejected if its verdict map declares `1=failed` **or** its source has an exact active `--self-test` handler. Both scripts have that exact handler (`check_infoless_fences.py:881`, `check_sweep_mutants.py:384`), and both rows declare `1=failed`.” (`ExecR1Registry.md:41-46`)

> “So no row-only probe relabel can reach 32 of 32; making it conformant would require editing the scripts' `--self-test` handlers (out of scope, and it would remove the gates' self-test) or the frozen counter (forbidden).” (`ExecR1Registry.md:57-60`)

The delivered R1 patch instead appends `claim withdrawn r57; not a claim gate until redesigned and re-controlled` in the verdict-map cell while retaining `gate` (`ExecR1Registry.md:17-25`). Q46 therefore requires the in-row annotation, not the impossible probe relabel. M70's fix sentence must be reconciled by the integrator; this report does not alter the frozen plan or lesson draft.

# Behavior, gates, surfaces, and limits

- **Behavior:** proposed Q46–Q48 rows only; no `corpus/QUALITY.md` edit. The `grounded in` cell carries each lesson entry and falsifier command; `supersedes` is `—` because none of the rows supersedes an existing criterion.
- **Gates run:** the three red falsifiers above only. No build, general tests, lint, formatter, network fetch, or client CLI ran. No tool was installed or updated.
- **Touched surfaces:** this report file only in the lane: `.ufo/waves/round-58/build/ScribeQuality.md`. The sandbox clone is `/fast/scratch/hyaku/kotoba-r58/ScribeQuality` at `3de87aad29e960c95ed35840442f424c48c29729`; no sandbox commit was made.
- **Out of scope:** integrating QUALITY or lesson prose, changing the frozen C1/C2 rules or targets, modifying a verifier, editing the plan, and resolving the R1 route conflict.
- **Known process limit:** before pinning `TMPDIR`, I ran an exploratory C2 command and two R4 monkeypatch variants with `timeout 900s` but without a `TMPDIR` assignment. The host check `timeout 30s bash -c 'printf "TMPDIR=%s\\n" "${TMPDIR-(unset)}"'` printed `TMPDIR=(unset)`, so their Python temporary-directory placement was not constrained to the seat clone; those outputs are not used as the final falsifiers. The C2 and focused R4 commands were rerun with `TMPDIR` explicitly set inside the clone and are the outputs pasted above. The initial broad R4 variant returned `self-test: 7 failure(s) over 244 assertions`, exit 1; it was superseded by the focused two-failure run. I cannot establish the temporary paths of the earlier exploratory runs from their outputs.
- **Artifact:** `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/build/ScribeQuality.md`.

## Superseded R1 diagnostic

Before reading `ExecR1Registry.md`, I tested the plan's proposed `probe` relabel directly:

```sh
timeout 900s python3 -B -c 'from pathlib import Path; rows=[x for x in Path("SKILL.md").read_text().splitlines() if "check_infoless_fences.py" in x]; row=rows[0] if len(rows)==1 else ""; kind="probe" if "| probe |" in row else "not probe"; annotated="yes" if "withdraw" in row.lower() else "no"; ok=kind=="probe" and annotated=="yes"; print("R1 registry check: %s (kind=%s, withdrawal annotation=%s)" % ("PASS" if ok else "FAIL",kind,annotated)); raise SystemExit(0 if ok else 1)'
```

```text
R1 registry check: FAIL (kind=not probe, withdrawal annotation=no)
exit code: 1
```

This diagnostic is not the Q46 falsifier: it encoded the plan's probe remedy, which the frozen registry counter rejects as described above. The final Q46 grep instead checks the withdrawal annotation.
