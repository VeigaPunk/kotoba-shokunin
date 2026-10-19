# kotoba — round 44 report — SKELETON

> Scribe seat **B1**. Populate only from the round-44 seat reports and landing-commit reruns. Do not turn a prior-round result or a claim declaration into a current measurement. Every measured cell needs its exact command, output and exit, relevant source/input hashes, and instant. Keep unknowns `[PENDING]`; do not smooth mismatches or delete pending cells.
>
> B1 dispatch snapshot at `2026-10-19T18:03:10Z`: `git rev-parse HEAD` → `6881ce31912cf52982de733d18d25e7ab7aae5c4`; `git rev-parse 'HEAD^{tree}'` → `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`; `git status --porcelain=v1` → `?? .ufo/round-44/`.
>
> Claims source: `.ufo/round-44/claims.json`; `python3 -m json.tool .ufo/round-44/claims.json` exited `0`; `sha256sum .ufo/round-44/claims.json` → `cf18423f099475ba9733dd790a8de69ffe517c8e07d64a7b70b04b2ac81daf4f` at the snapshot above. It declares round 44, loop A, position 8 of 12, provider `openai-codex/gpt-6-luna-max`, and 24 seats; these are registration metadata, not B1 measurements.
>
> Frozen-before reference for any claimed comparator change: `git rev-parse '6fbbff5^{tree}'` → `87e2517d7db26cb9b6522c2feca5a7d2f4621fbe`; `git show 6fbbff5:verifiers/compare_harness_independent.py | sha256sum` → `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`; `git show 6fbbff5:verifiers/harness-independent-scope.json | sha256sum` → `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`, all at `2026-10-19T18:03:10Z`. These pins do not themselves reproduce a before result.
>
> Round-43 context pins at the same instant, from `sha256sum .ufo/round-43/scouts/R1.md .ufo/round-43/scouts/E1.md .ufo/round-43/scouts/R2.md`: R1 `6f7c17da1478fc4214eafdbb847adf73a28140d74d051830b42477630d0c3204`, E1 `f6cbb3c73436ea40940948e3e6a02073b3dc5bcbc25996b50ce252b867d6f7d5`, R2 `329f482297d80121ff2c4215d23382e84a19573185349b68431bf97a8a60464c`. Their results are historical context only.

Lane: `kotoba-shokunin`. Claims / axes: **C1 depth**, **C2 operability**, **C3 calibration** — `.ufo/round-44/claims.json` (digest above). Dispatch HEAD: `6881ce31912cf52982de733d18d25e7ab7aae5c4`. Dispatch tree: `f005c7f1f8a46c2ddbcb4e6a48ca949afb2de56d`. Work commit: `[PENDING: parent integration]`. Status: `[PENDING: populate from seat reports and landing-commit reruns]`.

## Work performed

- **C1 (depth) — `[PENDING]`.** On frozen bytes from `6fbbff5`, replay the expected-only record/full-copy arm, R1's record+map composition, and E1's mixed map+list composition. Record whether each record channel's id-set, and the union of its ids with its companion map, stays within the honest scope-derived set. A record-supplied scoped-out value or an oversized composed set must fail closed with exit 2 and a class-named diagnostic. Preserve the honest 24-row join and replace the non-representative 28-value fixture with a fixture for the real 24-row case. At landing, rerun the same exact payload bytes and controls; capture argv, input/output hashes, stdout/stderr, exits, and source pins. Claim target declarations are in claims C1 and are not outcomes.
- **C2 (operability) — `[PENDING]`.** Rerun the three R2 residuals: dotted-id top-level map shadow; contradictory `check`/`id`; contradictory `re_derived`/`observed`. For each, record the exact payload, comparator/scope pins, output and exit; require fail-closed named exit 2 or an explicit trust-boundary decision with reason. Rerun the honest join, comparator self-test, and assertion-floor guard.
- **C3 (calibration) — `[PENDING]`.** Re-derive the loader-class census from the live OMP registry and reconcile it against the surfaces extractor and pinned OMP binary SHA/mtime. Run and retain the surfaces gate before/after; if a substrate rebuild is claimed, provide git evidence of it before re-pinning. If the extraction is stale, repair and re-pin it. Name any unresolved residual with its evidence; do not infer a green gate from the census alone.
- **Deliberately not done by B1:** `[PENDING: list seat exclusions; distinguish unrun probes from failed probes]`.

## Landed changes

- Work commit: `[PENDING: full sha; do not infer from dispatch HEAD]`.
- Changed paths: `[PENDING: derive from the landing commit; include only observed paths]`.
- Landing tree, exact rerun commands, outputs, source hashes, and instants: `[PENDING]`.

## Before → after measurements

Use frozen dispatch bytes for every before-cell and the landing commit for every after-cell. The registered `before` / `after` / `counting` fields in `claims.json` are targets, not measured outcomes. Each filled cell must include exact command and argv, output and exit, source/input hashes, and instant. For C1's comparator before-run, use `git show 6fbbff5:<path>` bytes, not the changing worktree.

| Claim / axis | Measurement to report | Before (frozen bytes) | After (landing commit) |
|---|---|---|---|
| C1 / depth | Expected-only record, R1 composition, E1 mixed map+list: each arm's fail-closed class and exit | `[PENDING: exact command, payload/comparator/scope hashes, output, exit, instant]` | `[PENDING: same arms and payloads, landing hashes, output, exit, instant]` |
| C1 / depth | Honest join; real-24-row fixture; comparator self-test and exact assertion floors | `[PENDING: commands, outputs, exits, hashes, instants]` | `[PENDING: same controls, landing hashes, outputs, exits, instants]` |
| C2 / operability | Dotted-id map shadow, `check`/`id`, and `re_derived`/`observed` residuals | `[PENDING: per-arm command, output, exit, hashes, instant]` | `[PENDING: same arms, landing hashes, output, exit, instant]` |
| C3 / calibration | Live registry loader-class census, surfaces gate, OMP binary SHA/mtime pin attribution | `[PENDING: exact commands, outputs, source/binary hashes, instant]` | `[PENDING: same checks, landing/binary hashes, outputs, instant]` |
| Gates | Applicable whole gate battery, including floors and corpus gates | `[PENDING: exact commands, outputs, exits, hashes, instants]` | `[PENDING: exact commands, outputs, exits, hashes, instants]` |

## Axis verdicts

Landing-commit evidence is authoritative. Each axis gets only **improved**, **unchanged**, or **worse**, with a short evidence citation. A surviving door is a finding, not a failed verification; an unrun check is not a pass.

- **Depth (C1):** `[PENDING: verdict + record/map arms and honest-control citation]`.
- **Operability (C2):** `[PENDING: verdict + all three residual-arm citations]`.
- **Calibration (C3):** `[PENDING: verdict + live registry / surfaces / OMP-pin citation]`.

## SHONEN

Rerun the applicable evidence from `SHONEN.md` at the landing commit. For every reported count, include the command, observed output, source hash, and instant; do not carry forward a prior-round value without remeasuring it.

- `[PENDING: box 1 evidence and mark]`
- `[PENDING: box 2 evidence and mark]`
- `[PENDING: box 3 evidence and mark]`
- `[PENDING: box 4 evidence and mark]`

`[PENDING: retain any stale claim or constraint that must remain visible in the published report]`
