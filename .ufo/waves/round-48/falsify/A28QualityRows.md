# A28QualityRows — falsify Q20 and Q21 (`corpus/QUALITY.md`)

Seat: `KotobaR48.A28QualityRows` (critic, leaf, no delegation). Date 2026-10-22 (UTC). Target commit
`887b6af` (C1 freshness), read at lane tip `84b9c9ba89559b51a72c83c2b9605b184df4ae9e`. Base `75f671b`.
Lane checkout read-only; the only file written there is this report. Runs used a private clone at
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A28QualityRows/clone` (checked out at `84b9c9b`).
Tools installed or updated: none. I used the system `python3`, `git`, and the already-installed PyYAML 6.0.3.
Web sources re-opened: none. Every claim below rests on lane bytes, lane-checker runs and PyYAML;
the packager (S012) verdicts I quote are peer measurements from `C2LaneCheckerRun.md` and are marked as such.

## Verdict

**DEFECT, medium.** Both rows are append-only and grounded in lesson rows that exist, and Q20 does fail
a bad candidate (base `SKILL.md:151`). But the round's own landed tree fails Q20 on a surface Q20 lists
(the checker's detail string). Under Q21, the record "Repaired by C1" for routed item 3 is too strong:
the cause it names is moved on only one of three live carriers. Q20's applies-to list also misses
`PROVINCE.md`, and its body does not cover the "wrong authority" half of its own grounding class M24.
The declared C1 count (34 to 35 entries) is not affected. Only the "repairs routed item 3" framing is.

## 1. Append-only — CONFIRMED

- `git diff 75f671b 84b9c9b -- corpus/QUALITY.md` (exit 0): exactly two `+` lines (Q20, Q21), zero `-` lines.
- `git log 75f671b..84b9c9b -- corpus/QUALITY.md`: one commit, `887b6af`.
- Count of `^| Q` rows: 19 at `75f671b`, 21 at `84b9c9b`. Both new rows have `supersedes` set to `—`.
- `git status --porcelain -- corpus/QUALITY.md corpus/lessons/round-48.md` in the lane is empty (no uncommitted drift).
- Pre-existing, not new: preamble line 7 still says `grounded in` names a row in `round-46.md`. Q19 to Q21
  point to other lessons in parentheses. Seat `FrQualityCriteria.md` F4 already flagged this.

## 2. Grounding — CONFIRMED with two defects

Both rows cite classes that exist in `corpus/lessons/round-48.md` § Mistakes: M24 is marked `none → Q20`
and M26 is marked `none → Q21`.

- **Class-name drift (low).** QUALITY's Q21 cell reads "M26 Repair named after the row, not the cause".
  The lesson row reads "M26 A repair claim named after the routed row, not the routed cause".
  `grep -c 'Repair named after the row, not the cause' corpus/lessons/round-48.md` → 0, so a lookup
  by the cell text finds nothing. Q19's precedent is a prefix truncation, which still matches. For M24,
  the truncated name finds its row (`grep -c 'Rule credited to the wrong authority'` → 1).
- **Q20's body does not cover half of M24 (medium).** M24 has two halves: (a) a rule credited to the
  wrong authority, and (b) a lexical approximation described as a vendor rule. QUALITY keeps only the
  name of half (a). Q20's body binds only "a check that approximates an authority's rule", which is
  half (b). Counterexample: S003's teaches cell at `75f671b` says "body under 500 lines; an
  Anthropic-only rule the open spec lacks" (`git show 75f671b:corpus/SOURCES.md | grep '^| S003'`).
  That cell is in Q20's applies-to list (SOURCES `teaches` cells), but it approximates nothing. It is
  an attribution plus an unswept negative claim. Q20 as written does not fail it, and Q14 applies
  only to knowledge and lesson prose. So the half of M24 that QUALITY's cell is named after still has no criterion.

## 3. Able to fail a bad candidate

**Q20 on base `SKILL.md:151` (`git show 75f671b:SKILL.md | sed -n 151p`) — WOULD HAVE FAILED.**
The line says `trigger.no_xml_tag` "gates the XML-tag rule" and that "Anthropic's reference packager
(S012) is stricter and refuses any `<`/`>`". It fails all three of Q20's clauses:
- It does not say the check is an approximation, and it names no parsed rule being approximated.
- It carries no counterexample in either direction.
- "stricter" is a label, and my runs show it is false as a direction:

| fixture (sha256 prefix) | lane `trigger.no_xml_tag` (my run, landed checker `4ea2100d…`) | `yaml.safe_load` description | packager (peer, `C2LaneCheckerRun.md`) |
|---|---|---|---|
| single-quoted `'Use \u003cb\u003e here.'` (`1ab29a6d`) | FAIL, exit 1 | `'Use \\u003cb\\u003e here.'`, no `<` | PASS (f08) |
| alias `description: *d`, anchor `"Use <b> here."` (`7a3e2b30`) | PASS, exit 0 | `'Use <b> here.'`, has `<` | FAIL (f02) |
| `Compares a < b and reports.` (`7a6d2abf`) | PASS, exit 0 | has `<` | FAIL (f06) |

The lane check both misses tags and over-flags, so "the packager is stricter" does not hold as a measured
direction. The landed line 151 passes Q20: it names the lexical approximation of the parsed rule, says
"the two disagree in both directions", and links the entry that holds the run counterexamples.
*Weakness in the lesson's own able-to-fail proof:* M24 shows Q20 failing by
`grep -c 'frontmatter-rule-authorities'` on the line (0 at base, 1 at landing). That grep only finds a
link. A line that keeps "is stricter" and adds the link would pass the grep and still fail Q20. The
proof stands in for Q20; it is not Q20.

**Q21 on the round-47 C3 calibration claim (`plans/round-47.md:34-39`, `LOG.md:2323`) — WOULD NOT HAVE FAILED.**
C3 named its causes: `LOG.md:2111` cites a runner that the line itself records as absent, and the
corpus index lacked the round-46 spot-check row. It re-measured both: checklist exit 1 to 0 (9/1 to 11/11,
"1 recorded absence excused"), and corpus integrity and independent checks DRIFT to 0. The spot-check
(`round-47-verifier-spotcheck.md:33`) rejected C3 on different grounds: green targets do not settle the
21/24 to 20/24 join or full no-harm. C3 never claimed to repair either. So Q21 is correctly narrow,
but the round-47 rejection would still need Q05, Q18 or no-harm judgment. Q21 adds nothing there.

**Strongest counterexample: Q21 applied to this round's own C1 — FAILS the "Repaired" wording.**
The entry states the cause of routed item 3 itself: "the lane described its `trigger.no_xml_tag` check as
if it executed a vendor rule" (`frontmatter-rule-authorities-round48.md:7-8`). There are three live
carriers of that description at `84b9c9b`:
1. `SKILL.md:151`: moved (repaired).
2. The checker's detail string `verify_skill_checklist.py:1307-1308`: unmoved. In the private clone,
   `python3 -B verifiers/verify_skill_checklist.py --repo . --check trigger.no_xml_tag` (exit 0) prints,
   on every PASS as well as FAIL: "(S003 Anthropic rule, absent from the open spec (S001); Anthropic's
   packager bans any '<'/'>' and is stricter)". `--json` carries the same `detail`. It cites S003 and
   S001, which this round superseded with S019 and S018. The entry admits this (`:72-73`: "left unchanged
   this round and stays a known text defect").
3. `PROVINCE.md:15`: unmoved. It says "S003's Anthropic rule … is executed on `name` and `description`
   by … `trigger.no_xml_tag`". Its last change was `7ad7fad` (round 47).

Yet `corpus/lessons/round-48.md` routed-items row 3 says "Repaired by C1", and `corpus/README.md:66`
says the entry "repairs routed item 3". Q21: closing the gap in one row without moving the cause on the
other carriers is `improved-bounded` and must say so. Carrier 2 is also a "checklist check", so Q20
fails the landed tree on a surface it lists. This shows the criterion can fail a candidate, and the
candidate it fails is this round's own.

## 4. Scope gap in Q20's applies-to — DEFECT (medium)

Q20 lists "checklist checks, SKILL.md rule prose, SOURCES `teaches` cells". M24 half (b) survives
word for word on `PROVINCE.md:15` (a lane identity surface), which Q20 does not list. As written, Q20
would pass a round that fixes `SKILL.md` and leaves `PROVINCE.md` saying the check executes a vendor rule.
That is this tree's exact state. The historical SCORECARD operability row (`SCORECARD.md:31`, "S003 rule
on parsed `name`+`description`") makes the same claim, but it is a dated record, and Q03/Q19 cover it.

## Impacted axes

- freshness: the C1 "repairs routed item 3" framing. The 35-entry count is unaffected.
- calibration: the records `round-48.md` routed row 3 and `corpus/README.md:66` overstate the repair.

## Smallest safe correction

1. Do not rewrite Q20 or Q21. Append a row that supersedes Q20. It should (a) widen applies-to to every
   lane surface that describes a check (`PROVINCE.md`, `corpus/README.md`, check detail strings), and
   (b) add the attribution clause: a rule credited to one authority, or called "X-only" or "Y lacks",
   carries the located quote and the sweep of the other authorities. Ground it in M24's full class name.
2. Change the C1 disposition to `improved-bounded`: the entry and `SKILL.md:151` are repaired, while the
   checker detail string `:1307-1308` and `PROVINCE.md:15` still carry the vendor-rule description.
   Alternatively, fix those two texts. The detail-string change is one string literal plus the self-test arms that match it.
3. In the Q21 cell, use the lesson's exact M26 class name, or a true prefix of it.

Not run by me: the producer-versus-instrument 11/10 live-row measurement behind M26's able-to-fail
proof, and the packager itself (no fetched code executed).

Report: .ufo/waves/round-48/falsify/A28QualityRows.md
