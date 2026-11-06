# ReviewerCounterV6 — review of the frozen v6 counter + C2 runner (round 98, w1)

Seat: ReviewerCounterV6 (read-only reviewer). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin at
freeze 63cd48d9de2c44eb40691ca05d3a41cc2f9a3248. Instruments under review:
verifiers/fixtures/round-98/selftest-kills.py (v6) and verifiers/fixtures/round-98/forgery-controls.py.
Scratch: /fast/scratch/hyaku/kotoba-r98/ReviewerCounterV6 (removed before yield).

## Byte identity of the instruments

- sha256 selftest-kills.py `2f31fe040c9e0ad7ae2fd87441531610e76c2ac48fa0789d5fb83519d205bd8f`:
  working tree == `git show 63cd48d9:...` == `git show a060b450:...`. Same for forgery-controls.py
  `c4710da772f1c723f3c5449ca37da38a0886f42325e3cd8fe884c033c05c5fdc`. Receipt headers carry the same
  digests. No .gitattributes at the freeze (git archive export-ignore bound is latent only).

## v6 vs v5 diff (saved: w1/ReviewerCounterV6/v6-vs-v5.diff)

- Rules 1-7 code paths unchanged: every `rules == "v5"` gate became `late = rules != "v4"`, which is
  equivalent for v5/v4 modes (v6 file offers one more mode, v6). New code is additive only:
  `non_dumpable()`, `child_env()` (rule 9), the pristine `git archive` export + `.git` guard (rule 8),
  the `except Exception` ladder (rule 10), imports ctypes/tarfile, scratch root kotoba-r98, usage line.
- Table equality (exec'd CLAIMS of both files, compared as Python objects):
  `r97c1 == v5 c1` True; `r96c1 == v5 r96c1` True; `r95c1 == v5 r95c1` True — anchors, replacements,
  counts and positive all byte-equal.
- Anchor uniqueness at freeze: all 9 c1 targets + p00, all 13 r97c1 targets + p00, all 11 r96c1
  targets + p00 match `verifiers/verify_dispatch_prompts.py` exactly once; all 3 r95c1 targets + n10
  match `verifiers/check_mutation_battery.py` exactly once (40 anchors, 0 violations). No mutant
  changes the line count (0 violations) — code decoys are constructible, and indeed all ran.

## `--rules v5` reproduces v5

- Code: per-run `git clone --shared --no-checkout` + `checkout --detach` (history present), env =
  parent env + TMPDIR/PYTHONDONTWRITEBYTECODE + HOME/XDG_CACHE_HOME, marker `# r97-decoy `, seed
  variable KOTOBA_R97_SEED, same job construction and shuffle — identical statements to v5.
- Probe (mid-run world, v5 mode): world/.git PRESENT, `git rev-parse HEAD` = 63cd48d9, shared history
  (evidence in this file's probe log section). Contrast: v6 mid-run world has NO .git (below).
- Probe (patched child printing `sorted(os.environ)`): under v6 the child env is exactly
  `HOME LANG PATH PYTHONDONTWRITEBYTECODE TMPDIR XDG_CACHE_HOME` (all 41 runs); under v5 rules the
  child reads the full parent environ (PARENT-ENVIRON READ-OK bytes=13363, all runs identical).
- Seeded-schedule identity: pending (deadbeefdeadbeef pair v5-c1 vs v6-r97c1 --rules v5).

## Rules 8-10 behaviour probes (scratch copies, real counter logic)

- Rule 8: during a live c2-v6 measure, a v6 per-run world held 12956 files and NO `.git`
  (`.../selftest-kills/run.*/r023.*/world/kotoba-shokunin git=absent`). The counter also refuses an
  export that carries .git (`if (pristine / ".git").exists()`). The only .git dirs under the C2
  scratch are the runner's own committed world repos (worlds/g3..., worlds/g7...), which the counter
  is *supposed* to read REV from — by design, not a rule-8 leak.
- Rule 9 (child env): see above — six variables only, in every run.
- Rule 9 (non-dumpable): with the real counter logic, every child under v6 gets
  `PermissionError: [Errno 13] ... '/proc/<ppid>/environ'` (all 41 runs identical); under
  `--rules v5` the same child reads it READ-OK. prctl(PR_SET_DUMPABLE 0) works on this host.
- Rule 10: a scratch copy made to raise `RuntimeError("probe-boom")` after world setup prints
  `C1-NOT-EVALUATED: unexpected RuntimeError: probe-boom` and exits 2 (no traceback). The same copy
  under `--rules v5` re-raises: Traceback, exit 1 — exactly v5's unguarded behaviour. REPO-as-file
  probe (real counter): `C1-NOT-EVALUATED: REV ... is not a commit of .../notarepo.txt`, exit 2.

## Fail-open review (code walk + probes)

- No silently-skipped run: a failed world copy/clone/archive raises NotEvaluated -> exit 2; the jobs
  loop has no continue-on-error path; `results[...]` lookups would KeyError -> rule 10 exit 2 (v6).
- git archive partial failure: tarfile error -> rule 10 exit 2; short archive then `arch.wait()!=0`
  -> NotEvaluated exit 2. Fail-closed either way.
- Honest pass hiding behind the git-less copy: the honest self-test is behaviourally exercised in the
  same world as the mutants (same cp of the same pristine tree), so a git-less-world breakage would
  fail the honest run too (fail-closed), and poscontrols r97c1/r96c1/r95c1 read MET in that world.
- Minor (low severity, stated here not blocking): if `prctl` ever failed, `non_dumpable()` prints the
  reason in the `rule 9:` line but does not fail the run; the predicate does not gate on it. On this
  host it reads `rule 9: counter non-dumpable` in every receipt and my re-runs. Observable, not
  silent; rule 9's child-env construction does not depend on prctl.
- `/proc/<ppid>/cmdline` and REPO object store reachability remain disclosed bounds (header + plan).

## C2 runner (code walk)

- Counter bytes measured AT REV: `git show REV:<counter>` -> scratch copy; world patches also read
  with `git show REV:<pdir>/<world>.patch`. Working tree never read.
- Worlds built only in scratch (`HYAKU_SCRATCH`-rooted work dir), cloned from the lane to
  `work/worlds/<world>`, checkout 679775ab, toplevel asserted == the scratch repo, patch applied
  `--index`, committed under `forgery <forgery@invalid>`. Lane never mutated.
- Seeding: `base_env` strips KOTOBA_R97_SEED from every measure; only g11 is re-seeded
  (deadbeefdeadbeef). Honest h1 (r96c1 at 801dd9bc) and h2 (r95c1 at REV) run unseeded.
- Scoring per header: refused iff not (rc 0 AND `-PREDICATE-MET`); held iff met; g2b reported, not
  scored; NOT-EVALUATED counts as refused (fail-closed). Table r96c1 for worlds/h1, r95c1 for h2.

## Predicate sentences

- C1: plan and v6 header sentences identical word-for-word (the plan wraps `<C>-PREDICATE-MET` in
  markdown backticks — formatting only).
- C2: condition identical — "forgeries refused 5 of 5 AND honest held 2 of 2"; the plan adds
  parenthetical world lists (g3, g7, g8, g10, g11-seeded / h1, h2) the header omits. The runner's
  FORGERIES and honest lists match the parentheticals exactly. Cosmetic, not semantic.

## Re-runs vs receipts (all at the freeze rev, my scratch)

- redbefore-c1-base: `C1 targets killed 0 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN;
  ... C1-PREDICATE-UNMET`, rc 1 — matches receipts/redbefore-c1-base.txt (0 of 9 UNMET rc 1).
- poscontrol-r97c1-base: `R97C1 targets killed 13 of 13 ... R97C1-PREDICATE-MET`, rc 0 — matches
  receipts/poscontrol-r97c1-base.txt (13 of 13 MET).
- c2-v6: `forgery g3... UNMET; g7 UNMET; g8 UNMET; g10 UNMET; g11 UNMET (honest REPORTED-FAILURE,
  targets still 11 of 11); bound g2b MET; honest h1 MET; h2 MET` →
  `C2 v6: forgeries refused 5 of 5; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-MET`, rc 0 —
  matches receipts/c2-v6.txt line-for-line (fresh world commit hashes differ, as expected for fresh
  forgery commits; g11 refused via honest-not-CLEAN, the seeded replay no longer matches reality).
- Seeded v5 counter c1 @ freeze, KOTOBA_R97_SEED=deadbeefdeadbeef: rc 0, 57 runs,
  `mirror runs reported 14 of 14; seed deadbeefdeadbeef` — the round-97 table is killed by the
  round-97 arms at the base, as expected.
- Seeded v6 counter r97c1 --rules v5, same seed: rc 0, 57 runs, `R97C1-PREDICATE-MET`. Schedule
  comparison: the (kind,name) sequence of all 57 runs and the run indexes are IDENTICAL to the v5
  counter's c1 run under the same seed (first 6: honest, code t04-fleetroot-no-baseline, comment
  t12-finish-single-fail-na, mirror t06-sibling-file-as-lane, honest, blind t01-rstrip-dot).
  `--rules v5` reproduces v5's schedule exactly.
- sources-opened.txt: S277 (subprocess env), S278 (git-archive tree-not-repo), S279
  (proc_pid_environ ptrace mode) carry digest + excerpt and ground rules 9/8/9 respectively; S280
  rejected as redundant with the flip recorded — consistent with the plan's Sourced/Frontier text.

## Findings

- **Blocking: none.** The v6 counter, the C2 runner and the pre-data receipts are mutually
  consistent, fail-closed on every path probed, and the claims' predicates are computable from the
  frozen bytes.
- Low (cosmetic): C2 predicate parentheticals exist in the plan only; the header sentence omits them.
  Condition text identical otherwise (plan backticks aside).
- Low (hardening note, not a defect): `non_dumpable()` failure would be printed in the `rule 9:` line
  but not gate the predicate. It reads `rule 9: counter non-dumpable` in every receipt and in all my
  runs; the child-env construction (the substantive half of rule 9) does not depend on prctl.
- Counter defect check demanded by the seat item: none found — rules 8/9/10 do what their header
  sentences say, `--rules v5` reproduces v5 (code + seeded schedule + env + .git world), and the
  r97c1/r96c1/r95c1 tables are byte-equal to v5's c1/r96c1/r95c1.

## Verdict

Recommend accepting the frozen instruments as the round-98 counting commands. C1's target command at
the freeze correctly reads UNMET 0 of 9 (do-nothing control holds), the positive controls hold, and
C2's target command reads MET 5 of 5 + 2 of 2 with the cause control and do-nothing control reading
3 of 5 as claimed.

## Probe logs (copies under w1/ReviewerCounterV6/)

rerun-redbefore-c1.txt, rerun-poscontrol-r97c1.txt, rerun-c2-v6.txt, probe-v5mode-c1.txt,
probe-env-out.txt, probe-environ-v6.txt, probe-environ-v5.txt, probe-raise-v6.txt,
probe-raise-v5.txt, probe-repo-file.txt, v6-vs-v5.diff.
