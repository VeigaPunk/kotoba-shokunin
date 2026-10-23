Result: DONE — v3 of the info-less fence counter is written as a C2 redesign input only at `.ufo/waves/round-57/build/check_infoless_fences_v3.py` (sha256 `eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a`, 1658 lines): `--self-test` is `0 failure(s) over 202 assertions`, a 26-mutant guard table is 26 killed / 0 survived / 0 harness errors, and the base measurement of `47c05558` is `168 of 264` with exit 1 and the new self-test conjunct met (`0 failure(s) over 1852 assertions (base floor 1852)`). No instrument fix was written.

# ExecC2CounterV3 — C2 counter v3 (redesign input, not a claim)

- Target: `.ufo/waves/round-57/build/check_infoless_fences_v3.py`, started from `.ufo/waves/round-57/w0/check_infoless_fences_v2.py` (sha256 `8e38838262dc10c53de1d91e32fdcc659e83ffb964ff4ef7b3264183e723fa34`, read in full before editing).
- The delivered bytes are byte-identical in the sandbox and the lane: `sha256sum` on both prints
  `eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a`.
- Executed only inside `/fast/scratch/hyaku/kotoba-r57/KotobaR57.ExecC2CounterV3` (clone at `01312a77e36317feb6e961aba77841ddab1225ca`). No git/jj write in the lane or the fleet repo; the lane received only this report and the counter file.
- `verifiers/verify_skill_checklist.py` was never written, copied or patched: the counter only extracts and executes the measured revision's own instrument. There is no instrument fix or sketch anywhere in the deliverable.

# What v3 adds, and where

## 1. Full-tree extraction and the self-test conjunct

- Archive is the whole tree, no pathspec: `archive_full()` at `check_infoless_fences_v3.py:269` runs `git -C <repo> archive --format=tar <full-rev>`. The v2 `verifiers` pathspec is gone (grep for `archive_verifiers` in the deliverable: no hits).
- `extract_tar()` (`:280`) extracts member by member with the stdlib `data` filter. A refused member under `verifiers/` is an `EnvError` (`exit 2`, message `archive cannot be extracted safely: …`), so the instrument can never be reached through a link; a refused member outside `verifiers/` is skipped and counted (see the base run's `full tree: 6039 archive member(s) refused by the data filter`, all of them absolute links in `.ufo/round-46` wave fixtures — checked: zero refusals under `verifiers/`).
- `run_selftest()` (`:603`) runs `timeout 120 python3 -B -P <tree>/verifiers/verify_skill_checklist.py --self-test` from a generator-named empty cwd with `PYTHONSAFEPATH=1`. `parse_selftest()` (`:587`) reads the last line matching `^(\d+) failure\(s\) over (\d+) assertions?$`. `selftest_met()` (`:596`) requires exit 0, `failures == 0`, and `assertions >= base_assertions`.
- The floor is measured at run time, not hard-coded: `measure()` (`:736`) extracts `BASE_REV`'s full tree first and runs its self-test the same way; a base that is red or unparseable is an `EnvError` (no floor ⇒ exit 2, never a silent pass).
- The predicate (`predicate_ok()` at `:695`) is now `N == T and T >= 120 and K == 0 and S == 1`. `main()` prints the receipt and folds S into the exit code:
  `instrument self-test: exit 0, 0 failure(s) over 1852 assertion(s) (base floor 1852): met`.
  I verified separately that the base instrument's self-test is green from a full-tree extract (not just a full checkout): `0 failure(s) over 1852 assertions`, exit 0, in 0.21 s.
- `run_case()` (`:616`) now rejects a wrapped run whose exit code is not 0 or 1 (`ACCEPTED_RETURN_CODES = (0, 1)` at `:165`): the coreutils wrapper's `124` timeout is a wrong case even when stdout holds valid JSON, while the instrument's own `1` (a FAIL check) is still parsed.

## 2. End-to-end self-test arms against stub instruments

Inside `--self-test` (`:1390`–`:1538`), `main()` is called with an injected git and runner. The fake git serves `rev-parse`, `show <base>:<instrument>` and the two full-tree archives (base and measured); `measure()` then does real extraction, real sha256, real planning, real case scoring and real predicate/exit-code arithmetic; only subprocess execution is simulated by the runner. Every world is asserted by its printed score line and its exit code:

| world | what the stub does | asserted result |
|---|---|---|
| positive | correct statuses, self-test 1852 green | exit 0, `264 of 264`, self-test line `met`, printed sha = sha of the extracted bytes |
| prints nothing | no stdout | exit 1, `0 of 264` |
| deleted instrument | tar has no instrument | exit 2, stderr names the absence |
| absolute symlink instrument | tar member is a symlink to `/etc/passwd` | exit 2, `archive cannot be extracted safely` |
| N/A with the head echoed | PASS for pass-expected, `N/A` + exact subject for hard negatives | exit 1, `72 of 264` (only pass-expected) |
| valid JSON, wrapper exit 124 | correct-looking JSON for both classes, rc 124 | exit 1, `0 of 264` |
| red self-test | every case correct, self-test `3 failure(s)` | exit 1, `264 of 264`, line `NOT MET` |
| below floor | every case correct, self-test `0 failure(s) over 1851 assertions` | exit 1, line `NOT MET` |

The archive argv is also pinned (`[["archive","--format=tar",BASE_REV], ["archive","--format=tar",MEASURED]]`), as are the self-test argv capsule (`["timeout","120","python3","-B","-P",<tree>/verifiers/...]`, last arg `--self-test`, empty cwd) and the run_case argv capsule.

## 3. Pinned class-shape arms

At `:977`: only H5 carries a fence info string (`{c.cls for c in plan if c.info} == {"H5"}`, every H5 = `bash`); H2's head line matches `^\S+ \| \S+$` with the first token resolvable by `shutil.which` and the third token equal to the head; H4's head line matches `^\S+ --opt=\S+:\S+$` with the first token equal to the head. The v2 arms (13 classes, 4 per class, twins, tokens, one fence, frontmatter) are unchanged.

# Retained evidence (all commands run in the sandbox)

## Self-test

```
$ python3 -B -P check_infoless_fences_v3.py --self-test ; echo SELFTEST-EXIT=$?
counter sha256 eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a
self-test: 0 failure(s) over 202 assertions
SELFTEST-EXIT=0
```
Receipt `probe/v3-selftest.txt`, sha256 `025a4442557dd945220c6eb084d4641e4e7452df08b657462aeefcc2b4c20e38`.

## Guard-mutation kill table

`mut/driver.py` replaces one exact implementation string per mutant (asserting exactly one occurrence), runs `timeout 180 python3 -B -P <mutant> --self-test`, and restores the pristine bytes. Killed = exit non-zero. Raw output `mut/kill-table.txt`, sha256 `2d579712534ca05249b062a60ac8f3e1809124873f89f65c42f5be07c17e619c`:

```
counter .../check_infoless_fences_v3.py sha256 eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a
| pristine | — | 0 | self-test: 0 failure(s) over 202 assertions |
| id | mutation | self-test exit | summary | verdict |
|---|---|---|---|---|
| M01 archive pathspec | ["archive", "--format=tar", rev, "verifiers"] | 1 | self-test: 8 failure(s) over 202 assertions | KILLED |
| M02 archive HEAD | ["archive", "--format=tar", "HEAD"] | 1 | self-test: 8 failure(s) over 202 assertions | KILLED |
| M03 drop conjunct |                              True) else 1 | 1 | self-test: 2 failure(s) over 202 assertions | KILLED |
| M04 drop floor | and st.assertions is not None) | 1 | self-test: 3 failure(s) over 202 assertions | KILLED |
| M05 drop exit code | True | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M06 drop failures | True | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M07 zero the failure count | return 0, int(match.group(2)) | 1 | self-test: 2 failure(s) over 202 assertions | KILLED |
| M08 base floor zero | base_assertions = 0 | 1 | self-test: 4 failure(s) over 202 assertions | KILLED |
| M09 ignore wrapper rc | if False: | 1 | self-test: 4 failure(s) over 202 assertions | KILLED |
| M10 D03 polarity |     if status == "PASS":
        return False | 1 | self-test: 2 failure(s) over 202 assertions | KILLED |
| M11 H4 colon dropped | return ["%s --opt=%s-%s" % (head, tok(), tok())], head, 0 | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M12 H2 pipe to semicolon | return ["ls ; %s" % head], head, 0 | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M13 bash tag on H4 | info = "bash" if cls == "H4" else "" | 1 | self-test: 2 failure(s) over 202 assertions | KILLED |
| M14 trust the archive | tf.extract(member, dest, filter="fully_trusted") | 1 | self-test: 3 failure(s) over 202 assertions | KILLED |
| M15 exit inverted | return 1 if predicate_ok(correct, total, len(suspicious), | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M16 self-test flag typo | str(instrument), "--selftest"] | 1 | self-test: 19 failure(s) over 202 assertions | KILLED |
| M17 drop -P from the self-test |     argv = ["timeout", str(SELFTEST_TIMEOUT), "python3", "-B | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M18 self-test on the base tree |         code, parsed = run_selftest(base_tree, env, runner=r | 1 | self-test: 4 failure(s) over 202 assertions | KILLED |
| M19 accept a refused instrument | if False: | 1 | self-test: 2 failure(s) over 202 assertions | KILLED |
| M20 run the working tree (A01) |             str(Path.cwd() / INSTRUMENT)] | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M21 sha from base bytes (A03) |         instrument_sha = hashlib.sha256(old_text.encode()).h | 1 | self-test: 1 failure(s) over 202 assertions | KILLED |
| M22 N summed from totals (P08) | correct = sum(pair[1] for pair in tallies.values()) | 1 | self-test: 6 failure(s) over 202 assertions | KILLED |
| M23 predicate on the total (P11) |     return 0 if predicate_ok(total, total, len(suspicious), | 1 | self-test: 3 failure(s) over 202 assertions | KILLED |
| M24 every case correct (P12) |             if True: | 1 | self-test: 6 failure(s) over 202 assertions | KILLED |
| M25 verdict negated (P13) |             if not good: | 1 | self-test: 8 failure(s) over 202 assertions | KILLED |
| M26 env failure exits 0 (P15) |         return 0, None | 1 | self-test: 3 failure(s) over 202 assertions | KILLED |
restored sha256 eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a (identical); pristine self-test exit 0, self-test: 0 failure(s) over 202 assertions
totals: 26 killed, 0 survived, 0 harness errors
```

Reading of the table against the job: the conjunct's three clauses are load-bearing (M03 conjunct in `main`, M04 floor, M05 exit code, M06 failure count, M07 parse, M08 base floor, M18 base tree); the wrapper-timeout rule is load-bearing (M09); verdict polarity is pinned (M10, M24, M25); class shapes are pinned (M11–M13); the archive is a full tree at the given rev (M01, M02) and the extracted copy is what runs (M20, M21); extraction refuses a linked instrument (M14, M19); the verdict arithmetic and exit code are pinned (M15, M22, M23, M26); the self-test command shape is pinned (M16, M17).

## Base run (expect exit 1)

```
$ python3 -B -P check_infoless_fences_v3.py --repo <sandbox> --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a ; echo BASE-EXIT=$?
counter sha256 eef46b9e0af6a7a4e3f9fd71a02cbd69979b5537cbb21869a7f86447b4d43a9a
measured 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
instrument sha256 629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab
full tree: 6039 archive member(s) refused by the data filter
instrument diff guard: 0 suspicious added line(s)
instrument self-test: exit 0, 0 failure(s) over 1852 assertion(s) (base floor 1852): met
preflight real command lines: 20 of 20 PASS alone
info-less fence cases correct 168 of 264 (pass-expected 0 of 72; hard negatives 168 of 192)
BASE-EXIT=1
```
Receipt `probe/v3-base-run.txt`, sha256 `18d33eb8bfacaaf63c66a26842d80089cfbe72408d08fba7cbb1c0763df19b56`. 96 wrong lines (P1 14, P2 14, P3 13, P4 18, P5 13, H3 24) — the same `168 of 264` score the w0 v2 receipt recorded, so the new conjunct and the full-tree extraction change no case verdict at base. Runtime 15–19 s per measured run (two 12,168-member full-tree extractions plus 264 real instrument runs); `--self-test` 1.5–2 s.

# Risks and limits

1. **The self-test conjunct is a text trust, not an authentication.** A stub that prints `0 failure(s) over <>= base> assertions` and exits 0 satisfies S. It is caught only when its case answers are hollow (the end-to-end arms show that path kills such a world). A counterfeit self-test plus a correct gate is indistinguishable from the real instrument by this counter alone; the diff review remains the decisive guard for that shape. This is stated rather than fixed.
2. **The extracted "full tree" omits members the data filter refuses.** At base these are 6,039 absolute links, all under `.ufo/round-46` wave fixtures; none under `verifiers/`. The count is printed on every run, and any refused `verifiers/` member is exit 2, so an instrument reached through a link cannot be scored.
3. **Base floor dependency.** The measured run needs `BASE_REV` in the repository and needs its instrument self-test to be green from a full-tree extract. If a later checkout drops that commit or changes its self-test, the counter exits 2 rather than guessing a floor.
4. **Simulated subprocess in the arms.** The eight end-to-end worlds inject a runner, so they exercise extraction, sha, planning, scoring, receipts and exit codes but not process spawning; spawning is exercised by the real base run. A hostile stub could still key on the runner environment; nothing mechanical removes that class (the v2 Q33 note said the same).
5. **Invocation.** The default repo is `Path(__file__).resolve().parent.parent`, so the file must sit in `verifiers/` when re-controlled (as v1/v2 were run) or be given `--repo`; the base run above used `--repo` because the deliverable is under `build/`.
6. **Not exercised:** P09, P14, P16, P17 analogues were not mutated (the table mutates 26 of the v1 survivor families above); no measurement of a fixed instrument exists, because writing one was out of scope. No claim is made — C2 stays withdrawn; this is redesign input for a later round's pre-freeze control.

# Hygiene

- Sandbox: `/fast/scratch/hyaku/kotoba-r57/KotobaR57.ExecC2CounterV3` (clone at `01312a77e36317feb6e961aba77841ddab1225ca`); all receipts under `probe/` and `mut/` there. No sandbox commit was made, so no sandbox hash is cited.
- Every command ran under `timeout` (≤ 900 s), sequential, one process at a time; nothing was killed; no `pkill`/`killall`.
- No tool installed or upgraded; no pacman transaction; no model call.
- Lane writes: this report and `.ufo/waves/round-57/build/check_infoless_fences_v3.py` only. No lane git/jj write, no fleet-repo write.
