# ConnectorOverlapR97 — overlap scan and planning data-walk (round 97, wave r97-w1)

Read-only seat. No repo writes, no patches, no READY file, no gate/counter runs that write the lane.
All measurements are `git show`/`grep`/`python3 -B` reads of the freeze commit
`148395bf42af97436b1b832a97a175515f981939` plus one `--self-test` invocation of the target instrument
(no writes outside `$TMPDIR`; the instrument's own scratch is `tempfile.TemporaryDirectory`, line 689).

Target surface of the round: `verifiers/verify_dispatch_prompts.py` (`self_test()` only) and the
round-97 fixtures. Question 1: does any *no-harm* instrument pin a blob, sha, line or assertion count
of that file or of `verifiers/fixtures/round-9*/`, so that adding arms or fixtures changes its reading?
Question 2: do sibling lanes carry kill counters / mutation harnesses with the g7/g8 shared-run-state
defect? Question 3: three round-98 candidates the round-97 evidence supports.

---

## Part 1 — overlap scan: nothing pins the bytes; one floor and one anchor table do pin behaviour

Measured at the freeze commit (`verifiers/verify_dispatch_prompts.py` sha256
`cf363a5c11a8bc863564aa6dccbe9491aa90f3cbcf37d598a5d68856173a99dd`, identical in the worktree and in
`git show 148395bf:verifiers/verify_dispatch_prompts.py`).

| Instrument | Exact lines | What it pins | Reading after new self-test arms |
|---|---|---|---|
| `verifiers/check_assertion_floors.py` | `:185` `EXPECTED_INSTRUMENTS = {` / `:195` `"dispatch_prompts": 56`; `:257-258` `INSTRUMENTS["dispatch_prompts"] = ("verifiers/verify_dispatch_prompts.py", 56, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)`; `:682` `match = re.search(pattern, proc.stdout)`; `:685` `ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0` | a **floor** (minimum), not an exact count; the summary regex; `failures == 0`; `rc == 0` | **UNCHANGED PASS.** Measured honest count at the freeze commit: `0 failure(s) over 78 assertions` (rc 0) — 78 ≥ 56. Adding arms only raises 78. |
| `verifiers/floors-registry.json` | `:49-52` `"dispatch_prompts": {"floor": 56, "path": "verifiers/verify_dispatch_prompts.py"}`; `:3` `"instrument_total": 19` | the out-of-file anchor for the two in-file tables; entry count | **UNCHANGED.** No row added or removed; the floor is not moved by adding assertions. |
| `verifiers/check_tip_battery.py` | `:178-185` `BATTERY` = six scripts (`check_gate_registry`, `check_assertion_floors`, `verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`, `check_correction_sweep`); `:114` `LINE_CAP = 900`; `:132-174` `INSTRUMENT_PINS` | line-cap and blob pins apply **only to those six** | **UNCHANGED.** `verify_dispatch_prompts.py` is in neither the battery nor `INSTRUMENT_PINS` → no line cap, no blob pin on it. |
| `verifiers/check_gate_registry.py` | `:17-18` universe = blobs **directly** under `verifiers/` ending `.py`/`.sh`, no recursion, `fixtures/` never counts; `:118-121` `git ls-tree -z <rev> verifiers/` | registry-row conformance for each top-level verifier | **UNCHANGED** for new files under `verifiers/fixtures/round-97/`. A **new top-level** `verifiers/*.py` would grow the universe and read `74 of 75` → keep self-test-only helpers inside `verify_dispatch_prompts.py` (as the ownership line already requires). |
| `SKILL.md` § Gate registry | `:491` `| verifiers/verify_dispatch_prompts.py | gate | python3 -B verifiers/verify_dispatch_prompts.py | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | verifiers/checklist-baseline.json, verifiers/fixtures/dispatch-prompts/manifest.json | self-test tree under $TMPDIR | kotoba |` | kind/entry/verdict map/self-test flag/pinned values/write scope/owner — **no assertion count** | **UNCHANGED.** `--self-test` stays an exact `add_argument` handler; nothing to edit. |
| `verifiers/fixtures/mutation-battery/manifest.tsv` | 24 lines = header + 23 rows; targets `check_freeze_gate.py` (11), `check_r86_routed_repairs_v3.py` (9), `check_mutation_battery.py` (3) | mutant anchors for those three files only | **UNCHANGED.** No row names `verify_dispatch_prompts.py`, so no anchor of this manifest can be duplicated or broken by new arms. |
| `verifiers/checklist-baseline.json` | `:196` `dispatch.04 → "delegated:verifiers/verify_dispatch_prompts.py"`; `:220` `dispatch.08 → same` | the delegation target must exist and be an instrument | **UNCHANGED** by `self_test()` edits. But `verify_skill_checklist.py:319` `BOX_PROOF_FLAG = "--box-proof"` and `:1048-1071` (inside `delegated_box_proof`, `:1031`) run the delegated instrument's `--box-proof`; that path is `box_proof()` (`:1113`), outside `self_test()` — the plan's no-harm battery already reads `boxes proven 2`. |
| `verifiers/check_substrate_pins.py` | `:78-81` `EXPECTED_PINS` = `omp_binary_sha256`, `omp_binary_mtime`, `opencode_binary_sha256` | substrate binaries only | **UNCHANGED.** No verifier-tree pin. |

**Fixtures tree.** No instrument enumerates `verifiers/fixtures/` (grep over `verifiers/*.py` for
`verifiers/fixtures` returns only explicit per-instrument paths: `box_proof_case_deletion.py:287`,
`check_callee_rename.py:66`, `check_freeze_gate.py:15-17`, `check_mutation_battery.py:55`,
`check_omp_catalogue_repro.py:16`, `verify_harness_independent.py:141`). **No blob, sha256, line count
or assertion count of `verifiers/fixtures/round-9*/` is pinned anywhere**, so the round-97 fixtures and
any future round-98 fixtures are inert for the no-harm battery. `verifiers/fixtures/dispatch-prompts/
manifest.json` carries a case table (`cases[].dir/file/check/expect_verdict/expect_conjunct`), **no
sha256 pins** — it is not affected unless cases are added (which would move `boxes proven 2`).

### 1.7 The one instrument that *does* pin the target file: the frozen anchor tables

The pin on `verifiers/verify_dispatch_prompts.py` is not a blob pin — it is the **literal anchor text**
in `CLAIMS["c1"]` (13 targets) and `CLAIMS["r96c1"]` (11 targets) of
`verifiers/fixtures/round-97/selftest-kills.py`, each applied with an expected occurrence count. Measured
against the freeze bytes, **every anchor matches exactly once** (24 of 24, plus the shared positive
`stem = stem[:-3]`):

```
c1  t01 'stem = m.group(2).rstrip(".,;:")'                    1   (line 186)
    t02 'return "none", None, "empty %s" % base'               1
    t03 '"status": "N/A",\n                "detail": "out of scope: fleet-root role'  1
    t04 '(state_dir / ("%s.report-baseline" % lane)).is_file():'  1
    t05 'PLACEHOLDER_RE = re.compile(r"<[^<>]*>")'             1   (line 145)
    t06 'if (fleet / ("%s-shokunin" % lane)).is_dir():'        1
    t07 'REPORT_PATH_RE = re.compile(r"\.ufo/reports/round-(\d+)/'  1  (line 142)
    t08 'ROLE_ROUND_RE = re.compile(r"\bround\s+(\d+)\b")'     1   (line 144)
    t09 'if note:'                                             1   (line 344)
    t10 'return "none", None, "unreadable %s (%s)" % (base, exc.strerror or exc)'  1
    t11 '(state_dir / ("%s.round" % lane)).is_file()'          1   (line 219)
    t12 '    if fails:\n        status = "FAIL"'               1   (lines 496-497; a bare `    if fails:` also exists at 505, the two-line anchor does not)
    t13 '"status": "N/A", "detail": "no report path found in the file"}'  1
    p00 'stem = stem[:-3]'                                     1   (line 190)
r96c1 t01..t11 (var-dropped, var-brace-only, var-bare-only, le-to-lt, finish-allna-pass,
    role-whole-text, dirs-subset, bad-first-only, wrong-first-only, nonint-baseline,
    noreport-04-pass)                                          1 each
```

**Consequence (the C1 builder's hard constraint, now measured rather than asserted):** a second
occurrence of any of these 24 strings anywhere in the file makes the counter's apply step fail →
`selftest-kills.py` exits 2 (could-not-evaluate) → C1 reads `C1-NOT-EVALUATED`, and the no-harm
`r96c1` positive control breaks at the same time. Highest-risk strings for new self-test code, because
they are ordinary Python: **`if note:`** (t09), **`    if fails:` + `        status = "FAIL"`** (t12),
**`stem = stem[:-3]`** (p00), **`if round_n <= value:`** (r96c1 t04), **`elif dirs != [round_n]:`**
(r96c1 t07), **`bad = [(r, s) for r, s in paths if`** (r96c1 t08). New arms should use different local
names (`note_text`, `failures_here`, `stripped`, `round_value`, `dir_list`, `bad_rows`).

### 1.8 Hazards the no-harm battery does *not* catch (name them; do not fix them here)

- **H1 — floor slack 22.** `check_assertion_floors.py:195,257` and `floors-registry.json:50` all say
  **56**; the honest count at the freeze commit is **78**. `:685` compares `assertions >= floor`, so a
  patch that deletes up to 22 existing `rec(...)` assertions still reads `PASS dispatch_prompts
  observed=56 floor=56`. This is the r62-F17 class the floor exists to stop, currently open by 22
  assertions — and C1 widens the gap. (Round-98 candidate A below.)
- **H2 — first-match summary parse.** `check_assertion_floors.py:682` uses `re.search` (first match)
  with `(?m)^(\d+) failure\(s\) over (\d+) assertions$`. A new arm that prints a nested instrument's
  summary line at column 0 *before* the final summary makes the guard read the nested number (usually
  `0` → `observed=0 floor=56` → FAIL, or a wrong count). New arms must not emit that line shape.
- **H3 — repo-dirtying arms.** The floors guard runs the self-test with `cwd=repo` and no `TMPDIR`
  override (`:673-675`); v5 rule 4 gives the *counter* a fresh clone, so a self-test arm that writes
  inside the repository would be invisible to C1 but would dirty the tree under the floors guard and
  the tip battery. Keep every new fixture under `tempfile.TemporaryDirectory` (the existing pattern,
  line 689).
- **H4 — box-proof coupling.** `verify_skill_checklist.py:1048-1071` runs the delegated instrument's
  `--box-proof`; `self_test()` edits are inert there, but any change that reaches `box_proof()`
  (`:1113`) or the manifest case table moves `boxes proven 2` and reds the checklist gate.

**Part 1 answer: no no-harm instrument pins a blob, sha, line or assertion count of
`verifiers/verify_dispatch_prompts.py` or of `verifiers/fixtures/round-9*/`. The bindings that exist are
(a) a *minimum* assertion floor of 56 against a current 78, (b) the 24 frozen anchor strings, each
required to occur exactly once, and (c) the `--box-proof` exit status via the checklist delegation. None
of the three changes its reading when arms are *added*; (b) changes to could-not-evaluate if an anchor
text is duplicated, and (a) is currently too loose to notice arm deletion.**

### 1.9 The scribe's three files: what the corpus instruments actually bind

The scribe owns `corpus/SOURCES.md` (append S273), `corpus/lessons/round-97.md` (new) and one
`corpus/README.md` index row. Measured couplings:

- `verifiers/verify_corpus_integrity.py` (in the tip battery, `check_tip_battery.py:182`) reads
  `git ls-files corpus/` (`:746` `"tracked_files": len(tracked)`), the FILE column of
  `corpus/README.md`, every `commit `<hex>`` citation and every report pointer. Its baseline is
  `verifiers/corpus-baseline.json` (`:134` `BASELINE_NAME`, `:1595` default path) which pins
  `corpus.index.tracked_files: expect 172`, `corpus.pointers.report_total: 127`,
  `corpus.pointers.commit_total: 59`.
- **That gate is already red at the freeze commit** (one of the plan's three carried red gates):
  `python3 -B verifiers/verify_corpus_integrity.py` → `4/9 checks pass; DRIFT: …`, rc **1**:
  `tracked_files observed=199 expected=172`, `unindexed observed=6 expected=0`,
  `report_total observed=161 expected=127`, `commit_total observed=68 expected=59`,
  `commit_unresolvable observed=1 expected=0`. The baseline was recorded at the round-74 start
  (`as_of 2026-11-04`, head `e03f9e2`) and is stale by 27 files.
- Consequence for the scribe: the new lesson adds 1 to `tracked_files` (199→200) and 1 to
  `unindexed` (6→7) **unless** the `corpus/README.md` FILE-column row matches it exactly (the plan's
  "one index row" is exactly what holds `unindexed` still); any `commit `<hex>`` or
  `.ufo/reports/round-97/…` citation in the lesson adds to `commit_total`/`report_total`. All four
  readings are already DRIFT, so the patch does not *newly* red the gate — but nothing in the round
  re-records `verifiers/corpus-baseline.json`, and no seat owns it.
- `verifiers/check_correction_sweep.py` (tip battery `:184`) uses a fixed registry of
  (file, stale, declared) rows; `corpus/SOURCES.md` appears in **no** row, so the S273 append is inert
  there, and the new lesson is not in the registry.
- `verifiers/check_overlap_levers.py` (floor 51) reads `corpus/SOURCES.md` but only the seven pinned
  client rows and their ids; an unrelated `S273` row is inert unless the id duplicates an existing one
  (measured: `grep -n "S273" corpus/SOURCES.md` → no match; last row is `S272` at `:213`).

---

## Part 2 — sibling lanes: the g7/g8 class is present, and not in `verifiers/`

Census first: **only `kotoba-shokunin` has a `verifiers/` tree.** `ls -d */verifiers` over the 21 lanes
returns exactly `kotoba-shokunin/verifiers`; the other 20 lanes carry 0 Python files there, so their
kill counters and mutation harnesses live in `.ufo/waves/**` and `reports/**`. Three instances of the
shared-run-state pattern, strongest first.

### 2.1 tsukuroi — one sandbox for every mutant, honest baseline once, `git clean` without `-x`

`tsukuroi-shokunin/.ufo/waves/round-26/w1/MutSelfAssessPlan/run-mutants.py`

- `:444-449` one `scratch` and **one** `sandbox` (`sandbox = os.path.join(scratch, "sandbox")`,
  `rmtree` + `makedirs` once, outside the loop);
- `:470` `baseline = run_detector(sandbox)` — the honest run happens **once, first**;
- `:489` `for mutant in mutants:` — every mutant mutates and is measured in that **same** sandbox;
- `:576-578` `restore()` = `git reset -q --hard <base>` + **`git clean -qfd`** — note the missing `-x`:
  **gitignored files survive the restore**, so a detector that writes a marker into an ignored path
  inside the sandbox carries state from mutant *n* to mutant *n+1*;
- `:369-371` `run_detector` spawns with `cwd=sandbox` and **inherited env** — no per-run `TMPDIR`,
  `HOME` or `XDG_CACHE_HOME`, no per-run clone, no post-target honest bracket, no mirror run.

This is the g7/g8 class in full: a stateful detector that fails only after the first (honest) run reads
`killed` for every mutant, and nothing in the harness can see it.

### 2.2 revenger — one work root for 12 vectors × 2 profiles × 4 stub runs, and a fail-open harness

`revenger-shokunin/reports/round-100/forge_reach9.py`

- `:283-284` `root = work / "forge9"` then **one** `shutil.rmtree(root)` before the loop; every main
  run and every stub self-test run lives under it;
- `:126-131` each builder run gets a fresh `run_dir` with `TMPDIR`/`HYAKU_SCRATCH` pointed inside it
  (`:123` rmtree per run) — good — but **`HOME` and `XDG_CACHE_HOME` are inherited** from the parent,
  and the **lane is the same** for every run, so state in `$HOME`, `/dev/shm` or the lane's object store
  survives all 12 vectors;
- `:293-294` the main runs happen before the stub self-tests at `:310-312`, all in the same root and
  against the same lane; the honest control is the *first* entry of the builder's own table
  (`revenger-shokunin/.ufo/waves/round-99/w1/CriticR99/fresh/build_fresh99.py:403-415`, where the
  honest tree is built first and `("CONTROL-honest", …)` is prepended to `entries`) — exactly the
  "honest run only first" ordering.

Adjacent, disclosed by that lane itself: `revenger-shokunin/.ufo/waves/round-100/w1/CriticR100.md:70-80`
(A1) — the harness decides `ACCEPTED` from the first `C1_VERDICT=` stdout line and **never reads the
exit code**, so a wrapper that always exits 0 is counted as refused. Different defect (fail-open
classification, not shared state), same family as the round-96 g3 recompile-compare world.

### 2.3 mado — repo isolated per mutant, environment not

`mado-shokunin/.ufo/waves/round-18/measure-mutants.py`

- `:541` one `mkdtemp` root; `:548-549` per-mutant `mroot` with `prepare_repo(lane, mroot)`, and
  `:436-448` `prepare_repo` builds a **fresh `git archive` + `git init` repo per mutant** — the repo
  side is properly isolated;
- `:344-349` `run_instrument` uses `subprocess.run(cmd, cwd=repo)` with **inherited env** — no
  `TMPDIR`/`HOME`/`XDG_CACHE_HOME` isolation;
- baseline-then-mutant per mutant, **no final honest bracket**.

Weakest of the three (per-mutant repo defeats the clone-marker variant g8), but a `$HOME`/`/dev/shm`
marker still survives every mutant and the honest baseline is never re-read.

### 2.4 Negative results (stated so the census is honest)

`kumitate-shokunin/.ufo/waves/round-51/build/MutInstrument/counter-probe.sh:22-24` does `rm -rf "$WORK"`
and rebuilds a fresh lane per probe (one probe per invocation) — not a multi-run harness.
`mado-shokunin/.ufo/waves/round-26/quality/counter-selftest.py:283` creates one `run_dir` per
invocation with a fake `tempfile` module (`:176-183`) — single-run, not a kill harness.
`audio`, `chousa`, `kagi`, `kengaku`, `kotodama`, `lore`, `souji`, `tabi`, `tameshi` show kill/mutant
files only as per-round artefacts, not as reusable harnesses.

**Cross-lane finding (for the report, not a write):** the g7/g8 class is **not** a kotoba-only defect.
Three sibling lanes run kill/mutation harnesses with (i) one sandbox or work root for every run,
(ii) the honest run only first, (iii) inherited `HOME`/`XDG_CACHE_HOME` and a shared lane, and in
tsukuroi's case (iv) a restore that leaves gitignored files in place (`git clean -qfd`, no `-x`). The
round-97 v5 rules 4-6 are a transferable fix; the tsukuroi `-x` variant is *not* covered by rules 4-6
either, because the marker lives inside the repo copy, not outside the per-run directories.

---

## Part 3 — three candidate round-98 claims (falsifiable before→after, each with a do-nothing control)

### A. Floor the dispatch-prompt self-test at its landed count (closes H1)

- **Surface:** `verifiers/check_assertion_floors.py:195,257`, `verifiers/floors-registry.json:50`, the
  guard docstring, and the admitted blob list `verifiers/check_tip_battery.py:132-174` (BUMP-IN-STEP:
  one change, four places).
- **Before (measured, this round):** honest `--self-test` = `0 failure(s) over 78 assertions`; floor 56;
  a mutant that deletes 22 `rec(...)` calls still reads `PASS dispatch_prompts observed=56 floor=56`
  (`:685` compares `>=`).
- **After:** floor = the landed count (78 + the C1 arms); the same deletion mutant reads
  `FAIL dispatch_prompts observed=… floor=…`, rc 1.
- **Do-nothing control:** the unmodified instrument at the landed revision reads `PASS … observed=N
  floor=N` (equality, not slack). Second control: a mutant that *adds* an arm still reads PASS (the
  floor is a minimum, so the fix cannot be satisfied by inflation alone).
- **Falsifier:** if the deletion mutant still reads PASS after the bump, the claim is unmet.
- **Why round-98 and not a seat edit:** the blob is pinned in `check_tip_battery.py:132-174` and the
  floor is cross-checked in two in-file tables plus the registry — a seat edit would red the tip
  battery; it needs a planned, reviewed postimage.

### B. Refuse the disclosed g2b bound (guard-aware code-object sniffer)

- **Surface:** the v5→v6 counter rules (`verifiers/fixtures/round-98/selftest-kills.py`), scored by
  `forgery-controls.py` with the committed g2b world.
- **Before (measured, frozen):** `forgery-controls.py v5` prints `bound g2b MET` — the counter accepts a
  forgery that sniffs its own compiled code objects and proves the decoy guard dead (counter docstring
  `Disclosed bounds`, line 41; plan § Disclosed bounds).
- **After:** `C2 v6: forgeries refused 3 of 3; honest held 2 of 2; bound g2b refused` with rc 0.
- **Do-nothing control:** `forgery-controls.py v6-as-v5` reads `bound g2b MET` (the cause control that
  shows the refusal comes from the new rule, not from a table or path change) — the same shape as this
  round's `c2-v5-as-v4.txt`.
- **Falsifier:** g2b still MET under v6, or either honest world (h1 `801dd9bc`, h2 `<rev>`) stops being
  held.

### C. Refuse state kept outside the per-run directories (the v5 rule-4/6 residual)

- **Surface:** v6 rule 8 — a post-target honest run plus a per-run clone of the *lane* (not only of the
  counter's repo), scored by a committed control world `g9-shm-marker` (marker in `/dev/shm` or the
  source repo's object store) next to g3/g7/g8.
- **Before ([INFERENCE], not measured this round):** the v5 docstring states the bound explicitly —
  "state kept outside the per-run directories (for example /dev/shm, /var/tmp or the source
  repository's object store) survives isolation, and only the honest bracket (rule 6) stands against
  it" — and rule 6 brackets only the *unmodified* self-test, so a forger that fakes failure after the
  first honest run is not caught. The wave's v5 forgery-attack seat is the cheap falsifier of this
  sentence; if it reports g9 MET, the before is confirmed and the claim is grounded.
- **After:** `forgeries refused 4 of 4; honest held 2 of 2` with `g9` refused and `g2b` unchanged.
- **Do-nothing control:** `v6-as-v5` on g9 reads MET (cause control); h1/h2 stay held under v6 (no
  over-refusal).
- **Falsifier:** g9 still MET under v6, or an honest world is refused.
- **Cross-lane transfer:** the same rule would catch tsukuroi's `git clean -qfd` residue only if the
  clone is rebuilt per run — worth stating as a bound, not claiming.

---

## Contradictions and risks (stated, not scored)

1. **The floor is a minimum but is documented as if it were a count.** `check_assertion_floors.py`
   docstring calls it "the recorded floor"; `:685` is `>=`. Both are true, but the 22-assertion slack
   means the guard's stated purpose (catch a dropped arm) is only 71% effective for this instrument
   (56/78). Not a defect in this round's claim; a disclosed weakness that C1 widens.
2. **C1's kill rule and the no-harm battery share one anchor table.** `selftest-kills.py r96c1` is both
   the C1 positive control and a no-harm reading; a duplicated anchor breaks both at once. The plan
   treats them as separable, and they are separable *in cause* but not *in failure mode*.
3. **Part 2's instances are not the same defect.** tsukuroi's ignored-file residue survives even a
   per-run clone of the *counter's* repo; revenger's is `HOME`/`XDG` inheritance plus honest-first
   ordering; mado's is environment only. Calling all three "g7/g8" would smooth a real difference —
   only tsukuroi's variant needs a rule beyond v5 rules 4-6.
4. **No sibling lane can be measured from here.** Their harnesses are historical artefacts at their own
   revisions; the file:line readings above are of the committed text, not of a re-run. I did not run
   them (read-only seat, and they would write their own scratch).
5. **"No-harm" is not "green" for the corpus row.** `verify_corpus_integrity.py` is already rc 1 at the
   freeze commit (five DRIFTs against a round-74 baseline, §1.9) and is a tip-battery member. The
   scribe's new lesson moves four of those numbers by one each; the honest reading of the landing is
   "no worse than base", and `verifiers/corpus-baseline.json` (unowned by any seat this round) is the
   file that would make it green. Saying the tip battery "passes at landing" without that qualifier
   would be false.

## Evidence (commands and the observed lines)

```
$ git show 148395bf:verifiers/verify_dispatch_prompts.py | sha256sum
cf363a5c11a8bc863564aa6dccbe9491aa90f3cbcf37d598a5d68856173a99dd  -
$ sha256sum verifiers/verify_dispatch_prompts.py
cf363a5c11a8bc863564aa6dccbe9491aa90f3cbcf37d598a5d68856173a99dd  verifiers/verify_dispatch_prompts.py
$ python3 -B verifiers/verify_dispatch_prompts.py --self-test | tail -1
0 failure(s) over 78 assertions                     (rc 0)
$ grep -n 'dispatch_prompts' verifiers/check_assertion_floors.py verifiers/floors-registry.json
check_assertion_floors.py:195:    "dispatch_prompts": 56,
check_assertion_floors.py:257:    "dispatch_prompts": ("verifiers/verify_dispatch_prompts.py", 56,
floors-registry.json:49:    "dispatch_prompts": {
floors-registry.json:50:      "floor": 56,
floors-registry.json:51:      "path": "verifiers/verify_dispatch_prompts.py"
$ sed -n '682p;685p' verifiers/check_assertion_floors.py
        match = re.search(pattern, proc.stdout)
        ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0
$ sed -n '178,185p' verifiers/check_tip_battery.py     # BATTERY: six scripts, target absent
$ sed -n '132,174p' verifiers/check_tip_battery.py     # INSTRUMENT_PINS: seven paths, target absent
$ awk -F'\t' 'NR>1{print $2}' verifiers/fixtures/mutation-battery/manifest.tsv | sort | uniq -c
     11 verifiers/check_freeze_gate.py
      3 verifiers/check_mutation_battery.py
      9 verifiers/check_r86_routed_repairs_v3.py
$ ls -d /home/vgpnk/Projects/shokunin/*/verifiers
/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers      # 20 sibling lanes: none
$ python3 -B verifiers/verify_corpus_integrity.py; echo rc=$?
corpus.index    tracked=199 unindexed=6 stale=0 missing=0  (211 FILE-column patterns over 198 md files)
corpus.pointers report_dead=0/161 commit_total=68 unresolvable=1 nonhash=0
DRIFT   corpus.index.tracked_files: observed=199 expected=172
DRIFT   corpus.index.unindexed: observed=6 expected=0 / empty
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed,
        corpus.pointers.report_total, corpus.pointers.commit_total,
        corpus.pointers.commit_unresolvable
rc=1
$ grep -n "S273" corpus/SOURCES.md          # no match; last row S272 at :213
# anchor census (import of the frozen counter, read-only; every row printed want=1 got=1)
c1 13 targets + positive, r96c1 11 targets + positive → 24 anchors, all count == 1
```

Scratch: `/fast/scratch/hyaku/kotoba-r97/ConnectorOverlapR97` (removed before yield). No tool installs.
