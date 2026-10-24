# ScribeMistakeQ61 — M102 / Q61 calibration review

Seat: `ScribeMistakeQ61` · role scribe · axis **calibration** · leaf (read-only; no product, plan, control, receipt or counter edit)
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
Pinned base (frozen plan): `11385e04e368c1e94ab1a5a89d7439033eb1f855`
Measured tip while reading: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (working-tree HEAD; receipts below were measured at `fc1b71e5` and `41196476`, not at this tip)
Working tree at read time: only ` M .ufo/waves/round-66/w1/swarm-registry.json` (a sibling's in-flight file; not touched by this seat)
Writes made: this report only.

## Verdict

1. **Captured-by `none` — accurate as to the missing prior criterion, but non-conforming to the lane's own retroactive-labeling precedent.** No QUALITY row at the base named an allowed repository set or a code-span/live-citation distinction (`11385e04:corpus/QUALITY.md` has 60 rows, Q01–Q60; zero `| Q61` rows). Q61 is committed this round (`corpus/QUALITY.md:76`, `supersedes = —`, grounded in M102), so `none` describes the prior state correctly. The gap is conventional: the lane writes `Captured-by: none at r<prior> — now **Q<new>**` when the round creates the criterion (`corpus/lessons/round-64.md:63`, M96 → Q60), and M103 in the same file does name Q61 (`corpus/lessons/round-66.md:32`); M102 omits the `— now Q61` half.

2. **Fix shown able to fail — yes, verified in committed bytes, with two citation defects.** The base arm is receipted at the exact cited base and enforced by exit code (counter returns 2 if the pinned base is not `0 of 2`). The no-hop kill world and the honest fixture exist and are load-bearing (`verifiers/check_r66_routed_repairs.py:96` is the conjunct the mutant removes; `:235` is the expected-False arm). However: (a) the arm-level result is attributed to `C2-counter-selftest.txt`, which records only an aggregate `0 failure(s) over 14 assertions` plus a file hash, no arm label or per-world verdict; (b) the sentence that `C2-before.txt` "records the exact … three unresolved tokens, including the closure-authored fleet report reference" is misrouted — that control records counts only and explicitly defers detail to `--json`; the token identities are in `C2-independent-before.txt:6` at a different pinned base (`41196476`). The underlying facts are true — I verified both by resolution and by lesson context.

## Q1 — does `none` name the missing prior criterion accurately?

Subject line (`corpus/lessons/round-66.md:18`):

> "Evidence: `.ufo/waves/round-66/controls/C2-before.txt` records the exact r66 base gate's three unresolved tokens, including the closure-authored fleet report reference; the same gate reported four unindexed closure spot-check files and stale count pins. Captured-by: `none` — the old resolver queried only the lane object database, and no QUALITY criterion named the allowed repository set or distinguished a quoted code-span example from a live reference."

Both clauses of the captured-by explanation are true at the base:

| Claim | Evidence | Result |
|---|---|---|
| No base QUALITY criterion names an allowed repository set | `git show 11385e04:corpus/QUALITY.md \| grep -cE '^\| Q61'` → `0`; row count → `60` (Q01–Q60); base grep for `resolution set`, `repository resolution`, `foreign`, `code span`, `code-span`, `quoted` in rows → empty | holds |
| "fleet root" not a prior rule | only base occurrence is line 60, inside Q49's **grounded-in** evidence prose ("round-58 R1 found `ReviewBudgetMove.md` written under the fleet root"), not in any criterion statement | holds |
| No prior code-span/live split | base rows contain no `quoted`/`code span` text; base code had `inside_quotes` only — `git diff 11385e04..HEAD -- verifiers/verify_corpus_integrity.py` shows `+def inside_code_span` and `+ or inside_code_span(line, match.start(0), match.end(0))` as round-66 additions | holds |
| "the old resolver queried only the lane object database" | base resolved commits via `git(_repo, "cat-file", "-e", …)` with no fleet hop; the whole `COMMIT_HOP_MARKER` + `def commit_resolves(hex_id, repo, fleet_root=FLEET_ROOT)` block is added by the r66 diff (`verifiers/verify_corpus_integrity.py:125, 588-600`) | holds |

Q61 identity check (`corpus/QUALITY.md:76`): "A commit-citation integrity gate states its repository resolution set and parses context separately from live citations: resolve a lane object in the lane repo, a fleet object in the declared fleet root, keep an object absent from both unresolved, and exclude a commit example wholly inside a matching Markdown code span. Its self-test carries lane-only, fleet-only, neither, live-token and code-span-context arms." — `supersedes = —`, `grounded in` = M102 + `verify_corpus_integrity.py --self-test`. It did not exist at base, so no earlier row could have captured the class.

Nearest prior rows and why they do not capture it: Q03 (`corpus/QUALITY.md:14`) requires a record to name the commit holding its bytes; Q41 (`:52`) requires a hash cited in a report to resolve in the lane repo. Q41 *narrows* resolution to the lane and states no allowed set, and neither row parses code-span context. So `none` is right on the merits.

**Convention gap (F3):** `corpus/lessons/round-64.md:63` records M96 as "Captured-by: none at r63 — now **Q60**". M102 writes only `none` although Q61 lands in the same round and names M102. M103, four lines below, writes "Captured-by: Q61 applies to every commit-citation integrity gate" (`:32`). The asymmetry is a labeling inconsistency against the lane's precedent, not a false captured-by.

## Q2 — is the fix shown able to fail?

Fix sentence (`corpus/lessons/round-66.md:18`):

> "Fix: resolve lane-first then fleet-root, exclude a complete matching code span from live citation counts, index the four closure-authored r62–r65 spot-check lessons, and re-record the observed baseline only after the new corpus entries land. Shown able to fail: the frozen r66 counter gives the pinned base `0 of 2`; its self-test's no-fleet-hop world fails D2, while the honest fixture passes; evidence `.ufo/waves/round-66/controls/C2-counter-selftest.txt` and the round-66 final receipts."

### (a) Base arm — receipt-backed and enforced

`C2-before.txt:5-9` prints, at the exact pinned base:

- `:5` `control at 11385e04: 0 of 2`
- `:6` `D1-r65-registries-committed: FAIL`
- `:7` `D2-corpus-integrity-reconciled: FAIL`
- `:8` `r66 routed defects closed 0 of 2`
- `:9` `exit=1`

Enforcement is real, not decorative: `verifiers/check_r66_routed_repairs.py:127-129` returns exit 2 with `could-not-evaluate: pinned base scores %d of 2, expected 0 of 2` when the base is not zero, so a counter that drifted to pass at base could not report 2 of 2. The after side is receipted at its measured revision: `C2-routed-after.txt:3-8` (`2 of 2`, both PASS, exit 0 at `fc1b71e5…`).

### (b) No-hop world and honest fixture — true in code, aggregate-only in the cited control

Code (`verifiers/check_r66_routed_repairs.py`):

- `:206-208` honest fixture writes `HOP_MARKER + "\ndef commit_resolves(hex_id): pass\n" + "def inside_code_span(line): pass\n" + "lambda hex_id: commit_resolves(hex_id)\n"`.
- `:212-213` `check("honest/D2", …, True)`; `check("honest/2-of-2", honest_n, 2)`.
- `:233-235` mutant writes `"def commit_resolves(hex_id): pass\n"` without the marker; `check("kill/D2-no-fleet-hop", check_d2(root, no_hop), False)`.
- `:96` is the load-bearing conjunct: `return (HOP_MARKER in integrity and "def commit_resolves(" in integrity and "inside_code_span" in integrity and "commit_resolves(hex_id" in integrity)`. Deleting `:96` flips `:235` to FAIL, so the arm does falsify the guard.

Cited control (`C2-counter-selftest.txt`) contains, in full: `:4` `self-test: 0 failure(s) over 14 assertions`, `:5` `exit=0`, `:8` sha256 `3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141`, `:10` prose freeze note. It names no arm and shows no D2 verdict. The hash does pin the instrument: `sha256sum verifiers/check_r66_routed_repairs.py` and `git show HEAD:verifiers/check_r66_routed_repairs.py | sha256sum` both return `3129c0d7…`, identical to `:8`. So the arm is recoverable from hash-pinned bytes plus a 14/14 aggregate, but the lesson's arm-level sentence is code-derived, not exhibited by the file it cites (F2).

### (c) Code-span exclusion — behaviorally true, and corroborated by the before/after arithmetic

The Q61 arms exist in the primary gate's self-test: `verifiers/verify_corpus_integrity.py:1040` `cites/commit-context/code-span-excluded`, `:1042` `cites/commit-context/live-citation-counted`, `:1055` `commit-hop/lane-first`, `:1056` `commit-hop/fleet-fallback`, `:1057` `commit-hop/neither` — the five arms Q61 names, plus `fleet-not-a-repo`, `fleet-missing-dir` and `marker-pinned`. Receipts: `C2-integrity-selftest.txt:4` (`0 failure(s) over 161 assertions`), instrument hash `febfa57e…` at `:10` and `C2-integrity-after.txt:9`.

The mechanism is independently corroborated by counts, which the counter's string checks alone could not show:

- before (`C2-before.txt:13`): `commit_total=38 unresolvable=3 … quoted-excluded=5`
- after (`C2-integrity-after.txt:5`): `commit_total=37 unresolvable=0 … quoted-excluded=6`

One token moved from the live total into `quoted-excluded` (38 → 37, 5 → 6) and two moved from unresolved to resolved in the fleet (3 → 0). That is exactly the claimed two-part fix: one code-span exclusion, two fleet hops.

### (d) The token-identity sentence is misrouted

M102's Evidence claims `C2-before.txt` "records the exact r66 base gate's three unresolved tokens, including the closure-authored fleet report reference". `C2-before.txt` records only aggregates — `:13` `commit_total=38 unresolvable=3 nonhash=0 (shapes […]; sites in --json)`, `:18` `DRIFT corpus.pointers.commit_unresolvable: observed=3 expected=0 / empty`. It names no token, and it explicitly defers sites to `--json`.

The identities are in a different file at a different revision: `C2-independent-before.txt:2` pins base `4119647685b60aea6186a8f4efa612502a6f6d3c`, and `:6` lists:

- `corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`
- `corpus/lessons/round-62-verifier-spotcheck.md:13: def4b9fffbf59e9e121b89ef73fbeb89426bd614`
- `corpus/lessons/round-65-verifier-spotcheck.md:11: 7b370d54bd0e74eef4aa90b2e8b2fc9736b3d39f`

with `:7` "The red is the same three repository-context/code-span instances, not a regression introduced by the primary gate repair."

I verified the classification rather than taking it from prose. Resolution via `git cat-file -e <hex>^{commit}`:

| Token | Lane repo | Fleet repo | Lesson context |
|---|---|---|---|
| `451a02ff` | absent | absent | `round-54-verifier-spotcheck.md:147` — nested-backtick code span: "`` commit `451a02ff` `` grammar in the new entry" (must be excluded as context, not resolved) |
| `def4b9ff…` | absent | **present** | `round-62-verifier-spotcheck.md:13` — "`.ufo/reports/round-62/kotoba.md` at fleet commit `def4b9ff…`" |
| `7b370d54…` | absent | **present** | `round-65-verifier-spotcheck.md:11` — "(fleet commit `7b370d54…`, authored"; this is the closure-authored fleet report reference |

Fleet root used by the gate: `verifiers/verify_corpus_integrity.py:125` `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")`, which is the fleet git top level.

So the sentence's *content* is right — one code-span example, two fleet-only objects, one of them closure-authored in r65 — but its *citation* points at a control that carries none of that detail, and the detail it points to sits at base `41196476`, not the control's `11385e04`. That is a provenance defect of the Q60/Q58 family (a receipt cited for content it does not carry), not a false claim (F1).

## Findings

**F1 — medium (calibration/provenance). Token-identity evidence misattributed.** `corpus/lessons/round-66.md:18` says `C2-before.txt` records the exact three tokens; it records counts only (`C2-before.txt:13,18`). Identities are at `C2-independent-before.txt:6` under base `41196476`. The claim is true (verified above) but a reader following the cited path cannot check it. Fix direction: cite `C2-independent-before.txt:2,6-7` for token identity, keep `C2-before.txt:13,18` for the count/DRIFT, and state the different base.

**F2 — small (calibration). Arm-level claim cited to an aggregate control.** `round-66.md:18` attributes "its self-test's no-fleet-hop world fails D2, while the honest fixture passes" to `C2-counter-selftest.txt`, whose entire content is `:4` an aggregate count, `:5` exit, `:8` hash, `:10` prose. The hash pins the source (`:8` = HEAD bytes), and the arms exist at `check_r66_routed_repairs.py:212-213,233-235`, so the claim holds — but it should cite the kill arm plus the hash pin, or a labelled arm transcript, rather than a 14/14 aggregate alone. The base arm (a) is properly receipted.

**F3 — small (consistency). `none` omits the retroactive criterion id.** Precedent `corpus/lessons/round-64.md:63` uses "none at r63 — now **Q60**"; M103 uses "Captured-by: Q61 …" (`round-66.md:32`); M102 writes bare `none` even though Q61 lands in this round and names M102 as its grounding (`corpus/QUALITY.md:76`). Accurate value, incomplete label.

**F4 — small (provenance, adjacent to M102).** Q61's own `grounded in` cell cites "the r66 no-hop counter world (`.ufo/waves/round-66/controls/C2-before.txt`)". That control contains no self-test world — it is the pinned-base counter run plus the integrity DRIFT block. The no-hop world is `check_r66_routed_repairs.py:233-235`, receipted in aggregate at `C2-counter-selftest.txt:4`. Q61's criterion text is satisfied by the gate's self-test, but its grounding citation has the same path mix-up as F1/F2. Not an M102 defect; recorded because it is what makes M102's `none` retroactively resolvable.

**F5 — peripheral, low confidence (no verdict).** The round-66 diff adds a comment at `verifiers/verify_corpus_integrity.py:585` calling the commit hop "the round-11 report-pointer hop's commit analogue". `git log -S'FLEET_ROOT'` shows the fleet-root pointer hop entering in `aeed089` "round-53: routed repairs — corpus fleet-report pointers …". A round-11 report-pointer convention may exist independently (`corpus/lessons/round-11.md:50` mentions "report pointers and commit"), so I do not call this wrong; it is a comment-only nit with no behavioral effect and no bearing on the two questions.

## Confirming evidence (observed this seat, read-only)

- `git show 11385e04:corpus/QUALITY.md`: 60 rows; `grep -c '^| Q61'` → 0; no row text matches `quoted|code.span|resolution set|repository resolution|foreign`; only "fleet root" hit is Q49's grounded-in prose at base line 60.
- `corpus/QUALITY.md:76`: Q61 present at HEAD, `supersedes = —`, grounded in M102 and `verify_corpus_integrity.py --self-test`; `git log -S'Q61'` first lands at `806b53b round-66: land G9 coupling and integrity fixes`.
- `sha256sum verifiers/check_r66_routed_repairs.py` = `git show HEAD:verifiers/check_r66_routed_repairs.py | sha256sum` = `3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141` = `C2-counter-selftest.txt:8`.
- Reset tests on the three tokens via `git -C <repo> cat-file -e <hex>^{commit}`: `451a02ff` absent in lane and fleet; `def4b9ff…` and `7b370d54…` fleet-only.
- `verifiers/check_r66_routed_repairs.py`: `:96` hop conjunct, `:127-129` base-must-be-zero guard, `:194` control arm, `:212-213` honest arms, `:233-235` no-hop kill arm; self-test totals 14 assertions, matching `C2-counter-selftest.txt:4`.
- `verifiers/verify_corpus_integrity.py`: `:125` `FLEET_ROOT`, `:321` `inside_code_span`, `:523` exclusion call site, `:1040/1042` code-span and live-citation arms, `:1055-1057` lane-only/fleet-only/neither arms, `:588-600` lane-first/fleet-root resolver.
- Base resolver was lane-only: the fleet hop, marker and `inside_code_span` are all `+` lines in `git diff 11385e04..HEAD -- verifiers/verify_corpus_integrity.py`; base had `inside_quotes` only.
- Count arithmetic: `C2-before.txt:13` (38 total / 3 unresolved / 5 quoted) → `C2-integrity-after.txt:5` (37 / 0 / 6), consistent with one code-span exclusion plus two fleet resolutions.
- After gate: `C2-integrity-after.txt:4-7` (`tracked=118 unindexed=0`, `9/9 checks pass`, exit 0 at `fc1b71e5…`); routed counter `C2-routed-after.txt:3-8` (`2 of 2`).

## Limits and provenance

- I did not rerun any gate, counter or self-test. Every number above is read from a committed control/receipt, or computed by a read-only git/hash command on committed bytes. No mutation sandbox was used because the questions are evidentiary, not behavioral.
- The pinned base (`11385e04`) and the measured revisions differ by design: `C2-before.txt` measures `11385e04` (counter) and a sandbox clone "at the same revision" (`:11`, integrity); `C2-routed-after`/`C2-integrity-after` measure `fc1b71e5`; `C2-independent-before.txt` measures `41196476`. Statements about "the base" above always name which file and which revision carried them.
- Working tree was not clean (` M .ufo/waves/round-66/w1/swarm-registry.json`); I read committed bytes (`git show HEAD:…`) where the distinction mattered, and the working-tree counter equals HEAD bytes as the sha check shows.
- `451a02ff` is an 8-hex short form; `git cat-file -e` returns nonzero in both repos, which is the correct outcome for a code-span example that Q61 removes before resolution — it is not evidence of a dead live citation.
- No conflicts to report for the canonical judge; no claim, counter, threshold, plan or receipt was changed.

## Out of scope (observed, not adjudicated)

- Q61 supersedes `—`. Base Q41 (`:52`) still says a report hash "resolves in the lane repo" while Q61 permits a declarative fleet fallback for gate evidence. Whether Q41 needs a cross-reference is a quality-bar question for the L1/critic, not an M102 finding; I did not test the round-57 report-hash script.
- M103's independent-gate claims (`round-66.md:32`, 103 assertions) were not audited here; only its Q61 captured-by was read for comparison.
- The dirty `swarm-registry.json` is another seat's surface and was left untouched.

## Artifacts read

- `plans/round-66.md` (C2 before/after predicates, do-nothing control declaration)
- `corpus/lessons/round-66.md:18` (M102), `:32` (M103)
- `corpus/QUALITY.md:76` (Q61); base `11385e04:corpus/QUALITY.md` (Q01–Q60); `corpus/lessons/round-64.md:63` (M96 precedent); `corpus/lessons/round-11.md:50`
- `.ufo/waves/round-66/controls/C2-before.txt`, `C2-counter-selftest.txt`
- `.ufo/waves/round-66/receipts/C2-routed-after.txt`, `C2-integrity-after.txt`, `C2-integrity-selftest.txt`, `C2-independent-before.txt`
- `verifiers/check_r66_routed_repairs.py`, `verifiers/verify_corpus_integrity.py`
- `corpus/lessons/round-54-verifier-spotcheck.md:147`, `round-62-verifier-spotcheck.md:13`, `round-65-verifier-spotcheck.md:11`
