Result: MIXED — Q29 is grounded in M36 and supersedes nothing (both hold), but "the sweep must exit 0 before the round's report" is a wish as landed (nothing runs, floors or records the sweep), the round's own corrections already fail Q29's letter (two M36-named stale phrases have no registry row), and "a manual grep is not the sweep" misstates what a single-file, literal-phrase registry can find.

Seat: KotobaR52a2.CriticQ29 (critic, falsify wave attempt 2). Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882`.
Target: `corpus/QUALITY.md:40` (Q29). Run window 2026-10-22T17:49Z–17:55Z.
Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/CriticQ29` (clone checked out at `c8407a45`); probe script
`/fast/scratch/hyaku/kotoba-r52a2/CriticQ29/probe_q29.py`. Instrument probed: `verifiers/check_correction_sweep.py`,
sha256 `02132ba184cf86062c1a0e4c2b403c9d2ac33ce9980b98c2fe564cd106b12a20`. No lane file edited, no installs.

## Reproduction (baseline for every attack below)

Run in the lane, read-only:

```
python3 -B verifiers/check_correction_sweep.py --rev c8579a4c5b48789e56fb9060ddd48f33569e1215   → exit 1
  FAIL r51-c2-readme corpus/README.md:119 … | FAIL r51-c2-scorecard-lead SCORECARD.md:28 … leading
  | FAIL r51-c2-province PROVINCE.md:17 … | correction sweep: 3 stale block(s)
--rev 4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb   → exit 1, same 3 FAIL lines
--rev c8407a453788df964df5a7b835dd0ce1360de882   → exit 0, correction sweep: 0 stale block(s)
--root .  (lane working tree, includes the uncommitted SCORECARD.md diff) → exit 0, 0 stale block(s)
--self-test → exit 0, 0 failure(s) over 5 assertions
```

## Attack 1: Is Q29 grounded in M36? HOLDS, with one LOW defect

- M36 exists: `corpus/lessons/round-52.md:10`, class `reference-drift`. Its fix cell names
  `verifiers/check_correction_sweep.py` and "New criterion Q29". Its red-before (`--rev c8579a4c` → exit 1, three FAILs)
  reproduces exactly (above). This satisfies the QUALITY header rule "No criterion exists without a lesson behind it"
  (`corpus/QUALITY.md:5`).
- M36's captured-by cell names PROTOCOL § Evidence standard, "Corrections sweep every mention"
  (`/home/vgpnk/Projects/shokunin/PROTOCOL.md:363-365`), and says the rule existed but was a manual grep. So Q29 turns
  an existing protocol rule into a tool. It is not a new judgment rule. That framing is consistent.
- **D5 (LOW, number-drift).** The grounded-in cell of Q29 says "missed **two** places". M36's evidence lists **three**
  places that round 51's sweep missed: `corpus/README.md:133-141`, `SCORECARD.md:28` and `PROVINCE.md:17`. The closure
  routed only two of them, but the round-51 sweep missed all three. The same "two places" wording sits in the README
  index row (`corpus/README.md:79`). Correction: "missed three places (two routed by the closure, one found in round 52)".

## Attack 2: Does Q29 duplicate or conflict with Q19, Q26, Q27, Q28?

- **Q19 (re-measure carried before-values): HOLDS, no overlap.** Q19 governs before-values at round start. Q29 governs
  how a later correction spreads to other files. They cover different objects at different times.
- **Q26 (a headline asserts nothing its counter does not measure): HOLDS, complementary.** Q26 checks a statement when
  it is written. Q29 checks that a statement already corrected is not left standing elsewhere. The SCORECARD lead
  falls under both, at different times. Neither row restates the other.
- **Q27 (seat-record and leftover sweep bound to seat writes): HOLDS.** The only overlap is the word "sweep": Q27
  sweeps seat output directories, Q29 sweeps stale claims. There is no conflict. The wording is slightly ambiguous
  because Q29 says "the sweep" and "a manual grep is not the sweep". Naming it "the correction sweep" removes that.
- **Q28 (judgment tables frozen at the plan commit): BREAKS as a tension (MEDIUM, duplicate authority).** Q28 freezes
  "a counter's judgment tables (allowed terms, vocabularies, pinned labels)" at the plan commit. M35, the mistake
  behind Q28, was a judgment table widened "in the same commit as the rows it scored". Q29 *requires* exactly that
  shape: the registry (the `stale` and `declared` patterns, which form a judgment table) goes in "in the same commit as
  the correction" it scores. Evidence:
  - The registry was authored in `c8407a45`, after the plan commit `4c003a4b`.
  - `git show --stat c8407a45` lists `verifiers/check_correction_sweep.py` (+144) alongside the repaired
    `SCORECARD.md`, `PROVINCE.md` and `corpus/README.md` in one commit.

  Today the rows do not collide in letter, because the sweep is a mistake-fix guard and Q28 applies to "claim
  counters". Q29 never says so, though. The first round that declares a calibration claim counted by this sweep (for
  example "stale blocks 3 → 0") puts the two rows in direct conflict. Smallest safe correction, in a superseding row:
  "The registry is a regression guard, not a claim counter; a claim counted by it freezes the registry at the plan
  commit (Q28)."

## Attack 3: Is "the sweep must exit 0 before the round's report" enforceable? BREAKS — a wish (MEDIUM-HIGH)

- **Nothing runs it.** I searched the whole fleet with ignore rules off:
  `rg --no-ignore --hidden -l check_correction_sweep -g '!**/.git/**' -g '!**/interactive-sessions/**' -g '!kotoba-shokunin/.ufo/waves/**' .`
  The hits are only `corpus/lessons/round-52.md`, `corpus/README.md`, `corpus/QUALITY.md`,
  `verifiers/check_correction_sweep.py`, `SCORECARD.md` and three jj operation-store records (commit messages). No gate
  script, no protocol step and no report template invokes it. Limit: that `rg` exited 2 after 897 s, meaning some paths
  could not be read; I had suppressed stderr, so I cannot name them. The absence therefore holds for every readable file
  in the fleet. Inside the lane, every file that runs other verifiers (`check_assertion_floors.py`,
  `check_substrate_pins.py`, `check_overlap_levers.py`, `floors-registry.json`, `baseline.json`) is readable and none
  names the correction sweep.
- **No floor covers it.** `verifiers/floors-registry.json` has `instrument_total: 12` and no entry for the correction
  sweep. In the sandbox, `python3 -B verifiers/check_assertion_floors.py` → exit 0, all PASS, and the sweep is not
  among the instruments listed.
- **Deleting a registry row is silent (probe P9).** I removed the row `r51-c2-province` from a sandbox copy:
  - `--self-test` → exit 0, "0 failure(s) over 5 assertions". The self-test never exercises the PROVINCE row
    (`check_correction_sweep.py:94`, where `province` defaults to "- nothing stale").
  - `--rev c8579a4c` → exit 1 with 2 FAILs instead of 3.

  Neither an anchor nor a floor notices the lost row. The rule "rows are not edited" exists only in the script's
  docstring (`check_correction_sweep.py:18`). Compare `floors-registry.json`'s `$comment`: tables inside the edited
  file "agree with each other by construction", so they need an anchor outside it. The build-wave design for this fix
  asked for exactly that, "a small committed registry `verifiers/superseded-claims.json`" naming "the files to sweep"
  (`.ufo/waves/round-52/build-taskcall-sent.json:169`). The landed version is in-file and has one `file` per row.
  (Probe P8: if the `declared` patterns are weakened to an empty regex, the self-test does go red, 3 failures over 5.
  So only weakening is guarded, and only when someone runs the self-test.)
- **"The round's report" has no receipt and no defined trigger.** No `LOG.md` entry for round 52 exists yet
  (`rg -n -i "round[- ]52" LOG.md` → no hits). The fleet has no `.ufo/reports/round-52/kotoba.md` (that directory holds
  only `kotodama.md`). The uncommitted SCORECARD diff (line 128 of the working tree) already says the defects were
  "caught by the new `verifiers/check_correction_sweep.py` (M36, Q29)" without any recorded command or exit code for the
  report-time run.
- **The timing drifts from the parent rule.** PROTOCOL.md:363 says "Before a round's commit". Q29 says "before the
  round's report". That makes two timing rules for one obligation. A lane report lands last (`PROTOCOL.md:117`), so
  Q29's timing lets stale commits land as long as they are fixed before the report.
- Smallest safe correction: a superseding row (or the L1's fix) that names the trigger and the receipt. The sweep runs
  in the step that already reruns instruments: add it to `floors-registry.json` and `check_assertion_floors.py` with a
  self-test that covers every registry row, so a lost row lowers the tally. The round's LOG entry or report then
  carries the pasted `check_correction_sweep.py --rev <head>` line with its exit code. Keep PROTOCOL's "before the
  round's commit" timing rather than introducing a second one.

## Attack 4: Does the round's own correction satisfy Q29? BREAKS (MEDIUM; one false-provenance clause)

Q29 says "the superseded claim's stale phrase and its declared result go into … the registry in the same commit as the
correction". M36 names more stale phrases than were registered. Probes run on copies of the `c8407a45` tree
(`python3 -B probe_q29.py`, exit 0, 17:52:20Z):

```
P0 control: no mutation                                         → exit 0, 0 stale block(s)
P1 control: drop registered PROVINCE:18 correction               → exit 1, FAIL r51-c2-province PROVINCE.md:17
P2 "six rows are new" re-added to SCORECARD:28 (named in M36)    → exit 0, 0 stale block(s)
P3 README:75 index row reverted to its c8579a4c bytes            → exit 0, 0 stale block(s)
```

- P2: M36 and routed defect 2 name "six rows are new" as stale, and `corpus/lessons/round-52.md:73` says it was
  "corrected to four". No registry row exists for it, so putting the phrase back stays green.
- P3: routed defect 1 says the README index row (`:75`) "omits `removed in a scope`". The correction at `:75` has no
  registry row, so reverting it stays green. Yet `corpus/lessons/round-52.md:70-71` reads "the index row (`:75`)
  carries a correction naming `removed in a scope`. Fixed; caught by `check_correction_sweep.py` (M36)." At
  `c8579a4c` the sweep flags `corpus/README.md:119` (the Core note), never `:75`.

  **False provenance:** the sweep did not catch the `:75` defect and cannot catch it.

Smallest correction: add registry rows for "six rows are new" (SCORECARD) and for the pre-falsify lever phrase
`removed everywhere, or automatic choice off` without `removed in a scope` (README `:75`). Narrow the "caught by"
clause to the Core note.

## Attack 5: "A manual grep is not the sweep" — BREAKS on coverage (MEDIUM)

The registry is a regression lock on literal phrases, each tied to one file. It cannot discover anything. Q29's
applies-to names "SKILL.md, … knowledge entries", which have no registry rows. Probes on copies of `c8407a45`:

```
P4 `overlap levers backed 7 of 7 clients` appended to SKILL.md                 → exit 0, 0 stale block(s)
P5 same phrase appended to corpus/knowledge/skill-overlap-levers-round51.md    → exit 0, 0 stale block(s)
P6 paraphrase "overlap levers backed 7/7 clients" appended to corpus/README.md → exit 0, 0 stale block(s)
P7 stale phrase plus an unrelated "passed 4 of 7 checks" in the same bullet    → exit 0 (false green: bare `4 of 7`)
```

The third place in M36 (`PROVINCE.md:17`) was found by "this round's sweep", meaning the L1's grep. The registry did
not exist until the same commit. Read literally, "a manual grep is not the sweep" lets a future L1 run only the
registry and skip discovery. That is the failure M36 records, made worse. Discovery still needs PROTOCOL.md:363's grep
over every touched file.

Smallest correction: "The grep finds every place; each place found gets a registry row, one row per file; the
registry keeps them found." The `declared` pattern should be specific to the claim (for example
`4 of 7 clients` or the counter id `7c81a787`), not a bare `4 of 7`. P7 overlaps the mistake-fix seat's target; it is
recorded here only because Q29 hands its verdict to this instrument.

## Attack 6: Should Q29 supersede an earlier row? HOLDS — `—` is right

`rg -n -i "sweep|correction" corpus/QUALITY.md` hits only Q14 (a negative claim carries its search), Q23 (attribution
sweep across authorities), Q27, Q28 and Q29. None governs spreading a correction across files, so there is no row to
supersede. The parent authority is PROTOCOL.md:363, which is not a QUALITY row. Q29 should **cite** it, for example in
the criterion text "mechanizes PROTOCOL § Evidence standard, Corrections sweep every mention". Today the link exists
only through M36's captured-by cell. Without it, the second timing rule in Attack 3 stays unexplained.

## Adjacent observation (outside Q29's target, [INFERENCE] on intent)

`corpus/lessons/round-51.md:3-7` (head paragraph) still gives the round-51 C2 as "(0 of 7 → 7 of 7)" with no
declared-counter qualifier in that block. It may be read as the claim's *target* rather than its result. Lessons are
not in PROTOCOL.md:363's file list. I am recording it, not scoring it.

The uncommitted SCORECARD diff says "the falsify wave ran on live roles only" for attempt 1. The attempt-2 context says
that wave was cut off and left no seat report. Another seat should check this; it is not scored here.

## Verdict

| attack | result | severity |
|---|---|---|
| grounded in M36 | HOLDS (count drift "two" vs three) | LOW |
| duplicate/conflict Q19, Q26, Q27 | HOLDS | — |
| conflict with Q28 (same-commit judgment table; claim/guard boundary unstated) | BREAKS (tension) | MEDIUM |
| "must exit 0 before the round's report" enforceable | BREAKS — a wish: no runner, no floor, no receipt, row deletion silent, timing drifts from PROTOCOL | MEDIUM-HIGH |
| round's own correction meets Q29 | BREAKS — two M36 phrases unregistered; README `:75` "caught by" is false provenance | MEDIUM |
| "a manual grep is not the sweep" | BREAKS — the registry cannot discover; SKILL.md, knowledge and paraphrase all green | MEDIUM |
| supersedes `—` | HOLDS | — |

Impacted axis: calibration (the criterion promises a gate it does not have) and consistency (a second timing rule
beside PROTOCOL.md:363). These defects are fixable. None is a tradeoff the judge must reject. Append-only correction:
a superseding row Q30 (supersedes Q29) that:

1. cites PROTOCOL.md:363 and keeps its "before the round's commit" timing;
2. says the grep finds and the registry keeps, with one row per file and per stale phrase found;
3. puts the sweep under `floors-registry.json` with a self-test covering every row;
4. requires the pasted `--rev <head>` run with its exit code in the round's LOG entry;
5. declares the registry a guard, not a claim counter, unless frozen at the plan commit (Q28).

Also: fix the M36 count in Q29's grounding and in README `:79`, add the two missing registry rows, and narrow
`round-52.md:71`'s "caught by".

Checks for the L1 after repair: `python3 -B verifiers/check_correction_sweep.py --self-test`; `--rev c8579a4c…` (now
expecting extra FAILs for the new rows); `--rev <head>` exit 0; `python3 -B verifiers/check_assertion_floors.py` with
the new instrument counted; rerun probes P2–P5 from `/fast/scratch/hyaku/kotoba-r52a2/CriticQ29/probe_q29.py` against
the repaired tree.
