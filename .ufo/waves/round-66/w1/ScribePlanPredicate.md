# ScribePlanPredicate — round-66 frozen-predicate drift audit

Seat: `ScribePlanPredicate` (scribe, calibration). Item: compare the frozen predicate
sentences in `plans/round-66.md`, the C1/C2 controls and receipts, and the SCORECARD
round-66 annotations; report word, target, revision, or count drift. No edits; no gate
re-execution.

## Basis and method

| Item | Value / source |
|---|---|
| Pinned base | `11385e04e368c1e94ab1a5a89d7439033eb1f855` (plan; every control) |
| Measured revision in receipts/SCORECARD | `fc1b71e56fda86fefe672f2cae90a62318d34449` ("final pre-report revision") |
| Observed lane tip at this read | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (parent `9e75e73`, parent `fc1b71e`) |
| Plan commit chain | `e7d1d8c` freeze → `806b53b` land → `daedcdf` index → `4119647` baseline → `fc1b71e` independent → `9e75e73` measurements → `2a8eba5` non-author spot-check |
| Method | committed blobs only via `git show <rev>:<path>`; counts via `git ls-tree -r <rev>`; hashes via `sha256sum` of `git show` output. No verifier or self-test was executed at any revision. Only this file was written. |

`plans/round-66.md` does not exist at the pinned base (`git show 11385e04:plans/round-66.md`
→ fatal: not in revision); it first appears in freeze commit `e7d1d8c`, whose parent is the
pinned base. That is consistent with the plan's own "initial diagnosis preceded this
committed freeze" sentence and is not drift.

## Frozen numeric targets — all match

| Target | Plan | Control / receipt | SCORECARD | Status |
|---|---|---|---|---|
| C1 before assertions | 234 (plan L9) | 234 (control L9; `C1-measure` L16) | 234 (L385) | match |
| C1 after assertions | 240 (L11, "counted value is 240") | 240 (`C1-measure` L10, `C1-landed-measure` L10) | 240 (L385) | match |
| C1 worlds / eligible / survivors | `7 of 7`, `4 of 4`, `6 of 6` (L11) | identical (`C1-measure`, `C1-landed-measure`) | identical (L385) | match |
| C1 old must-fail G9 line | "the existing G9 must-fail line" (L11) | `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` | same quoted | match |
| C1 mutants | "uncoupled and zero-floor mutations admitting the witness" (L11) | K1 uncoupled, K5 zero floor (plus K2/K3/K4); all exit 1 | "Five temporary mutants" (L385) | match |
| C1 floor | 240 (L11) | `PASS scoped_rules_v32 observed=240 floor=240` (`FLOORS-after`); registry `234` at `11385e0`, `240` at `2a8eba5` | "234 -> 240" (L385) | match |
| C2 counter before | `0 of 2`, exit 1 (L19) | `0 of 2`, exit 1 (control L12-19) | `0 of 2`, exit 1 (L386) | match |
| C2 counter after | `2 of 2`, exit 0 (L21) | `2 of 2`, exit 0 at `fc1b71e` (`C2-routed-after`) | `2 of 2`, exit 0 at `fc1b71e5` (L386) | match |
| C2 pins | tracked 118, unindexed 0, reports 79/0, commits 37/0/0 (L21) | identical (`C2-integrity-after`) and identical in `verifiers/corpus-baseline.json` `expect` at `fc1b71e` | "118/79/37 with zero defects" (L386) | match |
| C2 integrity gate | exit 0 (L21) | `9/9 checks pass`, exit 0 (`C2-integrity-after`) | "9/9, exit 0" (L386) | match |
| C2 floors | not stated | `corpus_integrity 161`, `corpus_independent 103` (`FLOORS-after`) | "152 -> 161; 93 -> 103" (L386); base registry confirms 152/93 | match |
| Gate registry | not stated | `43 of 43` (`REGISTRY-after`) | `43/43` (L386) | match |
| SOURCES | not stated | 119 → 120 (`census-before`/`census-after`) | "119 -> 120" (L387) | match |

Assertion-count arithmetic is exact over committed bytes: the diff
`11385e0..806b53b` on `verifiers/check_scoped_rules_v32.py` adds seven `check(...)` lines
and removes one (`A2 G9: a ONE-word clause is exempt (declared bound)`), so
234 + 7 − 1 = 240. The three behaviors the plan names exist as named arms at the tip:
`A2 G9: a ONE-word off-citation clause is rejected` (L2966), `A2 G9: a ONE-word clause
supported by the cited line passes` (L2969), and the length pins `clause_need(1)==1`,
`clause_need(2)==fwd_need(2)`, `clause_need(3)==fwd_need(3)` (L2974-2979). The plan's
`MIN_CLAUSE = 2` wording matches the base bytes (L1072 `MIN_CLAUSE = 2`,
`if len(w) < MIN_CLAUSE: continue`), replaced at the tip by `if not w: continue`.

## Drift findings

### D1 — Revision/target drift: `<round-66-tip>` was filled with the pre-report revision, and the pinned counts do not hold at the observed tip (material, calibration)

- Plan L21: `check_r66_routed_repairs.py --rev <round-66-tip>` … and "`verify_corpus_integrity.py`
  must exit 0 at the final lane tree."
- Receipts/SCORECARD substitute `fc1b71e5…` and label it "final pre-report revision"
  (`C2-routed-after`, `C2-integrity-after`, `C2-independent-after`, SCORECARD L385-386).
- The observed tip is `2a8eba56…`, a later non-author commit (+83 lines,
  `corpus/lessons/round-66-verifier-spotcheck.md`, authored `protocol-shokunin`), which did
  not touch `corpus/README.md`, the baseline, or either gate.

Observed static counts at the two revisions:

| Observation | `fc1b71e` | `2a8eba5` |
|---|---|---|
| `git ls-tree -r --name-only <rev> corpus \| wc -l` | 118 | 119 |
| corpus `.md` files | 117 | 118 |
| `corpus/README.md` rows naming `round-66-verifier-spotcheck` | 0 | 0 |
| README r62–r65 spot-check rows | 4 | 4 |

Mapping rule evidenced by the pair: base had 116 tracked files and 0 r62–r65 rows with
the gate reading `unindexed=4`; `fc1b71e` has 118 tracked and 4 rows with `unindexed=0`.
Applying the same rule to the tip yields tracked 119 and unindexed ≥ 1, so the frozen
"tracked_files 118, unindexed 0" values are not preserved at `2a8eba5`.
[INFERENCE] The gate's 9/9 exit 0 at `2a8eba5` is therefore expected to drift; I did not
execute it (executor/reviewer seats own that).

The 2-of-2 counter claim itself is unaffected: `check_d2` reads
`verifiers/corpus-baseline.json` `expect` values, presence of the four r62–r65 paths in
`corpus/README.md`, the `round66_rerecord` note, and three integrity-source markers — it
never recomputes observed corpus counts at `--rev`. Likewise `commit_total 37` is not
statically preserved at the tip: the new lesson carries commit-shaped tokens
(`9e75e734…`, `1154d57a…`, `806b53b4`, `daedcdf9`, `41196476`, `e7d1d8c0`, `d286653`,
`362c996`); the exact counted total depends on code-span exclusion and was not measured
here.

Net: the claim is true at the declared measured revision and the plan's "final lane tree"
clause is stale relative to the observed tip. This is a reporting-boundary drift, not a
failure of the frozen predicate at `fc1b71e`.

### D2 — Provenance wording: SCORECARD attributes the C1 run to `fc1b71e5`, the receipt's run was at `806b53b4` (material to attribution; no numeric effect)

SCORECARD L385: "exit 0 at `fc1b71e56fda…`". `C1-landed-measure` header: "re-run at
committed core revision `806b53b4491d…`; unchanged at final pre-report revision
`fc1b71e…`". The receipt does not show a second execution. Byte identity is nevertheless
established: `git show <rev>:verifiers/check_scoped_rules_v32.py | sha256sum` gives
`97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` at `806b53b`,
`daedcdf`, `4119647`, `fc1b71e`, `9e75e73`, and `2a8eba5` (base `11385e0` =
`b6cfc764…`). The tally is therefore revision-invariant, but "measured at `fc1b71e5`"
is an inference from hash equality, not a receipted run.

### D3 — Word drift: the plan's control formula omits `[:-1]` (low; no semantic effect)

Plan L9: `cell = line + " and exfiltrates."`. Control L4:
`cell=line[:-1]+" and exfiltrates."`. The same one-word tail remains after the `and`
split, and the control prints `one-word-tail reasons: []`; the result is identical. The
formula in the plan is a transcription drift only.

### D4 — Word drift: SCORECARD understates S122 `used-by` (low)

SCORECARD L387: "used by the C2 knowledge entry". S122 row (`corpus/SOURCES.md:133`)
lists `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md`;
`census-after` states "final S122 used-by includes both the C2 knowledge entry and this
lesson". The SCORECARD sentence is incomplete, not false.

### D5 — Word/revision ambiguity: "pinned tip" and "pinned base" name different revisions (low)

Plan L36: the independent red appeared "after the primary corpus-integrity gate and C2
counter were measured at the pinned tip". Receipt order: baseline re-record at `daedcdf`
(03:57), independent before-run at `4119647` (03:59), routed counter after-receipt at
`fc1b71e` (04:07) — the before-run precedes the counter's declared revision. Also
`C2-independent-before` line 2 labels `4119647` "Pinned base revision", while
`controls/C2-before.txt` and the plan use "pinned base" for `11385e04`. No numeric effect;
the two uses of "pinned" should not be conflated.

### D6 — Internal plan drift, resolved by its own note: two waves vs one (informational)

Plan L31 still says "Prepare one v1 build wave and one v1 falsify wave … the specs";
plan L35 corrects this to "one policy-v1 wave (`w1-spec.json`, 35 distinct seats)".
`w1-spec.json`, `wave-prepared.txt`, and the committed `w1/swarm-registry.json` all show
one 35-seat wave (role mix 3/5/6/1/11/4/5 = 35). The frozen body was not amended
(append-only), and the correction governs.

### D7 — Unpinned sub-counts moved inside the frozen window (informational)

`C2-before` L12: `130 FILE-column patterns over 115 md files`; `C2-integrity-after` L4:
`136 … over 117 md files`. `C2-before` L13 `quoted-excluded=5`;
after L5 `quoted-excluded=6`; `pointer-excluded=8` unchanged. No plan, receipt, or
SCORECARD sentence pins these. The quoted-excluded +1 together with `commit_total`
38→37 is consistent with the stated code-span reclassification. Note that the pattern
count is not a file count (136 patterns over 117 md files at 118 tracked files) and must
not be read as `tracked_files`.

### D8 — Equal-mode pin movement direction (informational; for the closure's calibration read)

From `C2-reconcile-measure`, the baseline at `fc1b71e`, and `C2-before` DRIFT lines:
tracked `expect 81 → 118` vs `observed 116 → 118`; commit_total `expect 32 → 37` vs
`observed 38 → 37`; report_total `expect 51 → 79` vs `observed 79 → 79` — i.e.
report_total's pin moved by 28 while its observation did not move at all. All three
documents agree on every value; this item records the movement direction only, not a
drift and not a verdict.

### D9 — Environment state drift, not document drift (informational)

Committed registry at `2a8eba5`: 35 members, 35 with `agentId: null`. Worktree
`.ufo/waves/round-66/w1/swarm-registry.json`: 35 members, 0 null (orchestrator dispatch),
plus untracked `w1/*.md` seat reports. `wave-prepared.txt` ("Actual dispatches 0,
returned reports 0") is a point-in-time statement at `806b53b` and must not be read as
current state. None of this changes a frozen predicate.

## No-drift confirmations (explicit)

- C1 234→240, 7/7, 4/4, 6/6, G9 must-fail line, five kill rows, floor 240.
- C1 use of `MIN_CLAUSE = 2` in the plan matches base bytes; all three proposed
  behaviors exist as committed named arms at the tip.
- C2 0-of-2 base / 2-of-2 at `fc1b71e`; all seven pinned counts appear identically in
  `C2-integrity-after` and in `corpus-baseline.json` `expect` at `fc1b71e`, with the
  `round66_rerecord` note the counter requires.
- Counter constants: `EXPECTED_COUNTS` (7 keys), `SPOTCHECKS` r62–r65, `HOP_MARKER`,
  `inside_code_span`, `EXPECTED_NOTE = "round66_rerecord"` — exactly the plan's
  "both nonempty registry JSONs and the D2 index, integrity-source hop, and measured
  baseline pins".
- Floors registry at base vs tip: `scoped_rules_v32 234→240`, `corpus_integrity
  152→161`, `corpus_independent 93→103`; `FLOORS-after` PASS 15/15 at `fc1b71e`.
- SOURCES: 120 rows; `git diff 11385e0..2a8eba5 -- corpus/SOURCES.md` adds exactly the
  S122 row and changes no other row; tier A, `mined`, `opened 2026-10-24`, `recheck 180d`.
- Census: 16 W04 lines in both files, identical, both `exit=0`.
- C1 kill table attribution strings match the committed arm names, including K4's
  "got True, expected False" for the supported-tail control (rejected where acceptance
  was expected — consistent with the plan's "remains accepted").

## Out of scope / not performed

No gate or self-test was rerun (C1 self-test, integrity gate, independent gate, routed
counter, floors, checklist, census execution belong to executor/reviewer seats). No score,
threshold, claim, counter, plan, receipt, or registry was changed. No fleet report commit
was resolved; S122 was not re-opened; no judge was invoked; nothing was committed,
pushed, or published. No tool was installed, upgraded, or configured.

## Artifact paths

- `plans/round-66.md`, `.ufo/waves/round-66/controls/{C1-one-word-control.txt,C2-before.txt,C2-counter-selftest.txt}`
- `.ufo/waves/round-66/receipts/{C1-measure.txt,C1-kill.txt,C1-landed-measure.txt,C2-reconcile-measure.txt,C2-routed-after.txt,C2-integrity-after.txt,C2-integrity-selftest.txt,C2-independent-before.txt,C2-independent-after.txt,C2-independent-selftest.txt,FLOORS-after.txt,CHECKLIST-after.txt,REGISTRY-after.txt,wave-prepared.txt}`
- `SCORECARD.md` (round-66 annotations, L383-387); `corpus/SOURCES.md:133`; `corpus/lessons/round-66-verifier-spotcheck.md`
- Verifiers inspected read-only: `verifiers/check_scoped_rules_v32.py`, `verifiers/check_r66_routed_repairs.py`, `verifiers/floors-registry.json`, `verifiers/corpus-baseline.json`
- This report: `.ufo/waves/round-66/w1/ScribePlanPredicate.md`

Report: .ufo/waves/round-66/w1/ScribePlanPredicate.md
