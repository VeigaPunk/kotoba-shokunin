# CriticC1Hollow — C1 hollow instruments and no-op successor

Date: 2026-10-23. Seat: `KotobaR62.CriticC1Hollow`. Assigned axis: **depth**. Impacted collateral axes: consistency/calibration (honest measurement), provenance, operability. This is an assigned critic review, not a canonical judgment, admission, integration, or shipping decision.

## Counterexample and finding

**All four requested hollows, plus a stronger payload-fingerprint H3 variant, printed the exact frozen C1 headline and two survivor records and exited 0.** Two are stronger than mere label printers:

- **H2 (reject direction only)** also satisfies the seeded reject/accept controls, all five benign checks, every value-only isolation vector, and the fresh-equivalence verdict checks. It runs the frozen oracle only in the pristine state, then fabricates `[]` for the disabled target guard. The intended second seeded control does **not**, by itself, catch this hollow.
- **H3/H3b (published catalogue)** satisfy both seeded controls, all five benign checks, and every value-only isolation vector without evaluating any guard. H3b fingerprints payloads, not IDs: renaming every instance still gives **15/15**, while measurement-time equivalent input bytes expose it (**7/15**).

The measured, independent observation guard exits **1** on every hollow and **0** on its real-oracle control. Its distinguishing requirement is **actual requested baseline/mutation invocations and exact returned-reason flow**, supplemented by Q47 input equivalents generated after the candidate is fixed. The report includes the complete runnable laboratory and guard; these are review reproductions, not a new scoring authority.

**The no-op successor attack also succeeds at the printed-label surface.** A full copy retaining the frozen `action_conjunct` prints `E2f fresh instances reject 2 of 2` and returns 0 from its added arm. On the exact pair now proposed in `ExecInstancesA2.md`, the unchanged function actually rejects **1 of 2**. On this review's two independently constructed G7-sensitive event cases it rejects **0 of 2**. The copied action function's AST is identical to the frozen original. The added label therefore cannot be accepted as the source of the count.

These are fixable instrumentation/authentication defects, not a reason to weaken the benign side, alter the immutable r61 oracle, implement G9 contrary to the declared bound, or credit depth from a green string. If the implementation retains only published equivalents, Q47's existing distinction applies: it is a record, not a supported mutation-kill claim. This seat does not make the canonical Rust judge's decision.

## Scope and evidence honesty

- Read `plans/round-62.md` first, then `skill://godspeed` and `/home/vgpnk/.omp/agent/RULES.md`.
- The authoritative contract is `plans/round-62.md:26-99,154-168,223-233`. Draft reports are data, not amendments to it.
- Read-only lane/fleet except this assigned report. Scratch writes stayed under `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/`. No peer file, lane product, fleet file, state file, Git/JJ index, or counter was changed. No Git/JJ command, network request, subagent dispatch, install, or alternate orchestration/judging runtime was invoked. Python runs were the expressly requested bounded experiments (one runner and at most one child; every shell deadline 120 s or less). Nothing was killed.
- The audited file was imported with `python3 -B`; its observed SHA256 was `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`. This is a **helper-bytes** binding, not a claimed measurement of the lane tip.
- The matrix battery here is independently constructed attack/control data, **not the final ten round instances and not C1 round data**. Its 4/5, surviving-2 aggregate demonstrates a counterfeit can hit the frozen headline; it does not resolve the plan's inconsistent 2-versus-1 expectation.
- At the lane verifier-directory inspection, `check_erratum_absorption.py` and `check_scoped_rules_v31.py` were not present. I therefore exercised the plan's intended controls with a transparent scratch driver; I did **not** run or certify either final implementation's self-test. The helper adapter is not a substitute for the final public `main(["--self-test"])` path.
- Scratch is untrusted. Scratch paths below are exact reproduction locations, **not cited lane evidence or committed receipts**. The full sources, fixtures and observed command transcripts are embedded in this report so the report is self-contained.
- The copied counter's full world/eligible self-test was **not run**: its `self_test()` creates Git repositories (`check_scoped_rules.py:1597-1605`), whereas this assignment forbids Git/JJ mutation. No claim that this no-op was measured at `worlds reject 7 of 7; eligible rows pass 4 of 4` is made. The isolated added E2f arm and the actual A2 calls were run.

## 1. Which intended arm catches each hollow?

Final experiment UTC: **2026-10-23 20:57:32Z**. Each bare instrument command used `--self-test` and exited **0**, printing the frozen headline plus the two expected-looking survivor records. The observation-guard command for each exited **1**.

| Instrument | Seeded controls | Benign | Value-only isolation | Actual requested calls / exact reason flow | Fresh equivalent verdicts | Catch / missing guard |
|---|---:|---:|---|---:|---:|---|
| H1 constants | 1/2 | 0/5 | fails | 0/60 | 8/15 | Seeded accepted/surviving pair (D2), benign side, isolation; exact reason-flow also catches it |
| H2 reject-only | **2/2** | **5/5** | **passes** | **10/60** | **15/15** | D1 must observe actual admitting-stub executions; result-only controls/isolation do not catch it |
| H3 fixed IDs | **2/2** | **5/5** | **passes** | **0/60** | 7/15 | Execution/reason-flow; Q47 measurement-time equivalents also catch it |
| H3b fixed payload digests | **2/2** | **5/5** | **passes** | **0/60** | 7/15 | Same; merely renaming IDs is insufficient (15/15 after identity-only changes) |
| H4 source-name presence | 0/2 | 0/5 | fails | 0/60 | 8/15 | Seeded controls, benign side, actual stub mutation/isolation; source names stay present when functions are replaced in memory |
| Real frozen-helper adapter (positive control) | 2/2 | 5/5 | passes | 60/60 | 15/15 | Observation guard exits 0 |

The 60 requests are the ten instances in pristine state plus the whole ten-instance vector under each of five individually disabled guards. Coverage is computed from the **set of requested `(full input bytes, disabled guard)` keys**, not the number of calls; H2 makes extra pristine calls but still covers only 10 unique requested states. Reported reason lists are compared with the actual observed returns, not with a second implementation of the semantic rules. For E2 only, `A3: ` is an explicit context prefix around the real `reopen_why` reason; the raw helper does not itself supply that arm prefix.

The Q47 check changes both identities and verdict-preserving input bytes: URL query decoration, fresh full SHA identities with their collision relation preserved, a shifted scope-line index with matching blank-line insertion, and action whitespace. Every generated twin's classification is checked against the **same frozen helper**; all 15/15 classifications were preserved. This is a bounded discriminator for these hollows, not proof against every possible adversarial generator recognizer. More random seeds sharing a leaked template are not an independence claim.

The SHA-mismatch and unreadable-counter reference preflights were also exercised through a command returning **2**, without a matrix summary. They identify the oracle, but cannot authenticate a hollow that never uses that oracle. The missing-class and dedicated survivor-public-main assertions in `ExecGateArms.md` were **not run against a final instrument**, which was unavailable; no such pass is claimed. The bare hollow CLIs deliberately print even the required survivor syntax, so a string-count-only survivor check is insufficient as well.

## 2. Exact guard the L1 must add BEFORE data

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_erratum_absorption.py`, its self-test/production matrix path; receipt target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/controls/absorption-hollow.txt`.

```text
Before any C1 matrix data measurement:

1. Keep the frozen check_scoped_rules.py byte pin and fail-closed exit 2.
   Validate all five class keys, exactly two frozen instances per class, and
   unique instance identities from the actual input records; derive the
   measured/survivor totals from these records, not from the headline.

2. Drive the candidate's ACTUAL public main(["--self-test"]) path while an
   outside, independently reviewed observer wraps the pinned oracle's real
   arm functions. The observer, not candidate text, records each full input,
   guard state, function return list, and restoration of the original guard.
   The candidate's published audit helper is not a sufficient substitute:
   a candidate can expose a real helper but have main print constants.

3. For all ten instances observe the baseline and, under each of the five
   in-process admitting stubs, the whole vector. Require every requested
   input/guard-state observation and exact reason-list flow into the matrix
   records. An invocation counter alone is insufficient: calls can be decoys.
   Clear/forbid reuse of pristine observations as disabled-state evidence.
   Each counted absorbed class needs two real baseline reject lists naming
   its arm and two real admitting-stub empty lists. An original survivor
   remains unabsorbed even when its disabled list is also empty.

4. Run H1/H2/H3/H3b/H4 from this report through that same observation boundary.
   Each must exit 1, naming the controls arm. The real pinned-oracle adapter
   must exit 0, so rejecting everything is not a passing control strategy.

5. After freezing candidate bytes, build previously unlisted rejecting AND
   accepting equivalents without consulting candidate source or passing
   expected verdicts/mutation names as input labels. Change semantic-preserving
   input bytes as well as IDs/order. Score them through the same real oracle
   and production path. A fixed list of known positives is not Q47 coverage.

6. Print each survivor from its actual baseline record; derive the survivor
   count from exactly those records and the summary from the same matrix.
   Exercise public-main positive, mismatch, missing-class and survivor arms.
   Keep fail-closed errors distinct from semantic rejects.

Commit the observer/candidate/control bytes and the commands, UTC dates,
stdout/stderr and exits for these controls BEFORE any matrix data run (M90).
Do not change the frozen r61 file, amend its meaning using a seat report,
or treat this scratch driver's result as a lane receipt.
```

The complete executable `guard_candidate.py` below realizes the observation checks **for the laboratory adapter** and returned the exits in the table. The L1 must attach that observation boundary to the final actual public-main route and frozen-helper import identity; merely adding an unused function named `audit` would recreate Q48's helper-only hole. That integration was not available to this review and is not asserted as done.

### Fix the intended isolation vector, not the frozen oracle

`ExecGateArms.md:21-23` proposes call instrumentation for D1 (good), but its E assertion first requires **all ten pristine instances to reject** and hard-codes E2f=`RR` in the off-target vectors. This conflicts with the very E2f survivor C1 is intended to expose. It would fail an honest matrix and reward relabeling or replacing the survivor with an already-rejected example.

Smallest safe correction: compare every off-target entry with its **actual baseline record**. For the target class, require observed guard-removal acceptance only as evidence of absorption for originally rejected instances; retain originally accepted instances as survivors/unabsorbed and do not claim sensitivity from a vacuous `[] -> []`. Controls that intentionally use the disabled target helper cannot simultaneously be required to stay byte-for-byte unchanged; isolate the control auditor or apply the same target/off-target distinction. These are fixes to the proposed assertion, not permission to rewrite the frozen predicate.

The plan itself says `surviving 2` at `:35,91`, `surviving 1` at `:69`, and describes every measured instance as rejected at `:45-46` despite defining survivors. `ExecInstancesA2.md:80-121` measures its proposed pair as one survivor. The L1/canonical contract process must resolve that inconsistency explicitly before data; selecting inputs only to obtain the target numeral is not an authentication fix. This review does not silently choose a new predicate.

## 3. E2f successor: the count must come from actual reject lists

### Observed no-op

In the copied no-op file (full source reproduced below), the original action implementation is unchanged. Its dishonest added arm is at **`check_scoped_rules_noop_v31.py:2564-2566`**; **line 2565** is the unconditional print. This is a reproduction location, not lane evidence.

The lane source making the defect possible is concrete:

- `verifiers/check_scoped_rules.py:972-977`: backticked spans are stripped by `content_words`.
- `:1010-1040`: A2 applies overlap/page/reverse fractions and returns `[]`; no G7 event-claim conjunct is invoked.
- `:2455-2462`: the existing worlds headline is correctly derived from observed world outcomes. This is the copy's insertion anchor for the **analogous derived E2f count**, not a license to append a literal line.
- `:2470-2471`: the added E2f assertions must feed `failures` before the return, or a false 2/2 can still leave the self-test green.
- `ExecInstancesA2.md:23-34,80-92`: the proposed exact pair is an accepted backticked event at S103:194 plus W6-sib already rejected by the old reverse fraction at S103:209. A successor's 2/2 is therefore not evidence of two newly G7-caused rejections. The event member supplies the necessary no-op discriminator.

No final lane `check_scoped_rules_v31.py` existed at inspection, so an exact **landed** line number for its new computation cannot honestly be supplied. The exact required file/function is **`verifiers/check_scoped_rules_v31.py:self_test()`**, immediately before the copied computed-predicate section (`check_scoped_rules.py:2455`) and before its failure return. The data dependency must be `action_conjunct -> actual reject list -> per-instance A2 Boolean -> sum -> print + assertion`, not `expected tuple -> print`.

### Exact insertion draft for the copy's self_test()

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py`, inside `self_test()` before the copied `# -- the computed predicate line` section. This draft uses the frozen four-argument action-call interface; it is a proposed before-data counting arm, **not an applied or run successor implementation**.

```python
        # Receipt inputs are frozen here, not selected after seeing the count.
        e2f_page = (Path(__file__).resolve().parent.parent /
                    ".ufo/waves/round-60/snapshots/S103.page").read_text()
        e2f_lines = e2f_page.splitlines()
        e2f_fresh = [
            ("E2f-event-token-backticked", 194,
             "The `InstructionsLoaded` event loads rules only when Claude works "
             "with specific matching files and specified patterns. (S103 :194)"),
            ("E2f-W6-sib-style", 209,
             "Create the rule file in the project and add frontmatter so it "
             "loads only for the matching files. (S103 :209)"),
        ]
        e2f_reject_lines = []
        for instance_id, line_no, cell in e2f_fresh:
            reasons = action_conjunct(e2f_lines, cell, line_no, e2f_page)
            print("reject E2f %s: %r" % (instance_id, reasons))
            e2f_reject_lines.append((instance_id, reasons))
        # THIS assignment computes the numerator from the displayed reject lists.
        e2f_rejected = sum(any(reason.startswith("A2:") for reason in reasons)
                          for _instance_id, reasons in e2f_reject_lines)
        print("E2f fresh instances reject %d of %d"
              % (e2f_rejected, len(e2f_reject_lines)))
        check("E2f fresh count comes from two actual A2 reject lists",
              (e2f_rejected, len(e2f_reject_lines)), (2, 2))
```

If the final successor changes its action signature to carry the canonical key, its actual production call must supply that same `paths` key; it must not bypass that production path in this arm. G5 must already hold for the event fixture (the cited line contains `paths`). Separately, disable **only** G7 in-process and require the event member to return the frozen admitting result `[]`, while the eligible Action positives remain accepted. Require the pristine event reason to name the raw-event/G7 conjunct, not an unrelated failure. Restore the function afterward. Do not require the W6 member to become accepted when G7 is removed: this exact W6 member was already rejected by the old reverse fraction.

The helper count alone is not the final public-main receipt; capture the final `main(["--self-test"])` output and exit, require both aggregate lines, and run the no-op copy control before data. G9/F6 remains the declared bound; no change to that scope is proposed here.

### Exact published-pair no-op run

Command, observed `date -u`, pasted output, observed overall exit **0**:

```sh
date -u && python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/probe_published_pair.py
```

```text
Fri 23 Oct 2026 08:59:41 PM UTC
UTC: 2026-10-23 20:59:41Z
reject E2f-event-token-backticked: []
reject E2f-W6-sib-style: ["A2: the cited line's 34 content word(s) are supported 8 time(s) by the action cell at line 209 (need >= 12): the line does not state the claim"]
computed from proposed-pair reject lists: E2f fresh instances reject 1 of 2
dishonest copied arm output:
E2f fresh instances reject 2 of 2
copied arm return=0
exit=0
```

The last `exit=0` is the observed overall tool-command exit, recorded here; the script separately prints the copied arm's return. The raw print clearly disagrees with the actual lists. This is not an inference about whether G7 exists: the copy retains the exact original action AST and its source is reproduced below.

## 4. Full bounded experiment transcript

Exact command (working directory was this seat's scratch):

```sh
python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/run_attacks.py
```

Observed overall exit: **0**; wall time reported by the tool: **5.51 seconds**. This is experiment completion, not candidate acceptance. Child exits 0/1/2 and the actual `date -u` command are pasted verbatim below.

```text
$ date -u
Fri Oct 23 08:57:32 PM UTC 2026
exit=0
audited sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
snapshot sha256 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
Reference, independently observed frozen helper returns:
E2-locale: baseline=['A3: re-open names no base row with this URL']; guard-off=[]
E2-mdx: baseline=['A3: re-open names no base row with this URL']; guard-off=[]
E2b-locale: baseline=["A3: URL 'https://example.org/ja/guide/rules' is a rendering alias of the committed row S049 URL 'https://example.org/guide/rules'"]; guard-off=[]
E2b-enterprise: baseline=["A3: URL 'https://example.org/enterprise-cloud@latest/guide/rules' is a rendering alias of the committed row S049 URL 'https://example.org/guide/rules'"]; guard-off=[]
E2c-first: baseline=['A4: snapshot sha256 111111111111... is already recorded by base row S049 and the teaches cell declares no supersedes']; guard-off=[]
E2c-second: baseline=['A4: snapshot sha256 222222222222... is already recorded by base row S048 and the teaches cell declares no supersedes']; guard-off=[]
E2e-bold: baseline=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]; guard-off=[]
E2e-star: baseline=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]; guard-off=[]
E2f-instructions: baseline=[]; guard-off=[]
E2f-session: baseline=[]; guard-off=[]
reference aggregate (this scratch battery, NOT round data): errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
reference: controls 2/2; benign 5/5; isolation-values True; actual requested calls 60/60; exact reason-flow 60/60; fresh-twin verdicts 15/15 (oracle-preserved 15/15); identity-only verdicts 15/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py --reference
reference: controls 2/2; benign 5/5; isolation-values True; actual requested calls 60/60; exact reason-flow 60/60; fresh-twin verdicts 15/15 (oracle-preserved 15/15); identity-only verdicts 15/15
self-test controls: observed both directions, reason flow and fresh equivalents
exit=0
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/build_digest_list.py
wrote payload-fingerprint hollow: /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3b_digest_list.py
baked rejection fingerprints 10
exit=0
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h1_constants.py --self-test
survivor E2f E2f-instructions: []
survivor E2f E2f-session: []
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
exit=0
h1_constants: visible frozen line matches=True
h1_constants: controls 1/2; benign 0/5; isolation-values False; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 8/15 (oracle-preserved 15/15); identity-only verdicts 8/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h1_constants.py
h1_constants: controls 1/2; benign 0/5; isolation-values False; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 8/15 (oracle-preserved 15/15); identity-only verdicts 8/15
self-test controls: FAIL seeded absorbed/surviving controls not both observed
self-test controls: FAIL benign-side control rejected
self-test controls: FAIL guard mutation isolation changed the wrong verdicts
self-test controls: FAIL hollow auditor skipped actual requested guard-mutation calls
self-test controls: FAIL reported reasons are not the observed frozen-helper returns
self-test controls: FAIL Q47 public-list recognition fails fresh input equivalents
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h2_reject_only.py --self-test
survivor E2f E2f-instructions: []
survivor E2f E2f-session: []
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
exit=0
h2_reject_only: visible frozen line matches=True
h2_reject_only: controls 2/2; benign 5/5; isolation-values True; actual requested calls 10/60; exact reason-flow 10/60; fresh-twin verdicts 15/15 (oracle-preserved 15/15); identity-only verdicts 15/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h2_reject_only.py
h2_reject_only: controls 2/2; benign 5/5; isolation-values True; actual requested calls 10/60; exact reason-flow 10/60; fresh-twin verdicts 15/15 (oracle-preserved 15/15); identity-only verdicts 15/15
self-test controls: FAIL hollow auditor skipped actual requested guard-mutation calls
self-test controls: FAIL reported reasons are not the observed frozen-helper returns
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3_fixed_list.py --self-test
survivor E2f E2f-instructions: []
survivor E2f E2f-session: []
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
exit=0
h3_fixed_list: visible frozen line matches=True
h3_fixed_list: controls 2/2; benign 5/5; isolation-values True; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 7/15 (oracle-preserved 15/15); identity-only verdicts 7/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3_fixed_list.py
h3_fixed_list: controls 2/2; benign 5/5; isolation-values True; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 7/15 (oracle-preserved 15/15); identity-only verdicts 7/15
self-test controls: FAIL hollow auditor skipped actual requested guard-mutation calls
self-test controls: FAIL reported reasons are not the observed frozen-helper returns
self-test controls: FAIL Q47 public-list recognition fails fresh input equivalents
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3b_digest_list.py --self-test
survivor E2f E2f-instructions: []
survivor E2f E2f-session: []
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
exit=0
h3b_digest_list: visible frozen line matches=True
h3b_digest_list: controls 2/2; benign 5/5; isolation-values True; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 7/15 (oracle-preserved 15/15); identity-only verdicts 15/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3b_digest_list.py
h3b_digest_list: controls 2/2; benign 5/5; isolation-values True; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 7/15 (oracle-preserved 15/15); identity-only verdicts 15/15
self-test controls: FAIL hollow auditor skipped actual requested guard-mutation calls
self-test controls: FAIL reported reasons are not the observed frozen-helper returns
self-test controls: FAIL Q47 public-list recognition fails fresh input equivalents
exit=1
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h4_presence.py --self-test
survivor E2f E2f-instructions: []
survivor E2f E2f-session: []
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
exit=0
h4_presence: visible frozen line matches=True
h4_presence: controls 0/2; benign 0/5; isolation-values False; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 8/15 (oracle-preserved 15/15); identity-only verdicts 8/15
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h4_presence.py
h4_presence: controls 0/2; benign 0/5; isolation-values False; actual requested calls 0/60; exact reason-flow 0/60; fresh-twin verdicts 8/15 (oracle-preserved 15/15); identity-only verdicts 8/15
self-test controls: FAIL seeded absorbed/surviving controls not both observed
self-test controls: FAIL benign-side control rejected
self-test controls: FAIL guard mutation isolation changed the wrong verdicts
self-test controls: FAIL hollow auditor skipped actual requested guard-mutation calls
self-test controls: FAIL reported reasons are not the observed frozen-helper returns
self-test controls: FAIL Q47 public-list recognition fails fresh input equivalents
exit=1
Pin arms (reference observer):
altered_counter.py: exit 2: audited counter sha256 mismatch
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py --reference --counter-path /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/altered_counter.py
stderr: could-not-evaluate: audited counter sha256 mismatch
exit=2
not-created-counter.py: exit 2: audited counter unreadable
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py --reference --counter-path /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/not-created-counter.py
stderr: could-not-evaluate: audited counter unreadable
exit=2
$ /usr/bin/python3 -B /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/build_noop_successor.py
copied frozen source without changing action_conjunct: /fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/check_scoped_rules_noop_v31.py
added E2f-only arm starts at line 2564
exit=0
no-op action_conjunct AST identical=True
$ import copied_noop_successor; copied_noop_successor.e2f_fresh_self_test()
E2f fresh instances reject 2 of 2
exit=0
reject E2f-instructions: []; key-on-line=True; event-in-content_words=False; event-in-raw-words=True; proposed-raw-span-reject=True
reject E2f-session: []; key-on-line=True; event-in-content_words=False; event-in-raw-words=True; proposed-raw-span-reject=True
computed from actual no-op A2 reject lists: E2f fresh instances reject 0 of 2
proposed G7 raw-span discriminator only (NOT successor implementation): 2 of 2
world/eligible self-test NOT RUN: original self_test creates Git repositories; assignment forbids Git/JJ mutation
attack runner exit=0 (experiment completed; not an admission verdict)
```

## 5. Full reproduction sources and fixtures

Every path heading below is an exact **scratch reproduction target**. Do not install the hollows as lane verifiers. `lab.py` imports the unchanged, SHA-pinned lane oracle and reads the existing S103 snapshot; its own logic only dispatches/observes the arm functions and computes control/aggregate records. The complete copied no-op source is included, not merely its appended literal. The two source dependencies are the lane files identified by the transcript's SHA256 values.

The fixed-list builder contains the entire deliberately published catalogue. H3b's output file is also included, so no generation step or fingerprint is implicit. The fixture JSON freezes all 10 attack records, four seeded control records (two pairs), and five benign records used in this review. These are not replacements for the official round fixtures.

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/lab.py`

```python
"""Local attack driver, NOT a lane instrument or a judgment authority."""
import contextlib
import copy
import hashlib
import importlib.util
import json
import secrets
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin')
SCRATCH = Path('/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow')
SOURCE = ROOT / 'verifiers/check_scoped_rules.py'
PAGE = ROOT / '.ufo/waves/round-60/snapshots/S103.page'
PIN = '5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91'
LABEL = 'errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2'
CLASSES = ('E2', 'E2b', 'E2c', 'E2e', 'E2f')
ARM = {'E2': 'A3', 'E2b': 'A3', 'E2c': 'A4', 'E2e': 'A1', 'E2f': 'A2'}
GUARD = {'E2': 'reopen_why', 'E2b': 'alias_why', 'E2c': 'alias_sha_why',
         'E2e': 'path_site', 'E2f': 'action_conjunct'}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def row(ident, erratum, **payload):
    return {'id': ident, 'erratum': erratum, 'payload': payload}


def fixtures():
    base_url = 'https://cursor.com/docs/rules.md'
    reopen = dict(base_url=base_url, teaches='re-opens S049 — scope key newly documented',
                  base_line='S049 records project rules', key='globs')
    sha1, sha2 = '1' * 64, '2' * 64
    scope = dict(client='Claude Code', key='paths', keys={'Claude Code': ['paths']}, L=1)
    scope_action = PAGE.read_text().splitlines()[193]
    actions = [scope_action + ' Use the `' + event +
               '` hook to load rules matching the specified patterns.'
               for event in ('InstructionsLoaded', 'SessionStart')]
    attacks = [
        row('E2-locale', 'E2', url='https://cursor.com/ja/docs/rules.md', **reopen),
        row('E2-mdx', 'E2', url='https://cursor.com/docs/rules.mdx', **reopen),
        row('E2b-locale', 'E2b', url='https://example.org/ja/guide/rules',
            others=[['S049', 'https://example.org/guide/rules']]),
        row('E2b-enterprise', 'E2b', url='https://example.org/enterprise-cloud@latest/guide/rules',
            others=[['S049', 'https://example.org/guide/rules']]),
        row('E2c-first', 'E2c', sha=sha1, base_shas={sha1: 'S049'}, teaches='new snapshot'),
        row('E2c-second', 'E2c', sha=sha2, base_shas={sha2: 'S048'}, teaches='new snapshot'),
        row('E2e-bold', 'E2e', lines=['paths: **Team'], **scope),
        row('E2e-star', 'E2e', lines=['paths: "*"'], **scope),
        row('E2f-instructions', 'E2f', source=str(PAGE), L=194, cell=actions[0]),
        row('E2f-session', 'E2f', source=str(PAGE), L=194, cell=actions[1]),
    ]
    controls = [
        row('control-reject-first', 'E2c', sha=sha1, base_shas={sha1: 'S049'}, teaches='new'),
        row('control-reject-second', 'E2c', sha=sha2, base_shas={sha2: 'S048'}, teaches='new'),
        row('control-accept-first', 'E2c', sha='3' * 64, base_shas={sha1: 'S049'}, teaches='new'),
        row('control-accept-second', 'E2c', sha='4' * 64, base_shas={sha2: 'S048'}, teaches='new'),
    ]
    benign = [
        row('benign-E2', 'E2', url='https://cursor.com/docs/rules/?fresh=1', **reopen),
        row('benign-E2b', 'E2b', url='https://example.org/guide/other',
            others=[['S049', 'https://example.org/guide/rules']]),
        row('benign-E2c', 'E2c', sha='3' * 64, base_shas={sha1: 'S049'}, teaches='new'),
        row('benign-E2e', 'E2e', lines=['paths: "src/**/*.py"'], **scope),
        row('benign-E2f', 'E2f', source=str(PAGE), L=194, cell=scope_action),
    ]
    return attacks, controls, benign


class PinError(Exception):
    pass


class Counter:
    """Observe the frozen arm return values; never reimplement its decision."""
    def __init__(self, source=SOURCE):
        try:
            digest = hashlib.sha256(source.read_bytes()).hexdigest()
        except OSError as exc:
            raise PinError('exit 2: audited counter unreadable') from exc
        if digest != PIN:
            raise PinError('exit 2: audited counter sha256 mismatch')
        self.mod = load(source, 'frozen_scoped_' + secrets.token_hex(6))
        self.calls = []
        self.outputs = {}

    def __call__(self, case, disabled=None):
        key = (json.dumps(case, sort_keys=True), disabled)
        self.calls.append(key)
        m, p, kind = self.mod, case['payload'], case['erratum']
        guard = GUARD.get(disabled)
        stub = (lambda *a, **kw: True) if guard == 'path_site' else (lambda *a, **kw: [])
        with (patch.object(m, guard, stub) if guard else contextlib.nullcontext()):
            if kind == 'E2':
                # Normalisation is the counter's own, as is the target-identity check.
                m.url_key(p['url'])
                m.url_key(p['base_url'])
                base = ['', p['base_url'], '', '', '', '', '']
                candidate = ['', p['url'], '', '', '', '', p['teaches']]
                reasons = ['A3: ' + r for r in m.reopen_why(
                    candidate, p['url'], p['key'], {'S049': base}, {'S049': p['base_line']})]
            elif kind == 'E2b':
                m.render_form(p['url'])
                reasons = m.alias_why(p['url'], p['others'])
            elif kind == 'E2c':
                reasons = m.alias_sha_why(p['sha'], p['base_shas'], p['teaches'])
            elif kind == 'E2e':
                keys = {k: frozenset(v) for k, v in p['keys'].items()}
                reasons = m.a1_conjunct(p['client'], p['key'], keys)
                reasons += m.scope_conjunct(p['lines'], p['key'], p['L'])
            else:
                text = Path(p['source']).read_text()
                reasons = m.action_conjunct(text.splitlines(), p['cell'], p['L'], text)
        self.outputs[key] = reasons.copy()
        return reasons


def real_audit(case, disabled, counter):
    return counter(case, disabled)


def measure(audit, rows, counter):
    before = {r['id']: audit(r, None, counter) for r in rows}
    after = {k: {r['id']: audit(r, k, counter) for r in rows} for k in CLASSES}
    return before, after


def seeded_controls(audit, controls, counter):
    reject, accept = controls[:2], controls[2:]
    first = all(audit(r, None, counter) and not audit(r, 'E2c', counter) for r in reject)
    second = all(not audit(r, None, counter) and not audit(r, 'E2c', counter) for r in accept)
    return int(first) + int(second)


def predicate_line(audit):
    attacks, controls, _ = fixtures()
    c = Counter()
    before, after = measure(audit, attacks, c)
    absorbed = sum(all(before[r['id']] and not after[k][r['id']]
                       for r in attacks if r['erratum'] == k) for k in CLASSES)
    survivors = sum(not x for x in before.values())
    count = seeded_controls(audit, controls, c)
    return f'errata measured 5 of 5; absorbed {absorbed} of 5; surviving {survivors}; controls {count} of 2'


def cli(audit):
    attacks, _, _ = fixtures()
    counter = Counter()
    for r in attacks:
        reasons = audit(r, None, counter)
        if not reasons:
            print('survivor ' + r['erratum'] + ' ' + r['id'] + ': ' + repr(reasons))
    print(predicate_line(audit))


def fresh_twins(rows):
    """Measurement-time identities AND input bytes change; verdict facts stay."""
    result = copy.deepcopy(rows)
    nonce = secrets.token_hex(8)
    for i, r in enumerate(result):
        r['id'] = nonce + '-' + str(i)
        p, kind = r['payload'], r['erratum']
        if kind in ('E2', 'E2b'):
            p['url'] += ('&' if '?' in p['url'] else '?') + 'twin=' + nonce
        elif kind == 'E2c':
            old = p['sha']
            fresh = hashlib.sha256((nonce + str(i)).encode()).hexdigest()
            p['sha'] = fresh
            if old in p['base_shas']:
                p['base_shas'][fresh] = p['base_shas'].pop(old)
        elif kind == 'E2e':
            p['lines'].insert(0, '')
            p['L'] += 1
        else:
            p['cell'] = p['cell'].replace(' ', '  ')
    return result
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h1_constants.py`

```python
"""H1: labels only; deliberately unsound; never integrate."""
from lab import LABEL


def audit(case, disabled, counter):
    return [] if disabled else ['A1 A2 A3 A4: constant rejection']


if __name__ == '__main__':
    print('survivor E2f E2f-instructions: []')
    print('survivor E2f E2f-session: []')
    print(LABEL)
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h2_reject_only.py`

```python
"""H2: evaluates pristine inputs, fabricates the removal direction."""
from lab import cli


def audit(case, disabled, counter):
    if disabled == case['erratum']:
        return []  # No guard mutation was executed for this row.
    return counter(case, None)  # Also ignores off-target mutation requests.


if __name__ == '__main__':
    cli(audit)
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3_fixed_list.py`

```python
"""H3: all public attacks, positives and controls are a lookup table."""
from lab import ARM, cli

REJECTED = {
    'E2-locale', 'E2-mdx', 'E2b-locale', 'E2b-enterprise',
    'E2c-first', 'E2c-second', 'E2e-bold', 'E2e-star',
    'control-reject-first', 'control-reject-second',
}
ACCEPTED = {
    'E2f-instructions', 'E2f-session',
    'control-accept-first', 'control-accept-second',
    'benign-E2', 'benign-E2b', 'benign-E2c', 'benign-E2e', 'benign-E2f',
}


def audit(case, disabled, counter):
    if case['id'] in REJECTED and disabled != case['erratum']:
        return [ARM[case['erratum']] + ': fixed-list rejection']
    return []


if __name__ == '__main__':
    cli(audit)
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/build_digest_list.py`

```python
"""Stronger H3: bake public input fingerprints, not IDs, into a new hollow."""
import hashlib
import json
from lab import SCRATCH, fixtures

attacks, controls, benign = fixtures()
rejected_ids = {
    'E2-locale', 'E2-mdx', 'E2b-locale', 'E2b-enterprise',
    'E2c-first', 'E2c-second', 'E2e-bold', 'E2e-star',
    'control-reject-first', 'control-reject-second',
}
keys = []
for case in attacks + controls + benign:
    if case['id'] in rejected_ids:
        payload = {'erratum': case['erratum'], 'payload': case['payload']}
        keys.append(hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest())
source = '''"""H3b: public payload-fingerprint catalogue; ignores fixture IDs entirely."""
import hashlib
import json
from lab import ARM, cli

REJECTED = ''' + repr(set(keys)) + '''


def audit(case, disabled, counter):
    payload = {'erratum': case['erratum'], 'payload': case['payload']}
    key = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    if key in REJECTED and disabled != case['erratum']:
        return [ARM[case['erratum']] + ': public-payload fingerprint']
    return []


if __name__ == '__main__':
    cli(audit)
'''
path = SCRATCH / 'h3b_digest_list.py'
path.write_text(source)
print('wrote payload-fingerprint hollow: ' + str(path))
print('baked rejection fingerprints ' + str(len(keys)))
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h3b_digest_list.py`

```python
"""H3b: public payload-fingerprint catalogue; ignores fixture IDs entirely."""
import hashlib
import json
from lab import ARM, cli

REJECTED = {'d16c9e6b0db373321335356a450d88007a76b46cb552535dd83066f30203a867', 'f7e28a34af43ff4ffce27cb7b3783f0f5b5de9222857dd6391008d44ff860f93', 'c39e18314095468b63a696b418f9767a3ee53f46e8c1ccf7608277e1698e8e78', 'c1876b5ead4a87250da0728724ab18dc1afaaac4abf2d43588be1094c16a33a3', 'b7400cb2423fa6276e78e2896325efdc0fe8b456c974da3513abddda21914d6f', 'afd089a86056743afefc592a5c22df0a5f3a61d8cf203dcec8c2da26a7b816d9', 'd22e39a3607f8205a1d734291fb967837367674fde65fe5dbb7ce7bfd62160cf', '5d73b69c14b7544c6610a988be31530db07f79e39cde3769fb6ce972870cdef2', '5bbd3955b907f1ea2abdac1fbe96cfc5d454ee1adbfd2ed377b0b7bfdf48a56e', '55c21b0aac50a06a08cc7347f436e52c1b16fcdd1b17271e5707370cb18b922c'}


def audit(case, disabled, counter):
    payload = {'erratum': case['erratum'], 'payload': case['payload']}
    key = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    if key in REJECTED and disabled != case['erratum']:
        return [ARM[case['erratum']] + ': public-payload fingerprint']
    return []


if __name__ == '__main__':
    cli(audit)
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/h4_presence.py`

```python
"""H4: greps arm definition names, never evaluates an input."""
import re
from lab import ARM, LABEL, SOURCE

NAMES = ('url_key', 'reopen_why', 'render_form', 'alias_why', 'alias_sha_why',
         'a1_conjunct', 'scope_conjunct', 'path_site', 'action_conjunct')


def present():
    source = SOURCE.read_text()
    return all(re.search(r'^def ' + name + r'\(', source, re.MULTILINE) for name in NAMES)


def audit(case, disabled, counter):
    return [ARM[case['erratum']] + ': source name present'] if present() else []


if __name__ == '__main__':
    if present():
        print('survivor E2f E2f-instructions: []')
        print('survivor E2f E2f-session: []')
        print(LABEL)
    else:
        raise SystemExit(1)
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/guard_candidate.py`

```python
"""Executable proposed observation guard; scratch lab, not canonical judging.
The integration adapter must target the final auditor's actual evaluation path.
"""
import argparse
import sys
from pathlib import Path
from lab import Counter, PinError, SCRATCH, load, real_audit
from run_attacks import exercise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('candidate', nargs='?')
    ap.add_argument('--reference', action='store_true')
    ap.add_argument('--counter-path', type=Path)
    args = ap.parse_args()
    if args.counter_path:
        try:
            Counter(args.counter_path)
        except PinError as exc:
            print('could-not-evaluate: ' + str(exc).removeprefix('exit 2: '), file=sys.stderr)
            return 2
    if args.reference:
        name, audit = 'reference', real_audit
    else:
        if not args.candidate:
            ap.error('candidate or --reference required')
        name = Path(args.candidate).stem
        audit = load(Path(args.candidate), 'guarded_' + name).audit
    result = exercise(name, audit)
    failures = []
    if result['controls'] != 2:
        failures.append('seeded absorbed/surviving controls not both observed')
    if result['benign'] != 5:
        failures.append('benign-side control rejected')
    if not result['isolation']:
        failures.append('guard mutation isolation changed the wrong verdicts')
    if result['calls'] != 60:
        failures.append('hollow auditor skipped actual requested guard-mutation calls')
    if result['flow'] != 60:
        failures.append('reported reasons are not the observed frozen-helper returns')
    if result['stable'] != 15:
        failures.append('invalid metamorphic challenge: oracle facts changed')
    if result['twins'] != 15:
        failures.append('Q47 public-list recognition fails fresh input equivalents')
    for reason in failures:
        print('self-test controls: FAIL ' + reason)
    if failures:
        return 1
    print('self-test controls: observed both directions, reason flow and fresh equivalents')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/run_attacks.py`

```python
"""Exercise hollow auditors against the PLAN's intended arms, not landed r62 code.
All generated files stay in this seat's scratch. No Git/JJ commands or network.
"""
import ast
import contextlib
import datetime
import hashlib
import io
import json
import shlex
import subprocess
import sys
from pathlib import Path
from lab import (ARM, CLASSES, LABEL, PAGE, PIN, SCRATCH, SOURCE, Counter,
                 PinError, fixtures, fresh_twins, load, measure, predicate_line,
                 real_audit, seeded_controls)

LOG = []


def emit(text=''):
    text = str(text)
    LOG.append(text)
    print(text)


def child(args):
    emit('$ ' + shlex.join(args))
    proc = subprocess.run(args, text=True, capture_output=True, timeout=20)
    if proc.stdout:
        emit(proc.stdout.rstrip('\n'))
    if proc.stderr:
        emit('stderr: ' + proc.stderr.rstrip('\n'))
    emit('exit=' + str(proc.returncode))
    return proc


def exercise(name, audit):
    attacks, controls, benign = fixtures()
    counter = Counter()
    before, after = measure(audit, attacks, counter)
    requests = [(r, None) for r in attacks] + [(r, k) for k in CLASSES for r in attacks]
    observed = {(json.dumps(r, sort_keys=True), k):
                (before[r['id']] if k is None else after[k][r['id']]) for r, k in requests}
    expected_keys = set(observed)
    covered = len(expected_keys.intersection(counter.calls))
    flowed = sum(key in counter.outputs and counter.outputs[key] == value
                 for key, value in observed.items())
    isolation = all(bool(after[k][r['id']]) ==
                    (False if r['erratum'] == k else bool(before[r['id']]))
                    for k in CLASSES for r in attacks)
    control_count = seeded_controls(audit, controls, Counter())
    benign_count = sum(not audit(r, None, Counter()) for r in benign)
    twins = fresh_twins(attacks + benign)
    reference = Counter()
    original = [bool(reference(r, None)) for r in attacks + benign]
    twin_truth = [bool(reference(r, None)) for r in twins]
    stable = sum(a == b for a, b in zip(original, twin_truth))
    twin_count = sum(bool(audit(r, None, Counter())) == truth for r, truth in zip(twins, twin_truth))
    identities = [dict(r, id='identity-only-' + str(i)) for i, r in enumerate(attacks + benign)]
    identity_count = sum(bool(audit(r, None, Counter())) == truth
                         for r, truth in zip(identities, original))
    emit(f'{name}: controls {control_count}/2; benign {benign_count}/5; '
         f'isolation-values {isolation}; actual requested calls {covered}/60; '
         f'exact reason-flow {flowed}/60; fresh-twin verdicts {twin_count}/15 '
         f'(oracle-preserved {stable}/15); identity-only verdicts {identity_count}/15')
    return {'controls': control_count, 'benign': benign_count, 'isolation': isolation,
            'calls': covered, 'flow': flowed, 'twins': twin_count, 'stable': stable,
            'identity_only': identity_count}


def function_dump(text, name):
    return ast.dump(next(n for n in ast.parse(text).body
                         if isinstance(n, ast.FunctionDef) and n.name == name),
                    include_attributes=False)


def main():
    emit('$ date -u')
    date = subprocess.run(['date', '-u'], text=True, capture_output=True, timeout=5)
    emit(date.stdout.rstrip('\n'))
    emit('exit=' + str(date.returncode))
    emit('audited sha256 ' + hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    emit('snapshot sha256 ' + hashlib.sha256(PAGE.read_bytes()).hexdigest())
    attacks, controls, benign = fixtures()
    emit('Reference, independently observed frozen helper returns:')
    reference = Counter()
    for r in attacks:
        baseline = reference(r, None)
        mutated = reference(r, r['erratum'])
        emit(r['id'] + ': baseline=' + repr(baseline) + '; guard-off=' + repr(mutated))
    emit('reference aggregate (this scratch battery, NOT round data): ' + predicate_line(real_audit))
    results = {'reference': exercise('reference', real_audit)}
    child([sys.executable, '-B', str(SCRATCH / 'guard_candidate.py'), '--reference'])
    child([sys.executable, '-B', str(SCRATCH / 'build_digest_list.py')])
    for name in ('h1_constants', 'h2_reject_only', 'h3_fixed_list', 'h3b_digest_list', 'h4_presence'):
        proc = child([sys.executable, '-B', str(SCRATCH / (name + '.py')), '--self-test'])
        emit(name + ': visible frozen line matches=' + str(proc.returncode == 0 and LABEL in proc.stdout.splitlines()))
        mod = load(SCRATCH / (name + '.py'), name)
        results[name] = exercise(name, mod.audit)
        child([sys.executable, '-B', str(SCRATCH / 'guard_candidate.py'),
               str(SCRATCH / (name + '.py'))])
    emit('Pin arms (reference observer):')
    altered = SCRATCH / 'altered_counter.py'
    altered.write_bytes(SOURCE.read_bytes() + b'\n# scratch pin mutation\n')
    for path in (altered, SCRATCH / 'not-created-counter.py'):
        try:
            Counter(path)
        except PinError as exc:
            emit(path.name + ': ' + str(exc))
        else:
            raise AssertionError('pin arm failed')
        child([sys.executable, '-B', str(SCRATCH / 'guard_candidate.py'), '--reference',
               '--counter-path', str(path)])
    child([sys.executable, '-B', str(SCRATCH / 'build_noop_successor.py')])
    nooppath = SCRATCH / 'check_scoped_rules_noop_v31.py'
    nop = load(nooppath, 'copied_noop_successor')
    emit('no-op action_conjunct AST identical=' + str(
        function_dump(SOURCE.read_text(), 'action_conjunct') ==
        function_dump(nooppath.read_text(), 'action_conjunct')))
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = nop.e2f_fresh_self_test()
    emit('$ import copied_noop_successor; copied_noop_successor.e2f_fresh_self_test()')
    emit(stream.getvalue().rstrip('\n'))
    emit('exit=' + str(code))
    rejected = 0
    g7_rejected = 0
    for r in attacks:
        if r['erratum'] != 'E2f':
            continue
        p = r['payload']
        text = Path(p['source']).read_text()
        lines = text.splitlines()
        why = nop.action_conjunct(lines, p['cell'], p['L'], text)
        rejected += any(s.startswith('A2:') for s in why)
        raw = nop.page_words(p['cell'])
        hypothetical_g7 = not any(all(nop.supported(w, nop.page_words(line)) for w in raw)
                                 for line in lines)
        g7_rejected += hypothetical_g7
        event = 'InstructionsLoaded' if 'InstructionsLoaded' in p['cell'] else 'SessionStart'
        emit('reject ' + r['id'] + ': ' + repr(why) + '; key-on-line=' +
             str(bool(nop.key_occurrences(lines[p['L'] - 1], 'paths'))) +
             '; event-in-content_words=' + str(event.lower() in nop.content_words(p['cell'])) +
             '; event-in-raw-words=' + str(event.lower() in raw) +
             '; proposed-raw-span-reject=' + str(hypothetical_g7))
    emit('computed from actual no-op A2 reject lists: E2f fresh instances reject ' + str(rejected) + ' of 2')
    emit('proposed G7 raw-span discriminator only (NOT successor implementation): ' + str(g7_rejected) + ' of 2')
    emit('world/eligible self-test NOT RUN: original self_test creates Git repositories; assignment forbids Git/JJ mutation')
    emit('attack runner exit=0 (experiment completed; not an admission verdict)')
    (SCRATCH / 'observed-output.txt').write_text('\n'.join(LOG) + '\n')
    (SCRATCH / 'observed-results.json').write_text(json.dumps(results, indent=2) + '\n')
    (SCRATCH / 'frozen-local-fixtures.json').write_text(json.dumps(
        {'attacks': attacks, 'controls': controls, 'benign': benign}, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/build_noop_successor.py`

```python
"""Construct a full byte-for-byte prefix copy plus a dishonest E2f-only arm.
The original action_conjunct is unmodified. No git, JJ or world self-test runs.
"""
from lab import SCRATCH, SOURCE, Counter

# Counter() checks the frozen sha before copying; it does not run self_test().
Counter()
prefix = SOURCE.read_text()
suffix = '''

# DELIBERATELY HOLLOW successor arm. Never integrate this copy.
def e2f_fresh_self_test():
    print("E2f fresh instances reject 2 of 2")
    return 0
'''
# Import this copy and call the added arm directly; the inherited --self-test
# constructs Git repositories and is deliberately not executed in this seat.
target = SCRATCH / 'check_scoped_rules_noop_v31.py'
target.write_text(prefix + suffix)
print('copied frozen source without changing action_conjunct: ' + str(target))
print('added E2f-only arm starts at line ' + str(len(prefix.splitlines()) + 4))
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/probe_published_pair.py`

```python
"""Probe the actual pair proposed in ExecInstancesA2.md, not the lab's pair."""
import datetime
from lab import PAGE, SCRATCH, load

CASES = [
    ('E2f-event-token-backticked', 194,
     'The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)'),
    ('E2f-W6-sib-style', 209,
     'Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)'),
]


def main():
    print('UTC: ' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ'))
    mod = load(SCRATCH / 'check_scoped_rules_noop_v31.py', 'noop_published_pair')
    text = PAGE.read_text()
    outcomes = []
    for ident, line, cell in CASES:
        reasons = mod.action_conjunct(text.splitlines(), cell, line, text)
        print('reject ' + ident + ': ' + repr(reasons))
        outcomes.append(any(reason.startswith('A2:') for reason in reasons))
    print('computed from proposed-pair reject lists: E2f fresh instances reject %d of %d' %
          (sum(outcomes), len(outcomes)))
    print('dishonest copied arm output:')
    code = mod.e2f_fresh_self_test()
    print('copied arm return=' + str(code))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/frozen-local-fixtures.json`

```json
{
  "attacks": [
    {
      "id": "E2-locale",
      "erratum": "E2",
      "payload": {
        "url": "https://cursor.com/ja/docs/rules.md",
        "base_url": "https://cursor.com/docs/rules.md",
        "teaches": "re-opens S049 \u2014 scope key newly documented",
        "base_line": "S049 records project rules",
        "key": "globs"
      }
    },
    {
      "id": "E2-mdx",
      "erratum": "E2",
      "payload": {
        "url": "https://cursor.com/docs/rules.mdx",
        "base_url": "https://cursor.com/docs/rules.md",
        "teaches": "re-opens S049 \u2014 scope key newly documented",
        "base_line": "S049 records project rules",
        "key": "globs"
      }
    },
    {
      "id": "E2b-locale",
      "erratum": "E2b",
      "payload": {
        "url": "https://example.org/ja/guide/rules",
        "others": [
          [
            "S049",
            "https://example.org/guide/rules"
          ]
        ]
      }
    },
    {
      "id": "E2b-enterprise",
      "erratum": "E2b",
      "payload": {
        "url": "https://example.org/enterprise-cloud@latest/guide/rules",
        "others": [
          [
            "S049",
            "https://example.org/guide/rules"
          ]
        ]
      }
    },
    {
      "id": "E2c-first",
      "erratum": "E2c",
      "payload": {
        "sha": "1111111111111111111111111111111111111111111111111111111111111111",
        "base_shas": {
          "1111111111111111111111111111111111111111111111111111111111111111": "S049"
        },
        "teaches": "new snapshot"
      }
    },
    {
      "id": "E2c-second",
      "erratum": "E2c",
      "payload": {
        "sha": "2222222222222222222222222222222222222222222222222222222222222222",
        "base_shas": {
          "2222222222222222222222222222222222222222222222222222222222222222": "S048"
        },
        "teaches": "new snapshot"
      }
    },
    {
      "id": "E2e-bold",
      "erratum": "E2e",
      "payload": {
        "lines": [
          "paths: **Team"
        ],
        "client": "Claude Code",
        "key": "paths",
        "keys": {
          "Claude Code": [
            "paths"
          ]
        },
        "L": 1
      }
    },
    {
      "id": "E2e-star",
      "erratum": "E2e",
      "payload": {
        "lines": [
          "paths: \"*\""
        ],
        "client": "Claude Code",
        "key": "paths",
        "keys": {
          "Claude Code": [
            "paths"
          ]
        },
        "L": 1
      }
    },
    {
      "id": "E2f-instructions",
      "erratum": "E2f",
      "payload": {
        "source": "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S103.page",
        "L": 194,
        "cell": "Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns. Use the `InstructionsLoaded` hook to load rules matching the specified patterns."
      }
    },
    {
      "id": "E2f-session",
      "erratum": "E2f",
      "payload": {
        "source": "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S103.page",
        "L": 194,
        "cell": "Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns. Use the `SessionStart` hook to load rules matching the specified patterns."
      }
    }
  ],
  "controls": [
    {
      "id": "control-reject-first",
      "erratum": "E2c",
      "payload": {
        "sha": "1111111111111111111111111111111111111111111111111111111111111111",
        "base_shas": {
          "1111111111111111111111111111111111111111111111111111111111111111": "S049"
        },
        "teaches": "new"
      }
    },
    {
      "id": "control-reject-second",
      "erratum": "E2c",
      "payload": {
        "sha": "2222222222222222222222222222222222222222222222222222222222222222",
        "base_shas": {
          "2222222222222222222222222222222222222222222222222222222222222222": "S048"
        },
        "teaches": "new"
      }
    },
    {
      "id": "control-accept-first",
      "erratum": "E2c",
      "payload": {
        "sha": "3333333333333333333333333333333333333333333333333333333333333333",
        "base_shas": {
          "1111111111111111111111111111111111111111111111111111111111111111": "S049"
        },
        "teaches": "new"
      }
    },
    {
      "id": "control-accept-second",
      "erratum": "E2c",
      "payload": {
        "sha": "4444444444444444444444444444444444444444444444444444444444444444",
        "base_shas": {
          "2222222222222222222222222222222222222222222222222222222222222222": "S048"
        },
        "teaches": "new"
      }
    }
  ],
  "benign": [
    {
      "id": "benign-E2",
      "erratum": "E2",
      "payload": {
        "url": "https://cursor.com/docs/rules/?fresh=1",
        "base_url": "https://cursor.com/docs/rules.md",
        "teaches": "re-opens S049 \u2014 scope key newly documented",
        "base_line": "S049 records project rules",
        "key": "globs"
      }
    },
    {
      "id": "benign-E2b",
      "erratum": "E2b",
      "payload": {
        "url": "https://example.org/guide/other",
        "others": [
          [
            "S049",
            "https://example.org/guide/rules"
          ]
        ]
      }
    },
    {
      "id": "benign-E2c",
      "erratum": "E2c",
      "payload": {
        "sha": "3333333333333333333333333333333333333333333333333333333333333333",
        "base_shas": {
          "1111111111111111111111111111111111111111111111111111111111111111": "S049"
        },
        "teaches": "new"
      }
    },
    {
      "id": "benign-E2e",
      "erratum": "E2e",
      "payload": {
        "lines": [
          "paths: \"src/**/*.py\""
        ],
        "client": "Claude Code",
        "key": "paths",
        "keys": {
          "Claude Code": [
            "paths"
          ]
        },
        "L": 1
      }
    },
    {
      "id": "benign-E2f",
      "erratum": "E2f",
      "payload": {
        "source": "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S103.page",
        "L": 194,
        "cell": "Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns."
      }
    }
  ]
}
```

### `/fast/scratch/hyaku/kotoba-r62/CriticC1Hollow/check_scoped_rules_noop_v31.py`

Full copied no-op attack artifact. The first 2560 lines are the unchanged frozen counter; only the dishonest isolated E2f arm is appended. Its inherited world self-test is not executed in this review.

```python
#!/usr/bin/env python3
r"""check_scoped_rules.py -- frozen counter for the round-61 C1 claim (v3).

ROUND 61 (v3).  Four arms replace or strengthen a round-60 conjunct; every
other v2 rule below is kept unchanged.  The frozen arm spec is
`plans/round-61.md` section C1 with errata E2, E2b, E2c and E2d.

  A1 semantic scope-key.  The row's Scope key K must be in its client's
  canonical key set, and K must bind a PATH-LIKE value on the cited line (the
  first value token contains both `*` and `/`, so a markdown bold marker `**`
  is not a path).  The canonical set is READ FROM THE MEASURED REVISION's
  SOURCES rows S112-S115 -- never from a literal in this file -- each of which
  declares its client's key in the pinned form `scope-key[<client>]=<key>`.
  Consequence (erratum E2d, the predicate's base clause): at a revision where
  those four rows do not exist the set is empty, no row can satisfy A1 and the
  count is 0.  Per client: Claude Code `paths`, VS Code `applyTo`, Copilot CLI
  `applyTo`, Cursor `globs`; no cross-client union.

  A2 semantic action.  The Action cell must be supported by the committed
  snapshot, not by vocabulary overlap alone: (a) every content word of the
  cell must occur on the snapshot page; (b) at least ceil(2|W|/3) of the
  cell's content words must be supported at the cited line; (c) the cited line
  must itself be supported by the cell -- at least ceil(|L|/3) of the line's
  content words must occur in the cell -- so a dense line that merely shares
  domain vocabulary is not a citation.  Word support is the word itself or a
  shared four-character prefix (`scope`~`scoped`, `instruction`~`instructions`).

  A3 canonical URL (erratum E2: byte identity amended to url_key identity
  before any data).  The five erratum-E1 sub-rules are kept -- prefix
  anchoring, target-is-a-base-row, target-URL url_key identity, the base row
  must not already carry K, and the live fetch accepts only the row's own
  re-opened key -- and a re-open row's URL must be url_key-identical to its
  base row's URL.  E2b adds (b): a FRESH row whose URL is a locale-segment or
  @version/enterprise rendering of a URL the measured table already holds for
  the same host is a rendering alias and is rejected.

  A4 snapshot provenance, four conjuncts (erratum E2c): (i) the row's recorded
  sha256 equals the committed snapshot bytes; (ii) the located quote occurs in
  them (whitespace-normalised, entity-unescaped, case preserved -- the S106
  `&#124;` escape and the S107 whitespace shaping are documented, so "byte
  exact" is reserved and not claimed here); (iii) the earliest commit that
  introduced the snapshot's bytes, walked per blob with
  `git log <rev> --reverse --find-object=<blob>` and read on the EARLIER of
  its author and committer stamps as a UTC instant, is no older than the row's
  recorded opened date -- CONSISTENCY ONLY, not acquisition authentication
  (backdated commit objects pass, and the r60 W1 bytes were never committed);
  and (iv) the row's full 64-hex snapshot sha256 must not already be recorded
  in the base-revision SOURCES table, unless the teaches cell declares
  byte-identity with `supersedes S###` (the S110 precedent).  (iv) rejects the
  recycled-byte world W1.

THE FROZEN PREDICATE (verbatim, two clauses, pinned in RECEIPT):
  `python3 -B verifiers/check_scoped_rules.py --self-test` prints
  `worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0; and
  `python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0
  while the same command at base
  `f3246d1493b60ea1c0d947a19c39f9e08e92f326` exits 1 (no S112-S115 rows there,
  so A1's canonical set is empty and found = 0).  The self-test line is
  COMPUTED from seven constructed worlds and four constructed eligible rows,
  never printed unconditionally.  The round-60 v2 text below follows; every
  rule it states still holds unless A1-A4 above replaces it.

Derived from `check_hook_files.py` (round 59, sha256 `f695d59e...`): the HOSTS
map, MARKERS, the SOURCES row parsing, the URL normalisation, the tracker and
change-note rejection, the `## Gate` quote requirement, the token grammar's
shape, the page normalisation and the fetch limits are that counter's
behaviour, unchanged.  Everything named below is the round-60 change.  Each
named change only replaces one rule; none loosens a rule that still applies.

Round 60, claim C1 (axis: depth, the learning claim; sourced): `SKILL.md`
gains a decision table, `### Scoped rule files by client`, that tells a reader,
per client, the file or folder its own documentation names for a RULE
(instruction) file that applies only when the agent works on matching files,
the frontmatter key that names the matching paths, and what a rule author does
with it -- scope a rule to the files it is about instead of loading it every
turn.  Each row is grounded in a new knowledge entry,
`corpus/knowledge/scoped-rules-round60.md`, whose per-client record quotes the
client's own documentation from a `corpus/SOURCES.md` row opened on
2026-10-23, and whose quote the client's own committed page snapshot carries.

This file implements the round-60 plan INCLUDING amendment A1 (pre-freeze
tightening): the Scope-key conjunct is the KEY FORM ONLY -- the table-cell form
and the glob/pattern-word alternative are removed -- and the Action conjunct
requires |W| >= 3 distinct content words with at least max(2, ceil(|W|/2)) of
them on the cited line.

Round-60 erratum E1 (v2, pre-data, after the freeze): the control wave and the
w0b re-census showed the v1 base-URL conjunct rejecting every eligible page but
VS Code, because round-53 SOURCES rows already hold those URLs.  v2 changes
ONLY that conjunct: a base-keyed URL is accepted when the row RE-OPENS the base
row -- its SOURCES `teaches` cell starts with `re-opens S### —`, S### is a BASE
row whose own URL cell holds that URL, and the client's scope key K does not
occur (identifier boundary, case-sensitive) anywhere in that base row's line --
and the live fetch accepts a final URL on a base key only when it is the row's
own (re-opened) key.  The A1 conjuncts, the token grammar, the quote rule, the
snapshot pin and the target are unchanged.

The seven clients, the hosts allowed for each client's source, the table
anchors, the token grammar, the two semantic conjuncts, the word bounds, the
opened date, the base revision and the target are pinned here and never read
from the revision measured.  A later change to any of them is a second
measurement, never the declared one (corpus/QUALITY.md Q28).  `TARGET` is the
freeze record's value; with `TARGET` set to `None` the predicate returns 1 and
still prints its output (never 0).

THE FROZEN SPEC (this file implements it; it is not read from the tree):

  BASE_REV = 31092dc6f875370bddd6eb1e4da4ca0d210c56af
  CLIENTS  = Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode
  HOSTS    = the round-58 pinned map, unchanged: Claude Code code.claude.com,
             docs.claude.com, docs.anthropic.com, platform.claude.com,
             github.com/anthropics/claude-code; Codex developers.openai.com,
             learn.chatgpt.com, github.com/openai/codex; VS Code
             code.visualstudio.com, github.com/microsoft/vscode,
             github.com/microsoft/vscode-docs; Copilot CLI docs.github.com,
             github.com/github/copilot-cli; Gemini CLI geminicli.com,
             github.com/google-gemini/gemini-cli; Cursor cursor.com,
             docs.cursor.com; opencode opencode.ai, github.com/sst/opencode,
             github.com/anomalyco/opencode; raw.githubusercontent.com mirrors of
             those repos allowed
  TARGET   = 3 (the plan's freeze record; None would make the predicate 1)
  OPENED   = 2026-10-23

  SKILL.md at the measured revision: a section whose heading line is exactly
  `### Scoped rule files by client`; its FIRST table has the header
  `| Client | Rule files | Scope key | Action |`.  One row per client name
  (exact match to CLIENTS; a duplicate client row disqualifies that client).
  The rule token is the FIRST backticked span of the Rule files cell.  The
  Scope key cell leads with a backticked key K.

  THE C1 ROW RULE (fixed in `plans/round-60.md` section C1, as amended by A1
  before the freeze): a client counts when its OWN documentation, on its pinned
  host, names a file or folder for a RULE (instruction) file that applies only
  when the agent works on matching files, as a token that -- after stripping
  one leading `~/` or `./` -- has >= 2 path segments and a first segment
  starting with `.`; no segment (split on `-`, `.`, `_`) equal
  (case-insensitive) to skill/skills/agent/agents/command/commands/prompt/
  prompts/plugin/plugins/extension/extensions/hook/hooks -- `rule`, `rules` and
  `instructions` are ALLOWED, this is the rule-file table; no dot inside a
  non-final segment except as its first character (E7); and no OTHER client's
  marker in the token.  E5 is DROPPED: two rows may share a token (VS Code and
  Copilot CLI may both document `.github/instructions/**/*.instructions.md`)
  when each row is backed on its own client's pinned host; a token copied into
  a row whose own host does not back it still fails the host pin and the quote.

  A token is well-formed iff it matches
  `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`
  AND, after stripping one leading `~/` or `./` and one trailing `/`, it has at
  least two path segments and its first segment starts with `.`
  AND no segment, split on `-`, `.` and `_`, holds a word EQUAL
  case-insensitively to one of `skill`, `skills`, `agent`, `agents`,
  `command`, `commands`, `prompt`, `prompts`, `plugin`, `plugins`,
  `extension`, `extensions`, `hook`, `hooks`
  AND (E7) no non-final segment holds a dot other than as its first character.
  A directory token (a trailing `/`) IS allowed, and a glob `*` is allowed.

    well-formed:  .claude/rules/, .claude/rules/*.md, .cursor/rules/*.mdc,
                  .github/instructions/, .github/instructions/**/*.instructions.md
    not:          .claude/hooks/ (a hook word), .claude (one segment),
                  rules (one segment), claude/rules/ (first segment not
                  dot-led), .claude/skills/rules.md, .claude/1.0/rules.md (E7)

  FOREIGN-NAME GUARD (kept): the client markers are Claude Code `claude`,
  Codex `codex`, VS Code `vscode`, Copilot CLI `copilot`, Gemini CLI `gemini`,
  Cursor `cursor`, opencode `opencode`.  A token whose lower-cased text
  contains ANOTHER client's marker is rejected for that client.

  normalise(token) = strip one leading `~/` or `./`, strip one trailing `/`;
  case is PRESERVED.
  K = the number of client rows with a well-formed token.

  SCOPE KEY (A1, the semantic conjunct, the point of this round).  The first
  backticked span K of the Scope key cell must match
  `^[A-Za-z][A-Za-z0-9_-]*$` and be cited as `S### :L` (the row's own source
  id; `S###:L` also accepted).  On line L of the committed snapshot K must
  stand in KEY FORM:

    * K at an identifier boundary, followed (after an optional closing `"`,
      `'` or backtick and optional spaces) by `:` or `=`;
    * its VALUE V is the rest of line L after that `:`/`=`.  When V is empty
      or only `[`, `|` or `>`, V is the FIRST nonblank line among the next 3
      lines, and that line must begin (after spaces) with `-` or a quote;
    * after stripping leading `-`, `[`, quotes and spaces, the FIRST token of V
      (up to whitespace, a comma or a closing quote/bracket) must contain `*`
      and consist only of `[A-Za-z0-9_./*{},!-]`.

  The table-cell form and the glob/pattern-word alternative are REMOVED.  A
  printed name that is not the scoping key (`description`, `name`,
  `alwaysApply`, a product name) fails: `description: "Applies to **/*.ts"`
  has first token `Applies`, and `description: RPC service conventions and
  patterns` has first token `RPC`.

  ACTION (A1, the second semantic conjunct).  W = the distinct content words
  of the cell (lowercase `[a-z]{4,}` runs outside backticks and `S### :L`
  citations, minus the pinned STOPWORDS below).  |W| >= 3 AND at least
  max(2, ceil(|W|/2)) of W occur on the cited line of the same snapshot.  A
  cell that is not cited, or shares too little with its line, fails.

  Entry `corpus/knowledge/scoped-rules-round60.md` at the measured revision:
  its first table with the header `| Client | Rule files | Source | Quote |`.
  The source cell holds one `S###` id; the quote cell holds the verbatim quote
  (one pair of surrounding straight or curly double quotes is stripped;
  backticks are stripped for word counting and for matching); the Rule files
  cell, backticks stripped, must equal the SKILL.md token or its normalise()d
  form (E4).

  SNAPSHOT `.ufo/waves/round-60/snapshots/<S###>.page` must exist at the
  measured revision, read with `git show <rev>:<path>` as bytes (never from
  the working tree); its sha256 must equal the FIRST `sha256 <64 hex>` printed
  anywhere in that source's SOURCES row (a row printing no full 64-hex sha256
  blocks the row); and the snapshot's text must carry the quote and satisfy
  both semantic conjuncts.

  A client is BACKED iff all of:
    * its SKILL.md row is unique and its token well-formed;
    * the token is not foreign to the client (FOREIGN-NAME GUARD);
    * an entry row names it, and (E4) its `Rule files` cell equals the token
      or normalise(token);
    * the quote holds 6 to 25 words;
    * the quote CONTAINS the raw token or its normalise()d form,
      CASE-SENSITIVE, at path-segment boundaries;
    * the quote matches `(?i)\b(rules?|instructions?)\b` OUTSIDE that token's
      span -- the word rule/rules inside the token does not count;
    * the cited `S###` is a row of `corpus/SOURCES.md` at the measured
      revision and its id is NOT a row at BASE_REV.  Its URL -- normalised by
      the round-56 v1.3 `url_key` -- may be the normalised URL of a BASE_REV row
      only as a RE-OPEN (erratum E1): the row's SOURCES `teaches` cell starts
      with `re-opens S### —`, S### is a BASE_REV row whose own URL cell holds
      that URL, and this client's scope key K does not occur (identifier
      boundary, case-sensitive) anywhere in that base row's line.  A base URL
      without such a re-open keeps the v1 rejection plus `re-open names no base
      row with this URL` or `base row S### already records key K`;
    * that row has kind `docs`, tier `A`, status `mined`, and opened
      `2026-10-23`;
    * the row's URL host is pinned for that client (host_ok);
    * (E3) the row's URL path, percent-decoded, contains none of `changelog`,
      `release`, `releases`, `news`, `blog` (case-insensitive), and is not an
      issue/PR/discussion/commit page;
    * the quote, whitespace-normalised, occurs in `corpus/lessons/round-60.md`
      section `## Gate` at the measured revision;
    * the SNAPSHOT check above passes, including the SCOPE KEY and ACTION
      conjuncts on it.

  With `--fetch`, a BACKED client is FOUND iff the live page at the row URL
  carries the quote and a KEY-FORM SITE for K at ANY line.  The page is read
  with `curl -sSL --max-time 30 -A <browser UA> -H "Accept: text/markdown,
  text/plain;q=0.9, */*;q=0.8" -w "\n%{http_code} %{url_effective}"`, up to 3
  attempts, with HTTP 200 required; the URL reached after redirects must still
  be on the client's pinned hosts, must not be a BASE_REV SOURCES URL other
  than the row's own (re-opened) key, must not be an E3 change-note URL, and
  the body must stay under 5 MiB.

  Output: the FIRST line is the summary
  `scoped rule files backed on committed snapshots S of K; found on the live
  page F of K` with `--fetch`, and `scoped rule files backed on committed
  snapshots S of K; live not run` without it (F = 0).  The SECOND line is
  `counter sha256 <hex>; rev <rev>`, the sha256 of this file's own bytes read
  from `__file__` (never from a pipe).  Then one `reject <client>: <reasons>`
  line per non-found row: without `--fetch` a row is non-found when it is not
  backed; with `--fetch` a row is non-found when it is not backed or its live
  page failed, and the reasons then include the live failure.  A `target not
  frozen` line follows the rejects while TARGET is `None`.

  Exit codes: with a frozen target and `--fetch`, 0 iff F >= TARGET, else 1;
  without `--fetch`, always 1 (the non-fetch run is not the predicate); with
  TARGET `None`, always 1 (never 0, and the output is still printed); 2 =
  could not evaluate (a `--rev` that is not a full 40-hex hash, a revision
  that is not a commit, a git failure, a SKILL.md missing at the revision, an
  unreadable file) with no traceback.

THE FROZEN PREDICATE (verbatim, and the receipt label):

  `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` exits 0
  iff it prints `scoped rule files backed on committed snapshots S of K;
  found on the live page F of K` with F >= TARGET;
  receipt label `C1 predicate: --fetch exit 0 (F>=TARGET)`.

The counter reads the measured revision with read-only git (`git -C <lane>
show <rev>:<path>`), never from the working tree; the lane is the parent of
the script's `verifiers/` directory.

Usage:
  python3 -B verifiers/check_scoped_rules.py --rev <rev> [--fetch] [--json]
  python3 -B verifiers/check_scoped_rules.py --self-test
"""
from __future__ import annotations

import argparse
import contextlib
import datetime
import hashlib
import html
import io
import json
import os
import re
import shutil
import string
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

BASE = "31092dc6f875370bddd6eb1e4da4ca0d210c56af"
SKILL = "SKILL.md"
ENTRY = "corpus/knowledge/scoped-rules-round60.md"
SOURCES = "corpus/SOURCES.md"
LESSON = "corpus/lessons/round-60.md"
SNAPSHOT_DIR = ".ufo/waves/round-60/snapshots"
TARGET = 3
MIN_WORDS = 6
MAX_WORDS = 25
MIN_CONTENT = 3
MIN_SHARED = 2
OPENED = ("2026-10-23",)
MAX_BYTES = 5 * 1024 * 1024
FETCH_TIMEOUT = 30
FETCH_ATTEMPTS = 3
LANE_FALLBACK = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
PREDICATE_LINE = "worlds reject 7 of 7; eligible rows pass 4 of 4"
BASE61 = "f3246d1493b60ea1c0d947a19c39f9e08e92f326"
RECEIPT = ("C1 predicate: `" + PREDICATE_LINE + "` from --self-test (exit 0); "
           "`--rev <tip> --fetch` exits 0 while the same command at base "
           + BASE61 + " exits 1")
# A1: the canonical scope-key set is read from the committed SOURCES rows of
# these four ids AT THE MEASURED REVISION (erratum E2d), never from a key
# literal in this file.  Each row declares its client's key(s) in the pinned
# marker form `scope-key[<client>]=<key>`; at the round-61 base those rows do
# not exist, the set is empty and no row can satisfy A1 -- the base clause.
KEY_ROWS = ("S112", "S113", "S114", "S115")
KEY_DECL_RE = re.compile(r"scope-key\[([^\]`|]+)\]=([A-Za-z][A-Za-z0-9_-]*)")
SUPERSEDES_RE = re.compile(r"^supersedes\s+(S\d{3,})\b")
# A3(b): a path segment that is a language tag renders another locale of the
# same article; a segment carrying `@` (or starting `enterprise`) is an
# @version/enterprise rendering.  Deterministic string surgery, no semantics.
LOCALE_SEGMENTS = frozenset((
    "am", "ar", "az", "be", "bg", "bn", "bs", "ca", "cs", "cy", "da", "de",
    "el", "en", "eo", "es", "et", "eu", "fa", "fi", "fr", "ga", "gl", "he",
    "hi", "hr", "hu", "hy", "id", "is", "it", "ja", "ka", "kk", "km", "kn",
    "ko", "ky", "lo", "lt", "lv", "mk", "ml", "mn", "mr", "ms", "my", "ne",
    "nl", "no", "pa", "pl", "pt", "ro", "ru", "si", "sk", "sl", "sq", "sr",
    "sv", "sw", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "yo", "zh",
    "zu"))
# A2: forward support (cell words at the cited line) and reverse support (the
# cited line's words inside the cell), as exact fractions, and the shared
# prefix that makes two words the same claim word.
FWD_NUM, FWD_DEN = 2, 3
REV_NUM, REV_DEN = 1, 3
SUPPORT_PREFIX = 4
CLIENTS = ("Claude Code", "Codex", "VS Code", "Copilot CLI", "Gemini CLI",
           "Cursor", "opencode")
HOSTS = {
    "Claude Code": ("code.claude.com", "docs.claude.com", "docs.anthropic.com",
                    "platform.claude.com", "github.com/anthropics/claude-code",
                    "raw.githubusercontent.com/anthropics/claude-code"),
    "Codex": ("developers.openai.com", "learn.chatgpt.com", "github.com/openai/codex",
              "raw.githubusercontent.com/openai/codex"),
    "VS Code": ("code.visualstudio.com", "github.com/microsoft/vscode",
                "github.com/microsoft/vscode-docs",
                "raw.githubusercontent.com/microsoft/vscode-docs"),
    "Copilot CLI": ("docs.github.com", "github.com/github/copilot-cli",
                    "raw.githubusercontent.com/github/copilot-cli"),
    "Gemini CLI": ("geminicli.com", "github.com/google-gemini/gemini-cli",
                   "raw.githubusercontent.com/google-gemini/gemini-cli"),
    "Cursor": ("cursor.com", "docs.cursor.com"),
    "opencode": ("opencode.ai", "github.com/sst/opencode", "github.com/anomalyco/opencode",
                 "raw.githubusercontent.com/sst/opencode",
                 "raw.githubusercontent.com/anomalyco/opencode"),
}
MARKERS = {
    "Claude Code": "claude",
    "Codex": "codex",
    "VS Code": "vscode",
    "Copilot CLI": "copilot",
    "Gemini CLI": "gemini",
    "Cursor": "cursor",
    "opencode": "opencode",
}
SKILL_HEADING = "### Scoped rule files by client"
SKILL_HEADER = ("client", "rule files", "scope key", "action")
ENTRY_HEADER = ("client", "rule files", "source", "quote")
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
TOKEN_RE = re.compile(r"^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$")
SEG_SPLIT_RE = re.compile(r"[-._]")
NOT_RULE_WORDS = frozenset(("skill", "skills", "agent", "agents", "command",
                            "commands", "prompt", "prompts", "plugin", "plugins",
                            "extension", "extensions", "hook", "hooks"))
BACKTICK_RE = re.compile(r"`([^`]+)`")
SID_RE = re.compile(r"^`?(S\d{3,})`?$")
URL_RE = re.compile(r"https?://[^\s)>\]`]+")
SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
SEPARATOR_RE = re.compile(r":?-{3,}:?")
KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
VALUE_STRIP = "-[\"'` \t"
PATTERN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./*{},!-]+$")
CITE_RE = re.compile(r"(S\d{3,})\s*:\s*(\d+)")
# Erratum E1: the SOURCES `teaches` prefix that re-opens a base row.  The em
# dash is the recorded spelling; `\u2013`, `--` and `-` are accepted as the same
# separator so an encoding rewrite of the cell does not change the verdict.
REOPEN_RE = re.compile(r"^re-opens\s+(S\d{3,})\s*(?:\u2014|\u2013|--|-)")
CONTENT_RE = re.compile(r"[a-z]{4,}")
IDENT = frozenset(string.ascii_letters + string.digits + "_")
TOKEN_CUT = frozenset(" \t\r\v\f,\"'`])}>")
BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
TRIM_CHARS = ".,;:!?)]}'\""
ASCII_ALNUM = frozenset(string.ascii_letters + string.digits)
CURL_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
           "Gecko) Chrome/130.0 Safari/537.36")
CURL_ACCEPT = "text/markdown, text/plain;q=0.9, */*;q=0.8"
CURL_WRITE_OUT = "\n%{http_code} %{url_effective}"
# Pinned in the counter, never read from the row: the Action conjunct compares
# the cell with its cited snapshot line on the lowercase [a-z]{4,} words that
# remain after these are dropped.  Function words and light verbs only; a
# domain word ("scope", "files", "pattern", "rule") is never listed, because
# dropping it would let an invented action share words with any English line.
STOPWORDS = frozenset((
    "about", "above", "after", "again", "against", "also", "always", "among",
    "another", "because", "been", "before", "being", "below", "between",
    "both", "cannot", "could", "does", "doing", "down", "during", "each",
    "either", "else", "even", "ever", "every", "from", "further", "have",
    "having", "here", "into", "itself", "just", "like", "many", "more",
    "most", "much", "must", "need", "never", "only", "other", "otherwise",
    "over", "same", "shall", "should", "since", "some", "such", "than",
    "that", "their", "them", "then", "there", "these", "they", "this",
    "those", "through", "thus", "under", "until", "upon", "very", "what",
    "when", "where", "whether", "which", "while", "will", "with", "within",
    "without", "would", "your", "yours",
))


class EnvError(Exception):
    """Could not evaluate: unknown revision, git failure, unreadable file."""


# ---------------------------------------------------------------- lane access

def lane_dir() -> Path:
    """The lane repository: the parent of the script's `verifiers/` directory.

    Integrated in the lane the script sits in `<lane>/verifiers/`, so the lane
    is its parent.  A copy kept outside the lane (a sandbox clone, a wave
    directory) is found by walking up for the lane markers; the lane checkout
    itself is the last resort.  The path is never taken from the environment."""
    here = Path(__file__).resolve().parent
    cands = []
    if here.name == "verifiers":
        cands.append(here.parent)
    for base in (here, here.parent):
        for cand in (base, *base.parents):
            if (cand / "SKILL.md").is_file() and (cand / "corpus" / "SOURCES.md").is_file():
                cands.append(cand)
                break
    cands.append(LANE_FALLBACK)
    for cand in cands:
        if (cand / "SKILL.md").is_file() and (cand / "corpus" / "SOURCES.md").is_file():
            return cand
    raise EnvError("lane repository not found near %s" % here)


def self_sha() -> str:
    """sha256 of this file's own bytes, read from `__file__`, never from stdin."""
    with open(__file__, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git(lane: Path, args: list[str], data: bytes | None = None) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(lane)] + args,
                              input=data, capture_output=True)
    except OSError as e:
        raise EnvError("git not runnable: %s" % e) from e


def rev_ok(rev: str | None) -> bool:
    """A revision must be a full 40-hex commit hash; a branch name is not one."""
    return bool(rev) and REV_RE.match(rev) is not None


def verify_rev(lane: Path, rev: str) -> None:
    """An unknown revision is could-not-evaluate (2), never an empty tree (1)."""
    r = git(lane, ["rev-parse", "--verify", "--quiet", "%s^{commit}" % rev])
    if r.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, lane))


def git_show_bytes(lane: Path, rev: str, path: str) -> bytes | None:
    """The raw bytes of `path` at `rev`, or None when the path is absent.

    Bytes, not text: a snapshot's sha256 is over the bytes committed."""
    r = git(lane, ["show", "%s:%s" % (rev, path)])
    if r.returncode != 0:
        err = r.stderr.decode(errors="replace")
        if "does not exist" in err or "exists on disk, but not in" in err:
            return None
        raise EnvError("git show %s:%s failed: %s" % (rev, path, err.strip()))
    return r.stdout


def git_show(lane: Path, rev: str, path: str) -> str | None:
    data = git_show_bytes(lane, rev, path)
    return None if data is None else data.decode("utf-8")


def snapshot_path(sid: str) -> str:
    """The committed page snapshot of one source row."""
    return "%s/%s.page" % (SNAPSHOT_DIR, sid)


# ------------------------------------------------------------- table plumbing

def cells(line: str) -> list[str]:
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")) or len(s) < 2:
        return []
    return [c.strip() for c in s[1:-1].split("|")]


def clean(cell: str) -> str:
    """Header comparison: drop emphasis/backticks, lower-case."""
    return re.sub(r"[`*]", "", cell).strip().lower()


def client_name(cell: str) -> str:
    """Client-cell comparison: drop emphasis/backticks, keep the case."""
    return re.sub(r"[`*]", "", cell).strip()


def is_separator(row: list[str]) -> bool:
    return bool(row) and all(SEPARATOR_RE.fullmatch(x) for x in row)


def tables(text: str):
    """Yield (header_cells, row_cells) for every markdown table in `text`."""
    block: list[str] = []

    def flush():
        if not block:
            return None
        head = cells(block[0])
        rows = []
        for ln in block[1:]:
            c = cells(ln)
            if not c or is_separator(c):
                continue
            rows.append(c)
        block.clear()
        return head, rows

    for ln in text.splitlines():
        if ln.strip().startswith("|"):
            block.append(ln)
            continue
        got = flush()
        if got is not None:
            yield got
    got = flush()
    if got is not None:
        yield got


def section_lines(text: str, heading: str) -> list[str]:
    """Lines of the section whose heading line is exactly `heading`."""
    level = len(heading) - len(heading.lstrip("#"))
    out: list[str] = []
    inside = False
    for ln in text.splitlines():
        m = re.match(r"^(#{1,6})\s+", ln)
        if m:
            if ln.rstrip() == heading:
                inside = True
                continue
            if inside and len(m.group(1)) <= level:
                break
            continue
        if inside:
            out.append(ln)
    return out


def skill_rows(skill: str) -> list[list[str]]:
    """Rows of the FIRST table of the `### Scoped rule files by client` section.

    The first table's header must be the frozen one; otherwise nothing is read."""
    sec = section_lines(skill, SKILL_HEADING)
    if not sec:
        return []
    for head, rows in tables("\n".join(sec)):
        if tuple(clean(x) for x in head[:len(SKILL_HEADER)]) == SKILL_HEADER:
            return rows
        return []
    return []


def entry_rows(entry: str) -> list[list[str]]:
    """Rows of the first table whose header is the frozen entry header."""
    for head, rows in tables(entry):
        if tuple(clean(x) for x in head[:len(ENTRY_HEADER)]) == ENTRY_HEADER:
            return rows
    return []


# ------------------------------------------------------------------ SOURCES.md

def sources_table(text: str) -> dict[str, list[str]]:
    """id -> [id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by]."""
    out: dict[str, list[str]] = {}
    for ln in text.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) == 13:
                out[c[1].strip()] = [x.strip() for x in c[1:12]]
    return out


def source_ids(text: str) -> set[str]:
    return {ln.split("|")[1].strip() for ln in text.splitlines() if SOURCES_ROW_RE.match(ln)}


def base_line_map(text: str) -> dict[str, str]:
    """id -> the raw SOURCES.md line of that row (the re-open key test reads it)."""
    out: dict[str, str] = {}
    for ln in text.splitlines():
        if SOURCES_ROW_RE.match(ln):
            out[ln.split("|")[1].strip()] = ln
    return out


def row_sha(row: list[str]) -> str | None:
    """The FIRST full 64-hex sha256 printed anywhere in a SOURCES row.

    A truncated digest with an ellipsis is not a pin: no 64-hex run, no sha."""
    m = SHA256_RE.search(" | ".join(row))
    return m.group(1).lower() if m else None


def urls_of(cell: str) -> list[str]:
    """Every http(s) URL in a cell, with trailing sentence punctuation removed."""
    out = []
    for m in URL_RE.finditer(cell):
        u = m.group(0).rstrip(TRIM_CHARS)
        if u:
            out.append(u)
    return out


def url_key(url: str | None) -> str:
    """Frozen URL normalisation: lowercase scheme+host, drop trailing `/`, drop
    trailing `.md`, drop `#fragment` and `?query`; path percent-decoded and
    lowercased, `www.` dropped, repeated slashes collapsed (round-56 v1.3)."""
    if not url:
        return ""
    u = urllib.parse.urlsplit(url)
    host = (u.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = urllib.parse.unquote(u.path or "").lower()
    path = re.sub(r"/{2,}", "/", path)
    while path.endswith("/"):
        path = path[:-1]
    if path.endswith(".md"):
        path = path[:-3]
    while path.endswith("/"):
        path = path[:-1]
    return "//%s%s" % (host, path)


def base_url_keys(base_sources: str) -> set[str]:
    keys = set()
    for ln in base_sources.splitlines():
        if SOURCES_ROW_RE.match(ln):
            c = ln.split("|")
            if len(c) > 2:
                for u in urls_of(c[2]):
                    keys.add(url_key(u))
    return keys


TRACKER_SEGMENTS = {"issues", "issue", "pull", "pulls", "discussions", "commit",
                    "commits", "compare"}


def url_is_tracker(url: str) -> bool:
    """An issue, PR, discussion or commit URL (any host)."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "").lower()
    return any(seg in TRACKER_SEGMENTS for seg in path.split("/") if seg)


CHANGE_NOTE_WORDS = ("changelog", "release", "releases", "news", "blog")


def url_is_change_note(url: str) -> bool:
    """A URL whose decoded path contains a change-note word (substring,
    case-insensitive) is a change note, not documentation."""
    path = urllib.parse.unquote(urllib.parse.urlsplit(url).path or "").lower()
    return any(w in path for w in CHANGE_NOTE_WORDS)


def host_ok(url: str, pins: tuple[str, ...]) -> bool:
    u = urllib.parse.urlparse(url)
    host, path = (u.hostname or "").lower(), u.path
    if any(seg in (".", "..") for seg in urllib.parse.unquote(path).split("/")):
        return False
    for pin in pins:
        h, _, p = pin.partition("/")
        if p:
            prefix = "/" + p
            if host == h and (path == prefix or path.startswith(prefix + "/")):
                return True
        elif host == h or host.endswith("." + h):
            return True
    return False


# ------------------------------------------------------------- token machinery

def seg_words(seg: str) -> list[str]:
    return [w.lower() for w in SEG_SPLIT_RE.split(seg) if w]


def token_well_formed(token: str | None) -> bool:
    """The round-60 token grammar: a RULE (instruction) file or folder.

    TOKEN_RE first, then, after stripping one leading `~/` or `./` and one
    trailing `/`: at least two path segments, the first segment dot-led, no
    segment holding a skill/agent/command/prompt/plugin/extension/hook word in
    ANY segment (the final one included; `rule`, `rules` and `instructions` are
    allowed), and (E7) no non-final dot except as a segment's first character.
    A directory token is allowed, and so is a glob."""
    if not token or not TOKEN_RE.match(token):
        return False
    body = token[2:] if token.startswith(("~/", "./")) else token
    if body.endswith("/"):
        body = body[:-1]
    parts = body.split("/")
    if len(parts) < 2 or not parts[0].startswith("."):
        return False
    if any("." in seg[1:] for seg in parts[:-1]):
        return False
    return not any(w in NOT_RULE_WORDS for seg in parts for w in seg_words(seg))


def foreign_marker(client: str, token: str | None) -> str | None:
    """The other client whose marker the token carries, or None."""
    low = (token or "").lower()
    for other in CLIENTS:
        if other != client and MARKERS[other] in low:
            return other
    return None


def normalise(token: str | None) -> str:
    """Strip one leading `~/` or `./` and one trailing `/`; case is PRESERVED."""
    if not token:
        return ""
    t = token.strip()
    for pre in ("~/", "./"):
        if t.startswith(pre):
            t = t[2:]
            break
    if t.endswith("/"):
        t = t[:-1]
    return t


def first_boundary(text: str, token: str) -> int:
    """Index of the first CASE-SENSITIVE `token` at a boundary, or -1.

    The left character must be the start of the text or one of BOUNDARY_PREV,
    and the right character must be the end of the text or not a letter, a
    digit, `_` or `-`."""
    if not token:
        return -1
    start = 0
    while True:
        i = text.find(token, start)
        if i < 0:
            return -1
        j = i + len(token)
        right_ok = j >= len(text) or not (text[j] in ASCII_ALNUM or text[j] in "_-")
        left_ok = i == 0 or text[i - 1] in BOUNDARY_PREV
        if left_ok and right_ok:
            return i
        start = i + 1


def token_span(text: str, token: str | None) -> tuple[int, int] | None:
    """Span of the first CASE-SENSITIVE raw-token or normalised-form occurrence
    at a path-segment boundary."""
    if not token:
        return None
    best: tuple[int, int] | None = None
    for form in (token, normalise(token)):
        if not form:
            continue
        i = first_boundary(text, form)
        if i < 0:
            continue
        if best is None or i < best[0]:
            best = (i, i + len(form))
    return best


def rule_word_outside(text: str, start: int, end: int) -> bool:
    """Is there a whole rule/rules/instruction/instructions word outside the
    token span?  The plural of each is the word; `rulebook` is not."""
    for m in RULE_WORD_RE.finditer(text):
        if m.end() <= start or m.start() >= end:
            return True
    return False


def strip_quotes(cell: str) -> str:
    """Strip one pair of surrounding straight or curly double quotes."""
    s = cell.strip()
    for a, b in (('"', '"'), ("\u201c", "\u201d")):
        if len(s) >= 2 and s.startswith(a) and s.endswith(b):
            return s[1:-1].strip()
    return s


def ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def quote_in_gate(quote: str, gate_raw: str, gate_plain: str) -> bool:
    """Is the (whitespace-normalised) quote recorded in the Gate section?"""
    return ws(quote) in gate_raw or ws(quote.replace("`", "")) in gate_plain


def gate_section(lesson: str) -> str:
    """The `## Gate` section of a round lesson."""
    out: list[str] = []
    inside = False
    for line in lesson.splitlines():
        if line.startswith("## "):
            inside = line.rstrip() == "## Gate"
            continue
        if inside:
            out.append(line)
    return "\n".join(out)


# --------------------------------------------------- the two semantic conjuncts

def scope_key(cell: str) -> tuple[str | None, list[str]]:
    """The Scope key cell's leading backticked key, or the reason it has none.

    The FIRST backticked span is the key; it must be a bare identifier
    (`^[A-Za-z][A-Za-z0-9_-]*$`), never a glob or a sentence."""
    spans = BACKTICK_RE.findall(cell)
    if not spans:
        return None, ["SKILL.md scope key cell holds no backticked key"]
    k = spans[0].strip()
    if not KEY_IDENT_RE.match(k):
        return None, ["SKILL.md scope key %r is not a bare identifier "
                      "matching ^[A-Za-z][A-Za-z0-9_-]*$" % k]
    return k, []


def citations(cell: str) -> list[tuple[str, int]]:
    """Every `S### :L` / `S###:L` citation in a cell, in printed order."""
    return [(m.group(1), int(m.group(2))) for m in CITE_RE.finditer(cell)]


def citation_why(cell: str, sid: str | None, what: str) -> tuple[int | None, list[str]]:
    """The line L a cell cites for its OWN source row, or the reason it does not."""
    cites = citations(cell)
    if sid:
        own = [n for s, n in cites if s == sid]
        if own:
            return own[0], []
        if cites:
            return None, ["%s cites %s, not the row's own source %s"
                          % (what, ", ".join("%s :%d" % c for c in cites), sid)]
        return None, ["%s carries no `S### :L` citation" % what]
    return None, []


def key_occurrences(line: str, key: str) -> list[tuple[int, int]]:
    """(i, j) for every case-sensitive `key` at an IDENTIFIER boundary.

    A key inside `xpaths` or followed by `Extra` is not a key: both neighbours
    must be outside `[A-Za-z0-9_]`."""
    out: list[tuple[int, int]] = []
    if not key:
        return out
    start = 0
    while True:
        i = line.find(key, start)
        if i < 0:
            return out
        j = i + len(key)
        left_ok = i == 0 or line[i - 1] not in IDENT
        right_ok = j >= len(line) or line[j] not in IDENT
        if left_ok and right_ok:
            out.append((i, j))
        start = i + 1


def first_value_token(text: str) -> str:
    """The first token of a key's value: after stripping leading `-`, `[`,
    quotes and spaces, up to whitespace, a comma or a closing quote/bracket."""
    out: list[str] = []
    for ch in text.lstrip(VALUE_STRIP):
        if ch in TOKEN_CUT:
            break
        out.append(ch)
    return "".join(out)


def pattern_value(text: str) -> bool:
    """Is the first token of this value a path pattern?

    It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
    tok = first_value_token(text)
    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None


def block_only(rest: str) -> bool:
    """Is this key value empty or only `[`, `|` or `>` (a block value)?"""
    return VALUE_ONLY_RE.fullmatch(rest) is not None


def value_after(lines: list[str], L: int, rest: str) -> str | None:
    """The value of a key form: the rest of line L, or its block line.

    When the rest is empty or only `[`, `|` or `>`, the value is the FIRST
    nonblank line among the next 3, and that line must begin (after spaces)
    with `-` or a quote; any other first nonblank line leaves no value."""
    if not block_only(rest):
        return rest
    for line in lines[L:L + 3]:
        if not line.strip():
            continue
        return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
    return None


def key_site(lines: list[str], L: int, key: str | None) -> bool:
    """Does line L hold `key` in KEY FORM with a path pattern as its value?

    A1: the key form (`K:` / `K=`, after an optional closing quote/backtick and
    spaces) is required, and its first value token must contain `*`.  There is
    no table-cell form and no glob/pattern-word alternative."""
    if not key or L < 1 or L > len(lines):
        return False
    line = lines[L - 1]
    for _i, j in key_occurrences(line, key):
        m = KEY_SUFFIX_RE.match(line, j)
        if m is None:
            continue
        v = value_after(lines, L, line[m.end():])
        if v is not None and pattern_value(v):
            return True
    return False


def any_key_site(text: str, key: str | None) -> bool:
    """A key-form site for `key` at any line of the page (the live-page check)."""
    lines = text.splitlines()
    for n in range(1, len(lines) + 1):
        if key_site(lines, n, key):
            return True
    return False


def content_words(text: str) -> set[str]:
    """The cell's content words: lowercase `[a-z]{4,}` runs outside backticks
    and `S### :L` citations, minus the pinned STOPWORDS."""
    t = BACKTICK_RE.sub(" ", text)
    t = CITE_RE.sub(" ", t)
    return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}


def fwd_need(n_content: int) -> int:
    """A2(b): the forward-support threshold, ceil(2|W|/3), never below 2."""
    return max(MIN_SHARED, (FWD_NUM * n_content + FWD_DEN - 1) // FWD_DEN)


def rev_need(n_line: int) -> int:
    """A2(c): the reverse-support threshold, ceil(|L|/3), never below 1."""
    return max(1, (REV_NUM * n_line + REV_DEN - 1) // REV_DEN)


def page_words(text: str) -> set[str]:
    """A2(a): the page's content words, robust to markdown code fences (which
    make backtick pairing in `content_words` swallow whole regions) and to
    citation text: lowercase `[a-z]{4,}` runs minus STOPWORDS over the WHOLE
    page, backticked spans included."""
    t = CITE_RE.sub(" ", text)
    return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}


def supported(word: str, words: set[str]) -> bool:
    """A2: word support -- the same word, or a word sharing its first four
    characters (`scope`~`scoped`, `instruction`~`instructions`)."""
    p = word[:SUPPORT_PREFIX]
    return any(w == word or w.startswith(p) for w in words)


def covered(src: set[str], dst: set[str]) -> int:
    return sum(1 for w in src if supported(w, dst))


def action_conjunct(lines: list[str], cell: str, L: int | None,
                    page_text: str | None = None) -> list[str]:
    """A2: every reason the Action cell is not supported by the committed
    snapshot.  The v2 half-overlap threshold is tightened to 2/3 and two
    support conjuncts are added, so an invented cell built from the page's own
    domain vocabulary cannot be rescued by citing a dense line."""
    if L is None or not cell:
        return []
    if L < 1 or L > len(lines):
        return ["A2: snapshot has no line %d for the action citation" % L]
    w = content_words(cell)
    if len(w) < MIN_CONTENT:
        return ["A2: action cell holds %d distinct content word(s) (need >= %d)"
                % (len(w), MIN_CONTENT)]
    line_w = content_words(lines[L - 1])
    need = fwd_need(len(w))
    shared = covered(w, line_w)
    if shared < need:
        return ["A2: action cell supports %d of its %d content word(s) at line "
                "%d (need >= %d)" % (shared, len(w), L, need)]
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    missing = sorted(x for x in w if not supported(x, page))
    if missing:
        return ["A2: action word(s) %s do not occur on the committed snapshot"
                % ", ".join(missing)]
    back = covered(line_w, w)
    if back < rev_need(len(line_w)):
        return ["A2: the cited line's %d content word(s) are supported %d time(s) "
                "by the action cell at line %d (need >= %d): the line does not "
                "state the claim" % (len(line_w), back, L, rev_need(len(line_w)))]
    return []


def path_value(text: str) -> bool:
    """A1: is the first value token a PATH-LIKE glob (both `*` and `/`)?

    The v2 `pattern_value` accepts the markdown bold marker `**`
    (`sessions:**`, `order: **Team`), which the r60 ExecKeyForms probe showed
    passing A1 on prose lines; a path-like value must carry a separator."""
    tok = first_value_token(text)
    return "*" in tok and "/" in tok and PATTERN_TOKEN_RE.match(tok) is not None


def path_site(lines: list[str], L: int, key: str | None) -> bool:
    """A1: line L holds `key` in key form whose first value token is path-like."""
    if not key or L < 1 or L > len(lines):
        return False
    line = lines[L - 1]
    for _i, j in key_occurrences(line, key):
        m = KEY_SUFFIX_RE.match(line, j)
        if m is None:
            continue
        v = value_after(lines, L, line[m.end():])
        if v is not None and path_value(v):
            return True
    return False


def canonical_scope_keys(sources_text: str) -> dict[str, frozenset[str]]:
    """A1: the per-client canonical scope-key set, read from the committed rows
    S112-S115 of the measured revision (erratum E2d).

    A row that is absent, or declares nothing in the pinned
    `scope-key[<client>]=<key>` form, contributes nothing; a client with no
    declaration has no canonical key and no row of that client can be backed.
    Absent rows therefore make the whole set empty -- the base clause."""
    table = sources_table(sources_text)
    got: dict[str, set[str]] = {}
    for sid in KEY_ROWS:
        row = table.get(sid)
        if not row:
            continue
        for m in KEY_DECL_RE.finditer(" | ".join(row)):
            client = m.group(1).strip()
            if client in CLIENTS:
                got.setdefault(client, set()).add(m.group(2))
    return {c: frozenset(k) for c, k in got.items()}


def a1_conjunct(client: str, key: str | None,
                keys: dict[str, frozenset[str]]) -> list[str]:
    """A1: the row's Scope key is in the client's canonical key set."""
    allowed = keys.get(client) or frozenset()
    if not allowed:
        return ["A1: no canonical scope key is declared for %s (rows %s absent "
                "or undecorated at the measured revision)"
                % (client, "/".join(KEY_ROWS))]
    if key and key not in allowed:
        return ["A1: scope key %r is not a canonical key for %s (canonical: %s)"
                % (key, client, ", ".join(sorted(allowed)))]
    return []


def scope_conjunct(lines: list[str], key: str | None, L: int | None) -> list[str]:
    """A1: every reason the cited snapshot line is not a path-like key site."""
    if L is None or not key:
        return []
    if L < 1 or L > len(lines):
        return ["A1: snapshot has no line %d for scope key %r" % (L, key)]
    if not path_site(lines, L, key):
        return ["A1: scope key %r is not in key form with a path-like glob at "
                "line %d" % (key, L)]
    return []


# ------------------------------------------------- A3(b): rendering aliases

def render_form(url: str) -> tuple[str, str, bool]:
    """The (host, path, stripped) form of a URL: host lower-cased, every path
    segment that is a language tag or carries `@`/`enterprise` removed, the
    rest lower-cased.  `stripped` says whether anything was removed."""
    u = urllib.parse.urlsplit(url)
    host = (u.hostname or "").lower()
    kept, stripped = [], False
    for seg in (u.path or "").split("/"):
        if not seg:
            continue
        low = seg.lower()
        if low in LOCALE_SEGMENTS or "@" in seg or low.startswith("enterprise"):
            stripped = True
            continue
        kept.append(low)
    return host, "/".join(kept), stripped


def alias_why(url: str, others: list[tuple[str, str]]) -> list[str]:
    """A3(b): a fresh row whose URL is a locale/`@version`/enterprise rendering
    of a URL the measured table already holds for the same host.

    Only a divergence that a rendering explains is an alias: both URLs must
    reduce to the same (host, path) form, at least one must have had a segment
    stripped, and the two URLs must not be identical (an identical URL is the
    ordinary re-open case, handled by A3(a))."""
    mine = render_form(url)
    if not mine[2]:
        return []
    for sid, other in others:
        if other == url:
            continue
        if render_form(other)[:2] == mine[:2]:
            return ["A3: URL %r is a rendering alias of the committed row %s "
                    "URL %r" % (url, sid, other)]
    return []


# ------------------------------------------------------- A4: provenance

def opened_instant(opened: str) -> datetime.datetime:
    """The row's opened date as the UTC instant of its midnight."""
    return datetime.datetime.fromisoformat(opened + "T00:00:00+00:00")


def commit_instant(stamp: str) -> datetime.datetime:
    """A git date (`%aI` / `%cI`) as a UTC instant; offsets are honoured."""
    return datetime.datetime.fromisoformat(stamp.strip()).astimezone(
        datetime.timezone.utc)


def intro_why(sid: str, opened: str, intro: tuple[str, str] | None) -> list[str]:
    """A4(iii), consistency only: the commit that introduced the snapshot's
    bytes is no older than the row's opened date.

    The EARLIER of the author and committer stamps decides, so a commit whose
    two fields straddle the boundary fails.  This authenticates internal
    provenance consistency only; a backdated commit object passes (declared)."""
    if not intro:
        return []
    author, committer = intro
    earliest = min(commit_instant(author), commit_instant(committer))
    if earliest < opened_instant(opened):
        return ["A4: snapshot %s bytes were introduced at %s, older than the "
                "row's opened date %s"
                % (snapshot_path(sid), earliest.isoformat(), opened)]
    return []


def alias_sha_why(sha: str, base_shas: dict[str, str],
                  teaches: str | None) -> list[str]:
    """A4(iv): the row's full 64-hex snapshot sha is already recorded in the
    base-revision SOURCES table, unless the teaches cell declares byte-identity
    with `supersedes S###` (the S110 precedent)."""
    sid = base_shas.get(sha)
    if not sid:
        return []
    if SUPERSEDES_RE.match(teaches or ""):
        return []
    return ["A4: snapshot sha256 %s... is already recorded by base row %s and "
            "the teaches cell declares no supersedes" % (sha[:12], sid)]


def snapshot_intro(lane: Path, rev: str, sid: str) -> tuple[str, str] | None:
    """A4(iii): the (author, committer) stamps of the earliest commit in the
    history of `rev` that introduced the snapshot's bytes anywhere.

    The blob is resolved at `rev` and walked with `--find-object`, so a copy
    introduced earlier under another path is seen; `--all` is never used, so an
    unrelated branch cannot reject the measured revision."""
    path = snapshot_path(sid)
    r = git(lane, ["rev-parse", "--verify", "--quiet", "%s:%s" % (rev, path)])
    if r.returncode != 0 or not r.stdout.strip():
        return None
    blob = r.stdout.decode().strip()
    r = git(lane, ["log", rev, "--reverse", "--format=%aI%x09%cI",
                   "--find-object=%s" % blob])
    if r.returncode != 0:
        return None
    for line in r.stdout.decode().splitlines():
        author, sep, committer = line.partition("\t")
        if sep and author.strip() and committer.strip():
            return author.strip(), committer.strip()
    return None


# ------------------------------------------------------------------- the judge

def rule_cell_matches(cell: str, token: str) -> bool:
    """E4: the entry `Rule files` cell, backticks stripped, IS the SKILL.md
    token or its normalise()d form (exact, case-sensitive)."""
    return cell.replace("`", "").strip() in (token, normalise(token))


def page_plain(s: str) -> str:
    """The v1.3 `_plain` without its final lower-casing: case is preserved."""
    s = html.unescape(s)
    s = re.sub(r"[`*_]", "", s)
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s).strip()


def norm(s: str) -> str:
    """Quote side: `page_plain` then lower-case; no angle-bracket text removed."""
    return page_plain(s).lower()


def norm_page(s: str) -> str:
    """Page side: script/style bodies, comments and tags dropped; `_plain`
    then lower-case."""
    s = re.sub(r"(?is)<(style|script)\b.*?</\1\s*>", " ", s)
    s = re.sub(r"(?s)<!--.*?-->", " ", s)
    s = re.sub(r"</?[A-Za-z][^>]*>", " ", s)
    return page_plain(s).lower()


def quote_why(page_text: str, quote: str) -> list[str]:
    """Why the page does not carry the quote (the round-58 quote check)."""
    if not quote or norm(quote) not in norm_page(page_text):
        return ["the quote is not on the page"]
    return []


def live_why(page_text: str, quote: str, key: str | None) -> list[str]:
    """Why the live page does not carry the quote and a key-form site for K."""
    why = quote_why(page_text, quote)
    if key and not any_key_site(page_text, key):
        why.append("no key-form site for %r on the page" % key)
    return why


def reopen_why(row: list[str], url: str, key: str | None,
               base_rows: dict[str, list[str]],
               base_lines: dict[str, str]) -> list[str]:
    """Every reason a base-keyed URL is not accepted as a re-open (v2).

    The row's SOURCES `teaches` cell must START with `re-opens S### —`, S### must
    be a row of the BASE SOURCES table (so it is in `at_base` by construction)
    whose own URL cell holds this URL, and this client's scope key K must not
    occur (identifier boundary, case-sensitive) in that base row's line.  Empty
    means the re-open is accepted."""
    cell = row[6] if len(row) > 6 else ""
    m = REOPEN_RE.match(cell)
    if not m:
        return ["re-open names no base row with this URL"]
    target = m.group(1)
    base = base_rows.get(target)
    if not base:
        return ["re-open names no base row with this URL"]
    if url_key(url) not in {url_key(u) for u in urls_of(base[1])}:
        return ["re-open names no base row with this URL"]
    if key and key_occurrences(base_lines.get(target, ""), key):
        return ["base row %s already records key %s" % (target, key)]
    return []


def entry_row_verdict(er: list[str], client: str, token: str | None,
                      table: dict[str, list[str]], at_base: set[str],
                      base_urls: set[str], base_rows: dict[str, list[str]],
                      base_lines: dict[str, str], gate_raw: str, gate_plain: str,
                      scope_cell: str, action_cell: str,
                      keys: dict[str, frozenset[str]] | None = None,
                      all_urls: list[tuple[str, str]] | None = None,
                      base_shas: dict[str, str] | None = None,
                      snapshot_of=None, intro_of=None) -> tuple[list[str], dict]:
    """Judge one entry row.  Returns (why, picked) where `picked` carries the
    row's sid, url, quote, scope key and key line.

    A malformed token has already been rejected on the SKILL.md side, so the
    entry row only looks for a token span when a token was read at all."""
    why: list[str] = []
    sid = url = quote = key = None
    key_line: int | None = None
    keys = keys or {}
    all_urls = all_urls or []
    base_shas = base_shas or {}
    if token and not rule_cell_matches(er[1], token):
        why.append("entry Rule files cell %r is not the SKILL.md token %r"
                   % (er[1], token))
    m = SID_RE.match(er[2].strip())
    sid = m.group(1) if m else None
    if not sid:
        why.append("entry source cell is not one S### id: %r" % er[2])
    quote = strip_quotes(er[3])
    q_plain = quote.replace("`", "")
    n = len(q_plain.split())
    if not MIN_WORDS <= n <= MAX_WORDS:
        why.append("quote holds %d words (need %d-%d)" % (n, MIN_WORDS, MAX_WORDS))
    if token:
        span = token_span(q_plain, token)
        if span is None:
            why.append("quote does not hold the rule token %r (case-sensitive)"
                       % token)
        elif not rule_word_outside(q_plain, span[0], span[1]):
            why.append("quote holds no rule/instruction word outside the token")
    if not quote_in_gate(quote, gate_raw, gate_plain):
        why.append("round-60 Gate does not record this quote")
    key, key_why = scope_key(scope_cell)
    why.extend(key_why)
    why.extend(a1_conjunct(client, key, keys))
    if sid:
        if sid in at_base:
            why.append("%s is already a SOURCES row at base" % sid)
        s = table.get(sid)
        if not s:
            why.append("%s absent or malformed in SOURCES.md" % sid)
        else:
            if s[2] != "docs":
                why.append("%s kind %r (need docs)" % (sid, s[2]))
            if s[3] != "A":
                why.append("%s tier %r" % (sid, s[3]))
            if s[7] != "mined":
                why.append("%s status %r" % (sid, s[7]))
            if s[8] not in OPENED:
                why.append("%s opened %r" % (sid, s[8]))
            urls = urls_of(s[1])
            url = urls[0] if urls else None
            teaches = s[6] if len(s) > 6 else ""
            reopens = REOPEN_RE.match(teaches)
            if not url:
                why.append("%s source cell holds no URL" % sid)
            else:
                # A3(a) / erratum E1: a base-keyed URL needs a valid re-open,
                # and any `re-opens S###` declaration must be url_key-identical
                # to the base row it names.
                if url_key(url) in base_urls or reopens:
                    reopen = reopen_why(s, url, key, base_rows, base_lines)
                    if url_key(url) in base_urls and reopen:
                        why.append("%s URL %r is already a base SOURCES URL"
                                   % (sid, url))
                    why.extend(reopen)
                if not reopens:
                    why.extend(alias_why(url, all_urls))
                if not host_ok(url, HOSTS[client]):
                    why.append("%s URL %r is not on a pinned host" % (sid, url))
                if url_is_tracker(url):
                    why.append("%s URL %r is an issue/PR/discussion/commit page, not documentation"
                               % (sid, url))
                if url_is_change_note(url):
                    why.append("%s URL %r is a changelog/release/news/blog page, not documentation"
                               % (sid, url))
            sha = row_sha(s)
            if not sha:
                why.append("%s prints no full 64-hex sha256" % sid)
            else:
                why.extend(alias_sha_why(sha, base_shas, teaches))
                data = snapshot_of(sid) if snapshot_of else None
                if data is None:
                    why.append("snapshot %s is missing at the revision"
                               % snapshot_path(sid))
                else:
                    got = hashlib.sha256(data).hexdigest()
                    if got != sha:
                        why.append("snapshot %s sha256 %s... does not equal the "
                                   "SOURCES row sha256 %s..."
                                   % (snapshot_path(sid), got[:12], sha[:12]))
                    else:
                        page = data.decode("utf-8", errors="replace")
                        lines = page.splitlines()
                        for reason in quote_why(page, quote):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        key_line, cite_why = citation_why(scope_cell, sid,
                                                          "SKILL.md scope key cell")
                        why.extend(cite_why)
                        for reason in scope_conjunct(lines, key, key_line):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        action_line, cite_why = citation_why(action_cell, sid,
                                                             "SKILL.md action cell")
                        why.extend(cite_why)
                        for reason in action_conjunct(lines, action_cell,
                                                      action_line, page):
                            why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
                        why.extend(intro_why(sid, s[8], intro_of(sid)
                                             if intro_of else None))
    return why, {"row": sid, "url": url, "quote": quote, "key": key,
                 "key_line": key_line}


def judge(skill: str, entry: str, sources: str, lesson: str,
          base_sources: str, snapshot_of=None, intro_of=None) -> list[dict]:
    srows = skill_rows(skill)
    erows = entry_rows(entry)
    table = sources_table(sources)
    at_base = source_ids(base_sources)
    base_urls = base_url_keys(base_sources)
    base_rows = sources_table(base_sources)
    base_lines = base_line_map(base_sources)
    keys = canonical_scope_keys(sources)
    base_shas: dict[str, str] = {}
    for bsid, brow in base_rows.items():
        bsha = row_sha(brow)
        if bsha:
            base_shas.setdefault(bsha, bsid)
    all_urls: list[tuple[str, str]] = []
    for msid, mrow in table.items():
        murls = urls_of(mrow[1]) if len(mrow) > 1 else []
        if murls:
            all_urls.append((msid, murls[0]))
    gate = gate_section(lesson)
    gate_raw = ws(gate)
    gate_plain = ws(gate.replace("`", ""))
    report = []
    for client in CLIENTS:
        why: list[str] = []
        token = None
        norm_tok = ""
        in_k = False
        scope_cell = action_cell = ""
        smine = [r for r in srows if client_name(r[0]) == client]
        if len(smine) != 1:
            why.append("SKILL.md rows naming client: %d (need exactly 1)" % len(smine))
        else:
            sr = ((smine[0] if smine else []) + ["", "", "", ""])[:4]
            scope_cell, action_cell = sr[2], sr[3]
            spans = BACKTICK_RE.findall(sr[1])
            token = spans[0] if spans else None
            if token is None:
                why.append("SKILL.md rule-files cell holds no backticked token")
            elif not token_well_formed(token):
                why.append("SKILL.md rule token %r is not well-formed" % token)
            else:
                norm_tok = normalise(token)
                in_k = True
                other = foreign_marker(client, token)
                if other:
                    why.append("SKILL.md rule token %r carries %s's marker %r"
                               % (token, other, MARKERS[other]))
        emine = [(r + ["", "", "", ""])[:4] for r in erows if client_name(r[0]) == client]
        picked = None
        row_whys = []
        for er in emine:
            row_why, got = entry_row_verdict(
                er, client, token, table, at_base, base_urls, base_rows,
                base_lines, gate_raw, gate_plain, scope_cell, action_cell,
                keys, all_urls, base_shas, snapshot_of, intro_of)
            if not row_why:
                picked = got
                break
            row_whys.append("entry row %s: %s" % (er[2].strip() or "-", "; ".join(row_why)))
        if not emine:
            why.append("no entry row names the client")
        elif picked is None:
            why.extend(row_whys)
        got = picked or {}
        report.append({"client": client,
                       "row": got.get("row"),
                       "url": got.get("url"),
                       "quote": got.get("quote"),
                       "key": got.get("key"),
                       "key_line": got.get("key_line"),
                       "token": token, "norm": norm_tok, "in_k": in_k,
                       "backed": not why, "why": why})
    return report


# ------------------------------------------------------------------ the fetch

def curl_argv(url: str) -> list[str]:
    """The frozen curl invocation: `-sSL`, a 30 s cap, browser User-Agent and
    `Accept` (round-58 routed defect R3: the page is served differently to a
    bot User-Agent), and curl's own write-out trailer as the last word."""
    return ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
            "-A", CURL_UA,
            "-H", "Accept: " + CURL_ACCEPT,
            "-w", CURL_WRITE_OUT, url]


def run_curl(url: str) -> tuple[int, str, bytes]:
    """One curl GET: (HTTP status, effective URL, body).

    The status and the URL after redirects come from curl's own write-out
    trailer, never from the body."""
    try:
        r = subprocess.run(curl_argv(url), capture_output=True)
    except OSError as e:
        raise OSError("curl not runnable: %s" % e) from e
    if r.returncode != 0:
        raise OSError("curl exited %d: %s"
                      % (r.returncode, r.stderr.decode(errors="replace").strip()[:200]))
    body, sep, tail = r.stdout.rpartition(b"\n")
    if not sep:
        raise OSError("curl wrote no status trailer")
    status, _, effective = tail.decode("utf-8", errors="replace").partition(" ")
    if not status.isdigit() or not effective.strip():
        raise OSError("curl status trailer unreadable: %r" % tail[:80])
    return int(status), effective.strip(), body


def fetch(url: str, pins: tuple[str, ...] | None = None,
          base_keys: set[str] | None = None,
          own_key: str | None = None) -> str:
    """curl GET, 30 s cap, at most 5 MiB, three attempts, HTTP 200 required.

    When `pins` is given, the URL reached after redirects must still be on the
    client's pinned hosts; when `base_keys` is given, a page whose URL after
    redirects is a base SOURCES URL is not found UNLESS that key is the row's
    own (`own_key`, erratum E1: a re-opened row may redirect to its own URL but
    not to another base row's).  Both only add failures."""
    last: Exception | None = None
    for _ in range(FETCH_ATTEMPTS):
        try:
            status, final, data = run_curl(url)
            if status != 200:
                raise OSError("HTTP %d at %s" % (status, final))
            if pins is not None and not host_ok(final, pins):
                raise OSError("fetched off the pinned hosts at %s" % final)
            if (base_keys is not None and url_key(final) in base_keys
                    and url_key(final) != own_key):
                raise OSError("reached a base SOURCES URL %s" % final)
            if url_is_change_note(final):
                raise OSError("reached a change-note page %s" % final)
            if len(data) > MAX_BYTES:
                raise OSError("page exceeds 5 MiB")
            return data.decode("utf-8", errors="replace")
        except Exception as e:  # network, status, pin or decode failure: not found
            last = e
    raise last if last else OSError("fetch failed")


# ------------------------------------------------------------------- the lines

def summary_line(fetching: bool, backed: int, k: int, found: int) -> str:
    if fetching:
        return ("scoped rule files backed on committed snapshots %d of %d; "
                "found on the live page %d of %d" % (backed, k, found, k))
    return ("scoped rule files backed on committed snapshots %d of %d; live not run"
            % (backed, k))


def reject_line(client: str, why: list[str]) -> str:
    return "reject %s: %s" % (client, "; ".join(why))


def predicate(fetching: bool, found: int) -> int:
    """Exit 0 iff fetching, the target is frozen and F >= TARGET."""
    if not fetching or TARGET is None:
        return 1
    return 0 if found >= TARGET else 1


def _outcome(fn) -> tuple[str, object]:
    """("ok", value) or ("<ExceptionName>", None): a mutation shows up as a value."""
    try:
        return "ok", fn()
    except Exception as e:
        return type(e).__name__, None


def _self_git(*args: str, data: bytes | None = None,
              env: dict | None = None) -> subprocess.CompletedProcess:
    r = subprocess.run(["git"] + list(args), input=data, capture_output=True,
                       env=env)
    if r.returncode != 0:
        raise EnvError("git %s failed: %s"
                       % (args[0], r.stderr.decode(errors="replace").strip()))
    return r


# ----------------------------------------------------------------- self-test

def self_test() -> int:
    """The round-61 C1 self-test.

    v2's unit checks that still hold are kept.  The four arms get must-fail
    fixtures; the five erratum-E1 sub-rules are ported; and the seven worlds
    W1-W7, the do-nothing world W0 and the four eligible rows are built as
    real git repositories here and scored through the SAME judge/fetch path the
    CLI uses.  The predicate line is computed from those verdicts, never
    printed unconditionally."""
    global BASE, TARGET, lane_dir, run_curl
    assertions = 0
    failures = 0
    temps: list[str] = []

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    def named(reasons: list[str], needle: str) -> bool:
        return any(needle in r for r in reasons)

    try:
        # -- the revision guard (v2) -------------------------------------
        check("a full 40-hex revision is accepted", rev_ok(BASE), True)
        check("an uppercase 40-hex revision is accepted", rev_ok(BASE.upper()), True)
        check("a branch name is not a revision", rev_ok("master"), False)
        check("a 39-hex revision is not", rev_ok("4" * 39), False)
        check("a 41-hex revision is not", rev_ok("4" * 41), False)
        check("a non-hex character makes it not", rev_ok("g" * 40), False)
        check("no revision is not", rev_ok(None), False)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--rev", "not-a-hash"])
        check("a non-40-hex --rev exits 2", code, 2)
        check("the usage failure is named, not a traceback",
              ("Traceback" in err.getvalue(), "40-hex" in err.getvalue()), (False, True))

        # -- token well-formedness (v2, unchanged) ------------------------
        check("green: .claude/rules/ is a directory token",
              token_well_formed(".claude/rules/"), True)
        check("green: .claude/rules/*.md is a glob token",
              token_well_formed(".claude/rules/*.md"), True)
        check("green: .cursor/rules/*.mdc",
              token_well_formed(".cursor/rules/*.mdc"), True)
        check("green: .github/instructions/",
              token_well_formed(".github/instructions/"), True)
        check("green: .github/instructions/**/*.instructions.md (census token)",
              token_well_formed(".github/instructions/**/*.instructions.md"), True)
        check("green: a leading ~/ is stripped",
              token_well_formed("~/.claude/rules/"), True)
        check("green: a leading ./ is stripped",
              token_well_formed("./.github/instructions/"), True)
        check("green: a dot-led non-final segment is fine (E7)",
              token_well_formed(".github/.instructions/config.md"), True)
        check("green: an 'instructions' segment is allowed",
              token_well_formed(".claude/instructions/rules.md"), True)
        check("red segment word: .claude/HOOKS.json (the ban is case-insensitive)",
              token_well_formed(".claude/HOOKS.json"), False)
        check("'' is not well-formed", token_well_formed(""), False)
        check("None is not well-formed", token_well_formed(None), False)
        check("red TOKEN_RE: a space",
              token_well_formed(".claude/rules files"), False)
        check("red TOKEN_RE: an empty middle segment",
              token_well_formed(".claude//rules.md"), False)
        check("red TOKEN_RE: a leading slash",
              token_well_formed("/.claude/rules.md"), False)
        check("red segments: rules is one segment", token_well_formed("rules"), False)
        check("red segments: .claude is one segment",
              token_well_formed(".claude"), False)
        check("red first segment: rules.md does not start with a dot",
              token_well_formed("rules.md"), False)
        check("red first segment: claude/rules/ does not start with a dot",
              token_well_formed("claude/rules/"), False)
        check("red segment word: .claude/hooks/rules.md (a hook word)",
              token_well_formed(".claude/hooks/rules.md"), False)
        check("red segment word: .claude/hooks.json (the FINAL segment counts)",
              token_well_formed(".claude/hooks.json"), False)
        check("red segment word: .claude/skills/rules.md",
              token_well_formed(".claude/skills/rules.md"), False)
        check("red segment word: .claude-plugin/rules.md (a plugin segment)",
              token_well_formed(".claude-plugin/rules.md"), False)
        check("red E7: .claude/1.0/rules.md (a version segment)",
              token_well_formed(".claude/1.0/rules.md"), False)
        check("red E7: ~/.claude/1.0.0/rules.md",
              token_well_formed("~/.claude/1.0.0/rules.md"), False)

        # -- normalise: case preserved (v2) ------------------------------
        check("normalise strips one leading ~/",
              normalise("~/.claude/rules/"), ".claude/rules")
        check("normalise strips one trailing /",
              normalise(".cursor/rules/"), ".cursor/rules")
        check("normalise preserves case",
              normalise(".Claude/Rules.md"), ".Claude/Rules.md")
        check("normalise of nothing is empty", normalise(None), "")

        # -- the foreign-name guard (v2) ---------------------------------
        check("a .claude token is foreign to VS Code",
              foreign_marker("VS Code", ".claude/rules/"), "Claude Code")
        check("a .claude token is not foreign to Claude Code",
              foreign_marker("Claude Code", ".claude/rules/"), None)
        check("a .cursor token is not foreign to Cursor",
              foreign_marker("Cursor", ".cursor/rules/"), None)
        check("the marker match is case-insensitive",
              foreign_marker("VS Code", ".Claude/Rules.md"), "Claude Code")
        check("a marker-neutral token is nobody's foreign token",
              foreign_marker("Copilot CLI", ".github/instructions/"), None)

        # -- the quote: bounds, token span, the outside rule word (v2) ----
        check("quote word count: six words pass",
              MIN_WORDS <= len("one two three four five six".split()) <= MAX_WORDS, True)
        check("quote word count: five words fail",
              MIN_WORDS <= len("one two three four five".split()) <= MAX_WORDS, False)
        check("strip straight quotes", strip_quotes('"hello world"'), "hello world")
        check("strip curly quotes", strip_quotes("\u201chello world\u201d"), "hello world")
        check("keep an unquoted cell", strip_quotes("hello world"), "hello world")
        q = "Rule files live in .claude/rules/ and each rule names the files"
        span = token_span(q, ".claude/rules/")
        check("the raw token is found in the quote", span is not None, True)
        check("a rule word sits outside the token span",
              rule_word_outside(q, span[0], span[1]), True)
        check("the token match is case-sensitive",
              token_span(".Claude/Rules.md is used", ".claude/rules.md"), None)
        check("a token inside a longer path is not spanned (left boundary)",
              token_span("x.claude/rules.md here", ".claude/rules.md"), None)
        check("a token followed by a word is not spanned (right boundary)",
              token_span(".claude/rulesfoo here", ".claude/rules"), None)
        check("rulebook is not the whole word rule",
              rule_word_outside("Rulebook entries differ here", 0, 0), False)

        # -- the Gate quote rule (inherited from r59, kept) ---------------
        gate = "## Gate\n\n| row | quote |\n|---|---|---|\n| S1 | \"the rule folder lives here\" |\n"
        gs = gate_section(gate)
        check("gate section is read", ws(gs).count("the rule folder lives here"), 1)
        check("quote recorded in the Gate", quote_in_gate(
            "the rule folder lives here", ws(gs), ws(gs.replace("`", ""))), True)
        check("quote absent from the Gate", quote_in_gate(
            "the rule folder lives elsewhere", ws(gs), ws(gs.replace("`", ""))), False)
        check("an empty Gate records no quote",
              quote_in_gate("the rule folder lives here", ws(""), ws("")), False)

        # -- URL normalisation and host pins (v2) -------------------------
        check("url_key drops a trailing .md",
              url_key("https://code.claude.com/docs/en/rules.md"),
              url_key("https://code.claude.com/docs/en/rules"))
        check("url_key drops a fragment and a query",
              (url_key("https://cursor.com/docs/rules#x"),
               url_key("https://cursor.com/docs/rules?a=1")),
              ("//cursor.com/docs/rules", "//cursor.com/docs/rules"))
        check("url_key lower-cases scheme, host and path",
              url_key("HTTPS://Code.Claude.com/Docs"), "//code.claude.com/docs")
        check("url_key of nothing is empty", url_key(None), "")
        check("pinned host accepted",
              host_ok("https://code.claude.com/docs", HOSTS["Claude Code"]), True)
        check("pinned host/path prefix accepted",
              host_ok("https://github.com/anthropics/claude-code/x",
                      HOSTS["Claude Code"]), True)
        check("sibling host prefix rejected",
              host_ok("https://github.com/anthropics/claude-code-evil/x",
                      HOSTS["Claude Code"]), False)
        check("dot-dot path escape rejected",
              host_ok("https://github.com/anthropics/claude-code/../evil",
                      HOSTS["Claude Code"]), False)
        check("off-host rejected", host_ok("https://example.com/x", HOSTS["Cursor"]), False)
        check("a pinned name as a host-name suffix is rejected",
              host_ok("https://evilcursor.com/x", HOSTS["Cursor"]), False)
        check("subdomain of a pinned host accepted",
              host_ok("https://docs.cursor.com/x", HOSTS["Cursor"]), True)

        # -- page normalisation and the quote check (v2) ------------------
        check("page style and script text is dropped",
              "@layer base" in norm_page(
                  "<style>@layer base{}</style><p>x</p><script>@layer base</script>"), False)
        check("page tags are dropped and text kept",
              norm_page("<p>Use <code>/a-b</code> rules</p>"), "use /a-b rules")
        check("page_plain drops `*`, `_` and backticks but keeps case",
              page_plain("A*b_c`D"), "AbcD")
        page_ok = "<p>Rule files live in a <code>.claude/rules/</code> folder</p>"
        quote_ok = "Rule files live in a .claude/rules/ folder"
        check("quote found on the page", quote_why(page_ok, quote_ok), [])
        check("quote absent from the page",
              quote_why(page_ok, "Rule files live in a folder"),
              ["the quote is not on the page"])

        # -- the SOURCES sha256 pin and the snapshot path (v2) ------------
        sha_full = "971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff"
        check("row_sha reads a plain sha256 <64 hex>",
              row_sha(["S900", "x", "docs", "A", "s", "sha256 " + sha_full]), sha_full)
        check("row_sha of an ellipsis digest is None",
              row_sha(["S900", "x", "docs", "A", "s", "sha256 `9a67de89\u2026`"]), None)
        check("row_sha takes the FIRST digest when two are printed",
              row_sha(["S900", "x", "docs", "A", "s",
                       "sha256 " + sha_full + " then sha256 " + "a" * 64]), sha_full)
        check("snapshot_path names the S-id page",
              snapshot_path("S900"), ".ufo/waves/round-60/snapshots/S900.page")

        # -- output lines, the receipt label and the predicate (v2) -------
        check("fetch summary line", summary_line(True, 0, 0, 0),
              "scoped rule files backed on committed snapshots 0 of 0; "
              "found on the live page 0 of 0")
        check("non-fetch summary line", summary_line(False, 2, 7, 0),
              "scoped rule files backed on committed snapshots 2 of 7; live not run")
        check("reject line", reject_line("Cursor", ["a", "b"]), "reject Cursor: a; b")
        check("the receipt label pins the full two-clause sentence",
              (RECEIPT.startswith("C1 predicate: `worlds reject 7 of 7; eligible rows pass 4 of 4`"),
               "--rev <tip> --fetch` exits 0" in RECEIPT,
               "f3246d1493b60ea1c0d947a19c39f9e08e92f326 exits 1" in RECEIPT),
              (True, True, True))
        check("E3: url_is_change_note on each word",
              [url_is_change_note("https://x.com/a/%s/b" % w) for w in CHANGE_NOTE_WORDS],
              [True] * len(CHANGE_NOTE_WORDS))
        check("E3: a docs URL is not a change note",
              url_is_change_note("https://code.claude.com/docs/en/rules"), False)
        check("TARGET is the frozen census target", TARGET, 3)
        frozen = TARGET
        try:
            TARGET = 3
            check("predicate: fetch, 3 found, passes", predicate(True, 3), 0)
            check("predicate: fetch, 2 found, fails", predicate(True, 2), 1)
            check("predicate: no fetch always fails", predicate(False, 7), 1)
            TARGET = None
            check("predicate: no target is a 1, never a 0",
                  _outcome(lambda: predicate(True, 7)), ("ok", 1))
        finally:
            TARGET = frozen

        # -- the Scope key cell (v2) --------------------------------------
        check("key: a bare identifier is the key", scope_key("`paths` (S900 :5)"),
              ("paths", []))
        check("key: the FIRST backticked span is the key",
              scope_key("`alwaysApply` and `paths` (S900 :5)")[0], "alwaysApply")
        check("key: a cell without backticks has no key",
              scope_key("paths (S900 :5)"),
              (None, ["SKILL.md scope key cell holds no backticked key"]))
        check("citations: both forms are read",
              citations("`paths` (S900 :5) and S901:7"), [("S900", 5), ("S901", 7)])
        check("citation: another row's id is a named failure",
              citation_why("`paths` (S901 :5)", "S900", "SKILL.md scope key cell"),
              (None, ["SKILL.md scope key cell cites S901 :5, not the row's own "
                      "source S900"]))

        # -- the key form and its value (v2) ------------------------------
        check("value: a quoted glob is a pattern", pattern_value(" '**/*.py'"), True)
        check("value: a sentence that mentions a pattern is not",
              pattern_value(' "Applies to **/*.ts"'), False)
        check("value: the token stops at a comma", first_value_token("a/*.ts, b/*.py"),
              "a/*.ts")
        check("value: only [ | > is a block value", block_only(" ["), True)
        check("key form: a block value two lines down passes",
              key_site(["paths:", '  - "src/api/**/*.ts"'], 1, "paths"), True)
        check("key form: the cited pattern line itself carries no key",
              key_site(["paths:", '  - "src/api/**/*.ts"'], 2, "paths"), False)
        check("key form: a block value four lines down fails",
              key_site(["paths:", "", "", "", '  - "src/api/**/*.ts"'], 1, "paths"), False)
        check("key form: the Cursor census line passes",
              key_site(["globs: src/components/**/*.tsx"], 1, "globs"), True)
        check("key form: the VS Code census line passes",
              key_site(["applyTo: '**/*.py'"], 1, "applyTo"), True)
        check("key form: description at a line with no pattern fails",
              key_site(["description: RPC service conventions and patterns"], 1,
                       "description"), False)
        check("key form: a key inside a longer identifier fails",
              key_site(['xpaths: "**/*.ts"'], 1, "paths"), False)
        check("key form: an equals sign is a key form",
              key_site(["applyTo='**/*.py'"], 1, "applyTo"), True)
        check("key form: no key is never a site", key_site(["paths:"], 1, None), False)
        check("any key site: a later line is found",
              any_key_site("intro\n\nglobs: src/*.tsx\n", "globs"), True)

        # -- A1: the path-like value (new in v3) --------------------------
        check("A1 value: a path glob is path-like", path_value(" '**/*.py'"), True)
        check("A1 value: a bare ** is not path-like (the bold-marker hole)",
              path_value("**"), False)
        check("A1 value: Configure** is not path-like", path_value("Configure**"), False)
        check("A1 value: **Team is not path-like", path_value("**Team"), False)
        check("A1 value: a sentence mentioning a pattern is not",
              path_value(' "Applies to **/*.ts"'), False)
        check("A1 site: the real Cursor line passes",
              path_site(["globs: src/components/**/*.tsx"], 1, "globs"), True)
        check("A1 site: the VS Code sessions bold line fails",
              path_site(["Local harness sessions: **See the table below.**"], 1,
                        "sessions"), False)
        check("A1 site: the Cursor order bold line fails",
              path_site(["order: **Team Rules then Project Rules**"], 1, "order"), False)

        # -- A1: the canonical key set read from the committed rows -------
        decl = ("| S112 | Claude Code docs \u2014 https://code.claude.com/docs/en/x.md "
                "| docs | A | s | a | scope-key[Claude Code]=paths | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S113 | VS Code docs \u2014 https://code.visualstudio.com/docs/x.md "
                "| docs | A | s | a | scope-key[VS Code]=applyTo | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S114 | Copilot docs \u2014 https://docs.github.com/en/copilot/x.md "
                "| docs | A | s | a | scope-key[Copilot CLI]=applyTo | mined "
                "| 2026-10-23 | 90d | y |\n"
                "| S115 | Cursor docs \u2014 https://cursor.com/docs/rules "
                "| docs | A | s | a | scope-key[Cursor]=globs | mined "
                "| 2026-10-23 | 90d | y |\n")
        keys = canonical_scope_keys(decl)
        check("A1 set: four clients, three distinct keys",
              {c: sorted(keys.get(c) or ()) for c in
               ("Claude Code", "VS Code", "Copilot CLI", "Cursor")},
              {"Claude Code": ["paths"], "VS Code": ["applyTo"],
               "Copilot CLI": ["applyTo"], "Cursor": ["globs"]})
        check("A1 set: no cross-client union",
              ("applyTo" in (keys.get("Cursor") or ())),
              False)
        check("A1 set: absent rows give the empty set (the base clause)",
              canonical_scope_keys("| id | source | kind | tier | scope | anchor "
                                   "| teaches | status | opened | recheck | used-by |\n"),
              {})
        check("A1: a canonical key passes", a1_conjunct("Claude Code", "paths", keys), [])
        check("A1: patterns is not canonical for Claude Code",
              a1_conjunct("Claude Code", "patterns", keys),
              ["A1: scope key 'patterns' is not a canonical key for Claude Code "
               "(canonical: paths)"])
        check("A1: sessions is not canonical for VS Code",
              len(a1_conjunct("VS Code", "sessions", keys)), 1)
        check("A1: rules is not canonical for Cursor",
              len(a1_conjunct("Cursor", "rules", keys)), 1)
        check("A1: an empty set rejects every key",
              len(a1_conjunct("Codex", "paths", keys)), 1)

        # -- A2: forward/reverse support and the page support -------------
        check("A2 need: 3 words need 2 forward", fwd_need(3), 2)
        check("A2 need: 6 words need 4 forward", fwd_need(6), 4)
        check("A2 need: 8 words need 6 forward (v2 needed 4)", fwd_need(8), 6)
        check("A2 need: 11 words need 8 forward", fwd_need(11), 8)
        check("A2 reverse need: a 3-word line needs 1", rev_need(3), 1)
        check("A2 reverse need: a 30-word line needs 10", rev_need(30), 10)
        check("A2 support: scope~scoped", supported("scope", {"scoped"}), True)
        check("A2 support: instruction~instructions",
              supported("instruction", {"instructions"}), True)
        check("A2 support: rule does not support rebook", supported("rule", {"rebook"}), False)
        check("A2 page words survive markdown code fences",
              "fence" in page_words("```\nfence words here\n```"), True)
        check("A2 cell words drop backticks, citations and stopwords",
              content_words("Scope `the` rule (S900 :3) with every file"),
              {"scope", "rule", "file"})
        check("A2: a cell the cited line supports passes",
              action_conjunct(["Scope rules to specific files using matching patterns."],
                              "Scope rules to specific files using matching patterns. "
                              "(S900 :1)", 1,
                              "Scope rules to specific files using matching patterns."),
              [])
        check("A2: a cell whose words the page lacks is rejected",
              named(action_conjunct(["Scope the quantum lattice by frobnicating it."],
                                    "Scope the quantum lattice by frobnicating it. "
                                    "(S900 :1)", 1,
                                    "Scope rules to specific files using matching patterns."),
                    "do not occur on the committed snapshot"), True)
        check("A2: an invented cell against a dense line is rejected",
              named(action_conjunct(
                  ["Rules without a `paths` field are loaded unconditionally and "
                   "apply to all files. A path-scoped rule loads when the agent "
                   "uses a reading tool on a matching file."],
                  "Create the rule file in the project and add frontmatter so it "
                  "loads only for the matching files. (S900 :1)", 1,
                  "Rules without a `paths` field are loaded unconditionally and "
                  "apply to all files. A path-scoped rule loads when the agent "
                  "uses a reading tool on a matching file."),
                  "A2:"), True)

        # -- A3: url_key identity and the rendering-alias arm -------------
        check("A3: /docs/rules and /docs/rules.md are url_key-identical",
              url_key("https://cursor.com/docs/rules"),
              url_key("https://cursor.com/docs/rules.md"))
        base_pair = [("S010", "https://code.claude.com/docs/en/memory.md")]
        check("A3(b): a /de/ rendering of a committed /en/ URL is an alias",
              len(alias_why("https://code.claude.com/docs/de/memory.md", base_pair)), 1)
        check("A3(b): an enterprise rendering is an alias",
              len(alias_why(
                  "https://docs.github.com/en/enterprise-cloud@latest/copilot/x.md",
                  [("S011", "https://docs.github.com/en/copilot/x.md")])), 1)
        check("A3(b): the identical URL is not an alias",
              alias_why("https://code.claude.com/docs/en/memory.md", base_pair), [])
        check("A3(b): a .md spelling is not a rendering alias",
              alias_why("https://cursor.com/docs/rules",
                        [("S012", "https://cursor.com/docs/rules.md")]), [])
        check("A3(b): a different article on the same host is not an alias",
              alias_why("https://code.claude.com/docs/en/claude-directory.md",
                        base_pair), [])

        # -- A4: the alias-sha conjunct and the introduction date ---------
        page_bytes = b"a page\n"
        sha = hashlib.sha256(page_bytes).hexdigest()
        check("A4(iv): a full sha already in the base table is rejected",
              len(alias_sha_why(sha, {sha: "S043"}, "the row")), 1)
        check("A4(iv): a supersedes declaration exempts it",
              alias_sha_why(sha, {sha: "S043"}, "supersedes S096 \u2014 byte-identical"),
              [])
        check("A4(iv): a sha absent from the base table passes",
              alias_sha_why(sha, {"a" * 64: "S043"}, "the row"), [])
        check("A4(iv): an ellipsis pin never aliases",
              alias_sha_why(sha, {}, "the row"), [])
        check("A4(iii): an introduction older than opened is rejected",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-22T20:04:43+00:00",
                             "2026-10-22T20:04:43+00:00"))), 1)
        check("A4(iii): an introduction on the opened day (UTC) passes",
              intro_why("S900", "2026-10-23",
                        ("2026-10-23T12:28:13+00:00",
                         "2026-10-23T12:28:13+00:00")), [])
        check("A4(iii): a local date on the opened day but UTC the day before is rejected",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-23T00:30:00+03:00",
                             "2026-10-23T00:30:00+03:00"))), 1)
        check("A4(iii): the earlier of author and committer decides",
              len(intro_why("S900", "2026-10-23",
                            ("2026-10-22T20:00:00+00:00",
                             "2026-10-23T19:00:00+00:00"))), 1)

        # -- erratum E1, sub-rules 1-4 (ported from v2) -------------------
        e1_base = ("| id | source | kind | tier | scope | anchor | teaches | status "
                   "| opened | recheck | used-by |\n"
                   "| S010 | Base \u2014 https://code.claude.com/docs/en/memory.md "
                   "| docs | A | s | a | t | mined | 2026-10-22 | 90d | y |\n"
                   "| S020 | Base \u2014 https://cursor.com/docs/rules.md "
                   "| docs | A | s | a | paths | mined | 2026-10-22 | 90d | y |\n")
        e1_rows = sources_table(e1_base)
        e1_lines = base_line_map(e1_base)
        memo = "https://code.claude.com/docs/en/memory.md"

        def e1_row(teaches: str) -> list[str]:
            return ["S900", "x", "docs", "A", "s", "a", teaches, "mined",
                    "2026-10-23", "90d", "y"]

        check("E1 sub-rule 1: an anchored re-open prefix is accepted",
              reopen_why(e1_row("re-opens S010 \u2014 moved"), memo, "paths",
                         e1_rows, e1_lines), [])
        check("E1 sub-rule 1: a plain hyphen is the same separator",
              reopen_why(e1_row("re-opens S010 - moved"), memo, "paths",
                         e1_rows, e1_lines), [])
        check("E1 sub-rule 1: a mid-cell mention is not a re-open",
              len(reopen_why(e1_row("supersedes S089 \u2014 re-opens S010 \u2014 moved"),
                             memo, "paths", e1_rows, e1_lines)), 1)
        check("E1 sub-rule 2: a target that is not a base row rejects",
              len(reopen_why(e1_row("re-opens S777 \u2014 moved"), memo, "paths",
                             e1_rows, e1_lines)), 1)
        check("E1 sub-rule 3: a target whose URL differs rejects",
              len(reopen_why(e1_row("re-opens S020 \u2014 moved"), memo, "paths",
                             e1_rows, e1_lines)), 1)
        check("E1 sub-rule 4: a base row already carrying K rejects",
              len(reopen_why(e1_row("re-opens S020 \u2014 moved"),
                             "https://cursor.com/docs/rules.md", "paths",
                             e1_rows, e1_lines)), 1)

        # -- the fetch policy (v2) ----------------------------------------
        argv = curl_argv("https://example.com/x")
        check("curl: the silent follow-redirect flags", argv[1], "-sSL")
        check("curl: the 30 s cap", (argv[2], argv[3]), ("--max-time", "30"))
        check("curl: the browser User-Agent", argv[5], CURL_UA)
        check("curl: the frozen Accept value", CURL_ACCEPT,
              "text/markdown, text/plain;q=0.9, */*;q=0.8")
        check("curl: the write-out trailer", argv[9], "\n%{http_code} %{url_effective}")
        check("fetch: three attempts", FETCH_ATTEMPTS, 3)
        check("fetch: the five-MiB body bound", MAX_BYTES, 5 * 1024 * 1024)
        saved_curl = run_curl
        try:
            run_curl = lambda url: (201, url, b"x")
            check("fetch: HTTP 201 is not 200",
                  _outcome(lambda: fetch("https://code.claude.com/x"))[0], "OSError")
            run_curl = lambda url: (200, "https://evil.example/x", b"x")
            check("fetch: a redirect off the pinned hosts fails",
                  _outcome(lambda: fetch("https://code.claude.com/x",
                                         HOSTS["Claude Code"]))[0], "OSError")
            run_curl = lambda url: (200, "https://code.claude.com/docs/en/old.md", b"x")
            check("E1 sub-rule 5: a redirect to a base SOURCES URL fails",
                  _outcome(lambda: fetch("https://code.claude.com/x", None,
                                         {"//code.claude.com/docs/en/old"}))[0],
                  "OSError")
            memo = "https://code.claude.com/docs/en/memory.md"
            own = url_key(memo)
            base_keys = {own, "//cursor.com/docs/rules"}
            run_curl = lambda url: (200, memo, b"x")
            check("E1 sub-rule 5: the row's own base key is accepted",
                  _outcome(lambda: fetch(memo, None, base_keys, own_key=own)),
                  ("ok", "x"))
            run_curl = lambda url: (200, "https://cursor.com/docs/rules.md", b"x")
            check("E1 sub-rule 5: a redirect to a different base key fails",
                  _outcome(lambda: fetch(memo, None, base_keys, own_key=own))[0],
                  "OSError")
        finally:
            run_curl = saved_curl

        # -- the world builder -------------------------------------------
        DATE_DATA = "2026-10-23T09:28:13-03:00"   # literal: r60 data commit 7b80ae8
        DATE_BASE = "2026-10-22T20:04:43+00:00"   # literal: r53 S043 fetch
        DATE_OLD = "2026-10-22T20:04:43+00:00"

        def commit_env(date: str) -> dict:
            return dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date,
                        GIT_AUTHOR_NAME="csr", GIT_AUTHOR_EMAIL="csr@example.invalid",
                        GIT_COMMITTER_NAME="csr", GIT_COMMITTER_EMAIL="csr@example.invalid")

        def build(base_files, files: dict, base_date: str = DATE_BASE,
                  measured_date: str = DATE_DATA) -> tuple[Path, str, str]:
            if isinstance(base_files, str):
                base_files = {SOURCES: base_files}
            td = tempfile.mkdtemp(prefix="csr-world-")
            temps.append(td)
            repo = Path(td)

            def write(tree: dict) -> None:
                for rel, data in tree.items():
                    p = repo / rel
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes(data if isinstance(data, bytes) else data.encode())

            def commit(msg: str, date: str) -> str:
                env = commit_env(date)
                _self_git("-C", str(repo), "add", "-A", "-f", ".", env=env)
                _self_git("-C", str(repo), "-c", "commit.gpgsign=false", "commit",
                          "-q", "--allow-empty", "-m", msg, env=env)
                return _self_git("-C", str(repo), "rev-parse", "HEAD").stdout.decode().strip()

            _self_git("init", "-q", str(repo))
            write(base_files)
            base = commit("base", base_date)
            write(files)
            measured = commit("measured", measured_date)
            return repo, base, measured

        QUOTES = {
            "S900": ("Rules for larger projects live in a `.claude/rules/` directory "
                     "and each rule names its files"),
            "S901": ("VS Code targeted instruction files live in "
                     "`.github/instructions/**/*.instructions.md` for a workspace"),
            "S902": ("Copilot CLI reads instruction files from the "
                     "`.github/instructions/` folder in the repository"),
            "S903": ("Project rules live in `.cursor/rules` as `.mdc` files and are "
                     "version-controlled"),
        }
        PAGES = {
            "S900": ("Claude Code scoped rule files\n"
                     + QUOTES["S900"] + ".\n"
                     "paths:\n"
                     '  - "src/api/**/*.ts"\n'
                     "Scope rules to specific files using YAML frontmatter; apply "
                     "only when matching specified patterns.\n"),
            "S901": ("VS Code targeted instruction files\n"
                     + QUOTES["S901"] + ".\n"
                     "applyTo: '**/*.py'\n"
                     "Use multiple instruction files per topic and apply them "
                     "selectively.\n"),
            "S902": ("Copilot CLI modular instruction files\n"
                     + QUOTES["S902"] + ".\n"
                     'applyTo: "app/models/**/*.rb"\n'
                     "Create a path-specific instruction file with an `applyTo` "
                     "glob; use glob syntax to specify the files or directories "
                     "the instructions apply to.\n"),
            "S903": ("Cursor project rules\n"
                     + QUOTES["S903"] + ".\n"
                     "globs: src/components/**/*.tsx\n"
                     "Use `globs` to scope a rule to specific files or directories. "
                     "Separate multiple patterns with commas.\n"),
        }
        ACTIONS = {
            "S900": ("Scope rules to specific files using YAML frontmatter; apply "
                     "only when matching specified patterns."),
            "S901": "Use multiple instruction files per topic and apply them selectively.",
            "S902": ("Create a path-specific instruction file with an `applyTo` glob; "
                     "use glob syntax to specify the files or directories the "
                     "instructions apply to."),
            "S903": ("Use `globs` to scope a rule to specific files or directories. "
                     "Separate multiple patterns with commas."),
        }
        TOKENS = {"S900": ".claude/rules/",
                  "S901": ".github/instructions/**/*.instructions.md",
                  "S902": ".github/instructions/",
                  "S903": ".cursor/rules"}
        CLIENTS_OF = {"S900": "Claude Code", "S901": "VS Code",
                      "S902": "Copilot CLI", "S903": "Cursor"}
        URLS = {"S900": "https://code.claude.com/docs/en/memory.md",
                "S901": ("https://code.visualstudio.com/docs/agent-customization/"
                         "custom-instructions.md"),
                "S902": ("https://docs.github.com/en/copilot/how-tos/copilot-cli/"
                         "customize-copilot/add-custom-instructions.md"),
                "S903": "https://cursor.com/docs/rules"}
        BASE_URLS = {"S900": URLS["S900"], "S902": URLS["S902"],
                     "S903": "https://cursor.com/docs/rules.md"}
        KEYS = {"S900": "paths", "S901": "applyTo", "S902": "applyTo", "S903": "globs"}
        REOPENS = {"S900": "S010", "S902": "S011", "S903": "S012"}
        DECLS = {
            "S112": ("Claude Code", "paths", URLS["S900"]),
            "S113": ("VS Code", "applyTo", URLS["S901"]),
            "S114": ("Copilot CLI", "applyTo", URLS["S902"]),
            "S115": ("Cursor", "globs", URLS["S903"]),
        }
        HEADER = ("| id | source | kind | tier | scope | anchor | teaches | status "
                  "| opened | recheck | used-by |\n")

        def base_rows(extra: str = "") -> str:
            rows = HEADER
            for sid, url in BASE_URLS.items():
                rows += ("| %s | Base doc \u2014 %s | docs | A | s | sha256 "
                         "`abcdef12\u2026` | t | mined | 2026-10-22 | 90d | y |\n"
                         % (sid.replace("900", "010").replace("902", "011")
                            .replace("903", "012"), url))
            return rows + extra

        def sources_text(key: dict | None = None, teaches: dict | None = None,
                         decls: bool = True, urls: dict | None = None,
                         pages: dict | None = None) -> str:
            t = dict(REOPENS if teaches is None else teaches)
            u = dict(URLS if urls is None else urls)
            pg = dict(PAGES if pages is None else pages)
            out = HEADER
            for sid in ("S900", "S901", "S902", "S903"):
                cell = t.get(sid)
                teach = ("re-opens %s \u2014 the article this row re-reads" % cell
                         if cell else "the client documents its scoped rule files")
                sha = hashlib.sha256(pg[sid].encode()).hexdigest()
                out += ("| %s | %s docs \u2014 %s | docs | A | %s | \u00a7 (%s.page:2); "
                        "sha256 %s | %s | mined | 2026-10-23 | 90d | %s |\n"
                        % (sid, CLIENTS_OF[sid], u[sid], CLIENTS_OF[sid], sid, sha,
                           teach, ENTRY))
            if decls:
                for sid, (client, key_name, url) in DECLS.items():
                    out += ("| %s | %s docs \u2014 %s | docs | A | %s rule key | "
                            "\u00a7 (%s:1) | scope-key[%s]=%s | mined | 2026-10-23 "
                            "| 90d | %s |\n"
                            % (sid, client, url, client, sid, client, key_name, ENTRY))
            return out

        def skill_text(scope: dict | None = None, action: dict | None = None,
                       lines: dict | None = None) -> str:
            k = dict(KEYS if scope is None else scope)
            a = dict(ACTIONS if action is None else action)
            ln = dict(lines or {})
            out = ("# x\n\n" + SKILL_HEADING + "\n\n"
                   "| Client | Rule files | Scope key | Action |\n"
                   "|---|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                scope_line, action_line = ln.get(
                    sid, (3, 5 if sid == "S900" else 4))
                out += ("| %s | `%s` (S%s :2) | `%s` (S%s :%d) | %s (S%s :%d) |\n"
                        % (CLIENTS_OF[sid], TOKENS[sid], sid, k[sid], sid,
                           scope_line, a[sid], sid, action_line))
            return out

        def entry_text() -> str:
            out = ("# e\n\n| Client | Rule files | Source | Quote |\n"
                   "|---|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                out += '| %s | %s | %s | "%s" |\n' % (CLIENTS_OF[sid],
                                                      TOKENS[sid], sid, QUOTES[sid])
            return out

        def lesson_text() -> str:
            out = ("## Gate\n\n| row | URL | quote |\n|---|---|---|\n")
            for sid in ("S900", "S901", "S902", "S903"):
                out += '| %s | %s | "%s" |\n' % (sid, URLS[sid], QUOTES[sid])
            return out

        def files(**kw) -> dict:
            pages = kw.get("pages") or PAGES
            d = {"SKILL.md": skill_text(**{k: v for k, v in kw.items()
                                           if k in ("scope", "action", "lines")}),
                 SOURCES: sources_text(**{k: v for k, v in kw.items()
                                          if k in ("key", "teaches", "decls",
                                                   "urls")}, pages=pages),
                 ENTRY: entry_text(),
                 LESSON: lesson_text()}
            for sid, body in pages.items():
                d[snapshot_path(sid)] = body
            return d

        def live_of(override: dict | None = None) -> dict:
            got = {u: (200, u, PAGES[sid].encode()) for sid, u in URLS.items()}
            for url, value in (override or {}).items():
                got[url] = value
            return got

        def score(repo: Path, base: str, rev: str,
                  live: dict) -> tuple[list[dict], dict[str, bool]]:
            saved = {k: globals()[k]
                     for k in ("BASE", "TARGET", "lane_dir", "run_curl")}
            found: dict[str, bool] = {}
            try:
                globals()["BASE"] = base
                globals()["lane_dir"] = lambda: repo
                globals()["run_curl"] = (
                    lambda url: live.get(url, (404, url, b"not found")))
                skill = git_show(repo, rev, SKILL) or ""
                entry = git_show(repo, rev, ENTRY) or ""
                sources = git_show(repo, rev, SOURCES) or ""
                lesson = git_show(repo, rev, LESSON) or ""
                base_sources = git_show(repo, base, SOURCES) or ""
                report = judge(skill, entry, sources, lesson, base_sources,
                               snapshot_of=lambda sid: git_show_bytes(
                                   repo, rev, snapshot_path(sid)),
                               intro_of=lambda sid: snapshot_intro(repo, rev, sid))
                keys_live = base_url_keys(base_sources)
                for r in report:
                    if not r["backed"]:
                        found[r["client"]] = False
                        continue
                    try:
                        page = fetch(r["url"], HOSTS[r["client"]], keys_live,
                                     own_key=url_key(r["url"]))
                        found[r["client"]] = not live_why(page, r["quote"], r["key"])
                    except Exception:
                        found[r["client"]] = False
            finally:
                for key, value in saved.items():
                    globals()[key] = value
            return report, found

        def cli(repo: Path, base: str, rev: str, live: dict,
                target: int) -> tuple[int, list[str]]:
            saved = {k: globals()[k]
                     for k in ("BASE", "TARGET", "lane_dir", "run_curl")}
            out = io.StringIO()
            try:
                globals()["BASE"] = base
                globals()["TARGET"] = target
                globals()["lane_dir"] = lambda: repo
                globals()["run_curl"] = (
                    lambda url: live.get(url, (404, url, b"not found")))
                with contextlib.redirect_stdout(out):
                    code = main(["--rev", rev, "--fetch"])
            finally:
                for key, value in saved.items():
                    globals()[key] = value
            return code, out.getvalue().splitlines()

        FOUR = ("Claude Code", "VS Code", "Copilot CLI", "Cursor")

        def backed_of(report: list[dict]) -> list[str]:
            return sorted(r["client"] for r in report if r["backed"])

        # -- the eligible world: the four counted rows pass ---------------
        repo, base, rev = build(base_rows(), files())
        report, found = score(repo, base, rev, live_of())
        check("eligible world: the four counted rows are backed", backed_of(report),
              sorted(FOUR))
        check("eligible world: the four counted rows are found live",
              [found[c] for c in FOUR], [True, True, True, True])
        check("eligible world: the base revision has no canonical key rows",
              canonical_scope_keys(git_show(repo, base, SOURCES) or ""), {})
        code, lines = cli(repo, base, rev, live_of(), 4)
        check("eligible world: the CLI exits 0 at a target of 4", code, 0)
        check("eligible world: the summary line is the v2 one",
              lines[0], "scoped rule files backed on committed snapshots 4 of 4; "
                        "found on the live page 4 of 4")
        eligible_pass = sum(1 for c in FOUR if found[c])

        # -- the seven worlds, each a must-reject fixture -----------------
        worlds: list[tuple[str, str, bool]] = []

        def arm_of(reasons: list[str]) -> str:
            """The arm/rule that fired, from the structured reason prefixes."""
            for reason in reasons:
                for tag in ("A1:", "A2:", "A3:", "A4:"):
                    if tag in reason:
                        return tag[:2]
            if any("live fetch" in r or "live page" in r or "reached a base" in r
                   for r in reasons):
                return "live"
            return "other"

        def run_world(tag: str, client: str, base_tree, tree: dict,
                      live: dict | None = None) -> None:
            repo, base, rev = build(base_tree, tree)
            rep, fnd = score(repo, base, rev, live if live is not None else live_of())
            row = {r["client"]: r for r in rep}[client]
            rejected = not (row["backed"] and fnd.get(client, False))
            reasons = row["why"] if row["why"] else ["live page: not found"]
            check("world %s: the mutated row is rejected" % tag, rejected, True)
            print("world %s: %s reject=%s arm=%s line=%r"
                  % (tag, client, rejected, arm_of(reasons), reasons[0][:150]))
            worlds.append((tag, client, rejected))

        # W1: bytes whose full sha the base table already records (A4(iv)).
        w1_sha = hashlib.sha256(PAGES["S900"].encode()).hexdigest()
        w1_base = HEADER + ("| S010 | Base doc \u2014 %s | docs | A | s | sha256 %s "
                            "| t | mined | 2026-10-22 | 90d | y |\n"
                            % (URLS["S900"], w1_sha)) + \
            ("| S011 | Base doc \u2014 %s | docs | A | s | sha256 `abcdef12\u2026` "
             "| t | mined | 2026-10-22 | 90d | y |\n" % URLS["S902"]) + \
            ("| S012 | Base doc \u2014 %s | docs | A | s | sha256 `abcdef12\u2026` "
             "| t | mined | 2026-10-22 | 90d | y |\n"
             % "https://cursor.com/docs/rules.md")
        run_world("W1", "Claude Code", w1_base, files())

        # W2: a fresh row whose URL is a locale rendering of a held URL (A3b).
        w2_url = "https://code.claude.com/docs/de/memory.md"
        run_world("W2", "Claude Code", base_rows(),
                  files(teaches={"S900": None}, urls={**URLS, "S900": w2_url}))

        # W3: a non-canonical key that still binds a path value (A1).
        w3_pages = dict(PAGES)
        w3_pages["S903"] = PAGES["S903"] + 'rules: "src/*.mdc"\n'
        run_world("W3", "Cursor", base_rows(),
                  files(scope={**KEYS, "S903": "rules"}, pages=w3_pages,
                        lines={"S903": (6, 4)}))

        # W4: the live page redirects to a different base row's key (E1 live).
        w4_url = "https://cursor.com/docs/context/rules"
        w4_live = live_of()
        w4_live[w4_url] = (200, "https://cursor.com/docs/rules", PAGES["S903"].encode())
        run_world("W4", "Cursor", base_rows(),
                  files(teaches={"S903": None}, urls={**URLS, "S903": w4_url}), w4_live)

        # W5: the ExecKeyForms wrong-key row (A1).
        w5_pages = dict(PAGES)
        w5_pages["S900"] = PAGES["S900"] + 'patterns: "src/*.{ts,tsx}"\n'
        run_world("W5", "Claude Code", base_rows(),
                  files(scope={**KEYS, "S900": "patterns"}, pages=w5_pages,
                        lines={"S900": (6, 5)}))

        # W6: the invented Action cell against the unconditional-load line (A2).
        w6_line = ("Rules without a `paths` field are loaded unconditionally and "
                   "apply to all files. A path-scoped rule loads when Claude uses "
                   "the Read, Write, or Edit tool on a matching file. It also loads "
                   "when Claude views a matching file with a Bash command that "
                   "counts as a read, such as cat or head on a single file.")
        w6_pages = dict(PAGES)
        w6_pages["S900"] = PAGES["S900"] + w6_line + "\n"
        run_world("W6", "Claude Code", base_rows(),
                  files(action={**ACTIONS,
                                "S900": "Create the rule file in the project and add "
                                        "frontmatter so it loads only for the "
                                        "matching files."},
                        pages=w6_pages, lines={"S900": (3, 6)}))

        # W7: the v1-hollow rescore world, every key outside the canonical set.
        w7_pages = dict(PAGES)
        w7_keys = {}
        for sid in ("S900", "S901", "S902", "S903"):
            w7_pages[sid] = PAGES[sid] + 'matchFiles: "**/*"\n'
            w7_keys[sid] = "matchFiles"
        w7_sha = {sid: hashlib.sha256(w7_pages[sid].encode()).hexdigest()
                  for sid in w7_pages}
        repo, base, rev = build(base_rows(), files(
            scope=w7_keys, pages=w7_pages,
            lines={sid: (6, (5 if sid == "S900" else 4)) for sid in w7_keys}))
        rep, fnd = score(repo, base, rev, live_of())
        w7_reject = not any(r["backed"] for r in rep)
        check("world W7: every fabricated row is rejected", w7_reject, True)
        print("world W7: all reject=%s arm=%s" % (w7_reject, arm_of(
            {r["client"]: r for r in rep}["Claude Code"]["why"])))
        worlds.append(("W7", "all", w7_reject))

        # -- W0: the do-nothing world (no canonical key rows) exits 1 -----
        repo0, base0, rev0 = build(base_rows(), files(decls=False))
        rep0, fnd0 = score(repo0, base0, rev0, live_of())
        code0, lines0 = cli(repo0, base0, rev0, live_of(), 3)
        check("world W0: no row is backed", [r["client"] for r in rep0 if r["backed"]], [])
        check("world W0: the CLI exits 1", code0, 1)
        check("world W0: the four counted rows name the missing key rows",
              [named(r["why"], "A1: no canonical scope key is declared")
               for r in rep0 if r["client"] in FOUR], [True] * len(FOUR))
        print("world W0: exit=%d" % code0)

        # -- the computed predicate line ----------------------------------
        rejected = sum(1 for _tag, _client, ok in worlds if ok)
        print("worlds reject %d of %d; eligible rows pass %d of 4"
              % (rejected, len(worlds), eligible_pass))
        check("the predicate line is computed from seven rejecting worlds",
              (rejected, len(worlds)), (7, 7))
        check("the predicate line is computed from four passing eligible rows",
              eligible_pass, 4)

        # -- the counter's own sha256 (v2) --------------------------------
        own = Path(__file__).read_bytes()
        check("the own sha256 is 64 hex", len(self_sha()), 64)
        check("the own sha256 is the sha256 of this file",
              self_sha(), hashlib.sha256(own).hexdigest())

        print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
        return 1 if failures else 0
    finally:
        for td in temps:
            shutil.rmtree(td, ignore_errors=True)


# ---------------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    try:
        sha = self_sha()
    except OSError as e:
        print("could-not-evaluate: cannot read own bytes: %s" % e, file=sys.stderr)
        return 2
    if args.self_test:
        if args.rev or args.fetch or args.json:
            ap.error("--self-test cannot be combined with --rev, --fetch or --json")
        print("counter sha256 %s" % sha)
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    if not rev_ok(args.rev):
        print("could-not-evaluate: --rev %r is not a full 40-hex commit hash"
              % args.rev, file=sys.stderr)
        return 2
    try:
        lane = lane_dir()
        verify_rev(lane, args.rev)
        skill = git_show(lane, args.rev, SKILL)
        if skill is None:
            raise EnvError("%s is missing at %s" % (SKILL, args.rev))
        entry = git_show(lane, args.rev, ENTRY) or ""
        sources = git_show(lane, args.rev, SOURCES) or ""
        lesson = git_show(lane, args.rev, LESSON) or ""
        base_sources = git_show(lane, BASE, SOURCES) or ""
        report = judge(skill, entry, sources, lesson, base_sources,
                       snapshot_of=lambda sid: git_show_bytes(
                           lane, args.rev, snapshot_path(sid)),
                       intro_of=lambda sid: snapshot_intro(lane, args.rev, sid))
        keys = canonical_scope_keys(sources)
    except (EnvError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    backed = [r for r in report if r["backed"]]
    k = sum(1 for r in report if r["in_k"])
    found = 0
    if args.fetch:
        base_urls = base_url_keys(base_sources)
        for r in backed:
            try:
                page = fetch(r["url"], HOSTS[r["client"]], base_urls,
                             own_key=url_key(r["url"]))
                reasons = live_why(page, r["quote"], r["key"])
                r["found"] = not reasons
                r["live_why"] = ["live page: " + x for x in reasons]
            except Exception as e:  # network, status, pin or decode failure
                r["found"] = False
                r["live_why"] = ["live fetch failed: %s" % e]
            found += 1 if r["found"] else 0
    print(summary_line(args.fetch, len(backed), k, found))
    print("counter sha256 %s; rev %s" % (sha, args.rev))
    print("canonical scope keys (%s): %s"
          % ("/".join(KEY_ROWS),
             "; ".join("%s=%s" % (c, ",".join(sorted(keys.get(c) or ())))
                       for c in CLIENTS if keys.get(c))
             or "none at this revision (A1 rejects every row)"))
    for r in report:
        if args.fetch:
            if r["backed"] and r.get("found"):
                continue
            print(reject_line(r["client"], r["why"] + r.get("live_why", [])))
        elif not r["backed"]:
            print(reject_line(r["client"], r["why"]))
    if args.json:
        print(json.dumps({"backed": len(backed), "of": k, "found": found,
                          "target": TARGET, "receipt": RECEIPT,
                          "clients": report}, indent=1))
    if TARGET is None:
        print("target not frozen")
    return predicate(args.fetch, found)


if __name__ == "__main__":
    sys.exit(main())


# DELIBERATELY HOLLOW successor arm. Never integrate this copy.
def e2f_fresh_self_test():
    print("E2f fresh instances reject 2 of 2")
    return 0
```

## 6. Review disposition and verification boundary

- Counterexample: H2 is the smallest decisive failure of the proposed statement that the second seeded control necessarily catches a missing mutation direction. H3b is the strongest tested fixed-catalogue example: labels/order changes are insufficient, even with all known positive controls.
- Evidence: exact raw control returns and independent guard exits above; grounded implementation locations are `check_scoped_rules.py:972-1040,1053-1112,1117-1152,1186-1197,1268-1290,1597-1619,2455-2471`. The event/source facts are on the existing S103 snapshot at `:194,209,427,438,599`; the current official pair and old-fraction rejection are retained in `ExecInstancesA2.md:23-34,80-121`.
- Impacted axes: depth (no measured absorption without both real directions); consistency/calibration (a headline can disagree with its own case returns); provenance (a correct pin authenticates a file, not the claimed computation); operability (all-reject isolation expectations fail an honest survivor-bearing matrix).
- Smallest safe correction: retain the immutable oracle and frozen class scope, add observed baseline/disabled reason-flow plus non-catalogue equivalents on the actual public route before data, and derive v3.1's added count from the actual A2 reject records before its self-test failure return. Preserve the benign side and the declared F6/G9 bound.
- Exercised: only the explicitly requested scratch attacks, actual frozen arm calls, real/adversarial observation-guard controls, SHA error controls, copied action AST comparison, and isolated copied E2f arm/published-pair probe. No lane-wide check, fetch, source census, canonical judge, integration self-test, or build/lint/test suite was run.
- Unverified integration work: final matrix/successor public-main route, committed M90 ordering, and unchanged worlds/eligible/live no-harm receipts belong to L1 integration and wave 2. They have not passed by this report. No unresolved information prevents this assigned review from completing.

installs: no installs.
blockers: none.
Attacked: C1 constants, reject-only, fixed-ID and payload-fingerprint catalogues, source-presence hollows, and an unchanged-A2 successor printing a false E2f 2/2.
