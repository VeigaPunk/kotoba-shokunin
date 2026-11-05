# Round 90 — addendum 1 (L1, pre-score; no candidate has been scored under the frozen predicate)

Basis: the wave's pre-landing findings (`.ufo/waves/round-90/w1/CriticClaims.md` F1/F6/F7/F10/F15/F16/F18,
`.ufo/waves/round-90/w1/ExecBattery.md` findings 1–5). The frozen-form predicate has never read exit 0
(G3 fails until the registry row lands), so no scored reading exists yet; these amendments land before
the landing measurement, as `plans/round-90.md` § Touch list provides. The plan text itself is not
edited; these rows carry the amendments.

## A1 — C1 manifest reclassification and minimum pins

- `d5-m1a-d5iii-leg-only` moves class `survivor` → `kill` (evidence: at the final bytes it flips both
  frozen d5 probes — `--self-test` arm `w_added_instance` exit 0 → 1 and the base-receipt probe
  `PASS d5iii` → `FAIL d5iii`; `.ufo/waves/round-90/w1/ExecBattery/d5-m1a-evidence.txt`). The r89
  `SURVIVED` row was measured against an earlier revision whose anchor (`if not grew:`) no longer exists
  at the final bytes (ExecBattery finding 2) — the correction to the r89 record lands in
  `corpus/lessons/round-90.md` § Mistakes/curator note (append-only; no r89 file is rewritten), and the
  manifest disposition cell names this addendum.
- The manifest counts become: kill 14, equivalent 6, survivor 0.
- The predicate gains minimum pins against an empty or trivial manifest (F6): exit 0 iff K == M and
  M ≥ 8 and E == E and E ≥ 4 and S == S_declared and guards G1–G3 PASS.

## A2 — C1 wording bounds (F7, F10)

- The kill set is the committed manifest (declared mutants); the equivalent set is GENERATED at
  measurement time by applying the three declared rewrite classes (AST comment insert, AST docstring
  marker, tokenize-level trailing whitespace) to every eligible site of each target. The `E == E` leg
  verifies that these declared rewrite classes are semantics-preserving for the frozen probe set — it
  is not a general equivalence oracle (Q47 satisfied by generation-at-measurement; Q26 headline bound:
  the claim asserts the two-sided measure over the declared classes, nothing stronger).
- The claim headline asserts K == M over the committed manifest and the generated-class survival; it
  does not assert universal mutant coverage (F9/F8 bound: 3 of the 13 ported r89 kills are
  self-test-only kills — recorded as such in the landing receipt).

## A3 — C2 headline bound (F1, F3)

- Measured outcome to be asserted: the census measured 83 installed surfaces on this host's live root;
  identical 0, drifted 0, lane-absent 83 — NO fleet lane name is installed on this host, so zero
  comparison outcomes (identical/drifted) were available; the move this claim asserts is the
  re-verification of the round-82/84 census method and the A1 name-uniqueness rule on THIS host's live
  surface (receipts pinned; NAME-COLLISION count 0), never a comparison result (Q26).
- Population: both counting methods read 83 (ScoutHostRoots: `for d …/*/ SKILL.md` glob = 83 and
  `ls | wc -l` = 83; structure 78 real dirs + 5 symlinks-to-directories, 5 pointing outside the root —
  disclosed). The predicate's N == 83 binds the measured run recorded in the receipt; a later host
  change re-reads at the entry's recheck, not mid-round.
- I + D + A == N is arithmetic (F2 bound, acknowledged; the content-bound controls ctl-c2-empty/fake
  carry the discrimination duty).

## A4 — SOURCES rows (F15, F16, F18)

- S260 `teaches` cells are bounded to clauses the saved page supports (F15: drop "indistinguishable"
  and "survives by construction" wordings; keep the located-quote-grounded vocabulary clauses); status
  `queued` at the freeze, flipped to `mined` only in the landing commit where
  `corpus/knowledge/mutation-battery-round90.md` exists (F16), with the flip logged old→new in the
  lesson.
- S261 (own-work, the r89 MutTesterGates committed bytes) is drafted by the L1 at landing (F18: the
  wave produced no candidate row), with anchor = `git show
  0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv` and the
  d5-m1a curator note from A1.
