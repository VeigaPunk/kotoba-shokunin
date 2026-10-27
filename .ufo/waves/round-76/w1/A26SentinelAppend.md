# A26SentinelAppend — append-only sentinel (round 76, w1)

Role: sentinel, report-only. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(fleet repo untouched: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=no`
printed nothing, exit 0).

**VERDICT: PASS — no lane file the round touches is a rewrite of filed bytes at
`eab64394dba08a47f6797a2e23719be14675b44b`; 0 deletions, 0 renames, 0 mode changes, 6/6 changed
paths inside the round-76 touch list, and the four append-only targets are insertion-only and
byte-preserved. Two integration conditions are flagged (F1, F2); neither is a deletion outside the
planned touch list.**

Measured revision: `eab6439` (round-76 head at measurement; worktree carries no tracked
modification — `git diff HEAD --stat` empty). Base: `b7f13f4b39cbd43076a85568adca763a6f674e7a`,
an ancestor of the measured rev (`git merge-base --is-ancestor` exit 0). Data had **not** landed at
measurement time (30 of 64 w1 reports present, `SKILL.md`/`SOURCES.md`/`LOG.md` untouched); the
check below is the one the L1/closure must re-run on the integrated tip.

## 1. What "append-only" is taken to mean (grounded, not invented)

The lane's own governance fixes the test, so this seat does not get to choose a convenient one:

- `PROTOCOL.md:463` — "`LOG.md` is append-only: entries are never rewritten or deleted; corrections
  land as new entries."
- `CORPUS.md:116` (fleet root, rule 2) — "**Append-only.** Only `status`, `recheck` and `used-by`
  change in place, and each change is logged old→new in the round lesson."

Two consequences drive every reading below:

- **A1 (the operative invariant): insertion-only byte preservation.** Every base line survives
  verbatim and in order; additions may sit anywhere. This is what "+ entries are never rewritten or
  deleted" means for a *sectioned* file: a new entry inside a closed section is legal.
- **A2 (reported separately, not required): tail-append.** `tip_bytes.startswith(base_bytes)` is
  true only when nothing was inserted above EOF. It holds for the round-75 lesson and the SCORECARD
  annotation, and it is **false by design** for the D2 line in LOG § Round 74 and the planned line in
  SCORECARD § planned (F3).

`corpus/SOURCES.md` is the one file where A1 cannot hold: rule 2 sanctions in-place edits to
`used-by`, so the S213 row is a single-line replacement and must be checked cell-wise instead.

## 2. The four named append-only targets (base vs measured rev)

| file | base lines/bytes | sha256 (base) | at `eab6439` | A1 | A2 | verdict |
|---|---|---:|---|---|---|---|
| `LOG.md` | 2810 / 561739 | `73bdf017…c8c5f3ca1adde795a0f492c01f` | identical | yes | yes | PASS |
| `SCORECARD.md` | 468 / 203212 | `04d37409…fba4f8e5ae1849c301` | identical | yes | yes | PASS |
| `corpus/lessons/round-75.md` | 12 / 2175 | `7f260fd5…ffa6807e79d57db6` | identical | yes | yes | PASS |
| `corpus/SOURCES.md` | 380 / 169568 | `4176098c…dec58aed8a11d9c91b9c6ff57` | identical (S213 edit not yet landed) | n/a | n/a | PASS (unguarded yet) |

All four end with a newline (`tail -c1 | xxd -p` = `0a`), so appends do not have to touch the last
filed byte to add one.

`corpus/SOURCES.md:153` is the only base line the round may replace. Current filed value of that row:

- line sha256 `5ad7e48b711589d2238621d429140a7d189890f35a677ede6641c29521608806`
- 13 pipe fields; `used-by` (field 12) = `corpus/knowledge/skill-eval-artefacts-round70.md`
- `status` (field 9) = `mined`, `anchor` (field 7) = the r70 quote — **neither may move this round**:
  `plans/round-76-addendum-1.md` § Correction withdrew the conjunct-(a) clause that asked the
  snapshot digest to equal the S213 anchor digest, on exactly the rule-2 ground that only
  `status`/`recheck`/`used-by` change in place.

## 3. Every touched file, and every deletion (the seat's listing duty)

```
$ git -C <lane> diff --diff-filter=DR --name-status b7f13f4..eab6439
(no output)                                        # 0 deleted, 0 renamed
$ git -C <lane> diff --numstat b7f13f4..eab6439
36      0  .ufo/waves/round-76/base-battery/base-battery.txt
1387    0  .ufo/waves/round-76/w1-dispatch.json
914     0  .ufo/waves/round-76/w1-spec.json
1       0  .ufo/waves/round-76/w1.ready
47      0  plans/round-76-addendum-1.md
74      0  plans/round-76.md
$ git -C <lane> diff --summary b7f13f4..eab6439     # six "create mode 100644" lines, no mode change
$ ls -la <lane>/.gitattributes                      # absent: no filters, no EOL normalisation
```

- **Deletions outside the planned touch list: 0.** There are no deletions at all, inside or outside
  it, at the measured rev.
- Changed-path classification (all six are new paths, so append-only is not applicable to them):
  `plans/round-76.md` (touch list), `plans/round-76-addendum-1.md` (touch list),
  `.ufo/waves/round-76/base-battery/base-battery.txt`, `…/w1-dispatch.json`, `…/w1-spec.json`,
  `…/w1.ready` (all under the `.ufo/waves/round-76/` prefix the touch list grants).
- Untracked wave artifacts (`build/`, `receipts/`, `snapshots/`, `w1/`, `w1.ready.dispatched`) are
  new paths under the same prefix; `w1.ready.dispatched` and `w1.ready.partial` are dispatch
  markers, not filed corpus bytes.

## 4. Where each planned addition must land (anchors for the integrator)

| target | physical shape | anchor |
|---|---|---|
| LOG § Round 75: R2/R3 receipt cites, R4 closing line | tail append | after `LOG.md:2810` (`- **Pointer:** … w2 falsify results pending …`, sha256 `30618f28…`); § Round 75 is the last section, so this is EOF |
| LOG § Round 74: D2 `d5aebcf` line | **mid-file insertion** (new bullet after the round-74 paragraph) | after `LOG.md:2803`, before the blank line 2804 and `## Round 75` at 2805. Legal under `PROTOCOL.md:463`; must not alter 2803 |
| LOG: round-76 entry | tail append | new `## Round 76 …` section after 2810 |
| SCORECARD: round-76 annotation | tail append | after `SCORECARD.md:468` (sha256 `51260231…`); the draft `build/scorecard-draft.md` header already states "append verbatim after the round-75 annotation, append-only, no filed byte rewritten" — verified true of the draft text |
| SCORECARD: "planned" note | **mid-file insertion** at the end of § planned | after line 179, before `## retired` at 181. The axes table and its annotation block (lines 24–36) must stay byte-identical: both claims say "score held" |
| `corpus/lessons/round-75.md`: R1 correction | tail append | after line 12 (sha256 `81e34c7d…`, the `\| attribution \| … \|` row) — see F5 for the blank-line requirement |
| `corpus/SOURCES.md`: S213 `used-by` | single-line, single-cell replacement | line 153, field 12 only (F4) |
| `SKILL.md`: § Body craft row, § Gate registry rows | insertions | row after line 216; registry rows after 512, before `## Sources` at 514 (see F1 for the preamble) |

## 5. Findings

### F1 — MEDIUM — the drafted SKILL.md patch rewrites two filed lines (not required by either claim)

`build/skill-patch.md` Pin 1 says "Replace the existing two-line paragraph with these three lines".
Simulated against the base bytes, the drafted patch is:

```
ops=[('replace', 1, 3), ('insert', 0, 1), ('insert', 0, 2)]   # 1 base line deleted, 6 added
SKILL.md 590 -> 595 lines
```

The deleted line is `SKILL.md:207`: its terminal `` `). `` becomes `` `; `` and the sentence continues
on two new lines (source: `build/skill-patch.md` § Pin 1). Line 206 survives.

Why this matters here: `SKILL.md` is on the touch list, so this is **not** a deletion outside it —
but it is the round's only planned rewrite of a filed body paragraph, in a file the plan itself
describes as "append-only where filed", and nothing in the frozen contract needs it:
`verifiers/check_spec_craft.py` (docstring lines 30–34) counts *rows* in
`### Body craft — the specification's skill-creation guides` that cite the page's `S###`; it never
pins the preamble. C1 conjunct (c) needs the new rule row, not a re-flowed preamble.

Smallest remediation (insertion-only, same line count):
keep lines 206–207 byte-identical and insert the round-76 pointer as two new lines after 207.

```
ops=[('insert', 0, 2), ('insert', 0, 1), ('insert', 0, 2)]    # 0 deleted
SKILL.md 590 -> 595 lines (budget 600)
```

If the L1 prefers the drafted re-flow, it must be declared in the addendum as a sanctioned in-place
edit; the append-only audit then reports `NOTE SKILL.md: 1 line(s) deleted` (see § 6), which is the
intended "declared rewrite" channel, not a failure.

### F2 — LOW — commit `eab6439` orphaned `## Reason` in the addendum (byte-safe, semantics broken)

`plans/round-76-addendum-1.md` now reads:

```
35: ## Reason
36: ## Wave role correction (validated topology)
...
45: Caught by L1 self-review against CORPUS.md rule 2 before data; …
```

The wave-role section was inserted between the heading and its body, so `## Reason` has no body and
the correction's reason paragraph now sits under the role heading. Zero deletions (`8 0` in
`git show --numstat eab6439`), so append-only holds; the defect is document structure introduced by
an "append" that was not at the tail. Remediation is itself insertion-only: insert a `## Reason`
heading before line 45 (+1 line), or move the new section after the reason paragraph (+9/−8 is not
allowed — prefer the former).

### F3 — LOW — two planned "appends" are mid-file insertions; the closure test must be A1, not A2

The D2 line (LOG § Round 74, after 2803) and the planned note (SCORECARD, before 181) are
insertions into the middle of sectioned files. They are legal (`PROTOCOL.md:463`: a correction lands
as a new entry) and they delete nothing, but a closure check written as
`tip_bytes.startswith(base_bytes)` will read **false** for `LOG.md` and `SCORECARD.md`. Use the
subsequence test in § 6, and do not record `tail-append=no` as a defect.

### F4 — LOW — `corpus/SOURCES.md` is the one sanctioned line rewrite; hold it to one cell

Guard at the tip: exactly one replaced base line, whose base sha256 is `5ad7e48b…`; the replacement
has the same 13 pipe fields; the changed field set is exactly `[11]` (0-based `used-by`); the new
cell contains `corpus/knowledge/description-craft-round76.md`. Anything else — `status` moved to
something else, an `anchor` digest edited in (withdrawn by addendum-1), a second row touched — is a
`CORPUS.md` rule-2 breach, and the audit's CTL3/CTL6 arms (§ 6) prove it is caught. The old→new
`used-by` value must also appear in `corpus/lessons/round-76.md` (rule 2, second clause).

### F5 — INFO — append mechanics: two of the four tails do not end in a blank line

`corpus/lessons/round-75.md` ends inside a markdown table (line 12 is a table row) and `LOG.md` ends
inside a bullet. A plain `printf '## Correction…' >>` produces no deleted byte, but the new paragraph
is then parsed as a table row / bullet continuation. Prefix the appended block with a blank line
(`'\n## Correction\n…'`); still insertion-only, and the R1 counter's content check is unaffected
either way.

### F6 — INFO — `verifiers/floors-registry.json` must be hand-edited, not re-serialised

66 lines of hand-indented JSON; the round-72 precedent changed `4 4` lines for four registry edits.
A `json.load` → `append` → `json.dump(indent=2)` add rewrites all 66 lines, which the audit reports
as `NOTE verifiers/floors-registry.json: 66 line(s) deleted` — inside the touch list, so not a
violation of this seat's rule, but a whole-file rewrite that hides the two intended rows. Insert the
two objects textually and keep `check_assertion_floors.py`'s in-file tables in step (bump-in-step
rule quoted in the file's own `$comment`).

## 6. Operability — the check to re-run on the integrated tip

Run from anywhere; read-only; exit 0 = append-only holds, 1 = violation, 2 = could-not-evaluate.
`BASE` is a parameter only so the control fixtures below can drive it; leave it defaulted on the lane.

```sh
#!/bin/sh
# usage: L=<lane> append_check.sh <tip-rev>
set -u
L=${L:-/home/vgpnk/Projects/shokunin/kotoba-shokunin}
R=${1:-HEAD}
BASE=${BASE:-b7f13f4b39cbd43076a85568adca763a6f674e7a}
[ "$(git -C "$L" rev-parse --show-toplevel 2>/dev/null)" = "$L" ] || { echo "not the lane: $L"; exit 2; }
git -C "$L" merge-base --is-ancestor "$BASE" "$R" || { echo "base $BASE not an ancestor of $R"; exit 2; }
echo "lane: $L"
echo "measured: $(git -C "$L" rev-parse "$R")  base: $BASE"
python3 -B - "$L" "$BASE" "$R" <<'PY'
import difflib, subprocess, sys

L, B, R = sys.argv[1:4]
APPEND_ONLY = ("LOG.md", "SCORECARD.md", "corpus/lessons/round-75.md")
TOUCH = {
    "verifiers/check_desc_craft.py", "verifiers/check_r75_routed_repairs.py",
    "corpus/knowledge/description-craft-round76.md", "plans/round-76.md",
    "plans/round-76-addendum-1.md", "SKILL.md", "verifiers/floors-registry.json",
    "verifiers/check_assertion_floors.py", "corpus/SOURCES.md",
    "corpus/lessons/round-75.md", "corpus/lessons/round-76.md",
    "corpus/QUALITY.md", "corpus/README.md", "LOG.md", "SCORECARD.md",
    "corpus/knowledge/sibling-overlap-census-round49.md",
}
PREFIX = ".ufo/waves/round-76/"
S213_SHA = "5ad7e48b711589d2238621d429140a7d189890f35a677ede6641c29521608806"
TOKEN = b"corpus/knowledge/description-craft-round76.md"
bad = []


def git(*a):
    return subprocess.run(["git", "-C", L] + list(a), capture_output=True, text=True).stdout


def show(rev, p):
    return subprocess.run(["git", "-C", L, "show", "%s:%s" % (rev, p)],
                          capture_output=True).stdout


dele = [x for x in git("diff", "--diff-filter=DR", "--name-only", B, R).splitlines() if x]
print("deletions/renames vs base: %d" % len(dele))
bad += ["deleted or renamed: %s" % d for d in dele]

changed = [x for x in git("diff", "--name-only", B, R).splitlines() if x]
out = [p for p in changed if p not in TOUCH and not p.startswith(PREFIX)]
print("changed paths vs base: %d (outside touch list: %d)" % (len(changed), len(out)))
bad += ["outside touch list: %s" % p for p in out]

for row in git("diff", "--numstat", B, R).splitlines():
    add, d, p = row.split("\t", 2)
    if d != "0":
        print("  lines deleted: %-40s -%s" % (p, d))

for f in APPEND_ONLY:
    a, b = show(B, f).splitlines(), show(R, f).splitlines()
    it = iter(b)
    ok = all(any(x == y for y in it) for x in a)
    tail = show(R, f).startswith(show(B, f))
    print("%-28s insertion-only=%s tail-append=%s (%d -> %d lines)"
          % (f, "yes" if ok else "NO", "yes" if tail else "no", len(a), len(b)))
    if not ok:
        bad.append("rewrite of filed bytes: %s" % f)

a = show(B, "corpus/SOURCES.md").splitlines()
b = show(R, "corpus/SOURCES.md").splitlines()
ops = [o for o in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
       if o[0] != "equal"]
if not ops:
    print("corpus/SOURCES.md: no change yet (S213 used-by not landed)")
else:
    reps = [o for o in ops if o[0] == "replace" and o[2] - o[1] == 1]
    print("corpus/SOURCES.md: %d non-equal hunk(s), %d single-line replace(s)"
          % (len(ops), len(reps)))
    if len(reps) != 1 or len(ops) != 1:
        bad.append("SOURCES.md: expected exactly one single-line replacement")
    else:
        i, j = reps[0][1], reps[0][3]
        oc = a[i].rstrip(b"\n").split(b"|")
        nc = b[j].rstrip(b"\n").split(b"|")
        cells = [k for k in range(min(len(oc), len(nc))) if oc[k] != nc[k]]
        print("  replaced base line %d, changed cells %s (expect [11] = used-by)"
              % (i + 1, cells))
        if cells != [11] or len(oc) != len(nc) or TOKEN not in nc[11]:
            bad.append("SOURCES.md S213 row: cells %s, count %d/%d, token %s"
                       % (cells, len(oc), len(nc), TOKEN in nc[11]))

for p in changed:
    if p in APPEND_ONLY or p == "corpus/SOURCES.md":
        continue
    d = [r for r in git("diff", "--numstat", B, R).splitlines() if r.endswith("\t" + p)]
    if d:
        n = d[0].split("\t")[1]
        if n != "0":
            print("  NOTE %s: %s line(s) deleted -- inside touch list, declare it" % (p, n))

for f in bad:
    print("FAIL %s" % f)
print("append check %s (%d violation(s))" % ("PASS" if not bad else "FAIL", len(bad)))
sys.exit(0 if not bad else 1)
PY
```

Measured with this exact block on the lane (`sh append_check.sh eab6439`, exit 0):

```
measured: eab64394dba08a47f6797a2e23719be14675b44b  base: b7f13f4b39cbd43076a85568adca763a6f674e7a
deletions/renames vs base: 0
changed paths vs base: 6 (outside touch list: 0)
LOG.md                       insertion-only=yes tail-append=yes (2810 -> 2810 lines)
SCORECARD.md                 insertion-only=yes tail-append=yes (468 -> 468 lines)
corpus/lessons/round-75.md   insertion-only=yes tail-append=yes (12 -> 12 lines)
corpus/SOURCES.md: no change yet (S213 used-by not landed)
append check PASS (0 violation(s))
```

### Controls (a guard that cannot fail is not a guard)

A two-commit fixture in `/fast/scratch/hyaku/kotoba-r76/A26SentinelAppend/` held the five filed
files at their base bytes (`git rev-parse --show-toplevel` asserted the fixture dir before every
commit). Ten worlds, each a single commit over the base commit, run through the block above:

| world | expected | got |
|---|---|---|
| CTL1 honest round: three tail appends + S213 `used-by` cell | 0 | 0 |
| CTL2 `LOG.md` truncated by 3 lines | 1 | 1 |
| CTL3 S213 `status` cell rewritten instead of `used-by` | 1 | 1 |
| CTL4 `round-75.md` M75-1 row reworded in place | 1 | 1 |
| CTL5 `SCORECARD.md` depth score cell rewritten | 1 | 1 |
| CTL6 S213 `used-by` + `anchor` rewritten | 1 | 1 |
| CTL7 change to a path outside the touch list | 1 | 1 |
| CTL8 `SCORECARD.md` deleted | 1 | 1 |
| CTL9 `SCORECARD.md` last line replaced (not appended) | 1 | 1 |
| CTL10 LOG § Round 74 mid-file insertion (the D2 shape) | 0 | 0 |

10/10 as expected, 8 must-fail arms all red. The same matrix was run against the fuller Python
audit (adds `--worktree` mode and per-file detail): same 10/10.

### Calibration / limits (stated, not assumed)

- This is a **guard**, not a claim counter: it passes on the base itself and on any no-change world
  (CTL "do nothing"). A green reading at a pre-landing rev therefore proves only "nothing filed has
  been rewritten *yet*"; it must be re-run after the L1 lands data, and the reading quoted in the
  SCORECARD belongs to that tip.
- It compares commits, so it cannot see a rewrite that was committed and then reverted, nor a
  force-push; `BASE` ancestry (`merge-base --is-ancestor`, exit 0 here) is the only history check.
- It reads `git show`, not the worktree; pass a rev, never a working tree. Uncommitted edits are
  invisible by construction (at measurement the worktree had none: `git diff HEAD --stat` empty).
- `corpus/lessons/round-76.md`, `corpus/QUALITY.md`, `corpus/README.md`, `verifiers/*` are in the
  touch list and were untouched at measurement; when they land, deletion counts there are reported
  as `NOTE` lines (declared rewrites), not failures — by design, since only the four named files and
  `SOURCES.md`'s cell carry an append-only obligation.

## 7. Commands run (evidence, with exit codes)

| command | result |
|---|---|
| `git -C <lane> rev-parse HEAD` | `eab64394dba08a47f6797a2e23719be14675b44b` |
| `git -C <lane> merge-base --is-ancestor b7f13f4 HEAD` | exit 0 |
| `git -C <lane> diff --diff-filter=DR --name-status b7f13f4..HEAD` | no output, exit 0 |
| `git -C <lane> diff --numstat b7f13f4..HEAD` | 6 files, `+2459 −0` |
| `git -C <lane> diff --summary b7f13f4..HEAD` | 6 `create mode 100644`, no mode change |
| `git -C <lane> diff HEAD --stat` | empty (worktree clean) |
| `git -C <lane> ls-files -d` | empty |
| `git -C /home/vgpnk/Projects/shokunin status --porcelain -uno` | empty (fleet root untouched) |
| `sh append_check.sh eab6439` | `append check PASS (0 violation(s))`, exit 0 |
| `AUDIT_SH=append_check.sh python3 -B controls.py` | `controls: 10 case(s), 0 unexpected`, exit 0 |
| `python3 -B append_audit.py --rev eab6439` | `append audit clean … 0 violation(s)`, exit 0 |
| `python3 -B append_audit.py --rev eab6439 --worktree` | same, exit 0 |
| `grep -n 'byte-identical\|differs from the base' verifiers/*.py` (Q73 sweep, re-run) | only `check_province_core.py` § Frontier/§ Adjacent pins + `check_tip_battery.py` instrument pins; none covers `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-75.md` or `SOURCES.md` — the plan's Q73 claim reproduces |

Installs: none (no package manager, no `uv`/`npx`/binary install this seat; pacman not run).
Processes: none left running; the only background work was short foreground `git`/`python3` calls.
Scratch `/fast/scratch/hyaku/kotoba-r76/A26SentinelAppend/` (fixture, `append_audit.py`,
`controls.py`, `append_check.sh`) is removed before this seat yields; this report is the only
artifact it leaves.

## 8. Adjacent observation (no action taken, out of this seat's surface)

`build/skill-patch.md` states "Net delta in this draft: **+5 lines → 595**" and the base is 590
lines, matching the plan's budget box (600). The insertion-only variant in F1 also lands at 595, so
the remediation costs no budget.
