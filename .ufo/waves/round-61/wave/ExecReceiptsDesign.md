# Round 61 — ExecReceiptsDesign: integration receipt formats (three files)

Seat: `kotoba-r61-wave-ExecReceiptsDesign` (executor, axis: operability).
Report path (lane-relative): `.ufo/waves/round-61/wave/ExecReceiptsDesign.md`.
Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated; read-only to this seat except this report).
Date: 2026-10-23 (hyaku run 5, round 61 attempt 1). All measurements below were run by this seat, read-only, in the lane repo
or in scratch under `/fast/scratch/hyaku/kotoba-r61/ExecReceiptsDesign/`.

**Scope of this seat's write:** this report only. No lane, fleet, sibling, `.ufo/state`, jj, or git-index file was written,
staged, committed, or pushed by this seat. No dispatch, no subagent, no ask tool.

**Outcome in one line:** three paste-verifiable receipt templates are delivered (world receipt, controls-ancestry receipt,
C1 measurement receipt), each with named `<PLACEHOLDERS>`, plus the commit order the L1 must follow for R-f to be true.

---

## 1. Ground verified by this seat (read-only; commands, outputs, `date -u`, exit codes)

### 1.1 The frozen R-f arm is a two-substring grep — and it fails on the house `exit=0` style

Read from the committed checker at `master` (`verifiers/check_routed_repairs.py`, blob sha256
`b26528043141b024970d3300ea3b299ce2d4d4eef595cab3ca8d09317014c979`, working copy byte-identical to the `master` blob):

```python
    ancestry = blobs.get(".ufo/waves/round-61/receipts/controls-ancestry.txt")
    rf = (
        ancestry is not None
        and "merge-base --is-ancestor" in ancestry
        and "exit 0" in ancestry
    )
```

Probed directly against a scratch copy of that same file (`/fast/scratch/hyaku/kotoba-r61/ExecReceiptsDesign/checker_copy.py`,
sha256 identical to the lane's) by calling the checker's own `check_repairs()` with a synthetic blob map
(`date -u` 2026-10-23T19:26Z, python 3.14.8):

```text
space exit 0 + invocation                     -> R-f ok = True
equals exit=0 + invocation                    -> R-f ok = False
only invocation                                -> R-f ok = False
only exit 0                                   -> R-f ok = False
prose only                                    -> R-f ok = False
exit 0 elsewhere (unrelated cmd)              -> R-f ok = False
```

Consequences the templates below are built around:

- The literal is **`exit 0` with a space**. `exit=0` (equals — the house style of the r60 `C1-measure.txt` and the
  census-after file) does **not** satisfy R-f. This is the single highest-risk token in the whole C2 arm.
- Both substrings must be present; neither alone suffices.
- The arm does **not** check that the `exit 0` belongs to the merge-base command, that the hashes resolve, or that the
  commits are distinct. A prose disclaimer carrying both literals scores R-f (confirmed above: "prose only" → True).
  The template therefore makes the receipt **substantive**, not merely greppable.

### 1.2 `git merge-base --is-ancestor` edge semantics, measured in the lane

`date -u` 2026-10-23T19:40Z and 2026-10-23T20:01Z, in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`:

```text
$ git merge-base --is-ancestor f3246d1493b60ea1c0d947a19c39f9e08e92f326 7827628
exit=0
$ git merge-base --is-ancestor 7827628 f3246d1493b60ea1c0d947a19c39f9e08e92f326
exit=1
$ git merge-base --is-ancestor master master
exit=0                      # reflexive: A==A also exits 0
$ git merge-base --is-ancestor 7827628 master; echo "exit $?"
exit 0
$ git merge-base --is-ancestor master 7827628; echo "exit $?"
exit 1
$ git rev-list --count 7827628..master
9
$ git merge-base 7827628 master
7827628a939b0333c89892dfcedc72e390ccfb60
$ test "$(git rev-parse 7827628)" != "$(git rev-parse master)"; echo "exit $?"
exit 0
```

Four measured facts the template depends on: (a) a commit is an ancestor of itself, so the inequality check is
**mandatory** — without it a degenerate same-commit pair passes; (b) argument order matters, so the pasted invocation
must show `<C_CTL> <C_DATA>` in that order; (c) `git merge-base A B` prints `A` itself when `A` is an ancestor of `B`
— a **self-checking** output line the reviewer can diff byte-for-byte, which no cosmetic receipt can fake; (d) the
lane's `HEAD` is detached (`git branch --show-current` prints empty; `git rev-parse --abbrev-ref HEAD` → `HEAD`), so
the canonical tip ref is `refs/heads/master` — `git rev-parse master`, never `HEAD` and never `@{u}`.

### 1.3 Lane-identity requirement

```text
$ git log -1 --format='%an|%ae|%cn|%ce' master
kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local
$ git log -1 --format='%an|%ae|%cn|%ce' f3246d1493b60ea1c0d947a19c39f9e08e92f326
protocol-shokunin|protocol@shokunin.local|protocol-shokunin|protocol@shokunin.local
```

`scripts/hyaku/jj-lane.sh` (`repo_path_allowed`, `candidate_has_identity`, push preflight) enforces
`user.name=<id>-shokunin` / `user.email=<id>@shokunin.local` for **author and committer**, and prints exactly one
citable hash line, `landed <hash>`, after `git ls-remote` verifies the remote tip. The base `f3246d1` is a live
counterexample: it is an ancestor of the tip yet carries a non-lane identity, so "exists + is an ancestor" is not
sufficient.

### 1.4 The committable-path gate permits the three target paths

`scripts/hyaku/jj-lane.sh` `repo_path_allowed()` rejects only `.git`, `.jj`, `.ufo` (the driver-runtime root), `.ufo/state`,
`.ufo/state/*`, `.ufo/watchdog.log`. `.ufo/waves/...` is **not** rejected — proved by the already-landed freeze commit
`7827628`, which committed `.ufo/waves/round-61/controls/C2-base.txt` (and `.ufo/waves/round-61/census-before.txt`,
`.ufo/waves/round-61/wave/*`). So all three target paths below are committable by the L1 through `jj-lane.sh commit`.

### 1.5 The frozen predicate sentence is byte-stable and extractable by an anchor

The plan's predicate block at `master` (`plans/round-61.md` lines 50–54) is unchanged since the freeze commit
`7827628` — same digest at both:

```text
$ git show 7827628:plans/round-61.md | sed -n '50,54p' | sha256sum
820d481c0a65b9f4acabdc5cf4a55fd568a0532ad82f6a054ea635e0879a2824  -
$ git show master:plans/round-61.md | sed -n '50,54p' | sha256sum
820d481c0a65b9f4acabdc5cf4a55fd568a0532ad82f6a054ea635e0879a2824  -
$ git show master:plans/round-61.md | sed -n '51,54p' | sha256sum
a35f4540fd8f33b3e4abc293fca8a1623be7dde6e14c69d71c75e3d53e714284  -
```

The block is also extractable **by content anchor**, not by fragile line numbers — this is the extraction the receipt
must be checked against, so that a later plan edit that shifts line numbers does not silently change the echoed
sentence:

```sh
git show <PLAN_REV>:plans/round-61.md \
  | awk '/^\*\*C1 predicate/{f=1} f{print} f&&/^command at base/{exit}' \
  | sha256sum
# -> 820d481c0a65b9f4acabdc5cf4a55fd568a0532ad82f6a054ea635e0879a2824  -
```

(verified at `7827628` and at `master` — identical digest both times; `date -u` 2026-10-23T20:05Z.)

The predicate sentence verbatim (5 lines, from `plans/round-61.md` lines 50–54 at `master`):

```text
**C1 predicate (same sentence in plan, counter label, receipt):**
`python3 -B verifiers/check_scoped_rules.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
`python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0 while the same
command at base `f3246d14` exits 1.
```

### 1.6 The C1 base conjunct is v3-specific — the receipt must say so or a reader can "refute" it

The r60 data commit `7b80ae8` is an **ancestor** of the r61 base `f3246d1` (measured `git merge-base --is-ancestor
7b80ae8 f3246d14` → exit 0), and the counter bytes that matter did not change between them
(`git diff --stat 7b80ae8 f3246d14 -- SKILL.md corpus/SOURCES.md corpus/knowledge/scoped-rules-round60.md
corpus/lessons/round-60.md .ufo/waves/round-60/snapshots verifiers/check_scoped_rules.py` → only 2 files, 4 insertions /
3 deletions, in the entry and lesson prose). Measured with the **committed v2 counter** at the base rev, live
(`date -u` 2026-10-23T20:02:20Z):

```text
$ timeout 300 python3 -B verifiers/check_scoped_rules.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
exit=0
```

**Under v2 the base conjunct is false** (v2 exits 0 at base). It becomes true under v3 by the E2d mechanism
(A1's canonical key set is read from the committed S112–S115 SOURCES rows at the measured revision; those rows do not
exist at `f3246d14` — measured `git show f3246d14:corpus/SOURCES.md | grep -cE '^\| S11[2-5] '` → **0** — so the key set
is empty, no row can satisfy A1, `found = 0 < TARGET`, exit 1). **Therefore the C1-measure receipt must carry the v3
counter sha256 on every run line**, so that a reader who mistakenly runs v2 at base cannot read the receipt as
refuted. This is the receipt's most load-bearing honesty feature.

### 1.7 The world-count trap: W0 is an extra arm, so a naive grep returns 8

The plan freezes **seven** counted worlds (W1–W7) and names **W0 as a do-nothing extra**; the predicate sentence says
`worlds reject 7 of 7`. Measured on a probe file carrying all eight rows:

```text
naive:    grep -cE '^W[0-9]+ .* exit 1$'  -> 8
scoped:   grep -cE '^W[1-7] .* exit 1$'  -> 7
W0 only:  grep -cE '^W0 .* exit 1$'      -> 1
```

A reviewer who greps the whole receipt for `^W[0-9]+ .* exit 1$` will count 8 and read it as a contradiction of "7 of 7".
The world receipt must therefore **state the counted set explicitly** and carry the scoped count command, so the
"7 of 7" claim is derived, not asserted. This is also why the world's `exit` column must carry the polarity inline.

### 1.8 The frozen C2 checker's own self-test passes, and the base control is 0 of 6

```text
$ python3 -B verifiers/check_routed_repairs.py --self-test          # date -u 2026-10-23T19:45:41Z
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

The committed base control `.ufo/waves/round-61/controls/C2-base.txt` reads
`routed repairs verified 0 of 6` / `base-exit=1` — matching the checker's own base-world arm.

### 1.9 The `census-after.txt` arm crashes on an empty file (adjacent risk, for the L1)

Probed by calling `check_repairs()` and `main()` on the scratch copy with an empty or whitespace-only census blob:

```text
census empty            -> EXCEPTION IndexError: list index out of range
census whitespace only  -> EXCEPTION IndexError: list index out of range
census missing          -> 1 of 6   (clean "missing" verdict)
main raised IndexError list index out of range
```

The R-d arm indexes `[-1]` of the non-blank lines without a length guard, so an **empty** `census-after.txt` makes the
whole counter raise instead of scoring 5 of 6 — a crash, not a verdict. The L1 must write the census-after file with a
real body ending in the literal `exit=0` (the r60 `census-before.txt` shape: rows then `exit=0`), never a 7-byte file.
This is outside this seat's three files, but it is the neighbouring receipt in the same commit and would take the C2
measurement down with it.

---

## 2. Template 1 — `.ufo/waves/round-61/receipts/C1-worlds.txt`

**Role:** the pre-data control receipt. It is committed **before** the L1's first C1 `--fetch` measurement (M90) and it
is what a reader re-runs to check that the seven worlds reject and the four eligible rows pass under the *frozen v3
counter bytes*. It is not read by `check_routed_repairs.py` (that checker reads only `LOG.md`, `corpus/QUALITY.md`,
`corpus/lessons/round-61.md`, `census-after.txt`, `receipts/controls-ancestry.txt`) — its authority is the **C1
predicate**, which is a different counter.

### 2.1 Format contract

- **Header block** (comment lines starting `#`): what the file is, the lane path, the writer, `date -u`, the frozen
  counter path + sha256 + the revision it was frozen at, the world-fixture root, and the **counted-set statement**.
- **Command block**: for each world, the exact command line, its raw stdout/stderr, and the observed exit code.
- **Summary block**: exactly one line per world, in the format `W<n> <name> exit <code>` — the format this seat's
  assignment fixes. The `<name>` is the frozen world label from `plans/round-61.md`; the `<code>` is the **observed
  process exit code of that world's evaluation**, and the receipt must define the polarity inline so `exit 1` is
  never misread as "the check failed".
- **Positivity block**: the four eligible rows with their pass results and the counter's own
  `worlds reject 7 of 7; eligible rows pass 4 of 4` line, pasted verbatim from the counter's stdout.
- **Digest block**: the sha256 of the counter file and of the fixture tree, so a reviewer can prove the bytes scored.

### 2.2 Template (copy-ready; every `<...>` is a named placeholder)

```text
# C1 world receipt - round 61, counter v3 (pre-data controls)
# lane repo: /home/vgpnk/Projects/shokunin/kotoba-shokunin
# written by: kotoba L1 round 61 (KotobaR61) via scripts/hyaku/jj-lane.sh commit --as kotoba
# date -u: <UTC_NOW>
# counter: verifiers/check_scoped_rules.py
# counter sha256: <COUNTER_SHA256>   (frozen at commit <COUNTER_FREEZE_REV>)
# world fixture root: .ufo/waves/round-61/worlds/
#
# COUNTED SET: the frozen seven are W1-W7 ("worlds reject 7 of 7").
# W0 is an EXTRA do-nothing arm (the base/no-section world) and is NOT counted in the 7 of 7.
# Counted seven, derived (not asserted):
#   $ grep -cE '^W[1-7] .* exit 1$' .ufo/waves/round-61/receipts/C1-worlds.txt
#   7
#   $ grep -cE '^W0 .* exit 1$' .ufo/waves/round-61/receipts/C1-worlds.txt
#   1
# A whole-file grep '^W[0-9]+ .* exit 1$' returns 8 - that is 7 counted + 1 extra arm, not a contradiction.
#
# POLARITY (read before reading any exit code below):
#   For a world row, exit 1 = the counter REJECTED that world (rows not backed) = the REQUIRED outcome.
#              exit 0 = the counter backed that world = a FAILURE (plan kill rule: any world exits 0 -> C1 fails).
#   For an eligible-row row, exit 0 = that eligible row passed (backed and live-found) = REQUIRED;
#              exit 1 = that eligible row failed = a FAILURE.
#
# --- world evaluations (command block) ---
# Each world is evaluated through the counter's production public main() path at its own fixture revision.
# Every world block names: fixture tree path, fixture commit, tree digest, command, raw stdout/stderr, exit code,
# and the rejecting arm / failed conjunct.

# --- case: W1 <W1_NAME> ---
# fixture tree: <W1_FIXTURE_PATH>
# fixture commit: <W1_FIXTURE_REV>
# fixture tree sha256: <W1_FIXTURE_SHA256>
# rejecting arm: <W1_ARM>            failed conjunct: <W1_CONJUNCT>
$ <W1_COMMAND>
<W1_STDOUT>
exit <W1_EXIT>

# --- case: W2 <W2_NAME> ---
# fixture tree: <W2_FIXTURE_PATH>
# fixture commit: <W2_FIXTURE_REV>
# fixture tree sha256: <W2_FIXTURE_SHA256>
# rejecting arm: <W2_ARM>            failed conjunct: <W2_CONJUNCT>
$ <W2_COMMAND>
<W2_STDOUT>
exit <W2_EXIT>

# --- case: W3 <W3_NAME> ---
# fixture tree: <W3_FIXTURE_PATH>
# fixture commit: <W3_FIXTURE_REV>
# fixture tree sha256: <W3_FIXTURE_SHA256>
# rejecting arm: <W3_ARM>            failed conjunct: <W3_CONJUNCT>
$ <W3_COMMAND>
<W3_STDOUT>
exit <W3_EXIT>

# --- case: W4 <W4_NAME> ---
# fixture tree: <W4_FIXTURE_PATH>
# fixture commit: <W4_FIXTURE_REV>
# fixture tree sha256: <W4_FIXTURE_SHA256>
# rejecting arm: <W4_ARM>            failed conjunct: <W4_CONJUNCT>
$ <W4_COMMAND>
<W4_STDOUT>
exit <W4_EXIT>

# --- case: W5 <W5_NAME> ---
# fixture tree: <W5_FIXTURE_PATH>
# fixture commit: <W5_FIXTURE_REV>
# fixture tree sha256: <W5_FIXTURE_SHA256>
# rejecting arm: <W5_ARM>            failed conjunct: <W5_CONJUNCT>
$ <W5_COMMAND>
<W5_STDOUT>
exit <W5_EXIT>

# --- case: W6 <W6_NAME> ---
# fixture tree: <W6_FIXTURE_PATH>
# fixture commit: <W6_FIXTURE_REV>
# fixture tree sha256: <W6_FIXTURE_SHA256>
# rejecting arm: <W6_ARM>            failed conjunct: <W6_CONJUNCT>
$ <W6_COMMAND>
<W6_STDOUT>
exit <W6_EXIT>

# --- case: W7 <W7_NAME> ---
# fixture tree: <W7_FIXTURE_PATH>
# fixture commit: <W7_FIXTURE_REV>
# fixture tree sha256: <W7_FIXTURE_SHA256>
# rejecting arm: <W7_ARM>            failed conjunct: <W7_CONJUNCT>
$ <W7_COMMAND>
<W7_STDOUT>
exit <W7_EXIT>

# --- case: W0 <W0_NAME> (EXTRA do-nothing arm; not counted in 7 of 7) ---
# fixture tree: <W0_FIXTURE_PATH>
# fixture commit: <W0_FIXTURE_REV>
# fixture tree sha256: <W0_FIXTURE_SHA256>
# expected: nothing backed; the counter's own do-nothing verdict
$ <W0_COMMAND>
<W0_STDOUT>
exit <W0_EXIT>

# --- eligible rows (the four r60 eligible rows must still pass) ---
# fixture tree: <ELIGIBLE_FIXTURE_PATH>
# fixture commit: <ELIGIBLE_FIXTURE_REV>
$ <ELIGIBLE_COMMAND>
<ELIGIBLE_STDOUT>
exit <ELIGIBLE_EXIT>

# --- counter's own aggregate line, pasted verbatim from the run above ---
# <COUNTER_WORDS_LINE>
#
# --- summary (one line per world; format: W<n> <name> exit <code>) ---
W0 <W0_NAME> exit <W0_EXIT>
W1 <W1_NAME> exit <W1_EXIT>
W2 <W2_NAME> exit <W2_EXIT>
W3 <W3_NAME> exit <W3_EXIT>
W4 <W4_NAME> exit <W4_EXIT>
W5 <W5_NAME> exit <W5_EXIT>
W6 <W6_NAME> exit <W6_EXIT>
W7 <W7_NAME> exit <W7_EXIT>
#
# --- eligible rows summary ---
# <ELIGIBLE_ROWS_SUMMARY>
#
# --- frozen counter identity (the bytes every line above was produced by) ---
# counter sha256: <COUNTER_SHA256>
# counter commit: <COUNTER_FREEZE_REV>
# fixture tree sha256: <WORLD_TREE_SHA256>
```

### 2.3 Named placeholders for template 1

`<UTC_NOW>` · `<COUNTER_SHA256>` · `<COUNTER_FREEZE_REV>` · `<W0_NAME>`…`<W7_NAME>` · `<W0_FIXTURE_PATH>`…
`<W7_FIXTURE_PATH>` · `<W0_FIXTURE_REV>`…`<W7_FIXTURE_REV>` · `<W0_FIXTURE_SHA256>`…`<W7_FIXTURE_SHA256>` ·
`<W0_ARM>`…`<W7_ARM>` · `<W0_CONJUNCT>`…`<W7_CONJUNCT>` · `<W0_COMMAND>`…`<W7_COMMAND>` · `<W0_STDOUT>`…`<W7_STDOUT>` ·
`<W0_EXIT>`…`<W7_EXIT>` · `<ELIGIBLE_FIXTURE_PATH>` · `<ELIGIBLE_FIXTURE_REV>` · `<ELIGIBLE_COMMAND>` ·
`<ELIGIBLE_STDOUT>` · `<ELIGIBLE_EXIT>` · `<COUNTER_WORDS_LINE>` · `<ELIGIBLE_ROWS_SUMMARY>` · `<WORLD_TREE_SHA256>`.

**Placeholder names are fixed world slots** (W0…W7, E1…), not free text, so a reviewer can diff two drafts
slot-by-slot.

### 2.4 Rules the L1 must honour for template 1

1. **The world labels come from the plan, not from the seat.** W1 `CtlReopenForged d` · W2 `CtlReopenHeldKey b` ·
   W3 `CtlReopenHeldKey a` · W4 `CtlReopenHeldKey c` · W5 wrong scope-key (ExecKeyForms) · W6 invented action ·
   W7 v1-hollow rescore world (regression) · W0 do-nothing extra (`plans/round-61.md` lines 40–43 at `master`).
2. **Every world row is derived from that world's own evaluation**, not from the aggregate line. The counter's
   aggregate (`worlds reject 7 of 7; eligible rows pass 4 of 4`) is **pasted**, and the per-world rows are the
   independent case results. An aggregate printed by the counter is not a world receipt.
3. **No placeholder may survive.** Before committing, `grep -cE '<[A-Z0-9_]+>' <file>` must print `0`; a surviving
   `<PLACEHOLDER>` is an unfilled slot, not evidence.
4. **The `exit` column is the observed process exit code** of the command pasted immediately above it — never a
   hand-written `1`.
5. **The counter sha256 line is mandatory** and must equal `sha256sum verifiers/check_scoped_rules.py` at the
   frozen commit; it is what makes the receipt re-runnable against the same bytes.
6. **W0 must be present and must exit 1** (a do-nothing world backs nothing). It is excluded from the 7 of 7 by the
   counted-set statement, not by omission.
7. **The receipt is committed before any C1 `--fetch` data measurement.** This is the M90 barrier and it is what the
   ancestry receipt's `C_CTL` hash will point at.

### 2.5 Shell-safety of the placeholder syntax (measured)

```text
$ bash -c 'echo <C_CTL_SHA>^{commit}'
bash: line 1: C_CTL_SHA: No such file or directory      # angle brackets = shell redirection
$ bash -c 'echo __C_CTL_SHA__^{commit}'
__C_CTL_SHA__^{commit}
```

Angle-bracket placeholders are **redirection syntax** in a shell. They are fine inside a text file (the receipt is
data, not a script), but a reviewer who pastes an unfilled line into bash gets a redirect error rather than the
intended message. Two consequences: (a) the unfilled-placeholder self-check (`grep -cE '<[A-Z0-9_]+>'` → 0) is the guard
against pasting a half-filled receipt; (b) the receipt's command block should show the **filled** command with the real
hash, not a placeholder, because that is what a reviewer re-runs.

---

## 3. Template 2 — `.ufo/waves/round-61/receipts/controls-ancestry.txt`

**Role:** the R-f receipt. It is what `check_routed_repairs.py` greps, and it is the artifact that shows the control
receipts precede the C1 data in the commit DAG.

### 3.1 The frozen grep contract this file must satisfy (measured, §1.1)

The blob must contain the literal `merge-base --is-ancestor` **and** the literal `exit 0` (space). The template below
satisfies it **and** makes the receipt substantive: the `exit 0` token appears **exactly once**, on the merge-base
verdict line, so the R-f hit cannot be produced by some unrelated command's status. Every other command prints
`status=N` instead of `exit N`. Measured on the template:

```text
$ grep -c 'exit 0' tmpl_ancestry2.txt
1
$ grep -n 'exit 0' tmpl_ancestry2.txt
18:exit 0
```

and the frozen checker scores it:

```text
R-f with my ancestry template -> 5 of 6   (the missing one is R-a in that probe world, not R-f)
  R-a count correction: ok
  R-b landed-scope names: ok
  R-c base-measure pointer: ok
  R-d census-after file: ok
  R-e byte-exact criterion + M91: ok
  R-f controls-ancestry receipt: ok
```

### 3.2 Template (copy-ready)

```text
# Round-61 controls-ancestry receipt (R-f)
# lane repo: /home/vgpnk/Projects/shokunin/kotoba-shokunin
# written by: kotoba L1 round 61 (KotobaR61) via scripts/hyaku/jj-lane.sh commit --as kotoba
# date -u: <UTC_NOW>
# branch tip at writing (git rev-parse master): <TIP>
# C_CTL  = control-receipts commit: counter v3 + world fixtures + receipts/C1-worlds.txt  -> <C_CTL_SHA>
# C_DATA = C1 data commit: the C1 measurement inputs (S112-S115 rows, snapshots, entry, SKILL section) -> <C_DATA_SHA>
#
# The space-separated exit-0 token appears EXACTLY ONCE below, on the merge-base verdict line;
# every other command prints status=N, so the frozen R-f grep cannot be satisfied by an unrelated status.
# The verdict below proves what it says: the reversed invocation must NOT be exit-0.

$ git rev-parse --verify <C_CTL_SHA>^{commit}; echo "status=$?"
<C_CTL_SHA>
status=0

$ git rev-parse --verify <C_DATA_SHA>^{commit}; echo "status=$?"
<C_DATA_SHA>
status=0

$ test "$(git rev-parse <C_CTL_SHA>)" != "$(git rev-parse <C_DATA_SHA>)"; echo "status=$?"
status=0

$ git merge-base --is-ancestor <C_CTL_SHA> <C_DATA_SHA>; echo "exit $?"
exit 0

$ git merge-base --is-ancestor <C_DATA_SHA> <C_CTL_SHA>; echo "status=$?"
status=1

$ git merge-base <C_CTL_SHA> <C_DATA_SHA>
<C_CTL_SHA>

$ git log -1 --format='%H %an <%ae> %cn <%ce>' <C_CTL_SHA>
<C_CTL_SHA> kotoba-shokunin <kotoba@shokunin.local> kotoba-shokunin <kotoba@shokunin.local>

$ git log -1 --format='%H %an <%ae> %cn <%ce>' <C_DATA_SHA>
<C_DATA_SHA> kotoba-shokunin <kotoba@shokunin.local> kotoba-shokunin <kotoba@shokunin.local>

$ git merge-base --is-ancestor <C_CTL_SHA> <TIP>; echo "status=$?"
status=0

$ git merge-base --is-ancestor <C_DATA_SHA> <TIP>; echo "status=$?"
status=0

$ git rev-list --count <C_CTL_SHA>..<C_DATA_SHA>
<C_COMMIT_DISTANCE>

$ git show --stat --oneline <C_CTL_SHA> | head -20
<C_CTL_STAT>

$ git show --stat --oneline <C_DATA_SHA> | head -20
<C_DATA_STAT>
```

### 3.3 Named placeholders for template 2

`<UTC_NOW>` · `<TIP>` · `<C_CTL_SHA>` · `<C_DATA_SHA>` · `<C_COMMIT_DISTANCE>` · `<C_CTL_STAT>` · `<C_DATA_STAT>`.

All four hashes are **full 40-hex lowercase** and must be the hashes the helper printed as `landed <hash>`, never
`HEAD`, never a branch name, never a jj change-id.

### 3.4 What each line buys (why the file is not just two greppable tokens)

| line | what it forecloses |
|---|---|
| `rev-parse --verify <sha>^{commit}` ×2 | a typo'd, invented, or foreign-repo hash; `^{commit}` also proves the object is a commit, not a blob/tree |
| `test "$(git rev-parse A)" != "$(git rev-parse B)"` | the degenerate same-commit pair — `--is-ancestor X X` exits 0 (measured, §1.2) |
| `merge-base --is-ancestor A B` → `exit 0` | the actual R-f claim, in the order the plan states it (controls first, data second) |
| the **reversed** invocation → `status=1` | an argument-order slip: `A B` and `B A` are not symmetric (measured: `B A` exits 1) |
| `git merge-base A B` printing `A` | a self-checking output: the printed bytes must equal the recorded control hash, which a disclaimer world cannot produce |
| `%an|%ae|%cn|%ce` ×2 | the base-commit counterexample (§1.3): a non-lane-identity commit can be an ancestor of the tip and still fail the lane contract |
| `merge-base --is-ancestor A/B <TIP>` ×2 | a receipt naming commits that are not on the branch tip |
| `rev-list --count A..B` + the two `--stat` blocks | role binding: the reviewer confirms A carries the fixtures/receipts and B carries the C1 data, so two old r60 hashes that trivially satisfy ancestry do not survive |

### 3.5 Rules the L1 must honour for template 2

1. **The `exit 0` token appears exactly once**, on the merge-base verdict line. All other statuses are `status=N`.
2. **The receipt lands in its own commit**, after `C_DATA` exists, so it can name `C_DATA`'s hash (a receipt cannot
   name a hash that does not yet exist).
3. **`<TIP>` is `git rev-parse master` at writing time** — the lane's `HEAD` is detached; `master` is the canonical
   ref and the C2 checker's own default measured rev.
4. **The claim is about the commit DAG, not about dispatch order.** The ancestry receipt proves *the control-receipts
   commit is an ancestor of the C1 data commit*. It does not prove the control seats were dispatched before the data
   seats were dispatched — that is a wall-clock/dispatch fact, and only a wave-dispatch or watchdog record can carry
   it. The receipt must not be cited for the stronger claim.
5. **Never edit the frozen checker to make R-f pass.** The arm is weak (two substrings; §1.1), but the repair is the
   substantive receipt plus reviewer re-runs (Q31), not a mid-round checker change (Q28).

---

## 4. Template 3 — `.ufo/waves/round-61/C1-measure.txt`

**Role:** the C1 measurement receipt: the counter sha256 line and the exact frozen predicate sentence, echoed.

### 4.1 The name collision the L1 must decide about (measured, not assumed)

The r60 receipt is `.ufo/waves/round-60/C1-measure.txt` (sha256
`29e88a1591136604feb603378fe441ddc094a4f96e598fcd965dc6708ac085c1`, 21 lines) and it is **after-only**: it measures
`7b80ae80` and contains no base-rev run. The base measurement for r60 lives in
`.ufo/waves/round-60/receipts/freeze2-selftest.txt` (sha256
`d9dca9e69c3dfb608513d552d10c62bd0b0db2957d3e90d282003490d32c8c54`). That asymmetry is exactly what R-c repairs.

The r61 receipt name has **two committed candidates** and they do not agree:

- this seat's assignment and the r60 precedent: `.ufo/waves/round-61/C1-measure.txt`;
- the plan's own erratum E2d (`plans/round-61.md` line 190 at `master`): "pinned verbatim in the v3 counter label and the
  integration receipt `C1-v3-measure.txt`".

The plan text is canonical over the dispatch string for wording (the plan says so of itself in E2d), but the
assignment's path is the one the wave spec and the sibling reviewer (`RevAncestry`) also use. **The L1 must pick one
and use it exactly once.** Two acceptable resolutions, with the trade-off:

- **(A) `C1-measure.txt`** — matches the r60 precedent and the wave spec; the collision with the r60 file is then
  disambiguated by the leading line (below), which names the round, the counter sha256, and the predicate sentence.
  Risk: a reader grepping the lane for `C1-measure.txt` finds two files, one per round.
- **(B) `C1-v3-measure.txt`** — matches the plan's E2d wording exactly; no basename collision with r60. Risk: it
  deviates from the wave spec's path and from the r60 precedent, and the R-c LOG line must still name the **r60**
  `C1-measure.txt` (the checker greps LOG.md for both `receipts/freeze2-selftest.txt` and `C1-measure.txt` on one
  line — a fully-qualified r60 path satisfies it; measured: `True`).

**This seat's recommendation: (B) `C1-v3-measure.txt`**, because the plan is the frozen contract and because it removes
the one ambiguity this round exists to repair — a pointer that names two different artifacts. If the L1 prefers (A),
the leading disambiguation line in §4.2 is then mandatory, not optional.

Whichever is chosen, the **R-c LOG line must fully qualify the r60 paths**, because the checker greps LOG.md for the bare
literals `receipts/freeze2-selftest.txt` and `C1-measure.txt` on one line (measured: a fully-qualified r60 path
`.ufo/waves/round-60/receipts/freeze2-selftest.txt` + `.ufo/waves/round-60/C1-measure.txt` satisfies it) — and the
direction must be stated (base = freeze2-selftest, after-only = C1-measure), since the arm cannot check direction.

### 4.2 Template (copy-ready; path per §4.1)

```text
# Round-61 C1 measurement receipt (counter v3)
# THIS FILE IS ROUND 61. The round-60 receipt is .ufo/waves/round-60/C1-measure.txt and measures a
# DIFFERENT counter (v2, sha256 ca2585a4...) at a DIFFERENT revision (7b80ae80). Do not read one as the other.
# lane repo: /home/vgpnk/Projects/shokunin/kotoba-shokunin
# written by: kotoba L1 round 61 (KotobaR61)
# date -u: <UTC_NOW>
# measured tip (git rev-parse master at measurement time): <TIP>
# base revision (the round-61 base, per the frozen predicate): f3246d1493b60ea1c0d947a19c39f9e08e92f326
# controls receipt commit (the M90 barrier this measurement ran behind): <C_CTL_SHA>
#
# --- frozen counter identity ---
# counter sha256: <COUNTER_SHA256>
# counter commit: <COUNTER_FREEZE_REV>
# (the counter's own stdout prints this same sha256 on every run below - if the two disagree, stop)
#
# --- THE FROZEN PREDICATE (echoed verbatim from plans/round-61.md, 5 lines) ---
# source: plans/round-61.md, extracted by content anchor
#   git show <PLAN_REV>:plans/round-61.md | awk '/^\*\*C1 predicate/{f=1} f{print} f&&/^command at base/{exit}'
# echoed-block sha256: <PREDICATE_BLOCK_SHA256>   (expect 820d481c0a65b9f4acabdc5cf4a55fd568a0532ad82f6a054ea635e0879a2824)
**C1 predicate (same sentence in plan, counter label, receipt):**
`python3 -B verifiers/check_scoped_rules.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
`python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0 while the same
command at base `f3246d14` exits 1.
#
# --- run 1: self-test (the worlds arm) ---
$ <SELFTEST_COMMAND>
<SELFTEST_STDOUT>
exit <SELFTEST_EXIT>
#
# --- run 2: tip, with --fetch (the eligible-rows arm) ---
$ <TIP_FETCH_COMMAND>
<TIP_FETCH_STDOUT>
exit <TIP_FETCH_EXIT>
#
# --- run 3: base, same command, same counter bytes (the base clause) ---
$ <BASE_FETCH_COMMAND>
<BASE_FETCH_STDOUT>
exit <BASE_FETCH_EXIT>
#
# --- verdict ---
# self-test worlds line: <WORLDS_LINE>
# tip --fetch: exit <TIP_FETCH_EXIT>   base --fetch: exit <BASE_FETCH_EXIT>
# C1 predicate met: <C1_PREDICATE_MET>   (yes/no, with the sentence above as the label)
#
# --- limits this receipt does not discharge ---
# - The base clause is TRUE UNDER V3 ONLY. Under committed v2 the same command at f3246d14 exits 0
#   (measured 2026-10-23T20:02:20Z). The v3 sha256 line above is what binds this receipt to v3.
# - A4 authenticates internal provenance consistency of committed bytes; it does not authenticate
#   wall-clock fetch time against a forged commit date.
# - The M90 dispatch-order question is NOT discharged here: the ancestry receipt proves commit-DAG
#   chronology only. Dispatch chronology needs a wave-dispatch/watchdog record.
# - An unrun check has not passed: every exit code above is a pasted observation, not an expectation.
```

### 4.3 Named placeholders for template 3

`<UTC_NOW>` · `<TIP>` · `<C_CTL_SHA>` · `<COUNTER_SHA256>` · `<COUNTER_FREEZE_REV>` · `<PLAN_REV>` ·
`<PREDICATE_BLOCK_SHA256>` · `<SELFTEST_COMMAND>` · `<SELFTEST_STDOUT>` · `<SELFTEST_EXIT>` ·
`<TIP_FETCH_COMMAND>` · `<TIP_FETCH_STDOUT>` · `<TIP_FETCH_EXIT>` · `<BASE_FETCH_COMMAND>` · `<BASE_FETCH_STDOUT>` ·
`<BASE_FETCH_EXIT>` · `<WORLDS_LINE>` · `<C1_PREDICATE_MET>`.

### 4.4 Rules the L1 must honour for template 3

1. **The predicate sentence is echoed byte-for-byte**, from `plans/round-61.md` by content anchor, and the receipt
   carries the sha256 of the echoed block. The expected digest is
   `820d481c0a65b9f4acabdc5cf4a55fd568a0532ad82f6a054ea635e0879a2824` — measured identical at the freeze commit
   `7827628` and at `master` (§1.5). If the digest differs, the plan moved and the receipt must be re-cut.
2. **Every run line carries the v3 counter sha256** (the counter prints it on stdout; the receipt repeats it once in
   the header and the reader can diff the two).
3. **Both arms of the predicate are measured in this one file**: the self-test worlds line (7 of 7 / 4 of 4) and the
   tip/base `--fetch` exits (0 / 1). A receipt carrying only the tip run does not discharge the predicate.
4. **The base run uses the same v3 bytes as the tip run** — the same file, the same sha256. Running the old v2 counter
   at base would exit 0 and look like a refutation (§1.6); the sha256 line prevents that misreading.
5. **The limits block is mandatory.** It names the v3-only base clause, the A4 wall-clock limit, and the
   dispatch-vs-DAG distinction. It is what keeps the receipt from being read as a stronger claim than it is.
6. **The M90 barrier hash is quoted** (`<C_CTL_SHA>`), so the receipt itself names the control commit it ran behind.
7. **No expectation is ever written as an observation.** `<C1_PREDICATE_MET>` is `yes`/`no` derived from the pasted
   exits, and the file states that every exit is pasted.

---

## 5. The commit order the L1 must create commits in, for R-f to be true

This is the ordering the assignment asks for. It is derived from the plan's own commit-order section, the M90 routing
(`corpus/lessons/round-60.md`, §8 of the r60 spot-check: "receipts before probing, controls complete before data
seats"), the plan's C1 text ("runs the 7 committed fixtures (receipts committed before any `--fetch` data
measurement, M90), then measures"), and the checker's blob-read-at-measured-rev behaviour (§1.1: the checker reads
`.ufo/waves/round-61/receipts/controls-ancestry.txt` as a blob **at the rev it measures**, so the receipt must already
be committed at that rev).

Notation: every step is one `scripts/hyaku/jj-lane.sh commit <lane> --as kotoba -m "<msg>" -- <paths>` followed by
`jj-lane.sh push <lane>`. **The only citable hash line is `landed <hash>`**, printed by the helper after
`git ls-remote` verifies the remote tip. Every hash named below is that `landed` value.

```text
  F  7827628a939b0333c89892dfcedc72e390ccfb60   plan freeze (DONE): plan, C2 checker, C2 base control,
                                                 census-before, wave spec/dispatch
  E  ...                                        pre-data errata (E1..E2f) - already landed as lane commits;
                                                 all are ancestors of the tip, all pre-data
  V  <V>                                        counter v3 + the seven world fixtures + the four eligible-row
                                                 fixtures + the frozen counter sha256 record.
                                                 NO C1 data rows, NO snapshots, NO entry yet.
  W  <W>                                        .ufo/waves/round-61/receipts/C1-worlds.txt  (the world receipt).
                                                 *** THIS IS C_CTL. ***  The M90 barrier commit: nothing C1 may be
                                                 measured with --fetch before this commit lands.
  D  <D>                                        the C1 DATA commit: S112-S115 SOURCES rows, the committed
                                                 snapshot bytes, corpus/knowledge/scoped-rules-counter-round61.md,
                                                 the SKILL.md section, the lesson Gate rows.
                                                 (R-a..R-c and R-e may land here or later; R-d needs the census-after
                                                 file, which must exist at the measured rev - so R-d lands at or
                                                 before the measured rev.)
  A  <A>                                        .ufo/waves/round-61/receipts/controls-ancestry.txt  (the R-f receipt).
                                                 *** THIS IS WHAT NAMES <W> AND <D>. ***  It must land AFTER <D>
                                                 (it cannot name a hash that does not exist yet) and BEFORE the
                                                 C1 --fetch measurement, so the ancestry receipt is a PRE-measurement
                                                 barrier, not a post-hoc annotation.
  M  <M>                                        .ufo/waves/round-61/C1-measure.txt (or C1-v3-measure.txt),
                                                 .ufo/waves/round-61/census-after.txt, and any remaining repairs.
                                                 The measurement itself runs at <A> (or at <M>'s parent), and the
                                                 receipt names the measured revision explicitly - never "master".
  R  <R>                                        the round report.
```

**The load-bearing constraints, stated so nothing is lost in handoff:**

1. **`W` (the world receipt) must be an ancestor of `D` (the C1 data commit).** This is the R-f claim. `W` must land
   **before** any C1 `--fetch` measurement — that is the M90 boundary, and it is what makes `W` a control rather than a
   description of a measurement that already happened.
2. **`A` (the ancestry receipt) lands after `D` and before the C1 `--fetch` measurement.** It names `W` and `D`; both
   hashes must already exist when its text is written.
3. **`A` must be an ancestor of the rev the C2 checker measures.** The checker reads the receipt as a blob at its
   measured rev (`git show <rev>:.ufo/waves/round-61/receipts/controls-ancestry.txt`); if the receipt is not committed
   at that rev, R-f scores `missing` and C2 exits 1 with `5 of 6`.
4. **The C2 measurement runs last**, at a rev where all six repair blobs are present: `LOG.md` (R-a/R-b/R-c),
   `corpus/QUALITY.md` + `corpus/lessons/round-61.md` (R-e), `.ufo/waves/round-61/census-after.txt` (R-d),
   `.ufo/waves/round-61/receipts/controls-ancestry.txt` (R-f). Then
   `python3 -B verifiers/check_routed_repairs.py --rev master` prints `routed repairs verified 6 of 6` and exits 0.
5. **One commit per receipt family**, never "controls and data in one commit" — the same-commit case is the M90 shape
   the round exists to repair, and `--is-ancestor X X` exits 0, so a merged pair would look green to the grep while
   being the defect. The `test ... != ...` line in template 2 exists precisely to catch this.
6. **Every one of these commits is a lane-identity commit** (`kotoba-shokunin <kotoba@shokunin.local>` as author **and**
   committer) and every cited hash is a full 40-hex `landed` hash.

---

## 6. Traps this seat measured, ranked by cost if the L1 misses them

| # | trap | measured consequence | guard in the templates |
|---|---|---|---|
| T1 | ancestry receipt written in the house `exit=0` style | R-f scores `missing` → C2 `5 of 6`, exit 1, despite real evidence (§1.1) | template 2 emits the space form `exit 0`, exactly once |
| T2 | ancestry receipt written before `D` exists | the `D` hash cannot be named → the receipt is either absent or names a future hash | template 2's `<C_DATA_SHA>` is a real landed hash; order §5 step A |
| T3 | controls and data landed in one commit | `--is-ancestor X X` exits 0 → the receipt looks green while being the M90 defect | template 2's inequality line; §5 constraint 5 |
| T4 | the world receipt's `exit 1` read as "the check failed" | the C1 predicate is inverted in the reader's head; a correct receipt reads as broken | template 1's POLARITY block |
| T5 | W0 counted with the seven | whole-file grep returns 8 against a `7 of 7` claim (§1.7) | template 1's COUNTED SET block with both scoped greps |
| T6 | a reader runs the **v2** counter at base and "refutes" the base clause | v2 at `f3246d14` exits **0** (§1.6); the receipt looks wrong | template 3's v3 sha256 on every run + the limits block |
| T7 | the world receipt's aggregate line used as the per-world source | one printed total is not seven case results | template 1's rule 2: the aggregate is pasted, the rows are derived |
| T8 | `census-after.txt` empty or whitespace | the R-d arm raises IndexError and the whole C2 counter crashes (not a 5-of-6 verdict) (§1.9) | §1.9 note; the file must carry a real body ending `exit=0` |
| T9 | the ancestry receipt cited as proof of **dispatch** order | it proves DAG chronology only; a dispatch claim needs a dispatch record | template 3's limits block |
| T10 | the r61 receipt named `C1-measure.txt` while the R-c LOG line also names `C1-measure.txt` | two artifacts, one bare name; the exact pointer-ambiguity class M91 repairs | §4.1: pick (A) or (B) once; fully qualify the r60 paths in the LOG line |
| T11 | a placeholder left unfilled in a receipt | a pasted `<C_CTL_SHA>` is a **shell redirect** (§2.5) and an unfilled slot is not evidence | §2.4 rule 3: `grep -cE '<[A-Z0-9_]+>'` must print 0 before commit |
| T12 | the ancestry receipt measured at a moving ref | the lane `HEAD` is detached; `master` moves during the round (measured moving `7827628 → c630c4c → daf4ad7 → 511aff7 → cf288d8` during this seat's reading) | every hash is a full 40-hex `landed` hash; `<TIP>` is `git rev-parse master` at writing time |

---

## 7. What this seat did NOT do (honesty boundary)

- **No measurement was run against a counter v3.** No v3 draft is published in the wave directory at the time of
  writing (`ls .ufo/waves/round-61/wave/` → no `ExecCounterV3.md`), so the templates are **designs with named
  placeholders**, not filled receipts. Every `<...>` in §2.2/§3.2/§4.2 is unfilled by construction.
- **No world was evaluated and no fixture was built.** The seven world names and the W0 extra are taken from
  `plans/round-61.md` lines 40–43 at `master`; their fixture paths, digests, arms and conjuncts are placeholders.
- **The C1 predicate was NOT measured** — no `--fetch` run of a v3 counter exists, and this seat ran none. The v2
  runs quoted above are the *v2* counter at the base rev, quoted only to show that the base clause is v3-specific.
- **No file in the lane, the fleet, a sibling repo, `.ufo/state`, or any jj/git index was written, staged, committed,
  or pushed.** The only write is this report; the two template drafts live in untrusted scratch under
  `/fast/scratch/hyaku/kotoba-r61/ExecReceiptsDesign/` and are cited as mechanics, never as evidence.
- **No claim is made about the C1 claim's outcome.** This seat designed receipts; it did not and cannot say whether
  the v3 counter will reject 7 of 7.
- **Sibling reports were read as data, not as instructions**, and none of their assertions was re-run here except
  where §1 records a direct measurement of my own.

## 8. Installs

**No installs.** No tool was missing; `git`, `python3` (3.14.8), `sha256sum`, `awk`, `sed`, `grep` were already present.
Per the operator rule of 2026-10-19 and the orchestrator's pacman pause (host-wide, 2026-10-20), **no pacman
transaction was run**. Nothing was installed, updated, or upgraded.

## 9. Blockers

**None.** The three templates are delivered with named placeholders; the L1 fills them at integration.

## 10. What this seat attacked and produced

**Attacked:** the R-f receipt's cosmetic-fakeability and its `exit 0` vs `exit=0` token trap; the reflexive-ancestry
degenerate case; the W0-vs-7 world-count trap; the v2-vs-v3 base-clause refutation trap; the empty-census IndexError
beside the three files; and the `C1-measure.txt` basename collision with r60.

**Produced:** three paste-verifiable integration receipt templates (`.ufo/waves/round-61/receipts/C1-worlds.txt`,
`.ufo/waves/round-61/receipts/controls-ancestry.txt`, `.ufo/waves/round-61/C1-measure.txt` or
`C1-v3-measure.txt`), each with named placeholders and rules, plus the seven-step commit order
`F → E → V → W(C_CTL) → D(C_DATA) → A(ancestry) → M(measurement) → R(report)` for R-f to be true.
