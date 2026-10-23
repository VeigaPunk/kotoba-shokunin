# CriticHollowC2 — frozen C2 dishonest-record attack

Date: 2026-10-23. Seat: `kotoba-r61-wave-CriticHollowC2`. Assigned axis: **calibration**. Collateral affected axis: **operability** (empty-input crash). This is an attack report, not an admission, round verdict, integration, or saturation decision.

## Finding

**All three requested cheap cheats work at the frozen checker's blob-reading boundary:** cosmetic LOG material, body-empty census receipts ending `exit=0`, and self-asserted ancestry. A combined world appending cosmetic/inverted text to the *real committed base* and supplying hollow receipts prints `routed repairs verified 6 of 6`; public `main()` returns 0. Fifteen dishonest variants returned 0 across the two probes below. Two negative controls returned 1; two genuinely empty/whitespace census inputs raised `IndexError` rather than returning a verdict.

The particularly strong ancestry counterexample is not merely a fabricated exit: the real read-only command `git merge-base --is-ancestor BASE BASE` returns 0, and a receipt of that truthful but reflexive relation satisfies R-f. BASE is not thereby a distinct control-receipts commit preceding a C1 data commit.

The counter itself already discloses its boundary (`verifiers/check_routed_repairs.py:34-37`): committed blobs, not substantive honesty. The defect is treating its six lexical presences as sufficient evidence of the six substantive repairs. This report supplies falsifications and guards; it does not replace the canonical judgment.

## Authority, provenance, and bounds

Read first: `plans/round-61.md`, especially C2 at lines 61–74. Then read the committed checker, C2 base receipt, r60 closure §7–§8, and the specified r60 controls/key-form ground. Relevant fixed evidence:

- Frozen checker commit: `7827628a939b0333c89892dfcedc72e390ccfb60`.
- Tested checker SHA-256: `61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356`.
- Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`.
- `.ufo/waves/round-61/controls/C2-base.txt:1-8` records six missing repairs, `routed repairs verified 0 of 6`, `base-exit=1`. **Read, not rerun here.**
- `corpus/lessons/round-60-verifier-spotcheck.md:114-143` states the actual routed causes: landed-scope omissions, the wrong base pointer, 32 claimed versus 29 committed seat reports, missing standalone after-census, shaped quotes called byte-exact, and pre-data controls.
- `.ufo/waves/round-60/receipts/freeze2-selftest.txt:7-10` is the base measurement: `--rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af`, exit 1, snapshots 0 of 0.
- `.ufo/waves/round-60/C1-measure.txt:3-13` instead measures `7b80ae80cda69a95b6fc90879395113a99a57912`; its live run exits 0, 4 of 4. The latter file is at the round-60 root, **not** inside `receipts/`.
- `.ufo/waves/round-60/controls/SUMMARY.md:14-22` discloses the cancelled wrong-key/invented-action seats without pre-data receipts. `.ufo/waves/round-60/controls-v2/SUMMARY.md:12-20` discloses two real-input provenance shortcuts meeting v2. These are reasons not to substitute asserted provenance for checked provenance.
- Existing `corpus/QUALITY.md` Q25–Q26, Q28, Q31, Q36 and Q50 distinguish a census observable from claim evidence, freeze the declared instrument, limit credited coverage to what it reads, and require revision-bound receipts.

**Measurement boundary:** no dishonest Git tree or commit was constructed. No Git/JJ mutation, lane/fleet/sibling edit, index write, `.ufo/state` write, scratch file, fetch, census, or judge invocation was performed. Only this report is written. The probes load the checker from its immutable Git object, verify its SHA, and drive its unchanged public `main()` while replacing only `git_show` with an exact path-to-blob fixture loader. All five blob reads and the normal printed verdict/return value are exercised. This is stronger than helper-only scoring, but **is not a claimed `--rev <dishonest-commit>` CLI run**. `main-return` is a function return; `probe-process-exit` is the actual Python process exit.

[INFERENCE] Committing the same ASCII blobs would produce the same result under the frozen CLI: its measurement path reads exactly those five blobs, and R-f performs no graph/object verification. That inference is not relabelled as an observed committed-world exit. A real dishonest-tree trial remains unrun under the no-Git-mutation bound. No claim is made here that C1, the landed C2 repair tree, self-tests, or no-harm checks have passed.

## Combined counterfeit fixture, exact target content

These are **counterexample data, not edits to apply**. The probe starts with committed BASE `LOG.md`/`corpus/QUALITY.md`, preserving their prior bytes, then appends the two blocks below. The other three paths receive the complete displayed bodies. In particular, there is no census execution and no ancestry execution in the combined hollow world.

Append to target `LOG.md`:

```markdown

## Unrepaired record: keyword examples only
The original report remains uncorrected.
build reports
claimed 32
committed 29
.ufo/waves/round-60/build
An unrelated old-round note mentions plans/round-60.md and considerthese/2026-10-23.md.
Retain C1-measure.txt as the r60 base pointer; do not use receipts/freeze2-selftest.txt.
```

Append to target `corpus/QUALITY.md`:

```markdown

Q56: byte-exact may describe whitespace-normalized equality.
```

Full target `corpus/lessons/round-61.md`:

```markdown
M91
```

Full target `.ufo/waves/round-61/census-after.txt`:

```text
exit=0
```

Full target `.ufo/waves/round-61/receipts/controls-ancestry.txt`:

```text
merge-base --is-ancestor
exit 0
```

Observed `H0-hollow-append-on-real-base`: all six repairs `ok`, `routed repairs verified 6 of 6`, `main-return=0`. The full pasted output is below.

## Filed bypasses and smallest safe guards

Every accepted case in this table printed `routed repairs verified 6 of 6` and returned 0 in the pinned public-main probe. These are not claimed rejections.

| ID / observed case | Counterexample and local cause | Smallest safe guard |
|---|---|---|
| H0 | All six hollow repairs together, appending to real BASE LOG/QUALITY. None of the underlying executions occurs. | Keep the frozen score as the lexical observable it actually is; require substantive, revision-bound guard evidence for **each of the same six repairs** before describing them as verified. Presence-only relabelling does not complete the specified repair work. |
| Ha — `Ha-split-negated-LOG-no-count-command` | R-a's four markers are on separate negated/unrelated lines; no counting command. Code at 69–74 searches the whole LOG although its own docstring promises one line at 20–22. | A scoped affirmative correction plus the actual counting command/output over the explicit committed **seat-report** population; a must-fail split-line/no-command control. Same-line matching alone would only fix the row-locality defect, not honesty. |
| Hb — `Hb-wrong-round-scope-mentions` | The two filenames occur only in an unrelated `## Round 1` hypothetical note. R-b reads neither the round-61 landed-scope section nor its relationship to the omitted report scope. | Review the current round's explicit landed-scope correction and the actual affected file list. Global historical mentions cannot discharge this route. |
| Hc — `Hc-reversed-base-pointer` | LOG explicitly keeps `C1-measure.txt` as the base and says **not** to use `receipts/freeze2-selftest.txt`. R-c accepts both names on one line regardless of direction. | Require the affirmative disambiguation and reopen the two existing receipts at their exact paths/revisions. The inverted statement must change the guard's exit. |
| Hd1 — `Hd-exit-tail-only` | The census file consists solely of `exit=0`. R-d checks only its last nonblank line (86–93). | Commit an actual after-run transcript naming command, measured revision, time and observed output/status; bind it to the instrument and input revision. A reviewer/independent replay must distinguish the empty receipt. |
| Hd2 — `Hd-failed-census-laundered-tail` | Body says census failed / wrong revision and contains `exit=1`; adding final `exit=0` makes R-d `ok`. | Bind a command's observed output and exit to that one invocation rather than any terminal success marker. Reject contradictory/unbound status claims. |
| He1 — `He-opposite-rule-orphan-M91` | Q56 expressly allows whitespace-normalized text to be called byte-exact; the lesson is only `M91`, with no `## Mistakes`, evidence, captured-by or fix. Both get credit. | Check the exact Q56 criterion row's actual restriction, plus an exact M91 mistake row carrying the required causal lesson and evidence. Assign semantic review explicitly; the opposite rule must fail its guard. |
| He2 — `He-different-identities-Q560-M910` | Entire criterion/lesson identifiers are `Q560` and `M910`, not Q56/M91. Substring containment at 97–100 changes identity. | Parse exact identifier cells/word boundaries, then validate their contents; add this must-fail identity arm. |
| Hf1 — `Hf-no-command-operands` | Ancestry has only the two required marker strings; no `git`, operands or objects. R-f never runs Git. | Resolve full control/data commit IDs, require distinct commits, verify their roles/contents, and independently execute the claimed relation. |
| Hf2 — `Hf-expected-success-actual-failure` | Receipt says `expected exit 0; actual exit 1`; substring `exit 0` wins. | Parse the **observed** exit belonging to the ancestry invocation, not an expected-code phrase. |
| Hf3 — `Hf-true-but-reflexive-base-ancestry` | The actual `git merge-base --is-ancestor BASE BASE` exits 0. Reusing that truthful receipt earns R-f although no strict control→data ordering is established. | Require distinct, correctly identified commits; prove controls are in CTL and the relevant C1 data is not already there, then verify CTL strictly precedes DATA. Mere non-strict ancestry is insufficient. |
| D1 — `D1-exit-belongs-to-other-command` | A real `git rev-parse --verify FREEZE` output/exit 0 is followed by `TODO: run merge-base --is-ancestor … (not yet done)`. R-f still passes. | Tie result/exit/operands to the same complete executed command; independently check that invocation, not a different successful one. |
| D2 — `D2-numeric-nearmiss-path-retained` | `claimed 320` and `committed 2990` contain the two frozen number strings. With the build path retained, R-a passes. | Parse exact integer values in the actual correction; compare them with an explicit report-population count, not substring hits. |
| D3 — `D3-before-receipt-reused-as-after` | The committed pre-round `census-before.txt` bytes are supplied as the after file without running a census; R-d accepts them. | Require after-invocation provenance bound to the revision. **Do not require before/after bytes to differ**: an honest repeated census can be identical. Equality alone is not evidence of staleness. |
| D5 — `D5-build-path-prefix-only` | The counting path can be changed to `.ufo/waves/round-60/build-not-the-report-directory`; its prefix still satisfies R-a. | Validate the exact counting target/path, not a prefix string, and bind it to the counting command and report population. |

### Guards that must not create a new calibration error

1. **M90 chronology is not commit ancestry alone.** Even a genuine strict ancestor relation can be arranged after data seats have already probed; it proves committed ordering, not completion-before-dispatch. Read the relevant receipt contents and the recorded dispatch/measurement chronology. I did not inspect or infer the live round-61 dispatch order, and make no claim that it violated M90. Do not close that stronger route solely from an ancestry receipt.
2. **The 29 denominator is seat reports, not all directory entries.** The r60 build directory also contains `check_word_counts.fixture.md`, `check_word_counts.py`, `ExecIndexCorpus.patch`, and `swarm-registry.json`. The frozen self-test's example `ls .ufo/waves/round-60/build | wc -l` does not define the intended report population. An all-files or all-markdown count is a different observable, not a refutation or replacement of the closure's 29 seat reports. Define the roster/exclusions explicitly rather than quietly changing the denominator.
3. **Identical census findings are allowed.** An inequality check would trade a cheap false positive for a false rejection of honest stable output. Likewise, do not require exactly the currently observed 13 W04 findings forever. Bind the real after invocation to its revision and preserve its actual findings.
4. **Frozen means frozen.** Q28 forbids replacing this counter's declared result by an in-wave hardened rewrite. Land any counter repair as a separately identified second measurement with its own source hash, controls and results. The smallest current-round correction is authentic repairs plus explicit independent guards/limits, not silently crediting a new instrument as the old one.

### Negative controls and malformed-input defect

- `Nd-explicit-failed-census`: replacing only census content with `exit=1` printed R-d `missing`, `routed repairs verified 5 of 6`, `main-return=1`.
- `Nf-no-ancestry-marker`: ancestry content `exit 0` alone printed R-f `missing`, `routed repairs verified 5 of 6`, `main-return=1`.
- `Xd-empty-census` (`""`) and `Xd-whitespace-census` (`"\n \t\n"`) each raised `IndexError: list index out of range`; no normal verdict was printed, and public `main()` did not return. This is not an acceptance bypass. The expression at line 89 indexes the filtered list without checking it has a last line. Smallest safe correction in a separately identified repair: treat an empty filtered list as missing/failed before indexing, with both cases in the self-test. Do not convert that exception into a synthetic success receipt.

The counterfeit acceptance is a fixable evidence/guard defect, not a defensible calibration/operability tradeoff. Merely adding cosmetic records cannot support the stated calibration improvement; conversely, banning equal census output would harm honest inputs. This seat does not issue a judge verdict.

## Cross-check with ExecC2Audit

Peer: `kotoba-r61-wave-ExecC2Audit`; announced report target `.ufo/waves/round-61/wave/ExecC2Audit.md`. Its messages are comparison data, **not substituted for this report's measurements**; no scratch file or scratch commit is cited as evidence here.

- **Independent overlap:** combined cosmetic world; R-a split/negated markers without a command; reversed R-c pointer; exit-tail-only R-d; inverse/out-of-row byte-exact rule and Q560/M910 identity substitutions; unproved ancestry markers. My cases above provide my own source-pinned observations.
- **Initially peer-only, then independently measured here:** D1 wrong-command exit ownership; D2 numeric near misses with the required path restored; D3 before-receipt copy. All three returned 0 in my second probe. The peer explicitly corrected its earlier D2 5/6 observation: it had inadvertently omitted the required path, so that run was not evidence that numeric near misses were rejected. My corrected-path probe closes that gap.
- **This seat's additions:** wrong-round R-b scope, a failed census body laundered by a final success tail, expected-vs-actual ancestry failure, actual reflexive BASE→BASE ancestry, exact-path-prefix D5, and empty/whitespace census crashes. These widen the bypass/input-class list beyond the initial peer list rather than being treated as agreement by default.
- **Peer-reported but not remeasured here:** ancestry receipts using hashes that do not identify objects. My no-operands and truthful-reflexive cases independently expose the same missing object/role verification boundary; the peer's specific `cat-file` outputs are not claimed as mine.
- **Interpretation corrections sent back:** copied census bytes alone do not demonstrate stale execution, so no inequality guard; all-files/all-markdown directory counts are not the seat-report count. The local directory listing establishes the existence of non-report artifacts, without rerunning or altering the frozen closure count.

## Reproduction and measurements

Both commands actually executed were argv `['python3', '-B', '-c', CODE]`, with cwd `/home/vgpnk/Projects/shokunin`, captured stdout/stderr, and the exact CODE shown below. No script file was written. `git show` reads only the fixed checker object and the listed committed inputs; `-B` prevents bytecode-file writes. The test loader is deliberately disclosed and is **not** a replacement judgment table. Assertions check the immutable counter hash and that each observed outcome matches the stated attack observation.

### Probe 1 — exact inline CODE

```python
import contextlib
import hashlib
import io
import subprocess
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FREEZE = "7827628a939b0333c89892dfcedc72e390ccfb60"
BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
PIN = "61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356"

print("date -u: " + subprocess.check_output(["date", "-u"], text=True).strip())
source = subprocess.check_output(["git", "-C", str(LANE), "show", FREEZE + ":verifiers/check_routed_repairs.py"])
print("counter-commit=" + FREEZE)
print("counter-sha256=" + hashlib.sha256(source).hexdigest())
assert hashlib.sha256(source).hexdigest() == PIN
ns = {"__file__": str(LANE / "verifiers/check_routed_repairs.py"), "__name__": "frozen_c2_attack"}
exec(compile(source, ns["__file__"], "exec"), ns)
read_committed = ns["git_show"]
base_log = read_committed(BASE, "LOG.md")
base_quality = read_committed(BASE, "corpus/QUALITY.md")
assert base_log is not None and base_quality is not None
CENSUS = ".ufo/waves/round-61/census-after.txt"
ANCESTRY = ".ufo/waves/round-61/receipts/controls-ancestry.txt"
LESSON = "corpus/lessons/round-61.md"
full_log = (
    "round-60 build reports claimed 32 committed 29 (`ls .ufo/waves/round-60/build | wc -l`)\n"
    "landed scope names plans/round-60.md and considerthese/2026-10-23.md\n"
    "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
)
full = {
    "LOG.md": full_log,
    "corpus/QUALITY.md": "Q56: byte-exact reserved for literal equality\n",
    LESSON: "## Mistakes\nM91: overstatement class\n",
    CENSUS: "kotoba ok\nexit=0\n",
    ANCESTRY: "$ git merge-base --is-ancestor $CTL $DATA\nexit 0\n",
}
hollow_log = (
    "\n## Unrepaired record: keyword examples only\n"
    "The original report remains uncorrected.\n"
    "build reports\nclaimed 32\ncommitted 29\n.ufo/waves/round-60/build\n"
    "An unrelated old-round note mentions plans/round-60.md and considerthese/2026-10-23.md.\n"
    "Retain C1-measure.txt as the r60 base pointer; do not use receipts/freeze2-selftest.txt.\n"
)
hollow = {
    "LOG.md": base_log + hollow_log,
    "corpus/QUALITY.md": base_quality + "\nQ56: byte-exact may describe whitespace-normalized equality.\n",
    LESSON: "M91\n",
    CENSUS: "exit=0\n",
    ANCESTRY: "merge-base --is-ancestor\nexit 0\n",
}
print("transport=fixture blob loader; frozen main/check_repairs/output unchanged; no Git tree written")
failures = 0

def run_case(name, blobs, want_exit, want_line=None, want_exception=None):
    global failures
    seen = []
    def load_fixture(rev, path):
        assert rev == "fixture:" + name
        seen.append(path)
        return blobs.get(path)
    ns["git_show"] = load_fixture
    out = io.StringIO()
    error = None
    result = None
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            result = ns["main"](["--rev", "fixture:" + name])
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
    finally:
        ns["git_show"] = read_committed
    print("\nCASE " + name)
    print(out.getvalue(), end="")
    if error:
        print("exception=" + error)
    print("main-return=" + str(result))
    print("blob-reads=" + str(len(seen)))
    ok = error.startswith(want_exception) if want_exception else (error is None and result == want_exit and (want_line is None or want_line in out.getvalue()))
    print("attack-observation=" + ("matched" if ok else "MISMATCH"))
    failures += not ok

run_case("H0-hollow-append-on-real-base", hollow, 0, "routed repairs verified 6 of 6")
ra_split = (
    "NOT REPAIRED: build reports\nNOT REPAIRED: claimed 32\nNOT REPAIRED: committed 29\n"
    "an example path only: .ufo/waves/round-60/build\n"
    "names only: plans/round-60.md considerthese/2026-10-23.md\n"
    "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
)
run_case("Ha-split-negated-LOG-no-count-command", {**full, "LOG.md": ra_split}, 0, "routed repairs verified 6 of 6")
rb_old = full_log.splitlines()[0] + "\n## Round 1: hypothetical paths only\nplans/round-60.md considerthese/2026-10-23.md\n" + full_log.splitlines()[2] + "\n"
run_case("Hb-wrong-round-scope-mentions", {**full, "LOG.md": rb_old}, 0, "routed repairs verified 6 of 6")
rc_inverse = "\n".join(full_log.splitlines()[:2]) + "\nRetain C1-measure.txt as the r60 base pointer; do not use receipts/freeze2-selftest.txt.\n"
run_case("Hc-reversed-base-pointer", {**full, "LOG.md": rc_inverse}, 0, "routed repairs verified 6 of 6")
run_case("Hd-exit-tail-only", {**full, CENSUS: "exit=0\n"}, 0, "routed repairs verified 6 of 6")
run_case("Hd-failed-census-laundered-tail", {**full, CENSUS: "census failed; not run against the claimed revision\nexit=1\nexit=0\n"}, 0, "routed repairs verified 6 of 6")
run_case("He-opposite-rule-orphan-M91", {**full, "corpus/QUALITY.md": "Q56: byte-exact may describe whitespace-normalized equality.\n", LESSON: "M91\n"}, 0, "routed repairs verified 6 of 6")
run_case("He-different-identities-Q560-M910", {**full, "corpus/QUALITY.md": "Q560: byte-exact\n", LESSON: "M910\n"}, 0, "routed repairs verified 6 of 6")
run_case("Hf-no-command-operands", {**full, ANCESTRY: "merge-base --is-ancestor\nexit 0\n"}, 0, "routed repairs verified 6 of 6")
run_case("Hf-expected-success-actual-failure", {**full, ANCESTRY: "merge-base --is-ancestor\nexpected exit 0; actual exit 1\n"}, 0, "routed repairs verified 6 of 6")
argv = ["git", "-C", str(LANE), "merge-base", "--is-ancestor", BASE, BASE]
ancestry = subprocess.run(argv, capture_output=True, text=True)
print("\nSELF-ANCESTRY COMMAND " + " ".join(argv))
print(ancestry.stdout + ancestry.stderr if ancestry.stdout or ancestry.stderr else "(no stdout/stderr)")
print("exit=" + str(ancestry.returncode))
same_receipt = "$ git merge-base --is-ancestor " + BASE + " " + BASE + "\nexit " + str(ancestry.returncode) + "\n"
run_case("Hf-true-but-reflexive-base-ancestry", {**full, ANCESTRY: same_receipt}, 0, "routed repairs verified 6 of 6")
run_case("Nd-explicit-failed-census", {**full, CENSUS: "exit=1\n"}, 1, "routed repairs verified 5 of 6")
run_case("Nf-no-ancestry-marker", {**full, ANCESTRY: "exit 0\n"}, 1, "routed repairs verified 5 of 6")
run_case("Xd-empty-census", {**full, CENSUS: ""}, None, want_exception="IndexError:")
run_case("Xd-whitespace-census", {**full, CENSUS: "\n \t\n"}, None, want_exception="IndexError:")
print("\nprobe mismatches=" + str(failures))
print("date -u: " + subprocess.check_output(["date", "-u"], text=True).strip())
raise SystemExit(1 if failures else 0)

```

Pasted stdout (includes the actual `date -u` outputs and the real reflexive-ancestry command's status):

```text
date -u: Fri Oct 23 07:12:44 PM UTC 2026
counter-commit=7827628a939b0333c89892dfcedc72e390ccfb60
counter-sha256=61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356
transport=fixture blob loader; frozen main/check_repairs/output unchanged; no Git tree written

CASE H0-hollow-append-on-real-base
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Ha-split-negated-LOG-no-count-command
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hb-wrong-round-scope-mentions
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hc-reversed-base-pointer
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hd-exit-tail-only
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hd-failed-census-laundered-tail
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE He-opposite-rule-orphan-M91
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE He-different-identities-Q560-M910
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hf-no-command-operands
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Hf-expected-success-actual-failure
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

SELF-ANCESTRY COMMAND git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin merge-base --is-ancestor f3246d1493b60ea1c0d947a19c39f9e08e92f326 f3246d1493b60ea1c0d947a19c39f9e08e92f326
(no stdout/stderr)
exit=0

CASE Hf-true-but-reflexive-base-ancestry
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE Nd-explicit-failed-census
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: missing
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 5 of 6
main-return=1
blob-reads=5
attack-observation=matched

CASE Nf-no-ancestry-marker
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: missing
routed repairs verified 5 of 6
main-return=1
blob-reads=5
attack-observation=matched

CASE Xd-empty-census
exception=IndexError: list index out of range
main-return=None
blob-reads=5
attack-observation=matched

CASE Xd-whitespace-census
exception=IndexError: list index out of range
main-return=None
blob-reads=5
attack-observation=matched

probe mismatches=0
date -u: Fri Oct 23 07:12:44 PM UTC 2026

```

stderr: empty. Actual probe process exit: 0. Normal `main()` returns and caught exceptions are separately labelled in the pasted output; a process exit 0 here means the attack observations matched, not that repairs occurred.

### Probe 2 — exact inline CODE

This probe shares the same setup and `run_case` definition, but executes only the four new cases; none of probe 1's cases is rerun.

```python
import contextlib
import hashlib
import io
import subprocess
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FREEZE = "7827628a939b0333c89892dfcedc72e390ccfb60"
BASE = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
PIN = "61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356"

print("date -u: " + subprocess.check_output(["date", "-u"], text=True).strip())
source = subprocess.check_output(["git", "-C", str(LANE), "show", FREEZE + ":verifiers/check_routed_repairs.py"])
print("counter-commit=" + FREEZE)
print("counter-sha256=" + hashlib.sha256(source).hexdigest())
assert hashlib.sha256(source).hexdigest() == PIN
ns = {"__file__": str(LANE / "verifiers/check_routed_repairs.py"), "__name__": "frozen_c2_attack"}
exec(compile(source, ns["__file__"], "exec"), ns)
read_committed = ns["git_show"]
base_log = read_committed(BASE, "LOG.md")
base_quality = read_committed(BASE, "corpus/QUALITY.md")
assert base_log is not None and base_quality is not None
CENSUS = ".ufo/waves/round-61/census-after.txt"
ANCESTRY = ".ufo/waves/round-61/receipts/controls-ancestry.txt"
LESSON = "corpus/lessons/round-61.md"
full_log = (
    "round-60 build reports claimed 32 committed 29 (`ls .ufo/waves/round-60/build | wc -l`)\n"
    "landed scope names plans/round-60.md and considerthese/2026-10-23.md\n"
    "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
)
full = {
    "LOG.md": full_log,
    "corpus/QUALITY.md": "Q56: byte-exact reserved for literal equality\n",
    LESSON: "## Mistakes\nM91: overstatement class\n",
    CENSUS: "kotoba ok\nexit=0\n",
    ANCESTRY: "$ git merge-base --is-ancestor $CTL $DATA\nexit 0\n",
}
hollow_log = (
    "\n## Unrepaired record: keyword examples only\n"
    "The original report remains uncorrected.\n"
    "build reports\nclaimed 32\ncommitted 29\n.ufo/waves/round-60/build\n"
    "An unrelated old-round note mentions plans/round-60.md and considerthese/2026-10-23.md.\n"
    "Retain C1-measure.txt as the r60 base pointer; do not use receipts/freeze2-selftest.txt.\n"
)
hollow = {
    "LOG.md": base_log + hollow_log,
    "corpus/QUALITY.md": base_quality + "\nQ56: byte-exact may describe whitespace-normalized equality.\n",
    LESSON: "M91\n",
    CENSUS: "exit=0\n",
    ANCESTRY: "merge-base --is-ancestor\nexit 0\n",
}
print("transport=fixture blob loader; frozen main/check_repairs/output unchanged; no Git tree written")
failures = 0

def run_case(name, blobs, want_exit, want_line=None, want_exception=None):
    global failures
    seen = []
    def load_fixture(rev, path):
        assert rev == "fixture:" + name
        seen.append(path)
        return blobs.get(path)
    ns["git_show"] = load_fixture
    out = io.StringIO()
    error = None
    result = None
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            result = ns["main"](["--rev", "fixture:" + name])
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
    finally:
        ns["git_show"] = read_committed
    print("\nCASE " + name)
    print(out.getvalue(), end="")
    if error:
        print("exception=" + error)
    print("main-return=" + str(result))
    print("blob-reads=" + str(len(seen)))
    ok = error.startswith(want_exception) if want_exception else (error is None and result == want_exit and (want_line is None or want_line in out.getvalue()))
    print("attack-observation=" + ("matched" if ok else "MISMATCH"))
    failures += not ok


other_argv = ["git", "-C", str(LANE), "rev-parse", "--verify", FREEZE]
other = subprocess.run(other_argv, capture_output=True, text=True)
print("OTHER-COMMAND " + " ".join(other_argv))
print(other.stdout + other.stderr, end="")
print("exit=" + str(other.returncode))
wrong_exit_owner = "$ git rev-parse --verify " + FREEZE + "\n" + other.stdout + "exit " + str(other.returncode) + "\nTODO: run merge-base --is-ancestor $CTL $DATA (not yet done)\n"
run_case("D1-exit-belongs-to-other-command", {**full, ANCESTRY: wrong_exit_owner}, 0, "routed repairs verified 6 of 6")
numeric_nearmiss = full_log.replace("claimed 32 committed 29", "claimed 320 committed 2990")
run_case("D2-numeric-nearmiss-path-retained", {**full, "LOG.md": numeric_nearmiss}, 0, "routed repairs verified 6 of 6")
census_before = read_committed(FREEZE, ".ufo/waves/round-61/census-before.txt")
assert census_before is not None
print("copied-census-before-sha256=" + hashlib.sha256(census_before.encode()).hexdigest())
run_case("D3-before-receipt-reused-as-after", {**full, CENSUS: census_before}, 0, "routed repairs verified 6 of 6")
wrong_path = full_log.replace(".ufo/waves/round-60/build", ".ufo/waves/round-60/build-not-the-report-directory")
run_case("D5-build-path-prefix-only", {**full, "LOG.md": wrong_path}, 0, "routed repairs verified 6 of 6")
print("\nprobe mismatches=" + str(failures))
print("date -u: " + subprocess.check_output(["date", "-u"], text=True).strip())
raise SystemExit(1 if failures else 0)

```

Pasted stdout:

```text
date -u: Fri Oct 23 07:15:53 PM UTC 2026
counter-commit=7827628a939b0333c89892dfcedc72e390ccfb60
counter-sha256=61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356
transport=fixture blob loader; frozen main/check_repairs/output unchanged; no Git tree written
OTHER-COMMAND git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse --verify 7827628a939b0333c89892dfcedc72e390ccfb60
7827628a939b0333c89892dfcedc72e390ccfb60
exit=0

CASE D1-exit-belongs-to-other-command
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE D2-numeric-nearmiss-path-retained
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched
copied-census-before-sha256=583547f6f66f7e051a9ee0f2d0a8d2357939f046a3a2b581c1b3d98f32439a9a

CASE D3-before-receipt-reused-as-after
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

CASE D5-build-path-prefix-only
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after file: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
main-return=0
blob-reads=5
attack-observation=matched

probe mismatches=0
date -u: Fri Oct 23 07:15:53 PM UTC 2026

```

stderr: empty. Actual probe process exit: 0.

### Honest non-results

No real dishonest committed-tree CLI trial, tip C2 measurement, C1 fetch, real after-census, counter self-test, build, lint, formatter, or no-harm suite was run by this seat. The existing base control was read rather than reconfirmed. The only real Git relation executed in the primary probe is the deliberately reflexive ancestry command printed above; the follow-up also runs the printed read-only revision-resolution command. Remaining claims must be judged on authentic landed receipts, not extrapolated from these fixture returns.

Installs: no installs.
Blockers: none.
Attacked: frozen C2 calibration's cosmetic records, hollow/reused census receipts, identifier/path/number near misses, and self-asserted or misbound control ancestry.
