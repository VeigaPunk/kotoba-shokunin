# Kb81V03Instruments — primary-byte instrument audit (round 81, w1)

Base audited: `b284223105f4d106f7e8f56ed4fd296c643cda0e` (lane HEAD == base at read time;
working tree `verify_corpus_integrity.py` 1471 lines, blob-visible sha256
`3e600f4b70e4664048c0c09b06bf6a28cb00ff37fbb8c78f597a1f1452c03748`;
`verify_corpus_independent.py` 1153 lines, sha256
`c9cef5b3ecca5e9cfdac26b77702ac39186049ed782ce4a250776939a06e7ff2`).
Method: read-only primary-byte audit, no gate execution. Drafts cross-checked:
`.ufo/waves/round-81/build/Kb81E01Integrity/final.diff` (blob `bbee51f`) and
`.ufo/waves/round-81/build/Kb81E02Independent.patch` (blob `5960294`), plus
`Kb81E03ExtManifest{,.json,-superseded.txt,-fetch.txt}` and
`Kb81E05Erratum.hunk-inventory.txt`.

## 0. Verdict summary

E01 and E02's published drafts implement the strengthened R1/R2 contract the
audit derives from the plan and the corpus bytes. The plan's literal
`## SHONEN` + 400 B identity arm is NOT safe on the live pointer population
(11 sites across 5 targets would die); both drafts already converged on the
era-conditional arm (`IDENTITY_FROM_ROUND = 19`) that the bytes prove is the
minimal discriminator. One binding conflict was found and is already resolved
by the seats (E03's flat manifest is marked superseded; the canonical schema is
E01's `{"commits": [{hash, repository, receipt, receipt_sha256}]}` with
`receipt_sha256 = e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f`
— independently re-measured here over `S231.fetch.json` bytes). E02's patch
carries one live code defect: `_committed_blob` is defined twice.

## 1. Token and pointer code paths — `verify_corpus_integrity.py`

Commit-token path (harvest → classify → aggregate → adjudicate):

- `COMMIT_RE` L151: `` commit `<token>` `` harvest; `(?<![A-Za-z0-9_-])`
  lookbehind keeps `pre-commit `/`xcommit ` out (self-test L1112).
- `citation_findings` L494–557, per line L511:
  - L526–529 `inside_quotes`/`inside_code_span` → `commit_quoted_detail`
    (context, never live).
  - L530 `TRUNCATED_COMMIT_RE` (7–40 hex + single U+2026) →
    `commit_truncated_detail` (context).
  - L533 `is_hex_object_id` (7–40 hex) fail → `commit_nonhash` (violation).
  - L536 `commit_total += 1`, L537 `commit_resolves(token.lower())` fail →
    `commit_unresolvable` (violation). **The R2 insertion point is exactly
    L537–538: the manifest consult must sit inside `not commit_resolves`, i.e.
    externality is asserted only after lane+fleet resolution has failed.** Any
    exemption applied before the lane/fleet lookup is the r80-E05 defect class.
- `commit_resolves` L600–612: `git cat-file -e <tok>^{commit}` lane first,
  `fleet_root` fallback second; fleet root missing/not-a-repo reads False.
  `COMMIT_HOP_MARKER` L597 is pinned by `commit-hop/marker-pinned` (self-test
  L1077–1078): the docstring may be extended but the frozen literal "resolves
  against the lane repository first, then the fleet root" MUST be kept
  verbatim or self-test breaks.
- `commit_peel_arg` L311: `<tok>^{commit}` — peel must stay (self-test L892);
  bare ref would accept trees/blobs.
- Aggregation: `corpus_observations` L623–690 (agg dict L643–653, details
  L655–663, injected lambdas L671–676); `CHECKS` L697–707 — only
  `commit_unresolvable`/`commit_nonhash` are violation classes; `commit_total`
  is equal-mode (baseline 46). `commit_external` MUST stay an observation/info
  class — it must never enter `CHECKS` as zero-mode and never enter
  `violations()` on the independent side.
- Detail plumbing: `DETAIL_KEYS` L709–720 prints `*_detail` lines.

Report-pointer path:

- `UFO_POINTER_RE` L146–148: the leading `(?:/|~|(?:\.\.?)*)[^\s`\"]*?` admits
  `:` in the token head, so `` `HEAD:.ufo/reports/round-77/kotoba.md` `` (the
  base's sole rev-shaped token, `corpus/lessons/round-77-verifier-spotcheck.md:15`)
  harvests WHOLE — current `report_dead` detail records the token including
  `HEAD:`; the tokenizer needs no change for R1.
- `is_excluded_pointer` L280–292 (placeholder marks, whitespace, glob,
  `..`-segment after leading hops) runs BEFORE resolution — keep semantics
  unchanged; `HEAD:` contains no `..` segment so it stays a checked pointer.
- `inside_quotes` L316 + L517–519 → `report_pointers_quoted_detail`: a quoted
  `<rev>:<path>` must remain quoted-context in r81 too.
- `report_total` counted at L520 for every non-excluded non-quoted token;
  baseline expect 109 in `verifiers/corpus-baseline.json` — already stale at
  base (observed 111; R4 refreshes). **The r81 patches must not change the
  harvested population: still 111 (verified by simulation, §4).**
- `report_pointer_exists` L273–277: citing-dir `resolve_pointer().is_file()`
  first, then `fleet_root / token` for bare `.ufo/reports/` tokens only — pure
  existence, no content check (the r80 W10 hole). **This function is the R1
  insertion point.** Its signature `report_pointer_exists(base, token,
  fleet_root=FLEET_ROOT)` receives `base` as an ABSOLUTE path
  (`_repo / base`, L675), which is what lets the rev arm discover the citing
  repo by walking `.git` upward (E01's approach) or by parameter.
- `pointer_shape` L295–303: `<rev>:` tokens fall through to `"bare"`; keeping
  that class preserves `pointer_shapes` keys (L504/L654) and the printed shape
  census (L1442). Introducing a fifth shape is legal but must touch both dict
  literals and self-test `shapes/class-counts`.
- Adjudication: `evaluate` L723–740, `zero` mode adjudicated baseline-free;
  `report_dead` stays zero-mode.

## 2. Token and pointer code paths — `verify_corpus_independent.py`

- `POINTER_RE` L123–125: `[^\s`"()\[\],;:]*` EXCLUDES `:` in the leading part,
  so `HEAD:.ufo/...` harvests WITHOUT `HEAD:` (token starts at `.ufo`). This is
  why the same site appears dead in both gates with different token text.
  **R2b must glue the `<rev>:` prefix onto the match** (E02: `REV_PREFIX_RE`
  L148–156 applied post-scan in `pointer_tokens` L237–241). `:` in the rev
  tail `[^`"]*?\.md` was already allowed, so `x:y/.ufo/...` tokens match whole.
- `pointer_exclusion` L236–246 (`angle-bracket`, `glob`, `whitespace`,
  `dotdot-after-hops`) — unchanged classes, runs before quote check.
- `quote_spans`/`code_span_spans`/`_inside` L147–197 → `report_quoted` /
  `commit_quoted` context arms — unchanged.
- `report_pointer_exists` L265–270 → E02 replaces with `report_target`
  (`(route, bytes)`: `object` via `git cat-file blob <tok>` citing-repo then
  fleet; `path` citing-dir; `fallback` fleet for bare tokens only; `dead`)
  plus `report_identity_ok` — the independent twin of E01's arm.
- `pointer_shape` L273–280: rev tokens stay `"bare"` (consistent with E01).
- `analyse_commits` L473–515: COMMIT_RE L126 (`\s` + `[^`\s]+` — slightly
  different grammar, same live population); quoted → `commit_quoted`;
  `TRUNCATED_RE` → `commit_truncated`; else `citations.append` (so
  `commit_total` counts non-hex too — fixture "five citations"); length+HEX
  fail → `commit_nonhash` (L490–492); else `cat-file -e <tok>^{commit}` lane,
  fleet only when `abspath(fleet_root) != abspath(repo)` (L494–497); fail →
  `unresolvable` (L498–499). **R2b insertion point is L498–499: route to
  `external` iff `token.lower() in externals`, else `unresolvable`.** E02 adds
  `externals` parameter defaulting to `external_commits(repo)` — call sites:
  `analyse` L535 and self-test calls L993/L1027 (all still compatible).
- `violations()` L568–575 sums only the six zero classes; `commit_external`
  must not enter it. `CHECK_IDS` L47–57 unchanged; `commit_hex_total` L503–506
  is INFO-only and correctly includes external-bound hex.

## 3. What MUST change vs. what MUST NOT

MUST change (both files, symmetry required — the gates are two witnesses of the
same classes; if only one learns `<rev>:` and the manifest, the other stays red
and the battery can never reach 6 of 6):

1. Report-pointer resolution gains a `<rev>:<path>` object arm BEFORE path
   resolution: token of form `<head>:.ufo/reports/...` → `git cat-file -e/-p`
   in the citing repo, then the fleet root; resolved bytes must pass the
   identity arm. E01 short-circuits inside `report_pointer_exists`
   (`token.partition(":")`); E02 routes inside `report_target`. Both correct.
2. Every *resolved* target (object or path) must bind report identity — with
   the era condition §4 proves necessary: `round-N` ≥ 19 (or rev-object always)
   ⇒ bytes contain `## SHONEN` AND ≥ 400 B; below 19 ⇒ existence only. A
   marker file substituted at a cited report path of round ≥ 19 (W8/W10 class)
   MUST read `report_dead`.
3. Commit path gains a manifest consult AFTER lane+fleet resolution fails:
   committed `verifiers/external-commits.json` read at `HEAD:` (committed
   bytes only — matching "reviewed evidence record pins it"), binding hash →
   {repository, receipt path, receipt sha256}; receipt must itself be
   committed at HEAD and carry the hash+repository. Failures ⇒
   `commit_unresolvable`, never `commit_external`. Both drafts read at HEAD via
   `git cat-file blob HEAD:<path>` — a deliberate deviation from the gates'
   working-tree rule, correct per "committed fetch/ls-remote receipt".
4. Manifest absent/malformed ⇒ zero bindings (fail closed): E01 catches
   `(ValueError, KeyError, TypeError)` on `["commits"]`; E02 catches
   `(AttributeError, KeyError, TypeError, UnicodeDecodeError, ValueError)` on
   the same access. Both fail closed.
5. `commit_external` + `commit_external_detail` land as observation-only
   fields in both files (agg dict, details dict, DETAIL_KEYS/render lists) —
   never CHECKS zero-mode, never `violations()`, never `exit_code`.

MUST NOT change (regression classes — the corpus still needs these arms green):

- `commit_truncated` (U+2026 arm) — order: truncated → nonhash → resolve.
- `commit_quoted` / `commit_quoted_detail` — inside double quotes OR a matched
  code span (double-backtick example, self-test L1046–1059 primary,
  L1019–1035 independent). The r80 E05 patch is the counter-example: it routed
  a NON-HEX token `o/r@deadbee` into `external` — `commit_nonhash` must keep
  every token `is_hex_object_id` rejects, unconditionally.
- `commit_nonhash` — external must be reachable ONLY after hex validation
  passes; non-hex tokens can never be external.
- `report_pointers_excluded` / `report_pointers_quoted` — exclusion runs
  before the rev/path distinction; quoted `HEAD:` stays context.
- `commit_peel_arg` peel (`^{commit}`), the lane-first-then-fleet order, the
  `fleet_root` constants, `COMMIT_HOP_MARKER` literal.
- `report_total`/`commit_total` semantics: totals count the checked population
  INCLUDING external-bound citations (observed 111 / 46 unchanged).
- `is_excluded_pointer`/`pointer_exclusion`, `pointer_shape` classes,
  `fenced_lines`/`fenced_line_numbers`, the index family wholesale.
- No external marker may ever exempt: `owner/repo@`, repo URLs, or any other
  line text MUST NOT enter the external decision (W6/W7/W9 classes) — E01/E02
  never read the citing line for the exemption, correct.
- No option injection: a rev head must not reach git as an option. E01's
  partition accepts `head` unrestricted — `git cat-file -e "-x:.ufo/…"` fails
  as an unknown option → fail closed (acceptable; E02's `REV_PREFIX_RE`
  `[A-Za-z_]|[0-9a-fA-F]{7,40}` additionally can't produce a `-` head). A
  `..` inside the rev parses as a range, not a blob → fail closed.

## 4. The identity-arm conflict — measured, and how the drafts resolved it

Plan §C1 repair 1 names the arm "contains `## SHONEN` and the file is ≥400
bytes … (a report-marker distinction arm)". Simulated against the live corpus
population (`git ls-files corpus/*.md`, full `UFO_POINTER_RE` harvest,
exclusion + quoted filtering — my own reimplementation, exit-code-free):
`report_total=111`, `dead=1` (the `HEAD:` token), `excluded=8`, `quoted=2` —
matching the committed base receipts (`report_dead 1`, `report_total 111≠109`
baseline drift from the plan's gate-truth table). Of the 110 resolvable sites,
the literal arm FAILS 11 sites over 5 targets:

- round-1/kotoba.md 3365 B no-SHONEN — cited 3× (README:26, round-1:4,
  round-1-aggregator-audit:9)
- round-4/kotoba.md 3367 B no-SHONEN — cited 2× (README:28, round-4:4)
- round-5/kotoba.md 5080 B no-SHONEN — cited 2× (README:24, round-5:4)
- round-8/kotoba.md 120 B no-SHONEN — cited 2× (README:49, round-8:5) — a real,
  committed closeout note ("Marker so fleet-2 respawns"), 120 bytes
- round-14/kotoba.md 9463 B no-SHONEN — cited 2× (checklist-execution-round15:70,
  round-9-aggregator-corpus-verdict:24)

A literal SHONEN+400 arm therefore produces `report_dead=11` at the landed tip —
red forever, since the corpus is append-only and the cited files themselves are
valid targets. No clean "SHONEN-era" boundary exists (SHONEN present at r3,
absent at r14). Both drafts independently chose the measured era split
`IDENTITY_FROM_ROUND = 19`: every resolved target ≥ round 19 in the corpus
carries `## SHONEN` and ≥400 B (r21 8358 B … r80 7822 B, plus `chousa.md` at
r58 10666 B — lane name is not part of identity, correct), and every target
below 19 is existence-only. Rev-object tokens assert identity unconditionally —
the spot-check cite `HEAD:.ufo/reports/round-77/kotoba.md` resolves to the
fleet blob (8547 B, `## SHONEN` present; `git -C <fleet> cat-file -e
'HEAD:.ufo/reports/round-77/kotoba.md'` exit 0, lane exit 128 — verified).
This keeps all 110 green while a 7-byte "marker" file at ANY cited round≥19
path or object reads dead — the W10 class. Audit position: this is the minimal
arm consistent with both the plan's stated purpose ("marker distinction, not
completeness judgment") and the committed bytes; the plan's parenthetical
`## SHONEN`+400 literal is falsified by corpus bytes and the era bound is the
required reconciliation (worth an L1 erratum note for the record).

## 5. Draft-vs-audit conformance checks (evidence, not re-execution)

- E01 `final.diff` (integrity, +137/-11 net hunks on the file; receipt
  `selftest-final.txt`: 0 failures over 178 assertions; `observation-delta.txt`:
  base `commit_unresolvable=2, report_dead=1` → final `0/0`, `commit_external=2`
  at SOURCES:171-172 — matches the audit's predicted deltas exactly).
- E02 `Kb81E02Independent.patch`: same arms on the independent implementation.
  **Defect: `_committed_blob` is defined twice (back-to-back ~L525–540 post-
  patch); the second definition wins and is the one used — dead code, remove
  the first copy before landing.** Its `external_commits` requires the receipt
  to be committed AND sha256-pinned AND to carry hash+repository — stronger
  than E01's (E01 requires sha256 + repository-name only). For the S231 receipt
  both predicates coincide (the note names `mistralai/mistral-vibe` and the
  hash verbatim — verified in the committed blob). Cross-gate asymmetry to
  record for review: E01 does not require the receipt to *name the hash*; a
  receipt that binds repo→something-else would still pass E01's reader. E02's
  `sha in text` check is the correct strengthened arm; E01 should adopt it or
  the L1 should note the residual gap (W6-class receipts that mention the repo
  but never the hash). Conflict-duplicate and abbreviation fail-closed in both.
- Manifest schema: E03's `Kb81E03ExtManifest.json` (flat array,
  `{hash, repo, evidence, pinned_at}`) does NOT satisfy either reader; the
  seats already dispositioned it — `Kb81E03ExtManifest-superseded.txt` records
  E01's `{"commits":[{hash, repository, receipt, receipt_sha256}]}` as the
  agreed schema. The integration must land exactly one manifest at
  `verifiers/external-commits.json` with:
  `hash 7bb48f213ac677f943d5c791199ed3dddf302f00`,
  `repository mistralai/mistral-vibe`,
  `receipt .ufo/waves/round-79/snapshots/S231.fetch.json`,
  `receipt_sha256 e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f`
  (sha256 re-measured over the committed working-tree bytes this audit).
- E05Erratum hunk inventory (counter): `LINE_CAP 40→140`, two pin-table
  additions (one per gate blob), self-test constants re-anchored to `LINE_CAP`,
  comment mentions only — matches E6 (a)–(d) exactly; numstat 21+/15- on
  `check_tip_battery.py`.
- Battery arithmetic re-measured: base→tip numstat over the six BATTERY
  scripts is +22/-3 (`check_assertion_floors.py` only) — so r81 headroom is
  118 added / 137 deleted under `LINE_CAP=140` (`added`/`deleted_lines` sum
  all six files, L299–320). The plan's "40 base-spent" is conservative vs the
  measured 22. Patch author's single landed blob per gate must equal the one
  pinned sha (base blobs `e470eaa…`/`edac0df…` are the pre-images pinned today;
  E6 adds `bbee51f`/`5960294`-class post-images — pin the FINAL reviewed blob).
- `floors` guard: `floors-registry.json` rows `corpus_integrity:164`,
  `corpus_independent:105` are lower bounds on self-test assertions — new arms
  only raise observed counts; never delete or skip assertions.
- Adjacent, out of R1/R2 scope (flag only): `verify_skill_checklist.py`
  `governance.citation_resolves` also predicates on existence
  (`candidate.exists()` L1294) — same W10-shaped hole; the plan does not repair
  it this round and it stays green both ways. `check_correction_sweep.py` has
  no pointer/token arms; no edits needed there.

## 6. Control-world mapping (what each strengthened arm must catch)

- W6 (real lane-created commit + `owner/repo@` marker, no manifest entry):
  absent lane+fleet → manifest lookup → absent ⇒ `commit_unresolvable` red. ✓
- W7 (dead lane hash in a lane-URL row): same path ⇒ red. The line marker is
  never read — the routing must not touch the line text. ✓
- W8 (marker file substituted at a fleet report path): path/fallback route,
  round≥19 ⇒ identity fails ⇒ `report_dead` red. ✓
- W9 (manifest entry without committed receipt proof): `receipt_sha256`
  mismatch or receipt absent at HEAD ⇒ unresolvable red. ✓
- W2/W3 (one repair only): each gate still red on the other's unfixed class —
  proves both arms load-bearing (gate red ⇒ battery ≤5 of 6).
- W4 (stubbed instrument): `instrument-pin` fails on blob identity regardless
  of `LINE_CAP` — erratum keeps pin load-bearing.

## 7. E03 manifest claim — cross-check verdict

`7bb48f213ac677f943d5c791199ed3dddf302f00` RESOLVES in `mistralai/mistral-vibe`
per the committed receipts: `S231.fetch.json` (tracked at base, verified
`git cat-file -e b2842231:.ufo/waves/round-79/snapshots/S231.fetch.json` → exit
0; content sha256 `e75f057a…`) records `main` → that hash by `git ls-remote` at
2026-10-27T21:43:03Z, HTTP 200, 77634 B, page sha256 `fc48a5db…` matching
`S231-vibe.md`/`S231.manifest`. It does NOT resolve in `badlogic/pi-mono`:
`S230.fetch.json` records pi-mono `main` at fetch time as
`bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` (last path-touching commit
`25cc5c7b…`); E03's fresh ls-remote (2026-10-28T02:28Z) shows pi-mono main now
`a9228305…` and zero hits for the hash across 4120 advertised refs. The object
is absent from lane and fleet object stores (both `cat-file -e` exit 128 —
re-verified). So the S230 row's repo attribution is wrong (R80-D4, repaired by
the S250 supersede row), the binding to `mistralai/mistral-vibe` is
receipt-verified, and the manifest entry is justified for exactly the two
occurrences at `corpus/SOURCES.md:171-172`.

## 8. Residual risks for reviewers

- Identity arm era bound (19) is inferred from absence in rounds 15–18 (no
  resolved targets in 15–18); a future pre-19-style report cited would be
  existence-only by design — acceptable per the marker-distinction purpose.
- E01 vs E02 receipt-content strictness asymmetry (§5): E02 requires the
  receipt to name the hash; E01 requires only repo-name + sha256 pin. Land the
  stricter predicate in both, or record the accepted gap.
- E02 `_committed_blob` duplicate definition — remove before the blob is
  pinned; the pinned blob must be the de-duplicated final bytes.
- `git_blob_bytes(repo, "HEAD:<receipt>")` reads committed bytes while the
  gate's corpus family reads the working tree — documented deviation; an
  uncommitted manifest edit silently does nothing (fail closed), which is the
  intended direction.

Tools: no installs (python3/git only). Scratch: none created.

VERDICT: R1/R2 repairs must land symmetric arms (rev-object + era-conditional identity; HEAD-committed manifest binding with sha256-pinned receipt) in BOTH corpus gates; the era bound 19 and E01's manifest schema are the measured reconciliations; E02 must drop its duplicate _committed_blob and ideally require the receipt to name the hash; E03's hash→mistral-vibe binding is receipt-verified and its flat manifest stays superseded.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81V03Instruments.md
