# SimpW2DeadWeight — YAGNI sweep of the round-64 lands (wave 2, seat report)

Seat: `kotoba-r64.SimpW2DeadWeight-2` · 2026-10-24 · tip measured: `c019919c97ab5fe98e87a7754b4449ea4e699c99`, base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.
Scope: `verifiers/check_r64_routed_repairs.py` (969 lines, read in full), `corpus/lessons/round-64.md`, `LOG.md:2599-2610`, cross-checked against the frozen predicates in `plans/round-64.md`. **I deleted nothing** — verdicts below are for the L1 to land. No tools installed this run (nothing needed beyond repo Python).

## Measured evidence (run at the tip)

- `python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c…` → all four checks PASS, `r63 routed defects closed 4 of 4`, rc=0.
- `--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` → all four FAIL, `closed 0 of 4`, rc=1, refusal line printed.
- Both arms together: wall time 2.79 s. Frozen predicate (plans/round-64.md:105-117) holds exactly as landed.
- Check-4 detail line on both runs: `runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23` — the static shape `(17, 2, 3)` is exercised, not decorative.

## Deletion candidates (agreed cuts, L1 to land)

**D1 — `_numstat_added` is a redundant second `git diff` per seat-edit check.**
Def at `check_r64_routed_repairs.py:86-95`; sole production caller at `:143`. `check_seat_edit` runs `_added_lines` (`:142`, `diff --unified=0`) and then `_numstat_added` (`:143`, `diff --numstat`) over the *same* rev pair and path — two subprocess spawns where one serves. For the text blob at issue, `added_count = len(added)` is identical (each added line appears exactly once as a `+` line in a `--unified=0` diff; empty diff → 0 both ways). Cut: delete `:86-95`, set `added_count = len(added)` at `:143`, collapse the `:144` guard to `added is None`. Saves one git invocation per check-1 evaluation (×2 per full run via `base_control`), 10 lines. Only theoretical divergence is a binary blob (numstat yields `-`, unified=0 yields `[]`), irrelevant to the markdown seat report this check reads.

**D2 — `append_axis` parameter of `_commit_log_variant` is dead machinery.**
Param at `:937`, dead branch `"- no axis correction"` at `:940`. Grep over the whole file: the only callsites are `:767-768` and `:777-778`, both passing `append_axis=True` — which is the default. No caller ever passes False, so the False branch is unreachable. Cut: drop the param and branch (`:937,:940`), drop the explicit `=True` at `:768,:778`. ~4 lines, zero behavior change.

**D3 — `lines` parameter of `_seat_edit_text` is never turned.**
Def `:538`; both callsites `:723`, `:813` use the default 82. The 60-line-floor arm (`:807-810`) writes its one-line file directly instead of `_seat_edit_text(lines=1)`, so the knob has no exerciser. Cut: inline the constant. 1 line.

## Kept after inspection (with reasons)

**K1 — `EXPECTED_ASSERTIONS` (`:38`, used only `:350`).** Logically redundant: `_static_assertion_count` derives count = fixed + loop_sites × arms from the same tuple checked at `:351`, so shape `(17, 2, 3)` implies 23. Strict YAGNI would cut it; **keep** — in an anti-cheat verifier the explicit frozen number keeps the refusal message ("count is not the frozen 23") self-contained, and the frozen plan names the number (`plans/round-64.md:142`). This is the one pure logic redundancy I found and I recommend keeping it deliberately.

**K2 — final self-test arm "baseline LOG leak" (`:925-926`).** Its assertion value duplicates the earlier base arm (`~:704`, which already requires `check_control_revs(root, base_rev)[0]` False inside `base_results`). Between the two, the worktree LOG gains a fully green r64 entry — but `check_control_revs` reads only committed blobs at `base_rev`, so the later arm provably re-asserts the identical value. Deleting it is safe; I lean **keep** as a cheap ordering canary (it pins that nothing in the preceding ~200 lines of world mutation leaks global state into the base refusal). Either disposition is defensible; this is the only duplicate assertion in the suite.

**K3 — `show_bytes` (`:69-73`) re-rolls the `git()` call in bytes mode.** Single caller (`:322`). Unifying into `git()` would add a text/binary parameter to the shared helper for one caller whose bytes round-trip (write_bytes + explicit `decode("utf-8")` at the AST parse) is intentional. Keep.

**K4 — `_r64_suffix_lines` fetched twice per rev (checks 2 and 3, `:188` and `:273`), plus twice more under `base_control`.** A cache/memo would be over-machinery for ≤4 `git show` calls per process. Keep.

**K5 — `run()` at `rev == BASE_REV` evaluates all four checks twice** (once in `base_control`, once in the loop) before refusing. Waste exists only in the control-demonstration case; restructuring would tangle the refusal semantics the frozen predicate depends on. Keep.

**K6 — `repo` at `:957` is checked but its toplevel unused; `LANE` (`:34`) has a single use (`:948` default).** Cosmetic at most; no cut worth the churn. `from __future__ import annotations` (`:24`) is a no-op on 3.10+ but free portability. Keep.

**No unused arms, no dead imports, no dead fixtures.** All four CHECKS entries are exercised by `run()` and by named self-test arms; `LABEL_ONLY_SOURCE` / `FINGERPRINT_SOURCE` / `WORKTREE_CHECK_SOURCE` / `HARDCODED_COUNT_CHECK_SOURCE` / `_green_control_source` / `_assert_argparse_rejects_base` / `_wrong_prefix` / `_embedded_hash` / `_replace_function` each have exactly the consumers their arm needs; every import is used. Every parameter of `_control_line` (`full`, `base_token`), `_r63_fixture_source` (`fixed_calls=18` at `:820`), and `_scorecard_text` (`reordered`, `move_table`) has an exerciser.

## Is the counter lean as landed?

Substantially yes. Production path is ~400 of 969 lines; the back half is the falsification rig (constructed worlds, process counter arms, substitution batteries) that the frozen plan §Hardening (`plans/round-64.md:153-157`) declares load-bearing — it is weight with a job, not dead weight. The three real cuts (D1-D3) total ~15 lines and one redundant git subprocess; nothing larger survived the read. The docstring's "(32 assertions)" claim is true: I statically count 26 fixed `check(` sites plus 3 counter-arm labels × 2 checks = 32 [static count from full read, consistent with the run's exit behavior].

## Lesson / entry filler check

**No filler found.** `corpus/lessons/round-64.md`: every section carries evidence pointers (S120 quotes with snapshot line numbers + word counts + sha256; M96-M98 with defect provenance; falsify table rows a-l/k' each naming source seats and a disposition; method provenance and bounds naming their debt). "Routed-input handling" §1-4 overlaps the falsify table by design — it maps routed inputs to claims, which is the round's contract, not duplication for its own sake. `LOG.md:2599-2610`: 12 dense bullets, each tied to a counted predicate, receipt path, or census artifact; "Discarded: nothing." is the standing convention line, and "(Wave-2 rows append below this table post-wave-2.)" in the lesson is a live placeholder for this very wave. Nothing to cut without losing record value.

## Tradeoffs

D1 changes two `None` sources into one (binary-file edge, immaterial here). D2/D3 are behavior-identical. All three are mechanical; the four-check predicate, the base-refusal rule, and the 32-assertion self-test are untouched by them.
