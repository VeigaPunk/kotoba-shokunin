# Kb81S03Scorecard — SCORECARD annotation draft (round 81, w1; revision 6)

Seat: scribe. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; landing observed at draft time: G0 `e6d48e6a9b11da4660df8145bd2f28c3238c5b83`, reconciliation `c15ebe8`, G1 `647d13d72d29281614d126fa271ff9a142137ec6`, G2 `65eaa854fff925d618f6ed1151690e52ef3d9ac4`, G3 `a597a15da200d1b3be38b0e1b567c9944c5ecb00`. Revision 2 rewrote the draft after the L1's route/response; revision 3 filled the G6 after-values the L1 relayed and recorded the rubric decision; revision 4 closed every placeholder for the G4 commit; revision 5 applied the Main ruling that C1 stops; revision 6 adds the minimal append patch `build/Kb81S03Scorecard.patch`. Written `2026-10-28T02:30Z`–`03:40Z`.

## Behaviour (revision 6)

`.ufo/waves/round-81/build/Kb81S03Scorecard.md` (19,758 B) is an append-only SCORECARD block in round-69/70/73/74/80 house style: a landing ledger (G0–G3 with contents read from `git log`/`git show --stat`), the C1 row, the C2 row, the no-harm row, and the Round-82 planned paragraph. The C1 row carries the G3 intermediate (`5 of 6`, integrity red only on the equal-mode baseline classes), then the G6 after-value both forms `6 of 6` with own exit 0 marked **falsified and not admitted**, and closes on the kill verdict; the C2 row carries the G3 composed value and the G6 after-value `1 of 1` with conjuncts a–g ok. Scores asserted: consistency **held 10**, depth **held 9** — no delta, on the rubric reasoning recorded in § Revision 3.

No placeholder remains: `grep -c '{{' build/Kb81S03Scorecard.md` → 0. The two counter hashes, the G6 measured rev, both after-values and the six-gate no-harm statement sit in the rows as text, each naming the rev or command it came from.

## Route / response

| L1 item | what changed in the draft | evidence |
|---|---|---|
| stale E6 cap 140→900, tight tuples | E6 rewritten as frozen: `LINE_CAP 40 → 900`; integrity tuple `("e470eaea…", "bbee51f2…")`, independent tuple `("edac0df7…", "59602942…")`; r80 addendum-1 members `71cb2730…`/`176abae3…` retired for these rows; the 140 is named once as a pre-freeze worktree value that never froze (M81-3) | `.ufo/waves/round-81/receipts/freeze-shas.txt`; `git show 65eaa854:verifiers/check_tip_battery.py \| sha256sum` → `1753b11c…` (blob `eb00200e`, 751 lines, 69 assertions); patch `c15680f8…`, +24/−16 |
| cap arithmetic | base-spent 22/3 + E01 +210/−10 + E02 +170/−16 = **+402/−29 ≤ 900** (498 headroom); +472/−31 named as the pre-final-patch figure, not a bound | freeze receipt; `Kb81E05Erratum.hunk-inventory.txt`; `Kb81E14PinAudit` |
| actual after-value only when receipts land | C1 after-value written as **observed, not claimed**: composed G1+G2+G3 `84f6c5a6` → `guards 5 of 5; tip battery exit 0: 5 of 6`, exit 1, integrity red only on the equal-mode baseline classes; C2 after-value `1 of 1`, exit 0, conjuncts a–g ok at composed `b3449ee2`; both rows keep `{{TIP}}`/receipt placeholders for the final | `Kb81E15Order/composed-full-tipbattery.txt`, `Kb81E15Order/C2-after.txt`, `Kb81E15Order/composed-integrity.json`, `composed-independent.json` |
| C1 no-harm checks | base readings written per receipt (registry 63/63, floors 17 PASS, checklist 11 PASS / line_budget 596 of 600, integrity 4/9 with 5 DRIFTs, independent 2 DRIFTs, sweep 0 stale, census `ok` 31 W04, SKILL 596 lines / 80,920 B); composed G3: registry 64/64, integrity red only on equal-mode classes; tip no-harm list quoted from plan § No-harm battery with `{{NOHARM}}` | `build/base-battery/index.txt` (+ `01…14`), `Kb81V04Gates-*`, `Kb81E15Order/G1-*` |
| manifest unpinned residual | recorded as a **declined, routed-to-82** residual: `external-commits.json` (blob `402ac290…`, 1176 B, 11 lines) is not in `INSTRUMENT_PINS` because E6's frozen line set admits exactly the two gate members; worlds A (no pin → silent at `4 of 6`), B (one pin line → `guards 5 of 5`), C (pinned + laundered record → `FAIL guard instrument-pin … is not a pinned blob`, `guards 4 of 5`); blob kept as hand-comparison anchor | `Kb81S01Lesson.md:19`, `Kb81Y01-probeA/B/C-*`, `Kb81Y01-receipts.txt:95-140`, `Kb81E05Erratum.counter-sha256.txt` |
| E01/E02 divergence | four classes written as residuals: external-binding **asymmetry** (E01 requires the repo named in the proof, E02 requires hash **and** repo and fails closed on contradictory duplicates → they can disagree only on a record naming the repo with a different hash); rev-prefix grammar skew (E01 first-`:` vs E02 `REV_PREFIX_RE`; `foo.md:15:…` and `HEAD@{1}:…` dead in E01, LIVE in E02); class-level count-unbounded carry; `SOFT_CROSS_CHECK` tolerating live disagreement | `Kb81S01Lesson.md:20-26`, `Kb81C03Residual.md` + `Kb81C03Residual-receipts.txt`, `Kb81E04Baseline.md:304` |
| S248 queued-used-by / W04 | written as row mechanics: L1 ruled S248 keeps `status queued` (setting it `mined` rejected) and becomes the registry's first **queued-but-used** row — at base all 8 `queued` rows carried `used-by —` and none of the 149 `mined` rows did; the status transition is routed to round 82 append-only; the separate S249 row re-cites S248's URL, so W04 duplicate-URL warnings go 31 → 32 and the census still ends `kotoba ok …` exit 0 | `Kb81S01Lesson.md:30`, `Kb81N01Sentinel`, `Kb81S05SourcesEdits.md:38-39`, `Kb81S11GateQuotes.md:158` |
| G0/G1/G2/G3 hashes | full hashes in the ledger with each commit's file set: G0 plan only; G1 corpus content + S249 snapshot/fetch/manifest + `dispositions/wapes.txt` + SOURCES/README + lesson; G2 both gate repairs + `external-commits.json` + amended counter; G3 C2 counter (1638 lines) + SKILL row/line + PROVINCE cell | `git log --oneline -10`, `git show --stat --format= <each>` |
| helper landing correction | two corrections recorded: (a) the r81 `run-battery.sh` (sha256 `19b878a1…`) is a **port** of the r80 runner that now captures the measured command's own status (`cmd >> f 2>&1; rc=$?; printf 'exit=%s\n'`) — which is why every base receipt carries `exit=` (M80-1/M81-2 closed for this runner); (b) the E6 erratum was **republished** as `c15680f8…` when the independent pin was found stale (`7b37461a…` → `59602942…`, `guards 4 of 5` on the stale bytes) | `diff .ufo/waves/round-80/build/run-battery.sh build/run-battery.sh`; `Kb81S01Lesson-pin-staleness.txt`; `Kb81E14PinAudit-obs-024022.txt` |
| placeholders | only final slots remain; a trailing HTML comment maps each and lists every command this seat ran | file tail |

## Revision 3 — G6 after-values and the rubric decision

L1 relayed the G6 observation at `daac4cc87b468d131baeaca816e7cfc478090ee3` (receipt not yet file-backed at draft time): tip battery both forms `guards 5 of 5; tip battery exit 0: 6 of 6`, each own exit 0, all six gates exit 0; `check_sdk_allowed_tools.py --repo . --rev daac4cc…` `1 of 1`, conjuncts a–g ok, exit 0. The draft now carries these as the after-values, attributed to the L1 and paired with `{{RECEIPT-C1-TIP}}` / `{{RECEIPT-C2-TIP}}` until the receipts are file-backed, and keeps exactly one tip placeholder — `{{TIP}}`, the G4 governance commit, which must re-print both lines.

Score decision uses the lane rubric, not the movement: band 10 is *repeated non-author verification in the opposite direction*. C1 stays **10** (the target is now met, but no non-author opposite-direction review of this counter exists, and r80's kill — three worlds reaching the old target while the repository was still wrong — is exactly what the band guards against). C2 stays **9** (the counted `0 of 1 → 1 of 1` is the counter's own declared floor: `the headline measures the FORM of the evidence shape, not the sourcing judgement`; one axis moving one counted unit is not a band move). No delta is asserted on either axis.

## Revision 4 — placeholders closed for G4

Per the L1 instruction, every placeholder is gone (`grep -c '{{' build/Kb81S03Scorecard.md` → 0; 18,041 B):

- C1 counter sha256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`, C2 counter sha256 `739a71810453f83c94468db25fc39c55f3bfbfdb224894a630d91e5aea86f985`.
- Both after-values cite the G6 measured rev `daac4cc87b468d131baeaca816e7cfc478090ee3` with the command and its output inline in the row, and both rows say in terms that the measurement is at G6 and never at the row's own commit — so no hash self-reference.
- `{{NOHARM}}` is replaced by the statement the L1 asked for: the tip battery's six component gates (registry, floors, checklist, corpus integrity, corpus independent, correction sweep) exit 0 at G6, with the baseline refresh having closed the corpus DRIFTs the base column records; the wider no-harm set (sources census, sibling census, report pointers) is run and cited in the round report after G4 and is explicitly not predicted in the row.

Scores unchanged and still rubric-driven: consistency 10, depth 9, no delta.

## Revision 5 — C1 kill verdict (Main ruling)

The C1 row now reads as an honest stop / kill: **unprovable, not admitted, consistency held 10, delta 0**. The G6 `6 of 6` stays in the row as a measurement, explicitly marked falsified and not admitted, with the two target-reaching control worlds cited from `w1/Kb81C01C1.md`:

- **W-A** (rev `f7388d3bf43af15b0d23386e965533ffec78e9fb`) — a self-written receipt asserting a real hash `8b1cc1b0…` (created in a separate clone; `cat-file -e` rc 128 in lane and fleet) belongs to `wrong-owner/wrong-repo`, with a manifest row and matching digest; both gates accept it as external; the world reads `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0.
- **W-C** (rev `4488e7f0a55d7d1f5968b5be7ebb42f54f073785`) — `HEAD:.ufo/reports/round-77/kotoba.md` is an 816-byte padded non-report that still carries `## SHONEN`; the world reads `6 of 6`, exit 0.

The row also corrects the attack report's attribution so the kill is not mis-owned: C01's § Counter-contract mismatch reads the plan as `LINE_CAP 140`; the frozen plan commit `e6d48e6` (and `c15ebe8`) reads `900`, so the 140 arithmetic is not part of the verdict — W-A and W-C alone carry it. C2 is untouched: `1 of 1` remains admitted evidence with no score move.

## Revision 6 — minimal append patch for G4

`build/Kb81S03Scorecard.patch` (19,091 B, sha256 `00bda7f4d0b0d742ec07dfdd1e22f399124571b50a656e2c2dfabc7a73080af2`): a ten-line pure-addition hunk appending the three finalized Round 81 rows and the Round 82 planned paragraph to the end of `SCORECARD.md`, no deletions, no placeholders (`grep -c '{{'` on the patch → 0). Hunk header `@@ -474,3 +474,13 @@` with the last three context lines being the round-74/79/80 paragraphs, so it targets the current G6 tree `daac4cc87b468d131baeaca816e7cfc478090ee3`.

Verification, all from a scratch clone at that rev (`git clone --shared`, `rev-parse --show-toplevel` asserted as the clone, removed afterwards):

- `git -C "$S/clone" diff --numstat` after appending → `10 0 SCORECARD.md`.
- `git -C "$S/clone" apply --check -v Kb81S03Scorecard.patch` → `Checking patch SCORECARD.md...` and exit 0.
- Applied for real in the clone: 476 → 486 lines, and `cmp` of the first 476 lines against the pre-append copy → identical, so prior content is unchanged.
- Read-only in the lane: `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin apply --check .ufo/waves/round-81/build/Kb81S03Scorecard.patch` → exit 0.

Scores in the appended rows: consistency **held 10** with a C1 honest stop / kill (unprovable, not admitted) and depth **held 9** with C2 `1 of 1` admitted evidence — no delta on either.

## What this seat verified itself (read-only)

`git -C . log --oneline -10`; `git rev-parse` on the four G commits; `git show --stat --format=` on each; `git show 65eaa854:verifiers/check_tip_battery.py | sha256sum` (`1753b11c…`); `git show a597a15d:verifiers/check_sdk_allowed_tools.py | sha256sum` (`739a7181…`, blob `ee2c57af`, 1638 lines); `cat .ufo/waves/round-81/receipts/freeze-shas.txt`; `cat build/base-battery/index.txt` + `tail` of `01`/`02`; `grep '^== W|^status:' build/c1_controls.txt` (10/10 PASS, all frozen lines `4 of 6`); `tail build/Kb81E15Order/composed-full-tipbattery.txt` (`5 of 6`); `cat build/Kb81E15Order/C2-after.txt` (`1 of 1`, conjuncts a–g ok, quote line 234, rev `b3449ee2`); `python3 -c json.load` on `composed-integrity.json` / `composed-independent.json`; `diff` of the two `run-battery.sh` copies; `stat -c %s .ufo/wapes` (594). No counter was executed by this seat; no tool installed.

## Findings

1. **M81-2 is closed for this round's runner, not for the older receipt.** `build/base-battery/01-tip-battery-dot.txt` and `-abs.txt` each end `exit=1`, while the earlier hand-written `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` still lacks `exit=`. The draft cites the runner receipts for the base column and no longer calls the gap open — but the older receipt remains an example of the class for the lesson.
2. **S249 / S248 duplicate URL is a ruled, measured cost, not a defect.** 32 W04 warnings with `kotoba ok` is the accepted state per L1's S248 ruling; the counter conjunct (b) is satisfiable because the census treats W04 as a warning. If a later census refuses duplicate URLs, the claim stops honestly rather than by narrowing.
3. **The strongest residual is the unpinned exemption manifest** (worlds A/B/C above): a seat can widen the exemption set with an internally consistent record+receipt pair that no guard sees, unless the manifest blob is pinned. Routed to r82; the draft states the scope of the decline (W6 still reds, W9 is enforced in code).
4. **The two corpus gates are not interchangeable** (asymmetric external binding + rev-prefix skew), and the divergence is note-stamped in one path (`SOFT_CROSS_CHECK`) while blocking in another (control W1's refresh refusal). Both are routed, not repaired.

## Out of scope / not done

No after-value measured by this seat: the G6 figures at `daac4cc…` are the L1's and are cited as G6-measured. No G6 baseline refresh, no tip battery invocation, no no-harm battery at the tip, no census, no commit. This seat read the lane read-only and wrote only its two files; the wider post-G4 no-harm battery is deliberately left to the round report rather than predicted in the annotation.

VERDICT: Revision 6 delivered — `build/Kb81S03Scorecard.patch` (sha256 `00bda7f4…`) appends the three finalized Round 81 rows and the Round 82 planned paragraph to `SCORECARD.md` as a ten-line pure addition (hunk `@@ -474,3 +474,13 @@`, no deletions, no placeholders), with `git apply --check` exit 0 in a scratch clone at G6 `daac4cc87b468d131baeaca816e7cfc478090ee3` and again read-only in the lane, and prior content byte-identical after applying; the rows hold consistency 10 (C1 honest stop / kill, unprovable, not admitted) and depth 9 (C2 `1 of 1` admitted), no delta on either.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S03Scorecard.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S03Scorecard.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S03Scorecard.md