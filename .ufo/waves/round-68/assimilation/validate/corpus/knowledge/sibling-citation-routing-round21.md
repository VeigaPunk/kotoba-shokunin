# Sibling citation routing — round 21 re-measure

Claim A artifact for round 21 (2026-10-19). Re-runs the round-16 R3 dead-token
predicate live against the five sibling `SKILL.md` files and records the delta.
Evidence: scout fragments `.ufo/round-21/scouts/A1.md` … `A7.md`; report
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-21/kotoba.md`.

## Method

Same predicate as round 16 (`corpus/knowledge/sibling-citation-routing-round16.md`
plus its companion JSON ledger): repo-rooted tokens are harvested from each
sibling `SKILL.md` and each is tested for existence/resolution. The predicate
instrument is byte-identical across rounds (kagi and kengaku lanes re-verified
the round-16 census pins reproduce bit-exactly). Sibling repos were read-only
throughout; no sibling repair was absorbed.

## Live counts at round 21 (HEAD 4e92f36)

| sibling | round-16 ledger | round-21 live | delta | notes |
|---|---|---|---|---|
| kagi | 2 | 2 | 0 | SKILL.md byte-identical to its round-16 pin; both tokens are `schematic` citation-class ellipses (actionable = false) |
| kake | 1 | 1 | 0 | SKILL.md drifted (29→31 subjects) without count drift; the occurrence line is byte-identical; route r16adj-route-kake still unacknowledged |
| kasegi | 5 | 5 | 0 | SKILL.md byte-identical to its round-16 pin; dead sites :33, :130, :304, :695, :720 |
| kengaku | 1 | 1 | 0 | SKILL.md drifted (52→69 subjects) without count drift; the brace-set token moved :578→:640, both targets exist, no repair owed |
| kumitate | 5 | 5 | 0 | SKILL.md byte-identical; occurrence keys identical (:84/:107/:183/:448/:671) |
| **total** | **14** | **14** | **0** | |

## Correction to the recorded headline

The round-16 headline carried in this repo's SCORECARD adjacency row and
LOG.md — "10 dead repo-rooted tokens (… kasegi 1 …)" — undercounts. The
round-16 ledger JSON always recorded 14 / kasegi 5, and replayed at HEAD it
still prints `kasegi unresolved 5` and fleet `unresolved 14` (scout A3; the
frozen recheck reproduces 226 subjects / 14 unresolved / 14 classified / 0
unclassified, exit 0). The SCORECARD and LOG records are corrected by the
round-21 entries; `.ufo/round-21/claims.json` keeps the error as filed — the
claim's counting command itself falsified the stated baseline, which is the
finding.

## Drift since round 16 (adjacency-relevant)

- kasegi's `../kasegi-shokunin/corpus/instruments/` gained **delegated-root resolution**
  post-round-16 (`resolve.py`, `anchorcheck.py` with ORIGIN_/MIRROR_ modes):
  measured `GONE`→`RESOLVES`, `OUTSIDE-BASE`→`IN-RANGE(ORIGIN)` (scout A6).
  Still no argument resolution; `anchorcheck.py` still always exits 0 (its
  :283) — a sibling-owned defect, routed, not fixed.
- kumitate `scripts/surface-probe.mjs` is byte-unchanged since 2026-10-13:
  still executes checklist commands without resolving arguments or delegated
  targets (scout A6). Actionable packet r16adj-12 is still live (latch
  persistence claim vs scripts that carry no such symbols) (scout A5).
- New fleet prior art since round 16 (scout A7): kasegi `test_resolve.py`
  (+12 min cases), kaidoku `citation-drift-probe.py` (11/11), kake
  `replay-proof.mjs`; and round 16's own scan had left kumitate `cite-check.mjs`
  (62/62 hermetic) uncredited.
- Live `delegated:` class usage: still zero fleet-wide — only kotoba fixtures
  and kagi's unrelated `delegated=D` ratio count (a naming collision, a
  different class).
- The packaged fleet-wide live recheck now exits 1 `source_drift` (kake and
  kengaku bytes moved); the frozen replay still reproduces the round-16
  counts exactly — a comparator property, not a defect.

## Route packets

All round-16 packets stand with delta 0: kagi ×2 (schematic class), kake ×1
(r16adj-route-kake, unacknowledged), kasegi ×5, kengaku ×1 (self-resolving
brace set), kumitate ×5 (including r16adj-12). No new packets are warranted —
the live counts equal the ledger. Sibling owners remain the repair authority

## Limit

Host-local measurement: the sibling paths above resolve on the survey host;
a fresh clone elsewhere cannot re-run the live predicate without the fleet
checkout (round-12's recorded machine-locality caveat applies).
