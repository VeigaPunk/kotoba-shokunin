# ScribeQ60 — QUALITY.md Q60 draft (round 64, wave 1)

Seat: `kotoba-r64.ScribeQ60` (scribe, leaf; no subagent dispatch). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base tip `c04fffbe`
(`git log -1` → `c04fffbeafcaf810897258d56f99cca736ed3a91 round-64: freeze plan — …`;
the dispatch's "078eec4" is the plan's *measurement* base, one commit earlier than the
freeze commit — both names are in play, so every command below prints its rev).
Mode: read-only outside this file. No installs, no git/jj writes, no product edits.

Axes this seat works: **calibration** (consistency sub-axis) — the row is a bar, so
what it measures and what it must not over-flag is the whole deliverable.

---

## D1 — the Q60 row (exact bytes; single table row, 5 cells / 6 pipes)

Insertion: **append after line 74 of `corpus/QUALITY.md`** (checked:
`git show HEAD:corpus/QUALITY.md | wc -l` → `74`; line 74 is the Q59 row, the file's
last line). Append-only: no existing row is touched, and Q60 carries `supersedes: —`
because it *extends* Q03 and Q58 without replacing either.

```markdown
| Q60 | An artifact cited with a revision must exist at that revision: a receipt or control run against a base B but committed later is cited by its committing rev plus the pinned base B ("committed at <rev>, run against base <rev>"), never as "<path> @ B" — citing committed paperwork at a revision that does not contain it is the M95 class. The check is `git cat-file -e <rev>:<path>`, which exits 128 (nonzero) for a path the revision does not carry; the rule binds the path-claim form only — an output or exit code recorded as "run against base B", with the receipt named bare beside it, is the legitimate pin and is not a violation. Extends Q03 (a record names the commit holding the bytes it describes) and Q58 (a routed defect closes on a counter, not prose); their committed cells are never rewritten. Fix shown able to fail: `git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` exits 128 while the same path at `8c4cefa` exits 0. | artifact citations in lane paperwork (reports, LOG.md, SCORECARD.md, corpus/lessons, receipt headers) and their routed repairs | M95 + M96 — `corpus/lessons/round-63.md` § Mistakes and `corpus/lessons/round-64.md` § Mistakes: the r63 verifier spot-check's defect 2 (`corpus/lessons/round-63-verifier-spotcheck.md:168-173`) routes the r63 report's Before→after lines (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md:31-32`), which cite both controls `@ 35d44b4b` while `C1-do-nothing-v31.txt` was added at `8c4cefa` and `C2-before-r62tip.txt` at `cbbee56` (`git log --diff-filter=A`; each control's bytes name base `35d44b4b` — C1 `at: 35d44b4b4dcd…`, C2 `not a tracked blob at 35d44b4b4dcd…` — and `verifiers/check_r63_routed_repairs.py:77` pins `BASE_REV_LITERAL`). Census: ScoutReceiptSweep `<PENDING>`. Executable guard: `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>`, check 2 `control-revs-named`. | — |
```

Pipe audit of the block above: 6 `|` characters = id, criterion, applies-to, grounded-in
(= the assignment's "Captured-by: M95/M96" — `corpus/QUALITY.md` has **no** captured-by
column; its header is `| id | criterion | applies to | grounded in | supersedes |`, so
M95/M96 land in `grounded in`, matching Q58/Q59's practice of merging evidence into that
cell).

### D1b — compact variant (same rule, short cells), if table width matters

```markdown
| Q60 | An artifact cited with a revision must exist at that revision; a receipt or control run against base B but committed later is cited "committed at <rev>, run against base <rev>", never "<path> @ B" (the M95 class). The check is `git cat-file -e <rev>:<path>` (exit 128 when absent); it binds the path-claim form, not an "output run against base B" pin. Extends Q03 and Q58. | artifact citations in lane paperwork; routed citation repairs | M95, M96; r63 spot-check defect 2 (`corpus/lessons/round-63-verifier-spotcheck.md:168-173`; controls added at `8c4cefa` / `cbbee56`, base `35d44b4b`); census ScoutReceiptSweep `<PENDING>`; guard `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>` check 2. | — |
```

Ship **D1**, not D1b, unless the L1 has a width budget: the assignment's frozen wording is
the criterion clause and D1 keeps it verbatim, including both citation forms and the
"never as `<path> @ B`" prohibition.

---

## D2 — two-line summary for the round-64 lesson's QUALITY pointer

```markdown
QUALITY gained **Q60** (cite-by-existing-revision): an artifact cited with a revision must exist at that revision — a receipt or control run against base B but committed later is cited "committed at <rev>, run against base <rev>", never "<path> @ B" (the M95 class); the check is `git cat-file -e <rev>:<path>`, which exits 128 for a path the revision does not carry, and it binds the path-claim form only, never an "output run against base B" pin.
Q60's guard is C2's check 2 `control-revs-named` (`python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>`): 0 of 4 at base `078eec4` → 4 of 4 at the round-64 tip (declared in `plans/round-64.md:112-121`), and its census over LOG.md / SCORECARD.md / `corpus/lessons/round-6*.md` is ScoutReceiptSweep's `<PENDING>`.
```

Both lines are prose-only additions to the round-64 lesson; nothing here rewrites a
committed lesson (Q59 discipline).

---

## Evidence (commands run this seat; outputs pasted verbatim)

E1 — the two controls are absent at the rev the r63 report cites, present at the commits
that add them (`git cat-file -e`; note **exit 128**, not 1):

```
$ for rev in 35d44b4b 8c4cefa cbbee56; do for f in …/C1-do-nothing-v31.txt …/C2-before-r62tip.txt; do
    out=$(git cat-file -e "$rev:$f" 2>&1); rc=$?; echo "git cat-file -e $rev:$(basename $f) => exit $rc${out:+  [$out]}"; done; done
git cat-file -e 35d44b4b:C1-do-nothing-v31.txt  => exit 128 [fatal: path '.ufo/waves/round-63/controls/C1-do-nothing-v31.txt' exists on disk, but not in '35d44b4b']
git cat-file -e 35d44b4b:C2-before-r62tip.txt  => exit 128 [fatal: path '.ufo/waves/round-63/controls/C2-before-r62tip.txt' exists on disk, but not in '35d44b4b']
git cat-file -e 8c4cefa:C1-do-nothing-v31.txt  => exit 0
git cat-file -e 8c4cefa:C2-before-r62tip.txt   => exit 128 [fatal: … not in '8c4cefa']
git cat-file -e cbbee56:C1-do-nothing-v31.txt  => exit 0
git cat-file -e cbbee56:C2-before-r62tip.txt   => exit 0
```

E2 — committing revs (`git log --diff-filter=A --format='%h %ci %s' -1 -- <path>`):

```
8c4cefa 2026-10-23 20:00:56 -0300  .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
cbbee56 2026-10-23 22:47:45 -0300  .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56 2026-10-23 22:47:45 -0300  .ufo/waves/round-63/receipts/C1-g9-measure.txt
2ba4547 2026-10-24 00:04:31 -0300  .ufo/waves/round-63/receipts/C2-successor-measure.txt
```

E3 — each control pins base `35d44b4b` internally (`git show <add-rev>:<path>`):

```
C1 line 2: at: 35d44b4b4dcdda234b5dbff7af37e432fec55f05
C2 line 1: FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
verifiers/check_r63_routed_repairs.py:77: BASE_REV_LITERAL = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
```

E4 — the routed defect, verbatim (`corpus/lessons/round-63-verifier-spotcheck.md:168-173`):
"**Report citation imprecision:** the Before→after section cites the two controls "@
`35d44b4b`", but `C1-do-nothing-v31.txt` was committed at `8c4cefa` and
`C2-before-r62tip.txt` at `cbbee56` (each pins base `35d44b4b` internally). The cited rev
does not contain the files — the M95 citation class, in the report itself. Cite the
committing rev plus the pinned base."

E5 — the defective sentences themselves (fleet tree, read-only; lane cannot edit them):

```
/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md:31  … (v31 control, `controls/C1-do-nothing-v31.txt` @ `35d44b4b`). After: …
/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md:32  … exit 1 @ `35d44b4b` (`controls/C2-before-r62tip.txt`; hardened re-run `receipts/C2-before-rerun.txt` — identical `0 of 5`) …
```

E6 — the executable guard does **not** exist at base (forward dependency):

```
$ ls -la verifiers/check_r64_routed_repairs.py
ls: cannot access 'verifiers/check_r64_routed_repairs.py': No such file or directory   (exit 2)
```

E7 — row shape audit at HEAD (why Q60 must be 5 cells): `git show HEAD:corpus/QUALITY.md |
awk 'NR==70{…gsub(/\|/,"|")}'` → `Q58 pipes=6`, `Q59 pipes=3`. Header row: `| id |
criterion | applies to | grounded in | supersedes |`. Q59 is **malformed at HEAD** (3
pipes = id + one merged cell; no applies-to / grounded-in / supersedes). Q60 follows Q58's
shape, not Q59's — see F4.

E8 — this seat's own citation census (fallback only, **not** the ScoutReceiptSweep count).
Script `/tmp/q60_census3.py` / `/tmp/q60_census4.py`; scope = `LOG.md`, `SCORECARD.md`,
`corpus/lessons/round-6*.md` (7 files), read from `HEAD`:

```
exact form  `<path>` (@|at) `<rev>`             : tested=4  EXIST=4  ABSENT=0
reversed form  @ `<rev>` ( `<path>` )           : tested=24 EXIST=0  ABSENT=24
same-line cross-product (rev × path, unbounded): pairs=3577 ABSENT=2556   ← noise, discarded
```

Reading: both naive grammars misfire in opposite directions, so **the census number is a
judgement task, not a regex count** (F5). Do not publish either of my numbers as the census.

---

## Findings (each names the claim it supports or falsifies)

**F1 — `<PENDING>` is a genuine external dependency.** `ScoutReceiptSweep` has published no
report at base: `.ufo/waves/round-64/w1/` contains only `swarm-registry.json` (`ls -la`), and
the registry entry is `{"kind":"spawn","agentId":"kotoba-r64.ScoutReceiptSweep","role":"scout"}`.
The row ships with the literal `ScoutReceiptSweep `<PENDING>`` slot; the L1 substitutes one
token when the scout's count lands (`CONTRACT: n of m attribution-form citations name a rev
that does not carry the path; command: …`). Supports: the assignment's own `<PENDING>`
marking. Falsifies: any later prose that reads Q60's census as measured at this wave.

**F2 — the M95 citation shape recurs on a *second* lane surface that C2 does not repair.**
`SCORECARD.md:373` (r63 axis annotation, committed) reads "… prints `survivors closed 5 of 6`
with `bound: G9 remains unimplemented` @ `35d44b4b` (`.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`)"
— the same attribution as r63 report line 31, on the surface the lane *can* edit. C2's check
2 as frozen scans an appended **LOG** suffix only (`plans/round-64.md:128-135`), so the
counter will print `4 of 4` with `SCORECARD.md:373` unchanged. Recommendation for the L1
(pick one, recorded before data): (a) extend check 2 to require the appended correction line
to name `SCORECARD.md:373`'s defective citation and its fix, or (b) keep check 2 as frozen
and bound Q60's evidence cell to "LOG correction landed; SCORECARD annotations of rounds ≤63
are not swept" (Q26: the cell may not imply a sweep the counter does not run). Either way,
the SCORECARD line is append-only history and is corrected by an appended round-64
annotation, never by rewriting line 373. Falsifies: reading "4 of 4" as class closure on
every lane surface.

**F3 — `git cat-file -e` exits 128, not 1, for a path the revision lacks** (E1). A row that
said "exits 1" would be a false statement about the tool the row names, i.e. fresh M95-class
drift inside the M95 row. D1's criterion therefore says "exits 128 (nonzero)". Supports Q60's
own subject matter; falsifies the plan's unstated assumption if any check tests `== 1`
(`grep -n 'cat-file' verifiers/*.py` shows the r63 counter's own use is `returncode != 0`
style — `verifiers/check_r63_routed_repairs.py` calls `git show`/`cat-file` with `!= 0`;
no equality test seen at base).

**F4 — Q59's committed row is a 2-cell row** (E7): 3 pipes where the header declares 5
columns. Consequence for this seat: Q59 is *not* a template for cell count, only for
wording discipline (mechanism clause + "Fix shown able to fail" + evidence pointers). The
L1 should route Q59's malformed shape as a scribal defect for the next QUALITY touch
(append-only: fixed by a superseding/corrective row or an appended note, never by rewriting
line 74). Supports: D1's 6-pipe audit. Falsifies: "follow Q58/Q59" read as "match Q59's
cells".

**F5 — the census grammar trap (calibration core).** Measured both directions (E8):
`<path>` @ `<rev>` exact adjacency finds **4/4 clean** citations and would report the class
as absent; the reversed form `@ <rev> (<path>)` finds **24/24 ABSENT**, but at least
`LOG.md:2465`, `LOG.md:2482`, `SCORECARD.md:28`, `SCORECARD.md:304` are *legitimate
measurement pins* ("exit 1 @ `a975cbbf` … (`.ufo/waves/round-59/C1-measure.txt`)": the rev is
the run's base, the path is the bare carrier). So a census that tests every same-line
(rev, path) pair over-flags by ~an order of magnitude, and one that tests only exact
adjacency under-flags to zero. The row must therefore carry the disambiguation in its
criterion (D1 does: "the rule binds the path-claim form only"), and the census must
adjudicate each hit as *attribution* (path's bytes at rev) vs *run pin* (output at rev,
path bare). Supports Q20's both-directions discipline for approximating checks. This is the
substance behind the assignment's "wording discipline follows Q58/Q59".

**F6 — the fleet r63 report is outside lane write bounds.** E5's lines live under
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md` (fleet tree), so the lane's
closure of defect 2 is (i) the appended LOG correction naming `committed at 8c4cefa, run
against base 35d44b4b` / `committed at cbbee56, run against base 35d44b4b` and (ii) Q60.
Q60's evidence cell therefore *describes* the report's defect and does not claim it was
fixed. Supports Q17's fleet-root report-only rule; falsifies any report sentence that says
the r63 report was corrected.

---

## Touched surfaces

- Written: this file only (`.ufo/waves/round-64/w1/ScribeQ60.md`).
- Read (lane): `corpus/QUALITY.md` (Q03, Q55–Q59, header), `plans/round-64.md` (C1, C2,
  checks 1–4, sources), `corpus/lessons/round-63.md` (M94, M95, row t),
  `corpus/lessons/round-63-verifier-spotcheck.md` (defects 1–6), `SCORECARD.md:28,373`,
  `LOG.md:2443-2581`, `.ufo/waves/round-64/w1-spec.json` + `w1/swarm-registry.json`,
  both r63 controls at their committing revs, `verifiers/check_r63_routed_repairs.py`.
- Read (fleet, read-only): `.ufo/reports/round-63/kotoba.md:18,31,32`.
- Scratch: `/tmp/q60_census{,2,3,4}.py` (no lane bytes).

## Out of scope / not done

- Not run: `verifiers/check_r64_routed_repairs.py` (does not exist, E6); its `0 of 4` / `4 of 4`
  numbers above are the plan's **declared** predicate (`plans/round-64.md:112-121`), not
  measurements by this seat.
- Not authored: the LOG correction text (peer `ScribeLOGCorr`), the round-64 lesson M96 row
  (peer `ScribeLesson` — Q60 forward-cites it), the SCORECARD round-64 annotation.
- No tool installs or upgrades; no git/jj writes; no product-code edits.

## Conflicts for the canonical judge (verbatim, not reconciled)

1. Base naming: the dispatch says "Base tip at dispatch: 078eec4 (plan freeze c04fffbe)",
   while `git log -1` at the lane reads `c04fffbeafcaf810897258d56f99cca736ed3a91 round-64:
   freeze plan — …` and `plans/round-64.md` calls `078eec4` the base tip / measurement base.
   Both revs are used literally in C1/C2 (`078eec4` as BASE_REV, `c04fffbe` as the freeze
   commit); Q60's row cites neither as a truth value, only the controls' revs.
2. Q60's census: assignment says "the ScoutReceiptSweep census count `<PENDING>`", while
   `w1-spec.json`'s scout prompt asks for a count over three surfaces; no scout output
   exists at base (F1). The row keeps the literal placeholder.
