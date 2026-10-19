# Seat V6b — C3-verifier-2 (kotoba-shokunin, round 38)

Task: 71-fixture byte-identity + live byte-invariance + corpus-gate fence
divergence probe (P7's r37 open item D4/F9 — measure, classify, name as debt
or fix in-scope).

Axes: freshness (C3 fence landing) primary; operability (gate byte-invariance)
secondary; depth (divergence classification) tertiary.
Posture: godspeed (name axes, iterate cheap in parallel, decide and report).
Every claim below carries a command + observed output, re-run at write time.

## Measurement pins

**FINAL STATE (2026-10-19T13:43:55Z): C3 LANDED mid-seat.** The live checklist
moved `9ea386da` -> `f8066f3b` -> **`214ae44dcba45ba1`** (18 FENCE_SHAPES, self-test
1597). Everything below marked **[landed]** was re-verified at `214ae44d`;
the earlier pins are kept because the divergence probe and corpus-fix work were
measured against them.

- HEAD `cb4e0f32`; worktree dirty with sibling C1/C2 landings in flight
  (`check_assertion_floors.py`, `floors-registry.json`,
  `verify_harness_independent.py`, `compare_harness_independent.py`,
  `corpus/README.md`, `verifiers/corpus-baseline.json`).
- Candidate history: `patched-c` `1c980a98…` -> `4acebe58…` -> `f2ee3701…`;
  then the live landing `f8066f3b` (= `patched-c` + a 2-line docstring
  restoration); then `214ae44d` adding the 3 container shapes and the floor bump.
- cmark 0.31.2 already present (`cmark --version` -> `cmark 0.31.2`); no install.
- All numbers re-run at write time; log `.ufo/round-38/drafts/v6b/final-receipt.txt`.

## FINDINGS

**F1 — 71-fixture byte-identity holds, against the sealed r37 manifest.**
`find verifiers/fixtures/checklist -type f | sort | xargs sha256sum | sha256sum`
-> `56351d061ece26ec34d04a06028f4a6afb2b4c1372d4bbb7916ec0ffabedea77` —
byte-for-byte the manifest V7 sealed in r37 (`scouts/V7.md`). `dirs=71
files=145`; `git status --porcelain verifiers/fixtures` -> 0 lines. No fixture
moved during the C3 drafts or the landing.

**F2 — Live gate stdout is byte-invariant through this seat.**
Pinned pre (`drafts/v6b/live-shas-pre.txt`, 13:33:55Z) vs final: `checklist
02de0b97…`, `corpus_integrity 77e7cc53…`, `corpus_independent 41301b83…`,
`harness 2b0bfc4c…`, `surfaces 549f90ff…`, `pins 82468d25…`, `checklist
--self-test ad311f5e…`, `corpus_integrity --self-test 3c276f86…` — identical.
`check_assertion_floors.py` and `fault_injection --self-test` **did** move
(`aff5a4a6…` -> `21bb0d11…`; `a1c650a4…` -> `33a7303b…`): the sibling C2
landing, not a C3 effect (floors registry grew 6 -> 8 instruments mid-seat).

**F3 — [superseded by F12] C3's container class was NOT landed at `9ea386da`.**
`python3 .ufo/round-38/drafts/p5/harness/oracle.py --repo .` (byte-identical to
`.ufo/round-37/evidence/v6-oracle.py`, verified by sha) ->
`probe lines=30 mismatches=4 (instrument vs cmark)`, the four being S07 L6,
S08 L7, S07b L7 and S07b L10 — exactly V6's r37 residuals. That was the live
state when this seat began; C3 landed later in the seat (F12).

**F4 — The drafted candidate closed it: 0/30 and byte-invariant on every gate.**
Against `f2ee3701` (and identically at `4acebe58`): oracle ->
`probe lines=30 mismatches=0`, `spec-vs-cmark disagreements=0`,
`unexplained cmark spans=0`, sha STABLE; builder battery `failing=0`;
`--self-test` `0 failure(s) over 1584`; live stdout sha under real paths
identical to the then-live instrument (`02de0b975bba42b4` both). The only
foreign-directory divergence is the known `trigger.name_directory` location
artifact, which vanishes under `--repo $R --skill $R/SKILL.md`.

**F5 — P7's r37 D4 divergence is a real silent false-PASS vector (measured end
to end, not inferred).** `drafts/v6b/fence_exploit_probe.py` builds a throwaway
corpus whose only coverage of `knowledge/b.md` is a coverage row quoted inside
a fenced example (the round-36 P3b class) and runs both gates. cmark 0.31.2 is
the oracle, classified by which source window reproduces each `code_block`'s
text — not by the `info` attribute, which cmark omits for an empty info string
(my first two harness versions got this wrong and reported garbage; both
mistakes are recorded in the draft's history).

```
shape                  row@L   cmark     integrity     independent   verdict
control-3backtick      L9      opaque    unindexed=1 rc=1 unindexed=1 rc=1 agree
short-closer           L10     opaque    unindexed=0 rc=0 unindexed=0 rc=0 FALSE PASS (silent)
info-closer            L10     opaque    unindexed=0 rc=0 unindexed=0 rc=0 FALSE PASS (silent)
closer-trailing-text   L10     opaque    unindexed=0 rc=0 unindexed=0 rc=0 FALSE PASS (silent)
blockquote             L9      opaque    unindexed=1 rc=1 unindexed=1 rc=1 agree
foreign-char-closer    L10     opaque    unindexed=1 rc=1 unindexed=1 rc=1 agree
tab-indented-opener    L10     live      unindexed=1 rc=1 unindexed=1 rc=1 FALSE FAIL (loud)
indented-4col          L10     live      unindexed=1 rc=1 unindexed=1 rc=1 FALSE FAIL (loud)
nested-item-4col       L10     opaque    unindexed=1 rc=1 unindexed=1 rc=1 agree

shapes=9  silent false-PASS=3  loud false-FAIL=2
```

Three spec-illegal pseudo-closers (````` ```` `` opened / ``` closed;
```python as a closer; ``` nope as a closer) make **both** gates report
`unindexed=0` and exit 0 where cmark says the row is fenced content and the file
must be unindexed (exit 1). The two `FALSE FAIL` rows exit 1 either way —
over-hiding is fail-safe, so they are debt, not exploitable. Root cause:
`FENCE_RE` + `fenced_lines` / `fenced_line_numbers` treat any fence-looking line
as a toggle (`verify_corpus_integrity.py:304-324`,
`verify_corpus_independent.py:216-234`) — no closer-length, same-character or
empty-info rule.

**F6 — Latent today: zero live corpus incidence.** Independent strict
re-derivation over all 52 corpus docs: `docs=52 interior/illegal fence-like
lines=0`, `docs where instrument != strict-spec opacity: 0`; the corrected
divergence probe agrees: `live corpus docs with fenced_lines != cmark: 0`.
Corpus census: 140 fence-like lines, 134 at column 0, 6 at column 2, **0** at
column 4+, **0** blockquote fences. So F5 is debt with a working exploit, not a
live break — it fires the first time a corpus doc closes a ````-opened block
with a short/info-bearing fence.

**F7 — The divergence class is closable in one function, and I proved it.**
`drafts/v6b/corpus_fix_candidate.py` applies the minimal CommonMark 4.5 closer
rule to copies of both instruments. Result: `compile rc=0` both;
self-tests green (`0 failure(s) over 119` / `59 assertions, 0 failures`);
live corpus gates' stdout **byte-identical** to live
(`stdout identical=True` for both); and the exploit matrix goes from
`silent false-PASS=3` to **0** for the three false-PASS shapes. Six matrix
shapes move (short-closer, info-closer, short-then-long, list-item-col4,
nested-item-col4, tab-indented), all toward cmark. Residual after the minimal
fix: `nested-item-4col` still diverges on the *independent* instrument only
(`unindexed=1` vs `0`) — container-relative scope, the same class V6's
checklist patch addresses, deliberately out of the minimal fix.

**F8 — [superseded by F12] `patched-c`'s self-test was BLIND to the class it
fixed.** Two mutants of `4acebe58` (M1: `rel` -> absolute column in
`fence_open`/`fence_close`; M2: drop the container-end fence termination) both
passed the self-test `0 failure(s) over 1584` rc=0 while the oracle reported
`mismatches=2`, because `FENCE_SHAPES` was still the 15 live entries with no
container shape. The landed `214ae44d` closes this (F12).

**F9 — `patched-full` is not landable.** Its self-test fails 2 assertions:
`fence[indented-code-decoy-four-spaces]: content lines []: got [1]` and
`fence[tab-indented-decoy-is-indented-code]: content lines []: got [1]`. V6
recommended `patched-c` for exactly this reason; I confirm.

**F10 — Routing pin: current at `9ea386da`, stale after the landing, now
re-issued.** At `9ea386da` P6's script said `pin already current`; after the
landing `STALE: re-pin needed 9ea386da5af5 -> 214ae44dcba4`. A sibling re-issued
it: the JSON's `instrument.sha256` now equals the live `214ae44dcba4` and the
script reports `pin already current` again. C3's third arm is satisfied.

**F11 — Observed sibling state (not my verification).** Mid-seat the floors
guard showed `FAIL harness_independent observed=71 floor=71 self_test_failures=6`
(C1's catalogue rows moving to `SCOPED_OUT`, `oc.log.skills_tag_hits: got 0 want
2`). At the final read all 8 instruments PASS (`harness_independent observed=86
floor=71`; `compare_harness_independent observed=76 floor=59`), guard exit 0.
One intermediate run read `FAIL compare_harness_independent observed=0 floor=59
summary=missing`; five consecutive re-runs then passed and the file's mtime
(10:46:14) shows it was being written during that run — a concurrent-edit
artifact, not a defect. Worth noting for the integrator: the guard runs
sibling instruments that other seats may be editing, so a single red run on a
shared tree is not evidence of a regression.

**F12 — [landed] C3 landed mid-seat and every arm I can measure now passes.**
The live instrument moved `9ea386da` -> `f8066f3b` -> `214ae44dcba4` (18
`FENCE_SHAPES`, self-test 1597). At `214ae44d`:
- oracle -> `probe lines=30 mismatches=0`, instrument sha STABLE (was 4 at
  `9ea386da`): the container class is closed on the live tree;
- `--self-test` -> `0 failure(s) over 1597 assertions`;
- 71-fixture identity still exact (`56351d06…`, 145 files / 71 dirs, git clean);
- **live stdout byte-invariant**: `git show HEAD:verifiers/verify_skill_checklist.py`
  (the pre-C3 `9ea386da`) run against `--repo $R --skill $R/SKILL.md` produces
  the identical sha `02de0b975bba42b4` and the same rc (1) as the landed file —
  `diff` empty;
- the 3 container shapes are present
  (`container-fence-four-abs-columns-in-item`, `container-fence-nested-item`,
  `container-fence-outdented-closer`), closing the F8 battery gap: my two
  container-logic mutants now **fail** the landed self-test (M1 `4 failure(s)
  over 1597` rc=1; M2 `5 failure(s)` rc=1) where at `patched-c` they passed
  0/1584 — so the class is regress-proof on the landed tree.

**F13 — [transient, caught and closed mid-seat] A real half-bump.** Between two
reads the guard's in-file tables and docstring said `checklist … 1597` while
`verifiers/floors-registry.json` still said `1584`; the guard named it `FAIL
registry floor drift: checklist registry=1584 expected=1597 row=1597` with real
exit **2** — the r37 C2 anchor working as designed. At the final read the
registry is consistent and the guard exits 0.

**F14 — [checker defect, not an instrument defect] r37's `verify_battery.py` is
container-blind.** It reports `battery shapes=18 failing=2` on the two
four-column container shapes. Raw cmark XML proves the **pins are correct** and
the checker is wrong: cmark emits `<item sourcepos="3:1-8:0"> …
<code_block sourcepos="5:5-7:7">- [ ] decoy-in-list-fence</code_block>` — the
block IS fenced and its content IS line 6, exactly the pin. The checker's
`cmark_code_spans` decides fenced-vs-indented with an absolute `cols <= 3` test,
so a container-relative opener at 4 absolute columns is misread as indented
code; my window classifier returns `fenced_opaque=[5,6,7]`,
`unexplained=none`. Landing the shapes was right; `verify_battery.py` needs the
same container-relative reading before it can grade them.

## ARTIFACTS (all under `.ufo/round-38/drafts/v6b/`)

- `fence_divergence_probe.py` + `divergence.txt` / `divergence.json` — the
  matrix vs cmark (self-checking window classifier; F5/F6)
- `fence_exploit_probe.py` + `exploit.txt` — the end-to-end false-PASS probe (F5)
- `corpus_fix_candidate.py` + `corpus-fix-candidate.txt` /
  `corpus-fix-matrix.txt` — the minimal in-scope fix and its grading (F7)
- `battery-discriminator.txt` — the M1/M2 mutants, re-run at `f2ee3701` (blind)
  **and at the landed `214ae44d` (caught)** — F8/F12
- `battery-checker-defect.txt` — the proof that r37's checker, not the pins, is
  wrong on the container shapes (F14)
- `before-head.out` / `after-landed.out` — the HEAD-vs-landed stdout pair (F12)
- `pre-state.txt`, `live-shas-pre.txt`, `final-receipt.txt` — pinned receipts (F1/F2/F12)
- `candtree/` — symlink mirror of the repo for in-place-equivalent candidate
  grading (verifiers/*.py + symlinks only; no whole-repo copy)
- `fixtures-pre.sha256` — 183-file fixture manifest at seat start

## DEFECTS

1. **[mine, fixed before publishing] Two harness bugs in my own probe.** (a) I
   classified a cmark `code_block` as fenced by the presence of an `info`
   attribute — cmark omits it for an empty info string, so run 1 reported 13
   bogus divergences. (b) "first source line matches a fence" then misclassified
   indented blocks holding fence-looking lines. Final version uses the r37
   oracle's window-matching method with an unexplained-span escape. Both wrong
   runs are in the draft history; only the final numbers are quoted.
2. **[mine, corrected] Direction labels.** I first printed all 5 divergences as
   "FALSE PASS"; end-to-end exit codes show 2 (tab-indented, 4-column) exit 1 =
   fail-safe. The probe now separates silent false-PASS from loud false-FAIL.
3. **[OPEN, MED — real exploit] The corpus gates share the r37 fence class**
   (F5): 3 confirmed silent false-PASS shapes on **both** instruments, 0 live
   incidence (F6). Outside C3's declared scope (C3 names the checklist
   instrument), but it is P7's D4 and the fix is proven one-function cheap (F7).
4. **[CLOSED mid-seat] `patched-c` had no container shape in `FENCE_SHAPES`**
   (F8): two container-logic reverts passed its self-test 0/1584; the landed
   `214ae44d` adds the three shapes and both mutants now fail (F12).
5. **[open, not landable] `patched-full` fails its own self-test** on two
   indented-decoy pins (F9).
6. **[OPEN, MED — tooling] r37's `verify_battery.py` cannot grade the landed
   battery** (F14): `failing=2`, but the pins are correct and the checker's
   absolute-column fenced test is the error. Fix the checker (or port my window
   classifier) before citing `failing=2` as an instrument defect.
7. **[CLOSED mid-seat, caught by the r37 C2 anchor] A live half-bump** (F13):
   in-file floors 1597 vs anchor 1584, guard exit 2 naming the drift; consistent
   at the final read. The anchor earning its keep in the wild.
8. **[process, mine] The worktree moved four times under me mid-seat.** Every
   number names the sha it was measured at; the C3 invariants were re-run at the
   landed sha (F12) and held.

## VERDICT INPUT

- **C3 / freshness — VERIFIED at the landed instrument `214ae44d`; all four
  declared arms now hold.**
  - *Met, measured on the landed tree (F12)*: oracle `mismatches=0` (was 4 at
    `9ea386da` — the container class is closed); self-test `0 failures over 1597
    assertions`; 71-fixture byte-identity exact (`56351d06…`, 145 files / 71
    dirs, git clean); live stdout byte-invariant — HEAD's `9ea386da` and the
    landed `214ae44d` produce the identical sha `02de0b975bba42b4` and rc 1
    under the same real paths; the 3 container shapes are in `FENCE_SHAPES`
    (18) and both container-logic mutants now fail the landed self-test (4 and
    5 failures), so the class is regress-proof.
  - *Met (F10)*: the routing-16 pin is re-issued to the landed sha and P6's
    script reports `pin already current`.
  - *Open, not an instrument regression (F14)*: r37's `verify_battery.py`
    reports `failing=2` on the new container shapes, but the pins match raw
    cmark XML and the checker's absolute-column test is the error. Fix the
    checker before citing that number.
  - Net: every substantive arm verifies at the landed sha. The one verdict I
    could not verify is `verify_battery.py`'s own, because it is container-blind.
- **Operability — no move from this seat, no harm.** Every gate I measured is
  byte-invariant under the C3 landing (F12) and under the corpus fix (F7); the
  only stdout movement I observed is the sibling C2/C1 landing (F2/F11). I also
  caught the transient half-bump the r37 anchor exists for (F13) — it was
  resolved in-step, and the guard exited 2 while it was live.
- **Depth — the divergence probe produced a classified, proven-closable
  defect** (F5/F6/F7): 3 silent false-PASS shapes on both corpus gates, 0 live
  incidence, one function to close, with a proof that the fix leaves both
  gates' live stdout byte-identical. That is the named debt P7's r37 hand-off
  asked for; it does not by itself move C1's axis.

## Limits

Point-in-time read of a shared working tree. The checklist instrument moved
four times during my seat (`9ea386da` -> `f8066f3b` -> `214ae44d`, plus the
`patched-c` drafts `1c980a98`/`4acebe58`/`f2ee3701`); every number names its
sha, and the C3 verdict pins the **landed** `214ae44d`. The corpus-gate numbers
(F5/F6/F7) were measured at `9ea386da`; both corpus instruments are
byte-unchanged since (`e6ddb217…` / `094d4673…`), so they still hold. Sibling
files changed mid-seat; re-run the floors guard and the oracle before
publishing. Statements about C1/C2 are observations of on-disk state, not
verification of their claims. No `/tmp`-only artifacts: the throwaway exploit
worlds are built under `tempfile.mkdtemp` and removed; every durable output
lives under `.ufo/round-38/drafts/v6b/`. No git mutation; no writes outside the
lane repo; no installs.
