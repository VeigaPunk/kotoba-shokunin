# ScoutW2SiblingVerify — independent sibling-overlap check

Seat: `kotoba-r64.ScoutW2SiblingVerify-2`. Axis: **adjacency**; controls: reproducibility and fair method attribution. Read-only outside this report; no dispatch, installs, production edits, index writes, or verifier executions.

## Findings

**STRICT_HITS = 0 for all three artifacts under the declared scan.** This independently agrees with the wave-1 adjacency disposition, but **ConnSibling's literal `M95` zero-hit control is wrong**: five occurrences occur in three sibling-corpus files, all unrelated homonyms after reading each hit. Kotodama's R64-M9 method credit is fair as a warning against selector-induced exclusivity and misattributing kills, not as evidence of exclusive kills.

| Pattern | Matching lines / occurrences | Files | Sibling lanes | Strict hits |
|---|---:|---:|---:|---:|
| `span_missing` (case-sensitive) | 0 | 0 | 0 | 0 |
| `g7_conjunct` (case-sensitive) | 0 | 0 | 0 | 0 |
| `check_r64` (case-sensitive) | 0 | 0 | 0 | 0 |
| `temporal mismatch` (case-insensitive) | 0 | 0 | 0 | 0 |
| `M95` (case-sensitive, literal substring) | **5** | **3** | **2** | **0** |

Each M95-matching line contains one occurrence. Per-lane M95 totals: kengaku 2, kotodama 3, every other sibling 0. Every lane has zero for the other four patterns.

| New artifact | STRICT_HITS | Basis |
|---|---:|---|
| `corpus/knowledge/g7-span-pinning-round64.md` | 0 | Neither G7 symbol occurs in sibling corpora; scoped knowledge-filename control finds only kotoba's entry. |
| `verifiers/check_r64_routed_repairs.py` | 0 | No sibling-corpus `check_r64` or correction-marker hit; verifier-filename control finds only kotoba's counter. |
| `corpus/lessons/round-64.md` / inherited row (t) | 0 | No sibling occurrence of its distinctive G7 symbols; the only sibling with the same lesson filename is kotodama, whose independently read claims concern language socialization, redirect edges, and its own closure defects. Method adjacency, not the same claim/artifact. |

Strict classification follows ScoutSiblingOverlap.md:14: same claim or same artifact, not common mutation-testing vocabulary, a shared round number, or an identifier homonym. The zeroes are bounded by this discovery/classification method, not a proof against every possible differently worded duplicate.

## Independent search scope and raw evidence

`glob` on `/home/vgpnk/Projects/shokunin/*/corpus` returned 21 corpus roots. Excluding kotoba leaves **20 sibling corpora**:

```text
audio-shokunin, chousa-shokunin, game-dev-2d-shokunin,
game-dev-3d-shokunin, kagi-shokunin, kaidoku-shokunin,
kake-shokunin, kama-shokunin, kasegi-shokunin, kengaku-shokunin,
kotodama-shokunin, kumitate-shokunin, lore-shokunin, mado-shokunin,
mori-shokunin, revenger-shokunin, souji-shokunin, tabi-shokunin,
tameshi-shokunin, tsukuroi-shokunin
```

I submitted five separate `grep` tool calls, one per requested pattern, each with all 20 absolute `.../<lane>/corpus` paths explicitly joined by semicolons, `gitignore:false`, `skip:0`; `case:true` except `case:false` for `temporal mismatch`. No extension filter or wave-1 result was used as a search input. These are literal discovery searches, not LSP semantic references.

Actual tool output for each of `span_missing`, `g7_conjunct`, `check_r64`, and `temporal mismatch`:

```text
No matches found
```

The M95 tool output identified these five matching lines (all three files opened at the relevant sections):

```text
kengaku-shokunin/corpus/evidence/round12-fleet/grader_r12_draft.py:4043
        ("M95 corrupt a bundled file's bytes", "r12.ordering.sha256.predictions-r12.md",
kengaku-shokunin/corpus/evidence/round14-fleet/r14-mutation.md:40
sha/content mutations, M91-M95 ordering/bundle corruptions, M96 pin mismatch —
kotodama-shokunin/corpus/knowledge/civilizations/zapotec-mixtec.md:17
- [M95] John Monaghan. 1995. *The Covenants with Earth and Rain: Exchange, Sacrifice, and Revelation in Mixtec Sociality*. University of Oklahoma Press. Modern ethnography: comparative leverage, not proof of unchanged preconquest belief.
kotodama-shokunin/corpus/knowledge/civilizations/zapotec-mixtec.md:69
- **Ñuhu** is discussed in scholarship on earth/sacred beings; it is rendered “earth/land,” with senses running from soil and terrain to the sacred [T01; S73, p. 66]. Exact tone contrasts and its relation to a particular town-name spelling remain `(to-verify)` here. Do not equate ñuu and ñuhu because their untoned romanizations resemble one another. [M95; JP11]
kotodama-shokunin/corpus/knowledge/civilizations/zapotec-mixtec.md:94
| Earth–rain relations | Exchange, sacrifice, and obligations in Monaghan's ethnography [M95] | Modern comparison; historical continuity must be argued, not presumed |
```

Repeating M95 with `gitignore:true` returned the same five lines in the same three files; ignore handling does not explain these omissions. The `grep` device does **not expose process exit codes**; none are invented here. Shell commands below include actual successful exit markers.

Scoped filename glob outputs:

```text
# kotoba-shokunin/corpus/knowledge/
g7-span-pinning-round64.md
```

```text
# kotoba-shokunin/
## verifiers/
check_r64_routed_repairs.py
## corpus/lessons/
round-64.md
# kotodama-shokunin/corpus/lessons/
round-64.md
```

These came from `*/corpus/knowledge/g7-span*`, `*/corpus/knowledge/*span-pinning*`, `*/corpus/knowledge/*span_pinning*`, `*/verifiers/check_r64*`, and `*/corpus/lessons/round-64.md`. An earlier recursive `*/corpus/**/...` glob timed out with partial output; it is **not** used as negative filename evidence. The narrower successful calls above replaced it. A positive-control grep on kotoba's landed `corpus/lessons/round-64.md` returned `M95` at lines 57, 61, 97 and 110 and `span_missing` at line 107.

## Strict reading of every nonzero hit

1. **Kengaku `_battery()`**, `corpus/evidence/round12-fleet/grader_r12_draft.py:4027–4053`: M91–M96 are ordering/hash/bundle mutants. M95's tuple expects `r12.ordering.sha256.predictions-r12.md` and supplies `{"file_mut": "write_bundle"}`. This is a bundled-file corruption mutant, not kotoba's citation naming the wrong committing revision. **Not strict.**
2. **Kengaku r14 report**, `corpus/evidence/round14-fleet/r14-mutation.md:1–43`: the report concerns its round-12 grader, 732 checks, S0–S7, and the M91–M95 ordering/bundle-corruption group. The M95 mention corroborates the same unrelated mutant identity. **Not strict.**
3. **Kotodama bibliography and references**, `corpus/knowledge/civilizations/zapotec-mixtec.md:9–23,65–70,86–97`: `[M95]` is expressly John Monaghan's **1995** ethnography, cited for sacred landscape and earth–rain relations. All three hits use that bibliography key, not a receipt/citation-revision defect label. **Not strict.**

## R64-M9 attribution

Observed source: `kotodama-shokunin/corpus/lessons/round-64.md:13–20,259–288`.

- Kotodama's O claim pins seven redirect-edge properties plus a DRIP fixture; Ca repairs that lane's own routed closure defects. Neither is G7 span pinning or kotoba's four r63 defects.
- R64-M9 says launching mutants with `--only` their pinned legs makes apparent equality of failure sets a property of selection, **not measured exclusivity** (259–263).
- It records collateral EDGE failures and the explicit caveat: “MUT verifies each mutant FAILs its PINNED leg; it does not verify exclusivity” (274–285).
- Its standing remedies are to narrow the claim to pinned-leg failure, or add a full-leg exclusivity measurement (285–288).

Observed transfer: `kotoba-shokunin/.ufo/waves/round-64/w1/ConnSibling.md:70–84` proposes full-suite mutant runs, arm-specific failure labels, and separate accounting for SM4/SM6's pre-existing `eligible world` kills. It expressly declines “fails exactly its arm and no other.” The landed lesson credits R64-M9 at `corpus/lessons/round-64.md:140–148`; the knowledge entry's landing note at `corpus/knowledge/g7-span-pinning-round64.md:5` separates the old SM4/SM6 kills from new-arm attribution.

[INFERENCE] **The credit is fair and bounded:** kotoba reuses the lesson about what a selected-leg result can establish and about attributing a kill to an actual measured arm. R64-M9 is not evidence that kotoba invented this testing method, that the substrates overlap, or that kotoba's mutant failures are exclusive. The landed parenthesis “mutant-leg exclusivity” should be read as the warning's subject, not an exclusivity assertion. I did not re-execute either lane's mutation battery.

## Disagreements with wave 1

- **Agree** with ScoutSiblingOverlap.md:24–36,75–81 on the four overlapping requested zero-count terms and on STRICT_HITS = 0. Its displayed authoritative recount does not include M95; I do not attribute a nonexistent M95 count to it.
- **Disagree** with ConnSibling.md:28–34's control that literal M95 appears outside kotoba only once, in fleet MANIFEST.json. There are additionally **three corpus files / five literal occurrences**. The implication at ConnSibling.md:51 that kengaku's corpus is M95-negative is also false.
- The literal-count discrepancy **does not change strict overlap**: each extra hit is unrelated after reading it. Git history dates these files before the round, and their scanned worktree blobs equal committed HEAD blobs (evidence below). [INFERENCE] This is a pre-existing literal-scan miss, not a new round-64 duplicate or just ignored-file noise. The exact wave-1 command and its original search coverage remain unavailable in that report, so its failure mechanism is unresolved.

## Revision binding and real command evidence

The lane HEAD at the initial read was `b99fb79c27042e0f8a598cbbb4d81479a806b518` (exit 0), not the assigned measured commit. I did not move any ref or index. Read-only blob queries show that both wave-1 reports and both landed attribution files are byte-identical at the measured commit, HEAD, and the read worktree.

Command (repo root):

```sh
git rev-parse c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/lessons/round-64.md HEAD:corpus/lessons/round-64.md c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/knowledge/g7-span-pinning-round64.md HEAD:corpus/knowledge/g7-span-pinning-round64.md c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/w1/ConnSibling.md HEAD:.ufo/waves/round-64/w1/ConnSibling.md c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/w1/ScoutSiblingOverlap.md HEAD:.ufo/waves/round-64/w1/ScoutSiblingOverlap.md && printf 'blob_revisions_exit=0\n'
```

Actual output:

```text
58ff37c04ae048ce00dcbbc53f1c2fa71693ef98
58ff37c04ae048ce00dcbbc53f1c2fa71693ef98
82f6e52d2689cb41c3af1e61ad6c85fef70e57db
82f6e52d2689cb41c3af1e61ad6c85fef70e57db
4b6f7e624053a4b9bd07fbd9f32bf65e359f5ea7
4b6f7e624053a4b9bd07fbd9f32bf65e359f5ea7
7cb68de1b3c320e8f09bb8ffa4c86e286543cf9c
7cb68de1b3c320e8f09bb8ffa4c86e286543cf9c
blob_revisions_exit=0
```

Command:

```sh
git hash-object corpus/lessons/round-64.md corpus/knowledge/g7-span-pinning-round64.md .ufo/waves/round-64/w1/ConnSibling.md .ufo/waves/round-64/w1/ScoutSiblingOverlap.md && printf 'worktree_blobs_exit=0\n' && date -u '+observation_utc=%Y-%m-%dT%H:%M:%SZ' && printf 'clock_exit=0\n'
```

Actual output:

```text
58ff37c04ae048ce00dcbbc53f1c2fa71693ef98
82f6e52d2689cb41c3af1e61ad6c85fef70e57db
4b6f7e624053a4b9bd07fbd9f32bf65e359f5ea7
7cb68de1b3c320e8f09bb8ffa4c86e286543cf9c
worktree_blobs_exit=0
observation_utc=2026-10-24T04:21:05Z
clock_exit=0
```

Commands and actual outputs dating the M95 files:

```sh
git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin log -1 --format='%H %cI %s' -- corpus/evidence/round12-fleet/grader_r12_draft.py corpus/evidence/round14-fleet/r14-mutation.md && printf 'kengaku_log_exit=0\n'
```

```text
0c16a79ecd12bcb9edfd6915e9d3ce619d0d9049 2026-09-29T01:21:34-03:00 round-14
kengaku_log_exit=0
```

```sh
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log -1 --format='%H %cI %s' -- corpus/knowledge/civilizations/zapotec-mixtec.md && printf 'kotodama_log_exit=0\n'
```

```text
9dc18ec1339bffd6f81e74f1a5742464ef578749 2026-10-17T18:17:00-03:00 round-9: admit F/O/D — escalated residuals, 7/7 gate baselines, D3 acceptance
kotodama_log_exit=0
```

Additional read-only `git rev-parse HEAD:<path>` / `git hash-object <path>` calls returned identical pairs for the three M95 files, all exit 0: kengaku grader `95ab327d630150781808702a0b49b01a03439efd`; kengaku r14 report `5237dbdc3910763912f31cec36e0682757229b60`; kotodama bibliography `12d45b4ded0a3aebf5b7817a0e111784c02e9e89`.

## Confidence and remaining gaps

- **High:** five requested literal scan counts; strict classification of every positive hit; textual basis for the bounded R64-M9 attribution; measured-tip identity of the four kotoba documents used.
- **Bound:** sibling searches are live corpus observations, not an atomic cross-repository historical snapshot at kotoba's c019919 commit. No binary-media semantic examination, renamed/fully paraphrased duplicate census, or scan outside the requested sibling-corpus roots is claimed. The verifier-filename control is supplementary only.
- **LSP unavailable:** requesting `xd://lsp` returned `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` There was no server/device to query or warm up. Searches are explicitly literal fallbacks; classifications come from the opened source/prose, not purported semantic-reference results. No exported API contract was changed or inferred from grep absence.
- **Rules dependency:** the requested `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` read returned `Path ... not found`. No tool installation or update was needed or performed; pacman was not invoked.
