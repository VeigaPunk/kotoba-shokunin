# ConnectorOverlapR98 — overlap scan and planning data-walk (round 98, w1)

Read-only seat. No repo writes; every measurement below is a read at the lane base
`a33f262fc94e3cf27f3c935b5c53c1336bb94166` unless a revision is named. Scratch:
`/fast/scratch/hyaku/kotoba-r98/ConnectorOverlapR98` (removed before yield).

## Part 1 — does any no-harm instrument pin the dispatch checker or the round-9* fixtures?

Answer: **no blob, no sha, no line count, no exact assertion count.** The only coupling is a
*minimum* assertion floor (56) and a *lower-bound-only* floors guard. Two adjacent couplings are
real and are named in §1.3–1.4 (the counter's own anchor strings and the corpus counts).

### 1.1 `verifiers/verify_dispatch_prompts.py` — nothing pins its bytes

| instrument | exact lines | what it pins | effect of adding self-test arms |
|---|---|---|---|
| `verifiers/check_tip_battery.py` | `INSTRUMENT_PINS` lines 132–176 | seven blob-pin rows: `check_gate_registry.py` (133), `check_assertion_floors.py` (134–145), `check_freeze_gate.py` (150–156), `verify_skill_checklist.py` (157–170), `verify_corpus_integrity.py` (171–173), `verify_corpus_independent.py` (174–176), `check_correction_sweep.py` (177). **No `verify_dispatch_prompts.py` row.** | none |
| same | `BATTERY` lines 178–185 | six scripts; `verify_dispatch_prompts.py` is **not** one of them | none |
| same | `run_guards()` line 325 (`scripts = [path for path, _ in BATTERY]`) and the `git diff --numstat … -- *scripts` that follows | `instrument-size` diffs only the six battery scripts | none |
| same | `no-deletions` guard lines 288–297 | fails only when a base path under `corpus/`, `verifiers/` or `SKILL.md` is **absent** at `<rev>` | additions pass |
| same | `spotcheck-identity` guard, `SPOTCHECK_DIR`/`SPOTCHECK_RE` lines 118–119 | only `corpus/lessons/*-verifier-spotcheck.md` present at the base; a file added at `<rev>` is INFO | `corpus/lessons/round-98.md` does not match the regex → INFO at most |
| `verifiers/check_assertion_floors.py` | line 257–258: `"dispatch_prompts": ("verifiers/verify_dispatch_prompts.py", 56, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)`; comparison line 685: `ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0` | floor **56**, a minimum | 105 → 105+N still passes |
| `verifiers/floors-registry.json` | lines 51–53: `"dispatch_prompts": {"floor": 56, "path": "verifiers/verify_dispatch_prompts.py"}` | floor + path only; **no sha256 field anywhere in the registry** | none |
| `verifiers/check_tip_battery.py` | `floors` guard lines 299–323 | fails only when `new < old` for a base row | none |
| `verifiers/check_gate_registry.py` | `judge_row()` lines 178–223: self-test flags need an exact `add_argument` handler (206–208); pinned-value paths must exist (217–219) | the `SKILL.md:491` row's `--self-test`/`--box-proof` handlers and the two named paths | handlers and paths stay; 74 of 74 unchanged |
| `verifiers/checklist-baseline.json` | `dispatch.04` lines 193–197 (`text_sha256` 195, `disposition` 196), `dispatch.08` lines 217–221 (`text_sha256` 219, `disposition` 220); `box_total` 45 (`boxes` 45) | the SKILL.md box text hashes + delegation dispositions; `box_total` is a box count, not an assertion count; read by `--box-proof` | `self_test()` edits do not touch SKILL.md or the map |

One indirect coupling to state: the tip battery's `verify_skill_checklist.py` child **executes**
the dispatch instrument's `--box-proof --map <map>` and requires exit 0
(`verifiers/verify_skill_checklist.py:68-72` docstring, `delegated_box_proof()` lines 1033-1072).
`self_test()` edits do not change `--box-proof`; any accidental production change would, which is
why the landing's `prod-identity` receipt (`landing-run.sh`) diffs the file outside `self_test()`.

Measured at the lane base (commands run from the lane root, `TMPDIR` in seat scratch):

```
$ python3 -B verifiers/verify_dispatch_prompts.py --self-test
0 failure(s) over 105 assertions            # real 0.063 s
$ python3 -B verifiers/check_assertion_floors.py --self-test
0 failure(s) over 176 assertions
$ python3 -B verifiers/check_gate_registry.py --rev a33f262f…
gate registry rows conformant 74 of 74 lane verifiers; phantom 0   # rc 0
```

So the floor (56) sits **49 assertions below** the current count (105) — the carried round-97
routed defect 5 ("floor 56 vs 105"), which this round does not claim. Adding arms cannot red any
of these instruments; it only widens the floor gap.

### 1.2 `verifiers/fixtures/round-9*/` — nothing pins the directory

`grep -rn "fixtures/round-9" verifiers/*.py` returns exactly one hit, a comment at
`verifiers/verify_dispatch_prompts.py:1105`. No no-harm instrument enumerates `verifiers/fixtures/round-9*`
or any fixtures directory; the only fixtures path any of them reaches is
`verifiers/fixtures/dispatch-prompts/manifest.json`, through the dispatch instrument's `--box-proof`.
The committed round-98 counter/runner and any future round-99 fixtures are therefore invisible to the
tip battery, the floors guard, the gate registry and the corpus gates. `verifiers/fixtures/dispatch-prompts/`
(the box-proof corpus) is untouched by round 98 (the plan forbids editing it).

### 1.3 The real coupling this round does have: the counter's own anchor strings

The v6 counter substitutes **literal anchor text** in `verifiers/verify_dispatch_prompts.py` and
requires each to match **exactly once** (`src.count(anchor)`). I re-derived all 34 anchors (9 c1
targets + 13 r97c1 + 11 r96c1 + p00) against the base file: **every one matches exactly once, and
none lies inside `self_test()` (span 679–1342; `box_proof()` starts at 1343, file 1560 lines).**
They are all production strings.

The non-obvious risk is that the count is a **substring** count: a new self-test comment, docstring
or fixture string that merely *quotes* an anchor turns the table into could-not-evaluate
(`C1-NOT-EVALUATED`, exit 2), which the plan's kill rule treats as a miss. The shortest anchors are
the dangerous ones (a builder is likely to write them naturally):

| anchor (shortest first) | table / arm | base line |
|---|---|---|
| `if note:` | r97c1 t09-file-note-dropped | 344 |
| `stem = stem[:-3]` | c1 positive p00-md-not-stripped | 190 |
| `if round_n <= value:` | r96c1 t04-le-to-lt | 475 |
| `elif dirs != [round_n]:` | r96c1 t07-dirs-subset | 464 |
| `    if legacy.is_file():` | c1 t07-legacy-exists | 247 |
| `    for f in result["files"]:` | c1 t03-verdict-first-file | 607 |
| `        if stem.endswith(".md"):` | c1 t09-md-uppercase | 189 |
| `stem = m.group(2).rstrip(".,;:")` | r97c1 t01-rstrip-dot | 186 |
| `verdicts[cid] = {"status": "N/A",` | r96c1 t11-noreport-04-pass | 366 |
| `m = ROLE_ROUND_RE.search(lines[0])` | r96c1 t06-role-whole-text | 200 |
| `bad = [(r, s) for r, s in paths if` | r96c1 t08-bad-first-only | 371 |
| `        if live.get(cid) != pinned:` | c1 t05-proof-live-hash-unenf | 1426 |
| `dirs = sorted({r for r, _s in paths})` | c1 t02-dirs-first-only | 460 |
| `    if fails:` (two-line anchor with `status = "FAIL"`) | r97c1 t12-finish-single-fail-na | 496, 505 |

The two-line t08 anchor (`"""The dispatch.04 box over the prompts directory."""` +
`names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())`, line 350) is the longest and
the least likely to be duplicated; the eight-character `if note:` is the most likely.

### 1.4 Adjacent second-order coupling: the corpus counts (ScribeCorpusR98's files)

`verifiers/verify_corpus_integrity.py` equal-pins three counts against
`verifiers/corpus-baseline.json` (docstring lines 6, 16, 23; `CHECKS` lines 806–814). At the base:

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=201 unindexed=7 stale=0 missing=0
corpus.pointers report_dead=0/165 commit_total=71 unresolvable=1 …
DRIFT corpus.index.tracked_files: observed=201 expected=172
DRIFT corpus.index.unindexed: observed=7 expected=0 / empty
DRIFT corpus.pointers.report_total: observed=165 expected=127
DRIFT corpus.pointers.commit_total: observed=71 expected=59
DRIFT corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty
4/9 checks pass; rc=1
```

`corpus/lessons/round-98.md` (new) grows `tracked_files` by 1 and, if it cites a lane report or a
backticked commit, `report_total`/`commit_total` too. The gate is **already red** (rc 1) and stays
red, so the tip battery's red *set* does not grow — but the DRIFT *values* do. Two bounds to state:

- `verifiers/verify_corpus_independent.py` at the base: `unindexed=7` and
  `commit_unresolvable=1` DRIFT, rc 1. ScribeCorpusR98's one README index row keeps `unindexed` at 7
  (the new lesson is indexed); a SOURCES row written with a backticked `commit \`<hex>\`` would grow
  `commit_total` and risk a new unresolvable token — write upstream pins without the backticked
  commit form (the round-48 note in `corpus-baseline.json`).
- `verifiers/check_r86_routed_repairs_v3.py` D5(iii) requires per-name value and detail
  **non-growth** against a base receipt. It is **not** in `.ufo/waves/round-98/landing-run.sh`, so the
  landing does not read it; if anyone runs it at the landing, the corpus growth fails D5(iii). Named
  as a bound, not a claim.

### 1.5 Timing headroom in the no-harm battery — the tightest coupling found

Two readings of the same battery:

- Round-97 landing receipt `.ufo/waves/round-97/receipts/landing/tip-battery.txt`:
  `gate verifiers/check_assertion_floors.py exit 0 wall 190.6s`.
- **This seat at the round-98 base `a33f262f…`, under the current wave's load** (receipt
  `.ufo/waves/round-98/w1/ConnectorOverlapR98/tip-battery-base.txt`):
  `gate verifiers/check_assertion_floors.py exit 0 wall 255.1s`, `wall 259.9s`,
  `guards 5 of 5; tip battery exit 0: 3 of 6` (rc 1; red set = `verify_skill_checklist`,
  `verify_corpus_integrity`, `verify_corpus_independent`).

Against `GATE_TIMEOUT_S = 280` (`check_tip_battery.py:113`) the headroom is **89.4 s at the r97
landing but only 24.9 s under this wave's load** — a 64.5 s load-driven swing. The dispatch
self-test is 0.063 s / 105 assertions and runs in-process, so in-process arms are free; an arm that
shells out (a subprocess `--box-proof`, a git fixture, a sleep) spends the headroom and can turn the
battery's `check_assertion_floors.py` row red — a red-set growth the plan forbids, and one that
would look like a C1 regression while being host load. The landing should run the tip battery on a
quiet host (or read the row's `wall` line, not only its exit) for exactly this reason.

## Part 2 — sibling lanes: the g10/g11 class outside kotoba (read-only)

The class the round-98 v6 rules close (measured child reads a committed reference of itself, or the
parent's environment) is a fleet-wide pattern. Sites, with the measured-child line:

| lane / file:line | what it hands the measured child | class |
|---|---|---|
| `kaidoku-shokunin/.ufo/waves/round-19/postfix-mutations.py:17-19` (`ENV = {k: v for k, v in os.environ.items() if not k.startswith(('GIT_','JJ_'))}`), `:28` `git clone -q --shared LANE repo`, `:32` `git checkout --detach source`, `:40` counter run with `env={**ENV, **(extra_env or {})}` | full parent env (minus GIT_/JJ_) **and** a clone with `.git` history; the counter is `tools/routed-r18.py --root repo --rev rev` | **g10 + g11** |
| `kama-shokunin/.ufo/waves/round-57/measured/R57Item12/mutants.py:18` `ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}`, `:39` `git checkout -q --detach sha`, `:40-42` instrument run `env=ENV` in the scratch clone | full parent env + clone history | **g10 + g11** |
| `kaidoku-shokunin/.ufo/waves/round-40/w1/artifacts/R40MutR39/mutate.py:95` `env=dict(os.environ, TMPDIR=S, HYAKU_SCRATCH=…)`, `:119` mutant run `--root S/clone` | full parent env + clone history | **g10 + g11** |
| `kaidoku-shokunin/.ufo/waves/round-100/w1/MutationC1/src/driver.py:76-86` copies a clone with `.git` and commits the mutant, `:113-114` runs the battery `--root job["clone"] --rev job["rev"]`, `:116` `subprocess.run(cmd, …, cwd=job["run"])` with **no `env=`** | clone history reachable to the measured battery **and** the full parent env inherited — the most recent sibling round in this sample | **g10 + g11** |
| `mado-shokunin/.ufo/waves/round-65/w1/R65MutCounters/evidence/harness/mut_c1.py:47-49` (`git -C repo rev-parse HEAD`, then `subprocess.run([...], capture_output=True, text=True, timeout=120)` with no `env=`) | inherited parent env; fixture repo is a git repo (`rev-parse HEAD`), so history is reachable | **g10 + g11** |
| `revenger-shokunin/.ufo/waves/round-89/w1/ReviewerR89C1/receipts/selftest-attack.py:41` `subprocess.run([...], capture_output=True, text=True)` (no `env=`); the world is labelled "base archive" at `:57` | inherited parent env; no history (archive) | **g11 only** |
| `kasegi-shokunin/.ufo/waves/round-65/signal-mutbat-r65.py:167-171` `subprocess.run([...], cwd=work, stdout=…, timeout=180)` (no `env=`) | inherited parent env | **g11 only** |
| `kotodama-shokunin/reports/round-98/controls/battery98.py:88` `ENV = dict(os.environ, TMPDIR=…)`, `:220` `subprocess.run(cmd, …, env=ENV, cwd=SCRATCH)`; same shape `battery99.py:90,222`; `battery100.py:188` (no `env=`) | full parent env to the measured counter; world is a plain scratch tree (no `.git`) | **g11 only** |
| `kagi-shokunin/.ufo/waves/round-24/tools/identity-swap.py:266` `git clone -q --no-hardlinks LANE pristine`, `:268` checkout rev; `evaluate()` `:218` uses a minimal env (`PATH`/`HOME`/`LANG`) | clone with `.git` history; env is minimal | **g10 only** (history reachable, env clean) |

Contrast (the good pattern): `kotodama-shokunin/reports/round-98/controls/forgery-controls.py:57`
exports each fixture with `git archive` — a plain tree with no `.git`, i.e. the v6 rule-8 shape.

This is a cross-lane finding, not a write: kotoba's v6 is the only lane in this sample that closes
both halves (git-less world **and** minimal child env). The sibling harnesses above would read a
HEAD-comparing or seed-reading forger as MET.

## Part 3 — three candidate round-99 claims the round-98 evidence supports

### Candidate A (depth, anti-shrink) — floor the dispatch self-test at its landed count

Round-98 leaves `dispatch_prompts` at floor 56 while the self-test reports 105 (+N after C1). An arm
can be deleted with every gate green (the r62 F17 class, re-found).

- **Before → after:** in a scratch clone, delete one `rec(...)` arm from
  `verifiers/verify_dispatch_prompts.py`; at the round-98 landing
  `python3 -B verifiers/check_assertion_floors.py` reads `PASS dispatch_prompts observed=104 floor=56`
  (exit 0). After raising the floor to the landed count in **both** in-file tables **and**
  `verifiers/floors-registry.json` (BUMP-IN-STEP rule, registry `$comment`) and admitting the new
  `check_assertion_floors.py` blob in `check_tip_battery.py` `INSTRUMENT_PINS` (lines 134–145), the
  same arm-deleted tree reads `FAIL dispatch_prompts observed=104 floor=105` (exit 1).
- **Do-nothing control:** the same arm-deleted tree at the round-98 landing reads PASS (exit 0).
- **Coupling to state:** `check_assertion_floors.py` is blob-pinned by the tip battery; the edit needs
  an admission row or `guard instrument-pin` reds. `instrument-size` cap 900 lines (line 114) is far
  away. This is the carried round-97 routed defect 5 ("floor 56 vs 105"), now with a measured
  before→after.

### Candidate B (consistency) — heal the corpus red, name the residual

The tip battery's three reds are `verify_skill_checklist` (governance citations), `verify_corpus_integrity`
(5 DRIFT) and `verify_corpus_independent` (2 DRIFT). The corpus half is repairable without touching a
non-author record: index the seven unindexed spot-checks (`corpus/lessons/round-91..97-verifier-spotcheck.md`)
in `corpus/README.md`, add the round-98 lesson row, and re-record the three `equal` counts from
`--no-baseline --json` (an expectation refresh, not a fitted denominator).

- **Before → after:** `python3 -B verifiers/verify_corpus_integrity.py` → before `4/9 checks pass;
  DRIFT: tracked_files, unindexed, report_total, commit_total, commit_unresolvable` (rc 1); after
  `8/9 checks pass; DRIFT: commit_unresolvable` (rc 1, the carried `corpus/lessons/round-81.md:8`
  absent test-world commit, a record the lane may not rewrite). `verify_corpus_independent.py` → 2
  DRIFT → 1. The **tip battery red set stays 3 of 6** (rc 1 either way); the target is the DRIFT
  count, not the red set — state that honestly.
- **Do-nothing control:** at the round-98 landing the same command reads `4/9` with
  `tracked=202` (the round-98 lesson added, baseline not re-recorded).

### Candidate C (consistency/calibration) — v7 rule for out-of-scratch state (the v6 header's own bound)

The v6 header states: "state kept outside the per-run directories (for example /dev/shm, /var/tmp)
survives isolation, and only the honest bracket (rule 6) stands against it." Build a committed
forgery world `g12-shm-marker` (the g7 shape writing its marker to `/dev/shm` instead of `TMPDIR`).

- **Before → after:** `forgery-controls.py v6 <rev>` on the g12 world → the counter reads
  `R96C1-PREDICATE-MET` for it (refused 0 of 1, i.e. the forgery is accepted). A v7 rule (two runs
  with distinct scratch roots plus a pre/post sweep of the named out-of-scratch dirs; a verdict that
  flips is refused) → `refused 1 of 1` while the frozen set stays `forgeries refused 5 of 5; honest
  held 2 of 2`.
- **Do-nothing control:** v6 at the round-98 landing on g12 reads MET (unrefused) — the same
  do-nothing reading the round-97 g10/g11 worlds had under v5.
- **Bound:** the `/proc/<ppid>/cmdline` bound (REV/REPO visible to the child) is not closed by this
  rule; it needs a filesystem sandbox or a different uid and stays disclosed.

## One bounded proposal (connector move)

**Pre-flight the 34 anchor strings before ExecArmsR98 writes READY, and forbid any new self-test
text that contains one of them.** The v6 counter's kill and its r97c1/r96c1 positive controls all
depend on `src.count(anchor) == 1` over the *whole file*, so a new arm that writes `if note:`,
`stem = stem[:-3]`, `if round_n <= value:` or `elif dirs != [round_n]:` in a comment, docstring or
fixture string turns C1 into `C1-NOT-EVALUATED` (exit 2) and the plan's kill rule reads it as unmet —
a silent loss on **depth** that no other seat's check would attribute to the arm text. The move costs
one command in the builder's own scratch clone and protects both axes:

```
# in $D, after the edit, before the patch:
python3 -B verifiers/fixtures/round-98/selftest-kills.py c1 <candidate> "$D"   # must read 9 of 9
python3 -B verifiers/fixtures/round-98/selftest-kills.py r97c1 <candidate> "$D" # must stay MET
python3 -B verifiers/fixtures/round-98/selftest-kills.py r96c1 <candidate> "$D" # must stay MET
```

Affected axes: depth (C1) protected from a could-not-evaluate; consistency (C2) protected because
r97c1/r96c1 are C2's positive controls. No harm: no file outside the builder's owned
`self_test()` region changes, the floors guard stays green (floor is a minimum), and the tip
battery's guards do not read the dispatch file (§1.1) — its only execution of it is the
`--box-proof` leg, which `self_test()` edits do not touch.

## Risks / contradictions stated, not smoothed

- **Timing:** the tip battery's `check_assertion_floors` row read **255.1 s against the 280 s cap**
  at the base under this wave's load (24.9 s headroom; 190.6 s at the r97 landing). A load spike or
  any subprocess-spending arm can turn that row red; the C1 arms must stay in-process, and the
  landing receipt should be read for its `wall` line, not only its exit code.
- The corpus gate is **already red** at the base (5 DRIFT); round-98's lesson grows the values. The
  plan's "red set not larger" is satisfied (script-level rc unchanged), but "no-harm" is not the same
  as "no change": `tracked_files` 201 → 202 and any new report/commit citation move with it.
- `check_r86_routed_repairs_v3.py` D5(iii) would fail on that growth; it is not in the landing
  battery, so this is a bound on any later reading, not a landing failure.
- The v6 counter's floor is 49 assertions below the observed count; C1 will widen the gap. The
  round-98 landing cannot claim anti-shrink for these arms (Candidate A is the round-99 fix).
- The sibling-lane census is a sample of the harnesses that name `mutant`/`kill`; it is not a
  complete fleet census (audio's live probes and other non-counter harnesses were excluded by
  construction).
