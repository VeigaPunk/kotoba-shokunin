# kotoba — round 41 report (2026-10-19) — SKELETON v1

> Scribe seat **B01**. Fill from `.ufo/round-41/scouts/` and re-run all landing-dependent
> checks at the landing commit. This is a verification round: do not turn a prior-round
> claim into a current measurement. Every measured value must carry its command, observed
> output, frozen source bytes / sha, and run instant. Keep unknowns `[PENDING]`; do not
> smooth mismatches or silently delete pending cells.
>
> Dispatch snapshot immediately before this skeleton was written: `date -u +%Y-%m-%dT%H:%M:%SZ`
> → `2026-10-19T16:32:55Z`; `git rev-parse HEAD` →
> `b1be35f9522f21c0c5b39879358a011806ab9200`; `git rev-parse 'HEAD^{tree}'` →
> `8bb24450a9c500c427019c7147013b4946525b09`; `sha256sum .ufo/round-41/claims.json` →
> `e27fa002404646d5ddf901cb2efb00232019d63bf365c3888248e3316c27d5a6`.

Lane: `kotoba-shokunin`. Round / loop / position and claim mapping: `.ufo/round-41/claims.json` (digest above).
Dispatch HEAD: `b1be35f9522f21c0c5b39879358a011806ab9200`.
Work commit: `[PENDING: integrator's landing commit sha]`.
Claims: **C1** depth · **C2** operability · **C3** calibration.
Status: `[PENDING: populate from the seat reports and landing-commit re-run]`.

## Work performed

- **C1 (depth) — `[PENDING]`.** Cite the union battery and fresh channel-hunt, with each
  listed payload-controllable channel's open/closed verdict, reproducer, command, exit,
  frozen source sha, and run instant. State whether any new hunt found a channel outside
  the census. Re-run the honest-payload comparator control.
- **C2 (operability) — `[PENDING]`.** Cite the full confinement / override residual matrix,
  the two trust-boundary checks, and the guard-self-test deletion probe. State whether the
  guard's own self-test count is floored or formally remains un-floorable, and include
  the exact floors reading from the guard run.
- **C3 (calibration) — `[PENDING]`.** Re-derive every quoted number in
  `corpus/knowledge/harness-independent-round37.md`, `SCORECARD.md`, and `LOG.md`
  sections for rounds 37–40 against the measured tree. List each mismatch and its
  append-only correction, or record that none was found.
- **Deliberately not done:** `[PENDING: record exclusions and why]`.

## Landed changes

- Work commit: `[PENDING: full sha; do not infer from dispatch HEAD]`.
- Files changed at landing: `[PENDING: list from the landing commit, with paths]`.
- Landing-tree state and re-run instant: `[PENDING: command + output + sha/tree]`.

## Before → after measurements

Use frozen dispatch bytes for every before-cell and the landing commit for every after-cell.
Do not use a live-tree reading as a substitute for a frozen before-state.

| Claim / axis | Measurement to report | Before (frozen dispatch bytes) | After (landing commit) |
|---|---|---|---|
| C1 / depth | Union-battery arms: surviving channels from R1, X2, T1, W1, and V1; include each reproducer and exit | `[PENDING: command, output, frozen sha, instant]` | `[PENDING: same arms re-run, command, output, landing sha, instant]` |
| C1 / depth | Fresh channel-hunt completeness and honest-payload comparator control | `[PENDING: command, output, frozen sha, instant]` | `[PENDING: command, output, landing sha, instant]` |
| C2 / operability | V3 confinement / override matrix, declared trust boundaries, and guard-self-test deletion probe | `[PENDING: command, output, frozen sha, instant]` | `[PENDING: command, output, landing sha, instant]` |
| C2 / operability | Floors registry and exact floors-guard result | `[PENDING: command, output, registry sha, instant]` | `[PENDING: command, output, registry sha, landing sha, instant]` |
| C3 / calibration | Re-measured corpus-document, SCORECARD, and LOG values; stale or over-broad “closed” statements | `[PENDING: command, output, source sha(s), instant]` | `[PENDING: command, output, source sha(s), landing sha, instant]` |

## Axis verdicts

Landing-commit evidence is authoritative. Each verdict must be only **improved**,
**unchanged**, or **worse**, with a short evidence citation; a surviving door is a finding,
not a failed verification.

- **Depth (C1):** `[PENDING: verdict + census / hunt citation]`.
- **Operability (C2):** `[PENDING: verdict + residual-matrix / guard citation]`.
- **Calibration (C3):** `[PENDING: verdict + reconciliation / errata citation]`.

## SHONEN

`[PENDING: re-run the applicable SHONEN evidence at the landing commit; include a command,
observed output, source sha, and instant for each reported count. Do not carry forward a
prior-round value without re-measuring it.]`

- `[PENDING: box 1 evidence and mark]`
- `[PENDING: box 2 evidence and mark]`
- `[PENDING: box 3 evidence and mark]`
- `[PENDING: box 4 evidence and mark]`

`[PENDING: note any stale SHONEN claim or constraint that must remain visible in the published report]`
