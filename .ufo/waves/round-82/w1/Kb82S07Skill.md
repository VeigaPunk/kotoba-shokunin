# Kb82S07Skill — minimal SKILL/PROVINCE author rule linking the current loader-refresh entry

Seat: Kb82S07Skill (scribe, leaf member — no subagent dispatch). Base `47dbe8781657de563ff867caca6244d28e3db504`.
Date: 2026-10-30. Axes judged: freshness, operability. Plan: `plans/round-82.md` (read first).

## Behavior delivered

One patch, `build/Kb82S07Skill.patch` (sha256 `2f13f78df3aa7fc5c401e6b99ef9aa3d03eea3000da5173792faaa2fdda46612`),
adds exactly **3 lines** to `SKILL.md` — a new final box in `## Trigger-fidelity checklist`
(inserted after the round-72 rung box, before `## Agent-definition fidelity checklist`):

```
- [ ] Present-tense host-substrate claims (binary paths, versions, embedded-JS
      anchors) in this file and `PROVINCE.md` link the latest loader-refresh
      entry in `LOG.md`; no second § Gate registry row for an existing gate.
```

The rule does three things, in 3 lines:
1. **Linking**: every present-tense host-substrate claim (omp/opencode binary paths,
   versions, embedded-JS anchors) in SKILL.md and PROVINCE.md must link the `LOG.md`
   entry of the latest loader refresh — today that is `LOG.md:2770`
   `## Round 72 — C1 depth (author-facing rules, sourced), C2 freshness (host substrate), C3 consistency (tip battery)`;
   the round-82 C1 entry (source **S251**, reserved per the plan, absent from base
   `corpus/SOURCES.md` — grep over base bytes, 0 matches) supersedes it when it lands.
2. **No duplicate registry row**: an existing gate (e.g. `verifiers/check_substrate_repin_v2.py`,
   registry row already at base `SKILL.md:510`) never gets a second `## Gate registry` row.
3. It is a checklist box, so the file's own box-map discipline (`SKILL.md:229-235`) pins it.

**PROVINCE.md is intentionally not edited.** `verifiers/check_province_core.py` (read in full,
lines 1-123) makes `## Frontier` and `## Adjacent` byte-identical to base `a5f7459f…`
(Adjacent except the round-74 errata ledger), and § Core bullets carry the entry+counter+round
convention — a rule with no knowledge entry belongs in SKILL.md, which the box names (`PROVINCE.md`)
explicitly, so the PROVINCE-side claims are covered without touching that file.

## Historical text inspected; stale path claims quoted precisely

Base SKILL.md (597 lines, sha256 `fb448d66e007730b15e76f48ec76a0d946182e7b75e476314b556c75d282f57a`)
§ Sources still carries two present-tense host claims that the lane's own round-72 held ground
contradicts (`PROVINCE.md` § Core, round-72 bullet: "omp.real and opencode v2.1.4 re-derived and
re-pinned (three classes ledgered in `verifiers/census-removals.json`)"):

- `SKILL.md:543-546` — `- opencode — npm \`opencode-ai\` 1.19.3 since round 47 (the \`${HOME}/.local/bin/opencode\`
  npx wrapper; pinned ELF and lineage in \`verifiers/baseline.json\` and
  \`corpus/knowledge/instruction-surface-census-round13.md\` § B′; the round-8/18
  \`${HOME}/.opencode/bin\` install is gone) + upstream \`github.com/sst/opencode\` (dev):`
  — the claim "the round-8/18 `~/.opencode/bin` install is gone" and the 1.19.3 npx-wrapper
  present tense conflict with the round-72 re-pin (opencode v2.1.4 at `~/.opencode/bin/opencode`).
- `SKILL.md:560-561` — "- \`${HOME}/.local/bin/omp\` embedded JS (\`strings -n 6\`; cite anchors, not offsets —
  ELF offsets and \`strings\` line numbers shift across builds):"
  — written for the pre-r72 ELF; after the r72 landing the embedded-JS readings lived in
  `~/.local/bin/omp.real` (the 1,680-byte wrapper had none), and per `plans/round-82.md` § C1
  the round-82 before-state is the inverse again: `~/.local/bin/omp.real` absent, `~/.local/bin/omp`
  an ELF at 18.14.0. Both directions of drift are why the rule binds claims to the refresh
  entry instead of restating absolute paths.

Base SKILL.md never names `omp.real` (grep over base bytes: 0 matches) — the r72 present-tense
edits the round-72 scout marked EDIT were never landed in SKILL.md § Sources; only the registry
row (`SKILL.md:510`) and the PROVINCE Core bullet carried the re-pin. That gap is the class the
new rule closes for the round-82 integration.

## Gates and touched surfaces

- `SKILL.md` +3 lines (the only production-adjacent surface touched; returned as a patch — no seat commit, no jj/git mutation outside the sandbox clone).
- No `## Gate registry` row added or modified; no SOURCES row; no knowledge entry; PROVINCE.md, LOG.md, SCORECARD.md, corpus/, verifiers/ untouched.
- No tool installed or upgraded (operator tooling directive: nothing needed; pacman untouched, host-wide pause honored). Disk-guard `status` ran first, exit 0 (`/fast/scratch/hyaku` 47% use).

## Sandbox verification (all commands `git -C`/`cd` into the asserted clone; toplevel asserted before every mutation)

Clone: `--shared` of the lane, checkout `47dbe8781657de563ff867caca6244d28e3db504`, `git status --porcelain` 0 lines, toplevel `/fast/scratch/hyaku/kotoba-r82/Kb82S07Skill/clone`.

1. `git apply --check` of the patch against restored base: **APPLY-CHECK-OK** (clean apply).
2. Patched `SKILL.md`: `wc -l` = **600** (base 597; budget box `File ≤ 600 lines` → 3-line headroom exactly consumed, **0 lines of SKILL.md headroom remain for the rest of round 82** — L1 must land any other SKILL.md edit as 1:1 replacements or removals).
3. Patched file sha256 `ed294d2106c298d34b556b781665111877e1d3190d22d2a3f6ddf91af59b4190`.
4. `python3 -B verifiers/verify_skill_checklist.py` in the clone, base vs patched (receipts:
   `build/Kb82S07Skill-checklist-base-run.txt` sha256 `7fdf30c4…c2540`,
   `build/Kb82S07Skill-checklist-patched-run.txt` sha256 `0a9e3625…07a7b`). Delta is exactly:
   - `checklist.box_map_complete`: PASS `evaluated 45 — 45 boxes mapped` → **FAIL `evaluated 46 — unmapped box at line 311 (section 'Trigger-fidelity checklist', sha256 ae87c289c919…)`** — the designed no-silent-add behavior; the printed sha prefix matches the box text hash computed below. This is the single integration requirement the patch creates.
   - `trigger.line_budget`: PASS both, `597 … within budget 600` → `600 … within budget 600`.
   - `trigger.no_placeholder`: 530 → 533 scanned lines, PASS both (the new box carries no marker).
   - `trigger.citation_resolves` FAIL shifts line 587 → 590 (same single finding, `../.ufo/reports/round-7/kotoba.md`): a **sandbox artifact** — `../.ufo/` resolves at the fleet root in the real lane checkout, not from a scratch clone; present identically at base in this sandbox, not introduced by the patch. Same for `trigger.name_directory` FAIL (`name 'kotoba-shokunin' != directory 'clone'` — the sandbox dir name) and the `governance.citation_resolves` FAIL text (same `../.ufo/…` resolution class, byte-identical base vs patched). None of these is a claim about the fleet tree.
5. Baseline-map row for the L1 (map normalization per `verifiers/checklist-baseline.json` header,
   verified shape lines 1-23; last existing trigger id is `trigger.19`):
   - `box_id`: `trigger.20`, section `Trigger-fidelity checklist`
   - normalized-text sha256: `ae87c289c9194ad6f86cb9418481ca07b22c776f25661918f97c15848a83c46f`
     (computed with the map's stated normalization: marker stripped, continuations joined with one space, whitespace collapsed; independently confirmed by the gate's own FAIL line above)
   - proposed disposition: `unexecuted:host-substrate path freshness is host state, not file text; the rule binds claims to the latest loader-refresh LOG entry (round-72 landing today; the round-82 C1 entry with S251 when it lands)`

## Analysis, not run (labeled as such)

- `verifiers/check_author_rules.py` (read, docstring lines 1-70 + RULES table): requires **exactly one** box per rule A1-A4 matching frozen tokens **and ending with** that rule's `(sourced: …; entry: …)` tail; `TOTAL = 4`. The new box carries no sourced tail and none of the A1-A4 token sets (no `name/unique/precedence`, `authority/level/body`, `install/trust/command`, `prompt/always-on/skill/index` as whole words), so the N-of-4 count and the exactly-one conjunct are structurally unaffected. Not executed — analysis from the counter source only.
- `check_province_core.py`: PROVINCE.md untouched ⇒ `## Frontier`/`## Adjacent` byte-identity and the 2-of-2 Core count unaffected. Not executed.
- The executed-box `trigger.citation_resolves` checks only backticked tokens with repo-prefix implication; the box's backticked tokens (`PROVINCE.md`, `LOG.md`) are root files with no prefix and exist — consistent with the PASS observed in run 4 (no new citation finding).

## Out of scope (not done, not claimed)

- C1 re-derivation/re-pin values for omp 18.14.0 (L1/executor seats; S251 receipt).
- C2 hermetic checklist self-test repair (the `governance` arm; the base-vs-patched runs here are sandbox runs, not the C2 counter's 1863-assertion self-test).
- Editing the two stale § Sources claims themselves: that is C1's landing content and would consume the 0 remaining budget lines; the rule makes the linkage obligation durable instead. The precise quotes above are the L1's edit targets.
- No 6/6 tip-battery claim, no after-data production scoring, no control-world creation beyond the sandbox runs above.

## Limits

- All gate evidence is from the shared sandbox clone at base; no fleet-tree gate was run.
- S251 does not exist at base; the rule text deliberately does not cite it (no dangling reference); the linkage target rotates with each landing by design.
- The two receipts capture the sandbox's environmental FAILs verbatim; they are not fleet-tree reds.

Report trailer: `.ufo/waves/round-82/w1/Kb82S07Skill.md` (this file, relative to `/home/vgpnk/Projects/shokunin/kotoba-shokunin`).

VERDICT: DRAFT-READY — 3-line SKILL.md author rule patch verified in the sandbox against base 47dbe8781657de563ff867caca6244d28e3db504: clean apply, 600/600 line budget, exactly one designed integration requirement (checklist-baseline map row trigger.20, sha ae87c289c9194ad6f86cb9418481ca07b22c776f25661918f97c15848a83c46f), no gate-registry row, PROVINCE.md untouched; stale path claims at SKILL.md:543-546 and 560-561 quoted with their round-72 contradictions.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S07Skill.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S07Skill-checklist-base-run.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S07Skill-checklist-patched-run.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82S07Skill.md
