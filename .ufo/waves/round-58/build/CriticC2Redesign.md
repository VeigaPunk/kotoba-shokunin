Result: DONE — A future v2 should measure executed fixture outcomes under a frozen runner, not source signatures or self-reported assertion totals.

## Scope and impacted axes

Design review only. C2 remains withdrawn; neither round-58 counter, its predicate, its targets, nor its existing receipts should change. This proposal requires a separately frozen future measurement. The round-58 R3 arms remain defect work, not evidence that C2 was rescued (`plans/round-58.md:86-98`). No judgment, admission, integration, or runtime invocation is supplied here.

Primary axis: **operability** — a self-test must actually exercise the correction sweep and discriminate its stated defects. Related risks: **calibration** (calling textual discrimination behavioral coverage), **coverage** (counting duplicates while losing a required scenario), and operability harm from rejecting genuinely equivalent implementations or breaking the CLI while hiding source. These are review concerns, not scored axis moves. Canonical axis definitions: `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/AXES.md:9-16,27-38`.

## Counterexample and local evidence

The strongest available counterexample is already measured; repeating it is unnecessary.

| Evidence | Recorded result | What it establishes |
|---|---|---|
| `controls/CtlC2SourceGrep.md:9-15,75-105` | `sweep mutants killed 11 of 11; equivalents survived 5 of 5`, exit 0 | An early return checks eleven source substrings, canonicalizing the two published regex spellings, while making every original behavioral arm unreachable. |
| `controls/CtlC2Snapshot.md:9-24,57-80` | K=11, E=0, exit 1 | Equivalent survival rejects the exact snapshot shortcut; K alone is insufficient. |
| `controls/CtlC2AllFail.md:30-66,267-291,321-345` | Line count K=8/E=4; case-call count K=4/E=5; both exit 1 | High K and an assertion/case census can reflect source shape rather than sweep behavior. |
| `controls/CtlC2AllFail.md:7-16,175-183,213-237` | Always-1: exit 2 before scoring; always-0: K=0/E=5, exit 1 | Baseline failure is not a killed-mutant result. |
| `controls/CtlC2DoNothing.md:13-29,40-103` | Base and duplicate-clean-case world K=4/E=5, exit 1 | Additional cases and prose need not add coverage. |

Paths in this table are relative to `.ufo/waves/round-58/`. These are inspected prior receipts, not executions by this seat. Their commands and full outputs are at the cited locations.

The mechanism is visible in the frozen counter: `run_self_test` returns only the child's exit (`verifiers/check_sweep_mutants.py:234-255`); `evaluate` accepts any nonzero mutant exit, including a timeout (`:258-273`). It neither verifies that a sweep was executed nor consumes assertion evidence. The positive synthetic fixture also parses case text and probes registry patterns directly (`:150-178,286-313`); it tests counter mechanics, not an actual `sweep(reader(...))` path. Do not promote that fixture into independent behavioral evidence.

### Strongest counterexample to the suggested guards

[INFERENCE, static design attack; not executed] Merely increasing the equivalent family does not repair the trust boundary. A shortcut can inspect registry IDs and evaluate the three declared regexes on fixed positive/negative strings, without invoking `sweep`, `reader`, or the CLI. That survives arbitrary harmless regex spellings without enumerating them. If source files are hidden, live registry objects and code constants remain accessible to unrestricted Python. Printing a plausible assertion total then defeats an output-count floor.

There is direct local support for the last limitation: `verifiers/check_assertion_floors.py:98-103` explicitly trusts child-reported counts and excludes deliberately fake totals. Reuse its summary convention if useful, but do not present that guard as an adversarial authenticity check.

A naive source-blind implementation also causes a false red: the genuine self-test resolves its own script and launches it for CLI error tests (`verifiers/check_correction_sweep.py:235-276`); module initialization derives `LANE` from `__file__` (`:30`). Unlinking the source, removing `__file__`, or substituting a different directory can break those tests or change the repository identity. That is an instrument defect, not successful mutant detection.

## Smallest safe correction: one trusted runner, candidate fixtures as data

**Recommendation:** retain the existing case-helper approach, but make its runner and comparison authority immutable for the future claim. The candidate-controlled surface is fixture data and literal expectations, not an arbitrary Python verdict function. This is a deliberately bounded test interface, not an attempt to sandbox unrestricted Python by deleting its source.

A preparatory, unclaimed migration must preserve the current CLI contract and existing self-test scenarios. The normal `--self-test` and the v2 measurement must use the same runner and the same candidate fixture records. There must not be one meaningful suite in the counter and an unrelated or unreachable suite in the delivered verifier.

### 1. Freeze authority outside the measured candidate

The future manifest pins the trusted runner, allowed edit surface, production functions and registry, dependency-loading policy, fixture schema, defect schemas, equivalence transformations, observation normalization, sample width, mandatory obligation set, and result taxonomy. The measurement loads that manifest from its own frozen revision, never from the candidate.

Use the existing correction rule as the behavioral authority: a stale-containing Markdown block requires the declared pattern in that block, with the existing leading-result condition (`verifiers/check_correction_sweep.py:10-18,116-130`). Do not add a second registry with independently maintained correction facts. Any independent expected outcomes in the measurement are explicitly frozen test expectations for that rule, not a replacement corpus authority.

The scope check rejects executable edits outside the fixture surface, including altered imports, early returns, output remaps, helper replacements, and adjacent modules that shadow dependencies. Its loader accepts fixture literals only; importing the candidate to obtain its fixtures would execute the very code this boundary is meant to exclude. The isolated measurement must not import candidate-side helper modules or inherit Git/Python search-path redirections. This implements the external guards required by `corpus/QUALITY.md:44` (Q33), rather than trusting a plan sentence.

### 2. Execute candidate fixtures; do not infer execution from their text

A fixture records actual input files and independently written expected exit/finding IDs. The trusted runner materializes those files, runs the real correction-sweep path, and compares the actual exit and exact finding identities. Expected values must not be calculated by calling the implementation being tested. Retain file/line and leading-result information where the scenario tests them; do not reduce every observation to a Boolean exit.

The parent owns the execution ledger: fixture identity, input digest, expected/actual result, and completed comparison. Candidate stdout is diagnostic only. The familiar `N assertions` self-test summary can remain, but acceptance uses the parent's completed observations and requires the summary to agree. A child-written JSON event stream is not more authoritative than a child-written integer.

Here, **source-blind** means candidate fixture data has no executable access to target source, registry objects, run labels, or parent state. It does not mean denying the pinned production CLI its legitimate script path. Keep `LANE`, `__file__`, and CLI subprocess behavior intact inside the isolated fixture repository. No candidate-authored Python runs in the measurement process.

### 3. Require semantic obligations and causal witnesses

For each of the three round-57 registry entries, require these independently observed roles:

- stale text with no correction: the exact intended finding;
- the same stale text with its full correction: clean for that entry;
- the same stale text with the weaker near-correction: still the intended finding. For S076/S078 this is a bare `Round-57` note without `correction`; for the singular-agent entry it is `migrate-v1.mdx` without `:486`.

The frozen parent validates the roles from actual fixture content and known test expectations; a fixture's self-assigned name is insufficient. The same candidate witness must pass on pristine production and produce the expected assertion mismatch under its corresponding production defect. A sweep call whose result is ignored is not a comparison. A regex-only helper probe is not a sweep witness.

Preserve the other existing regression and CLI-error obligations. Define the floor as the cardinality of the frozen mandatory obligation set, counting each `(rule, scenario, required route)` once after a completed comparison. Repeated clean cases, renamed cases, padding, extra summary lines, and repeated generated instances of one obligation do not raise that coverage count. Keep the raw comparison total as a separate diagnostic.

Do not silently conflate the old eleven edits:

- M01–M06 alter production registry behavior and need causal behavioral witnesses.
- M07 deletes fixture seeding. A missing required fixture file needs a named fixture-integrity rejection, not credit for an incidental traceback.
- M08–M11 delete tests, not production behavior. Measure loss of the last executed witness for the corresponding red/green obligation. If another genuine executed witness replaces a deleted named case, rejecting it merely for losing that name would repeat the case-count mistake.

Thus the future report has separate production-discrimination, fixture-integrity, and obligation-retention results. It must not relabel them as the frozen round-58 K=11 metric. This distinction changes no round-58 result.

### 4. Generate equivalents at measurement time, with reproducible sampling

Freeze a restricted, semantics-preserving generator, not a small published spelling table. Use 32 distinct composite rewrites from one 256-bit seed drawn and recorded after sealing the candidate revision. Freeze the seed-generation rule and generator version beforehand; record the first draw, and never reroll or discard a failing sample. Publish the seed and exact generated artifacts for replay.

The family should compose noncapturing grouping and literal-character regex spellings for the supported patterns, harmless comments/blank lines, registry order, and fixture order. The required sample schedule includes changed regex spelling and source layout, not merely random comment nonces. Its combinatorial size frustrates exact-text memorization; size is not itself evidence of behavior. Do not pretend to generate arbitrary regex equivalents: only transformations with stated preservation arguments are eligible.

Apply semantic defect operators to the intended production node independently of its spelling; do not reuse brittle `old`-substring applicability. Run the pristine/equivalent and corresponding defective versions across the same generated representations. Every required defect/representation cell must discriminate; aggregate totals must not conceal a missed cell.

Equivalence is relative to the declared observation: equal exit and equal finding identities/locations, disregarding order only where order is explicitly outside the claim. A registry permutation can reorder raw diagnostic lines (`sweep` iterates `REGISTRY`, `main` prints its list); do not call it byte-output-equivalent. Do not sort away an ordering property the claim actually promises.

The parent also derives independent safe variations of candidate fixtures, such as neutral text and valid block-layout variants within the declared input class, with expected results fixed independently of the candidate. This provides Q33's independently constructed input without substituting a separate parent-only suite for candidate-test coverage.

### 5. Require attributable failures and replayable receipts

A production mutant counts only when a real comparison observes the designated semantic divergence after the corresponding pristine comparison succeeded. A generic nonzero exit, syntax error, signal, timeout, source-read denial, missing loader, or malformed summary is not a killed mutant. Fixture-integrity failures have their own named result.

Keep bounded isolated runs, cleared Git pointers, no live-lane access, and receipts containing candidate/runner/manifest hashes, seed, generated input and mutant digests, per-cell results, wall time, and exit classifications. Timeout is could-not-evaluate, with no kill credit; host contention cannot become positive evidence. Unsupported transformation or absent mutation target is also non-credit, never silently dropped from the denominator.

**Future acceptance conjunction:** scope and provenance valid; pristine and all required equivalents complete with correct outcomes; every required production defect has its causal witness in every scheduled representation; fixture-integrity and last-witness deletion controls are rejected for their designated reasons; every mandatory observation cell is completed; summary and parent ledger agree; no could-not-evaluate result remains. This is a proposed future contract, not an implemented or measured predicate.

## Each guard's cheapest remaining shortcut

These are attacks on each guard in isolation. The conjunction is necessary; none earns a universal anti-cheating claim.

| Guard | Cheapest shortcut that still beats it alone | Necessary complement / limit |
|---|---|---|
| Frozen diff scope and literal fixture interface | Leave allowed fixtures empty or fill them with redundant clean cases. | Mandatory semantic obligations and actual mutation discrimination. |
| Measurement-time equivalent family | Check registry IDs and regex behavior directly; ignore spelling and never call the sweep. | Real sweep observations attributed to candidate fixtures. |
| Source-blind candidate evaluation | Supply one valid clean fixture and do no discriminating work. If unrestricted Python is retained instead, inspect live globals/code constants. | Mandatory witnesses; choose the data interface rather than claiming unlinking is an adversarial sandbox. |
| Floor parsed from self-test stdout | Print the required count before returning. | Parent-owned observation ledger; the existing assertion-floor guard explicitly does not close this attack. |
| Parent-owned raw execution/count ledger | Repeat the same successful clean comparison many times, or label one input as several scenarios. | Deduplicated semantic obligation cells and independent validation of scenario content. |
| External behavioral input check | Let the implementation handle the parent's probes while the candidate self-test remains dead. | Bind observed coverage to the exact candidate fixture records also used by delivered `--self-test`. |
| Mandatory causal mutant witnesses | Overfit to the finite published defect/input family while omitting an untested block shape or correction variant. | Generated independent variations and explicit bounded coverage; finite sampling never proves all possible defects are caught. |
| Named failure taxonomy and provenance hashes | Produce an unrelated assertion mismatch only in mutant runs; a hash does not explain why a test failed. | Compare actual/expected observations and their designated causal delta. A hostile or broken trusted runner remains outside this test's proof. |

The remaining bounded-family limitation is not a fixable spelling defect. No finite counter establishes general behavioral completeness or operability saturation. The future claim must name the covered obligations and generator family; a claim of universal shortcut resistance would exceed this evidence (Q26/Q31, `corpus/QUALITY.md:37,42`). Tradeoffs such as rejecting legitimate CLI use or changing a promised output order are harm to report to the canonical judge, not costs this critic may silently admit.

## Why the supplied worlds cannot satisfy this design

[INFERENCE — architectural rejection paths, not v2 executions.]

| Supplied world | Required rejection / non-credit reason |
|---|---|
| SourceGrep | Its executable early return is outside the fixture edit surface; source membership is neither a completed sweep comparison nor a causal witness. The design does not rely solely on adding unlisted regex spellings. |
| Snapshot | Same authority violation; hashing source supplies no fixture observations. Source-layout equivalents additionally contradict its acceptance rule. |
| Line count / case-call count | Same authority violation; neither supplies observed semantic cells. Renaming or padding fixtures cannot raise deduplicated coverage. |
| Always-0 / always-1 | No discriminating comparisons; the latter also lacks a valid pristine result. Neither receives mutation credit. |
| Do-nothing / duplicate-clean-case padding | They may remain valid baseline suites, but cannot meet the newly required near-correction witnesses or discrimination cells. Duplicate clean comparisons add zero obligation coverage. |

A future control wave must include valid-interface versions of empty/padded fixtures, false expectations, forged summaries, discarded real sweep results, and parent-only probes with a dead candidate suite. It must also include a genuine positive suite and a genuine CLI-preserving equivalent suite. Otherwise merely making the old shortcuts syntactically ineligible would be hollow hardening. The same frozen composite and sampled representations must be used on all these controls before any future claim data; failed controls do not license changing the frozen round-58 instrument.

## Work performed and provenance

Read both required counters, the actual correction-sweep path, all four C2 control receipts, the plan erratum, the existing assertion-floor trust boundary, and the relevant corpus criteria. No counter, self-test, probe, mutant, sandbox world, or lane code was executed by this seat. No external sources were fetched and no tools installed or updated. Only this report was written.

Two read-only receipt-binding checks were run from the lane. Both exited 0; neither executes the Python bytes:

```sh
set -o pipefail && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git --no-optional-locks show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_sweep_mutants.py | timeout 30 sha256sum
```

Observed output:

```text
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  -
```

```sh
set -o pipefail && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git --no-optional-locks show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_correction_sweep.py | timeout 30 sha256sum
```

Observed output:

```text
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  -
```

These match the frozen counter/target hashes recorded in `controls/CtlC2SourceGrep.md:148-151`, `controls/CtlC2Snapshot.md:127-131`, and the other controls. They bind the inspected baseline evidence, not a claim that v2 exists or has passed anything.

Report: .ufo/waves/round-58/build/CriticC2Redesign.md
