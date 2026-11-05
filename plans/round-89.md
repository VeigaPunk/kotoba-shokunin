# kotoba round 89 — plan and freeze (draft; freeze pending control execution)

Host: Linux `7.2.11-arch1-1`, omp 18.15.0. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
branch `master`.
**Base (lane tip at plan draft):** `a5b3b15c00b1de5db321e4226a0a7db17340e605` (the round-88 verifier
spot-check commit; `jj-lane.sh state` → `ahead=0 behind=0`, tree clean at draft time).
**Freeze protocol (routed defect 3, round-88 spotcheck):** this file freezes the predicate sentences,
targets, controls and kill rules at DRAFT. The freeze commit (after wave `r89-w1` settles) appends the
EXECUTED control receipts and the freeze header, and changes no predicate/target/kill-rule sentence
(the freeze-receipt command `git diff <draft> <freeze> -- plans/round-89.md` shows receipt/header lines
only). No counter byte may change after the first candidate score (kill rules below). A freeze whose
declared control expectation cannot be observed is REFUSED, not landed — that refusal is claim C1's
subject.

## Fresh-start reading (run-15 authorization "Authorize all", 2026-11-05)

Read before declaring (last three closures + spot-checks):
`corpus/lessons/round-88-verifier-spotcheck.md` (C1 killed under the frozen kill rule — post-score
counter repair; C2 not verified — frozen discrimination control unsatisfiable; routed defects 1–6),
`corpus/lessons/round-87-verifier-spotcheck.md` (rejected-honest-stop: forged ledgers reached C1;
exact-set D5 unreachable by honest work), `corpus/lessons/round-85-verifier-spotcheck.md` (C1
unprovable: vacuous worlds satisfied the frozen predicate). Each shapes this round: no counter repair
after any score (both kill rules); every control is EXECUTED before the freeze commit; the C2
successor is instance-level and discriminating against the r88 blindness (v2 reads exit 0 on the
added-instance world — receipt below).

## Measured before-state (round start, receipts committed with the draft)

| Measurement | Command | Observed | Receipt |
|---|---|---|---|
| SOURCES census, base | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | exit 0, 183 rows, 33 W04 duplicate-url warnings (pre-existing, unchanged) | `.ufo/waves/round-89/receipts/census-before.txt` |
| SOURCES rows | `grep -cE '^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 183 (last S257) | same receipt |
| C1 absence sweep | `git grep -n 'freeze_gate\|freeze-gate' -- verifiers plans` @ `a5b3b15c` | 0 hits — no freeze-refusal instrument exists | `.ufo/waves/round-89/receipts/before-c1-absence.txt` |
| Assimilation collisions | the §10 id-collision recipe into `.ufo/waves/round-89/assimilation/` | reg 183, staged 188, collisions 55 (unchanged from round 88; open L0 `kotoba | round-88` line 322) | `assimilation/{reg-ids,staged-ids,collisions}` |
| C2 v2 blindness | `python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test` | `1 failure(s) over 16 assertions` — arm `w_added_red` (frozen control) "reads it as PASS"; exit 1 | `.ufo/waves/round-89/receipts/before-v2-selftest.txt` |

The round-88 v2 gate (`check_r86_routed_repairs_v2.py`) and the r88 C1 counter
(`check_omp_root_semantics_v2.py`) are FROZEN and stay byte-identical this round.

---

## C1 — depth (score 9, owned lowest): the freeze gate refuses an unsatisfiable freeze

**Surface changed.** A new lane instrument class: a gate that executes a plan's declared pre-freeze
controls and refuses the freeze when a declared expectation cannot be observed. Round 88 shipped a
freeze containing the control `w_added_red` that had never been executed and whose declared FAIL its
own predicate could not produce (F1; spotcheck routed defect 3). The r88 instruments stay untouched.

**Instrument.** `verifiers/check_freeze_gate.py` (new). It parses a plan/fixture `## Controls` block
whose entries each declare `- control <name>: <command>` plus an `expect:` line (`exit <rc>` and/or
`stdout contains <literal>`), executes every declared control with `cwd` = the lane root, `TMPDIR`
honoured and a per-control timeout, and compares declared vs observed. Verdict ladder:
`0` = every control held (freeze may proceed); `1` = refused, naming the first violated control with
declared-vs-observed; `2` = could-not-evaluate (a declared command missing/not executable/timeout);
`3` = invalid spec (a control with no command or no expectation, or an empty block).

**Frozen predicate** (the same sentence here, in the gate's docstring, and in every receipt):

    python3 -B verifiers/check_freeze_gate.py --self-test
        -> prints "0 failure(s) over N assertions" (N >= floors floor), exit 0
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md
        -> exit 1, refusal names "w_added_red"
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md
        -> exit 0

The two fixtures reconstruct the round-88 C2 control declarations: `r88-controls.md` declares what the
r88 freeze expected (`w_added_red` to FAIL D5), each control's command being a committed simulator
(`verifiers/fixtures/freeze-gate/sim-*.sh`) that prints the OBSERVED verdict grounded in the
committed r88 receipts (fail-closed: a simulator whose receipt is absent exits nonzero);
`r88-controls-fixed.md` declares the observed verdicts, so the same gate holds. This reproduces F1
mechanically: the r88 declaration and the observable reality disagree, and the gate refuses.

**Target:** all three arms above, exit codes as stated, at the landing revision.

**Do-nothing control:** the before-state receipt (absence sweep, 0 hits) — with no instrument, an
unsatisfiable control ships unexecuted; the empirical no-work outcome is round-88 F1 itself
(`corpus/lessons/round-88.md` § Mistakes row 2; spotcheck routed defect 3).

**Shortcut controls (Q37), each a self-test arm that must fail:** (a) a stub plan whose controls all
declare exit 0 against the refusing fixture's simulator — killed by the `r88-controls.md` arm; (b) a
plan omitting one declared control — killed by an omission arm (spec-invalid, exit 3); (c) an
expectation-sign flip — killed by a flip arm (exit 1); (d) a malformed declaration (no command) —
killed (exit 3).

**Mutation battery (declared; scored this round, Q47 two-sided):** expectation-flip mutant,
control-skip mutant, parse-shortcut mutant — each killed (gate exits nonzero on the armed fixture);
semantics-preserving equivalent (reordered controls, reformatted expect line) survives (exit codes
unchanged). Battery receipt committed before the claim's headline is asserted in LOG/SCORECARD.

**Kill rule (C1):** the gate, its fixtures, its floors row or either fixture plan changed **after the
first candidate score** kills C1. A pre-score amendment is an addendum that ships its own re-run
controls and may not widen the target or change the predicate sentence.

**Sourced (§2b).** The knowledge entry `corpus/knowledge/freeze-gate-round89.md` opens with the
provenance trio citing rows opened THIS round: S258 (external, the preregistration-methods source the
scout opens with access date, sha256 and a located ≤25-word quote — the freeze-before-data principle
this gate mechanizes) and S259 (own-work: the round-88 verifier spot-check at `a5b3b15c`, routed
defects 3–4 — the requirement record).

---

## C2 — consistency (calibration sub-axis, score 10): the routed D5 gate reads instances

**Surface changed.** The lane's routed-repairs gate D5. The r88 v2 gate tests name-set identity and
name monotonicity only, so an added integrity finding under an already-red name is invisible (its own
frozen control `w_added_red` cannot fail; CriticFalsify C2-S2/S3 pass worlds the frozen text names as
failures). The v2 gate stays byte-frozen as the do-nothing control. The successor is
`verifiers/check_r86_routed_repairs_v3.py` (new): D1–D4 carried from v2 unchanged in meaning; D5
replaced by the instance-level test.

**Frozen predicate** (the same sentence here, in the gate's docstring, and in every receipt):

    python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt <receipt.json> [--root <dir>]
        -> prints "r86 routed defects closed N of 5" and "instance drift K",
           exit 0 iff N == 5 AND K == 0 AND the pinned snapshot digests match;
           exit 1 otherwise, naming the first failing leg (d5i | d5ii | d5iii | snapshot_tampered | d1..d4);
           exit 2 = could-not-evaluate.

- **Base receipt.** At the freeze the gate writes `--write-base-receipt` output
  (`.ufo/waves/round-89/receipts/d5v3-base-receipt.json`), pinning: the revision it was written at,
  sha256 of `verifiers/verify_corpus_integrity.py` and of `verifiers/corpus-baseline.json` (snapshot
  digest pins, PROTOCOL §Gate standard "two evidences"), and the full integrity observation dict
  (all nine checks, live values, measured in the lane working tree).
- **D5(i) identity:** the check-name list at the measured root equals the receipt's (a silenced or
  removed check fails); `verify_corpus_integrity.py --self-test` exits 0 at the measured root.
- **D5(ii) name monotone:** the DRIFT name set at the measured root is a subset of the receipt's
  (an added red-name fails; a healed red passes).
- **D5(iii) instance non-growth:** for every check name, the observed value at the measured root is
  ≤ the receipt's value — the `(name, observed)` tuple of each red name is non-growing after the
  freeze. This is the leg v2 cannot express (the r88 blindness), and it is satisfiable because the
  receipt is written at the freeze revision, AFTER the round's corpus landings (which carry their own
  README index rows in the same commit): the honest landing between freeze receipt and final tip adds
  no corpus bytes, so every tuple holds; any post-freeze corpus addition under an already-red name
  fails.
- **Location discipline (Q79).** The receipt is written in the lane; a world measured elsewhere must
  first pass the same committed bytes in lane and in the world checkout with identical observation
  dicts (the equivalence receipt is a pre-freeze control); a name whose verdict the checkout location
  flips is could-not-evaluate for that world, never a silent verdict. Bare fleet-root report paths
  are the known location-dependent shape (r88 ExecMonotoneD5 F2); the pre-freeze equivalence run
  pins it.

**Controls — each EXECUTED and receipted BEFORE the freeze commit** (worlds built by a seat that did
not author the gate, under `/fast/scratch/hyaku/kotoba-r89/ExecCtlWorlds/`, receipts copied to
`.ufo/waves/round-89/receipts/`; fixture definitions committed under `verifiers/fixtures/d5v3/`):

- `w_added_instance` — the freeze revision plus one new corpus lesson line citing an unresolvable
  commit (an added finding under already-red `pointers.commit_unresolvable` and `commit_total`) →
  v3 exit 1 naming `d5iii`. **Do-nothing/discrimination control:** the frozen v2 gate's monotone
  reading on the same world class is exit 0 (blind) — receipted from the v2 self-test arm and a
  direct world run.
- `w_silenced` — the freeze revision with one integrity check silenced (script edited in the world) →
  v3 exit 1 naming `d5i` (and/or `snapshot_tampered`).
- `w_rerecorded` — the freeze revision with `corpus-baseline.json` expectations re-recorded to match
  drifted counts → v3 exit 1 naming `snapshot_tampered` (a re-recorded baseline cannot green D5).
- `w_healed` — the freeze revision with one red instance healed (the `commit_unresolvable` citation
  resolved) → v3 exit 0 (a healed red PASSES; blanket refusal is not a gain).
- `w_tip` — the honest landing tip → exit 0.
- `w_equivalence` — a pristine checkout of the freeze revision measured in lane and in the world
  checkout → identical observation dicts (the Q79 location receipt).

**Target:** `N == 5` and `K == 0`, exit 0 at the landing tip measured against the freeze receipt; and
the five control polarities as stated, receipts committed before the freeze.

**Honest bound, stated before data:** the round inherits the base reds
(`index.tracked_files`, `index.unindexed`, `pointers.report_total`, `pointers.commit_total`,
`pointers.commit_unresolvable` — re-measured at the base with the freeze receipts). The round repairs
only instance growth attributable to its own landed files, by adding README index rows in the landing
commit; `corpus-baseline.json` and `verify_corpus_integrity.py` are NOT edited, and
`pointers.commit_unresolvable` (the `corpus/lessons/round-81.md:8` dead clone commit, L0
`kotoba | round-87`) stays red at 1 by design — a healed red would pass, but the lane does not
claim it.

**Kill rule (C2):** the v3 gate, its fixture definitions, the base receipt or the snapshot digest pins
changed after the first candidate score kills C2. The v2 gate and the integrity instrument are not
edited by this round.

**Sourced (§2b).** The knowledge entry `corpus/knowledge/instance-d5-round89.md` opens with the
provenance trio citing S259 (the round-88 spot-check's routed defect 4, opened this round).

---

## Record corrections (mined mistakes, not claims)

1. **Filed-report rewrite (r88 spotcheck routed defect 1).** The round-88 report's filed bytes were
   rewritten in place (`5306df4` filed a 199-line version; `d6c5ec57` replaced it with the 104-line
   honest-stop version) — corrections must land as appended errata naming the superseded text, never
   a rewrite. Class `landing`; captured-by `none`; fix: criterion Q81 in `corpus/QUALITY.md` (this
   round), and this round never rewrites a filed report byte.
2. **Count without its artifact (r88 spotcheck routed defect 5).** The r88 lesson's assimilation
   parenthetical said "MERGE-REPORT.md, 188 rows" — 188 is `SOURCES.append.md`'s row count
   (MERGE-REPORT.md is 155 lines / 113 table lines). Class `attribution`; captured-by Q76 (the
   criterion existed and was not consulted); fix: the round-89 lesson records the corrected counts
   with both counting commands (Q76 form) and never repeats the misattribution; no criterion rewrite
   (Q76 already owns the rule).

## Frontier step (§2b, CORPUS.md contract v1)

- `corpus/SOURCES.md`: two new rows S258 (external preregistration-methods source) and S259 (own-work:
  `corpus/lessons/round-88-verifier-spotcheck.md @ a5b3b15c`, routed defects 3–4), opened this round;
  the lesson's `## Gate` records URL/access date/sha256/≤25-word located quote per new row. Status
  changes to existing rows: none expected; any change is logged old→new in the lesson.
- Mistakes mined: the two record corrections above (both with evidence pointers and captured-by).
- Sourced claim: C1's knowledge entry cites S258 (+S259); C2's cites S259.
- Assimilation: none — 55 id collisions re-derived this round
  (`assimilation/collisions`), the renumber-or-retire ruling is open (L0 `kotoba | round-88`).
  Considerthese: the three still-unimplemented proposals in `considerthese/2026-10-26.md` are
  reviewed; none is taken this round (proposal 2 is L0-blocked, line 174; 3 and 5 do not fit the
  claim cap beside the two routed successors) — routed to a later round.

## Round shape and freeze protocol

One v1 wave `r89-w1` (band 8–16, policy `scripts/hyaku/ufo-wave-policy.json`), 12 seats:
3 executor (ExecFreezeGate, ExecD5Gate, ExecCtlWorlds), 3 scribe (ScribeEntry, ScribeSources,
ScribeLesson), 1 scout (ScoutSource), 2 reviewer (ReviewerFreezeGate, ReviewerD5Gate), 1 critic
(CriticFalsify), 1 mutation-tester (MutTesterGates), 1 connector. Attack share 4/12 ≥ 25%; the
canonical §3 planner seat is held by the L1 (the validator excludes `planner`).

Order of record: (1) this draft is committed BEFORE the wave dispatch (predicates/targets/kill rules
frozen); (2) the wave builds instruments and executes every declared control; (3) after WAVE-DONE the
L1 verifies each control receipt, then the FREEZE commit lands: this file's freeze header + receipts,
the two instruments, their fixture trees, floors rows, SKILL.md registry rows (+2), the corpus
landings (SOURCES rows, knowledge entries, lesson, Q81, README index rows INCLUDING the round-88
spot-check file), the wave evidence, and LOG.md's freeze entry; (4) the candidate scores are measured
at the freeze revision and the landing commit adds only measurement receipts, the LOG settlement and
SCORECARD annotations — `git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus`
prints nothing (the landing-receipt command proves no post-score byte change). Corpus files never
cite `.ufo/reports/round-89/kotoba.md` (the report does not exist at freeze time; a dead pointer
would add a red `pointers.report_dead` name).
