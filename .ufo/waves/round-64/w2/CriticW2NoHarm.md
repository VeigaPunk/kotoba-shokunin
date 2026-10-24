# Round 64 wave 2 — adversarial no-harm audit

Seat: `kotoba-r64.CriticW2NoHarm-2`.

Scope: inherited no-harm battery, its base==base twin, and receipt identity at the assigned measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`. Canonical axes: **depth + consistency (calibration sub-axis)**. This report supplies counterexamples, not a canonical judgment or score change.

## Findings

### F1 — two NEW red arms at the assigned measured tip

The complete receipt committed in `b99fb79c27042e0f8a598cbbb4d81479a806b518` measures **c019919c**, not b99fb79c, and ends:

```text
FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md 
FAIL  check-ptr   unresolved citation pointers grew (base=3 tip=4)
no-harm FAILED: 2 arm(s) failed
noharm exit=1
```

Neither red has a pre-existing red twin in `w1/ExecNoHarmBase.md`: its identity run reports `corpus-idx` PASS and `check-ptr` PASS with `base=3 tip=3`, then `no-harm OK`, `COMMAND_EXIT_CODE=0`.

**Strongest counterexample:** the coarse `corpus` arm stays PASS because `corpus.index.unindexed` was already a baseline DRIFT kind, but the separately required **corpus-idx** arm detects two newly unindexed files. Treating the coarse PASS as coverage of the enlarged defect population would conceal this regression. The pointer arm independently detects net growth from three unresolved references to four. Its output specifically includes both newly cited round-64 measurement receipts, absent from the c019919c tree.

**Impacted axes:** consistency/calibration directly (receipt provenance and inherited-gate accounting). [INFERENCE] These artifact/index failures do not by themselves demonstrate a changed production G7 verdict or falsify the four new pinning arms; they do prevent an unqualified no-harm assertion at c019919c.

**Smallest safe correction:** retain the negative c019919c receipt. The later b99fb79c commit already adds the two corpus-index rows and the measurement receipts; measure that explicitly declared post-fix candidate against the pinned base and capture its entire output and terminal exit. Never attach a b99fb79c result to c019919c or reclassify these two new reds as inherited informational exceptions. A fixed later revision is a new measurement, not a retroactive repair of c019919c.

This is a fixable artifact/integration defect, not a demonstrated unavoidable axis tradeoff. Canonical disposition remains with the Rust judge.

### F2 — the working receipt is a different, incomplete measurement

At inspection, the requested working-tree `receipts/noharm-tip.txt` contained only 15 lines: a run targeting **b99fb79c**, dated `2026-10-24T04:18:14Z`, ending after `PASS boxproof`. It had seven PASS arms, no remaining 14 gating-arm results, no informational lines, no verdict, and no terminal exit code.

Its `corpus-idx` and `check-ptr` PASS lines differ from the complete c019919c receipt committed at b99fb79c. The b99fb79c commit is a child of c019919c and changes SCORECARD, SHONEN, and corpus/README in addition to adding receipts. Consequently the two target trees are not interchangeable.

**Impacted axes:** consistency/calibration, specifically measurement identity and false provenance.

**Smallest safe correction:** preserve separately named complete receipts for each measured revision, explicitly distinguishing **measured revision** from **receipt-committing revision**. Do not publish the partial b99fb79c rerun as evidence that the assigned c019919c measurement passed. Dependency: a complete b99fb79c run was not available in the inspected working receipt. This leaf did not wait for another seat or poll its run.

## Every gating arm compared

Baseline evidence: `w1/ExecNoHarmBase.md:31–71`. Assigned-tip evidence: the full committed receipt reproduced below.

| Arm | Base==base identity receipt | Base→c019919c receipt |
| --- | --- | --- |
| reg_gate | PASS, exits 0/0 | PASS, exits 0/0 |
| corpus | PASS, no new DRIFT kind | PASS, same baseline kind set |
| corpus-idx | PASS, no new unindexed files | **FAIL: new knowledge/g7-span-pinning-round64.md and lessons/round-64.md** |
| sources | PASS, exits 0/0 | PASS, exits 0/0 |
| checklist | PASS, no new failing check id | PASS, same failing-id set |
| check-ptr | PASS, 3→3 | **FAIL, 3→4** |
| boxproof | PASS, exits 0/0 | PASS, exits 0/0 |
| floors | PASS, exits 0/0 | PASS, exits 0/0 |
| agentdefs | PASS, exit 0, normalized columns identical | PASS, same |
| explicit | PASS, exit 0, normalized columns identical | PASS, same |
| desc | PASS, exit 0, normalized columns identical | PASS, same |
| mcp | PASS, exit 0, normalized columns identical | PASS, same |
| plugin | PASS comparator; underlying exit 1 in both columns | PASS comparator; underlying exit 1 in both columns |
| hooks | PASS, exit 0, normalized columns identical | PASS, same |
| scoped | PASS, exits 0/0 | PASS, exits 0/0 |
| absorption | PASS, tip self-test exit 0 | PASS, same |
| repairs-v2 | PASS, tip self-test exit 0 | PASS, same |
| scoped-v31 | PASS, tip self-test exit 0 | PASS, same |
| battery-self | PASS, changed verdict detected | PASS, same |
| battery-self2 | PASS, injected DRIFT kind detected | PASS, same |
| battery-self3 | PASS, exit-2 guard reported | PASS, same |

Totals: identity **21 PASS / 0 FAIL**; measured c019919c **19 PASS / 2 FAIL**. No gating arm was omitted from this comparison.

### Known nonzero exceptions: twins present, not new red

These lines are byte-identical in the baseline report and the complete c019919c receipt:

```text
PASS  plugin      exit 1 and normalized output identical in both columns
INFO  scoped-rules-v31 --rev 43fe0180 --fetch (optional/live): exit=2: could-not-evaluate: --rev '43fe0180' is not a full 40-hex commit hash
```

The plugin arm is technically a **gating equality comparison that PASSes inherited exit-1 output**, not a FAIL arm or permission for arbitrary exit-1 regressions. The optional v31 live-fetch exit 2 is informational. Neither exception explains `corpus-idx` or `check-ptr`. The other informational lines also match the baseline transcript, including the inherited `reject opencode` summaries.

## Exact command evidence

### Complete c019919c receipt recovered from its committing revision

Command (read-only; exit **0**):

```bash
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show b99fb79c27042e0f8a598cbbb4d81479a806b518:.ufo/waves/round-64/receipts/noharm-tip.txt
```

Full returned content (the embedded battery exit is **1**, distinct from the successful reader command):

```text
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        078eec4a1f6a41c64ff8806f58b46a67cd413bfc
noharm: tip         c019919c97ab5fe98e87a7754b4449ea4e699c99
noharm: sandbox     /tmp/kotoba-r62-noharm.DgdHZ6
noharm: date -u     2026-10-24T04:10:41Z
noharm: column base ready (078eec4a1f6a41c64ff8806f58b46a67cd413bfc)
noharm: column tip ready (c019919c97ab5fe98e87a7754b4449ea4e699c99)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md 
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
FAIL  check-ptr   unresolved citation pointers grew (base=3 tip=4)
        tip: FAIL governance.citation_resolves: evaluated 1190 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from
        tip:  LOG.md:2580: '.ufo/watchdog.log' does not resolve from
        tip:  LOG.md:2602: '.ufo/waves/round-64/receipts/C1-span-measure.txt' does not resolve from
        tip:  LOG.md:2603: '.ufo/waves/round-64/receipts/C2-r64-measure.txt' does not resolve from
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  absorption  check_erratum_absorption.py self-test exited 0 at tip
PASS  repairs-v2  check_routed_repairs_v2.py self-test exited 0 at tip
PASS  scoped-v31  check_scoped_rules_v31.py self-test exited 0 at tip
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
PASS  battery-self2 an injected new corpus DRIFT kind was detected by the comparison
PASS  battery-self3 an exit-2 (could-not-evaluate) column is caught by the comparison guard
--- informational ---
INFO  routed-repairs (C2 predicate; the L1 measures it) exit=0: routed repairs verified 6 of 6
INFO  scoped-rules self-test at tip: self-test: 0 failure(s) over 189 assertions
INFO  scoped-rules --rev tip  --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  scoped-rules --rev base --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  (the inherited C1 control: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)
INFO  scoped-rules-v31 --rev 43fe0180 --fetch (optional/live): exit=2: could-not-evaluate: --rev '43fe0180' is not a full 40-hex commit hash
--- verdict ---
no-harm FAILED: 2 arm(s) failed
noharm exit=1
```

### Working receipt snapshot inspected by `read`

The requested file existed, so the fallback battery invocation was not run by this seat. Its complete inspected contents were:

```text
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        078eec4a1f6a41c64ff8806f58b46a67cd413bfc
noharm: tip         b99fb79c27042e0f8a598cbbb4d81479a806b518
noharm: sandbox     /tmp/kotoba-r62-noharm.F4Ix1g
noharm: date -u     2026-10-24T04:18:14Z
noharm: column base ready (078eec4a1f6a41c64ff8806f58b46a67cd413bfc)
noharm: column tip ready (b99fb79c27042e0f8a598cbbb4d81479a806b518)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-62-verifier-spotcheck.md corpus/lessons/round-63-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=3 tip=3)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
```

No battery exit code was present in that snapshot; none is inferred.

### Revision/provenance commands

Command (read-only; exit **128**):

```bash
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/noharm-tip.txt
```

```text
fatal: path '.ufo/waves/round-64/receipts/noharm-tip.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
```

Command (read-only; exit **0**):

```bash
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show --no-patch --format='commit %H%nparents %P%nsubject %s' c019919c97ab5fe98e87a7754b4449ea4e699c99 b99fb79c27042e0f8a598cbbb4d81479a806b518
```

```text
commit c019919c97ab5fe98e87a7754b4449ea4e699c99
parents 5613392d5a4a14a50753ab0ed5545fe7d85f3d9f
subject round-64: wave-1 integration — C1 G7 span_missing pinning arms (223 assertions, hardened arm 4), C2 r64 routed-repairs counter (32-assertion self-test), LOG corrections block + round-64 entry, S120+entry+lesson+Q60, inherited MutW2SplitClauses edit + ExecW2E2Patch drift note, w1 evidence + controls
commit b99fb79c27042e0f8a598cbbb4d81479a806b518
parents c019919c97ab5fe98e87a7754b4449ea4e699c99
subject round-64: measurements — C1/C2 receipts at c019919c, SCORECARD round-64 annotations + Next-65, SHONEN refresh, README corpus-index rows, w2 spec/dispatch
```

Command (read-only; exit **0**):

```bash
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only c019919c97ab5fe98e87a7754b4449ea4e699c99 corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md corpus/README.md
```

```text
corpus/README.md
corpus/knowledge/g7-span-pinning-round64.md
corpus/lessons/round-64.md
```

## Bounds and tools

- Read the godspeed skill, frozen plan including E1–E3, complete baseline report, and complete battery source. No lane production files, Git/JJ state, or sibling files were changed. Only this requested report was written.
- No battery, test suite, build, formatter, judge, or alternate runtime was invoked. Findings compare existing transcripts and read-only Git evidence; no user-reported failure was rerun merely for confirmation.
- No tools installed or updated. The authorized tooling-rules path `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was read-attempted and returned `not found`; no installation depended on it.
- This audit does not expand the bounded C1/C2 claims into a new predicate. It identifies two concrete inherited-battery regressions at the named measured revision and the separate incomplete post-fix receipt dependency.
