Result: HOLDS — the routed-defect-5 repair to `verifiers/check_gate_registry.py` (commit `4d700b17`) closes the all-probe/none route and the borrowed-flag substring route at the tip; the residual gaps found are narrow and mostly inside the docstring's disclosed limits.

Scope: routed defect 5 — `git diff a10240c0 4d700b17 -- verifiers/check_gate_registry.py` (78 insertions, 11 deletions; `has_flag_handler` added, probe rule added to `judge_row`, substring flag test replaced, self-test arms added). Sandbox clone: `/fast/scratch/hyaku/kotoba-r55/ReviewRegistryHarden` at `f0e6b695b746775823b65a8c45de7d50ea33e84f`. Lane untouched. Every command capped with `timeout`.

## Assigned checks (all exercised, exits pasted)

1. `timeout 900 python3 -B verifiers/check_gate_registry.py --self-test` (sandbox, tip)
   → exit **0**, `self-test: 0 failure(s) over 28 assertions`.

2. `timeout 900 python3 -B verifiers/check_gate_registry.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f`
   → exit **0**, `gate registry rows conformant 26 of 26 lane verifiers; phantom 0` (expected 26 of 26, phantom 0 — matches).

3. All-probe/none registry at the tip fails (the routed hole is closed).
   Sandbox commit `c0f68eab2a47214cd3982b0b15782eabeff2ba87`: all 26 registry rows rewritten to kind `probe`, verdict `0=clean`, self-test `none`, pinned `none`.
   - New counter: `--rev c0f68eab` → exit **1**, `conformant 0 of 26`; every row rejected with `probe script has an exact --self-test handler`.
   - Pre-fix counter (bytes from `a10240c0`, run from a subdir of the same clone so `LANE` resolves to the clone): `--rev c0f68eab` → exit **0**, `conformant 26 of 26`. The routed defect reproduced verbatim: the mechanical all-probe/none table reached M of M under the old code and cannot under the new.

4. Borrowed `--self-test` flag in a comment of a gate without a handler fails.
   Sandbox commit `9845d3e04e17f10670d222011859e2c9b4269b21`: `verifiers/check_sibling_census.py` `add_argument("--self-test", ...)` (tip line 894) removed, replaced by a comment containing the literal `--self-test`.
   - New counter: exit **1**, `conformant 25 of 26`; `verifiers/check_sibling_census.py no self-test flag --self-test lacks an exact handler`.
   - Old counter: exit **0**, `conformant 26 of 26` — the substring test accepted the borrowed literal, exactly the round-54 `RegCheckOpencodeRepin` draft-row defect.

5. Could-not-evaluate path intact: `--rev deadbeef…beef` → exit **2**, `could-not-evaluate: git ls-tree failed: fatal: not a tree object`. The exit-2 path was not touched by the patch (matches ExecRegistryHarden receipt 4: R/G probes still exit 2, controls held).

## Q31 — the rule as written vs the rule as coded

Docstring (tip `:34-38`): *"a `probe` is rejected if its verdict map declares `1=failed` or its source has an exact active `--self-test` handler."* Code (`judge_row` `:193-197`): `("1","failed") in pairs` → reject; `has_flag_handler(path, src, "--self-test")` → reject. **Consistent.** Exercised via `judge_row`/`has_flag_handler` imports:

- `1=failed`, `1 -> failed`, `1 → failed` all reject (PAIR_RE covers all three spellings).
- `2=failed` and `1=could-not-evaluate` on a probe: CONFORMANT — narrow by design, disclosed as "a narrow failure-capability rule" (Q31).
- Probe naming a script whose `--self-test` appears only in a comment: CONFORMANT — the handler test is exact, not substring.
- Probe `none`/handler-less script: CONFORMANT — correct, the row is then an honest description.

## Findings (all minor; none defeats the routed repair)

1. **Minor — "active" overstates the check; dead code counts.** `has_flag_handler` accepts `if False: ap.add_argument('--self-test')` (Python AST) and `if false; then case x in --self-test) ;; esac fi` (shell) — observed `True` for both. The docstring says "exact **active** handler … Comments and longer lookalike flags do not count" but reachability is not checked. A gate could register `--self-test` on dead code. Mitigation: inserting dead code into a lane gate is itself a lane-file change a reviewer would see; the docstring also discloses "it does not run the script". Reported, not fixed (bounds).
2. **Minor — shell heredoc can fake an arm.** `cat <<EOF\ncase x in\n--self-test) go ;;\nEOF` returns `True`: the line scanner tracks `case`/`esac` keywords, not syntax, so case-looking text inside a heredoc (or any string data line) satisfies the shell gate's self-test cell. A substring-of-data hole survives for `.sh` — currently one lane script (`fault_injection_corpus.sh`, whose real arm `:46 --self-test) SELFTEST=1; shift ;;` is detected correctly, `has_flag_handler` → `True`).
3. **Minor — over-rejection (safe direction).** Real handlers missed: combined shell arms `--self-test|-s) go ;;` → `False`; Python flag passed via a name (`F='--self-test'; ap.add_argument(F)`) → `False`; unparseable Python → `False`. These fail the registry row rather than falsely passing it, so they tighten, not loosen, the counter; noted for completeness.
4. **Residual hollow shape (disclosed).** A probe may still declare `2=failed` (any failed code except `1`) — the spotcheck's "check kind against the script" was narrowed to this pair-+-handler rule; a `2=failed` probe is a smaller hole than the routed one (gate-only duties still bypassed only for rows without `1=failed` and without a `--self-test` handler). Consistent with the Q31 disclosure.

## Consistency judgment

Code, docstring and self-test agree on all exercised arms (28/28 self-test assertions; every module-level probe/comment/lookalike case behaved as documented). The two named routed attacks fail at the tip with the exact expected messages, and the old counter's opposite verdicts confirm the fix — not ambient strictness — causes the rejections. The counter's frozen surface (heading, header, universe rule, kinds, classes, owner) is unchanged; judging lines it kept are byte-identical in behavior on conformant inputs (26 of 26 at tip both pre- and post-fix would read the same honest table).

## Verification gaps

- Did not re-run `check_could_not_evaluate.py` end-to-end on the tip (its per-gate receipt for this counter is in `build/ExecRegistryHarden.md` §4 and the exit-2 path is confirmed above); sibling seat `W2RerunC1`/C2 reruns cover the fleet counters.
- "Active" reachability (finding 1) was demonstrated at the function level, not via a committed lane mutation — same code path the committed mutations exercised.

No tools installed. No lane files modified; all git writes confined to the sandbox clone.
