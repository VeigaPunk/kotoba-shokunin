# ConnectorOverlapR99 — overlap scan and planning data-walk (round 99, w1)

Read-only seat. No repo writes; every measurement below is a read at the lane freeze
`b53e209603e7c480cd975ea543e415b66f695438` (round base `52e8e95a`, instrument `c0489d14`) unless a
revision is named. Scratch `/fast/scratch/hyaku/kotoba-r99/ConnectorOverlapR99` (removed before
yield); receipts under `.ufo/waves/round-99/w1/ConnectorOverlapR99/`.

## Part 1 — cross-claim overlap: C1 ↔ C2

Short answer. **C1 → C2: one hard coupling and three soft ones.** C1's `self_test()` edit cannot
move any C2 *predicate* conjunct except through the checklist gate's delegated `--box-proof`, which
C1's kill rule already pins at `boxes proven 2` rc 0. **C2 → C1: no coupling at all** — the dispatch
self-test reads only `SKILL.md` and its own tempdir, and none of C2's files is on that path. The
non-obvious exposures are second-order: (i) the L1's own round-99 `LOG.md`/`SCORECARD.md` append is
inside C2's landing reading, and (ii) C1's added arms spend the tip battery's 280 s floors-gate
headroom, which C2's *predicate* does not read but the landing's no-harm reading does.

### 1.1 What C2 reads of C1's surface (exact lines)

| C2 surface | exact lines | what it does with `verifiers/verify_dispatch_prompts.py` | effect of C1's `self_test()` edit |
|---|---|---|---|
| `verify_skill_checklist.py` delegated box proof | `:1031` `def delegated_box_proof`, `:1045` `supports_box_proof`, `:1059-1064` `subprocess.run(argv … cwd=base)`, `:1065` `if proc.returncode != 0`, `:1314` call site | **executes** `verify_dispatch_prompts.py --box-proof --map <map>` from the sandbox root; a non-zero exit is a `problem` and the checklist gate is red | none **iff** `--box-proof` stays `boxes proven 2` rc 0 — C1's kill rule (`plans/round-99.md` § C1) pins exactly this |
| `verify_skill_checklist.py --self-test` (C2 `SELFTEST_FLOOR` 1864, `carried-reds.py:68-73`) | `:2632-2725` delegated-proof arms (`delegated_tree` `:2639`, stubs `:2671-2687`, tempdir `:2688`) | never runs the live dispatch file | none |
| `check_assertion_floors.py` row | `:257-258` `"dispatch_prompts": ("verifiers/verify_dispatch_prompts.py", 56, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)`; comparison `:685` `assertions >= floor and failures == 0 and proc.returncode == 0`; child timeout `:671-675` (base 360 s, `:208`) | reruns `--self-test`, parses the summary line | floor is a **minimum** (56 vs 128 observed) → adding arms keeps it PASS; the summary line format must stay byte-shaped `^(\d+) failure\(s\) over (\d+) assertions$` |
| `verifiers/floors-registry.json` | `:49-52` `"dispatch_prompts": {"floor": 56, "path": "verifiers/verify_dispatch_prompts.py"}` | path + floor only, no sha | none |
| `check_gate_registry.py` `judge_row` | `:178-223`; self-test flag needs an exact `add_argument` handler `:204-208`; pinned-value paths must exist `:210-219` | reads the `SKILL.md:491` row and the script's AST | C1 must keep `--self-test` and `--box-proof` as exact `add_argument` handlers and keep `verifiers/checklist-baseline.json` + `verifiers/fixtures/dispatch-prompts/manifest.json` present |
| `check_tip_battery.py` guards | `INSTRUMENT_PINS` `:132-176` (**no** `verify_dispatch_prompts.py` row), `BATTERY` `:178-185` (six scripts, not this one), `instrument-size` diff `:325-341`, `no-deletions` `:288-297`, `instrument-pin` `:343-352`, guard ids `:423-426` | none of the five guards reads the dispatch file's bytes | **zero** effect on C2's `guards 5 of 5` conjunct |
| `carried-reds.py` predicate | `:58-66` `GATES`/`FROZEN`/`BATTERY`, `:68-73` floors, `:195-206` reds loop, `:245-246` guards parse, `:252` `met` | `met = green == 3 and held == 3 and frozen == 4 and guards_ok` | the battery's **gate exits are not in the predicate** (only `guards 5 of 5`); so the floors-gate wall time is not a C2 predicate risk |

Measured at the freeze (receipts in this directory): `verify_dispatch_prompts.py --self-test` →
`0 failure(s) over 128 assertions`, wall 0.11 s; `--box-proof` → `boxes proven 2`, wall 0.05 s;
`check_gate_registry.py --rev b53e2096` → `gate registry rows conformant 74 of 74 lane verifiers;
phantom 0`, rc 0.

### 1.2 What C1 reads of C2's surface — nothing

The C1 counter exports REV with `git archive` (rule 8) and runs `--self-test` in a per-run copy. The
self-test spans `verifiers/verify_dispatch_prompts.py:679-1525`; its only live read is
`Path(__file__).resolve().parent.parent / SKILL_NAME` (`:990-996`), i.e. the tree's `SKILL.md`, and
every fixture write goes under its tempdir (`root / "proof"`, `:1004`). It reads no `corpus/` file,
no `LOG.md`, no `SCORECARD.md`, no `verifiers/corpus-baseline.json` and no
`verifiers/checklist-baseline.json` (that name is only used for the synthetic map it writes at
`:1025-1029`). C2's changed files are `corpus/README.md`, `corpus/lessons/round-81.md`,
`corpus/lessons/round-99.md`, `corpus/SOURCES.md`, `verifiers/corpus-baseline.json`,
`verifiers/verify_skill_checklist.py`, `verifiers/check_tip_battery.py`, `LOG.md` — none on the
self-test's read path. The C1 counter's 49 frozen anchors all live in
`verifiers/verify_dispatch_prompts.py`, which C2 does not touch (verified: every anchor of
`CLAIMS["c1"]`, `["r98c1"]`, `["r97c1"]`, `["r96c1"]` matches exactly once at the freeze).

The exact C2 change sites, each named against the C1 read path:

| C2 change | exact site | read by the dispatch self-test? |
|---|---|---|
| coverage-map rows | `corpus/README.md` (appended table rows; no line pin) | no |
| round-81 hash quoting | `corpus/lessons/round-81.md:8` | no |
| equal-mode baseline | `verifiers/corpus-baseline.json` (read at `verify_corpus_integrity.py:806-816`) | no |
| checklist corrections data | `verifiers/verify_skill_checklist.py:425` `GOVERNANCE_CORRECTIONS_HORIZON` + `:426` `GOVERNANCE_CORRECTIONS` block | no |
| battery pin | `verifiers/check_tip_battery.py:132-176` `INSTRUMENT_PINS` | no |
| correction notice | end of `LOG.md` (append) | no |

The C1 counter reads the counter's own tables (frozen at `c0489d14`) and, per run, a `git archive`
export of REV; it never reads `verifiers/verify_skill_checklist.py`, `verifiers/check_tip_battery.py`,
`verifiers/corpus-baseline.json`, `corpus/*` or `LOG.md` for a verdict.

### 1.3 The one hard coupling, and its failure mode

C2's checklist green is a **tripwire on C1's production code**: `verify_skill_checklist.py:1314`
runs the dispatch instrument's `--box-proof` and `:1065` reds the checklist on any non-zero exit.
If C1's edit (or a helper it adds) changes `box_proof()` or its exit ladder, C2 fails at the landing
**while C1's own counter can still read MET** — the `c1` table has no box-proof-exit mutant. The
reverse is not true: C2's data-only checklist change cannot move the dispatch self-test.

### 1.4 Second-order: the L1's own append is inside C2's landing reading

`verify_skill_checklist.py:394` `GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")`;
`check_governance_citations` (`:1752-1817`) scans **every line** of both files (`citation_subjects`
`:1612`, called `:1781`), and the
`GOVERNANCE_CORRECTIONS_HORIZON` only bounds which notice lines may *excuse* a subject. The C2
counter is measured at the landing, so the L1's round-99 `LOG.md` entry (appended after the
ExecRedsR99 notice) and its `SCORECARD.md` entry are scanned: one repo-rooted dead `.ufo/...`
citation or one nonexistent path in either re-reds the checklist and C2 fails. `plans/round-99.md`
§ C2 already states this rule; this is the mechanism it rests on.

### 1.5 Timing: C1's arms spend the battery's floors-gate headroom

Measured at the freeze under this wave's load (receipt `base-readings.txt`):
`python3 -B verifiers/check_assertion_floors.py` → `PASS dispatch_prompts observed=128 floor=56`,
**WALL 226.07 s** against `check_tip_battery.py:113` `GATE_TIMEOUT_S = 280` → 53.9 s headroom. The
floors guard reruns 19 self-tests (`check_assertion_floors.py:662`), the dispatch one included, so
every second C1's arms add is spent inside that cap. C2's predicate does not read the battery's gate
exits (§1.1 last row), but the landing's `tip battery exit 0: N of 6` does — a load spike or a
subprocess-spending C1 arm can turn that row red without any gate being wrong.

### 1.6 Corpus baseline ordering (C2 internal, stated for the integration)

At the freeze: `verify_corpus_integrity.py` → `tracked=203 unindexed=8 report_total=166
commit_total=73 unresolvable=1`, `4/9 checks pass`, rc 1; `verify_corpus_independent.py` rc 1;
`verify_skill_checklist.py` rc 1 with **10 PASS, 1 FAIL, 0 N/A** (the one FAIL is
`governance.citation_resolves`, `evaluated 1652`). `carried-reds.py:64` `CHECKLIST_PASS_MIN = 11`
is the gate's whole check count, so the C2 route must turn that single FAIL into the 11th PASS —
there is no spare check. The equal-mode counts
(`verify_corpus_integrity.py:806-816`) are compared to `verifiers/corpus-baseline.json`, so the
baseline must be re-recorded **after** every corpus change of the landing tree: ExecRedsR99's
re-record is against its own candidate, and ScribeCorpusR99's `corpus/lessons/round-99.md` (+1
tracked, +1 coverage row, possibly +1 report/commit citation) and the `S281` row drift it. The
round-81 quote fix also moves `commit_total` 73 → 72. The C2 counter's `frozen` conjuncts do not
include the baseline, so this is a `reds` conjunct risk only, exactly as `plans/round-99.md` says.

One C2-internal coupling to state: `check_correction_sweep.py` (a battery gate, not in the C2
predicate) reads `corpus/README.md` blocks at registry rows `:32` (`r51-c2-readme`), `:44`
(`r52-c2-readme-five`), `:65` (`r53-c2-readme-six-child`) and `:82`
(`r58-r2-readme-plugin-sources`); at the freeze it reads `correction sweep: 0 stale block(s)` rc 0.
ExecRedsR99's coverage-map rows must not remove a declared pattern from a block that carries its
stale phrase, or the landing's `tip battery exit 0: N of 6` drops a row with no C2 predicate change.

## Part 2 — sibling lanes (read-only)

### 2.1 The ScoutTipReds F6 class: no-harm rules that accept an unchanged red set

| lane / file:line | clause | class |
|---|---|---|
| `kama-shokunin/plans/round-87-claims.md:99-100` | "Harm rule: every `PRE_REPORT_ARM` line that is `ok` at `362b0d4a` … stays `ok` at `R`; … **Arms that were red at base may turn green**" | one-directional no-harm: base-red arms are never required to heal (the F6 shape in a harm rule) |
| `kama-shokunin/plans/round-80-claims.md:177-179` | "Arm 8 is therefore red at the base and stays red at the tip; this round adds no append-only deletion of its own and **reports the inherited red as debt, never as a green gate**" | inherited red accepted as debt — the exact F6 acceptance |
| `game-dev-3d-shokunin/reports/round-104/r104-verification-protocol.md:589` | "On this host a *full* run always exits `1` (the known reds below), so a non-zero exit there is **expected**, not a regression" | a documented standing red set written into the verification protocol |

Contrast (the class's origin, for the report): `kotoba-shokunin/plans/round-98.md:26` — "the landing
tip battery is a no-harm reading (red set must not grow)" — is what round 99's C2 replaces with a
counter that must read MET (`plans/round-99.md:126-127`). The three sibling clauses above are the
same acceptance shape outside kotoba; none of them is claimed or edited here.

### 2.2 Governance files citing fleet paths repo-rooted

Scan: backticked spans starting `.ufo/` or `../` in each sibling lane's `LOG.md`/`SCORECARD.md`;
class = the path exists at the fleet root `/home/vgpnk/Projects/shokunin` but **not** at the lane
root. Receipt: `ConnectorOverlapR99/sibling-repo-rooted-citations.txt` (one line per citation).

- **247 citations in 20 of 20 sibling lanes; 140 unique tokens.** Top tokens:
  `.ufo/l0-questions.md` 74 (61 bare + 8 `:145` + 3 `:165` + 2 `:233`), `.ufo/watchdog.log` 12,
  `.ufo/state/` 6, `.ufo/waves/kaika/steer.md` 5.
- Only 7 of 20 lanes ever use the `../.ufo/` hop the kotoba convention requires, and sparsely
  (1–2 spans each: kagi, kake, kama, kasegi, kengaku, souji, tsukuroi).
- Exact examples: `kama-shokunin/LOG.md:89` (`.ufo/l0-questions.md`),
  `kagi-shokunin/LOG.md:1770` (`.ufo/watchdog.log`),
  `audio-shokunin/SCORECARD.md:1079` (`.ufo/reports/round-101/audio.md`),
  `game-dev-3d-shokunin/SCORECARD.md:394` (`.ufo/reports/round-108/game-dev-3d.md`).
  All four tokens exist at the fleet root and not at the lane root (checked).
- Bound: whether a lane's own convention permits repo-rooted `.ufo/` is per-lane; kotoba's written
  convention is the `../` hop (`verify_skill_checklist.py:393` `CITATION_ROOTS` includes `../`, and
  the round-57/58/59 rows use it). This is a cross-lane finding, not a claim about any sibling's
  gate.

## Part 3 — three candidate round-100 claims (each falsifiable, with a do-nothing control)

### Candidate A (consistency/calibration) — the v7 counter makes g11's refusal reproducible and closes the g16 pristine-export hole (g13's argv leak is the same rule family)

Evidence: `corpus/lessons/round-98-verifier-spotcheck.md:88-89` — two readings of identical bytes at
one revision disagree, so "the v6 g11 refusal is not reproducible: it rests on a `/dev/shm` marker
another process can delete" (routed defect 1, carried to round 100 by `plans/round-99.md`).
`.ufo/waves/round-98/w1/ExecForgeryV6.md` F1/F2 — `g16-work-pristine-ref` and
`g13-ppid-cmdline-ref` both read `R96C1-PREDICATE-MET` under v6 (receipts
`g16-work-pristine-ref.counter-v6.txt`, `g13-ppid-cmdline-ref.counter-v6.txt`); the v6 header's own
disclosed bound names the `/proc/<ppid>/cmdline` channel.

- **Before → after:** at the round-99 landing, two runs of the same g11 world at the same revision
  disagree (refused with the `/dev/shm/.r97-*` marker present, accepted when it is absent), and
  `selftest-kills.py r96c1 <g16-world>` reads `R96C1-PREDICATE-MET` (rc 0). A v7 counter that (i)
  gives every run a private scratch root and sweeps the named out-of-scratch dirs before/after (so
  a verdict that flips on leftover state is refused), (ii) removes the shared pristine tree before
  the child starts (per-run private copy only), and (iii) spawns the child through a launcher whose
  argv carries no REV/REPO, reads `refused 1 of 1` twice on g11 and `refused 1 of 1` on g16/g13,
  while the frozen set stays `forgeries refused 5 of 5; honest held 2 of 2` and
  `r96c1`/`r95c1`/`r97c1` stay MET.
- **Do-nothing control:** v6 at the round-99 landing reads MET on g16/g13 (the two receipts above)
  and disagrees on g11 across the two readings (spotcheck `:88-89`), so the "after" is not
  reachable without the rule change.
- **Bound:** g15 (filesystem scan + reflog) needs a filesystem sandbox or a different uid; it stays
  disclosed, not claimed.

### Candidate B (depth, anti-shrink) — floor the dispatch self-test at its landed count

Evidence: `check_assertion_floors.py:195` and `:257` both carry floor **56**;
`floors-registry.json:49-52` agrees; the observed count at the freeze is **128** (measured, 0.11 s).
Gap 72 assertions: one `rec(...)` arm can be deleted with the guard still green (the r62 F17 class).

- **Before → after:** in a scratch clone at the round-99 landing, delete one `rec(...)` arm from
  `verifiers/verify_dispatch_prompts.py` → `check_assertion_floors.py` prints
  `PASS dispatch_prompts observed=127 floor=56`, exit 0. After raising the floor to the landed count
  in **both** in-file tables (`:195`, `:257`), `verifiers/floors-registry.json:49-52` and the guard
  docstring (`:10`), and admitting the new `check_assertion_floors.py` blob in
  `check_tip_battery.py:134-145`, the same arm-deleted tree prints
  `FAIL dispatch_prompts observed=127 floor=128`, exit 1.
- **Do-nothing control:** the same arm-deleted tree at the round-99 landing reads PASS (exit 0).
- **Ordering:** take the floor **after** C1's arms land (observed 128 → 128+N); the BUMP-IN-STEP
  rule (`floors-registry.json` `$comment`) requires the registry, both tables and the docstring in
  one change, and the battery pin is load-bearing (`FAIL instrument-pin` otherwise).

### Candidate C (consistency) — the comma-anchor gate defect (`strip_token_dressing`)

Evidence: `verifiers/verify_skill_checklist.py:1079-1084` strips `file.md:42` and `file.md:42-45`
but not the comma list; `SCORECARD.md:529` carries
`corpus/lessons/round-80-verifier-spotcheck.md:30,37`, which the gate tests as a path
(ScoutTipReds §2.1 row 7, F5).

- **Before → after:** on a scratch world at the round-99 landing **with the `:30,37` correction row
  removed** (a control world, not the lane), `verify_skill_checklist.py` reads 1 bad
  (`SCORECARD.md:529 … 'corpus/lessons/round-80-verifier-spotcheck.md:30,37' does not resolve`).
  After extending the regex at `:1082` to `^(.+\.\w+):\d+(?:[,-]\d+)*$` and adding one behavioural
  self-test arm (`strip_token_dressing` on the comma form), the same world reads 0 bad, and the
  self-test goes 1864 → 1865+ assertions; the new `verify_skill_checklist.py` blob is admitted in
  `check_tip_battery.py:157-170`.
- **Do-nothing control:** the same correction-row-removed world at the landing reads 1 bad.
- **Bound:** with C2's correction row in place the token is already excused as data, so the live red
  count is not the target — the target is the gate defect, shown by a *new* comma-anchor citation
  (red before, green after) and by the self-test arm.

## One bounded proposal (connector move)

**One pre-flight gate for ExecArmsR99 that fuses the three constraints the two claims put on the new
arms: anchors unique, `--box-proof` unchanged, no subprocess.** The v6.1 counter substitutes literal
anchor text and requires `src.count(anchor) == 1` over the whole file; a new arm that merely *quotes*
one of them in a comment, docstring or fixture string turns the table into `C1-NOT-EVALUATED`
(exit 2), which the plan's kill rule reads as a miss. Measured at the freeze: all 49 anchors match
exactly once, and the shortest are the dangerous ones —

| anchor | table(s) | length | base line |
|---|---|---|---|
| `if note:` | r97c1 t09 | 8 | 344 |
| `live = {}` | **c1 t04 (new)** | 17 | 1583 |
| `stem = stem[:-3]` | p00 (c1/r98c1/r97c1/r96c1) | 16 | 190 |
| `if round_n <= value:` | r96c1 t04 | 20 | 475 |
| `for cid in wanted:` | **c1 t06 (new)** | 22 | 567 |
| `elif rr != round_n:` | **c1 t02 (new)** | 22 | 451 |
| `    if fails:\n        status = "FAIL"` | **c1 t12 AND r97c1 t12** (shared) | 37 | 496, 505 |

The shared t12 anchor is the sharpest: one duplicate breaks **two** tables (c1 and the r97c1
positive control). The move costs three commands in the builder's own clone, after the edit and
before the patch: `selftest-kills.py c1 <candidate> "$D"` must read `C1-PREDICATE-MET`, and
`r98c1`/`r97c1`/`r96c1` must stay MET; plus two invariants already measured here — `--box-proof`
must still read `boxes proven 2` rc 0 (C2's checklist tripwire, §1.3) and the new arms must stay
in-process (`--self-test` is 0.11 s at the freeze; the floors guard has 53.9 s of headroom, §1.5).
Affected axes: depth (C1) protected from a could-not-evaluate; consistency (C2) protected because
the checklist's `--box-proof` leg and the r97c1 positive control are the same instrument. No harm:
no file outside the builder's owned `self_test()` region changes, the floors guard stays green
(floor is a minimum), and the tip battery's guards do not read the dispatch file (§1.1).

## Risks / contradictions stated, not smoothed

- **C1 → C2 tripwire.** C2's checklist green executes C1's `--box-proof` (`:1314`, `:1065`); a C1
  regression there reds C2 while C1's own counter can still read MET. The C1 kill rule pins
  `boxes proven 2` rc 0, and the C2 counter is the independent tripwire.
- **Timing.** The floors guard measured **226.07 s against the 280 s cap** at the freeze under this
  wave's load (53.9 s headroom). C1's arms run inside it; a subprocess-spending arm can turn the
  landing's battery row red with no gate wrong. C2's *predicate* does not read gate exits — only
  `guards 5 of 5` — so this is a landing no-harm risk, not a C2 predicate risk.
- **The L1's own append is in C2's reading.** `governance.citation_resolves` scans every
  `LOG.md`/`SCORECARD.md` line; the horizon only bounds which notice lines excuse. A repo-rooted
  dead `.ufo/...` token in the L1's round-99 entry re-reds C2 at the landing.
- **Baseline ordering.** ExecRedsR99's equal-mode re-record drifts by ScribeCorpusR99's files (+1
  tracked, +1 coverage row, any report/commit citation); the L1 must re-record at integration, as
  `plans/round-99.md` says. The round-81 quote fix moves `commit_total` 73 → 72.
- **Sibling F6 clauses** are read-only evidence; whether any sibling lane's own convention permits
  its repo-rooted `.ufo/` citations is per-lane and not claimed here.
- **Observed lane-side artifact (not this seat's, not touched):** an untracked 366 MB clone at
  `kotoba-shokunin/repo/` (mtime 2026-11-06 10:59, `git -C repo rev-parse HEAD` =
  `b53e209603e7c480cd975ea543e415b66f695438`, clean) sits in the lane root. It is not on any gate's
  read path (`git ls-files`-based checks ignore untracked paths), but the L1's landing cleanliness
  check will see it; the owning seat should remove it before integration.
