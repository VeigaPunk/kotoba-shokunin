# Kb81C04Honesty — claim-admission honesty audit (round 81, w1)

Seat: critic. Scope: plans/round-81.md read cold; audit questions (a)–(e). All findings
grounded in lane bytes at base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; commands and
exits quoted. No counter was run for an after-value (none exists yet); every mechanism
claim below is read out of committed verifier source or committed receipts.

Evidence base (all exits observed this audit, lane repo read-only):
- `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`: `guards 5 of 5; tip battery
  exit 0: 4 of 6`; reds = `verify_corpus_integrity.py` exit 1 (0.2s),
  `verify_corpus_independent.py` exit 1 (0.5s); other four gates exit 0.
- `verifiers/check_tip_battery.py` head+body: `BATTERY` = 6 instruments
  (gate_registry, assertion_floors, skill_checklist, corpus_integrity,
  corpus_independent, correction_sweep); `LINE_CAP = 40` (line 111) feeds BOTH
  `added > LINE_CAP` (line 316) and `deleted_lines > LINE_CAP` (line 318);
  `INSTRUMENT_PINS` = 6 keys, integrity pin-tuple currently 2 shas (base + r80 blob).
- `verify_corpus_integrity.py:264-277`: report-pointer resolution is filesystem-only
  (`resolve_pointer` → `is_file`), fleet hop only for tokens literally starting
  `.ufo/reports/`. `:61-68`: `commit_truncated` (U+2026) and `commit_quoted` arms exist
  and are exempt from `commit_unresolvable`.
- Fleet/lane resolution test (this audit):
  `git -C <lane> cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md'` → fatal, absent
  in lane at HEAD; `git -C <fleet> cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md'`
  → exit 0, `cat-file -s` = 8547 B, `grep -c '## SHONEN'` = 1. Lane history carries no
  `.ufo/reports/round-77/` at all (`git log --all -- .ufo/reports/round-77/` empty).
- `git status --porcelain` at lane: `?? .ufo/wapes` (untracked).
- `check_gate_registry.py:16-25`: universe = every blob directly under `verifiers/`;
  conformance = exactly one `## Gate registry` row agreeing with the blob.
- `check_sources_append_only.py`: exists, walks SOURCES.md per commit; NOT in BATTERY.
- `corpus/SOURCES.md`: S230/S231 rows both carry `7bb48f213ac677f943d5c791199ed3dddf302f00`
  (lines ~171-172); S230's own fetch receipt (`.ufo/waves/round-79/snapshots/S230.fetch.json`)
  states pi-mono `main = bb65e3e4971…`, so the row's revision anchor is false on its
  face; S231.fetch.json's ls-remote pins `7bb48f21…` to `mistralai/mistral-vibe` ✓.
- S248 (SOURCES.md:189): URL `code.claude.com/docs/en/agent-sdk/skills.md`, fetched
  2026-10-27, HTTP 200, 28395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca
  402be9b886946f01e5a2`; located quotes already include `allowedTools`.
- r80 lesson `corpus/lessons/round-80-verifier-spotcheck.md`: carries exactly 2 report
  pointers, both `.ufo/reports/round-80/kotoba.md`; no `HEAD:` token; no other corpus
  file references it (grep over corpus/ → only itself).
- `floors-registry.json`: 17 rows, none on corpus paths → no floor guards SOURCES.md
  or the lessons dir.
- `.ufo/waves/round-81/receipts/` at audit time: `census-before.txt`,
  `tipbattery-base-dot.txt` only (no absolute-form base receipt, no freeze-shas.txt —
  expected mid-wave, recorded for freshness).

## (a) Is C1's `6 of 6` reachable by a do-nothing control — and which repairs are load-bearing?

Base decomposition (which gate owns which red):
- integrity: `tracked_files` 155≠154, `unindexed` 1 (round-80 lesson), `report_total`
  111≠109, `report_dead` 1 (r77 lesson:15 `HEAD:` token), `commit_unresolvable` 2
  (S230/S231 `7bb48f21…`).
- independent: `report_dead` 1 + `commit_unresolvable` 2 only.

Load-bearing ledger (proof type: W = declared world, M = mechanism proof, U = unproven):

| Repair | Moves count? | Proof |
|---|---|---|
| R1 report-pointer object resolution + content identity | YES — only repair-side fix for `report_dead` in BOTH gates | M: `HEAD:` token resolves only in the fleet object store (8547 B, SHONEN ✓); the new `<rev>:<path>` git-expression arm + fleet hop clears it, and the ≥400 B/`## SHONEN` arm keeps W8's marker dead. W8 probes exactly the content-identity arm. |
| R2 external-commit verified binding | YES — only repair-side fix for `commit_unresolvable` in BOTH gates | M: `7bb48f21…` absent from lane and fleet object stores (gate DRIFT). W6/W7 probe the marker-masking and dead-hash variants. |
| R3 `.ufo/wapes` disposition | NO — count-neutral | M: file is untracked (`?? .ufo/wapes`); corpus gates read committed `corpus/` bytes only. Moral repair for routed R80-D2 — honest as a disposition, but it does not move any count and should not be implied to. |
| R4 index + baseline refresh | YES but NOT UNIQUELY | M: all three drifts (`tracked_files`, `unindexed`, `report_total`) trace to ONE file — the r80 lesson (+1 tracked, +2 report pointers, sole unindexed). Deleting that one file flips the same three classes and it is not a base spotcheck (SPOTCHECK_RE, not at base → only INFO line), not pinned, not referenced. No declared world exercises the delete. |
| R5 S230 supersede row | NO — count-neutral | M: once the hash is manifest-exempt, row prose is gate-invisible; S230's `badlogic/pi-mono` anchor stays false prose the corpus keeps (append-only design: correction lives in S250). Honesty repair, not counter repair. New hex the S250 row cites (e.g. `bb65e3e4…`, `25cc5c7b…`) MUST each land in `external-commits.json` with a receipt or R5 breaks R2 — the plan's "both hex occurrences classify commit_external" covers only `7bb48f21…`; flag: pin the new hashes too or cite them truncated. |
| R6 registry row | CONDITIONALLY load-bearing | M: the C2 counter is a new `verifiers/` blob; `check_gate_registry` universe = all `verifiers/` blobs needing exactly one conformant row. Counter-without-row → registry red → 5 of 6. Plan's "lands with the counter file in the same commit" is exactly right. |

Direct answer: NO pure do-nothing control reaches `6 of 6` — W0 stays `4 of 6`
(mechanism-certain). BUT a declared-controls gap exists:

**FINDING A1 (consistency defect, counter-fixable at plan level): the scrub-and-delete
world reaches `6 of 6` with R2 and R4 never landing.** World W_S: R1 lands (unavoidable —
the `HEAD:` token lives in pinned r77 spotcheck bytes), the r80 lesson is deleted
(flips all three drift classes), and the two `7bb48f21…` tokens are re-shaped in place
— append `…` → `commit_truncated` arm, or quote-wrap → `commit_quoted` arm — both are
existing legal classifications, so no row need even be removed and
`check_sources_append_only` would not see a protected-cell breach anyway (and it is
not in the battery). Result: `commit_unresolvable`→0, `report_dead`→0, all drifts→0 =
`6 of 6` with R2, R4, R5 absent. The declared worlds prove each repair INSUFFICIENT
alone (W1, W2, W3); none proves R2 or R4 NECESSARY. The plan's gloss "proves R1+R2
load-bearing" is true of W1 only in the sufficiency direction. Smallest corrections:
declare W_S in the control list (expected `6 of 6` → reported as a counter defect per
freeze discipline, forcing the claim to stop), and/or add
`check_sources_append_only.py` to the § No-harm battery (it is absent from both BATTERY
and the no-harm list today). Without one of these, `6 of 6` certifies the arithmetic
of the corpus, not the provenance of the fix — a calibration claim about consistency
that a lie passes.

**FINDING A2 (minor): R3/R5/R6 carry no count.** Listing them inside the C1 repair
block is fine (they are routed defects), but the plan text does not say which repairs
move counts; R3/R5 are inert on the predicate. Precision nit only.

## (b) Is C2's `documented` conjunct-set enumerable end-to-end by ONE command?

Yes on paper; the counter is not yet built (no `verifiers/check_sdk_allowed_tools.py`
at base — `ls verifiers/`). Per-conjunct enumeration:

- (a) entry file exists + `source:`/`verified-at:`/`recheck:` fields → parseable frontmatter/lines on committed blob. Enumerable.
- (b) S249 row = 11 cells, `mined`, tier A/B, `used-by` names entry, canonical URL → cell-split + literal compares. Enumerable.
- (c) anchor names `.ufo/waves/round-81/snapshots/S249.md` + sha256(committed blob) == counter pin == fetch-record pin → `git cat-file` + sha256sum + JSON field read. Enumerable.
- (d) located quote ≤25 words containing `allowed-tools`|`allowedTools`, occurring in the snapshot text after the first heading → substring + word count + heading offset. Enumerable.
- (e) S248 `used-by` names the new entry → cell compare on committed bytes. Enumerable (old→new log is lesson prose — the counter can't grade it; see (c)).
- (f) SKILL.md "names the SDK channel in the `allowed-tools` author-facing rule area" + conformant registry row → **enumerable ONLY if the counter pins concrete tokens** (e.g. literal `allowedTools`/`allowed_tools` inside the `Treat allowed-tools` paragraph at SKILL.md:164 region) plus a mini-conformance check (reuse the registry universe logic in-file; do not delegate to `check_gate_registry`'s exit or the claim silently inherits a sibling gate). As spec'd, "names" without a pinned token is a judgment. FLAG B1.
- (g) README names entry + PROVINCE `## Core` "names the SDK channel addition" → same token-pinning requirement (e.g. `allowedTools` inside `## Core` at PROVINCE.md:8). FLAG B1 same class.

So: enumerable end-to-end by one command — CONDITIONAL on the counter spec pinning
literal tokens for (f)/(g) and on conjunct-internal evaluation. Otherwise (f)/(g)
degenerate into prose verdicts inside a "measured" claim.

## (c) Universal clauses the counter can't enumerate

- Claim-side universals are all enumerable: `INSTRUMENT_PINS` pin-table is a finite
  byte-equality sweep; `absent from lane and fleet` is two `cat-file -e` calls per
  token; `<rev>:<path>` resolution is two `cat-file -e` calls.
- `report content identity` = `## SHONEN` presence + ≥400 B — enumerable; W8 probes it.
- R2's "the committed fetch/ls-remote receipt that proves the repo→hash association" —
  **enumerable only if the manifest pins receipt path + expected repo + expected hash
  and the counter field-checks the committed receipt** (the receipts are JSON with
  url/note fields — S230/S231 receipts show parseable structure). If the manifest only
  names a path, W9 covers absence but NOT a receipt that proves repo B while the
  manifest claims repo A. Smallest correction: manifest rows carry
  `{hash, repo, receipt_path, receipt_sha256}` and the counter verifies both identity
  and the repo/hash fields inside the receipt bytes. FLAG C1.
- Plan-side (not claim-side) universals that stay judgment: "the five guards' checks
  stay semantically identical" (kill rule) — uncountable by design; instrument-pin
  makes the byte-diff auditable, so acceptable, but the kill rule leans on review, not
  measurement. Acceptable as declared.
- E6(d) "comment cap mentions updated so text does not contradict the bound" — the
  self-test/comment clause is a textual sweep, enumerable but stated loosely;
  low risk.

## (d) Exploratory-vs-measured split

- C2's predicate is committed-bytes-measurable end to end; no rider hides in the
  counter itself. The single-quote convention matches the corpus precedent.
- **FINDING D1 (soft rider):** the plan's framing asserts "a managed-settings
  override" as part of the channel. The conjuncts measure ONE located quote containing
  `allowed-tools|allowedTools`; if that quote does not carry the override claim, the
  override is unverified prose riding inside a measured claim. Precedent exists:
  r80's counter registry row declares "the grant-semantics rider is exploratory"
  (SKILL.md:518). Smallest correction: require the located quote to contain the
  second-channel claim (`allowedTools` AND the grant context), or mark the override
  exploratory in the r81 counter's registry row — matching the lane's own convention.
- **FINDING D2 (freshness honesty):** S249 is a NEW ROW of an OLD SOURCE — S248
  already carries the identical URL, same fetch day, same sha256 `ac62c2df…`, and its
  located quotes already name `allowedTools`. S249 adds no new evidence; it re-mines
  the same fetched page under a second scope. This matches duplicate-scope precedent
  (S065/S227 already pair the same `code.claude.com` host under different scopes; the
  census prints this as an expected W04 warning class), and the plan never claims a
  new page — but the depth gain is the entry + `used-by` expansion, not new sourcing.
  Honest if the row/lesson states it re-mines S248's URL; the counter should verify
  S249's snapshot sha against S249's OWN fetch record (conjunct c does this) so the
  pin isn't copied provenance. Also note for the counter builder: conjunct (b)'s
  "canonical URL" equality with S248's URL is REQUIRED, not a defect.
- Assimilation/considerthese stay outside C2 (plan §Frontier) — split is clean there.

## (e) LINE_CAP 140 — measured or guessed?

Partially justified, with two arithmetic defects:

- The declared justification (E6, plan line 26): `instrument-pin` carries the load;
  estimate "60–120 added lines" for the two-gate binding repair; freeze receipts record
  measured numstat before data; stop if over bound. This is Q65-pattern
  declare-then-measure-with-stop — NOT a bare guess.
- **FINDING E1 (kill-arithmetic defect):** the kill line says "40 base-spent +
  measured added ≤ 140". Actual base-spent is 22 added / 3 deleted
  (`tipbattery-base-dot.txt:2`); the r80 instrument change measured +28/+10 = 38 added
  across the two corpus gates (`Kb80E05GrammarFix.numstat-six.txt`). Anchoring on 40
  makes the effective kill headroom 100 added lines vs the estimate's upper bound of
  120 — a measured added in (100,120] is inside the declared estimate yet triggers the
  stop. Internally inconsistent bounds. Smallest correction: re-anchor to the measured
  base-spend — "measured base-spent (22) + measured added ≤ 140".
- **FINDING E2 (undeclared relaxation):** `LINE_CAP` feeds the deleted-lines bound too
  (check_tip_battery.py:318). 40→140 relaxes instrument DELETION 3.5× with zero
  justification (the plan argues only the addition side). Harmless in practice —
  instrument-pin still requires base-or-pinned blobs, so a delete-stub fails the pin —
  but the erratum's "no other line" phrasing should note the bound is bidirectional.
- Freshness gap: receipts/ holds only the `--repo .` base form. The claim predicates
  BOTH forms at base AND tip; capture `tipbattery-base-abs.txt` before freeze or the
  base half of the predicate rests on one form.

## Verdict table

| Q | Answer |
|---|---|
| (a) do-nothing reaches 6 of 6? | No (W0 → 4 of 6). But W_S scrub-and-delete reaches 6 of 6 without R2/R4 — undeclared world class; repairs R1 (sole fix for report_dead), R2, R6-conditional are genuinely load-bearing; R4 is replaceable by deletion; R3/R5 count-neutral. |
| (b) C2 enumerable by one command? | Yes, conditional on pinning literal tokens for conjuncts (f)/(g) and conjunct-internal evaluation; counter not yet built. |
| (c) universal clauses? | Claim-side: none unenumerable. R2's receipt-proof clause needs manifest-pinned receipt fields (C1). Kill-rule "semantically identical" is judgment, declared. |
| (d) split honest? | Yes, with a soft rider: managed-settings override unmeasured (D1); S249 re-mines S248's identical fetch — state it (D2). |
| (e) 140 justified? | Estimate-with-stop, not guessed — but kill arithmetic anchors on 40 vs measured 22 (E1), and the cap silently relaxes deletions too (E2). |

No false claims found; the plan is honest in structure and its W0–W9 controls are the
right family. The claim-defect candidates above are fixable pre-freeze: declare W_S,
add append-only to the no-harm battery, re-anchor kill arithmetic to 22, pin tokens
for conjuncts (f)/(g), pin receipt fields in `external-commits.json`, and capture the
absolute-form base receipt.

VERDICT: claims admissible after six pre-freeze corrections — W_S scrub/delete world declared (or append-only in no-harm battery), kill arithmetic re-anchored to measured base-spend 22, conjuncts (f)/(g) token-pinned, external-commits.json receipt fields verified, S249 re-mine stated, absolute-form base receipt captured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81C04Honesty.md
