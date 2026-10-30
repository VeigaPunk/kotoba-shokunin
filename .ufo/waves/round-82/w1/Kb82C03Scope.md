# Kb82C03Scope — claim-headline audit (C1 freshness / C2 operability)

Seat: critic, leaf member. Base: `47dbe8781657de563ff867caca6244d28e3db504`; freeze commit `006a834` (receipts + plan only, no production bytes). Judged axes: freshness, operability. Method: headline/premise audit against local evidence; no production after-data; only gate self-tests and the named before-command were run (both authorized).

## Audit result

**Both claim headlines are supported by local evidence. Two defects found: one factual imprecision in the lowest-axis premise (minor, fixable), one bounded headline overreach in the C2 "hermetic" framing (fixable by a scoping sentence). No judge-blocking tradeoff identified.**

### C1 — "host-bound documentary loader parity, not exhaustive discovery" — SUPPORTED

- The counter `verifiers/check_substrate_repin_v2.py` is the unchanged round-72 counter: `git log --follow` shows exactly one touching commit, `30d27da` (round-72 freeze 2). The docstring freezes the predicate sentence and pins `BASE_REV`, `PINS_TOTAL=3`, `CHECKS_TOTAL=7` (lines 124-127) and `FROZEN_REMOVALS` (3 classes, lines 138-149) in-file, never read from the measured revision.
- Documentary parity, not discovery: the surfaces half is `verify_surfaces.py`, whose 7 checks are `check_literal_present`, `check_no_uncovered_class`, `check_table_parity`, `check_literal_parity`, `check_opencode_extract`, `check_kind_parity`, `check_excluded_reason` — all comparisons of the tree's documented loader classes/literals against `strings -n 4` dumps of the installed binaries. Nothing enumerates unpinned surfaces, nothing executes the binary, nothing measures prompt behavior. The headline's two negations ("not exhaustive discovery", "not prompt effectiveness") match the counter's semantics exactly.
- Host-bound: the counter reads the live host binaries (`~/.local/bin/omp`, `~/.opencode/bin/opencode`) and reports measured sha256/bytes on its own second line; it extracts the measured revision's own `verifiers/`+`corpus/` and runs that tree's gates with no path flag (explicit trust boundary, per docstring P/S/K).
- Before-state verified from committed receipts: `receipts/before-pins.txt` = 1 PASS / 2 UNREADABLE, exit 2 (missing `~/.local/bin/omp.real`); `receipts/before-c1-counter.txt` = exit 2 "cannot evaluate" (do-nothing misses the 3/3,7/7,3/3 target).
- Installed-substrate premise verified live: `/home/vgpnk/.local/bin/omp` is an ELF 64-bit x86-64, `omp/18.14.0`, sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`.
- Removal ledger: `verifiers/census-removals.json` at base carries exactly the 3 frozen classes (`opencode:instructions/CONTEXT.md`, `opencode:instructions/CLAUDE.md`, `opencode:claude-home/CLAUDE.md`); `corpus/SOURCES.md` tops out at S250, so the plan's "S251 reserved, opened this round" is a consistent reservation, not a provenance collision.
- Self-test (authorized control): `check_substrate_repin_v2.py --self-test` → `0 failure(s) over 16 assertions`, exit 0; 13 shortcut worlds discriminate (satisfying green ×3, stale mtime red, surfaces red, present-literal-ledgered red, absent-class-unledgered red, re-verdicted class red, extra pin row red, extra check red, bad ledger exit 2, missing gate exit 2, pinned-bytes-not-live red, empty report exit 2) — covering the plan's listed shortcut worlds (unchanged tree, path-only/stub, pin-only, removed class, changed live bytes).

### C2 — "operability, not calibration" — SUPPORTED, with one scoping defect

- Defect mechanism confirmed in source: `verify_skill_checklist.py:2521-2529` — the arm `governance: live round-65 corrections land, errata-excused` runs `check_governance_citations(live_repo, …)` with `live_repo = Path(__file__).resolve().parent.parent`, i.e. the live checkout; `GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")` (line 394). The arm is genuinely fixture-in-name-only.
- Before-state reproduced exactly (2026-10-30 run): `1 failure(s)  over 1863 assertions`, exit 1; identical failure detail to `receipts/before-checklist-selftest.txt` (SCORECARD.md:480 `.ufo/wapes`, :482 `corpus/lessons/round-80-verifier-spotcheck.md:30,37`, :484 `.ufo/reports/round-81/kotoba.md` ×2; same exclusion counts 10 quoted / 3 schematic / 2 absences / 4 corrections). Do-nothing control misses the `0 failure(s)` target.
- Live gate independently red: `receipts/before-checklist.txt` shows the public `governance.citation_resolves` FAIL on the same dead subjects — so the plan's "public gate keeps flagging genuinely dead citations" premise is supported, and the repair's required separation (selftest green while live gate stays red) is meaningful, not vacuous.
- "Not calibration" is structurally protected by the plan: the failing arm is to be *replaced by isolated fixture evidence*, "not deleted or remapped to success"; no assertion-count floor reduction (N ≥ 1863); the four required fixture discriminators already exist in the self-test (valid correction green :2490, missing correction red :2497, restored stale target red :2512, unrelated dead subject red :2519).
- S251 note: no SOURCES.md row exists yet; consistent with "opened this round".

## Defects

**D1 (minor, factual — lowest-axis premise).** Plan: "depth remains 9 and consistency/calibration 10." The SCORECARD axis table (measured at base) reads: depth 9; **consistency (calibration sub-axis) 10**; coverage 8.5; operability 8.5; freshness 8; **calibration (advisory) 8.5 — was 8.0**; adjacency 8.0 — was 7.5. The calibration *axis* is 8.5, not 10; only the consistency sub-axis row carries 10. The freshness-at-8 "tied for the lowest non-retired score" half of the premise is accurate (adjacency 8.0 ties it). Smallest safe correction: one phrase — "consistency sub-axis 10, calibration axis 8.5". Impact: freshness/operability axes unaffected; this is a documentation-precision fix, not a predicate change.

**D2 (bounded headline overreach — C2 "hermetic").** Even after the named arm is fixture-replaced, a second live-reading arm remains in the same `--self-test`: `governance: LOG.md:2678 erratum is load-bearing` (`verify_skill_checklist.py:2538-2552`) calls `check_governance_citations(live_repo, …)` twice. Its assertions are robust to *new* dead subjects (it only requires FAIL + the named line 2678 — it stayed green in today's 1-failure run), so the plan's required discriminator "modifying unrelated live governance must not change fixture self-test results" still holds for it, and a future in-place edit of LOG.md:2678 flipping it red is its tamper-detection purpose, not a fixture regression. But strictly, the post-fix selftest is not fully hermetic: "hermetic checklist selftest" overclaims as a universal. Smallest safe correction: one scoping sentence in the plan/claim — hermeticity covers the fixture arms; the load-bearing arm is an intentional live tamper-evidence read pinned to LOG.md:2678/horizon 2678, retained (deleting it would violate "not deleted" and lose the r71-r72 boundary regression). Fixable defect, not a tradeoff the canonical judge must reject.

**Observation (not a defect).** Plan says the failing arm "reads the evolving live SCORECARD"; precisely it reads live LOG.md *and* live SCORECARD.md (GOVERNANCE_FILES). The observed failure is SCORECARD-side; the replacement fixture should isolate both files.

## Causal separability — VERIFIED BOTH DIRECTIONS

- C1 does not run the checklist: `check_substrate_repin_v2.py` references only `check_substrate_pins.py` + `verify_surfaces.py` (+ its own live opencode `strings` pass); grep for "checklist" in the counter: no hits.
- C2 does not read the host extraction gates: `verify_skill_checklist.py` has no reference to `check_substrate_repin_v2.py`, `verify_surfaces.py`, or host binaries (`opencode` hits are citation-root prefixes in docstrings; `~/.local/bin` appears only in a doc example).
- File-level authority is disjoint: C1 authors touch `verify_surfaces.py` / `surfaces-baseline.json` / `baseline.json` / `census-removals.json`; C2 authors touch `verify_skill_checklist.py`. Neither counter's verdict is a function of the other's files.

## Evidence (command-owned, all run 2026-10-30)

| Check | Result |
|---|---|
| `file` + `sha256sum` + `omp --version` on `~/.local/bin/omp` | ELF x86-64, sha256 `e7dd2b60…`, `omp/18.14.0` |
| `git log --follow -- verifiers/check_substrate_repin_v2.py` | single touching commit `30d27da` (r72) |
| `python3 -B verifiers/check_substrate_repin_v2.py --self-test` | `0 failure(s) over 16 assertions`, exit 0 |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` (named before command) | `1 failure(s) over 1863 assertions`, exit 1 — byte-identical failure detail to committed receipt |
| SCORECARD axis table @ base | depth 9, consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0 |
| receipts `before-pins.txt` / `before-c1-counter.txt` / `before-checklist.txt` / `before-checklist-selftest.txt` | match plan's before-narrative |

Full transcripts: `build/Kb82C03Scope-evidence.txt`.

## Impacted axes

- freshness (C1): headline and premise supported; no score implication. D1 touches only the plan's wording of a neighboring axis's score.
- operability (C2): headline supported with D2 scoping; no score implication (plan preclaims no increase).

VERDICT: C1 and C2 claim headlines SUPPORTED by local evidence; causally separable counters CONFIRMED both directions; two fixable defects — D1 "consistency/calibration 10" misstates the calibration axis score (8.5), D2 "hermetic" overclaims while the LOG.md:2678 load-bearing arm stays live — each repaired by one phrase; no universal clause found unsupported beyond these; no judge-blocking tradeoff.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C03Scope.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C03Scope-evidence.txt
