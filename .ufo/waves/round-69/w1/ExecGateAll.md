# ExecGateAll — round-69 wave-1 gate battery (kotoba)

**Scope:** run the assigned seven-gate battery against the lane tip with the L1's uncommitted
round-69 draft, print each command with its exit code and verdict line, and report every gate that
is not green. Leaf seat: no mutation of the lane, no commits, no jj.

**Verdict up front: 3 of 7 green, 4 red.** `check_gate_registry` 49/49, `check_skill_precedence`
5/5 and `check_province_core` 2/2 are green. `verify_corpus_integrity` (5/9), `verify_corpus_independent`
(exit 1), `verify_skill_checklist` (exit 1) and `check_r68_routed_repairs` (4/8) are red, for four
distinct causes: a stale corpus baseline, one missing coverage-map row, a SKILL.md line-budget
overrun, and two dead LOG.md citations that predate the round.

## Measurement setup

| item | value |
|---|---|
| lane | `/home/vgpnk/Projects/shokunin/kotoba-shokunin` |
| lane branch tip (`git rev-parse master`) | `a238989a96cb0d2b939679126b832d75b861ca6e` (r69 plan commit) |
| plan's pinned base | `a5f7459f99bb27bf697e9438362e75ac5833eca8` (r68 spot-check) |
| draft state | uncommitted: 7 modified tracked files + `corpus/knowledge/skill-name-precedence-round69.md` and `corpus/lessons/round-69.md` untracked |
| measurement sandbox | `/tmp/r69sandbox/kotoba-shokunin` = `git clone --shared` of the lane at `a238989` + rsync of the lane working tree + one integration commit |
| integration rev measured by `--rev` counters | `b8c6e6a178495401c744e43fa007e882a5351568` |
| base sandbox | `/tmp/r69base/kotoba-shokunin` = `git worktree add --detach a238989` with the same sibling mirror |

Why an integration commit exists: `check_gate_registry`, `check_r68_routed_repairs`,
`check_skill_precedence` and `check_province_core` read **committed** bytes at `--rev`
(`check_skill_precedence`'s `_materialize` runs `git show <rev>:<path>`; the other three read the
tree the same way). The draft is uncommitted, so at the bare tip every
content claim is necessarily `0 of N` (verified, see § Base controls). The sandbox commit is the
only faithful way to measure the draft's committed-byte verdict without touching the lane's index.
Nothing was written to the lane; the commit lives only in `/tmp`.

Sandbox fidelity: the lane's own checks are path-sensitive. The first sandbox was named
`/tmp/r69-gate`, which produced two false results — `trigger.name_directory`
(`name 'kotoba-shokunin' != directory 'r69-gate'`) and 15 extra `governance.citation_resolves`
tokens (four shown: `../PROTOCOL.md`, `../kasegi-shokunin/corpus/instruments/resolve.py`,
`…/anchorcheck.py`, `../AXES.md`; "+11 more" elided) because `../` pointed at `/tmp`. The sandbox
used for every
number below is named `kotoba-shokunin` and its parent mirrors the fleet root: every sibling lane
entry and the hidden entries `.devin .gitignore .omp .scratch .tower .ufo` are symlinked into
`/tmp/r69sandbox` (and `/tmp/r69base`) so `../…` citations resolve exactly as in the real fleet.
`.git`, `.jj`, `__pycache__` and `.ufo/waves/round-68/w1/controls/c2falsify-clone/` (269 MB) are
excluded from the rsync; the clone is the path the round-69 lesson dispositions as removed.

## The assigned battery, verbatim

Run from `/tmp/r69sandbox/kotoba-shokunin`, `T=b8c6e6a178495401c744e43fa007e882a5351568`.

### 1. `python3 -B verifiers/verify_corpus_integrity.py --json`

```
exit=1
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total
```

Expected by the assignment: 9/9, exit 0. **RED.** JSON detail:

| check | mode | observed | expected |
|---|---|---|---|
| `corpus.index.tracked_files` | equal | 127 | 124 |
| `corpus.index.unindexed` | zero | 1 (`corpus/lessons/round-69.md`) | 0 / empty |
| `corpus.pointers.report_total` | equal | 87 | 85 |
| `corpus.pointers.commit_total` | equal | 39 | 38 |

The other five checks (`stale_patterns`, `missing_paths`, `report_dead`, `commit_unresolvable`,
`commit_nonhash`) PASS at 0.

### 2. `python3 -B verifiers/verify_corpus_independent.py --json`

```
exit=1
DRIFT corpus.index.unindexed: {"mode": "zero", "observed": 1}
```

Expected: exit 0. **RED.** All other eight results are PASS or INFO
(`tracked_files` 127, `report_total` 87, `commit_total` 39 are intentionally `observe`/INFO here).
The single unindexed file is `corpus/lessons/round-69.md`.

### 3. `python3 -B verifiers/verify_skill_checklist.py --json`

```
exit=1
{"exit_code": 1, "fail": 2, "na": 0, "pass": 9}
FAIL trigger.line_budget | 603 lines exceed budget 600 (from box at line 319)
FAIL governance.citation_resolves | LOG.md:2676: '.ufo/waves/round-67/w1/controls/census-validate-append.txt'
       does not resolve; LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve
       (10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused,
        0 recorded correction(s) excused)
```

Expected: exit 0. **RED.**

### 4. `python3 -B verifiers/check_gate_registry.py --rev b8c6e6a1…`

```
exit=0
gate registry rows conformant 49 of 49 lane verifiers; phantom 0
```

**GREEN.** Matches the expected 49 of 49. All three round-69 counters have conformant rows.

### 5. `python3 -B verifiers/check_r68_routed_repairs.py --rev b8c6e6a1…`

```
exit=1
measured-rev: b8c6e6a178495401c744e43fa007e882a5351568
r68 routed defects closed 4 of 8
  - D3: verifiers/check_r67_routed_repairs.py still runs `git checkout` (a git write in the lane)
  - D6: corpus/lessons/round-69.md § Mistakes has no row naming R68-6 and S201
  - D7: .ufo/waves/round-68/w1/controls/c2falsify-clone/ is neither committed nor dispositioned
  - D8: baseline corpus.index.tracked_files expects 124, the gate measures 127
  - D8: baseline corpus.index.unindexed expects 0, the gate measures 1
  - D8: baseline corpus.pointers.report_total expects 85, the gate measures 87
  - D8: baseline corpus.pointers.commit_total expects 38, the gate measures 39
```

Expected: 8 of 8, exit 0. **RED at 4 of 8.** D1, D2, D4 and D5 are green (no finding printed).

### 6. `python3 -B verifiers/check_skill_precedence.py --rev b8c6e6a1…`

```
exit=0
measured-rev: b8c6e6a178495401c744e43fa007e882a5351568
skill precedence backed 5 of 5
```

**GREEN.** Matches the expected 5 of 5.

### 7. `python3 -B verifiers/check_province_core.py --rev b8c6e6a1…`

```
exit=0
measured-rev: b8c6e6a178495401c744e43fa007e882a5351568
province core rows 2 of 2
```

**GREEN.** Matches the expected 2 of 2; `## Frontier`/`## Adjacent` untouched-conjunct also holds
(the counter returns 0 only when both areas and the byte-identical conjunct pass).

## Base controls, re-derived (not accepted from any seat)

| command | at `a238989` (bare tip, no draft) | at integration `b8c6e6a1` |
|---|---|---|
| `check_skill_precedence.py --rev` | `skill precedence backed 0 of 5`, exit 1 | `5 of 5`, exit 0 |
| `check_r68_routed_repairs.py --rev` | `r68 routed defects closed 0 of 8`, exit 1 | `4 of 8`, exit 1 |
| `check_province_core.py --rev` | `province core rows 0 of 2`, exit 1 | `2 of 2`, exit 0 |
| `verify_corpus_integrity.py` | `6/9 checks pass`, exit 1 | `5/9 checks pass`, exit 1 |
| `verify_skill_checklist.py` (base worktree) | `trigger.line_budget` **PASS** — `600 lines within budget 600` | FAIL at 603 |
| `verify_skill_checklist.py --check governance.citation_resolves` (base worktree) | **FAIL** on the same two LOG.md tokens | FAIL (same two tokens) |

Base integrity measured today at `a238989` reproduces the committed
`.ufo/waves/round-69/controls/C2-base-integrity.txt` byte-for-byte in its drift set
(`125/1/87` vs `124/0/85`), so the base control is honest and my sandbox is not inflating the
numbers. Base JSON detail: `tracked_files 125`, `unindexed 1` =
`corpus/lessons/round-68-verifier-spotcheck.md`, `report_total 87`, `commit_total 38` (38 matches
the baseline, so `commit_total` is a *draft-only* drift). The base checklist run over the worktree
(`--repo`/`--skill` override) is exit 1 with **one** real failure — the same
`governance.citation_resolves` tokens; `trigger.line_budget` passes. (`checklist.box_map_complete`
reports N/A in that override invocation because `--skill` was given without `--map`; in the in-repo
draft run it is PASS, so that is an invocation artifact, not a base condition.) Repository counts: `git ls-tree -r -- corpus` = 125 at `a5f7459` and `a238989`, 127 at the
integration rev (+ only `corpus/knowledge/skill-name-precedence-round69.md` and
`corpus/lessons/round-69.md`).

## Red-gate root causes (each with the minimal green path)

### A. `corpus-baseline.json` was never re-recorded (R68-8) — integrity ×4 and C2 D8

`verifiers/corpus-baseline.json` is **not** among the draft's modified files. Its pinned expectations
are still the r68 ones, while the gate measures the draft's own additions. Two of the four drifts are
**inherited at the base** (`tracked_files` 125 vs 124 and `report_total` 87 vs 85 are already wrong at
`a5f7459`/`a238989`); two are produced by the draft's commit (+2 tracked corpus files → 127, +1
commit → 39).

The `unindexed` drift cannot be cleared by re-recording at all: its mode is `zero`, so a baseline that
records `1` still fails the gate. The fix is an index row, not a baseline edit.

Green path: add the coverage-map row (B below), then record the baseline from the gate's own
`--no-baseline --json` measurement **at the content commit** — `127` tracked, `0` unindexed, `87`
report pointers, `39` commits (38 at base + the content commit itself).

### B. `corpus/lessons/round-69.md` is not indexed — independent DRIFT + integrity DRIFT

Evidence: `grep -c 'round-69.md' corpus/README.md` = **0**; the new entry
`corpus/knowledge/skill-name-precedence-round69.md` = **1** (so C1's index conjunct is genuinely
satisfied). The draft does add the missing row for the r68 closure's lesson
(`round-68-verifier-spotcheck.md`: 0 rows at base → 1 row in the draft), i.e. it fixed the inherited
unindexed file and opened its own. Net count stays 1, which is why the drift reads the same as the base
but against a different file.

### C. `trigger.line_budget` — draft-introduced regression

Base `SKILL.md` = 600 lines and the check PASSes (`600 lines within budget 600 (from box at line 319)`).
The draft's three gate-registry rows (`check_skill_precedence.py`, `check_r68_routed_repairs.py`,
`check_province_core.py`, added in the diff at `SKILL.md:517-519`) make the file 603. The registry gate
requires those rows, so the fix is to reclaim three lines elsewhere in `SKILL.md`, not to drop them.

### D. `governance.citation_resolves` — inherited, and beyond the frozen correction horizon

Both dead tokens are in `LOG.md` and are **not** touched by the draft (`git diff a238989 -- LOG.md` is
empty):

```
LOG.md:2675  - **Erratum (append-only; routed defect R67-2).** … cites …
LOG.md:2676    `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the file that exists is
LOG.md:2677    `.ufo/waves/round-67/controls/census-validate-append.txt`.
LOG.md:2678  - **Routed defect R67-3 (disclosure).** `.ufo/waves/round-67/w1/controls/junk-world/` …
```

`git blame` puts lines 2674-2679 in `605b84b` — *round-68: C1 depth client trust gates (entry,
S198-S202, counter) and C2 consistency routed r67 repairs* — which is an ancestor of `a5f7459`, the
r68 spot-check tip. Neither path exists at the base or at the draft (`git ls-tree -r a238989` carries
only `.ufo/waves/round-67/controls/census-validate-append.txt`, with no `w1`). The r65 correction
mechanism cannot excuse them: `GOVERNANCE_CORRECTIONS_HORIZON = 2621` and its three rows are
byte-pinned to lines 2619-2621, so a notice at line 2676 and a stale token at 2676/2678 are outside
the horizon by construction.

Consequence for the round: the r68 closure's stated tip result
(`.ufo/waves/round-68/w1/CriticC2Predicate.md:11`, "Tip: `9/9 checks pass` exit 0 · independent
`--json` exit 0") **does not reproduce at its own tip**. `verify_skill_checklist` is red at `a238989`
and at the integration rev for the same two tokens. This is an instrument-level red, not a draft
regression, and a content-only edit cannot clear it (appending another notice changes nothing while
the horizon is pinned at 2621).

### E. C2 D3 — the conjunct flags a *legitimate* sandbox checkout (instrument false positive)

`verifiers/check_r68_routed_repairs.py:227`:

```python
if re.search(r"[\"']checkout[\"']", src):
    return [f"D3: {R67_COUNTER} still runs `git checkout` (a git write in the lane)"]
```

Any quoted `'checkout'` in `verifiers/check_r67_routed_repairs.py` trips it. The draft's r67 counter
does no lane write — it materializes a `/tmp` clone and checks out the measured rev **in the clone**:

```python
proc = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout", str(self.path), str(clone)], …)
subprocess.run(["git", "-C", str(clone), "checkout", "-q", self.rev], …)
```

So the detector cannot distinguish the routed defect (`git checkout <rev> -- corpus verifiers` in the
lane, which wrote the lane's index) from the sandbox operation the counter's own `--repo` arm needs.
The same regex would *pass* a lane write phrased as `git --work-tree=. restore`. D3's other two
conjuncts (base-content verdict `0 of 4`, tip `4 of 4`) are green.

Green paths: (i) materialize the r67 sandbox with `git archive <rev> | tar -x -C <tmp>` so the literal
does not occur, or (ii) narrow the detector to a checkout whose `-C`/`--work-tree` target is the lane
(root) rather than a `/tmp` clone. Option (ii) is an instrument change and collides with Q28.

### F. C2 D6 — the required tokens are split across two lines

`d6_mistake` requires **one** line of `§ Mistakes` containing both `R68-6` and `S201`
(`any("R68-6" in l and "S201" in l …)`). The lesson has `R68-6` on line 102 and `S201` on line 103
(`- **M111 — class: a refusal whose reason is false (R68-6).** Evidence: … round-68.md` / `§ Gate
refused the staged S201 quote …`). Rewording line 102 to carry both tokens clears it; the criterion
half (`QUALITY.md` row citing `round-69.md`) is satisfied.

### G. C2 D7 — the disposition names an abbreviated path

`d7_wave_paths` parses `disposition: removed <path>` with `([^`\s]+)`. The lesson writes:

```
dispositioned as removed (the clone: `disposition: removed .../c2falsify-clone/`)
```

so the captured path is `.../c2falsify-clone/`, not
`.ufo/waves/round-68/w1/controls/c2falsify-clone/`. The other 23 paths pass: the ten modified r68
logs carry blobs that differ from the base and the thirteen other untracked paths (seven seat
reports, four drafts, `c2falsify2.py`, `seat-results.json`) are committed. Writing the full path
clears D7.

## What a green battery requires (minimal, itemized)

1. `corpus/README.md`: one coverage-map row for `corpus/lessons/round-69.md` (clears independent, and
   the `unindexed` drift in integrity — a zero-check, so re-recording cannot substitute).
2. `verifiers/corpus-baseline.json`: re-record the four `expect` values from the gate's own
   `--no-baseline --json` at the content commit — `127 / 0 / 87 / 39` (clears the other three
   integrity drifts and C2 D8).
3. `SKILL.md`: reclaim 3 lines so the file is ≤ 600 while keeping the three registry rows.
4. `corpus/lessons/round-69.md`: put `R68-6` and `S201` on one line (D6) and write the full
   `disposition: removed .ufo/waves/round-68/w1/controls/c2falsify-clone/` path (D7).
5. C2 D3: change the r67 counter's sandbox materialization away from the literal `checkout`
   (e.g. `git archive`), or narrow the D3 detector — an instrument decision, not a content edit.
6. Checklist `governance.citation_resolves`: the two r67 LOG.md tokens (lines 2676/2678) must resolve,
   or the correction mechanism must cover them. With `GOVERNANCE_CORRECTIONS_HORIZON = 2621` pinned
   and byte-pinned rows, an appended notice alone cannot clear this; the lane must either commit the
   two cited paths or widen the frozen instrument (Q28 event). **This is the one red that cannot be
   closed inside the round's stated content scope — escalate to L1.**

Already green and not to be disturbed: `check_gate_registry` 49/49, `check_skill_precedence` 5/5,
`check_province_core` 2/2, and C2 D1/D2/D4/D5.

## Caveats and risks

- **`commit_total` 39 is commit-shape, not content.** My integration commit is the 39th; the lane's
  real content commit will also be the 39th, so the expected value a builder must record is 39, not 38.
  If the lane splits the round-69 landing into two commits, the number moves and D8 fails again —
  the baseline must be recorded from the gate's own measurement at the final rev, not by arithmetic.
- **The `0 recorded correction(s) excused` figure in the draft run is sandbox-influenced** (the base
  worktree, run with the same instrument, reports `3 recorded correction(s) excused`). The two
  failing tokens are identical in both runs, so the red is real either way; only the excusal counter
  differs, because the draft sandbox carries the lane's untracked `.ufo` content.
- `check_skill_precedence.py --fetch` was **not** run: it is not in this seat's assigned battery and
  belongs to the fetch/scout arm.
- No gate was run inside the lane. All execution happened in `/tmp/r69sandbox` and `/tmp/r69base`;
  lane git use was read-only (`rev-parse`, `log`, `show`, `ls-tree`, `blame`, `diff`, `status`).
- At most two gate processes ran concurrently (contention cap: 4).

## Installs

None. No tool was installed or updated for this seat.

## Reproduction

```
git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/r69sandbox/kotoba-shokunin
# mirror siblings + hidden entries of /home/vgpnk/Projects/shokunin into /tmp/r69sandbox
rsync -a --exclude='.git/' --exclude='.jj/' --exclude='__pycache__/' \
      --exclude='.ufo/waves/round-68/w1/controls/c2falsify-clone/' \
      /home/vgpnk/Projects/shokunin/kotoba-shokunin/ /tmp/r69sandbox/kotoba-shokunin/
cd /tmp/r69sandbox/kotoba-shokunin && git add -A && git commit -m 'round-69 draft integration snapshot'
# then the seven commands above with --rev <that commit>
```

Raw outputs in `/tmp/r69-ev3/`: `integrity_json`, `integrity_human`, `independent_json`,
`independent_human`, `checklist_json`, `checklist_human`, `registry`, `r68`, `precedence`,
`province` (integration rev `b8c6e6a1`); `base_integrity`, `base_integrity_json`,
`base_checklist_json` (base `a238989`, the latter two from `--repo /tmp/r69base/kotoba-shokunin`).
