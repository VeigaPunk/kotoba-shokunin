# ExecPointersControls — pointer-gate shortcut and hard-negative worlds (round 73, wave 1)

Seat `kotoba-r73.ExecPointersControls` (executor, leaf; no dispatch). Lane `kotoba-shokunin`, branch
`master`, base `072048fa8e8a52c707d25f7079772fa317244eb7`, plan `b337035`. I wrote no committed lane file
(`git status --porcelain | grep -v '^?? .ufo/waves/round-73/'` printed nothing after the whole battery).

## Verdict

**The control battery is delivered and all 19 readings match at the gate's final freeze candidate
`sha256:2537a22733c45e58da387777ed9e632e03f0819a54761cf0875db23659ddddf6` (40,352 B, `--self-test` 0
failures over 57 assertions, RED-BEFORE `34 of 37` exit 1).** Four of my worlds read pass-but-should-not
(or fail-but-should-pass) on earlier drafts; all four are now fixed in the gate, and so is the cross-round
nearest-name residual (F8), so the worlds double as regression pins. One item remains for the L1's freeze
addendum: the counter still prints its old frozen sentence ("exit 0 iff U == 0") beside the new tail.

## What was measured

Draft: `.ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py` (seat ExecPointersGate).
The draft moved under me during the battery (eight sizes in ~8 minutes: 29,865 → 30,301 → 31,500 → 32,979
→ 33,282 → 35,072 → 39,836 → 40,352 B). Every reading file under
`.ufo/waves/round-73/w1/build/ExecPointersControls/readings/` carries the gate sha it was produced with, so
a straddle is visible; `readings/GATE.txt` names the final one.

Final run, exact command and observed output (excerpt; 19 rows, `MATCH` every row):

```
$ python3 -B .ufo/waves/round-73/w1/build/ExecPointersControls/run_worlds.py
# gate sha256:2537a22733c45e58da387777ed9e632e03f0819a54761cf0875db23659ddddf6 bytes:40352 mtime:2026-10-25T21:12:51
world	report	rev	exit	expect	verdict	reading
dir-only	report.md	ac8fc595	2	2	MATCH	report pointers resolved 5 of 5; unresolved 0
no-pointers	report.md	ac8fc595	2	2	MATCH	report pointers resolved 0 of 0; unresolved 0
multiword-span	report-broken.md	ac8fc595	1	1	MATCH	report pointers resolved 0 of 1; unresolved 1
line-suffix	report.md	ac8fc595	0	0	MATCH	report pointers resolved 2 of 2; unresolved 0
untracked-worktree	report.md	072048fa	1	1	MATCH	report pointers resolved 2 of 4; unresolved 2
later-rev-only	report.md	072048fa	1	1	MATCH	report pointers resolved 1 of 4; unresolved 3
later-rev-only@control	report.md	ac8fc595	0	0	MATCH	report pointers resolved 4 of 4; unresolved 0
... (12 further rows in readings/summary.tsv)
```

`$ python3 -B <gate> --self-test` → `self-test: 0 failure(s) over 57 assertions`, exit 0.

RED-BEFORE, re-run by me at the final sha (not taken from the gate seat):

```
$ python3 -B .ufo/waves/round-73/w1/build/ExecPointersGate/check_report_pointers.py \
    --report /home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md --repo . \
    --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --round 72
report pointers resolved 34 of 37; unresolved 3
pointer objects: blob 33, directory 1
unresolved pointer: S2xx.sha256 (report line 45) -> .ufo/waves/round-72/receipts/S2xx.sha256 (nearest: none)
unresolved pointer: tip-check_tip_battery.txt (report line 70) -> .ufo/waves/round-72/receipts/tip-check_tip_battery.txt (nearest: tip-tip_battery.txt)
unresolved pointer: receipts/tip-check_substrate_repin_v2.txt (report line 103) -> .ufo/waves/round-72/receipts/tip-check_substrate_repin_v2.txt (nearest: tip-substrate_repin_v2.txt)
# exit: 1
```

The two defect tokens of the mined mistake are named; the plan's RED-BEFORE requirement is met. The
receipt is `.ufo/waves/round-73/w1/build/ExecPointersControls/readings/red-before-r72-report.txt` (command
and gate sha in its header). Report lines
quoted (≤25 words, `sed -n` output): line 70 "(`tip-check_tip_battery.txt`, `tip-tip_battery-run2.txt`):
the counter's sandbox reads `check_assertion_floors.py` and"; line 103
"(`receipts/tip-check_substrate_repin_v2.txt`)."; line 45 "the `S2xx.sha256` manifests), `__pycache__`
removed; the last sweep ran after the last wave-1 settle." The committed files are
`.ufo/waves/round-72/receipts/tip-tip_battery.txt` and `.../tip-substrate_repin_v2.txt`
(`git ls-tree --name-only 072048f .ufo/waves/round-72/receipts/`).

## Findings

### F1 — vacuous `0 of 0` read as pass (defect; fixed) — headline

World `.ufo/waves/round-73/w1/build/ExecPointersControls/no-pointers/`. At sha `fd533ff` (32,979 B):

```
$ python3 -B <gate> --report .../no-pointers/report.md --repo . --rev ac8fc595… --round 73
report pointers resolved 0 of 0; unresolved 0        # exit 0
```

and the self-test pinned it: `rec("empty: zero pointers is exit 0", …)` (observed at
`check_report_pointers.py:734` on the 32,979 B snapshot; the same arm was at `:688` on the 31,500 B
snapshot and `:741` on the 33,282 B one, as the file grew; `main` ended `return EXIT_FAIL if rows else
EXIT_OK`, line 476 on the 32,979 B snapshot). A report that drops its backticks passed. Fixed at
`2d1d793`:

```
cannot evaluate: the report holds no backticked pointer token, so nothing was resolved   # exit 2
```

Same class through the fence rule: `fence-hides-prose/report-fence-only.md` (a broken receipt named only
inside a fence) read `0 of 0` exit 0 at `fd533ff`, now exit 2.

### F2 — one prose word inside the span hid a broken pointer (defect; fixed) — headline

World `multiword-span/`. At `fd533ff`:

```
$ python3 -B <gate> --report .../multiword-span/report-broken.md --repo . --rev ac8fc595… --round 73
report pointers resolved 0 of 0; unresolved 0        # exit 0
```

The report cites `` `.ufo/waves/round-72/receipts/tip-check_tip_battery.txt (exit 1, closure)` `` — a path
that does not exist at the revision. Cause: `is_command_span` returned true whenever the first word
contained `/` ("a path followed by arguments"), so the span was skipped whole. Fixed at `2d1d793`:

```
report pointers resolved 0 of 1; unresolved 1
pointer objects: blob 0, directory 0
unresolved pointer: .ufo/waves/round-72/receipts/tip-check_tip_battery.txt (report line 3) -> .ufo/waves/round-72/receipts/tip-check_tip_battery.txt (nearest: tip-tip_battery.txt)   # exit 1
```

and the valid variant (`corpus/lessons/round-72.md § Mistakes` in one span) now reads `1 of 1` instead of
`0 of 0` — M no longer undercounts the lane's own `<path> § <section>` citation form.

### F3 — every pointer a directory read as pass (honesty defect; fixed) — headline

World `dir-only/`: five tokens, all directories at `ac8fc59` (`receipts/`, `corpus/lessons/`,
`verifiers/`, `.ufo/waves/round-73/`, `plans/`). Measured with git:

```
$ git cat-file -t ac8fc595:corpus/lessons/   -> tree
$ git cat-file -t ac8fc595:verifiers/        -> tree
$ git cat-file -t 072048f:.ufo/waves/round-72/receipts/ -> tree
$ git cat-file -t 072048f:receipts/          -> fatal: path 'receipts/' does not exist … (exit 128)
```

At `fd533ff` the draft read `report pointers resolved 5 of 5; unresolved 0`, exit 0 — a report whose whole
evidence block certifies nothing; the docstring even declared "(a directory resolves as a tree)" (line 73
on that snapshot). The r72 report itself cites one honest directory (`receipts/base-outputs/`). Fixed at
`2d1d793`:

```
report pointers resolved 5 of 5; unresolved 0
pointer objects: blob 0, directory 5
cannot evaluate: every pointer names a directory, and a directory is not a file a reader can open   # exit 2
```

Fair use stays green: `dir-legit/` (one directory + one blob) reads `2 of 2` exit 0.

### F4 — `path:line` citations were a false positive (defect; fixed) — blocks an honest r73 report

World `line-suffix/`: `corpus/knowledge/frontmatter-trigger-surface.md:116-120` (the form the r73 plan and
addendum use) plus `verifiers/check_tip_battery.py`. At `fd533ff`:

```
report pointers resolved 1 of 2; unresolved 1
unresolved pointer: corpus/knowledge/frontmatter-trigger-surface.md:116-120 (report line 3) -> corpus/knowledge/frontmatter-trigger-surface.md:116-120 (nearest: frontmatter-trigger-surface.md)   # exit 1
```

The nearest name is the same file, so only the suffix failed; `git cat-file -e
ac8fc595:corpus/knowledge/frontmatter-trigger-surface.md:116-120` exits 128 while the path itself is a
blob. Fixed at `2d1d793` (`LOCATOR_SUFFIX = re.compile(r":\d+(?:-\d+)?$")`, line 160): `2 of 2` exit 0.
Residual, out of class: the locator is stripped, not verified — a probe report citing
`corpus/lessons/round-72.md:99999` (the file has 98 lines at `ac8fc59`) reads `1 of 1` exit 0. The draft
documents this in its blind-spot list.

### F5 — Q60 revision discipline verified (no defect)

`later-rev-only/report.md` names `receipts/census-before.txt`, `receipts/m127-l1-repro.txt` and
`plans/round-73.md`, none of which exists at the base rev
(`git cat-file -e 072048f:<path>` → exit 128 for all three; the same text at `ac8fc59` → blobs). Reading:
`1 of 4` exit 1 at the base, `4 of 4` exit 0 at the control rev. The gate resolves at `--rev`, not at
HEAD.

### F6 — untracked working tree verified (no defect)

`untracked-worktree/` builds a fleet-shaped `--shared` clone at `072048f`
(`git clone --shared -q --no-checkout`, checkout of the rev, `rev-parse --show-toplevel` equal to the
sandbox before any write) and writes `.ufo/waves/round-72/receipts/tip-check_tip_battery.txt` as an
untracked file. Reading: `2 of 4` exit 1, naming both occurrences of the token (prefixed and bare). The
gate reads committed objects only; it did not fall back to the work tree.

### F7 — wrong-round mapping, typo repair, traversal (no defect)

- `wrong-round-receipts/report.md` (round 73) cites `receipts/c2-base.txt`, which exists only at round 72:
  `2 of 3` exit 1, target `.ufo/waves/round-73/receipts/c2-base.txt`. The corrected copy (full round
  path) reads `3 of 3` exit 0.
- `typo-near/report.md` (edit distance 1 each) reads `1 of 3` exit 1 with exact suggestions:
  `(nearest: census-before.txt)`, `(nearest: check_tip_battery.py)`.
- Traversal does not buy a resolution: `git cat-file -e
  ac8fc595:.ufo/waves/round-73/receipts/../../SKILL.md` → `fatal: path … does not exist` (git rejects the
  `..` segment), so a `receipts/../..` token cannot resolve.
- Existing-but-wrong artifact (c2 cited where c3 was meant) passes (`1 of 1` exit 0) — semantic, out of the
  gate's class, stated in the draft.
- Bare `c3-base.txt` at round 73 resolves to the round-72 receipt (`1 of 1` exit 0) — R8's ladder, round
  attribution lost, stated in the draft's blind spots.

### F8 — operability: nearest-name could not suggest a cross-round repair (fixed)

`wrong-round-receipts/report.md` printed `(nearest: base-sweeps.txt)` for
`.ufo/waves/round-73/receipts/c2-base.txt`; the file the author meant is
`.ufo/waves/round-72/receipts/c2-base.txt` (a blob at both revs). Fixed at `2537a22`, observed:

```
unresolved pointer: receipts/c2-base.txt (report line 4) -> .ufo/waves/round-73/receipts/c2-base.txt (nearest: base-sweeps.txt, other round: .ufo/waves/round-72/receipts/c2-base.txt)
```

### F9 — the frozen sentence and the ladder disagree in the same docstring (freeze-bookkeeping)

At `2d1d793` the docstring prints "exit 0 iff U == 0" (line 22) and, 3 lines later, the tail "`M == 0` or
`B == 0` is exit 2 (cannot evaluate), never exit 0" (line 25, repeated in the exit-codes block at line
94-98). The behaviour is right; the frozen sentence must be amended by the L1 (plan/spec/receipt carry the
same sentence, per the seat spec) or the counter contradicts itself. I cannot amend it — only the L1
freezes counters.

### F10 — RED-BEFORE noise: the redaction mask (note for the r73 report)

The r72 report's `S2xx.sha256` (line 45) is a mask, not a file: the gate lists it as the third unresolved
token with `nearest: none`. The plan's RED-BEFORE requirement (name the `tip-check_*` tokens) is met, but
if the r73 report re-uses the mask the gate will fail it spuriously. Use the real manifest names or accept
one known false line.

## Draft instability observed (evidence for the freeze discipline)

The draft was mid-write during my battery and crashed twice on its own CLI, so any receipt taken without a
sha header is untrustworthy:

- 29,865 B snapshot: `--self-test` and any bare token → `NameError: name 'FIXTURE_MARKERS' is not defined`
  (line 314, `_ranked`).
- 32,100 B snapshot: `NameError: name 'LOCATOR_SUFFIX' is not defined` (line 266, `classify_token`) on a
  report that must exit 0 (`wrong-round-receipts/report-correct.md`), while the self-test printed 42
  assertions in the same minute.
- 35,072 B snapshot (`143a955`): the three behaviour fixes landed but the self-test read `1 failure(s)
  over 46 assertions` (`FAIL empty: zero pointers is exit 0 (got (2, …))`) — the stale arm for the defect
  just fixed.

At `2d1d793` all of this is resolved (56 assertions, green). **The freeze must re-run
`run_worlds.py` and `--self-test` at the frozen sha**; the runner records the sha per reading, so a
straddle cannot pass silently.

## Files changed (deliverables only; nothing committed)

- `.ufo/waves/round-73/w1/build/ExecPointersControls/` — 12 worlds, 18 report fixtures, 12 `world.json`,
  `run_worlds.py`, `README.md`, `readings/` (19 readings — 18 reports plus the control-rev run — plus
  `summary.tsv`, `GATE.txt`, `selftest.txt`, `red-before-r72-report.txt`).
- `.ufo/waves/round-73/w1/ExecPointersControls.md` — this report.

Scratch `/tmp/k73w1-ExecPointersControls.*`, `/tmp/k73w1-ptr-dir.txt`, `/tmp/ptrgate-spec.txt` removed;
runner sandboxes removed by the runner (`ls -d /tmp/k73w1-ExecPointersControls*` → nothing). No tool
install or upgrade. No lane gate run (the L1 owns gate execution); no fleet-repo mutation; no jj mutation.

## Risks and blockers

- **Risk (medium):** the gate changed six times during the battery; a freeze that does not re-run
  `run_worlds.py` at the frozen sha could ship a different counter than the one 19 readings describe.
- **Risk (low):** F10 — the r73 report must not re-use `S2xx.sha256`, or RED-BEFORE/after receipts will
  carry a false unresolved line.
- **Blocker:** none for this seat. The two items the L1 must land before freeze 2: the predicate sentence
  merge (F9) and the counter's adoption of the D1/D3 tail in the freeze addendum (already written into the
  docstring by the gate seat and marked "the L1 lands the tail in the same addendum that freezes this
  counter").
