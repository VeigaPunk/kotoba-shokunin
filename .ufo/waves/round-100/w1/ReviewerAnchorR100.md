# ReviewerAnchorR100 — C2 patch review (round 100, wave r100-w1)

Seat: ReviewerAnchorR100. Item: review `.ufo/waves/round-100/w1/ExecAnchorR100/ExecAnchorR100.patch`
against `plans/round-100.md` § C2 and the `anchor-lists.py` v1 header. Status: **IN PROGRESS — waiting
for ExecAnchorR100_READY** (poll every 120 s, cap 75 min). This file is updated as evidence lands.

## Review axes (blocking first)

1. **[B] Fix line byte-equality** — the changed line in `strip_token_dressing` must be byte-equal to
   the counter's `FIX_LINE` (`    m = re.match(r"^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$", tok)\n`).
2. **[B] Regex shape** — accepts only `:N`, `:N-M`, comma-joined digit lists; refuses every other
   suffix (trailing comma at the regex level, empty segment, leading comma, word segments, dangling
   dash). Verified against the frozen truth table semantics (r01–r14 × both paths).
3. **[B] No collateral reading change** — gate run with `--json` at 03a98eb and at the candidate;
   every evaluated subject list diffed (trigger.citation_resolves, governance.citation_resolves, the
   command checks that use `path_like_arg`); every token whose normalisation changed must be named.
4. **[B] Data change confined** — the one `GOVERNANCE_CORRECTIONS` row with stale token
   `corpus/lessons/round-80-verifier-spotcheck.md:30,37` is the only data change; the REV corrections
   block equals the base block minus exactly that row.
5. **[B] Removal honesty** — with the fix the row's subject resolves (fail-closed correction check
   would reject it); `LOG.md:3598` stays as history; the patch must not touch `LOG.md`.
6. **[B] New arms** — behaviour-only (call main/run_checks/read_text/strip_token_dressing, read the
   result), source-blind (no read of the checklist's own source — the kill conjunct is on-disk-only,
   so a source-sniffing arm would fake a kill), exceptions caught into the `rec(...)` tally, no
   git/network/env beyond TMPDIR/HOME, argv explicit, stdout captured in-process; the arm kills the
   revert mutant.
7. **[B] Battery pins-only** — `check_tip_battery.py` hunk entirely inside `INSTRUMENT_PINS = {...}`.
8. **[B] Counter on the candidate** — `anchor-lists.py <candidate-rev> <scratch-repo>` must read
   `C2 mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok`,
   `C2-PREDICATE-MET`, rc 0.
9. Ownership — patch touches only `verifiers/verify_skill_checklist.py` (fix line, `self_test()`
   body, the one corrections row) and `verifiers/check_tip_battery.py` (`INSTRUMENT_PINS` block
   only). Nothing else — not the docstring, not `LOG.md`, not SKILL.md, not corpus files.

## Evidence log

- Scratch: `/fast/scratch/hyaku/kotoba-r100/ReviewerAnchorR100/` (TMPDIR + HYAKU_SCRATCH exported;
  removed before yield). Clone `repo` at `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`, clean
  (`rev-parse --show-toplevel` = the clone dir).
- Instrument bytes: `anchor-lists.py` sha256 `c31db02dca3a292c394bdfd551106996a40250e42c80bc27d6190c51fc99af02`
  (matches the pre-data receipt header). `BASE_LINE`/`FIX_LINE` extracted via `ast.literal_eval`
  and mirrored into `confinement_check.py` (pre-counter conjunct mirror) and `regex_battery.py`
  (behaviour battery) and `subject_diff.py` (evaluated-subject diff harness).
- Pre-data control readings (receipts): c2-base `mismatches 8 of 28; gate GREEN; self-test HELD
  (1864); kill ABSENT; frozen 2 of 3; battery ok` UNMET rc 1 — rows r01–r04 on both paths, all eight
  MISMATCH, no other row touched; this is the exact before-state the patch must heal and nothing more.
- Base `--json` gate on the clone: pass 8 / fail 3 / exit 1 — all three FAILs environmental, not
  content: `trigger.name_directory` (clone dir named `repo`), `trigger.citation_resolves` 260
  evaluated (first miss `../.ufo/reports/round-7/kotoba.md` — `../` hops resolve against the clone's
  parent, not the fleet root), `governance.citation_resolves` 1679 evaluated (corrected tokens
  `../.ufo/...` unresolvable from scratch). The counter's gate instead runs in the round-base
  `build_sandbox` fleet-shaped sandbox (fleet entries symlinked beside it), which is the GREEN
  authority. Saved as `gate-base-json.txt`; the same-environment candidate run isolates patch effects.
- Subject-diff harness validated: base-vs-base all keys `same` (trigger.citations 260,
  governance.subjects 1687 / live 1679 / red 54 environmental, corrections excused 6 / problems 14
  environmental, command.subjects 36 / segments 23, normalisation_changes 0).
- Counter internals confirmed: kill conjunct substitutes FIX_LINE→BASE_LINE ON DISK in the sandbox
  copy (so a source-sniffing self-test arm would fake a kill — arm code review is mandatory and
  mine), requires FIX_LINE to occur exactly once in the REV checklist, and requires the reported
  failure shape (exit 1 + `self-test FAIL: ` + `N failure(s) over M assertions`, N≥1). `checklist_confined`
  compares base+FIX_LINE vs REV outside the self_test region and the corrections block, and requires
  REV rows == base rows minus exactly the `RETIRED_STALE` row.
- Battery pin schema: `INSTRUMENT_PINS` maps script → tuple of allowed git blob hashes
  (`rev-parse rev:path`); round-99 prior art appends the new blob with a naming comment and keeps
  earlier pins. The REV checklist blob must be inside the REV pins block for `guards 5 of 5`.
- Real-tree grounding: the only live `path.ext:N,M` subject is SCORECARD.md:529 (per LOG.md:3598 the
  stale token `corpus/lessons/round-80-verifier-spotcheck.md:30,37`, corrected to the bare path);
  LOG.md:3598's notice quotes the stale token in double quotes → excluded from governance subjects
  (the notice stays inert history); `corpus/lessons/round-80-verifier-spotcheck.md` exists (72
  lines) so the subject resolves once the fix lands → row removal is honest. SKILL.md's comma
  anchors (lines 115–121, e.g. ``S090 `:10,18,34,40-42` ``) are file-less spans — not citation
  subjects at base or candidate.
- Behaviour battery calibrated on the BASE module: exactly the comma-list ACCEPT shapes fail
  (`:30,37`, `:3,7-9`, `:10,18,34,40-42`, `:30,37,`, `:30-40,42`), zero REFUSE failures. Two
  pre-existing dressing quirks noted (unchanged by the fix, out of scope): `.` is not trailing
  punct (`:42.` stays refused), and a trailing punct-run including `:` strips to the bare path
  (`x.md:,` → `x.md`).

## Findings

### Blocking findings

None. Every axis checked passes.

### Axis-by-axis verdicts (candidate = 03a98eb + ExecAnchorR100.patch = `7145b87ef2fc9e42c3500895a70057a910a3f73f` in my scratch clone)

1. **Fix line byte-equality — PASS.** The checklist blob at the candidate is `94d11c7a103590bfeea93910da6710bd8a64f0c6` (byte-identical to the builder's pinned blob, so our clones hold the same bytes). The changed line occurs exactly once and equals the counter's `FIX_LINE` byte-for-byte (`confinement_check.py`: "fix line occurrences in REV checklist: 1"; base line 0 occurrences).
2. **Regex shape — PASS.** Behaviour battery on the candidate module (`regex_battery.py`): every digit-list accept resolves to the bare path (`:42`, `:1-2`, `:30,37`, `:3,7-9`, `:30-40,42`, `:10,18,34,40-42`, `:30,37,` via the pre-existing trailing-punct strip) and every malformed suffix keeps the anchor (`:30,,37`, `:,30`, `:5-`, `:30-`, `:30,abc`, `:abc`, `:30-40-50`, `:30--40`, `:30;37`, `:+30`, `:30.37`, `: 30`, `:0x30`, `:42.`, `:30,-37`, `:3,7-`). Base module fails exactly the comma accepts and none of the refuses — the delta is exactly the claim.
3. **No collateral reading change — PASS, two normalisation changes named.** A tree-wide sweep (SKILL.md + LOG.md + SCORECARD.md inline spans, base vs candidate module) finds exactly two raw tokens whose normalisation changed: (a) `corpus/lessons/round-80-verifier-spotcheck.md:30,37` → `corpus/lessons/round-80-verifier-spotcheck.md` — the intended heal; (b) `skills.mdx:137,142` → `skills.mdx` (SKILL.md:190 table cell) — **inert**: it carries no `CITATION_ROOTS` prefix so it is not a citation subject on either side, and it is not a fenced command argument (command subjects unchanged). Same-environment gate `--json` diff (base vs candidate on my clone): every check byte-identical except `governance.citation_resolves` — evaluated 1679 → 1680, the SCORECARD.md:529 subject now live and resolving instead of excused; `trigger.citation_resolves` 260 unchanged, `trigger.command_binary_resolves` 36 subjects / 23 segments unchanged.
4. **Data change confined — PASS.** Corrections rows: base 20 → candidate 19; candidate rows == base rows minus exactly `(3598, '49419804…', 'SCORECARD.md', 529, 'corpus/lessons/round-80-verifier-spotcheck.md:30,37', 'corpus/lessons/round-80-verifier-spotcheck.md')`; zero rows added, zero rows otherwise changed. Checklist bytes equal to base+FIX_LINE outside the `self_test` region and the corrections block (the counter's own `checklist_confined` shape, mirrored). Battery identical outside its `INSTRUMENT_PINS` block; the pins diff is exactly the tail of the `verify_skill_checklist.py` tuple (admission comment + new blob, "earlier four blobs are kept" — prior four pins intact).
5. **Removal honesty — PASS.** With the fix, the row's subject resolves (`corpus/lessons/round-80-verifier-spotcheck.md` exists, 72 lines), so keeping the row would trip the fail-closed "names no live red subject" branch of `correction_problems` — removal is required, not cosmetic. The patch has no `LOG.md` hunk: the byte-pinned notice at LOG.md:3598 stays as history (its stale token is double-quoted there, hence excluded from governance subjects — it never was a live red subject itself).
6. **New arms — PASS (anti-sniffing reviewed; kill verified independently).** All 22 new assertions sit inside the `self_test()` body (region after the delegated-proof block, before the summary print; exactly one `^def self_test` region still matches the counter's regex). Arms observe behaviour only: they build a fixture world under `tempfile.TemporaryDirectory` (TMPDIR-honoured), write fixture `corpus/lessons/x.md` (40 lines), `LOG.md`/`SCORECARD.md`, call `check_citation_resolves` / `check_governance_citations` and assert status/evaluated through `rec(...)`. No read of the module's own source, no `__file__`, no inspect, no git, no network, no environment variables; every call is wrapped in `try/except → rec(..., False, repr(exc))` so a raising mutant reports failures instead of crashing. Coverage: 7 resolving tokens × {trigger, governance} + 4 red tokens × {trigger, governance} (governance world asserts `evaluated == 2` — non-vacuous on both sides). Independent revert-mutant run (FIX→BASE swapped on disk in my clone, honest bytes restored afterwards, `git status` clean): exit 1, `self-test FAIL: ` × 8, summary `8 failure(s) over 1886 assertions` — exactly the four comma-token trigger arms and four comma-token governance arms fail; the bare/`:42`/`:1-2` and all red-token arms still pass, so the kill is attributable to the claim's surface, not to collateral breakage.
7. **Battery pins-only — PASS** (see 4). The pinned blob equals the candidate checklist blob (verified `rev-parse HEAD:verifiers/verify_skill_checklist.py`).
8. **Counter on the candidate — PASS.** `anchor-lists.py 7145b87ef2fc9e42c3500895a70057a910a3f73f <my clone>` (frozen bytes, sha256 `c31db02d…`, one run) reads:
   `C2 mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok` → `C2-PREDICATE-MET`, rc 0.
   Detail: 28/28 rows OK on both public paths; sandbox gate exit 0, 11 PASS lines, 0 FAIL/N/A; self-test exit 0 at 1886 assertions (floor 1864); revert mutant `exit 1 last '8 failure(s) over 1886 assertions'` — identical to my independent on-disk revert run; frozen 3/3 (checklist confined YES, battery IDENTICAL outside INSTRUMENT_PINS, both corpus verifiers IDENTICAL); battery guards 5 of 5 with `gate verifiers/verify_skill_checklist.py exit 0 wall 1.6s`, `tip battery exit 0: 4 of 6` — the two red corpus gates are the known landing drift (unindexed round-99 spot-check lesson), which the counter deliberately does not score (`battery exit 1 ok`). The reading matches the builder's own receipt line-for-line.
9. **Ownership — PASS.** The patch's only files are `verifiers/verify_skill_checklist.py` (the three admitted shapes: fix line, `self_test()` arms, the one corrections row) and `verifiers/check_tip_battery.py` (`INSTRUMENT_PINS` block only). Docstring, `GOVERNANCE_CORRECTIONS_HORIZON`, `LOG.md`, SKILL.md, corpus files, and the two frozen corpus verifiers untouched (frozen conjuncts in the counter re-verify the latter).

### Non-blocking observations

- The arm set is a subset of the counter's frozen truth table (no dangling-dash / `30-40-50` / leading-punct arm); acceptable — the counter owns the full table, the arms own the kill.
- Pre-existing dressing quirks (unchanged by the patch, confirmed identical at base): `.` is not trailing punct so `:42.` stays refused, and a whole trailing punct-run including `:` strips to the bare path (`x.md:,` → `x.md`).
- `skills.mdx:137,142` (SKILL.md:190) now normalises to `skills.mdx` — inert today on every evaluated surface (not a citation subject: no `CITATION_ROOTS` prefix; not a fenced argument), but it is a latent semantic change: if that token is ever cited in a live position it will be tested as `skills.mdx` (absent at the repo root → still red, anchor no longer part of the path). This is the intended "anchors do not change the path" semantics; recorded for the frontier, not a defect.

## Residual risk / verification gaps

- The gate-GREEN authority is the counter's fleet-shaped sandbox; my clone-local gate run is environment-red by construction (`../`-hops and clone-dir name) and was used only for the same-environment base↔candidate diff — the counter's GREEN at the candidate is the scored reading.
- One counter run consumed (candidate); no second run needed — no discrepancy to adjudicate.
- Reviewer's verdict is a recommendation: I do not edit, judge, integrate, or ship; the L1 lands after the wave.

## Receipts (all under `.ufo/waves/round-100/w1/ReviewerAnchorR100/`)

- `counter-candidate.txt` — frozen `anchor-lists.py` on my candidate `7145b87e…`: `C2-PREDICATE-MET` rc 0.
- `confinement-check.txt` — mirrored frozen conjuncts (fix line ×1, regions unique, bytes equal outside admitted shapes, rows = base − row 3598 exactly, pins-only battery, blob pinned).
- `regex-battery-cand.txt` — behaviour battery ALL OK on the candidate module.
- `subject-diff.txt`, `gate-base-json.txt`, `gate-cand-json.txt` — evaluated-subject and gate `--json` base↔candidate diffs (only governance.citation_resolves differs, the intended heal).
- `revert-mutant-selftest.txt` — independent on-disk revert run: `8 failure(s) over 1886 assertions`, exactly the comma arms.

Tooling installs: none (stdlib python only; no pacman, no uv, no downloads).

## Evidence log
