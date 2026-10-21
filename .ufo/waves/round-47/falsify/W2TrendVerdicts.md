verdict: PARTIAL — round-47 learning-trend accounting at 7ad7fad: no trend verdict is on record anywhere in the landed tree, and the evidence gives expansion `unchanged`, quality `harmed` (one knowledge entry left carrying a falsified present-tense opencode claim while its sibling was marked), discernment `unchanged` (no non-author spot-check for round 47).

# W2TrendVerdicts — expansion / quality / discernment for round 47

Landed tree `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Canonical scratch clone `/fast/scratch/kotoba-r47/w2/W2TrendVerdicts/kotoba-shokunin` (clone + `checkout --detach` exit 0; `rev-parse HEAD` = `7ad7fad…`; `git status --porcelain | wc -l` = 0). All path:line cites are at `7ad7fad` unless marked BASE. Definitions: `/home/vgpnk/Projects/shokunin/LEARNING.md:29-38` (the three-trend table), `:42-48` (non-author gate / `unprovable-but-better`), `:77-78` (frontier→core recorded in LOG). Raw counts: `.ufo/waves/round-47/falsify/W2TrendVerdicts.anchors.json`.

## 0. The premise is itself a finding: the round recorded no trend verdicts

`grep -n -i "trend\|expansion\|discernment" LOG.md` → one hit, `LOG.md:1157` ("Expansion/quality/discernment **unchanged**"), inside an older round's verdict block; the round-47 entry `LOG.md:2317-2326` contains none of the three words. `grep -n -i "trend\|expansion\|discernment" SCORECARD.md` → one hit, `SCORECARD.md:211`, also an older (round-20) block. `corpus/lessons/round-47.md` has no trend section. The only trend text is a wave-1 prediction, `.ufo/waves/round-47/build/ConnLearningTrends.md` (not a corpus record, and it predicted `unchanged/unchanged/unchanged`).

LEARNING requires "one verdict each, every round" (`LEARNING.md:26`). Round 47 landed axes (`LOG.md:2317` heading: C1 freshness, C2 operability, C3 calibration) but no trend accounting. The verdicts below are therefore first proposals, not a re-score of an existing record.

## 1. Expansion — `unchanged`

**Evidence (strict `improved when` cell, `LEARNING.md:33`).** No `corpus/knowledge/` entry was admitted: 34 `.md` entries at BASE, 34 at HEAD (`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` → 34/34, exit 0), and the only knowledge diff is one modification:

```
git diff --name-status c61a973b..7ad7fad -- corpus/knowledge
M	corpus/knowledge/instruction-surface-census-round13.md        (exit 0)
git diff --numstat c61a973b..7ad7fad -- corpus/knowledge
88  5  corpus/knowledge/instruction-surface-census-round13.md
```

No capability row entered `SCORECARD.md`: `git diff c61a973b..7ad7fad -- SCORECARD.md` is 7 insertions / 3 deletions, all inside the three axis rows (`SCORECARD.md:31-33`), and `git diff c61a973b..7ad7fad -- SCORECARD.md | grep -c '^+.*Capability'` → 0.

**What the round did do on expansion-adjacent ground, and why it does not flip the cell.**

- `corpus/SOURCES.md` 11 → 15 rows (`S012` at `:25` `mined` kind `code`; `S013` `:26` and `S014` `:27` `queued` docs; `S015` `:28` `mined` own-work). `S012` is the registry's first `code`-kind row (`git show c61a973b:corpus/SOURCES.md | grep -c '| code |'` → 0; HEAD → 1). That is a genuinely new *kind* of source, but the improved cell is net-new admitted entries; `S012`'s `used-by` is `SKILL.md`, not a knowledge entry (`SOURCES.md:25`).
- The XML-token half of the Loader-rule freshness frontier moved to Core (`PROVINCE.md:15`), but that frontier row was already entered at round 46 — no new area was entered — and no entry was admitted on it.
- The two wave-1 candidate entries were drafted and not admitted: `.ufo/waves/round-47/build/KnowDescriptionRule.md` and `.ufo/waves/round-47/build/KnowSubstrateRecensus.md`; `.ufo/waves/round-47/build/CritExpansionClaim.md` §"Third re-check" says the description draft "meets all six … corrections **as a proposal**" and "Expansion becomes `improved` only when the L1 lands" the README row, the S row, the index re-record and the Gate. None of those landings happened for a knowledge entry; only the SOURCES rows landed.

**Counterexample against any `improved` reading.** If expansion were `improved`, the gate would need a new coverage-map knowledge row. `git diff c61a973b..7ad7fad -- corpus/README.md` shows exactly two index rows (`README.md:63` round-46 spot-check, `:64` round-47 lesson) and the frontier-row rewrite (`:76`); no `knowledge/` row. Repro is one command: `git diff c61a973b..7ad7fad -- corpus/README.md`.

`unprovable-but-better` is also unavailable: that status is admitted only through the non-author gate (`LEARNING.md:46-48`), and §3 shows that gate is absent for round 47. So `unchanged`, with the S012 `code` kind and the frontier→core half recorded as uncredited expansion-side work (the same way round 46's corpus conformance was "landed without credit", `corpus/lessons/round-46-verifier-spotcheck.md:17`).

## 2. Quality — `harmed`

The harm clause is literal: "an entry is found false or stale and left unmarked" (`LEARNING.md:34`). Round 47's own re-derivation found the v2.0.26 opencode model false and marked **one** of the two entries that assert it.

**The unmarked entry.** `corpus/knowledge/opencode-extraction-round14.md:8-11` says, in the present tense:

> "are preserved verbatim as the round's evidence. The current rule set — OC-1…OC-6 over `ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`, the API-managed instruction entries and an env-gate — is the round-18 re-derivation recorded in `instruction-surface-census-round13.md` § B (errata block) …"

At `7ad7fad` that is false for the pinned substrate, by the same occurrence-count method the round itself uses (`d.count(anchor)` over `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`):

```
ConfigInstructionPlugin 0   ReadTool.Plugin 0   SessionInstructions 0
InstructionDiscovery 0      session.instructions.entry.put 0
InstructionContext.observe 1   system-context-builtins 1   CONTEXT.md 1
disableClaudeCodePrompt 3   fn("Instruction.resolve") 1   Instructions from:  4
```

The census entry says exactly the opposite in its new § B′: "Every v2.0.26 anchor is absent from the 1.19.3 dump … and every round-14 anchor is present" (`instruction-surface-census-round13.md:221-224`), and its ledger marks the v1 ids `resurrected` (:315-321). The extraction entry carries no round-47 mark: `grep -c '1\.19\.3' corpus/knowledge/opencode-extraction-round14.md` → 0; `grep -c 'round 47\|round-47'` → 0. Its round-18 pointer ("recorded in … § B (errata block)") now lands on a section whose round-47 errata (`:164-167`) says § B is the v2.0.26 binary and "the live opencode classes are in § B′" — so the corpus as a whole is one hop from the correction, but the entry that owns the OC-1…OC-6 definitions remains a false present-tense statement about the current substrate.

**The positive half, which is real and should not be averaged away.**

- The census edit is an append-only re-verdict with exact bytes preserved: the five v2.0.26 rows deleted from § B/§ C are re-added byte-identically in `## Superseded class rows and the round-47 opencode ledger` (`:287-303`). I compared every occurrence: a Python exact-string check over the five ids returns `exact-any-match: True` for all five (repro in the JSON artifact). The census's "bytes unchanged" claim survives the attack.
- The new § B′ counts are sound: every ledger anchor count matches my independent `d.count()` run (table above), including the three that a line-oriented `grep -c` would report differently (`disableClaudeCodePrompt` 3 occurrences, not 2 lines).
- The re-verification is gate-live: `python3 -B verifiers/verify_surfaces.py --json` → exit 0, 7/7 PASS, `table_parity` 42 ids, `no_uncovered_class` 8/8, `opencode_extract` 9/9 ids from 7/7 rules; `check_substrate_pins.py` → exit 0, `OK 3/3 pins hold` at `fdbc8136…` / `179ca421…`. So the harm is a marking defect in the sibling entry, not a defect in the re-derivation.

**Stated counterargument (not smoothed).** A reviewer may read the extraction entry's round-18 block as a dated record ("2026-10-14 errata … dump `d9123b9b…`, opencode v2.0.26") and therefore as already scoped. That reading cannot rescue the literal sentence "The current rule set … is the round-18 re-derivation", which is present-tense and unnamed in time; the lane's own convention keeps dated records but corrects present-tense sites, and the round applied that convention to the census's identical statement and not to this one. If the reviewer accepts the dated-reading anyway, quality becomes `improved` on the census re-verification, not `harmed`. The strict clause decides the verdict above.

**Limit on the improved half.** The census entry still has no `source:` / `verified-at:` / `recheck:` head triple (`grep -n 'verified-at\|recheck\|source:'` on the entry → no output), so the re-verification is body-dated only. This is pre-existing Q12 debt (M16, `corpus/lessons/round-46.md:34` reports 32 of 34 entries lacking it), not a new admission failure; but it is why the improvement cannot be called machine-findable.

## 3. Discernment — `unchanged`

No non-author spot-check exists for round 47 at `7ad7fad`:

- `corpus/lessons/round-47.md` § Gate (`:27-58`) contains the four new source rows, the re-opened rows, one rejected candidate (`:52-54`, the 3-line `spec/agent-skills-spec.md` pointer), and the C1 ledger pointer. It contains **no** spot-check result. `grep -n 'Spot-check\|spot-check' corpus/lessons/round-47.md` → only `:7`, a reference to the round-46 file.
- The only spot-check in the corpus is round 46's, authored by the kaika integrator, not the lane: `corpus/lessons/round-46-verifier-spotcheck.md:1-13` (admit S003/S006 `agree`, reject S011 `agree`). Round 47 *indexed* it (`corpus/README.md:63`) but did not produce its own.
- The wave-2 falsify seats are `KotobaR47-2.*`, i.e. dispatched by the lane's L1 (`LEARNING.md:45-46`: "A subagent the lane dispatched is still the lane"). This report is lane-authored review by contract, not non-author closure, and it does not write SHONEN marks.
- `corpus/QUALITY.md:30` (Q19) is grounded — its `grounded in` cell names M20 (`corpus/lessons/round-47.md:19`), which carries command + output — but it came from an internal measurement mistake, not from a spot-check disagreement, so it does not hit the discernment `improved` cell (`LEARNING.md:35`). It also contradicts the QUALITY header at `:5`, which says `grounded in` names the class row "in `corpus/lessons/round-46.md` § Mistakes" — Q19 names a round-47 row. That is a stale sentence in the live document, fixable by generalizing it to "the round lesson's § Mistakes"; it does not invalidate Q19's grounding.

**Gate-completeness gap (same section, `LEARNING.md:69-70`).** The Gate must carry "candidates considered, admitted, rejected (with reasons), and the spot-check result". Round 47's Gate carries source rows and one source rejection, but not the disposition of the two knowledge-entry candidates (`build/KnowDescriptionRule.md`, `build/KnowSubstrateRecensus.md`) and not the spot-check result. `git diff c61a973b..7ad7fad -- corpus/lessons/round-47.md` is an add-only 58-line file; the omission is not an accident of diff truncation.

## 4. Supporting calibration findings (they inform, but do not replace, the three verdicts)

1. **Frontier→core move is not in LOG.** `PROVINCE.md:15` records "Frontmatter XML-tag rule (round 47, moved from Frontier)"; `git diff c61a973b..7ad7fad -- LOG.md | grep -c 'to Core\|moved from Frontier\|frontier.*core'` → 0. LEARNING says the move is "recorded in `LOG.md`" (`LEARNING.md:77-78`). The C2 bullet (`LOG.md:2322`) records the landing without the province move.
2. **S010's registry row is stale by its own recheck field.** `corpus/SOURCES.md:23` (`status queued`, `recheck on-commit`) ends "the frontmatter check is a lenient structural parse with **no XML-tag rule**". At `7ad7fad` the check exists: `trigger.no_xml_tag` at `verifiers/verify_skill_checklist.py:97,310,1294`. The lesson's Gate says "no existing row's `status`, `recheck` or `used-by` changed (old→new: none)" (`corpus/lessons/round-47.md:29-30`), which is true but does not disclose that the row's `teaches` claim was falsified by C2. Append-only contract means the fix is a superseding row or a Gate line, not an in-place edit; neither is present.
3. **The "floors exit=0" after-value is load-marginal.** `verifiers/check_assertion_floors.py:129` hard-codes `SELF_TEST_TIMEOUT_S = 120`. In my clone the guard exited **2** with `FAIL harness_independent self-test timed out after 120s (hung?)`; a solo re-run of `verify_harness_independent.py --self-test` exited 0 in **1m51.096s** (`0 failure(s) over 104 assertions`) — an 8.9 s margin. The after battery (`.ufo/waves/round-47/after/SUMMARY.md` `floors exit=0`) reproduces only on an idle host; the gate is not deterministic under load.
4. **Count reconciliation for the record claims.** `corpus-baseline.json` `tracked_files` 58→60 is correct at the file level: `git ls-tree -r --name-only 7ad7fad corpus | wc -l` = 60 (59 `.md` + 1 `.json`, `corpus/knowledge/sibling-citation-routing-round16.json`); BASE actual = 59. `verify_corpus_integrity.py --json` exits 0 with `tracked_files: 60`, and `verify_corpus_independent.py --json` exits 0. The "60" is not a fabricated denominator.

## 5. Proposed move (one, bounded)

**Append a round-47 errata block to `corpus/knowledge/opencode-extraction-round14.md`**, immediately after the round-18 block (after `:12`), stating in four lines: (a) the pinned substrate is now npm `opencode-ai` 1.19.3, sha256 `179ca421…`; (b) every v2.0.26 anchor the round-18 block called current is absent (`ConfigInstructionPlugin` 0, `ReadTool.Plugin` 0, `SessionInstructions` 0, `InstructionDiscovery` 0, `session.instructions.entry.put` 0); (c) the round-14 v1 shapes are live again and the current rule set is recorded in `instruction-surface-census-round13.md` § B′ (`:212`) and its ledger (`:287`); (d) the round-18 statement remains as the dated record it is, superseded for the current substrate.

Why this is the non-obvious move: the round already paid for the re-derivation and marked the census entry; the extraction entry is the *second live authority* over the same OC-1…OC-6 ids, and it is the one whose header a reader hits when following the rule definitions. One append converts the `harmed` clause into `improved` (a stale entry re-verified with an append-only mark, `LEARNING.md:34`) without admitting a new entry, moving a row, or touching a baseline. It is a knowledge-entry edit only, so it cannot change `tracked_files` (60 stays 60) and cannot disturb `table_parity`.

Risks: keep the round-18 block bytes untouched (append-only; the census's own move-preserves-bytes discipline is the precedent); do not make the `recheck` a path under `/fast/scratch/...` or the npx cache (ephemeral, Q04) — cite `python3 -B verifiers/verify_surfaces.py --json` plus the frozen-dump count command; do not restate § B′'s opencode class table in this entry (that would create a third authority). If the L1 wants the S010 supersession and the Gate spot-check line too, those are separate moves, not this one.

## 6. Verification of the proposal (what the L1 should run after appending)

- `grep -c '1\.19\.3' corpus/knowledge/opencode-extraction-round14.md` → 1 (today 0).
- `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 0, `tracked_files: 60` (no new file).
- `python3 -B verifiers/verify_surfaces.py --json` → exit 0, `surfaces.table_parity` PASS (the errata is outside `## Class inventory`).
- `git diff c61a973b..<new>` on the entry shows no deleted line inside the round-18 block.

## 7. Commands run (exit codes, key output)

All in `/fast/scratch/kotoba-r47/w2/W2TrendVerdicts/kotoba-shokunin` unless noted.

| command | exit | key output |
|---|---|---|
| clone + `git checkout --detach 7ad7fad…`; `git status --porcelain \| wc -l` | 0 | HEAD `7ad7fad…`; 0 dirty lines |
| `git diff --name-status c61a973b..7ad7fad -- corpus/knowledge` | 0 | `M …instruction-surface-census-round13.md` only |
| `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -c '\.md$'` | 0 | 34 at BASE / 34 at HEAD |
| `git ls-tree -r --name-only 7ad7fad corpus \| wc -l` | 0 | 60 (59 md + 1 json); BASE 59 |
| `python3 -B verifiers/verify_surfaces.py --json` | 0 | 7/7 PASS; `table_parity` 42 ids; `opencode_extract` 9/9 from 7/7 rules |
| `python3 -B verifiers/check_substrate_pins.py` | 0 | `OK 3/3 pins hold`; omp `delta 0 ns` |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | 0 | `tracked_files: 60` |
| `python3 -B verifiers/verify_corpus_independent.py --json` | 0 | no DRIFT |
| `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | 11/11 PASS |
| `python3 -B verifiers/check_assertion_floors.py` | 2 | `FAIL harness_independent self-test timed out after 120s (hung?)`; other 8 PASS at floor |
| `time timeout 300 python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 104 assertions`; 1m51.096s |
| Python `d.count(anchor)` over the 1.19.3 dump (20 anchors) | 0 | table in §2 and JSON artifact |
| Python exact-string probe of the 5 moved census rows | 0 | `exact-any-match: True` ×5 |
| `grep -n 'Spot-check\|spot-check' corpus/lessons/round-47.md` | 0 | `:7` only (round-46 file reference) |
| `grep -c '1\.19\.3' corpus/knowledge/opencode-extraction-round14.md` | 1 | 0 |
| `sha256sum …/opencode-ai/bin/opencode.exe` | 0 | `179ca421…` (= the cited pin) |
| `git diff c61a973b..7ad7fad -- LOG.md \| grep -c 'to Core\|moved from Frontier\|frontier.*core'` | 1 | 0 |

No tools were installed or updated.

## 8. What I did NOT check

- I did not re-derive C1's callee allowlist (`lq/Xl/Fo`), C2's XML-tag matcher logic, or C3's `GOVERNANCE_ERRATA` registry; those are other wave-2 seats' targets. I used the landed gate exits as evidence that the re-derivation is live, not as proof its internals are correct.
- I did not re-fetch S012/S013/S014 or re-verify their quotes/anchor line numbers; I treated the landed `corpus/SOURCES.md` rows and `## Gate` records as data. A wrong source quote would not change the trend verdicts (no entry cites S013/S014; S012's used-by is `SKILL.md`), but it would change the discernment sample.
- I did not run the fault harness, `verify_harness_claims.py` (known 21/28 red, carried), or the full after battery; I ran five gates plus floors.
- I did not classify whether the extraction entry should be treated as an exempt dated record; I state both readings and score the strict clause. I also did not audit the other round-18/round-27 opencode prose for v2-era present-tense claims beyond `grep -rn "v2\.0\.26" corpus/knowledge`, which returned only the extraction entry and the census's own marked history.
- I did not inspect the 72 wave-1 reports beyond `ConnLearningTrends.md`, `CritExpansionClaim.md`, and the records they cite; I did not read the fleet `.ufo/reports/round-47/` kotodama report, which is another lane's.
- I did not check SHONEN marks, fleet-root LOG/SCORECARD, or jj state. I did not run any non-author adjudication; per contract this report cannot supply one.
