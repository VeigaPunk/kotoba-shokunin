# Checklist execution, round 15 — pre-registration (written before landing)

**Lane:** kotoba-shokunin. **Round:** 15. **Axis move:** `operability` (7.5, the
lowest row in `SCORECARD.md`, tied with `calibration` and `adjacency` at 7.5).

**Move-selection record.** The mission prompt says *pick the lowest-scoring axis*.
Round 13's L0 question (may a lane work an advisory axis as its lowest-axis move,
and D-78's `AXES.md`↔`MISSION.md` naming) is still unanswered, and this round
again works the lowest row rather than an owned one — recorded, not
re-litigated. `operability` is chosen over the two other 7.5 rows because it
carries a **named, pre-falsified, unlanded deliverable**: round 13's plan
(`SCORECARD.md` § planned, item 2) already wrote the falsifier for exactly this
move, and the `operability` row already names the residual — "`SKILL.md`
checklist boxes remain the only un-automated procedures (40 boxes)".

**Scope fence (stated before landing).** This move executes *one* checklist's
boxes on *one* file class (`SKILL.md`). It does **not** claim the other 26 boxes
are executed, and it does **not** get relabelled as a `coverage` gain: the
coverage row moves this round only as the round-14 measurement debt (§ Round-14
closure), never as a consequence of this move.

**Pre-state (commands to re-run, at `29c17be`, working tree clean):**

| Fact | Command | Value |
|---|---|---|
| boxes in file | `grep -c '^- \[ \]' SKILL.md` | 40 (14/9/9/8 by section) |
| boxes executed by a committed instrument | (no command existed) | **0** |
| instruments in `verifiers/` | `ls verifiers/*.py verifiers/*.sh \| wc -l` | 5 (4 py + 1 sh) |
| operability row | `SCORECARD.md` | 7.5 — was 7 |

## Claim under test (falsifiable)

> As of round 15, **seven** of the 40 `SKILL.md` checklist boxes are executed by
> a committed instrument (`verifiers/verify_skill_checklist.py`) instead of read
> by a human, **one** is delegated to an existing instrument by name, and the
> remaining **32** are mapped to `unexecuted:<reason>` — and every box in the
> file is mapped to exactly one of those three dispositions by
> `verifiers/checklist-baseline.json`, pinned with the box's text sha256 so that
> a reworded, added, or removed box FAILs the run.

Falsified by any of: a check that passes with the defect present; a box absent
from the map; a map entry with no live box; a reworded box that still passes; a
check whose `evaluated` count is 0 yet reports PASS.

## Properties

| # | Property | How it is falsified |
|---|---|---|
| P1 | Every executed box's rule is stated with its failure mode and its limits (rule table in this file) | a reviewer finds a rule whose stated limit is contradicted by its own fixture |
| P2 | Each check fails closed on a fixture carrying exactly that defect | per-check broken fixture + `--self-test` asserting exit code **and** failing check id |
| P3 | No vacuous PASS: every check reports `evaluated N`; `N == 0` is a FAIL | empty/clean fixture with zero subjects → FAIL, not PASS |
| P4 | The box map is two-way and hash-pinned | reworded box → FAIL naming the box id; extra map entry → FAIL |
| P5 | The instrument is hermetic and read-only over foreign repos | sentinel audit; fleet run touches sibling `SKILL.md` files with no write |
| P6 | A non-author re-derives the executed/unexecuted split from the file's box text and agrees | reviewer lane, disagreeing entry named rather than averaged |

## Outcome bands (pre-registered)

| Band | Condition | operability |
|---|---|---|
| full | P2–P4 all hold, `--self-test` green with ≥1 assertion per check, mutation lane finds no escape inside the seven executed checks, reviewer re-derivation agrees, fleet application lands | **8.5** (8 = independently re-measured; +0.5 = one of the two band-9 criteria — machine-checked) |
| partial | instrument green and self-tested, but ≥1 escape or ≥1 unresolved lane disagreement | 8.0 |
| no move | any check cannot fail, or the map is decorative (a new box passes unmapped) | 7.5 |
| regression | the instrument reports a defect on the live file that a reviewer shows is not a defect (false positive) without an adjudicated rule fix | 7.0 |

## Round-14 closure (recording debt, not a second move)

Round 14 landed the opencode-side machine check and the census row-column parity
(`29c17be`) but the round terminated before the score was recorded: `SCORECARD.md`
still reads `coverage … 8.0 … Last change 13`, and
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-14/kotoba.md` is a DRAFT carrying `[PENDING]` markers.
Round 14's own pre-registration bands were full ⇒ 8.5 / partial ⇒ 8.25 /
no-move ⇒ 8.0. Round 15 re-measures the landed artifacts against those bands and
records the result **attributed to round 14** in `SCORECARD.md`, with the
attribution defect (unscored landing) named in `LOG.md`. Corrections to the
round-14 report land as an erratum appended after its filed bytes (PROTOCOL.md:
a filed report is a record, never rewritten).

## L2 plan (≥8 lanes, one batched call; floor is `/home/vgpnk/projects/shokunin/MISSION.md` § L2)

Batch 1 — `R15Plan` (planner), `R15Connector` (connector) @m_lunamax;
`R15Populate`, `R15Exec` (executors), `R15Surfaces` (scout) @m_flash;
`R15Rules` (critic), `R15Witness` (labrat), `R15R14` (reviewer), `R15Safety`
(sentinel) @m_zfl. Batch 2 (post-build) — `R15Mutate` (mutation-tester),
`R15Review` (reviewer), `R15Agree` (labrat), `R15Dead` (simplifier), `R15Distill`
(distiller), `R15Critic` (critic) @m_zfl.

## Amendment A1 — box set and counts (appended before landing, `SKILL.md` 591 lines)

Appended rather than rewritten: the frozen bytes above stay, and this entry names
what they supersede.

1. **A box was inserted, not removed.** Building the executor exposed a hole in
   the checklist itself: no box required that the frontmatter *parses*, so a file
   with no frontmatter would have passed the name/literal/anti-trigger boxes
   vacuously. `SKILL.md` now carries it as trigger box 1. Counting command
   (unchanged form): `awk '/^## /{h=$0; if(!(h in s)){s[h]=1; o[++n]=h}}
   /^- \[ \]/{c[h]++} END{for(i=1;i<=n;i++) if(c(o[i])) printf …}'` — the
   landed form prints
   `## Trigger-fidelity checklist: 15; ## Agent-definition: 9; ## Dispatch-prompt: 9; ## Always-on: 8`.
2. **Superseded counts, stated plainly.** Against the frozen 40-box file, **six**
   boxes were executed (name, literal trigger, anti-trigger, commands, line
   budget, no-placeholder); the seventh execution is a box this round *added*.
   So the claim's "seven" is seven of the 41-box landed set, six of the frozen 40
   — the insert is an improvement to the checklist, not a way of reaching a
   number, and this line is here so a reader does not have to reconstruct that.
   The delegated and unexecuted counts follow the same shift: one delegated, 33
   unexecuted in the landed 41.
3. **Bounds.** `Trigger-fidelity checklist: 15` (was 14), total boxes 41 (was
   40), `SKILL.md` 675 → 591 lines (the moved sections are listed in
   `LOG.md` round-15; the ≤600 box previously FAILED on this file).

## Amendment A2 — two rules corrected by the blind witness (appended before landing)

The round's blind-witness lane (`R15Witness`, dispatched from the spec only, not
allowed to read the build) hand-derived verdicts for 4 SKILL.md files and returned
two findings that falsify rules as frozen above. Both are adopted here; P3 is
restated.

1. **`trigger.command_binary_resolves` scanned the wrong surface.** Fenced
   blocks only → the witness measured **0 fenced blocks** in 3 of its 4 files
   (kotoba@`63ceba7`, kagi, bailian-sandbox), i.e. the check would have reported
   `evaluated 0` on nearly every real skill file. The box's own text says "fenced
   block **or inline**". Rule now: scan fenced blocks (info string ∈ {empty,
   `bash`, `sh`, `shell`, `console`}) **and single-backtick inline spans**, taking
   an inline span as a command candidate only when its first token matches
   `^[a-z][a-z0-9_+-]*$` (no `.`, `/`, `:`, `-`-leading, or `<…>` anywhere in the
   span), which drops identifiers (`trigger.line_budget`), paths
   (`verifiers/verify_x.py`), frontmatter keys (`name:`), flags (`--max-lines`)
   and templates (`bl <cmd> --help`).
2. **The vacuity floor was too blunt.** P3 as written (`N == 0` is a FAIL) would
   have failed a clean file that simply names no commands. Restated: every check
   prints `evaluated N`; `N == 0` prints **`N/A` plus the reason** and is never a
   PASS; a run in which the executed checks produce no subject at all exits 1; and
   the fixture world — not the live file — is what proves extraction fires, one
   fixture per shape (fenced-only, inline-only, both).
3. **`trigger.no_placeholder` distance window removed.** The frozen rule excluded
   a marker only within 30 chars of a negation; the witness found the file's own
   box line (`- [ ] No \`TODO\`, placeholder sections, or "coming soon"`) puts
   `coming soon` 32 chars after `No` — a false positive on the lane's own text.
   Rule now: excluded when inside a backticked span, **or** when a negation token
   (`no`, `not`, `never`, `avoid`, `without`) appears earlier on the same line —
   order matters, so a stub line that says `TODO: no longer needed` is still caught.

Consequence for the fleet reading: FAILs produced by the extraction on *foreign*
files are hints, not verdicts, because the extractor cannot distinguish a
Hyprland config block from a shell block; the module docstring must say so, and
the lane report routes them rather than fixing them.

## Amendment A3 — the command extraction set is declared, not shape-guessed (before landing)

A2's inline rule (first token matches `^[a-z][a-z0-9_+-]*$`) was tested against the
lane's own file and produced **78 candidates, 56 unresolvable** — prose spans like
`` `description` ``, `` `name` ``, `` `commit` ``, `` `role` `` are bare lowercase
words, indistinguishable by shape from `` `ls` `` or `` `md5sum` ``. Shape cannot
separate a command from a noun here, so A2 item 1's filter is replaced:

**The instrument ships a declared command vocabulary**
(`verifiers/checklist-command-vocabulary.json`, or a `commands` block inside the
baseline): the heads it treats as commands when they head an inline span or a
fenced-block line — `python3, bash, sh, node, npm, git, sqlite3, grep, awk, sed,
find, ls, cat, wc, md5sum, sha256sum, strings, comm, diff, sort, uniq, jq, curl,
tar, systemctl, omp, opencode, bl, xargs`. A span is a subject when its head is in
that set, the span carries no `<…>` placeholder, and the head is not
flag/path/identifier-shaped. Fenced blocks stay as in A2 (info string ∈ {empty,
bash, sh, shell, console}). Every subject's head must resolve: absolute path
exists, `shutil.which`, or repo-relative path exists.

Limits this buys and what it costs, both stated in the module docstring: the set
is *declared and regenerable* (it is the vocabulary the round-15 census found
across this repo's fenced blocks plus the fleet's own tools), so a command outside
it is invisible to the check — that is the ceiling, named, not hidden. It buys
what shape-guessing cannot: no false positives from prose nouns, and a
falsifiable verdict for `` `bl` ``-class bins, which are absent on this host by
design and must therefore be declared in `metadata.requires` or checked by a
prerequisite step (which is exactly what the box demands).

Measured against the live file: `SKILL.md` carries **0 fenced blocks**; the
declared vocabulary yields ~10 inline subjects (`python3` ×4, `md5sum` ×3, `ls`,
`grep`, `strings` ×2, `git`), all resolvable on this host — so the check reports a
real `evaluated N > 0`, not a vacuous `N/A`.

## Amendment A4 — the anti-trigger vocabulary must read CJK (before landing)

The population lane (`R15Populate`) enumerated **138** `SKILL.md` files on this
host (`find -L ~/.agents/skills -maxdepth 2 -name SKILL.md` → 15;
`find -L ~/projects ~/Projects -maxdepth 8 -name SKILL.md -not -path
'*/node_modules/*' -not -path '*/.git/*'` → 123; the `-L` matters, 11 of 17
`.agents/skills` entries are symlinks and a plain `find` misses them) and applied
the seven-marker anti-trigger vocabulary to all of them: **135 of 138 FAIL**.

That number is not a fleet verdict, it is a rule defect: this host's skill
descriptions are bilingual and the markers actually in use are CJK —
bailian-gen `反触发：…`, bailian-cli `不要用于…`, bailian-sandbox `不用于…`
(the blind witness flagged this too). An English-only vocabulary reports a
non-defect as a defect, which the rubric grades as regression (band 7.0), not
improvement. The vocabulary therefore adds the observed CJK markers —
`反触发`, `不用于`, `不要用于`, `排除`, `勿用于` — and the module docstring states
that the list is the *observed* marker set, so a novel phrasing (any language)
can still pass unearned and an unlisted phrasing can still fail unearned. Both
directions of that limit are named in the check's detail line, not smoothed.

Same lane, two more numbers the round uses: `line_budget` FAILs 16 of 138 (kasegi
997, kumitate 652, kagi 618 — sibling repos, routed, not fixed; kotoba 591 now
passes) and `frontmatter_parses` FAILs exactly 2, both real files with no
frontmatter at all — which is what makes the byte-level fixture for that check a
faithful model rather than a constructor's invention.

## Landed results (appended after the build)

| Artifact | sha256 | Extent |
|---|---|---|
| `verifiers/verify_skill_checklist.py` | `f169f2479ca4a76df5eca4f900a77369ece3ed8a3521832a4edf01ef4f98272e` | 8 checks, exit 0/1/2/3, `--self-test` |
| `verifiers/checklist-baseline.json` | `6bccc6b2de9edaebb87031beb6138963c9f10720fde817fd6a0da32a6e9b7c26` | 41 boxes: 7 executed / 1 delegated / 33 unexecuted; schema `kotoba-checklist-v1` + a pinned `normalization` field |
| `verifiers/checklist-command-vocabulary.json` | `200f38dd0fdc27867e9dbdc29d96afb1847b41c0dff8fff542c622b47ccbf9cc` | 29 declared command heads, schema `kotoba-command-vocab-v1` |
| `verifiers/fixtures/checklist/` | — | 39 case dirs, one per defect class (`clean`, per-check broken copies, `anti-quoted-negation`, `command-wrapper-inner`, `command-heredoc-cd`, `command-fence-filter`, `commands-fenced-only`, `commands-both`, `map-box-reworded`, …) |

**Lane-run evidence (all commands re-run by L1 at the landed tree):**

| Run | Result |
|---|---|
| live, from the repo root | `exit 0`, 8 × PASS — `box_map evaluated 41 (7 executed/1 delegated/33 unexecuted)`; `line_budget evaluated 597 within budget 600 (from box at line 326)`; `command_binary_resolves evaluated 16 subjects / 261 segments`; `no_placeholder evaluated 548` |
| live, from `/tmp` | `exit 0` (cwd-independent) |
| `--self-test` | `0 failure(s) over 648 assertions`, exit 0 |
| `--json` | object with `checks`, `exit_code`, `pass`, `fail`, `na` |
| **red-before** — pre-state snapshot `git show 63ceba7:SKILL.md` placed in a directory named `kotoba-shokunin`, run with the landed map | `exit 1`, exactly two FAILs: `trigger.line_budget: evaluated 675 — 675 lines exceed budget 600 (from box at line 392)` and `checklist.box_map_complete` naming the unmatched box ids; the other six PASS |
| budget catch on a mid-round edit of this file | a 603-line intermediate state FAILed `trigger.line_budget` (603 > 600) until the file was trimmed — the check caught its own author |

**Fleet application (read-only, `--skill` per sibling, box-level checks; FAILs
are routed to the owning lane, never fixed here):**

| Lane | Result |
|---|---|
| kagi | `literal_trigger_string` FAIL, `anti_trigger_clause` FAIL, `line_budget` FAIL (653) |
| kake | `literal_trigger_string` FAIL, `anti_trigger_clause` FAIL |
| kasegi | `literal_trigger_string` FAIL, `anti_trigger_clause` FAIL, `line_budget` FAIL (997), `command_binary_resolves` FAIL (a diagram line inside an info-less fence read as a command) |
| kengaku | `literal_trigger_string` FAIL, `anti_trigger_clause` FAIL |
| kumitate | `literal_trigger_string` FAIL, `anti_trigger_clause` FAIL, `line_budget` FAIL (664) |

All five sibling descriptions fail the literal-trigger and anti-trigger boxes —
the same finding round 5 and the round-8 aggregator audit reached by hand, and the
round-8 rewrite set (`corpus/knowledge/sibling-description-rewrites-round8.md`) is
still unapplied. Counts for kagi/kumitate moved between this run and the
population lane's earlier one (618 → 653, 652 → 664), i.e. those lanes are editing
live; the check measures bytes, not a snapshot.

## Ceilings carried (what this round does not claim)

- **33 of 41 boxes are still read by a human.** They are mapped with reasons, not
  executed. The reason text for the three non-SKILL checklists names the surface
  and its population (`opencode/agents/*.md` 53 files over 3 roots, `.ufo/prompts`
  89 canonical + 3 fixture files, AGENTS.md-class 7 files).
- **Two of the eight checks are shape or vocabulary tests** (`literal_trigger_string`,
  `anti_trigger_clause`), so a novel phrasing can fail unearned and a quoted
  non-trigger can pass unearned; both say so in their detail lines.
- **The command check sees its declared vocabulary and info-less/shell fenced
  blocks only.** kasegi's FAIL above is the live example of the false-positive
  edge: an info-less fence holding a table is read as commands. Foreign-file FAILs
  are hints; the owning lane reads them, not this instrument.
- **`frontmatter_parses` is a structural parse, not YAML-semantic validation**
  (stdlib only): gross malformation fails, subtle YAML pathology does not.
- **The box map is pinned to normalization, not to intent.** A reworded box FAILs;
  so does an editor's re-wrap — the difference is visible in the detail line and
  is settled by regenerating the map, which is exactly the drift signal wanted.
- **Nothing here proves a SKILL.md whose boxes are unexecuted is weak.** The map
  records the disposition; the judgement stays with a reader.
- **Five extraction escapes, measured not assumed** (mutation lane, 45 mutations):
  a nonexistent command named inline outside the declared vocabulary; one hidden in
  a heredoc body; `echo <nonexistent>` in a shell fence (only segment heads
  resolve — flags and arguments are unchecked); whole-box reordering within a
  section (the map is a text multiset and deliberately order-blind); and
  `delegated:<path>` pointing at a file that exists but is no instrument. Each is
  named here so it cannot be read as a silent hole.

## Amendment A5 — verification verdicts, the five escapes, and the band (after the build)

Fifteen lanes ran (9 + 6, one batched call each). The four that changed the
artifact:

| Lane | Finding that moved the artifact |
|---|---|
| `R15Witness` (blind, spec-only) | fenced-only command extraction would be empty on 3 of its 4 files → A2; the 30-char negation window false-positived on the file's own box → A2.3 |
| `R15Populate` | 138 SKILL.md files on this host; the English-only anti-trigger vocabulary failed 135 of them → A4 (CJK markers) |
| `R15Rules` (critic) | 6 of 8 rules broken with executed counterexamples: multiset parity, pinned normalization, registry-bound `executed:` ids, frontmatter block parse, abspath'd directory, box-bound budget, word-bounded negation, wrapper unwrap — all repaired before landing |
| `R15Agree` | **false positive, adjudicated WITNESS-RIGHT**: the frontmatter parser rejected valid nested `metadata:` blocks (37/138 fleet files) → repaired in-round, fixtures `fm-nested-metadata` / `fm-stray-indent` added |

`R15Review` re-derived the map independently (41 boxes, exact multiset match) and
named five discrepancies, all closed: two stale/incorrect box annotations, a
stub that said "Eighteen rows" for a 20-row table, and two builder-number drifts
explained by L1's post-build edits. `R15Dead` removed five dead-weight items
(`xargs` unreachable in the vocabulary, an unconsulted fixture vocabulary file, a
vacuous conditional, an unread schema field, a speculative empty-scalar).
`R15Critic` found two live escapes — a `- [x]` marker toggle and a
`delegated:` target that does not exist — and **both were closed in-round** with
fixtures `marker-checked`, `marker-near-miss`, `map-dead-delegated`; the mutation
lane then re-verified them as closed and measured the new
`annotation↔disposition` binding.

**The mutation lane's five escapes, named.** 45 mutations, 35 caught, 5 escaped:

| Escape | Status |
|---|---|
| `M22` a nonexistent command named inline outside the declared vocabulary | ceiling declared in A3 and § Ceilings |
| `M23` a nonexistent command hidden in a heredoc **body** | ceiling: heredoc bodies are stdin data, skipped by construction (A2/A3) |
| `M35` `echo <nonexistent>` inside a shell fence — only segment *heads* resolve | ceiling: flags and arguments are not covered (stated in the box annotation) |
| `M38` reordering whole boxes within one section | ceiling: the map pins box text as a multiset, deliberately order-blind |
| `M40` `delegated:SKILL.md` — delegation checks existence, not instrument-ness | **new ceiling**, surfaced by this lane; recorded, not hidden |

**Band decision, taken against the pre-registration rather than around it.** The
pre-registered full band required "mutation lane finds no escape inside the seven
executed checks". Five escapes exist, so that condition **fails as written** and
the band is the pre-registered **partial: operability 7.5 → 8.0**. The other full
conditions do hold (P2–P4 verified by two lanes, `--self-test` green with 772
assertions and ≥1 per check, reviewer re-derivation agrees, fleet application
landed) — which is why the move counts at all — but the half-point stays
withheld. What earns 8.5 next round, stated now: close `M35` (resolve arguments
that look like paths) and `M40` (require the delegated target to be a script with
a check contract), or re-pre-register the condition as "no escape outside the
documented ceilings" and defend that wording before the build.
