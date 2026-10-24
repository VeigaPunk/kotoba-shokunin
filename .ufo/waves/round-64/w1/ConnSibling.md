# ConnSibling — kotoba round 64 wave 1

Seat: `kotoba-r64.ConnSibling`. Read-only outside this file. No installs. No subagents. Sibling seats still running were not waited on; their in-flight kotoba reports are not inputs.

Axes named: **depth** (owned low, 9) and **consistency / calibration** (held 10). One move below improves depth and does not harm calibration. It does not rewrite either frozen predicate.

## Sweep commands and counts

Lane roots considered: 24 directories under `/home/vgpnk/Projects/shokunin/` after dropping `kotoba-shokunin`, `reports`, `research`, `scratch`, `scripts`, `templates`, `local`, `dir` (python listing, exit 0). `bash:` is a real directory name and is in the 24.

```
lanes_scanned 24
audio-shokunin:            reports/round-63, reports/round-64
chousa, game-dev-3d, kagi, kaidoku, kaidoku-sh2, kake, kama, kasegi,
kengaku, kumitate, lore, mado, mori, mori-shokukin, souji, tabi,
tameshi, tameshi-shokukin, tsukuroi, bash: :   NONE
game-dev-2d-shokunin:      reports/round-63, reports/round-64
kotodama-shokunin:         corpus/lessons/round-63.md, round-64.md,
                           round-63-verifier-spotcheck.md,
                           .ufo/waves/round-63, .ufo/waves/round-64,
                           reports/round-63, reports/round-64
revenger-shokunin:         corpus/lessons/round-63.md,
                           .ufo/waves/round-63, reports/round-63
```

Fleet copies (not lane repos): `.ufo/reports/round-63/` = `audio.md`, `game-dev-2d.md`, `kotoba.md`, `kotodama.md`, `revenger.md` (5). `.ufo/reports/round-64/` = `audio.md`, `game-dev-2d.md` (2). No `plans/round-63.md` or `plans/round-64.md` in any sibling.

Zero-hit controls (rg file counts, exit 0):

| pattern | files outside `kotoba-shokunin` |
|---|---|
| `span_missing\|g7_conjunct\|exfiltrates credentials` | **1** (`/home/vgpnk/Projects/shokunin/MANIFEST.json`, quoting this lane's own closure) |
| literal `M95` | **1** (same MANIFEST) |
| `load-bearing branch\|pinning arm\|span_missing` under `kagi-shokunin` | **0** |

Broader vocabulary is not a hit. `citation-drift|citation freshness|M95|reference-drift` under `*/corpus */plans */.ufo/waves` (excluding this lane) is 1235 kaidoku / 316 kagi / 129 kengaku / 45 tsukuroi / 30 mado / 24 tameshi / 22 kake / 19 tabi / 19 mori / 16 kama / 7 chousa / 5 souji / 5 kotodama / 3 lore / 1 revenger / 1 kumitate. `load-bearing|mutant kill|mutation testing|pinning arm|surviving mutant` is non-zero in 20 of 24 lanes (kagi 3821 down to kasegi and game-dev-3d at 13). Those counts are the noise floor: fleet mutation-testing habit, not this round's three grounds.

## Lane-by-lane verdicts

Grounds: (1) G7 span / fabricated-word check, (2) M95-class citation-freshness or citation-drift counter, (3) mutation-pinning of a load-bearing branch.

| lane | artifact read | overlap verdict |
|---|---|---|
| kotodama-shokunin | `corpus/lessons/round-64.md` (602 lines; claims header + R64-M8..M10); `corpus/lessons/round-63.md` head; `corpus/lessons/round-63-verifier-spotcheck.md` items 4–5; fleet `.ufo/reports/round-63/kotodama.md` | **Strictest near-neighbor. Method overlap, substrate independent.** O pins seven redirect-edge properties a prior residual measured unpinned, and ten byte-patched mutants must fail a pinned leg (`ACCEPT-O-64`). Ca closes seven round-63 routed defects with `accept-ca.py`. Not G7, not M95, not `span_missing`. |
| revenger-shokunin | `corpus/lessons/round-63.md` M33–M34 region; fleet `.ufo/reports/round-63/revenger.md` | **Weak method adjacency, independent ground.** C3 is an attributed forged-receipt kill (0/2 → 2/2). M34 is counter-substitution: a counter-only tree can print the frozen numbers with none of the claimed work. No r64 artifact. Not G7, not citation-rev drift. |
| kaidoku-shokunin | `.ufo/gates/citation-drift/` (`citation-drift-probe.py`, `pointer-table.json`, `expected.json`); `corpus/lessons/round-20.md` R19-D6c | **Same word, different class.** Operational pointer-table line pins and a HEAD-revision probe. Last lesson hit is round 20. Not M95 (a report names the wrong committing rev while the file's internal pin is right). No r63/r64 artifact. Not G7. |
| kake-shokunin | `corpus/SOURCES.md` S014 and the "Citation freshness" search-log line | **Independent.** Path-local freshness: citing-line ±2 window, citation text blanked before absence vocabulary (`scripts/freshness-sweep.mjs`). Not a routed-defect counter. No r63/r64 artifact. |
| kagi-shokunin | `corpus/knowledge/drift-gate.md` head | **Independent.** Host-file mode/line/sha pins (`drift-baseline.tsv`, `drift-symbols.tsv`). "Drift" here is janitor-binary drift. Zero `span_missing` / `pinning arm`. No r63/r64 artifact. |
| audio-shokunin | fleet `.ufo/reports/round-64/audio.md`; lane `reports/round-64` present | **Independent.** Valid-bits→codec step map; seven adjacent-byte boundaries. Pinning of a measured map, not a guard-branch mutant battery. Not G7, not citation drift. |
| game-dev-2d-shokunin | fleet `.ufo/reports/round-64/game-dev-2d.md` | **Rhyme only.** While-live signature gate rejects forged post-death markers and accepts genuine ones. Forgery-vs-genuine is the shape of a positive/negative witness pair, on a different substrate (process death, not backticked words). Not a mutant-pin of a load-bearing branch. |
| chousa, game-dev-3d, kaidoku-sh2, kama, kasegi, kengaku, kumitate, lore, mado, mori, mori-shokukin, souji, tabi, tameshi, tameshi-shokukin, tsukuroi, `bash:` | no `round-63`/`round-64` lesson, plan, or wave; corpus scan negative for `span_missing`, `g7_conjunct`, literal `M95` | **No hit on the three grounds.** Mutation-testing and citation-drift *words* occur in several corpora (counts above) and were not promoted to overlap. |

G7 fabricated-word checking: **no sibling.** The only non-kotoba file is the fleet MANIFEST quoting this lane.

## Strictest near-neighbor

**kotodama-shokunin, `corpus/lessons/round-64.md` R64-M9** (claim O's pin-the-unpinned-arm shape, and the sentence above `ACCEPT-O-64`). R64-M10 is the runner-up and only corroborates C2's already-declared suffix scope; it is not the move.

## What kotoba-r64 can learn

Kotodama's O claim did the same *kind* of work C1 is about to do: properties a previous round had measured unpinned were given legs, and each byte-patched mutant had to fail its pinned leg. The lesson they mined after the predicate was already green is the part that transfers. R64-M9: the claim text said each of ten mutants fails **exactly** its pinned leg, but the MUT leg launched each mutant with `--only` its pins, so a failure set equal to the pins was a property of the selector, not a measurement. An independent EDGE sweep on the repaired bytes (`reports/round-64/telemetry/exactness-sweep-o.txt`) showed the sentence was false for at least three mutants (m5 collateral on EDGE_SCHEMEREL; m1 also fails EDGE_USERINFO and EDGE_HTTPS; m2 also fails EDGE_MALTARG) while the frozen predicate stayed `ACCEPT-O-64: PASS`, exit 0. Their own receipt caveat is the rule: "MUT verifies each mutant FAILs its PINNED leg; it does not verify exclusivity." Kotoba's committed §11 table already has the split that makes this concrete: with the four arms present, SM1/SM2/SM3/SM5 die on those arms' own `A2 G7:` labels, while SM4 and SM6 die on the pre-existing `FAIL eligible world: the four counted rows are backed` (`.ufo/waves/round-63/w2/MutW2V32.md` lines 974–979). Crediting "all six red" to the four new arms would repeat R64-M9. So would adding "fails exactly this arm" above the frozen 223-assertion line — that is the sentence kotodama's sweep falsified without turning the predicate red. Do not import `accept-o.py`, the redirect-edge legs, or Ca's log-token scan; R64-M10 (a bare `W04` token flipped NITS FAIL to PASS) only confirms the vacuity C2 already forbids with suffix-scoped, boundary-tightened scans.

## Contradictions (not smoothed)

1. Kotodama's standing fix offers two disjuncts: narrow the claim to "fails its pinned leg", or add a full-leg exclusivity leg. Their later sweep shows the second disjunct's sentence is **false** on the repaired bytes. Importing exclusivity into C1 would copy a falsified sentence.
2. "All six `span_missing` mutants go red on the 223-assertion suite" (measured, §11) and "the four new arms pin all six" (not measured) are different claims. SM4 and SM6 were already red on the 219-assertion suite via `eligible world`, before the four arms existed (lines 914, 916).
3. Kaidoku's citation-drift probe and kake's S014 freshness sweep share vocabulary with M95 and share nothing else. Using either as C2's check would certify the wrong surface (pointer-table lines, or a ±2 path window) and leave the `8c4cefa` / `cbbee56` vs `@ 35d44b4b` defect uncounted.
4. Game-dev-2d's forged-vs-genuine gate and audio's adjacent-byte pins are boundary discipline on other substrates. They are not a second implementation of `g7_conjunct`.

## Proposed move (one, bounded)

**Kill-receipt discriminating-label rule, on the already-declared C1 kill-rule control. Do not edit the frozen predicate.**

When the SM1–SM6 battery is receipted, run each mutant against the **full** landed `--self-test` (no `--only` the expected arm — that is the R64-M9 selector bug) and paste the `check()` failure label. Credit a new arm only when that label is the arm's own:

| mutant | credit only if the FAIL label is |
|---|---|
| SM1 | `A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected` |
| SM2 | `A2 G7: a backticked span word shorter than four characters is not rejected` |
| SM3 | `A2 G7: a backticked span made only of stopwords is not rejected` |
| SM5 | `A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it` |
| SM4, SM6 | pre-existing `eligible world: the four counted rows are backed` — not one of the four new arms |

Collateral failures are listed and not promoted into the claim sentence. Do not add "fails exactly its arm and no other" to the predicate, the LOG suffix, or the C2 counter. The frozen predicate stays the four lines ending in `self-test: 0 failure(s) over 223 assertions`, exit 0, on the unmutated file.

## Affected axes

- **Depth: improved**, if the receipt is kept. The lowest owned axis moves because each surviving-at-219 mutant (SM1, SM2, SM3, SM5) is tied to the witness that §11 measured, not to "some assertion went red".
- **Consistency / calibration: not harmed**, and protected against the R64-M9 failure mode. The sentence above the predicate is not widened past what a full-suite label proves. C2's four checks and its suffix scope are unchanged, so the do-nothing conjunct at `078eec4` (`0 of 4`, exit nonzero) is untouched.

## Risks

- If a re-measure shows SM2 (or SM3, SM5) red only on `eligible world` while its negative-witness arm stays green, that arm did not pin. That is a C1 falsifier, not a reason to accept exit≠0.
- Recording SM4/SM6's pre-existing red as evidence the new arms work would be the calibration harm this move exists to avoid.
- Promoting the move into the frozen predicate (exclusivity required for exit 0) would desync plan, counter label, and receipt, and would encode a sentence kotodama already falsified. Out of scope.
- Copying kotodama's Ca NITS old→new sentence pattern into C2 would be a second move. Not proposed. C2 already requires computed revs, both scores, and non-hex boundaries on an appended LOG suffix.

## Verification (for the L1 after the arms exist; not run here)

The four arms are not in the committed self-test at this seat's dispatch base; this seat did not re-run §11's battery and does not treat the 2026-10-23 measurement as a fresh exit code.

After the arms land, on a scratch tree only:

1. Unmutated: `python3 -B verifiers/check_scoped_rules_v32.py --self-test` prints the four frozen lines including `self-test: 0 failure(s) over 223 assertions` and exits 0.
2. For each of SM1–SM6, the same command on the mutated copy exits nonzero and the first `FAIL` label matches the table above. Paste all six labels into the kill receipt.
3. Confirm the run was the full suite: the command line has no `--only`, and a mutant that fails an unrelated label is not credited to an arm whose label is absent.
4. Do-nothing control stays the plan's: v31 cannot print the 223 line. C2 at `078eec4` stays `r63 routed defects closed 0 of 4`.

§11's already-printed labels (lines 974–979) are the expected strings for step 2, with SM5's kill line truncated in that file at "page lack"; the full label is the `check()` string at lines 959–966.

## Dependency

No kotoba wave-1 sibling report was required. In-flight seats were not blocked on. Kotodama's `reports/round-64/telemetry/exactness-sweep-o.txt` was cited from their lesson, not re-executed.
