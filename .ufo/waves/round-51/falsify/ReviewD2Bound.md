Verdict: HOLDS-BOUNDED. Every behaviour the D2 bound describes reproduces at HEAD 59903b26, but the bound is miscalibrated: its carried-finding list disagrees across three records and omits F4 and F5, and its word "advertises" hides a false red I reproduced (N2).

Scope: SKILL.md:132-141 (the D2 bound), the "Round-51 qualifier (routed defect D2)" at the end of the SCORECARD operability cell (SCORECARD.md:31), and the round-50 falsify report `.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1-F5. Judged on calibration. Judged bytes: lane HEAD 59903b2637689739a5b9901956301da72d0effe1. `verifiers/verify_skill_checklist.py` sha256 325d22ef...d51eae (lane working copy and HEAD identical). SKILL.md sha256 60786fb4...927a (identical). `git log 956ee1676e4c18480bce8ac3993541462be76e11..HEAD -- verifiers/verify_skill_checklist.py` prints nothing: the verifier is unchanged since the round-50 verdict.

## Findings

**N1 Medium: the carried list is stated three ways, and none names the full open set.** All five F1-F5 are open at HEAD; none is fixed (code evidence in the table).
- SKILL.md:139 says "F1-F3, carried". It omits F4 and F5.
- The qualifier (SCORECARD.md:31, committed) says "The F3-F5 fixes ... are carried". It says nothing about F1 or F2, the fail-open itself.
- `corpus/lessons/round-51.md:112-115` (committed) says D2 is "bounded" and names only F3-F5 as carried.
Fix: one list in all three places, "F1-F5 open at HEAD; the fail-open (F1, F2) is bounded at SKILL.md:135-139".

**N2 Medium: "advertises the flag" is a substring test. A help text that only mentions the flag triggers a red with no reason (new; not in round-50 F1-F5).**
- `verify_skill_checklist.py:971`: `if BOX_PROOF_FLAG in (proc.stdout + proc.stderr)`. Any occurrence of the text `--box-proof` counts as "advertised".
- Reproduced (variant `mention`): help text reads "Use --box-proof ...", but no argument is defined. Gate exit 1: `FAIL checklist.box_map_complete: delegated instrument 'verifiers/probe_mention.py' failed its --box-proof (exit 2)`. The argparse error went to stderr, and the detail drops it (line 1018 reads stdout only).
Fix: SKILL.md:135 should say "its --help text contains the text `--box-proof`", and the bound should name this false red.

**N3 Low-Medium: SKILL.md omits the decode crash (F5) and the dropped reason (F4).**
- F5 reproduced (variant `bytes`): gate exit 1, traceback ending `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0`, no JSON. Only `TimeoutExpired` and `OSError` are caught (lines 967, 969). The file has no catch-all. The qualifier names the crash; SKILL.md does not.
- F4 reproduced through `mention`: the reason is lost. No bound text names F4 except by the range "F1-F3" or "F3-F5".
- The proof run has the same decode exposure (line 1007 `text=True`; no catch at 1009 or 1013). [INFERENCE from code; not run.]

**N4 Low: the status line that says D2 is "carried" exists only in the uncommitted working copy.** The lane working copy of SCORECARD.md has 319 lines; HEAD has 311. Differing hunks (python difflib against HEAD): lines 28 and 32 (round-51 depth and freshness rows; HEAD's freshness row still cites round 48); lines 123-126 (a "Round 51 completed" paragraph and a "Next: round 52" line reading "the checklist gate's fail-open on unprobeable delegates (D2, carried)"); lines 258-259 (two round-51 table rows); lines 271-272 (a round-51 calibration note). HEAD line 122 reads "Next: round 51". The qualifier (line 31) is identical in HEAD and the working copy, so it is landed. The "D2, carried" status is not landed. Who wrote the working-copy edits is unknown.

**N5 Info: two different "four" sets.** The qualifier and the lesson say "the four `MutBoxProofGate` survivors are carried". Those are M3, M7, M11 and M12 (`.ufo/waves/round-50/falsify/MutBoxProofGate.md:33-42`): gaps in the gate's own self-test (help check on stderr, `--map` not passed, detail taken from stderr, cwd). SKILL.md:139-141 names a different four (dispatch-prompt fixture gaps). Neither record names its four, so a reader can merge them.

## Statement check (SKILL.md:132-141 and the qualifier)

| # | Where | Claim | Code at HEAD (verify_skill_checklist.py) | Reproduction (exit codes) | Verdict |
|---|---|---|---|---|---|
| S1 | SKILL.md:135-136 | Gate runs `--box-proof` only when the `--help` probe advertises it | 999-1003 | visible: proof runs (exit 1); hidden: not run (exit 0) | HOLDS; "advertises" is a substring test (N2) |
| S2 | SKILL.md:136-137 | Probe that times out, cannot execute, or does not show the flag is reported PASS "not run" | timeout 967-968; OSError 969-970; no flag 971-973; not runnable 996-998; PASS path 1000-1002, 1334-1336 | timeout (sleep probe): PASS, exit 0; OSError: PASS, exit 0; no flag: PASS, exit 0; not runnable: PASS, exit 0 | HOLDS. The "not runnable" branch (996-998) is a fourth PASS path the bound leaves unnamed |
| S3 | SKILL.md:137-138 | "so the gate fails open there" | n/a | hidden stub's own `--box-proof` exits 1 ("boxes proven 0"); gate PASS, exit 0 | HOLDS |
| S4 | SKILL.md:138-139 | Relative `--map` from another directory gives a false red | `map_path = Path(args.map)` unresolved at 2534; `--map` passed at 1005; child `cwd=str(base)` at 1008 | relative: exit 1 FAIL "(exit 2): boxes proven 0"; absolute: exit 0 PASS "boxes proven 2" | HOLDS |
| S5 | SKILL.md:139 | "(ReviewBoxProofGate.md F1-F3, carried)" | cited file is tracked at HEAD (`git ls-files`, exit 0) | F1-F5 all open (N1) | HOLDS-BOUNDED: list incomplete (N1, N3) |
| S6 | SKILL.md:139-141 | Four named gaps "have no fixture yet" | n/a | not verified (dispatch instrument; outside named scope); keyword grep of `verifiers/fixtures/dispatch-prompts` for the four terms: no matches (weak evidence) | NOT VERIFIED |
| Q1 | qualifier | Same as S1-S3 | as above | as above | HOLDS |
| Q2 | qualifier | Names `supports_box_proof` and `delegated_box_proof` | defined at 960 and 985 | n/a | HOLDS |
| Q3 | qualifier | Non-UTF-8 help output crashes the gate | 966-970 catch only timeout and OSError; 1007 `text=True` | `bytes`: exit 1, traceback, no JSON | HOLDS |
| Q4 | qualifier | "The one live delegate advertises the flag and is green" | n/a | HEAD clone: exit 0, PASS "boxes proven 2"; dispatch `--help` exit 0 | HOLDS |
| Q5 | qualifier | "The F3-F5 fixes and the four MutBoxProofGate survivors are carried" | 2534 and 1018 still unfixed | survivors M3/M7/M11/M12 per MutBoxProofGate.md:33-42 | HOLDS as "not fixed"; incomplete (N1, N5) |

## Reproduction

Setup: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r51/falsify/D2Bound/lane`, then `git -C .../lane checkout -q 59903b26...` (rev-parse prints 59903b2637689739a5b9901956301da72d0effe1). Each variant lives in `.../D2Bound/variants/<name>/`: a copy of SKILL.md, a copy of the HEAD map with the two dispatch dispositions changed to a stub, and the stub. Gate command for every variant: `python3 -B <clone>/verifiers/verify_skill_checklist.py --repo <v> --skill <v>/SKILL.md --map <v>/verifiers/checklist-baseline.json --check checklist.box_map_complete --json`.

| case | target | gate exit | status | detail (verbatim; shortened) |
|---|---|---|---|---|
| live, HEAD map | verify_dispatch_prompts.py | 0 | PASS | "...--box-proof exit 0: boxes proven 2" |
| hidden (flag SUPPRESSed; own proof exit 1) | probe_hidden.py | 0 | PASS | "...no --box-proof support (the --help probe does not advertise --box-proof), not run" |
| visible (control, same stub, flag shown) | probe_visible.py | 1 | FAIL | "delegated instrument 'verifiers/probe_visible.py' failed its --box-proof (exit 1): boxes proven 0" |
| badinterp (`#!/nonexistent/interp`, mode 755) | probe_badinterp | 0 | PASS | "...the --help probe failed ([Errno 2] No such file or directory ...), not run" |
| noexec (shebang, mode 644) | probe_noexec | 0 | PASS | "...not runnable (no interpreter, not executable), not run" |
| sleep (`--help` sleeps 300 s) | probe_sleep.py | 0 | PASS | "...the --help probe timed out), not run" (120 s probe limit) |
| mention (help text only) | probe_mention.py | 1 | FAIL | "delegated instrument 'verifiers/probe_mention.py' failed its --box-proof (exit 2)" |
| bytes (`--help` writes \xff\xfe) | probe_bytes.py | 1 | no JSON | traceback: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0 |
| relative `--map` (live map, run from scratch root) | verify_dispatch_prompts.py | 1 | FAIL | "...failed its --box-proof (exit 2): boxes proven 0" |
| absolute `--map` (same) | verify_dispatch_prompts.py | 0 | PASS | "...--box-proof exit 0: boxes proven 2" |

Hidden stub detail: `--help` exit 0; "--box-proof" present in help: False. Its own `--box-proof` run: exit 1, stdout "boxes proven 0". Visible stub: "--box-proof" present in help: True.

Other commands and exit codes:
- `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete --json` (clone at HEAD): exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --help`: exit 0. `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json`: exit 0, stdout "boxes proven 2".
- `git cat-file -t 956ee1676e4c18480bce8ac3993541462be76e11`: prints commit.
- `git ls-files .ufo/waves/round-50/falsify/ReviewBoxProofGate.md`: prints the path; exit 0.
- `sha256sum` of the verifier and SKILL.md: lane and clone identical (values above).

## Residual risk and verification gaps
- The proof run's 120 s timeout (lines 1009-1012) and its decode exposure (line 1007) were not run. [INFERENCE from code.]
- S6 and the "no fixture yet" wording (SKILL.md:139-141) are not verified beyond a keyword grep, which found no matches.
- The dispatch instrument's "boxes proven 2 only when ..." (SKILL.md:132-134) was checked only by the live run.
- The uncommitted SCORECARD rows (N4) are not judged as landed. Other seats may cover them.
- F6 (self-test arms) and the round-50 self-test count were not re-measured.

## Recommended repairs (not applied)
1. SKILL.md:135: replace "advertises the flag" with "its --help text contains `--box-proof`". Name the mention false red.
2. SKILL.md:139 and the qualifier: give one carried list, F1-F5, open at HEAD. Name M3, M7, M11 and M12 separately from the four fixture gaps.
3. Lesson D2: say the fail-open (F1, F2) is open and carried, and bounded at SKILL.md:132-141.
4. Commit the SCORECARD working-copy rows, or revert them, so HEAD carries the D2 status.

## Writes and tools
- Lane: this report is the only file written. Read-only git commands were run in the lane: `rev-parse HEAD`, `log --oneline -3`, `status --porcelain` (twice), `diff --stat -- SCORECARD.md`, `diff -- SCORECARD.md`. `git status` may refresh the index stat cache; no content changed. The lane is jj-colocated, so its git index is stale; every HEAD comparison used the clone or python file reads.
- Scratch: `/fast/scratch/hyaku/kotoba-r51/falsify/D2Bound/` (lane clone at 59903b26; `variants/`).
- Tools: none installed or updated. Present: python3, git, sha256sum.
