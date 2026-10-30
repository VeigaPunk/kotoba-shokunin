# Kb82V04Governance — E04/E05 unclaimed-maintenance review

Seat: reviewer, axes freshness/operability. Base `47dbe8781657de563ff867caca6244d28e3db504` (r81
non-author closure tip; lane read-only, all mutation inside a `--shared` scratch clone of that rev).
Scope: the two corpus-gate repair families the r80/r81 plans call E04 (report-pointer resolution +
report content identity, `verify_corpus_integrity.py`) and E05 (external-commit verified binding,
both corpus gates via `verifiers/external-commits.json`), their routed residuals, and the
governance principles the seat names: correction points to the SAME artifact, absence stays
absence, zero-class carry exact not arbitrary, no rewrite of appended history, no claim that
report identity is fixed.

## Method

Read `plans/round-82.md`, `plans/round-82-addendum-1.md`, `plans/round-80.md`, `plans/round-81.md`,
`corpus/lessons/round-81.md`, `corpus/lessons/round-81-verifier-spotcheck.md`, both gates, the
manifest, the baseline, the r81 refresh script, and `check_tip_battery.py` pins. Then rebuilt five
control worlds on the **current frozen gate bytes** in the scratch clone (world heads in
`build/Kb82V04Governance-receipts.txt`; raw gate JSONs `build/Kb82V04Governance-*.json`). Every
run captured its own exit (`cmd > f 2>&1; rc=$?`); the lane was never written; fixture commits used
the scratch identity only.

## Findings (severity-ordered)

**HIGH — R81-D1 binding skew is live and the W-A forged-binding class still reaches `commit_external`.**
`verify_corpus_integrity.py:684-708` requires the manifest-bound receipt to sha256-match AND name
the repository — it does **not** require the bound hash inside the receipt, while
`verify_corpus_independent.py:559` requires `sha in text and name.lower() in text`. On world
`wa-forge` (head `c05e80bb`, receipts attached): a test-authored receipt naming
`wrong-owner/wrong-repo` but **not** the hash, plus a manifest row and matching sha256, moves the
genuinely-absent `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` to `commit_external=3 /
commit_unresolvable=0` in the integrity gate while the independent gate on the same bytes keeps
`commit_unresolvable=1, external=2` — the two public gates disagree on one committed tree. The r81
L1 declined the ready patch (`Kb81E01Integrity.hashcheck-DECLINED`, sha256 `0ab1b089…`) because a
changed instrument forces a counter repin; the stricter variant never landed. Any r82 repair must
also add manifest pinning (`INSTRUMENT_PINS` at `check_tip_battery.py:132` still lacks
`verifiers/external-commits.json`) or the same bytes stay unpinned-but-admitted. Receipt: wa-forge
world JSONs; instrument lines cited above.

**MEDIUM — W-C padded-report class is live: `## SHONEN` + ≥400 B padding passes report identity.**
World `wc-pad` (head `096518d7`): an 816-byte blob (`## SHONEN` + 29 padding lines, no report
content) committed at `.ufo/reports/round-83/kotoba.md` and cited `HEAD:`-form is **not**
`report_dead` in either gate; the control `HEAD:.ufo/reports/round-84/kotoba.md` (absent
everywhere) reads dead in both. `report_content_ok` (`verify_corpus_integrity.py:298`) is a
marker-plus-size distinction arm, and the lane already knows it — the r81 spotcheck verdict is
"unprovable-but-better" and names this "a *narrower* hole". It is correctly **not** claimed fixed
anywhere I read; kept open is honest, claimed closed would be the defect. Receipts: wc-*.json.

**MEDIUM — rev-prefix grammar skew between the gates persists.**
World `wr-revprefix` (head `b3becc1c`): the token
`corpus/lessons/round-77-verifier-spotcheck.md:15:.ufo/reports/round-77/kotoba.md` reads
`report_dead` in the integrity gate but **LIVE** in the independent gate (no `REV_PREFIX_RE` match
→ bare-path downgrade → fleet hop to the real 8,547 B report). `HEAD@{1}:` prefixes read dead in
both. Same class as r81 residual critic World D; unclaimed at r82 base. Receipts: wr-*.json.

**MEDIUM — ellipsis laundering live on the committed regexes.**
`TRUNCATED_COMMIT_RE` `\A[0-9a-fA-F]{7,40}\u2026\Z` (`:162` integrity, `:147` independent): on world
`we-ellipsis` (head `1813ad39`), `` commit `0123456789abcdef0123456789abcdef01234567` `` →
`commit_unresolvable` +1 while the same 40 hex + `…` → `commit_truncated` (context, no red) in
**both** gates. The r81-routed smallest correction `{7,39}` moves no live class: all five committed
truncations are genuine short prefixes (`fb6a28ee…`, `955ffd5d…`, `661e538…`, `56b0764e…`,
`25cc5c7b…`). Receipts: we-*.json.

**MEDIUM — zero-class carry is class-level and count-unbounded; the r82 re-baseline must bind the
exact count.** `refresh-corpus-baseline.py` carries `--carry` as a `set` of check-ids; a carried
residual lands the observed count in `measured_against.note` prose only (line 311) — a second
defect in a carried class has no gate-visible signature (laundering-shaped gap, confirmed in
code). Positive boundary verified in code: `row["expect"] = 0` is unconditional for zero-mode
classes (line 285) — a baseline **can never** record a nonzero zero-mode value, and index classes
can never be carried (Refused). At r82 base the live red is exactly
`commit_unresolvable=1` (`corpus/lessons/round-81.md:8` citing the W-A fabricated commit
`8b1cc1b…`) and `unindexed=1` (`corpus/lessons/round-81-verifier-spotcheck.md`). **Absence stays
absence, correctly:** the fabricated hash is absent from lane+fleet and not in the manifest, so it
stays red — the honest disposition is a documented `--carry corpus.pointers.commit_unresolvable`
with the exact token and count `1` named in the round lesson/report, **never** an
`external-commits.json` row (a binding for this hash would itself be the W-A forgery) and never
editing the landed r81 lesson. The index class needs a coverage-map row, not a carry.

**LOW — SOFT_CROSS_CHECK tolerance asymmetry (r81 residual, unclaimed).**
`SOFT_CROSS_CHECK = INDEPENDENT_KEYS - HARD_CROSS_CHECK` (refresh script `:104`): a zero-class
disagreement between the two gates is printed and tolerated on the write path while the C1 W1
control refuses the same divergence on the battery path.

**LOW — spotcheck-identity anchored at `072048fa` (`check_tip_battery.py:111`).**
Files added after the pinned base are `info.append` only (`:338`); post-r73 spot-check files are
never identity-checked. Unclaimed residual, routed.

**PASS — correction points to the SAME artifact.** S250 opens `supersedes S230 —`, names the same
hash `7bb48f21…`, and binds the verified repository (`mistralai/mistral-vibe`, receipt
`S231.fetch.json` sha256 `e75f057a…` matching `external-commits.json`); S230 stays as the audit
trail. The r82 addendum's three corrections name the same artifacts they correct (the pins row in
`check_tip_battery.py:138-140`, the true intake base `47dbe87`, the stale "round51" premise in the
committed plan) and were filed as `plans/round-82-addendum-1.md` — a new file, not a rewrite of the
frozen plan.

**PASS — appended history not rewritten.** `plans/round-82.md` has one commit (`006a834`);
r81-era commits delete zero lines in `LOG.md`/`SCORECARD.md`; `corpus/lessons/round-7[7-9]*` and
`round-8[0-1]*` were touched only by their own round's commits (the one cross-round exception is
`fad752b` "round-17" fixing a path-capitalization typo inside round-8 files — a pre-convention,
content-neutral repair, recorded here for completeness). The r81 lesson's own edits (`e49dbbd`,
`23e838c`) predate the round report.

**PASS — no "report identity fixed" claim.** SCORECARD r81 row records C1 as honest-stop /
unprovable, score held; the spotcheck explicitly re-flags all six residuals I re-verified live.
The r82 addendum calls the checklist pin admission "governance maintenance, not a new 6/6
tip-battery claim" and states "No old report's frozen measurement is retroactively replaced".

**PASS — zero-class carry exactness, current instance.** The live `commit_unresolvable=1` has
exact documented evidence (the token, the line, and the W-A world it came from); carrying it
without that exact figure would be the arbitrary carry the seat warns against. The r82 plan's
re-baseline scope is consistent: equal-mode drift only (`tracked_files 157→158`,
`report_total 113→117`, `commit_total 47→50`), zero classes never carried without evidence.

## Residual risk / verification gaps

- I did not replay Kb81C01's byte-identical W-A/W-C artifacts; my worlds are independent
  constructions of the same classes on the current bytes — same conclusion, weaker byte parity.
- The r82 plan asks each routed defect to land "repaired with red/green evidence or explicitly
  retained open": my verdict is **retain open** for W-A/R81-D1, W-C, rev-prefix, carry-bound and
  spotcheck-anchor (each needs a counter repin or instrument change = a declared erratum, out of a
  leaf reviewer's reach); the `{7,39}` ellipsis bound is the only zero-blast-radius repair.
- Any E05 strengthening must answer W-A, not just R81-D1: even a hash-in-receipt check does not
  prove the receipt is a real fetch. Provenance for a receipt remains unclaimed machinery (W-A
  forged one trivially).
- Clone caveat, recorded in receipts: `corpus/lessons/round-81.md:29`'s `../../.ufo/…` pointer
  resolves only under the fleet layout (four-hop symlink) — it reads `report_dead=1` in scratch
  clones vs 0 in the lane. Location artifact of my environment, not a gate finding; future worlds
  should reproduce in a fleet-positioned sandbox.
- Not reviewed (out of seat scope): the C1 substrate re-pin worlds, the C2 checklist self-test
  repair, sibling w1 seat files (per the no-poll rule — e.g. the in-flight S248 `queued→mined`
  worktree edit, a permitted mutable-cell change that must carry its old→new lesson log).

VERDICT: E04/E05 maintenance is honestly disposed, not fixed — all six routed residuals reproduced live on the frozen bytes (W-A/R81-D1 HIGH; W-C, rev-prefix, ellipsis, carry-bound MEDIUM; SOFT-cross-check and spotcheck-anchor LOW); same-artifact corrections, absence-stays-absence, exact-carry discipline, and append-only history all verified clean; no claim of fixed report identity anywhere.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82V04Governance.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V04Governance-receipts.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82V04Governance-{base,wc-pad,wa-forge,we-ellipsis,wr-revprefix}-{integrity,independent}.json
