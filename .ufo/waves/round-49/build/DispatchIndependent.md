# DispatchIndependent — C2 second instrument (independence arm)

Round 49 build wave, kotoba lane. Independent second instrument for claim C2
(operability). Author seat; not the author of `verifiers/verify_dispatch_prompts.py`.

## Findings (read these first)

1. **The prompt directory is a moving target during the wave.** `.ufo/prompts/` gained 2
   files between two runs 25 minutes apart (375 → 377 scanned; 288 → 289 in scope;
   dispatch.08 failures 165 → 166). Every count here is pinned to the `generated_at_utc`
   stamp in `indep.json`; the L1 must re-run to compare against the other instrument,
   not compare against these numbers.

2. **dispatch.04 — 7 failures out of 289 in-scope files (282 pass).** Six `*-L1.md`
   prompts carry the literal `<lane>` placeholder in their report path
   (`.ufo/reports/round-1/<lane>.md`) and a stem that is not the lane id: `kake-L1.md`,
   `kasegi-L1.md`, `kengaku-L1.md`, `kotoba-L1.md`, `kumitate-L1.md`, `protocol-L1.md`.
   The seventh is `aggregator-L1.md`, whose report path stem is `AGGREGATE.md` — a fleet
   convention (the file `.ufo/reports/AGGREGATE.md` exists at the fleet root), not a
   placeholder; the box's literal reading fails it and the convention is recorded in the
   record's `convention_exception` field, not as a pass. **This is the box's own named
   defect** ("a `<lane>` placeholder cost two lanes their canonical round-1 report
   names") — here it is six lanes.

3. **dispatch.08 — 166 failures out of 289 in-scope files (123 pass), and every one comes
   from the state-bound conjunct alone.** Conjunct breakdown: `token_identity = 0`,
   `state_bound = 166`. Across all 289 in-scope prompts there is **not one** round-token
   mismatch between filename, role line and report dir: the round-token identity
   property the box names is *clean* on this corpus, and the failures are entirely the
   `≤ .ufo/state/<id>.round` comparison.

4. **Root cause of the 166: the fleet's `.ufo/state/<id>.round` files are stale, not the
   prompts.** All 21 `.round` files carry mtime `2026-10-15` — unwritten for a week,
   while the lanes are at rounds 16–62. Measured examples: `kotoba.round=16` while
   `kotoba.report-baseline=49` and the lane is at round 49; `kagi.round=16` while kagi
   is at 28; `revenger.round=1` while revenger is at 62. Reading the lane's *live*
   next-round value from the hyaku driver's own state dir
   (`~/.local/state/shokunin-hyaku/next/<lane>`) instead: **159 of the 166 failures
   would pass**; the remaining **7 are the same 7 files** with no entry in that dir at
   all (`aggregator-round-11/12.md`, `audio-round-101.md`,
   `game-dev-2d-round-105.md`, `game-dev-3d-round-108.md`, `lore-round-103.md`,
   `protocol-round-15.md`). **The box as written compares a prompt against a stale
   anchor** — a finding about the corpus, not a defect in the prompts, and the single
   thing the L1 most needs before reading either instrument's dispatch.08 numbers.

5. **Two lanes have no `.round` file at all** — `kotodama` and `souji` (only
   `.report-baseline`). Their 14 prompts fail dispatch.08 with "no state file for lane
   X, so N <= state round cannot be established" — the bound is unverifiable, not
   violated; they are marked `unverifiable` on the state component. An implementation
   treating an absent anchor as "not applicable" would score them pass; mine scores
   them fail and flags the difference. **22 in-scope files in total carry an
   unverifiable dispatch.08 component**: these 14 plus the 8 `*-L1.md` prompts (an
   `-L1` filename carries no round token, so that conjunct cannot be checked).

## Judgement calls (for the L1's diff)

Each is a place where a second implementation could reasonably differ.

| # | judgement | what I chose | why |
|---|---|---|---|
| J1 | **Where the report path is** | every occurrence of `.ufo/reports/round-<N>/<stem>` in the body; the stem is stripped of trailing prose punctuation (`:`, `,`, `.`, `;`); **all** occurrences must satisfy dispatch.04. A `.ufo/reports/round-N/` reference with no file stem is a *directory* reference, excluded from both boxes | the box says "the report path", singular; in practice it appears 1–4× per file, always with the same round. `aggregator-L1.md` L7 names the dir, L9 the file; counting the dir as a path would fabricate a stem mismatch |
| J2 | **Which lane id** | parsed from the prompt **file name**, never from the role line's self-description | the box says "the lane's `<id>`" and "filename = the lane's `<id>`". Role lines disagree with file names in several lanes (`kasegi-shokunin` vs `kasegi`, `shokunin-protocol` vs `protocol`) |
| J3 | **`*-L1.md` files** | in scope; dispatch.04 applies normally; for dispatch.08 the *filename* conjunct is `unverifiable` (an `-L1` name carries no token) while role-line, report-dir and state-bound are still checked | the box puts spawn and round files in one checklist; failing all 8 L1 files on a filename that structurally cannot carry a token would be a false red |
| J4 | **`*-round-N-continuation-<tag>.md`** | in scope as an ordinary round prompt; the token is the `<N>` after `-round-`; the tag goes into `filename_round_suffix`, ignored for the token | the tag names a *continuation of* round N. 4 such files (`revenger`, `tabi`, `tameshi`, `tsukuroi`, all `-continuation-kaika`) |
| J5 | **`closure/` subdirectory** | **out of scope** (88 files) — measured and reported per file, not counted in the in-scope totals | these are hyaku *non-author integrator* prompts, not a lane's own round dispatch prompt. Their per-file verdicts are in `indep.json` for the L1 to diff either way |
| J6 | **Which state file** | the lane's own `.ufo/state/<id>.round`, keyed by the file-name lane id — never a sibling's file | the box says so explicitly ("equality against a sibling's state is wrong") |
| J7 | **Stale anchor** | the box is applied **literally** against the stale `.round` value (so 166 fail); a diagnostic `alt_state_round` field records the live value without changing any verdict | I must not quietly substitute a different authority to make the numbers look better; the staleness is reported as a finding instead |
| J8 | **Absent anchor** | absent `.round` → dispatch.08 **fails** with "cannot be established", state component marked `unverifiable` | the box asserts a bound that cannot be shown to hold; scoring it pass would assert something unverified |
| J9 | **The `AGGREGATE.md` stem** | dispatch.04 **fails** `aggregator-L1.md`; the convention is recorded in `convention_exception` only | the box's literal text says filename = lane id; the reader gets both facts |
| J10 | **Role-line round extraction** | first non-blank line, plus the next 4 lines as fallback | the closure-role form states `**chousa round 27**` on its *second* line; the lane-dispatch form has it on line 1 |
| J11 | **Unsubstituted variable** | a stem containing `<…>`, `${…}`, `{{…}}` or `$VAR` fails dispatch.04 | the box names "no `<…>` placeholder or unsubstituted variable" |
| J12 | **In-scope surface** | the prompt directory's own `*.md` files (289 at the pinned stamp) | the checklist says "observed form: `/home/vgpnk/projects/shokunin/.ufo/prompts/`" |

## Totals (pinned to `indep.json` `generated_at_utc = 2026-10-22T10:22:59+00:00`)

```
files scanned: 377     in-scope: 289   out-of-scope: 88   {"closure": 88, "dispatch": 289}
failures dispatch.04: 7   (passes 282)
failures dispatch.08: 166 (passes 123)
dispatch.08 conjunct breakdown: token_identity=0 state_bound=166
dispatch.08 failure classes: {"state-bound-exceeded": 166}
dispatch.08 alt-state diagnostic: {"failures_that_persist_on_alt_state": 7,
  "failures_that_would_pass_on_alt_state": 159, "failures_with_no_alt_state_value": 7}
```
Failing files (dispatch.04, 7): `aggregator-L1.md`, `kake-L1.md`, `kasegi-L1.md`,
`kengaku-L1.md`, `kotoba-L1.md`, `kumitate-L1.md`, `protocol-L1.md`.
Failing files (dispatch.08, 166): every in-scope file whose round token exceeds its
lane's `.ufo/state/<id>.round`; list: `summary.failing_files["dispatch.08"]` in
`indep.json` and in `run.txt`.

## Evidence (commands, exit codes, paths)

```
$ python3 indep.py --self-test
SELF-TEST PASS: 8 fixture arms behaved as specified          # exit 0
```
The 8 self-test arms cover: pass/pass; `<lane>` placeholder (04 fail, 08 fail);
wrong stem (04 fail, 08 pass); role-line mismatch (04 pass, 08 fail); token over
state (04 pass, 08 fail); `${LANE}` variable (04 fail, 08 pass); report-dir ≠ role
line (04 pass, 08 fail); `*-L1.md` form (pass/pass). Each arm has a must-fail
counterpart; `--self-test` exits non-zero on any misbehaviour.

```
$ python3 indep.py --out indep.json                               # exit 0
$ ls -1 .ufo/prompts/*.md | wc -l                                 → 289
$ ls -1 .ufo/prompts/closure/*.md | wc -l                          → 88
$ grep -lE '\.ufo/reports/round-[0-9]+/<lane>\.md' *.md | wc -l    → 6
$ grep -lE '\.ufo/reports/round-[0-9]+/AGGREGATE\.md' *.md         → aggregator-L1.md
$ ls -l --time-style=+%Y-%m-%d .ufo/state/*.round | awk '{print $6}' | sort -u → 2026-10-15
$ cat .ufo/state/kotoba.round / cut -d' ' -f1 .ufo/state/kotoba.report-baseline → 16 / 49
$ cat ~/.local/state/shokunin-hyaku/next/kotoba                   → 49
$ ls .ufo/state/kotodama.round .ufo/state/souji.round → No such file (exit 2)
```
(paths relative to the fleet root `/home/vgpnk/Projects/shokunin`.) Determinism: two
consecutive runs over an unchanged directory gave identical per-file verdicts for all
377 files and an identical summary.

Artifacts (outside the lane checkout, in the seat scratch dir; hashes are of the pinned
`generated_at_utc = 2026-10-22T10:22:59+00:00` run; `run.txt` is that run's stdout;
full prefix `/fast/scratch/hyaku/kotoba-r49/seats/DispatchIndependent/`):

| path | sha256 |
|---|---|
| `indep.py` | `86f111659906cdb2898825b2a7613a03287f5775eb32ffddba2e4f0e76dd44f4` |
| `indep.json` | `267e9c62703d2263c4f8e9cdc388f1588c01287b7f1a9670b84d44b8061f37fa` |

## Scope and bounds honoured

- Did **not** read `verifiers/verify_dispatch_prompts.py` or any other lane verifier;
  the two boxes were implemented from the SKILL.md box texts only (`SKILL.md:313-315`,
  `:325-327`).
- Read-only on `.ufo/prompts` and `.ufo/state`; wrote nothing outside the seat scratch
  dir and this report file. No git/jj write command in the lane, the fleet repo, or any
  sibling lane. No tool install needed (Python 3 stdlib only).

## Risks / what the L1 should decide

- **R1 (high) — the state anchor.** dispatch.08's `≤` conjunct is measured against a
  stale file. If the L1's other instrument reads the same `.round` files, both report
  ~166 failures and agree — but both are measuring staleness, not prompt quality. If
  the other instrument reads a different anchor, the numbers diverge for a reason that
  is *not* a per-file prompt disagreement, and the diff must not be read as "the
  prompts changed". I recommend the L1 state the anchor in the other instrument's
  docstring before comparing.
- **R2 (medium) — the moving population.** Counts drift within the wave; pin both
  instruments to one snapshot, or compare per-file verdicts by name, not count.
- **R3 (medium) — absent-anchor policy (J8), 14 files**; **R4 (medium) — L1-file
  filename conjunct (J3), 8 files**; **R5 (low) — closure scope (J5), 88 files**;
  **R6 (low) — `AGGREGATE.md` (J9), 1 file**. Each is a policy choice where the other
  instrument could reasonably differ; every affected file's verdict is in `indep.json`,
  so the diff reconciles file by file rather than by count.
