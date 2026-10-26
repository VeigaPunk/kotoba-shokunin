# ScoutSibKamaKasegiR74 — C2 sibling re-read: kama, kasegi

**Verdict:** both proposals equal r49 (`adjacent`/`adjacent`; no row moves). Nothing differs from r49 in class or basis; what changed is only the pin and the bytes around it (below). Basis differs between the lanes: kama is **sibling-stated** (its own corpus file), kasegi is **kotoba-stated only**.

All reads are committed bytes at the frozen heads (`git -C <lane>-shokunin show/grep <head40>`), never the working trees. Freeze rows: `kama master 3e6fdbe9… d87d6f74… d5518399…`, `kasegi master a155310d… 0e1b60d5… adf70152…`. Blob check: `git -C kama-shokunin ls-tree 3e6fdbe9… SKILL.md PROVINCE.md` → `d87d6f743f12… SKILL.md`, `d55183990675… PROVINCE.md` (equal to the freeze); `git -C kasegi-shokunin ls-tree a155310d… SKILL.md PROVINCE.md` → `0e1b60d5db5d… SKILL.md`, `adf701525640… PROVINCE.md` (equal). Both heads: `cat-file -t` = `commit`; r49 pins are ancestors (`merge-base --is-ancestor` → ancestor).

Deliverables: `.ufo/waves/round-74/w1/build/ScoutSibKamaKasegiR74/kama.json`, `…/kasegi.json` (full objects below).

## kama

Rule read (`corpus/knowledge/sibling-overlap-census-round49.md:43-60`, plus § Round 50 precedence `:246-262`): `contested` = sibling's scope surfaces claim part of kotoba's core; `adjacent` = either side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split; precedence: a claim makes it `contested` unless the sibling's own surfaces state a split assigning that element.

Sweep (all at `3e6fdbe9`):
- `git -C kama-shokunin grep -n -w -i kotoba 3e6fdbe9 -- SKILL.md PROVINCE.md` → no output (0 hits). `-i` without `-w` on those two files: exit 1.
- `git -C kama-shokunin grep -n -w -i kotoba 3e6fdbe9 -- . ':!LOG.md' ':!.ufo'` → 13 hits in 4 files: `MINT.md:20`, `MINT.md:42`, `corpus/knowledge/consumer-registry.md:91,92,332,342`, `corpus/knowledge/cross-lane-scope.md:6,13,14,29,32,41`, `corpus/knowledge/listener-census.md:63`.
- Deciding sentence (`git -C kama-shokunin show 3e6fdbe9:corpus/knowledge/cross-lane-scope.md | sed -n 29p`): `| A model/baseURL/fallback statement in an agent file versus truth about the service. | **Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of the target endpoint.` (cell continues; dropped: the janitor/distiller clause and path pointers).
- `MINT.md:42` (`sed -n 42p`): `| kotoba | prompt & skill craft | instruction surfaces, not services |`.
- Contested arm: `git grep -n -i -E 'AGENTS\.md|SKILL\.md|system prompt|dispatch prompt|agent file|instruction' 3e6fdbe9 -- SKILL.md PROVINCE.md` → 6 hits, all about kama's own SKILL.md/instrument text (`PROVINCE.md:97,113,135`; `SKILL.md:425,1091,1229`), none claims another lane's prompt/skill file. Registry rows `consumer-registry.md:91-92` label kotoba the owner (`` `kotoba` [INFERENCE] (agent-instruction surface) ``) and judge only endpoint facts/absences; `:56-57` records the agent directory as "Deleted since round 2". Per R50 reading ("reading or verifying a non-craft fact held in such text is not a claim") the arm does not fire.
- Unchanged-since-pin check: `git -C kama-shokunin diff --shortstat c808ba07… 3e6fdbe9… -- corpus/knowledge/cross-lane-scope.md MINT.md corpus/knowledge/consumer-registry.md` → empty (0 bytes), so the split sentence and rows are byte-identical to r49's pin. `git diff --shortstat c808ba07… 3e6fdbe9… -- SKILL.md PROVINCE.md` → ` 2 files changed, 417 insertions(+), 8 deletions(-)`; `rev-list --count c808ba07..3e6fdbe9` → 139.
- Mechanical columns: description (`sed -n 3p`) = `description: Domain specialist — local model serving & endpoint health — scopes local LLM endpoints, baseURL drift, model-id reconciliation. Rank: shonen.`; `grep -o -i -w` of the 18 lane names over it → none (names-kotoba `no`, arbitration `no`, matching r49's cells). `SKILL.md:8` still `Local model serving & endpoint health. This lane answers exactly one question:` (r49's quote is intact at the same line; this proposal quotes the description instead).
- Quote check: `sed -n 3p` of the blob piped to `grep -c '<quote>'` → 1. Quote 15 words, copied from `SKILL.md:3`, dropped: `description: Domain specialist — ` prefix and `. Rank: shonen.` suffix.

Decision: `adjacent`, clause 2, basis sibling (kama's own corpus file assigns the wording to kotoba). Class unchanged from r49 (basis `sibling`, R50 ruling).

```json
{
  "lane": "kama",
  "head40": "3e6fdbe9e0ca1ca5b633d0b312d5561301e924c4",
  "r49_classification": "adjacent",
  "r49_pin": "c808ba07f09c4be55413d3d6516c542ab69b64f8",
  "proposed_classification": "adjacent",
  "changed": "No. Class and basis unchanged. SKILL.md+PROVINCE.md grew 417+/8- with 0 kotoba hits; cross-lane-scope.md:29, consumer-registry.md:91-92 and MINT.md:42 are byte-identical to the pin (empty diff --shortstat); SKILL.md:8 still at line 8, this entry quotes the description at SKILL.md:3.",
  "skill_file": "SKILL.md",
  "quote": "local model serving & endpoint health — scopes local LLM endpoints, baseURL drift, model-id reconciliation",
  "quote_path_line": "SKILL.md:3",
  "kotoba_mentions": [],
  "boundary": "kama owns local model-serving endpoint identity and health (SKILL.md:8-9); its own corpus assigns agent-file model/fallback wording to kotoba (cross-lane-scope.md:29); kotoba owns instruction text, kama verifies the endpoint."
}
```
(The saved `kama.json` additionally carries `proposed_clause`, `kotoba_mentions_note` listing the non-scope-surface hits with kind, and `sweep`.) `kotoba_mentions` hits in kama's SKILL.md/PROVINCE.md: none. Kinds of the other-file hits: `MINT.md:42`, `cross-lane-scope.md:13,14,29,32` split; `MINT.md:20`, `cross-lane-scope.md:6,41`, `consumer-registry.md:332,342`, `listener-census.md:63` citation; `consumer-registry.md:91,92` claim-adjacent owner label.

## kasegi

Sweep (all at `a155310d`):
- `git -C kasegi-shokunin grep -n -w -i kotoba a155310d -- SKILL.md PROVINCE.md` → no output (0 hits); `-i` without `-w` also exit 1.
- `git -C kasegi-shokunin grep -n -w -i kotoba a155310d -- . ':!LOG.md' ':!.ufo'` → 4 hits, 2 files: `corpus/instruments/citation-survival.tsv:1025` (a `GONE` row for `kotoba-shokunin/corpus/knowledge/fleet-skill-audit-round5.md`), `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4,:6,:18`. Line 4: `- **Filed by:** kotoba round-5 report (2026-09-28), …`; line 5: `- **Mirrored by:** aggregator round-5 … Aggregator-owned file; the owning lane corrects SKILL.md.` These relay kotoba's own finding; they are not a sibling-stated split (r49's reading, re-derived: the text assigns nothing to kotoba).
- kasegi's own scope: `PROVINCE.md:43-52` § Adjacent lists `chousa`, `kagi`, `kake`, `kengaku` and `Live-target testing is refused; this corpus is documentation only.` — kotoba absent. `PROVINCE.md:24-25` Owns/Refuses are generic ("anything outside this domain").
- Contested arm negative sweep: `git grep -n -i -E 'audit.*(skill|prompt)|rewrite.*(skill|prompt)|AGENTS\.md|prompt[- ]craft|SKILL\.md of' a155310d -- SKILL.md PROVINCE.md` → 2 hits (`SKILL.md:986`, `:1071`), both about kasegi's own SKILL.md (cited-path audit; `score-gap.py` reporter), no claim over another lane's files. Description check: no lane name in `description` (`grep -o -i -w` over line 3 → exit 1): names-kotoba `no`, arbitration `no`.
- Kotoba side at base `1e03d19` (`git show 1e03d199…:SKILL.md | sed -n 8p` → `  reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate`, and the next line says they "own their own SKILL.md content — this skill audits and reports"). The kotoba-side clause of the rule is therefore still true at base; under R50 "a split stated only by kotoba may still make a row with no claim `adjacent`" → `adjacent`, basis kotoba. If the wave-2 seats read the rule as requiring a sibling-side split, this row would become `none` (the 0-kotoba-hit rule (e) would then pass); that is a rule-interpretation question for them, not a byte fact: r49 `Correction to § Classification rule`/basis line (`census-round49.md:284-290,325-326`) already answers it as basis `kotoba`.
- Delta: `git -C kasegi-shokunin diff --shortstat 1fafde8f… a155310d… -- SKILL.md PROVINCE.md` → ` 2 files changed, 72 insertions(+), 1 deletion(-)`; `rev-list --count 1fafde8f..a155310d` → 50. The one deletion is PROVINCE.md "Frontier F01–F08" → F01–F10 etc. (hunk `@@ -35,7 +35,10`); SKILL.md:3 description and PROVINCE.md:3 Domain are byte-identical to the pin (`sed -n 3p` at both revs equal).
- Quote check: `sed -n 3p` of `a155310d:SKILL.md` piped to `grep -c '<quote>'` → 1. 11 words, dropped `description: Domain specialist — ` prefix and `. Rank: shonen.` suffix. (`PROVINCE.md:3`, `**Domain:** bounty & security research — scopes ~/Projects/bounties, program rules, claim packages`, carries the same text.)

```json
{
  "lane": "kasegi",
  "head40": "a155310d1ee9aacc07c3ce62328105a46c0392b4",
  "r49_classification": "adjacent",
  "r49_pin": "1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a",
  "proposed_classification": "adjacent",
  "changed": "No. Class and basis (kotoba) unchanged. 72+/1- since the pin = frontier F09-F15 admissions in PROVINCE.md; SKILL.md:3 and PROVINCE.md:3 byte-identical; still 0 kotoba hits in SKILL.md/PROVINCE.md; PROVINCE § Adjacent still omits kotoba.",
  "skill_file": "SKILL.md",
  "quote": "bounty & security research — scopes ~/Projects/bounties, program rules, claim packages",
  "quote_path_line": "SKILL.md:3",
  "kotoba_mentions": [],
  "boundary": "kasegi owns bounty and security research (programs, rules, claim packages; SKILL.md:3) and states no split with kotoba; kotoba's own description names kasegi as owning its SKILL.md content while kotoba audits and reports."
}
```
(Saved `kasegi.json` additionally carries `proposed_clause`, `kotoba_mentions_note`, `sweep`.)

## Unobserved / caveats
- Did not run `check_sibling_census.py` or the future r74 counter (entry not built); quote location verified with `sed -n 3p … | grep -c` only.
- Did not re-read sibling working trees (by instruction). Router behaviour not observed (shokunin skills are outside omp discovery roots, per r49).
- Tooling installed: none.
