# C02CritPredicate — predicate identity audit (round 77 w1)

## Axis framing
- **Depth:** C1 sourced description-craft target, six conjuncts.
- **Consistency:** C2 routed R1–R4 target, four repairs.
- **Calibration/operability:** predicate and receipt identity; reproducible direct exit-status capture.

## Comparison table

“Predicate sentence” below means the full command + success condition + base/red behavior, not just its printed result phrase. Exact sentence sources are normalized for line breaks; punctuation and wording are otherwise preserved.

| Claim | Plan r76 | Plan r77 (operational sentence) | Frozen counter docstring | Receipt at r77 base | SCORECARD draft (r76 draft; no r77 draft existed at audit) | Exact differences |
|---|---|---|---|---|---|---|
| C1 | `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed K of 6` and exits 0 only when all six conjuncts **below** hold at `<rev>`; at base `b7f13f4b39cbd43076a85568adca763a6f674e7a` it prints `description craft backed 0 of 6` and exits 1. | Same command/result/exit condition, says all six conjuncts hold (omits “below”); says **at the r77 base** `2f675548eaad2a037a899d39247c1fd7a88aaf48` (the r76 base was `b7f13f4b39cbd43076a85568adca763a6f674e7a`). | Same command/result/exit condition and “all six conjuncts hold”; says only **at base** `b7f13f4b39cbd43076a85568adca763a6f674e7a`. | `c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt` gives command, counter sha, measured rev, six conjunct results, `description craft backed 0 of 6`, `exit=1`; **no full predicate sentence**. | r76 draft exactly matches r76 plan sentence, including “below” and the r76 base; not an r77 draft. | r77 plan changes the base hash and explicitly labels it r77, omits “below”; unchanged docstring still names r76 base and omits formatting backticks around command/revision. Receipt is a measurement record, not a quotation of the predicate. Historical r76 SCORECARD appropriately remains r76-specific. |
| C2 | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four repairs **below** hold at `<rev>`; at base `b7f13f4b39cbd43076a85568adca763a6f674e7a` it prints `r75 routed repairs closed 0 of 4` and exits 1. | Same command/result/exit condition, says all four repairs hold (omits “below”); says **at the r77 base** `2f675548eaad2a037a899d39247c1fd7a88aaf48` (r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a`). | Same command/result/exit condition and “all four repairs below hold”; says only **at base** `b7f13f4b39cbd43076a85568adca763a6f674e7a`. | `c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt` gives command (with `--work <scratch>` annotation), frozen-counter sha, measured rev, R1–R4 open, `r75 routed repairs closed 0 of 4`, `exit=1`; **no full predicate sentence**. | r76 draft exactly matches r76 plan sentence, including “below” and r76 base; not an r77 draft. | Same cross-round base mismatch and missing receipt quotation as C1. `--work` is an environment/sandbox option, not part of the predicate command. |

Exact r77 plan wording (one sentence each):
- C1: `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed K of 6` and exits 0 only when all six conjuncts hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (the r76 base was `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `description craft backed 0 of 6` and exits 1.
- C2: `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four repairs hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `r75 routed repairs closed 0 of 4` and exits 1.

## Evidence and falsifiers

- `sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` returned respectively `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` and `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`. `git rev-parse ec7f853:<counter> HEAD:<counter>` returned identical blob IDs for each counter, confirming unchanged bytes from freeze to r77 HEAD.
- In a `git clone --shared` scratch clone rooted at `/fast/scratch/hyaku/kotoba-r77/C02CritPredicate/clone`, direct runs of both counters at `b7f13f4b39cbd43076a85568adca763a6f674e7a`, `2f675548eaad2a037a899d39247c1fd7a88aaf48`, and `6523aced1ee0ebe07dca996213bdc645a6acbd1e` each printed C1 `description craft backed 0 of 6`, exit 1, and C2 `r75 routed repairs closed 0 of 4`, exit 1. C2 was invoked with `--work /fast/scratch/hyaku/kotoba-r77/C02CritPredicate/work`. No clone/commit was made; scratch was removed on shell exit.
- r77 receipts: the C1 and C2 base receipts show their own exit statuses explicitly. This confirms the r77 base red behavior but does not make their headers quotations of the predicate.
- `plans/round-76-addendum-2.md` §5 says the plan's canonical sentence remains the one under each claim and says counter docstrings quote those sentences verbatim, including the full base hash, with SCORECARD rows and receipt labels citing the same string. That cannot be literally true for r77 while preserving frozen counter bytes and changing the base revision: the docstrings necessarily retain the r76 base. The r77 plan discloses this in §9 but does not amend the r76 convention; existing r77 receipts also do not carry the sentence. This is a real documentation/identity mismatch, not a counter behavior defect.
- `plans/round-76.md` C1(a) originally said the snapshot digest equals the S213 anchor-update digest. `round-76-addendum-1.md` explicitly withdraws that clause because CORPUS rule 2 forbids in-place anchor edits, and specifies the four alternative digest locations. r77 §28 says conjuncts are as corrected by addendum 1 and its counter implements that corrected four-location rule; no contradiction found there. The pinned source digest is `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` in the snapshot manifest, matching the stated pin.
- The apparent R2 interpretation conflict is resolved by `round-76-addendum-5.md`: C2 R2 is specifically the r75 final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de`, re-runs both corpus gates there and compares normalized stdout; addenda 2/3's alternatives were withdrawn. r77 §40 states this correctly. C1 measurement conventions in addenda 1 and 4 are reflected in the counter docstring and r77 §28.

## Additional critical no-harm contradiction

The round-77 plan asserts the corpus gates are repaired at the new base and lists `check_gate_registry.py --rev` plus `check_assertion_floors.py` in the required final battery. Running directly in the isolated scratch clone at frozen HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` falsified the blanket no-harm expectation:

- `python3 -B verifiers/check_gate_registry.py --rev HEAD`: `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1.
- `python3 -B verifiers/check_assertion_floors.py`: all printed floor lines PASS, but process exit 1.
- `python3 -B verifiers/check_tip_battery.py --rev HEAD`: exit 1; output reports six constituent gate failures (including assertion floors, checklist, both corpus gates), with `guards 5 of 5`.

These are observed at frozen pre-data HEAD; the plan's own receipt claims corpus gates exit 0 **at base 2f67554**, while the checker runs at HEAD include the freeze commit but no data. The missing two registry rows and red floors need explicit investigation/repair before any no-harm claim; they must not be conflated with the predicate wording issue. The r77 plan's landing order does not name adding missing gate-registry rows/floor registrations, despite the no-harm requirement. Round-76 addendum 6 prose claims the relevant guard changes were already included; measured output takes precedence.

## Minimal pre-data correction

Proposed text is in `build/C02CritPredicate.proposed-addendum.md`. It preserves frozen counter bytes and targets, explicitly discloses the historical-vs-current base hash difference, limits “verbatim sentence” requirements to r77 operational records (not the immutable historical docstrings), and requires that later r77 receipts/SCORECARD drafts reproduce the operational sentence. It also flags the independently observed no-harm gate failures as unresolved prerequisites, rather than endorsing the addendum's claim as a predicate-only fix.

No files outside the assigned round-77 build/report paths were edited; no tools were installed.

VERDICT: Predicate targets and frozen counter behavior are coherent, but verbatim identity is impossible as currently worded and r77 receipts omit the sentence; pre-data addendum required. Frozen HEAD also fails required no-harm gates, blocking any honest no-harm claim.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/C02CritPredicate.proposed-addendum.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/C02CritPredicate.md