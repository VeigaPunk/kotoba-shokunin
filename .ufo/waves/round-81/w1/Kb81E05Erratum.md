# Kb81E05Erratum — C1 erratum E6: the amended tip-battery counter (round 81, w1)

Seat: executor, leaf. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base for every measurement: `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Scratch: `/fast/scratch/hyaku/kotoba-r81/Kb81E05Erratum/` (four clones, each asserted
`git rev-parse --show-toplevel` = its own dir before any git operation; removed before yield).
No tool installed or upgraded; pacman not invoked; no host service touched; no background job left.
**I measured no claim after-value.** Nothing below is a reading of the C1 target; only counter-internal
self-test bytes and patch arithmetic are reported.

## 0. Deliverables (all under `.ufo/waves/round-81/build/`)

| artefact | value |
|---|---|
| `Kb81E05Erratum.patch` | sha256 `c15680f81d2684fc40ef7aeef21143f217ecf4e4fc62b9ea91a7bd5787cfcf4f` |
| `Kb81E05Erratum.sha256` (digest of the patch; `sha256sum -c` OK from the lane root) | — |
| `Kb81E05Erratum.counter-sha256.txt` | counter post-image digest + blob + numstat |
| `Kb81E05Erratum.pin-provenance.txt` | how each pin was derived, and what it supersedes |
| `Kb81E05Erratum.hunk-inventory.txt` | the exact E6 line set, by erratum item |
| `Kb81E05Erratum.selftest.txt` | self-test from the patch applied in a fresh clone |
| `Kb81E05Erratum.selftest-cap900-naive.txt` | item (c) red-before, regenerated on these bytes |

Amended counter `verifiers/check_tip_battery.py`: blob `eb00200ee6987a2fd95086915a333fe258aa6c82`,
sha256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`, 751 lines.
Base counter: blob `a356e9d101f3021687a80e73fca284e7436976d2`, sha256 `e33b17d7…`, 743 lines.
Patch numstat: **24 added / 16 deleted**, `verifiers/check_tip_battery.py` only.
`git apply --check` rc=0 and `git apply` rc=0 in a fresh base clone; applying the patch reproduces the
post-image sha256 and blob id above byte-for-byte.

## 1. What the patch changes (erratum E6, as revised pre-freeze by the L1)

E6 was first declared by the ticket as `LINE_CAP 40 → 140`. **The frozen plan (`e6d48e6`) declares
`LINE_CAP = 900` and TIGHT `(base, reviewed r81)` tuples**, per the L1's pre-freeze revision
(`LINE_CAP is 900 (not 140)`; `do NOT append to the existing tuple, REPLACE it`), and the orchestrator
confirmed that the 140 in my ticket was superseded. This patch implements the frozen shape and says so in
the prose it touches. No after-value was measured under any cap.

**Ruling history, recorded because it reversed three times and a later reader must not re-open it:** the L1
first revised 140 → 900 with tight tuples; it then issued a correction reverting to `LINE_CAP 140` with
superset tuples (and asked me to wait for "minimal" E01/E02 patches); it then reversed again and confirmed
**900 with tight tuples** as the frozen E6, explicitly withdrawing the 140/superset message. I built the
140-superset skeleton in scratch but **never published it**; every published artifact of this seat carries
900 with tight tuples, and the two pins name the seats' final (non-minimal) bytes. Both seats have stated
their bytes are final for this wave.

1. **(a) Cap bound** — `LINE_CAP = 40` → `LINE_CAP = 900`. The only executable constant changed.

**Evidence that 900/tight is the frozen text, read from the plan bytes myself** (`plans/round-81.md`,
sha256 `d6bd43ebfe7ba253898cba8df7cdcb1ceba2e5513485ac760e700b8ec6af701c`, mtime 2026-10-27T23:43):
line 15 — `INSTRUMENT_PINS for the two corpus gates reset to TIGHT tuples (<r72 base blob>, <reviewed r81
blob>) admitting exactly the round-81 post-image, LINE_CAP 40→900 as the outer no-laundering bound`;
line 26 — `(a) LINE_CAP = 40 → LINE_CAP = 900 — … measured the two reviewed r81 gate patches at a final
composed +402/-29 vs base-spent 22/3 (E01 numstat +210/-10, E02 numstat +170/-16; the earlier audit figure
+472/-31 measured pre-final patch bytes and is reconciled in .ufo/waves/round-81/receipts/freeze-shas.txt)`;
line 28 — kill rule `base-spent + measured added > 900`. `grep -c 140 plans/round-81.md` = 0. So the
`+203/-10` / `+247/-18` figures are already reconciled upstream, and my patch's prose (210/170, 402) agrees
with the frozen text.
2. **(b) Pin table** — the two corpus-gate rows become tight `(base blob, reviewed r81 blob)` tuples:
   - `verifiers/verify_corpus_integrity.py`: `(71cb2730…, e470eaae…)` → `(e470eaae…, bbee51f2…)`
   - `verifiers/verify_corpus_independent.py`: `(176abae3…, edac0df7…)` → `(edac0df7…, 59602942…)`
   The r80 addendum-1 alternates (`71cb2730…`, `176abae3…`) **leave the admitted set**. The other four rows
   are untouched, no row is dropped, and every row still admits its own base blob.
3. **(c) Self-test constants derive from `LINE_CAP`** — size world `range(41)` → `range(LINE_CAP + 1)` with
   its expectation formatted as `%d lines > %d % (LINE_CAP + 1, LINE_CAP)`; stub world `padding=60` →
   `padding=LINE_CAP + 1` with the same derived expectation. Arm semantics unchanged: a `>LINE_CAP` gain
   and a `>LINE_CAP` loss still trip `instrument-size` by name.
4. **(d) Comment cap mentions updated** — guard docstring, the r73 base comment ("the cap stays 40" → "was
   40 until round 81's erratum E6 raised it to 900", naming the measured 210/170 evidence and the
   22 + 210 + 170 = 402 arithmetic) and the E2 pin comment ("inside 40 lines" → "inside the size cap", plus
   the tight-tuple ruling and the statement that the pins, not the size bound, carry the anti-laundering
   load).

Not changed: guard ids, guard count, guard logic, the five guards' checks, `TOTAL`, `GATE_TIMEOUT_S`,
`BATTERY`, `BASE`, the frozen printed line, exit codes.

## 2. Why (c) is not optional — measured, not argued

The same final file with `LINE_CAP = 900` but the old constants (`range(41)`, `padding=60`, `"gain 41 lines
> 40"`, `"lose 60 lines > 40"`) reads **exit 1, `self-test: 4 failure(s) over 69 assertions`**: the size
world and the stub world both stop exiting 1, so both cap arms silently stop enforcing
(`Kb81E05Erratum.selftest-cap900-naive.txt`). This is the r80 E5 finding reproduced on r81 bytes: moving
the cap alone makes the counter's own arithmetic inert.

## 3. Pins — derived from primary bytes, with four pre-freeze cuts absorbed

For both pins I applied the producing seat's **published patch** in my own base clone and ran
`git hash-object` — I never copied a published `.blob` string.

| row | pinned blob (final) | source patch (final) | patch sha256 | numstat |
|---|---|---|---|---|
| `verify_corpus_integrity.py` | `bbee51f2bae5b33b123a546150e83352d68eeebc` | `Kb81E01Integrity.patch` | `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` | 210 / 10 |
| `verify_corpus_independent.py` | `59602942075d8fe77061876fb52eb32a44313697` | `Kb81E02Independent.patch` | `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` | 170 / 16 |

Both matched the values the producing seats reported. The patches touch disjoint files, so the pins are
order-independent by construction.

**Churn, declared in full** (each absorbed by re-deriving from the new patch, never by guessing):
E01 `1e5588cf…` (203/10) → final `bbee51f2…` (210/10), revised on E03's hardening asks (40-hex-only
manifest hashes by exact equality; the committed receipt must name its repository). E02 `7b37461a…`
(247/18) → final `59602942…` (170/16). `Kb81E14PinAudit` caught the E02 staleness on my intermediate patch
`c66103f3…`; I re-verified their three claims from primary bytes before repinning. Superseded blobs
(`1e5588cf…`, `7b37461a…`, and E01's reverted `19ef9268…`) are **not** in the table; a stale pin of any of
them reads `FAIL guard instrument-pin` at the tip. Both seats have since stated their bytes are frozen.

`verifiers/external-commits.json` (E01's new manifest, blob `402ac290baef66e19a4ac6bcc3b801e78ca5a035`) is
**not** pinned: E6's line set admits exactly two new pin members, both instrument blobs. Its blob is
recorded in `Kb81E05Erratum.counter-sha256.txt` as a freeze-receipt line, so a later widening of the
exemption set stays visible without touching the pin table.

## 4. Cap arithmetic (declared pre-data, from measured bytes)

`BATTERY` lists six scripts and `check_tip_battery.py` is **not** among them, so this patch's own 24 added
lines are outside the cap it edits. Over the six measured scripts, pinned r73 base → r81 base:

```
22 added / 3 deleted   (verifiers/check_assertion_floors.py only)
+210 / +10             E01  verify_corpus_integrity.py
+170 / +16             E02  verify_corpus_independent.py
= 402 added / 29 deleted  vs LINE_CAP 900  ->  498 added lines of headroom
```

Commands: `git diff --numstat 072048fa..b2842231 -- <six scripts>`, and `git apply --numstat
Kb81E01Integrity.patch` / `Kb81E02Independent.patch` in a base clone. Under the ticket's original
`LINE_CAP 140` the same arithmetic read 479 > 140 (on the then-current cuts); I escalated that to the L1 as
a pre-data overrun before measuring any after-value, and the L1's revision to 900 resolved it. Under the
current cuts the equivalent figure is 402 — also > 140, so the revision is load-bearing, not cosmetic.

## 5. Self-test — the only counter-internal reading I took

```
$ python3 -B verifiers/check_tip_battery.py --self-test      # amended clone
self-test: 0 failure(s) over 69 assertions
exit 0

$ git apply Kb81E05Erratum.patch && python3 -B verifiers/check_tip_battery.py --self-test   # fresh base clone
self-test: 0 failure(s) over 69 assertions
exit 0
```

69 assertions is the base counter's assertion count, so no arm was added, dropped, or re-scoped. The
assertion pinning the frozen line (`guards 5 of 5; tip battery exit 0: 6 of 6` on a satisfying world) is
unchanged and green.

## 6. What I ported from round 80, and what changed

- **Ported (structure, not bytes):** the r80 E5 erratum's shape — a cap change declared with arithmetic,
  self-test constants re-anchored so the cap arms keep biting, a measured red-before receipt proving the
  cap alone is inert, and pins re-derived from the producing seat's patch rather than copied from a
  `.blob`. Also ported: "the pins, not the size bound, carry the anti-laundering load".
- **Superseded:** r80's `Kb80E05GrammarFix` marker grammar for external commits (r81 `R2` binds repo→hash
  through a committed manifest plus a receipt that names its repository) and r80's `Kb80E04DeadPointer`
  (r81 `R1` adds report **content** identity on top of resolution).
- **Changed vs r80's numbers:** the cap is 900, not 60; the r80 pin members (`68ccce1c…`, `e887de71…`)
  do not appear at all — the r80 C1 stack never landed (the claim was killed) and this wave's pins name
  the r81 classes only.

## 6b. Reconciliation with the independent order check (Kb81E15Order)

`Kb81E15Order` measured the intermediate artifact `adb35625…` and flagged two departures from the erratum
as first declared: `LINE_CAP = 900` (not 140) and the pin rows losing their r80 alternates. Both are the
L1's own **pre-freeze revisions**, quoted verbatim in §1 — `LINE_CAP is 900 (not 140)` and `TIGHT tuples …
do NOT append to the existing tuple, REPLACE it`. Their reading is correct on the bytes it names and is
superseded by the current patch `c15680f8…`; their 472 vs my 402 is the two seats' pre-freeze revisions
(E01 203→210, E02 247→170). Nothing was narrowed or widened by me after seeing a reading.

## 7a. Residual defect (routed, L1-declined): the exemption manifest is unpinned

`Kb81Y01Simplify`'s YAGNI audit found that `verifiers/external-commits.json` — the data deciding which
absent hex tokens are exempt as third-repository commits — is pinned nowhere, so a laundering edit to the
manifest itself fires no guard. Their measured control on base-counter bytes: unpinned `guards 5 of 5`; one
pin row `guards 5 of 5`; a laundered second record `FAIL guard instrument-pin: verifiers/external-commits.json
blob 56ce95a… is not a pinned blob`, `guards 4 of 5`. I did **not** re-run that (it is a claim after-value);
what I can attest from bytes is the mechanism — the pin loop iterates `INSTRUMENT_PINS` with no `BATTERY`
filter (base bytes 310-314), so a data file is checked exactly like a script.

I published the fix as an **opt-in** variant rather than landing it:

- `.ufo/waves/round-81/build/Kb81E05Erratum.manifest-pin-variant.patch` — sha256
  `89932a0389587fba1a05688b7041eca5aff8bc108b2230cd36ed54036d756b2b`, numstat 28/16, counter blob
  `c8f16aa1…`, self-test `0 failure(s) over 69 assertions`; one extra row
  `"verifiers/external-commits.json": ("402ac290baef66e19a4ac6bcc3b801e78ca5a035",)` plus a note comment.
- The row's blob I verified myself from primary bytes: applying `Kb81E01Integrity.patch` (sha256 `6bbb304b…`)
  to `b2842231` and `git hash-object verifiers/external-commits.json` gives
  `402ac290baef66e19a4ac6bcc3b801e78ca5a035` (11 lines, sha256 `326fab4c…`).
- It is **not** the frozen artifact and it will **not** land this round: the L1 declined it — "the frozen E6
  line set explicitly allows exactly the two reviewed r81 gate instrument blobs; changing to add a
  data-manifest pin is post-freeze scope … Record manifest-unpinned as an explicit residual/routed defect
  with the simplifier's controls". The artifacts stay in the build dir as the **measured control** for the
  residual defect (note file: `Kb81E05Erratum.manifest-pin-variant.NOTE.txt`), and the frozen triple is
  untouched. Mitigation while the defect stands, at no line cost: the manifest blob `402ac290…` is recorded
  in `Kb81E05Erratum.counter-sha256.txt`, so a later round that edits the exemption set can compare against
  a recorded value even though no guard fires. Recommended disposition for a later round: a declared pin
  member for the manifest — the mechanism already works.
  **Residual scope, so the decline is not over-read** (Y01's scoping, agreed): W6 still reds and W9 is
  enforced by code (`external_binding` fails closed on a missing or mismatched digest), so what stays open is
  not a wide-open manifest but *widening with an internally consistent record+receipt pair* — visible to
  review, invisible to a guard. The comparison anchor is the recorded blob `402ac290…`.

Also relayed upstream, not mine to fix: E01's `external_binding` checks only the repository in the proof
while E02 also requires the hash there (latent divergence, no live red), and plan R1's identity sentence
omits the round-19 floor (Y01 measured 10 false positives without it).

## 7b. Routed, L1-decision: E01's hash-in-receipt variant (declined by me, post-freeze scope)

`Kb81E01Integrity` published a labelled variant tightening its own R2 condition:
`Kb81E01Integrity.hashcheck.patch` (sha256 `0ab1b089…`, post-image blob `53cee5a2…`, numstat 215/10, +5
lines over the pinned `bbee51f2…`), adding `and hex_id.lower().encode() in proof` so the receipt must name
the hash as well as the repository — the literal sentence of plan line 15 and E02's R2b behaviour. Their
measurement: self-test 0 failures / 179 assertions, live figures identical to the pinned bytes (the live
S231 receipt carries both), cap arithmetic 22 + 215 + 170 = 407, still inside 900.

I declined the swap and routed it to the L1, for the same reason the L1 declined the manifest pin:
post-freeze scope, after-value worlds already run, and a swap would move the pinned instrument value and
invalidate the counter sha256 frozen in `receipts/freeze-shas.txt` while buying no red-to-green this round
(the divergence is latent). `bbee51f2…` therefore stands as the pinned value. The L1 has since ruled the same way — frozen bytes land, no republish, no after-value: the variant is renamed
`Kb81E01Integrity.hashcheck-DECLINED.patch` with a sidecar stating it is outside the landing set and must not
be pinned, and the gap is routed as follow-on repair **R81-D1** (E01's `external_binding` checks the receipt's
digest pin and repository but not the cited hash; E02 checks both; the live receipt carries both, so no
current red). `bbee51f2…` therefore stands as the pinned value, and 53cee5a2… must not be pinned. If a later
round takes R81-D1, the counter plus every sidecar must be republished against the new blob and E01's old
patch must be *replaced* in the landing recipe, not applied alongside it.

## 7. Risks and open items for the L1

1. **Pin staleness is the only way this counter can go red for bookkeeping reasons.** Four pre-freeze
   cuts were absorbed; a fifth revision anywhere means this patch must be re-frozen with the new blob.
   Freeze the values in §0/§3 together, as one triple: patch sha256, counter sha256, both pin blobs.
2. **`check_tip_battery.py` has no `floors-registry.json` row** (r80's finding, unchanged — outside E6's
   line set). Its 69 assertions are unfloored, so the assertion count is not itself guarded.
3. **Order at integration:** the counter patch is independent of E01/E02 (disjoint files, verified rc=0),
   but the two pins only hold once *both* repair patches are in the tree. Landing the counter without them
   converts two `instrument-pin` rows into red — the intended signal, not a counter bug.
4. **I did not run the tip battery on any r81 stack** (105 s, and it is the claim measurement).
   L1/BatteryRunner owns that after the freeze.

VERDICT: The E6 counter patch is published and final for this wave — `LINE_CAP 40 → 900`, the two corpus-gate pin rows replaced by tight `(base, reviewed r81)` tuples (`bbee51f2…` / `59602942…`, both re-derived by me from the published patches and both matching the producing seats after four pre-freeze cuts), and the size/stub self-test constants re-anchored to derive from `LINE_CAP`; it applies clean to `b2842231` in a fresh clone, reproduces blob `eb00200e…` / sha256 `1753b11c…` byte-for-byte, and its self-test reads `0 failure(s) over 69 assertions` exit 0 on both byte paths, while the cap-only variant reads 4 failures exit 1; the measured instrument arithmetic is 402 added / 29 deleted against 900 (498 lines of headroom), and I measured no claim after-value.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.sha256; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.counter-sha256.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.pin-provenance.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.hunk-inventory.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.selftest.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E05Erratum.selftest-cap900-naive.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E05Erratum.md
