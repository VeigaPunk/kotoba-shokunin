Result: MIXED — the instrument's target-directory reader holds against every escape, loop, FIFO, device, huge-file, unreadable and non-UTF-8 probe I ran (all exit 2, no outside byte read), but the C2 counter still executes an out-of-revision delegate given an absolute or `..` disposition (fresh proof: `2 of 8`, exit 0, outside stub executed), and the checklist gate's "delegates outside the map's repo" guard is lexical only, so a symlink inside the repo executes an out-of-repo program twice.

Seat: W2SentinelAlwaysOn. Judged revision `c775d6823bfca8f0de8c0874032a954438b38edc`, sandbox clone
`/fast/scratch/hyaku/kotoba-r53/w2/W2SentinelAlwaysOn` (checked out at that rev). Every write below happened in
that clone (`probe/…`, `probe/mut` a second clone of the lane, used only to create probe commits); the lane was
read only. No tool installed or upgraded (nothing was needed).

## Claims I reproduced first (controls, not my findings)

| Command (sandbox clone) | Exit | Output |
|---|---|---|
| `python3 -B verifiers/check_alwayson_boxes.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 0 | `always-on boxes executed and discriminating 2 of 8` + `alwayson.04: counted (6 of 6 …)`, `alwayson.07: counted (6 of 6 …)` |
| `python3 -B verifiers/verify_alwayson.py --self-test` | 0 | `0 failure(s) over 89 assertions` |

## F1 — BREAKS (Medium) — the C2 counter executes a delegate from outside the measured revision

Trust boundary: `check_alwayson_boxes.py` reads dispositions from the revision under measurement and joins them
to the extracted tree with no relativity check.

- Code: `verifiers/check_alwayson_boxes.py:144` `script = tree / d.split(":", 1)[1]`; `:145` accepts any
  `script.is_file()`; `:135` is the only extraction hardening (`tf.extractall(tree, filter="data")`).
- Fresh proof (both forms in one revision, `probe/mut` HEAD `2abf60af2a78d1fccaa15da43e2b33cfbef7a2b0`):
  `alwayson.04` → `delegated:/fast/scratch/.../probe/evil.py`, `alwayson.07` → `delegated:../../../../../../../fast/scratch/.../probe/evil.py`.
  `python3 -B verifiers/check_alwayson_boxes.py --rev HEAD --repo probe/mut` → exit 0,
  `always-on boxes executed and discriminating 2 of 8`, and `probe/evil.marker` exists with
  `executed alwayson.07 prose-mention` — the out-of-revision stub ran every case. My stub cheats by
  reading the planted case directory name, so it reproduces all 12 pinned verdicts with no rule logic.
- This is the gap the plan erratum §3 admits (`plans/round-53.md:126`). Two precisions the erratum's
  assigned guard does not cover: (a) the guard as written — "relative paths listed by
  `git ls-tree -r <rev>`" — lists symlink entries too; my probe revision's absolute-symlink delegate is
  printed by `git -C probe/mut ls-tree -r --name-only HEAD -- verifiers | grep link-delegate` →
  `verifiers/link-delegate.py`, so that name-check would pass; (b) the real containment on the symlink
  vector is tarfile's `filter="data"`, not any check in the counter — replacing it with
  `filter="fully_trusted"` (`probe/cmut2.py:135`) makes the same revision print
  `2 of 2` exit 0 with `probe/evil.marker` PRESENT, i.e. the delegate is materialised as
  `tree/verifiers/link-delegate.py -> /fast/scratch/.../probe/evil.py` and executed.
- With the judged code (filter intact) the same revision exits 2:
  `cannot evaluate: 'verifiers/link-delegate.py' is a link to an absolute path` — fail-closed, good.
- Impact: the C2 claim is measured on arbitrary revisions; one disposition line makes `2 of 8` exit 0 while
  the executed logic lives anywhere on the host. The claim's evidence chain has no counter-level signal.
- Smallest remediation (no case change; the counter and its 12 cases stay frozen): after
  `rel = d.split(":", 1)[1]`, reject `PurePosixPath(rel).is_absolute()` or `".." in rel.split("/")`, and require
  `not script.is_symlink()` and `script.resolve().relative_to(tree.resolve())`; print the rejected
  disposition verbatim in the `not counted (…)` line.

## F2 — BREAKS (Low) — the denominator `8` is revision-controlled; the exit code cannot see it

- Code: `verifiers/check_alwayson_boxes.py:164` prints `len(section)` from the revision's own map;
  `:166` `return 0 if n == len(CASES) else 1` (hard-coded 2, never 8).
- Proof (`probe/mut`, section reduced to the two alwayson boxes): exit 0,
  `always-on boxes executed and discriminating 2 of 2`; judged revision prints `2 of 8` with the same exit 0.
- Erratum §3 already says `"of 8"` is text-only, so this confirms rather than discovers. It stays Low because
  the printed line differs visibly. Mitigating control is in the other gate, not here:
  `verify_skill_checklist.py:1215` `floor = m.get("box_total")` fails a shrink below the map's declared floor
  — but that floor is declared by the same map, so a revision that lowers `box_total` to 2 and drops the six
  boxes from `SKILL.md` in one commit would pass both [INFERENCE: I did not build that two-sided shrink].

## F3 — BREAKS (Low) — the checklist gate's outside-repo guard is lexical; a symlink defeats it and the program runs

- Code: `verifiers/verify_skill_checklist.py:1244-1253` — `candidate = base / target` then
  `if Path(target).is_absolute() or ".." in target.split("/")`. `:924` `is_instrument` uses `is_file()` and
  `:956` `os.access(candidate, os.X_OK)`; both follow symlinks. No resolved-containment test anywhere.
- Positive controls (guard works for the forms it names), by calling `check_box_map` with
  `repo=map_repo=/fast/scratch/.../probe/gate`:
  `delegated:/fast/scratch/.../probe/outside/evil.py` → FAIL, detail
  `map entry alwayson.07 delegates outside the map's repo: '…/probe/outside/evil.py'`;
  `delegated:../../outside/evil.py` → FAIL, `delegates outside the map's repo: '../../outside/evil.py'`.
- Escape: `delegated:verifiers/link-evil.py` where `probe/gate/verifiers/link-evil.py` is a symlink to
  `probe/outside/evil.py`. Result: no delegation problem recorded, and the outside file ran twice —
  marker contents `ran with argv=['--help']` and
  `ran with argv=['--box-proof', '--map', '…/probe/gate/verifiers/checklist-baseline.json']`.
- Second variant, no suffix: `delegated:verifiers/hostprog` (symlink to an executable host program).
  `is_instrument` → True (shebang through the link), `instrument_command` →
  `['/fast/scratch/.../probe/gate/verifiers/hostprog']`, i.e. the host program is executed directly with
  `--box-proof`; a program that prints `--box-proof` on `--help` and exits 0 launders an unproven delegation
  into "exit 0".
- Impact: the guard's own sentence — "delegates outside the map's repo" — is false for symlinks; a map-repo
  snapshot taken from an untrusted source can run arbitrary host programs under the gate's identity and mark
  a delegation proven. Marginal gain over the by-design execution of repo instruments, hence Low.
- Overlap: `falsify/W2ReviewChecklistDelegate.md` § Residual risk declares this exact vector "pre-existing …
  Not treated as a defect". My probe shows it is reachable and executes, so it should be recorded as a named
  residual with evidence rather than dismissed. It predates this round (round-16 R2 shape), which is why I do
  not raise it above Low.
- Smallest remediation: after `candidate = base / target`, wrap
  `candidate.resolve(strict=True).relative_to(base.resolve())` and append the same "delegates outside the map's
  repo" problem on `ValueError`; one self-test arm beside `delegated-escape`
  (`verify_skill_checklist.py:2054`). Exit code on the real map does not change.

## F4 — BREAKS (Low, race-gated) — the rule-file reader opens before it checks regular-ness, so a FIFO blocks forever

- Code: `verifiers/verify_alwayson.py:203` `os.open(resolved[-1], flags, dir_fd=parent_fd)` with
  `O_RDONLY|O_NOFOLLOW` and no `O_NONBLOCK`; only then `:209` `os.fstat`, `:210` `S_ISREG`.
- Deterministic proof at the function boundary (FIFO named `AGENTS.md`):
  `timeout 6 python3 -c "… va._read_resolved(root, 'AGENTS.md', ('AGENTS.md',))"` → exit **124**, i.e. the
  open blocked until the timeout killed it. Nothing printed.
- Reachability is narrower than it looks: `_resolve_candidate` rejects a FIFO, a symlink to a FIFO and a
  device before the read (probes P7/P14/P16 below, all exit 2 `is not a regular file`), so the hang needs a
  resolve→open swap. I raced it (a swapper renaming a FIFO over `AGENTS.md` while running the gate) for 400
  attempts: `attempts=400 hangs=0` — I did **not** observe a hang through `evaluate`. Treat reachability as
  [INFERENCE]: a writer with access to the audited directory wins the gate's usability, not its verdict.
- Blast radius: the gate is called by `verify_skill_checklist.py` with `BOX_PROOF_TIMEOUT = 120`
  (`:313`) and by the counter with `TIMEOUT = 20` (`check_alwayson_boxes.py:61`); both degrade to "not
  counted"/timeout, so the failure mode is a lost measurement, never a false PASS.
- Smallest remediation: open with `O_NONBLOCK` added to the flags (or `O_PATH`, `fstat`, then reopen) so a
  non-regular file is rejected before a blocking open.

## F5 — BREAKS (Low) — metadata reads are unbounded and follow symlinks, unlike the rule-file reader beside them

- Code: `verifiers/verify_alwayson.py:437` (`_load_fixture_map` → `manifest.json`), `:554` (`--box-proof` map),
  `:568` (live `SKILL.md`), all plain `read_text()`. The rule-file path in the same module is capped
  (`MAX_FILE_BYTES`), no-follow, regular-only.
- Proof: `probe/oomsuite/fixtures/manifest.json -> /dev/zero`, run under
  `resource.setrlimit(RLIMIT_AS, 256 MiB)` with `main(['--box-proof','--fixtures','probe/oomsuite/fixtures'])`
  → `MEMORYERROR: unbounded metadata read (manifest symlink to /dev/zero)`.
- Impact: DoS on the gate only (no code exec, no data printed); requires write access to the verifiers tree,
  which is already trusted for the map's content. Reported because the asymmetry is a latent trap: the same
  hardening the module already implements is one helper away.
- Smallest remediation: one bounded `open(..., O_NOFOLLOW)` + `fstat` reader reused for all three reads.

## F6 — Info — fail-closed false positive on a repo whose `.claude` points outside

`ln -s /home/vgpnk/.claude <target>/.claude` → exit 2,
`symlink for .claude/AGENTS.md escapes target directory`, for the whole box. No leak, no false PASS, but the
instrument refuses to audit any repo using that layout, and none of the six pinned cases exercises it. Not a
security defect; recorded so the L1 can decide whether it belongs in the operability note.

## Attacks that HOLD (evidence, exit codes)

All against the judged `verifiers/verify_alwayson.py`, targets under `probe/work/`:

| # | Probe | Exit | Observed detail |
|---|---|---|---|
| P1 | `AGENTS.md -> /etc/passwd` (outside file) | 2 | `symlink for AGENTS.md escapes target directory` |
| P2 | `.claude -> <outside dir>` with `AGENTS.md` inside | 2 | `symlink for .claude/AGENTS.md escapes target directory` |
| P3 | `AGENTS.md -> CLAUDE.md -> AGENTS.md` | 2 | `too many symlink hops for AGENTS.md` |
| P4 | `sub/loop -> ../sub` beside a plain `AGENTS.md` | 0 | PASS, `1 selected files` (loop never entered) |
| P5 | `.claude -> .claude` (self-referential dir) | 2 | `too many symlink hops for .claude/AGENTS.md` |
| P6 | 2 MiB `AGENTS.md` | 2 | `exceeds the 1048576-byte limit` (size checked before any read: `:212` precedes the read loop) |
| P7 | FIFO named `AGENTS.md` | 2 | `AGENTS.md is not a regular file` |
| P8 | `AGENTS.md` mode 000 | 2 | `cannot open AGENTS.md without following links ([Errno 13] Permission denied)` |
| P9 | `AGENTS.md` with `\xff\xfe\x00` | 2 | `AGENTS.md is not UTF-8 text` |
| P10 | `--target` is a regular file / absent | 2 / 2 | `target is not a directory` / `cannot read target directory … [Errno 2]` |
| P11 | `CLAUDE.md -> <absolute path inside target>` | 0 | PASS, `2 selected files; no independent AGENTS/CLAUDE pair` — the documented redirect form still works |
| P12 | `AGENTS.md -> /nonexistent/file` | 2 | `symlink for AGENTS.md escapes target directory` |
| P13 | `AGENTS.md -> ../escapee.md` (relative escape) | 2 | `symlink for AGENTS.md escapes target directory` |
| P14 | `mknod AGENTS.md c 1 5` (char device) | 2 | `AGENTS.md is not a regular file` |
| P16 | `AGENTS.md -> pipe` (symlink to FIFO) | 2 | `AGENTS.md is not a regular file` |
| P17 | target directory mode 000 | 2 | `cannot read target directory … [Errno 13]` |
| P18 | `AGENTS.md` is a directory | 2 | `AGENTS.md is not a regular file` |
| P19 | `.claude` is a regular file | 2 | `non-directory path component in .claude/AGENTS.md` |

Structural HOLDS, by reading the code:

- The instrument never executes or writes anything from the target: no `subprocess`, `os.system`, `exec(`,
  `eval(`, `write_text`, `mkdir`, `unlink`, `chmod` anywhere in `verifiers/verify_alwayson.py` (grep returns
  nothing).
- `_read_resolved` re-opens the final component with `O_NOFOLLOW` after resolution (`:203`), and
  `_open_directory` (`:114-127`) uses `O_NOFOLLOW|O_DIRECTORY` for every component, so a directory swapped for
  a symlink between resolve and read is refused rather than followed.
- A dangling symlink is an ERROR, not a skip (`:161-163`), so it cannot be used to make a candidate disappear.
- Absolute-but-inside symlink targets are re-rooted with `relative_to(root)` (`:168-177`), and a target that
  merely string-prefixes the root (`/tmp/ab` vs root `/tmp/a`) fails that component-wise test.
- The relative `..` escape is refused at `:140-142` when the resolved stack is empty.
- Judged revision's own map is clean: `git show c775d682:verifiers/checklist-baseline.json` gives
  `alwayson.04`/`alwayson.07` = `delegated:verifiers/verify_alwayson.py` (relative, section pinned,
  `box_total` 41), and `git ls-tree -r c775d682 -- verifiers/verify_alwayson.py` →
  `100755 blob a761c9d0…` (regular blob, not mode 120000). The erratum's disposition guard holds *at this
  revision*; its weakness is only against a future revision (F1).
- Adversarial delegate strings do not crash the gate: NUL in the target, a 4000-component path, a trailing
  slash and a space-only target all produce FAIL 2 with a problem line, no traceback.

## Observations (not the claim)

- `verify_alwayson.py --check alwayson.04 --target /home/vgpnk/Projects/shokunin/kotoba-shokunin` → PASS
  (`no recognized date or transient cue in 1 selected files`); `alwayson.07` → PASS
  (`1 selected files; no independent AGENTS/CLAUDE pair`); the fleet root `/home/vgpnk/Projects/shokunin`
  → PASS for `alwayson.04`. Reported as observations only.
- Running `verify_alwayson.py --box-proof` without `-B` writes `verifiers/__pycache__/` (gitignored,
  `.gitignore:2`); both real callers pass `-B`, so no lane pollution in practice.

## Residual risk / gaps in my own work

- The FIFO hang through the public CLI is race-gated; I demonstrated the blocking `os.open` deterministically
  and failed to win the race in 400 attempts. Labelled [INFERENCE] where it matters.
- F2's two-sided shrink (map `box_total` lowered together with the `SKILL.md` boxes) is reasoning from
  `verify_skill_checklist.py:1215`, not a run.
- I attacked only this surface: the always-on instrument, the C2 counter, and the checklist gate's delegate
  path. C1, the SOURCES rows and the census are other seats' targets.
