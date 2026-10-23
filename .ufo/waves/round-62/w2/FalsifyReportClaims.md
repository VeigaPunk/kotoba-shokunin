# FalsifyReportClaims — round-62 wave-2 claim audit

Reviewer: `L1kotoba62.FalsifyReportClaims`. Primary axis: calibration (the consistency sub-axis); affected secondary axes: depth and operability.

Review target: **`e6da78bbe420722dd18a13182a7c4b64ce02f005`**, not the changing working tree. Repository-relative locations below refer to that commit. I read `plans/round-62.md` first, including its E1 addenda; the original C1 prediction is explicitly superseded, so I do not score its old expected values as an undisclosed contradiction. This is an evidence/counterexample report, **not a round verdict, admission, or closure**. No judge or other agent runtime was invoked.

## Numbered defects and smallest safe corrections

1. **The blanket no-harm sentence has no supporting completed receipt.**
   - **Sentence:** `SCORECARD.md:36`: “No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged.” `LOG.md:2564` points neutrally at `noharm-tip.txt`; the completed-round paragraph at `SCORECARD.md:369` also credits the no-harm-count repair without disclosing this round's incomplete battery.
   - **Counterexample/evidence:** the committed `.ufo/waves/round-62/noharm-tip.txt:12-23` records failing registry and corpus-index arms and ends `Battery exit code: 124`, not `no-harm OK`. Its measured revision is `3e7aed9b…`, before the final corpus/registry/successor changes. `w1/ExecNoHarmRun.md:7-19` expressly says later arms were not reached. The receipt census in **D1** computes `PASS=5`, `FAIL=2`, no completed self-verification arms. Hash preservation and the bounded self-tests reproduced in **A1-A5** do not establish every axis's no-harm condition.
   - **Axes:** calibration; operability. This is not evidence that the later tip is necessarily harmed; it is evidence that the universal sentence is unsupported.
   - **Smallest correction:** append an explicit correction: the inherited counters' hashes/bounded self-tests were preserved, but the committed no-harm battery failed/timed out and later arms were unevaluated. A completed, revision-pinned final battery receipt is required before substituting a positive no-harm claim. Do not describe an unrun arm as passed.

2. **The claimed successful census-after receipt is not committed at all.**
   - **Sentences:** `LOG.md:2558`: “`.ufo/waves/round-62/census-after.txt` carries the validator body and its `exit=` line; round-end exit 0 after the corpus files land”; `LOG.md:2562`: “Census before 15 W04 `exit=0` → after 16 W04 `exit=0`”; `SCORECARD.md:369`: “census 15 → 16 W04 exit 0.”
   - **Counterexample/evidence:** **D2** executes `git show e6da78bb…:.ufo/waves/round-62/census-after.txt` and exits **128**, reporting that the path exists on disk but not in the commit. The working-tree copy I opened during the review was an interim receipt naming missing used-by files and `exit=1`; it cannot serve as a committed exit-0 receipt. Crucially, a *fresh* validation of the complete committed snapshot does exit 0 (**B10**), while the round-start snapshot does so in **C4**; these fresh observations do not retroactively create the cited receipt.
   - **Axes:** calibration; operability.
   - **Smallest correction:** commit a newly observed census-after receipt naming its actual measured revision and complete command/output/exit, and distinguish it from the interim failure. Cite **B9/B10/C3/C4** if using this review's re-derivation; do not retain the dead receipt pointer as if it already evidenced success.

3. **“Round 62 completed” and the round totals are premature, visibly unfinished assertions.**
   - **Sentences:** `SCORECARD.md:369` opens “Round 62 completed” but later says “wave 2 `{W2_COUNT}` attack seats; total `{TOTAL}`.” `LOG.md:2563` says “Wave 2 … N seats” and “Round total = 39 + 5 + N.” The lesson's `## Falsify corrections` still contains “(to be filled by wave 2).”
   - **Counterexample/evidence:** **D1** finds no committed wave-2 paths at the assigned revision. The placeholders are literal committed text, not a counting result. The assignment itself is a pre-report falsification review, not a non-author closure. **F1** shows the completed-round annotation being introduced while these placeholders remain.
   - **Axes:** calibration.
   - **Smallest correction:** mark the annotation as measured work pending falsification/closure, not completed. Before the final report, replace symbolic totals with command-derived committed dispatch/report counts, and record actual falsify dispositions. Preserve the non-author closure boundary already stated at `SCORECARD.md:36`.

4. **The current wave-1 census mixes a historical result with later replacement/completion reports.**
   - **Sentences:** `LOG.md:2547` says the dead seats “are named, not replaced”; `LOG.md:2563` and `SCORECARD.md:369` describe wave 1 as “34 reports, 5 dead” / “seat count 34 of 39 here.”
   - **Counterexample/evidence:** that historical result is correctly reproducible at `3e7aed9b…` (**B6**). At the actual review tip, the identical command gives **`35 of 39; missing 4; unmatched 3`**, exit 1 (**B7**), and the directory contains **38** Markdown reports (**D1**). `w1/ExecSuccessor31.md` is now present and is the completion implementation report; the original count had named that seat missing. The unmatched reports are `ExecNoHarmRun.md`, `ScoutRegistry.md`, and `ScribeLessonQ57.md`. A filename collision must not silently credit the original dead seat with a later call's report.
   - **Axes:** calibration; identity/provenance.
   - **Smallest correction:** retain the original attempt's census explicitly as historical at its revision; separately inventory the completion call with distinct identities/report provenance. Publish the final-tip census and distinguish original missing seats from completion deliverables. Do not silently re-label the old exit-1 receipt a final census.

5. **The completion-call count and exhaustive re-verification claim lack a committed accounting instrument.**
   - **Sentences:** `LOG.md:2563`: “Build-completion call: 5 seats (executor 2, scribe 2, scout 1)”; `LOG.md:2547`: “each reused artifact was re-verified here.” The same completion-call count is carried into `SCORECARD.md:369` and the symbolic round total.
   - **Counterexample/evidence:** **D1** lists the committed direct JSON dispatch/spec metadata: only the original `w1-dispatch.json`, `w1-plan.json`, and `w1-spec.json`. The original dispatch accounts for its own spawn count, not a separately identifiable completion batch. **B7** demonstrates that completion reports have been mixed into that original report directory. The predicate receipts authenticate specific code runs, not an exhaustive re-verification of every reused wave report.
   - **Axes:** calibration; provenance.
   - **Smallest correction:** commit the completion call's actual dispatch/roster and associate its reports with that call before including its spawn count in the report. Replace “each reused artifact” with the specific re-verifications for which a receipt exists, or attach the exhaustive artifact-to-check mapping. This is an unsupported committed-evidence claim, not an assertion that no such call occurred.

6. **C2's self-test “tip/H2” is a different revision from the declared measured-data tip.**
   - **Sentence/predicate:** `plans/round-62.md:132-137` defines H2 as the measured tip tree and the tip side as the round-62 data revision. `LOG.md:2552` and `SCORECARD.md:36,369` carry the unqualified self-test headline “honest passed 2 of 2; … tip 6 of 6” beside receipt revision `3e7aed9b…`.
   - **Counterexample/evidence:** `check_routed_repairs_v2.py:31,514-525` fixes `TIP_REV` to **`45a7ecfac9e203297f3146c45d63f5e79367470c`**, the plan-freeze tree. **A3** and the committed C2 receipt explicitly print that historical revision for the H2 CLI call. The distinct CLI measurements at data revision and review tip really do return `6 of 6` (**B2/B3**); the numerical result is not disputed, but those are not the self-test's H2 observation.
   - **Axes:** calibration; measurement identity.
   - **Smallest correction:** name H2's actual historical revision and separately cite the data/final-tip CLI receipts; never relabel the self-test's H2 as a data-tip run. If the frozen H2 identity is required literally, a corrected separately identified successor measurement and new receipt are needed. The canonical judge, not this review, resolves that predicate-identity consequence.

7. **“Imports those six checks unchanged” obscures which evaluator actually produces the successor score.**
   - **Sentence:** `LOG.md:2554`: “The v2 successor imports those six checks unchanged and adds its own G-a…G-f hardening”; the same rationale appears in `SCORECARD.md:36`'s no-harm sentence.
   - **Counterexample/evidence:** `check_routed_repairs_v2.py:302-329` computes production results from its own local `r_a_…` through `r_f_…` functions. Its calls to `frozen.check_repairs` are comparison controls in the self-test (`:448-452,472-478,500-502,518-520`), not the successor's production evaluator. **A1** verifies the frozen file's unchanged digest; **A3/E4** verify bounded frozen comparisons, not unchanged production semantics.
   - **Axes:** calibration; authority/evaluator identity.
   - **Smallest correction:** say “the frozen counter file is unchanged and its `check_repairs` is re-run as a comparison control; the successor separately implements the same six repair properties with G-a…G-f hardening.” Do not use the import as proof of universal no-harm.

8. **The lesson gives the wrong diagnostic for its cited hollow-control receipt.**
   - **Sentence:** `corpus/lessons/round-62.md:25`: “its diagnostic is a missing `check_scoped_rules.py` path, not the intended guard-direction rejection.”
   - **Counterexample/evidence:** the committed `controls/absorption-hollow.txt:6-9` says **`absorption self-test failed: guard-mutation direction is missing for one or more errata`**, `exit=1`. It does not report a missing counter path. The independently reconstructed reject-only control in **E1** produces that same diagnostic; **E2** separately reconstructs the label-only control. These reconstructions are not claimed to be the original `/tmp/r62hollow` mutant files.
   - **Axes:** calibration; depth.
   - **Smallest correction:** append/carry a falsify correction naming the actual receipt and diagnostic, and remove the erroneous missing-path interpretation from any final report. Do not downgrade the recorded guard-direction failure into an environment failure.

9. **M93's quoted forcing evidence is not itself an absorption claim, while actual stale implementation claims remain unmarked.**
   - **Sentence/evidence chain:** `corpus/lessons/round-62.md:25` supports “erratum recorded as absorbed” chiefly by quoting the r61 report's “five pre-data arm amendments each forced by a measured attack.” `w1/ScoutPriorReceipts.md:18` expressly states that that quotation **does not claim the attacks were re-run on the landed counter**.
   - **Counterexample/evidence:** the stronger, directly falsifiable source is already local: `corpus/knowledge/scoped-rules-counter-round61.md:20` describes the frozen implementation as having no commented/negated/equals-form keys, and `:23-26` describes a raw tokenizer/claim-verb guard. Those claims conflict with the reproduced E2e/E2f survivors (**A2**) and with the corrected entry. The old entry remains independently indexed at `corpus/README.md:105`; it contains no explicit erratum pointing to these corrections.
   - **Axes:** calibration; depth; quality trend.
   - **Smallest correction:** ground M93 in the actual implementation-overclaim locations, not merely the truthful statement that attacks forced plan amendments. Add an explicit supersession/erratum link identifying the stale r61 arm descriptions and adjust the index description accordingly, without rewriting the non-author spot-check or pretending the historical report used an unquoted “absorbed” verdict.

10. **The before-state citation does not carry the claimed search commands or the cited timestamp.**
    - **Sentence:** `LOG.md:2549`: “Five targeted searches … (`controls/absorption-before.txt`, 2026-10-23T20:53:36Z) → 0 of 5 …”.
    - **Counterexample/evidence:** that receipt's timestamp is **`2026-10-23T20:57:43Z`**. It lists conclusions/seat mention counts but not the actual five search command bodies. `w1/ScoutPriorReceipts.md:126-159` likewise gives a “Census command” label plus results and a prose description, not the Python command source. **D1** supplies a fresh explicit committed-file count sweep: each forcing seat has no landed-sha mention, and it names every r61 file that does mention the pin. The bounded before-state is consistent with that sweep plus inspection of those files; the claimed historical command/time provenance is not.
    - **Axes:** calibration; reproducibility.
    - **Smallest correction:** cite the receipt's actual timestamp and commit an executable/re-runnable census command with its output. Bound “every r61 amendment” to the five audited forcing attack tables; do not turn a prefix-mention census alone into a proof about every possible arm-level experiment.

11. **The strict controls-before-first-data statement is stronger than the committed chronology establishes.**
    - **Sentences:** `plans/round-62.md:297-303` says every control receipt lands before the first matrix/successor data receipt and “no data run precedes its controls”; `LOG.md:2547,2560` carries the controls-before-data narrative.
    - **Counterexample/evidence:** `controls/absorption-hollow.txt:16-28` itself contains a real complete matrix measurement, including the actual computed survivors and headline. **D4** shows that receipt and the instrument first landing **together** at `3e7aed9b…`; the separately named data receipt lands later at `f9ab0812…`. `w1/ExecAbsorbInstrument.md:45-67`, also in the earlier wave evidence, already records the real matrix result. **E6** does establish ancestry of the earlier control commit; it does not make the real matrix observations inside the later control/wave files occur strictly after those same files were committed.
    - **Axes:** calibration; experimental provenance.
    - **Smallest correction:** state the precise supported fact: prior before-controls precede the instrument/hollow-control commit, and the separately named formal data receipt follows it. Explicitly disclose the real green-path matrix data co-landed with its hollow-control receipt. If the frozen strict reading excludes that, it is a historical contract issue for the canonical judge, not something prose, changed filenames, or rewritten history can repair. Preserve the receipts.

12. **The next-step sentence changes the measurement unit from instances to erratum classes.**
    - **Sentence:** `SCORECARD.md:371`: “the six surviving errata classes (E2c condition 5/6, E2e negation/commented/equals forms, E2f G7) …”; it then names G9 separately as residual.
    - **Counterexample/evidence:** **A2** measures the frozen five groups and reports survivors in the **three** groups E2c/E2e/E2f, with **six instances**, one of which is explicitly the G9 compound-purpose instance. **A4** reports the successor closing **five of those six**, with G9 surviving. The sentence's list is neither the matrix's class universe nor its exact survivor-instance universe.
    - **Axes:** calibration; depth.
    - **Smallest correction:** use “three erratum groups / six matrix instances,” name the actual instance set, and keep the successor's measured closure and the proposed live-row work separate. Do not imply six new classes or that G9 was outside the measured survivors.

13. **The “complete” landed-scope list omits a non-author delta and should preserve its ownership explicitly.**
    - **Sentence:** `LOG.md:2556`: “R-b landed scope (round 62, complete list to date): …”.
    - **Counterexample/evidence:** `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --name-status a745411c66d4765e9ac0ce48f1d96c34f425dab4 e6da78bbe420722dd18a13182a7c4b64ce02f005` includes `A corpus/lessons/round-61-verifier-spotcheck.md`, which the list omits. **F2** identifies its intervening additions/correction as `protocol-shokunin` commits, not lane-authored round-62 work. The README index repair is lane work; the outside review itself is not.
    - **Axes:** calibration; ownership/adjacency.
    - **Smallest correction:** qualify the list as lane-authored changes and separately name the intervening non-author closure artifact, or include it in a complete base-to-tip delta explicitly attributed to its author. Do not edit or claim authorship of that outside review.

## Bounded claims the evidence does support

- C1's exact amended matrix headline and survivor names reproduce (**A2**). Its frozen pin matches (**A1**). The original C1 numerical expectation is superseded by E1, not a hidden changed target.
- The v3.1 successor reproduces its bounded closure/world/assertion output (**A4**) and the separately specified committed/live measurement (**C1**). G9 remains named, not repaired by assertion. The original scoped-rules counter also reproduces its self-test and committed/live result (**A5/C2**).
- C2's headline reproduces (**A3**), with the H2 identity caveat above. The base, data, and assigned-tip CLI measurements reproduce (**B1-B4**). The frozen comparison counter and seat-count self-tests reproduce (**E3/E4**).
- The source census really changes **115 → 116** rows (**C3/B9**); the complete committed corpus now validates with the new warning row (**C4/B10**). This is a new review observation, not the missing committed census-after receipt.
- S118 was re-opened with the Read tool at <https://code.claude.com/docs/en/memory.md>. The live page still states that `paths` takes glob patterns and accepts a YAML list or comma-separated string under **Rule frontmatter reference**. The committed snapshot's located line is `.ufo/waves/round-62/snapshots/S118.page:250`; its size and digest reproduce (**D3/A1**). I do not claim the freshly opened live response is byte-identical to the snapshot, nor that vendor prose proves the runtime guards.
- The actual registry is conformant **39 of 39, phantom 0**, exit 0 (**B8**). The new instrument rows say **gate**, not capability/probe. **F1** shows annotations rather than a new capabilities-table row. I found no newly claimed capability row in the audited scorecard delta; a registry row is not a capability demonstration.

## Execution boundaries

All verifier execution used an isolated `/tmp` clone populated by `git archive` of the assigned commit; the lane itself was read-only apart from this report. The base corpus used a separate archived round-start snapshot. No source, counter, registry, corpus, fleet, sibling, state, manifest, Git index, or JJ file was edited. No subagents or background jobs were dispatched. Commands were serial, individually bounded to the assigned command deadline. No tools were installed or updated.

I did **not** re-run the full no-harm battery; its committed failed/timed-out receipt and the executor's explicit account are evidence of what was reached, not a green result. The appendices below contain the exact commands/output/exits of the counting and bounded control commands actually exercised. The reconstructed controls are clearly distinguished from the unavailable original scratch mutant files.

Sandbox construction used:

```sh
git clone --shared --no-checkout --quiet /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb && git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin archive e6da78bbe420722dd18a13182a7c4b64ce02f005 | tar -x -C /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb
git clone --shared --no-checkout --quiet /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba-r62-FalsifyReportClaims-base-a745411c && git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin archive a745411c66d4765e9ac0ce48f1d96c34f425dab4 | tar -x -C /tmp/kotoba-r62-FalsifyReportClaims-base-a745411c
```

## Exact command transcripts

Working directory for the commands was `/tmp/kotoba-r62-FalsifyReportClaims-e6da78bb`, except the round-start census commands, whose working directory was `/tmp/kotoba-r62-FalsifyReportClaims-base-a745411c`. Repository-internal path arguments to `--spec`, `--dir`, and Git are deliberately repository-relative as their interfaces require; executable paths and filesystem reads are absolute. Standard error was captured with standard output; the exit line was appended from the process return code.

```text
### A1 frozen file digests
$ sha256sum /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_erratum_absorption.py /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules.py /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules_v31.py /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs.py /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/.ufo/waves/round-62/snapshots/S118.page
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_erratum_absorption.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules.py
a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules_v31.py
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs.py
02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/.ufo/waves/round-62/snapshots/S118.page
exit=0
```

```text
### A2 C1 counted predicate
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

```text
### A3 C2 counted predicate
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py --self-test
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
exit=0
```

```text
### A4 C1 successor self-test
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules_v31.py --self-test
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
exit=0
```

```text
### A5 frozen C1 no-harm self-test
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
self-test: 0 failure(s) over 189 assertions
exit=0
```

```text
### B1 C2 base CLI
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

```text
### B2 C2 data CLI
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
exit=0
```

```text
### B3 C2 assigned-tip CLI
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs_v2.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
exit=0
```

```text
### B4 frozen C2 base CLI
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

```text
### B5 r61 seat census
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_seat_counts.py --spec .ufo/waves/round-61/wave-spec.json --dir .ufo/waves/round-61/wave --rev a745411c66d4765e9ac0ce48f1d96c34f425dab4
seat reports committed 65 of 68; missing 3: SentNovelty, RevCounterHistory, SimplEntry; unmatched 0: none
exit=1
```

```text
### B6 r62 data seat census
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w1-spec.json --dir .ufo/waves/round-62/w1 --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
seat reports committed 34 of 39; missing 5: ExecSuccessor31, ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 0: none
exit=1
```

```text
### B7 r62 assigned-tip seat census
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w1-spec.json --dir .ufo/waves/round-62/w1 --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
seat reports committed 35 of 39; missing 4: ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 3: ExecNoHarmRun.md, ScoutRegistry.md, ScribeLessonQ57.md
exit=1
```

```text
### B8 assigned-tip gate registry
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_gate_registry.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
verifiers/box_proof_case_deletion.py         OK 
verifiers/check_agent_definitions.py         OK 
verifiers/check_agentdef_boxes.py            OK 
verifiers/check_alwayson_boxes.py            OK 
verifiers/check_assertion_floors.py          OK 
verifiers/check_callee_rename.py             OK 
verifiers/check_command_files.py             OK 
verifiers/check_correction_sweep.py          OK 
verifiers/check_could_not_evaluate.py        OK 
verifiers/check_description_thresholds.py    OK 
verifiers/check_erratum_absorption.py        OK 
verifiers/check_explicit_invocation.py       OK 
verifiers/check_gate_finding_delta.py        OK 
verifiers/check_gate_registry.py             OK 
verifiers/check_hook_files.py                OK 
verifiers/check_infoless_fences.py           OK 
verifiers/check_mcp_instructions.py          OK 
verifiers/check_opencode_repin.py            OK 
verifiers/check_overlap_levers.py            OK 
verifiers/check_plugin_manifests.py          OK 
verifiers/check_routed_repairs.py            OK 
verifiers/check_routed_repairs_v2.py         OK 
verifiers/check_scoped_rules.py              OK 
verifiers/check_scoped_rules_v31.py          OK 
verifiers/check_seat_counts.py               OK 
verifiers/check_sibling_census.py            OK 
verifiers/check_sources_append_only.py       OK 
verifiers/check_substrate_pins.py            OK 
verifiers/check_sweep_mutants.py             OK 
verifiers/compare_harness_independent.py     OK 
verifiers/fault_injection_corpus.sh          OK 
verifiers/verify_alwayson.py                 OK 
verifiers/verify_corpus_independent.py       OK 
verifiers/verify_corpus_integrity.py         OK 
verifiers/verify_dispatch_prompts.py         OK 
verifiers/verify_harness_claims.py           OK 
verifiers/verify_harness_independent.py      OK 
verifiers/verify_skill_checklist.py          OK 
verifiers/verify_surfaces.py                 OK 
gate registry rows conformant 39 of 39 lane verifiers; phantom 0
exit=0
```

```text
### B9 assigned-tip source census
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/corpus/SOURCES.md --today 2026-10-23
file	rows	116
file	tier.A	113
file	tier.B	2
file	tier.C	1
file	status.mined	108
file	status.queued	7
file	status.rejected	1
FLEET	rows	116
FLEET	tier.A	113
FLEET	tier.B	2
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	7
FLEET	status.mined	108
FLEET	status.rejected	1
FLEET	status.invalid	0
FLEET	missing	0
exit=0
```

```text
### B10 assigned-tip source validation
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/corpus/SOURCES.md --today 2026-10-23
file	W04	S018 duplicate url agentskills.io/specification across scopes
file	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
file	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
file	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
file	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
file	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
file	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
file	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
file	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
file	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
file	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S115 duplicate url cursor.com/docs/rules across scopes
file	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
file	ok	/tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/corpus/SOURCES.md
exit=0
```

```text
### C1 successor committed/live measurement
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules_v31.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; rev 43fe01804708d65e53965b4be31e9dc7dce793e4
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=0
```

```text
### C2 frozen scoped-rules committed/live measurement
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_scoped_rules.py --rev 43fe01804708d65e53965b4be31e9dc7dce793e4 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; rev 43fe01804708d65e53965b4be31e9dc7dce793e4
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=0
```

```text
### C3 round-start source census
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file /tmp/kotoba-r62-FalsifyReportClaims-base-a745411c/corpus/SOURCES.md --today 2026-10-23
file	rows	115
file	tier.A	112
file	tier.B	2
file	tier.C	1
file	status.mined	107
file	status.queued	7
file	status.rejected	1
FLEET	rows	115
FLEET	tier.A	112
FLEET	tier.B	2
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	7
FLEET	status.mined	107
FLEET	status.rejected	1
FLEET	status.invalid	0
FLEET	missing	0
exit=0
```

```text
### C4 round-start source validation
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /tmp/kotoba-r62-FalsifyReportClaims-base-a745411c/corpus/SOURCES.md --today 2026-10-23
file	W04	S018 duplicate url agentskills.io/specification across scopes
file	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
file	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
file	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
file	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
file	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
file	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
file	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
file	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
file	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
file	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S115 duplicate url cursor.com/docs/rules across scopes
file	ok	/tmp/kotoba-r62-FalsifyReportClaims-base-a745411c/corpus/SOURCES.md
exit=0
```

```text
### D1 committed census re-derivations
$ python3 -B -c 'import subprocess, json, re
R = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
V = "e6da78bbe420722dd18a13182a7c4b64ce02f005"
P = "a745411c66d4765e9ac0ce48f1d96c34f425dab4"
def git(*args):
    p = subprocess.run(["git", "-C", R, *args], capture_output=True, text=True)
    if p.returncode: raise SystemExit(p.stderr)
    return p.stdout
build = git("ls-tree", "-r", "--name-only", V, "--", ".ufo/waves/round-60/build").splitlines()
pattern = re.compile(r"^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$")
print("r60 basename census:", sum(bool(pattern.fullmatch(p.rsplit("/",1)[-1])) for p in build))
round_paths = git("ls-tree", "-r", "--name-only", V, "--", ".ufo/waves/round-62").splitlines()
print("r62 direct JSON metadata:")
for p in round_paths:
    if p.count("/") == 3 and p.endswith(".json"): print(p)
print("r62 w1 direct .md files:", sum(p.startswith(".ufo/waves/round-62/w1/") and p.count("/")==4 and p.endswith(".md") for p in round_paths))
print("r62 w2 committed paths:", sum(p.startswith(".ufo/waves/round-62/w2/") for p in round_paths))
for n in (61,62):
    text = git("show", V+f":.ufo/waves/round-{n}/noharm-tip.txt")
    passed = [ln for ln in text.splitlines() if ln.startswith("PASS  ")]
    failed = [ln for ln in text.splitlines() if ln.startswith("FAIL  ")]
    controls = [ln for ln in passed if ln.split()[1].startswith("battery-self")]
    print(f"r{n} noharm: PASS={len(passed)} comparison={len(passed)-len(controls)} self-verification={len(controls)} FAIL={len(failed)}")
    print("terminal:", text.splitlines()[-1])
seats = ["MutA3", "MutFixtures", "MutA4", "MutA1", "MutA2"]
sha_prefix = "5a5adc94"
print("r61 attack-seat landed-sha occurrences:")
for seat in seats:
    text = git("show", P+":.ufo/waves/round-61/wave/"+seat+".md")
    print(seat+": "+str(text.count(sha_prefix)))
print("r61 pinned-sha file census:")
r61 = git("ls-tree", "-r", "--name-only", P, "--", ".ufo/waves/round-61").splitlines()
for p in r61:
    text = git("show", P+":"+p)
    hits = text.count(sha_prefix)
    if hits: print(p+": "+str(hits))
'
r60 basename census: 29
r62 direct JSON metadata:
.ufo/waves/round-62/w1-dispatch.json
.ufo/waves/round-62/w1-plan.json
.ufo/waves/round-62/w1-spec.json
r62 w1 direct .md files: 38
r62 w2 committed paths: 0
r61 noharm: PASS=18 comparison=15 self-verification=3 FAIL=0
terminal: exit=0
r62 noharm: PASS=5 comparison=5 self-verification=0 FAIL=2
terminal: Battery exit code: 124
r61 attack-seat landed-sha occurrences:
MutA3: 0
MutFixtures: 0
MutA4: 0
MutA1: 0
MutA2: 0
r61 pinned-sha file census:
.ufo/waves/round-61/C1-v3-measure.txt: 2
.ufo/waves/round-61/controls/C1-base.txt: 1
.ufo/waves/round-61/receipts/C1-worlds.txt: 3
.ufo/waves/round-61/wave/ExecCounterV3.md: 5
exit=0
```

```text
### D2 committed census-after receipt lookup
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:.ufo/waves/round-62/census-after.txt
fatal: path '.ufo/waves/round-62/census-after.txt' exists on disk, but not in 'e6da78bbe420722dd18a13182a7c4b64ce02f005'
exit=128
```

```text
### D3 committed snapshot size
$ wc -c /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/.ufo/waves/round-62/snapshots/S118.page
55354 /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/.ufo/waves/round-62/snapshots/S118.page
exit=0
```

```text
### D4 pre-data control chronology
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --reverse --format=%H%x09%s a745411c66d4765e9ac0ce48f1d96c34f425dab4..e6da78bbe420722dd18a13182a7c4b64ce02f005 -- verifiers/check_erratum_absorption.py .ufo/waves/round-62/controls/absorption-hollow.txt .ufo/waves/round-62/C1-absorb-measure.txt
3e7aed9b61bbfd83e0c800213b6dfc6da6191f85	round-62: wave-1 evidence (34 of 39 seat reports) + inherited fixes — absorption instrument draft + hollow/label control, routed-repairs v2 draft, S118 row/snapshot, r61 stray-n repair
f9ab0812a574c369aa5cb94616e6ddffd1c5202b	round-62: data receipts — C1 absorption matrix (measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2) and C2 routed-repairs successor (dishonest 6 of 6 rejected, honest 2 of 2, base 0 of 6, tip 6 of 6); seat-count receipt 34 of 39
exit=0
```

```text
### E1 independently reconstructed reject-only control
$ python3 -B -c 'import sys
sys.path.insert(0, '"'"'/tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers'"'"')
import check_erratum_absorption as m
real_run = m.run_matrix
m.run_matrix = lambda counter, *args, **kwargs: real_run(counter, execute_mutations=False)
raise SystemExit(m.main(["--self-test"]))
'
absorption self-test failed: guard-mutation direction is missing for one or more errata
exit=1
```

```text
### E2 independently reconstructed label-only control
$ python3 -B -c 'import sys
sys.path.insert(0, '"'"'/tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers'"'"')
import check_erratum_absorption as m
real_run = m.run_matrix
m.run_matrix = lambda counter, *args, **kwargs: real_run(counter, scorer=m.label_scorer, **kwargs)
raise SystemExit(m.main(["--self-test"]))
'
absorption self-test failed: seeded controls did not classify in both directions
exit=1
```

```text
### E3 seat-count gate self-test
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_seat_counts.py --self-test
self-test complete: (3, [], []) (want (3, [], [])) ok
self-test one-missing: (2, ['Beta']) (want (2, ['Beta'])) ok
self-test registry-is-not-a-seat: [] (want []) ok
self-test round61-shape: (1, ['Beta', 'Gamma'], ['Note.md']) (want (1, ['Beta', 'Gamma'], ['Note.md'])) ok
self-test empty-spec-raises: True (want True) ok
seat reports committed 1 of 3; missing 2: Beta, Gamma; unmatched 1: Note.md
self-test arm-count: 5 (want 5) ok
self-test: 0 failure(s)
exit=0
```

```text
### E4 frozen repairs self-test
$ python3 -B /tmp/kotoba-r62-FalsifyReportClaims-e6da78bb/verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

```text
### E5 r61 owned ancestry command
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a 43fe01804708d65e53965b4be31e9dc7dce793e4
exit=0
```

```text
### E6 round-62 formal controls/data ancestry
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin merge-base --is-ancestor 9f03dcd742701d284cf90d75c43ad53711776c61 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
exit=0
```

```text
### F1 scorecard changes against round-start
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --unified=0 a745411c66d4765e9ac0ce48f1d96c34f425dab4 e6da78bbe420722dd18a13182a7c4b64ce02f005 -- SCORECARD.md
diff --git a/SCORECARD.md b/SCORECARD.md
index 6cbacd4..5296ab4 100644
--- a/SCORECARD.md
+++ b/SCORECARD.md
@@ -35,0 +36,2 @@ criteria of the next band met.
+**Round 62 axis annotations (append-only; verdicts belong to the non-author closure).** *Depth (C1, score held 9):* the erratum-absorption matrix measures the five r61 errata against the landed v3 counter (sha256 `5a5adc94…`) arm-by-arm: `python3 -B verifiers/check_erratum_absorption.py --self-test` → `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`, exit 0 at receipt rev `3e7aed9b` (`.ufo/waves/round-62/C1-absorb-measure.txt`); before: 0 of 5 committed arm-level receipts (`.ufo/waves/round-62/controls/absorption-before.txt`); kill arms in `controls/absorption-hollow.txt` (hollow exit 1, label-only exit 1, real exit 0). Survivors: E2c ×2, E2e ×2, E2f ×2 (G9 stays a declared bound). The v3.1 successor (`verifiers/check_scoped_rules_v31.py`) is separate fix evidence, not part of the counted predicate. No band move is claimed: depth 9 waits on the non-author closure (r60 E2 exploratory ruling unchanged). *Consistency/calibration sub-axis (C2, score held 10):* the routed-repairs successor `python3 -B verifiers/check_routed_repairs_v2.py --self-test` → `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`, exit 0; CLI base `f3246d14` `0 of 6` exit 1 → data rev `3e7aed9b` `6 of 6` exit 0 (`.ufo/waves/round-62/C2-successor-measure.txt`); before: frozen counter accepts D1–D6 `6 of 6` and H1 `4 of 6` (`controls/frozen-repairs-dishonest.txt`). No capabilities row: both new instruments are registered gates, not repertoire (AXES.md § Capabilities). No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged.
+
@@ -367 +369,3 @@ things stand.
-**Next: round 62** — candidates: (1) depth: the v3 counter's first measured-successor exercise on NEW rows only after the closure upholds the frozen predicate (per CriticC1Scope's bounded-successor wording); the W8 escape class and A2's F6 bound are the named residuals. (2) calibration: the `check_routed_repairs.py` honest-pass hardening (ExecC2Audit's G-a registry-roster re-derivation) as a separately identified successor measurement, NOT a rewrite of the frozen six. Standing debt: SentBounds' pre-wave baseline receipt; helper-invocation receipts (op origin unverifiable from op log alone).
+**Round 62 completed (hyaku run 5, attempt 2; attempt 1 OOM-killed mid-wave):** claims C1 depth (erratum-absorption matrix) and C2 calibration (routed-repairs successor). C1 counted predicate `python3 -B verifiers/check_erratum_absorption.py --self-test` → `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`, exit 0 at receipt rev `3e7aed9b` (`.ufo/waves/round-62/C1-absorb-measure.txt`), before 0 of 5 committed arm-level receipts; depth held 9 (band move waits on the non-author closure). C2 `python3 -B verifiers/check_routed_repairs_v2.py --self-test` → `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`, exit 0; CLI base `f3246d14` `0 of 6` exit 1 → `3e7aed9b` `6 of 6` exit 0 (`C2-successor-measure.txt`); the consistency row held 10. Frontier: SOURCES 115 → 116 rows (S118, re-opens S103), census 15 → 16 W04 exit 0; lesson M93 + Q57. r61 routed defects worked: seat count 34 of 39 here / 65 of 68 + `RevCounterHistory` named there; the stray-`n` provenance repair; the C2 byte-freeze wording (`95ade9be…`); the no-harm arm count; the Gate reject sample. Round shape: wave 1 39 (34 reports, 5 dead), build-completion call 5, wave 2 {W2_COUNT} attack seats; total {TOTAL}. Report `.ufo/reports/round-62/kotoba.md`.
+
+**Next: round 63** — candidates: (1) depth: the six surviving errata classes (E2c condition 5/6, E2e negation/commented/equals forms, E2f G7) as live-row fixes once the closure upholds the frozen matrix; the W8 escape class and A2's F6 compound-purpose bound (G9) stay the named residuals. (2) calibration: the v2 successor's first exercise on fresh routed defects (the G-a count against a new round's build subtree), not a rewrite of the frozen six. Standing debt: SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions.
exit=0
```

```text
### F2 non-author closure delta ownership
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --format=%H%x09%an%x09%s a745411c66d4765e9ac0ce48f1d96c34f425dab4..e6da78bbe420722dd18a13182a7c4b64ce02f005 -- corpus/lessons/round-61-verifier-spotcheck.md
fecb3d6119f3e75ae7e816a5848fdb2295f8b0f4	protocol-shokunin	round-61 verifier spot-check: appended count correction (21 cited hashes)
a1cb8abc3911a5df3a2877915509118e384651a4	protocol-shokunin	round-61 verifier spot-check (integrator, hyaku): non-author admit/reject
exit=0
```
