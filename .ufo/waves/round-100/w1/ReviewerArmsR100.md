# ReviewerArmsR100 — review of the C1 patch (ExecArmsR100)

Seat: ReviewerArmsR100 (round 100, wave r100-w1). Verdict: **no blocking findings — the C1 patch
is sound and its claim reads MET on my own candidate build.**

- Patch reviewed: `.ufo/waves/round-100/w1/ExecArmsR100/ExecArmsR100.patch`
  (sha256 `7b4e2dbc2450ebbc34360c557897b9b60f0895005cd1d0d631b4dac1746c857e`, matches READY).
- Candidate built by me: `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687` + that patch = scratch-clone
  commit `56dadcc569edc455049411ac755a98d7a7ac5803` (scratch identity, `rev-parse --show-toplevel`
  asserted = the scratch repo before commit). Patch applied with `git apply` (and `--check` first)
  on a clean clone at the freeze.

## 1. Static review

- **Production byte-identity outside `self_test()`:** the diff is ONE file, ONE hunk
  (`@@ -1781,6 +1781,150 @@`), 144 insertions, 0 deletions; the hunk sits inside `self_test()`
  (spans 679–1791 at base), immediately after the `r99-t12` arm and before the failure print.
  Everything outside `self_test()` is byte-identical (pure insertion cannot move other bytes; diff
  context confirms). No second file in the commit.
- **ANTI-SNIFFING:** every new arm observes behaviour only — `_run_main(...)` (in-process `main`
  with explicit argv), direct `read_text(...)` and `run_checks(...)` calls on fixture inputs — and
  asserts on the returned values/exit codes. No arm reads the checker's own source (no `__file__`
  read, no `inspect`, no compile/read of the instrument), no git, no network, no environment reads.
  Corroborated dynamically: source-blind AND mirror runs are REPORTED-FAILURE for every target
  (mirror runs reported 7 of 7), which a source-reading arm cannot fake symmetrically.
- **FROZEN ANCHORS:** counted all 7 anchor texts (t01..t06 + p00 `stem = stem[:-3]`) on the
  candidate's committed file — each still matches **exactly once** (base reference also 1 each).
  The new code deliberately avoids the anchor shapes: no `for cid in wanted:` (t06 arm iterates
  `t06_results`), no `is_dir` call at all, no `return path.read_text(...)`.
- **Every assertion goes through `rec(...)`:** t04's mutant world raises `NotADirectoryError`
  inside `_run_main`; the helper converts it to `rc=-1` + `err="raised NotADirectoryError…"` and
  the arm's own `try/except` is belt-and-braces — the run still prints the summary and exits 1
  (REPORTED-FAILURE), never a RUN-ERROR. Counter: `run errors 0`.
- **Fixture hygiene:** all fixtures live under the `self_test` `TemporaryDirectory` (`_main_case`
  builds under `root`, TMPDIR-honoured). The chmod-000 file is restored `0o600` in a `finally`
  before the cleanup; on this host (uid 1000) the real EnvError branch ran — evidenced by the t02
  kill reading `got (1, ...)`, impossible under the root-skip branch.
- **No leak between arms:** `_run_main` (base helper, unchanged) captures stdout/stderr with
  `contextlib.redirect_stdout/stderr` inside a `with` and guards `main` exceptions internally, so a
  raising arm cannot leak redirections; argv is passed explicitly per call and `build_parser()` is
  rebuilt per `main` call, so no argv/argparse state carries between arms.
- **t02 guard:** `os.access` skip records a PASSING assertion (honest stays CLEAN as root) instead
  of a false failure — exactly the instructed guard.

## 2. Manual mutant kills (each anchor applied by hand to the candidate; receipt
`ReviewerArmsR100/manual-mutants-cand.txt`)

All 7 substituted worlds: rc 1, REPORTED-FAILURE, summary present. The assertion that fails, per
target (honest baseline: `0 failure(s) over 168 assertions`, rc 0 — 154 + 14 new):

| target | failing assertion (`self-test FAIL: …`) | got | failures |
|---|---|---|---|
| t01-notdir-exit-zero | `r100-t01-notdir-exit-zero: main() with a plain file as --prompts exits 2` | `(0, '', 'ERROR … not a directory …')` | 4 / 168 |
| t02-enverror-exit-one | `r100-t02-enverror-exit-one: main() over a prompts dir holding a mode-000 prompt exits 2, not 1` | `(1, '', 'ERROR … Permission denied …')` | 1 / 168 |
| t03-json-exitcode-zero | `r100-t03-json-exitcode-zero: the emitted JSON payload's exit_code is 2` | `{'checks': [], … 'exit_code': 0 …}` | 1 / 168 |
| t04-dircheck-exists | `r100-t04-dircheck-exists: main() with a plain file as --prompts exits 2` (caught, not a crash) | `(-1, '', "raised NotADirectoryError(20, …)")` | 6 / 168 |
| t05-readtext-latin1 | `r100-t05-readtext-latin1: read_text returns exactly that UTF-8 text` | `'cafÃ©\n'` | 1 / 168 |
| t06-runchecks-sorted | `r100-t06-runchecks-sorted: run_checks returns results in request order` (request `[08, 04]`) | `['dispatch.04', 'dispatch.08']` | 1 / 168 |
| p00 (positive) | control/`t01-rstrip-dot`/proof arms, as at base | — | 12 / 168 |

Each kill is for the stated reason (MutTesterDispatchR99 § Differential witnesses / F2 / F3 / F5);
t06 is killed by the F3 discriminator itself — the arm requests `["dispatch.08", "dispatch.04"]`
and asserts request order, so a stable sort by id does NOT survive. Under t04 the t01/t03 arms also
fail (over-kill, harmless).

## 3. Counter readings on my candidate `56dadcc` (instrument at `d1e1170` bytes, lane path)

- `selftest-kills.py c1 56dadcc… $D` → `C1 targets killed 6 of 6 (run errors 0); positive killed
  1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6` / `rules v6: honest
  runs CLEAN 3 of 3; mirror runs reported 7 of 7` / **`C1-PREDICATE-MET`**, rc 0. (receipt
  `ReviewerArmsR100/c1-cand.txt`, seed `466f3fb2e0d67842`)
- `c1 … --rules v5` → same tally, **`C1-PREDICATE-MET`**, rc 0. (`c1-v5-cand.txt`, seed
  `d488f3daef60b719`)
- `r99c1` → `R99C1 targets killed 12 of 12 … R99C1-PREDICATE-MET`, rc 0 (`r99c1-cand.txt`).
- `r98c1` → `R98C1 targets killed 9 of 9 … R98C1-PREDICATE-MET`, rc 0 (`r98c1-cand.txt`).
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` on the candidate tree →
  `boxes proven 2`, rc 0.
- Honest candidate self-test, direct: `0 failure(s) over 168 assertions`, rc 0 (`honest-cand.txt`).

All kill-rule conjuncts I can observe hold: anchors match, r99c1/r98c1 MET, box-proof 2 rc 0,
production outside `self_test()` unchanged, no counter bytes touched by this patch.

## Findings (by severity)

Blocking: none.

Non-blocking observations:

1. **t02 kill is host-dependent (disclosed, correctly guarded).** As root the mode-000 arm records
   its passing skip assertion and t02 would survive; C1-PREDICATE then reads UNMET on a root
   re-read. This is the instrument's own documented bound (instrument `t09` arm carries the same
   guard; round-99 report: "this run is uid 1000"). The L1's scored landing reading must run as a
   non-root uid, as all round-100 receipts did.
2. **t04 arm's first rec is vacuously true in the mutant world** ("raises no exception" passes
   because `_run_main` converts the raise to `rc=-1`); the kill is carried by the "exits 2" rec
   (and the ERROR-line rec). Cosmetic; kill strength unaffected.
3. Honest assertion count grows 154 → 168. No predicate pins the count (C1 needs CLEAN only), and
   the C2 checklist floor is a different instrument's self-test — unaffected.

## Residual risk and verification gaps

- I measured C1 at its own candidate (base + ExecArmsR100 only), per § Separability; the L1's
  landing re-read (all three patches + corpus-baseline re-record) is the scored one and is not
  mine. `--rules v4` was not in my item's list and was not run.
- The counter's own disclosed bounds (state outside per-run dirs, `/proc/<ppid>/cmdline` readable)
  apply unchanged; nothing in this patch exploits them.

## Files written (all under `.ufo/waves/round-100/w1/ReviewerArmsR100/` + this report)

`c1-cand.txt`, `c1-v5-cand.txt`, `r99c1-cand.txt`, `r98c1-cand.txt`, `manual-mutants-cand.txt`,
`honest-cand.txt`. Scratch `/fast/scratch/hyaku/kotoba-r100/ReviewerArmsR100` deleted before
yielding. No lane file outside my w1 dir and this report was written; no git/jj write outside the
scratch clone.
