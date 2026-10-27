# Round 78 — pre-data freeze (kotoba, attempt 1)

Date: 2026-10-27. Base: `9f796a598a588c365e6cb7cb57c6752872771d5d` (lane helper state; clean, ahead=0). Author: L1 `KotobaR78`.

## Claim choice and control

The lane scores depth 9 and consistency 10; depth is the lowest owned axis. C1 targets depth and is sourced at S213, opened in round 77. C2 targets consistency (calibration sub-axis). Both inherit round 77's two frozen predicates unchanged because round 77 did not declare a successful claim data landing. However, the non-author round-77 closure found decisive counterexamples to both: C1 reaches 6/6 with a 489-byte stub and unchanged description; C2 reaches 4/4 with pasted R1/R3/R4 text plus real historical gate stdout. These are committed evidence at `.ufo/waves/round-77/w1/C01CritDoNothing.md:5-12` and its receipts. Therefore neither predicate is eligible to support a new claim. The do-nothing control reaches both targets. This attempt is an honest stop before data: no claim is frozen as admissible, no narrowed or replacement predicate is invented after the counterexamples, and no claim data will be landed.

## Evidence and baseline

- Lane base: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse refs/heads/master` → `9f796a598a588c365e6cb7cb57c6752872771d5d`; `jj-lane.sh state ...` reported clean, `ahead=0`.
- Round-start source census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok`, with existing W04 duplicate-URL warnings including S213. No source row changed or newly opened by this attempt.
- C1 do-nothing target reached: committed round-77 control C1-W1 is a minimal stub, does not alter SKILL description, and prints `description craft backed 6 of 6`, exit 0 (`.ufo/waves/round-77/w1/C01CritDoNothing.md:5-7`; raw outcomes in `.ufo/waves/round-77/build/C01CritDoNothing.receipts.txt`).
- C2 do-nothing target reached: same control suite prints `r75 routed repairs closed 4 of 4`, exit 0 using pasted text and historical stdout; it separately records forged/non-run R2 receipts fail (`.ufo/waves/round-77/w1/C01CritDoNothing.md:7`).

## Disposition

No admissible frozen predicate exists in the inherited plan. Do not dispatch data-writing work against these claims. A new predicate must be designed and controlled in a later round, before any claim data; this attempt does not create a substitute target. No axis is claimed improved or harmed; no score change.

## Assimilation and frontier

Assimilation: none. No `considerthese/` proposal or shokuknow package is adopted; the inherited claim predicates fail the mandatory do-nothing control before such data work can begin. No SOURCES row is added.

## Mistakes mined

Predicate-reachability · `.ufo/waves/round-77/w1/C01CritDoNothing.md:5-8` · captured-by: frozen-counter/do-nothing control requirement in the round protocol · fix: score the cheapest control against frozen bytes before data; a target reached without the semantic change invalidates that predicate.
