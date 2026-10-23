# CriticTiming — controls-before-data chronology

Seat: `kotoba-r61-wave-CriticTiming-3`. Review date: 2026-10-23 UTC.
Scope: read-only chronology attack; this report is the only file written. No verifier, judge, runtime, fetch, git/jj mutation, or dispatch was invoked. All repository paths below are relative to `/home/vgpnk/Projects/shokunin/kotoba-shokunin` unless an absolute command is shown.

Axes: **operability** primarily; **calibration** for C2/R-f's honest meaning; **depth** for the evidentiary validity of measured C1. No admission or round verdict is issued here.

## Counterexample and finding

**The shortcut is commit-order laundering:** acquire or measure C1 data while its controls are unfinished, then commit the control paperwork before the data paperwork and cite a green ancestry check as proof that controls preceded data. That reproduces M90 even when the final DAG looks tidy. A same-commit variant is weaker still: `git merge-base --is-ancestor X X` succeeds, although nothing strictly preceded anything.

I exercised that same-commit variant against the real freeze commit; Git returned `exit 0` (full command/output below). The frozen C2 checker does not distinguish it: `verifiers/check_routed_repairs.py:104-110` tests only whether the ancestry blob contains `merge-base --is-ancestor` and `exit 0`. **[INFERENCE from the inspected Boolean expression, not a checker run]** A receipt documenting that reflexive invocation satisfies R-f's text test, without proving strict order or execution order. The checker explicitly disclaims substantive honesty at lines 34-37; leave its frozen definition unchanged rather than retrofitting a second declared measurement.

There are two different boundaries:

1. The round-61 plan's C1 boundary is committed world receipts **before any `--fetch` data measurement** (`plans/round-61.md:55-59`). A single integrating L1 can still enforce that boundary with the commit sequence below.
2. The routed M90 boundary is stronger: receipts before probing, controls complete **before data-seat dispatch**, and cancellation with a receipt (`corpus/lessons/round-60-verifier-spotcheck.md:134-139`). A commit DAG alone cannot establish this event history, and later commit splitting cannot repair a past violation.

Do not silently replace boundary 2 with boundary 1 and label the result “M90 fixed.” This is a substantive calibration issue, not merely a preferred ordering of bookkeeping files.

## Local evidence

| Evidence | What it establishes |
|---|---|
| `plans/round-61.md:21-59` | The fixed A1-A4 classes, seven worlds, four eligible positives, exact predicate, and pre-fetch receipt requirement. |
| `plans/round-61.md:61-74` | C2's six repairs; its base control precedes repairs; R-f is a receipt about control/data ancestry. |
| `plans/round-61.md:108-112` | The broad integration list groups counter, fixtures, receipts, rows, entries, lesson and accounting. It does not itself supply the required internal barriers. |
| `corpus/lessons/round-60.md:62` | M90: semantic control seats had no pre-data receipts, and the build wave was dispatched while v2 controls were still scoring. Its fix requires a first receipt before optional probing. |
| `corpus/lessons/round-60-verifier-spotcheck.md:134-139` | Explicitly routes complete-controls-before-data-seat-dispatch to r61. |
| `.ufo/waves/round-60/controls/SUMMARY.md:14-22` | The cancelled wrong-key/action seats lacked worlds/receipts; self-test arms and a build-wave finding were substitutes, not missing pre-data receipts. |
| `.ufo/waves/round-60/controls-v2/SUMMARY.md:12-20` | W1/W2 met v2; the exploratory declaration preceded committed C1 data. That distinction did not erase the separate M90 dispatch defect. |
| `.ufo/waves/round-60/build/ExecKeyForms.md:1-6,194-210` | The semantic attack inspected in-flight sibling data and found an end-to-end wrong-key pass. Useful attack evidence is not automatically a pre-data control. |
| `.ufo/waves/round-61/controls/C2-base.txt:1-8` | Existing recorded result: all six repairs missing, `routed repairs verified 0 of 6`, `base-exit=1`. This seat did not rerun it. |
| `verifiers/check_routed_repairs.py:13-15,104-110` | Frozen counter authority and the limited substring-only R-f check. |

### Existing freeze anchor

Observed freeze commit: `7827628a939b0333c89892dfcedc72e390ccfb60` (`F`). It already includes the checker and C2 base receipt. Its lane identity is visible in the timed inspection below. Therefore **do not recreate the C2 “before” result after repairing the tree**; use the already committed control, with the frozen plan's target base `f3246d1493b60ea1c0d947a19c39f9e08e92f326` (`B`). The eight-line control file does not itself print a command, target revision or UTC time; cite the freeze/plan alongside it and do not invent those missing transcript fields.

### Existing single-wave pressure on M90

The stored dispatch specification contains a single batch with both control-building and source-acquisition work:

- `.ufo/waves/round-61/wave-spec.json`, item `ExecCounterV3`, drafts v3 and derives its A1 keys from the source rows being drafted in this wave.
- The same file, items `ScribeS112` through `ScribeS115`, directs immediate canonical-page fetching and delivers snapshot bytes/rows for L1 integration. `ScribeS112` explicitly says to fetch as v2 does, record UTC/status/bytes/sha, and deliver a snapshot for `.ufo/waves/round-61/snapshots/`.
- `.ufo/waves/round-61/wave-dispatch.json` says to issue exactly one batched call and includes the ScribeS112 source-fetch task in that call.
- The inspected `wave/swarm-registry.json` has `createdAt=2026-10-23T19:07:00.604Z`, but the inspected ScribeS112/ExecCounterV3/ExecWorldFixtures member records have null agent IDs. This generated registry is **not** a completed-controls or actual launch-time receipt.

**[INFERENCE]** If that batch launches as specified without an external barrier, data-seat dispatch is not gated on completed v3 controls. I did not observe the actual source-seat launch/fetch timestamps or an earlier completed v3 control receipt, so I do not assert their execution order. That missing event evidence must not be replaced by a later ancestry result. The single-wave instruction is not evidence that M90's stronger historical boundary was met.

## Exact operable integration order

The following is a proposed L1 sequence, **not a claim that these future commits or checks exist**. Letters denote immutable full commit IDs to be recorded when they exist. All commits remain the sole L1's work through the lane's authorized wrapper; this report prescribes no leaf mutation.

```text
B = f3246d1493b60ea1c0d947a19c39f9e08e92f326
  -> F = 7827628a939b0333c89892dfcedc72e390ccfb60
  -> V (counter v3 + historical-world/eligible-control fixtures frozen)
  -> W (observed C1-worlds receipt committed)
  -> D (new integrated C1 input rows/snapshots/entry; R-a..R-e repairs)
  -> A (pre-fetch ancestry receipt; R-f; measured tip T = A)
  -> [execute C1 base/tip fetch measurements and C2 tip measurement at T]
  -> M (actual measurement receipts only)
  -> round report commit
```

1. **F — already committed C2 control, before repairs.** Retain its checker unchanged. The relevant comparison is that frozen checker reading `--rev B`, then the same checker reading the repaired tip; not two different implementations from two checkouts. F contains the recorded base `0 of 6`, exit 1.
2. **V — freeze executable C1 control inputs.** Integrate v3 plus the seven reconstructed r60 worlds, W0 and the four eligible historical positive fixtures. Record the source digest and fixture identities. These are controls, not newly acquired S112-S115 measurement rows. Finish in-wave hardening before this freeze. Do not first land all new data and then call the subsequently tested counter “pre-data.”
3. **Run controls at V, then commit W.** `.ufo/waves/round-61/receipts/C1-worlds.txt` records the actual command, UTC, V, counter/fixture digests, each W1-W7 rejection, W0's do-nothing rejection, four positive results, exact `worlds reject 7 of 7; eligible rows pass 4 of 4` line, and suite exit code. The whole `--self-test` command must exit 0; individual negative-world evaluations must reject, not be mislabeled as successful worlds. Commit this receipt **before the L1's first C1 measurement fetch**. Historical positive fixtures let this barrier exist without first measuring the new rows live.
4. **D — input/data commit strictly after W.** Integrate the new C1 SOURCES rows, committed snapshot bytes and knowledge/SKILL content. R-a..R-e can land here because F already precedes them. Keep the source/fixtures pinned at V. The receipt inventory must identify D as the first introduction of the new measurement input, not merely pick a later descendant of data that was already in W. No new `--fetch` measurement has run yet under this proposed schedule.
5. **A — ancestry receipt strictly after D and before any measurement fetch.** Write and commit `.ufo/waves/round-61/receipts/controls-ancestry.txt`. It names **W as the control-receipts commit and D as the input-data commit**, records actual UTC, checks unequal IDs and `git merge-base --is-ancestor W D`, and records command output/status. Both IDs must have the lane identity and be ancestors of the then-current lane tip. Include the path/row inventory proving W carries the complete world receipt and D introduces the new measurement inputs; check that the frozen counter/fixtures did not change. This lands R-f. At A all six C2 repairs can exist, while C1 data measurement is still unrun.
6. **Measure immutable tip T=A, only now.** Use the same frozen v3 bytes for `python3 -B verifiers/check_scoped_rules.py --rev B --fetch` and `python3 -B verifiers/check_scoped_rules.py --rev T --fetch`; the frozen predicate requires actual exit 1 at B and exit 0 at T. Then use the F-frozen routed-repair checker with `--rev T`; C2 requires actual `routed repairs verified 6 of 6`, exit 0. Record UTC, absolute command/cwd, the literal B/T hashes, counter digest, full stdout/stderr and actual exit codes. Do not substitute the old v2 executable at B for the new counter reading B's committed inputs. This seat ran none of these commands.
7. **M — commit observed measurements, then report.** Commit `.ufo/waves/round-61/C1-measure.txt` and the chosen C2 measurement receipt, without changing the measured source/input. Cite T as the revision actually measured, not M or a moving `master` label. Any intervening implementation/input change invalidates the claim that the same frozen artifact was controlled and measured.

This gives the required internal sequence **worlds receipt W -> ancestry A -> fetch execution -> measurement receipt M**, and independently **checker/base-control F -> repairs D/A -> tip measurement T**.

### Avoid the future-commit identity trap

The stored `RevAncestry` item in `wave-spec.json` describes `C_data` as a commit “carrying the C1 --fetch measurement.” That artifact wording cannot govern this assignment's required pre-fetch ancestry barrier: such a commit does not exist until after the fetch. An ancestry receipt naming that future hash cannot be honestly generated before the fetch, and putting the receipt in the commit whose own final hash it records creates a self-reference problem.

The smallest correction is **separate input and measurement identities**: D carries inputs; M carries observed output. The pre-fetch receipt proves W precedes D. Once M exists, a later additive receipt may also prove W precedes M if required; that later proof never substitutes for A's pre-fetch barrier. Do not invent M in advance, relabel a post-fetch receipt as pre-fetch, or amend a cited commit to manufacture the desired order.

## The catching receipt, and its limits

The existing R-f string test is not the catching mechanism. The honest catching evidence is the **paired pre-fetch ancestry and measurement transcript**:

- `receipts/controls-ancestry.txt`: full W/D IDs; `W != D`; real `merge-base --is-ancestor W D` result; control-receipt/input inventory; frozen digest; actual UTC. Inspect the introduction history, not just the selected endpoint names.
- `C1-measure.txt`: immediately before the first actual `--fetch`, record the committed A/T, verify W/A exist and precede T, print the same frozen counter digest and UTC, then paste the measurement invocation and its actual output/exit. This distinguishes executing after the barrier from merely committing output after it.
- For the **full M90 dispatch claim**, also cite the actual completed-control and data-seat launch/first-acquisition records (or their committed digest). Source-seat `date -u` fetch receipts earlier than W expose early acquisition even when D was committed later. A draft dispatch JSON or a later commit timestamp is not a substitute for those event records.

The concrete strict-ancestry guard to add to the receipt protocol is `test "$W" != "$D"` alongside the existing `git merge-base --is-ancestor "$W" "$D"`, with both actual statuses recorded. These commands are recommendations, not observed new receipts. Non-equality closes the exercised reflexive case; **it does not close early acquisition followed by honestly ordered commits**. Only the execution/dispatch evidence addresses that larger shortcut. As with the plan's declared A4 limit, internally consistent records do not authenticate wall-clock truth against an author forging all timestamps.

Smallest safe correction: split V/W/D/A/M as above; retain the frozen C2 counter; strengthen the *receipt evidence*, not its declared score; explicitly limit any claim to the boundary the evidence establishes. If acquisition/dispatch already preceded completed controls, preserve and disclose that history. No later ordering fix can turn it into completed-controls-before-dispatch. Treat “faster concurrent acquisition in exchange for pre-data independence” as a real unresolved trade for the canonical judge, not an admitted no-harm improvement. This critic makes no judgment or admission.

## Exercised read-only observations

### Freeze commit and included control artifacts

Command:

```sh
date -u && git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show --format=fuller --stat 7827628a939b0333c89892dfcedc72e390ccfb60 && printf 'exit=0\n'
```

Pasted output:

```text
Fri 23 Oct 2026 07:11:15 PM UTC
commit 7827628a939b0333c89892dfcedc72e390ccfb60
Author:     kotoba-shokunin <kotoba@shokunin.local>
AuthorDate: Fri Oct 23 15:48:49 2026 -0300
Commit:     kotoba-shokunin <kotoba@shokunin.local>
CommitDate: Fri Oct 23 16:07:09 2026 -0300

    round-61: plan freeze (3 claims, frozen predicates), C2 routed-repairs counter + base control, census-before, v2 wave spec+dispatch (68 seats, 46 attack)

 .ufo/waves/round-61/census-before.txt        |   15 +
 .ufo/waves/round-61/controls/C2-base.txt     |    8 +
 .ufo/waves/round-61/wave-dispatch.json       | 1064 ++++++++++++++++++++++++++
 .ufo/waves/round-61/wave-spec.json           |  559 ++++++++++++++
 .ufo/waves/round-61/wave/swarm-registry.json |  690 +++++++++++++++++
 plans/round-61.md                            |  112 +++
 verifiers/check_routed_repairs.py            |  215 ++++++
 7 files changed, 2663 insertions(+)
exit=0
```

The author date and committer date differ. Use the DAG and actual event receipts rather than choosing whichever timestamp makes an order look favorable.

### Exercised reflexive-ancestry counterexample

Command:

```sh
date -u && git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin merge-base --is-ancestor 7827628a939b0333c89892dfcedc72e390ccfb60 7827628a939b0333c89892dfcedc72e390ccfb60 && printf 'exit 0\n'
```

Pasted output:

```text
Fri 23 Oct 2026 07:11:59 PM UTC
exit 0
```

Git itself produced no stdout. The printed status is reached only after a successful ancestry command. Equal endpoints therefore produce exactly the two marker substrings inspected by R-f when the invocation is included in the receipt.

### Observed working-tree fingerprints (not a v3 freeze or a gate run)

Command:

```sh
date -u && sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py && printf 'exit=0\n'
```

Pasted output:

```text
Fri 23 Oct 2026 07:12:43 PM UTC
61d8c5831d1904cba921ccc547b8308753c1726e704d4cc2b5cec10d60c77356  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
exit=0
```

The scoped-rules digest matches the r60 v2 digest recorded in `controls-v2/SUMMARY.md:3`; it is not a measurement of a delivered v3 implementation. No C1/C2 verifier results, full-wave completion, source-fetch order, or post-integration checks are claimed by this seat. L1 must exercise the named controls, ancestry barrier and frozen base/tip measurements on the actual integrated bytes.

Installs: no installs.
Blockers: none for this review; actual v3/control/fetch/dispatch chronology remains unverified, not passed.
Attacked: commit-order laundering, reflexive ancestry, and the input-commit/measurement-commit identity trap in C1/C2 integration.
