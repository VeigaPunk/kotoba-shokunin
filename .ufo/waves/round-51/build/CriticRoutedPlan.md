Seat: KotobaR51.CriticRoutedPlan (build wave, round 51, critic). Base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`.

**Result: FAILS for `plans/round-51.md` § Routed defects as written. Five of its seven lines (D1, D2, D3, D6, D7) drop or misplace a routed sub-item, D4 has the placement problem, and D5 holds only once a path is fixed. With the build-spec items counted, the result is HOLDS-BOUNDED: the items cover the D1 command, the D3 eight-page bound and the D6 generic-refusal bound. Five gaps stay open even then: D1 trigger, D2 carry, D3 coupling, D4 placement, D7 new-instrument floor. The precedence-rule constraint HOLDS-BOUNDED.**

## Table

| D | plan line | verdict | missing piece (smallest safe correction) |
|---|---|---|---|
| D1 | commit DescDraft byte-exact; disposition and seat-accounting correction in round-51 lesson and LOG; leftover sweep after last seat write | GAP | (a) The plan text drops the **misroot** half of "misroot and leftover sweep". (b) "After the last seat write" has no observable trigger. The `LeftoverSweep` seat runs inside the build wave, so its output predates the last write by construction and cannot discharge D1. Fix: the L1 re-runs the lane and fleet-root sweep right before the final lane commit and again before the report commit. Each time it records the newest mtime under `.ufo/waves/round-51/` and checks that the mtime is earlier than the sweep time. (c) The plan does not name the misdated landing hash (`956ee167` should be `542f515`). The `D1Disposition` item does. (d) Fleet prompt §5 also asks that the report name the leftover. |
| D2 | bound the sentence at `SCORECARD.md:31` and `SKILL.md:135` | GAP | Choosing the bound is allowed by the spot-check. But `corpus/lessons/round-50.md:199` says "carried to round 51 with the four `MutBoxProofGate.md` survivors". Neither the plan's D2 or D7 line nor any build item (`D2Bound`, `CarryD7`) re-carries or fixes the F3–F5 false red and crash paths or the 4 survivors. Fix: add one carry line for each to D7. Format nit: the round-50 convention is `**Round-50 qualifier (routed defect D2):**`, appended at the end of the evidence cell (`SCORECARD.md:31`). `D2Bound` asks for `Round 51 qualifier (routed D2):`. Use `**Round-51 qualifier (routed defect D2):**`. |
| D3 | `corpus/README.md:72` corrected; `SKILL.md:375-377` rewritten under C2 | GAP | (a) The spot-check names two faults at `SKILL.md:375-377`. The plan covers only the "documented remedy" one, through C2. It does not name the missing **eight-page bound** on "No client documents a rule…" (`D3Sweep` does). (b) The SKILL.md fix depends on C2 landing. If C2 ends below 7 of 7 and its table is held, D3 stays unfixed. D3 is a calibration defect that does not depend on C2. Fix: land the bounded sentence whether or not C2 lands, citing Copilot SDK `skills.md:805-810`. (c) `corpus/README.md:72` carries a second withdrawn phrase, "the documented remedy is a more specific description". The spot-check named only "every documented rule is keyed on the name". Correct both. (d) "Supersedes finding 4" must be an appended section in `skill-selection-rules-round50.md`. Knowledge entries are append-only: the census entry was +182/−0 in round 50 and is headed "Appended round 50 (append-only)". Finding 4 must not be edited in place. |
| D4 | appended correction of the reject reason; the page becomes a row because C2 cites it | GAP (placement) | The plan answers "decide whether to write the row" (yes). It does not say where the correction lives, and the `SrcCopilotSdk` item says "replacing the round-50 lesson's reject reason". Precedent at `corpus/lessons/round-50.md:80-86`: "The round-49 lesson is append-only and owned by its round, so the erratum lives here". `round-49.md` had 0 changed lines in round 50. Fix: append the erratum in `corpus/lessons/round-51.md`, not by editing `round-50.md:44`. The row decision should rest on finding 3 as well as on C2. The round-50 entry already cites "SDK `skills.md:685`, a page opened by the build seat but not written as a row" (entry § Falsify-wave corrections). So `used-by` should also name `skill-selection-rules-round50`, and an appended note should retire "not written as a row". |
| D5 | `PROVINCE.md:44` kama quote and citation; census line 273 kengaku `README.md:192` | HOLDS-BOUNDED | Both sub-items are covered. One path is wrong, inherited from the spot-check: the file is kengaku **`corpus/README.md:192`**, which lists six outputs. At pin `1f3b0f1e`, top-level `README.md` has 14 lines. The `D5Rows` prompt points the seat at `…:README.md` lines 185-200, which do not exist. The census correction must fix the quote only and must not re-rule kengaku. A re-ruling would apply the precedence rule (see D6). The ruling's basis ("reads only the SKILL.md of the lane it runs in") is consistent with the six own-lane outputs. |
| D6 | rule marked provisional until L0; note it was written after the rows were known; not extended or relied on | GAP (plan text) | The plan line drops "**resolve or bound** the generic-refusal exit (`RowTameshiR50` F4)". The `D6Provisional` item covers it as a bound, and a bound is the only option that obeys the constraint: resolving would rewrite the rule before L0 answers. Fix: the plan says "bound, not resolve". The appended section marks tameshi as "cleared by a generic refusal" with no class change. |
| D7 | carried with reasons | GAP | `CarryD7` enumerates all seven sub-items, including the floors-registry gap and F30–F33. Counterexample: this round adds a self-tested counter, `verifiers/check_overlap_levers.py --self-test`, and the `LeverGuard` spec has no floors-registry step. The registry has 11 instruments and names neither driver (command below). So round 51 would leave two unregistered claim counters, the class of NoHarmGates F2 ("the C2 counter is unregistered"). The lane treated this as debt before: `SCORECARD.md:118` said "`check_sibling_census.py` is not yet in the floors registry", and round 50 floored it. Fix: add an `overlap_levers` row (registry, both in-file tables and the docstring, bumped in step, `instrument_total` 11 → 12), or carry it explicitly next to `box_proof_case_deletion.py`. That driver has no `--self-test`, so it cannot be floored as-is, which justifies its carry. |

## Ruling on DescDraft (spot-check § Ruling)

- The bytes are still the closure's bytes: the mtime is `2026-10-22 10:52:19.554935837 -0300`, which matches the spot-check's 10:52:19.55. The file is 10,079 B, sha256 `0181a45953242fcff7595a91d8c1036b10dc4dc7aaae5303baa1cb445c3d2348`. The spot-check recorded no hash, so to make "byte-exact" checkable, put this sha256 in the disposition line and compare it again at commit time.
- `D2D4Wording.md` is tracked (`git ls-files --error-unmatch` exit 0, mtime 10:51:16), so only its accounting needs correcting, not its bytes.
- The seat-accounting correction belongs in the round-51 lesson and LOG, as the plan says, never in the fleet round-50 report. The report has a single filing commit with no addenda (spot-check Step-1, round-49 D1). HOLDS.

## Precedence-rule constraint (not extended, not relied on)

- HOLDS-BOUNDED. Neither claim counter reads the rule's output. `verify_surfaces.py` reads the omp dump. The `LeverGuard` spec reads only `SKILL.md`, `corpus/SOURCES.md` and the new entry.
- A sibling grep for overlap-lever ground found 0 lines in every sibling lane at master (command below), so `SiblingOverlapScan` is unlikely to force a contested ruling. [INFERENCE: that seat's wider pattern set could still hit something.]
- Tension to state explicitly: fleet `l0-questions.md:105` says "kotoba keeps this as its reading until answered". The D6 section should define "not relied on" as no new ruling, no row moved, and no claim counter reading the rule. Otherwise "keeps as its reading" and "not relied on" read as contradictory.
- The D5 kengaku correction sits inside the rule's rulings bullet. It must stay quote-only (see D5).

## SCORECARD / LOG conventions round 50 followed

- **LOG is append-only across rounds.** Round 50 shows +24/−0 against `f3046466`, with 0 lines starting `-` in `diff -U0`. One of the round's own lines was edited before filing, and that was disclosed (spot-check, `2abd290`). A dead earlier citation is handled with an in-source erratum, not a LOG edit (`l0-questions.md:85`).
- **SCORECARD has two kinds of change.**
  - A *claimed* axis row is rewritten in place. The new round's head goes first and the prior text is kept verbatim as `**Round 49 (as recorded):**`. Checked: the old row-31 and row-34 evidence text is a verbatim substring of the new rows.
  - Corrections to other text are *appended*:
    - `**Round-50 qualifier (routed defect D2):**` at the end of the evidence cell;
    - "Round 49 correction to the `Next: round 49` block above (… append-only)" as a new paragraph (`SCORECARD.md:114`);
    - completion, `Next:`, move-log and capability rows.
  - Earlier `Next:` blocks stay (`:112`, `:118`, `:122`).
- Round 51 should therefore:
  - rewrite only the freshness and depth rows, keeping `**Round 48 (as recorded):**` and the depth equivalent;
  - append the D2 qualifier to row 31 after the round-50 qualifier;
  - leave the existing round-50 text in row 31 untouched.
- `corpus/README.md` index rows *are* rewritten in place historically (for example `9f2f1a7` +1/−1), so the D3 index fix in place fits convention. Lessons and knowledge entries are append-only (D3d, D4).

## Evidence (all read-only; exit codes verbatim)

- `git -C <lane> rev-parse HEAD` → `43ca0bfb…`; `git status --porcelain` → `?? .ufo/waves/round-50/build/DescDraft.md`, `?? .ufo/waves/round-51/`, `?? plans/round-51.md`. Exit 0.
- `git diff -U0 f3046466 43ca0bfb -- SCORECARD.md | head -80`: rows 31 and 34 are replaced and lines 120-123, 252-253 and 262 are added. Exit 0.
- `git diff --numstat f3046466 43ca0bfb -- LOG.md SCORECARD.md PROVINCE.md corpus/…` → LOG 24/0, SCORECARD 9/2, PROVINCE 8/8, census entry 182/0, README 7/0, round-49 lesson absent (0 changes). Exit 0.
- `git diff -U0 f3046466 43ca0bfb -- LOG.md | grep -c '^-[^-]'` → 0.
- The python substring check (old row-31 and row-34 evidence cell inside the new row) printed `True` for both. Exit 0.
- `git show 43ca0bfb:corpus/lessons/round-50.md | sed -n '80,90p'` → the erratum-location sentence quoted under D4. `grep -n 'MutBoxProofGate|fail.open'` → `round-50.md:171,193,199`, `LOG.md:2407`. Exit 0.
- `git show 43ca0bfb:SKILL.md | sed -n '371,380p'` and `corpus/README.md | sed -n 72p` → the texts quoted under D3. Exit 0.
- `build-spec.json` has 33 items and no D4-named item; D4 sits inside `SrcCopilotSdk`, whose prompt reads "one appended correction paragraph replacing the round-50 lesson's reject reason". `LeverGuard` has no floors step. Read with `python3 -c 'json.load…'`, exit 0.
- `floors-registry.json` instruments → 11 keys (checklist … sibling_census); its `path` values include neither `box_proof_case_deletion.py` nor `check_overlap_levers.py`. Exit 0. `box_proof_case_deletion.py` argparse has `--rev`, `--repo` and `--in-place`, and no self-test.
- `git -C kengaku-shokunin show 1f3b0f1e:README.md | wc -l` → 14; `…:corpus/README.md | wc -l` → 367. Line 192 lists "SOURCES census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries". Exit 0.
- Sibling loop `git -C <repo> grep -niE 'disabledSkills|disable-model-invocation|overlapping skill|skills? (deny|disable)' <master> -- corpus SKILL.md PROVINCE.md | wc -l` → no lane printed a count above 0. Exit 0.
- `stat -c '%y %s'` and `sha256sum` on DescDraft → the values above. Exit 0.
- Fleet `l0-questions.md:105` (kotoba round-50 line) ends "…kotoba keeps this as its reading until answered." Fleet `.ufo/prompts/kotoba-round-51.md:318-325` §5 is the inherited-state rule. Exit 0.

Tools installed: none. Scratch: `/fast/scratch/hyaku/kotoba-r51/build/CriticRoutedPlan/` (`items.txt`, `SC.md`, read copies only). No lane writes other than this report.
