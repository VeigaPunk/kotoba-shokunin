# ReviewC1Diff — C1 diff `4c003a4..c2107ecf` on `verifiers/verify_surfaces.py`

Result: MIXED — the declared-admission rule itself holds (counter fresh at 4 of 4, live omp extraction exactly the 8 declared pairs, admission/decoy/planted semantics verified), but the cutover silently disarms `surfaces.no_uncovered_class`'s empty-baseline tripwire (a new 0==0 silent pass, the defect class this module exists to kill), and two comments misstate the admission set.

Scope notes: `verifiers/verify_surfaces.py` is byte-identical at c2107ecf and the judged c8407a4 (`git diff --stat` between the two on this file is empty), so all line numbers below are both the C1 diff hunks and the shipping bytes, cited from my sandbox clone `/fast/scratch/hyaku/kotoba-r52a2/ReviewC1Diff` (checkout c8407a4). All probes were run there; the lane was only read. No tools installed.

## Findings

### MEDIUM — `surfaces.no_uncovered_class` lost its empty-baseline 0==0 tripwire (regression vs pre-C1, unpinned by self-test)

C1 derives extraction from the baseline (`main` hunk: `extract_classes(dumps[h], h, declared_loader_pairs(entries, h) ...)`, shipping lines 1623-1626; admission filter `admitted = {c for c, g, f in calls if (g, f) in declared}` :512, `return {(g, f) for c, g, f in calls if c in admitted}` :513). An empty omp baseline therefore admits nothing and empties `found`. Both guards inside the check are entry-driven and stay silent:

- vacuity arm :826-831 requires `loader_group_declared` non-empty — empty baseline → empty list → silent;
- extractor-blind arm :832-841 iterates `entries` for literals present in the dump — no entries → `blind` empty → silent.

Probe (same bytes, same argv, only the mode differs — sandbox clone):

```
# shipped generic mode
main(["--omp-strings","verifiers/fixtures/surfaces/strings-omp-18.12.6.txt",
      "--opencode-strings",".../strings-opencode-clean.txt",
      "--baseline","verifiers/fixtures/surfaces/baseline-empty.json",
      "--check","surfaces.no_uncovered_class"])
-> exit 0, "PASS surfaces.no_uncovered_class: all 0 extracted loader class(es) declared"
# pre-C1 behavior (extract_classes(..., declared=None), allowlist), identical bytes
-> exit 1, "FAIL ... 8 loader class(es) undeclared in baseline: omp:agents-md/AGENTS.md, ..."
```
Same result reproduced at the shipped CLI (sandbox clone, committed bytes): `python3 -B verifiers/verify_surfaces.py --omp-strings verifiers/fixtures/surfaces/strings-omp-18.12.6.txt --opencode-strings verifiers/fixtures/surfaces/strings-opencode-clean.txt --baseline verifiers/fixtures/surfaces/baseline-empty.json --check surfaces.no_uncovered_class` → `PASS surfaces.no_uncovered_class: all 0 extracted loader class(es) declared`, exit 0.


That 0==0 pass is exactly the defect class the module documents as forbidden: module docstring :133-135 "An empty baseline therefore FAILs naming every extracted opencode class instead of passing on 0==0" (opencode keeps that property; omp lost it in this hunk), and `check_table_parity` :876-878 "vacuous parity is not a pass". The in-repo fixture `verifiers/fixtures/surfaces/baseline-empty.json` is precisely such a degenerate baseline, and `--check surfaces.no_uncovered_class` alone (or with `literal_present`, which then reports "0 loader-kind entries verified" and passes) reproduces it; a full default run still fails via `table_parity` (41 extra inventory rows), which is why nothing shipped goes red today. The self-test's only empty-baseline arm (h), shipping :1427-1441, uses the dead `strings-empty.txt` + `inventory-empty.md` and pins only `table_parity`/`literal_parity` — the "live dump + empty baseline + no_uncovered_class" case is unpinned (self-test is green at 0/129 while the probe passes silently).

Trigger needs a degenerate or tampered baseline, and the frozen counter uses the real baseline, so C1's stated claim is unaffected — but this is a defense-in-depth regression introduced by the diff, so it must be fixed (e.g., fail when the dump yields registration-shaped calls but the omp admission set is empty, independent of entries) and pinned.

### LOW — headline comment and docstring misstate the admission set ("loader-group")

- Comment :223-224: "a callee is ADMITTED when at least one of its call sites registers a (group, file) pair the baseline declares for omp as `loader-group`".
- `extract_classes` docstring :472: "omp with ``declared`` (the baseline's omp loader-group pairs)".

Actual: `declared_loader_pairs` :516-529 takes every baseline omp class id whatever its `context_kind` (its own docstring :518-523 correctly explains the rekind-laundering rationale). Measured on the shipped baseline: 33 of 33 omp pairs are admitted, only 8 are loader-group; 25 pairs (e.g. `omp:clinerules/.clinerules`, `omp:codex/AGENTS.md`) enter admission via doc/prompt-text/etc. rows. The behavior is correct per the round's design (kind-dependence would reopen the rekind hole); the two comments are false and contradict the function they describe. A maintainer trusting :223-224/:472 would "fix" `declared_loader_pairs` back to loader-group-only and silently reintroduce the laundering bypass that self-test arms rekind-doc/rekind-partial pin.

### LOW — ":231 loud, never silent" overclaims for the check it names; member-call lookbehind makes partial invisibility reachable

- `OMP_GENERIC_CALL_RE` lookbehind :235 `(?<![A-Za-z0-9_$.])` excludes a preceding `.`, so a namespaced call `o.Kl(u, "gemini", "GEMINI.md")` matches nothing. The retained allowlist `OMP_CALL_RE` :212 has `(?<![A-Za-z0-9_$])` (no dot) and does match it. Probe: allowlist mode extracts `('gemini','GEMINI.md')` from that line; generic mode extracts nothing. The exclusion is the right call for a minified bundle (a `o.Kl(` is a property access, not the free registration binding; Q18 control pins it) — but it means callee-side shape changes are invisible to the rule the comment says only argument-side shape changes defeat.
- Partial invisibility is silent inside `no_uncovered_class` itself: namespacing only `bq` in the 18.12.6 fixture (2 of 8 pairs vanish) leaves `pairs` non-empty, so vacuity :826 and the blind arm :832 (gated on `not pairs`) both stay silent — probe extracts 6 of 8 with no problem string from that check. It is caught loudly only by the sibling check `literal_present` (:780-786 per-row probe; probe exit 1 naming both pairs) — which the counter does run, but the comment attributes the loudness to "the vacuity guard".
- Worst sub-case, unpinned: a rebuild that namespaces the callee AND registers a new pair through it is fully silent — the new pair is undeclared (so `literal_present` never probes it) and unextracted (so `no_uncovered_class` never names it). The frozen counter's fixtures pin only pure renames, not callee-namespacing.
- Mitigating evidence: on all three committed omp fixtures the two modes extract identical sets (probe: `generic=8 allowlist=8 equal=True`, `generic=8 allowlist=8 equal=True`, `generic=2 allowlist=2 equal=True`), and on the live omp binary the new rule extracts exactly the 8 declared pairs (`--json` substrate run, `no_uncovered_class` PASS "all 8 extracted loader class(es) declared"). No live shrink today.

### INFO — "declared=None callers" (:232-233) is an empty production set; mode plumbing is otherwise sound

No production caller passes `declared=None` for omp: the only call site is `main` :1623-1626 (omp gets `declared_loader_pairs`, opencode gets None and uses `CALL_RE`). Allowlist mode's remaining users are exactly the self-test historical arms named in the same sentence. `OMP_CALLEE_MODE` :239 is read at call time (:483-485); `run_capture` :1031-1034 runs `main` in-process, so the self-test's mutations do reach the code under test, and both arms restore in `finally` (:1136-1138, :1193-1196). No leak found. Minor wording fix suggested only.

### INFO — over-admission can only fail loud (no action)

All-kind admission widens the decoy-admission surface (a callee registering any of the 33 declared pairs is admitted and all its `.md` registrations surface). That direction can produce false FAILs (loud, by design "surfaces as an undeclared class") and can never hide a pair; rekind-laundering stays covered. No defect.

## Holds (verified, not taken on faith)

- Counter at the judged rev: `python3 -B verifiers/check_callee_rename.py --rev c8407a45...` → `callee-rename robust 4 of 4 fixtures`, exit 0 (default seed; the `--seed 7`/`--seed 1234` passes are the L1's claim, not re-run here). The counter drives the gate via subprocess CLI with `--check surfaces.literal_present --check surfaces.no_uncovered_class` (check_callee_rename.py :17, :130-133), so it measures the shipped declared mode; the script is unchanged since the plan commit (empty diff `4c003a4..c8407a4` on it).
- Self-test: `0 failure(s) over 129 assertions`, exit 0; floors-registry `surfaces` 119 → 129 matches (diff verified); `check_assertion_floors.py:156` row agrees.
- Admission semantics independently reproduced: decoy `q(u,"evil","EVIL.md")` stays out; a planted `Yq(u,"newgroup","NEWFILE.md")` by a renamed admitted callee surfaces; member call not matched; wrapper nesting `await R(Ho(u, ...))` in the fixture parses correctly (outer `R(` cannot match the argument shape).
- The silent `if m:` skip at :528-529 in `declared_loader_pairs` is unreachable from the CLI: `load_baseline` validates every class_id against `CLASS_ID_RE` and the harness prefix and raises otherwise (:346-356).

## Environment observation (not a defect of this diff — route to L1)

The live opencode substrate moved mid-round, so two plan no-harm guards do not currently reproduce: pinned path `/home/vgpnk/.opencode/bin/opencode` does not exist; `opencode` on PATH is `1.19.4` at `/home/vgpnk/.local/bin/opencode`; verify_surfaces resolved a 214,522,032-byte npx-cache `opencode.exe` with mtime 2026-10-22T17:50:30Z (after attempt 1 died at 17:26Z). Consequence, measured at c8407a4: `verify_surfaces.py --json` → pass 6 / fail 1 / exit 1 (`surfaces.opencode_extract` FAIL: OC-4 and OC-6 anchors missing; omp half fully green, 42 entries + 8/8 declared), and `check_substrate_pins.py` → `DRIFT 1/3 pins failed: opencode_binary_sha256`, true exit 1. Zero attribution to the C1 change (it is data drift, and the omp pin still matches); the C2 `--fetch` and any opencode no-harm claim measured before 17:50Z will not re-measure green until the substrate is restored or re-pinned.

## Post-review lane observation (2026-10-22, read-only `git status`/`diff` on the lane)

The lane working tree at HEAD c8407a4 now shows uncommitted modifications to 10 files (`PROVINCE.md`, `SCORECARD.md`, `SKILL.md`, `corpus/QUALITY.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/knowledge/mcp-server-instructions-round52.md`, `corpus/lessons/round-52.md`, `verifiers/check_correction_sweep.py`, `verifiers/verify_surfaces.py`) — the context's record of "one uncommitted file (SCORECARD.md)" from attempt 1 is stale; attempt-2 falsify repairs are visibly landing uncommitted (the tree diff of `verify_surfaces.py` is labeled "(round 52 falsify, CriticC1Escape P4)"; SCORECARD's coverage row cites S041/S042 and a 7-of-7 re-measure on "the attempt-2 corrections commit"). Lane facts for L1:

1. **The tree patch widens admission but does not close the MEDIUM defect.** Working-tree `verify_surfaces.py` :509-518 now admits also `g.startswith("<unresolved-var:") and f in declared_files` — any callee whose call has an unresolved group and a declared FILE gets admitted, so a decoy `q(u, VAR_UNRESOLVED, "AGENTS.md")` pulls q's whole registration set into extraction (loud over-extraction, acceptable) — but the empty-baseline 0==0 pass of the MEDIUM finding is untouched: an empty admission set still extracts nothing and every guard inside `check_no_uncovered_class` stays silent.
2. **All reviewer citations above are the COMMITTED bytes c2107ecf == c8407a4** (sandbox clone; `diff --stat c2107ecf c8407a4` on this file is empty). If the uncommitted tree lands as the corrections commit, re-run the P3 empty-baseline probe and re-check the :223-224 / :472 comment falsifications before closing MEDIUM/LOW-1.
## Residual risk and verification gaps

- `--seed 7` and `--seed 1234` counter variants not re-run by this seat.
- The MEDIUM defect's fix is L1's to make; until then `no_uncovered_class` alone must not be treated as a standalone tripwire against a degenerate baseline.
- Callee-namespacing escape (LOW, last sub-case) is not covered by any pinned fixture; a fixture pinning it would close the gap the comment's loudness claim leaves open.
- I did not re-open the C2 sources or the SCORECARD working-tree diff (out of scope for this seat).
