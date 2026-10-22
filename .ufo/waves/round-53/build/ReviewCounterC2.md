Result: MIXED — the frozen C2 counter is correct on its claim surface (2-of-8 reachable, always-PASS/always-FAIL both killed, exit rule and section filter verified) but has one medium defect (a `delegated:` absolute or escaping path runs a host file as the instrument, bypassing "in the revision") and one low-medium defect (a shape-malformed map exits 1 with a traceback instead of `cannot evaluate`/exit 2).

Reviewed: `verifiers/check_alwayson_boxes.py` frozen at plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` (line numbers below are that file). Sandbox clone `/fast/scratch/hyaku/kotoba-r53/ReviewCounterC2` at the plan commit; every probe below was executed there, counter binary always the lane's frozen file, invoked as `python3 -B .../check_alwayson_boxes.py --rev <rev> --repo <clone>`. No tools installed this session; probes used only git + stock python3. LSP device: no `lsp` tool exists in this session's inventory, so no language-server answers were possible; all checks are text-level reading plus executed probes (recorded as required, not as semantic proof).

## Findings by severity

### MEDIUM — F1: the delegated path is not confined to the revision; a host file can serve as the instrument
`check_alwayson_boxes.py:144-147`:
```python
script = tree / d.split(":", 1)[1]
if not script.is_file():
```
`Path.__truediv__` discards the base when the right operand is absolute, so a disposition `delegated:/abs/path.py` never resolves inside the extracted `git archive` tree (`:133-135`); `is_file()` then matches any file on the host. The docstring contract says "that file exists **in the revision**" (`:30`), and this is exactly the guarantee the extraction exists to provide.

Demonstrated (sandbox commit `5c9dc3e`, "mutant: absolute disposition, instrument absent from revision"):
- dispositions: `delegated:/fast/scratch/hyaku/kotoba-r53/ReviewCounterC2-host/always_host.py` (the correct delegate, placed outside the clone);
- `verifiers/always_on_check.py` deleted from the revision; `git archive --format=tar HEAD -- verifiers | tar -t | grep -c always_on_check.py` → `0`, grep exit 1 (absent);
- run: prints `always-on boxes executed and discriminating 2 of 8`, both boxes `counted (6 of 6 cases as pinned)`, **exit 0**.

So a revision with no instrument at all satisfies the counter, because the counting instrument lives on the host and is free to change after the measurement. This is the M12/M16 class the round-52 spot-check routed against `check_mcp_instructions.py`, and the sibling gate already carries the guard this counter lacks: `verify_skill_checklist.py:2054` self-test arm `delegated-escape` expects `"outside the map's repo"`. (A contaminated first attempt of this probe, sandbox commit `734c5df`, still demonstrated the same execution path; the clean rerun above is the evidence of record.) Recommendation: require the path to be relative and its resolved location to stay under the extracted tree (reject absolute paths and any `..` escape) — note `is_file()` follows symlinks, so a resolved-path containment check, not an existence check.

### LOW-MEDIUM — F2: a shape-malformed map crashes with exit 1 instead of `cannot evaluate` (exit 2)
`check_alwayson_boxes.py:129` fetches `["boxes"]` and `:136` iterates it; the handler at `:161` catches `CalledProcessError, JSONDecodeError, KeyError, OSError, tarfile.TarError` — not `TypeError`/`AttributeError`. A map that is valid JSON but the wrong shape therefore escapes the contract's exit-2 arm (`:43`: "2 = could not evaluate (git failure, unreadable map)") and reports as claim-false. Demonstrated (sandbox commit `ea26879`, `"boxes": null`):
```
Traceback (most recent call last):
  File ".../check_alwayson_boxes.py", line 136, in main
    section = [b for b in boxes if b.get("section") == SECTION]
TypeError: 'NoneType' object is not iterable
exit=1
```
`boxes` as a string, or entries that are not dicts, fail the same way (`b.get` → AttributeError). An unreadable map is indistinguishable from a red claim. Fix: add `TypeError, AttributeError` to the `:161` tuple, or validate shapes on load. (Contrast: `"boxes"` missing outright is caught — KeyError → exit 2; and a truly absent file/bad rev is exit 2, verified below.)

### LOW — F3: N counts only the two pinned boxes; the printed "N of T" cannot see other executed boxes
`:139` iterates the frozen `CASES` dict only, so an executed-and-passing delegation of, say, `alwayson.01` never enters `n`; `:164` would still print `2 of 8`. The frozen claim statement is exactly this printed line, so the claim is safe, but the sentence ("boxes executed and discriminating N of T") reads as section-wide executed coverage while it is pinned-box coverage. Denominator T does honestly track the revision's section size (`:136`, `:164`). Reviewer guidance, not a code change: read N as "of the counter's pinned boxes".

### INFO — F4: per-case timeout only; a hostile delegate costs ~4 minutes of wall
Sleeper delegate (`time.sleep(25)` per invocation, sandbox commit `b0e318d`): all 12 cases report `saw timeout` (`:111-112`), result `0 of 8`, exit 1, wall 240.30 s (12 × `TIMEOUT=20`, `:59`). Correct and bounded, but there is no aggregate budget and `subprocess.run` (`:109-110`) kills only the direct child — a grandchild inheriting the stdout pipe could extend `communicate()` past the timeout ([INFERENCE] on CPython `run` semantics; not exercised). Not blocking: revision-controlled delegates in this repo are plain scripts.

### INFO — F5: minor asymmetry in the not-counted message
`:142` prints `d.split(':')[0]` (no maxsplit) where `:144/:146` use `split(':', 1)`; harmless for the observed `unexecuted`/`<absent>` prefixes, cosmetic only.

## Verified-clean surface (each item exercised, not assumed)
- **Section filter**: `SECTION` (`:58`) equals the baseline `section` value byte-for-byte for all 8 always-on boxes in `verifiers/checklist-baseline.json` at the plan commit (JSON inspection: 8 boxes, section `'Always-on constraint-file checklist (AGENTS.md-class)'`, matching `SKILL.md:360` header). Observed denominators `0 of 8` / `2 of 8`.
- **Case planting**: `plant` (`:96-104`) writes UTF-8 explicitly (`:104`); the symlink case plants `AGENTS.md` before `os.symlink("AGENTS.md", CLAUDE.md)` (dict insertion order, `:82`), relative target resolves to the sibling — the `symlink-redirect` PASS case counts only if the delegate resolves it (my correct delegate did, see run below).
- **Contract parse**: `:113-119` requires an exact `{"id": <box>, "status": PASS|FAIL}` entry plus pinned exit code; catches `JSONDecodeError/StopIteration/AttributeError/TypeError`. Exercised: non-JSON stdout delegate (commit `649534f`) → all 12 cases `no \`alwayson.0x\` entry`, `0 of 8`, exit 1.
- **Timeout**: exercised, F4 above.
- **`cannot evaluate` arm**: `--rev deadbeefdeadbeef` → stderr `cannot evaluate: ... returned non-zero exit status 128`, exit 2. KeyError (missing `boxes`) and OSError (plant/symlink failures, inside the `:128` try) are covered; only the shape-malformed cases of F2 escape.
- **Exit rule**: `:166` `return 0 if n == len(CASES) else 1` with `len(CASES) == 2` — exit 0 iff both pinned boxes count, independent of T, exactly as the docstring (`:42-43`) and the plan's claim line pin it.
- **Case set discrimination** (plan C2 paragraph): 04 splits 2 PASS controls (incl. `version-number`, which kills a bare "digits" date detector) / 4 FAIL cases (ISO date, ISO timestamp, month-name day, dated CLAUDE.md — kills an AGENTS.md-only scanner); 07 splits 4 PASS (incl. `@AGENTS.md` import and symlink redirect) / 2 FAIL (two independent files; prose mention — kills a substring "AGENTS.md" detector). All 12 cases fired in the mutant runs above with per-case messages naming every violation.

## Reachability demonstration (claim `2 of 8` is attainable)
Sandbox clone at plan commit `3bb0a7a`; demo delegate `verifiers/always_on_check.py` (correct implementation: ISO/timestamp/month-day date scan over both rule files resolving symlinks; canonical-name rule: one file PASS, symlink or `@AGENTS.md`-first-line redirect PASS, otherwise FAIL); dispositions of `alwayson.04`/`alwayson.07` set to `delegated:verifiers/always_on_check.py` (text_sha256 anchors `e88887ba…`, `ade1f600…` untouched — boxes unchanged, so the box map stays hash-pinned to the live SKILL.md).

| rev (sandbox) | delegate | output | exit |
|---|---|---|---|
| `3bb0a7a` (base) | — | `always-on boxes executed and discriminating 0 of 8`; both `not counted (disposition unexecuted)` — reproduces the plan's before-value | 1 |
| `d0e26aa` | correct | `always-on boxes executed and discriminating 2 of 8`; `alwayson.04: counted (6 of 6 cases as pinned)`; `alwayson.07: counted (6 of 6 cases as pinned)` | **0** |
| `222f8a8` | always-PASS | `0 of 8`; 04: 4 FAIL-cases wrong (iso-date, iso-timestamp, month-day, dated-claude-md); 07: 2 wrong (two-rule-files, prose-mention) | 1 |
| `5371086` | always-FAIL | `0 of 8`; 04: 2 PASS-cases wrong (plain-rules, version-number); 07: 4 wrong (agents-only, claude-only, import-redirect, symlink-redirect) | 1 |
| `5c9dc3e` | host-file bypass | `2 of 8`, exit 0 with instrument absent from the revision — **F1** | 0 (defect) |
| `ea26879` | `boxes: null` | TypeError traceback — **F2** | 1 (defect, should be 2) |
| `649534f` | non-JSON | `0 of 8`, missing-entry messages | 1 |
| `b0e318d` | sleeper 25 s | `0 of 8`, `saw timeout` ×12, 240.3 s wall | 1 |

## Residual risk and verification gaps
- The counter never checks that the delegate's `--check` for the *other* pinned box behaves; each box is judged only through its own cases (by design, per-box). A delegate could special-case box ids; the case text does not leak the expected status, so this requires a deliberately case-fitting instrument — visible in review of the revision, not by the counter.
- F4's grandchild-holds-pipe variant of the timeout was not exercised; CPython semantics only.
- I did not run the round-52 frozen counters or `verify_skill_checklist.py` against the demo commits (no-harm guards are the L1's integration concern; note that `verify_skill_checklist.py`'s delegated gate would additionally require the instrument to exist in the working tree and, if it supports `--box-proof`, to pass it — the demo delegate supports neither requirement and would rely on the "no --box-proof support, not run" branch at `verify_skill_checklist.py:1001`).
- No LSP server was available (no `lsp` device in this session); definition/reference checks were done by reading the single-file counter and executing it — the counter has no other callers (`grep` for `check_alwayson_boxes` in the lane finds only the plan, lessons, and this counter itself).
- Sandbox commits `734c5df` (contaminated bypass probe) and the probe chain remain in `/fast/scratch/hyaku/kotoba-r53/ReviewCounterC2`; nothing was written to the lane except this report, nothing pushed.
