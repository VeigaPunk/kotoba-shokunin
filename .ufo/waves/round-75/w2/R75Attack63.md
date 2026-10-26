# R75Attack63 — attack on Facet 63

## Axes
Depth and operability: whether the asserted error-body gap exists in the measured counter, and whether the proposed check exercises it.

## Verdict
**Finding survives, with one qualification.** The evidence supports a real scope gap: the recorded-404 arm rejects a non-200 status, not an error-shaped body returned with status 200. Facet 63's proposed title-constant remedy is not established as necessary or sufficient by its cited evidence; it would pin all titles and requires a maintenance/re-pin path.

## Independent evidence
Measured lane revision is `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Reopened `verifiers/check_spec_craft.py` at that revision:

- `quote_line_problems` checks that a quote follows the first H1 and excludes headings, a subtitle blockquote before the first H2, and lines matching the `skill-creation/` link pattern (`:714-748`). It has no generic error-page/title classification.
- `page_unique` requires a located token to be unique among snapshots (`:903-907`); that is not an error-body test.
- fetch validation independently requires status `200`, byte count and digest agreement (`:915-930`).
- the sole 404 self-test flips a `200` log cell to `404` (`:1722-1725`); it does not test a body served with status 200.
- `_repin` rebuilds manifest/fetch log and swaps registry digests for edited snapshots (`:1200-1214`); `_run_spec` updates `PAGE_SHA` in world mode (`:1776-1790`). Thus a properly re-signed soft-404 world is a feasible test, not ruled out by the harness design.

The cited W6 fixture has the same error body in each named snapshot and `FETCH.tsv` marks all three `404`; the quickstart body is 705 bytes, SHA-256 `5694925680c9842fc9631f25ba7cf2a881ddf1503173d5237e16455144dfebad`. This fixture does not isolate body-shape rejection. The committed quickstart source snapshot instead has SHA-256 `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb`, so the frozen pin is a real additional obstacle for these specific round-74 bytes, not a general future-body guard.

## Detector and mutation status

Ran the bounded counter at the measured revision: `python verifiers/check_spec_craft.py --rev 65a5c7a663249e0522cc49e4a148424200d9ddfe` → exit 0; output includes `spec craft pages backed 3 of 3` and all three pages backed. A no-argument invocation exited 2 because `--rev <revision>` is required. No mutant was run: the actual proposed arm is self-test code that would require modifying a scratch copy and exercising its internal `_repin`/world harness; this probe did not claim a mutation kill. Therefore this baseline run is not evidence that the proposed soft-404 world is rejected. No lane bytes were changed; before/after evidence hashes above are those of the cited source and fixture files.

## Attack assessment
The central claim is materially supported by implementation: status-200 soft-404-shaped content has no general error-body rejection path, and the existing W6/404 test conflates content and status. Facet 63's exact predicted `3 of 3` output for its hypothetical bespoke world remains **unverified** here; the code read makes it plausible but does not substitute for running that mutation. Its title-constant control is an overbroad proposed remedy, not a demonstrated requirement: the evidence establishes absence of a body guard, not that pinning every title is the right guard. The report appropriately labels its predicted world as inference and notes frozen `PAGE_SHA` protects the three current snapshots.

Report trailer: Facet 63; independent evidence reopened at 65a5c7a663249e0522cc49e4a148424200d9ddfe; baseline counter run as reported; no mutant, no lane edits, no live fetch, no install, no scratch created.