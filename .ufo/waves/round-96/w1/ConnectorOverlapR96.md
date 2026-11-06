# ConnectorOverlapR96 — overlap scan and planning data-walk (round 96, w1)

Seat: `ConnectorOverlapR96` (connector, read-only). Scope: no repo writes; receipts and this report only.
Base for every reading: freeze commit `679775abb9277a7b8d17f060b0f5b4ced2b127b6` (lane
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`), read-only.

## Part 1 — does any no-harm instrument pin a blob, sha, line or assertion count of `verifiers/verify_dispatch_prompts.py`?

Answer: **no exact-count pin, no blob pin, no line pin.** One *first-match* parsing hazard, one
minimum-floor dependency, and one prose-only reference. Details, exact lines:

| instrument | what it reads about `verify_dispatch_prompts.py` | exact line | verdict |
|---|---|---|---|
| `verifiers/check_assertion_floors.py` | row `"dispatch_prompts": ("verifiers/verify_dispatch_prompts.py", 56, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)` | `check_assertion_floors.py:257-258` | **minimum**, not exact: `ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0` (`:685`). Adding arms raises `observed`; PASS. |
| `verifiers/floors-registry.json` | `"dispatch_prompts": {"floor": 56, "path": "verifiers/verify_dispatch_prompts.py"}` | `floors-registry.json:49-52` | registry drift only compares path+floor between registry and the two in-file tables (`:488-494`); unchanged floor ⇒ no drift. |
| `verifiers/check_tip_battery.py` | nothing: `BATTERY` is the six scripts `check_gate_registry`, `check_assertion_floors`, `verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`, `check_correction_sweep`; `INSTRUMENT_PINS` has no key for the dispatch instrument; `instrument-size` diffs only `[path for path, _ in BATTERY]` | `check_tip_battery.py:176-183` (BATTERY), `:131-172` (INSTRUMENT_PINS), `:325` (`scripts = [path for path, _ in BATTERY]`), `:329` (`git diff --numstat … -- *scripts`) | no pin. `no-deletions` covers the path (`GUARDED_PREFIXES = ("corpus/", "verifiers/")`, `:115`, `:288-290`) — the file must exist, not match a blob. |
| `verifiers/check_gate_registry.py` | requires exactly one registry row naming the path in the universe of `verifiers/*.py|*.sh` blobs; `judge_row` checks the row's entry command names the path, the self-test cell's flag has an exact handler, pinned paths exist | `check_gate_registry.py:118-129` (universe, `ls-tree verifiers/` non-recursive), `:178-226` (judge_row) | no count/sha. Adding arms keeps the `--self-test` handler and the row. |
| `verifiers/box_proof_case_deletion.py` | runs `verify_dispatch_prompts.py --box-proof --map …` at a rev and deletes one manifest case at a time | `box_proof_case_deletion.py:62-65`, `:186` | reads `--box-proof` only; `--box-proof` is a separate function (`verify_dispatch_prompts.py:985`) and never calls `self_test()`. No sha/count pin. |
| `verifiers/fixtures/mutation-battery/manifest.tsv` | no row targets `verifiers/verify_dispatch_prompts.py`; targets are `check_freeze_gate.py`, `check_r86_routed_repairs_v3.py`, `check_mutation_battery.py` | manifest rows, `target` column | no overlap. |
| `verifiers/checklist-baseline.json` | `dispatch.04` / `dispatch.08` rows carry `text_sha256` of the **SKILL.md box text** and `disposition: delegated:verifiers/verify_dispatch_prompts.py` | `checklist-baseline.json:190-200`, `:216-220` | pins SKILL.md prose, not the instrument. No seat edits SKILL.md. |
| `SKILL.md` § Gate registry | one row: `| verifiers/verify_dispatch_prompts.py | gate | python3 -B verifiers/verify_dispatch_prompts.py | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | verifiers/checklist-baseline.json, verifiers/fixtures/dispatch-prompts/manifest.json | self-test tree under $TMPDIR | kotoba |` | `SKILL.md:491` | no assertion count, no sha. |
| `verifiers/verify_skill_checklist.py` | live run executes the delegated instrument's `--box-proof --map <map>` and requires exit 0 | `verify_skill_checklist.py:1031-1071`, `:1313-1314` | `--box-proof` only; arms in `self_test()` do not touch it. |

### The one real hazard: first-match parsing of the summary line

`check_assertion_floors.py:682` uses `re.search(pattern, proc.stdout)` with
`(?m)^(\d+) failure\(s\) over (\d+) assertions$` — it takes the **first** matching line, not the last.
`verify_dispatch_prompts.py` prints that line exactly once, at `:977`, after the arm loop.
⇒ A new self-test arm (or a helper it calls) that prints a line of the form
`<N> failure(s) over <M> assertions` **before** the final summary would make the floors guard read
the wrong count (and could read `observed=0` → FAIL). The round-96 counter is more lenient (it takes
`found[-1]`, `selftest-kills.py:127-135`), so the counter would stay MET while the floors gate reds —
an asymmetry the builder must not walk into. Constraint for `ExecArmsR96`: new arms report through
`rec(...)` only; no intermediate summary-shaped line.

Second, smaller hazard: the floors guard requires `failures == 0` and `returncode == 0` on the honest
run. An arm that is honest-but-wrong (fails on unmutated bytes) reds the floors gate at landing even
though the counter's honest conjunct also reds. Same failure, two gates.

### What a floor bump would cost (and why not to bump)

`floors-registry.json:2` states the BUMP-IN-STEP RULE: a floor move requires the registry, **both**
in-file tables (`EXPECTED_INSTRUMENTS` `:195`, `INSTRUMENTS` `:257`) and the guard docstring
(`:9-10`, `:48`) in one change; a half-bump exits 2 with `FAIL registry floor drift: dispatch_prompts`.
The plan (§ Disclosed bounds) keeps `dispatch_prompts` at 56 — a floor, not an exact count. Since
`:685` is `>=`, leaving 56 is correct and costs nothing; bumping would be an unclaimed edit to a
frozen-adjacent file (`check_assertion_floors.py` is not in any seat's ownership this round).

### Not pinned, but worth naming

- `corpus/lessons/round-83.md:117` and `SCORECARD.md` rows mention `dispatch_prompts PASS` — prose.
- `LOG.md:2394` records "self-test 32 → 56" — history, not a reader.
- `verifiers/check_correction_sweep.py` scans corpus for stale blocks; the round-96 lesson must not
  claim a stale count, but it does not read the instrument.

## Part 2 — sibling lanes: dispatch-prompt checkers / kill counters on prompt instruments

(method: exhaustive `grep -rl --binary-files=without-match "dispatch\.04"` per lane, `find -name
"*selftest-kills*"`, `grep -rl "source-blind"`, `ls */verifiers`, `find -maxdepth 2 -name
"*prompt*|*mutant*|*mutation*|*kill*"` over `/home/vgpnk/Projects/shokunin/*-shokunin`, excluding
`*/sandboxes/*`; receipt `ConnectorOverlapR96/sibling-scan.txt`)

- `dispatch.04` — **one hit in the whole fleet, and it is a quote of kotoba's own instrument**:
  `chousa-shokunin/.ufo/waves/round-73/w1/R73S03/.ufo__l0-questions.md.txt:104` copies the fleet
  `l0-questions` line "kotoba's `verifiers/verify_dispatch_prompts.py` fails dispatch.04 on them on
  every live run. Fleet-owned files; kotoba records the failure and edits nothing there." No sibling
  implements a dispatch-prompt checker.
- `selftest-kills` — **0 hits outside kotoba**; the only files with that name are kotoba's own
  `verifiers/fixtures/round-94|95|96/selftest-kills.py`.
- `source-blind` — hits are wave artifacts and prose, not production instruments:
  `chousa-shokunin/.ufo/waves/round-75/w1/R75Mutation/artifacts/*.py` (7 files) and
  `chousa-shokunin/corpus/evidence/round75/loader-matrix-v2.py`;
  `kama-shokunin/.ufo/waves/round-28/{controls,controls-A1}/…/guess.py` and
  `kama-shokunin/.ufo/waves/round-28/count-c1.py`.
- **No sibling has a `verifiers/` directory at all** (`ls */verifiers` → empty for kama, kengaku,
  chousa, mado, and the other 16). Their gates live in `scripts/`, `tools/`, `plans/` or nowhere.

**Technique prior art (kill counters), none on a prompt instrument:**

| sibling | tool | shape | relation to kotoba v4 |
|---|---|---|---|
| kumitate | `scripts/gate-mutants.mjs` (contract `kumitate-gate-mutants-v2`, kill predicate K43) | every control/mutant gets its own temp copy of `scripts/`; killed iff evaluable and the gate reds | on-disk, not source-blind; judges by exit class, not a failure-line prefix |
| tsukuroi | `tools/mutation-kill-r82.py`, `r83.py` | 26 committed single-clause mutants; "killed when its own `--selftest` exits non-zero" | exit-code-only — the exact weakness v3 rule 1 fixes |
| tabi | `scripts/check-gate-mutants.mjs` + `gate-mutants.json` | on-disk gate mutants | same family |
| tameshi | `tools/*-mutants.spec` | method specs; tameshi owns the reusable mutation method | method owner, no prompt surface |
| kama | `tools/round86-mutant-owners.py` | owner ledger | not a runner |
| kengaku | `plans/mutant_direction_check.py` | one-off plan check | not a runner |

- Adjacent-lane boundary (kotoba `PROVINCE.md` § Adjacent): `kengaku` `adjacent` — "kengaku owns
  measured capability effects of prompt format and hands reusable craft out; kotoba owns the
  prompt/skill craft rules" (`:68`); `kumitate` `adjacent` — "kumitate owns dispatch/orchestration
  tooling and routes 'Prompt and skill craft → kotoba'" (`:70`); `tameshi` `adjacent` — "tameshi owns
  the reusable fixture and mutation method while each lane's gate stays its own; **kotoba's
  `verifiers/*` are unsurveyed sightings there**" (`:77`).
- **Routed finding (not an edit):** tameshi's `corpus/knowledge/fleet-kill-rate-ledger.md:127` lists
  "kotoba `verifiers/*` — file existence is O, their gate-ness is U until a survey admits them". C1's
  new counter is therefore invisible to the fleet kill-rate ledger; integration should report it to
  tameshi rather than assume coverage. This is the only cross-lane consequence of C1 found.
- Conclusion: C1's surface (`verify_dispatch_prompts.py` self-test as a kill target) has **no prior
  art in the fleet and no overlap with any sibling's PROVINCE**. The *technique* is kotoba's own
  v1–v3 lineage (rounds 93–95); the *surface* is new. The live `dispatch.04` red on six fleet-owned
  `*-L1.md` prompts is recorded fleet policy ("kotoba records the failure and edits nothing there"),
  so it must not be read as a C1 defect.

## Part 3 — three candidate round-97 claims (falsifiable before→after + do-nothing control)

Drawn from (a) the recon sweep's survivors not in C1's frozen set, (b) SKILL.md prompt/skill craft,
(c) `considerthese/2026-10-26.md` proposals.

### Candidate A — the sweep survivors outside the frozen set (depth)

Surface: the same instrument, `verifiers/verify_dispatch_prompts.py --self-test`.
Recon survivors not in `CLAIMS["c1"]` (`receipts/recon-sweep.txt`): `m-rstrip-dot`
(`stem = m.group(2).rstrip(".,;:")` → `.rstrip(",;:")`), `m-empty-baseline-pass`
(`return "none", None, "empty %s" % base` → `return "baseline", 10**9, …`), `m-fleetroot-stem-pass`
(`"status": "N/A", "detail": "out of scope: fleet-root role` → `"status": "PASS"`), plus
`m-stem-sibling-pass` (`is_dir()` → `.exists()`) and `m-legacy-as-baseline` (already killed at base).
I verified each of the four live anchors occurs **exactly once** in the freeze bytes
(`ConnectorOverlapR96/anchor-counts.txt`), so a v5 table is well-formed.
- Before: `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 56
  assertions`, rc 0, with each mutant applied on disk (recon; the v5 counter must re-measure
  source-blind).
- After: arms added; a v5 counter table `c2` naming the four anchors → `killed 4 of 4`, honest CLEAN,
  comment/code decoys held.
- Do-nothing control: the v5 counter at the round-96 landing revision → `killed 0 of 4`, rc 1.
- Falsifier: any target whose anchor does not match exactly once → could-not-evaluate (honest stop).
- Alternative under the same axis: close the v4 **code-object-sniffer bound** (a sniffer of its own
  compiled code objects that also proves the decoy guard dead is not caught) with a decoy shape the
  sniffer cannot prove dead — a stricter claim, but it needs a forgery world first.

### Candidate B — seven of nine dispatch boxes are still prose (coverage)

Surface: SKILL.md § Dispatch-prompt fidelity checklist. Measured from
`verifiers/checklist-baseline.json` at the freeze commit (`ConnectorOverlapR96/checklist-counts.txt`):
**45 boxes — 8 executed, 4 delegated, 33 unexecuted**; the dispatch section is 9 boxes,
**2 delegated (`dispatch.04`, `dispatch.08`), 7 unexecuted** (`dispatch.01–03`, `05–07`, `09`).
- Before: `python3 -B verifiers/verify_skill_checklist.py` → detail
  `45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)` (`verify_skill_checklist.py:1374-1379`).
- After: one more dispatch box delegated to a fixture-backed instrument (e.g. `dispatch.05`'s
  "report path is lane-relative and ends at the lane report file"), its `--box-proof` proves the new
  box, map moves `delegated 4 → 5` (dispatch `2 → 3`), `unexecuted 33 → 32`; the box's
  `text_sha256` re-pinned in the same change.
- Do-nothing control: the same run at the round-96 landing revision → `delegated 4`.
- Falsifier: a delegation that does not move the map is not a measurement; a stale `text_sha256`
  makes `--box-proof` exit 1.

### Candidate C — the size ceiling the operator proposal names, made executable (operability)

Surface: `SKILL.md` byte/line budget (considerthese 2026-10-26 § Self-improvement #1: "a byte ceiling
in the floors guard (hold ≤ 70 KB, then ratchet down) and a 200-char max-line check").
- Before (measured at the freeze commit, `ConnectorOverlapR96/skill-size.txt`): `git show
  679775ab:SKILL.md` → **600 lines, 92,672 B**, longest line **1,491 chars (line 518)**, 165 lines
  > 120 chars, 94 lines > 300 chars. The proposal's 2026-10-26 figure was 78,569 B at `314e4a1`;
  the file has grown 14,103 B since. No gate reads bytes or line length.
- After: a gate reads `SKILL.md` bytes and max line length at a named rev and prints
  `skill bytes N of 70000; longest line L of 200`, exit 0/1. Over by 22,672 B (32.4 %) and by
  1,291 chars at the freeze commit, so the first landing is a red-before receipt plus the gate.
- Do-nothing control: the same gate at the round-96 landing revision → exit 1 naming both overages.
- Falsifier: if the landing revision is already ≤ 70 KB and ≤ 200-char lines, the before-value is
  false and the claim must be re-scoped before data.
- Caveat: SKILL.md is at the 600/600-line budget and no seat may edit it — so the *gate* is the
  claim; the reflow is a separate, operator-approved claim.

Also noted (not proposed): considerthese #2 (move § Gate registry to `verifiers/REGISTRY.md`) would
change `check_gate_registry.py`'s input file — a large, frozen-adjacent move, not a one-round claim.

## Measured evidence (this seat, read-only; scratch clone at the freeze commit)

Method: `git clone -q --shared <lane> $S/repo && git -C $S/repo checkout -q 679775abb9…`;
`git -C $S/repo rev-parse --show-toplevel` → `/fast/scratch/hyaku/kotoba-r96/ConnectorOverlapR96/repo`.
No lane write; no commit; no `--rev` reading of the lane beyond `git show`.

1. **Honest baseline (lane working tree, freeze bytes):**
   `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 56 assertions`,
   rc 0; exactly **one** line matches `^[0-9]+ failure\(s\) over [0-9]+ assertions$` (counted with
   `grep -cE`). This is the line `check_assertion_floors.py:682` would read.
2. **One extra arm raises the count and nothing else moves.** In the scratch clone I added one
   `rec("connector probe: one extra arm raises the observed count", True, None)` after
   `write_manifest(cases)` (`verify_dispatch_prompts.py:973`):
   - `--self-test` → `0 failure(s) over 57 assertions`, rc 0;
   - `--box-proof` → `boxes proven 2`, rc 0 (unchanged — `box_proof()` is a separate function,
     `:985`, and `main()` dispatches on the flag, `:1150-1157`);
   - the 12 frozen anchors still occur exactly once (counted from the freeze bytes:
     t01…t11 and p00 each `count=1`).
3. **The first-match hazard is real, and the minimum-floor reading is proven (two floors-guard runs,
   ~8 min total, receipt `ConnectorOverlapR96/floors-two-variants.txt`).** Variant 2 (scratch clone
   `repo2`) inserts `print("0 failure(s) over 3 assertions")` before the final summary; the instrument
   then prints two summary-shaped lines (`0 failure(s) over 3 assertions`, then `0 failure(s) over 56
   assertions`, rc 0). `python3 -B verifiers/check_assertion_floors.py` in each clone:
   - variant 1 (one extra `rec` arm, 57 assertions): `PASS dispatch_prompts observed=57 floor=56`, rc 0
     — **the floor is a minimum; adding arms is safe, and the whole 19-row guard is green at the
     freeze commit**;
   - variant 2 (intermediate summary-shaped line): `FAIL dispatch_prompts observed=3 floor=56`, rc 1
     — `check_assertion_floors.py:682`'s `re.search` takes the **first** match, so one stray
     summary-shaped print reds a gate the round-96 counter would still call MET (it takes
     `found[-1]`, `selftest-kills.py:127-135`).
   ⇒ Hard constraint for `ExecArmsR96`: new arms report through `rec(...)` only; no arm, helper or
   fixture writer may print a line matching `^\d+ failure\(s\) over \d+ assertions$`.
4. **Anchor uniqueness at the freeze commit** (all must stay exactly 1):
   `t01-var-dropped` 1, `t02-var-brace-only` 1, `t03-var-bare-only` 1, `t04-le-to-lt` 1,
   `t05-finish-allna-pass` 1, `t06-role-whole-text` 1, `t07-dirs-subset` 1, `t08-bad-first-only` 1,
   `t09-wrong-first-only` 1, `t10-nonint-baseline` 1, `t11-noreport-04-pass` 1,
   `p00-md-not-stripped` 1. (Computed by importing the frozen counter's `CLAIMS["c1"]` and counting
   each `old` in `git show 679775ab:verifiers/verify_dispatch_prompts.py`.)
5. **Counter mechanics that constrain the arms** (`selftest-kills.py:144-235`): the mutant text is
   written to a temp file, **unlinked**, compiled with `dont_inherit=True` and exec'd as `__main__`
   with `sys.argv=[path, "--self-test"]`; the clone's file keeps honest bytes. `code_decoy` requires
   the mutant to keep the **same line count** and inserts the changed statement under
   `if __name__ == "__decoy__":` immediately before the original (climbing an `elif` to its enclosing
   if-chain, v4 rule 2). Consequence: adding lines to `self_test()` is free; adding a **second copy of
   an anchor statement** is fatal (could-not-evaluate).

## Status

Part 1 complete (plus measured evidence). Part 2 complete. Part 3 complete (three candidates).
No repo writes; scratch clone only.

**Headline for the builders:** floor 56 is a **minimum** (`check_assertion_floors.py:685`), proven by
`PASS dispatch_prompts observed=57 floor=56` on a one-arm clone; the one way to red the floors gate
while the counter stays MET is a stray summary-shaped print (`FAIL dispatch_prompts observed=3
floor=56`, proven on a second clone). Receipts: `ConnectorOverlapR96/{floors-two-variants,
selftest-counts,anchor-counts,checklist-counts,skill-size,sibling-scan}.txt`.
