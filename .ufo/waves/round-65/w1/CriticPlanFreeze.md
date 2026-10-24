# CriticPlanFreeze — round-65 wave-1: plan-freeze discipline audit

Scope: (a) commit order — plan freeze `2fdfc1fd` before implementation `80bb8921`;
(b) byte-identity of the frozen predicate sentence across plan / SCORECARD / receipts;
(c) no after-state counting before the freeze (receipt commits vs freeze commit).
Lane repo only, read-only; all evidence from committed bytes.

## Verdict

Freeze **order holds and is clean**; plan immutability holds; no receipt file exists
at or before the freeze commit. But two defects found: **D1 — `FLOORS-after.txt`
records a state no committed revision can produce** (false "@ 80bb8921" provenance,
unpinned), and **D2 — the "same sentence in plan, counter and receipt" claim is
literally false** (three byte-diffs plus the sentence is absent from every receipt
file). Both are fixable provenance/wording defects; neither indicates fabricated
measurement — the C1/C2 predicates hold on committed bytes at `80bb8921`.

## A. Commit order — VERIFIED

```
$ git show -s --format='%h | %ci | %s' <revs>
2fdfc1f | 2026-10-24 02:42:52 | round-65: plan freeze + before-controls + S121 snapshot
80bb892 | 2026-10-24 03:01:30 | round-65: C1 closing package ... 223->234 ... checklist 1852->1862
5253b28 | 2026-10-24 03:03:37 | round-65: measurement receipts at 80bb8921 ...
0e104f4 | 2026-10-24 03:10:39 | round-65: frontier step ... + SCORECARD round-65 annotations ...
```
Parents: `2fdfc1f^ = c98d1378236b…` (the r64 tip named as base in the plan),
`80bb892^ = 2fdfc1f`, `5253b28^ = 80bb892` — linear, monotone timestamps, no rewrite.
`git diff 2fdfc1f HEAD -- plans/round-65.md` → empty; `git log -- plans/round-65.md`
shows exactly one commit. **Plan is immutable since freeze.**

## B. No after-state before the freeze — VERIFIED

Freeze commit `git show --stat 2fdfc1f`: only `census-before.txt` (16 W04 + ok row =
17 lines, 118 census rows per plan), `controls/C1-before.txt` (223 assertions, sha
`f8f69cad…`, `@ c98d137`), `controls/C2-before.txt` (`"fail": 1`, exit 1 @ c98d137),
`S121.pdf`/`S121.txt`, `plans/round-65.md`. `git show 2fdfc1f:plans/round-65.md |
grep -n '234\|1862'` → **no hits** (exit 1): the landed counts did not leak into the
frozen text. `git log --reverse -- .ufo/waves/round-65/` → first receipt-bearing
commit is `5253b28` (03:03:37, post-freeze). Before-controls at the freeze carry the
correct pinned base (`@ c98d137…` headers).

## C. Byte-identity of the frozen predicate — FALSIFIED (D2)

Plan (frozen, `plans/round-65.md:57-66`), SCORECARD (`Round 65 axis annotations`,
line ~381), and receipts compared verbatim:

1. `N` instantiation — intended, per Q28 (`where N is the assertion count measured
   at landing`): plan `over N assertions`/`floor N` → SCORECARD `over 234
   assertions`/`floor 234`. Acceptable under the freeze convention.
2. **Kill-lane order differs**: plan `…M10, M12, M17, M14, SPAN_FIRST…` vs SCORECARD
   `…M10, M12, M14, M17, SPAN_FIRST…` — a retyped sentence, not a copy.
3. **Attribution clause rewritten**: plan `(SM4/SM6 attribution per the R64-M9 rule:
   pre-existing 'eligible world' / A2 cell arms respectively)` vs SCORECARD
   `(SM4 first via the M17 prefix arm, SM6 first via the pre-existing A2 cell arm,
   M11 first via pre-existing main-world collateral with the new arm as named
   witness — attribution per the R64-M9 rule and 'MutW2M7M22' F7)`.
4. **Sentence absent from every receipt**: `grep -rn 'predicate\|Frozen'`
   over `receipts/*.txt` → 0 hits; `kill conjunct`, `M11-upper`, `floor N`,
   `floor 234` → 0 hits. Receipts carry measured output + pins only.
5. C2 same pattern: plan `…PASS — before: "fail": 1, exit 1 @ 'c98d137' (10/1).
   The checklist floor moves 1852 → M…` vs SCORECARD `…PASS. Before: "fail": 1,
   exit 1 @ 'c98d137' (10/1; 'controls/C2-before.txt')` + `(self-test 1852 →
   1862…)` — instantiated + reworded; absent from `C2-governance-measure.txt`.
6. **Lane-name drift**: `M11-upper` (plan + SCORECARD predicate) / `M11-exact-case`
   (SCORECARD prose) / `M11-page-no-lower` (kill-receipt lane label). Receipt header
   discloses the M11 kill is collateral (pre-existing main-world arms die first;
   new arm FAILs as named witness, MutW2M7M22 F7) — disclosed, so not hidden, but
   three names for one arm defeats mechanical cross-checks of the kill conjunct.

Under a charitable "same predicate modulo (sha256, N) instantiation" reading the
substance is sustained — but the artifacts claim *the same sentence*, and that is
not true in any of the three places it must be true.

## D. `FLOORS-after.txt` false provenance — FALSIFIED (D1, strongest counterexample)

`receipts/FLOORS-after.txt` (committed `5253b28`, subject "measurement receipts at
80bb8921"), header `… # after, with scoped_rules_v32 row` — **no rev pin**:
```
PASS checklist observed=1852 floor=1852
...
PASS scoped_rules_v32 observed=234 floor=234
exit=0
```
But at the very commit it claims to measure:
```
$ git show 80bb892:verifiers/floors-registry.json → checklist floor: 1862, v32 floor: 234, total: 15
$ git show 80bb892:verifiers/check_assertion_floors.py | grep → "checklist": 1862 (both tables + docstring)
$ receipts/C2-governance-measure.txt → "0 failure(s) over 1862 assertions"
```
The bump 1852→1862 (registry + both guard tables + docstring + instrument self-test
arms) landed atomically inside `80bb892` alongside the v32 row registration. No
committed revision can print `scoped_rules_v32 floor=234` *and*
`checklist observed=1852 floor=1852` in one run — the file is a working-tree
mid-edit capture (row added, bump not yet saved), committed as an "@ 80bb8921"
receipt. Consequences: (a) it does not attest the committed-state floors conjunct;
(b) its generation time is unpinned — the mid-state was captured before the bump
save inside the implementation session, and the record cannot exclude a pre-freeze
run, which is the exact failure the freeze protocol exists to exclude
[INFERENCE: mid-edit timing is bounded to the implementation session by content;
earlier cannot be excluded]. Sibling receipts all pin revs
(`C1-close-measure.txt` "committed bytes via git archive"; `FLOORS-before.txt`
`@ c98d137`) — this one broke the discipline.

## E. Supporting checks that hold

- Receipt sha leg: `git show 80bb892:verifiers/check_scoped_rules_v32.py |
  sha256sum` = `b6cfc764…` = receipt pin (`counter sha256 b6cfc764…`).
- `C1-close-measure.txt` output satisfies instantiated predicate: `worlds reject
  7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, `self-test: 0
  failure(s) over 234 assertions`, `exit=0`.
- `C1-close-kill.txt`: every named lane exit=1 (SM1–SM6, M7, M8, M9, M10, M12,
  M17, M14, SPAN_FIRST, SPAN_LAST, M20, M11), equivalents M19/M22 exit=0,
  `RESULT: ALL OK`, `harness_exit=0`.
- `C2-governance-measure.txt`: `"fail": 0`, `exit_code 0`, `governance.citation_resolves PASS` (3 recorded corrections excused).
- Registry + guard @ `80bb892` consistent: checklist 1862 / v32 234 / total 15.

## F. Minor ordering note (D3)

`controls/FLOORS-before.txt` (the before-control for the floors leg of C1's
conjunct) was committed in `4a2defd` at 03:15:50 — *after* the after-receipts
(03:03:37) and frontier commit (03:10:39). It is pinned `@ c98d137` and correct in
content, but the freeze commit shipped no floors before-control although the C1
predicate includes the floors clause; a before-control recorded after its
after-measurement is a weak control ordering. Not a violation of "re-measure at
round start, never copy" — a completeness gap in the freeze bundle.

## Impacted axes / claims

- **Calibration (assigned axis): D1 + D2 hit.** Receipt provenance and the
  byte-identity claim are exactly what a non-author closure greps for; both are
  currently overclaimed.
- C1 depth predicate: holds at `80bb892` on committed bytes (kill battery + measure
  verified above); the floors leg is *asserted* by registry/guard/instrument
  consistency at HEAD but the *receipt* for it (D1) is not rev-attestable.
- C2 consistency predicate: holds at `80bb892` (`"fail": 0`, exit 0).
- No evidence of after-state counting committed *at/before* the freeze; the
  freeze commit itself is before-state only.

## Smallest safe corrections

1. Re-run `python3 -B verifiers/check_assertion_floors.py` on committed bytes at a
   pinned rev; rewrite `FLOORS-after.txt` with an `@ <rev>` header (or annotate the
   file as a mid-edit capture + record the rev-verified equivalent alongside).
2. Fix the convention wording once, in SCORECARD + future plans: "same predicate
   sentence modulo instantiation of (sha256, N) at landing" — and paste the
   instantiated sentence verbatim into the measure receipt header so the
   byte-identity claim is actually grep-verifiable. Publish a lane-name →
   kill-label map (the kill receipt's attribution comment half-does this for M11).
3. Record the late `FLOORS-before.txt` commitment in the round-65 lesson/LOG as a
   control-ordering note.

## Install/tooling record

None — read-only audit; stock `git`, `sha256sum`, `grep`, `python3`. Pacman pause
respected (no installs needed).

Report: .ufo/waves/round-65/w1/CriticPlanFreeze.md
