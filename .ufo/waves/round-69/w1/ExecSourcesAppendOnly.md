# ExecSourcesAppendOnly — round-69 wave 1 (consistency / SOURCES append-only)

Seat scope: the assigned append-only gate, the frozen census count, the malformed-row count and the
frozen `sources-census.sh validate`. Read-only on the lane; every executing check was run from a
`git clone --shared` sandbox at `/tmp/r69-append-only-1717020`. No file inside the lane was written
except this report. No tool installs were made.

Measured lane tip: `a238989a96cb0d2b939679126b832d75b861ca6e` (`master`, = plan commit).
Assigned base: `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` (round-53 verifier spot-check).

## Verdict

**The three assigned numbers pass. The assigned gate predicate does not: it exits 1, not 0.**

Detail: row count 134 ✓, malformed rows 0 ✓, census validate exit 0 ✓ — but
`check_sources_append_only.py --base 422ffd10… --rev a238989…` exits **1** with exactly one breach.

The failure is **not round-69 debt**: the round-69 window is clean *and vacuous*, and the single
breach is an isolated, already-disclosed round-64 commit. The worktree append that carries round-69's
six new rows is a pure append and would pass the gate if committed. Details and the exact
disposition choices follow.

## 1. Required numbers (all four commands, exact results)

| # | check | result | expected | verdict |
|---|---|---|---|---|
| 1 | `check_sources_append_only.py --base 422ffd10… --rev a238989…` | **exit 1** — 1 breach, 1 of 20 commits | exit 0 | **FAIL** (carried r64 breach) |
| 2 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | **134** | 134 | PASS |
| 3 | malformed rows (row-shaped lines with NF≠13) | **0** | 0 | PASS |
| 4 | `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **exit 0**, 18 W04, `ok …/corpus/SOURCES.md` | exit 0 | PASS |

Full output of the failing gate:

```
log  5a097e12b S046 used-by: …les-round53.md -> …les-round53.md, corpus/l…
log  6de8e2eb4 S028 used-by: …les-round50.md -> …les-round50.md, corpus/k…
log  9e75e7345 S122 used-by: …ion-round66.md -> …ion-round66.md, corpus/l…
breach dad926c48 S120 teaches: … productive, §III-B2) -> … productive, §VI Related Work `#S6.p3.1`, sn…
sources append-only breach 1 change(s) in 1 of 20 commits
```

Gate self-test: `self-test: 0 failure(s) over 21 assertions`, exit 0.

Row-count note: the frozen 134 is the **worktree** figure. At `HEAD` the registry holds 128 rows; the
6-row delta is exactly the uncommitted round-69 append (S203–S208). 128 + 6 = 134 — the census
number is not stale, it is measuring the draft under review, as intended.

## 2. Breach diagnosis — one cell, one commit, already on the mistake ledger

Exact cell, parsed with the gate's own header-driven parser at `dad926c48^` and `dad926c48`:

```
S120 / teaches: 339 chars -> 385 chars
  "… caveat's section moved §III-B2 -> §VI Related Work `#S6.p3.1`, snapshot lines 1911-1916"
```

All ten other cells of S120 are byte-identical between parent and commit. `teaches` is a **protected**
cell (rule 2 permits only `status`, `recheck`, `used-by`), so this is a genuine rule-2 breach, not a
gate artefact.

Range decomposition (each run in the sandbox):

| range | commits scanned | result |
|---|---|---|
| `422ffd1..dad926c48` | 15 | exit 1 — the one breach |
| `dad926c48..a238989` (tail) | 5 | exit 0, 0 protected-cell changes, 1 permitted log (S122) |
| `a5f7459..a238989` (round-69 window) | **0** | exit 0 — *vacuous*: no round-69 commit touches `corpus/SOURCES.md` |

Why the round-69 window is vacuous: `git log --oneline a5f7459..a238989 -- corpus/SOURCES.md | wc -l`
→ `0`. Round-69's registry append exists **only in the working tree** (`M corpus/SOURCES.md`), so a
commit-walking gate cannot see it at all. Any "exit 0" quoted from that window is evidence about the
absence of commits, not about the append.

The breach is disclosed and unrepaired. `corpus/lessons/round-64.md`:

- line 107, mistake ledger: *"the append-only SOURCES gate flags the S120 teaches-cell caveat
  correction as a breach (in-place cell edit, same round as the row landed) | **recorded** —
  correction stands …; the `supersedes S120` row form is the round-65-compliant alternative"*;
- line 128 logs the citation move old → new.

`grep -nE 'supersedes S120' corpus/SOURCES.md` → **NONE**. The round-65-compliant remedy the lesson
itself names was never applied, so the registry's current S120 row is still the product of an
in-place edit, and no correction row carries the change.

**The lane already knows, and the exit-1 is the gate's designed verdict.** Three in-lane corroborations
mean this is a *known red arm with a standing disposition*, not a newly discovered bug:

- `LOG.md` round-64, **No-harm final**: *"The final battery at `9a66f0cc` (`receipts/noharm-final.txt`)
  is green on every arm except `sources` (`check_sources_append_only.py --base 422ffd10`): the wave-2
  correction of S120's teaches-cell caveat (`§III-B2` → `§VI Related Work #S6.p3.1`) is an in-place
  registry-cell edit, which the append-only draft gate flags as one breach. Disposition: the correction
  st[ands] …"*. The arm has been red since round 64, by decision.
- `SKILL.md:504` publishes precisely `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` with
  `0=clean, 1=failed, 2=could-not-evaluate`. The assigned command **is** the lane's documented gate
  invocation, and `1` is a legitimate published outcome — but it is not `0`, so any receipt that says
  "append-only clean" against this base is false.
- `corpus/QUALITY.md` **Q34**: append-only compliance is claimed only by running this gate over the
  claimed range and pasting it; it *"exits 1 on a protected-cell rewrite"*. My reading of the exit code
  is therefore the gate behaving as specified, not a measurement artefact.

A side observation on Q34's caveat ("at round 55 the gate reports a removed row by a crash, not a
verdict line"): that defect **no longer reproduces** — mutation arm D below gets a clean
`breach … S999 row: row present -> absent` verdict line.

**Structural point the wave must not miss:** exit 0 at base `422ffd1` is **unreachable by content
repair**. The gate walks every commit in the range; `dad926c48` is immutable lane history. Appending a
`supersedes S120` row today fixes the registry's *current* state but cannot change that commit's diff.
Only a narrowed `--base` (which hides a recorded breach) or a history rewrite (forbidden by the lane
bounds) changes the exit code.

## 3. The round-69 append itself is clean — and passes the gate when committed

Worktree vs `HEAD` (`HEAD:corpus/SOURCES.md` → 128 rows; worktree → 134 rows), compared cell-by-cell
with the gate's parser and permission set:

- line-level diff: **6 insertions, 0 deletions, 0 modifications**, all at `@@ -143,0 +144,6 @@` — pure append;
- added rows: `S203 S204 S205 S206 S207 S208`; removed rows: **none**;
- protected-cell changes on pre-existing rows: **NONE**;
- permitted-cell changes on pre-existing rows: **NONE**;
- every new row carries all 11 columns, `status=mined`, `opened=2026-10-25`, `recheck=90d`, and a real
  `used-by` (`corpus/knowledge/skill-name-precedence-round69.md` for S203–S207,
  `corpus/knowledge/client-trust-gates-round68.md` for S208);
- S208's teaches opens `supersedes S201 —`, i.e. the planned D5 supersede form. S207 carries no
  supersede clause (it is a new-scope row on the opencode document).

Forward proof: copying the lane's worktree `corpus/SOURCES.md` unchanged into the sandbox and
committing it gives

```
gate --base a5f7459… --rev <that commit>  -> sources append-only rows clean: 1 commits scanned,
                                             0 protected-cell changes   exit 0
gate --base 422ffd1… --rev <that commit>  -> still the dad926c48 breach   exit 1
```

So committing round-69's append does not add a breach; it also does not remove the carried one.

Census before/after (the plan's frontier step): **before = 16 W04** (sandbox at `HEAD`), **after = 18
W04** (worktree), exit 0 in both. The two new warnings are `S207` (opencode docs, the third row on
that document) and `S208` (Microsoft Agent Framework, explicit supersede). W04 is a warning and never
changes exit status, but the +2 delta is a real census movement that the round lesson's census-after
note must state — the plan's own text names 16 as the before-figure, so a silent 18 would be the
M109-class omission again.

## 4. Gate non-vacuity — four mutation arms, sandbox only

Run in `/tmp/r69-append-only-1717020`; the lane was never written.

| arm | world | result |
|---|---|---|
| A | append a new row | exit 0, `1 commits scanned, 0 protected-cell changes` |
| B | edit the appended row's `teaches` in place | exit 1, `breach … S999 teaches: teaches probe -> teaches PROBE-EDIT` |
| C2 | `status` queued→mined on the appended row, nothing else | exit 0, exactly one `log … S999 status: queued -> mined` |
| D | delete a row | exit 1, `breach … S999 row: row present -> absent` |

(Arm C in the first pass shared a range with arm B and therefore exited 1; arm C2 is the clean
permitted-only control.) The gate discriminates append / permitted-edit / protected-edit / deletion
correctly, so arm-A-style green lines are meaningful.

## 5. Rule-2 prose logging for the three permitted-cell notes — complete

Rule 2 also requires each in-place `status`/`recheck`/`used-by` change to be logged old→new in the
round lesson. All three notes in the assigned range are documented:

- `S046` — `corpus/lessons/round-54.md:46` (`used-by` old → new, round-53 spot-check routed defect 2);
- `S028` — `corpus/lessons/round-58.md:38-40` (`### Rows touched (old → new)`, `used-by` old → new);
- `S122` — `corpus/lessons/round-66.md:36` (`used-by` old → new).

No prose gap on the permitted cells.

## 6. Disposition options for the L1 (ranked, with the cost of each)

Given the round-64 standing disposition ("correction stands"), the wave has **no obligation to make
this gate green** — but it has a hard obligation not to report it green. What round 69 can decide is
whether the *current registry state* gets the compliance form the round-64 lesson already named.

1. **Fix forward + keep the honest base (recommended).** Append a `supersedes S120 —` row quoting the
   `§VI Related Work #S6.p3.1, snapshot lines 1911-1916` repair (the form `round-64.md:107` named),
   so the registry's current state is compliant. The assigned predicate still exits 1 and **must be
   reported as exit 1**, with `dad926c48` and the round-64 ledger line as the attributed cause.
2. **Re-base the gate, disclose the exclusion.** `--base dad926c48` (exclusive) or
   `--base a5f7459` yields exit 0, but the former silently skips the one recorded breach and the
   latter scans 0 commits. Either is acceptable **only** with the exclusion written into the receipt
   next to the command; neither may be presented as "append-only verified clean since round 53".
3. **History rewrite** — forbidden by the lane bounds. Not a candidate.

Do not let a future seat restate this as "append-only exits 0": at the assigned base it does not, and
the reason is recorded in two places inside the lane's own lessons.

## 7. Environment notes worth keeping

- `sources-census.sh validate --file` resolves `used-by` paths relative to the **file's own directory**;
  pointing it at a `/tmp` copy produces a wall of spurious `E11` and exit 1. Validate a copy only when
  it sits at `<lane>/corpus/SOURCES.md`, or pass the lane directory as the argument and let the script
  find the registry (what was done here for the after-state).
- The sandbox clone is `git clone --shared` of the lane; the 269 MB `round-68/w1/controls/c2falsify-clone`
  is untracked and does not travel into it, so the sandbox is cheap and contains no control scratch.
- No tool installs or updates were made for this seat.

## Retained evidence

- sandbox: `/tmp/r69-append-only-1717020` (disposable; shared clone)
- all commands and outputs quoted above; every executing run happened in the sandbox, the lane saw
  only `git show`/`git log`/`git diff`/`grep`/`awk` (read-only)
- `dad926c48ab3cfc550cdc240856efa3171be9e29` = the single breach commit (round-64 wave-2 integration)
- `a5f7459f99bb27bf697e9438362e75ac5833eca8` = round-69 base / `a238989a96cb0d2b939679126b832d75b861ca6e` = measured tip
