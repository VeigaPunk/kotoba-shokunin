Result: DONE — `check_assertion_floors.py` now returns 2 when Git cannot be run; its C2 G/S/V controls pass, though the frozen overall C2 counter remains unmet at 14/25.

## Change

- Sandbox commit: `5f448f31c3b6815ed2bf78e5461c3ed675294889`.
- Delivered unified diff: `.ufo/waves/round-55/build/FixAssertionFloors.patch`.
- In `verifiers/check_assertion_floors.py:464-468`, normal evaluation now runs a silent `git --version` preflight and maps `OSError` (including `FileNotFoundError`) to a `could-not-evaluate:` stderr line and exit 2. The clean path continues into the existing checks without added output.
- F30 at `verifiers/check_assertion_floors.py:1205-1219` runs the gate with a PATH containing only a `python3` link and asserts exit 2 plus the diagnostic. This adds two counted assertions; it addresses QUALITY Q05 (`corpus/QUALITY.md:16`).

## Probe causes

- **R — not applicable.** At the plan commit, this gate's parser accepts `--repo`, `--script`, `--self-test-timeout`, and `--self-test`, but no revision argument (`verifiers/check_assertion_floors.py:453-461`). The frozen C2 receipt has only G, S, and V entries for this gate (`.ufo/waves/round-55/controls/C2-base.txt:49-51`). No R probe or unknown-revision behavior exists to repair; I did not add revision semantics.
- **G — child-test failures were reported as an ordinary failed verdict.** The gate itself did not run Git. It launched each instrument's Python self-test (`verifiers/check_assertion_floors.py:527-542` at the plan commit), caught only a subprocess timeout, and treated missing child output/nonzero child status as a floor failure. One child, `verify_corpus_independent.py`, calls Git directly without catching `OSError` (`verifiers/verify_corpus_independent.py:65-68`); its self-test fixture setup invokes that helper (`:582-588`). With Git absent, the parent therefore returned 1 instead of identifying the environment as unevaluable.

  The frozen base receipt, `.ufo/waves/round-55/controls/C2-base.txt:49-51`, records this gate's G probe as `expect 2 got 1 MISS`, with S and V controls both passing. The failure mechanism above is grounded in the gate and child source paths; no separate detailed base stdout is claimed here.

## Evidence

- Base self-test, using the script extracted from plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` in the sandbox:
  ```text
  0 failure(s) over 150 assertions
  base self-test exit 0
  ```
- Updated self-test: `timeout 900 python3 -B verifiers/check_assertion_floors.py --self-test`:
  ```text
  0 failure(s) over 152 assertions
  exit 0
  ```
- Updated direct G probe with PATH restricted to the `python3` link:
  ```text
  could-not-evaluate: git not runnable: [Errno 2] No such file or directory: 'git'
  exit 2
  ```
- Frozen counter after the sandbox commit: `timeout 900 python3 -B verifiers/check_could_not_evaluate.py --rev HEAD`. It measured `5f448f31c3b6815ed2bf78e5461c3ed675294889`; the assigned gate lines and summary were:
  ```text
  check_assertion_floors.py          G expect 2   got 2 ok
  check_assertion_floors.py          S expect 0   got 0 ok
  check_assertion_floors.py          V expect 0|1 got 0 ok
  could-not-evaluate probes honoured 14 of 25; controls held 13 of 13
  ```
  Counter exit: 1. Other registered gates still have probe misses; they were outside this assignment.
- Real verdict at plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`: exit 0; all 13 instrument rows passed. The `floors_guard` row was `PASS floors_guard observed=150 floor=150`; the final row was `PASS alwayson observed=89 floor=89`.
- Real verdict at sandbox commit `5f448f31c3b6815ed2bf78e5461c3ed675294889`: exit 0; all 13 rows passed. `floors_guard` is now `PASS floors_guard observed=152 floor=150` because its two regression assertions are counted; the identical final row is `PASS alwayson observed=89 floor=89`. The gate emits no aggregate summary line. Its real-verdict exit and final row are unchanged; the changed floors_guard count is the expected regression-arm increase.
- Diff stat against the plan commit: `verifiers/check_assertion_floors.py | 21 +++++++++++++++++++++`; `1 file changed, 21 insertions(+)`.

## Risks and blockers

- No blocker for this gate. The full C2 predicate is not met yet: the frozen counter exited 1 at 14/25, despite this gate's G/S/V passing.
- No LSP interface was exposed by the available tools; this was a local control-flow change, with no symbol refactor.
- No tools were installed or updated.
