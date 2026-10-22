Result: DONE — drafted lesson row M45 (`append-only-breach`) for the S050 in-place `anchor` edit in `e792607e`, with a range gate that is red on that commit (exit 1) and green on both the immediately preceding range (exit 0) and a populated range that edits the same file (exit 0), and with the same gate finding 12 earlier unrecorded breaches of the same rule.

# ScribeMistake — round 54, frontier step 3 (mine one mistake)

Seat: leaf, kotoba-shokunin. Sandbox for every write and run:
`/fast/scratch/hyaku/kotoba-r54/ScribeMistake`, cloned from the lane and checked out at
`7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` (180 commits, full history, no `--depth`). The lane was read
only; the only lane write is this file. No tool installs were needed (python3 and git only).

## 1. Which candidate, and why (calibration)

**(a) the S050 in-place `anchor` edit — chosen.**

| candidate | evidence strength | already captured? | fix falsifiable? |
|---|---|---|---|
| (a) S050 `anchor` edited in place, `e792607e` | exact commit, exact cell, before/after bytes reproduce from `git show` (§2.1); the lane's own lesson names the rule and admits the breach (`corpus/lessons/round-53.md:43-46`) | **no criterion, no instrument** — the only append-only test in the corpus is an eyeball that reports "no removed row" (`corpus/lessons/round-52-verifier-spotcheck.md:30`) and cannot see a rewrite (§5) | yes — a range gate, red on `e792607e`, green before it (§4) |
| (b) plan states before-values measured `21:30Z`–`21:32Z`, counters ran ~`21:08Z`–`21:11Z` | exact: the plan commit's own committer time is `21:12:08Z`, 17m52s–19m52s before the earliest claimed measurement (§2.2) | **yes, twice** — Q19 (`corpus/QUALITY.md:30`, "re-measured at round start and printed with its command and commit") and the plan's own erratum (`plans/round-54.md:73-77`), written before wave 1 | only by prose: "write the true time" cannot be made to fail mechanically; the row's fix column would read "none, procedural" |
| (c) round-53 spot-check defects | each is a routed repair, not a new class; (4) is C2, (5) and (6) are in this round's plan, (2) is a content correction | yes — all seven routed defects are listed in `plans/round-54.md:57-66` | n/a |

(a) also has the property that makes a mistake worth mining: it **recurred** after the lane knew the rule.
Round 51 refused the identical move and cited rule 2 (`corpus/lessons/round-51.md:65`, "Contract v1 rule 2
forbids editing `teaches` in place"), and round 52 asserted "None of S001–S031 changed in place"
(`corpus/lessons/round-52.md:90`) — which this gate confirms for round 52's commits. Rounds 49, 50 and 53
broke the same rule.

(b) is a real defect and I am not disputing it; it is already recorded and its class ("a record wider or
other than what happened") is already in the lesson table as M43 (`corpus/lessons/round-53.md:14`). Mining
it again would add a row without adding a falsifier.

## 2. Evidence, verified in the sandbox

### 2.1 The routed instance

```
$ git show e792607e -- corpus/SOURCES.md
corpus/SOURCES.md | 3 ++-
1 file changed, 2 insertions(+), 1 deletion(-)      # one row rewritten, one row appended

$ # cell-level compare of the S050 row at e792607e^ and e792607e
CELL 6 changed:
  - ... body identical to `docs/src/ai/instructions.md` at commit `cfb894a5` (frontmatter only differs)
  + ... body identical to `docs/src/ai/instructions.md` at zed-industries/zed@`cfb894a5` (frontmatter only differs)
```

Cells 1–5 and 7–11 of the row are byte-identical; cell 6 is `anchor` (header at `corpus/SOURCES.md:7`:
`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`).

The rule: `CORPUS.md:116`, contract v1 rule 2 — "**Append-only.** Only `status`, `recheck` and `used-by`
change in place, and each change is logged old→new in the round lesson. A correction is a new row whose
`teaches` opens `supersedes S0NN —`."

The motive is in the lane's own words (`corpus/lessons/round-53.md:43-46`): the edit was made "because the
corpus gate reads the words 'commit `<hex>`' as a lane commit pointer and flagged the upstream Zed hash as
`commit_unresolvable` … This edits a cell the contract keeps append-only (rule 2 allows only `status`,
`recheck`, `used-by`); it is disclosed here rather than carried as a red gate or a duplicate row." So an
instrument that does not model rule 2 pushed the lane across it, and the breach was filed as prose.

### 2.2 Candidate (b), for the record

```
$ git log -1 --format='%cI %aI' e33715486a45a4a857b64c30e6b695f7995858b8
2026-10-22T18:12:08-03:00 2026-10-22T18:04:30-03:00        # = 21:12:08Z / 21:04:30Z
$ grep -n '21:30Z\|21:31Z\|21:32Z' plans/round-54.md
6:  measured by the L1 at round start, 2026-10-22T21:30Z
27: Before at `422ffd10` (2026-10-22T21:31Z)
42: Before at `422ffd10` (2026-10-22T21:32Z)
```

The record states three measurement times that are 17m52s to 19m52s **after** the commit that contains
them; both the author and committer timestamps of `e3371548` precede every one of them. Deterministic from
git alone, no clock needed. The plan already carries the erratum (`plans/round-54.md:73-77`) with the same
arithmetic. **[INFERENCE]** that this was transcription and not back-dating: the plan's stated runs
("between 21:08Z and 21:11Z") are consistent with the commit's author time and there is no evidence of a
later run being claimed.

### 2.3 The same rule, broken earlier and unrecorded

Full audit of every commit reachable from the tip whose diff touches `corpus/SOURCES.md` (§4 arm E):

| commit | date (committer) | protected cells changed in place |
|---|---|---|
| `bfd5a583a` | 2026-10-22T08:37:22-03:00 (round 49) | S022 `teaches` |
| `542f51567` | 2026-10-22T10:25:02-03:00 (round 50) | S019 `scope`, `anchor`, `teaches`; S022 `scope`, `anchor`, `teaches` |
| `bf109cacc` | 2026-10-22T10:41:43-03:00 (round 50, "S019/S022/S026/S028 cells") | S019 `teaches`; S022 `teaches`; S026 `scope`, `teaches`; S028 `teaches` |
| `e792607e` | 2026-10-22T17:48:01-03:00 (round 53) | S050 `anchor` |

13 changes in 4 of 16 commits, from the file's creation (`f2f9ee1d8`, 11 rows) to `7ad05d34` (52 rows).

How the lane recorded them:

- Round 49: "Status changes logged old→new: S022 and S023 created as `mined`; S018 `used-by` as above.
  **No other row** moved" (`corpus/lessons/round-49.md:50`) — the row did move (`bfd5a583a` changed its
  `teaches` cell).
- Round 50: "S019 and S022 also **gain anchor, scope and teaches text** for the round-50 facts (seat
  reports carry each old→new cell). **No other row moved**" (`corpus/lessons/round-50.md:76-78`) — the cells
  are disclosed, but as an ordinary gain, not as a rule-2 breach; `bf109cacc`'s S026/S028 rewrites are not
  in that sentence at all.
- Round 53: disclosed **as a breach** (`corpus/lessons/round-53.md:43-46`), and routed by the outside
  spot-check as defect 3 (`corpus/lessons/round-53-verifier-spotcheck.md:192`).

Round 52 is clean in the scan, which agrees with the round-52 lesson's own claim
(`corpus/lessons/round-52.md:90`); that agreement is a calibration datum for the gate, not a courtesy.

## 3. Drafted row (paste-ready into `corpus/lessons/round-54.md` § Mistakes)

```markdown
| M45 | `append-only-breach` | `corpus/SOURCES.md` rows were rewritten in place across commits. `CORPUS.md:116` (contract v1 rule 2) lets only `status`, `recheck` and `used-by` change in place and requires a correction to be a new row opening `supersedes S0NN —`. Routed instance: `e792607e` rewrote S050's `anchor` cell, "…at commit `cfb894a5`…" → "…at zed-industries/zed@`cfb894a5`…", to clear the lane gate's `commit_unresolvable` reading; the round-53 lesson discloses it and names the rule (`corpus/lessons/round-53.md:43-46`) and the outside spot-check routed it (`corpus/lessons/round-53-verifier-spotcheck.md:192`). The same scan finds 12 more protected-cell changes in 3 earlier commits, none filed as a breach: `bfd5a583a` S022 `teaches`; `542f51567` S019 `scope`, `anchor`, `teaches` and S022 `scope`, `anchor`, `teaches`; `bf109cacc` S019 `teaches`, S022 `teaches`, S026 `scope`, `teaches`, S028 `teaches` — 13 changes in 4 of 16 commits from the file's creation to `7ad05d34`. Round 49's summary says "No other row" moved (`corpus/lessons/round-49.md:50`); round 50's says the cells "gain anchor, scope and teaches text" and "No other row moved" (`corpus/lessons/round-50.md:76-78`), which discloses the cells as an ordinary gain; round 51 refused the same edit and cited the rule (`corpus/lessons/round-51.md:65`). | none — no criterion governs SOURCES.md history and no instrument reads it: no verifier runs `git rev-list` or `git log` (four read a revision's bytes with `git show`, none compares a row against its parent), `scripts/sources-census.sh` makes 0 `git` calls, and the corpus's one append-only test records "no removed row" from a `git diff` piped through `grep` for removed lines (`corpus/lessons/round-52-verifier-spotcheck.md:30`), which cannot tell a rewritten row from an appended one | `verifiers/check_sources_append_only.py` (draft, seat sandbox, 189 lines, sha256 `d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`): walks `--base..--rev`, parses every registry row at each commit and its parent, exits 1 on a protected-cell change or a dropped row. Arms: red `--base 55973a20 --rev e792607e` → `breach e792607e8 S050 anchor: …at commit \`cfb894a5\`… -> …at zed-industries/zed@\`cfb894a5\`…`, `1 change(s) in 1 of 1 commits`, exit 1; green `--base 55973a20 --rev e792607e^` → clean, exit 0; green on a populated range that edits the file `--base 34cfffbb --rev 55973a20` → 4 commits scanned, 0 changes, exit 0; `--self-test` → 0 failure(s) over 14 assertions, including a must-fail `anchor in place` arm. Landing it needs a disposition of the 12 earlier changes (operator ratification, or one superseding row each) and, under `verifiers/`, a SKILL.md Gate registry row — M is 23 at `7ad05d34`, so 24 after. |
```

Two properties of the row I checked rather than assumed: it carries no `|` inside any cell (the table needs
none), and every commit id, line number and quote in it was printed by a command in §2 or §4 of this report.

## 4. The fix, shown able to fail

Script: `sources_append_only_draft.py` in the sandbox clone root (189 lines, sha256
`d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`; full text in the appendix). It is a
draft: I ran it in the sandbox only and the lane was not touched. Its integration name would be
`verifiers/check_sources_append_only.py`.

Mechanism. `git rev-list --reverse --no-merges <base>..<rev> -- corpus/SOURCES.md` gives the commits in
reach whose diff touches the registry. For each, the table is parsed at the commit and at its parent; the
header row supplies the column names, so a cell is compared to the cell it replaced, not to a position.
A cell differing outside `status`, `recheck`, `used-by` is a breach; a row present at the parent and absent
at the commit is a breach; a permitted-column change prints as a `log` line (rule 2 also requires it in the
round lesson, which is prose this gate does not read — the docstring says so, per Q31). Output names the
first differing window, so the reader sees the change and not the head of a long cell.

| arm | command (run in `/fast/scratch/hyaku/kotoba-r54/ScribeMistake`) | observed | exit |
|---|---|---|---|
| A self-test | `python3 -B sources_append_only_draft.py --self-test` | `self-test: 0 failure(s) over 14 assertions` | 0 |
| B **red** | `python3 -B sources_append_only_draft.py --base 55973a20ac728f7b11ac8de518620ba128c13afa --rev e792607e85c78998bbf0ae4e2b5d350683eec0f7` | `breach e792607e8 S050 anchor: …ctions.md` at commit `cfb894a5` (frontmatter… -> …ctions.md` at zed-industries/zed@`cfb894a5` …` / `sources append-only breach 1 change(s) in 1 of 1 commits` | 1 |
| C **green**, same lower bound, head moved back one | `… --base 55973a20ac… --rev 'e792607e85c78998bbf0ae4e2b5d350683eec0f7^'` | `sources append-only rows clean: 0 commits scanned, 0 protected-cell changes` | 0 |
| D **green** on a populated range that edits the file | `… --base 34cfffbb242fe05c37f3a1bcd093f689c54f1431 --rev 55973a20ac728f7b11ac8de518620ba128c13afa` | 3 `log` lines (`S004 status: queued -> mined`, `S004 used-by`, `S019 used-by`), then `sources append-only rows clean: 4 commits scanned, 0 protected-cell changes` | 0 |
| E full audit to tip | `… --rev 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39 --quiet-log` | the 13 breach lines of §2.3, `sources append-only breach 13 change(s) in 4 of 16 commits`; `real 0m0.074s` | 1 |

Arm B is the mistake; arm C is the same command with the head moved one commit back, so nothing but the
measured commit changed between red and green. Arm D is the control that matters for a gate of this shape:
it runs over four commits that do edit `corpus/SOURCES.md` (adding S051 and changing permitted cells) and
stays green, so the red in B is not "any commit that touches the file". Arm E is the carried state: if the
gate lands in `verifiers/`, the lane is red at `7ad05d34` until the 12 earlier changes are ratified or
corrected.

Self-test arms (14 assertions, each arm two assertions: breach count and log-note count): unchanged table →
0/0; `status` in place → 0 breaches, 1 log; `used-by` in place → 0/1; **`anchor` in place → 1/0 (must-fail)**;
`teaches` in place → 2/0; row appended → 0/0; row removed → 1/0. The must-fail arms are the ones that go red
if the comparator's exemption list were widened to cover `anchor` or `teaches`.

## 5. Why no existing rule or instrument caught it

1. **No criterion names the act.** `corpus/QUALITY.md` has no row on registry mutation. The nearest, Q19
   (`corpus/QUALITY.md:30`), governs before-values, and Q26/Q31 govern prose width. Rule 2 lives in the
   contract (`CORPUS.md:116`) and nowhere in an instrument.
2. **No verifier walks history.** `grep -ln 'rev-list' verifiers/*.py verifiers/*.sh` → no file (exit 1);
   `grep -ln 'git log' …` → no file (exit 1). Four verifiers read a revision's bytes with `git show`
   (`check_callee_rename.py`, `check_description_thresholds.py`, `check_mcp_instructions.py`,
   `check_sibling_census.py`), and none compares a row against its parent commit.
3. **The census reads the working tree only.** `grep -c git /home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
   → `0`. Its E01–E11/W01–W03 checks (script lines 126–144) are about the current table (row shape, ids,
   kinds, tiers, statuses, dangling `used-by`), so a rewrite that leaves the current table well-formed is
   invisible to it.
4. **The corpus's one append-only test cannot see a rewrite.** `corpus/lessons/round-52-verifier-spotcheck.md:30`
   records `git diff c8579a4c 0c9180a6 -- corpus/SOURCES.md | grep '^-\|'` → "no removed row" → pass. Run
   on the red commit, that command prints
   `-| S050 …` on one side and `+| S050 …` plus `+| S052 …` on the other (measured: `minus 2 plus 3`), so a
   rewritten row enters the same channel as a deleted one and the recorded verdict has no vocabulary for
   "rewritten". A row that is edited in place is therefore *reported as* a removal, or read as a
   delete-and-re-add of the same id and passed.

What the gate that *did* touch this episode could see: `verify_corpus_integrity.py` resolves commit tokens
in corpus files. It read the upstream Zed hash in S050's `anchor` as an unresolvable lane commit, the lane
reworded the cell to clear it, and the reword is the breach. One gate's finding produced another rule's
violation, and nothing sat between them.

## 6. What the L1 should know before integrating

- **M at the tip is 23, not 21.** `git ls-tree 422ffd10 verifiers/` counts 21 `.py`/`.sh` blobs; at
  `e3371548` and `7ad05d34` it is 23, because the plan commit adds `check_description_thresholds.py` and
  `check_gate_registry.py`. C2's statement is parameterised `<M>`, so this is not a defect — but the after
  line will read `conformant 23 of 23`.
- **Landing this gate changes N.** Under `verifiers/` it raises C2's M to 24 and needs a `## Gate registry`
  row that the frozen counter accepts: name `verifiers/check_sources_append_only.py`, kind `gate`, entry
  command containing that path, verdict map `0=clean`, `1=failed` (and `2=could-not-evaluate`), self-test
  `--self-test`, pinned values `in-file` (it pins no external file), non-empty write scope, owner `kotoba`.
  Under `scripts/` it changes nothing in C2 but is not a graded gate.
- **A floors entry is not needed, and cannot be added alone.** `verifiers/floors-registry.json` carries 13
  instruments for 23 verifiers, and `check_assertion_floors.py` reconciles that file against its own two
  in-file tables (`EXPECTED_INSTRUMENTS` at `:132`, `INSTRUMENTS`); it never enumerates `verifiers/`. An
  entry added to the JSON without a matching table row is `row vanish` drift (`:351-354`), so a floor for
  the new gate would mean editing both in-file tables too. The gate needs neither.
- **The red carried state is a decision, not a bug.** 12 of the 13 changes predate this round. Rule 2's own
  repair is "a new row whose `teaches` opens `supersedes S0NN —`", and the round-51 lesson records why the
  lane avoided that for S024 (a superseding row with the same URL adds a W04 duplicate-URL warning,
  `corpus/lessons/round-51.md:65-67`). So the L1's real choice is: ratify the 12 older rewrites via L0, or
  write superseding rows and accept the W04 warnings, or land the gate with `--base` per round and keep the
  full audit as a reported measurement rather than a gate. I did not decide this.
- **Do not paste the row's evidence as a claim about behaviour.** The row states what the scan prints; it
  states nothing about whether the newer cell text is truer than the older.

## 7. Limits of this report

- Verified by reading and running: the S050 cell change and its identity, the four commit dates, the three
  earlier commits' changed cells, the absence of history walks in `verifiers/`, the census script's zero
  `git` calls, the round-52 test's output shape on the red commit, the row counts (11 / 51 / 52) and the
  malformed-row count (0) at three revisions, M = 21/23/23, and all five gate arms.
- Not verified: whether any of the 12 earlier rewrites had an operator's or an L1's blessing; I only
  established that no lesson files them as a rule-2 breach, and that rule 2 does not admit an in-place
  `scope`, `anchor` or `teaches` change under any wording I found. I also did not test the gate against a
  hostile history (a row whose column count changes, a file rename); the parser skips such a row and leaves
  it to the census, which the docstring says.
- Blind spots measured, not assumed: `--no-merges` skips 2 merge commits in this history, and neither
  changes `corpus/SOURCES.md` against either parent (`git diff --name-only <m>^1 <m> -- corpus/SOURCES.md`
  → 0 paths, and against `^2` → 0 paths), so the skip loses nothing here.
- The row's `captured-by` says no criterion governs SOURCES history. It does not say no criterion *could*;
  I am not proposing a new Q row, because the gate is the cheaper instrument and the row's fix column
  carries it.

## Appendix — the check as code text

Delivered as `verifiers/check_sources_append_only.py`; this is the file I ran (sandbox path
`/fast/scratch/hyaku/kotoba-r54/ScribeMistake/sources_append_only_draft.py`).

```python
#!/usr/bin/env python3
"""Draft gate: corpus/SOURCES.md is append-only (CORPUS.md section
"SOURCES.md — where a shokunin learns", rule 2).

Rule 2, verbatim: "Only `status`, `recheck` and `used-by` change in place, and each
change is logged old->new in the round lesson. A correction is a new row whose
`teaches` opens `supersedes S0NN —`."

This gate walks every commit reachable from --rev whose diff touches
corpus/SOURCES.md, parses the registry table at the commit and at its parent, and
reports:

  * a row whose protected cell (every column except status, recheck, used-by)
    differs in place          -> breach, exit 1
  * a row present at the parent and absent at the commit -> breach, exit 1

An in-place change to one of the three permitted columns is printed as a "log"
line: rule 2 also requires it to be recorded old->new in the round lesson, which
is prose this gate does not read. The gate reports it, it does not grade it.

Output: one line per breach, then one summary line.
Exit: 0 clean, 1 breached, 2 usage/environment failure.
"""
import argparse
import re
import subprocess
import sys

PATH = "corpus/SOURCES.md"
PERMITTED = ("status", "recheck", "used-by")
ROW = re.compile(r"^\|\s*(S\d{3,})\s*\|")
HEADER = re.compile(r"^\|\s*id\s*\|")


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], capture_output=True, text=True
    )


def blob(repo, rev):
    r = git(repo, "show", "%s:%s" % (rev, PATH))
    return r.stdout if r.returncode == 0 else None


def parse(text):
    """id -> {column: cell} for every registry row; columns come from the header."""
    cols = None
    rows = {}
    for line in text.splitlines():
        if HEADER.match(line):
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            continue
        m = ROW.match(line)
        if not m or cols is None:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(cols):
            continue  # malformed row; the census owns that finding
        rows[m.group(1)] = dict(zip(cols, cells))
    return rows


def compare(before, after):
    """(breaches, log_notes) between two parsed tables."""
    breaches, notes = [], []
    for rid in sorted(before):
        b = before[rid]
        a = after.get(rid)
        if a is None:
            breaches.append((rid, "row", "removed", "", ""))
            continue
        for col in b:
            if col == "id" or b[col] == a.get(col, ""):
                continue
            rec = (rid, col, b[col], a.get(col, ""))
            if col in PERMITTED:
                notes.append(rec)
            else:
                breaches.append(rec)
    return breaches, notes


def delta(old, new, width=44):
    """Show the window around the first differing character, not the head."""
    if old == "" and new == "":
        return "row present -> absent", ""
    i = 0
    while i < min(len(old), len(new)) and old[i] == new[i]:
        i += 1
    start = max(0, i - 14)
    lead = "\u2026" if start else ""
    return (
        lead + old[start : start + width] + ("\u2026" if start + width < len(old) else ""),
        lead + new[start : start + width] + ("\u2026" if start + width < len(new) else ""),
    )


def scan(repo, rev, base=None):
    rng = "%s..%s" % (base, rev) if base else rev
    commits = git(repo, "rev-list", "--reverse", "--no-merges", rng, "--", PATH)
    if commits.returncode != 0:
        sys.stderr.write("rev-list failed: %s\n" % commits.stderr.strip())
        raise SystemExit(2)
    breaches, notes, scanned, breached_commits = [], [], 0, set()
    for c in commits.stdout.split():
        before = blob(repo, c + "^")
        after = blob(repo, c)
        if before is None or after is None:
            continue  # root commit, or the file was created/removed here
        scanned += 1
        b, n = compare(parse(before), parse(after))
        for rec in b:
            breaches.append((c,) + rec)
            breached_commits.add(c)
        for rec in n:
            notes.append((c,) + rec)
    return breaches, notes, scanned, len(breached_commits)


def self_test():
    """Comparative arms: the table comparator must fail on the wrong shapes."""
    base = (
        "| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| S001 | a | docs | A | s | anchor one | t | queued | 2026-10-19 | 90d | \u2014 |\n"
        "| S002 | b | docs | A | s | anchor two | t | mined | 2026-10-19 | 90d | SKILL.md |\n"
    )
    arms = [
        ("unchanged", base, base, 0, 0),
        ("status in place", base, base.replace("| queued |", "| mined |"), 0, 1),
        ("used-by in place", base, base.replace("| \u2014 |", "| LOG.md |"), 0, 1),
        ("anchor in place", base, base.replace("anchor one", "anchor 1"), 1, 0),
        ("teaches in place", base, base.replace("| t |", "| t2 |"), 2, 0),
        (
            "row appended",
            base,
            base + "| S003 | c | docs | A | s | anchor | t | queued | 2026-10-19 | 90d | \u2014 |\n",
            0,
            0,
        ),
        ("row removed", base, base.replace(
            "| S002 | b | docs | A | s | anchor two | t | mined | 2026-10-19 | 90d | SKILL.md |\n", ""
        ), 1, 0),
    ]
    failures, assertions = [], 0
    for name, before, after, want_b, want_n in arms:
        b, n = compare(parse(before), parse(after))
        assertions += 2
        if len(b) != want_b:
            failures.append("%s: %d breach(es), wanted %d" % (name, len(b), want_b))
        if len(n) != want_n:
            failures.append("%s: %d log note(s), wanted %d" % (name, len(n), want_n))
    for f in failures:
        print("FAIL " + f)
    print("self-test: %d failure(s) over %d assertions" % (len(failures), assertions))
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", default="HEAD", help="revision to scan back from")
    ap.add_argument("--base", default=None, help="optional exclusive lower bound (base..rev)")
    ap.add_argument("--repo", default=".", help="lane repository root")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--quiet-log", action="store_true", help="hide permitted-cell notes")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    breaches, notes, scanned, ncommits = scan(a.repo, a.rev, a.base)
    if not a.quiet_log:
        for c, rid, col, old, new in notes:
            o, n = delta(old, new, 24)
            print("log  %s %s %s: %s -> %s" % (c[:9], rid, col, o, n))
    for c, rid, col, old, new in breaches:
        o, n = delta(old, new)
        print("breach %s %s %s: %s -> %s" % (c[:9], rid, col, o, n))
    if breaches:
        print(
            "sources append-only breach %d change(s) in %d of %d commits"
            % (len(breaches), ncommits, scanned)
        )
        return 1
    print("sources append-only rows clean: %d commits scanned, 0 protected-cell changes" % scanned)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```
