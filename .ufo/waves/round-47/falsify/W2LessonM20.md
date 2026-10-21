verdict: PARTIAL — every pointer in M20 re-runs exactly and the prototype does fail the three stale copies and pass a fresh control, but that witness tests a version literal, not the M20 class (copied before-values); Q19's wording is not decidable, and the landing commit itself trips the prototype it cites as its proof.

# Scope

Lane: `KotobaR47-2.W2LessonM20-2` (reviewer, leaf, no subagents). Attacked
`corpus/lessons/round-47.md:19` (M20) at tip `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`
(BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`), its "Shown able to fail" evidence
`.ufo/waves/round-47/build/MistakeStalePremise.premise-check.txt`, and the criterion it
grounds, `corpus/QUALITY.md:30` (Q19).

All work in the canonical-layout scratch clone
`/fast/scratch/kotoba-r47/w2/W2LessonM20/kotoba-shokunin` (`git clone --no-hardlinks` of the
lane repo, symlinked siblings, `git checkout --detach 7ad7fad` / `c61a973`). The production
tree under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was never mutated: my lane writes
are the two artifacts named below plus this report, all under `.ufo/waves/round-47/falsify/`.
No `git add/commit/stash/reset/switch/pull/push` and no mutating `jj` command was run in the
lane repo. The prototype was **applied from the committed patch**
(`.ufo/waves/round-47/build/MistakeStalePremise.patch`, sha256
`a83419d785ffe141945790b9bdd4b627ef1342d135f84c20e6ef14b4c74f460f` — identical to the hash the
wave-1 report claims) into the scratch clone only; it is not committed anywhere at 7ad7fad.

# Findings

## F1 — HIGH — the "shown able to fail" witness does not witness the M20 class; it passes the exact mistake M20 names

M20's class is *"Stale planned premise (before-values copied, not re-measured)"*
(`corpus/lessons/round-47.md:19`). The load-bearing stale content in the three copies was the
**count pair** `"surfaces 5/7, pins 1/3"`, copied verbatim from the round-44 before-column
(`.ufo/reports/round-44/kotoba.md:28` → `| C3 | substrate red | surfaces 5/7 (0/8 loader-class),
pins 1/3 | …`). The prototype compares **only version literals and absolute `/…/bin/…` paths**
against the live binary: `.ufo/waves/round-47/build/MistakeStalePremise.patch:21`
(`OMP_VERSION_RE = re.compile(r"\bomp[ /]18\.12\.(\d+)\b")`), `:22` (`ABS_BIN_RE`), `:48`
(`for m in OMP_VERSION_RE.finditer(line)`), `:52` (path existence). It never inspects a count,
a command, a commit, or a date.

Counterexample (repro in the scratch clone, fixture text also in
`.ufo/waves/round-47/falsify/W2LessonM20.counterexamples.json`):

```
$ cat /fast/scratch/kotoba-r47/w2/W2LessonM20/ce/copied-counts.md
Before: omp 18.12.5 live
Before: surfaces 5/7, pins 1/3
$ python3 -B verifiers/check_planned_premises.py .../copied-counts.md
PASS every named premise matches live omp 18.12.5
exit=0
```

That file carries the **exact** M20 stale before-value, and the prototype passes it. The true
measurement of the same quantity at BASE is not "5/7, 1/3" but `surfaces exit 2` and
`pins exit 2 DRIFT 3/3` (re-run below). So the prototype cannot distinguish a re-measured
premise from a copied one; it distinguishes "mentions 18.12.3" from "mentions 18.12.5".

Consequence for the admission: Q19 (`corpus/QUALITY.md:30`) requires that a planned before-value
"is re-measured at round start **and printed with its command and commit**", and M20's
`captured-by` cell asserts the class is now captured ("none → Q19"). The only evidence offered
for Q19 exercises none of that — the passing fixture above *violates* Q19's own sentence and
still passes the instrument. The wave-1 report itself concedes the limit
(`.ufo/waves/round-47/build/MistakeStalePremise.md`, § Counterexamples and limits: "The
prototype checks only version literals and absolute binary paths. It does not check count
literals such as `surfaces 5/7` or `pins 1/3`."), but M20's row and the admitted criterion do
not carry that concession forward — the row says the prototype "fails on all three stale copies
… and passes a fresh control", which reads as a class witness and is not one.

## F2 — HIGH — the landing commit fails the very prototype it cites as its proof; "struck" is undefined, so Q19's compliance at the tip is undecidable

Re-running the prototype against the **tip** files (patch applied at 7ad7fad in the scratch
clone; live `omp --version` → `omp/18.12.5`):

```
$ python3 -B verifiers/check_planned_premises.py SCORECARD.md
FAIL SCORECARD.md:101: planned omp 18.12.3 != live omp 18.12.5
FAIL SCORECARD.md:106: planned omp 18.12.3 != live omp 18.12.5
exit=1
$ python3 -B verifiers/check_planned_premises.py corpus/README.md
FAIL corpus/README.md:76: planned omp 18.12.3 != live omp 18.12.5
exit=1
$ python3 -B verifiers/check_planned_premises.py PROVINCE.md
FAIL PROVINCE.md:22: planned omp 18.12.3 != live omp 18.12.5
exit=1
```

Two distinct defects are visible here.

**(a) The stale value was annotated, not struck.** `SCORECARD.md:101` (the round-47
`**Next: round 47**` block) still reads, verbatim at 7ad7fad: "extract the 8 loader-group
literals and call shapes from installed omp 18.12.3 … **Before: surfaces 5/7, pins 1/3**". The
correction lives in a *different* paragraph further down, `SCORECARD.md:106` ("Q19 correction to
the `Next: round 47` block above: its C1 before-values … were a stale copy"). Q19 says a copied
value "is struck". Nothing in the repo defines what "struck" means: `grep -rn 'struck' corpus/*.md
CORPUS.md` returns exactly one hit — the Q19 row itself. The correction prose also has to
*quote* the stale literal to be a correction, and the prototype flags that quotation
(`SCORECARD.md:106` FAIL above; the same shape reproduced standalone as fixture
`erratum-mention.md` → exit 1). So the instrument cannot express the one form the criterion
requires — a Q18-class false red on a class of input the instrument must tolerate.

**(b) Two readings, opposite answers, no rule to pick.** Literal reading ("the value is still
there, so it is not struck") → the landing commit violates the criterion it minted in the same
commit. Charitable reading ("the round-47 score used the corrected values, `SCORECARD.md:106` +
`.ufo/waves/round-47/before/SUMMARY.md`") → the landing commit complies. Q19 as written
contains no clause that decides between them ("never scored against" is a statement about the
scoring process, not about any committed artifact), so a reviewer cannot decide whether
7ad7fad satisfies the criterion that 7ad7fad introduced.

A second false-red class, same mechanism (fixture `historical-table.md`, exit 1): any plan file
that lists previous versions in a table — the normal way to record what changed — is reported as
carrying stale premises.

## F3 — MED — the prototype is blind exactly when the substrate family changes (the next likely event)

`OMP_VERSION_RE` hardcodes the `18.12.` series (`patch:21`) and `live_omp` raises on anything
else (`patch:31`, "no 18.12.x in: …").

```
$ cat .../ce/major-bump.md
Before: omp 19.0.1 live
$ python3 -B verifiers/check_planned_premises.py .../ce/major-bump.md
PASS every named premise matches live omp 18.12.5      # exit=0  — the literal is never compared
$ python3 -B verifiers/check_planned_premises.py .../ce/major-bump.md --omp-binary .../ce/omp-fake-19
ERROR cannot read live omp version: no 18.12.x in: 'omp/19.0.1'   # exit=2
```

There is no state in which the instrument reports "planned omp 19.x != live omp 19.x": a plan
naming a different series is silently accepted, and a live omp off the 18.12 series makes the
gate exit 2. Given that this round's own frontier is loader/extract lineage churn
(`corpus/knowledge/instruction-surface-census-round13.md` § B′, the omp extractor being a
callee-name allowlist), a series bump is the expected next substrate event — and at that moment
the gate is either blind or dead, never useful.

## F4 — MED — Q19's wording is not falsifiable as written

`corpus/QUALITY.md:30`:

> A carried or planned before-value is re-measured at round start and printed with its command
> and commit; a value copied from an earlier record is struck, never scored against.

Testability, defect by defect:

1. **"round start" has no marker.** No commit, no date, no artifact defines the instant the
   round starts, and "printed with its command and commit" does not say *which* commit (the BASE
   at round start, or the commit the measurement was taken at). Two readers can satisfy "printed
   with its command and commit" with different commits.
2. **"struck" has no convention** (see F2a): `grep -rn 'struck'` over `corpus/` and `CORPUS.md`
   → 1 hit, the Q19 row itself. No strike marker, syntax, or registry exists, so compliance is
   a matter of taste.
3. **"never scored against" is not a property of any artifact.** It is a rule about the scoring
   process; nothing in the tree can be inspected to decide it.
4. **The `applies to` cell is wider than the criterion sentence.** It lists "SCORECARD `planned`
   rows, plan before-columns, **Frontier figures**", but the sentence governs *before-values*.
   The tip's Frontier figures are `PROVINCE.md:22` ("omp 18.12.5 and opencode 1.19.3 were
   re-derived and re-pinned (surfaces 7/7, pins 3/3 at default resolution)") and
   `corpus/README.md:76` (same pair). Both carry **no command and no commit**. Under the
   scope reading, 7ad7fad violates Q19 in its own front door; under the sentence reading it does
   not.
5. **"before-value" is undefined.** `grep -rn 'before-value' corpus/ CORPUS.md` → 0 hits outside
   the lesson row, so the set of in-scope values is not enumerable by any rule; a checker must
   guess which numbers are "before-values" (the SCORECARD has several number-like cells that
   are neither).
6. **No instrument is registered for it.** `grep -rn 'Q0[0-9]\|Q1[0-9]' verifiers/` → 0 hits:
   no criterion (Q01–Q19) appears in any machine-readable registry, so Q19 is prose-only. Its
   sole enforcement is a prose reminder in `SCORECARD.md:108` ("**Next: round 48** — re-measure
   every before-value first (Q19)").

Not a defect (checked, so it is not counted): Q19 does not duplicate Q09 or Q13 — Q09 governs
post-rebuild redness, Q13 is scoped to "knowledge/lesson prose" and prescribes a format
(`<number> — <command> <date>`) that Q19 does not reuse; Q19 adds the commit and the strike
rule and widens the scope to front-door plan rows.

## F5 — MED — "shown able to fail" is not reproducible from the repository alone

At 7ad7fad there is no `verifiers/check_planned_premises.py` (`ls verifiers/` → no such file).
What is committed is the patch (`.ufo/waves/round-47/build/MistakeStalePremise.patch`,
sha256 `a83419d7…`, matching the wave-1 report) and the output log
(`…/MistakeStalePremise.premise-check.txt`, sha256 `0d0f177cd8c44aea1cdd590bd4f9727c2f00e81b2dfeb1768259bc0f53a2ef26`,
matching the report's `0d0f177c…`). The five **fixture files** (`stale.md`, `fresh.md`,
`absent-path.md`, `present-path.md`, `omp-fake-5`) are **not** in git —
`git ls-files | grep -E 'omp-fake|fixtures/(stale|fresh|absent-path|present-path)'` → no
match; they live only in the wave-1 lane scratch
`/fast/scratch/kotoba-r47/MistakeStalePremise/fixtures/`. I reconstructed them from the
report's prose and my re-run then matched the committed log **byte for byte** (see § What
survived), so the evidence is sound — but a reviewer who lacks that scratch directory must
rebuild the control from a text log, and the "fresh control" arm is 25 bytes of prose. The
control is also not hermetic: the three stale-copy runs depend on the *live* omp being
18.12.x, which is the very drift under test.

## F6 — LOW — the admission bar's own stated contract is contradicted by the row it added, with no erratum

`corpus/QUALITY.md:5-6` (header, unchanged by the landing):

> No criterion exists without a lesson behind it — `grounded in` names the class row in
> `corpus/lessons/round-46.md` § Mistakes.

and `corpus/README.md:60` (index row for `QUALITY.md`):

> the lane's own quality bar, created round 46: every criterion cites its row in
> `lessons/round-46.md` § Mistakes …

Q19 (`corpus/QUALITY.md:30`) grounds in `corpus/lessons/round-47.md` § Mistakes — the first row
grounded outside round-46. The landing diff touched the criterion table only:
`git show 7ad7fad -- corpus/QUALITY.md` → `@@ -27,6 +27,7 @@ … +| Q19 | …` (1 insertion, no
header change), and `corpus/README.md:60` still carries the old sentence. Either the header
needed an update (its prose is not criterion rows and is not append-only) or Q19 violates the
bar's stated rule; the round recorded neither. Round-47 also did not note that it was the first
criterion to leave round-46 — no row, no erratum, no note.

## F7 — LOW — the lesson's fix text and the admitted criterion are not the same rule

`corpus/lessons/round-47.md:19` (M20 fix cell): "Q19: a planned before-value is re-measured at
round start and **recorded** with its command and commit, **or struck**."
`corpus/QUALITY.md:30`: "…**printed** with its command and commit; a value copied from an earlier
record **is struck, never scored against**."

The lesson states an *option* ("or struck"); the criterion states a *mandatory* strike plus a
scoring prohibition. A reader who implements from the lesson row gets the weaker rule. The
lesson's `captured-by` cell ("none → Q19 (Q09 covers a rebuild, not a copied premise)") and the
criterion's `supersedes` cell (`—`) agree on that point, so this is a wording drift between the
two artifacts of the same claim, not a substantive disagreement.

## F8 — LOW (bookkeeping) — the wave-1 report's `file:line` pointers are BASE-scoped and already stale at the tip

`.ufo/waves/round-47/build/MistakeStalePremise.md` cites `SCORECARD.md:101`,
`corpus/README.md:74`, `PROVINCE.md:21`. Those are **BASE-accurate** (verified: the prototype's
BASE run prints exactly `SCORECARD.md:101`, `corpus/README.md:74`, `PROVINCE.md:21`), but at
7ad7fad the same literals sit at `SCORECARD.md:101`, `corpus/README.md:76`, `PROVINCE.md:22`.
The report is not a lesson file, so this is not an M22 violation, but a future reader who runs
the build report's pointers against the tip will land two lines off in two of three files.

# What survived the attack (findings too — nothing below was broken)

Every pointer in M20's evidence cell re-ran exactly as written.

1. `git show c61a973:SCORECARD.md | grep -c 'installed omp 18.12.3'` → **1**, exit 0. ✓
2. `omp --version` → `omp/18.12.5`, exit 0. ✓ (live omp is still 18.12.5 at review time)
3. BASE `python3 -B verifiers/verify_surfaces.py --json` → **exit 2**, `"error": "opencode
   binary not found: /home/vgpnk/.opencode/bin/opencode"` — matches
   `.ufo/waves/round-47/before/SUMMARY.md:3` ("surfaces default: exit=2"). ✓ (run detached: the
   in-shell invocation died with the caller's process group and printed nothing — [INFERENCE]
   cause, the verifier terminates the group; the detached run completed and produced exit 2)
4. BASE `python3 -B verifiers/check_substrate_pins.py` → **exit 2**, `DRIFT 3/3 pins failed:
   omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256` — matches
   `.ufo/waves/round-47/before/SUMMARY.md:5` ("pins: exit=2 DRIFT 3/3"). ✓
5. `corpus/lessons/round-46.md:27` (M9) → `DRIFT 2/3 pins failed: omp_binary_sha256,
   omp_binary_mtime` — the "itself recorded DRIFT 2/3" pointer. ✓
6. Provenance of the copied figures: `.ufo/reports/round-44/kotoba.md:28` → `surfaces 5/7
   (0/8 loader-class), pins 1/3`; `git log -S 'pins 1/3' --format='%h %s'` → `032f47b` (round 44
   publish), `f2f9ee1` (round 46 landing), `7ad7fad` (round 47 landing). ✓
7. **The committed "shown able to fail" log reproduces byte-for-byte.** I re-ran all eight arms
   (patch applied to BASE) and diffed against
   `.ufo/waves/round-47/build/MistakeStalePremise.premise-check.txt`: `diff` clean (after
   normalising the fixture path prefix). The three stale copies fail (exit 1, 1, 1) and the fresh
   control passes (exit 0). **M20's literal claim — "fails on all three stale copies …
   and passes a fresh control" — HOLDS.** What does not hold is the *class* implication drawn
   from it (F1) and the landing's own compliance (F2).
8. Artifact hashes agree with the wave-1 report: `premise-check.txt` sha256 `0d0f177c…`,
   `MistakeStalePremise.patch` sha256 `a83419d7…`. ✓
9. **The round-47 plan complied with Q19's substance** even though Q19 post-dates it:
   `plans/round-47.md:3-5` names BASE `c61a973…`, the before-run record and the frozen
   snapshot; `plans/round-47.md:22-27` gives the re-measured before-values with their commands
   (`verify_surfaces.py` exit 2 … `check_substrate_pins.py` exit 2, 3/3 pins failed; `Count:
   python3 -B verifiers/verify_surfaces.py --json`; `python3 -B verifiers/check_substrate_pins.py`).
   The round did what Q19 later demanded. The gap is that the criterion was written to be
   satisfiable by prose alone and no instrument was kept.

# What I did NOT check

- C1's substance: the omp callee allowlist (`lq`/`Xl`/`Fo`), the opencode 1.19.3 lineage, the
  re-derived OC-1..OC-6 rules, and the tip-side `surfaces 7/7 exit 0` / `pins 3/3 exit 0` runs.
  I ran the two gates **only at BASE**, because they are M20's before-column pointers; the
  after-column is other seats' scope.
- I never executed `~/.local/bin/opencode` or any opencode binary; I read only the frozen
  snapshot and `SHA256SUMS` indirectly through the wave-1 artifacts.
- The duplication/overlap question between Q19 and Q09/Q13 in depth (the dedicated `W2Q19`
  seat owns it); I only checked that the scopes differ and that the wording does not reuse
  Q13's format.
- `corpus/SOURCES.md` S012–S015, `corpus/knowledge/instruction-surface-census-round13.md`, the
  corpus baseline/`tracked_files` change, the checklist gate, and the fault-harness planter
  fix — none of this lane's claim.
- No tree-wide sweep for other stale premise literals beyond the three front-door files and
  `plans/round-47.md` (the wave-1 report scoped its own grep the same way). A full sweep could
  find more stale copies; I did not run one.
- I did not wire the prototype into any verifier, checklist, or round-start procedure, and I did
  not mutation-test it beyond the five counterexamples above — there is nothing to mutate in
  the committed tree, since the instrument is not committed (F5).
- I did not re-derive the S015 snapshot digests, and I did not verify the shared scratch
  directory's `SHA256SUMS` myself.
- Governance decision left open for the integrator: whether Q19 is prospective (from round 48)
  or retroactive to 7ad7fad. My F2 finding states both readings; I did not rule on which the
  lane should adopt.

# Commands (all run read-only, in the scratch clone unless noted)

```
git -C kotoba-shokunin show c61a973:SCORECARD.md | grep -c 'installed omp 18.12.3'   # -> 1, exit 0
omp --version                                                                      # -> omp/18.12.5, exit 0
git -C kotoba-shokunin log -S 'pins 1/3' --format='%h %s'                            # -> 7ad7fad, f2f9ee1, 032f47b
sha256sum .ufo/waves/round-47/build/MistakeStalePremise.premise-check.txt             # -> 0d0f177c…
sha256sum .ufo/waves/round-47/build/MistakeStalePremise.patch                         # -> a83419d7…
git ls-files | grep -E 'omp-fake|fixtures/(stale|fresh|absent-path|present-path)'     # -> (no match)
git show 7ad7fad -- corpus/QUALITY.md                                                # -> 1 insertion, header untouched
grep -rn 'Q0[0-9]\|Q1[0-9]' verifiers/                                               # -> (no hits)
grep -rn 'struck' corpus/*.md CORPUS.md                                               # -> only corpus/QUALITY.md:30
grep -rn 'before-value' corpus/ CORPUS.md                                             # -> only corpus/lessons/round-47.md:19
# BASE gates (run detached: the in-shell run died with the caller's process group [INFERENCE cause])
python3 -B verifiers/verify_surfaces.py --json          # -> exit 2
python3 -B verifiers/check_substrate_pins.py             # -> exit 2, DRIFT 3/3
# prototype (applied from the committed patch into the scratch clone, never into the lane)
python3 -B verifiers/check_planned_premises.py SCORECARD.md        # BASE exit 1 (:101) / TIP exit 1 (:101,:106)
python3 -B verifiers/check_planned_premises.py corpus/README.md    # BASE exit 1 (:74) / TIP exit 1 (:76)
python3 -B verifiers/check_planned_premises.py PROVINCE.md         # BASE exit 1 (:21) / TIP exit 1 (:22)
python3 -B verifiers/check_planned_premises.py <fixtures>/{stale,fresh,absent-path,present-path}.md --omp-binary <fixtures>/omp-fake-5
#   -> exit 1, 0, 1, 0  (byte-identical to the committed log)
python3 -B verifiers/check_planned_premises.py SCORECARD.md --omp-binary /nonexistent/omp   # -> exit 2
# counterexamples
python3 -B verifiers/check_planned_premises.py .../ce/copied-counts.md     # -> exit 0 (PASS; carries the M20 stale counts)
python3 -B verifiers/check_planned_premises.py .../ce/major-bump.md        # -> exit 0 (PASS; omp 19.0.1 never compared)
python3 -B verifiers/check_planned_premises.py .../ce/major-bump.md --omp-binary .../ce/omp-fake-19   # -> exit 2
python3 -B verifiers/check_planned_premises.py .../ce/erratum-mention.md   # -> exit 1 (false red on the correction)
python3 -B verifiers/check_planned_premises.py .../ce/historical-table.md  # -> exit 1 (false red on a version history table)
```

# Tools and installs

No tool was installed, upgraded, or removed. Commands used: `git` (clone/checkout/diff/show/log
in the scratch clone only), `python3 -B`, `omp --version`, `sha256sum`, `grep`, `diff`,
`printf`, `setsid` (to survive a verifier that kills the caller's process group). No pacman,
uv, npm, or cargo transaction was performed.

# Artifacts

- `.ufo/waves/round-47/falsify/W2LessonM20.md` — this report.
- `.ufo/waves/round-47/falsify/W2LessonM20.premise-rerun.txt` — the full re-run battery: M20
  pointers 1–4, the prototype on the three stale copies at BASE, the four fixture arms, the
  no-omp arm, the five counterexamples, and the prototype's run on the three front-door files
  at TIP 7ad7fad, with exit codes. (The two BASE gate runs are recorded from detached
  invocations — see § Commands.)
- `.ufo/waves/round-47/falsify/W2LessonM20.counterexamples.json` — fixture texts, observed exit
  codes and the point each counterexample makes.

# Checks the integrator should run

- Read `SCORECARD.md:101` against `corpus/QUALITY.md:30` and decide the reading: is the round-47
  plan block's before-value *struck* by the correction at `SCORECARD.md:106`, or still live?
  Q19 needs a decidable answer before it can gate anything.
- If Q19 is to keep the "shown able to fail" evidence, it needs an arm that fails on a plan
  carrying **only** the copied count pair (`surfaces 5/7, pins 1/3`) with a current version
  literal — that is the class, and the current prototype passes it.
- If the prototype is kept, it needs: a series-agnostic version regex, a strike/erratum and
  version-history tolerance (the Q18 control arm), and committed fixtures; otherwise the M20
  witness should be re-labelled as "the version literal can go stale", which is a weaker claim
  than the row makes.
- `corpus/QUALITY.md:5-6` and `corpus/README.md:60` state that every criterion cites a
  round-46 lesson row; Q19 does not. Either extend both statements to the current round's
  lesson file or record the exception.
