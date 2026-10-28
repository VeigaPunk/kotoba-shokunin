# Kb81R02TipRecon — tip-battery forensics at base b284223105f4d106f7e8f56ed4fd296c643cda0e

Scout seat, round 81 w1. Reconstructed why `python3 -B verifiers/check_tip_battery.py --rev <rev>` reads
`guards 5 of 5; tip battery exit 0: 4 of 6` at the r81 base. Method: rebuilt the counter's own
fleet-shaped sandbox (per `verifiers/check_tip_battery.py:175-203` — `git clone --shared --no-checkout`
of the lane into `sandbox/kotoba-shokunin`, every other fleet-root entry symlinked beside it, checkout
of `b284223105f4d106f7e8f56ed4fd296c643cda0e`, clean tree) and ran each BATTERY member
(`check_tip_battery.py:146-152`) from the clone root with direct exit capture. Composed result agrees
with the committed base receipt `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` (same 4/6 split,
same two reds). Per-gate receipts: `.ufo/waves/round-81/build/Kb81R02TipRecon-gate-*.txt`.

## Gate 1 — verifiers/check_gate_registry.py --rev b2842231…  → GREEN

- Command: `python3 -B verifiers/check_gate_registry.py --rev b284223105f4d106f7e8f56ed4fd296c643cda0e` (cwd = sandbox clone root)
- Exit: 0. Tail: `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`.
- Expectation (green): met.

## Gate 2 — verifiers/check_assertion_floors.py → GREEN

- Command: `python3 -B verifiers/check_assertion_floors.py`
- Exit: 0, wall 107.6 s (the battery's ~105 s wall is this gate). Tail: 12 `PASS` floors rows
  (pins 62, harness_independent 123, compare 330, floors_guard 165, dispatch_prompts 56,
  sibling_census 68, overlap_levers 55/51, alwayson 89, correction_sweep 25, scoped_rules_v32 240,
  spec_craft 250, sibling_reread 47).
- Expectation (green): met.

## Gate 3 — verifiers/verify_skill_checklist.py → GREEN

- Command: `python3 -B verifiers/verify_skill_checklist.py`
- Exit: 0. Tail: `PASS trigger.citation_resolves: 212`, `PASS governance.citation_resolves: 1324`.
- Expectation (green): met.

## Gate 4 — verifiers/verify_corpus_integrity.py → RED (exit 1) — 5 DRIFTs, all mapped

- Command: `python3 -B verifiers/verify_corpus_integrity.py`
- Exit: 1. Summary: `corpus.index tracked=155 unindexed=1 stale=0 missing=0`;
  `corpus.pointers report_dead=1/111 commit_total=46 unresolvable=2`;
  `4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
  corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_unresolvable`.

Per-DRIFT cause (verified at base):

1. `corpus.index.tracked_files` observed=155 expected=154 — `git ls-files corpus/` at b2842231
   returns 155 paths (154 `.md` + `corpus/knowledge/sibling-citation-routing-round16.json`); baseline
   `verifiers/corpus-baseline.json` expects 154, recorded at r80 tip `9a16e9d`. Sole added tracked
   corpus file since: `corpus/lessons/round-80-verifier-spotcheck.md` (landed at `b284223`, commit
   subject `round-80 verifier spot-check (integrator, hyaku): non-author admit/reject`).
   → Maps to R4 (baseline refresh). The `.ufo/wapes` leg of the spec's "wapes + rows + refresh"
   bundle is a *precondition*, not a drift cause: `refresh-corpus-baseline.py:135-144` Refuses on any
   `git status --porcelain` output, and the lane worktree carries untracked `?? .ufo/wapes`
   (594 B, r80 C2 quote-probe rows) — R3's disposition is what un-dirties the tree so R4 can run.
2. `corpus.index.unindexed` observed=1 — `corpus/lessons/round-80-verifier-spotcheck.md` is tracked
   but not denoted by any coverage-map cell in `corpus/README.md` (grep confirms no row; the r79
   file's row at corpus/README.md:157 literally says "landed without an index row, indexed round 80").
   → Maps to R4 row (index, never edit).
3. `corpus.pointers.report_total` observed=111 expected=109 — equal-mode drift, not a defect in the
   corpus: +2 live pointer tokens, both in the new spotcheck file at lines 5 and 10
   (`.ufo/reports/round-80/kotoba.md`; that report exists at the fleet root, 7822 B, so neither is
   dead). → Maps to R4 (baseline re-record; same wapes precondition).
4. `corpus.pointers.report_dead` observed=1 — `corpus/lessons/round-77-verifier-spotcheck.md:15`
   token `HEAD:.ufo/reports/round-77/kotoba.md`. Failure class: the gate's `UFO_POINTER_RE`
   (`verify_corpus_integrity.py:146-148`, char class allows `:`) captures `HEAD:` as part of the
   token, then `resolve_pointer`/`report_pointer_exists` (`:264-277`) treats it as a *filesystem*
   path — `(corpus/lessons/../)/HEAD:.ufo/reports/…` is not a file and `HEAD:.ufo/…` fails the
   `.ufo/reports/` fleet-root test (`startswith` fails on the `HEAD:` prefix). It is a git object
   expression: `git -C <fleet> cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md'` → rc=0 (8547 B,
   contains `## SHONEN`); in the *lane* `HEAD:.ufo/…` → rc=128 (report is a fleet object only).
   → Maps to R1 (`<rev>:<path>` git-object resolution lane-first-then-fleet + `## SHONEN`/≥400 B
   content-identity arm — the r80 E04 patch design, strengthened; the cited object already satisfies
   the new identity arm: 1 `## SHONEN` hit, 8547 B ≥ 400).
5. `corpus.pointers.commit_unresolvable` observed=2 — `corpus/SOURCES.md:171` (S230) and `:172`
   (S231), same token `7bb48f213ac677f943d5c791199ed3dddf302f00`. Direct probe at base:
   `git cat-file -e <hash>^{commit}` rc=128 in lane AND fleet; `git cat-file -e <hash>` (any object)
   rc=1 in both. S230 anchors it to `badlogic/pi-mono` (wrong repository — routed R80-D4); S231 names
   `mistralai/mistral-vibe` (correct, per `.ufo/waves/round-79/snapshots/S230.fetch.json` /
   `S231.fetch.json`, both present). The marker-based `owner/repo@` line grammar (r80 E05) was killed
   by W8/W9; a line marker alone never exempts.
   → Maps to R2 (new `verifiers/external-commits.json` verified binding, both gates) + manifest rows
   + S250 supersede row for S230 (plan repair 5).

## Gate 5 — verifiers/verify_corpus_independent.py → RED (exit 1) — 2 zero-mode DRIFTs

- Command: `python3 -B verifiers/verify_corpus_independent.py`
- Exit: 1. Zero-mode DRIFTs: `corpus.index.unindexed` observed=1 and
  `corpus.pointers.commit_unresolvable` observed=2 — same causes and same repairs as gate 4
  (`unindexed` → R4 row; `commit_unresolvable` → R2 + S250). `tracked_files` 155 and
  `report_total` 111 are INFO-mode here, not red.
- NOTE — plan line 9 inaccuracy (not a plan gap, a receipt-text misstatement): the plan records
  independent failing "on the same `commit_unresolvable` 2 plus `report_dead` 1". Measured truth
  (this run and the r80-refresh baseline note itself, which records the divergence as
  "report_dead integrity 1 vs independent 0"): independent's `report_dead` is **PASS observed=0**,
  and its red set is `{unindexed=1, commit_unresolvable=2}`, not `{commit_unresolvable=2,
  report_dead=1}`. Mechanism: independent's `POINTER_RE` (`verify_corpus_independent.py:123-125`)
  excludes `:` from the leading class, so `HEAD:` is not part of the token; it then resolves
  `.ufo/reports/round-77/kotoba.md` at the fleet root (present → alive). Repair coverage is fine —
  R2 fixes both gates on the hash; the r81 pins add one reviewed blob to *each* gate — but R1's
  `<rev>:<path>` arm is integrity-only by construction: independent's regex can never even capture
  a `<rev>:`-prefixed token, so its `report_dead` can never fire on that class. The seat pool
  strengthening independent should know this divergence is regex-level, not resolution-level.

## Gate 6 — verifiers/check_correction_sweep.py --root . → GREEN

- Command: `python3 -B verifiers/check_correction_sweep.py --root .`
- Exit: 0. `correction sweep: 0 stale block(s)`.
- Expectation (green): met.

## Tally and mapping verdict

4 green (registry, floors, checklist, sweep) + 2 red (integrity, independent) = `tip battery
exit 0: 4 of 6`, matching the composed receipt `guards 5 of 5` (all five guards held — the 22+/3−
instrument delta is the base-recorded r76/r80 verifier churn, under the 40 cap; E6's 140 cap is a
tip-side change and does not alter the base reading).

| red class | gate(s) | named repair | mapped? |
|---|---|---|---|
| `corpus.index.tracked_files` 155≠154 | integrity | R4 baseline refresh (precondition R3 wapes disposition: refresh refuses dirty tree) | yes |
| `corpus.index.unindexed` 1 | integrity + independent | R4 coverage-map row for `corpus/lessons/round-80-verifier-spotcheck.md` | yes |
| `corpus.pointers.report_total` 111≠109 | integrity | R4 baseline refresh (+2 live tokens in new file; wapes precondition as above) | yes |
| `corpus.pointers.report_dead` 1 | integrity | R1 `<rev>:<path>` object resolution + content identity | yes |
| `corpus.pointers.commit_unresolvable` 2 | integrity + independent | R2 `external-commits.json` verified binding + S250 supersede row | yes |

No unmapped red — no plan gap in the repair set. Two footnotes for the integrator: (a) the spec's
"`tracked_files`/`report_total` → wapes" leg is precondition-level only (dirty-tree refusal), the
drift cause itself is the +1 tracked file / +2 live tokens → refresh; (b) plan line 9's independent
drift list ("`commit_unresolvable` 2 plus `report_dead` 1") is a misstatement — measured red set is
`unindexed` 1 + `commit_unresolvable` 2, and `report_dead` is PASS 0 there because the regex excludes
`:` (both corpus gates still need their r81 pinned blob per E6).

VERDICT: base 4-of-6 fully reconstructed — integrity red on {tracked_files, unindexed, report_total → R4+R3; report_dead → R1; commit_unresolvable → R2+S250}, independent red on {unindexed → R4; commit_unresolvable → R2}; every red maps to a named repair, no plan gap (plan line 9's independent drift list misstates report_dead).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81R02TipRecon.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81R02TipRecon-gate-{gate-registry,floors,checklist,integrity,independent,sweep}.txt
