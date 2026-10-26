# R75Attack08 — falsification of R75Facet08 (wave 2)

Target: `.ufo/waves/round-75/w1/R75Facet08.md` (calibration/operability facet on the r74 closure's C1 page-fidelity row).
Measured revision: lane `kotoba-shokunin` master `65a5c7a` (confirmed `git rev-parse --short HEAD` = `65a5c7a`; log subject "round-74: hyaku run-8 orchestrator salvage …").

## Verdict

**FACET SURVIVES.** Its central factual claim — the r74 closure text is calibrated: verdict bounded to coverage `improved`, "Re-measured" vs "Evidence-verified only" drawn explicitly, page fidelity labelled a judgement — is verified against committed bytes at `65a5c7a`. All four citations land at the exact claimed lines, the cited counter receipts exist with the recorded values, and the facet's proposed controls are non-vacuous (the one artifact it asks for does not exist anywhere in the lane). Three minor findings below; none overturns the facet.

## Central claim, re-opened at committed bytes

1. `corpus/lessons/round-74-verifier-spotcheck.md:58` — verified. The page-fidelity row reads exactly as summarized: "~44 line pointers: best-practices `:78 :90-92 :96 :111 :119 :122 :129 :147 :149-159 :167 :231 :247-249`, using-scripts `:9 … :299-304`, quickstart `:13 … :64-74`"; "rule groups faithful 5/5 + 5/5 + 5/5, table rows 3/3; **0 overreach, 0 unsupported**"; the entry's hedges recorded as accurate. File is clean at HEAD (`git status --porcelain` empty for it); added post-`ec2c1d3` in commit `314e4a1` ("round-74 verifier spot-check (integrator, hyaku): non-author admit/reject") — consistent with it being r74's closure artifact, exactly as the facet treats it.
2. `:63-64` — verified: "Re-measured: rows, base sweep, snapshot digests, live bytes, page fidelity, line count. Evidence-verified only: the counter's `0 of 3 → 3 of 3` and its 250-assertion self-test. **Verdict: coverage `improved`.**" The facet's "0/3→3/3" and "coverage `improved`" quotations are faithful.
3. `corpus/QUALITY.md:36-37` — verified: Q25 at line 36 (counter shown able to fail on a content mutant; content guard whose exit changes), Q26 at line 37 (every headline clause turned on by counter output or a falsifiable cited guard). The facet's one-line characterizations are accurate.
4. `corpus/knowledge/skill-eval-artefacts-round70.md:74-80` — verified **at committed HEAD bytes** (`git show HEAD:…`, lines 74-80): "## Scope and refusals" (:74), refusal of any native-client-execution claim (:76-78), opt-in `skill-creator` plugin distinguished from client behaviour (:78-81). **Hazard found and resolved:** this file is dirty in the working tree (` M`); the diff appends a "## Round 75 correction" section at lines 86-88 only. The cited 74-80 range is byte-identical at HEAD, so the facet's "committed source row" framing stands. Recorded as a re-opener caveat: any citation at lines ≥86 of that file is currently working-tree-only.
5. `plans/round-74.md:3-17` — verified: ":3 Frozen before any wave seat scored any claim"; ":13 Round shape: **two v1 waves**" with wave-1/wave-2 description at :14-16. The facet's historical-not-frozen-r75 handling is correct.

## Receipt / control tests performed (read-only)

- `.ufo/waves/round-74/receipts/c1-base-freeze.txt` exists: `spec craft pages backed 0 of 3`, exit=1 at base `1e03d19`, counter sha256 `bd34ec1bfded53706921fd7c0bb833712daa3d4f9f98812ee81dfc6765769d01`.
- `receipts/c1-selftest-freeze.txt` exists: `--self-test exit=0` with PASS arms including must-fail mutants (token-stuffed row, queued-not-mined, prefix-token, another page's token).
- Committed `verifiers/check_spec_craft.py` hashes to `bd34ec1bfded…` — equal to the hash recorded in both freeze receipts (Q24-style instrument-hash check passes), corroborating spotcheck `:60`, which the facet's calibration reading leans on.
- `receipts/c1-data-559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd.txt` exists (name matches spotcheck `:60`).
- Lane-wide search for the distinctive pointer strings (`149-159`, `247-249`, `299-304`): the only in-lane hit is the spotcheck's own cell (line 58; other hits are unrelated round-33/kengaku content). **No committed reviewer artifact enumerates the ~44 pointers with per-clause verdicts** — the two closure reviewer seats' outputs survive only as the lesson's summary (spotcheck `:18-19` says their outputs "are summarised below with their commands"). The facet's auditability caveat is therefore real, and its proposed reviewer-artifact control is non-vacuous.
- No counters were executed and no live fetch was made; the facet asserts no counter behavior, so none was needed. LSP device: not present in this seat's tool inventory (markdown/corpus surface; no language server applies) — evidence is committed-byte textual, per the fallback rule.

## Findings (minor; none fatal)

- **F1 (overstated gap, low severity).** Facet08: the cell "does not enumerate all ~44 pointers". Expanding the visible ranges gives 45 pointers (best-practices 26 + using-scripts 7 + quickstart 12), already ≈ the claimed ~44; the `…` gaps block exact reconstruction but the cell is nearly complete. The claim is literally true (not all pointers individually visible) but overstates the enumeration deficit. The load-bearing half — reviewer outputs not reproduced — is confirmed (see search above).
- **F2 (unnamed tension, low severity).** The same closure lists "page fidelity" under "Re-measured" (`:63`) while its row labels it "the judgement" (`:58`). The facet's calibration reading remains accurate and its Limits section already prices in the consequence (medium auditability confidence); it simply never names this internal wording tension.
- **F3 (partial duplicate, medium relevance to wave dedup).** R75Facet25 cites the same four anchors (spotcheck `:58`, `:60-64`; QUALITY `:36-37`; round70 `:76-80`) and reaches the same calibration conclusion. Distinct deltas keep them separate findings: Facet08 contributes the auditability gap (reviewer outputs, pointer enumeration) and the reviewer-artifact + falsification-arm control; Facet25 contributes Q23 (`QUALITY.md:34`) and the claim-to-source-table control. Facet10 overlaps moderately on the C1-recheck surface (`:46-64`, improved verdict, evidence-verified distinction) with a different thesis (staleness/category-confusion). Neither of the two fully subsumes the other.
- **F4 (already-implemented sub-control, low severity).** The facet's control clause "preserve the exact committed source snapshot hash" is already standard corpus practice (snapshots pinned via `MANIFEST.sha256`; spotcheck re-check row "snapshots pinned"). Non-novel; the novel deltas are the reviewer artifact and the Q25/Q26 falsification arm.

## Residual risk / verification gaps

- The ~44-pointer fidelity result itself remains unverifiable from committed bytes (no per-clause reviewer artifact exists) — this is the facet's own stated limit, confirmed, not a defect in it.
- The counter's `0 of 3 → 3 of 3` was not re-executed here (read-only wave posture; receipts + instrument hash + self-test receipt corroborate the recorded values). A wave that needs live proof can run `python3 -B verifiers/check_spec_craft.py --rev <base>` and `--self-test` and compare to the receipts.
- `skill-eval-artefacts-round70.md` is dirty; if the pending round-75 correction is committed with lines inserted above 74, that file's citations must be re-anchored.

Report path: `.ufo/waves/round-75/w2/R75Attack08.md`. No edits outside this report; no scratch used (nothing to clean); no commits, pushes, or jj mutations.
