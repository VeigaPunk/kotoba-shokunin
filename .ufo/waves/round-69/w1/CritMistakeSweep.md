# CritMistakeSweep — round-69 wave 1 (critic)

**Scope (assignment).** Falsify the round's own mistake mining: (a) sweep `corpus/lessons/` for a
round-68 lesson that already mined the R68-6 class (wrong refusal reason) or the R68-7 class
(uncommitted wave paths); if a class was already captured, the new row must say so; (b) sweep
`corpus/lessons/round-69.md` for ungrounded numbers — every count must carry a command or a
resolvable pointer. Report only. No lane file was edited.

**Bytes measured.** `corpus/lessons/round-69.md` sha256
`534f73489d837fa864bbb4ccc3198983cb6889e5e87c1b41321ac0f7285c8e06` (135 lines, mtime 07:17:50;
the L1 rewrote the file at 07:17 after my first read at 07:08 — this report targets the 07:17 bytes
and names the delta found). Lane tip measured: `a238989a` (frozen plan) on base `a5f7459f`.
Counters and code were run only from `git clone --shared /tmp/crit69`, never in the lane.

**Verdict.** The mining is *substantively* sound for R68-7 and *not* sound for R68-6: the R68-6 row
states a false provenance (`Captured by: none`) for a class that the corpus had already mined
twice, and restates the round-68 ground it mines incorrectly. Two numbers do not reproduce
(S206 word count; the `unreachable` class label), and three counts have no resolvable pointer
despite being reproducible. None of this is caught by the C2 counter this round ships.

---

## F1 — BLOCKING. `M111 … Captured by: none` is false: the class was already mined at r51 and
re-captured at r68.

Claim under test (`corpus/lessons/round-69.md:107`):

> Captured by: none (the refusal's stated reason was asserted, not observed).

Counterexample, from committed corpus bytes:

1. **Same class, mined four rounds earlier.** `corpus/lessons/round-51.md:17` (row M33):
   "A gate rejection reason characterized a source page's content with no line behind it, and the
   page contradicted the reason" — captured-by cell (`:17`, cell 3): "Q23 … and Q14 (the same
   reason is a negative claim about the page's content with no sweep behind it); caught only by the
   non-author closure". M33 is the wrong-reason-on-a-rejection class, with the capture criteria
   named. `corpus/QUALITY.md:25` still carries Q14 ("A negative claim carries its sweep"); Q23 is
   at `:34` (located quote from the authority), Q26 at `:37`, Q36 at `:47`. Q14 is exactly the rule
   M111's defect violated.
2. **Same instance, captured one round earlier.** `corpus/lessons/round-68-verifier-spotcheck.md`
   § Discernment spot-check, row "S201 staged quote ('All three skill tools require approval by
   default')" verdict **disagree**, with the two-occurrence count; and § Routed defects
   `R68-6 (:179-183)`: "The lesson's refusal of the staged S201 quote states that the page does not
   carry the staged words. It does, verbatim, twice … Mine this as a mistake row". That file is a
   committed `corpus/lessons/` lesson with `round: 68`.
3. The round-69 lesson cites `round-68-verifier-spotcheck.md` **nowhere** (`grep -a` over the whole
   file returns no hit) while it names the same closure's R68-7 for M112 (`:114-116`). The two
   rows use the `Captured by:` field inconsistently: M112 credits the closure's routed defect,
   M111 denies any capture although the same file captured it in prose *and* in the routed list.

**Impact.** M111 teaches a false provenance. The class-fix line it needs (Q62) is presented as
unprecedented while Q14 already governs the same negative-claim failure mode (F3). This is the
same defect family as M107 (a line asserted against the lane's own evidence) and M110 (a closure
artefact left unrecorded) — the round reproduces the class in its own correction.

**Smallest safe correction (lesson text, one field + one clause).**
- M111 `Captured by:` → name both authorities in the corpus's own vocabulary:
  "R68-6 in `corpus/lessons/round-68-verifier-spotcheck.md` (discernment row: two occurrences
  measured) for this instance; M33 in `corpus/lessons/round-51.md` for the class (captured by
  Q23 + Q14). The r68 lesson itself captured nothing."
- Keep the parenthetical "the refusal's stated reason was asserted" only as the *mechanism*, not as
  the capture history.

## F2 — BLOCKING. The row misquotes the round-68 ground it mines (the class recurs inside the
correction).

Round-69 `:52-54` (Refused bullet) and `:112-113` (M111) both say round 68 refused the staged
quote "on the ground that the page does not carry them" / "does not state it".

Round-68's actual ground (`corpus/lessons/round-68.md:52-58`) is different:

> The page states the rule as a tool list — "load_skill, read_skill_resource, run_skill_script
> require approval by default" — not with the staged words "All three skill tools". The staged
> wording is a paraphrase, so it is not admitted as a located quote … Flip: a fetch that renders
> the literal phrase "All three skill tools require approval by default" would clear it.

r68 asserted *paraphrase-vs-verbatim*, not absence. The round-68 closure itself stated the ground
accurately ("The lesson's stated ground ('the page … not with the staged words') is false"). The
round-69 row replaces the precise, falsifiable ground with an absence claim that no reader of
r68.md would recognise — so the mined lesson loses its bearing: the true defect was refusing on
an unchecked paraphrase judgement while the lane's own scout log had already located the sentence
elsewhere (`ScoutMsAgentFramework.log:62-64`, verified present and identical at `a5f7459`).

Live re-check (my own fetch, not the lane's): `curl -sSL
https://learn.microsoft.com/en-us/agent-framework/agents/skills` (156,387 B) →
`grep -c "All three skill tools require approval by default"` = **2**, both inside
`<p>` tool-approval prose. So the sentence is verbatim twice, and r68's paraphrase ground was
false — the class stands; only the restatement is wrong.

**Smallest safe correction.** In both places, quote r68's own words: "refused the staged quote
because 'the staged wording is a paraphrase' — a paraphrase judgement asserted without a sweep,
while the literal phrase was on the page twice". No change to the verdict.

## F3 — Q62 duplicates a criterion the lane already holds (duplicate authority, undisclosed).

`corpus/QUALITY.md:78` (Q62, added by this round: `git diff --stat HEAD -- corpus/QUALITY.md` →
`2 ++`, `git show HEAD:corpus/QUALITY.md | grep -c Q62` → 0) reads: "A refusal's reason is grounded
before it is recorded … never on an assertion that the source lacks the words". `QUALITY.md:25`
(Q14) already reads: "A negative claim carries its sweep: the search that produced the absence".
M33's captured-by cell names Q14 for exactly this reason class. The lesson says "the QUALITY
criterion Q62 grounds refusals in observed facts" without noting it restates Q14 (and Q23's
located-quote-from-the-authority rule). Two criteria for one failure mode is the duplicate-authority
defect the closure charges elsewhere.

Charge split, for fairness: the duplicate authority was *routed in* — R68-6's own wording ends
"and add the grounded criterion to `corpus/QUALITY.md`", without checking that Q14/Q23 already
cover the class. The lane is still the one that ships the second criterion and presents it as new.

**Smallest safe correction.** Keep Q62 only if it is written as a *refinement* of Q14 with the
Q14 reference in its evidence cell; otherwise drop the new row and cite Q14 in M111. Either way the
lesson must not present Q62 as a fresh capture.

## F4 — S206 quote word count does not reproduce: stated 12, measured 11.

`round-69.md:49`: `"the project-level skill takes precedence and the user-level skill is ignored."
(12 words)`. Count of the quoted string = **11** (`the|project-level|skill|takes|precedence|and|
the|user-level|skill|is|ignored.`). Live page (my fetch, 38,509 B) carries exactly that sentence,
also 11 words: "If a project-level (…) and a user-level (…) skills share the same name, the
project-level skill takes precedence and the user-level skill is ignored."
The other four counts reproduce (8/9/6/8) and their strings are present on the four fetched pages
(raw + tag-stripped: Roo 1/1, Amp 1/1, Deep Code 3/3, opencode 1/1).

**Smallest safe correction.** `(12 words)` → `(11 words)`. (Within C1's ≤25-word bound either way,
so this is a citation-form defect, not a claim defect.)

## F5 — The `unreachable` count has no class label in the pointer it cites.

`round-69.md:97`: "**13 rows** — 7 `payload-absent` and 6 `unreachable`
(`assimilation/quarantine-slice`)". The artifact holds 13 lines; 7 carry `` `payload-absent` ``; the
other six read, verbatim:

```
 S236`   the cited source could not be fetched, so no quote was checked
 S237`   … S238` … S239` … S243` … S169`
```

i.e. the class cell is missing, the ids carry a stray backtick, and the word `unreachable` appears
nowhere in the file (`grep -oE 'unreachable' | wc -l` → 0). The six-row class is only recoverable by
mapping the ids to r68's table (`round-68.md`, the 13-row verdict table), which is a second
document. The total (13) and the 7 reproduce; the label does not.

**Smallest safe correction.** Normalise the six rows to ` S169   `unreachable` ` (class cell
present, backtick closed) or amend the sentence to "13 rows — 7 ``payload-absent``; the other six
were unfetchable (rows `S169`, `S236`–`S239`, `S243`)" so the pointer carries the number.

## F6 — `0 collisions` cites an empty file; the two operands are unpointed.

`round-69.md:82-83`: "128 registry ids, 188 staged ids, **0 collisions**
(`.ufo/waves/round-69/assimilation/collisions`)". The pointer is a **0-byte** file: it records no
header, no command and no operands. Both counts and the result do reproduce from the sibling
artifacts, which the lesson does not name:

```
wc -l .ufo/waves/round-69/assimilation/{reg-ids,staged-ids}   -> 128 / 188
comm -12 <(sort reg-ids) <(sort staged-ids) | wc -l           -> 0
```

`assimilation/guard-proof/` (SOURCES.md, collisions, collisions-col0, reg-ids, reg-ids-col0) is
present and supports the non-vacuity sentence as written.

**Smallest safe correction.** Print the two counts and the `comm` command into the collisions file
(or cite `reg-ids`/`staged-ids` and the command in the sentence).

## F7 — `1,020 parsed characters` carries no command (reproducible: 1,020 / stripped 1,019).

`round-69.md:106-107`. Reproduced:

```
python3 -c "import yaml;print(len(yaml.safe_load(open('SKILL.md').read().split('---')[1])['description']))"  -> 1020
folded/stripped length                                                                                        -> 1019
```

The cap side is grounded (`corpus/knowledge/skill-listing-thresholds-round54.md:15-16,42-46`,
1,024 for four clients). The measurement is a carried value from `round-68.md` (which stated
1,019 stripped / 1,020 parsed and its method) with no command or pointer here — Q19's
"re-measure and print the command" is met by the value but not by the record.

**Smallest safe correction.** Append the one-line `yaml.safe_load` command (or point at
`round-68.md`'s measurement paragraph as the carried source).

## F8 — `13 minutes` has no path/line, and the frozen plan asserts the opposite.

`round-69.md:10-11` cites only "watchdog `lane-dead-no-report kotoba round=69`". The count
reproduces from the fleet log (06:46:36 launch → 06:59:59 death = 13m23s), lines
`.ufo/watchdog.log:1304` and `:1309`; attempt 2 launches `:1310`. But the **frozen plan**
(`plans/round-69.md`, inherited-state paragraph) states: "The watchdog log shows no
`lane-dead-no-report kotoba round=69` line: no earlier attempt." That sentence was true when the
plan text was authored (author date 03:31) and false 2.6 min after it was committed (committer date
06:57:22, death 06:59:59). The plan is read by every seat and is quoted as the round's premise; the
lesson silently contradicts it without saying the plan is stale.

**Smallest safe correction.** Lesson: point at `.ufo/watchdog.log:1304,1309`. Main: record the
plan's inherited-state line as a stale carried before-value (Q19) in the round's own record, not
only in the lesson.

## F9 — "passes at the round-69 tip" is not a measurement at any existing tip.

`round-69.md:119` (M111) and `:21-22` (freeze explanation) both certify the state "at the committed
round-69 tip". Measured:

```
cd /tmp/crit69 && git checkout -q a238989
python3 -B verifiers/check_r68_routed_repairs.py --rev a5f7459  -> r68 routed defects closed 0 of 8, exit 1
python3 -B verifiers/check_r68_routed_repairs.py --rev a238989  -> r68 routed defects closed 0 of 8, exit 1
```

The base figure is correct; the tip figure is `0 of 8` at the only existing tip, because the
lesson, S208, Q62 and the 24 wave paths are all uncommitted. So "passes at the round-69 tip" is a
prediction about a commit that does not yet exist, written in the present tense.

The freeze paragraph's "18 assertions" **does** reproduce (counter overlaid with the working-tree
entry: `self-test: 0 failure(s) over 18 assertions`, exit 0; and `--rev a238989` prints
`skill precedence backed 0 of 5`, exit 1, "entry missing").

**Smallest safe correction.** Reword both to the landing condition ("passes once the round-69
commit lands"; C2's plan already words D7 this way), or cite the hash after it exists.

## What verifies (not a finding, for calibration balance)

| Lesson figure | Command / pointer | Result |
|---|---|---|
| `a5f7459` base = `0 of 8` | `check_r68_routed_repairs.py --rev a5f7459` | `0 of 8`, exit 1 ✓ |
| `--rev` missing entry = `0 of 5`, exit 1 | `check_skill_precedence.py --rev a238989` | ✓ (content verdict) |
| `18 assertions` | `--self-test` over the overlay | `0 failure(s) over 18`, exit 0 ✓ |
| five quotes present on their pages | my `curl`, raw + tag-stripped | 1/1/3/1/1 occurrences ✓ |
| `24` paths, `10` modified / `14` untracked | `git status --porcelain .ufo/waves/round-68 \| wc -l`; `awk '{print $1}'` | 24 = 10 M + 14 `??` ✓ |
| `269 MB` clone | `du -sh .ufo/waves/round-68/w1/controls/c2falsify-clone` | `269M` ✓ |
| `2dd3567a` landed row vs 24 dirty paths | `.ufo/reports/round-68/kotoba.md:32`; status above | ✓ M112's evidence holds |
| `128`/`188` ids, `0` collisions | `wc -l reg-ids staged-ids`; `comm -12` | 128/188/0 ✓ |
| `13` rows, `7` `payload-absent` | `wc -l`; `grep -oE` | 13 / 7 ✓ (F5 for the six) |
| six rows gained, none lost | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | 128 → 134 ✓ |
| S203–S208 shape | 11 cells, `opened 2026-10-25`, `used-by` as stated | ✓ |
| `1,024` cap pointer | `skill-listing-thresholds-round54.md:15-16,42-46` | ✓ |
| `S208` amendment in the r68 entry | `client-trust-gates-round68.md:81-82` | ✓ |

## Impacted axes (advisory — no axis was moved by this seat)

- **calibration**: the round adds a mistake row whose provenance field is false (F1) and whose
  restatement of the mined record is false (F2) — a self-assessment miss of the class it mines.
  This is the axis the round must not claim improvement on until F1/F2 land.
- **consistency**: Q62 duplicates Q14 (F3); the `recheck`/word-count cell for S206 is off by one
  (F4); the quarantine artifact is malformed (F5).
- **depth / coverage**: unaffected — C1's five quotes and the counter's 5-of-5/18-assertion arms
  reproduce against current bytes; C3 untouched by this seat.
- **operability**: the C2 counter cannot protect against F1–F5: `check_r68_routed_repairs.py:42-43`
  discloses D4/D6 as presence floors, and `d6_mistake` (`:267-276`) tests only for a line
  containing both `R68-6` and `S201` plus a QUALITY row citing `round-69.md`. A false
  `Captured by:` and a misquoted ground pass by construction, so `8 of 8` is not evidence that the
  mining is correct.

## Changelog of this seat's own observations

- 07:08 read of `round-69.md` (8,546 B) had no freeze-receipt paragraph and no `18 assertions`
  line; the 07:17 rewrite (9,234 B, sha `534f734…`) added both. F1–F5 hold on the 07:17 bytes;
  the `18 assertions` and `0 of 5` figures were re-verified against the new text.

Tool installs: none. Processes started: two `curl` batches and one `git clone --shared` + counter
runs, all under `/tmp`, all exited; nothing left running.
