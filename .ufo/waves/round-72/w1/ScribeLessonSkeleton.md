# ScribeLessonSkeleton — round-72 wave 1 (build)

**Verdict:** the `corpus/lessons/round-72.md` skeleton is drafted in house form with all five
required sections; every value that depends on a later measurement is a `<<…>>` placeholder and no
number is estimated. Three of the brief's factual characterisations do not survive my own re-open and
are recorded below as corrections/conflicts (F2, F3, F4); the brief's `14 rounds` in M126 (F5) and the
plan's `four instruments` (F4) are left as placeholders rather than repeated. Nothing committed in the
lane was edited; no counter was written.

Deliverables:

- `.ufo/waves/round-72/w1/build/ScribeLessonSkeleton/round-72.md` (16,732 B) — the lesson skeleton.
- `.ufo/waves/round-72/w1/build/ScribeLessonSkeleton/Q65-row.md` (3,022 B) — the QUALITY row draft
  for the one mistake with `none` in the existing bar (M124).

## F1 — the skeleton's fixed inputs are the frozen plan's own sentences, re-read

Commands (lane root unless stated):

```
$ grep -n 'check_author_rules.py --rev\|check_substrate_repin_v2.py --rev\|check_tip_battery.py --rev' plans/round-72.md
76:python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints "author-facing rules in SKILL.md N of 4", exit 0 when N == 4
118:python3 -B verifiers/check_substrate_repin_v2.py --rev <rev>  ->  prints "host substrate re-derived: pins OK k/3; surfaces pass p of 7; removal ledger l of l verified", exit 0 when k == 3 and p == 7 and the ledger conjunct holds
153:python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery exit 0: N of 6", exit 0 when N == 6
```

Freeze commit present: `git cat-file -t 7b229a18` → `commit`; `git log --oneline -1 7b229a18` →
`7b229a1 round-72: plan frozen …`. Base is an ancestor of `master`
(`git merge-base --is-ancestor c69711ee08279609374d895bb0f3c8c18ccf15c9 master` → exit 0); `master`
now reads `e61fd294c2e1cdd16d594b57b310254183ace1e7` (plan + wave-1 spec commits on top of the base).
Insertion surface for C1 checked: `## Trigger-fidelity checklist` at `SKILL.md:253`, next `## ` at
`SKILL.md:328`.

C1's three held entries exist and their `used-by` cells carry the ids the plan cites:

```
$ grep -oE '^\| S[0-9]{3} ' <(grep 'skill-name-precedence-round69.md' corpus/SOURCES.md) | tr -d '| ' | tr '\n' ' '
S203 S204 S205 S206 S207
$ … 'instruction-authority-ladder-round67.md' … → S123 S124 S129
$ … 'client-trust-gates-round68.md' …          → S198 S199 S200 S201 S202 S208
```

(`corpus/knowledge/resident-index-and-rungs-round72.md` does not exist yet — A4's entry is this
round's to write.) Front matter uses the r70/r71 house form `author: kotoba L1 (hyaku run 7, round
72, attempt 1)` — same content as the brief's unparenthesised string.

## F2 — M124 is grounded; the promised `53 of 53` was never true in any commit

```
$ python3 -B verifiers/check_gate_registry.py --rev c69711ee08279609374d895bb0f3c8c18ccf15c9 | tail -1
gate registry rows conformant 51 of 53 lane verifiers; phantom 0        (exit 1)
$ git log --oneline -S'check_skill_evals_v2' -- SKILL.md
(no output)
$ git show 53d7019:SKILL.md | grep -c 'check_skill_evals_v2\|check_r69_routed_repairs_v2'
0
$ sed -n '168,173p' plans/round-71.md
`verify_skill_checklist.py --json` (SKILL.md ≤ 600 lines — two blank lines are consumed for the
two new registry rows), `verify_corpus_integrity.py`, `verify_corpus_independent.py --json`,
`check_gate_registry.py --rev <tip>` (53 of 53), `check_assertion_floors.py`, census `validate`
exit 0.
$ tail -1 .ufo/waves/round-72/receipts/base-battery.txt
SKILL.md lines: 600  bytes: 72688
```

The r71 plan promised the value at `plans/round-71.md:171` and stated the budget arithmetic at
`:169-170`; the rows were never added in any commit (`-S` search empty at every rev, including the
r71 closure tip `53d7019`), so `53 of 53` is a record-vs-tree stale premise, and the row add was
promised into a file already at its 600-line ceiling.

The promised **battery** was also not run at its own tip — the r71 report's battery is three gates,
not the plan's six:

```
$ grep -n 'verify_skill_checklist.py --json\|verify_corpus_integrity.py\|sources-census.sh validate\|git status --porcelain' .ufo/reports/round-71/kotoba.md
53:- `verify_skill_checklist.py --json`: **11/11 PASS** (SKILL.md 600/600 lines)
54:- `verify_corpus_integrity.py`: **9/9 pass** (baseline re-recorded at `eb394f5`/`53d7019`)
55:- `sources-census.sh validate`: exit 0 — receipt `census-after.txt`
56:- `git status --porcelain` (lane): clean at report time
```

Omitting `verify_corpus_independent.py`, `check_gate_registry.py`, `check_assertion_floors.py`.

## F3 — M125's mechanism is verified; the brief's placement of it is only half right (correction)

The stale arm and the erratum that invalidates it coexist in the same file, at the r71 tip and at the
base:

```
$ grep -n 'GOVERNANCE_ERRATA_HORIZON = \|junk-world/\|only LOG.md:2678 red' verifiers/verify_skill_checklist.py
400:GOVERNANCE_ERRATA_HORIZON = 2678
412:    # Round 71 (routed defect K69-11, round-70 closure): LOG.md:2678 records
2522:        rec("governance: live round-65 corrections land, only LOG.md:2678 red",
$ sed -n '1752,1753p' verifiers/verify_skill_checklist.py
def check_governance_citations(repo: Path, errata=GOVERNANCE_ERRATA,
                               horizon: int = GOVERNANCE_ERRATA_HORIZON,
$ git show 53d7019:verifiers/verify_skill_checklist.py | grep -n 'GOVERNANCE_ERRATA_HORIZON = \|only LOG.md:2678 red'
400:GOVERNANCE_ERRATA_HORIZON = 2678
2522:        rec("governance: live round-65 corrections land, only LOG.md:2678 red",
$ git diff --stat 53d7019 c69711ee08279609374d895bb0f3c8c18ccf15c9 -- verifiers/verify_skill_checklist.py
(no output)
```

Observed red: `FAIL checklist observed=1862 floor=1862 self_test_failures=1`
(`.ufo/waves/round-72/receipts/base-outputs/check_assertion_floors.out:5`).

**Correction to the brief:** "found only because the floors gate was not in the r71 tip battery" is
true of the r71 **report** (`:53-56` above) and false of the r71 **plan**, which lists
`check_assertion_floors.py` at `plans/round-71.md:172`. The skeleton states it that way (plan listed
it; report did not run it) — the mechanism is the same, the attribution differs.

## F4 — conflict: the round-72 plan's C3 sentence about the r71 report is unsupported by the bytes

`plans/round-72.md` § C3 states the r71 report "lists `Corpus gates … green`". I cannot find that
string:

```
$ grep -in 'corpus gates' .ufo/reports/round-71/kotoba.md
(no output, exit 1)
$ grep -in 'green' .ufo/reports/round-71/kotoba.md
(no output, exit 1)
```

What the report actually carries is the three-bullet battery at `:53-56` (F2/F3). The skeleton
therefore records the report's battery contents, not the plan's characterisation. Reported verbatim
for the canonical judge; I did not reinterpret the predicate (C3's predicate is unaffected — it
counts the six commands at `--rev`, not what r71 wrote).

Also conflicting: the plan's C2 says "four instruments are red on a host drift"; the base battery
lists five non-zero substrate instruments — `check_substrate_pins` 2, `verify_surfaces` 2,
`verify_harness_claims` 2, `check_opencode_repin` 1, `compare_harness_independent` 2
(`receipts/base-battery.txt`). The skeleton prints the five with their receipts and leaves
`<<reconcile at landing>>`.

## F5 — M126: the "14 rounds" is not re-derived here and stays a placeholder

The last freshness re-pin on the card is round 53:

```
$ grep -n 'freshness' SCORECARD.md | head -3
32:| freshness (advisory) | 8 | **round 53 (C1 — opencode 1.19.4 re-derived and re-pinned …
```

Round 72 minus round 53 is 19 rounds, not 14, and I found no committed freshness **receipt** after
round 53. The only committed runs of the pins instrument in `.ufo/waves` are round 47's
`round-47/before/check_substrate_pins.py.out` and this round's
`round-72/receipts/base-outputs/check_substrate_pins.out`; every `pins OK 3/3` hit in rounds 67–71 is
a copy of the r53 record or a seat quoting it:

```
$ grep -rl 'pins OK 3/3' .ufo/waves/ | sed 's|.ufo/waves/||' | cut -d/ -f1 | sort -u | tr '\n' ' '
round-51 round-52 round-53 round-54 round-67 round-68 round-69 round-70 round-71 round-72
$ grep -rl 'pins OK 3/3' .ufo/waves/round-6[7-9] .ufo/waves/round-7[0-2]
…round-67/controls/validate/SCORECARD.md …round-70/assimilation/validate/corpus/README.md …
round-70/w1/CritCalibration.md …round-71/controls/c1-junk-world/scorecard.md …
```

(validate mirrors and control worlds carrying the lane's own r53 text). I did not invent a count: the
skeleton writes the derived fact ("last re-pin round 53, `SCORECARD.md:32`") and a
`<<N — brief states 14>>` cell.

## F6 — id collision and guard proof re-derived

```
$ wc -l .ufo/waves/round-72/assimilation/{reg-ids,staged-ids,collisions}
 139 reg-ids
 188 staged-ids
  11 collisions
$ comm -12 <(sort reg-ids) <(sort staged-ids) | tr '\n' ' '
S203 S204 S205 S206 S207 S208 S209 S210 S211 S212 S213
$ grep -cE '^ {0,3}\| S234 \|' assimilation/guard-proof/SOURCES-with-indented-S234.md
1
$ grep -cE '^\| S234 \|' assimilation/guard-proof/SOURCES-with-indented-S234.md
0            (grep exit 1 — zero matches)
```

139 lane ids agrees with the base census (`receipts/census-before.txt`, `rows: 139`). The collision
set is exactly `collisions`; every colliding id is a lane row of rounds 69–71. **The theme's staged
ids do not collide** (S248, S254–S256, S261–S264 all sit above the lane ceiling S213), and
`CORPUS.md:89` ("the next unused; never reused") makes S214 the next lane id — the skeleton's
renumber table is by document with `<<S2__>>` cells.

Gap noted: `assimilation/guard-proof/` holds the fixture only — **no output file** for the two
patterns; the counts above are my own run and the skeleton says so.

## F7 — staged entry provenance gap (feeds C1's conjunct (c))

```
$ grep -n 'S255\|S256' context-rot-and-always-on-context.md skill-vs-always-on-boundary.md
context-rot-and-always-on-context.md:27:**And the specification's own budget lands in the same place.** The one-pager (S255)
context-rot-and-always-on-context.md:29:(~50-100 tokens per skill)", and the client-implementation guide (S256) puts the
$ grep -c '^source:' skill-vs-always-on-boundary.md context-rot-and-always-on-context.md
skill-vs-always-on-boundary.md:4
context-rot-and-always-on-context.md:2
```

The second entry's body cites S255 and S256 but its `source:` lines name only S254 and S248 — on
admission it needs a `source:` line per cited id, which is also C1's conjunct (c). Recorded in the
skeleton's Gate.

Related document fact: staged S256's page is the one the lane already holds —
`grep -nE '^\| S002 ' corpus/SOURCES.md` → `corpus/SOURCES.md:15` with URL
`https://agentskills.io/client-implementation/adding-skills-support` (the staged row cites the `.md`
form). Quarantine row S168 also names the same URL as staged S248
(`https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals`), so the S168 hand-check
and the S248 admission touch one document — recorded in the skeleton's quarantine table.

## F8 — QUALITY mapping for the three mistakes

| mistake | class | criterion that should have caught it | why |
|---|---|---|---|
| M124 | `stale-premise` (record-vs-tree) | **none → Q65 drafted** | Q19 (`QUALITY.md:30`) binds a carried **before**-value; `53 of 53` is a promised **after**-value, and nothing binds a plan's own battery or a row add against a line ceiling. Q65 = "a plan's no-harm battery is run at its own base before the plan freezes, and a promised row add is checked against the stated budget". |
| M125 | `reference-drift` | **Q50** (`QUALITY.md:61`) | the r71 report's tip battery (`:53-56`) states three gate results at tip `53d7019` with no committed receipt for the plan-listed floors gate, so the red had no tip receipt to contradict it. Q36 is adjacent but binds a *cited* receipt's revision, not an omitted gate. |
| M126 | `stale-premise` | **Q09** (`QUALITY.md:20`) | "A substrate rebuild makes freshness red until the extraction is re-derived and re-pinned; 'no rebaseline' is open debt, not a pass" — the exact carried debt. |

Q65 draft: `.ufo/waves/round-72/w1/build/ScribeLessonSkeleton/Q65-row.md`, with the checks it can be
tested by (`check_gate_registry --rev c69711e` → `51 of 53`, exit 1, re-run by me; the `-S` search
empty; `SKILL.md lines: 600  bytes: 72688`).

## F9 — considerthese item 3 is quoted from the operator file, not paraphrased

```
$ grep -n "never changes the checklist" considerthese/2026-10-25.md
21:3. **Route each knowledge entry's "what a skill author does" bullets into the audit checklist.** …
$ grep -o "A knowledge entry that never changes the checklist is depth the agent can't use." considerthese/2026-10-25.md | wc -w
14
```

Quote used in the skeleton: `"A knowledge entry that never changes the checklist is depth the agent
can't use."` (14 words, `considerthese/2026-10-25.md:21`, dropped bytes: the rest of the item).

## Out of scope / not done (by seat bounds)

- No committed lane file touched; no counter written (`verifiers/check_author_rules.py`,
  `check_substrate_repin_v2.py`, `check_tip_battery.py` do not exist yet —
  `ls verifiers/ | grep -E 'author_rules|substrate_repin|tip_battery'` → no output).
- No gate run except the one read-only re-run in F2; no sandbox, no git write, no jj command.
- No `/home/vgpnk/Projects/shokuknow` write; the staged package was read only.
- Lane worktree state observed, not touched: `git status --porcelain` lists only round-72 wave paths
  (`?? .ufo/waves/round-72/{snapshots,w1.ready,w1.ready.dispatched,w1/}`), which the L1 owns.
- Tooling: nothing installed or upgraded this round (no package manager run).
- `## Wave-1 findings` and a standalone `## considerthese` section (r70/r71 house form) are not in the
  skeleton because the brief fixes five sections; the considerthese result sits inside `## Gate` as
  the brief asks, and the L1 may hoist it.
