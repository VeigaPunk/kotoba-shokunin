# Kb80E04DeadPointer — C1 repair 4: the dead report pointer (PORT to base 398cbe1)

Seat: executor, round 80 wave w1 (leaf; no spawns, no subagents, one scratch clone of my own).
Lane base for every measurement: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Lane tip observed
during my run: `a481913bafeb1ec5c231fd581f13da6ae5a306dc` ("round-80: correct base unresolvable
citation locators before claim data", a plans-only commit — the instrument bytes are unchanged).

Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E04DeadPointer/{clone,clone2,clone3,fleetshape2}`
(`git rev-parse --show-toplevel` asserted per clone before every mutation; `TMPDIR` inside the
scratch). Receipts: `.ufo/waves/round-80/build/Kb80E04DeadPointer/` (24 files) and the two
flat deliverables `Kb80E04DeadPointer.patch` / `Kb80E04DeadPointer.blob` /
`Kb80E04DeadPointer.composed-blob.txt`. No tool was installed or upgraded; pacman was not
invoked; no background service; scratch removed before yield (§9).

## 1. Verdict up front

The r79 repair **ports cleanly and unchanged** to the round-80 base: the patch file is
byte-identical to the r79 artefact, its context did not drift, and the repair does exactly what
the r79 seat measured — `report_dead` 1 → 0 with **every other observation byte-identical**.
The self-test is green with the fix (0/165) and red without it (`FAIL pointer/rev/dead: got
(3, 3) want (2, 3)`, exit 1).

Two things the r79 seat could not resolve are now resolved, because other seats' bytes exist:

- **The pin value.** The composed E04∘grammar blob is
  `cc182613a4d089c41e44f11b50e03b45ce582dd8` (integrity) and
  `89f392daab3e4181db3ded7676ca0879871ef7ff` (independent) — measured from the published stack
  `Kb80Y01-simplified.patch`, which embeds my E04 hunk **byte-identically** (programmatic
  comparison of the added lines, §6). E06's published counter patch
  (`Kb80E06CounterErratum.patch`) pins exactly these two values, and the composed stack's tip
  battery reads `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, in **both** the absolute
  `--repo <clone>` form and the `--repo .` form (§5).
- **The residual from r79 §7 B1/B3** (the pin guard had no re-pin path in-round; the `W7` control
  was unguarded) are counter/plan matters, not mine — the erratum opened the pin path and the
  plan's Addendum 1/2 corrected the locators.

I did **not** score any claim after-value; §5 reports the tip battery of a *stack world* I
assembled from other seats' published bytes, in my own scratch, as evidence for the L1 — the
claim's after-value belongs to the L1 at the landed tip.

## 2. The patch, and why the port is byte-identical

Source: `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`
(sha256 `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78`) plus its report
`.ufo/waves/round-79/w1/Kb79E04DeadPointer.md` (the red-before arm, the Q05/Q18/Q58 argument).

Context check FIRST, against the CURRENT bytes of `verifiers/verify_corpus_integrity.py` at
`398cbe1`:

```
$ git -C "$S/clone" rev-parse 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93:verifiers/verify_corpus_integrity.py
e470eaaea5ef11c582b8353c9344ddf730c1a57a      # == the r79 patch's index line "e470eaa"
$ git apply --check <r79 patch>       # scratch clone at 398cbe1
apply_check_rc=0
$ git apply --check <r79 patch>       # lane tip a481913
apply_check_rc=0
```

The base blob is the r79 patch's pre-image blob, so **nothing moved**; the port is the same
diff. Published copy:
`.ufo/waves/round-80/build/Kb80E04DeadPointer.patch`
(sha256 `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78` — equal to the r79
patch's sha256 exactly, so the port is byte-identical).

The diff (one file, `verifiers/verify_corpus_integrity.py`, +17/−0):

```
@@ -272,6 +272,12 @@ def resolve_pointer(base: Path, token: str) -> Path:
 def report_pointer_exists(base: Path, token: str, fleet_root: Path = FLEET_ROOT) -> bool:
     """Check the citing directory first, then the fleet root for bare report paths."""
+    head, _, rest = token.partition(":")
+    if head and rest.startswith(".ufo/reports/"):  # `<rev>:<path>`: a revision, not a tree path
+        at = base.resolve()  # the citing repository first, then the fleet root
+        lane = next((p for p in (at, *at.parents) if (p / ".git").exists()), None)
+        return bool(lane) and git_ok(lane, "cat-file", "-e", token) or git_ok(
+            fleet_root, "cat-file", "-e", token)
@@ -1023,6 +1029,17 @@ def self_test() -> int:
+        # round 79: the fleet repo is a revision `HEAD:.ufo/...` resolves in.
+        subprocess.run(["git", "init", "-q", str(fleet_root)], check=True)
+        ... (fixture commit) ...
+        rev_found = citation_findings("corpus/lessons/rev.md", ...)
+        eq("pointer/rev/dead", (rev_found["report_dead"], rev_found["report_total"]), (2, 3))
```

## 3. The red-before arm, and the green after (own exit status, no pipeline)

Recipe: `.ufo/waves/round-80/build/Kb80E04DeadPointer/recipe-selftest-arms-and-fix.sh`
(hunk #2 of the patch applied alone; hunk #1 = the fix). Receipts:
`selftest-arms-only-redbefore.txt`, `selftest-postfix.txt`.

```
$ git apply arms-only.patch        # the self-test arm, WITHOUT the fix
$ python3 -B verifiers/verify_corpus_integrity.py --self-test
FAIL pointer/rev/dead: got (3, 3) want (2, 3)
self-test: 1 failure(s) over 165 assertions
exit=1

$ git apply Kb80E04DeadPointer.patch      # fix + arm
$ python3 -B verifiers/verify_corpus_integrity.py --self-test
self-test: 0 failure(s) over 165 assertions
exit=0
```

Assertion count: base 164 → with the arm 165 (`self-test: 0 failure(s) over 164 assertions` at
base, `over 165` after). The floors gate reads the row as
`PASS corpus_integrity observed=165 floor=164` (`floors-repair.txt`) — i.e. the arm is ABOVE the
published floor, so the floor still passes; the arm is not itself floored (r79 §7 B2 remains
true: dropping the arm later still reads PASS at floor 164). I did not touch
`verifiers/floors-registry.json` (a registry-only bump reds the guard, per r79).

## 4. The live gate: what moved and what did not

Same scratch clone, one command each, exit status captured by the command itself.

Base (instrument bytes reverted to `398cbe1`) — receipt `integrity-base.txt` / `.json`:

```
corpus.index    tracked=152 unindexed=1 stale=0 missing=0  (169 FILE-column patterns over 151 md files)
corpus.pointers report_dead=1/109 commit_total=46 unresolvable=2 nonhash=0 ...
           report_dead: corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md
3/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
  corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_total,
  corpus.pointers.commit_unresolvable
exit=1
```

Repaired — receipt `integrity-repair.txt` / `.json`:

```
corpus.index    tracked=152 unindexed=1 stale=0 missing=0  (169 FILE-column patterns over 151 md files)
corpus.pointers report_dead=0/109 commit_total=46 unresolvable=2 nonhash=0 ...
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
  corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
exit=1
```

**The whole observation diff base→E04 is exactly two keys** (computed over the two `--json`
receipts, key by key over every observed field):

```
DIFF report_dead       1 -> 0
DIFF report_dead_detail ['corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md'] -> []
```

Every other observation is byte-identical, including `commit_total 46`, `commit_unresolvable 2`,
`report_total 109`, `tracked_files 152`, `unindexed 1`. So E04 is **neutral** on the commit
classes (repair 5's business) and on the index classes (repair 3's business).

The independent gate is untouched by E04 and already reads the corpus answer at base:
`report_dead: 0 of 119 candidates` at base (`independent-base.json`) and `report_dead: 0` with
the repair (`independent-repair.json`) — the two gates agree on `checked=106/109, dead=0` after
the repair, as the r79 seat measured.

Fleet-shaped sandbox (the shape the tip battery builds: a clone of the lane plus the fleet
root's other entries symlinked beside it) — receipt `integrity-fleet-shaped-sandbox.txt`:
`report_dead=0/109`, the same five remaining DRIFTs. The repair holds in that shape too.

Which hop resolves it (`which-hop.txt`, `probe_which_hop.py`):

```
citing dir        : /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons
lane repo (hop 1) : /home/vgpnk/Projects/shokunin/kotoba-shokunin
  git cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md' -> rc=128     (lane has no round-77 report)
fleet repo (hop 2): /home/vgpnk/Projects/shokunin
  git cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md' -> rc=0       (the fleet carries it)
lane working tree has the path: False
fleet working tree has the path: True
```

So the live token resolves through the **fleet hop**, as designed: the report it names is a
fleet artefact, the lane has never carried it.

## 5. Held-out classes: no new false red, no lost green

Probe (independent, in my scratch, loading the instrument from the clone):
`probe_rev_pointer.py`, receipts `probe-base.txt` (base bytes) and `probe-repair.txt`
(repair bytes). Each row is one token class, resolved by `report_pointer_exists` against a
fixture lane repo + fixture fleet repo:

| class | token | base | repair | expected |
|---|---|---|---|---|
| A rev-in-lane | `HEAD:.ufo/reports/round-60/kotoba.md` | False | **True** | True (the repair's purpose) |
| B rev-in-fleet | `HEAD:.ufo/reports/round-61/kotoba.md` | False | **True** | True |
| C rev-in-lane, file UNCOMMITTED in the lane worktree | `HEAD:.ufo/reports/round-62/kotoba.md` | False | False | False — a revision-resolving predicate cannot be bought by an uncommitted file |
| D rev absent from both | `HEAD:.ufo/reports/round-99/kotoba.md` | False | False | False |
| E unresolvable revision | `nosuchrev:.ufo/reports/round-60/kotoba.md` | False | False | False |
| F bare in lane | `.ufo/reports/round-60/kotoba.md` | False | False | unchanged |
| G bare absent | `.ufo/reports/round-98/kotoba.md` | False | False | unchanged |
| H absolute, absent | `/nonexistent/abs/report.md` | False | False | unchanged |
| I relative two-up | `../../.ufo/reports/round-60/kotoba.md` | True | True | unchanged (green stays green) |

Only A and B flip, and they flip **green** — the repair cannot turn an alive pointer dead, and
classes D/E (the two negatives the arm pins) stay dead. That is the r79 Q18 claim re-verified
against the round-80 base bytes, plus one extra class (C) that shows the working-tree reading
cannot be satisfied by an uncommitted file.

## 6. Composition with the other repairs: measured, order-independent

`.ufo/waves/round-80/build/Kb80E04DeadPointer/compute-combined-blob.sh <grammar-patch>` prints
the composed blob, the patched independent blob, and the six-instrument numstat against the
pinned battery base `072048fa8e8a52c707d25f7079772fa317244eb7` (the base the `instrument-size`
and `instrument-pin` guards diff against — **not** `398cbe1`).

Applied to the published stack `Kb80Y01-simplified.patch` (the one stack carrying a grammar
class today) on base `398cbe1`, `git apply --check` rc=0:

```
integrity blob (E04+grammar): cc182613a4d089c41e44f11b50e03b45ce582dd8
independent blob (grammar)  : 89f392daab3e4181db3ded7676ca0879871ef7ff
six-instrument numstat vs base 072048fa:
22	3	verifiers/check_assertion_floors.py
75	4	verifiers/verify_corpus_independent.py
113	1	verifiers/verify_corpus_integrity.py
```

My E04 hunk is inside that stack **byte-identically**: I extracted Y01's hunks for
`verifiers/verify_corpus_integrity.py` and compared the added lines — Y01's
`@@ -272,6 +274,12 @@ def resolve_pointer` hunk's added lines equal my patch hunk #1's added
lines exactly (True). So `cc1826…` genuinely is E04∘grammar, not "grammar instead of E04".

Order independence, measured: E04-first then grammar → `cc1826…`; grammar-first then E04 →
`cc1826…` — identical (git applies the second patch with an offset in that order; the resulting
content is the same).

Size arithmetic (the guard's own): base spend at `398cbe1` is **22 added / 3 deleted**, all in
`verifiers/check_assertion_floors.py` (the r76 D4 bump, not mine); E04 adds **17/0**; so the
grammar class has **21 added lines across BOTH corpus gates** under the erratum's cap 60 — the
plan's arithmetic exactly ("22 already spent at base + 17 E04 + grammar ≤ 21 = 60"). The Y01
stack lands at 59 added / 10 deleted and its `instrument-size` guard reads PASS.

## 7. What the composed stack's tip battery reads (a world I assembled, in my scratch)

I assembled the stack world from published bytes only — `Kb80Y01-simplified.patch` (which carries
E04 + the grammar class + the amended counter + the coverage rows + the baseline refresh +
the symlink + the registry rows) applied to base `398cbe1` in a fresh clone
(`clone3`), committed as `4d700ff0a72f5778d2f36402257c721ea1d4eab9`. Recipe:
`recipe-composed-stack.sh`. This is evidence for the L1, **not** a claim score.

Absolute form (receipt `tipbattery-composed-stack-abs.txt`):

```
$ python3 -B verifiers/check_tip_battery.py --rev 4d700ff0… --repo "$S/clone3" --fleet /home/vgpnk/Projects/shokunin
measured rev 4d700ff0… in a fleet-shaped sandbox; base 072048fa…
guarded paths 586, deleted 0; floors 15 rows; instruments added 59 / deleted 10 lines (cap 60); spotcheck base files 27
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0
gate verifiers/check_assertion_floors.py exit 0 wall 109.9s
gate verifiers/verify_skill_checklist.py exit 0
gate verifiers/verify_corpus_integrity.py exit 0
gate verifiers/verify_corpus_independent.py exit 0
gate verifiers/check_correction_sweep.py exit 0
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6
exit=0
```

Dot form (`--repo .`, run from the lane root of the scratch tree, same real fleet root —
receipt `tipbattery-composed-stack-dot.txt`): identical readings, `guards 5 of 5; tip battery
exit 0: 6 of 6`, `exit=0`.

**A scratch-environment caveat, named because it is a red I hit and diagnosed rather than
hidden.** My first two dot-form attempts put the lane copy in a *synthetic* fleet-shaped parent
(my own directory tree with symlinks) and read `4 of 6`: `check_assertion_floors.py` exit 1 and
`verify_skill_checklist.py` exit 1. Diagnosis (receipt
`dotform2-checklist-synthetic-fleet-parent.txt`): the checklist's `governance.citation_resolves`
row resolves fleet-root-relative tokens such as `../kasegi-shokunin/corpus/instruments/resolve.py`
from the lane's *parent directory* — in my synthetic parent those siblings were absent, so the
row could not resolve them. With the real fleet root as the parent the same stack reads 6 of 6.
So that red is an artefact of my sandbox's shape, not a property of the stack. I kept both
receipts (`tipbattery-composed-stack-dot-SYNTHETIC-FLEET-PARENT.txt`,
`dotform2-checklist-synthetic-fleet-parent.txt`) so the diagnosis is on the record.

### E04-only stack, for the pin's sake (receipt `tipbattery-repair.txt`, `…-dotform.txt`)

At my E04-only rev `83f6dc055308d889bf91a229457149cde61d38a0` under the **frozen round-72
counter** (the pins do not include my blob yet):

```
guard instrument-size PASS
FAIL guard instrument-pin: verifiers/verify_corpus_integrity.py blob 051b8c5f… at 83f6dc0… is not a pinned blob
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 1
gate verifiers/check_assertion_floors.py exit 1
gate verifiers/verify_skill_checklist.py exit 1
gate verifiers/verify_corpus_integrity.py exit 1
gate verifiers/verify_corpus_independent.py exit 1
gate verifiers/check_correction_sweep.py exit 0
fleet root /home/vgpnk/Projects/shokunin; guards 4 of 5; tip battery exit 0: 1 of 6
exit=1
```

i.e. on an E04-only stack the **only** guard that moves is `instrument-pin` — the signature for
the W4/W6 worlds, and the reason the erratum must pin the composed blob.

## 8. Deliverables and their exact values

| file | kind | value |
|---|---|---|
| `.ufo/waves/round-80/build/Kb80E04DeadPointer.patch` | plain `git apply` diff vs `398cbe1` | 1 file, +17/−0; sha256 `d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78` (identical to the r79 patch) |
| `.ufo/waves/round-80/build/Kb80E04DeadPointer.blob` | one line, E04-ONLY blob | `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f  verifiers/verify_corpus_integrity.py` |
| `.ufo/waves/round-80/build/Kb80E04DeadPointer.composed-blob.txt` | composed (E04∘grammar) blob values + provenance | integrity `cc182613a4d089c41e44f11b50e03b45ce582dd8`, independent `89f392daab3e4181db3ded7676ca0879871ef7ff` |
| `.ufo/waves/round-80/build/Kb80E04DeadPointer/` | 31 files (26 receipts + 3 recipes + 2 probes) | see the file list below |

The E04-only blob is the **cross-check** value; the L1's plan Addendum 1 states the pin is the
composed blob, and E06's published counter patch pins `cc1826…` / `89f392…` — consistent with
what I measured.

Receipts in `.ufo/waves/round-80/build/Kb80E04DeadPointer/`:

```
selftest-arms-only-redbefore.txt          the red-before proof (fix removed, arm present), exit=1
selftest-postfix.txt                      self-test with fix + arm, exit=0
arms-only.patch                           the arm alone (recipe for the red-before)
integrity-base.txt / integrity-base.json  live gate at base (instrument bytes reverted)
integrity-repair.txt / integrity-repair.json   live gate with the repair
integrity-E03plusE04.txt                  live gate with E03's published rows + E04
integrity-fleet-shaped-sandbox.txt        live gate inside a fleet-shaped sandbox
independent-base.json / independent-repair.json   the independent gate, base and repaired
floors-repair.txt                         check_assertion_floors at the repaired rev
probe_rev_pointer.py + probe-base.txt + probe-repair.txt   the held-out class probe (§5)
probe_which_hop.py + which-hop.txt        which hop resolves the live token
tipbattery-repair.txt                     tip battery at the E04-only rev (absolute form)
tipbattery-repair-dotform.txt             tip battery at the E04-only rev (--repo . form)
tipbattery-composed-stack-abs.txt         tip battery at the composed stack (absolute form)
tipbattery-composed-stack-dot.txt         tip battery at the composed stack (--repo . form)
tipbattery-composed-stack-dot-SYNTHETIC-FLEET-PARENT.txt   the sandbox-shape red, kept for the record
dotform2-checklist-synthetic-fleet-parent.txt               its diagnosis
composed-stack-rev.txt / -integrity-blob.txt / -independent-blob.txt   the composed stack's rev and blobs
compute-combined-blob.sh                  one command to recompute the composed blobs for any grammar patch
recipe-selftest-arms-and-fix.sh           recipe for the red-before / green-after pair
recipe-composed-stack.sh                  recipe for the composed-stack measurement
reference-S07-quality-world-normalized.patch   a reference grammar diff (NOT a proposal; 171 added lines, over budget)
BLOB-SEMANTICS.md                         what the published shas mean and which pin to use
```

## 9. Risks, residuals, blockers — named, not repaired

1. **The repair resolves `HEAD` at measurement time.** The fleet hop asks
   `git -C <fleet> cat-file -e HEAD:.ufo/reports/round-77/kotoba.md`; the fleet's HEAD carries
   that path today (`git cat-file -e` rc=0; the report's own commit `5d1f2e5a` is an ancestor of
   fleet HEAD `0428b7ef`) but the path is **absent at fleet `HEAD~50`**. So the verdict is a
   presence check at a moving ref, not at a pinned commit: a fleet history rewrite that drops
   the report would silently re-red the row. Same class as r79 §8 residual 2; not repaired by me
   (the honest alternative — pinning a commit — would change what the citation means).
2. **E04 alone cannot be measured as 6 of 6** under any counter that lacks the composed pin:
   its own receipt shows `guards 4 of 5` with `instrument-pin` as the single red. The erratum
   fixes it; the composed blob is published (§8).
3. **The grammar class and E04 both edit `verifiers/verify_corpus_integrity.py`.** Whoever
   integrates must apply them so the resulting file matches the pinned composed blob
   `cc1826…`; my helper computes it, and the composed value is order-independent.
4. **The floor for `corpus_integrity` stays 164 while the observed count is 165** (r79 §7 B2):
   the new arm is above the floor, so the gate is green, but the arm is not itself floored —
   dropping it later still reads PASS. A real bump needs `EXPECTED_INSTRUMENTS`, `INSTRUMENTS`
   and `verifiers/floors-registry.json` moved together (a registry-only bump reds the guard,
   per r79). Not my file; not repaired by me.
5. **The coverage rows and the files they promise must land together.** With E03's published rows
   applied and the two new corpus files absent, the index block reads `unindexed 0, stale 2,
   missing 2` (`integrity-E03plusE04.txt`) — the rows promise `lessons/round-80.md` and
   `knowledge/allowed-tools-surfaces-round80.md`, which are not tracked yet. Not my item (E03/S08
   own it); I measured it because the baseline refresh's refusal order depends on it.
6. **The two live `commit_unresolvable` tokens are not the ones the plan named.** Measured on
   both corpus gates at `398cbe1`: the blockers are `corpus/SOURCES.md:171` and `:172`, **both**
   the hash `7bb48f213ac677f943d5c791199ed3dddf302f00`; the plan's `451a02ff` / `cfb894a5` are
   `commit_quoted` context. The L1's plan Addendum 2 already records this correction. I do not
   touch `corpus/SOURCES.md` (M45 pattern: no rewriting of citation rows).
7. **Scratch hygiene.** Two of my own defects, caught and repaired mid-run, recorded for
   honesty: (a) two concurrent git commands in one clone collided on `.git/index.lock` (I
   re-ran the affected measurement serially in a fresh clone — the numbers quoted above come
   from the serial re-runs); (b) my first "dot-form" runs put the lane copy in a synthetic
   fleet parent, which red-coded two gates for an environmental reason (§7). No lane file,
   index, commit or scratch path outside my own directory was touched; the lane tree shows only
   untracked `.ufo/waves/round-80/**` paths (other seats' outputs) and no staged change.

## 10. What the L1 should do with this

1. Land `.ufo/waves/round-80/build/Kb80E04DeadPointer.patch` (or the identical bytes already
   embedded in the stack patches) on top of the base; the composed integrity blob must then be
   `cc182613a4d089c41e44f11b50e03b45ce582dd8` for the pin to hold — recompute with
   `compute-combined-blob.sh` if the grammar bytes differ from Y01's.
2. Verify after integration (each command's own exit status):
   `python3 -B verifiers/verify_corpus_integrity.py --self-test` → 0 failures / 165 assertions;
   `python3 -B verifiers/verify_corpus_integrity.py` → `report_dead 0` and, after the baseline
   refresh, exit 0; `python3 -B verifiers/check_tip_battery.py --rev <tip> --repo .` and the
   absolute `--repo <lane>` form → `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0.
3. Do not re-pin `051b8c5f…` alone: it is the E04-only cross-check value; the pin needs the
   composed blob.

VERDICT: The E04 dead-report-pointer repair ports to the round-80 base unchanged and byte-identically (patch sha256 d7169dd8…, `git apply --check` rc=0 on base and on the lane tip; self-test 0/165 green, arms-only red-before `FAIL pointer/rev/dead: got (3, 3) want (2, 3)` exit 1); it moves the live gate's `report_dead` 1→0 with every other observation byte-identical, and the composed E04∘grammar blobs are measured and published (integrity `cc182613a4d089c41e44f11b50e03b45ce582dd8`, independent `89f392daab3e4181db3ded7676ca0879871ef7ff`, order-independent) so the erratum's pin can carry the composed value — E04-only `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` is the cross-check value, not the pin.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.patch (sha256 d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78); /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.blob; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.composed-blob.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer/ (31 files: 26 receipts, 3 recipes, 2 probes); /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E04DeadPointer.md
