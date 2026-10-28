# Kb80E06CounterErratum — C1 erratum E5: the amended tip-battery counter (final, E05-canonical pins)

Seat: executor, round 80 wave w1 (leaf; no spawns, no subagents). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base for every measurement: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E06CounterErratum/` (asserted `rev-parse --show-toplevel` = its own
clone before every git mutation; removed before this yield, with its receipts copied into the build dir).
No tool was installed or upgraded; pacman was not invoked; no host service was touched; no background service
was left running.

**This report describes the FINAL stream.** An earlier stream pinned the `Kb80Y01Simplify` candidate class
(blobs `cc182613…` / `89f392da…`, counter sha256 `15cc1761…`); `Kb80E05GrammarFix` published the **canonical**
repair-5 patch afterwards, the L1 ruled that the canonical E05 class is what lands, and I re-pinned to it. The
superseded stream's receipts are retained under `Kb80E06CounterErratum/superseded-y01-pins/` so the record shows
both, and its readings are marked provisional wherever they appear below.

## 0. What I produced (final)

| artefact | path (relative to the lane root) | sha256 |
|---|---|---|
| the E5 patch | `.ufo/waves/round-80/build/Kb80E06CounterErratum.patch` | `fcd886870d3689468c8fa2a5f9aad27b4e0b25e9a4ca06dcf89d7fe297b80382` |
| the amended counter FILE | `.ufo/waves/round-80/build/check_tip_battery.amended.py` | `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276` |
| the amended counter's digest | `.ufo/waves/round-80/build/Kb80E06CounterErratum.sha256` | (names the file above) |
| the exact line set | `.ufo/waves/round-80/build/Kb80E06CounterErratum.hunk-inventory.txt` | — |
| the landing recipe | `.ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh` | `b13ce13c03ca25bb6072308dd361cf2272c6c31ba2bee52383b4774e97c68ea7` |
| the recipe's first step | `.ufo/waves/round-80/build/Kb80E06CounterErratum.Y01bundle-minus-counter.patch` | `938ee8df50df1094bf7a169790bb5b6242de0b11827d046bbabbb15294a3f4b6` |
| receipts | `.ufo/waves/round-80/build/Kb80E06CounterErratum/` | — |

The patch applies to the base with `git apply --check` rc=0 and applying it reproduces the amended file
byte-for-byte (`20e49601…` both). numstat base→amended: **30 added / 12 deleted**, `verifiers/check_tip_battery.py` only.

## 1. The decisive measurement: the amended counter reads the final stack green

World (built by the landing recipe in §5c): the published bundle minus its counter hunk (E01 registry rows, the
round-76 symlink, the coverage rows, the refreshed baseline, E04's pointer fix) **plus the canonical E05 grammar
class**, my amended counter, and the C2 pieces. Rev `fc91d8d22b1099f8865acdfdd61008e54b5f4b94`, tree
`a207fafbc3920136268b96d492daf5ce4d9b59a4`. Receipt `Kb80E06CounterErratum/final-stack-e05-pins.txt`:

```
measured rev fc91d8d22b1099f8865acdfdd61008e54b5f4b94 in a fleet-shaped sandbox; base 072048fa8e8a52c707d25f7079772fa317244eb7
guarded paths 586, deleted 0; floors 15 rows; instruments added 60 / deleted 8 lines (cap 60); spotcheck base files 27
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.4s
gate verifiers/check_assertion_floors.py exit 0 wall 108.2s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.6s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6
exit=0
```

`instruments added 60 / deleted 8 lines (cap 60)` — the stack sits **exactly at** the cap (the guard fails only
above it), which is the plan's declared arithmetic `22 (at base) + 17 (E04) + 21 (grammar) = 60`. There is **zero
headroom**: one more added line in any battery script trips `instrument-size` by name.

## 2. E5's exact line set

1. **`LINE_CAP = 40` → `60`**, with a comment recording the plan's arithmetic, naming the two canonical E05 blobs,
   and stating that the pin guard — not the size bound — carries the anti-laundering load.
2. **The two pin rows gain one member each** (nothing else; base blobs stay in their rows):
   - `verifiers/verify_corpus_integrity.py` → `+ 68ccce1c152c915e16893a5157c9d5878df779fb` (E04∘E05 composed)
   - `verifiers/verify_corpus_independent.py` → `+ e887de71892ecfc6be5b3f47e362ce8a766c5c89` (E05)
   The guard's test is `blob not in allowed` over a **tuple** (counter lines 310-314), so a row may carry several
   allowed blobs — but per the L1's ruling **exactly two new members total** were added; no Y01 alternates were
   retained, so the tuple is not broadened.
3. **The two self-test fixture constants re-anchored to `LINE_CAP`**, arm semantics unchanged: the size world
   (`range(LINE_CAP + 1)` and the detail string derived as `"… gain %d lines > %d" % (LINE_CAP + 1, LINE_CAP)`)
   and the stub world (`padding=LINE_CAP + 1`, `"… lose %d lines > %d"`).
4. **The docstring/comment cap mentions updated** (base lines 42-43 "at most 40 … lose at most 40" → 60; base
   lines 105-106 "the cap stays 40" → "the cap was 40 until erratum E5").
5. **The existing instrument-pin arm's edit widened from 2 lines to 41** so the self-test itself shows the plan's
   property: a 41-line gain is inside cap 60, the size guard PASSES, and the **pin** alone rejects it. This is the
   one hunk beyond the plan's four items; the L1's §Addendum 1 lists it, and it drops out cleanly if unwanted.

Self-test on the final bytes: **`self-test: 0 failure(s) over 69 assertions`, exit 0** — the same 69 assertions as
the base counter (no arm added or dropped).

## 3. Why E5 cannot be "LINE_CAP and nothing else" — the red-before, measured

With ONLY the cap moved to 60 the counter's own self-test goes **RED at 4 failed assertions** (exit 1): the size
world grows an instrument by 41 lines and expects `"instruments gain 41 lines > 40"` (41 ≤ 60 now, so no failure,
world exits 0), and the stub world deletes 60 lines and expects `"lose 60 lines > 40"` (60 > 60 false). Receipt
`Kb80E06CounterErratum/selftest-cap60-naive.txt`. That is why item 3 above exists. Reported to the L1 before
freezing; the L1 accepted it and appended `plans/round-80.md § Addendum 1` (commit
`308bff94eab9e296631d6c1201566a02a224d559`) naming the exact line set. Nothing was narrowed to make prose true.

## 4. The two pinned blobs — provenance, composition, order-independence

**The canonical class.** `Kb80E05GrammarFix` published `Kb80E05GrammarFix.patch` (sha256
`a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3`) with `Kb80E05GrammarFix.blobs` naming
integrity `68ccce1c…` and independent `e887de71…`. I re-derived both from primary bytes in a fresh clone at the
base: apply `Kb80E04DeadPointer.patch` (apply-check rc=0), then `Kb80E05GrammarFix.patch` (apply-check rc=0 on the
E04 tree), then `git hash-object` — **`68ccce1c152c915e16893a5157c9d5878df779fb`** and
**`e887de71892ecfc6be5b3f47e362ce8a766c5c89`**, matching the published `.blobs` and `combined-blob.txt`. The
six-instrument numstat at that composition is `22/3 + 10/3 + 28/2 = 60 added / 8 deleted`.

**Why the earlier stream was wrong.** My first pins (`cc182613…` / `89f392da…`) were composed over the
`Kb80Y01Simplify` candidate class — the only published class at the time. `Kb80V03Instruments` found on primary
bytes that E05's canonical patch produces different blobs, and the L1 ruled for E05. Had the earlier pins shipped
against an E05 stack, `instrument-pin` would have failed at the tip for both gates — a bookkeeping red, not a
repo-state red. The Y01-stream receipts are retained under `superseded-y01-pins/` and are **provisional only**;
they are not the declared after-value.

**Order-independence.** E05's patch is E04-free and applies in both orders; `Kb80E05GrammarFix` measured both
orders rc=0 with an identical composed blob, and my E04-then-E05 run reproduces the published value. So the pin
does not depend on the L1's integration order.

**The reconciliation I did not take.** `Kb80E05GrammarFix` offered to keep the Y01 blobs as additional allowed
members so either class would pass. The L1 explicitly rejected that ("avoid tuple broadening"; Addendum 1 said
exactly two blobs), and I agree: a pin table that accepts both classes would stop recording *which* reviewed class
landed. Exactly two members, naming the canonical class only.

## 5. The landing recipe, and the three defects peers found in it

The recipe is one command: `bash .ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh <work-dir>`.
It lands the published bundle minus its counter hunk, **resets the two corpus gates to the base and applies E04
then E05** (so the class is canonical, not Y01's), writes my counter, adds the C2 counter + its registry row + the
C2 entry + its coverage row + the snapshot MANIFEST, commits, refreshes the baseline, commits again. Measured
output (receipt `landing-recipe-output.txt`): rev `fc91d8d2…`, counter `20e49601…`, blobs `68ccce1c…`/`e887de71…`,
numstat `22/3 + 10/3 + 28/2 = 60/8`, registry gate `63 of 63 … phantom 0`, baseline refresh `9/9 checks pass`.

Three defects were found in this recipe by peers, all real, all fixed and measured:

**5a. The fork with the published bundle (Kb80S15FreezeShas).** My patch and the bundle both modify
`check_tip_battery.py`, so `git apply Kb80E06CounterErratum.patch` on a bundle tree fails at
`verifiers/check_tip_battery.py:103`. Resolved by publishing the bundle **minus its counter hunk** as the
recipe's first step.

**5b. The C2 gap (F19).** The recipe's "6 of 6" was a **C1-only** reading; adding the C2 counter without its
registry row makes the registry gate read **62 of 63, exit 1**. Four pieces were needed, each measured: the C2
counter; its gate-registry row (S09's row inserted verbatim — the patch does not apply because the bundle shifted
`SKILL.md`); the snapshot `MANIFEST.sha256` (the six digests from the sentinel proposal, each verified against the
committed bytes before writing); and the C2 entry + its coverage-map row (inserted into the **Coverage map** table
— my first attempt put it in the Frontier table and the gate still read `corpus.index.unindexed=1`, which also made
the baseline refresh refuse). The refresh needs a **clean tree**, so the order is commit → refresh → commit.

**5c. Non-reproducibility.** Two runs gave different revs **and different trees** — the trees differing only in
`verifiers/corpus-baseline.json`'s `head`/`note`, because the refresh records **the commit sha it was refreshed
at**. Fixed by exporting fixed `GIT_AUTHOR_DATE` / `GIT_COMMITTER_DATE` (`2026-10-27T00:00:00 +0000`). The fix
was verified before the class change (two runs → rev `0c730880…`, tree `dde9e843…`, baseline `1058c8da…`, and the
freeze assembler's third run agreed).

**Citable unit.** Because the baseline embeds a commit id, the baseline file is **not a pure function of the
tree**: the citable unit is the **triple (inputs, dates, tree)**, and the freeze pins the baseline's bytes beside
the tree id. Also for reviewers: that `head` field quotes the recipe's pre-refresh commit, which resolves only
inside the producing clone (`git cat-file -t` → `commit` there; `fatal: Not a valid object name` in both the lane
and the fleet), as its own label says. Receipt `head-field-resolution.txt`.

## 6. Control worlds on the FINAL counter bytes

Every receipt carries the command's own exit status (never a pipeline's).

| world | reading | exit | receipt |
|---|---|---|---|
| **final stack** (E05 canonical class + C2) | `guards 5 of 5; tip battery exit 0: 6 of 6`; added 60 / deleted 8 | **0** | `final-stack-e05-pins.txt` |
| **W0** do-nothing (empty commit on the r80 base), absolute `--repo` | `guards 5 of 5; tip battery exit 0: 1 of 6`; added 22 / deleted 3 | **1** | `w0-final.txt` |
| **W0** the same, `--repo .` form from the lane root | `guards 5 of 5; tip battery exit 0: 1 of 6` | **1** | `w0-dot-final.txt` |
| **W-stub** integrity instrument → 2-line `sys.exit(0)` stub | `FAIL instrument-size: instruments lose 1473 lines > 60` **and** `FAIL instrument-pin: … blob e15e0b45… is not a pinned blob`; `guards 3 of 5; tip battery exit 0: 2 of 6` | **1** | `wstub-final.txt` |

The stub world is the plan's W6 shortcut control: stubbing an instrument fails **both** the size guard (it deletes
~1473 lines) and the pin guard (the blob is unpinned), and never reaches 6 of 6 under any cap. The do-nothing
world is unchanged by E5 in both `--repo` forms.

Earlier worlds measured on the superseded Y01 stream (W30 isolation — size PASS, pin FAIL; W41 — both fail) are
retained under `superseded-y01-pins/` and are **provisional**; their logic still holds, but they are not readings
of the final counter.

## 7. The same-rev contrast: what E5 actually changed (Y01-stream measurement, logic unchanged)

Run on the superseded stack, both counters against the **same rev** `b85d1e358e6fe0da18ab095e2fe8061c7bd2dce3`:

| counter | guards | battery | exit |
|---|---|---|---|
| round-72 ORIGINAL bytes (`e33b17d7…`) | **3 of 5** — `FAIL instrument-size: instruments gain 59 lines > 40` + **both** `instrument-pin` failures | `6 of 6` | **1** |
| my E5-amended bytes | **5 of 5** — all PASS | `6 of 6` | **0** |

The six **gate verdicts are identical in both runs**. The honest shape of the claim: the repo state does not move
the gates; the counter's declared bound and pin table do, and the old bound/pin table could not see the new state.
(Measured on the Y01 stack; the pin arithmetic differs on the E05 stack only in which blob is the pinned one — the
contrast's logic is identical. Receipts `round72-counter-on-stack.txt` / `amended-counter-on-stack.txt`.)

## 8. The cap arithmetic — reported, not absorbed

`instrument-size` diffs the six battery scripts against the counter's **pinned r72 base `072048fa…`**, not against
the r80 base. At the r80 base they already spend **22 added / 3 deleted**, all in `check_assertion_floors.py` (the
r76 D4 bump). E04 adds 17 → 39; E05 adds 21 (10 independent + 11 integrity) → **60**, exactly the cap. Four seats
measured this independently (me, Kb80E03IndexBaseline, Kb80E10Battery, Kb80E16PinAudit) and the L1 kept the cap at
60 with no narrowing. The budget is now spent in full: **any further added line in a battery script trips
`instrument-size` by name**, which is the plan's honest-stop channel and not something the counter should absorb.

## 9. Findings I did not repair (routed, not mine)

1. **The plan's `commit_unresolvable` pair is not the live red.** The plan names
   `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`; both gates read those as `commit_quoted`
   context (already excluded). The live red is `corpus/SOURCES.md:171` and `:172`, both hash
   `7bb48f213ac677f943d5c791199ed3dddf302f00` (rows S230/S231), where the third-repo name is a **separate**
   backticked token on the same line — so the plan's "(or otherwise an explicit third-repository citation)" clause
   is the load-bearing one, not the in-token `owner/repo@<hex>` grammar. Confirmed independently by five seats.
2. **`SOURCES.md:171` (S230) appears to cite the wrong repository's commit** (the S230 snapshot record has pi-mono
   at `bb65e3e4…`; `7bb48f21…` is the mistral-vibe commit per the S231 record). Reported by Kb80E08C2Entry; the
   frontier step forbids editing the anchor cell.
3. **`verifiers/floors-registry.json` has no row for `check_tip_battery.py`** (17 rows, none for it), so neither the
   base counter's 69 assertions nor the amended counter's are floored. Noted, not changed.
4. **A stray file sits at the lane root of `.ufo/`**: `.ufo/wapes` (a C2 quote-probe transcript, mtime 20:17). Not
   mine — my seat writes only under `.ufo/waves/round-80/build/` and this report — so I left it untouched; it is
   outside the lane's write scope and should be moved or removed before integration.

## 10. What the L1 should do next

1. **Land with the recipe** — `bash .ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh <work-dir>`
   produces the stack green on registry (63 of 63), refresh (9/9) and battery (6 of 6) in one run. If landing by
   hand: bundle-minus-counter, **reset the two gates to the base and apply E04 then E05**, then my counter, then
   the C2 pieces, then commit → refresh → commit.
2. **Record in the freeze:** counter sha256 `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`,
   patch sha256 `fcd886870d3689468c8fa2a5f9aad27b4e0b25e9a4ca06dcf89d7fe297b80382`, recipe sha256
   `b13ce13c03ca25bb6072308dd361cf2272c6c31ba2bee52383b4774e97c68ea7`, pins
   `68ccce1c152c915e16893a5157c9d5878df779fb` / `e887de71892ecfc6be5b3f47e362ce8a766c5c89`, and the line set of
   §2. **The earlier Y01-stream values (`15cc1761…`, `cc182613…`, `89f392da…`) are superseded and must not be
   frozen.**
3. **Any earlier 6 of 6 is provisional** — including my own Y01-stream stack receipt. The declared after-value
   belongs at the frozen tip, after `receipts/freeze-shas.txt` is committed, with its own receipt.
4. Route the findings in §9 to the round-80 lesson.

VERDICT: The E5-amended counter is final on the CANONICAL E05 class — LINE_CAP 40→60, the two canonical blobs pinned (`68ccce1c…` integrity / `e887de71…` independent, exactly two new members, no Y01 alternates), the two cap-40 self-test fixtures re-anchored to LINE_CAP, the pin arm widened to 41 lines so the pin alone rejects an in-cap gain — self-test green at 0 failures / 69 assertions, and MEASURED on the final C1+C2 stack at "guards 5 of 5; tip battery exit 0: 6 of 6", exit 0, with instruments added 60 / deleted 8 against the pinned r72 base (the cap exactly, zero headroom); the do-nothing world stays at 1 of 6 (exit 1) in both --repo forms and the stubbed-instrument world fails both instrument-size and instrument-pin (3 of 5, 2 of 6, exit 1); the one-command landing recipe lands that stack with registry 63 of 63 and refresh 9/9.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/check_tip_battery.amended.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum.sha256; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum.hunk-inventory.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum.Y01bundle-minus-counter.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E06CounterErratum/; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E06CounterErratum.md
