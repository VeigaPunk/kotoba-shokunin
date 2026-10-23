# NoHarmScores — no-harm on records review (wave 2, round 55)

Result: DONE — no harm found on the checked records: axis scores unchanged, LOG.md and SOURCES append-only, no deleted files, SKILL.md at 598 lines (≤600), and the one prior-round record modified (skill-overlap-levers-round51.md) was a pure append that I verified byte-exact.

Revision pair:
- base: `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`
- tip (master at run time): `f0e6b695b746775823b65a8c45de7d50ea33e84f` — `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master` → `f0e6b695b746775823b65a8c45de7d50ea33e84f` (run at `date -u` → `Fri 23 Oct 2026 12:08:52 AM UTC`).

## Checks (all run in the lane, read-only git)

### 1. SCORECARD.md axis scores — identical at both revisions

Extracted the Score column from the `## axes` table at both revisions:

```
$ git show f0e5de82:SCORECARD.md | awk '/^\| Axis \| Score/{f=1;next} f&&/^\|/{split($0,a,"|"); ...}'
depth => 9
consistency (calibration sub-axis) => 10
coverage => 8.5 — was 8.0
operability (advisory) => 8.5 — was 8.0
freshness (advisory) => 8
calibration (advisory) => 8.5 — was 8.0
adjacency (advisory) => 8.0 — was 7.5
```

Identical output at `f0e6b695`. No axis score moved. SCORECARD.md itself changed only by additions: non-header removed-line count 0 (`git diff f0e5de82 f0e6b695 -- SCORECARD.md | grep -c '^-[^-]'` → `0`).

### 2. LOG.md append-only — clean

```
$ git diff f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c f0e6b695b746775823b65a8c45de7d50ea33e84f -- LOG.md | grep -c '^-[^-]'
0
```

No non-header removed line; the LOG.md diff is purely additive.

### 3. SOURCES append-only — pass

```
$ cd /fast/scratch/hyaku/kotoba-r55/NoHarmScores   # sandbox clone at f0e6b695
$ python3 -B verifiers/check_sources_append_only.py --base f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c --rev f0e6b695b746775823b65a8c45de7d50ea33e84f
sources append-only rows clean: 1 commits scanned, 0 protected-cell changes
$ echo $?
0
```

Sandbox clone per bounds: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/NoHarmScores && git -C /fast/scratch/hyaku/kotoba-r55/NoHarmScores checkout -q f0e6b695b746775823b65a8c45de7d50ea33e84f` (clone OK, checkout OK). No git writes in the lane.

### 4. Deleted files — none

```
$ git diff --name-status --diff-filter=D f0e5de82 f0e6b695
(empty)
```

Full change histogram base→tip: 64 A, 15 M, 0 D, 0 R (79 paths total).

### 5. SKILL.md line count — 598 ≤ 600

- base: `git show f0e5de82:SKILL.md | wc -l` → 599
- tip: `git show f0e6b695:SKILL.md | wc -l` → 598 (one less than the plan-declared 599; the round-55 move freed lines)

### 6. Prior-round record touched — pure append, and the "verbatim" claim verified

The only modified prior-round record is `corpus/knowledge/skill-overlap-levers-round51.md` (round-51 entry). Its diff is add-only (non-header removed-line count 0) and appends a `## Moved from SKILL.md § Anti-patterns (round 55, verbatim)` section quoting exactly base SKILL.md lines 407–426.

I verified the byte-exactness claim (not taken on trust): exactly the 20 lines `sed -n '407,426p'` of base `SKILL.md` vs the appended block (added lines 9–28 of the file diff) are byte-identical:

```
$ cmp /tmp/base_block.bin /tmp/app_block.bin && echo CMP-IDENTICAL
CMP-IDENTICAL
$ sha256sum /tmp/base_block.bin /tmp/app_block.bin
1423f8ce569b3e409541b984694f017fe56fc0792946027743ac68b71c4b6c19  /tmp/base_block.bin
1423f8ce569b3e409541b984694f017fe56fc0792946027743ac68b71c4b6c19  /tmp/app_block.bin
```

This is the round-55 move that made room for the `### Explicit invocation by client` table (plan: SKILL.md 599/600 → any added table replaces or compresses existing text, and the change is logged; the entry documents the move and SKILL.md keeps a pointer to it). Not a record harm.

## Observations (not findings)

- SKILL.md's round-54 "Description thresholds by client" table cells were edited (Codex, Gemini CLI, Cursor rows — e.g. the Codex evidence cell reworded; Gemini CLI row now pins loader/prompt-template lines and a commit). This is the routed defect (3) repair "the four over-wide C1 cells narrowed" (plans/round-55.md § Frontier step and routed defects), explicitly in round-55 scope. It does not touch the scores or the append-only records above.
- `verifiers/check_could_not_evaluate.py` is a new gate at the tip (only for the counter, not a record).
- I did not run the remainder-55 counters (C1/C2 predicates), inspect gate patches, or reopen S065–S071 — those are other seats' assignments; this seat is scoped to no-harm on records.

## Residual risk / verification gaps

- "Records" checked here: SCORECARD.md, LOG.md, SOURCES (via the frozen append-only verifier), deleted files, SKILL.md line count, and the one modified prior-round knowledge entry. Other record-carrying files (e.g. `corpus/lessons/round-55.md`, `corpus/QUALITY.md`, `corpus/README.md`, prior-round lesson/knowledge files) were not audited line-by-line; the 15 modified files list is above in case the integrator wants a narrower follow-up.
- The two counters' receipts and the SOURCES census were not re-derived here (other seats).
