# ScribeEntry — round 86 w1 report

## Behavior
Wrote `corpus/knowledge/omp-catalogue-model-round86.md`, the C1 knowledge entry: header (`source: S255`, verified against `corpus/SOURCES.md:196`), `verified-at: 2026-11-04`, `recheck: on-release`, `ground:`; §1 render rule with 11 located source lines plus offsets; §2 roots, priority and precedence (from `w1/ScoutRootsSource/source-packet.md` plus the final `verifiers/omp-skill-roots.tsv`, 12 rows); §3 errata table (28 quoted rows plus 2 code-literal rows, file:line, verdict, evidence); §4 before→after: 83 of 215 (K0-a1) → 215 of 215 (ExecModel score.txt).

## Gates (exercised)
- Quote re-location: `.ufo/waves/round-86/w1/ScribeEntry/quote-locate.txt`. Result: `ELF quotes at offset: 33/33; ledger quotes located: 12/12; errata quotes at file:line: 28/28; bad=0`. Every quote is 25 words or fewer.
- Fixture counts quoted in the entry were recomputed from `catalogue.json`: `215 151 228 186` (entries, renders ending in `…`, cache rows, `key:model` rows).
- CANDIDATE_READY appeared on the 10th 120 s check (2026-11-04 19:33). The counter was not re-run: the score is copied from `w1/ExecModel/score.txt`.

## Touched surfaces
- corpus/knowledge/omp-catalogue-model-round86.md (new)
- .ufo/waves/round-86/w1/ScribeEntry/quote-locate.txt, .ufo/waves/round-86/w1/ScribeEntry.md

## Findings
1. **Word-cut floor.** omp 18.15.0 `dnt` cuts at the last space only when that space is at index ≥ 40 (`const c = o >= E ? r.slice(0, o).trimEnd() : r;` @178770368). The H7s code in `harness-verifier-round10.md:48` has no floor. The other lane spec lines listed in the §3 table leave the floor out.
2. **Model-keyed preview rows.** When the compressor's output is unusable, the preview is stored under `key:modelKey` (`e.put(u, dnt(r.description));` @178775605). These rows never serve a render. In the fixture they are 186 of the 228 rows (42 bare-key).
3. **Cache key input.** `A` hashes `e.description` as loaded, with no whitespace collapse in the key function. `render-mechanism-round7.md:26-27` says "ws-normalised"; the table marks it changed.
4. **Cache path.** The store is `agentSubdir(…, "data")`, so it resolves to `$XDG_DATA_HOME/omp` when that dir exists (offset 166896000). `~/.local/share/omp` is absent on this host, so `~/.omp/agent/skill-descriptions.db` holds here but not in general.
5. **Cached-line count conflict.** `plans/round-86.md:110` says "15 of 215 lines are cached". A render-text match against the 42 bare-key fixture rows gives 35. That is text equality, not key equality, and short descriptions render the same either way. I did not reconcile the two; the entry cites the plan's 15 as the plan's.
6. **Counter changed after the freeze.** The counter sha256 differs between freeze `ecfad51` (`2390eec2…`) and addendum-1 `b9ee548` (`39a014f2…`). The candidate was scored on the addendum counter. `plans/round-86.md:86-87` (kill rule) reads "the counter, its fixture or its pins changed after this freeze". `plans/round-86-addendum-1.md` says it was committed before any candidate data. Reported verbatim for the judge; no verdict here.
7. **Ledger plugin quote.** The row `~/.omp/plugins/node_modules/*/skills` cites `var Gh = ".omp";`, a config-dir constant, not the scan line `dir: Zo.join(R.path, "skills"),` (@173914936). It is located, but weak on meaning. This is a review item under `plans/round-86.md:80-82`.
8. **Precedence simplified.** The candidate model keeps first-root-wins. omp instead namespaces a differing same-name copy as `<ns>/<name>` (@177497593). The two are equal on this host (no overlapping names per ScoutRootsSource).

## Out of scope
SKILL.md and the corpus files in §3 were not edited (the L1 adds errata). No counter, fixture or ledger edits. No tool installs.

## Risks
The SKILL.md line pointers are working-tree lines; lines ≥ 522 sit one below base `e5d966b`, because an uncommitted row was added at line 522. The §4 landing number is the L1's to record at the landing commit.
