# R75Facet57 — a live gate-registry row states a figure its own script has not printed since `bf98d28`

Seat R75Facet57 (leaf, read-only). Lane `kotoba-shokunin`, HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
No lane file edited; measurements run against a throwaway clone at the same rev
(`/fast/scratch/hyaku/kotoba-r75/R75Facet57/fixture`, `git rev-parse --show-toplevel` = the fixture), removed on exit.

## 1. The facet

`SKILL.md:503` is the `## Gate registry` row for `verifiers/check_skill_evals.py`. Its verdict-map cell states:

> `skill eval facts backed 8 of 8` at the measured rev and `0 of 8` at the pinned base

Two surfaces repeat the command as the one that counts the round-70 entry:

- `corpus/knowledge/skill-eval-artefacts-round70.md:8` — `recheck: 90d — python3 -B verifiers/check_skill_evals.py --rev <rev> --fetch (the eight quotes …)`
- `corpus/README.md:133` — "counted by `verifiers/check_skill_evals.py --rev <rev>`"

Measured today: **the command prints `skill eval facts backed 1 of 8`, exit 1**, at lane HEAD and at `bf98d28`
(round 71). The level holds across the whole `bf98d28..HEAD` range by construction: 36 commits sit in it and
`git log --oneline bf98d28..HEAD -- corpus/knowledge/skill-eval-artefacts-round70.md verifiers/check_skill_evals.py`
prints nothing, so neither the entry's cited rows nor v1's pin table moved. The row is `kind = gate`, so under Q46's
reading ("the `gate` kind alone reads as a live claim gate") it asserts a live green result that does not exist, and
under Q04 ("Every `recheck:`/source command resolves and runs today") the recheck command resolves, runs, and is red —
the silent-citation form Q04 forbids.

## 2. Observation (executed, not inferred)

All runs: lane script, `--repo` = the clone, `--rev` as shown. Output verbatim.

| rev | what it is | v1 `check_skill_evals.py` | v2 `check_skill_evals_v2.py` |
|---|---|---|---|
| `7d51253f…` | r70 pinned base | `0 of 8`, exit 1 (`entry … absent`) | not run |
| `8edeb49` | row + entry land | `8 of 8`, exit 0 | not run |
| `4dba3bc` | r70 tip | `8 of 8`, exit 0 | `1 of 10`, exit 1 |
| `bf98d28` | r71 re-point to S211/S212/S213 | **`1 of 8`, exit 1** | `10 of 10`, exit 0 |
| `65a5c7a` | HEAD | **`1 of 8`, exit 1** | `10 of 10`, exit 0 |

```
$ python3 -B verifiers/check_skill_evals.py --repo . --rev HEAD
measured-rev: 65a5c7a663249e0522cc49e4a148424200d9ddfe
skill eval facts backed 1 of 8
  F1: S212 has no pinned snapshot
  … F2–F6: S212 has no pinned snapshot
  F7: S213 has no pinned snapshot
exit=1
$ python3 -B verifiers/check_skill_evals_v2.py --repo . --rev HEAD
skill eval artefacts verified 10 of 10        exit=0
$ python3 -B verifiers/check_skill_evals.py --self-test
self-test: 0 failure(s) over 13 assertions
```

The single backed fact is F8 (S211); F1–F6 cite S212 and F7 cites S213, none of which v1 can pin.

## 3. Mechanism (why the row went stale, from committed bytes)

- `corpus/knowledge/skill-eval-artefacts-round70.md:5-6` now carry `source:` lines for **S212** and **S213**
  ("supersedes S209/S210 for citation"); the entry's fact rows follow them.
- `bf98d28` (2026-10-25 11:13:29 -0300) is the commit "… C2 upstream-revision anchors — S212/S213 superseding rows
  on agentskills/agentskills@69ef37e, entry + SKILL.md re-pointed to S211/S212/S213".
- `verifiers/check_skill_evals.py:46-57` pins snapshots for **S209, S210, S211 only**; `:157` turns any other id into
  the finding above. The pin table is the frozen judgment table (Q28) and must not be widened — the successor
  `check_skill_evals_v2.py:72-89` maps S212→S209 bytes and S213→S210 bytes instead.
- So the r71 move was correct and the counter swap was correct **for the claim**; what was never updated is the r70
  registry row's figure and the two pointers that name v1 as the live instrument.

## 4. Factual support and control weakness

- The row's *mechanism* prose is still true of the script (facts, located quotes, pinned snapshots, row `mined`).
  Its **figure** is false, and so is the implicit claim that this script counts the entry today.
- `verifiers/check_gate_registry.py:21-43` reads name, kind, command, verdict-map **classes**, self-test flag,
  pinned-value paths, write scope, owner; the verdict cell is parsed only for `<code>=<class>` pairs (`:26-28`), and
  `:45-47` says outright that "The counter does not run verifier scripts or prove their actual exit statuses". A
  stale figure inside a syntactically valid verdict cell is therefore invisible to the registry gate (Q31 surface).
- `grep -c check_skill_evals verifiers/check_tip_battery.py` → **0**: the tip battery never runs this gate.
- No later record discloses the change: `grep -rn "check_skill_evals" corpus/lessons/round-7[1-4]*.md` → no hits;
  repo-wide, every reference outside `verifiers/` is a round-70 artefact plus the three surfaces above
  (`corpus/knowledge/skill-eval-artefacts-round70.md:8`, `corpus/README.md:133`, `plans/round-70.md`). [INFERENCE:
  "no record" is that grep sweep, not an exhaustive history of every round artifact.]
- The successor does not catch it either: `check_skill_evals_v2.py` reads `source:` ids only to intersect them with
  `PINNED_DOCS` (`:213-220`), so the entry's stale `recheck:` line and the registry figure affect nothing in it.

## 5. Class size (bounded, measured)

`grep -c "at the measured rev" SKILL.md` → **4** (`SKILL.md:478, 499, 501, 503`). Re-measured at HEAD:

| row | claimed | printed at HEAD |
|---|---|---|
| `:478` `check_instruction_authority.py` | `grounded 1 of 1` | `1 of 1`, exit 0 |
| `:499` `check_skill_precedence.py` | `backed 5 of 5` | `5 of 5`, exit 0 |
| `:501` `check_province_core.py` | `rows 2 of 2` | `2 of 2`, exit 0 |
| `:503` `check_skill_evals.py` | `backed 8 of 8` | **`1 of 8`, exit 1** |

So the defect is 1 of 4 today, and 3 of 4 arms already exist as a green control. The 4 rows are a census at this rev,
not the class of all future figure-bearing rows.

## 6. Candidate claim for r75 (calibration)

Do **not** size this as a depth or freshness claim: no knowledge ground moves, and the entry's substance is still
verified by a green instrument (v2, `10 of 10`). The honest shapes are:

1. **Bookkeeping repair, no axis** — annotate the row and re-point the two pointers; record it as a status change, not
   an improvement.
2. **A control claim (consistency/calibration), if a counter is built**: headline bounded to what the counter prints,
   e.g. "gate-registry figures recomputed `4 of 4`" — with the red-before **`1 of 4` at HEAD** and the green-after
   `4 of 4` both measured. The headline must not say "the registry is accurate"; the counter reads 4 rows.
3. A repair claim must name the routed cause (Q21): the cause is the r71 re-point leaving v1's row and pointers
   behind, not "a stale line".

## 7. Control design (both arms already measured on this facet)

Proposed `verifiers/check_registry_figures.py`: for each `## Gate registry` row whose verdict cell matches
`` `… N of M` at the measured rev ``, extract the backticked figure and the row's entry-command cell, run the command
at `--rev <rev>` in a sandbox clone, and require the printed `N of M` to equal the claim and exit 0.

- **Red arm**: HEAD `65a5c7a` before repair — `1 of 4`, exit 1, naming `:503` (`claimed 8 of 8, printed 1 of 8`) and
  the other three green. This is the exact world measured in §5.
- **Green arm**: HEAD after the annotation/re-point — `4 of 4`, exit 0.
- **Instantiation arm** (Q48): drive `main()` on a fixture registry with one figure changed to `9 of 9` and assert exit 1
  with the printed line; helper-only calls do not cover the path.
- A second, cheaper check needs no new script: `python3 -B verifiers/check_skill_evals.py --rev 65a5c7a | grep backed`
  must print `8 of 8` — it prints `1 of 8`. That one-liner is the falsifier, and it is already red.
- Runtime: with a local clone all four runs returned inside the 240 s cap; v1 and v2 are single-digit-second runs, the
  other three completed promptly (Q39: record wall time and load in the receipt rather than claiming headroom).

## 8. Repair, with the constraints that bind it

1. **`SKILL.md:503` verdict cell — append, do not rewrite.** Precedent in the same table: `:455` and `:480` carry
   "claim withdrawn r56/r57 before data; not a claim gate until redesigned and re-controlled". Proposed text: name the
   rev where the figure was true (`8 of 8` at `4dba3bc`) and the rev where it went red (`1 of 8` from `bf98d28`; pin
   table S209–S211, entry cites S211/S212/S213), and name `check_skill_evals_v2.py` as the live instrument. Q36/Q50
   require the figure to carry its revision; the row currently carries none.
2. **Keep `kind = gate`.** Q46: a `probe` relabel is checked by `check_gate_registry.py` first, and a `probe` may not
   carry a `--self-test` handler — v1 has one, so a relabel fails the registry gate.
3. **Do not touch v1's code or add S212/S213 to its `SNAPSHOTS`** (Q28: the judgment table is frozen; the successor
   exists for exactly that reason).
4. **Re-point `corpus/knowledge/skill-eval-artefacts-round70.md:8` and `corpus/README.md:133` at
   `check_skill_evals_v2.py`** (v2's pin table admits the rows the entry cites; measured `10 of 10`, exit 0 at HEAD).
5. **Q73 sweep already run**: `grep -n "differs from the base\|byte-identical" verifiers/*.py` shows byte-identity
   conjuncts only on `PROVINCE.md` § Frontier/§ Adjacent (`check_province_core.py:24,45,48,108`) and on six scripts
   (`check_tip_battery.py:50,54,122,328`); **no counter pins `SKILL.md` byte-identical**, so an in-cell edit to
   `:503` does not redden a historical conjunct. Line budget: `SKILL.md` is 590 lines (cap 600) and an in-cell edit
   adds 0.
6. Not verified here (out of seat scope, must be run by the integrating round): `check_gate_registry.py` and
   `verify_corpus_integrity.py`/tip battery after the edit.

## 9. Risks

1. A future "fix" that makes v1 green by widening its pin table would breach Q28 and duplicate v2; the annotation must
   say the figure is *frozen at its rev*, not broken.
2. The red figure sits in a `gate` row; a reader who trusts kind over prose will treat the lane's skill-eval gate as
   failing at every tip rev — the ambiguity is the defect, and a bare revert to "8 of 8" would be a false statement
   about today.
3. `0 of 8` at the base is true only because the entry does not exist (`:125-127` `entry … absent`), i.e. a weak
   do-nothing arm; it should not be cited as evidence of the counter's discrimination.
4. The 4-row population is a census at `65a5c7a`; a counter keyed to those four line numbers repeats the M129/M2
   mistake if later rounds add figure-bearing rows without enumerating them dynamically.
5. Editing `corpus/README.md:133` touches the corpus index; its own integrity gate was not run by this seat.

## 10. Boundary against sibling facets

This report claims only the gate-registry figure/pointer defect above. `SKILL.md:193`'s threshold × runs arithmetic
(and the S209–S213 citation parenthetical) is another facet, covered by the wave-1 reports that cite it; the
round-70 entry's S065 near-miss evidence (no committed page snapshot; `S065` row pinned to a 2026-10-22 fetch,
112,748 B, sha `909dd50a…`, while the entry quotes lines 968/981 of a 2026-10-25 text-converted fetch, 118,172 B,
sha `acb1f138…`; `grep -rn S065 verifiers/` → 0 hits) is a third facet, observed but not claimed here.

## 11. Retained evidence

```
$ git -C fixture rev-parse HEAD
65a5c7a663249e0522cc49e4a148424200d9ddfe
$ python3 -B verifiers/check_skill_evals.py --repo . --rev 7d51253f99906b8551b6a0a108761eedac00de74
skill eval facts backed 0 of 8        exit=1   (entry absent)
$ … --rev 8edeb49   -> 8 of 8, exit 0
$ … --rev 4dba3bc   -> 8 of 8, exit 0
$ … --rev bf98d28   -> 1 of 8, exit 1   (F1–F6 S212, F7 S213)
$ … --rev HEAD      -> 1 of 8, exit 1
$ python3 -B verifiers/check_skill_evals.py --self-test -> 0 failure(s) over 13 assertions
$ python3 -B verifiers/check_skill_evals_v2.py --repo . --rev 4dba3bc -> 1 of 10, exit 1
$ …                                         --rev bf98d28 -> 10 of 10, exit 0
$ …                                         --rev HEAD    -> 10 of 10, exit 0
$ python3 -B verifiers/check_instruction_authority.py --repo . --rev HEAD -> 1 of 1, exit 0
$ python3 -B verifiers/check_skill_precedence.py      --repo . --rev HEAD -> 5 of 5, exit 0
$ python3 -B verifiers/check_province_core.py         --repo . --rev HEAD -> province core rows 2 of 2, exit 0
$ grep -c "at the measured rev" SKILL.md                      -> 4
$ grep -c check_skill_evals verifiers/check_tip_battery.py     -> 0
$ grep -rn "check_skill_evals" corpus/lessons/round-7[1-4]*.md -> (no output)
$ git rev-list --count bf98d28..HEAD                         -> 36
$ git log --oneline bf98d28..HEAD -- corpus/knowledge/skill-eval-artefacts-round70.md verifiers/check_skill_evals.py
                                                             -> (no output)
```

No tool installs or updates. No live fetch (§ boundary: no source additions, no network reads of sources).
