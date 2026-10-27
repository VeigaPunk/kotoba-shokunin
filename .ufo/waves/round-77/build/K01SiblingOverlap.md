# K01SiblingOverlap — round 77 w1 sibling-overlap scan (adjacency)

Seat: K01SiblingOverlap (leaf, read-only on siblings). Lane: kotoba-shokunin, HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`git -C … rev-parse HEAD`; `status` shows only untracked round-77 wave files). Scope: the 20 sibling lanes under `/home/vgpnk/Projects/shokunin/*-shokunin/` (kotoba skipped). No sibling file was written, no git write was run, no check was edited.

## 0. Method and bounds

- Searched lane trees with the grep and find tools, excluding `.git`, `node_modules`, `.ufo/`, `reports/`, `waves/`, `evidence/`, `live/`, and json/jsonl/txt/log/wav artefacts. Those excluded trees are other rounds' artefacts or raw captures, not rules a sibling states; a hit there is noted only where it matters.
- Positive control: the same `agentskills.io` search over kotoba's `corpus/knowledge` returned hits (`sibling-overlap-census-round74.md:1`, `skill-eval-artefacts-round70.md:1-2`, `frontmatter-rule-authorities-round48.md:1`), so the scan is not vacuous.
- Read-only verifier run: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` (exit 0; `rows 20 verified 20`, `province rows 20 matched 20`), and the same for the round-49 file (exit 1; `province rows 20 matched 4`). Raw outputs: `.ufo/waves/round-77/build/K01SiblingOverlap.census-r74-at-head.txt`, `…census-r49-at-head.txt`.
- Read-only import of `check_sibling_census.description_of` and `split_clauses` to measure kotoba's own frontmatter (no file written).
- Tooling: none installed. Stdlib python3 only. Scratch `/fast/scratch/hyaku/kotoba-r77/K01SiblingOverlap/` (removed before yield).

## 1. STRICT hits (same URL or same rule text)

| id | surface | where | owner | verdict |
|---|---|---|---|---|
| S-a | S213 URL `agentskills.io/skill-creation/optimizing-descriptions.md` | none in any sibling lane's corpus, SKILL.md, PROVINCE.md, tools or verifiers (scoped scan of kagi, kumitate, kengaku, tsukuroi, tameshi corpora; broad scan of all 20 with the exclusions above) | kotoba (`corpus/knowledge/sibling-overlap-census-round74.md:1-6`, `corpus/knowledge/skill-eval-artefacts-round70.md:1-6`) | no strict URL overlap |
| S-b | rule text "Use imperative phrasing" / "Err on the side of being pushy" (S213 snapshot `.ufo/waves/round-76/snapshots/optimizing-descriptions.md:25,27`) | no sibling hit (`pushy`, `imperative phrasing`, `description craft` swept; only fleet-root LOG/MANIFEST/.scratch rows matched, which are not lanes) | kotoba (`corpus/lessons/round-75.md:5`) | no strict rule-text overlap |
| S-c | description length 1–1024 (S018 `description` field) | kotoba's own census gate: `verifiers/check_sibling_census.py:89, 417-418, 521` | kotoba (round-49/74 census) | same constant, same source row, kotoba-owned; not a sibling |
| S-d | routed-repair counter family `check_*routed_repairs*.py` / `check_rNN_routed_repairs*.py` | zero sibling files with that name (`find` over lanes for `*routed*`, `check_*repair*`); kotoba's own predecessors `verifiers/check_routed_repairs.py`, `check_routed_repairs_v2.py`, `check_r63…check_r75_routed_repairs.py` | kotoba | in-lane succession, not sibling overlap |

## 2. LOOSE hits (same concept or numeric convention, different text, different surface)

| id | sibling file:line | what overlaps | axis touched | owner / handling |
|---|---|---|---|---|
| L-1 | `kumitate-shokunin/scripts/routed-ledger.mjs:17, 32, 35` | "located quote (<= 25 words)" binding of ledger rows to routed items; closed rows bind answer by `path:line` plus a located quote on that line | C2 R1 (routed text arms), C1(b) quote bound | kumitate owns; report only |
| L-2 | `kengaku-shokunin/plans/routed_open.py:4-6, 26-29` | one row per routed finding, an id appears once ever, refusal is a decision, summary withheld on a broken row | C2 (routed item lifecycle) | kengaku owns |
| L-3 | `tameshi-shokunin/corpus/routed-defects.json:4` | "one row per item routed by the round-40..49 closure spot-checks" | C2 | tameshi owns |
| L-4 | `mori-shokunin/tools/mori-routed-check.py:1-3, 10-19` | R1..R4 round-23 routed items re-derived at a committed revision by git-object reads only, nothing written; the nearest structural analogue of `check_r75_routed_repairs.py` | C2 (shape) | mori owns; not the same repairs or text |
| L-5 | `chousa-shokunin/corpus/evidence/round40/routed-defect-dispositions.json` | per-routed-defect disposition record | C2 | chousa owns |
| L-6 | ~17 sibling lanes' `.md/.py/.mjs/.sh` files contain "25 words" (counts, unclassified: chousa 26, kagi 8, kaidoku 33, kake 28, kama 44, kasegi 42, kengaku 42, kotodama 26, kumitate 17, lore 1, mado 62, mori 37, revenger 19, souji 33, tabi 28, tameshi 31, tsukuroi 60) | same numeric bound, separately authored; no fleet-root CORPUS.md/PROTOCOL.md/MISSION.md rule (grep empty) | C1(b), C2 R1 | each lane; the number is a convention, not a shared rule; counts not classified beyond L-1 |
| L-7 | sibling SKILL.md frontmatter `description` (17 readable files; flattened length, my regex, approximate): kengaku ~884, game-dev-3d ~737, lore ~650, kotodama ~615, kaidoku ~604, mado 73, tabi 78, tsukuroi 79, others 73–375 | none begins with an imperative verb ("Domain specialist —" or "Triggers:" or a quoted noun phrase); all ≤1024 | C1 (imperative phrasing, length) | each lane; not absorbed. S213's imperative guidance is kotoba-only in the fleet |
| L-8 | sibling receipts with `exit=$?` idiom (per lane, not exhaustive: tabi 28, audio 11, kengaku 5, kumitate 4, chousa 4, others 0–2) | receipt hygiene, capture-own-exit | C2 R2, pipeline-exit defect of r76 | each lane; not audited exhaustively; sibling tool sweep for `\| tail/head` masking a gate verdict found only fleet hyaku/ufo scripts that pipe for display or parse |
| L-9 | kotoba's own `sibling-overlap-census-round49.md` recheck line (`:3`) | still says exit 0 / `rows 20 verified 20`, but at HEAD it is exit 1, `province rows 20 matched 4`, because round 74 re-pinned PROVINCE | adjacency freshness | kotoba owns; the round-74 census is green (exit 0, 20/20, 20/20). The round-49 file is superseded in practice but carries no superseded note |

## 3. Measured overlap with C1 inside kotoba (sibling-census gate vs the description rewrite)

- kotoba SKILL.md frontmatter `description`, measured by census `description_of` (whitespace-collapsed): **1021 characters; cap 1024; headroom 3** (read-only import; output recorded in §0). The C1 counter's own render (clip-preserving) is 1022 per the plan's addendum 1; the two conventions differ by one character on the same field.
- S213 advises an explicit "Err on the side of being pushy … list the contexts where the skill applies" (snapshot `optimizing-descriptions.md:27`). Any description rewrite that follows that advice adds characters. With 3 characters of headroom, a description edit must drop a named sibling or clause, and the census requires named neighbours (G1/G2). The r76 draft's body row (`.ufo/waves/round-76/build/skill-patch.md:17`) is a Body-craft row, not a description edit, so C1 (c) can be satisfied without touching the description. Any description edit must re-run `check_sibling_census.py --rev` at the candidate revision.
- Gap in the frozen no-harm battery: the plan's list (`plans/round-77.md:46-49`) does not include `verifiers/check_sibling_census.py` or `verifiers/check_sibling_reread.py`, both of which read the description or the sibling heads. Recommend adding them to the battery (plan change before data, not by this seat).
- Census word-match of kotoba's description: it names 10 of the 20 siblings by word match (chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi, tsukuroi); mori, souji, tabi, kaidoku, mado, revenger, lore, game-dev-3d were checked and not named (audio, game-dev-2d not checked). Consistent with the census's "9 adjacent" wording plus kotodama's NOT clause; not a discrepancy I can confirm.

## 4. Cross-claim pattern (C1 and C2): both pass on a presence proxy

- C1 (b) counts quotes that occur verbatim in the snapshot, page-unique and cited; (c) passes when a SKILL.md row holds two quote fragments from the page. A row that quotes S213 and inverts it passes (c). Substance is not checked.
- C2 R1's text arms, per the frozen counter's own trust-boundary note (`verifiers/check_r75_routed_repairs.py`, docstring "Trust boundary"), are "presence-and-quote floors … they count named strings, not substance." R2 and R3 are recomputed; R1's arms are not.
- Both carry a measurement convention that a proxy can drift on (C1 clip 1022 vs stripped 1021; C2 R2 normalised stdout).

Proposed single QUALITY criterion for w2 critics (not landed here): **substance binding of presence conjuncts.** Every conjunct that is satisfied by a named string or quote needs a mutant that keeps the string and breaks what the string is claimed to support (a rule row that quotes S213 in the inverted sense; a repair note naming R2 against a receipt on a different revision). A counter whose conjuncts all survive that mutant set is scored presence-only, not substance. The companion rule: one measurement convention per field, named in the counter (the 1022/1021 pair above is the instance).

## 5. Ownership and handling

- Every LOOSE hit is owned by its sibling lane (kumitate, kengaku, tameshi, mori, chousa, each lane for its own descriptions and receipts). Reported, not absorbed. No sibling file was touched.
- Kotoba-owned items: S-c, S-d, L-9, and the census battery gap in §3. These are for the L1, not for w1 edits.
- No STRICT sibling overlap with the S213 URL or rule text was found.

## 6. Verdict inputs

- Strict sibling overlap with C1 or C2: none found (§1 S-a, S-b, S-d).
- Material finding for the L1: the kotoba description has 3 characters of census headroom (§3), and the no-harm battery omits the census gate.
- Cross-claim QUALITY candidate: substance binding of presence conjuncts (§4).

VERDICT: no strict sibling URL or rule-text overlap with C1/C2; the material finding is kotoba's own description at 1021 of 1024 census characters, with check_sibling_census.py missing from the no-harm battery, plus one shared presence-proxy pattern worth one QUALITY criterion.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/K01SiblingOverlap.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/K01SiblingOverlap.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/K01SiblingOverlap.census-r74-at-head.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/K01SiblingOverlap.census-r49-at-head.txt
