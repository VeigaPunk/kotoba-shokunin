# ConnW2Fleet — kotoba round 64 wave 2

Seat: `kotoba-r64.ConnW2Fleet`. Read-only outside this file. No installs. No subagents. In-flight sibling seats were not waited on.

Axes named: **depth** (owned low, 9) and **consistency / calibration** (held 10). One move below improves calibration and does not harm depth. It does not rewrite either frozen predicate.

Closest sibling for the *remaining* gap is **not** kake's freshness sweep and **not** another kotodama pin leg. It is revenger's round-64 attributed-kill rule (`reports/round-64/measure.py` C4, `last.endswith(...)`, exit≠0, an unrelated assertion does not count). Kotodama's pinning legs are the closest *already-imported* implementation. Kake is the closest citation-freshness instrument and the wrong next import.

## Sweep (exit 0)

Python stdlib walk, 2026-10-24, this seat. Surfaces: fleet `.ufo/reports/round-64/*`; each sibling `reports/round-64/**/*.{md,py,txt,json}` (no `__pycache__`, skip files >2 MiB); plus, when present, `corpus/lessons/round-64.md`, `corpus/SOURCES.md`, `scripts/freshness-sweep.mjs`, `reports/round-64/{accept-o.py,accept-ca.py,claims.md,measure.py}`. Case-folded substring. Needles:

- routed_repairs: `routed repairs` | `routed defects` | `accept-ca` | `check_r64_routed` | `check_r63_routed`
- citation_freshness: `citation freshness` | `freshness-sweep` | `citing-line` | `unannotatedcites`
- kill_conjunct: `kill conjunct` | `pinned leg` | `pinned_fail` | `forged receipt stdout` | `discriminating fail`

```text
lanes 23
fleet_r64 ['audio.md', 'game-dev-2d.md', 'kotodama.md']
audio-shokunin        files=11  NONE
chousa-shokunin       files=1   NONE
game-dev-2d-shokunin  files=11  NONE
game-dev-3d-shokunin  files=1   NONE
kagi-shokunin         files=1   NONE
kaidoku-shokunin      files=1   NONE
kake-shokunin         files=2   citation_freshness=2
  corpus/SOURCES.md :: citation freshness
  scripts/freshness-sweep.mjs :: freshness-sweep
kama-shokunin         files=1   NONE
kasegi-shokunin       files=1   NONE
kengaku-shokunin      files=1   NONE
kotoba-shokunin       files=2   routed_repairs=1; kill_conjunct=1
  corpus/lessons/round-64.md :: routed defects
  corpus/lessons/round-64.md :: kill conjunct
kotodama-shokunin     files=36  routed_repairs=5; kill_conjunct=8
  reports/round-64/accept-ca.py :: accept-ca
  reports/round-64/accept-o.py :: pinned leg
kumitate-shokunin     files=1   NONE
lore-shokunin         files=1   NONE
mado-shokunin         files=1   NONE
mori-shokunin         files=1   NONE
revenger-shokunin     files=3   kill_conjunct=2
  reports/round-64/claims.md :: forged receipt stdout
  reports/round-64/measure.py :: forged receipt stdout
souji-shokunin        files=1   routed_repairs=1
  corpus/SOURCES.md :: routed defects
tabi-shokunin         files=1   NONE
tameshi-shokunin      files=1   NONE
tsukuroi-shokunin     files=1   routed_repairs=1
  corpus/SOURCES.md :: routed repairs
EXIT_SWEEP=0
```

`files=1` on a NONE or SOURCES-only lane is that lane's `corpus/SOURCES.md` (or the one extra named file). It is not a round-64 tree. Fleet `round-64/` is three files: `audio.md` (2026-10-13, valid-bits codec map), `game-dev-2d.md` (2026-10-13, while-live signature gate), `kotodama.md` (2026-10-24). No revenger fleet report yet (claims are pre-registration, not a closure).

Grep of `verifiers/check_r64_routed_repairs.py` for `span-kill|kill conjunct|SM1_branch|discriminat`: **no matches**. The C1 kill conjunct is a pasted receipt plus prose. The C2 counter does not recompute it.

## Lane table

| lane | artifact read | instrument | verdict |
|---|---|---|---|
| kotodama-shokunin | fleet `.ufo/reports/round-64/kotodama.md`; `reports/round-64/accept-ca.py` (7 legs, defects 1–4 and 8–10); `accept-o.py` MUT loop ~1043–1142; lesson `corpus/lessons/round-64.md` R64-M9 | routed-repairs counter **and** pinning-leg kill | **Closest already-imported sibling.** Ca is the same shape as `check_r64_routed_repairs.py` (computed legs over committed bytes, frozen `ACCEPT-CA-64`). O's MUT still launches each mutant with `--only` its pins (`accept-o.py` ~1107–1111) and sets `pinned_fail` from that selected set (~1120–1124). R64-M9: the exclusivity sentence is false on their repaired bytes (m1, m2, m5); the predicate still passes. Wave-1 `ConnSibling` already imported "full suite, credit the arm's own label, do not claim exclusivity" (plan E3.1). Do not import a second pin leg or the exclusivity disjunct. |
| revenger-shokunin | `reports/round-64/claims.md` C2 (lines 57–80); `reports/round-64/measure.py` lines 210–249 | kill-conjunct receipt, stricter | **Closest remaining sibling.** C4 credits a kill only when `rc != 0 and last.endswith("forged receipt stdout accepted")`. A crash or an unrelated assertion is not attributed (`claims.md` lines 73–76). Round is open; no fleet closure report. Not G7, not a routed-repairs counter. |
| kake-shokunin | `corpus/SOURCES.md` S014 and the "Citation freshness" search-log line (~149); `scripts/freshness-sweep.mjs` `annotate` ~117–122 and ~300–326, per-cite AND ~488–497, selftest case `m` ~1344–1359 | citation-freshness | **Closest freshness instrument, wrong next import.** Citing-line ±2, citation text blanked before absence vocabulary, one annotated cite must not hide an unannotated cite of the same token. No `reports/round-64`. Not M95 (report names `@ 35d44b4b` while the file committed at `8c4cefa` / `cbbee56`). Not a kill conjunct. |
| audio-shokunin | fleet `audio.md`; 10 `reports/round-64/r64-*.md` names, bodies not the three needles (sweep NONE) | none of the three | Independent. Adjacent-byte codec map, 2026-10-13. |
| game-dev-2d-shokunin | fleet `game-dev-2d.md`; same 10-name tree; sweep NONE | none of the three | Rhyme only. Forged vs genuine post-death markers. |
| souji-shokunin | `corpus/SOURCES.md` S041 | phrase only | "Routed defects lines 160-164" is their own round-14 spot-check section. No round-64 tree. Not a counter. |
| tsukuroi-shokunin | `corpus/SOURCES.md` ~261 | phrase only | Round-20 curation sentence ("support the routed repairs?"). No round-64 tree. |
| chousa, game-dev-3d, kagi, kaidoku, kama, kasegi, kengaku, kumitate, lore, mado, mori, tabi, tameshi | sweep NONE on the named surfaces | none | No round-64 report and no needle. |

## What the landed kotoba bytes already say (the contradiction)

`corpus/knowledge/g7-span-pinning-round64.md:5` (landing note):

> SM1–SM6 all red, each by its own arm's `check()` label except SM4/SM6 which the pre-existing `eligible world` arms kill — attribution per the kotodama R64-M9 lesson

The measured-record table at line 85 repeats SM6 as `red (eligible world)` on the four-arm row.

The kill receipt `.ufo/waves/round-64/receipts/C1-span-kill.txt` does not say that for SM6:

```text
SM4_page_check_dropped: exit=1 | FAIL eligible world: the four counted rows are backed: ...
SM6_branch_always_fires: exit=1 | FAIL A2: a cell the cited line supports passes: ...; FAIL A2 G7: a backticked span made only of stopwords is not rejected: ...
```

SM1, SM2, SM3, SM5's first (and, on the MutSpanArms single-failure runs, only) FAIL is the new arm's own label. SM4's first FAIL is `eligible world`. SM6's first FAIL is the pre-existing `A2: a cell the cited line supports passes`.

`w1/MutSpanArms.md` lines 196–206, SM6 on the 223-assertion suite: **10 failures**. First is the A2 cell-support line. Later lines include `eligible world`, then the **new** stopwords arm, the **new** short-word arm, and arm 4. `w1/RevC1Predicate.md` lines 248–254 already recorded this: "§11 quoted the world FAIL for SM6; my first-failing assertion is the A2 one." The landing note still uses the eligible-world sentence.

Under revenger's rule, SM6 is attributed to the A2 cell-support label only. It is not attributed to `eligible world` (that FAIL is not the registered line). It is not attributed to any of the four new arms (those FAILs are collateral). The entry's "attribution per R64-M9" clause states the lesson and then violates it.

Kake does not fix this. `corpus/knowledge/compound-clause-citation-round63.md:120-132` already keeps historical `219` inside a dated freshness note and points at 223. A path-window sweep would not see that number, and a naive "no `219` left" scan would false-red the note. Wave-1 contradiction 3 stands: using kake as a C2 check certifies the wrong surface.

## Contradictions (not smoothed)

1. "SM6 is killed by `eligible world`" (entry line 5 and table line 85) and "SM6's first FAIL is `A2: a cell the cited line supports passes`" (kill receipt line 8; RevC1Predicate lines 245–254; MutSpanArms line 200) are both in this round's artifacts. Both can be true only if "killed by" means "some later FAIL mentions". That reading also makes the new stopwords, short-word, and arm-4 labels killers of SM6, which is the credit-claim the R64-M9 lesson forbids.
2. Kotodama's standing fix still offers exclusivity. Their exactness sweep showed that sentence false for m1, m2, and m5 while `ACCEPT-O-64` stayed PASS (lesson R64-M9). SM6's ten-failure set is the same shape. Importing exclusivity would copy a falsified sentence onto a mutant this round already measured as multiply red.
3. Revenger attributes by the **last** line because their verdict is one line. Kotoba's self-test ends on `self-test: N failure(s) over 223 assertions`. A literal `last.endswith` port would un-credit SM1–SM5. The compatible part is the predicate shape (exit≠0 **and** the registered label), not the string position.
4. Kake's per-cite AND is real and is the right fix for "one annotated `219` hides another `219`". It is not the defect the landing note has. C2's four checks already refuse whole-LOG token scans (E1/E3). A fifth freshness-sweep check is a second move.

## Proposed move (one, bounded)

**Re-attribute SM6 to its first FAIL only. Do not edit the frozen predicates.**

In `corpus/knowledge/g7-span-pinning-round64.md` landing note and the "+ the four arms" table cell, replace the joint "SM4/SM6 … eligible world" credit with the receipt's first FAIL:

| mutant | credit iff exit≠0 and the first `FAIL` label is | collateral (list, do not credit) |
|---|---|---|
| SM1, SM2, SM3, SM5 | that mutant's own `A2 G7:` arm label (kill receipt lines 3–5, 7) | none on the MutSpanArms single-failure runs |
| SM4 | `eligible world: the four counted rows are backed` | the other eligible-world lines on that run |
| SM6 | `A2: a cell the cited line supports passes` | `eligible world`, the new stopwords arm, the new short-word arm, arm 4 (MutSpanArms lines 201–206) |

Same rule as revenger C4 (`rc != 0` and the registered label), with the registered label = the first `FAIL` line, because that is the line this suite actually discriminates on. Paste the collateral labels in the kill receipt; they already appear for SM6's stopwords line and should also name the later eligible-world and arm-4 lines if the receipt is refreshed. Do not reorder assertions so `eligible world` prints first. Do not add "fails exactly one arm" to the predicate, the LOG suffix, or `check_r64_routed_repairs.py`.

## Affected axes

- **Consistency / calibration: improved**, if the note and the table cell change. The entry stops claiming an eligible-world kill the receipt's first line does not show, and stops letting SM6's collateral stopwords FAIL read as a new-arm pin. The "per R64-M9" clause becomes something the pasted lines satisfy.
- **Depth: not harmed.** SM1, SM2, SM3, and SM5 stay first-FAIL pins of the four new arms. SM6 was never one of those four pins (plan E3.1; ConnSibling table). The 223-assertion predicate and the C2 `4 of 4` / base `0 of 4` conjuncts stay as frozen.

## Risks

- Refreshing the receipt by deleting the collateral stopwords FAIL, instead of labeling it collateral, would hide the R64-M9 fact. The move is to name it.
- Porting revenger's `last.endswith` unchanged credits the tally line and drops the real pins.
- Adding the credit rule to the frozen self-test sentence, or to the C2 counter, desyncs plan, counter, and receipt. Out of scope. The C2 counter's bound stays the four spot-check defects.
- Treating kake's sweep as the C2 freshness repair reopens wave-1 contradiction 3.

## Verification (for the L1; not run here)

1. After the note edit, the SM6 sentence's credited label equals `C1-span-kill.txt` line 8's first `FAIL` and `MutSpanArms.md` line 200. It does not equal `eligible world`.
2. SM1–SM5 credited labels still match kill-receipt lines 3–7 and MutSpanArms lines 182–195.
3. `python3 -B verifiers/check_scoped_rules_v32.py --self-test` still prints `self-test: 0 failure(s) over 223 assertions`, exit 0. `python3 -B verifiers/check_r64_routed_repairs.py --rev <tip>` still prints `4 of 4`, exit 0, and the pinned base still prints `0 of 4`, exit nonzero. This seat did not re-run them.
4. Do not run `scripts/freshness-sweep.mjs` against this corpus.

## Dependency

Revenger round 64 is open (`claims.md` is a pre-registration; fleet `.ufo/reports/round-64/` has no `revenger.md`). The attribution rule was read from their committed `measure.py` and `claims.md`, not from a closure report. Kotodama `exactness-sweep-o.txt` was not re-executed; R64-M9 was read from `corpus/lessons/round-64.md`. No kotoba wave-2 sibling report was an input.
