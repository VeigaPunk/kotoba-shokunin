# Kb80E16PinAudit — round 80, wave w1

Seat: `Kb80E16PinAudit` (leaf, freeze-set pin audit). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Lane base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; lane HEAD at audit time
`c2f69d4f7b5887c409d7c3975d6aebc2e312c406`.

Deliverable (every value with its command and its status):
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E16PinAudit.txt`
(29 KB, 10 sections).

## What I did

Recomputed the round-80 freeze-set pins from PRIMARY bytes and cross-checked
every pin other seats published. No claim after-value scored, no counter
narrowed, no artifact repaired, no lane file written outside
`.ufo/waves/round-80/`. All mutating git ran in scratch clones under
`/fast/scratch/hyaku/kotoba-r80/Kb80E16PinAudit`, each asserted with
`git rev-parse --show-toplevel`; the lane repo was read-only (no commit, add,
checkout, stash or push). The scratch tree is removed.

## Pin values (recomputed, not quoted)

| pin | value | status |
|---|---|---|
| `verifiers/check_tip_battery.py` sha256 (worktree = base = HEAD) | `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a` | equals the r79 freeze receipt; unchanged this round |
| `check_gate_registry.py` blob @base | `95ffed389f483c3d6f93db3c08dcfdb9a2240576` | already in INSTRUMENT_PINS |
| `check_assertion_floors.py` blob @base | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | already pinned |
| `verify_skill_checklist.py` blob @base | `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f` | already pinned |
| `verify_corpus_integrity.py` blob @base | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` | already pinned |
| `verify_corpus_independent.py` blob @base | `edac0df79324ba62ee25ff10a6a4d422ef59da61` | already pinned |
| `check_correction_sweep.py` blob @base | `c94b771fa7d798ef45fc3bb640422ee7910f81a6` | already pinned |
| r79 E04 patch sha256 | `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78` | equals the plan's `d7169dd8…` |
| E04 result blob (integrity) | `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` | equals E04's published `.blob` |
| fleet `.ufo/reports/round-76/kotoba.md` sha256 | `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f` | equals the plan's `a025051d…` |
| six snapshot sha256s | S226 `9a67de89…`, S227 `31623035…`, S228 `81409d89…`, S229 `34016233…`, S230 `5b980552…`, S231 `fc48a5db…` | all equal their `.manifest` pin, their r79 fetch record and the actual committed bytes |

Cross-checked published pins: `Kb80E04DeadPointer.blob` (match),
`Kb80E06CounterErratum.sha256` / `check_tip_battery.amended.py` (match,
`15cc1761…`), `Kb80E04DeadPointer/composed-stack-*.txt` (match), Y01's composed
pins (match, and independently confirmed by seat Kb80V03Instruments).

## Disagreements, explicitly

1. **E04 patch path.** The plan/brief quote
   `.ufo/waves/round-79/build/Kb79E04DeadPointer.patch`; the file is at
   `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`
   (a directory). Digest matches — path error only.
2. **`MANIFEST.sha256` does not exist** at
   `.ufo/waves/round-79/snapshots/` (base or HEAD). The tree carries six per-id
   `.manifest` files whose six digests equal the committed snapshot bytes
   exactly. The aggregate file is a NEW file the stack must add; the C2
   counter's conjunct (c) reads exactly that path and exits 2 without it
   (reproduced). Proposed content:
   `.ufo/waves/round-80/build/Kb80N01Sentinel-MANIFEST.proposed`.
3. **S229 live bytes have moved** (live `20fd76d8…` vs pinned/committed
   `34016233…`). The pin must stay on the committed bytes; an anchor cell
   carrying the live digest fails conjunct (c). The other five are stable.
4. **The cap-only provisional counter** (`Kb80E06CounterErratum.cap60-provisional.py`)
   has an UNCHANGED pin table (`grep -c 051b8c5f` = 0). Measured on a
   base+E04 tree it fails `instrument-pin` ("guards 4 of 5; tip battery exit 0:
   1 of 6", exit 1). E5 as published delivers only the `LINE_CAP` half.
5. **`Kb80M02Battery-pristine-counter.py` has a RED self-test as published**
   (4 failures / 69 assertions, exit 1) — its `LINE_CAP` is 60 while its
   fixture padding is hardcoded 41/60, and its independent pin row duplicates
   the base blob instead of adding a new one.
6. **The C2 counter's self-pin is stale**: `SELF_SHA = 1f9744c8…` but the
   blanked sha of its own bytes is `f6569f6b…` → every real measurement exits
   2 with "environment error: counter drifted". Reproduced against the E10
   stack.
7. **The C2 counter does not yet print the plan's frozen strings from its
   print statements.** The current build copy (sha256 `b4ca1561…`, rewritten
   mid-wave from the r79 draft's `74e067cc…`) carries the strings
   "allowed-tools surfaces documented N of 6" / "generator world: M of 6" in
   its DOCSTRING only; lines 2281-2282 still print "… backed N of 6" and
   "script-only world: M of 6"; `TARGET` is still 5 with exit rule
   `n >= TARGET and …` where the plan freezes `N == 6`; and `ENTRY` is still
   `corpus/knowledge/allowed-tools-surfaces-round79.md` where the plan names
   `…-round80.md` (the published entry file). Measured on the E10 stack:
   "entry …-round79.md absent at <tip>", "allowed-tools surfaces backed 0 of
   6", exit 1.
8. **C2 counter defect (structural):** the Q70 locator cannot admit ANY
   Microsoft-Agent-Framework quote, so "6 of 6" is unreachable with the
   committed S229 snapshot. `S229-msaf.html` names the field exactly once
   (raw line 818); in the counter's own `text_view` that is view line 95,
   while `quote_location()` rejects any quote starting at or before
   `first_head + 1 = 169`, and `first_head` is view line 168 — a PYTHON
   COMMENT inside a code sample, not a heading (the page's real `<h1>` is raw
   line 676). Measured with the counter's own functions: S226/S227/S228/S230/
   S231 locate, S229 always returns "quote lies in the first-heading block
   (Q70)". Reported, never repaired by narrowing a quote.
9. **Line-cap arithmetic.** The guard diffs against the PINNED r72 base
   `072048fa…`, not the round-80 base: 22 added / 3 deleted at base (all 22 in
   `check_assertion_floors.py`), 39 after E04, leaving 21 lines for the grammar
   class across BOTH corpus gates. The published S07 candidate adds 171 (210
   total) — it does not fit cap 60; the Y01/E10 composed stack adds 59 total
   and does fit, with one line of headroom.
10. **Anchor trap:** the two live `commit_unresolvable` tokens at base are ONE
    40-hex digest cited twice (`7bb48f21…`, `corpus/SOURCES.md:171` row S230
    and `:172` row S231); the plan's named `451a02ff` / `cfb894a5` are
    `commit_quoted` context. S230's anchor additionally names the MISTRAL-VIBE
    commit as pi-mono's (pi-mono's head at fetch time was `bb65e3e4…`, also
    absent from lane and fleet). A grammar class keyed only on an in-token
    `owner/repo@<hex>` clears neither; the plan's "or otherwise an explicit
    third-repository citation" clause at line scope is the load-bearing one.
    No SOURCES row edited.

## Measurements I own

- Base anchor, my own two runs with direct exit capture (not the L1's receipt):
  `--repo .` from the lane root and the absolute `--repo <lane>` form both
  print `guards 5 of 5; tip battery exit 0: 1 of 6` and exit 1 (wall 115.3 s
  each). Matches the plan and
  `.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` (which ends `exit=1`).
- Composed stack (Y01 bytes) in my scratch clone at tip
  `38ec6d8d6f82d941e0f9a048c5ce8c8be4f120f8`: `guards 5 of 5; tip battery exit
  0: 6 of 6`, exit 0 — all five guards PASS, all six gates exit 0.
- E10's published stack patch applied in my scratch clone (tip
  `bcd381a024ec4588bb432422731e83ffbfebe608`), counter = their
  `check_tip_battery.amended.py`: `guards 5 of 5; tip battery exit 0: 6 of 6`,
  exit 0. Agrees with their two published receipts. This is the FULL STACK
  world, not one of the plan's W0-W7 CONTROL worlds; the plan's kill rule
  targets a control world reaching 6 of 6. I score nothing; the distinction
  is stated for the L1.
- The symlink repair resolves only in a fleet-shaped tree (the lane's parent
  must hold the fleet); there the target is byte-identical to the pinned fleet
  file, and in a bare clone the link dangles (fails closed).

## Not done (by design)

No claim after-value scored; no control world scored; no counter narrowed, no
guard logic edited, no artifact repaired; no MANIFEST.json / templates /
scripts / .ufo/state / corpus / SKILL.md / PROVINCE.md / verifiers edits; no
lane commit, add, checkout, stash or push; no credential, token or `op://`
reference in any file or message. No tool was installed or upgraded this wave.

## Addendum: the lane tip moved during the wave

The L1 landed two plan-only commits mid-audit (`308bff9`, `a481913b` — each
touching `plans/round-80.md` only). I re-verified at the new tip
`a481913bafeb1ec5c231fd581f13da6ae5a306dc`: the counter bytes are unchanged
(sha256 `e33b17d7…`), `LINE_CAP` is still 40 and the pin table still carries
no new blob — E5 has not landed in the lane yet — and all six instrument blobs
at the tip are the BASE blobs, all already members of the pin table. Both
plan addenda agree with my measurements: Addendum 1 states E5's exact amended
line set (which is the shape of the published `check_tip_battery.amended.py`,
sha256 `15cc1761…`, self-test 0 failures / 69 assertions, exit 0) and the
pin-ordering fact I measured (integrity pin = the E04∘E05 COMPOSED blob, not
the E04-only `051b8c5f…`); Addendum 2 corrects the base `commit_unresolvable`
locator to `corpus/SOURCES.md:171-172` / `7bb48f21…`, exactly what I measured
in §7.9. The amended plan still calls the base tip-battery ABSOLUTE-form
receipt "pending"; my own absolute-form run produced the identical line and
exit 1 (§ Measurements I own) and is available to the L1 as a receipt.

## Addendum 2: E05 landed, E06 re-published (post-audit re-check)

Both landed after the first draft of this report; I recomputed everything from
primary bytes.

- **E05 CONFIRMED.** Patch sha256
  `a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3` (equals its
  own `.patch.sha256`). Applied to base after E04 (both rc 0 in my scratch
  clone): `verify_corpus_integrity.py` = `68ccce1c152c915e16893a5157c9d5878df779fb`,
  `verify_corpus_independent.py` = `e887de71892ecfc6be5b3f47e362ce8a766c5c89` —
  exactly E05's published `.blobs` / `.combined-blob.txt`. Reverse order (E05
  first, E04 second) gives the SAME two blobs, so the composition is
  order-independent.
- **Cap is exactly spent.** Six-instrument numstat vs the pinned r72 base
  `072048fa`: 22/3 + 10/3 + 28/2 = **60 added / 8 deleted**. The guard tests
  `added > 60`, so this PASSES with **zero headroom**; one more added line in
  any instrument fails `instrument-size`.
- **The new E06 counter replaces the pins.** `build/Kb80E06CounterErratum.sha256`
  = `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`; my
  recomputation of `check_tip_battery.amended.py` matches it; `LINE_CAP = 60`;
  pin rows now carry `68ccce1c…` / `e887de71…`; `grep -c "cc18261\|89f392d"` = 0,
  i.e. the Y01 pins are gone rather than kept alongside. Self-test 0 failures /
  69 assertions, exit 0 (my run). Consequence: a Y01-bundled stack, or an
  E04-only stack (`051b8c5f…` is also unpinned), now fails `instrument-pin`.
  E05's own `pin-reconciliation.txt` recommends keeping both pairs; E06 shipped
  the narrower variant. Whichever patch lands, the pin rows must name the bytes
  that land.
- **My own stack measurement** (E04+E05 in a scratch clone at tip
  `270056b53e2e44186ceb7fadb78979b7a46cbc32`, new counter, `--fleet` the fleet
  root): `guards 5 of 5` — all five guards PASS including `instrument-pin` at
  60/8 exactly at the cap — and `tip battery exit 0: 1 of 6`, exit 1. The 1 of 6
  is the other repairs' absence in this minimal stack (no registry rows, no
  symlink, no coverage rows/baseline), so the five non-sweep gates keep their
  base reds. The full stack (E10, Y01 bytes, own counter) reads
  `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0.
- **E05's class effect**, quoted from its own `stack-integrity.json` (not
  re-measured by me): `commit_unresolvable 0`, `commit_external 2`,
  `commit_total 46`, `report_dead 0`, `unindexed 0`.

## Risks / blockers

- E05 landed late; its blobs are `68ccce1c…` / `e887de71…` and the NEW E06
  counter (`20e49601…`) pins exactly those. But that counter no longer pins
  Y01's `cc182613…` / `89f392d…` nor E04's `051b8c5f…`, so a Y01-bundled or
  E04-only stack fails `instrument-pin`. The pin rows must match the landed
  patch; E05's `pin-reconciliation.txt` recommends keeping both pairs, E06
  shipped replacement.
- The E04+E05 stack spends the cap exactly (60 added / 8 deleted, cap 60): any
  further instrument growth trips `instrument-size`.
- The C2 counter is unmeasurable until `SELF_SHA` is refilled, its print
  statements still emit the r79 strings with `TARGET = 5` and `ENTRY` still at
  the `-round79.md` path, and the S229 Q70 defect independently makes the msaf
  surface unsatisfiable — so C2's "6 of 6" is unreachable as of this audit.
- `.ufo/waves/round-79/snapshots/MANIFEST.sha256` still does not exist in the
  committed tree (six per-id `.manifest` files only); C2's conjunct (c) exits 2
  without it.

VERDICT: Every reachable published pin matches my independent recomputation (counter sha, six base instrument blobs, E04 patch sha + result blob, fleet round-76 sha, six snapshot pins, the Y01 composed pair, and — post-audit — E05's `68ccce1c…`/`e887de71…` and the new E06 counter `20e49601…` whose pins equal E05's bytes); the disagreements are path/naming errors, a missing committed MANIFEST.sha256, a stale SELF_SHA, a red-self-test counter copy, a pin table that replaced rather than extended the reviewed blobs, a cap that is spent exactly, and a structural Q70 defect that makes the C2 "6 of 6" unreachable — each reported with the command and exit that show it, none repaired.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E16PinAudit.txt
