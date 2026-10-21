verdict: PARTIAL — GOVERNANCE_ERRATA (LOG.md:2111 pin, horizon 2315) at 7ad7fad: the required stale and one-byte drift mutations fail as specified; the landing record's "governance evaluated 804" is refuted (gate says 848), a non-UTF-8 byte breaks the documented exit taxonomy, and the pin's hash convention is undocumented.

# W2ErrataRestore — GOVERNANCE_ERRATA falsification at 7ad7fad

Lane: KotobaR47-2.W2ErrataRestore-2 (leaf). Target commit 7ad7fadfc09354b74fb66605dfb0c1182c115a2f. Production repo was read-only to me; all mutations ran in a canonical-layout clone (`/fast/scratch/kotoba-r47/w2/W2ErrataRestore/kotoba-shokunin`) or scratch probe trees (`/fast/scratch/kotoba-r47/w2/W2ErrataBase`, `/fast/scratch/kotoba-r47/w2/W2ErrataProbe`). Artifacts: `.ufo/waves/round-47/falsify/W2ErrataRestore.*`.

## 1. Required test outcomes (Work section)

Clone HEAD after my commits is `2e6e5c1`; `git diff --stat 7ad7fad 2e6e5c1` is empty, so the net tree equals 7ad7fad.

| Step | State | Command | Exit | Governance detail (verbatim) |
|---|---|---|---|---|
| 0 baseline | 7ad7fad, clean | `python3 verifiers/verify_skill_checklist.py` | 0 | `PASS governance.citation_resolves: evaluated 848 — 848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused` (11 PASS lines) |
| 1 stale | stub at `.ufo/round-45/drafts/v10/post-r44-hunt.py`, uncommitted | same | **1** | `FAIL governance.citation_resolves: evaluated 849 — erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py': stale, the path now resolves; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 0 recorded absence(s) excused` |
| 1b stale, committed | stub in commit `d68eae3` | same (default run only) | **1** | identical detail |
| 1c stub removed | commit `2e6e5c1` | same | 0 | `PASS … evaluated 848 … 1 recorded absence(s) excused` |
| 2 drift | one byte: LOG.md:2111 `19:38:15Z` → `19:38:16Z` (edit tool) | same | **1** | `FAIL governance.citation_resolves: evaluated 849 — erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py': line text drifted; LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve from /fast/scratch/kotoba-r47/w2/W2ErrataRestore/kotoba-shokunin; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 0 recorded absence(s) excused` |
| 2 json | same | `--json` | 1 | `exit_code` 1, `pass` 10, `fail` 1, `na` 0 |
| 2 control | `git checkout -- LOG.md` | same | 0 | `PASS … 1 recorded absence(s) excused`; LOG.md byte-identical to pre-edit HEAD |

Byte proof: `cmp -l` of `git show HEAD:LOG.md` against the edited file reports exactly one differing byte, offset 359172 (1-based), octal 065 → 066 (`5` → `6`). Both files are 430190 bytes; `git diff --numstat` is `1 1 LOG.md`. Post-edit line sha256 is `496a1179f5b0a3254c46f3dfbb7477cfa2db641d1bfa225d0ac41e2685bc1ab1`, not the pin `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135`.

Restore provenance: no original runner can be restored. `git log --all -- .ufo/round-45/drafts/v10/post-r44-hunt.py` returns no commits (rc 0). A search of `/home/vgpnk/Projects/shokunin` and `/fast/scratch/kotoba-r47` at depth ≤ 7 finds no `post-r44-hunt.py` (rc 0, empty). The file restored for the test is a 5-line, 284-byte stub. The gate only tests existence (`safe_resolve`, `verifiers/verify_skill_checklist.py:886–905`, `exists()`), so content cannot change the verdict. The runner's result JSON does exist: `.ufo/round-45/evidence/v10-post-r44-hunt.json`.

## 2. Findings

### F1 — calibration (landing record refuted): LOG.md:2323 says "governance evaluated 804"; the landed gate evaluates 848
- Record: `LOG.md:2323` — "Checklist `--json` exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (governance evaluated 804, 1 recorded absence excused)".
- Re-run at 7ad7fad: default rc 0 with 11 PASS; `--check governance.citation_resolves` rc 0 with `evaluated 848`. The 11/11 and exit 0 claims reproduce; the 804 does not.
- Decomposition (the verifier's own `citation_subjects`, imported read-only): raw subjects at HEAD = 849 (LOG 622 + SCORECARD 227). Minus 1 excused = 848 (`verifiers/verify_skill_checklist.py:1572–1574`). At BASE c61a973, raw = 805 (LOG 589 + SCORECARD 216). The landing added 33 LOG subjects (LOG.md:2319–2326) and 11 SCORECARD subjects (`git diff --numstat c61a973 7ad7fad`: LOG +11/−0, SCORECARD +7/−3).
- 804 = 805 − 1, which is the sentinel's pre-implementation prediction: `.ufo/waves/round-47/build/C3SentinelErrata.md:37` — "expected … raw candidates 805, one registered exception, 804 remaining checked". `[INFERENCE]` the record copied that prediction rather than re-measuring after the landing's own citations were added; I observed no commit that produces 804 (BASE 805, HEAD 848).
- Verdicts are unaffected; the record number is wrong. A correction belongs in an append-only LOG entry, not an edit of line 2323.

### F2 — operability (exit taxonomy violated): a non-UTF-8 byte in a governed or target file aborts with a traceback
- Repro (probe tree at 7ad7fad): append `b"\xff\n"` to `LOG.md` → rc 1, stdout 0 bytes, last stderr line `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 430190: invalid start byte`. Same with `b"\xff"` appended to `SKILL.md` → rc 1, stdout 0 bytes, `… position 35017`.
- Cause: `read_text` (`verifiers/verify_skill_checklist.py:427–432`) and the governance read (`:1556–1558`) catch `OSError` only. `EnvError` is documented as exit 2 (`:415–416`) and returned as 2 (`:2359`, `:2368`). A decode error instead exits 1 — the same code as a governance FAIL (`:2413`) — and prints nothing, because verdict lines print only after the loop (`:2417–2419`).
- Fail-closed, so not a bypass. Severity: operability.

### F3 — operability / calibration: the pin's hash convention is undocumented, and the obvious re-derivation disagrees with the pin
- The gate hashes each line's text without its terminator (`splitlines()` at `:1557`, hash at `:1532`) → `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135`, matching the pin.
- `sed -n '2111p' LOG.md | sha256sum` → `d7b4c6289e30ad0d9c23554c066742802d5c325f9bea9929dce5fa717d981c7a` (includes the newline). The comment (`:373–376`) and docstring (`:192–195`) say only "line sha256" / "matches the row's SHA-256". An operator re-deriving the pin the obvious way concludes it is wrong.

### F4 — operability, latent: line numbers come from `str.splitlines()`, not `\n`
- Probe P2: a single U+2028 replacing blank LOG.md line 2 → rc 1, `FAIL … erratum LOG.md:2111 …: line text drifted; LOG.md:2112: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve …`. The `\n`-numbered line 2111 is unchanged (checked: `split('\n')[2110]` equal), so the message says "drifted" and names the subject on a different line.
- `LOG.md` and `SCORECARD.md` contain zero of U+2028, U+2029, U+0085, U+000B, U+000C, U+001C–U+001E (counted). Latent today.

### F5 — calibration: the pin covers content, not the terminator
- Probe P4: CRLF added to pinned line 2111 only (+1 byte) → rc 0, `PASS … 848 … 1 recorded absence(s) excused`. The comment at `verifiers/verify_skill_checklist.py:375` says "must match its line byte-for-byte", which overstates the check.

### F6 — calibration boundary (by design): same-line double quotes exempt a dead citation with no pin or horizon
- Probe P3a: a new final LOG line `"`corpus/gone-quoted.md` exited 2: runner absent"` → rc 0, `10 quoted meta-finding(s)` (up from 9), PASS.
- Probe P3b: the same line without quotes → rc 1, `FAIL … LOG.md:2327: 'corpus/gone-unquoted.md' does not resolve …`.
- Exemption: `:1467` (`quoted`), `:1484–1486` (exclusion), documented at `:236–241`. The errata is bounded by horizon, hash, and still-dead test (`:239–241`); the quote exemption is bounded only by its counter.

### F7 — calibration (wording): "at or below the horizon" versus the implemented `line <= horizon`
- Docs: `verifiers/verify_skill_checklist.py:193` and `:374` say "at or below the horizon". Code: `:1528` `1 <= line <= min(horizon, len(log_lines))`. In file order "below" reads as "after 2315", the opposite of the rule. Boundary checked: horizon 2111 → PASS (inclusive); horizon 2110 → `is past horizon 2110 or absent`.

### F8 — coverage (informational): LOG.md:2111 claims three runners exited 2; the gate sees one
- Only `.ufo/round-45/drafts/v10/post-r44-hunt.py` is a backticked `.ufo/` token on that line. The V10 replay commands and the R41 draft references are described in `.ufo/round-46/scouts/U1.md:15` and `:17`, which are outside `GOVERNANCE_FILES` (`verifiers/verify_skill_checklist.py:371`).

### F9 — freshness (HOLDS): the excused absence is still true
- `.ufo/round-45/drafts/` is absent in the clone and in production; no `post-r44-hunt.py` at depth ≤ 7. The pinned sentence still describes the tree.
- Horizon 2315 is the last line of the round-46 landing entry (LOG.md:2315); 2316 is blank and 2317 starts round 47. Round-47 lines 2319–2326 all resolve, so no new excusal is needed.

### F10 — mechanism (HOLDS): errata logic on the real LOG, probed by import without file edits
- As shipped: PASS, evaluated 848, 1 excused.
- `errata=()`: FAIL, evaluated 849, `LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve …`. The row is load-bearing.
- Zero SHA: FAIL with `line text drifted` plus the unresolved subject. Wrong token: FAIL with `names no subject on the line` plus the unresolved subject.
- Logic: `errata_problems` at `verifiers/verify_skill_checklist.py:1519–1542`; `check_governance_citations` at `:1545–1597`.

### F11 — mutation testing: each errata branch is caught by the self-test; M1 is also caught by the floors guard
| Mutant (probe tree) | Self-test (pristine rc 0, 0 failures / 1845) | Assertion that caught it | Effect on the real repo state |
|---|---|---|---|
| M1 stale branch → `elif False` (`:1538`) | rc 1, 1 failure | `governance: erratum for a restored path is stale` (`:2224–2225`) | Floors guard: `FAIL checklist observed=1845 floor=1845 self_test_failures=1`, rc 1 (pristine `PASS checklist observed=1845 floor=1845`, rc 0; `verifiers/check_assertion_floors.py:144–145`, `:511`). With stub restored and the mutant in place, default gate rc 0 PASS: a bypass if both self-test and floors are skipped. |
| M2 sha check → `if False` (`:1532`) | rc 1, 1 failure | `governance: erratum line drift fails closed` (`:2212`, `:2218`) | With the one-byte drift and the mutant in place, default gate rc 0 PASS: a bypass. Floors guard not run for M2 — `[INFERENCE]` it behaves like M1. |
| M3 horizon `min(horizon, len) − 1` (`:1528`) | rc 1, 6 failures | includes `governance: pinned recorded absence is excused and counted` (`:2201`) | n/a |
| M4 subject check → `elif False` (`:1536`) | rc 1, 1 failure | `governance: erratum no subject fails closed` (`:2214–2218`) | n/a |

Operability note: the default gate does not run its own self-test (`--self-test` is a separate mode). The stale and sha branches are protected by the self-test and floors pair, not by the gate's own run. This is defence in depth, not a defect.

## 3. Commands and exit codes

Clone: `/fast/scratch/kotoba-r47/w2/W2ErrataRestore/kotoba-shokunin`. Interpreter: `python3` (3.14 per the traceback path).

1. `git clone -q --no-hardlinks … && git checkout -q --detach 7ad7fad…` → rc 0.
2. `python3 verifiers/verify_skill_checklist.py` → rc 0 (11 PASS). `--check governance.citation_resolves` → rc 0. `--json` → rc 0. `--self-test` → rc 0, `0 failure(s) over 1845 assertions`.
3. `sed -n '2111p' LOG.md | sha256sum` → `d7b4c628…` (rc 0). Terminator-free line hash via `splitlines()` → `7dcbf123…` (matches pin).
4. `git log --all -- .ufo/round-45/drafts/v10/post-r44-hunt.py` → rc 0, no output.
5. `find /home/vgpnk/Projects/shokunin /fast/scratch/kotoba-r47 -maxdepth 7 -name 'post-r44-hunt.py'` → rc 0, no output.
6. `timeout 120 find … -name '*r44-hunt*'` (unbounded depth) → rc 124 (timed out). It found only `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/round-45/evidence/v10-post-r44-hunt.json`.
7. Stub written (`write`, uncommitted): default rc 1 (stale), governance-only rc 1, `--json` rc 1. Committed as `d68eae3`: default rc 1.
8. `git rm` + commit `2e6e5c1`; default gate rc 0 (PASS, 848, 1 excused).
9. One-byte edit (`edit`, LOG.md:2111); `cmp` vs HEAD rc 1 (single byte, offset 359172); `git diff --numstat` `1 1 LOG.md`; default gate rc 1 (drift); `--json` rc 1 (`exit_code` 1, pass 10, fail 1).
10. `git diff > …drift.patch`; `git checkout -- LOG.md` rc 0; default gate rc 0; `cmp` with pre-edit copy rc 0.
11. BASE c61a973 in a canonical clone (`/fast/scratch/kotoba-r47/w2/W2ErrataBase`): default gate rc 1; `FAIL governance.citation_resolves: evaluated 805 — LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve from …; 9 quoted meta-finding(s), 3 schematic token(s) excluded`; 9 PASS lines. This matches `.ufo/waves/round-47/before/SUMMARY.md` ("9 PASS/1 FAIL … LOG.md:2111").
12. Raw subject counts by import of `citation_subjects` (read-only): HEAD LOG 622 / SCORECARD 227; BASE LOG 589 / SCORECARD 216.
13. Errata probes by import (`check_governance_citations(errata=…, horizon=…)`, no file edits): as shipped PASS 848/1; `errata=()` FAIL 849; horizon 2110 FAIL; horizon 2111 PASS; zero SHA FAIL (`line text drifted`); wrong token FAIL (`names no subject on the line`).
14. Probe tree P0–P5 (`W2ErrataRestore.probes.txt`): P0 rc 0; P1 rc 1; P2 rc 1; P3a rc 0; P3b rc 1; P4 rc 0; P5 rc 1. Probe LOG restored byte-identical after each step.
15. Mutants M1–M4 (`W2ErrataRestore.mutants.txt`): self-test rc 1 each; real-state M1 rc 0 and M2 rc 0 (see F11).
16. Floors guard in the probe tree (`W2ErrataRestore.floors.txt`): pristine rc 0 (102 s); M1 rc 1 (100 s). Verifier restored byte-identical.
17. `grep -n '804' LOG.md SCORECARD.md PROVINCE.md plans/round-47.md` — the only governance count is LOG.md:2323.

## 4. Not checked
- Other C1/C2/C3 items and frontier (corpus/README index rows, corpus-baseline 58→60, fault-harness planter fix, S012–S015, Q19, M20–M22). These belong to sibling lanes. I only saw the checklist, the floors guard, and the before/after SUMMARY lines.
- Exit codes of the corpus integrity, corpus independent, fault-harness, surfaces and pins gates. Not run by me, except the floors guard in the probe tree.
- Production `LOG.md` and `SCORECARD.md` were not diffed against 7ad7fad. Every LOG/SCORECARD reading came from the 7ad7fad clone; the production working copy was not written.
- The original runner's content was not recovered. Its only trace is the result JSON, which I did not parse.
- Unbounded filesystem search for the runner (timed out at 120 s). The search was depth-limited to 7.
- CRLF and lone-CR line breaks on lines other than 2111. Separator characters beyond the 8 counted.
- `--json` on the decode-error path (not run; same code path `[INFERENCE]`).
- Floors guard run for M2 (not run; same path as M1 `[INFERENCE]`).
- Frozen substrates under `/fast/scratch/kotoba-r47/shared/` (outside this target).
- labrat probe: not dispatched (no spawn tool in this lane; not needed for this target).

## 5. Tools
None installed or upgraded. Used the existing `git`, `python3`, `find`, `grep`, `cmp`, `sha256sum`, `timeout`.

## 6. Artifacts (`.ufo/waves/round-47/falsify/`)
- Baseline 7ad7fad: `W2ErrataRestore.baseline.txt`, `.baseline.json`, `.baseline.governance.txt`.
- BASE c61a973: `W2ErrataRestore.base-c61a973.txt`.
- Stale: `W2ErrataRestore.stale.txt`, `.stale.json`, `.stale.governance.txt`, `.stale-committed.txt`, `.stale.patch`.
- Removed: `W2ErrataRestore.restored-removed.txt`.
- Drift: `W2ErrataRestore.drift.txt`, `.drift.json`, `.drift.patch`, `.drift-reverted.txt`.
- Probes: `W2ErrataRestore.probes.txt`, `W2ErrataRestore.probe-nonutf8.stderr.txt`.
- Mutants and floors: `W2ErrataRestore.mutants.txt`, `W2ErrataRestore.floors.txt`.
