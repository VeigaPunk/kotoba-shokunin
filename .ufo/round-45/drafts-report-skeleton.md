# kotoba — round 45 report — SKELETON

> Scribe seat **B1**. Populate this from round-45 scout reports and fresh reruns. Claim declarations and prior-round readings are not current outcomes. Every filled number needs its exact command and argv, observed output and exit, run instant, frozen input/source hashes, and Git HEAD/tree. Keep all unknowns `[PENDING]`.
>
> Pre-write snapshot at `2026-10-19T18:35:32Z`: `git rev-parse HEAD` → `032f47bd13fdff0cd2ccea5f902df9690ad09376`; `git rev-parse 'HEAD^{tree}'` → `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. `git status --porcelain=v1` → ` M verifiers/check_assertion_floors.py`, ` M verifiers/compare_harness_independent.py`, ` M verifiers/floors-registry.json`, `?? .ufo/round-45/`, `?? verifiers/fixtures/compare-harness-independent/status-lone-nonstring/`. These are shared-tree observations, not attributed to B1.
>
> Claim source `.ufo/round-45/claims.json`: `python3 -m json.tool .ufo/round-45/claims.json` exited `0`; `sha256sum .ufo/round-45/claims.json` → `69675f5c08d948e6e6c5aabe303fbda1d2d0eea3f7f96f7476b6dac147406c27` at the snapshot above. It registers round 45, loop A, position 9 of 12, provider `openai-codex/gpt-6-luna-max`, 40 seats, owned depth 9, advisory operability/calibration 8.5; these are pre-registration metadata, not findings.
>
> Comparator bytes: `git show '6881ce3:verifiers/compare_harness_independent.py' | sha256sum` → `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; `git show '032f47b:verifiers/compare_harness_independent.py' | sha256sum` → `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`. Thus `13b6d791` is the settled comparator's SHA-256 prefix, not a Git revision. At the same snapshot, `sha256sum verifiers/compare_harness_independent.py` → `215c5ca5f87c9036aeea83da8d10214fa1a2e37938977afa540b705ffe2c6fc9`, differing from the settled Git blob; do not treat that moving worktree file as the landed comparator. For R44's frozen-before/after claims, use `git show 6881ce3:<path>` and `git show 032f47b:<path>` bytes. For this round's current-target hunts, explicitly run the `032f47b` comparator bytes; after-round cells require the parent's landing commit.
>
> R41 census reference: `sha256sum corpus/knowledge/harness-independent-round41-census.md` → `b06742e4dff0093b28d0a621cd3475799d76b5464ea23b785bc53fe20b75f79f`. Archived runner/input identities at the snapshot: `v10-replay-probes.py` `02395bcee546fbd839ef74e6dc0d80a75687678943ce56ef5f67096bb812d2fa`; `v10-channel-census.py` `7b3f99ce77f11bef0920615b4f7efd0bd4b063e013ef558bcc1b92f276eeb2e9`; `v10-channel-census.json` `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0`. The archived `probe-results.json` / `subprocess-replay.json` hashes (`b6293543…` / `9f187342…`) differ from the retained `v10-` files (`cf60e7a9…` / `991d8d95…`); `cmp -s` returned nonzero for both pairs at `2026-10-19T18:34:38Z`. Choose and pin the intended source set; do not conflate replay generations or mistake the old frozen-comparator replay for a current hunt.

Lane: `kotoba-shokunin`. Claims: **C1 depth**, **C2 operability**, **C3 calibration** — source and digest above. Dispatch HEAD/tree: `032f47bd13fdff0cd2ccea5f902df9690ad09376` / `7c5e0a753eb39babfd66033d0f7ee08054191b3a`. Work commit: `[PENDING: parent integration commit]`. Round status: `[PENDING: populate only from fresh, pinned evidence]`.

## Work performed

- **C1 / depth — `[PENDING]`.** Replay the entire R41 census class and fresh-hunt every payload-controlled channel against the settled `032f47b` comparator bytes. Re-derive the historical baseline count from its counting inputs; record every arm id, channel, payload hash, comparator/scope hash, argv, result, exit, and instant. Enumerate every surviving exit-0 contradiction, with a declared reason or a one-function blocker; do not require the result to be zero open doors. Re-run the honest live join. The archived V10 replay command alone is not a substitute for a current-target replay.
- **C2 / operability — `[PENDING]`.** Re-run both X2 residuals: conflicting `expected`/`expected_value` values, and a lone non-string `status`. Record per-arm payload and comparator hashes, exact argv/output/exit, and either a named fail-closed exit or the explicit declared-with-reason disposition. Re-run the honest join and applicable fixture/self-test checks.
- **C3 / calibration — `[PENDING]`.** Append a post-R44 annotation to `corpus/knowledge/harness-independent-round41-census.md`; preserve the R41 measurement and mark each R43/R44 closure with its closing Git SHA. Re-derive quoted counts in that census, SCORECARD, and LOG R43–R44 from the cited bytes. Record the exact `recheck` invocation and its result; do not rewrite historical claims.
- **Deliberately not done by B1:** `[PENDING: list each unrun probe/check and why; distinguish it from a failed run]`.

## Landed changes

- Work commit: `[PENDING: full SHA; do not infer from dispatch HEAD]`.
- Changed paths: `[PENDING: derive from landing commit; include only observed changes]`.
- Landing HEAD/tree and exact reruns, outputs/exits, source/input hashes, and instants: `[PENDING]`.

## Before → after measurements

For R44 closure-red-before claims, use the frozen R44 dispatch bytes from `6881ce3` and landed closure bytes from `032f47b`. For R45 after-values, use the actual parent landing commit. Never substitute the currently modified worktree comparator. Every cell needs the exact command, result, source/input hashes, and timestamp.

| Claim / axis | Measurement | Frozen before | R45 landing after |
|---|---|---|---|
| C1 / depth | R41 census replay: arm count and classification totals | `[PENDING: replay command, input/driver hashes, output, exit, instant]` | `[PENDING: fresh current-target replay; same arm set; landing hashes/output/exit/instant]` |
| C1 / depth | Fresh channel-hunt: complete open-door list and classification | `[PENDING: exact comparator/payload/scope bytes, argv, outputs/exits, instant]` | `[PENDING: same hunt on landing bytes; list every survivor]` |
| C1 / depth | Honest join and comparator self-test | `[PENDING: command/output/exit/hash/instant]` | `[PENDING: rerun both on landing bytes]` |
| C2 / operability | `expected`/`expected_value` conflict; lone non-string `status` | `[PENDING: each arm's command, output, exit, payload/source hashes, instant]` | `[PENDING: same arms on landing bytes, or declared-with-reason evidence]` |
| C3 / calibration | Census annotation, quoted-number reconciliation, executable `recheck` | `[PENDING: source hashes and exact derived commands/results]` | `[PENDING: append-only result and recheck command/output/hash/instant]` |
| Gates | Live join, exact floors guard, corpus gates and applicable self-tests | `[PENDING: exact commands/outputs/exits/hashes/instants]` | `[PENDING: same gates on landing tree; retain red results]` |

## Open-door inventory

Include every arm, not only doors named in the registration. Separate open, closed, control, diagnostic, and declared trust-boundary cases; each entry needs its payload channel, exact input/result hashes, command/output/exit, and classification rationale.

| Door / arm | Channel and contradiction | Result / exit | Classification and reason | Evidence pin |
|---|---|---|---|---|
| `[PENDING]` | `[PENDING]` | `[PENDING]` | `[PENDING]` | `[PENDING]` |

- Reproducible residual count versus the R41 baseline: `[PENDING: both numbers re-derived from pinned counting inputs and commands]`.
- R44's claimed settled closure boundary versus any fresh survivor: `[PENDING: cite frozen source/output pins; do not infer from old reports]`.

## Axis verdicts

Landing evidence decides. Use only **improved**, **unchanged**, or **worse**. A surviving door is a finding, not a failed verification; an unrun check is not a pass.

- **Depth (C1):** `[PENDING: verdict + census, fresh-hunt, and honest-join citations]`.
- **Operability (C2):** `[PENDING: verdict + both X2 residual citations]`.
- **Calibration (C3):** `[PENDING: verdict + append-only census / quoted-number / recheck citations]`.

## SHONEN

Re-run the applicable evidence from `SHONEN.md` at the landing tree. Every reported count must carry the exact command, output, source hash, and instant; do not transfer a prior-round mark.

- `[PENDING: box 1 evidence and mark]`
- `[PENDING: box 2 evidence and mark]`
- `[PENDING: box 3 evidence and mark]`
- `[PENDING: box 4 evidence and mark]`

`[PENDING: preserve any stale claim, declared reason, or limitation that must remain visible]`
