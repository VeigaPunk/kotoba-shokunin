VERDICT: HOLDS-BOUNDED. The floors bump at 59903b26 is complete: registry, both in-file tables, docstring and self-test anchors agree on the 12 live instruments, and each half-bump I ran exits 2 with a named line. Bound: the docstring step of BUMP-IN-STEP is checked by nothing, although the registry `$comment` says a half-bump "fails loudly on the side that was missed" (F1).

# ReviewFloorsBump: round-51 falsify, floors diff at HEAD 59903b26

Scope: `git diff 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10 59903b2637689739a5b9901956301da72d0effe1 -- verifiers/floors-registry.json verifiers/check_assertion_floors.py`, plus the BUMP-IN-STEP rule and the overlap self-test output pattern.
Private clones (all at 59903b2637689739a5b9901956301da72d0effe1, checked with `git rev-parse --short HEAD` = 59903b2): `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewFloorsBump/{lane,probeDoc,probeReg,probeFail}`.
Lane: read-only use only (`git diff`, `git show`, `git clone`). No jj command run. Tools installed or upgraded: none (git, python3, od only).

## Findings

### F1 — LOW (operability): the docstring step is unenforced; the registry comment overstates the guard
- Claim, `verifiers/floors-registry.json` line 2 (`$comment`): "a half-bump now fails loudly on the side that was missed".
- Probe C (docstring text only, `overlap_levers 22` changed to `21` on guard line 8, clone probeDoc): `python3 -B verifiers/check_assertion_floors.py` exit 0; 12 PASS lines, including `PASS overlap_levers observed=22 floor=22`.
- Code check: `_grep` for `__doc__|docstring|BUMP-IN-STEP` over `verifiers/check_assertion_floors.py` finds no code site. Only the registry `$comment` matches.
- Effect: a stale docstring passes silently. Floor gating is intact (registry and tables still cross-check), so this is documentation drift, not a gate bypass.
- Options for the L1: reword the `$comment` so the docstring is named as prose checked by hand; or add an arm requiring each registry `name floor` pair to appear in the docstring (new code, not built here).

### F2 — NIT: indentation of the bumped line
- BASE, `git show 43ca0bfb…:verifiers/floors-registry.json` line 3: ` "instrument_total": 11,` (one space). HEAD line 3: `  "instrument_total": 12,` (two spaces). Line 4 `"instruments"` keeps one space. Valid JSON; style only.

### F3 — NIT: line length
- `verifiers/check_assertion_floors.py` line 874 (the round-51 edit to the harness_independent arm comment) is over 100 columns (`_grep '^.{101,}$'`). Other lines over 100 predate this round (lines 24–35, 197, 340, 453). Style only.

### F4 — note, no action: the new row has no self-test anchor
- `expected_surfaces`, `row_surfaces` and the F6 total anchor now use 115 and 12, and the swaps land exactly once (self-test exit 0). The overlap row has no anchor; neither does `sibling_census`. The registry-side check is generic over every row, so the row is still covered.

## BUMP-IN-STEP, place by place (HEAD 59903b26)

| Place | surfaces 99 to 115 | overlap_levers (new, floor 22) | instrument_total 11 to 12 |
|---|---|---|---|
| registry `verifiers/floors-registry.json` | line 42 `"floor": 115` | lines 37–40, floor 22, path `verifiers/check_overlap_levers.py` | line 3 = 12 |
| `EXPECTED_INSTRUMENTS` | line 132 = 115 | line 140 = 22 | n/a |
| `INSTRUMENTS` | line 154 = 115 (pattern and groups unchanged) | lines 171–172, `(…, 22, r"(?m)^(\d+) failures\n(\d+) assertions$", 2, 1)` | n/a |
| module docstring | line 8 `surfaces 115`, line 10 round-51 note | line 8 `overlap_levers 22`, line 11 round-51 note | n/a |
| self-test anchors | `expected_surfaces`, `row_surfaces` use 115 | none (F4) | F6 swaps `"instrument_total": 12` (line 712) |

Counts (commands): registry entries = 12 (read of the registry: checklist, compare_harness_independent, corpus_independent, corpus_integrity, floors_guard, harness, harness_independent, pins, overlap_levers, surfaces, dispatch_prompts, sibling_census). `EXPECTED_INSTRUMENTS` keys = 12. Docstring floors = 12, each equal to its table value. HEAD guard output has no `size drift` line, and its 12 PASS lines match.

## Probes (private clones; exit codes verbatim)

| id | change (clone) | command | exit | output |
|---|---|---|---|---|
| H1 | none, HEAD | `python3 -B verifiers/check_assertion_floors.py` | 0 | 12 PASS lines; `PASS surfaces observed=115 floor=115`; `PASS overlap_levers observed=22 floor=22` |
| H2 | none, HEAD | `python3 -B verifiers/check_assertion_floors.py --self-test` | 0 | `0 failure(s) over 150 assertions` |
| H3 | none, HEAD | `python3 -B verifiers/check_overlap_levers.py --self-test` | 0 | stdout bytes `0 failures\n22 assertions\n` (`od -c`) |
| A | overlap row deleted from registry only (lane clone) | guard | 2 | `FAIL registry size drift: instrument_total=12 but 11 entries in verifiers/floors-registry.json`; `FAIL registry extra row: overlap_levers (carried by the guard tables, absent from verifiers/floors-registry.json)`; no PASS line |
| B | overlap floor 22 to 21 in both in-file tables, registry untouched (lane clone) | guard | 2 | `FAIL registry floor drift: overlap_levers registry=22 expected=21 row=21`; no PASS line |
| A′ | registry floor 22 to 21 only (probeReg) | guard | 2 | `FAIL registry floor drift: overlap_levers registry=21 expected=22 row=22` |
| C | docstring text only, 22 to 21 (probeDoc) | guard | 0 | 12 PASS, including `PASS overlap_levers observed=22 floor=22` (F1) |
| D | overlap self-test control check forced red (probeFail; the detail text "expected 7 backed, got 7" is an artifact of the flipped condition) | `check_overlap_levers.py --self-test` | 1 | `FAIL control world: …`; `1 failures`; `22 assertions` |
| D′ | same tree as D | guard | 1 | `FAIL overlap_levers observed=22 floor=22 self_test_failures=1` |

Reading of A and B: each exits 2 before any instrument runs, names the class and the row, and prints no PASS line. The row-deletion case (A) names two lines, one per side of the mismatch.

## Output pattern: `(?m)^(\d+) failures\n(\d+) assertions$`, groups (2, 1)
- It parses the real output: H3 bytes are `0 failures\n22 assertions\n`, and H1 reads `observed=22`. The failure branch also parses: D′ reads `self_test_failures=1` from `1 failures` / `22 assertions`.
- Group order is (assertion, failure). This matches the convention in `corpus_independent` (`(1, 2)`, with "assertions, failures" order) and the `failure(s) over N assertions` rows (`(2, 1)`).
- No-match behavior (read at guard lines 527–530, not run): `assertions = int(…) if match else 0` and `ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0`. An unparseable self-test output gives FAIL, not silence. The guard reads stdout, and the overlap self-test prints its summary to stdout (H3).

## Verdict basis
- Surfaces 99 to 115 is consistent across registry, both tables, docstring and anchors (H1 exit 0; H2 exit 0).
- Overlap row (floor 22, path, pattern) is consistent across registry, `INSTRUMENTS` and `EXPECTED_INSTRUMENTS`, and passes at 22 (H1).
- Total 11 to 12 matches the 12 entries; the guard's size check is silent at HEAD.
- Half-bumps are refused: A, B and A′ exit 2. Docstring-only drift is not refused (C, F1).

## Residual risk and gaps
- A round-47 record shows `FAIL harness_independent self-test timed out after 120s (hung?)` (`.ufo/waves/round-47/falsify/W2ShonenEvidence.floors-default.out`, line 7); the same record reruns it to PASS (`…floors-timeout300.out`). Not reproduced here (H1 passed). The 120 s per-instrument timeout is a standing flake risk, not from this diff.
- Stale counts: I checked live files only (`verifiers/`, `SKILL.md`, `SCORECARD.md`, `README.md`, `LOG.md`, `corpus/QUALITY.md`, `plans/`). The round-49/50 entries in `LOG.md` (lines 2393–2397) say "10 to 11" and are history. No live stale floor found.
- Not checked: the other no-harm gates and BaseReplay (other seats); whether the surfaces count of 115 measures what the claim says (the guard checks the count only).
