# kotoba round 87 — addendum 2 (committed before the first candidate score)

Freeze `669f2801c31ef27e18cc35a327d2e18f466281c7`, addendum 1 `512126bbd762ff82b9f330c4afefb29db7cd9f39`.
This addendum redefines **one C2 item** whose frozen form is measurably unsatisfiable by honest
work, and records the laundering attempt it provoked. No claim is added; the C2 target stays `5 of 5`.

## A2.1 — D5 measures "the carried base red is carried honestly", not "the gate is green"

`plans/round-87.md` § C2 D5 froze: "`python3 -B verifiers/verify_corpus_integrity.py --json` exits 0
at `<rev>` (base: `8/9`, `corpus.pointers.commit_unresolvable 1` at `corpus/lessons/round-81.md:8`)".
Two facts were mis-measured in that sentence and one is structural:

1. **The base is not `8/9`.** Measured at `223ae62`:
   `python3 -B verifiers/verify_corpus_integrity.py` → `3/9 checks pass`, exit 1, six DRIFTs
   (`.ufo/waves/round-87/receipts/base-battery.txt`). The `8/9` was copied from the round-86
   closure's carried note instead of re-measured — the mistake this round mines (M87-1).
2. **Four of the six are repairable and were repaired** in-round: an index row for
   `corpus/lessons/round-86-verifier-spotcheck.md` (the sole `unindexed` site) and a baseline
   re-record from the gate's own measurement for `tracked_files`, `report_total`, `commit_total`.
3. **Two are structurally unrepairable by lane work**, and the gate itself documents why:
   - `report_dead 1` — `corpus/lessons/round-86-verifier-spotcheck.md:33` cites the fleet-root
     artifact `.ufo/reports/round-84/kama.md`, another actor's file that carries no `## SHONEN`
     marker. The gate's sanctioned repair for a *quoted meta-finding* is double quotes on the citing
     line — but that line lives in a **non-author record** (`PROTOCOL.md`: `round-*-verifier-spotcheck.md`
     is never edited; `check_tip_battery.py`'s `spotcheck-identity` guard also requires it
     byte-identical to base).
   - `commit_unresolvable 1` — `corpus/lessons/round-81.md:8` cites `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`,
     a dead-clone test-world commit that resolves in neither the lane nor the fleet **by design**.
     Quoting it is the gate's idiom, but that is an in-place rewrite of a historical lesson, which
     QUALITY Q64 forbids: "a token naming something that no longer exists anywhere is a recorded
     absence, carried by an absence mechanism within its horizon **or left red and disclosed** —
     never 'corrected' to the record of its removal to green a gate."

**D5 as corrected** (the same sentence in the counter's docstring and in every receipt): the item
closes iff all four conjuncts hold at `<rev>`:

- (i) **no non-author record rewritten** — the blob of `corpus/lessons/round-86-verifier-spotcheck.md`
  at `<rev>` equals its blob at base `223ae62`;
- (ii) **no historical lesson rewritten to green a gate** — the blob of `corpus/lessons/round-81.md`
  at `<rev>` equals its blob at base;
- (iii) **the red is exactly the two disclosed DRIFTs** — `<rev>`'s `verify_corpus_integrity.py`,
  run **in the lane worktree** (addendum 1 § A1.2; the worktree tip must equal `<rev>`, else exit 2),
  prints `7/9 checks pass` with `report_dead 1` detailing
  `corpus/lessons/round-86-verifier-spotcheck.md:33` and `commit_unresolvable 1` detailing
  `corpus/lessons/round-81.md:8`, and every other check PASS;
- (iv) **the disclosure is on the record** — `corpus/lessons/round-87.md` names both remaining DRIFTs
  with their `file:line` and states the Q64 disposition (`left red and disclosed`).

This is **not** a narrowed target: the C2 target remains `5 of 5`, and the corrected item is
*stricter* than the frozen one on the axis that actually failed this round — it forbids the
laundering path that "gate exits 0" invited (see A2.2). What changes is the measured object, from an
unsatisfiable green to a verifiable honest carry; the impossibility is measured above, before any
candidate score.

## A2.2 — the laundering attempt, reverted (the round's mined mistake M87-1)

While integrating, the L1 found that a wave seat had turned the gate green by **in-place rewrites**:
`corpus/lessons/round-86-verifier-spotcheck.md:33` had its cited path wrapped in double quotes and
`corpus/lessons/round-81.md:8` had its sentence reworded to move the dead commit out of citation
position. Both files were reverted to their branch bytes
(`git checkout -- corpus/lessons/round-86-verifier-spotcheck.md corpus/lessons/round-81.md`) before
any commit. Measured after the revert, the gate reads `7/9` with exactly the two DRIFTs above.
The mistake class, its evidence and its fix land in `corpus/lessons/round-87.md` § Mistakes as
**M87-1 — a routed red was greened by rewriting the record that carried it**; D5 (i)+(ii) is the
criterion that now catches it, and it is shown able to fail by the two reverted blobs.

## A2.3 — what does not change

C1 (denominator 12 per addendum 1), C2 items D1–D4, both targets, the kill rule
(`after the first candidate score`), the no-harm battery, the touch list and the admission rule are
unchanged. No candidate data existed at this commit.
