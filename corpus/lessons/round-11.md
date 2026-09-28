# Lessons — round 11

Round: 11. Axis move: **consistency** (declared calibration sub-axis). Artifact
half: `corpus/knowledge/corpus-integrity-round11.md`; machine half:
`verifiers/verify_corpus_integrity.py` + `verifiers/corpus-baseline.json`.
landing hash `4dd7753`.

## Worked

- **Counting commands are claims, and they expire silently.** Three separate
  counting recipes in this repo's own artifacts could not express the class they
  named: a pattern whose `[0-9]` could never match a two-digit round (false zero
  *with the defect present*), a `comm` whose regex could not tokenize a brace row
  (three indexed files reported as unindexed), and a `grep` for `../.ufo` that
  also matches `../../.ufo` (identical count before and after the repair). The
  fix is not a better command but a committed one: `--self-test` pins the matcher
  model, and the check ids name the property.
- **Scope the class before asserting over it.** A "do all pointers resolve?"
  check over every relative-looking token fails on this corpus for six distinct,
  legitimate reasons (see the artifact's exclusion table). The landed class is
  narrow — `.ufo/reports/round-N/*.md` tokens that are not placeholders or
  schematic — and covers 19 live pointers plus the 10 that were dead.
- **A digest is not a commit.** `SKILL.md` @ `143fe473…` was an **md5**, printed
  with the same `@` notation used for commits; `cat-file ^{commit}` on it fails by
  construction. The repair is a label (`@ md5 … (commit 3b029b8)`), not a hash
  change. This is the class of defect that a resolver check would have flagged as
  a false positive, which is why that check was rejected rather than landed.
- **Reproduce the before-state by cloning.** An uncommitted repair reads as
  "agree" to any check that reads the working tree, and a synthetic
  `archive + init` tree reports 18 unresolvable commits that do not exist in
  history. `git clone --no-hardlinks` is the honest before-state.

## Did not work / rejected

- **A revision-pin resolvability check** (`@ <hex>` must resolve as an object):
  rejected because the same notation carries digests; a label classifier would be
  a second convention with no fixture. The two offending sites were relabelled.
- **`comm` with `sort -u` on the README side**: the two sides are not the same
  kind of set — one is backticked tokens from a table cell, the other is paths
  from the index. Sorting cannot fix a tokenizer mismatch. Brace expansion +
  `fnmatch` can.
- **Reporting the `/tmp` quota failure as a property of the round-10 command**:
  the observed `comm: file 1 is not in sorted order` came from a truncated
  scratch file under disk pressure. Recorded as `[UNVERIFIED]`, not as the defect;
  the defect that reproduces is the brace row.

## Carry forward

- `LOG.md`, `SCORECARD.md` and `SKILL.md` carry report pointers and commit
  citations that no check reads (the verifier scans tracked `corpus/*.md` only).
- 18 of the 19 checked pointers are host-absolute: portable in this corpus,
  brittle across hosts.
- `SKILL.md`'s 39 checklist boxes remain lane-attested — machine-checked counting
  is not machine-checked execution.
- Two `equal`-mode check ids fire on legitimate corpus growth; the re-record
  procedure is manual and documented in the artifact.

## L2 lanes (13 this round; MISSION.md floor 8)

One batch of 9 at round start: `ScoutIndexBefore` (before-state instrument, and
the author of the `comm` defect repro), `ScoutPointerCensus` (four-form pointer
census + exclusion list), `ExecVerifierDraft` (the script), `ExecArtifactDrafts`
(prose drafts), `PlanRound12`, `ConnectorSiblingOverlap` (kumitate
`scripts/cite-check.mjs` overlap routed to the aggregator), `CriticPreFalsify`
(band-9 strict ruling), `SentinelCrossDomain` (four external defects re-verified),
`ReviewTraceability` (27 checks mapped to 38 claims, 14 uncovered). One batch of
4 after landing: `ColdRunRecord` (non-author cold run → `cold-run-round11.md`),
`FaultInjection`, `CheckFalsifiability`, `CriticPostFalsify`.