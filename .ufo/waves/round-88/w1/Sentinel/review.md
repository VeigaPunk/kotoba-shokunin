# Sentinel review — C1 v2 and C2 v2 instruments (round 88, w1)

Seat: Sentinel (read-only review). Scope: `verifiers/check_omp_root_semantics_v2.py` (sha256 `506a2ba9…`),
`verifiers/check_r86_routed_repairs_v2.py` (sha256 `10bd5508…`), and `verifiers/floors-registry.json`
(no v2 row present at review time).

Handoff status at review time (2026-11-05, ~06:40 local):
- `C2_READY` present (06:04), content names sha `10bd5508…` and discloses `1 failure(s) over 16 assertions`.
- `C1_READY` ABSENT. The 45-minute poll window ended without it. C1 is reviewed as it stands on disk (file written 06:24).

Summary: 9 findings; 3 blocking (F1, F2, F3).

## Findings

### F1 — BLOCKING — C1 v2 self-test and `--rev` crash on an unbound local
- `verifiers/check_omp_root_semantics_v2.py:320-336` (`reader_grounded`): `last_absent` is assigned only inside the loop
  body after the join-token test; the fall-through `return` at 334-336 reads it. When no ELF line carries a join token
  for any reader offset, `last_absent` is unbound.
- Observed: `TMPDIR=… python3 -B verifiers/check_omp_root_semantics_v2.py --self-test --work …` ends with
  `UnboundLocalError: cannot access local variable 'last_absent'` (raised from `score` at 631 via `world` at 829 and
  `self_test` at 914), exit 1.
- Risk: (a) exit 1 is the content-fail code, so a crash reads as a content verdict, breaking the 0/1/2 ladder; (b) `run()`
  catches only `Inconclusive` (1094, 1123), so `--rev` on such a world also dies with a traceback; (c) `forged_verdicts`
  (684) catches `(OSError, ValueError, KeyError, TypeError)` only, so the forged-world rejections that take this path
  are counted by accident of the crash, not by a designed verdict. The M count cannot be trusted until this is fixed.
- Fix (owner ExecLiveBound): initialise `last_absent` (or return a named reason) before the loop; add a self-test arm
  that exercises the no-join-token fall-through and asserts exit 1 with a named reason, not an exception.

### F2 — BLOCKING — C2 v2 self-test is red; its frozen control `w_added_red` reads PASS; `C2_READY` written anyway
- `verifiers/check_r86_routed_repairs_v2.py` (self_test, arm `w_added_red`, ~line 355): observed
  `1 failure(s) over 16 assertions`. The added unresolvable commit citation adds no new DRIFT name; the (ii) test is a
  name-set subset (`monotone_holds`), so `commit_unresolvable` (already DRIFT at base) passes. The plan's frozen
  control expects `D5 FAIL via (ii)`.
- The counter itself acknowledges this (self-test label: "counter defect, see ExecMonotoneD5.md"). Sentinel does not
  alter the predicate; the fix belongs to the counter (instance-level monotone, e.g. per-name instance counts from the
  integrity `observed` field), not a predicate edit.
- Handoff breach: `C2_READY` is specified as written "after the v2 gate's own --self-test passes". It was written over a
  red self-test (its own content admits `1 failure`). Admission must not treat C2_READY as a passing self-test handoff.
- Blocking because the frozen discrimination control fails on the landed instrument.

### F3 — BLOCKING (scratch convention) — C2 v2 `--self-test` ignores `--work`
- `verifiers/check_r86_routed_repairs_v2.py:183-185` calls `self_test()` with no argument; `self_test` (295) and its
  fixture `tempfile.TemporaryDirectory(prefix="r88-routed-v2-fixture-")` (321) take no `dir=`.
- Observed: `--self-test --work $S/w1` with `TMPDIR=$S` left `$S/w1` empty; the fixture went to `TMPDIR`. With
  `TMPDIR` unset, the fixture falls back to `tempfile.gettempdir()`, i.e. `/tmp`.
- The operator convention is "honour TMPDIR and accept a scratch argument"; a `--work` argument that is accepted and
  then ignored breaks it. Fix is one line (pass `work` into `self_test` and create the fixture under it).

### F4 — non-blocking — C2 v2 default scratch falls back to `/tmp`
- `verifiers/check_r86_routed_repairs_v2.py:193`: `Path(os.environ.get("TMPDIR") or tempfile.gettempdir())`.
  Not a hardcoded literal, but without `TMPDIR` or `--work` the clone tree (a full checkout) lands in `/tmp`.
- Recommend exit 2 (could-not-evaluate) when neither is given, or require `--work`.

### F5 — non-blocking — C1 v2 S5 "never execs" guard is a substring check and its report line is constant
- `verifiers/check_omp_root_semantics_v2.py:863-866` asserts that the source contains no `Popen`, `os.system`,
  `os.exec`, `os.spawn`, `socket`, `urllib`, `http.client`, `requests`. `subprocess.run([OMP_BINARY, …])` would pass it.
- `run()` prints `guard S5 … PASS` (1054-1055) as a literal string, not as the result of a check. S2 (1053) is printed
  the same way (enforcement itself is in `open_elf`, 268-288, which does work).
- Current code: the only `subprocess.run` is the git call at 254 (`["git", "-C", …, "show", …]`); the ELF is mmapped
  `ACCESS_READ` (274) and never executed. Verified by reading. The guard is weak, not violated.
- Recommend: assert no `subprocess` call names `OMP_BINARY`, and print S5 from a computed value.

### F6 — non-blocking — C2 v2 executes the revision's own integrity script
- `verifiers/check_r86_routed_repairs_v2.py:87-88`: `subprocess.run([sys.executable, "-B", INTEGRITY, "--json"], cwd=tree, timeout=300)`.
  For any `--rev`, the committed `verify_corpus_integrity.py` of that revision runs with the user's privileges in the
  scratch clone. Acceptable for the lane's own commits; it is a trust boundary for any other revision. Document it.
- `--rev` is resolved to a full SHA by `r87._resolve` (rev-parse `^{commit}`) before `checkout --detach` (line 72), so no
  option injection or `..` reaches the checkout.

### F7 — non-blocking — C1 v2 `--rev` reaches `git show` unvalidated
- `verifiers/check_omp_root_semantics_v2.py:254`: `["git", "-C", repo, "show", f"{rev}:{path}"]`. Argv list, no shell, so
  no injection. A `--rev` beginning with `-` is parsed by git as an option and yields `None` ("absent"), which fails S1
  rather than passing. No timeout on this call. Recommend resolving `rev` with `rev-parse --verify` first, as the C2
  gate does.

### F8 — non-blocking — C1 v2 floors row missing
- `verifiers/floors-registry.json` contains no `omp_root_semantics_v2` row (grep empty at 06:39). The run prints
  `floors row … absent`; S4 cannot pass on `--rev` until ExecLiveBound adds the row (its assigned single row).

### F9 — non-blocking — `git status` touches `.git` in the lane
- My own `git -C <lane> status --short` (read-only) refreshed `.git` (index stat cache). Lane `status` output was
  byte-identical before and after my runs. No lane tracked or untracked file changed by the seat.

## Positive checks (verified)

- ELF access: C1 v2 imports `mmap`, not `subprocess` for the ELF; `open_elf` uses `mmap.ACCESS_READ`; the pinned sha
  `6737ee24…` is in `OMP_SHA256` (119). No exec of the ELF anywhere in either counter (grep of `subprocess`, `Popen`,
  `os.system`, `os.exec`, `os.spawn`, `exec[lv]p?(` in both files).
- Network: no `socket`, `urllib`, `http`, `requests` import in either counter.
- Credentials / environment: neither counter reads `os.environ` except `TMPDIR` (C2 193; C1 uses `--work` only).
  No `HOME`/secret read. C1 uses frozen constants `/home/u/proj/sub`, `/home/u` (synthetic probe, not the host).
- Lane git writes: none. C2 runs `clone --shared` (read of lane), `rev-parse`, and `checkout --detach` only inside the
  scratch clone, after asserting `rev-parse --show-toplevel` equals the clone (line 69-70). C1 runs `git show` only.
  No `commit`, `add`, `reset`, `stash`, `push`, `checkout` against the lane.
- `..`: C1 rejects `..` segments in patterns, candidates and probes (lines 368-374, 418-419, 490-493, 514-528). C2 has
  no path arguments beyond the revision, which is resolved to a SHA.
- Scratch writes: C1 writes nothing (only `work.mkdir` at 846, arms in memory). C2 writes only under the mkdtemp
  subdirectory it creates and removes it with `shutil.rmtree(work, ignore_errors=True)` (line 212), which cannot touch a
  path outside that subdirectory.

## Scratch and host run (evidence)

Host: Linux, omp 18.15.0 pinned ELF not executed. Scratch `/fast/scratch/hyaku/kotoba-r88/Sentinel`. `TMPDIR` exported to it.

    $ TMPDIR=$S python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test --work $S/w1
    1 failure(s) over 16 assertions
    FAIL arm w_added_red (frozen control): … monotone: DRIFT at rev [... 6 names ...] is a subset of base [... 6 names ...]
    rc=1

    $ TMPDIR=$S python3 -B verifiers/check_omp_root_semantics_v2.py --self-test --work $S/w2
    Traceback … UnboundLocalError: cannot access local variable 'last_absent' …
    rc=1

    $ find /tmp -maxdepth 1 -newer $S/MARK        # after both runs, second listing
    /tmp
    /tmp/alma.log
    /tmp/mori-r17-ctxcheck-8pyr2076

    $ git -C <lane> status --short  (before) == (after)   "lane status unchanged"

Unattributed: one `/tmp/tmpxs3q8h2t` (no v2 prefix) appeared in the first listing and was gone on the next. Neither v2
counter creates a `tmp…` name with no prefix; not attributed, not reproduced.

Verdict on the scratch-argument check (plan item): C1 v2 honours `--work` (mkdir only, arms in memory). C2 v2 does not
honour `--work` for `--self-test` (F3). With `TMPDIR` set, neither run wrote into `/tmp` by its own code path.

## Admission

Blocking: F1 (C1 crash on the no-join-token path), F2 (C2 frozen control red; C2_READY written over red), F3 (C2 ignores
`--work`). Non-blocking: F4–F9. C1 cannot be admitted until F1 and F8 are closed; C2 cannot be admitted until F2 and F3
are closed.
