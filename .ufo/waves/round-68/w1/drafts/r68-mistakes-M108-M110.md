# Draft — round-68 lesson `## Mistakes` entries for the three routed r67 defects

**Numbering note (conflict reported, not resolved — the L1 owns the verdict).** The task says
"M107 onward", but the committed `corpus/lessons/round-67.md:131` already holds
`**M107 — class: a seat wrote into a production directory it did not own.**` (landed at
`532cda09ad39a4b8d45bdded86d6dd9a53755141` per the spot-check's step-1 note, cited as "lesson
M107" at `corpus/lessons/round-67-verifier-spotcheck.md:34,92`), and the landed round-68 lesson
(`605b84b`, `corpus/lessons/round-68.md:133`) starts at `M107` again — two different M107s on
`master`. These drafts therefore use the next free ids **M108–M110**. If the L1 rules the
landed `M107–M110` numbering stands, shift every id below down by one (M107–M109); the text is
otherwise id-agnostic. Form follows the committed round-67 entries (M104–M107):
Evidence / Captured-by / Fix / Shown able to fail.

---

- **M108 — class: a before-line stated from the plan's expectation, not from the receipt it
  cites.** Evidence: the round-67 report states the frozen before as "at the pinned base it
  prints `0 of 1` and exits nonzero" and its Before line says "`authority ladder grounded 0 of
  1`, **exit nonzero**" while citing, in the same line, the receipt whose committed bytes read
  `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at
  2a8eba56b3f9321b70c569fa2816d42237ca49a2` and `exit=2`
  (`.ufo/reports/round-67/kotoba.md:40,42`, fleet repo; `.ufo/waves/round-67/receipts/C2-authority-measure.txt`);
  `LOG.md:2639` and `SCORECARD.md:391` repeat the same `0 of 1` before-line. Re-executed this
  round: `python3 -B verifiers/check_instruction_authority.py --rev
  2a8eba56b3f9321b70c569fa2816d42237ca49a2` prints that line on **stderr**, stdout empty,
  **exit 2**. The hyaku closure re-ran it in an isolated base checkout with the same result and
  routed defect 1: "Do not leave LOG/SCORECARD/report asserting the unobserved line"
  (`corpus/lessons/round-67-verifier-spotcheck.md` § C2 and § Routed defects 1); on the r67
  plan's own kill rule (`plans/round-67.md:97-98`) the r67 C2 claim is a **miss as declared**.
  Captured-by: `none` — Q50 requires a committed receipt for a stated gate result but is scoped
  to tip results; no criterion forces the stated line to be read off the receipt cited beside
  it. Fix (landed at the wave-1 content commit `605b84b`): an appended erratum, never a
  rewrite — `LOG.md:2667` (routed defect R67-1) and `SCORECARD.md:423` (errata for R67-1 and
  R67-2) name the observed exit-2 line and state the r67 C2 claim stands a miss as declared;
  the r67 report itself is not edited; the r68 counter is built with the corrected
  classification from the start (a missing entry is a content verdict — `0 of 5`, exit 1 — not
  an environment error), per `plans/round-68.md` § C1 counter semantics. Shown able to fail:
  the base re-run above decides — any erratum or surviving prose still asserting `0 of 1` at
  the base is falsified by re-running the same command; before the repair the plan's frozen
  before reads `0 of 4` on the routed-repairs counter, and after it
  `python3 -B verifiers/check_r67_routed_repairs.py --rev <rev>` prints `r67 routed defects
  closed 4 of 4` (this seat's re-run at `2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f`, exit 0).
- **M109 — class: a receipt cited at a path that does not hold it.** Evidence: the round-67
  report's census line cites the pre-append gate as
  `.ufo/waves/round-67/w1/controls/census-validate-append.txt`
  (`.ufo/reports/round-67/kotoba.md:55`, fleet repo); that path does not exist (`ls` →
  `No such file or directory`), and the bytes are at
  `.ufo/waves/round-67/controls/census-validate-append.txt` (1573 bytes, ending `file ok
  …/.ufo/waves/round-67/controls/validate/corpus/SOURCES.md`). The round-67 lesson's own
  § Evidence pins (`corpus/lessons/round-67.md:129`) repeats the same `w1/` path, and the
  closure routed defect 2 naming both paths (`corpus/lessons/round-67-verifier-spotcheck.md`
  § Routed defects 2). The lesson's other `w1/controls/` citations (`C1-base.txt`,
  `C1-half-controls.txt`) do resolve; the defect is this one receipt. Captured-by: `none` —
  Q60 binds artifacts cited *with a revision* (`path @ rev`); the report cited a bare path, and
  no pointer check reads `.ufo/` paperwork outside `corpus/`. Fix (landed at `605b84b`): the
  erratum names the real path (`LOG.md:2675`, routed defect R67-2; `SCORECARD.md:423`); the
  r67 report is not edited; the same correction covers the lesson's Evidence-pins line. Shown
  able to fail: `test -e` decides — the cited `w1/controls/` path fails while
  `.ufo/waves/round-67/controls/census-validate-append.txt` resolves.
- **M110 — class: an untracked control mirror left behind and left undisclosed.** Evidence:
  `.ufo/waves/round-67/w1/controls/junk-world/` — the r67 C2 junk-world control mirror,
  measured `254M` by the closure's `du -sh`, its own `.git` objects included — stayed untracked
  in the lane working tree after round 67; the round-67 report and lesson disclose no leftover
  (spot-check § Leftovers: "The report and the lesson do not disclose that it remains
  untracked"), and the r67 lesson's appended M107 asserts the final sweep left
  `git status --porcelain` "lists nothing after it" while the closure's porcelain still printed
  `?? .ufo/waves/round-67/w1/controls/junk-world/` (`corpus/lessons/round-67-verifier-spotcheck.md`
  step-1 table and § Leftovers: "porcelain still lists the junk-world tree"); routed defect 3.
  At this seat's measurement the tree is gone from the working tree (`du: cannot access … No
  such file or directory`; `git status --porcelain` no longer lists it) — the removal is the
  round-68 repair (plan R67-3: disclosed and removed this round). Captured-by: `none` — Q27/Q40
  gate the final sweep on seat writes and seat-writable directories, not on control worlds a
  seat created; no criterion requires a round to disclose an untracked tree it leaves behind.
  Fix (landed at `605b84b`): disclosed in `LOG.md:2678` (routed defect R67-3, with the 254 MB
  size) and in the round-68 lesson, and removed from the working tree — control scratch, not
  round evidence. The closure's appended-correction trigger for the r67 M107 "lists nothing"
  sentence was conditional "while that tree remains"; the tree no longer remains, so whether a
  further appended note in `corpus/lessons/round-67.md` is still wanted is the L1's call. Shown
  able to fail: `git status --porcelain` decides — it printed
  `?? .ufo/waves/round-67/w1/controls/junk-world/` at the r68 base and prints nothing for that
  path after the removal; a recurrence re-appears on the same command.
