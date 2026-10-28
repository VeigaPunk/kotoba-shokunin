Kb81L02Ctl — counter-independence probe (Round 81 w1)

## Axes

- **Consistency / calibration (C1):** measured-revision instrument execution is disclosed, but the pin guard has a mechanically exploitable gap; the declared target is not independent of newly added code.
- **Depth / sourced (C2):** the planned counter measures evidence-shape conformance. An independent generator can populate that shape; semantic depth is not measured by this predicate and the plan does not declare a form-level headline or assign a Q74 generator score.
- **Operability:** both defects have small, concrete amendments/controls; no lane files were changed.

## Counterexample — decisive C1 laundering world

At the lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`, I made an isolated scratch clone, asserted its top-level was the clone, and added exactly one new file: `verifiers/argparse.py` containing `raise SystemExit(0)`. No pinned instrument was edited. Commit: `d8a8997cd747ae08a0f6e2fcff9c29a6464471ae`.

Exact measured command:

`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py --repo /fast/scratch/hyaku/kotoba-r81/Kb81L02Ctl/clone --rev d8a8997cd747ae08a0f6e2fcff9c29a6464471ae`

Observed exit **0** and final line: `fleet root /fast/scratch/hyaku/kotoba-r81/Kb81L02Ctl; guards 5 of 5; tip battery exit 0: 6 of 6`. All six battery scripts import `argparse`; when Python runs `verifiers/<script>.py`, the script directory is import-searchable, so the revision-added sibling shadows stdlib `argparse` and exits 0 before each gate runs. The size guard only measures the six `BATTERY` paths; `INSTRUMENT_PINS` only checks those named paths. The new sibling is not deleted, size-checked, or pinned. `-B` does not isolate imports. Direct micro-probe confirmed the shadow: importing `argparse` with this file exits 0 before the probe body. A `sitecustomize.py` attempt did not auto-load (negative control); the counterexample uses `argparse.py`, which is actually imported by all six instruments.

The world receipt and micro-probe are `.ufo/waves/round-81/build/Kb81L02Ctl-shadow-world.txt` and `.ufo/waves/round-81/build/Kb81L02Ctl-shadow-microprobe.txt`. The world is a counter defect, not a reason to narrow the claim: it reaches the target while all the base's corpus/pointer defects are still present.

**Smallest safe correction:** close the code-import surface, not only the six entry-point blobs. Reject unreviewed additions under `verifiers/` (allow only explicitly reviewed/pinned new files such as the planned C2 counter), or otherwise make all Python subprocesses immune to checkout-local shadow modules, including instruments' nested self-test subprocesses. Add this exact `verifiers/argparse.py` control to the amended/frozen counter. `-I` on the outer battery launch alone is insufficient if an instrument spawns a non-isolated Python child. The plan's W4 stubbing test does not cover this sibling-module class; Q37's same-frozen-counter script-shadow control does.

## Q33 — C1 trust boundary and circularity

`check_tip_battery.py` does execute code from the measured revision: `run_battery()` constructs `[sys.executable, "-B", script]` and sets `cwd` to the sandbox checkout. The plan's E6 sentence does declare the intended boundary: every battery instrument at the measured revision must equal a base blob or reviewed pin; it also names `instrument-pin` as the anti-laundering guard. That is the circularity declaration, and the counter's own SHA is intended to be recorded in `freeze-shas.txt` before outcomes. However, the live shadow world proves the declared guard does **not** cover the actual Python import closure. The five guards run in the outer counter cannot detect the new module. Thus the declared pin design is directionally right but inadequate; do not report C1 as independently verified until the closure control rejects this world.

For Q33's external guard requirement, the relevant evidence is the frozen counter/pin identity, reviewed instrument blobs, and the independently scored shortcut worlds. Those controls do not substitute for an import-closure guard: the demonstrated `argparse.py` addition passed all five. The C1 result presently has a fixable, material calibration/consistency defect.

## C2 — Q74 and form versus semantics

The C2 counter was not yet present in `round-81/build/` when this probe ran, so findings here assess the frozen plan and E09 builder specification, not an executed new counter. The plan's conjuncts (a)–(g) are mechanically generable: read the committed snapshot, compute/use its pinned digest and located quote, write the entry fields and registry row, update S248 `used-by`, and emit the required SKILL/README/PROVINCE strings. These checks can establish the specified **form**. They cannot establish that a quoted passage semantically supports the prose's claim that the SDK has a second grant channel or that managed settings override it. The r80 `check_allowed_tools.py` explicitly contains a generator world and calls its claim FORM-LEVEL; E09's prompt requires the self-test and C0–C4, but does not require a separate independent generator world or a printed generator score. E07's assigned worlds are only C0–C4; the listed C2 falsifier/reviewer seats address other attacks and semantic review, not Q74 generator scoring.

The plan headline describes C2 as “depth (sourced)” and says the SDK channel “extends” the documentary matrix; it does **not** label the measured claim form-level. V02 is assigned to check entry claims against S249's snapshot, which is useful semantic review but is not the independent-generator score Q74 requires. The generator can be mechanically independent of the counter's in-file self-test and still write the complete proposed shape using committed page bytes; no quote-meaning judgment is needed to satisfy the form conjuncts.

**Smallest safe correction:** explicitly bound the counter headline to the form-level fact it measures (and disclose the semantic judgment as separately assigned to named non-authors), then score a separate independent mechanical generator that writes the full entry + row + snapshot evidence shape against the same frozen predicate before admitting the number. If that generator reaches 1 of 1, the number is form-only and cannot evidence semantic depth by itself. Keep the source-content review separate and cite it for the semantic statement. Do not treat C0–C4 as a substitute for Q74.

## Evidence scope / freshness

Read first: `plans/round-81.md`; `corpus/QUALITY.md` Q33, Q51, Q74; C1 `verifiers/check_tip_battery.py` including `run_battery`, guards, and self-test; r80 `verifiers/check_allowed_tools.py` generator-world design; E09/E07/C02/V02 prompts from `w1-spec.json`. At time of inspection, the r81 C2 counter and freeze receipt were absent from the build/receipts directories, so no claims are made about their eventual bytes or behavior. I did not run a tip battery at the true landed r81 revision.

Scratch clone/probe was removed before delivery. No tools installed.

VERDICT: C1 is falsified by a measured-revision sibling-module shadow that reaches 6/6; C2 is form-level by construction and the plan omits Q74's independent generator score and headline bound.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81L02Ctl.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81L02Ctl-shadow-world.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81L02Ctl-shadow-microprobe.txt