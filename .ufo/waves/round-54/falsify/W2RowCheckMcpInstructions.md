Result: HOLDS — every cell of the `verifiers/check_mcp_instructions.py` registry row verified in a sandbox clone at 58db81c4; no cell breaks, three residual risks noted.

Scope attacked: SKILL.md:463 row `| verifiers/check_mcp_instructions.py | gate | python3 -B verifiers/check_mcp_instructions.py --rev <rev> | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | in-file | none; --fetch reads the network | kotoba |`, landed at bf65974c (SKILL.md:449 in that commit, identical text). Sandbox: `/fast/scratch/hyaku/kotoba-r54/KotobaR54.W2RowCheckMcpInstructions` at 58db81c4465b0e9b07ef2485b87d8970683afac6. All line numbers are `verifiers/check_mcp_instructions.py` unless named.

# Cell-by-cell

- **Name — HOLDS.** `verifiers/check_mcp_instructions.py` is a `.py` blob directly under `verifiers/` (in the counter's universe; `check_gate_registry.py:16-18` universe rule). Row name cell is byte-identical.
- **Kind `gate` — HOLDS.** The script can fail: empty root produced `mcp instructions backed 0 of 7 clients`, exit 1 (below). Not a probe.
- **Entry command — HOLDS.** Ran verbatim from the sandbox root:
  `python3 -B verifiers/check_mcp_instructions.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6` → exit 0; last line `mcp instructions backed 7 of 7 clients` (all seven clients BACKED). Command text contains `verifiers/check_mcp_instructions.py`; `--rev` path uses read-only `git -C <lane> show <rev>:<path>` (line 102).
- **Verdict map `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS, residual R1/R2.**
  - 0: `return 0 if value >= TARGET` (line 365, TARGET=3 at line 66); observed exit 0 above (7 ≥ 3).
  - 1: same line, else branch; observed: `--root /tmp/mcp-empty-root` → `backed 0 of 7 clients`, exit 1.
  - 2: `except RuntimeError → return 2` (lines 285–287); observed: `--rev bogus-name` → `could-not-evaluate: git show bogus-name:... failed: fatal: invalid object name 'bogus-name'.`, exit 2. Argparse errors also exit 2 (`ap.error` at lines 277, 280; observed `--self-test --rev HEAD` → usage error, exit 2), consistent with the SKILL.md:450 rule "an undeclared nonzero code reads as could-not-evaluate".
  - No other code is produced: the only exits are `return self_test()` (0/1, line 278), `ap.error` (2), `return 2` (287), `return 0/1` (365). Every produced code is declared.
- **Self-test `--self-test` — HOLDS, residual R3.** Literal flag at lines 48 and 273; line 278 dispatches to the in-file `self_test()` (lines 223–263) — the script's own test code, not a nested gate call or usage text. Observed: `python3 -B verifiers/check_mcp_instructions.py --self-test` → exit 0; last line `self-test: 0 failure(s) over 10 assertions` (exercises the M12 host-pin and M16 Gate-quote mutant arms, lines 234–260).
- **Pinned values `in-file` — HOLDS.** Every expected-value constant is in-file and never read from the measured revision (docstring lines 12–16): `ENTRY/SOURCES/LESSON` (63–65), `TARGET/OPENED/WORD/MAX_WORDS` (66–69), `CLIENTS` (70–71), `HOSTS` (72–90), `HEADER` (91), regexes (92–97). The three corpus paths the script reads are measured surfaces, not pinned expected values — so `in-file` is correct, and more correct than the wave-1 builder's own draft (`RegCheckMcpInstructions.md:3` listed the three measured files; the landed row improved on it). No external baseline/JSON is read anywhere.
- **Write scope `none; --fetch reads the network` — HOLDS.** Full-file sweep (`open|write|mkdtemp|tempfile|mkdir|os\.|shutil|subprocess`): only line 102 (`git show`, read-only) and line 219 (`urllib.request.urlopen`, GET, reached only under `--fetch` at lines 342–351). No filesystem write exists in the script. `--fetch` does hit the network (lines 217–220); not exercised — optional flag, entry command doesn't need it.
- **Owner `kotoba` — HOLDS.** Matches `OWNER = "kotoba"` (`check_gate_registry.py:65`) and the row rule (lines 35–36).

# Residual risks (not cell breaks)

- **R1 (low, semantics):** a well-formed but absent revision returns `failed`, not `could-not-evaluate`. `--rev 0000000000000000000000000000000000000000` → each `git show` fails with `exists on disk, but not in` (line 106 → treated as file-absent) → `backed 0 of 7`, exit 1. The malformed-rev path returns 2. Both codes are declared, so the map is unbroken, but an unmeasurable revision reads as a failed measurement. Lane-owned vocabulary (PROTOCOL pins only the classes); sibling counters behave differently (`check_gate_registry.py` raises RuntimeError → 2 for unreadable trees).
- **R2 (low, generic):** uncaught exceptions exit 1 = `failed` rather than `could-not-evaluate`. Observed: non-UTF-8 entry file under `--root` → `UnicodeDecodeError` traceback, exit 1. A crash is indistinguishable from a legitimately failed gate; the SKILL.md fallback rule can't help because 1 is declared. Shared by every sibling Python gate; flagging once here as a fleet-wide semantic hole, not this row's defect.
- **R3 (standard gap, pre-existing):** `--self-test` is helper-only — pure-function assertions over `host_ok`/`gate_quote_matches`, no fixture tree, no exit-code or finding-id assertion. PROTOCOL.md § Gate standard, Self-test bullet: "a helper-only or model-only self-check does not satisfy this clause". The row honestly records the flag that exists, and the registry counter only requires the literal flag in bytes (`check_gate_registry.py:29-31`); sibling rows land the same shape (`check_gate_registry.py:203+`, `check_description_thresholds.py:307+` are also fixture-less-assertion style — `check_gate_registry.py`'s does synthesize fixture strings in-memory). If the clause is enforced literally the gap is the script's, not the row's: the row needs no correction.

# Cross-checks

- Frozen-counters rule: `git diff e33715486a45 58db81c4465b -- verifiers/check_mcp_instructions.py` → empty (0 lines). Counter untouched this round; `verify_surfaces.py` untouched by this item.
- Script history (context for "frozen" docstring, lines 12–16): created at round-52 plan commit `4c003a4b`, then modified by round-53 commits `aeed089` (D4 exact host/quote match) and `b5dc7dc` (MCP pin rejects dot segments) — matching logic tightened per round-53 lesson M42; the round-52 pinned values themselves are unchanged, so the "frozen" claim holds in substance.
- Row text in the landed commit equals the current row verbatim (`git show bf65974c:SKILL.md` line 449).

No proposed row correction: no cell breaks.
