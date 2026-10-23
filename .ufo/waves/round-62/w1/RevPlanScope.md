# RevPlanScope — r62 pre-data shortcut and claim-scope attack

Seat: `KotobaR62.RevPlanScope`. Review date: 2026-10-23 UTC.

**Axes attacked:** calibration first; C1 depth and the operability of its evidence second. This is an advisory plan review, not a claim verdict, admission, or integration decision. FAIL / CONDITIONAL / PASS below classify the specified plan provisions only. The canonical judge retains judgment.

Reviewed `plans/round-62.md` first, at dispatch revision `45a7ecfac9e203297f3146c45d63f5e79367470c`. The plan's working-tree bytes matched its dispatch blob. No candidate instrument, matrix, successor, mutation sweep, live fetch, or other runtime was executed. Hollow controls below are **descriptions**, as permitted by the assignment, not observed r62 control receipts. Historical outputs are explicitly attributed to their committed reports. My only write is this report; no scratch files, index changes, git/jj mutations, installs, dispatches, or peer messages were made.

## 1. Findings at a glance

All plan line numbers below refer to the reviewed dispatch blob `e50fa66a1933e55166c241802b4dd83afe3e4785`.

| ID | Status | Plan lines | Counterexample / finding | Impacted axes | Smallest safe correction |
| --- | --- | --- | --- | --- | --- |
| F1 | **FAIL** | 35, 40–50, 69–71, 88–92 | C1 has incompatible after-values: `surviving 2` versus `surviving 1`; its definition of measured also requires every instance rejected, contradicting either survivor count. | calibration, depth | Preserve the frozen declaration, append a pre-data erratum identifying the conflict, distinguish measured from rejected, and declare one internally consistent result tuple before running data. A changed predicate is a separately identified measurement, not a silent correction of the frozen one. |
| F2 | **FAIL** | 35, 47–50, 94–98 | On the `surviving 2` target, E2f's two instances already pass. Replacing its guard by an admitting stub cannot change either verdict, although the isolation arm says **each** mutation must change its erratum's verdicts. | calibration, depth | Require zero cross-class changes for every mutation; require the two own-class reject→accept flips only for an erratum actually scored absorbed. Print zero flips for an unabsorbed pair; do not count them as a kill. |
| F3 | **FAIL** | 53–56, 94–98, 156–158, 232–233 | A per-label lookup or a source-presence lookup can fabricate both seeded directions and the diagonal mutation matrix. A constant-printer receipt is not a receipt killing either stronger shortcut. | calibration, depth | Define the mutable component and an independent driver, with generated content variants and renamed IDs; commit named label/presence control receipts under the frozen predicate before data. |
| F4 | **FAIL** | 94, 186–188, 212–213 | Ten fixed attacks, five fixed benign controls, and five fixed guard mutations do not satisfy Q47's non-fixed-equivalent requirement for a mutation-kill **claim**. A published lookup table can satisfy the two-sided results. | calibration, depth | Generate semantics-preserving equivalents at measurement time after candidate freeze and record the generated cases/seed for replay; otherwise keep the fixed mutation matrix as a bounded record, not claimed mutation-kill discrimination. |
| F5 | **CONDITIONAL** for unconditional constants; **FAIL** for a frozen-counter remap | 123–152, 154–165 | Base=0 and H1/H2 do distinguish an evaluator returning 6 everywhere or 0 everywhere, **if those evaluations really run**. They do not distinguish a frozen scorer plus a fixed D/H exception table. No C2 shortcut-control receipt is named. | calibration | Commit an independent constant-control receipt and a remap receipt, including a paired real-tree roster perturbation with unchanged repair text. The frozen-counter dishonest receipt is a before measurement, not a successor control. |
| F6 | **CONDITIONAL** | 109–119, 134–148 | C2 declares one concrete summary and one command. Replay of its real tip component still needs a named data revision and committed implementation; `round-62 data revision` is not yet an immutable input identifier. | calibration, operability | Have the committed receipt name the exact instrument bytes and measured revision, with the base/tip CLI outputs and exits. Do not infer a tip pass from the synthetic self-test. |
| F7 | **PASS** at declared dependency scope | 29, 73–86, 112, 123–144 | C1 can run against scoped-rules bytes without C2; C2 can run against repairs/roster bytes without the matrix or v3.1. Exact independent commands are in §4. | calibration | Keep those dependencies separate in implementation and receipts. A shared tip commit does not itself make the claims causally dependent. |
| F8 | **FAIL** | 64–71, 179–181 | Missing G7 does not logically imply that every legitimate E2f specimen survives other A2 checks. Calling any 5/5 result a counter defect prejudges fixture membership from the desired outcome. | calibration, depth | Freeze class eligibility independently of the desired verdict. Record unexpected 5/5 unchanged; distinguish a falsified prediction from an independently established fixture/counter defect. Never select replacement instances to restore 4/5 under the original measurement. |
| F9 | **CONDITIONAL** identity boundary | 105–107, 139–144 | The motivation names registry-roster re-derivation, but G-a defines a filename-regex census, not membership in `swarm-registry.json`. Those authorities can disagree. | calibration, depth | Either call it the explicitly bounded name-pattern count, or derive the roster count and check membership. Do not credit the former as the latter. |
| F10 | **FAIL** sequencing ambiguity | 154–168 versus 207–216 | The before receipts are required before any data in §Controls, but commit-order step 5 puts `before receipts` with the data. The C2 remap/constant receipts and the C1 presence/fixed-list receipts are absent from the named pre-data list. | calibration | Unambiguously put all relevant before/control receipts in the pre-data commit, with data later. A promise to falsify in wave 2 does not repair a missing pre-data control. |
| F11 | **CONDITIONAL** universal wording; **PASS** for C2's bounded universe | 23–24, 55–60, 73–76, 123–137, 232–233 | `gap is closed`, `a presence counter cannot pass it`, and self-detection of any hollow printer overstate the finite observations. C2's six D trees and two H trees are explicitly bounded and do not themselves claim all dishonest/honest repairs. | calibration, depth | Keep C1 results explicitly sample-bound and name the particular shortcuts killed. Retain C2's bounded universe. A hash pin is evidence about pinned file bytes, not by itself every imported/executed dependency. |

These are fixable declaration/control defects. The tradeoff that cannot be disguised is preserving a published fixed-list-only mutation exercise while claiming Q47-style discriminating power: if left unchanged, it must remain a record rather than the stronger claim. Likewise an honest miss by v3.1 is not completion of C1's promised successor after-state; lines 83–85 correctly allow reporting the miss, not turning it into a pass.

## 2. Cheapest hollow controls and the receipts that must kill them

### 2.1 C1: label auditor

**[INFERENCE / described control, not executed.]** Take the *real* frozen scoped-rules file, verify its real digest, and use the real frozen instance catalogue. Do not evaluate its guard functions. Instead return a table keyed by `(erratum ID, instance ID, disabled guard ID)`:

```text
For E2, E2b, E2c, E2e:
  original: rejected, rejected
  own guard disabled: accepted, accepted
  every other guard disabled: rejected, rejected
For E2f:
  original and every disabled-guard state: accepted, accepted
For seeded rejected control pair:
  original: rejected, rejected; its guard disabled: accepted, accepted
For seeded accepted control pair:
  original and disabled: accepted, accepted
For each published benign control:
  accepted in every relevant state
```

This table supplies `absorbed 4 of 5; surviving 2; controls 2 of 2` and all attainable isolation observations without measuring any attack's content. It also exposes F2: E2f has zero flips, so a requirement that all five mutations flip cannot coexist with the headline. Fake reason lists can be taken from literal arm labels; the instrument need not derive them from the input.

**Required killer:** the existing target `.ufo/waves/round-62/controls/absorption-hollow.txt` must at least identify which component was replaced and what independent driver rejected it. A separate proposed target `.ufo/waves/round-62/controls/absorption-label.txt` should record the stronger label-table control under the same frozen predicate, not merely a single constant result.

**Does the written control kill it? No such kill is specified.** Lines 53–56 supply two *known* seeded outcomes; labels can encode both. Lines 156–158 only promise a constant-printing variant. If the whole `--self-test` implementation is replaceable, a program that prints the frozen line and returns zero cannot detect its own hollowness. If only an evaluator is replaceable, that narrower mutation boundary must be explicit and the independent driver must not trust the candidate's expected-result table.

Smallest content-sensitive correction: keep the independent expected verdicts outside the candidate, rename identifiers, supply new semantics-preserving representations after freeze, and actually invoke the evaluator on those input bytes. A label table must then fail on at least one such input; the receipt names that arm. This is a bounded demonstrated kill, not a universal impossibility theorem about cheating programs.

### 2.2 C1: presence counter

**[INFERENCE / described control, not executed.]** Read the actual pinned source and check only for the real strings `url_key`, `reopen_why`, `render_form`, `alias_why`, `alias_sha_why`, `path_site`, and `action_conjunct`. If present, emit the published expected table/summary; use known fixture IDs to supply seeded-control answers. Equivalently inspect whether a disabled function was replaced by the known admitting stub, without calling the original guard. This holds real source bytes but no absorption measurement.

**Required killer:** proposed `.ufo/waves/round-62/controls/absorption-presence.txt`, or an explicitly expanded `absorption-hollow.txt` that records this exact stronger candidate and a changed verdict on a content-sensitive input.

**Written control: not enough.** The sha pin at lines 58–60/164–165 authenticates the same file this shortcut reads; it does not force execution of its guards. The assertion at lines 232–233 that a presence counter cannot pass is not a runnable killer. Q25 explicitly distinguishes a presence/census observable from evidence of the claimed content.

### 2.3 C1: fixed-list mutation matrix, including Q47

**[INFERENCE / described control, not executed.]** Extend the same table to every published guard deletion and benign equivalent. Reject exactly the known guard-deletion signatures and admit exactly the published equivalent signatures; keep the source's guard names and the frozen counter digest intact. This can produce a perfectly diagonal matrix and keep every published benign example while implementing no general distinction between removed and preserved semantics.

**Required killer:** proposed `.ufo/waves/round-62/controls/absorption-fixed-list.txt`, showing that a fixed-list recognizer fails on the measurement-time equivalent set. Record generation after candidate freeze and retain the seed/generated cases in committed evidence so the resulting receipt can be replayed. Merely adding five more published equivalents is not the Q47 correction.

**Written control: fails the Q47 design condition.** Lines 186–188 and 212–213 freeze the finite catalogue; lines 94–98 name Q47 but specify isolation rather than non-fixed equivalents.

**Strongest already available counterexample, not a new run:** committed `.ufo/waves/round-58/controls/CtlC2SourceGrep.md:9–15` describes a source-only shortcut that immediately returned before the behavioral tests, normalized two published spellings, and keyed on the known mutant strings. Its pasted shortcut result at lines 85–105 is:

```text
sweep mutants killed 11 of 11; equivalents survived 5 of 5
```

with exit 0, despite not calling the claimed behavioral sweep. This is the incident explicitly cited by `corpus/QUALITY.md:58` (Q47). It is direct local evidence that “two sides plus a fixed list” is insufficient; it is not evidence that the unbuilt r62 instrument has already been exploited.

### 2.4 C2: constant returns

**[INFERENCE / described controls, not executed.]** Replace only the successor's evaluator by `(6, six ok findings)` for every input; separately replace it by `(0, six missing findings)`. Do not alter the independent test driver. The first must fail the base-world arm; the second must fail H1/H2. A third, stronger shortcut returns constants by known world/fixture identity rather than returning one constant globally.

**Required killer:** proposed `.ufo/waves/round-62/controls/repairs-constants.txt`, with the real frozen predicate invocation, exact mutation boundary, failing arm, and exit for each control.

**Written control:** lines 150–152 are a sensible **nominal discriminator for the first two controls**, conditional on computed evaluations and a retained independent driver. They do not kill per-world constants. No such C2 successor control receipt appears in the named list at lines 154–165. `.ufo/waves/round-62/controls/frozen-repairs-dishonest.txt` measures the old scorer's before behavior; it cannot demonstrate that the new scorer rejects a shortcut.

### 2.5 C2: frozen-counter remap

**[INFERENCE / described control, not executed.]** Import the real, unchanged `check_routed_repairs.check_repairs`, execute it on the real input blobs, and return its score except for a small exception table: the six known D fixture fingerprints map to 5; H1's known house-style fingerprint maps to 6; base remains 0; the known passing tip remains 6. A context/fixture-ID branch can substitute for fingerprints if fixtures are exposed that way. This uses real findings and can satisfy the published summary while never deriving the r60 report count from the measured tree.

A content-grounded paired control is stronger than arguing about labels. The current frozen scorer receives only five repair blobs (`check_routed_repairs.py:142–149`) and computes its six booleans without a roster input (`:71–119`). Consider two committed input trees with **identical five repair blobs**:

```text
T29: declared committed count 29; measured name-pattern population 29
T30: same five repair blobs; add one matching report-name entry under
     .ufo/waves/round-60/build/, giving population 30
```

For the plan's G-a, unchanged `committed 29` must pass that conjunct in T29 and fail it in T30. A scorer depending only on the frozen result and those unchanged blobs cannot distinguish the pair. It must either pass the stale count or reject the honest count. A separate variant updating the declaration to 30 checks that the successor is not merely hardcoded to reject population 30. These are requested controls to construct, not existing r62 committed trees.

**Required killer:** proposed `.ufo/waves/round-62/controls/repairs-remap.txt`, running the frozen predicate against the remap implementation, with independently supplied paired tree populations and generated D/H representations. H1 must also exercise the public CLI on an honest committed input, rather than only a helper map. Preserve all old-counter scores as separate before observations.

**Written control: no specified kill.** D1's one fixed `(30, 29)` case can be special-cased, and importing the old scorer proves only that the old computation ran. The plan needs a change in the result when the relevant *tree input* changes, not a promise that D/H results are “computed.”

Local evidence is not hypothetical about the old scorer: `.ufo/waves/round-61/wave/ExecC2Audit.md:122–188` records dishonest real-text variants passing the old counter, including bodyless census, negation, wrong pointer direction, and a tree with no r60 build directory. I did not rerun those reported failures. The currently committed source independently shows why the tree-population pair is indistinguishable to a frozen-score-only remap.

### 2.6 Receipt inventory and order

The plan currently names only:

```text
.ufo/waves/round-62/controls/absorption-hollow.txt
.ufo/waves/round-62/controls/absorption-before.txt
.ufo/waves/round-62/controls/frozen-repairs-dishonest.txt
```

plus the scoped-rules digest in the instrument/control receipt. The five additional receipt paths above are **proposed targets only**, not files created or results observed by this seat. The v3.1 successor is also part of C1: its new raw-tokenizer arm must not gain credit from printing `E2f fresh instances reject 2 of 2` without the corresponding computations and positive-side preservation. The C1 control coverage must explicitly include that second measurement path.

All relevant shortcut controls and before receipts must precede the matrix/successor data runs. Resolve the contradictory `before receipts` placement in commit-order step 5. A receipt for a failed candidate is a control receipt; a green self-test of the actual candidate is not by itself a shortcut-control receipt. Q37's other applicable shortcut surfaces, including import shadowing, are not discharged merely by pinning the scoped-rules file.

## 3. One concrete after-state, one command, committed bytes

### C1 — FAIL as written

Exact plan sentence, lines 88–92:

> **Before → after.** Before: no committed receipt measures any erratum against the landed counter; the five amendments are evidenced against plan text only (`grep` over `.ufo/waves/round-61/` receipts for per-erratum arm-level results prints 0 of 5). After: `errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2` (the matrix), and the successor's `E2f fresh instances reject 2 of 2` with worlds/eligible unchanged.

Frozen matrix command, lines 28–30:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_erratum_absorption.py --self-test
```

Frozen successor command, lines 78–80:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py --self-test
```

The matrix command alone cannot rederive the entire after-state, which also promises a successor result. It could be a concrete **tuple** rather than a scalar, using the single compound command in §4, but the plan must name that tuple and resolve F1 first. In particular:

* Lines 35/91 say `surviving 2`; line 69 says `surviving 1`.
* Lines 45–46 say every one of the ten instances is rejected; either nonzero survivor count contradicts that definition.
* Four absorbed classes imply eight rejected instances, but **do not by themselves determine the fifth pair's number of survivors**. A class can fail absorption because of a surviving member or because the disabled guard does not admit it. The total must be measured, not inferred from `absorbed 4`.
* The before claim gives no exact grep expression, input-file set, or counter-to-class mapping; the informal mention of grep is not a re-derivation command for `0 of 5`. This does not establish the opposite baseline; it leaves the claimed baseline unauditable as written.

The new files were not present in the verifier inventory when inspected. That is expected at the build stage, not a separately discovered implementation failure. These are planned commands, not successful runs.

### C2 — concrete declared value; committed replay CONDITIONAL

Exact frozen statement, lines 112–121: the following command “prints” the stated line “and exits 0”:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --self-test
```

```text
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
```

Exact after sentence, lines 146–148:

> **Before → after.** Before (re-measured, committed receipt): frozen counter `dishonest accepted 6 of 6; honest passed 1 of 2`; base 0 of 6. After: successor `dishonest rejected 6 of 6; honest passed 2 of 2`; tip 6 of 6.

This is a single unambiguous declared result. It is reproducible over committed input **only if** the self-test actually performs the stated base/tip CLI runs, the receipt names the immutable data revision and instrument bytes, and all synthetic trees/expected findings are committed or deterministically reconstructed from committed bytes. The plan currently names the base fully but only calls the tip “round-62 data revision” (136–137). It gives no exact revision-bound tip CLI command yet. Neither the missing future hash nor the unbuilt script is a current pass or an excuse to substitute a fixture-only result.

The old counter's CLI spelling is evidenced at `check_routed_repairs.py:122–158`; the new counter's CLI implementation was not available for inspection. I do not assert that it already implements `--rev` or that its self-test has passed.

## 4. Causal separability: exact independent commands

**PASS for the plan's declared dependencies; actual implementation remains unrun.** These commands use absolute paths because this seat starts at the fleet root.

C1's complete promised tuple can be checked independently of C2 with:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_erratum_absorption.py --self-test && python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py --self-test
```

C2 can be checked independently of C1 with:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --self-test
```

The first compound command is an explicit proposed aggregation of the plan's two C1 commands, not a new implemented CLI. The scopes are independent: C1 uses the frozen scoped-rules module, its instance inputs and v3.1; C2 uses the frozen repairs module, repair blobs, and r60 report-name population. Nothing in C2's stated G-a..G-f requires `check_erratum_absorption.py`, S118, or v3.1. Nothing in C1 requires the repairs successor's verdict. C1's dependence on its **own** successor is not dependence on C2.

Implementation must not introduce a shared `r62 success` boolean, a C2 fixture harvested from C1's *claimed* output instead of committed repair evidence, or a self-test that imports the other new gate as a prerequisite. A common measured commit is fine; a shared asserted result is not. The old scoped-rules no-harm `--fetch` is a separately reported live check, not a replacement for the committed-byte absorption result.

## 5. Expected-result bias and the 5-of-5 kill rule

Exact sentence, plan lines 68–71:

> The matrix is therefore expected to report **E2f unabsorbed** with its event-claim instance surviving: `absorbed 4 of 5; surviving 1` (the count printed is computed; if it prints 5 of 5 the frozen E2f instances were not the erratum's class and the round records a counter defect). The other four errata are expected absorbed.

**Naming the written kill:** at 5/5 the plan calls it a counter defect, rather than accepting a larger score. Its exact frozen 4/5 target is not met. That is a useful anti-score-inflation intention, but the stated *reason* is not established by that number.

**Counterexample to the inference:** a genuine unsupported event/load claim can also contain an unsupported content word, cite an unhelpful line, or fail the forward/reverse fraction. The existing `action_conjunct` rejects those at `check_scoped_rules.py:1018–1039`, without G7. Disabling the whole action guard admits such a specimen. The pair may therefore meet the plan's definition of “absorbed” even though the implementation lacks an event-specific conjunct. It remains an event-claim specimen; a 5/5 result does not prove it belonged to the wrong class. Conversely, one can add backticked false event text that `content_words` erases (`:972–977`), making a suitable survivor plausible. Neither direction is measured here.

Committed r61 evidence makes the distinction explicit: `MutA2.md:214–224` warns that real eligible actions are paraphrases and that raw claim detection must not use the tokenizer that erases event names. At `:321–338` it also places F6's non-load compound-purpose attack **outside** the frozen load/event arm. Thus “no G7/G9 implementation” is not a single outcome oracle for arbitrary E2f inputs, and F6 cannot silently replace an event-claim survivor to force the expected count.

**Smallest safe rule:** freeze an independently reviewable E2f class criterion and its two specimens before measurement. If 5/5 prints, preserve that exact output and mark the frozen 4/5 prediction unmet. Apply an independent class/content audit to distinguish (a) genuine but incidentally caught E2f examples, (b) invalid examples, and (c) an instrument defect. Do not relabel, discard, or tune the original specimens to get 4/5. A changed matrix is a second measurement beside the declared one under Q28, with its own controls. The lesson's prewritten E2f-gap story at lines 179–181 must remain a hypothesis until that evidence exists.

## 6. Universal clauses, identity, and premature saturation

### C1

* **FAIL if interpreted universally:** `a presence counter cannot pass it` (233), and a hollow line printer necessarily failing the second control (55–56). The lookup constructions above defeat those inferences from the listed finite observations. Replace these with the exact named candidate/control receipt outcomes, once run.
* **CONDITIONAL:** `The E2f gap is closed` (73). The target at 82–83 measures two new instances plus preservation of seven worlds/four eligible rows. It does not establish that every event-claim counterfeit is excluded. Safe phrasing is “the two frozen E2f instances are rejected by the separately named v3.1 measurement”; keep F6/G9 explicitly surviving as 75–76 already requires.
* **CONDITIONAL:** `absorbed` could imply an entire attack class at 23–24. Lines 47–50 do provide a two-specimen operational definition. Keep that bound visible on the entry, registry annotation, lesson, and SCORECARD; do not turn it into a universal security/semantic assertion.
* **PASS for the intended identity separation:** old `check_scoped_rules.py` stays pinned and unmodified (58–62, 85–86), and v3.1 has a different path. A v3.1 success must not be reported as the old frozen counter absorbing E2f. A hash comparison alone also does not prove import provenance; execute/load the file whose bytes were pinned and do not count an import-shadowing shortcut as killed without a receipt.

### C2

* **PASS for boundedness:** lines 123–137 enumerate six dishonest trees and two honest worlds. `dishonest rejected 6 of 6` is not “all dishonesty rejected,” nor does `honest passed 2 of 2` mean every house-style repair passes. Preserve that exact universe.
* **CONDITIONAL identity drift:** the motivating quote at 106–107 names registry-roster re-derivation. Yet G-a at 139–142 counts regex-matching filenames. A non-roster file with a matching name increases that census while leaving actual roster-member receipts unchanged; a recursively nested matching basename also requires an explicit interpretation of the `ls-tree` full paths. These are different populations. The committed prior audit, `ExecC2Audit.md:343–362,373–385`, explicitly identifies registry membership minus missing reports as its authority. The plan may define a narrower name census, but must not falsely attribute registry honesty to it.
* **PASS for successor identity:** the six old repair checks remain a separate frozen measurement (123–125), rather than being silently rewritten. The current frozen checker itself says it does not judge substantive repair honesty (`check_routed_repairs.py:34–37`). Its score is not provenance for calling the new H2 tree substantively honest.

No saturation/retirement decision is made here. The plan's calibration score of 10 (5–8) does not waive its control obligations, and the open owned-versus-all-axes issue at 6–8 is explicitly an L0 question rather than this seat's ruling.

## 7. Evidence identity and observed command receipts

All commands below were read-only identity/clock observations, not behavior verification. They were collected in this review on 2026-10-23 UTC. The separately collected UTC clock receipt was:

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'
```

```text
2026-10-23T20:50:33Z
```

Exit 0. This is the clock observation, not a claim that every subsequent read occurred in that same second.

### Working-tree SHA-256 identities

Command:

```sh
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-62.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
```

Output, 2026-10-23 UTC (same collection batch as the UTC clock above):

```text
5c6067c4d453f47a8149a05b969ab9b2755026c6d0ea09771eb49199f32f734c  /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-62.md
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
```

Exit 0. The last digest identifies the current frozen file; it is not represented as the earlier audit report's `9ee77d47…` revision.

### Committed evidence membership

Command:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree 45a7ecfac9e203297f3146c45d63f5e79367470c -- plans/round-62.md verifiers/check_scoped_rules.py verifiers/check_routed_repairs.py .ufo/waves/round-61/wave/ExecC2Audit.md .ufo/waves/round-61/wave/MutA2.md .ufo/waves/round-58/controls/CtlC2SourceGrep.md
```

Output, 2026-10-23 UTC; exit 0:

```text
100644 blob bd5764ab22d33ac4de874d6ba24287c01f7b97e1	.ufo/waves/round-58/controls/CtlC2SourceGrep.md
100644 blob 7d0dfe6c1b700f7361103a4b95545a19aa9422ce	.ufo/waves/round-61/wave/ExecC2Audit.md
100644 blob c9f6e9a0e4d60bc1ba9c054a05a0e9be198a9762	.ufo/waves/round-61/wave/MutA2.md
100644 blob e50fa66a1933e55166c241802b4dd83afe3e4785	plans/round-62.md
100755 blob 56b86f61004ff2e9d319d8cc87459b5cd702b51f	verifiers/check_routed_repairs.py
100755 blob fed067aae805d7815ccbfe3801873939853d4491	verifiers/check_scoped_rules.py
```

Binding the read files to those committed objects:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin hash-object /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-62.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-61/wave/ExecC2Audit.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-61/wave/MutA2.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-58/controls/CtlC2SourceGrep.md
```

Output, 2026-10-23 UTC; exit 0:

```text
e50fa66a1933e55166c241802b4dd83afe3e4785
fed067aae805d7815ccbfe3801873939853d4491
56b86f61004ff2e9d319d8cc87459b5cd702b51f
7d0dfe6c1b700f7361103a4b95545a19aa9422ce
c9f6e9a0e4d60bc1ba9c054a05a0e9be198a9762
bd5764ab22d33ac4de874d6ba24287c01f7b97e1
```

`hash-object` was used without `-w`. No object or index was written.

### Honesty boundary

No r62 control, self-test, matrix, successor, or live check has passed **in this seat's work**. No empirical claim is made about the behavior of future executor drafts. The missing prerequisite for empirical confirmation is the integrated candidate implementation plus its independently specified pre-data control harness/receipts; that is build work assigned elsewhere, not a blocker to this completed plan attack. Proposed corrections and target receipt names above have not been integrated.

Installs: no installs.
Blockers: none.
Attacked: r62 C1/C2 pre-data shortcut discrimination, concrete after-values, causal independence, expected-result bias, and bounded claim provenance.
