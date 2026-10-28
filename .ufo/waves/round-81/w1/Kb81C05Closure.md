Kb81C05Closure — routed-defect closure audit (round 81, w1)

seat: Kb81C05Closure (critic, leaf). Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Scope: R80-D1..D4 from `corpus/lessons/round-80-verifier-spotcheck.md` § Routed defects. For each: the
exact mechanism this round claims closes it, then a scratch re-trigger of the defect class. Instance-only
closure = `improved-bounded` (Q21), not closed. All gate runs in scratch clones under
`/fast/scratch/hyaku/kotoba-r81/Kb81C05Closure/` (toplevel asserted per world); receipts:
`.ufo/waves/round-81/build/Kb81C05Closure-receipts.txt`. This seat scored NO claim after-value; every run
below is a control-class re-trigger on reviewer-visible bytes.

Patches audited: `build/Kb81E01Integrity.patch` (verify_corpus_integrity + shipped
`verifiers/external-commits.json` dict-form manifest) and `build/Kb81E02Independent.patch`
(verify_corpus_independent). Self-tests green: E01 `--self-test` 178 assertions, 0 failures; E02
109 assertions, 0 failures (measured by this seat on respun `d8bf88c8`; the seat's build log
reports the same pass verdict).

## R80-D1 (attribution): OPEN — no mechanism exists

Defect: the r80 report landed via hyaku sweep under the lane identity (`git log` attribution defect).
This round's claimed mechanism: none. `plans/round-81.md` never names R80-D1 or "attribution" (grep over
the plan: zero hits); the r80 lesson itself routed it as "record only; no lane fix possible" — the
orchestrator, not the lane, owns report authorship. No verifier can see it (author identity is not a
committed-bytes property the corpus gates check). Verdict: **OPEN** — unclosable by lane mechanics,
correctly not claimed. Any seat report or scorecard row that lists D1 as "closed" is false provenance.

## R80-D2 (stray `.ufo/wapes`): IMPROVED-BOUNDED — instance disposed, class has no gate

Mechanism: plan §C1 R3 moves `.ufo/wapes` (594 B untracked probe output) to
`.ufo/waves/round-81/dispositions/wapes.txt`; the lesson draft records the disposition sha256 must
survive (`build/Kb81S01Lesson.md` mistakes table, sha `930e2bd6…`).

Re-trigger (class): in scratch at base + committed `.ufo/wapee` (probe-shaped, committed outside
`corpus/`), `verify_corpus_integrity.py --repo .` exits 1 with only the pre-existing base drifts —
`tracked_files` counts `git ls-files corpus/` only (verifier line 639), so a stray under `.ufo/` is
invisible whether untracked (original shape) or committed (stronger shape). Receipts §D2a.

Class status: no mechanical gate watches probe artifacts outside `.ufo/waves/`. Two mitigations exist
but neither is a gate: (a) `build/refresh-corpus-baseline.py` refuses a dirty tree
(`status --porcelain --untracked-files=all`, lines 135–143) — an operational tripwire that only fires
when the refresh is run, and the stray can be cleaned manually first; (b) the lesson drafts candidate
criterion **Q76** ("a seat's probe/debug output lands only inside the wave dir") — `grep -c Q76
corpus/QUALITY.md` → 0, candidate only, not a row. Verdict: **IMPROVED-BOUNDED** per Q21 — the routed
instance is re-measured and disposed; the class is open with a named, unadopted candidate criterion.
That is the honest reading of "move the file": nothing catches the next `.ufo/wapee` except the
integrator's eyes.

## R80-D3 (instruments control-reachable, W8–W10): IMPROVED-BOUNDED — strong binding; two holes found and closed in respin

Claimed mechanism (plan §C1 R1+R2): report targets bind content identity (`## SHONEN` + ≥400 B);
external commits classify only via committed evidence manifest + receipt; line markers never exempt.

Re-trigger results (receipts §D3, §D3b, §D4A–C; the E02 column reflects respin `d8bf88c8`, not the superseded 7b37461a bytes):

| arm | E01 (integrity) | E02 (independent) |
|---|---|---|
| committed 7 B marker, `<rev>:<path>` object route | `report_dead` ✓ | `report_dead` ✓ |
| committed 7 B marker, worktree path route (round 98) | `report_dead` ✓ | `report_dead` ✓ |
| SHONEN-bearing 3.9 KB non-report at report path | green (declared bound) | green (declared bound) |
| pre-19 marker (round-10 path, existence contract) | green (declared bound) | green (declared bound) |
| forged manifest+receipt binding absent donor sha → `acme/widget` | `commit_external` (F4) | `commit_external` (F4) |
| contradictory manifest rows (same hash, two repos) | — | `commit_unresolvable`, bound={} ✓ fail-closed |
| manifest repo ≠ receipt repo | — | `commit_unresolvable` ✓ fail-closed |
| bare-list manifest (E03 superseded schema) | n/a | `unresolvable=3 external=0` ✓ fail-closed |
| legit binding (`7bb48f21…` → mistral-vibe, pinned receipt) | `commit_external` ✓ | `commit_external` ✓ |

Findings:
- F1 (E02 defect, CLOSED in respin `d8bf88c8`): the first published patch exempted the "path" route
  from `report_identity_ok`, so a worktree marker at any `.ufo/reports/round-N/*.md` stayed green —
  the plan binds identity on "path OR object". Reported to the seat 2026-10-27; the respin adopted
  E01's round≥19 bound on all routes; re-verified `dead=2` on the new bytes. The duplicate
  `_committed_blob` definition is functionally equivalent and intentionally left in frozen bytes;
  the seat recorded residual R6 / next-round cleanup (post-freeze edit would fail `instrument-pin`).
- F2 (schema divergence, CLOSED): E01 parses `manifest["commits"]` (dict, `repository`/`receipt`/
  mandatory `receipt_sha256`, 40-hex only); E02's first bytes tolerated a bare list + `repo`/`evidence`
  + optional pin — a future shape change would flip one gate silently. The respin asserts the dict-only
  contract; re-verified bare-list → fail-closed. E03's published list-form JSON is SUPERSEDED (their
  build note; E01's dict is canonical). Deliberate remaining divergence, stated by the seat: E02 also
  requires the committed receipt bytes to carry hash AND repository (E01 pins the digest and checks
  the repository) — strictly stronger, no live difference on the single S231 record.
- F3 (declared bound, verified green): report-shaped non-reports pass content identity on all routes in
  both gates — the mechanism is explicitly a marker distinction, so the surviving class (fabricated
  report-shaped content) is disclosed, not hidden.
- F4 (declared bound, verified green): a committed manifest+receipt pair that consistently binds an
  absent hash to a repo it does not own is admitted by both gates — provenance is review-trust
  (committed bytes), not mechanical. Unbound/mismatched/contradictory bindings all fail-closed.
- F5 (correct directional fix, measured): the `HEAD:.ufo/reports/round-77/kotoba.md` token that was
  `report_dead` at base revives under both gates — the fleet object resolves and carries `## SHONEN`
  (8547 B). The `7bb48f21…` citations classify `commit_external` on the pinned S231 receipt. Verified.

Verdict: **IMPROVED-BOUNDED** — the W8–W10 classes are killed where the plan binds them (object route,
fleet fallback, manifest/receipt consistency); survivals are the plan's declared distinction bounds plus
F1/F2, which are fixable before integration, not tradeoffs.

## R80-D4 (S230 wrong-repo anchor; future instances): IMPROVED-BOUNDED — bound-but-wrong survives

Claimed mechanism: R2 manifest binding + R5 S250 supersede row (`supersedes S230 —`, records the
verified `mistralai/mistral-vibe` binding; S230 kept append-only). Verified against bytes: E03's
re-derivation (`build/Kb81E03ExtManifest-fetch.txt`) re-ran `git ls-remote` live — mistral-vibe
`refs/heads/main` and `HEAD` both `7bb48f21…` at 2026-10-28T02:28Z; pi-mono's 4120 advertised refs
contain the token zero times; the commit-pinned raw README is byte-identical to snapshot S231-vibe.md
(sha256 `fc48a5db…`). The E03 receipt genuinely binds repo→hash.

Re-trigger (future wrong-repo anchor):
- caught: an absent hash cited with NO manifest row, an `owner/repo@` marker, or a row whose manifest
  entry contradicts the receipt → `commit_unresolvable` (red). Verified under E02, same code in E01.
- survives: (a) the S230 row prose itself keeps asserting `badlogic/pi-mono` for a hash the manifest
  binds to `mistralai/mistral-vibe` — the gate never compares row prose to manifest repo, and append-only
  makes that permanent by design; a future row doing the same silently agrees. (b) a consistent
  wrong-repo manifest+receipt pair (manifest says `acme/widget`, receipt names `acme/widget`, hash
  belongs elsewhere) is admitted — F4 above, measured on both gates.

So: the gate-visible cause (`commit_unresolvable` on an absent hash) is closed for bound and unbound
arms alike; the semantic cause (wrong-repo attribution reaching readers) survives at two layers —
append-only prose vs. manifest, and manifest provenance vs. repo truth. The S250 supersede row +
reviewed evidence is the fix for the semantic layer, and it is human-visible, not gate-enforced.
Verdict: **IMPROVED-BOUNDED** — honest if declared; the plan's "verified binding" phrase covers
evidence-to-manifest consistency, not repo-truth, and the audit trail (S250) carries the truth. If a
seat report claims D4 closed outright, it overstates the gate's reach.

## Cross-cutting notes for the L1

- E01's patch also lands `verifiers/external-commits.json` (blob `402ac290…`, pin
  `e75f057a…` = committed receipt bytes, E03-verified). E03's list-form candidate is superseded —
  integrate E01's file, not E03's.
- E02's respin (`d8bf88c8`) fixed F1+F2 and is the byte set to pin; the seat intentionally retains the
  duplicate `_committed_blob` definition as disclosed residual R6 because its instrument blob is
  frozen/pinned (next-round cleanup). Its blob sha `59602942…`; no further edits without re-freezing.
- Q76 (stray probe artifacts inside wave dirs) is a real candidate criterion for the next round; this
  round only disposes the instance.
- Tooling: no installs performed or needed; stdlib `python3 -B`, `git`, `sha256sum` throughout.

VERDICT: D1 OPEN; D2, D3, D4 IMPROVED-BOUNDED. E02's path-route and manifest-schema defects were fixed in the audited respin; remaining gaps are the unguarded stray-artifact class and the declared content-identity and evidence-provenance bounds.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81C05Closure.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81C05Closure-receipts.txt
