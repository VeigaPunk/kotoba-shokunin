# Round 85 — kotoba (attempt 1, Linux host)

Base for this attempt: `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b` (master; the
round-84 non-author spot-check landing). Freeze: `f822dd113fe9f58661dd642dc207669581a4ab57`
(the plan, the claims and the base receipts, committed before any after-value
existed). Two claims on distinct axes: **C1 depth** (owned lowest axis, 9) — the
lane's own `SKILL.md` description obeys the render rule the lane documents, with
a committed trigger eval set (sourced to S213); **C2 freshness** (advisory
tied-lowest axis, 8.0) — the substrate pin names this host's `omp` and the
loader census re-derives across the 18.12.6 → 18.15.0 drift.

**C1 was killed before any production after-value was scored.** R6's gameable
wording was implemented faithfully, but the counter also deviated from the
frozen R8 quote-location requirement. R6 counts rows rather than distinct queries:
nine identical positives or nine irrelevant negatives with one generic shared
token satisfy every rule and read 8 of 8. No production description
change is claimed and none was made: the parsed description is unchanged at
1 021 characters with a 151-character first sentence (150 excluding the
terminating period), and the counter is quarantined as historical bytes, not an
active gate. **C2 was measured**: the two-command predicate holds at the
integration commit, after three negative controls were landed first.

## Gate

- **S213 — the one source this round opened live (tier A, mined).**
  `https://agentskills.io/skill-creation/optimizing-descriptions.md`, access
  date 2026-11-04, HTTP **200**, **13 403 B**, sha256
  `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` —
  byte-identical to the lane's committed snapshot
  `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (`cmp` exit 0), so
  the page has not moved since round 76. Fetch record
  `.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`; located quotes
  `.ufo/waves/round-85/w1/ScoutSource/source-packet.md`. Five quotes, each
  verbatim at the stated page line of the live bytes, each ≤ 25 words, each
  re-counted here with the same command the packet used (the page bytes are
  read from the committed snapshot, which `cmp` shows identical to the live
  fetch):

  - **(a) page line 17** — `This means the description carries the entire burden of triggering.` — 10 words.
    `grep -o 'This means the description carries the entire burden of triggering\.' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 10
  - **(b) page line 25** — `**Use imperative phrasing.** Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."` — 21 words.
    `grep -o '\*\*Use imperative phrasing\.\*\* Frame the description as an instruction to the agent: "Use this skill when\.\.\." rather than "This skill does\.\.\."' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 21
  - **(c) page line 41** — `Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't.` — 13 words.
    `grep -o "Aim for about 20 queries: 8-10 that should trigger and 8-10 that shouldn't\." .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 13
  - **(c2) page line 56** — `The most valuable negative test cases are **near-misses** — queries that share keywords or concepts with your skill but actually need something different.` — 23 words.
    `grep -o 'The most valuable negative test cases are \*\*near-misses\*\* — queries that share keywords or concepts with your skill but actually need something different\.' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 23
  - **(d) page line 28** — `The [specification](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters.` — 9 words.
    `grep -o 'The \[specification\](https://agentskills.io/specification.md#description-field) enforces a hard limit of 1024 characters\.' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 9
  - **(e) page line 19** — `One important nuance: agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone.` — 21 words.
    `grep -o 'One important nuance: agents typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone\.' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 21

  The page's own pass criterion for a negative row, at page line 92, is
  `A should-not-trigger query passes if its trigger rate is below that threshold.`
  — 12 words, the sentence that complements the S213 registry row's own quoted
  sentence (`A should-trigger query passes if its trigger rate is above a
  threshold (0.5 is a reasonable default).`, the first half of the same page
  line).
  `grep -o 'A should-not-trigger query passes if its trigger rate is below that threshold\.' .ufo/waves/round-76/snapshots/optimizing-descriptions.md | wc -w` → 12
  That is why a row count (R6) is a shape condition and not a
  trigger-behaviour measurement.

- **Round-start census** `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
  validate --root /home/vgpnk/Projects/shokunin kotoba` → exit **1**, 180 E12
  rows (`S001`…`S254` "row outside Registry section"), receipt
  `.ufo/waves/round-85/receipts/census-round-start.txt` (run before any lane
  change, at the freeze). **Round-end census** the same command → exit **0**,
  33 W04 duplicate-URL warnings and **0 E rows**, last line `kotoba ok
  /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`; the
  lane-file form `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
  validate --file corpus/SOURCES.md` → exit **0**, 33 W04 rows, last line `file
  ok` (receipts `.ufo/waves/round-85/w1/ScribeSources/census-fleet-root.txt`
  and `census-lane-file.txt`). The fleet-root form and the `--file` form read
  the same file — the lane is the only kotoba lane in the fleet conf — so the
  two readings are one measurement, not two. Row-count command
  `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → **180 before, 180
  after**. **Rows added: 0** — S213 already holds this URL, so a new row would
  be a W04 duplicate, the round-74 rejection reason. **Rows touched: S213**,
  `used-by` old → new:
  ` corpus/knowledge/skill-eval-artefacts-round70.md ` →
  ` corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-trigger-discipline-round85.md `
  (row kept at 13 pipe-separated fields, no literal `|` inside a cell; both
  paths exist on disk; receipt `.ufo/waves/round-85/w1/ScribeSources/s213-usedby.txt`).
  **Frontier rows advanced: 0** — S213's status was already `mined` (opened
  2026-10-25, recheck 90d) and this round re-opened the same row without
  changing its status. The corpus/README.md § Frontier *Loader-rule freshness*
  row still reads round 51's omp 18.12.6 re-pin; the round-85 substrate
  re-pin is recorded in `verifiers/baseline.json` (`omp_round85_note`) and in
  the C2 landing commit, and advancing that frontier row is not this round's
  claim.

- **C1 depth — killed before data (owned lowest axis, 9).** Frozen predicate,
  verbatim from the plan (§ C1): "`python3 -B verifiers/check_description_render.py
  --rev <rev>` (NEW counter, round-85 bytes; frozen by this plan's commit before
  any after-value exists) prints `description render rules met N of 8` and exits
  0 iff N == 8." **Base reading**, measured at the base rev with the frozen
  instrument: `description render rules met 4 of 8`, exit 1 — R1 first sentence
  151 chars (cap 99), R4 no `use this skill when`, R6 eval set absent, R8
  sourced entry absent; R2, R3, R5, R7 green (receipt
  `.ufo/waves/round-85/w1/ExecC1Counter/base-receipt.txt`; instrument sha256
  `79b8273c5a952a865e5182c4d348f594f6b4881c2221121c8b89eeb47b69957a`).
  **After-value: none.** The frozen controls W0 (base bytes), W1 (naive 99-char
  cut) and W2 (token dump) all stay below 8 of 8, but the attack seat's
  independent oracle found three worlds that reach 8 of 8 under the *literal*
  frozen rules: nine identical should-trigger rows (W5), nine irrelevant
  negatives that keep one generic token (W6), and a description whose first
  terminator is an abbreviation dot (W7) — receipt
  `.ufo/waves/round-85/w1/ReviewerC1/oracle-receipt.txt`, Table B, and the
  function-level counter/oracle comparison
  `.ufo/waves/round-85/w1/ReviewerC1/counter-comparison.txt` (counter and
  oracle agree on all seven saved worlds, so this is a property of the frozen
  rule sentences, not a counter defect). Two further identity findings against
  the frozen text: R8 accepts any double-quoted 3–25-word span with no located
  quote, and adds a three-word minimum the plan does not state (both recorded
  in `.ufo/waves/round-85/w1/ReviewerC1/review.md`). The security seat added
  two findings on the same instrument: R5 executes the target revision's census
  Python with inherited environment and permissions, so an untrusted revision
  could forge an R5 pass (S85-08), and R8 accepts an invented short quotation
  (S85-09) — `.ufo/waves/round-85/w1/Sentinel/audit.md`. **Disposition:** the
  claim stops before data. The instrument was committed at
  `759cf35457c92c110f61e82630ccee00a598215f` and then quarantined unchanged at
  `47085c8c528245e88197d716b48a8325a97414f7` — the bytes and their fixtures
  now live under `.ufo/waves/round-85/frozen/`, the active
  `verifiers/check_description_render.py` and its `SKILL.md` § Gate registry
  row were removed, and the quarantine note
  `.ufo/waves/round-85/frozen/QUARANTINE.txt` states that the relocated copy
  must not be run. **The frozen rule sentences were not changed and the R6
  wording was not strengthened**; no post-scoring predicate repair is claimed,
  and no expansion or no-harm is claimed from this claim. The documentary half
  landed instead: `corpus/knowledge/description-trigger-discipline-round85.md`
  (8 682 B, sha256
  `48c8869698a85988a420234f01c68b799f545fed9a3388f4dd66fb99a27f4ad8`) cites
  S213, carries `verified-at: 2026-11-04`, a `recheck:` command, and located
  quotes — and states plainly that the production description is unchanged and
  that the candidate description and eval set are wave artefacts only.

- **C2 freshness — measured (advisory tied-lowest axis, 8.0).** Frozen
  predicate, verbatim from the plan (§ C2): "`python3 -B
  verifiers/check_substrate_pins.py` exits 0 printing `OK 3/3 pins hold`, AND
  `python3 -B verifiers/verify_surfaces.py --json` exits 0 with `"pass": 7` and
  `"fail": 0`." **Base readings**, measured at the same base: the pins exit
  **2** with `UNREADABLE 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`
  (the pinned path `/home/vgpnk/.local/bin/omp.real` does not exist on this
  host) and the surfaces exit **2** with `"error": "omp binary not found:
  /home/vgpnk/.local/bin/omp.real"` (receipt
  `.ufo/waves/round-85/receipts/before-gates.txt`). **After-value**, measured at
  the integration commit `bf9ab28e011e4243356078951e33d919ad63a0c5`: the pins
  exit **0** with `OK 3/3 pins hold` (omp sha256
  `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`, mtime
  delta 0 ns at tolerance 0 ns, opencode sha256 unchanged) and the surfaces
  exit **0** with `"pass": 7`, `"fail": 0` — receipt
  `.ufo/waves/round-85/receipts/c2-after.json`; re-measured at the tip by this
  seat with the same two commands, same readings. The four host defaults were
  migrated to the ELF this host actually runs (`/home/vgpnk/.local/bin/omp`,
  `omp/18.15.0`, 276 785 328 B; the round-72 "omp is a crash-restart wrapper
  whose ELF is `omp.real`" premise is false here — `omp.real` exists nowhere on
  this host). **Negative controls landed first**, at
  `51fffd1933f0a44bfeb9434688b4f850ff21aec6`: the opencode sha256 written under
  the omp pin exits 1 (`DRIFT 1/3 pins failed`), a deleted omp pin exits 1
  (`PIN_ABSENT 2/3 pins failed`), and the same candidate scored against a
  different ELF exits 1 (`DRIFT 2/3 pins failed`) — the guard is not vacuous.
  One bound is named rather than hidden: a *coarse* mtime pin (second or
  millisecond precision) still exits 0, because the checker derives its
  tolerance from the precision the pin states; the landed pin carries nine
  fractional digits and a 0 ns delta, and a 1 ns error exits 1
  (`.ufo/waves/round-85/w1/ReviewerC2/review.md`, W9–W13). No layer of this
  claim is a no-harm claim: the substrate evidence is the measurement.

- **Records this round touched.** (1) **S213** — re-opened live (above) and its
  `used-by` cell extended with the round-85 documentary entry; no row added, no
  status change, no other cell changed (the anchor cell's protected text is
  unchanged — the only cell that differs from the base is `used-by`). (2) **The
  CRLF normalization of `corpus/SOURCES.md`** — removing 436 CRLF pairs
  reduced the normalization-only bytes from 203 260 to 202 824 without changing
  cells (`.ufo/waves/round-85/w1/ScribeSources/crlf-proof.txt`). The final file
  then adds S213's permitted `used-by` text. The normalization-only empty diff
  is historical evidence, not a claim that the final file equals the base modulo
  CR. Protected-cell comparison at final integration shows only `used-by` differs.
  These source edits landed at `6a520b6a916028cf8ea069cf7d7d5660f5b54e0c`.
  (3) **The seven index rows** for `lessons/round-81-verifier-spotcheck.md`,
  `lessons/round-82.md`, `lessons/round-82-verifier-spotcheck.md`,
  `lessons/round-83.md`, `lessons/round-83-verifier-spotcheck.md`,
  `lessons/round-84.md`, `lessons/round-84-verifier-spotcheck.md` (the list the
  base gate printed, `.ufo/waves/round-85/receipts/before-gates.txt`) — plus the
  eighth row for the round-85 entry itself, all added to `corpus/README.md` §
  Coverage map in the same commit; `corpus.index.unindexed` now reads 0
  (`.ufo/waves/round-85/w1/ScribeSources/corpus-integrity.txt`,
  `corpus-independent.txt`). **This lesson's own coverage-map row is the
  integrator's landing step, not a completed one:** `corpus/README.md` is
  ScribeSources' file and no row names `lessons/round-85.md` yet, so the row must
  land in the same commit as this file's bytes (a row before the bytes exist
  reads `corpus.index.missing_paths` = 1; no row at all reads
  `corpus.index.unindexed` = 1 — both measured by ScribeSources in
  `.ufo/waves/round-85/w1/ScribeSources/residual-index-ordering.txt`, which
  assigns the ordering to the integrator).

- **Assimilation.** The round-74-rejected staged entry
  (`spec-description-trigger-discipline.md`, refused because its source row
  S231 duplicates the URL the lane already holds as S213 and its best-practices
  half is already carried by the admitted S223 entry) is adopted **through this
  lane's own gate** as the round-85 entry, re-grounded on S213 and on the live
  bytes: 11 of 13 staged claims survive re-grounding, 2 are refused (the
  trigger-miss telemetry claim — the page carries no telemetry sentence, so it
  is the lane's inference and is labelled as one — and the three-way tension
  about negative conditions, whose cited page identities were not re-opened for
  this entry), and the best-practices half stays refused as located-and-already-
  carried material. The staged entry's own `source:` ids (S231/S232) are the
  package registry's, not this lane's: in this lane S231 is the Mistral Vibe
  README and S232 is OpenAI Codex Skills, so the round-85 entry names S213.
  **considerthese** proposal 3 (the description audit, raised four days
  running) is executed by C1 and killed there; proposals 1 and 2 are sized out
  below.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| **M85-1 (r84-D1) — a numeric wording claim carried without a counting command, so the reader cannot re-derive the number.** The round-84 lesson's and the round-84 report's ruled-out bullet reads "10 FAIL instruments at the r83 tip receipt `after-floors-gate-r83.txt`"; the cited receipt holds **11** `FAIL` rows, and 10 is the count only after excluding the gate's own guard row `floors_guard`, which the prose never says. The prose also carries no command at all, so neither 10 nor 11 could be re-derived. | `corpus/lessons/round-84-verifier-spotcheck.md` § defects (r84-D1); the receipt `.ufo/waves/round-83/receipts/after-floors-gate-r83.txt`; the r84 prose at `corpus/lessons/round-84.md` § Ruled out | the lane's counting-command rule (Q13 requires a count to carry its command as `<number> — <command> <date>`) had no criterion for a count quoted from **another artifact's rows**, where the row-selection rule is part of the claim; the closure judge named the defect, this round's correction names the count | a new criterion row **Q76** appended to `corpus/QUALITY.md` (appended, never renumbered): a count quoted from another artifact's rows names that artifact and the row-selection rule, not only the number; and an append-only correction block appended to `corpus/lessons/round-84.md` (§ Correction, round 85) naming the measured count and its counting command. |
| **M85-2 — a committed registry that parsed on the authoring host and read as 180 E12 rows on the reading host: a byte-level defect with no content change.** The census's `## Registry` heading test compares a `\r`-suffixed heading against `Registry`, so the section is never entered and every row in the file is reported "outside Registry section". The registry's cells were always correct; only the line endings were host-dependent. | `.ufo/waves/round-85/receipts/census-round-start.txt` (exit 1, 180 E12 rows at the freeze); the CRLF proof in `.ufo/waves/round-85/w1/ScribeSources/crlf-proof.txt` (436 CRLF pairs removed, 203 260 → 202 824 B, cell-identical modulo CR) | the census E12 class, which caught it as soon as the census was run on this host — the class is the capture, and it fired before the registry was touched | LF normalization of `corpus/SOURCES.md` (no cell changed), plus the lesson rule: **a registry change is validated with the census on the host that will read it, and the census is run before the report**, not only on the host that wrote it. |
| **M85-3 — the frozen C1 predicate measured form, not the claimed content: literal R6 counts rows rather than distinct queries, so a vacuous eval set passes every rule.** Nine identical should-trigger rows satisfy both the 8–10 band and the "≥ 5 indirect positives" floor; nine irrelevant negatives that each keep one generic token satisfy the "shares a ≥ 4-character word" near-miss clause; a description whose first terminator is an abbreviation dot satisfies R1's literal period rule while its real opening sentence runs past the 99-character listing cut. Under the frozen rules each of those worlds reads 8 of 8, so the counter's exit code cannot separate a real eval set from a vacuous one. R8 additionally accepted an unlocated quotation, and R5 executed the target revision's census Python with inherited privileges. | `.ufo/waves/round-85/w1/ReviewerC1/oracle-receipt.txt` (Table B: W5 8/8, W6 8/8, W7 8/8) and `counter-comparison.txt` (counter and oracle agree on all seven saved worlds — the defect is in the frozen rule sentences, not in the counter); `.ufo/waves/round-85/w1/ReviewerC1/review.md` (High and Medium findings, plus the two R8 identity disagreements); `.ufo/waves/round-85/w1/Sentinel/audit.md` (S85-08, S85-09) | the wave-1 attack seats (the independent oracle, the counter/oracle differential and the security audit), i.e. the falsify wave itself, not a later reviewer | the claim stops before data and the instrument is quarantined unchanged as historical bytes (preserved at `759cf35457c92c110f61e82630ccee00a598215f`, quarantined at `47085c8c528245e88197d716b48a8325a97414f7` under `.ufo/waves/round-85/frozen/`, active gate and registry row removed); the R6 wording is **not** strengthened and no after-value is claimed. The frozen rules, their labels and their wording are unchanged; a future round that wants a trigger-behaviour claim needs a different predicate, not a patched one. |
| **M85-4 — a documentary entry asserted positions its cited page does not carry.** The drafted round-85 entry's § 4 read S213 as putting negative conditions only in the eval set — a positive-only rule the page contradicts at line 156 ("Add specificity about what the skill does *not* do") — and carried the staged package's TRAE and Chiba positions inside an S213-sourced entry although neither page was re-opened for it. It also carried the package registry's `source:` ids (S231/S232), which in this lane name unrelated rows. | `.ufo/waves/round-85/w1/ScribeC1Entry.md` § 7 (what the L1 changed in the entry and why it was right); the staged-claim verdict table and the registry-id mapping in `.ufo/waves/round-85/w1/ScoutSource/source-packet.md` (claims 11–13 refused; S231/S232 mapped to S213/S223) | the scout's staged-claim verdict table and the L1's review of the entry before it landed (a source-overreach caught in-round, pre-land) | the landed entry's final bytes (8 682 B, sha256 `48c8869698a85988a420234f01c68b799f545fed9a3388f4dd66fb99a27f4ad8`) cite S213 only, refuse the TRAE/Chiba comparison with an explicit flip (open the original sources in a later round, locate the text, evaluate each claim separately), and label the trigger-miss point as the lane's inference; the page's line 156 is the counter-example that keeps the lane's `Anti-triggers:` scope clause from being read as a rule S213 forbids. |

## Ruled out

- **The byte ceiling and the Gate-registry move (considerthese proposals 1 and
  2) are sized out, not decided.** Both are separate rounds' work and neither
  is this round's axis: the byte/line-length ceiling belongs to the floors
  guard, whose measured subject this round did not touch, and moving `## Gate
  registry` out of `SKILL.md` is a relocation of a protocol-named home — an L0
  question, not a lane claim (Q67). Round 85's own landing touches neither:
  the registry move would have collided with the round-85 registry work
  (the CRLF repair and the S213 `used-by` cell), so running both at once would
  have put two writers on `corpus/README.md` and `corpus/SOURCES.md` in one
  round.
- **No new S-row for the description page.** S213 already holds
  `https://agentskills.io/skill-creation/optimizing-descriptions.md` (and
  S210 holds the same URL), so a row minted this round would be a W04
  duplicate — the round-74 rejection reason — and the census already reports
  S213 among the known duplicate-URL warnings. The page was re-opened instead:
  rows added 0, S213's `used-by` extended.
- **The round-49 sibling census is not the guard's base.** It is stale: read
  now, `python3 -B verifiers/check_sibling_census.py
  corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
  --skill SKILL.md` reads `province rows 20 matched 4` and exits 1 (15 FAIL
  rows on the lane pins). The current base is the round-74 census,
  `corpus/knowledge/sibling-overlap-census-round74.md`, which reads `province
  rows 20 matched 20` and `skill description names 10 of 10 non-none lanes`,
  exit 0 — the census PROVINCE was re-pinned at round 74.

## Correction (round 85, append-only; the round-84 r84-D1 numeric wording)

The lesson's and the report's ruled-out bullet above read "10 FAIL instruments at
the r83 tip receipt `after-floors-gate-r83.txt`". **Measured count: 11 `FAIL`
rows** in that receipt, of which 10 remain after the gate's own guard row
`floors_guard` is excluded — an exclusion the prose never stated, and the
prose carried no counting command at all, so neither number was re-derivable
from the record. The counting commands, run 2026-11-04:

- `grep -c '^FAIL' .ufo/waves/round-83/receipts/after-floors-gate-r83.txt` → **11**
- `grep '^FAIL' .ufo/waves/round-83/receipts/after-floors-gate-r83.txt | grep -vc 'floors_guard'` → **10**

The ruled-out decision itself is unaffected: the set of degraded instruments is
real and stays named debt; only the number's wording was wrong. The lesson's
text above is not rewritten.

## Correction (round 85, append-only; the wave's attack-role accounting)

The frozen plan and claims state an attack share of 6 of 16 seats = 37.5 %.
Counted against the strict addendum attack-role set
(reviewer / critic / mutation-tester / labrat), the wave's dispatched seats give
**4 of 16 = 25 %** (two reviewers, one critic, one mutation-tester): the
sentinel and revenger seats are supplementary adversarial seats and are not
members of that set, and no labrat seat exists in the dispatched wave — the
validator's role taxonomy has no such role. The plan's own "6 attack seats"
figure counted the two supplementary seats as attack seats. The frozen plan
(`plans/round-85.md`) and the frozen claims
(`.ufo/waves/round-85/claims.json`) are **not rewritten**; this correction is
appended here and in `LOG.md`. The wave still meets the 25 % floor, and the
seat accounting is unchanged.

## Correction (round 85, append-only; the C1 claim's disposition)

C1 is recorded as **killed before data**, not as a measured improvement and not
as a narrowing: the frozen counter read 4 of 8 at the base, the frozen W0/W1/W2
controls stayed below 8 of 8, three worlds outside that control set reached
8 of 8 under the literal frozen rules, and the instrument was therefore
quarantined unchanged instead of being scored against production. No
production description change landed, no eval set landed in production, and no
trigger capability is claimed. The documentary half of the round landed
separately and is labelled as documentary.

## L1 final integration notes

- The artifact-level plan froze at `f822dd113fe9f58661dd642dc207669581a4ab57`;
  executable counter bytes landed later at `759cf35457c92c110f61e82630ccee00a598215f`.
  The plan's wording must not be read as proof of a pre-existing executable freeze.
- The draft entry always cited lane S213; staged S231/S232 were a **mapping risk**,
  not an observed wrong-id edit to the final entry. The M85-4 sentence claiming
  the draft itself carried those ids is withdrawn by this clarification.
- Connector's original report overstates the round-74 flip. The old lesson requires
  a specification page stating a trigger rule S213 does not; this round reopens
  S213 itself and does not satisfy that original condition. The historical
  refusal remains. The new, separately grounded documentary note adopts only
  verified S213 guidance, not the original package entry wholesale.
- Corpus baseline refresh must retain the deliberate dead-clone citation at
  `corpus/lessons/round-81.md:8` as an unresolved finding; no fabricated external
  provenance or nonzero zero-mode expectation is authorized.
- Final wave settlement arrived from Main: all 16 seats settled. The results
  envelope records an orchestrator-kernel restart and missing original final
  payloads; all 16 seat reports remain on disk. Original provider/death-status
  telemetry cannot be reconstructed from that envelope.
