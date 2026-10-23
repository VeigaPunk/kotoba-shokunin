Result: DONE — the frozen C2 counter is delivered (sha256 `b3dbe72f…d1ac`), its 105-assertion self-test passes, all 34 guard mutations are killed, and at `47c0555` it measures 48 of 120 (pass-expected 0 of 60, hard negatives 48 of 60) with exit 1 in 5.5 s.

# w0 / ExecCounterC2 — the C2 info-less-fence counter

I wrote no content the counter scores: no `SKILL.md` section, knowledge entry,
`SOURCES.md` row, lesson, or instrument fix. The two files below are the whole
deliverable; the L1 copies the script into `verifiers/`.

## Delivered files

| path | sha256 | role |
|---|---|---|
| `.ufo/waves/round-57/w0/check_infoless_fences.py` | `b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac` | the counter (Python 3 stdlib only, `#!/usr/bin/env python3`) |
| `.ufo/waves/round-57/w0/ExecCounterC2.md` | — | this receipt |

`sha256sum` of the delivered counter bytes:
```
b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac  .ufo/waves/round-57/w0/check_infoless_fences.py
```

Behavior, one paragraph: with `--rev` the counter refuses anything but a
resolvable full 40-hex hash, `git archive`s the measured revision's
`verifiers/` tree into a fresh temp dir, runs **only** that extracted copy of
`verify_skill_checklist.py` (printed as `instrument sha256`), and drives 120
cases — 3 seeds × 10 classes × 4 — each in its own fresh dir holding a
`SKILL.md` of frontmatter + heading + one fenced block. Every token (table
cells, diagram labels, key names, bogus command heads) is one draw from one
generator; tokens that `shutil.which` resolves, that are shell
keywords/builtins, or that repeat inside a case are redrawn, so a bogus head
is not distinguishable by shape. It prints `counter sha256 <own bytes>`,
`measured <rev>`, `instrument sha256 <executed bytes>`, the frozen summary
line, and one `wrong <seed> <class> <dirname> status=<s>` line per wrong case.
`--self-test` runs 105 in-process arms and prints
`self-test: 0 failure(s) over 105 assertions`.

The script's docstring states the frozen spec as implemented, including the
L1 amendment of 2026-10-23 (one token generator; no `zq` prefix, no fixed
`[a-z]{3}`+6-hex shape) and the implementation notes (stdlib `tarfile`
extraction instead of a shell pipe; the coreutils `timeout 60` plus a 70 s
subprocess backstop; `status=unparseable` for an unparseable result).

## Evidence

### 1. `--self-test`

```
$ python3 -B -P kotoba/verifiers/check_infoless_fences.py --self-test
counter sha256 b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac
self-test: 0 failure(s) over 105 assertions
exit=0
```

The arms cover: frozen constants and plan totals; per-seed determinism
(`plan_cases` twice, equal); class counts; shuffle (every seed block's class
order differs from the unshuffled canonical order); one fence per skill and
`name: <dirname>` in the frontmatter; token shape / unresolvability against the
real `shutil.which` / reserved-free / per-case distinctness; every class's
shape (alignment row, box-drawing range, `+` box, arrows, key:value and
uppercase variant, H3 table-then-head, head position per H class); every
generator rejection branch; JSON parsing; verdicts; wrong-line formatting;
predicate arithmetic (120/120, 119/120, 119/119, 0/0, 150/150, 149/150);
`--rev` / flag-conflict guards; git plumbing and tar extraction with injected
runners; the exact frozen per-case argv, cwd and `PYTHONSAFEPATH=1`; the
timeout path; and the env-failure→exit-2 mapping.

### 2. Base measurement at `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`

Run from the sandbox clone, where the counter sits in `verifiers/` so the
default `--repo` (parent of the script's directory) is the clone. Wall time
5.463 s (`real`), every subprocess under `timeout`.

```
$ python3 -B -P kotoba/verifiers/check_infoless_fences.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
counter sha256 b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac
measured 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
instrument sha256 629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab
info-less fence cases correct 48 of 120 (pass-expected 0 of 60; hard negatives 48 of 60)
wrong 11 P2 skill-b7baf0a6 status=FAIL
wrong 11 P4 skill-778326b7 status=FAIL
wrong 11 P3 skill-403c7afd status=FAIL
wrong 11 H3 skill-26f4e796 status=FAIL
wrong 11 P4 skill-3e8d3a59 status=FAIL
wrong 11 P3 skill-16f92d8e status=FAIL
wrong 11 P4 skill-ed491ba5 status=FAIL
wrong 11 P2 skill-cd872ab4 status=FAIL
wrong 11 P5 skill-acca0702 status=FAIL
wrong 11 P5 skill-a911453e status=FAIL
wrong 11 H3 skill-85699c89 status=FAIL
wrong 11 P5 skill-d705424a status=FAIL
wrong 11 P1 skill-6b52b08d status=FAIL
wrong 11 H3 skill-42b54a4b status=FAIL
wrong 11 P4 skill-b5c83913 status=FAIL
wrong 11 P2 skill-3b6b6092 status=FAIL
wrong 11 P1 skill-73cf256d status=FAIL
wrong 11 H3 skill-f4e1d042 status=FAIL
wrong 11 P1 skill-5cb58b8e status=FAIL
wrong 11 P5 skill-28d2fe33 status=FAIL
wrong 11 P3 skill-9c1c6a5e status=FAIL
wrong 11 P2 skill-85d516a8 status=FAIL
wrong 11 P1 skill-724c9052 status=FAIL
wrong 11 P3 skill-a75fdb6e status=FAIL
wrong 22 H3 skill-990cdd5b status=FAIL
wrong 22 P2 skill-a888ceb4 status=FAIL
wrong 22 P5 skill-08bb6fd5 status=FAIL
wrong 22 P4 skill-8e7e4eb0 status=FAIL
wrong 22 P3 skill-72790373 status=FAIL
wrong 22 P2 skill-3ba5ecb9 status=FAIL
wrong 22 P1 skill-c48e5689 status=FAIL
wrong 22 P1 skill-f54d35bf status=FAIL
wrong 22 P2 skill-d100bd11 status=FAIL
wrong 22 P5 skill-128be818 status=FAIL
wrong 22 P4 skill-a65e77e2 status=FAIL
wrong 22 P3 skill-e620b575 status=FAIL
wrong 22 P5 skill-3db0f05d status=FAIL
wrong 22 P4 skill-0c3c197f status=FAIL
wrong 22 P5 skill-acaf708f status=FAIL
wrong 22 P3 skill-594da8cf status=FAIL
wrong 22 P1 skill-f1569c7f status=FAIL
wrong 22 H3 skill-ea21e4dc status=FAIL
wrong 22 P1 skill-a125ed7e status=FAIL
wrong 22 H3 skill-e5c5eaaa status=FAIL
wrong 22 P2 skill-afb36237 status=FAIL
wrong 22 P4 skill-2250bf8d status=FAIL
wrong 22 P3 skill-91fb1fb6 status=FAIL
wrong 22 H3 skill-6c19539e status=FAIL
wrong 33 P2 skill-f6382be3 status=FAIL
wrong 33 P2 skill-a8deaca5 status=FAIL
wrong 33 H3 skill-f5cc307a status=FAIL
wrong 33 P4 skill-766f57f2 status=FAIL
wrong 33 P1 skill-d9aae57c status=FAIL
wrong 33 P2 skill-d422c4e4 status=FAIL
wrong 33 P5 skill-85e6930c status=FAIL
wrong 33 P1 skill-d23c54db status=FAIL
wrong 33 P5 skill-e835a6ad status=FAIL
wrong 33 P1 skill-6ed79007 status=FAIL
wrong 33 P4 skill-46e6bb25 status=FAIL
wrong 33 P1 skill-92010b38 status=FAIL
wrong 33 P3 skill-e94cfa9b status=FAIL
wrong 33 P3 skill-bfc1dae1 status=FAIL
wrong 33 P3 skill-85dbeef3 status=FAIL
wrong 33 P5 skill-cf0c68ee status=FAIL
wrong 33 H3 skill-242a8150 status=FAIL
wrong 33 P5 skill-779e0521 status=FAIL
wrong 33 P3 skill-4f85aa1b status=FAIL
wrong 33 P2 skill-a69acfab status=FAIL
wrong 33 H3 skill-8fb4522b status=FAIL
wrong 33 H3 skill-90171ee8 status=FAIL
wrong 33 P4 skill-fa4a5b38 status=FAIL
wrong 33 P4 skill-9b707242 status=FAIL
exit=1
```

76 output lines: 4 header/summary + 72 wrong lines (60 pass-expected + 12
H3). Reading: the pass-expected half is **0 of 60**, as expected — the current
instrument reads every info-less fence line as a shell segment
(`verifiers/verify_skill_checklist.py:131-132`), so table cells, box-drawing
lines, arrow lines and `key:` lines all fail. Hard negatives are **48 of 60**,
not 60 of 60; the 12 misses are all H3, see §6.

The inserted real command of every pass-expected case is achievable on this
instrument — a minimal info-less fence holding only the command passes,
so the P classes demand nothing impossible once the class lines stop being
read as commands:

~~~~
$ (minimal info-less fence holding only `ls -la`)         PASS :: 1 segments; 1 command subject(s) resolve
$ (minimal info-less fence holding only `git --version`)  PASS :: 1 segments; 1 command subject(s) resolve
$ which ls git
/usr/bin/ls
/usr/bin/git
~~~~

The delivered file, run in place from the report dir with `--repo` pointing at
the sandbox clone, produced byte-identical output and exit 1 (6.229 s):

```
$ python3 -B -P .ufo/waves/round-57/w0/check_infoless_fences.py \
      --rev 47c05558… --repo /fast/scratch/hyaku/kotoba-r57/ExecCounterC2/kotoba
… info-less fence cases correct 48 of 120 (pass-expected 0 of 60; hard negatives 48 of 60)
exit=1        # `cmp` against the sandbox run: identical
```

### 3. Usage / environment exits (no traceback)

```
$ … --rev abc                                                exit 2  "--rev 'abc' is not a full 40-hex hash"
$ … --rev 0000000000000000000000000000000000000000            exit 2  "git rev-parse --verify …^{commit} failed … (exit 128): fatal: Needed a single revision"
$ … --self-test --rev 47c05558…                              exit 2  "--self-test cannot be combined with --rev or --seed"
$ … (no arguments)                                           exit 2  "--rev is required (a full 40-hex commit hash)"
```

### 4. Predicate below the frozen floor

```
$ … --rev 47c05558… --seed 5
info-less fence cases correct 16 of 40 (pass-expected 0 of 20; hard negatives 16 of 20)
exit=1
```

T = 40 < 120 fails even though only the H3 truncation is wrong; `N < T` on the
default seeds fails too (48 ≠ 120). Both halves of the predicate are also
asserted in the self-test (arms `predicate: one wrong fails`, `predicate:
fewer than 120 fails`).

### 5. The measured instrument is the committed blob, not the working tree

```
$ git -C kotoba show 47c05558…:verifiers/verify_skill_checklist.py | sha256sum
629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab  -
# matches "instrument sha256 629867d1…" printed by the measured run
$ git -C kotoba status --porcelain
?? verifiers/check_infoless_fences.py        # the counter copy, untracked; nothing else
```

`git archive` excludes the untracked counter, and the only path the counter
executes is `<tmp>/verifiers/verify_skill_checklist.py`.

### 6. Finding: H3 is wrong at base only because the instrument truncates its detail at four failures

H3 asks for `status == FAIL` **and** the case's bogus head inside the check's
detail text. The verifier builds that detail from `bad[:4]` plus
`" … (+%d more)"` (`verifiers/verify_skill_checklist.py:1746-1748`), and the
info-less table rows fail before the H3 head line, so the head is pushed into
the hidden tail. Probe on the generated seed-11 H3 case
(`skill-26f4e796`), extracted base instrument, same argv as the counter:

~~~~
```
| deboguza218 | puvefogo-vazudemi |
|---|:---:|
| lezesavu | neduhaf-boceh |
| wudapajo | pikira |
fepipec lapu
```
detail: "9 segments; line 9: 'deboguza218' …; line 9: 'puvefogo-vazudemi' …;
         line 10: '---' …; line 10: ':---:' … … (+5 more)"
status='FAIL'   bogus head 'fepipec' in detail: False
~~~~

So the H3 rule is measurable and correct by construction, but at this revision
the instrument's own detail cap makes it unobservable. This is why the frozen
expectation "hard negatives 60 of 60" reads **48 of 60** at base: H1/H2/H4/H5
are 48/48, H3 is 0/12. On a fixed instrument the table cells stop being
subjects, H3's only failing subject is `fepipec`, and the detail contains it
[INFERENCE — no fix exists to run here]. I did not weaken the frozen rule to
make the base number prettier; if the L1 wants 60 of 60 at base, the H3
correctness rule itself would have to change before freeze.

## R5 guard-mutation kill table

Method: the driver (sandbox `mutate.py`) asserts each `old` string occurs
exactly once in the delivered bytes, writes the mutated copy under
`/fast/scratch/hyaku/kotoba-r57/ExecCounterC2/mut/<guard>.py`, and runs
`python3 -B -P <mutant> --self-test` under `timeout 300`. `killed` = self-test
exit ≠ 0 with a named failing arm; `SURVIVED` = exit 0. Pristine self-test
before the sweep: `rc=0`. Counts: **34 mutations, 0 survived, 0 bad
mutations**.

| guard | mutation | self-test | first failing arm |
|---|---|---|---|
| rev-missing | delete the empty-rev rejection (return None) | killed | FAIL rev |
| rev-format | negate the 40-hex test | killed | FAIL rev |
| usage-conflict | delete the `--self-test` flag-conflict rejection | killed | FAIL conflict |
| own-sha-raises | replace the unreadable-own-file raise with a silent return | killed | FAIL sha |
| resolve-git-failure | delete the rev-parse return-code rejection | killed | FAIL resolve |
| resolve-non-hex | delete the full-hash check on rev-parse output | killed | FAIL resolve |
| archive-git-failure | delete the `git archive` return-code rejection | killed | FAIL archive |
| instrument-absent | delete the extracted-instrument existence rejection | killed | FAIL extract |
| tools-absent | delete the missing-tool rejection | killed | FAIL tools |
| token-shape | delete the token shape rejection | killed | FAIL token |
| token-taken | delete the duplicate-token rejection | killed | FAIL token |
| token-reserved | delete the shell-keyword/builtin rejection | killed | FAIL token |
| token-which | delete the `shutil.which` rejection | killed | FAIL every generated token unresolvable |
| token-exhausted | replace the draw-cap raise with a silent return | killed | FAIL token |
| dirname-taken | delete the duplicate-directory-name rejection | killed | FAIL dirname |
| dirname-exhausted | replace the name-cap raise with a silent return | killed | FAIL dirname |
| parse-json-error | delete the unparseable-JSON rejection | killed | FAIL parse |
| parse-doc-dict | delete the non-dict-document rejection | killed | FAIL parse |
| parse-checks-list | delete the non-list-checks rejection | killed | FAIL parse |
| parse-item-dict | negate the non-dict-entry skip | killed | FAIL parse |
| parse-check-id | turn the id-mismatch skip into a fall-through | killed | FAIL parse |
| parse-status-str | delete the non-string-status rejection | killed | FAIL parse |
| parse-no-match | delete the no-matching-check result | killed | FAIL parse |
| verdict-unparseable | negate the unparseable-is-wrong rule | killed | FAIL verdict |
| verdict-pass-status | accept any status for pass-expected cases | killed | FAIL verdict |
| verdict-negative-status | drop the FAIL requirement for hard negatives | killed | FAIL verdict |
| verdict-negative-head | drop the detail-contains-head requirement | killed | FAIL verdict |
| wrong-line-status | change the unparseable status token | killed | FAIL wrong line on unparseable |
| predicate-all-correct | drop the `N == T` half of the predicate | killed | FAIL predicate |
| predicate-floor | drop the `T >= 120` half of the predicate | killed | FAIL predicate |
| runner-timeout | treat a timed-out case as good | killed | FAIL runner |
| guarded-env-exit | stop mapping environment failures to exit 2 | killed | FAIL guarded |
| plan-shuffle | delete the per-seed case shuffle | killed | FAIL shuffle changes every seed block |
| class-count | change the frozen 4 cases per class to 3 | killed | FAIL cases per class |

Two branches are **not** in the table because they are not rejection guards:
main's `if sha is None: return code` and `if result is None: return code`
(`check_infoless_fences.py:884-886, 899-901`). They only turn `guarded()`'s
already-armed exit code into `main`'s return value; the observed CLI runs in
§3 (exit 2 for four distinct failures, no traceback) are their evidence. They
cannot be armed in-process without a seam that only a subprocess would
exercise, and the frozen spec asks for in-process arms.

## Risks, assumptions, limits

1. **H3 at base (above).** The counter reports 48/120 here; the 12 H3 misses
   are the instrument's 4-item detail cap, not a counter defect. The frozen
   predicate is unchanged; exit 1 is the correct base verdict either way
   (`N ≠ T`).
2. **Host PATH is part of the draw.** `make_token` rejects anything
   `shutil.which` resolves, so the same seed can draw a different token
   sequence on a host with a different PATH; case directory names in `wrong`
   lines are therefore host-dependent. Verdicts are not: the classes judge
   status, not token text. The in-process determinism arm is exact per host.
3. **Repeated seeds inflate T.** `--seed 5 --seed 5` measures the block twice;
   only the frozen `N == T and T >= 120` is judged. Use the defaults (11 22 33)
   for the claim.
4. **`--repo` default needs the file in `verifiers/`.** Running the copy from
   the w0 report dir without `--repo` exits 2 (git failure in that directory);
   run it as the L1 will after copying, or pass `--repo <lane>`.
5. **Editing after this receipt changes the sha line.** The printed `counter
   sha256` is the file's own bytes; the value above binds the delivered bytes
   only.
6. **Python ≥ 3.12** for `tarfile.extractall(filter="data")`; this host runs
   3.14.8. Older interpreters would raise before `guarded()` can map it.
7. The 70 s subprocess backstop is longer than the spec's `timeout 60`, so a
   hung wrapper is the wrapper's own 124 and a wedged wrapper still returns
   (as a wrong case).

## Hygiene

- Sandbox: `/fast/scratch/hyaku/kotoba-r57/ExecCounterC2/kotoba`, cloned from
  the lane, checked out at `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`; the only
  change in it is the untracked `verifiers/check_infoless_fences.py` copy
  (`git status --porcelain` above). No sandbox commit was made.
- Lane writes: only the two delivered files under
  `.ufo/waves/round-57/w0/`; no git/jj writes in the lane or the fleet repo.
- Every run was wrapped in `timeout` (≤ 600 s); no process was killed; no
  background job was started.
- No tool install or upgrade was needed; pacman was not touched.
