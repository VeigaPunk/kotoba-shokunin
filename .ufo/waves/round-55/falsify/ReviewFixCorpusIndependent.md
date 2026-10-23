# ReviewFixCorpusIndependent — C2 patch review: `verifiers/verify_corpus_independent.py`

Result: DONE — The C2 change to `verify_corpus_independent.py` (a10240c0 → e966cd59, byte-identical to tip f0e6b695) conforms to every checked item: judging lines and clean-path output are byte-identical on the same input, exit 1 findings are never remapped to 2, there is no argv/temp-dir/PATH keying, the two new self-test arms assert the fixed exit code and stderr prefix and fail on either revert, a real drift finding exits 1 under both code versions, and both measured revisions print the same verdict (`exit 1`). The only behaviour change is exactly the intended one: a git-dependent invocation with git absent now exits 2 (`could-not-evaluate: git not runnable: ...`) instead of dying on `FileNotFoundError` (exit 1 via traceback).

Scope: lane frozen counter `verifiers/check_could_not_evaluate.py` and `verifiers/verify_surfaces.py` are unchanged a10240c0 → f0e6b695 (`git diff a10240c0 f0e6b695 -- <both files>` → empty). The patch under review is the whole change to this gate: `git diff a10240c0 e966cd59 -- verifiers/verify_corpus_independent.py` → 22 insertions, 6 deletions; `git diff e966cd59 f0e6b695 --` for this file → 0 lines (commit e966cd59 is the only commit in range touching it). Frozen probe shape for this gate (`check_could_not_evaluate.py:81`): `(real=[], rprobes=[])` — no R probes; G = default form `[]` with git absent expecting 2; S = `--self-test` expecting 0; V = `[]` expecting 0|1. All runs in sandbox clone `/fast/scratch/hyaku/kotoba-r55/ReviewFixCorpusIndependent` at f0e6b695; lane file untouched (sha256 `8b66d62b…f7c8` identical lane vs clone). No tools installed. `date -u` at run time: `Fri 23 Oct 2026 12:19:54 AM UTC`.

## The diff, in full

- `EnvError` docstring reworded (doc only).
- `_git()` (`:65-71`): `subprocess.run(["git","-C",repo,*args], …)` wrapped in `try/except OSError` → `raise EnvError("git not runnable: %s")`. Nothing else changes; non-zero git returncodes still surface as `CompletedProcess` to the callers (`tracked_paths`, `analyse`, `analyse_commits`), untouched.
- `self_test()` (`:989-1001`): two new end-to-end arms — child run `--repo <clean fixture>` with `PATH` set to a directory holding only a `python3` symlink; asserts `returncode == 2` and `stderr.startswith("could-not-evaluate: git not runnable:")`.
- `main()` (`:1030`): the pre-existing `except EnvError → stderr + return 2` stderr prefix `environment unreadable:` renamed to `could-not-evaluate:` (could-not-evaluate path only).

## Check 1 — judging lines unchanged (PASS)

Everything that reads, compares, counts, or prints on the clean path is byte-untouched: `POINTER_RE`/`COMMIT_RE`/`FENCE_RE`/`HEX_RE`, `coverage_cells`, `expand_braces`, `analyse_index`, `analyse_pointers`, `analyse_commits`, `analyse`, `results_of`, `violations`, `exit_code`, `render` (all `:100-559`), and `main`'s verdict path. Proof: same repo, both code versions → byte-identical stdout. On the sandbox worktree of f0e5de82:

```
python3 scratch/gate_base.py --repo scratch/wt-f0e5 > out_base_f0e5.txt   # rc=1
python3 scratch/gate_tip.py  --repo scratch/wt-f0e5 > out_tip_f0e5.txt    # rc=1
diff -u out_base_f0e5.txt out_tip_f0e5.txt  → no output; OUTPUT-IDENTICAL
```

Also byte-identical on a minimal clean fixture (exit 0) and `--json` on a drifting fixture (`diff` empty; both rc=1). The only output change anywhere is the stderr prefix on the exit-2 path, which the lane registry (`SKILL.md:471`, verdict map `2=could-not-evaluate`) sanctions; no lane consumer greps `environment unreadable` (grep: only knowledge-doc prose; sibling gates already print `could-not-evaluate:`).

## Check 2 — no exit-1→2 remap, no catch-all, no keying (PASS)

- The new `except OSError` sits inside `_git`, around process spawn. It fires only when the git child cannot be exec'd at all (`ENOENT`/`EACCES`/`E2BIG`) — environment inability by definition. Findings can only be emitted after `analyse()` completes; a git exec failure mid-analysis discards everything, so a computed finding can never reach exit 2 through this path (verified code-path-wise; no post-analyse `_git` call exists).
- No `except Exception`/`BaseException` anywhere; `FileNotFoundError` was an uncaught traceback at base for all callers, now uniformly `EnvError` → 2. `ValueError`/`UnicodeDecodeError`/etc. remain uncaught, as at base.
- `grep -n "argv\|PATH\|environ\|mkdtemp\|sys.executable\|sys.argv"` on the tip file: PATH/tmpdir/`sys.executable` reads appear only inside `self_test()` (`:708,992-994`); `os.environ["HOME"]` in `resolve_pointer` (`:205`) is pre-existing judging code, unchanged. No keying on argv shape, temp names, or PATH strings in the verdict path.
- The `except EnvError` in `main` is a *rename* of the prefix on an existing path, not a widened catch — base already mapped EnvError to 2.

## Check 3 — self-test arms assert exit codes and fail on revert (PASS)

Tip self-test: `python3 scratch/gate_tip.py --self-test` → `self-test: 95 assertions, 0 failures`, **rc=0** (`ok 94 - cli: unavailable git exits 2`, `ok 95 - cli: unavailable git reports could-not-evaluate`).

Two partial-revert variants (new arms kept, production change reverted one at a time):

```
# Variant A — _git OSError→EnvError reverted to base shape:
python3 scratch/gate_revert_git.py --self-test
  not ok 94 - cli: unavailable git exits 2: got 1 want 2
  not ok 95 - cli: unavailable git reports could-not-evaluate: got False want True
  self-test: 95 assertions, 2 failures   → rc=1

# Variant B — stderr prefix reverted to "environment unreadable:":
python3 scratch/gate_revert_msg.py --self-test
  ok 94 - cli: unavailable git exits 2
  not ok 95 - cli: unavailable git reports could-not-evaluate: got False want True
  self-test: 95 assertions, 1 failures   → rc=1
```

So arm 94 pins the `_git` fix and arm 95 pins the stderr prefix; neither is vacuous. (A full revert to the a10240c0 file also removes the arms and passes its own 93-assertion self-test — inherent to shipping test+fix in one commit; not a defect.)

## Check 4 — red anchor: real finding exits 1 at base, still 1 at tip (PASS)

Fixture `scratch/fix-drift`: `corpus/` with `knowledge/orphan.md` tracked but absent from the README coverage map → `unindexed=1` → DRIFT.

```
python3 scratch/gate_base.py --repo scratch/fix-drift  → ... corpus.index.unindexed zero observed=1 DRIFT
                                                       ! corpus/knowledge/orphan.md ; exit 1 ; rc=1
python3 scratch/gate_tip.py  --repo scratch/fix-drift  → byte-identical output ; exit 1 ; rc=1
```

A stronger in-repo anchor: f0e5de82 itself is a real exit-1 input (unindexed spotcheck lesson + unresolvable commit citation), and base vs tip code produce byte-identical exit-1 output on it (Check 1). The finding path is fully preserved.

## Check 5 — real verdict at f0e5de82 and f0e6b695 prints the same summary line (PASS)

Each revision's own gate on its own tree:

```
f0e5de82 (worktree scratch/wt-f0e5):  ... commit_unresolvable  observed=1 DRIFT ; exit 1 ; rc=1
f0e6b695 (clone root):                ... commit_unresolvable  observed=1 DRIFT ; exit 1 ; rc=1
```

Same summary line `exit 1` and same verdict column at both revisions. Counts differ only where the measured corpus differs (`tracked_files` 82→84, `index_tokens` 99→102, `unindexed` 1→0 — the spotcheck lesson gained coverage at tip), as expected when the measured revision changes; the code change itself alters nothing (byte-identical output on the same tree, Check 1).

Context, not a finding of this patch: both revisions' exit 1 is driven by `commit_unresolvable=1` — `corpus/lessons/round-54-verifier-spotcheck.md:147` writes `commit \`451a02ff\`` inside a double-backtick span; the gate's `COMMIT_RE` counts it (only `"`-quoted spans are excluded) and `451a02ff` is genuinely absent from the lane object store (`git cat-file -e 451a02ff^{commit}` → rc=128; it is a gemini-cli upstream commit). This is pre-existing corpus/judgement interaction identical at base and tip — the gate is honestly reporting drift; whether the citation deserves exclusion is a corpus-side question outside this patch's scope.

## Check 6 — `--root`/default forms without git (PARTIAL-WORDING NOTE; tip behaviour is the intended fix)

This gate's argument is `--repo` (there is no `--root`); forms probed with `PATH=<dir holding only a python3 symlink>`:

```
base  --root <dir>  → rc=2  (argparse "unrecognized arguments: --root …")
tip   --root <dir>  → rc=2  (identical argparse rejection)   ← keeps base exit code
base  --repo <dir>  → rc=1  (FileNotFoundError traceback)
tip   --repo <dir>  → rc=2  (could-not-evaluate: git not runnable: [Errno 2] …)   ← the fix
base  <no args>     → rc=1  (FileNotFoundError traceback)
tip   <no args>     → rc=2  (could-not-evaluate: git not runnable: …)             ← the fix
base  --self-test   → rc=1  (FileNotFoundError traceback)
tip   --self-test   → rc=1  (uncaught EnvError traceback — fixture construction needs git)  ← keeps base exit code
```

The git-dependent forms (`--repo`, default) change 1→2 — that is precisely the class-G probe the counter's `([],[])` real-args G run measures, and the registry verdict map (`SKILL.md:471`) declares 2 for it. Forms that do not reach analysis (unrecognized `--root`, `--self-test` environment failure) keep their base exit codes exactly. Read literally, "keep their base exit code" cannot hold for the git-dependent forms — that would mean the fix does nothing; the observed split is the correct reading.

## Residual risk / verification gaps

1. `except OSError` around the spawn also converts exotic spawn failures (`EACCES` on a non-executable `git`, `E2BIG`) to 2 — all are honest could-not-evaluate, never a verdict; no realistic path remaps a computed finding.
2. `EnvError` raised mid-analysis by a *non-zero git returncode* (e.g. `ls-files` failing on a corrupt repo) was already 2 at base — unchanged.
3. `--self-test` under a no-git PATH still traceback-exits 1 rather than 2 at tip; same as base, and outside the frozen probes (the counter always runs S with normal PATH). Not a defect for C2; noted for completeness.
4. I did not re-run the full 25-probe counter (assigned to `W2RerunC2`); this gate's three registered lines (G, S, V) were exercised directly with the counter's own argument shapes and PATH mechanics and behave as the predicate requires (2 / 0 / 1-or-0).

No installs were needed (python3, git, diff, sha256sum — all pre-existing).
