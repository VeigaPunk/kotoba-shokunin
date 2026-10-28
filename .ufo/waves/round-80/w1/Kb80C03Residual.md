# Kb80C03Residual — residual + no-harm attack (round 80, w1)

Seat: critic (leaf). Scope: attack the residuals and the no-harm claim across four assigned
questions. Method: read-only analysis over committed bytes at base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, the r79 reviewed drafts, the round-80 plan, and
this round's receipts/build outputs as they existed at review time. No lane file mutated; no
counter after-value measured (the battery is Kb80E10Battery's seat). Every claim below carries
its command or its quoted bytes.

Evidence base (commands actually run, own exit status captured):

- `git -C <lane> diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 -- <six battery instruments>` →
  `22  3  verifiers/check_assertion_floors.py` only. The other five instruments are unchanged
  from the r73 pinned base. So "22 already spent at base" (plan kill rule) is exact, and the
  seat prompt's "22 spent + 38 headroom" reads: cap 40 → 18 headroom; cap 60 → 38 headroom.
- `git apply --numstat .ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`
  at base → `17  0  verifiers/verify_corpus_integrity.py`, applies clean. The plan's "+17 E04"
  is exact. Plan arithmetic 22 + 17 + grammar ≤ 21 = 60 therefore saturates the new cap exactly
  at the landed tip.
- Lane `verifiers/check_tip_battery.py:105` today: `LINE_CAP = 40`; `INSTRUMENT_PINS` holds
  1–3 blobs per instrument (11 pins total). E5 is a real amendment, not yet landed at review time.
- `.ufo/waves/round-80/receipts/census-before.txt` (this round's own receipt): 24 lines
  `kotoba W04 … across scopes` (including S227/S229/S230/S231 — the six C2 rows themselves
  duplicate pre-existing URLs across scopes), then `kotoba ok …/corpus/SOURCES.md`. Exit 0.
  This is live evidence that W04 never moves the census exit.
- Registry id sweep: `grep -oE '^\| S[0-9]+' corpus/SOURCES.md | sort -u` → max id **S231**.
  New rejection rows at S232+ are E03-collision-free.
- `scripts/sources-census.sh:640-653,671-672`: E04 fires only when the current row is
  non-rejected AND a prior non-rejected row holds the same (URL, scope) pair AND teaches lacks
  `supersedes S[0-9]{3}`; W04 fires when a URL is seen under a new scope string, with no
  status guard; W02 fires when a rejected row's teaches cell is < 8 chars. Selftest arms
  "W04-does-not-fail-validation" (exit 0) and "W-only-registry-exit-0" (exit 0).
- Both corpus gates count the same git universe: `verify_corpus_independent.py:104-113`
  (`tracked_paths` → `git ls-files corpus/`) and `verify_corpus_integrity.py:616-617`
  (`git ls-files corpus/`). The refresh script performs no third-source count of its own.
- `check_report_pointers.py` docstring + `corpus/QUALITY.md:84` (Q68) + plan line 59: the gate
  resolves every backticked lane pointer at the cited rev; plan line 59 is the plan's only
  mention of it or of `check_sibling_census.py`. No fallback sentence exists anywhere in
  `plans/round-80.md` for either (grep: one hit, line 59).
- `.ufo/waves/round-79/build/Kb79E03IndexBaseline.baseline-snapshot.patch`: the r79 refresh
  recorded tracked_files 144→150, report_total 99→106, commit_total 43→45, **carrying**
  `corpus.pointers.report_dead` at observed 1 (`--carry corpus.pointers.report_dead`), and
  stamped the instrument divergence "integrity 1 vs independent 0" plus a
  `measured_against.head` of a **detached scratch commit "not resolvable in the lane
  repository"**.
- `.ufo/waves/round-80/receipts/` at review time contains only `census-before.txt`,
  `m80-1-pipe-vs-direct.txt`, `tipbattery-base-dot.txt`. `freeze-shas.txt` and the abs-form
  base receipt are not yet present (peers in flight; L1 must land them before any 6-of-6).

---

## 1. What does the round HARM? (erratum E5: LINE_CAP 40→60)

**The direct capability delta is smaller than the seat prompt assumes, and the plan does price
the core of it — but two consequences are unpriced.**

Concretely, what 60 lines permit that 40 did not, against the r73 pinned base with 22 already
spent at the r80 base:

- Single-instrument additions of 19–38 lines become size-legal (cap 40 leaves 18; cap 60
  leaves 38). Concrete shapes that fit in 19–38 lines, per instrument:
  - `verify_corpus_integrity.py` (1470 lines): a worktree-fallback or symlink-accepting arm in
    report-pointer resolution (~15–25 lines) — the exact class the E04 repair is hardening.
  - `verify_corpus_independent.py` (1153 lines): a parallel grammar/exception arm (~10–20).
  - `verify_skill_checklist.py` (2821 lines): an exception table for the citation-resolution
    arm (~15–25 lines).
  - `check_gate_registry.py` (378 lines) / `check_assertion_floors.py` (1422 lines): a
    row-exemption or floor-relaxation list (~5–15 lines — these would have fit even under the
    old 18-line headroom).
- The deletions side loosens identically: up to 57 further deletions at the r80 tip (60 − 3
  already spent) vs 37 under cap 40.

**Do the pins still catch them? Yes — and this is the load-bearing fact the plan states once,
correctly, before data (kill-rule parenthetical, plan line 26): `instrument-pin` is
byte-exact.** Any edit to any of the six instruments changes its blob sha; the guard
(`check_tip_battery.py:330-337`) fails the rev unless the blob equals the r73 base or a listed
pin, with no size dimension at all. Every weakening listed above fails `instrument-pin`
regardless of the cap. The stub control (W6) fails on both guards (+2/−~1000 trips the
deletion side under any cap). So under the **frozen r80 counter**, the extra 20 lines buy a
laundering world nothing: the cap only ever binds in worlds where the pin layer is
simultaneously relaxed.

The two worlds where the cap number matters:

1. **Counter-amending future rounds.** A future round declares its own erratum (E2 set the
   precedent in r72; E5 extends it) adding a "reviewed" blob to `INSTRUMENT_PINS` and an
   instrument edit within the cap. In that world the cap is that round's own declared bound —
   60 vs 40 changes the depth of weakening one round may self-authorize by exactly 20 lines,
   but the hole is the pin-table amendment channel, not its size. The counter's own bytes are
   guarded by no guard: the round freeze receipt (`freeze-shas.txt`) is a social control, and
   the kill rule binds only the round that declares it.
2. **The saturation inversion — unpriced.** Because 22 + 17 + ≤21 = 60 exactly, the r80 tip
   consumes the entire budget. Under the frozen counter, round 81+ has **zero** headroom for
   any instrument repair: any single-line fix to a battery instrument requires a further
   erratum (E6). The plan nowhere states that E5 converts the cap from a per-round budget
   into a permanently exhausted one; this is the round's real legacy, an operability debt
   inherited by every future round, and it is not priced.

Also unpriced: **pin-table growth is monotonic weakening of `instrument-pin`.** 11 pins today,
13 after E5 (one for the E04+grammar integrity blob, one for the grammar independent blob —
"exactly the two reviewed blobs the instrument seats publish", plan C1). Each additional
allowed blob is another byte-exact instrument the guard will accept; three rounds (r72, r76
bump, r80) have now each grown the table. No plan text notes the cumulative direction.

**Is the harm priced anywhere?** Partially, once, before data: plan line 26 ("the pin guard
carries the anti-laundering load … the size bound is secondary"), which is the correct pricing
for the capability question. Not priced: the saturation consequence, the cumulative pin-table
growth, and the unguarded-counter channel. None of these is a fixable defect in this round's
frozen predicates — they are tradeoffs the canonical judge should weigh as declared costs.
**Smallest safe correction:** one plan sentence recording (a) 60/60 saturation at the tip and
its E6-for-any-future-touch consequence, (b) that future pin additions must name the reviewing
seat per blob (the plan already requires the blobs be "reviewed" — make the reviewer explicit
in the receipt), and (c) that the cap escalation precedent is E5's true cost.

## 2. Is the baseline refresh self-sealing?

**Not merely transcription — it is two-instrument-agreed transcription with the zero-mode
classes never fitted, which is the right design for a calibration axis; the residual
self-sealing channel is a shared measurement universe, and there are three smaller provenance
nits.**

What the refresh script actually does (`refresh-corpus-baseline.py`, read in full):

- Records the three `equal`-mode expectations (`tracked_files`, `report_total`,
  `commit_total`) from the integrity gate's **own** `--no-baseline --json` observation — yes,
  the gate's own output is the source (docstring: "copied from the gate's own … observation").
- **Cross-checks every recorded class against the independent re-derivation**
  (`INDEPENDENT_KEYS` + `HARD_CROSS_CHECK`): disagreement on any of the six hard classes
  **refuses** the write (exit 2, baseline untouched). Single-gate transcription bugs are
  caught. The independent gate is a separate implementation with its own tokenizer and
  counting code (`verify_corpus_independent.py` docstring), so agreement is evidence, not
  restatement — for the harvest-based classes (`report_total`, `commit_total`) this is a real
  independence test.
- **Zero-mode classes are never fitted**: `expect` stays 0; a nonzero observation refuses
  unless named by `--carry`; the plan mandates `--carry none`, so at the r80 refresh every
  zero class must already read 0 — i.e. repairs 2+4 must have landed first. This is the
  anti-self-sealing load, and it is correctly placed: the classes that adjudicate violations
  can never be laundered into the baseline.
- Post-write it re-runs the gate and refuses (exit 3) on any drift it does not own.

### Critical correction: external-commit blocker provenance

The plan's description of the two base `commit_unresolvable` blockers is contradicted by the
round's own primary receipts. `Kb80E02-base-integrity.json:54-56` and
`Kb80E02-base-independent.txt:28-29` name **only**:

- `corpus/SOURCES.md:171` — `7bb48f213ac677f943d5c791199ed3dddf302f00`
- `corpus/SOURCES.md:172` — the same hash.

The S230 row attributes the same pure-hex token to `badlogic/pi-mono`, while S231 names it as
the Vibe served revision; the fetch records disambiguate the provenance: S230's pi-mono
`main`/path commits are `bb65e3e4…` / `25c5c7bf…`, and S231's Mistral Vibe `main` commit is
`7bb48f21…`. The owner/repo is a separate backticked token before `commit`, not an
`owner/repo@<hex>` token. The plan's specific google-gemini/zed examples therefore do not
identify the measured blockers.


This is a direct counterexample to a grammar class implemented **only** for in-token
`owner/repo@<hex>`: that predicate catches neither measured blocker. The broader plan
parenthetical (“or otherwise an explicit third-repository citation”) is necessary. The
published `Kb80S07Quality-world.patch` does implement line-context markers (backticked
`owner/repo` before `commit`, and a single raw-GitHub source URL); Kb80E12Census measured both
gates with E04+S07: `commit_unresolvable` 2→0, `external=2` (gate exits remain 1 for other
drifts). Thus the marker class does clear the actual blockers in that world; this is not an
open unresolvable-token bug for that candidate.

However, its INFO provenance is wrong for S230: the candidate reports hash `7bb48f…` as
`repo badlogic/pi-mono` because it takes the row URL, while the fetch records show that hash
belongs to Mistral Vibe. The classification-only gate clears the red but must not be read as
validation of the source attribution. The plan should replace its named google-gemini/zed
examples with the actual S230/S231 blockers, and the lesson should record the S230 row/fetch
record mismatch. The source row itself is pinned/re-opened and must not be edited in place.

Impact: C1's actual external-class zero is measured in the S07 scratch world; the remaining
blocker is the candidate's size kill rule (§ following), plus the source-provenance error.
This does not affect C2's form-level depth predicate.

### Stack-assembly counterexample: the current grammar candidate cannot fit

I measured the published candidate directly with read-only
`git apply --numstat .ufo/waves/round-80/build/Kb80S07Quality-world.patch`:
`96 1 verifiers/verify_corpus_integrity.py` and
`75 4 verifiers/verify_corpus_independent.py` — 171 added lines across the two guarded
instruments. Together with the independently measured base `22/3` and E04 `17/0`, that
produces `210 added / 8 deleted` against the pinned r73 base, not the plan's maximum
`60 added`; the amended cap-60 counter (`Kb80E06CounterErratum.cap60-provisional.py:111-119`)
still fails `instrument-size`. The plan leaves only 21 added lines for grammar after 22 base
+ 17 E04; the published candidate is eight times that remainder. If this is the E05 repair
that lands, the plan's kill rule requires an honest C1 stop, not a larger cap or a post-data
budget rewrite. The smallest safe correction is a grammar implementation with all required
classifiers and red-before arms within 21 added instrument lines; if that cannot be done,
stop C1 as declared.

Do not use the apparent helper-file escape as a safe way around this limit. The frozen
counter's `BATTERY` list (`verifiers/check_tip_battery.py:145-152`) and `INSTRUMENT_PINS`
cover only the six gate scripts; `instrument-size` diffs only that list
(`:292-320`), and `no-deletions` derives failures only from base paths missing at the rev
(`:250-264`)—it does not reject new paths. A new helper under `verifiers/` imported by a
pinned gate would therefore be outside both the numstat scope and the blob-pin check:
changing helper bytes could alter gate results while the pinned gate blob stays unchanged.
Safely guarding that helper requires changing the frozen counter's script/pin inventory
(guard logic), which the plan's kill rule itself forbids without stopping C1. The E12 note's
suggested helper move is thus not a safe third option; within this frozen counter, the only
safe route is a <=21-added-line implementation inside the already pinned instruments,
otherwise the declared honest stop.

The C2 entry did initially contain a third citation context: line 125 said the Mistral Vibe
README was served from full hash `7bb48f213ac677f943d5c791199ed3dddf302f00`, with only the
bare name `mistral-vibe` on that line. The candidate's owner/repo-before-`commit` and
single-GitHub-URL markers would not match it. **This specific hazard is now fixed in the
current build entry bytes:** lines 129–130 refer to `S230.fetch.json` / `S231.fetch.json`
rather than embedding hashes, and Kb80E08C2Entry reports the integrity gate's COMMIT_RE scan
found zero commit-shaped citations in the entry. This is evidence that the entry no longer
adds an unresolvable citation; do not leave the earlier finding labelled open.

There remains an adjacent source-provenance defect in the frozen `corpus/SOURCES.md` row:
S230:171 attributes `7bb48f213ac677f943d5c791199ed3dddf302f00` to `badlogic/pi-mono`, while
`.ufo/waves/round-79/snapshots/S230.fetch.json:10` records pi-mono `main` at
`bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` and the last commit touching the fetched path as
`25c5c7bf4cbc76b2e134c729eb8d57d521ed749`; `.ufo/waves/round-79/snapshots/S231.fetch.json`
identifies `7bb48f…` as the Mistral Vibe revision. The negative-sweep/new-entry citation
fix does not repair that frozen row. Since this round's frontier step says the six re-opened
rows receive no other cell changes, the smallest safe correction is an append-only lesson
erratum identifying the S230 attribution mismatch; do not edit the pinned source row this
round.

### Adjacent C2 residual: the actual HTML Q70 quote is structurally rejected

`Kb80S11GateQuotes.md` § F1 and companion receipts report a direct counter probe on the
real S229 snapshot: `quote_location()` returns false with “quote lies in the first-heading
block (Q70)”; all other five entry quotes pass. The artifact traces the mismatch: HTML
tag-stripping removes the page's real `<h1>` (raw S229-msaf.html line 676); the first
text-view line starting `#` is a Python comment at view line 169, while the sole
`allowed-tools` occurrence / available quote is at view line 95. The draft rule
`idx <= first_head + 1` therefore rejects the only admissible S229 quote, not merely a
suboptimal quote choice. This is a C2 reachability defect: without a Q70-correct HTML heading
rule, the counter cannot document all six surfaces and the `N == 6` predicate cannot pass.
Smallest safe correction: derive heading boundaries from the HTML structure before tag
stripping (or otherwise preserve a typed heading marker), then re-probe S229 plus Markdown
Q70 controls. This is not fixed by the hash-removal edit above.

Impact: the E5 cap / E05 size finding remains conditional on the intended patch; S230/S231
still require line-context classification, and the S230 source-row attribution mismatch is
an append-only lesson erratum because the frontier forbids rewriting those re-opened cells.
The C2 entry's extra commit citation is fixed; the independent S229 Q70 defect remains and
impacts C2 depth.

Impact: C1 remains conditional on an E05 implementation that fits the declared 21-line
remainder and makes both corpus gates classify the actual S230/S231 blockers as external.
Separately, the current published C2 counter has a measured S229 Q70 false negative, so its
six-of-six headline is not substantiated until the HTML heading defect is repaired and
re-probed. These are distinct, fixable instrument defects; neither is fixed by deleting the
extra hash from the C2 entry.

 

Where the self-sealing critique still bites:

- **Shared universe.** Both gates derive `tracked_files` from `git ls-files corpus/`
  (independent `:106`, integrity `:617`) and both harvest commit/report tokens from the same
  tracked corpus files. The cross-check verifies two implementations of the *same
  measurement universe*; a universe-level blind spot (an identically wrong ls-files scope, a
  shared token-exclusion rule) self-seals with both instruments in smiling agreement. The
  refresh script never performs its own third-source count (a direct `git ls-files corpus/ |
  wc -l` inside the script would anchor `tracked_files` outside both gates). Mitigation
  already present: the recorded classes are raw counts where universe bugs are unlikely, and
  the zero classes stay pinned at 0. Assessment: a real but narrow residual, acceptable for a
  calibration anchor — the baseline's honest job is "the tip matches the recorded tip", not
  "the counts are metaphysically true".
- **Carry-forward provenance.** The r79 snapshot shows the mechanism's weak point in action:
  the r79 refresh *carried* `report_dead` at 1 (integrity reads the dead
  `HEAD:.ufo/reports/round-77/kotoba.md` token; independent reads 0 — the divergence is
  stamped, honestly). The r80 plan's "--carry none" converts that carried residual into a hard
  refusal: if repairs 2+4 do not zero `report_dead`, the refresh exits 2 and C1 stops. The
  plan asserts (does not prove) the repairs zero it — the E04 patch's resolution arm is
  exactly where that assertion lives. Coupling worth naming, not a defect.
- **Provenance nits (unpriced, all fixable in one line each):**
  1. `--note-key` defaults to `round79_rerecord` and the note text says "round 79 C1 repair"
     verbatim; the plan's literal refresh command omits `--note-key`, so the r80 baseline
     would record round-80 facts under a round-79 label — provenance drift in a committed
     file whose entire purpose is provenance.
  2. The r79 `measured_against.head` is a detached scratch commit "not resolvable in the lane
     repository". If the L1 runs the r80 refresh in a scratch clone again, the committed
     baseline again names a foreign object. Running it in the lane at the real pre-report
     commit (clean-tree precondition holds there) keeps the head resolvable.
  3. `as_of` uses `date.today()` — host-local; fine on UTC hosts, but the census selftest
     goes to some length over UTC date handling and the baseline does not.

**Smallest safe correction:** pass `--note-key round80_rerecord`; run the refresh in the lane
at the true pre-report commit; add the script's own `git ls-files corpus/ | wc -l` anchor as
a third-source check on `tracked_files` (one subprocess call, refuses on mismatch). Item 3
may be left as-is.

## 3. S232+ rejection rows — census W04 duplicates: exit status and warning text

**Measured: the census exits 0 after all twelve S232–S243 rejection rows are added.** The
after-receipt records 31 total W04 warnings (24 before + 7 new), then `kotoba-shokunin ok`,
`exit=0`; no W02 is emitted.

Mechanics (`sources-census.sh:640-653,671-672`), with the selftest's own exit captures:

- **E04 is structurally silent for rejected rows.** It requires the *current* row to be
  non-rejected (`status!="rejected"`) and a *prior* non-rejected row for the same
  normalized-URL+scope pair (`url_scope_nonrejected`). A rejected row duplicates nothing:
  not as the new row, and not as the prior row (the r79 selftest's
  "E04-rejected-pair-exemption-mutant" pins the both-rejected case at exit 0). The escape is
  deliberate: a retained rejection must be able to name the URL it rejected.
- **W04 is the warning that will fire.** It has no status guard: any row whose normalized URL
  was already seen under a *different scope string* prints
  `kotoba\tW04\tS23x duplicate url <host/path> across scopes` and never moves the exit
  (selftest "W04-does-not-fail-validation" → exit 0; "W-only-registry-exit-0" → exit 0; this
  round's `census-before.txt` already shows 24 W04 lines then `kotoba ok`, exit 0).
- **W02 is the other plausible warning:** `kotoba\tW02\tS23x thin reject reason` when the
  teaches cell is under 8 chars. Any real rejection sentence clears it trivially.
- The E-classes that could actually red the census for the new rows are the ordinary ones:
  E03 duplicate id (impossible — registry max is S231), E08 future opened date (rows are
  opened 2026-10-27 = today, fine), E09 malformed recheck, E11 dangling used-by path on disk
  (rejection rows should carry `—`; if the L1 names the round-80 lesson instead, that file
  must exist in the worktree at validate time).

Actual new W04 rows in `.ufo/waves/round-80/build/Kb80E12Census-census-after-174.txt` are:
S234 `opencode.ai/docs/skills`, S235 `geminicli.com/docs/cli/skills`, S238
`ampcode.com/docs/customize/skills`, S239 `docs.roocode.com/features/skills`, S240
`kilo.ai/docs/customize/skills`, S241 `junie.jetbrains.com/docs/agent-skills.html`, and
S243 `hermes-agent.nousresearch.com/docs/user-guide/features/skills`; each says
`duplicate url <normalized-url> across scopes`. Thus the earlier prediction was partly right
(kilo does warn) but wrong about learn.chatgpt.com: it emits no new W04 for the added rows.
The receipt shows no W02 warnings, so the actual rejection teaches cells all clear the
8-character threshold.

Latent collision worth one line: the staged package at `shokuknow/merge/kotoba/` (read-only;
outside every validated registry — confirmed at `/home/vgpnk/Projects/shokuknow/merge/kotoba`)
already names rows S232, S236, S237 in its `SOURCES.append.md`. No census impact this round
(E03 is per-registry-file); but if that staged file is ever adopted after r80 claims S232,
E03 fires on adoption. Future-round hygiene, recorded here so it is never a surprise.

## 4. The two gates left to the L1 — is there a fallback?

**No. The plan prescribes neither a fallback nor an owner for `check_report_pointers.py` or
`check_sibling_census.py`; line 59 of `plans/round-80.md` is the plan's only mention of
either (grep, single hit). If either reds at the final tip, the round machinery has no named
recovery path.**

What can be derived (not prescribed):

- **`check_report_pointers.py --report .ufo/reports/round-80/kotoba.md` (Q68, run at the
  report commit).** Exit 1 names each unresolved backticked pointer with its report line and
  the nearest existing name; exit 2 when the report holds no pointer or only directories.
  Because its subject is the report file itself, it cannot run earlier — the r79 battery
  runner already records this (`.ufo/waves/round-79/w1/Kb80E07BatteryRunner.md` F6: "cannot
  be revision-bound… why it is the runner's optional fourth argument"). The derived
  recovery: fix the report or the tree in a **follow-up commit** and re-run; the frozen C1/C2
  predicates are rev-parametric (`--rev <rev>`), so a moved tip is admissible **only if every
  after-value is re-measured at the landed tip** — the receipt set must be regenerated, not
  relabeled. The r80 report should also be written pointer-carefully: R3 skips command spans,
  R6 skips absolute paths and line locators, so the report's receipt citations must be
  repo-relative inline spans, not fenced or command-wrapped.
- **`check_sibling_census.py --skill SKILL.md`.** The no-harm invocation arms only `--skill`
  (no `--province`, no census positional): the gate reads the SKILL.md **frontmatter
  description only** and checks that every non-`none` sibling lane is named in it with an
  ownership/arbitration marker (G1). C2's conjunct (g) adds "one rule line naming ≥3
  surfaces" — if that line lands in the **body**, the gate cannot see it and cannot move; if
  it lands in the **description**, it can red the gate (names like claude/factory/spec without
  arbitration markers). The plan asserts "must not move the sibling guard" but names no
  remedy if it does. Derived recovery: move the rule line to the body, or give the
  description clause the G1 marker, then re-run. Environmental fragility the plan also does
  not name: the gate re-reads sibling repos live at their pinned commits
  (`git -C <fleet>/<lane>-shukunin show <pin>:<path>`) — a sibling GC or rewrite reds it
  through no fault of round 80.
- Neither gate is inside either frozen predicate, so a red there does not falsify C1 or C2 —
  but the no-harm battery is the round's own Q72 closure discipline, so a red blocks honest
  closure with no written fallback.

**Smallest safe correction:** one plan sentence per gate — (a) sibling census: the C2 rule
line lives in the SKILL.md body, not the frontmatter description; if it reds anyway, the L1
restores the G1 markers pre-report-commit; (b) report pointers: a red at the report commit
triggers a fix commit and full re-measurement of every cited after-value at the new tip
(receipts regenerated, never relabeled). These are plan-text additions only; no counter, gate
logic, or repair changes.

---

## Cross-cutting residuals (named for the L1, not assigned to any peer)

1. `freeze-shas.txt` is absent from `.ufo/waves/round-80/receipts/` at review time; the
   frozen predicate requires it record the E5-amended counter's sha "before any after-value
   is measured". Sequencing constraint, not a defect yet.
2. The abs-form base battery receipt (`tipbattery-base-abs.txt`, named by the plan) is also
   absent; only the dot form is present. Both forms are part of the frozen predicate.
3. Refresh `--note-key` / detached-head / `as_of` nits — see §2, smallest corrections given.

No control world was scored by this seat. Concrete counterexamples were found: the published
grammar candidate adds 171 lines against a 21-line remaining budget; the S230 source row
attributes a foreign commit to pi-mono; and the published C2 counter rejects the only valid
S229 quote under Q70. The entry's added hash citation was subsequently removed in current
build bytes. The S07 grammar world does clear the actual two `commit_unresolvable` tokens, but
fails the size guard; an unpinned helper is not a safe workaround under this counter.

VERDICT: C1 is not substantiated: S07 clears the real S230/S231 blockers (external=2, unresolvable=0) but its +171 grammar lines produce 210 total against cap 60; landing it triggers the declared honest-stop rule, and an unpinned helper bypass is unsafe. C2 is not substantiated: the current counter rejects S229's only valid quote under Q70. The entry's extra hash citation is fixed in current bytes; S230's source-row commit attribution still needs an append-only lesson erratum. The census after S232–S243 exits 0 with 7 new W04 warnings and no W02; baseline shared-universe/provenance risks and missing final-tip fallbacks remain.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80C03Residual.md
