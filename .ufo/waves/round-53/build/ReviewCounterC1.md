Result: DONE — frozen `verifiers/check_opencode_repin.py` reviewed line-by-line at plan commit 3bb0a7a; base run reproduces the documented before-value exactly; one Medium vacuity hole (counts PASS rows, not check ids — false exit 0 demonstrated) plus a family of crash-instead-of-exit-2 inputs; extraction scope and all four metric legs otherwise verified correct.

# Scope and method

File reviewed: `verifiers/check_opencode_repin.py` at `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` (working-tree copy byte-identical: `git diff 3bb0a7a -- verifiers/check_opencode_repin.py` → 0 lines). All experiments ran in my sandbox clone `/fast/scratch/hyaku/kotoba-r53/ReviewCounterC1`; lane files untouched except this report.

# Verified correct (no defect)

- **Extraction scope is sufficient and complete.** `extract` (line 65-68) archives `verifiers corpus`. The gate needs only: `verifiers/surfaces-baseline.json` (baseline), `verifiers/fixtures/surfaces/` (self-test; 38 files confirmed in archive), `corpus/knowledge/instruction-surface-census-round13.md` (inventory, confirmed in archive), plus the two host binaries and the `strings` tool. The pins script needs only `verifiers/baseline.json` + the same host paths. `git archive <rev> -- verifiers corpus` at `4daf6c8` lists all of these. Nothing the gate reads is missing from the archive.
- **A missing scope path is loud, not silent**: `git archive HEAD -- verifiers no-such-dir` exits 128 → `CalledProcessError` → caught at line 123 → counter exit 2.
- **Field names match reality.** Gate `--json` emits `{"checks": [{"id", "status", "detail"}...]}` (gate `emit_json`, verify_surfaces.py:1591-1603); counter reads `checks`/`status`/`id` at lines 100-103 — including `surfaces.opencode_extract` lookup. Pins script emits `{"checks": [{"pin", "verdict"}...]}` (check_substrate_pins.py:265); counter reads `checks`/`verdict`=="PASS" at lines 107-109. `status` vs `verdict` asymmetry is real and correctly handled.
- **Self-test tally parse matches the gate's format** (`"%d failure(s) over %d assertions"`, gate line 1524): counter lines 116-121.
- **Frozen constants verified against base**: `CHECKS_TOTAL=7` = `len(CHECK_IDS)` (gate:254-262); `PINS_TOTAL=3` = `len(EXPECTED_PINS)` (pins:76-80); `SELFTEST_FLOOR=129` = `floors-registry.json instruments.surfaces.floor`; `len(base opencode classes)` = 9 unique ids (verified via surfaces-baseline.json).
- **Kept-class comparison is conservative** (lines 71-78, 110-111): same `class_id` + same `(literal, context_kind, verdict)` required; renaming/retiring/re-kinding/re-verdicting → not kept; missing keys → `KeyError`/`None`-mismatch → exit 2 or not-kept.
- **Exit codes verified end-to-end**:
  - Lane, `--rev e78dff66`: `opencode re-pin: surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions` / substrate line names opencode.exe sha256 `538fcb1b…` / **exit 1** — matches the C1 before-value exactly.
  - Sandbox commit `4daf6c8` (re-pin only: `baseline.json` opencode sha `179ca421→538fcb1b`, 1 file +1/−1): `6 of 7 (FAIL); pins OK 3/3; kept 9 of 9; 0/129` → **exit 1**, as expected. The counter correctly refuses a sha-only re-pin.
- **`tarfile.filter="data"`** blocks traversal/device/outside-symlink escapes; `FilterError` subclasses `TarError` → caught → exit 2.
- **`mtime` pin is deterministic** (stat vs pinned ISO, tolerance_ns — pins:257), not wall-clock; pins 3/3 held across all runs.

# Findings

## M1 (Medium) — P counts PASS rows, not distinct check ids → fabricated 7-of-7 exits 0

Counter lines 100-103:
```python
checks = sj.get("checks", sj.get("results", []))
p = sum(1 for c in checks if c.get("status") == "PASS")
oc = next((c.get("status") for c in checks if c.get("id") == "surfaces.opencode_extract"), "ABSENT")
```
`CHECKS_TOTAL=7` is only the printed denominator; the numerator counts rows with `status == "PASS"` regardless of `id`, and `oc` takes the first matching row. Demonstrated end-to-end on sandbox commit `8b77e48` (on top of the re-pin commit `4daf6c8`): a gate that emits 7 rows, all PASS, while **dropping `surfaces.no_uncovered_class` and duplicating `surfaces.literal_present`** produced

```
opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
… exit=0
```

A revision can green the counter while its gate silently covers only 6 of the 7 checks. Mitigation path is wave-2 review (diff the revision's `emit_json`/`results.append` path, gate:1630-1644) since the counter is frozen and cannot be widened. [VERIFIED by run]

## M2 (Medium) — Crash instead of exit 2 on malformed JSON field values

The `except` tuple (lines 123-124: `CalledProcessError, JSONDecodeError, KeyError, ValueError, OSError, TarError`) omits `TypeError` and `AttributeError`, and line 130 sits outside the `try` entirely. Demonstrated, each on its own sandbox commit (re-pin parent):

- Gate emits `"checks": null` → `TypeError: 'NoneType' object is not iterable` at counter line 101 → traceback, **exit 1** (mutB). `.get("checks", fallback)` returns `None` when the key exists with a null value — the nested fallbacks at 100/107 only fire on missing keys.
- Gate emits `"substrate": null` → `AttributeError` at line 122 (`sj.get("substrate", {}).get("opencode", {})` → `None.get`) → traceback, **exit 1** (mutC).
- Gate emits `"substrate": {"opencode": null}` → `sub` is `None`; line 130 `sub.get('path')` is **outside** the try → traceback, **exit 1** (mutD).
- Pins script emits `"checks": null` → `TypeError: len(None)` at line 108 → traceback, **exit 1** (mutE).
- Code-cited siblings (not run): a checks/rows list of non-dicts → `AttributeError` on `.get` (lines 101-103, 109); a tally line whose last token is `over` while containing `failure(s)`/`assertions` → `IndexError` at line 120 — same uncaught class.

Contract (docstring line 36): `2 = could not evaluate`. These inputs produce an uncaught traceback with exit 1. Direction is loud (never 0), so it misclassifies rather than masks — but it still violates the exit-code contract and prints an ugly crash on an innocuously-malformed revision output.

## M3 (Low-Medium) — substrate line (the freshness binding) is not bound to the exit code

`sub` (line 122) never enters `ok` (line 131); lines 127-130 print `None` fields uncomplainingly. Demonstrated: the mutF2 run printed `substrate opencode: None sha256 None bytes None` while other metrics evaluated normally. A revision whose gate stops emitting `substrate` still exits 0, and the plan's promise that "the second line names the measured opencode binary" becomes vacuous. Related: the measured binary is whatever the *revision's* `DEFAULT_BINARIES`/`BINARIES` point to — the counter never binds the canonical path (`/home/vgpnk/.npm/_npx/…/opencode.exe`); a coordinated repoint of both scripts' defaults to a frozen snapshot keeps exit 0 while the live substrate drifts. The substrate line reveals that only if the gate still reports truthfully. Pins leg (`k==n==3`) is the real binary binding; wave-2 should diff the revision's `DEFAULT_BINARIES`/`BINARIES` constants.

## L1 (Low) — kept-K comparison is duplicate-blind; currently backstopped only by the gate's loader

`opencode_classes` (lines 71-78) builds a dict with last-wins; K counts `len(base)` ids present in `rev_cls` (line 111). Demonstrated on `503917c` (re-pin parent): a `surfaces-baseline.json` declaring `opencode:read-hook/instructions` twice — mutated literal `DIFFERENT-REMINDER` first, original `<system-reminder>` last — still prints `kept 9 of 9`. End-to-end it did not pass today: the gate's own `load_baseline` rejects duplicate class ids (`BaselineError`, gate:352-354) → gate emitted empty `checks` → `0 of 7` → exit 1. But the *K metric itself* masks the duplicate; a revision that also relaxed its gate's loader would keep `kept 9/9` green.

## L2 (Low) — self-test tally brittleness

- Lines 115-121: if the self-test run crashes before printing the tally (e.g., fixture missing → gate traceback), `f = a = -1` and the counter prints `self-test -1 failure(s) over -1 assertions` — exit 1, conservative, but dishonest-looking output.
- `int(parts[0])` assumes an unprefixed tally line; a revision emitting `self-test: 0 failure(s) over 200 assertions` → `ValueError` → caught → exit 2 (`cannot evaluate`). Wrong direction for a parseable tally; floor check should have treated it as A=200.
- `t.returncode` ignored entirely: a self-test that prints `0 failure(s)` then exits nonzero on a late harness error still passes the leg.

## L3 (Low, observation) — gate error paths report as claim-false (exit 1), not could-not-evaluate (exit 2)

Gate env error (`exit_code` 2, `checks: []`) or baseline error (`exit_code` 3, `checks: []`) → counter prints `surfaces pass 0 of 7 (opencode_extract ABSENT)` → exit 1. Defensible — the claim is not demonstrated — but it conflates "a check failed" with "the gate could not load its baseline" (seen in the mutF2 run). Not a contract violation; flagging for awareness.

## L4 (Low) — no subprocess timeouts

Lines 97-98, 104-105, 112-113 run the revision's gate/pins/self-test with no `timeout`. A hung revision script hangs the counter forever (hosting risk only, not a verdict defect).

# Answer to "is there any input on which it crashes instead of exiting 2?"

Yes — four demonstrated end-to-end (mutB/mutC/mutD/mutE above), plus code-cited `AttributeError`/`IndexError` siblings. Root cause: the except tuple at lines 123-124 lacks `TypeError`/`AttributeError`/`IndexError`, and line 130 is outside the `try`.

# Residual risk and verification gaps

- The counter trusts the revision's own gate JSON. M1 is the substantive consequence: a fabricated `checks` array clears the surfaces leg while pins (3/3), kept (9/9) and self-test (0/129) still bind their three legs. Catching it requires wave-2 code review of the revision's `verify_surfaces.py` emit path — which the plan already assigns to reviewers/mutation-testers ("what the counter does not measure").
- Not exercised: every malformed shape (four demonstrated, three code-cited); timeout behavior; `--repo` pointing at a repo lacking BASE_REV (would exit 2 via `CalledProcessError` on `git show`).
- The `self-test` run ignores `--repo` semantically (gate self-test reads script-relative `FIXTURES`), so `--repo <tree>` on line 112 is harmless but cosmetic.
- jj-colocation: `--repo` default derives from the counter's own path (`Path(__file__).resolve().parent.parent`); invoked in-place it resolves to the lane git repo and works. A copied-out counter would default to the wrong repo and exit 2 — loud, fine.

# Reproduction index

- Lane (read-only): `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/check_opencode_repin.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` → exit 1, 6/7, 2/3, 9/9, 0/129.
- Sandbox commits: `4daf6c8` re-pin-only → exit 1, pins 3/3; `39a3f7b` checks-null → traceback exit 1; `17507a0` substrate-null → traceback exit 1; `e98822a` pins checks-null → traceback exit 1; `503917c` duplicate class_id → kept 9/9 masked (exit 1 via gate baseline rejection); `8b77e48` fabricated 7-row all-PASS → **exit 0** (the M1 false pass).
- Host tools used: python3 (host), git 2.x, tar — no installs required for this review.
