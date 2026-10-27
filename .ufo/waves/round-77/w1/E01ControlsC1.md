# E01ControlsC1 — Q37 C1 control worlds on the frozen blob

Seat: E01ControlsC1 (executor, leaf) · kotoba round 77, wave w1 · 2026-10-27
Claim: C1 depth (sourced, S213). Instrument: `verifiers/check_desc_craft.py`,
frozen bytes sha256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`.

## Headline

**No counter defect.** All five must-fail worlds fail with their own exit status 1 and
none of them prints `description craft backed 6 of 6`; the honest attribution arm
prints exactly `description craft backed 6 of 6` and exits 0. The frozen blob is
satisfiable by an honest world built on the real committed base bytes, and it rejects
each of the five shortcuts (fabrication, wrong-page real text, token dump, cheapest
do-nothing, number reformatting).

Nothing was edited in the lane tree, the lane index or any verifier; no claim data was
written (freeze discipline).

## Frozen blob verification (three independent byte sources)

| source | sha256 |
|---|---|
| lane worktree `verifiers/check_desc_craft.py` | `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` |
| committed blob at lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (read from a `git clone --shared` scratch clone) | same |
| the counter copy each world was scored with | same |
| `--print-self-sha` of that copy | `d5a06d6e89c7515e46096515f631a921377252fe574153b266a8beeae96c9da1` |

The counter's own in-file drift guard therefore passed on every scoring run (a drifted
copy exits 2, never 0). Interpreter: `/usr/bin/python3` (Python 3.14.8).

## Worlds and results

Each world is an isolated scratch git repo (`mktemp -d` under
`/fast/scratch/hyaku/kotoba-r77/E01ControlsC1/worlds`), `git -C "$D" init -q`, local
`user.name=scratch-r77` / `user.email=scratch@example.invalid`, a `rev-parse
--show-toplevel` assertion equal to the world dir before the one `add` + `commit`, and
explicit `-C` on every git call. Real bytes come from the claim base
`2f675548eaad2a037a899d39247c1fd7a88aaf48` (SKILL.md, `corpus/SOURCES.md`, and the three
committed page snapshots + `MANIFEST.sha256` + `fetch-record.json`); the snapshot digests
were asserted equal to the counter's pinned `PAGE_SHA` constants before any world used them.

Scoring form, one subprocess per world (no pipeline, so no pipeline exit status):

```
python3 -B <counter-copy> --repo <world> --rev <world-head>   # exit code = process's own
```

| world | construction (delta against W0) | must fail because | exit | printed | failing conjuncts |
|---|---|---|---|---|---|
| **W0** honest baseline (attribution arm, not a must-fail world) | base SKILL.md + one act-on row in § Body craft; S213 `used-by` cell extended; entry with 5 located page-unique quotes, audit 1022/151, provenance trio; lesson with `## Gate` + old→new log; the three real snapshots + manifest + fetch record | — (it must reach the target; every must-fail world differs from it in one dimension) | **0** | `description craft backed 6 of 6` | none |
| **W1** fabricated | stub entry + no snapshot bytes; no lesson, no registry edit, no audit table | nothing backs any conjunct | 1 | `backed 0 of 6` | a b c d e f |
| **W2** wrong-page real text | W0 with the rule rows quoting the committed **best-practices** snapshot verbatim | the page-unique arm of (b) must reject real bytes from the wrong page | 1 | `backed 5 of 6` | b |
| **W3** token dump | W0 with the entry replaced by a trio + a heading naming `(a)…(f)` and no content | naming conjuncts is not content | 1 | `backed 4 of 6` | b d |
| **W4** cheapest do-nothing | only the rewritten SKILL.md row + the S213 `used-by` edit; no entry, no lesson, no snapshots | the two cheapest edits alone back nothing | 1 | `backed 0 of 6` | a b c d e f |
| **W5** audit numbers reformatted | W0 with the audit table stating the stripped render 1021 instead of the clip-preserving 1022 | (d) recomputes from this world's SKILL.md and must reject the renumbered value | 1 | `backed 5 of 6` | d |

Printed matrix (from the receipt, `P` = the counter's own `: pass`, `F` = `: fail`):

```
world  backed exit  (a) (b) (c) (d) (e) (f)
W0       6/6    0  P P P P P P
W1       0/6    1  F F F F F F
W2       5/6    1  P F P P P P
W3       4/6    1  P F P F P P
W4       0/6    1  F F F F F F
W5       5/6    1  P P P F P P
```

Exact counter findings for the targeted arms (verbatim from the receipt):

- W2 `(b) corpus/knowledge/description-craft-round76.md carries 1 located page-unique quote(s) of the required 4`
- W3 `(b) … carries 0 located page-unique quote(s) of the required 4` and two (d) findings
- W5 `(d) the entry's rendered \`description\` length [1021] does not equal the recomputed clip render 1022 (stripped variant 1021)`

World tip revisions recorded in the receipt (the worlds themselves were scratch repos and
are removed per the seat rule): W0 `16764e0b…`, W1 `0bdf5250…`, W2 `a23cdd9c…`,
W3 `bf5cb389…`, W4 `cecac9bf…`, W5 `876a6bad…` (full 40-hex in the receipt).

## How each arm actually bites (grounded in the counter's own code paths)

- **(b)** counts a double-quoted span only when it is 3–25 words, occurs on a single
  physical line after the page's first heading in the optimizing-descriptions snapshot,
  is absent from *both* other snapshots (page-unique), and at least one of its occurrence
  lines is cited somewhere in the entry. W2's five best-practices quotes are real, verbatim
  and individually page-unique — the arm rejects them solely on the wrong page, which is
  the falsifier the plan asks for. W2 counts 1 rather than 0 only because its source line
  keeps the honest head-line quote (`Err on the side of being pushy`, `optimizing-descriptions.md:27`);
  the threshold of 4 still fails it.
- **(c)** needs one Body craft row citing both the entry path and `S213` and carrying at
  least two ≥3-word quote/backtick spans located in the snapshot. Verified against the
  *real* SKILL.md section (`### Body craft — the specification's skill-creation guides`,
  one matching heading at line 205) — not against a fixture.
- **(d)** recomputes from the world's committed `SKILL.md`. Inserting the Body craft row
  leaves the frontmatter untouched: clip **1022** / stripped **1021** / first sentence
  **151** before and after (the driver hard-fails if the insertion changes them). W5 shows
  that only the clip value passes; 1021 is rejected.
- **(a)** accepts the real round-76 snapshot set unchanged (digests, manifest, HTTP-200
  fetch record with matching byte counts) and fails closed on an empty snapshot set (W1)
  or a missing set (W4).
- **(e)/(f)** fail in W1/W4 for the plainest reasons (no registry, no provenance line); in
  W0 they pass on the real `corpus/SOURCES.md` with only the S213 cell extended, plus a
  lesson paragraph in the lane's `old -> new` house style.

## Cross-checks run

- The frozen counter's own `--self-test --work <scratch>/selftest`: **exit 0**,
  `self-test: 0 failure(s) over 53 assertions` — consistent with the plan's
  `receipts/selftests-base.txt` (53 assertions). Run on the frozen copy, in scratch.
- The r76 control receipt (`.ufo/waves/round-76/receipts/c1-controls.txt`) was scored on an
  earlier blob (`87837d7aad4eb570a1a50734358077f1513b6ba8862e31a9c9d7d98283d3cd25`). Its
  qualitative outcomes (all must-fail worlds exit 1, honest world 6/6 exit 0) are
  reproduced here on the frozen `cf3c45d9…` blob. The per-arm counts differ where the
  worlds are constructed differently: r76's fabricated arm kept `SOURCES.md` and the entry's
  source line honest and printed `2 of 6`, while W1 here strips those too and prints
  `0 of 6`; r76's wrong-page arm printed `0 of 6` for (b) where W2 counts 1 (honest head
  quote kept) and still fails. Both runs agree on the property that matters: nothing that
  must fail reaches the target.

## What this does and does not prove

- **Does**: the frozen predicate is satisfiable on the real committed base bytes, and each
  of the five named shortcuts is rejected with the intended conjunct. A control world that
  met the target would have been reported first as a counter defect; none did.
- **Does not**: this is not claim data and not the r77 landing. W0's entry is instrument
  text assembled by this seat to prove satisfiability; the wave's data drafts
  (`.ufo/waves/round-76/build/entry-draft.md`, `skill-patch.md`, …) and their verification
  against the frozen counter are other seats' work (E06 and the w2 falsifiers). Nothing
  from W0 was pasted into the lane.

## Hygiene and scope

- No installs, no upgrades, no `pacman` (host-wide pause respected).
- Lane writes: only the three files below. The lane git index, jj state, `MANIFEST.json`,
  `templates/`, `scripts/`, `.ufo/state/` and `considerthese/` were not touched; the only
  lane changes in `git status` are the wave's own untracked `.ufo/waves/round-77/` paths.
- Scratch `/fast/scratch/hyaku/kotoba-r77/E01ControlsC1` (clone, worlds, counter copy,
  selftest worlds) was removed after the receipt was written; a stray `__pycache__` from a
  syntax check was deleted. A `TMPDIR` pointing under `/tmp` is refused by the driver.

## Risks / blockers

- The six worlds were scratch repos and are gone; they are reproducible only by re-running
  the driver. The receipt is the retained artifact (world file lists, tip revs, exact
  commands, per-run stdout and exit codes).
- W1 and W4 both print 0 of 6 by construction; they falsify different shortcuts (fabrication
  vs. the two cheapest edits) but they do not separate (e)/(f) from (a)/(b)/(c)/(d). The
  counter's own `--self-test` carries the per-conjunct arms for those.
- No blockers: the assignment's required evidence exists and every gate was run with its own
  exit status.

## Files written

- `.ufo/waves/round-77/build/E01ControlsC1.build_controls.py` (driver; honours `--work`
  then `TMPDIR`, never `/tmp`; asserts toplevel, local git identity, and the three counter
  digests; refuses to score if the lane/copy blob is not the frozen hash)
- `.ufo/waves/round-77/build/E01ControlsC1.c1-controls.txt` (receipt: counter sha256 on its
  first lines, per-world why/rev/files/command/exit/stdout, matrix, verdict)
- `.ufo/waves/round-77/w1/E01ControlsC1.md` (this report)

VERDICT: PASS — on the frozen C1 blob (cf3c45d9…), all five must-fail control worlds exit 1 without reaching the target and the honest attribution world prints exactly `description craft backed 6 of 6` (exit 0); no counter defect.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E01ControlsC1.build_controls.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E01ControlsC1.c1-controls.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E01ControlsC1.md
