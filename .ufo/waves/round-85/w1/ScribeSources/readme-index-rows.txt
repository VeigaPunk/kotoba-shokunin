# corpus/README.md — 8 coverage-map index rows added
# seat: ScribeSources · round 85 · date 2026-11-04
# section: '## Coverage map' (rows appended at the end of the table, before '## Frontier')

## the seven files that were unindexed at the base commit
(source: .ufo/waves/round-85/receipts/before-gates.txt — verify_corpus_integrity.py)
listed 7 under 'unindexed:': round-81-verifier-spotcheck.md, round-82.md,
round-82-verifier-spotcheck.md, round-83.md, round-83-verifier-spotcheck.md,
round-84.md, round-84-verifier-spotcheck.md)

## plus the eighth row the L1 directed (message: 'index row new entry+lesson round85')
  | Description trigger discipline (round 85) | `knowledge/description-trigger-discipline-round85.md` |
  — the round-85 documentary entry (ScribeC1Entry's file), which names S213 in its
    source: line and was on disk (11 597 B) when this row was written.

## each row: area | file | basis (one clause, taken from that file's own head)
  line 158  area=Round-80 lessons
             file=`lessons/round-80.md`
             basis=the round's two claims recorded as measured or pending, never as declared: `## Gate` holds the base battery reading (`guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1, with the six-gate breakdown that makes it 1 and not 2) and defers the after-value to the L1's tip receipt; the six re-op…
  line 160  area=Round-80 non-author spot-check (closure)
             file=`lessons/round-80-verifier-spotcheck.md`
             basis=written by the hyaku closure, not the lane (outside review; never edited here): round 80's step-1 conformance (the report landed through a hyaku sweep under the lane identity — attribution defect R80-D1, status-neutral), the per-claim re-check — C1 `unprovable` and killed, its three canoni…
  line 161  area=Round-81 lessons
             file=`lessons/round-81.md`
             basis=`## Gate` the two frozen predicates with their base readings and freeze receipts — C1 `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1 (registry, floors, checklist and correction-sweep exit 0; corpus integrity and independent red) and C2 `sdk allowed-tools surface documented 0 of 1`, ex…
  line 163  area=Round-81 non-author spot-check (closure)
             file=`lessons/round-81-verifier-spotcheck.md`
             basis=the hyaku closure's non-author spot-check of round 81, closed against lane HEAD e3841861 and the round-81 report landing under the lane identity, whose step-1 conformance table and per-claim re-check find C1 killed by its own controls and route the orphan-rev defect D1
  line 164  area=Round-82 lessons
             file=`lessons/round-82.md`
             basis=round 82's lane lesson (attempt 3 on the Windows host, after two Linux-host dispatches), whose two claims are C1' freshness — the host's installed-skill instruction surfaces enumerated, hashed and classified by a new read-only instrument sourced to S251 — and C2' operability, the checklist…
  line 165  area=Round-82 non-author spot-check (closure)
             file=`lessons/round-82-verifier-spotcheck.md`
             basis=the hyaku closure's non-author spot-check of round 82 attempt 3 on the Windows host, closed against lane HEAD 5f2eacd2, whose step-1 conformance table checks report attribution, the SHONEN boxes, cited-commit ancestry and freeze ordering, with its defects listed in §6
  line 166  area=Round-83 lessons
             file=`lessons/round-83.md`
             basis=round 83's lane lesson (attempt 1 on the Windows host), a fresh-start round that first spot-checks the three rejected closures (r79, r80, r81) before claiming C1 operability — the tip battery surviving Windows cleanup lock contention — and C2 freshness, the r82 host-skill drift census re-v…
  line 167  area=Round-83 non-author spot-check (closure)
             file=`lessons/round-83-verifier-spotcheck.md`
             basis=the hyaku closure's non-author spot-check of round 83, closed 2026-11-01 against lane tip 9f203ce8, written by the closure judge rather than by the lane and left for the orchestrator to commit
  line 168  area=Round-84 lessons
             file=`lessons/round-84.md`
             basis=round 84's lane lesson (attempt 1 on the Windows host), which claims C1 coverage — the second host skills root C:/Users/jpvei/.agents/skills enumerated and governed — and C2 freshness, the round-72 A1 name-uniqueness rule re-verified against the live installed surfaces and finding 2 duplic…
  line 169  area=Round-84 non-author spot-check (closure)
             file=`lessons/round-84-verifier-spotcheck.md`
             basis=the hyaku closure's non-author spot-check of round 84, a fresh-session closure judge over base ae09f71f to head 462d240c, whose conformance table passes every check and verifies the R83-V1 carry-in first
  line 170  area=Description trigger discipline (round 85)
             file=`knowledge/description-trigger-discipline-round85.md`
             basis=what S213's page states about a skill description, re-opened live 2026-11-04 (HTTP 200, 13 403 B, sha256 7cc54fbb…, byte-identical to the committed r76 snapshot): the description carries the entire triggering burden, the imperative "Use this skill when" form, the 1024-character limit, and …

## shape check on the eight new rows (same shape as the existing rows)
  rows matched: 8
  line 163  cells=5  file-cell=`lessons/round-81-verifier-spotcheck.md`
  line 164  cells=5  file-cell=`lessons/round-82.md`
  line 165  cells=5  file-cell=`lessons/round-82-verifier-spotcheck.md`
  line 166  cells=5  file-cell=`lessons/round-83.md`
  line 167  cells=5  file-cell=`lessons/round-83-verifier-spotcheck.md`
  line 168  cells=5  file-cell=`lessons/round-84.md`
  line 169  cells=5  file-cell=`lessons/round-84-verifier-spotcheck.md`
  line 170  cells=5  file-cell=`knowledge/description-trigger-discipline-round85.md`
  all rows have 5 pipe-split cells (Area | File | Basis): True
  every File cell holds exactly one backticked token: True
  no literal | inside any cell: True

## the seven inherited files are closure/lane records: indexed here, never edited
  git status --short corpus/lessons/ ->
  (empty: no lesson file was modified)

## git diff scope
  8	0	corpus/README.md
  (8 insertions, 0 deletions — no existing row was touched)
