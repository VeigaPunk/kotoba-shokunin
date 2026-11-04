# Round 85 — Sibling / Cross-Source Scan & Connector Synthesis

**Seat:** Connector  
**Lane:** kotoba-shokunin  
**Round:** 85 (Attempt 1, hyaku run 15)  
**Host:** Linux (`7.2.11-arch1-1`)  
**Base commit:** `1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b`  
**Freeze commit:** `f822dd113fe9f58661dd642dc207669581a4ab57`  

---

## 1. Sibling Scan at Committed Heads

Committed heads surveyed:
- `kengaku-shokunin`: `35b1e4e09d7666889e561ede274485aba1e2ad11`
- `kumitate-shokunin`: `232350995d3001e606609aaf22ba1b58168d3655`
- `tameshi-shokunin`: `d10a9c66d6181cddcad52cdbffd672beb886ff6c`

### Sibling Survey Table

| Sibling Lane | Committed Head | (a) Description render cut / trigger-eval discipline held? (file:line) | (b) Host substrate pinning of installed harness held? (file:line) | Collides with C1? | Collides with C2? |
|---|---|---|---|---|---|
| **kengaku-shokunin** | `35b1e4e09d76` | **No.** `kengaku-shokunin/PROVINCE.md:32-34` explicitly cedes prompt/skill-craft rules and render/trigger behaviour to kotoba: `kotoba: prompt- and skill-craft rules, render/trigger behaviour — this lane keeps the measured effect of prompt format on capability and hands the reusable craft implication out.` Also confirmed in `kengaku-shokunin/SKILL.md:3`. | **No.** `kengaku-shokunin/PROVINCE.md:14-15, 20` pins local served model endpoints (`127.0.0.1:34113`, `127.0.0.1:45669`/`:1234`) and runs hermetic offline replay grader `grader.py` over internal probe logs. Refuses model-serving plane config (`PROVINCE.md:26-27`) and has zero pins or checks over installed host harness binaries (`omp`/`opencode`). | **No collision.** | **No collision.** |
| **kumitate-shokunin** | `232350995d30` | **No.** `kumitate-shokunin/PROVINCE.md:32` routes prompt craft out: `Prompt and skill craft → kotoba.` Scopes only OMP task/hub dispatch, ufo-fsd scripts, and runtime (`kumitate-shokunin/SKILL.md:3`). | **No.** `kumitate-shokunin/PROVINCE.md:16, 57-58` gates the shape of `~/.omp/agent` depth-1 members via `scripts/omp-census.mjs` (names, kinds, modes), but explicitly rules member content and binary hashing out of scope (`readdir + lstat only`). Kumitate recognizes host substrate re-derivation and binary pinning (`omp.real`, `opencode`) as kotoba's owned ground in `kumitate-shokunin/.ufo/waves/round-80/w1/K80ConnectSiblings.md:180-183`. | **No collision.** | **No collision.** |
| **tameshi-shokunin** | `d10a9c66d618` | **No.** `tameshi-shokunin/PROVINCE.md:14-17` refuses product domains: `Refuses: product domains — every lane's gate remains its own; tameshi owns only the reusable craft... Never edits a sibling's gate code.` Confirmed in `tameshi-shokunin/SKILL.md:3` (`Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'`) and `kotoba-shokunin/PROVINCE.md:77`. | **No.** `tameshi-shokunin/PROVINCE.md:7-12, 28-38` owns general verification-fixture craft, mutation testing kill-rate ledgers, and hermetic suite patterns across fleet gates. Holds no binary hash or mtime pins of the host harness. | **No collision.** | **No collision.** |

---

## 2. Staged Package Entry & Round-74 Flip Condition

### Reading
- Staged package entry: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md` (lines 4-8):
  - Sources S231 (`https://agentskills.io/skill-creation/optimizing-descriptions.md`) and S232 (`https://agentskills.io/skill-creation/best-practices.md`), fetched 2026-10-23.
  - Ground: `the lane's description-writing and trigger-fidelity item — the corpus held the Anthropic description rule and the trigger-eval loop, but not the format maintainers' own guidance or eval design.`
- Round-74 verifier spot-check rejection row (`corpus/lessons/round-74-verifier-spotcheck.md:116`):
  - `| staged spec-description-trigger-discipline.md | reject | /home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md (source S231 = …/optimizing-descriptions.md); git show ec2c1d3:corpus/SOURCES.md | grep -n optimizing-descriptions | agree | the URL is already held twice (S210, S213), so the row would be a W04 duplicate; its best-practices half (staged S232) is now carried by the admitted S223 entry; flip stated |`
- Round-74 lesson recorded flip condition (`corpus/lessons/round-74.md:57-60`):
  - `Rejected, with reason and flip ... (1) staged spec-description-trigger-discipline.md: its source row S231 is agentskills.io/skill-creation/optimizing-descriptions.md, a URL the lane already holds as S213 ... so appending it would add a W04 duplicate-URL row ... flip: a page of the specification that states a trigger rule S213 does not.`

### Flip Condition Satisfaction: **YES**

The round-74 flip condition — adopting the trigger discipline content while citing the already-held registry row S213 instead of minting a duplicate row S231, and refusing the already-carried best-practices half (staged S232, already held by S223) — is **satisfied** by round 85's plan:
1. `plans/round-85.md:65-67` (Rule R8 definition):
   `- **R8 sourced_entry** — corpus/knowledge/description-trigger-discipline-round85.md exists at the measured rev with source: naming S213, verified-at: 2026-11-04, a recheck: value, and a located quote of ≤ 25 words.`
2. `plans/round-85.md:114-119` (Frontier step §2b):
   `- corpus/SOURCES.md: ... This round: **no new row** (S213 already holds the page; a new row would be a W04 duplicate — the round-74 rejection reason), S213 re-opened live this round (HTTP status, bytes, sha256, located quote, access date) and its used-by gains the new entry (old→new logged in the lesson). Rows added: 0. Rows touched: S213 (used-by)...`
3. `plans/round-85.md:125-128` (Assimilation):
   `- Assimilation: merge/kotoba/ — the round-74-rejected spec-description-trigger-discipline.md is adopted through this lane's own gate as the round-85 entry, re-grounded on S213 (the row the package's S231 duplicates); refused material (its best-practices half, already carried by S223) stays refused with the reason recorded.`
4. `.ufo/waves/round-85/claims.json:19, 61-64`:
   `"sourced_row": "S213"`, `"sources_rows_added": 0, "sources_rows_touched": ["S213"]`, `"assimilation": "merge/kotoba spec-description-trigger-discipline re-grounded on S213 through this lane's gate"`.

---

## 3. Merge/Kotoba Staged Overlaps & Unimplemented Considerthese Proposals

### Staged Entries in `shokuknow/merge/kotoba/` Overlapping C1 or C2
1. `description-writing-and-trigger-testing.md` (overlaps C1 depth):
   - *Why:* Synthesizes Anthropic's reference skill creator (S204), Qwen Code conventions (S205, S206), and SkillRouter/SkillsBench (S210, S211) to define description writing rules (explicit function and triggering context) and procedural trigger evaluation (20 queries, should-trigger vs should-not-trigger, 60/40 train/test split, 3 runs). Directly overlaps C1's description trigger discipline and eval-set shape (R1–R4, R6).
2. `spec-eval-file-format.md` (overlaps C1 depth):
   - *Why:* Sources S234 (`https://agentskills.io/skill-creation/evaluating-skills.md`) defining the evaluation artifact (`evals/evals.json`), script-based assertion grading over mechanical properties, and distinguishing trigger queries (whether the skill fires) from execution assertions (whether the output is correct). Overlaps C1's eval set fixture and testing discipline.
3. `skill-invocation-is-the-bottleneck.md` (overlaps C1 depth):
   - *Why:* Sources Vercel (S248) and Anthropic (S253) measuring a 56% non-invocation failure rate when descriptions fail to trigger skills, and demonstrating recovery via explicit prompting. Overlaps the motivation behind C1's imperative invocation (R4) and trigger prefixing (R2), though empirical capability rate measurement remains ceded to kengaku.
4. `client-frontmatter-and-discovery-divergence.md` (overlaps C1 depth):
   - *Why:* Sources Deep Code (S250), Junie (S252), and specification client implementation docs (S255, S256) analyzing field requirement divergence (required vs recommended `description`, lenient loading), touching C1's frontmatter ceiling (R3) and clean syntax rules (R7).
5. **C2 Substrate Overlap:** **None.** No staged entry under `shokuknow/merge/kotoba/` covers host substrate binary pinning, loader class extraction, or ELF inspection of `omp` / `opencode`.

### Unimplemented `considerthese` Proposals Not Touched by Round 85
From `considerthese/2026-10-26.md` (operator-authored suggestions):
- **Proposal 1 — SKILL.md Byte Ceiling and Line Length Cap:** Proposal to cap `SKILL.md` size in floors guard (hold <= 70 KB, then ratchet down) and add a 200-char max-line check to arrest file growth (at round 74: 590 lines, 78,569 B). Explicitly sized out of round 85 as a separate round (`plans/round-85.md:130`).
- **Proposal 2 — Move `## Gate registry` out of `SKILL.md`:** Proposal to move the 24.9 KB gate registry section out of `SKILL.md` into `verifiers/REGISTRY.md` and redirect `check_gate_registry.py` there. Explicitly sized out of round 85 as a separate round (`plans/round-85.md:130`).
- **Proposal 4 — Gating Round Closure on Falsify Wave Completion:** Proposal to close rounds as "provisional" in `SCORECARD.md` if wave 2 (falsify) is not dispatched, pending a mutation battery or non-author spot-check. Unimplemented; not touched by round 85.
- **Proposal 5 — Evidence Growth Budget:** Proposal to introduce a per-round evidence cap or compress seat logs after closure to bound repository and `.ufo/` size growth (which had reached 203 MB). Unimplemented; not touched by round 85.
*(Note: Proposal 3 — description self-audit against specification trigger discipline — is the single proposal actively executed by C1 in round 85).*

---

## 4. No-Absorb Line

**Kotoba must not claim measured capability effects or empirical invocation/benchmark rates of prompt format (owned by kengaku-shokunin, `kengaku-shokunin/PROVINCE.md:32-34`), harness orchestration dispatch/runtime tooling (owned by kumitate-shokunin, `kumitate-shokunin/PROVINCE.md:3,32`), or general fixture/mutation testing methods (owned by tameshi-shokunin, `tameshi-shokunin/PROVINCE.md:3,14-17`).**

---

## 5. Non-Obvious Move: Substrate-Grounded Listing Cut & Eval Trigger-Isolation (C1 + C2 Synthesis)

### Evidence
1. **C1 (depth)** introduces Rule R1 (`first_sentence_le_99`), which is empirically based on omp's skill-listing preview truncation at offset 99 (`slice(0, _8n-1)` where `_8n=100`, documented in `SKILL.md:29-30`).
2. **C2 (freshness)** re-pins the host substrate ELF `/home/vgpnk/.local/bin/omp` (omp 18.15.0), while `verify_surfaces.py` checks 7 loader surface classes (`omp:agents-md/AGENTS.md`, `omp:claude-md/CLAUDE.md`, etc.).
3. **Decoupling Gap:** `verify_surfaces.py` extracts only discovery/loader calls (`.md`-suffixed registration calls); it does not inspect or pin the skill description preview truncation logic or constants. Live string inspection of `/home/vgpnk/.local/bin/omp` demonstrates that `previewSkillDescription`, `SkillDescriptionCatalog`, `SkillDescriptionStore`, and `skill-descriptions.db` reside in bytecode chunk `skill-descriptions-gdjp0ezs.js`.
4. **Eval Set Contamination Gap:** C1's Rule R6 (`eval_set_shape`) validates the static lexical shape of `verifiers/fixtures/description-eval-round85.tsv` (8–10 positive, 8–10 negative, >=5 indirect positives without declared trigger terms, near-misses sharing >=1 word >=4 chars), but does not check for semantic trigger contamination against the candidate payload (`plans/round-85.md:77`). Specifically, a near-miss `should-not-trigger` query could inadvertently match a declared trigger phrase, or an indirect `should-trigger` query could trigger an anti-trigger phrase.

### Affected Axes
- `depth` (C1, owned lowest axis, 9)
- `freshness` (C2, advisory tied-lowest axis, 8.0)

### Proposed Move
**Synthesize C1 and C2 through Substrate Grounding and Eval Set Trigger-Isolation:**
1. *Substrate-Grounded Listing Cut (Freshness deepening):* In `verify_surfaces.py` or a companion check, add an explicit symbol assertion verifying that the pinned `omp` binary exports `previewSkillDescription` and references `skill-descriptions.db`. This mechanically couples C1's 99-character ceiling to the verified C2 substrate ELF, ensuring R1's threshold cannot silently become an ungrounded historical relic across future harness releases.
2. *Eval-Set Semantic Isolation (Depth deepening):* Enforce a semantic boundary check on `description-eval-round85.tsv`:
   - No `should-not-trigger` query may contain any multi-word literal phrase declared in the description's `Triggers:` clause.
   - No `should-trigger` query may contain any phrase declared in the description's `Anti-triggers:` clause.
   This deepens eval set quality without altering the 8 frozen rule strings of C1.

### Risks
- `omp`'s bundle is compiled into minified bun bytecode chunks; verifying internal constants like `_8n=100` directly in bytecode requires AST decompilation or bytecode parsing rather than plain literal scanning. Symbol-presence checks (`previewSkillDescription`, `skill-descriptions.db`) must remain robust against minified chunk name changes.
- Near-miss queries intentionally share vocabulary with the description (required by R6); the isolation check must strictly differentiate between individual shared words (permitted/required) and full multi-word trigger phrases (prohibited in negative queries).

### Verification
- Substrate symbol presence verified directly on the pinned host binary:
  `strings -n 8 /home/vgpnk/.local/bin/omp | grep -E "(previewSkillDescription|skill-descriptions\.db)"` (receipt: `.ufo/waves/round-85/w1/Connector/omp-preview-strings.txt`).
- Eval-set trigger isolation can be verified offline by token/substring matching between `verifiers/fixtures/description-eval-round85.tsv` and the candidate description's frontmatter trigger clauses.
