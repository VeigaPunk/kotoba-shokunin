# Kb79CR01C1Target — C1 target/counter attack

## Evidence and counterexample

I read `plans/round-79.md` first, then the frozen `verifiers/check_tip_battery.py` source and both base receipts. I did not build a scratch candidate: the reachable tempting candidate would be an alternate commit whose six gate scripts already match pinned green blobs, but the pins shown in lines 125–141 are restricted to specifically named digests, and the measured failing bases plus plan's listed failures do not supply an alternate set of green blobs. I therefore have no executed candidate output to quote. No shortcut-world result is inferred from unrun work.

Relevant source: `build_sandbox` lines 175–203 clones the selected repo revision, symlinks fleet siblings, checks out the rev. `run_guards` lines 244–336 compares base/revision tree membership, floors, instrument diffs/pins and base spotcheck hashes. `run_battery` lines 339–358 runs six fixed scripts from the checked-out sandbox and records each return code. `measure` lines 373–399 prints five guard IDs, counts `rc == 0` as a green gate and returns 0 only if all six green and no guard failures.

Base evidence (both `receipts/tipbattery-base-dot.txt` and `tipbattery-base-abs.txt`): exact final line is `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6`; each ends `exit=1`. The dot/absolute forms therefore agree at base, as reported, but this does not establish the target's both-form success condition.

## Sentence coverage / axes

The counter output turns on the printed guard tally and gate count; process exit is the counter process result. However it does not print which invocation form (`--repo .` versus absolute path) was used, nor does a single successful execution establish the required success in both forms. The report line only prints fleet root, guards and gate count (source lines 396–399), so both-form provenance requires separate captured invocations/receipts. Also, wording `prints ... and exits 0 at <rev>` is not itself a property checked by the six-gate count alone; harness must capture each command's own exit status (the plan explicitly requires that at lines 66–68).

Impacted axes: consistency/calibration (target ambiguity and missing form-specific evidence), operability (must actually invoke/capture both forms), robustness (counter can only assess the specified six script return codes and guards).

## Guard feasibility and hollow-green risk

The guard arithmetic is not inherently unsatisfiable. The five guard categories are independent checks; a plausible minimal correction set affects non-instrument repository data and a small number of source lines: registry rows for two existing verifier scripts; correct the stale citation target; corpus index/pointer/commit-count repairs; and fix the assertion-floor self-test cause without lowering floors. This should fit ≤40 added instrument lines because the implied fixes need no instrument edits if gate implementations already correctly detect repaired state. This is an inference, not a measured patch. The floor guard forbids lowering existing floors; instrument pin requires the six scripts to be one of expressly permitted blobs; no-deletions preserves all guarded base paths; spotcheck identity bars edits to existing verifier-spotcheck files. Additional spotcheck files are explicitly informational, not blocked (source lines 322–331).

Cheapest hollow-green path is repairing records to satisfy superficial checks while leaving the underlying provenance/consistency defects: e.g. make corpus index counts and pointers self-consistent with fabricated or misleading rows, and add registry entries for present scripts without proving they are appropriate skills. The battery only observes six exit statuses and structural guards; it does not independently validate the truth of underlying corpus records. For the floors failure, patching its checker is blocked by pin, so the cheap avenue is manipulating inputs/self-test trigger rather than weakening checker. This is a risk, not an executed falsifier.

## Verdict

target needs change before freeze: preserve explicit two-form invocation evidence as a required acceptance artifact, and add a pre-data adversarial control that reaches all six green via self-consistent-but-false repository records or otherwise demonstrates the six gates' semantic limits. Current output alone does not encode invocation form, and I did not execute a control world. No counter defect is claimed absent a run.

VERDICT: target needs change before freeze: form-specific evidence is external to the counter output; semantic hollow-green risk remains untested
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79CR01C1Target.md