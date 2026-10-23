Result: MIXED — C2 does not verify as declared. Its frozen predicate is met by two shortcuts that skip the claimed work: D, a remap of findings 1→2, and S, a standard-library shadow module. Under addendum §9 an exit 0 therefore proves nothing, and the recorded run at `e966cd59` missed anyway (`12 of 13`) because of host load, not because of a patch. Out-of-counter checks show the landed patches are the claimed work, as narrowly worded, and neither shortcut.

Seat: KotobaR55.CriticC2Landed (critic, read-only on the lane). Sandbox: clone `/fast/scratch/hyaku/kotoba-r55/CriticC2Landed` at `f0e6b695`, with worktrees `CriticC2Landed-base` (`f0e5de82`) and `CriticC2Landed-plan` (`a10240c0`). Receipts are under `/fast/scratch/hyaku/kotoba-r55/CriticC2Landed-scratch/`. No installs. No lane writes except this file.

## Ruling 1 — Is the frozen predicate's verdict meaningful when a shortcut meets it?

It means something only in one direction.
- §9 (`/home/vgpnk/Projects/shokunin/scripts/hyaku/lane-addendum.md:212-216`) says: "build the cheapest control that skips the claimed work, score it with the frozen counter … if it meets the target, the counter or target is wrong — fix it before data."
- Lines 217-219 say: "A rule changed after any seat has scored is not the claim's rule."
- `CriticC2Sizing` (`.ufo/waves/round-55/build/CriticC2Sizing.md`, table rows D and S) met `25 of 25; 13 of 13`, exit 0, with two shortcuts that skip the claimed work:
  - D (`9c992b8d`) remaps exit 1 to exit 2.
  - S (`eb97c954`) adds `verifiers/argparse.py` and changes no gate.
- The critic found these after data had been scored, so the counter cannot be fixed for this claim (M50, `corpus/lessons/round-55.md:47`, "Not amended").
- Consequence: under the declared rule, an exit 0 is necessary but not sufficient, so it cannot verify C2. An exit 1 is still a real miss of the declared rule, because no shortcut makes a miss less of a miss.
- The verdict is "does not verify as declared" whatever the tip run prints. Out-of-counter evidence (Ruling 2) can support a trend label. It can never stand in as the claim's rule (lines 217-219).

## Ruling 2 — Do the landed patches use only the P pattern? Yes. Is P the claimed work or a shortcut? It is the claimed work. M50 is wider than its evidence here.

The C2 patch commit is `e966cd5` (8 files, +287/−13, `git diff e966cd5^ e966cd5 -- verifiers/`). The other verifier changes in `a10240c0..e966cd59` are a different kind of work:
- `b04a900`: the C1 counter v2.
- `4d700b1`: `check_gate_registry.py` (routed defect 5, judging lines, by design) and `fault_injection_corpus.sh`. The registry diff adds no exit-2, `rev-parse` or `EnvError` path; its only new `except` is `(SyntaxError, UnicodeDecodeError)` inside `has_flag_handler`.

Each `e966cd5` patch adds only these two things:
- An entry check, `git rev-parse --verify --quiet REV^{commit}`. It is in `box_proof_case_deletion.py`, `check_gate_finding_delta.py` (base and head), `check_overlap_levers.py`, `check_mcp_instructions.py`, `check_description_thresholds.py` and `check_correction_sweep.py`.
- `OSError` mapped to 2 at the git call sites:
  - `box_proof` (`export_tree`)
  - `overlap` (`git_show`, `verify_rev`)
  - `verify_corpus_independent` (`_git` raises `EnvError`)
  - `finding_delta`, `mcp`, `description_thresholds` and `correction_sweep` (their `except` tuples)
  - `check_assertion_floors.py`: a `git --version` preflight that catches only `OSError`

Evidence that this is P and not D, A, S or a label key:
- **Added-line scan** of the `e966cd5` diff, for `except Exception|except BaseException|except:|excepthook|sys.argv|"--self-test" in|returncode == 1|kotoba-r55|nogit-bin|__file__ … in|os._exit|atexit|sys.path`. It has one hit: a local variable `nogit_bin` in the floors self-test (diff line 102). There is no remap, catch-all, excepthook, argv sniffing or label key.
- **The extra `subprocess.CalledProcessError` catch in finding delta** (`check_gate_finding_delta.py:220`) can only come from `git archive` (`:62`) and `git read-tree` (`:83`), both `check=True`. Those are environment failures. The child gate's verdict path does not raise it.
- **Red-anchor control** (CriticC2Sizing correction 2). The same command was run with base gate bytes and tip gate bytes. All 18 runs exit 1 (`anchors.txt`, 00:10:41Z–00:10:48Z):
  - `box_proof --rev f3046466`
  - `finding_delta --base e3371548 --head a10240c0`
  - `overlap --rev 43ca0bfb` and `--rev 7c81a787` (the round-54 before-receipt)
  - `mcp --rev c8579a4c` and `--rev 4c003a4b` (round 51)
  - `description_thresholds --rev 422ffd10` and `--rev e3371548` (round 52)
  - `correction_sweep --rev c8579a4c`

  D and A would give 2 here. Variant A moved the round 51, 52 and 54 before-receipts to 2, and the landed patches do not.
- **Stdout identity.** Those 9 anchors plus 5 runs at `--rev f0e6b695` give stdout identical between base and tip bytes, after stripping `/tmp/…` paths: 14 of 14 `SAME` (`anchor-stdout.txt`). [INFERENCE] The judging lines' output did not move.
- **Hidden regression of naive P.** CriticC2Sizing Q4: the `--root` forms exit 2 with git absent. It is not present here. With git absent, `--root .` exits 0 at both base and tip for `correction_sweep`, `mcp`, `description_thresholds` and `overlap`; with git present all are 0 too (`root-nogit.txt`, 00:11:03Z). The landed checks sit under `if args.rev`. The critic's P (`65f5d237`) instead sniffs `sys.argv`, uses `shutil.which`, and keys on `"--self-test" not in sys.argv` (read in `CriticC2Sizing` clone, `git diff 65f5d237^ 65f5d237`).
- **Self-test arms.** All 7 changed gates I timed run `--self-test`, exit 0 at tip, and gain 2–4 assertions (`selftest-times.txt`):
  - `box_proof` 10→14
  - `correction_sweep` 11→13
  - `description_thresholds` 22→24
  - `finding_delta` 9→12
  - `mcp` 10→14
  - `overlap` 51→53
  - `corpus_independent` 93→95

  Wall time grows by at most 0.8 s. The floors run shows `floors_guard observed=152` at tip against 150 at base.

Why P is the claimed work and not a shortcut:
- The declared claim is "each gate exits 2 on two frozen could-not-evaluate inputs, while it still exits 0 on its own self-test and 0 or 1 on a real revision" (counter docstring, `verifiers/check_could_not_evaluate.py:9-11`; plan `plans/round-55.md:51-54`).
- A revision check and an `OSError` catch are the direct fix for exactly those two inputs, and they leave real verdicts intact, as the anchors show.
- §9's test is "skips the claimed work". P does not skip it. P only shows that the claim is narrow: it saturates on two input classes.

**Correction to M50:** M50 lists "an entry check only (`65f5d237`)" with the remap and the shadow as ways the predicate was met hollowly. Only D and S skip the claimed work. P is the claimed work in its cheapest form. Its naive placement had a `--root` regression the counter does not probe, and the landed patches avoid it. Smallest safe wording for M50: "met … with a remap of findings 1→2 (`9c992b8d`) and a standard-library shadow `verifiers/argparse.py` with no gate change (`eb97c954`); a bare entry check (`65f5d237`) also met it, which shows the claim covers two input classes, not could-not-evaluate in general".

Two defects remain inside the P pattern. Neither moves the claim, since both are outside its two classes. Probe: a fake `git` that prints `fatal: detected dubious ownership in repository` and exits 128, first on PATH, git present (`git128.txt`, 00:12:35Z).
1. **Misattributed diagnostic.** Base gives exit 1 for `box_proof` (tarfile `ReadError`), `finding_delta` (`CalledProcessError` traceback) and `overlap`. Tip gives exit 2 for all 7 git-reading gates I probed, but the message says `revision 'f0e6b695' is not a commit`. Git refused; the revision was not unknown.
2. **Floors preflight ignores git's exit code.** `check_assertion_floors.py`'s preflight (`subprocess.run(["git", "--version"])`, `e966cd5` diff, the `main` hunk at old line 461) does not check `returncode`. The floors run under the exit-128 git exited 2, but only because `harness_independent self-test timed out after 120s` (`floors-git128.txt`). The same run also printed floor failures for three child self-tests whose git calls were refused: `FAIL corpus_independent observed=0 floor=93 summary=missing`, `FAIL sibling_census observed=0 floor=68 summary=missing` and `FAIL overlap_levers observed=0 floor=51 summary=missing`. So the preflight let the refusing git through, and the failures landed on the floor-fail channel. [INFERENCE] Without the timeout, the gate would exit 1 here, as at base (CriticC2Sizing `probes2.txt` §C). The exit code without the timeout was **not checked**.

Out-of-class misses that still exit 1 (corrupt manifest, non-JSON child output, misshapen baseline): CriticC2Sizing Q3. I did not re-run them.

## Ruling 3 — Standard-library-named modules under `verifiers/` at `f0e6b695`: none.

- Interpreter: `python 3.14.8`, `sys.stdlib_module_names` has 297 names; I added `sitecustomize` and `usercustomize`.
- 35 top-level tracked entries under `verifiers/` (`git ls-tree --name-only f0e6b695 verifiers/`). Stem collisions: `[]`.
- Repo-wide, every tracked `*.py|*.pyc|*.so|*.pth` and `__init__.py`: collisions `[]`.
- `a10240c0`: `[]`. `f0e5de82`: `[]`.
- Checked against 25 modules removed from recent standard libraries (`imp`, `distutils`, `asynchat`, `cgi`, …): `[]`.
- No tracked `__pycache__` or `.pyc` files.
- The only `sys.path` edit in a gate is `verify_alwayson.py:576`, which inserts `verifiers/` explicitly.
- [INFERENCE] So the S shortcut is not present at the tip.

## Measurement at the tip

The L1 receipt `.ufo/waves/round-55/C2-measure-e966cd59.txt` reads `could-not-evaluate probes honoured 25 of 25; controls held 12 of 13`, `exit 1`. Its last line shows `check_assertion_floors.py V expect 0|1 got 2 MISS`, at load average 65–104.

I ran `check_assertion_floors.py` (the V form, no arguments) on base bytes and on tip bytes concurrently:
- Base: `exit 2 wall 141s`.
- Tip: `exit 2 wall 142s`.
- Both have one FAIL, `FAIL harness_independent self-test timed out after 120s (hung?)`.
- Load average was 82.7–89.4 (`floors-V-*.txt`, 00:15:0xZ–00:17:25Z).
- `harness_independent` is not touched by any round-55 patch.

So the V miss is load-caused and identical on the untouched base, which confirms CriticC2Sizing Q5. The patches did not cause it.

Counter at the tip, from a checkout of the plan commit `a10240c0`, with `PYTHONSAFEPATH=1` (CriticC2Sizing correction 1). The counter's sha256 is `0c1258e2…56c3d` in both trees. Command:

`PYTHONSAFEPATH=1 timeout 900 python3 -B verifiers/check_could_not_evaluate.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f`

Two runs gave the same result: `counter-tip-safe.txt` (00:10:55Z–00:14:56Z, load average 73.5 → 78.0) and `counter-tip-safe2.txt` (00:15:24Z–00:19:31Z, load average 86.2 → 89.8). Each shows:
- `measured f0e6b695b746775823b65a8c45de7d50ea33e84f`
- `could-not-evaluate probes honoured 25 of 25; controls held 12 of 13`, `exit 1`
- The only MISS is `check_assertion_floors.py V expect 0|1 got 2` (line 52), the same load-caused control miss as at `e966cd59`.

So the declared predicate misses at the tip on this host. The safe-path run moves nothing: with no standard-library-named module present, all 25 probes are still honoured.

## Recommended verdict wording (closure and record)

> C2 operability — **does not verify as declared** (`unprovable-but-better`). Frozen predicate `check_could_not_evaluate.py --rev <rev>` (counter frozen at `a10240c0`): `13 of 25; 13 of 13`, exit 1 @ `f0e5de82` → `25 of 25; 12 of 13`, exit 1 @ `e966cd59`, and the same at the tip `f0e6b695` (re-run under `PYTHONSAFEPATH=1` from a plan-commit checkout). The one control miss is `check_assertion_floors.py` exiting 2 when its nested 120 s `harness_independent` self-test timed out at load average ~100; base gate bytes fail the same control the same way under the same load. A met predicate would not verify the claim either: after data, a remap of findings 1→2 and a standard-library shadow module with no gate change each met it, so under addendum §9 the counter is wrong, and it is not amended. Outside the claim's rule, the landed patches add only a revision check and OSError→2 paths. Every changed gate still exits 1, with stdout identical to base, at nine recorded red anchors. No tracked module has a standard-library name. The `--root` forms with git absent still exit 0. What changed, no wider than that evidence: eight gates now exit 2 on an unknown revision and with git absent from PATH. They do not "honour could-not-evaluate" in general: a corrupt manifest, non-JSON child output and a misshapen baseline still exit 1.

Edits that follow from this, for the L1 to integrate:
- **`SCORECARD.md:140` and `LOG.md` (round-55 entry, line 6 of the block).** Keep "a miss as declared", but add that the miss is load-caused and reproduces on base bytes. Add that a met predicate would also not verify. Avoid any wording that implies the patches failed a control.
- **M50:** narrow it as in Ruling 2. P is not a shortcut.
- **Q37 (`corpus/QUALITY.md:48`):** it names "a gate that remaps real findings to the claimed code". Add the measurement-stability control: the V control must report the gate's stderr, or run on an idle host with `uptime` pasted, because a nested-timeout 2 cannot be told apart from a remap 2 on the counter line. The counter saves no gate output (`check_could_not_evaluate.py:131-136` keeps only `returncode`).

## Minor

- **`check_mcp_instructions.py:274`.** The new self-test arm makes `tempfile.TemporaryDirectory(prefix="mcp-self-test-", dir=LANE)`, so a self-test in the real lane briefly creates an untracked directory in the lane root. It is harmless to the counter, which runs in a temporary clone. A concurrent `git status` or census during the self-test could see it. Smallest fix: drop `dir=LANE`; the arm only needs a PATH directory.
- **`verify_corpus_independent.py` stderr prefix.** It changed from `environment unreadable:` to `could-not-evaluate:`, and exit 2 is unchanged. Grep found no consumer of the old prefix. `fault_injection_corpus.sh:143` captures `err.txt` but does not match on it, and the other hits are exit-code legends in docstrings and corpus prose.

## Commands (exit codes)

- `git diff e966cd5^ e966cd5 -- verifiers/` → saved as `c2.diff` (556 lines). Exit 0.
- Red anchors: 18 runs, all exit 1 (`anchors.txt`).
- Stdout identity: 14 of 14 `SAME` (`anchor-stdout.txt`).
- `--root .` with git absent: 8 runs, all exit 0 (`root-nogit.txt`).
- Fake exit-128 git: base `1,1,1,2,2,2,2`, tip `2,2,2,2,2,2,2` (`git128.txt`). Floors under it: exit 2 from a timeout, plus 3 floor-fail lines with `summary=missing` (`floors-git128.txt`).
- Self-tests: 14 runs, all exit 0 (`selftest-times.txt`).
- Floors V: base exit 2 (141 s), tip exit 2 (142 s), both from a `harness_independent` timeout.
- Standard-library scan: `[]` at `f0e6b695`, `a10240c0` and `f0e5de82`.
- Counter at the tip was run twice under the same guards:
  - `counter-tip-safe.txt`, 00:10:55Z–00:14:56Z, load average 73–78.
  - `counter-tip-safe2.txt`, 00:15:24Z–00:19:31Z.
  - Both printed `25 of 25; controls held 12 of 13`, `exit 1`, and each had one MISS: `check_assertion_floors.py` V got 2.
