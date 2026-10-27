# B20ConnOverlap — sibling-overlap scan for description-craft ground (round 76, w1)

Seat: B20ConnOverlap (leaf, report only). Read-only: no lane file, registry, counter or claim data was written.
Frozen contract: `PLANS/ROUND-76.MD` was NOT found under the lane tree (`read` of
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/PLANS/ROUND-76.MD` → not found; `glob` `kotoba-shokunin/**/ROUND-76*` → no files).
This scan therefore uses the seat spec's own ground definition ("skill-description writing or trigger evaluation") and does not check the contract's touch list.

## Coverage

- Sibling `PROVINCE.md`: 20 siblings (lanes other than kotoba) enumerated by glob; all 20 scanned by grep for skill / frontmatter / trigger terms. Full read: kengaku, chousa, kumitate, kotoba (the three named in the seat spec plus kotoba's own scope).
- Sibling `SKILL.md`: 18 of 20 read by grep with the description-craft pattern. `audio-shokunin/SKILL.md` and `game-dev-2d-shokunin/SKILL.md` do not exist at those paths (tool reported "Skipped missing paths").
- Full read of frontmatter `description` for kengaku, chousa, kumitate, kotoba.
- Sibling `corpus/` trees (20): grep for `optimizing-descriptions`, `skill-creation`, `agentskills.io`, `should_trigger`, `trigger eval`, `trigger fidelity`, `description craft`, `description optimi`, `skill description`.
- Note on tooling: a `*` glob inside a `;`-joined grep path did not expand across siblings on the first attempt, so the scan was re-run with explicit absolute paths per sibling. Results below come from the explicit-path runs.

## STRICT_HITS

Definition used: a sibling scope text (PROVINCE.md or SKILL.md, or a sibling corpus entry) that names description-craft or trigger-evaluation as that sibling's own ground.

**STRICT_HITS = 0.**

No sibling PROVINCE.md or SKILL.md claims skill-description writing, description optimisation, or trigger-eval design. The only "trigger" text in sibling SKILL.md files is each lane's own `Triggers:` / `Anti-trigger:` clause in its frontmatter description (kengaku, chousa, kotodama, kaidoku, mori, souji, tameshi in the single-line scan). Those are instances of the convention, not claims about how to write or evaluate a description, so they do not count.

## Adjacent hits (not STRICT, recorded so the L1 can route them)

1. **Mechanism overlap with chousa (1 hit).** The C1 claim asks for sha256-pinned snapshots and located quotes. chousa names that mechanism as its own:
   - `chousa-shokunin/PROVINCE.md:5-8` — "Owns: … claim-vs-source verification; … this lane's own corpus and gates."
   - `chousa-shokunin/SKILL.md` decision table, row "Cite a located quote from a registered web source (r29)" → `python3 tools/quote-reopen.py verify --items <tsv>`.
   - `chousa-shokunin/SKILL.md` checklist: every web quote re-opened with `tools/quote-reopen.py`; `research-gate.sh verify-claims` requires a `"sha256"` pin per claim.
   The description-craft ground is not chousa's, so this is a method-level touch, not a STRICT hit. Recommendation: the C1 entry should cite chousa's gate or name why it does not, rather than fork a second located-quote check. Kotoba's own round-71 README line (`corpus/README.md:137`) says "located quotes re-verified on the .mdx sources" without naming a chousa tool.

2. **Routing into kotoba (4 allocations, no overlap).** Each names skill/prompt craft as kotoba's and does not claim it:
   - `kengaku-shokunin/PROVINCE.md:30-32` — "kotoba: prompt- and skill-craft rules, render/trigger behaviour"; and `:138` in the Adjacent table.
   - `kengaku-shokunin/SKILL.md` description — "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)."
   - `kumitate-shokunin/PROVINCE.md:29` — "Prompt and skill craft → kotoba."
   - `kotodama-shokunin/PROVINCE.md:20` and its SKILL.md description — "NOT prompt/skill craft (kotoba)."

3. **Stale contested row in kengaku evidence (freshness, 1 hit).** `kengaku-shokunin/corpus/evidence/round9-fleet/sibling-overlap.md:12` classifies kotoba as **Contested** with "measured router-visible prompt/description behavior." That is a round-9 artefact. The current `kengaku-shokunin/PROVINCE.md:30-32` hands "render/trigger behaviour" to kotoba, and kengaku's `corpus/knowledge`, `corpus/README.md` and `SKILL.md` contain no skill-activation or router-visible entry (grep: no matches). The C1 entry should cite the current PROVINCE line, not the round-9 "Contested" row.

4. **Lexical false positives (0 strict).**
   - `kumitate-shokunin/corpus/knowledge/omp-agent-root.md:25` and `kumitate-shokunin/scripts/omp-census.mjs:73` — `skill-descriptions.db` is an OMP cache file in a permission census. Not description craft.
   - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/executability/materials.md:168` (F22) — a git-history note of a shipped skill's description commit. Audit of a third-party skill's history, not craft guidance.
   - `kengaku-shokunin/PROVINCE.md:161` and similar — `skill` only as a path segment.

## Duplicate check

**No sibling holds a description-craft entry.** No sibling corpus or scope text contains `optimizing-descriptions`, `agentskills.io/skill-creation`, `should_trigger`, `trigger eval`, or `description optimi`. Lexical hits on `skill description` were the false positives in item 4 above.

**Intra-lane duplicate risk (kotoba itself, not a sibling).** The source the C1 claim wants to admit is already held in this lane, so an entry that re-admits it would be a duplicate:
- `kotoba-shokunin/corpus/SOURCES.md:153` — S213 "Agent Skills — Optimizing skill descriptions", `docs`, tier A, "supersedes S210 for citation", with the quote "A should-trigger query passes if its trigger rate is above a threshold".
- `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:6` and `:33` (F7) — the same S213 quote used as a grounded row.
- `kotoba-shokunin/SKILL.md:193` — trigger-set and `should_trigger` guidance already cites S211–S213.
- `kotoba-shokunin/corpus/README.md:232` — "Still not held: … the `optimizing-descriptions` trigger-eval design beyond S213." So the open ground is the description-craft guidance beyond the eval protocol, not S213 itself.

Recommendation for the L1: frame the C1 entry as new rows for the description-craft guidance and treat S213 as an existing row to cite, not re-admit.

**Namespace note.** kengaku's `S213` (`kengaku-shokunin/.ufo/waves/round-*/…`) is a different source in another lane's ID space. IDs are per-lane, so this is not a fleet collision. It matters only if a cross-lane citation uses a bare `S213`; qualify with the lane name.

## Verdict

- STRICT_HITS = 0 (no sibling claims description-craft or trigger-evaluation ground).
- ADJACENT: mechanism overlap with chousa (located quotes, sha256 pins) = 1; routing allocations into kotoba = 4; stale kengaku "Contested" row = 1.
- Sibling duplicate of a description-craft entry: none. Intra-lane duplicate risk: S213 already held (SOURCES.md:153, skill-eval-artefacts-round70.md:6).
- Blocker: `PLANS/ROUND-76.MD` not found under the lane tree, so the frozen touch list was not checked.

Installs: none. Scratch: none created. Report only; no lane, registry or counter file touched.

VERDICT: STRICT_HITS=0 ADJACENT=6 DUPLICATE_SIBLING=none DUPLICATE_INTRA_LANE=S213(existing) BLOCKER=PLANS/ROUND-76.MD-absent
