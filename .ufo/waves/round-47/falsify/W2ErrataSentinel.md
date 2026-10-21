verdict: PARTIAL — the default CLI keeps the sole LOG.md:2111 waiver narrow, but the Python checker API accepts caller-supplied waivers and the horizon is co-editable

## Findings

### LOW — Caller-supplied `errata` can waive any dead LOG citation outside the CLI

**Evidence at 7ad7fad:** `verifiers/verify_skill_checklist.py:1545-1547` exposes `errata` and `horizon` as caller-controlled parameters. `:1526-1541` validates only the supplied rows (line bound, byte hash, substring, subject on LOG, path still dead); it does not require the row to equal the module's `GOVERNANCE_ERRATA`. `:2400-2401` is the production CLI call and supplies only `repo`, so that path uses the module defaults. The checker’s default registry is the one row at `:377-383`, pinning `LOG.md:2111`.

**Repro:** In an isolated temporary repo, I made `LOG.md` line 2 be `- \`corpus/gone.md\` replay failed: runner missing`, kept a resolving `corpus/live.md` citation so the check was non-vacuous, and left `corpus/gone.md` absent. With `row = (2, sha256(line), "corpus/gone.md", "runner missing")`, the in-memory call `check_governance_citations(repo, errata=(row,), horizon=2)` returned `PASS` and counted one recorded absence; without that row the dead citation failed. This requires no verifier-file diff, but it does require a caller to bypass the CLI and deliberately invoke the Python helper with overrides. Repository search found the CLI as the only live source caller using the default; the other calls are the helper’s self-tests or historical artifacts.

**Impact:** A downstream importer that treats this function as a trusted gate can inject an arbitrary LOG waiver. I found no such active in-repo production caller, so this is an API-contract risk, not a demonstrated bypass of the current CLI.

**Smallest remediation:** Keep the production checker entry point fixed to module-owned policy; move override-based fixture tests behind a separate internal test helper rather than exposing waiver and horizon overrides on the checker used as a gate.

### LOW / policy observation — Horizon is both a line-count cap and a manually editable constant

**Evidence at 7ad7fad:** `verifiers/verify_skill_checklist.py:377` sets `GOVERNANCE_ERRATA_HORIZON = 2315`. At `:1528`, a row must satisfy `1 <= line <= min(horizon, len(log_lines))`. Thus an erratum cannot point past the current LOG, but the active ceiling is not derived from its line count: at the landed state `LOG.md` has 2326 lines and the default ceiling remains 2315. The row table and ceiling are in the verifier itself, with no separate pinned horizon check found in this surface.

**Mutation repro in the canonical-layout scratch clone:** I appended an absent citation at `LOG.md:2327`, added a row containing its exact line SHA-256/token/absence text, and changed the cloned horizon to 2327. The ordinary CLI then returned PASS and reported `2 recorded absence(s) excused`. Using only the original row returned FAIL naming `LOG.md:2327`; using the added row with horizon 2315 also returned FAIL (`past horizon 2315`). The changed clone was committed as `2bab4b4` (`test(falsify): reproduce governance errata extension`). No production verifier or LOG file was changed.

**Conclusion:** The default checker does not silently gain a new exception from a LOG/SCORECARD-only change; widening the default policy requires a visible verifier diff adding a row and, for later lines, changing the constant. A reviewer can catch that diff, but the mechanism does not independently prevent an author from co-editing its own horizon and registry in one commit.

**Smallest remediation:** If the horizon is meant to be immutable history, validate it against an independently maintained/pinned baseline rather than relying on a constant in the same verifier as the errata table. The current `min(...)` guard should remain to reject nonexistent LOG lines.

### INFO — SCORECARD.md citations are not excused by a matching LOG erratum

**Evidence at 7ad7fad:** `verifiers/verify_skill_checklist.py:1524-1525` builds the erratum subject set from `source == "LOG.md"`; `:1572-1573` removes only matching LOG subjects. I tested a live, exact erratum row for a dead token in LOG plus the same dead token in `SCORECARD.md`; the result remained FAIL and named `SCORECARD.md:2`. This confirms the row cannot excuse SCORECARD subjects, even when its token is duplicated there.

**Smallest remediation:** None indicated; retain this source-specific filtering.

## Commands and evidence

All commands ran in the isolated clone at `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2ErrataSentinel-2/kotoba-shokunin`, initially detached at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.

- `python3 verifiers/verify_skill_checklist.py --self-test` at the landed snapshot: **exit 0**, `0 failure(s) over 1845 assertions`.
- `python3 verifiers/verify_skill_checklist.py --check governance.citation_resolves` at the landed snapshot: **exit 0**, PASS, evaluated 848, `1 recorded absence(s) excused`.
- On the first cloned mutation attempt, the test row used a digest that omitted the `- ` list marker; the checker correctly returned **exit 1** with `line text drifted`. After hashing the full line bytes, the cloned mutation command `python3 verifiers/verify_skill_checklist.py --check governance.citation_resolves` returned **exit 0**, PASS, evaluated 848, `2 recorded absence(s) excused`.
- `python3 verifiers/verify_skill_checklist.py --self-test` after the clone mutation: **exit 0**, `0 failure(s) over 1845 assertions`.
- The focused in-memory Python harness (not a shell command) asserted: new LOG citation without the added row → FAIL at line 2327; added row with old horizon → FAIL at horizon 2315; expanded horizon plus row → PASS; exact LOG erratum plus duplicated dead SCORECARD token → FAIL at `SCORECARD.md:2`. All four assertions passed.

## Not checked

I did not re-run C1 substrate/pin measurements, C2 XML-trigger checks, corpus integrity/independent gates, the fault-injection harness, or the broader round-47 frontier/source claims. I did not assess whether the historical absence statement at `LOG.md:2111` is substantively true beyond the landed row’s byte/hash/subject behavior.