# ReviewerArmsR99 — review of the C1 patch (ExecArmsR99)

Status: **COMPLETE — no blocking findings.** All checks below executed on the evidence named.

## Subject
- Patch: `.ufo/waves/round-99/w1/ExecArmsR99/ExecArmsR99.patch`, sha256 `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924` (READY pending at review start; commit-diff.txt identical modulo `a/b` vs `c/i` diff-prefix letters, i.e. `git diff --cached --binary` form — content equal, `git apply` fine).
- Base: freeze `b53e209603e7c480cd975ea543e415b66f695438`; candidate (scratch commit, identity `scratch <scratch@invalid>`): `61a20f8cd85bf9718736310c49cf58ddfc27a0d7`.
- Scratch: `/fast/scratch/hyaku/kotoba-r99/ReviewerArmsR99` (clone `.../repo`, `rev-parse --show-toplevel` = clone path; git-less world `.../world` via `git archive HEAD`).

## Production bytes (blocking check: PASS)
- `git apply --check` on the freeze: OK.
- `git diff --stat b53e2096..61a20f8`: `verifiers/verify_dispatch_prompts.py | 270 +++++++++++` — 270 insertions, 0 deletions, ONE hunk `@@ -1512,6 +1512,276 @@ def self_test() -> int:`. The hunk sits inside `self_test()` (inserted after the round-98 arms, before the `for f in failures:` summary block). All production code (`read_text` … `box_proof`/`main`) byte-identical.
- FROZEN ANCHORS: mechanical audit (`anchor_audit.py` importing `CLAIMS` from the frozen counter) — all 53 anchors of `c1`, `r98c1`, `r97c1`, `r96c1` (on `verify_dispatch_prompts.py`) and `r95c1` (on `check_mutation_battery.py`) match exactly once in the candidate and once in the base; `anchors bad: 0`. No new occurrence of any anchor text anywhere in the file (the new arms build map/manifest data but never restate a comparison line, `for cid in wanted`, `live = {}`, `entries[e.get("box_id")] = e`, `if fails:\n        status = "FAIL"`, `stem = stem[:-3]`, the L1/ROUND regexes, or `main`'s `code =`/`wanted =` lines).

## Anti-sniffing (PASS)
- Every new arm calls a production function on fixture inputs and asserts the observed result: `lane_of` + `evaluate_dispatch_04` (t01), `evaluate_dispatch_08` + `_verdict_of` (t02), in-process `box_proof` via `run_proof` (t03/t04/t05/t10/t11), `run_checks` (t06), `main` via `_run_main` (t07/t08), `evaluate_dispatch_04` (t09), `evaluate_dispatch_08` (t12). No arm reads the checker's source, `__file__` text, git, network, or any environment variable. The only file reads are fixture data (the temp proof tree's SKILL.md copy in t04 — data, not checker source).
- Every assertion goes through `rec(...)` (the `self-test FAIL: ` prefix); t06 wraps `run_checks` in try/except → `rec`; `_run_main` catches any exception into the captured stderr and returns rc −1 → `rec`; t09 catches `EnvError`/other exceptions → `rec`. Hand runs confirm every kill is a REPORTED failure (rc 1 + `self-test FAIL: ` lines + `N failure(s) over 154 assertions`, N ≥ 1), never a crash/RUN-ERROR.
- t07/t08 main() arms: `_run_main` passes argv explicitly to `main(argv)` (argparse `parse_args(argv)` — no `sys.argv` mutation) and captures stdout+stderr in-process via `contextlib.redirect_*`; no leak between arms (each `main()` call parses fresh argv). The counter's parse of the last summary line is not polluted (hand runs show clean stdout).
- t09 guard: `victim.chmod(0o000)` then `os.access(victim, os.R_OK)` → on a readable (root) run it records a skip note through `rec(..., True, ...)` instead of a false failure; this host runs uid 1000, so the real arm fired. The chmod-000 file is restored to 0600 in `finally` before TemporaryDirectory cleanup.

## Fixtures and TMPDIR (PASS)
- All new fixtures live under the base `root` of the existing `tempfile.TemporaryDirectory(prefix="dispatch-selftest-")` (lane_case cases, `_main_case` cases, proof tree, map/manifest writes). No network, no git, no env beyond TMPDIR/HOME. Every transient state is restored in-arm (map_path restored after t03/t11; SKILL.md restored after t04; manifest restored after t05/t10; chmod restored after t09).

## Per-mutant kill attribution (hand-applied in the git-less world, minimal env; receipt `ReviewerArmsR99/hand-mutants.txt`)
Honest (unmutated candidate): rc 0, `0 failure(s) over 154 assertions` (base 128 + 26 new).

| mutant | rc | summary | failing assertions (all `self-test FAIL: `) |
|---|---|---|---|
| t01-l1-suffix-unanchored | 1 | 3/154 | all three r99-t01: `lane_of rejects 'kote-L1.md.bak': got ('kote', None, 'l1')`; `'kote-L1.md.bak' evaluates 0 files: got 1`; `… is out of scope: got []` |
| t02-role-round-above | 1 | 3/154 | r99-t02 both (`filename_role_round_equal: got {'status': 'PASS', …}`; `file FAIL: got {… 'verdict': 'PASS' …}`) + r99-t12's status assertion (cross-talk, also a new arm) |
| t03-proof-map-hash-unenf | 1 | 2/154 | r99-t03 both: `zeroed map text_sha256 refuses the proof: got (0, 'boxes proven 2\\n', '')`; `refusal names the pinned hash: got ''` |
| t04-proof-missing-skill | 1 | 2/154 | r99-t04 both: `deleted SKILL.md refuses the proof: got (0, 'boxes proven 2\\n', 'box-proof: cannot read SKILL.md …')`; `refusal names the live hash: got 'box-proof: cannot read SKILL.md …'` |
| t05-proof-verdict-mismatch | 1 | 2/154 | r99-t05 both: `PASS-labelled duplicate refuses the proof: got (0, 'boxes proven 2\\n', '')`; `refusal names the verdict mismatch: got ''` |
| t06-runchecks-first-only | 1 | 2/154 | r99-t06: `returns both results: got ['dispatch.04']`; `second result is evaluated: got [{…'id': 'dispatch.04'…}]` |
| t07-main-fail-exit-zero | 1 | 2/154 | r99-t07 `main() on a FAILing check exits 1: got (0, 'FAIL dispatch.04: …')` + r99-t08's second call `--check dispatch.08 exits 1: got (0, …)` |
| t08-main-check-ignored | 1 | 2/154 | r99-t08: `--check dispatch.04 exits 0: got (1, 'PASS dispatch.04…FAIL dispatch.08…')`; `prints one result line: got 'PASS dispatch.04…FAIL dispatch.08…'` |
| t09-readtext-oserror-empty | 1 | 1/154 | r99-t09: `an unreadable prompt file raises EnvError: got (None, {…'status': 'N/A', 'evaluated': 1…})` (uid-1000 run; guard took the real arm) |
| t10-verdict-of-prefix | 1 | 2/154 | r99-t10 both: `prefix control-case file refuses the proof: got (0, 'boxes proven 2\\n', '')`; `refusal says not evaluated: got ''` |
| t11-map-duplicate-first | 1 | 1/154 | r99-t11: `good second entry wins…: got (1, 'boxes proven 1\\n', "…map disposition is 'executed:…'…")` |
| t12-finish-fails-nas | 1 | 1/154 | r99-t12: `the mixed FAIL+N/A check reads FAIL: got ('N/A', '2 file(s) evaluated: 0 PASS, 1 FAIL, 1 N/A…')` |
| p00-md-not-stripped (positive) | 1 | 12/154 | existing arms (`control: dispatch.04 verdict PASS`, `report_paths keeps an absolute report path`, t01-rstrip-dot …) + r99 arms incidentally |

Every target kills for the stated reason (each named arm observes exactly the behaviour the mutant disables). Kills are REPORTED failures in the hand run; the counter's blind+mirror reading is recorded below.

## Counter readings on the candidate (61a20f8)
Receipts: `.ufo/waves/round-99/w1/ReviewerArmsR99/cand-*.txt`. All run with `HYAKU_SCRATCH`/`TMPDIR` in my scratch, REPO = my clone.

- `selftest-kills.py c1 61a20f8` (v6): `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12` · `rules v6: honest runs CLEAN 3 of 3; mirror runs reported 13 of 13; seed c1f460fe97274193` · **`C1-PREDICATE-MET`, rc 0** — the frozen target tally.
- `c1 61a20f8 --rules v5`: identical tally; `rules v5: honest runs CLEAN 3 of 3; mirror runs reported 13 of 13; seed a64930f6aecc9943` · **MET, rc 0**.
- `r98c1 61a20f8`: `9 of 9 … R98C1-PREDICATE-MET` rc 0 (seed 07d8be4145de4ed5).
- `r97c1 61a20f8`: `13 of 13 … R97C1-PREDICATE-MET` rc 0 (seed 2432672b6d8e14c6).
- `r96c1 61a20f8` (kill-rule control, extra): `11 of 11 … R96C1-PREDICATE-MET` rc 0.
- `r95c1 61a20f8` (kill-rule control, extra): `3 of 3 … R95C1-PREDICATE-MET` rc 0. All four kill-rule controls (r98c1/r97c1/r96c1/r95c1) still read MET on the candidate.
- `verify_dispatch_prompts.py --box-proof` in the clone: `boxes proven 2`, rc 0 (receipt `cand-box-proof.txt`).
- Direct honest `--self-test` in the clone under `env -i` (PATH/LANG/TMPDIR/HOME/PYTHONDONTWRITEBYTECODE only): `0 failure(s) over 154 assertions`, TMPDIR empty afterwards — no fixture leftovers incl. the chmod-000 file.
- Builder's own receipts (ExecArmsR99/c1-v6.txt, c1-rulesv5.txt, r98c1.txt, r97c1.txt) show the same tallies under different shuffle seeds — independent agreement.
- `ExecArmsR99_READY` appeared with sha256 `9b705bc8…f9af924` = the patch file sha256 I measured before READY existed.

## Findings
1. (non-blocking, observation) Under t02 the r99-t12 assertion fails too (`got ('N/A', '2 file(s) evaluated: 0 PASS, 0 FAIL, 2 N/A…')`): a role-round-above defect flips the t12 fixture's first file, so the mixed check reads N/A. Correct cross-talk between two new arms — each mutant still names its own arm's assertion first; no impact on the kill rule.
2. (non-blocking) The patch is 270 appended lines in one hunk; the honest count goes 128 → 154 assertions (+26). Under the counter all 12 comment decoys and 12 code decoys HOLD, so none of the new assertion text reintroduces an anchor or breaks a decoy compile.
3. No blocking finding against plans/round-99.md § C1, ANTI-SNIFFING, FROZEN ANCHORS, or fixture/TMPDIR hygiene.

## Verdict
- **Blocking findings: none.** The candidate kills t01..t12 and the positive under both v6 and v5 rules (`C1-PREDICATE-MET`, rc 0, run errors 0), each kill attributable to a named r99-tXX assertion observing the exact behaviour the mutant disables; production code outside `self_test()` is byte-identical (one 270-line insertion hunk inside it); all 53 frozen anchors match exactly once; fixtures are TMPDIR-bound and cleaned; the main() arms are argv-explicit and stdout-captured with no cross-arm leak.

## Residual risk / verification gaps
- The hand runs used the counter's own CLAIMS table (anchors/replacements), so mutant construction is not independent of the counter — but the anchors are frozen instrument bytes and the counter's blind+mirror reading is the authoritative kill evidence anyway.
- I did not run the C2 counters or the corpus baseline: those belong to ReviewerRedsR99/SentinelScopeR99 and the landing step. C1↔C2 interaction is none: the patch touches only `self_test()` (the checklist's delegated `--box-proof` stays `boxes proven 2` rc 0 — measured above).
- t09's kill depends on a non-root runner (uid 1000 here); a root-run counter would see the guarded skip note and t09 would not kill — this is the disclosed guard behaviour, not a defect.

## Tooling
- No tools installed or upgraded; no host setting changed; no pacman. Scratch `/fast/scratch/hyaku/kotoba-r99/ReviewerArmsR99` (incl. clones, world, tmpcheck) removed before yield.
