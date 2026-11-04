# kotoba round 87 — plan and freeze

Host: Linux `7.2.11-arch1-1`, omp 18.15.0 (ELF `/home/vgpnk/.local/bin/omp`, sha256
`6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`).
Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`.
**Base:** `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (the round-86 non-author
spot-check landing, `corpus/lessons/round-86-verifier-spotcheck.md`).
**Freeze:** this file alone, committed before any candidate data.

The round carries **two claims** on two distinct owned axes. Both are carried
from the round-86 non-author closure's routed-defect queue
(`corpus/lessons/round-86-verifier-spotcheck.md` § 6), which is the queue of
record; neither is a re-scoring of a rule the lane already holds.

Lowest-axis obligation: owned axes are **depth 9** and **consistency 10**
(`SCORECARD.md` § axes). The lowest owned axis is **depth**, and C1 works it.
The all-axes reading (freshness 8.0 / adjacency 8.0, advisory and tied) stays
the lane's open L0 question (`.ufo/l0-questions.md` round-73/74 lines) and is
not settled here; both readings are stated in the report, as rounds 47–86 did.

---

## C1 — depth (score 9, owned lowest): root semantics grounded per root

**Surface changed.** The lane's model of *which roots omp reads and by what code*.
Round 86 landed `verifiers/omp-skill-roots.tsv` (13 rows, `root_pattern` +
`binary_quote`) whose quotes are doc/string-table lines: the closure's CF1
finding is that **no code quote can satisfy the round-86 dot rule for the plugin
root**, because the ELF contains no `.omp/plugins` literal and the reader is
`Zo.join(R.path, "skills")` (`.ufo/waves/round-86/w1/ReviewerRoots/review.md`).
CF2 is that `{cwd}/` expands to every ancestor including `$HOME`; CF3/P4 is that
the sandbox hides the plugin registry files.

Round 87 adds a second, additive ledger `verifiers/omp-skill-roots-semantics.tsv`
(header `root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`) and the
counter below. The round-86 ledger and its counter are **not edited** — the
frozen round-86 counter requires exactly two tab-separated cells per row
(`check_omp_catalogue_repro.py:177-179`), so a third column there would turn its
G4 red; that is the no-harm reason for a separate file.

**Frozen predicate** (the same sentence here, in the counter's docstring and in
every receipt):

    python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
        -> prints "omp root semantics grounded N of 13", exit 0 iff N == 13 and
           guards S1-S3 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

**Row grounded** iff all four conjuncts hold for that row of
`verifiers/omp-skill-roots-semantics.tsv`:

1. **pattern** — `root_pattern` equals the row's pattern in the round-86 ledger
   at `<rev>` (no row added, dropped or renamed), contains no `..` segment and
   no wildcard in its first segment.
2. **reader** — `reader_quote` (>= 12 chars) occurs verbatim in the installed omp
   ELF **and** on an ELF line that also carries a path-join token from the frozen
   set `JOIN_TOKENS` (a token of the shape `join(`, `.join(`, `resolve(`,
   `path.join`), so a doc/string-table line cannot satisfy it.
3. **module** — `module` names a source module; the header comment
   `// packages/<module>` occurs in the ELF and the reader quote's first
   occurrence lies **after** that header's last occurrence.
4. **bound** — for a `{cwd}/` row the expansion set (the session cwd and its
   ancestors) **excludes** `$HOME` and above unless the row's pattern is a `~/`
   row, and the counter's matcher refuses any candidate root that contains a
   `..` segment after normalization. Probed on a frozen ancestor chain
   (`/home/u/proj/sub` → `/home/u/proj`, `/home/u`, `/home`, `/`).

Guards: **S1** the ledger is read from `<rev>`'s committed bytes (`git show`),
never the worktree; **S2** the ELF sha256 equals `OMP_SHA256` (else exit 2);
**S3** the ledger's 13 `root_pattern` values equal the round-86 ledger's 13 at
`<rev>` (a shrunken ledger cannot pass).

**Target:** N = 13 of 13 with S1–S3 PASS.
**Base:** `0 of 13`, exit 1 — at the base revision
`verifiers/omp-skill-roots-semantics.tsv` does not exist, so no row carries a
reader quote; the counter reports this as a **content** verdict (exit 1), not an
environment error (exit 2), per the round-68 routed defect R67-1.

**Do-nothing control (frozen counter, before data):** the cheapest path that
skips the claimed work — a ledger whose `reader_quote` cell repeats the existing
`binary_quote` doc line — must read **< 13**. Additional forgery worlds, each
required to stay red: `w_docquote` (doc string in `reader_quote`), `w_nomodule`
(module header absent from the ELF), `w_dotdot` (a `..` pattern), `w_star` (a
`*` first segment), `w_shrink` (12 rows), `w_bound` (a `{cwd}/` row whose
expansion reaches `$HOME`). Every world is committed with its receipt before
the first candidate score.

**Sourced.** C1's knowledge entry cites a `corpus/SOURCES.md` row **opened this
round** (the omp skill-loader module read in the ELF and re-opened upstream).

---

## C2 — consistency (calibration sub-axis, score 10): the five routed r86 defects close

**Surface changed.** The lane's own record defects routed by the round-86
non-author closure (`corpus/lessons/round-86-verifier-spotcheck.md` § 6 items
1–5 and 7).

**Frozen predicate:**

    python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5;
           exit 1 otherwise; exit 2 = could-not-evaluate.

**Items** (each recomputed from `<rev>`'s committed bytes; Q58):

- **D1 — tip after-values carry a committed receipt** (r86 § 6.1; the r85 D2
  recurrence). At `<rev>`: `.ufo/waves/round-86/receipts/tip-catalogue.txt` and
  `tip-registry.txt` exist, name the measured revision, carry `exit=0` and the
  lines `omp catalogue lines reproduced 215 of 215` / `gate registry rows
  conformant 67 of 67`, and the two instruments (`check_omp_catalogue_repro.py`,
  `check_gate_registry.py`) are byte-identical between the r86 landing commit
  `04647b0f715ff3c4f314b0d8f03dea28bc453688` and `<rev>` (so the reading
  carries forward).
- **D2 — the planner-seat reason is cited, not asserted** (r86 § 6.2). The
  lane's record carries the validator's own sentence verbatim —
  `planner/distiller/labrat/Main are frozen-topology seats and can never be
  swarm lanes.` — and the counter re-reads
  `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`, confirming the sentence
  occurs there and that `SWARM_ROLES` does not contain `planner`.
- **D3 — the lesson's `## Gate` carries a reject row** (r86 § 6.3):
  `corpus/lessons/round-87.md` `## Gate` holds >= 1 row whose decision cell is
  `reject` with a reason of >= 8 words.
- **D4 — the kill rule names the data boundary** (r86 § 6.4): `plans/round-87.md`
  states the instrument boundary as `after the first candidate score` verbatim.
- **D5 — the carried base red closes** (r86 § 6.7): `python3 -B
  verifiers/verify_corpus_integrity.py --json` exits 0 at `<rev>` (base:
  `8/9`, `corpus.pointers.commit_unresolvable 1` at `corpus/lessons/round-81.md:8`).

**Target:** 5 of 5, exit 0. **Base:** `0 of 5`, exit 1 (none of the five exists
at the base revision).

**Do-nothing control:** a record commit that mentions the five items in prose
but supplies no receipt, no verbatim validator sentence, a `## Gate` with a
"rejected" mention inside a paragraph rather than a row, the old kill-rule
wording and the unrepaired pointer must read **0 of 5**. `w_prose`,
`w_wrongrev` (receipt naming another revision), `w_gateprose` and
`w_norepair` worlds are committed with receipts before the first candidate
score.

---

## Kill rule (instrument boundary)

Each claim's predicate, target and kill rule are frozen by this commit. A
counter, its ledger/fixture or its pins changed **after the first candidate
score** kills that claim; an amendment committed **before** the first candidate
score is an addendum that must ship its own re-run controls, may not widen the
target and may not change the predicate sentence (the round-86 closure's ruling,
`corpus/lessons/round-86-verifier-spotcheck.md` § 2, adopted here verbatim as
the wording the closure asked for). A target is never narrowed after data; a
miss is an honest stop.

## No-harm battery

Q65 (base run) and Q72 (post-state run) apply. Base values are measured at
`223ae62` and committed as `.ufo/waves/round-87/receipts/base-battery.txt`; the
post-state battery is run after integration and committed as
`receipts/after-battery.txt`. A command that the claims turn red is replaced,
not promised. Nothing in the touch list is pinned byte-identical by an earlier
counter: the Q73 sweep `grep -n 'differs from the base\|byte-identical'
verifiers/*.py` is committed as `receipts/q73-sweep.txt`; the round-86 ledger
and counter are outside the touch list (see C1).

## Touch list

`verifiers/omp-skill-roots-semantics.tsv` (new), `verifiers/check_omp_root_semantics.py`
(new), `verifiers/check_r86_routed_repairs.py` (new), `SKILL.md` (two gate-registry
rows + one registry row each, within the 600-line budget), `corpus/knowledge/omp-root-semantics-round87.md`
(new), `corpus/SOURCES.md` (one row), `corpus/README.md` (§ Frontier note, append),
`corpus/QUALITY.md` (one criterion), `corpus/lessons/round-87.md` (new),
`corpus/lessons/round-86.md` (append-only correction block), `LOG.md` (append),
`SCORECARD.md` (append), `plans/round-87*.md`, `.ufo/waves/round-87/**`.

## Frontier step (§2b, `CORPUS.md` contract v1)

- `corpus/SOURCES.md` curated: one row opened **this round** (the omp skill-loader
  module: ELF quote + upstream re-open with access date and a <= 25-word located
  quote); every `status`/`recheck`/`used-by` change logged old→new in the lesson.
- Census before (round start, base `223ae62`) and after (round end), the frozen
  command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba`; both exit codes pasted in the report.
- One mistake mined into `corpus/lessons/round-87.md` `## Mistakes`
  (class · evidence · captured-by · fix, the fix shown able to fail).
- Sourced claim: C1 rests on the new row.
- Assimilation: `/home/vgpnk/Projects/shokuknow/merge/kotoba/` is absent on this
  host (`ls /home/vgpnk/Projects/shokuknow/merge/` → no such directory), so the
  round reports `Assimilation: none` with that command.
- `considerthese/2026-10-26.md` proposal 1 (byte/line ceiling on `SKILL.md`) is
  mined: the round measures the file and lands a QUALITY criterion (a ceiling is
  a ratchet measured at the freeze, never a promise); the floors-guard change is
  routed, not landed, because a floor red at base cannot land.

## Round shape (hyaku run 15, band 8–16)

ONE v1 wave, 14 seats, under `scripts/hyaku/ufo-wave-policy.json`
(`waveMinLanes` 8, `waveMaxLanes` 16, `maxLanes` 256): scout 2, executor 4,
scribe 3, connector 1, reviewer 1, critic 1, mutation-tester 1, sentinel 1.
Attack set (reviewer, critic, mutation-tester, sentinel) = 4 of 14 = 28.6 % >= 25 %;
connector seats 1 (<= 2). The §3 planner seat is held by the L1: the swarm
validator's `SWARM_ROLES` excludes `planner` (D2 above carries the citation);
the planning data-walk rides the connector and the two scouts.

## Admission

Both claims verify on their frozen counters at the landed revision, no axis is
harmed, and the non-author closure rules. Round 86's own lesson is honoured: the
number alone is not the evidence where a script-only world can reach the target
(Q71/Q74) — an independent mechanical generator world is scored on C1's frozen
counter and its score is named beside the target in the report and the lesson.
