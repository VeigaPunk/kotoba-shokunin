# C2 design attack — operability

## Findings first

**Rating: fails as sized; holds-bounded as a prospective capability after correction.**
This is a design finding, not an admission judgment or a verdict on the parallel build.
The proposed capability is useful; its declared counter does not measure its claim.

### 1. The after-value is an R2-class content-blind counter

`plans/round-49.md` C2 calls the change “boxes executed” but measures only disposition strings.
Its jq command does not inspect the delegated file at all. Even conjoining
`checklist.box_map_complete` proves only existence plus instrument-shaped bytes,
not that dispatch.04 or dispatch.08 runs, has subjects, or rejects defects.

Strongest counterexample: in a private clone, mapping both boxes to the unrelated
existing `verifiers/verify_harness_independent.py` yielded counter **2** and map
check **PASS**, exit 0. No dispatch instrument was created. A file containing
only `#!/bin/sh\n` also yielded **2**, map **PASS**, exit 0.
The latter is 10 bytes, not the “two-byte” label mistakenly printed by the probe.
Control: mapping dispatch.04 to `README.md` failed the map check, exit 1.

`delegated:` semantically assigns enforcement to another instrument; a truthful
“box executed” claim therefore requires that instrument to implement the box.
The schema's enforcement is much weaker. The docstring explicitly acknowledges
that the check never runs delegated instruments (lines 247–249).
This is not permission to credit an unrelated or narrower instrument as full execution.

### 2. Both boxes need an explicit mechanical contract

**dispatch.04:** mechanically checkable only after declaring report-path extraction,
placeholder/variable grammar, and lane identity. The id must have an authoritative
binding, not merely agreement between two attacker-controlled strings.
A wrong filename plus matching wrong report stem can satisfy filename-derived identity.
Scanning every `<...>` span is not the stated rule: kotoba-round-10.md line 11 has
an intentional L0-side-channel `<lane>` template outside the report path;
kotoba-round-49.md lines 197 and 271 have command-template placeholders.
`aggregator-L1.md` reports to `AGGREGATE.md`: either explicitly exclude non-lane
roles or report this mismatch rather than silently adding an exception.

**dispatch.08:** the state clause is part of the box, not optional context.
`kotoba-round-49.md` line 1, its filename, and its report directory agree on 49,
but `.ufo/state/kotoba.round` contains 16. A check omitting the state comparison
would pass a concrete input the full box rejects. Missing state files cannot be PASS.
Literal execution may correctly FAIL stale fleet prompts; that is not an instrument defect.
The false premise that the state file holds the latest round must be exposed, not hidden.

Smallest safe choices: implement the entire current box and disclose its live failures,
or change the box before landing to name the intended authority and re-pin its text hash.
Do not silently substitute MANIFEST, omit the state clause, or count only token equality
as full dispatch.08 execution. A SKILL annotation can name a bounded approximation,
but cannot make an omitted conjunct true. Q20/Q23-style disclosure belongs in the
box/annotation and every surface claiming this capability, with run examples of
misses and over-flags. Delegated boxes currently have no enforced annotation check;
only `executed:` annotations are checked at verifier lines 1180–1203.

### 3. Strongest alternative after-value

Replace the metadata-only after-value with **2 box-bound, content-tested executed rules**.
Use one committed recheck command over a committed fixture corpus: emit 2 only when
both named boxes have evaluated subjects, valid controls pass, each conjunct has a
must-fail mutation, and replacing the delegate with a no-op/unrelated instrument
makes that same recheck fail. Otherwise exit nonzero, not “2”.
Bind the tested rules to the map's box text hashes; document any bounded parsing model.
The disposition count may remain supporting evidence, honestly labelled “map entries”.
This keeps §6.9's one concrete value/one command without claiming fleet-wide cleanliness.
No after-value for the actual parallel build was observed in this review.

### 4. Capability-table row is conditional, not justified by the map flip

AXES.md § Capabilities requires a demonstrated running capability and evidence pointer.
A bounded dispatch-prompt linter can merit a row after an observed passing self-test
and a real run with truthful PASS/FAIL/N/A results and scope; a dirty fleet scan need
not mean the linter is broken. The row must not imply fleet compliance or full-box
coverage if it implements less. Pin fleet input bytes: a new mori-round-25.md appeared
during this review, so a live directory count is not reproducible from lane bytes alone.
Update the current live-count claims in SKILL.md:126–127 and corpus/README.md:84–88
when dispositions change; both currently describe 8 executed / 0 delegated / 33 unexecuted.
Prior local warning: LOG.md:645–648 records a delegated instrument that never scanned
SKILL.md and therefore did not enforce its assigned box; round 16 replaced that mapping.

Impacted axes: **operability** directly; consistency and discernment if metadata is
credited as execution or a stale authority is silently replaced. No score recommendation.

## Evidence and receipts

Lane base observed: `git rev-parse master HEAD` → both
`a5adc146a2995dcc5a95a6d8db6e5674f75191ac` (exit 0).
Private clone: `/fast/scratch/hyaku/kotoba-r49/seats/CriticC2Sizing/clone`.
Commands below ran there, not in the lane; the clone map was restored afterward.

- C2 jq command from the plan: base 0; stub arm 2; unrelated-instrument arm 2 (exit 0).
- `python3 verifiers/verify_skill_checklist.py --check checklist.box_map_complete`:
  base PASS/0; stub PASS/0; unrelated instrument PASS/0; README control FAIL/1;
  restored map PASS/0. These are map checks, not dispatch execution tests.
- `python3 probe.py /home/vgpnk/Projects/shokunin` (scratch script, exit 0),
  2026-10-22T09:42:43Z: 286 top-level files; 273 matching round files;
  148 exceed state; 14 lack state; 7 report-stem mismatches; 6 report placeholders;
  237 files contain angle-bracket placeholders somewhere. This exploratory regex
  probe is not a canonical dispatch verifier and its input directory was changing.
- Probe path: `/fast/scratch/hyaku/kotoba-r49/seats/CriticC2Sizing/probe.py`;
  sha256 `c5c551e8f0677c4e7f46cc28d9548e532cee7871c71c98e8b160752afb17abea`.
- `sha256sum` (exit 0), base files:
  verifier `f570e0f909a186c55e14575dedf765d839edb6f3921dd95a18dd6e1698c8a6e7`;
  map `82bf86d60b72f7e165df7f347379d2ffb65268dea811878b09dbd1b52c74df86`;
  SKILL `1923484600b5879c16d390aff43698f0974616946150c0b20787ed5e65d3ee22`;
  plan `05536b72bca5d42d283561501718aec305e9e40fa0935001510068618ce192ad`.
- Required reading: plan C2; verifier lines 1–120, 247–249, 1125–1224;
  SKILL lines 300–330; session prompt §6.9; QUALITY Q20/Q23; AXES § Capabilities.
  `skill://godspeed` was subsequently opened successfully; the earlier filesystem
  search claiming it absent was not conclusive and is withdrawn.

No production edits, patches, admissions, runtime orchestration, or tool installs.
Only this report was written in the lane checkout.
