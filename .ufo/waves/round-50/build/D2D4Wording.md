# D2 and D4 wording sweep — every lane surface, base `f3046466`, landed state `a78fec1`

Seat: `KotobaR50.D2D4Wording` (scribe, wave-50 build). Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Read-only on the lane checkout; no lane file was
edited by this seat. No tools installed or upgraded.

## Result

The round-49 closure named five overstatements. **Four of the five surfaces they were carried on are
now corrected in the landed tree (`956ee167`, `a78fec1`); five residual hits survive, and one new
false claim was introduced by the round-50 landing.** The correction reached the two SCORECARD axes
rows and the verifier docstring/help, and missed the census entry's own opening sentence and counts
line, the corpus README index row and Known-gaps prose, and the round-49 LOG landing record.

## Hit list at base `f3046466`

Class key: **A** = append-only surface (append a correction, never rewrite) — LOG.md, lessons,
knowledge entries, and the round-labelled blocks in `corpus/README.md`. **R** = rewritable row or
prose (rewritten each round) — the SCORECARD axes rows, capability rows, move-log rows, the
`corpus/README.md` index rows and Known-gaps bullets, `SKILL.md`, `PROVINCE.md`, the verifiers.

| # | path:line | phrase | class | landed state at `a78fec1` |
|---|---|---|---|---|
| 1 | `verifiers/verify_dispatch_prompts.py:487-488` | argparse `--box-proof` help: "discriminate every conjunct" | R | **corrected** — help now names the six conjuncts, one must-fail case each (`a78fec1`) |
| 2 | `verifiers/verify_dispatch_prompts.py:738-739` | `box_proof` docstring: "fixtures discriminate every conjunct" | R | **corrected** — docstring now scopes coverage to the six named conjuncts and names the four unfixtured clauses |
| 3 | `SCORECARD.md:31` | operability axes row: "**round 49 (C2 — dispatch-prompt boxes executed…**", "executes `dispatch.04` … and `dispatch.08`" | R | **corrected** — row rewritten to round-50 text; a "Round-50 qualifier (routed defect D2)" sits at the end of the evidence cell |
| 4 | `SCORECARD.md:116` | "Round 49 completed" paragraph: "dispatch-prompt boxes executed by `verifiers/verify_dispatch_prompts.py`" | A (historical round paragraph; R3's correction was appended as a new paragraph, not a rewrite) | **uncorrected** — paragraph untouched; the D2 bound now lives only in the axes row |
| 5 | `corpus/README.md:78` | Known-gaps row: "31 of 41 at round 49: `dispatch.04` and `dispatch.08` are delegated to `../verifiers/verify_dispatch_prompts.py`" | R | **uncorrected** — no six-conjunct bound, no mention of the round-50 coverage enforcement or the gate |
| 6 | `corpus/README.md:91-96` | "…are now delegated to `verifiers/verify_dispatch_prompts.py`, which executes them over `.ufo/prompts/` (its `--box-proof` prints `boxes proven 2`)" | R | **uncorrected** — same; the "executes them" clause now understates too (the proof enforces its own coverage and the gate runs it) |
| 7 | `corpus/knowledge/checklist-execution-round15.md:27` | "boxes executed by a committed instrument \| (no command existed) \| **0**" | A | **not a defect** — round-15 count of the 41 `SKILL.md` boxes, accurate for its date; leave |
| 8 | `corpus/lessons/round-49.md:6-7` | "C2 operability — `verifiers/verify_dispatch_prompts.py` executing dispatch-prompt boxes `dispatch.04` and `dispatch.08`" | A | **bounded elsewhere** — the same lesson's § C2 box proof bound (`corpus/lessons/round-49.md:102-104`) already says the proof "does not enforce its own coverage"; round-50's lesson records M31 |
| 9 | `plans/round-49.md:48` | "### C2 — operability (8.5): dispatch-prompt checklist boxes executed" | A (one plan file per round) | **not carried forward** — `plans/round-50.md` states C2 as a deletion-enforced counter, not as "executed" |
| 10 | `plans/round-49.md:76` | "The full `dispatch.08` box is executed, state clause included" | A | superseded by the round-50 plan; the closure named this line, and it is now a historical record |
| 11 | `SCORECARD.md:34` | adjacency axes row: "all 20 sibling lanes classified at pinned sibling commits **from their own bytes** (9 adjacent, 11 none, **0 contested** …)" | R | **corrected** — row rewritten to round-50 text; a "Round-50 qualifier (routed defect D4)" sits at the end of the evidence cell |
| 12 | `corpus/README.md:69` | index row: "all 20 sibling lanes classified against kotoba's province at pinned sibling commits (9 adjacent, 11 none, **0 contested** …)" | R | **uncorrected** — row byte-identical to base (`git diff f3046466 a78fec1 -- corpus/README.md` shows no change to it) |
| 13 | `corpus/knowledge/sibling-overlap-census-round49.md:9-10` | "This entry classifies all 20 against kotoba's province, **from each sibling's own committed bytes** at a pinned commit" | A | **uncorrected** — the appended round-50 section corrects the *basis column* for kake/kasegi and adds the precedence rule, but never says this opening sentence was overstated |
| 14 | `corpus/knowledge/sibling-overlap-census-round49.md:99` | "- 9 adjacent, 11 none, **0 contested** — `awk … \| sort \| uniq -c`" | A | **partially qualified** — the appended section repeats "No row moves; the counts stay 9 adjacent, 11 none, 0 contested" under the new precedence rule, but never states that the round-49 zero had no rule behind it |
| 15 | `LOG.md:2371` | round-49 landing record: "(20 rows at pinned sibling commits, one seat per lane; 7 adjacent, 13 none, **0 contested**)" | A | **uncorrected** — the falsify-wave entry at `LOG.md:2381` already supersedes 7/13 with 9/11, but nothing appends that the round-49 zero had no precedence rule behind it |
| 16 | `corpus/lessons/round-49-verifier-spotcheck.md:78-80, 125, 220, 229` | the closure's own quotations of the five phrases | A | **do not touch** — this is the routing source, and it names the defect correctly |
| 17 | `PROVINCE.md` (all of § Adjacent, § Core, § Frontier) | — | R | **clean** — no hit for any of the five phrases. The kake/kasegi rows already said the true basis ("kotoba's description names kake among the lanes that own their own SKILL.md content"), so PROVINCE was never the overstated surface |
| 18 | `SCORECARD.md:154`, `corpus/knowledge/checklist-execution-round15.md` | round-15 move-log row "7 boxes executed" | R / A | **not a defect** — a dated round-15 count of the 41 `SKILL.md` boxes, not of `dispatch.04`/`dispatch.08` |

### New false claim introduced by the round-50 landing

| path:line | text | why it is false now |
|---|---|---|
| `SCORECARD.md:261` (capability row "dispatch-prompt box check") | "… and **no gate runs `--box-proof`**" | The round-50 gate does run it. `python3 -B verifiers/verify_skill_checklist.py --json` → exit 0, detail `delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`. This row was rewritable and was left stale. |

### Two inconsistencies inside the landed text (and the falsify wave's own verdicts on them)

The round-50 falsify seat `.ufo/waves/round-50/falsify/ReviewKakeKasegiBasis.md` rates the D4
qualifier **FAILS** on the same row (`SCORECARD.md:34`): its F2 holds that the aggregator-mirrored
lessons are aggregator routing records and not a sibling-stated split (so the correct basis label is
`kotoba`), that the qualifier as first landed at `956ee167` said "found only in round 50" and spliced
into the round-49 counter command, and that the qualifier is **incomplete because it omits tameshi**
— whose round-49 basis the census itself records as kotoba's base `PROVINCE.md` line
(`corpus/knowledge/sibling-overlap-census-round49.md:147-149`). `a78fec1` already fixed the two
points that seat raised about the wording (the "found only in round 50" phrase is gone; the
qualifier moved to the end of the cell, out of the command span) and corrected the census basis to
`kotoba`, but **the tameshi omission stands**: the landed D4 qualifier names kake and kasegi only.


- `SCORECARD.md:34` at `956ee167` spliced the D4 qualifier **into the middle of the published `awk … | grep -cE …` command span**, splitting it into two spans; the second is not runnable (`bash -c` on it → syntax error). `a78fec1` moved the qualifier to the end of the evidence cell and the awk span is intact again. Caught and fixed inside the wave.
- `corpus/knowledge/sibling-overlap-census-round49.md` now carries both "Basis both." (line 289) and "**kake and kasegi basis is `kotoba`, not `both`**" (line 326). The later line wins and `SCORECARD.md:34` and `corpus/lessons/round-50.md:128` both follow it, but the entry is append-only, so both statements stand in the file.

## Qualifier text

### D2 — SCORECARD operability row (landed, `SCORECARD.md:31`, end of evidence cell)

    **Round-50 qualifier (routed defect D2):** "executed" above means the instrument runs the two
    boxes; the round-49 proof covered six named conjuncts, one fixture each, and did not enforce its
    own coverage.

### D4 — SCORECARD adjacency row (landed, `SCORECARD.md:34`, end of evidence cell)

    **Round-50 qualifier (routed defect D4):** "from their own bytes" overstated the round-49 basis:
    kake and kasegi were classed `adjacent` from kotoba's own description (the aggregator-owned
    lessons in their corpora relay kotoba's round-5 finding and are not a sibling-stated split, census
    entry round-50 corrections); the round-49 "0 contested" had no precedence rule behind it until
    round 50 (census entry, precedence section).

Both were appended at the **end of the evidence cell**, never inside a command span.

### Text still missing — exact wording to append, by surface

`corpus/knowledge/sibling-overlap-census-round49.md` (append-only; append as a new section or as
sentences in the round-50 section, do not rewrite lines 9-10 or 99):

    **Correction to this entry's opening sentence (routed defect D4).** The sentence above that this
    entry classifies the 20 lanes "from each sibling's own committed bytes" overstated the round-49
    basis. The classification rule reads "either side's committed scope surfaces", so kake and kasegi
    were classed `adjacent` from kotoba's own description, and seven of the nine `adjacent` rows carry
    `names kotoba` = `no` in this entry's own table. The count "0 contested" in § Counts below is the
    round-49 count; the `contested` arm had no precedence rule against a stated split until round 50
    (§ Round 50: precedence between `contested` and a stated split).

`corpus/README.md:69` (rewritable index row):

    all 20 sibling lanes classified against kotoba's province at pinned sibling commits (9 adjacent,
    11 none, 0 contested — 7/13 at the first landing, corrected by the falsify wave; 0 contested under
    the round-49 rule, which had no precedence between `contested` and a stated split; kake and kasegi
    are adjacent from kotoba's own description, not their own bytes)

`corpus/README.md:78` and `:91-96` (rewritable Known-gaps prose): add that the proof now covers the six
named conjuncts with one must-fail case each and that the checklist gate runs `--box-proof`; the
unsubstituted variable, the `≤` equality boundary, the legacy-state arm and a non-digit round folder
still have no fixture.

`LOG.md:2371` (append-only): append to the round-49 landing record that the "0 contested" there had no
precedence rule behind it until round 50, and that kake and kasegi were classed from kotoba's own
description.

`SCORECARD.md:261` (rewritable capability row): replace "and no gate runs `--box-proof`" with the
measured fact that `verifiers/verify_skill_checklist.py` check `checklist.box_map_complete` now runs
each delegated instrument's `--box-proof` and fails on a non-zero exit.

## Findings

1. **The correction reached two of five overstatement-bearing surfaces.** The census entry repeats
   "from each sibling's own committed bytes" in its own opening sentence, so a reader who opens the
   entry — not the SCORECARD — still reads the overstated basis as the entry's own claim. The
   round-49 closure's D4 named the SCORECARD row only; the census entry is the surface that carries
   the claim at length.
2. **"0 contested" needs a rule, not a number.** The appended round-50 precedence section makes the
   count defensible going forward ("No row moves; the counts stay 9 adjacent, 11 none, 0 contested")
   but never says the round-49 zero was unruled. Three candidate `contested` elements were recorded
   and left unruled at round 49 (`corpus/knowledge/sibling-overlap-census-round49.md` falsify-wave
   corrections: kengaku's census script, tameshi naming kagi's checklist runner, kama's consumer
   registry).
3. **The "all 20 … from their own bytes" clause is false on the census's own table.** Seven of the
   nine `adjacent` rows carry `names kotoba` = `no`, and the rule's own text admits kotoba-side
   surfaces. The kake/kasegi correction narrows it further: the aggregator-mirrored lessons in their
   corpora relay kotoba's own round-5 finding and are not a sibling-stated split, so the basis is
   `kotoba`, not `both`.
4. **The three surfaces that list the "no fixture" clauses list different ones.** `LOG.md:2382` names
   four (unsubstituted variable before the report path, non-digit round folder, `≤` equality
   boundary, legacy-state arm); `SKILL.md` named three before `a78fec1` and now names four; the
   SCORECARD capability row still names two (unsubstituted variable, non-digit round folder) and
   omits the `≤` boundary and the legacy-state arm. Any wording fix that quotes the clause list
   should take the four-clause list from `LOG.md:2382` and the landed `SKILL.md`.
5. **One stale row the landing created rather than fixed.** `SCORECARD.md:261` asserts no gate runs
   `--box-proof`; the round-50 gate does run it.
6. **The D4 qualifier is still incomplete on tameshi.** The census's own round-49 falsify note
   (`corpus/knowledge/sibling-overlap-census-round49.md:147-149`) records tameshi's basis as kotoba's
   base `PROVINCE.md` line "tameshi — verification-fixture craft and mutation testing", which names
   only tameshi's ground, with tameshi's own wave report as corroboration only — so at round 49
   tameshi, like kake and kasegi, did not rest on the sibling's own bytes. The landed qualifier names
   kake and kasegi only. The falsify seat `ReviewKakeKasegiBasis.md` F2(d) says the same. The
   qualifier should name tameshi's basis too, and the "5 of 20"-style figures it quotes should be
   read against the round-49 basis column, not the round-50 one.
7. **`corpus/lessons/round-50.md:128-130` (the D4 bullet) repeats the same incomplete pair.** It says
   the row "now says that kake and kasegi are `adjacent` because of kotoba's own description, not
   their own bytes" — same omission of tameshi, and it does not name the "0 contested" precedence
   point that the SCORECARD qualifier does. The lesson is append-only; a corrected D4 bullet must be
   appended, not edited.

## Evidence (commands, exit codes)

    git -C kotoba-shokunin rev-parse HEAD                      → f30464660c675d1c1e2851a3bf0366a3aaffe5a8 (base)
    git -C kotoba-shokunin log --oneline -3                    → a78fec1, 956ee16, 542f515 (landed)
    grep -rn 'every conjunct' SCORECARD.md SKILL.md PROVINCE.md README.md AGENTS.md \
      corpus/README.md corpus/QUALITY.md corpus/SOURCES.md corpus/knowledge/*.md \
      corpus/lessons/round-49.md verifiers/*.py LOG.md          → exit 0; 2 hits at base
                                                               (verifiers/verify_dispatch_prompts.py:488, :739)
    grep -rn 'own bytes|own committed bytes|0 contested|all 20 sibling|boxes executed' <same set> → exit 0; 13 hits at base
    grep -n 'every conjunct' verifiers/verify_dispatch_prompts.py (worktree, a78fec1) → exit 0; 1 hit, line 996,
                                                               scoped wording ("every conjunct named for the box in CONJUNCTS")
    git show f304646:SCORECARD.md | grep -n 'own bytes|boxes executed|0 contested' → exit 0; lines 31, 34, 116, 150
    git show f304646:corpus/knowledge/sibling-overlap-census-round49.md | grep -n 'own committed bytes|0 contested' → exit 0; lines 10, 99
    git show f304646:corpus/README.md | grep -c 'all 20 sibling lanes classified' → exit 0; 1 (line 69)
    git diff f3046466 a78fec1 -- corpus/README.md | grep -E '^[-+]\| Fleet'  → exit 1 (no change to the census index row)
    python3 -c "…manifest…" (verifiers/fixtures/dispatch-prompts/manifest.json) → 9 cases: 6 must-fail, 2 control, 1 N/A;
                                                               6 distinct expect_conjunct names
    git show f304646:verifiers/verify_dispatch_prompts.py | grep -n 'every conjunct' → exit 0; 488, 739
    python3 -B verifiers/verify_skill_checklist.py --json      → exit 0, 11/11 PASS; detail
                                                               "delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2"
    awk -F' \\| ' '…census table… && $5=="adjacent"' corpus/knowledge/sibling-overlap-census-round49.md
                                                               → 9 rows; 7 of them with $6=="no" (chousa, kagi, kake, kama, kasegi, kumitate, tameshi)
    git -C kengaku-shokunin show 1f3b0f1e…:plans/round25_census.sh | sed -n '37,40p'
                                                               → "cwd is not a lane root (needs SKILL.md and corpus/)" exit 2
    git -C chousa-shokunin grep -li kotoba 6c5eb146… -- PROVINCE.md corpus SKILL.md MINT.md → exit 0; only MINT.md and
                                                               corpus/evidence/* logs — no scope-surface split (basis kotoba)
    git -C kake-shokunin show e73d48bb…:corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md → exit 0;
                                                               "Aggregator-owned file; the owning lane corrects `SKILL.md`."

No lane, fleet or sibling writes. No tools installed or upgraded (read `~/.omp/agent/RULES.md`).
No web sources opened.

## Out of scope (not mine, named for the integrator)

- `corpus/lessons/round-49-verifier-spotcheck.md` is the closure's record; it quotes the five phrases
  on purpose and must not be edited.
- The round-49 base's `plans/round-49.md` and `corpus/lessons/round-49.md` keep their round-49 wording
  as history; the correction belongs to the round-50 surfaces.
