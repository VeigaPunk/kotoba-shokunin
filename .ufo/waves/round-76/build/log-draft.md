# LOG § Round 76 entry — draft (seat B19LogScribe)

Status: **draft, not applied.** The L1 (`KotobaR76`) integrates after the freeze; this file carries the
exact text to paste plus the placeholders that only the integrator can fill from committed bytes.
Nothing here is a measurement of a tip that has not run: at authoring time
`verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` are **absent** from the base
tree (`ls verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` → no such file), and the
round-76 receipts directory held `census-before.txt`, `d4-selftests.txt` and `fetch-recheck.txt` at this
seat's read. Every `<angle-bracket>`
token below is a placeholder; the two Outcome command lines are the **frozen predicate strings quoted
from `plans/round-76.md`** (lines 24 and 40), not observed output.

Sources read for this draft (committed bytes at lane `HEAD` `4de12b61f75c73e3675ef0e422cc2be0f7da8960`; no
tracked file modified — the only untracked paths are round-76 wave-internal: `build/`, `receipts/`,
`snapshots/`, `w1/`, `w1.ready.dispatched`):

- `plans/round-76.md` (committed in `abd8e5cfd45ea3863b344ac58a187b0c5de620d0`)
- `corpus/lessons/round-75-verifier-spotcheck.md` § 6 (R1–R4 verbatim), § 2–5
- `LOG.md:2805-2810` (§ Round 75 filed entry; the append target), `LOG.md:2801-2803` (§ Round 74)
- `.ufo/waves/round-76/base-battery/base-battery.txt`
- `.ufo/waves/round-76/w1-dispatch.json` (64 seats, wave `kotoba-r76-w1`)
- `.ufo/waves/round-76/build/{w2-registry-note.md,scorecard-draft.md,skill-patch.md,quotes-s213.md}`
  (sibling drafts, cited only for interface consistency)
- `.ufo/waves/round-75/w2-results.json`, `.ufo/waves/round-75/w2/*.md` (re-measured, see § Measurement log)

Placeholder substitution table — fill only from a receipt that exists:

| placeholder | meaning | fill from |
|---|---|---|
| `<tip>` | final lane tip the counters and no-harm battery measure | `git rev-parse HEAD` at report time; must equal the first line of `receipts/noharm-at-tip.txt` |
| `<freeze>` | counter-freeze commit (counters + control receipts + snapshots) | the freeze commit's full sha |
| `<land-c1>` | C1 data commit (snapshot chain, entry, SKILL.md rows, S213 used-by, lesson) | the landing commit's full sha |
| `<land-c2>` | C2 repair commit (r75 correction, receipts R1/R2, note filing R3, LOG § Round 75 append R4) | the landing commit's full sha |
| `<land-d>` | disclosed hygiene commit (D2/D3/D4, SCORECARD annotation) | the landing commit's full sha |
| `<lines-at-tip>` | `SKILL.md` line count at `<tip>` | `git show <tip>:SKILL.md \| wc -l`; base 590, planned 595, budget 600 |
| `<tip-rev>` (r75 append) | revision the R2 receipt actually measured | see Flag F2 |

---

## Paste-ready text 1 — `## Round 76` entry (append at end of `LOG.md`, after the Round 75 block)

> `## Round 76 — C1 depth (sourced: description-craft guidance admitted, acted on and audited on kotoba's own description) and C2 consistency (calibration sub-axis: r75 routed defects R1–R4 closed)`
>
> - **Trigger:** the round-76 steer (hyaku run 10, attempt 1) at base `b7f13f4b39cbd43076a85568adca763a6f674e7a`, and the round-75 non-author closure's routed defects R1–R4 (`corpus/lessons/round-75-verifier-spotcheck.md` § 6): R1, the lesson's M75-1 “stale premise” and the `## Gate` reject built on it are false — the 1,021-character figure was current (the r75 spot-check renders 1,022 folded, frontmatter block lines 4–18); R2, the r75 post-landing corpus-gate greens were claimed in prose with no receipt; R3, `R75Attack28` names a report that does not exist (63 of 64 files); R4, the r75 section still ends “w2 falsify results pending”. C1's motivation is `considerthese/2026-10-26.md` proposal 3 (the description page the r75 Gate rejected); the hold is lifted for the documentary half only — the r74 precedent (`corpus/knowledge/spec-skill-creation-craft-round74.md`, S223–S225) admits guide advice with pinned snapshots and located quotes, and every eval-fidelity claim (should-trigger measurement) stays held. Carried check: the r74 closure's D1–D5 — D1 landed in r75; D2–D4 were unworked at base and close this round as disclosed hygiene repairs outside C2's frozen counter; D5 stays conditional and unlanded, recorded not landed.
> - **Action:** plan `abd8e5cfd45ea3863b344ac58a187b0c5de620d0` (`plans/round-76.md`), with the base battery recorded at `b7f13f4` in `.ufo/waves/round-76/base-battery/base-battery.txt`: gate registry `60 of 60; phantom 0`, floors `PASS` (89/25/240), checklist `pass 11`, `check_sibling_reread` `20 of 20`, census exit 0 with 151 rows, `SKILL.md` 590 of 600 lines. That receipt's **two corpus-gate entries carry no gate exit code** — each is the last three JSON lines plus an `exit=$?` taken after a pipe (Flag F6) — and at `b7f13f4` both corpus gates read red on r75-closure drift (the spot-check lesson row unindexed in `corpus/README.md`, `verifiers/corpus-baseline.json` pointers stale); the tip no-harm receipt therefore records both gates' own exit codes after the index row and baseline re-record. Wave `w1` `4de12b61f75c73e3675ef0e422cc2be0f7da8960`: one v2 wave, 64 seats by the committed dispatch (15 executor, 10 scribe, 10 reviewer, 10 scout, 6 critic, 4 mutation-tester, 3 simplifier, 3 revenger, 2 sentinel, 1 connector). Counters frozen at `<freeze>` **before data** — `verifiers/check_desc_craft.py` (C1, six conjuncts) and `verifiers/check_r75_routed_repairs.py` (C2, four repairs) — with the red-before-data and control receipts under `.ufo/waves/round-76/receipts/` (Q37: C1-W1 fabricated stub, C1-W2 real text from the wrong page of the snapshot set, C1-W3 token dump, C2-W1 token dump; each rejected). C1 landed `<land-c1>`: the three-page snapshot chain in `.ufo/waves/round-76/snapshots/` (`optimizing-descriptions.md` `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, `evaluating-skills.md` `a799805f…`, `best-practices.md` `ab9f3b60…`, digests in `MANIFEST.sha256`, `fetch-record.json` HTTP 200 records, and the counter's pinned digest table, the S213 anchor digest moving with them); the entry `corpus/knowledge/description-craft-round76.md` with page-unique located quotes and an audit table; the `SKILL.md` § Body craft description-craft rule row citing the entry and S213; S213's `used-by` cell; and the old→new registry change in `corpus/lessons/round-76.md`. C2 landed `<land-c2>`: the appended r75 correction naming the superseded M75-1 text and Gate reject, with receipt `.ufo/waves/round-76/receipts/r1-folded-render.txt` recomputing the folded render from the measured revision's `SKILL.md` (R1); the tip no-harm receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` cited from § Round 75 (R2); `.ufo/waves/round-76/w2-registry-note.md` reconciling `R75Attack28` with a machine-checkable results excerpt, cited from § Round 75 (R3); the § Round 75 closing append (R4); and the two counter rows in `verifiers/floors-registry.json`, with `verifiers/check_assertion_floors.py` and its in-file tables moved in step. D2 (`d5aebcf` never listed in § Round 74), D3 (missing forward pointer in `corpus/knowledge/sibling-overlap-census-round49.md`) and D4 (`check_spec_craft`/`check_sibling_reread` absent from the floors registry) land `<land-d>` as disclosed hygiene repairs outside both frozen counters, with the `SCORECARD.md` annotation. Assimilation: none — the staged package's description-trigger note rests on the same page and is re-grounded in-round instead (CORPUS.md rule 1); considerthese proposals 1, 2, 4 and 5 are declined with reasons in the round-76 lesson.
> - **Outcome:** `python3 -B verifiers/check_desc_craft.py --rev <tip>` → `description craft backed 6 of 6`, exit 0 (base `b7f13f4` → `description craft backed 0 of 6`, exit 1). `python3 -B verifiers/check_r75_routed_repairs.py --rev <tip>` → `r75 routed repairs closed 4 of 4`, exit 0 (base `b7f13f4` → `r75 routed repairs closed 0 of 4`, exit 1). Both counters' `--self-test` drive `main()` on a satisfying fixture against the exact exit-0 line and carry the must-fail arms (empty snapshot set, quote from the wrong page of the set, digest mismatch, audit value disagreeing with the recompute, missing `used-by`; receipt naming no tip revision, correction naming no superseded text, note absent, closing line absent), and both reject the committed junk worlds. Bound, stated so the headline cannot outrun the counter: the counter counts the snapshot chain, page-unique quotes, the act-on row, the recomputed audit values, the registry cell and the provenance trio — it does **not** adjudicate whether the page teaches these rules (that is the named non-author attack seats' and the closure's judgement), and a script-only reformat that makes the audit numbers agree with the recompute reaches conjunct (d); the headline claims admission, backing and an audit table matching recomputed values only. No-harm at `<tip>`: receipt `.ufo/waves/round-76/receipts/noharm-at-tip.txt` (same battery plus `check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py --json`, census and the line-budget check); `SKILL.md` `<lines-at-tip>` of 600.
> - **Pointer:** `plans/round-76.md`, `corpus/lessons/round-76.md`, `corpus/knowledge/description-craft-round76.md`, `.ufo/waves/round-76/snapshots/`, `.ufo/waves/round-76/receipts/`, `.ufo/waves/round-76/w2-registry-note.md`, `.ufo/waves/round-76/w1/`.

Notes on the paste:
- Strip the `> ` prefix from every line (it marks the boundary of this draft, not LOG content).
- One blank line before the `## Round 76` heading; heading level and bullet order match `## Round 71`–`## Round 73` and `## Round 75`.
- The two Outcome invocations are the frozen predicate's command forms (`plans/round-76.md:24`, `:40`) — do
  not paraphrase them. If a counter prints a different verdict line or exit code at `<tip>`, the claim
  failed: record the **observed** line in the LOG and route the gap, do not paste this text.
- The Action's landing list must match the commits that actually land. Drop any item that does not land
  and record it in `corpus/lessons/round-76.md` instead; an unlanded item left in the LOG is a false claim.
- Do not add a fifth bullet; rounds 71–73 carry four.

---

## Paste-ready text 2 — `## Round 75` closing append (R4 + R2 + R3 citations)

Append-only, immediately after the existing r75 `**Pointer:**` bullet at `LOG.md:2810`
(`- **Pointer:** \`.ufo/waves/round-75/w1/\` (64-seat wave-1 reports); w2 falsify results pending;
\`corpus/lessons/round-75.md\`.`). The filed “w2 falsify results pending” text is **not** rewritten (R4 is
append-only). One blank line before the first appended bullet.

> - **W2 settlement (closing line appended in round 76; R4):** wave `kotoba-r75-w2` settled 64 of 64 results with 0 dead seats and 63 of 64 report files present; the one absent report, seat `R75Attack28` (named `kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md`, which does not exist), is recorded as a phantom in `.ufo/waves/round-76/w2-registry-note.md` (R3).
> - **No-harm receipt (appended in round 76; R2):** the post-landing corpus-gate greens this entry claimed in prose only are re-run and receipted at `<tip-rev>` in `.ufo/waves/round-76/receipts/noharm-at-tip.txt` — `python3 -B verifiers/verify_corpus_integrity.py --json` and `python3 -B verifiers/verify_corpus_independent.py --json`, stdout and exit codes recorded.

Consistency with the owner: the R4 sentence is **verbatim** the text seat `B09RepairR3R4` adopted and
asked to be mirrored (IRC, this wave); B09 owns R4 and explicitly leaves the R2 receipt sentence to
this seat. If B09 lands a different R4 wording, mirror B09's file rather than this copy and leave the R4
anchor strings below unchanged only if they still occur in the landed sentence — otherwise update the
anchor list, not the filed entry.

Placement facts verified for the append: `LOG.md` ends at line 2810 with the r75 Pointer bullet and a
single trailing newline (`tail -c 200 | xxd`: `…round-75.md`.\n`); § Round 75 spans lines 2805–2810;
§ Round 74 spans 2801–2803. The wave id `kotoba-r75-w2` is grounded in `.ufo/waves/round-75/w2-dispatch.json`
(`wave` field); `w2-results.json` itself carries `wave: "w2"`, `lane: "kotoba"`, `round: 75` — if the
counter reads the id from the results file, use `w2` in the sentence instead and adjust the R4 anchor.

---

## Anchor strings the C2 counter must look for (settle with `B07RepairCounter` before freeze)

`verifiers/check_r75_routed_repairs.py` checks content, not filenames (plan § C2). The literal strings
this draft commits to, in `LOG.md` § Round 75 (lines ≥ 2811 after the append):

| repair | required to occur in § Round 75 | occurs in |
|---|---|---|
| R4 (closing line, appended after “w2 falsify results pending”) | `wave \`kotoba-r75-w2\` settled 64 of 64 results with 0 dead seats and 63 of 64 report files present` and `R75Attack28` and `phantom` | append bullet 1 |
| R3 (note cited) | `.ufo/waves/round-76/w2-registry-note.md` | append bullet 1 |
| R2 (receipt cited) | `.ufo/waves/round-76/receipts/noharm-at-tip.txt` | append bullet 2 |

Ordering requirement: both appended bullets must sit **after** the string `w2 falsify results pending`
(currently `LOG.md:2810`). A counter that checks only presence would pass on a pre-append file if the
strings collided elsewhere; requiring index(citation) > index(`w2 falsify results pending`) makes the
append-ness machine-checkable, which is what R4's wording asks for.

For C1's conjunct (e) the lesson logs the S213 `used-by` old→new change in
`corpus/lessons/round-76.md`; the LOG entry names it but the counter must read the lesson, not this text.

---

## Cross-draft consistency (checked against sibling drafts, this wave)

- `build/scorecard-draft.md` (B18): same claim labels, same frozen predicate sentences, same base
  revision, same `0 of 6` / `0 of 4` base readings, same tip-receipt paths; its placeholder set
  (`<tip>`, `<C1 tip receipt path>`, `<C2 tip receipt path>`) is compatible — the LOG entry names
  `.ufo/waves/round-76/receipts/noharm-at-tip.txt` and the counter commands rather than separate C1/C2 tip
  receipts, so if B18's integrator keeps per-claim tip receipts, add their paths to the LOG Outcome
  rather than renaming this draft's clause.
- `build/w2-registry-note.md` (B09): the numbers the closing line quotes (64 seats / 64 results / 0 empty
  outputs / 63 `.md` files / 64 directory entries with `swarm-registry.json` / `R75Attack28` absent in
  both path forms / no add-commit in any ref) match its re-measurements and mine. **File the note at the
  landing path `.ufo/waves/round-76/w2-registry-note.md`, not the `build/` copy** — the counter reads the
  landing path.
- `build/skill-patch.md` (B13): `SKILL.md` 590 → 595 planned (+5: 1 preamble wrap, 1 rule row, 2 registry
  rows, rounded by the wrap); the entry `corpus/knowledge/description-craft-round76.md` and the counter
  name cited in the LOG Action are the ones that patch names.
- `build/quotes-s213.md` (B04): S213 digest `7cc54fbb…` and the two other snapshot digests match
  `snapshots/MANIFEST.sha256` and my own `sha256sum` of the files.
- `build/B10RepairD2D3.*` (B10): the D2 repair exists in two forms — formA inserts inside § Round 74 and
  breaks the base-LOG byte-prefix property, formB appends a `## Round 74 correction (append-only …)`
  section at the tail. This entry is also tail-appended, so formB and it compose in either order and keep
  the prefix; if the L1 chooses formA instead, nothing in this draft changes (it names § Round 74 but does
  not depend on formA's bytes).

---

## Measurement log (commands actually run by this seat, read-only)

Working directory `/home/vgpnk/Projects/shokunin/kotoba-shokunin` throughout.

| command | observed |
|---|---|
| `git rev-parse HEAD` | `4de12b61f75c73e3675ef0e422cc2be0f7da8960` |
| `git status --porcelain` | `?? .ufo/waves/round-76/w1.ready.partial`, `?? .ufo/waves/round-76/w1/` (dispatcher output, not mine) |
| `git log --oneline -8` | `4de12b6` (wave spec+dispatch), `abd8e5c` (plan + base battery), `b7f13f4` (r75 closure spot-check) … |
| `git show --stat abd8e5c` | 2 files, `plans/round-76.md` 74 +, `base-battery.txt` 36 + |
| `git show --stat 4de12b6` | 3 files, `w1-dispatch.json`, `w1-spec.json`, `w1.ready`; `counts.spawn` 64 |
| `git show b7f13f4…:SKILL.md \| wc -l` | `590` |
| folded description render at `b7f13f4` **and** `ac9f295` | 15 value lines (frontmatter 4–18); `' '.join(lines)` = **1021** chars; with the folded scalar's terminating newline = **1022**; PyYAML on the frontmatter text with the closing newline stripped = **1021** (see Flag F1) |
| `ls .ufo/waves/round-75/w2/*.md \| wc -l` | `63` |
| `python3` read of `.ufo/waves/round-75/w2-results.json` | `seats` 64, `results` 64 entries, 64 unique names, 0 empty `output` |
| `sha256sum .ufo/waves/round-76/snapshots/*.md` vs `MANIFEST.sha256` | three-way match: `7cc54fbb…`, `a799805f…`, `ab9f3b60…` |
| `grep -n "w2 falsify results pending" LOG.md` | `2810` (single occurrence) |
| `grep -n "^## Round" LOG.md \| tail` | § 74 at 2801, § 75 at 2805; no § 76 yet |
| `ls .ufo/waves/round-76/build/ ; ls .ufo/waves/round-76/receipts/ ; ls .ufo/waves/round-76/snapshots/` | `build`: `w2-registry-note.md`, `scorecard-draft.md`, `skill-patch.md`, `quotes-s213.md`, `check_receipt_revs.sh`, `log-draft.md` (this file); `receipts`: `census-before.txt`, `d4-selftests.txt`, `fetch-recheck.txt`; `snapshots`: the three pages + `MANIFEST.sha256` + `fetch-record.json` |
| `ls .ufo/waves/round-76/w1/*.md \| wc -l` | `20` at this seat's read and growing — the wave's reports are still landing |
| role census of `w1-dispatch.json` `taskCall.tasks` (`agent` field) | executor 15, scribe 10, reviewer 10, scout 10, critic 6, mutation-tester 4, simplifier 3, revenger 3, sentinel 2, connector 1 = 64; `grep -c sonic w1-spec.json w1-dispatch.json` → `0`, `0` (see Flag F5) |
| read `.ufo/waves/round-76/base-battery/base-battery.txt` | 36 lines; the two corpus-gate sections are truncated to `}`, `]`, `}` followed by `exit=0` (a post-pipe `$?`), and `check_spec_craft.py` shows only its three `backed:` lines — no gate exit code for those three entries (Flag F6) |
| `.ufo/waves/round-75/w2-dispatch.json` `wave` field | `kotoba-r75-w2` (the `w2-results.json` carries `wave: "w2"`) |

No writes were made outside `.ufo/waves/round-76/build/log-draft.md` and
`.ufo/waves/round-76/w1/B19LogScribe.md`. No git/jj mutation; no process started; no install.

---

## Flags for the L1 (do not silently resolve; each is a counter-visible definition)

**F1 — the folded-render number is convention-dependent (1021 vs 1022).** Measured on committed bytes at
both `b7f13f4` and `ac9f295`: the description value occupies 15 lines (frontmatter lines 4–18), the lines
joined by single spaces are 1021 characters, and adding the folded scalar's terminating newline gives
1022. The r75 spot-check (§ 4, reject row) asserts 1,022; plan § C2 R1 requires the receipt to
“recomput[e] the render length from the measured revision's `SKILL.md` and prin[t] 1022”, and requires
the counter to recompute R1's 1022 from bytes. A counter whose recompute uses the PyYAML/no-trailing-
newline reading prints 1021 and then cannot both recompute and agree. **Pin the convention explicitly**
in `check_r75_routed_repairs.py`, in `receipts/r1-folded-render.txt`, and in the lesson correction (e.g.
“folded scalar incl. its terminating line break”), and align C1's conjunct (d) to the same convention —
otherwise the two claims can disagree on the same string. Messaged to `B07RepairCounter` and
`B06DescCounter`; unresolved as of this draft.

**F2 — R2's receipt revision.** R2 as worded by the spot-check asks for a receipt at the **r75** final tip
(`ac9f29510d3914a6edb97c8dbdb3445cab9141de`); plan § C2 R2 relocates it to
`.ufo/waves/round-76/receipts/noharm-at-tip.txt` and requires it to name “the tip revision on its first
line”, which in this round reads as the round-76 tip. A receipt measuring only the round-76 tip does not
by itself prove r75's claimed greens. Honest closures: (i) the receipt carries **both** measurements —
`ac9f295` via a scratch worktree (`verify_corpus_integrity.py` accepts `--repo`) on its first two lines,
then the round-76 tip — and the § Round 75 bullet names `ac9f295`; or (ii) the bullet says only that the
gates are re-run at the round-76 tip and drops any r75-tip implication. Pick one and make the counter
check the revision it actually requires. Also note the spot-check's own suggested path was
`.ufo/waves/round-75/receipts/noharm-at-tip.txt`; the plan's round-76 path governs, and the § Round 75
bullet must cite the plan path (both are cited here in that order of authority). Messaged to
`B07RepairCounter`.

**F3 — D2/D3/D4 sit outside both counters.** The LOG Action discloses them; a closure that reads only the
two counter lines will not see them. Their receipts (`.ufo/waves/round-76/receipts/d4-selftests.txt` and
siblings) must be named in the report or they are unverifiable hygiene claims.

**F4 — `w1/` is untracked at authoring time.** The wave's own reports land under `.ufo/waves/round-76/w1/`
and were not committed when this draft was written; the Pointer bullet names the directory, so the
integrator must commit the reports (as in r75) before the Pointer resolves.

**F5 — the wave's stated build/attack split is not reproducible, and one declared L2 role has no seat.**
Plan § Wave shape states “**64 seats** — 30 build + 34 attack (attack share 53%)” and lists a §3 L2 floor
that includes `labrat 4` and `sonic 1`. The committed dispatch (`w1-dispatch.json`, `4de12b6`) registers
64 seats with these roles: 15 executor, 10 scribe, 10 reviewer, 10 scout, 6 critic, 4 mutation-tester,
3 simplifier, 3 revenger, 2 sentinel, 1 connector; `grep -c sonic` is `0` in both `w1-spec.json` and
`w1-dispatch.json`. Counting attack seats by the plan's own definition (reviewer, critic,
mutation-tester, sentinel, simplifier, revenger) gives 28; adding the 10 scouts gives 38; by the `A`
name prefix it is 36 — none is 34, so 53% is not reproducible from the wave's own artifact. Labrats exist
only as seat-level children (every seat prompt says “no subagent dispatch except your single labrat”), so
`labrat 4` is met off-wave; `sonic 1` has no seat anywhere in the dispatch, so that declared floor is
unmet at wave level. This LOG entry therefore states the dispatch's **role census** and no build/attack
split; the mismatch belongs in `corpus/lessons/round-76.md` as its own row, not in the LOG as an
unreproducible number. Separately, the wave commit message (`4de12b6`) reads “34% attack share” — a third
variant of the same figure.

**F6 — the base battery's corpus-gate entries cannot be read as greens, and R2 now needs a touch-list
addendum.** `.ufo/waves/round-76/base-battery/base-battery.txt` prints, for each of
`verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json`, only the last three lines of
the JSON (`}`, `]`, `}`) followed by `exit=0`; that `exit=$?` was taken after a pipe, so it reports the
pipeline's status, not the gate's. `check_spec_craft.py`'s verdict line is truncated the same way (only
its three `backed:` lines survive; its `spec craft pages backed 3 of 3` line is not in the receipt). Seat
`B10RepairD2D3` re-measured both corpus gates at `b7f13f4` and `4de12b6`: **exit 1** with four DRIFTs —
`corpus.index.tracked_files` 145 vs 144, `corpus.index.unindexed` 1 vs 0 (the r75 spot-check lesson has no
`corpus/README.md` row), `corpus.pointers.report_total` 101 vs 99, `corpus.pointers.commit_total` 44 vs 43
— root cause the r75 closure commit (`b7f13f4`) landing the lesson unindexed without re-recording
`verifiers/corpus-baseline.json` (evidence:
`.ufo/waves/round-76/build/B10RepairD2D3.measurements.txt` § 3–4). This seat did **not** re-run those
gates; the peer measurement is taken as given. Consequences:
(i) the LOG Action must not republish `exit 0` for those two gates — this draft now states the artifact and
the red state instead;
(ii) C2's R2 receipt can show green only after the `corpus/README.md` index row lands **and**
`verifiers/corpus-baseline.json` is re-recorded; `verifiers/corpus-baseline.json` is **absent from plan
§ Touch list**, so landing it is a disclosed scope deviation and needs `plans/round-76-addendum-1.md`;
(iii) F2 gains a path: measure `ac9f295` (the r75 tip) first — if the drift is introduced by `b7f13f4`
itself, `ac9f295` is the revision R2 is about and belongs on the receipt's first line;
(iv) every receipt this round must capture exit codes without a pipeline
(`cmd >out 2>&1; rc=$?`, or `set -o pipefail`).

---

## What this seat did not do (scope)

- Did not edit `LOG.md`, `SCORECARD.md`, `SKILL.md`, any verifier, any lesson or entry — draft only.
- Did not run either frozen counter (absent at authoring time) and did not produce any receipt.
- Did not draft the § Round 74 `d5aebcf` line (D2) or the SCORECARD annotation (B18).
