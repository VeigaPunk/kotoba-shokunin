# kotoba — round 43 report — SKELETON

> Scribe seat **B1**. Fill from the round-43 scouts and re-run every landing-dependent
> check at the landing commit. Do not turn a prior-round claim into a current measurement.
> Every measured value needs its exact command, observed output, frozen source bytes / sha,
> and run instant. Keep unknowns `[PENDING]`; do not smooth mismatches or delete pending
> cells.
>
> Dispatch snapshot immediately before this scaffold was written: `date -u +%Y-%m-%dT%H:%M:%SZ`
> → `2026-10-19T17:24:31Z`; `git rev-parse HEAD` →
> `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`; `git rev-parse 'HEAD^{tree}'` →
> `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`; `git status --porcelain=v1` →
> `?? .ufo/round-43/`.
>
> Claim metadata and registered target statements are declarations, not B1 measurements.
> Source: `.ufo/round-43/claims.json`; `python3 -m json.tool .ufo/round-43/claims.json`
> exited `0`; `sha256sum .ufo/round-43/claims.json` →
> `c1185d5b19193baf1975068634491883b8dbf6225c4aef5205478d9e88ec898e` at
> `2026-10-19T17:24:31Z`.
>
> Census arm names and reachability ordering are reference context only, not current
> measurements. Source: `corpus/knowledge/harness-independent-round41-census.md`;
> `sha256sum corpus/knowledge/harness-independent-round41-census.md` →
> `b06742e4dff0093b28d0a621cd3475799d76b5464ea23b785bc53fe20b75f79f` at
> `2026-10-19T17:24:31Z`. Report-shape reference: `.ufo/reports/round-41/kotoba.md`,
> SHA-256 `e8bc58d8249e5041f8ed2e6537cb351f5f62b0a7a7c8b490667ba093299dd68f`;
> `sha256sum .ufo/reports/round-41/kotoba.md` at the same instant.

Lane: `kotoba-shokunin`. Round / loop / position / provider / seat count: read from the
claims source above; do not infer them from a later worktree state.
Dispatch HEAD: `1c79e8698a5a297f32fda4d71f0a23be2ec4248f`.
Dispatch tree: `cd9d3814e8cdb664081746aa17e0557ddaa3e6c8`.
Work commit: `[PENDING: integrator's landing commit sha]`.
Claims: **C1** depth · **C2** operability · **C3** freshness — `.ufo/round-43/claims.json` (digest above).
Status: `[PENDING: populate from seat reports and landing-commit re-runs]`.

## Work performed

- **C1 (depth) — `[PENDING]`.** Re-run the C02 top-reachability heldout payload-map arms
  named in the frozen census: `heldout-expected-only-full-copy`,
  `heldout-flat-dotted-map`, `heldout-nested-checks-map`,
  `heldout-nested-expected-wrapper`, `heldout-nested-observations-wrapper`, and
  `heldout-wrapper-precedence-expected-over-observations`. Record each arm's exact argv,
  output, exit, class name, frozen comparator / input hashes, and instant. Separately run
  the honest-payload join control. The registered requirement is that a scoped-out row
  cannot receive a payload-supplied value and an oversized flat/nested map fails closed;
  verify against the claim source rather than treating its declared targets as results.
- **C2 (operability) — `[PENDING]`.** Re-run the registered X2/V03/V04/H02 arms for
  un-contract top-level fields, within-record `status` / `state` disagreement, and
  `secondary_agree` bounds. State whether foreign fields are rejected or formally ignored,
  include named exits and exact outputs, and re-run the honest join. The claim's before/after
  text is pre-registration only.
- **C3 (freshness) — `[PENDING]`.** Re-derive the blockquote-fence, unclosed-at-EOF, and
  mixed-character closer cases against the declared cmark oracle. Run the shape battery on
  copies through both corpus instruments if a silent false-PASS is present; otherwise record
  the actual classification. Re-run live incidence, stdout byte-invariance, and floors.
- **Deliberately not done:** `[PENDING: list exclusions and why; distinguish a probe not run
  from a failed probe]`.

## Landed changes

- Work commit: `[PENDING: full sha; do not infer from dispatch HEAD]`.
- Changed paths: `[PENDING: derive from the landing commit; include only observed paths]`.
- Landing tree, exact re-run commands, outputs, source hashes, and instant:
  `[PENDING]`.

## Before → after measurements

Use frozen dispatch bytes for every before-cell and the landing commit for every after-cell.
The registered `before` / `after` / `counting` fields in `claims.json` define requested
measurements, not measured outcomes. Do not substitute a live-tree reading for frozen bytes.
Each filled cell must include the exact command, output, relevant frozen source/input sha,
and instant.

| Claim / axis | Measurement to report | Before (frozen dispatch bytes) | After (landing commit) |
|---|---|---|---|
| C1 / depth | Each heldout payload-map arm and its fail-closed class | `[PENDING: exact command, output, frozen shas, instant]` | `[PENDING: same arms, exact command, output, landing shas, instant]` |
| C1 / depth | Honest-payload comparator control | `[PENDING: command, output, frozen shas, instant]` | `[PENDING: command, output, landing shas, instant]` |
| C1 / depth | Comparator fixtures / self-test and exact floors | `[PENDING: command, output, source shas, instant]` | `[PENDING: command, output, landing shas, instant]` |
| C2 / operability | Foreign fields, `status` / `state`, and secondary-agreement bound | `[PENDING: each arm, command, output, frozen shas, instant]` | `[PENDING: same arms, command, output, landing shas, instant]` |
| C3 / freshness | cmark classifications and both instrument copies | `[PENDING: oracle + gate commands, outputs, frozen shas, instant]` | `[PENDING: same shapes, commands, outputs, landing shas, instant]` |
| C3 / freshness | Live corpus incidence, stdout byte-invariance, and exact floors | `[PENDING: commands, outputs, source shas, instant]` | `[PENDING: commands, outputs, landing shas, instant]` |
| gates | Whole applicable gate battery | `[PENDING: exact commands, outputs, source shas, instant]` | `[PENDING: exact commands, outputs, landing shas, instant]` |

## Axis verdicts

Landing-commit evidence is authoritative. Each verdict is only **improved**, **unchanged**,
or **worse**, with a short evidence citation. A surviving door is a finding, not a failed
verification; an unrun check is not a pass.

- **Depth (C1):** `[PENDING: verdict + heldout-arm / honest-control citation]`.
- **Operability (C2):** `[PENDING: verdict + field / alias / bound citation]`.
- **Freshness (C3):** `[PENDING: verdict + cmark / corpus-gate citation]`.

## SHONEN

Re-run the applicable evidence from `SHONEN.md` at the landing commit. For each reported
count include its command, observed output, source sha, and instant; do not carry forward a
prior-round value without re-measuring it.

- `[PENDING: box 1 evidence and mark]`
- `[PENDING: box 2 evidence and mark]`
- `[PENDING: box 3 evidence and mark]`
- `[PENDING: box 4 evidence and mark]`

`[PENDING: retain any stale claim or constraint that must remain visible in the published report]`
