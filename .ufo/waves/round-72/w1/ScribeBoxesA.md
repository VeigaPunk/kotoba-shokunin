# ScribeBoxesA — A1/A2 author-facing checklist boxes (round 72, wave 1, build)

**Verdict.** Both boxes are drafted, both satisfy the C1 predicate's rule-(a) shape on a scratch copy
of `SKILL.md` (exactly one box per rule inside `## Trigger-fidelity checklist`, frozen token set as
whole words, tail ending in the frozen `(sourced: …; entry: …)` form), and both score 0 at the base —
the do-nothing control holds for these two rules. They **cannot be landed as they stand**: `SKILL.md`
is 600 of 600 lines at the base and each box is 4 lines, so a 2-box insert reads
`608 lines exceed budget 600`. Landing also requires three companion edits I did not make (L1 owns
them): two `verifiers/checklist-baseline.json` entries (hashes below), `box_total` 41 → 43, and the
section's box-count sentence.

Lane state when I read: `git rev-parse HEAD` → `e61fd294c2e1cdd16d594b57b310254183ace1e7` (the wave-1
spec commit); `git diff --stat c69711e HEAD` → 24 files, 23 under `.ufo/waves/round-72/` plus
`plans/round-72.md` (`git diff --name-only c69711e HEAD | grep -v '^\.ufo/waves/round-72/'` → that one
path only), so no `SKILL.md`, `corpus/`, `verifiers/` or `opencode/` content differs from the base.
`wc -l SKILL.md` → `600`, `wc -c SKILL.md` → `72688`.

## The two boxes (verbatim; nothing else proposed for SKILL.md)

```markdown
- [ ] `name` is unique among the skills likely installed alongside it: a
      same-name collision resolves by precedence order on four of the five
      cited clients, not by merging; the orders differ per client. (sourced: S203,
      S204, S205, S206, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)
- [ ] Every instruction the `body` gives names the `authority` level it
      speaks at and asserts no higher one: a skill body is text a model may
      obey, not a privileged level, and no fixed ladder settles conflicts.
      (sourced: S123, S129; entry: corpus/knowledge/instruction-authority-ladder-round67.md)
```

Insertion point used in the scratch proof: after `SKILL.md:326` (the last continuation line of the
`trigger.no_placeholder` box), before the blank line 327 and `## Agent-definition fidelity checklist`
at 328. Continuation indent is 6 spaces, matching every live box; no blank line inside a box (a blank
line ends a box's continuation in `extract_boxes`).

## F1 — Section boundary and existing box style (read, not assumed)

```
$ sed -n '253,266p' SKILL.md | cat -A | cut -c1-110
## Trigger-fidelity checklist$
$
Run before shipping any SKILL.md. Every item is checkable by reading the file M-bM-^@M-^T$
no runtime needed. (For AGENTS.md / dispatch prompts, use the per-surface rows$
in "Instruction surfaces" instead M-bM-^@M-^T this checklist assumes a routed file.)$
$
Eight of the fifteen boxes are **executed, not read** M-bM-^@M-^T marked$
`(executed: <check-id>)`: `python3 verifiers/verify_skill_checklist.py` runs them$
...
- [ ] Frontmatter parses: the file opens with `---`, closes it, and carries a$
```
Section runs 253–327; `## Agent-definition fidelity checklist` starts at 328. Live box count in the
section at the base: 15 (`grep -n '^- \[ \]' SKILL.md` → 266,270,272,274,278,283,284,291,293,298,302,311,318,320,323).
Quote (SKILL.md:259, 11 words, nothing dropped): `Eight of the fifteen boxes are **executed, not read** — marked`.
Quote (SKILL.md:255–256, 11 words; the line break between `file —` and `no runtime` replaced by one
space): `Every item is checkable by reading the file — no runtime needed.`

## F2 — A1 predicate evidence (rule (a), token set, tail, hash, widths)

Extraction was done with the lane's own extractor, not a re-implementation:

```
$ python3 -c "<import verifiers/verify_skill_checklist.py via importlib; extract_boxes(scratch lines)>"
boxes total 43 in section 17 near_misses 0
line 327 sha 4e8201bf3798fcefcf1d755cd2971cfbd52cbeb591844ceff16e2a0d20095238
  text: `name` is unique among the skills likely installed alongside it: a same-name collision
        resolves by precedence order on four of the five cited clients, not by merging; the orders
        differ per client. (sourced: S203, S204, S205, S206, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)
A1 token_hits 1 with_tail 1
   cited ['S203','S204','S205','S206','S207'] equals expected True sha 4e8201bf3798…
```
Line widths of the four lines: `72, 74, 82, 87` — every line ≤96, max 87 (cap 96).

Content check against the entry's own rows (quotes are the entry's located quotes, re-read, not
paraphrased):

- entry:30 — `- **Four of the five cited routes resolve a collision by order, not by merging.** One body wins and`
  (14-word quote, nothing dropped): `Four of the five cited routes resolve a collision by order, not by merging.`
  This is why the box says "on four of the five cited clients, not by merging" rather than asserting
  order for all five — opencode is the fifth and states no order.
- entry:38 — `- **The portable rule is therefore uniqueness.**` (6-word quote): `The portable rule is therefore uniqueness.`
  This is the rule's action clause (`name` is unique).
- The "orders differ per client" clause is the entry's § The per-client map table (Roo Code scope
  order; Amp an eleven-source list whose order inverts by tree; Deep Code numbered root priority;
  Junie the project/user pair only; opencode none).

## F3 — A2 predicate evidence

```
line 331 sha 8ec8b2fd1a36c3f766091c34f9e42febb364327040c3141ac1aea4b6b31bd044
  text: Every instruction the `body` gives names the `authority` level it speaks at and asserts no
        higher one: a skill body is text a model may obey, not a privileged level, and no fixed
        ladder settles conflicts. (sourced: S123, S129; entry: corpus/knowledge/instruction-authority-ladder-round67.md)
A2 token_hits 1 with_tail 1
   cited ['S123','S129'] equals expected True sha 8ec8b2fd1a36…
```
Line widths: `71, 75, 74, 92` — all ≤96, max 92.

Content check (entry quotes re-read from bytes):

- entry:25 — `**Why it matters to skill craft.** A `SKILL.md` body is not a privileged instruction; it is text`
  (9-word quote): `A `SKILL.md` body is not a privileged instruction` — grounds "a skill body is text a
  model may obey, not a privileged level".
- entry:42–43 — line 42 ends `…must` and line 43 begins `name the authority level it speaks at.`; the
  two lines joined with one space (dropped bytes: the line break), 20-word quote:
  `Any future claim of the form "a skill body may instruct X" must name the authority level it speaks at.`
  This is the rule's action clause.
- S129's contribution ("no fixed ladder settles conflicts") is the entry's ManyIH paragraph: the fixed
  paradigm "assumes a fixed, small set of privilege levels (typically fewer than five)".

## F4 — Observable test per box, and the baseline classification

**A1 test (file comparison over the install set — two commands, both read-only).**
`SKILL.md:2` carries `name: kotoba-shokunin`. The test compares that value with every skill name the
clients actually load on this host (`~/.agents/skills`, `~/.claude/skills` — the two roots that exist):

```
$ grep -rh '^name:' --include=SKILL.md /home/vgpnk/.agents/skills /home/vgpnk/.claude/skills | sort | uniq -d | wc -l
0
$ grep -rh '^name:' --include=SKILL.md /home/vgpnk/.agents/skills /home/vgpnk/.claude/skills | wc -l
81
$ grep -rh '^name:' --include=SKILL.md /home/vgpnk/.agents/skills /home/vgpnk/.claude/skills | grep -x 'name: kotoba-shokunin'; echo "MATCH_EXIT=$?"
MATCH_EXIT=1
```
Empty `uniq -d` and exit 1 on the exact-name lookup = no collision today. A non-empty `uniq -d` line,
or exit 0 on the `grep -x`, is the failure.

**A2 test (grep over this file).** Every instruction block must name the level it speaks at, and no
line may assert a higher one:

```
$ grep -ncE '\b(authority|level)\b' SKILL.md
4
$ grep -nEi 'ignore (all|any|the) ' SKILL.md
(no output)
```
Failure = zero level-token hits, or any hit of the higher-authority assertion vocabulary. Limit, named:
this is a vocabulary test on two patterns, not a per-sentence ranking (the baseline reason says so).

**Baseline classification (verbatim strings for the L1 to paste, `unexecuted:` form only — no check id
in `verify_skill_checklist.py` evaluates either rule):**

- A1, `box_id: trigger.16`, `text_sha256: 4e8201bf3798fcefcf1d755cd2971cfbd52cbeb591844ceff16e2a0d20095238`
  `unexecuted:name uniqueness depends on the skills installed beside this one, not on this file's text; the file-side proxy is a grep of the frontmatter name against sibling names, which the gate has no install set for`
- A2, `box_id: trigger.17`, `text_sha256: 8ec8b2fd1a36c3f766091c34f9e42febb364327040c3141ac1aea4b6b31bd044`
  `unexecuted:whether every body instruction names its authority level and asserts no higher one is a reading judgement over prose; no check id here segments instructions or ranks levels (verifiers/check_instruction_authority.py grounds the entry, not the body)`

A2 is deliberately **not** `delegated:verifiers/check_instruction_authority.py`: that instrument
(`verifiers/check_instruction_authority.py:5-30`) checks the *entry* is grounded (source lines, row
status, quotes, README index) and says nothing about the skill body's instructions.

## F5 — Map work the landing requires (measured, not inferred)

Running the lane's gate on the scratch copy with the **live** map:

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --skill /tmp/k72w1-ScribeBoxesA.brOS/kotoba-shokunin/SKILL.md --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --map verifiers/checklist-baseline.json
FAIL checklist.box_map_complete: evaluated 43 — unmapped box at line 327 (section 'Trigger-fidelity checklist', sha256 4e8201bf3798…); unmapped box at line 331 (section 'Trigger-fidelity checklist', sha256 8ec8b2fd1a36…)
FAIL trigger.line_budget: evaluated 608 — 608 lines exceed budget 600 (from box at line 320)
RC 1
```
With a scratch map carrying the two entries above, the unmapped-box failure disappears (the only
remaining `box_map_complete` text is the delegated-target probe failing against a `/tmp` base —
`map entry dispatch.04 delegates to a target that does not exist` — an artefact of the scratch root,
not of my entries; the live run proves the real base is green: `PASS checklist.box_map_complete:
evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)`, `REAL EXIT=0`).

`box_total` is a floor with a hard error below the entry count (`verify_skill_checklist.py:541-550`:
`box map %s: box_total %d is below the declared entry count %d` → `MapError`, exit 3), so **41 must
become 43**. The executed/delegated counts do not change (both new boxes are `unexecuted:`), but the
section sentence `Eight of the fifteen boxes …` (SKILL.md:259) must read `seventeen` once both land —
that is the only in-file count statement: `grep -rn "fifteen boxes" --include=*.md .` returns
SKILL.md:259 plus four frozen copies under `.ufo/` (`.ufo/round-33/SKILL.md:183`,
`.ufo/waves/round-67/controls/validate/SKILL.md:259`,
`.ufo/waves/round-68/assimilation/validate/SKILL.md:258`, and a round-27 scout note), which are
scratch/control snapshots, not the live file.

Section-scoped counters are unaffected: `verifiers/check_agentdef_boxes.py:17` counts only boxes whose
`section` is `Agent-definition fidelity checklist`; `verifiers/check_alwayson_boxes.py` the same for
its own section.

## F6 — Line budget: 8 lines must be freed, or use the 3-line variants

`SKILL.md` is exactly at the bound the file states (`File ≤ 600 lines`, SKILL.md:320) and the gate
reads the box's own number (`trigger.line_budget: evaluated 608 — 608 lines exceed budget 600`). Two
4-line boxes cost 8 lines. If the L1 cannot free 8, these 3-line variants pass the same predicate
(same extractor, same token/tail regex) and cost 6:

```markdown
- [ ] `name` is unique among the skills likely installed alongside it: a
      same-name collision resolves by precedence order, never by merging.
      (sourced: S203, S204, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)
- [ ] Every instruction the `body` gives names the `authority` level it
      speaks at and asserts no higher one: a body is text a model may obey.
      (sourced: S123, S129; entry: corpus/knowledge/instruction-authority-ladder-round67.md)
```
Measured: A1-3 `lens [72,73,91] tokens True tail True cited ['S203','S204','S207']`
sha `b0dcd7edfe3a437177c3f2eb5727fae4e1fe38bca19b222170bdd3cd79443088`; A2-3 `lens [71,75,92]
tokens True tail True cited ['S123','S129']` sha `d4084372dcc3fe4940b490e292a5d2c4cdd6d0e80680a3d011889327d03e6704`.
They are shallower (A1 drops two of the five order-clients; A2 drops "not a privileged level, and no
fixed ladder settles conflicts"), so the 4-line pair is the recommendation and the 3-line pair is the
fallback if the budget cannot be freed. Do not mix: the hashes above are per-variant.

## F7 — Rules (b) and (c) re-checked row by row (not taken from the plan)

```
$ python3 -c "<split each registry row on '|' for S203..S207, S123, S129>"
S123 cells= 11  status= mined | tier= A | opened= 2026-10-24 | recheck= 90d
  used-by= corpus/knowledge/instruction-authority-ladder-round67.md, corpus/lessons/round-67.md
S129 cells= 11  status= mined | tier= A | opened= 2026-10-24 | recheck= 90d
  used-by= corpus/knowledge/instruction-authority-ladder-round67.md, corpus/lessons/round-67.md
S203..S207 cells= 11 each  status= mined | tier= A | opened= 2026-10-25 | recheck= 90d
  used-by= corpus/knowledge/skill-name-precedence-round69.md
```
Every cited id is an 11-cell row, `mined`, tier `A`, and its `used-by` cell lists exactly the entry the
tail names. Entry provenance trio at the measured bytes:

```
$ sed -n '1,7p' corpus/knowledge/skill-name-precedence-round69.md
source: S203 … / source: S204 … / source: S205 … / source: S206 … / source: S207 …
verified-at: 2026-10-25
recheck: 90d — re-fetch all five pages …
$ sed -n '1,7p' corpus/knowledge/instruction-authority-ladder-round67.md
source: S123 … / source: S124 … / source: S129 …
verified-at: 2026-10-24
recheck: 90d — …
$ git diff --stat c69711e -- corpus/knowledge/skill-name-precedence-round69.md corpus/knowledge/instruction-authority-ladder-round67.md
(no output)
```
So the two entries are byte-identical at base `c69711e` and at HEAD. Every id my tails cite is on its
entry's own `source:` line (A1: all five; A2: S123 and S129 — S124 is cited by the entry but not by
the box, which rule (a) permits).

## F8 — Controls I ran against my own reading of the predicate

Scratch worlds built by inserting text into a copy of the live `SKILL.md`, then extracting with the
lane's `extract_boxes` (HTML comments stripped first, as predicate (a) says "HTML comments and fenced
blocks removed"):

| world | A1 hits |
|---|---|
| base, unmodified | 0 |
| boxes inserted after line 326 (the draft) | 1 |
| same box placed after `## Agent-definition fidelity checklist` (outside the section) | 0 |
| token-stuffed box, no tail (`- [ ] `name` `unique` `precedence``) | 0 |
| box wrapped in `<!-- … -->` (comments stripped) | 0 |
| box wrapped in `<!-- … -->` **without** stripping | 1 |

Base A2 hits: 0. The last row is a note for whoever writes `check_author_rules.py`:
`verify_skill_checklist.py`'s `extract_boxes` does not strip HTML comments, so a comment-hidden box is
a *live* box to the checklist gate and a *dead* one to a counter that follows predicate (a) — the C1
counter must do its own stripping, and the two instruments will disagree by design on that world.

## F9 — Consistency observations routed to the L1 (not defects I may fix)

1. **Section preamble vs A1's test surface.** SKILL.md:255–256 says every item is "checkable by reading
   the file — no runtime needed"; A1's test reads *sibling* files (the install set), not this file
   alone. Either the preamble becomes "reading the file and the skills installed beside it", or A1 is
   scoped to "unique among the skills this repo's own catalogue names". I did not choose; the box text
   is the plan's rule.
2. **`corpus/knowledge/checklist-execution-round15.md:213`** pins the map's old sha
   (`6bccc6b2…`) and "41 boxes: 7 executed / 1 delegated / 33 unexecuted". It is a round-15 record, and
   no gate reads that sha (`grep -rln 6bccc6b2 verifiers/` → no output), so it needs no edit; named
   here only so a wave-2 reader does not mistake it for a live pin.
3. `checklist-execution-round15.md:248` and `:286` repeat the 41-box figure in the same historical
   register.

## Out of scope / not done

- A3 (install-path trust, S198–S202/S208) and A4 (rung, `resident-index-and-rungs-round72.md`): other
  seats' rules; no draft here.
- No edit to `SKILL.md`, `verifiers/checklist-baseline.json`, any counter, `corpus/`, `plans/`,
  `LOG.md`, `SCORECARD.md`; no git write; no jj call.
- No tool installed or upgraded (nothing needed; the two greps and the lane's own Python gate covered
  every check).
- Scratch world `/tmp/k72w1-ScribeBoxesA.brOS` used for the inserts and the gate runs, then deleted.

## Artifacts

- This report: `.ufo/waves/round-72/w1/ScribeBoxesA.md`
- No deliverable file under `.ufo/waves/round-72/w1/build/ScribeBoxesA/` — the deliverable is the
  fenced block above plus the two hashes and disposition strings in F4.
