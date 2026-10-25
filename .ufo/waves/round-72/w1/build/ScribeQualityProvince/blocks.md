# Round 72 — append-only draft blocks (ScribeQualityProvince)

Three blocks drafted for later landing by the L1. None are written to the lane.
Result values are left as `<<…>>` placeholders — wave-2 counts are not known at wave-1 build time.
Style matched to the existing append-only text at `PROVINCE.md:28-29` and `corpus/README.md:152-216`.

---

## Block 1 — PROVINCE.md § Core bullet (append after the round-68 bullet at `PROVINCE.md:29`)

- Author-facing rules reach the audit checklist (round 72, sourced): the four rules an executing agent can act on in `SKILL.md` § Trigger-fidelity checklist — name uniqueness (`corpus/knowledge/skill-name-precedence-round69.md`, S203–S207), authority level (`corpus/knowledge/instruction-authority-ladder-round67.md`, S123 and S129), install-path trust (`corpus/knowledge/client-trust-gates-round68.md`, S198–S202 and S208) and the resident-index-vs-on-demand rung (`corpus/knowledge/resident-index-and-rungs-round72.md`, rows opened this round) — counted by `verifiers/check_author_rules.py --rev <rev>` (`author-facing rules in SKILL.md <<N>> of 4`); host substrate census counted by `verifiers/check_substrate_repin_v2.py --rev <rev>` (pins OK <<k>>/3; surfaces pass <<p>> of 7; removal ledger <<l>> of <<l>> verified); tip battery counted by `verifiers/check_tip_battery.py --rev <rev>` (`tip battery exit 0: <<N>> of 6`).

---

## Block 2 — corpus/README.md § Frontier note (append after the round-60 note at `corpus/README.md:216`, before `## Known gaps`)

**Round 72 (append-only note on the loader-rule row above; new frontier lead):** *Loader-rule freshness* — the host substrate drifted and the re-pin is the round's C2 build work: the omp half is a path move onto `omp.real` (the `~/.local/bin/omp` wrapper is a 1,680-byte crash-restart script installed 2026-10-23; its real binary `~/.local/bin/omp.real` is byte-identical to the round-51 pin — sha256 `85d9daf3…`, ns-exact mtime 2026-10-21T20:37:24.615549837-03:00), while the opencode half is a new lineage — v2.1.4 at `~/.opencode/bin/opencode` (the dump carries `2.1.4` and no `1.19.4`; the literal `CONTEXT.md` is absent from the v2.1.4 dump) — so the loader rules OC-1…OC-6 must be re-derived on it. The re-pinned host is checked by `../verifiers/check_substrate_repin_v2.py --rev <rev>` (`host substrate re-derived: pins OK <<k>>/3; surfaces pass <<p>> of 7; removal ledger <<l>> of <<l>> verified`). Still not held: re-derivation stays manual, and the v2.1.4 extraction read pending the Q45 population census. **New frontier lead:** `SKILL.md` is measured in lines only — 600 lines / 72,688 B at base `c69711e` against the specification's activation guidance (~5,000 tokens under, per S256, to be confirmed by the source seats) — and the Gate-registry block is ~17 KB (~24%) of the file; the considerthese 2026-10-25 proposals 1 (byte ceiling) and 2 (registry relocation) stay leads, not worked this round (one considerthese item per round).

---

## Block 3 — SHONEN.md evidence-line pointers for the round-72 report (updates NOT written; SHONEN is operator-owned form)

- Box 1 (decision tables / error patterns / checklists / cited sources): `python3 -B verifiers/check_author_rules.py --rev <rev>` → `author-facing rules in SKILL.md <<N>> of 4`; tip SKILL.md lines/bytes at `<rev>`; `python3 -B verifiers/check_gate_registry.py --rev <rev>` (conformant row count).
- Box 2 (end-to-end domain task executed and logged): the base battery receipt (`.ufo/waves/round-72/receipts/base-battery.txt`, measured-rev `c69711e`) vs the tip battery receipt committed at the measured tip; the round-72 LOG.md entry (`corpus/lessons/round-72.md` § Gate).
- Box 3 (instructions executable without oral context): the C1 counter's `--self-test` and the shortcut-control bundles committed before data, showing the four rules are machine-checkable; no fresh non-author cold run this round (box remains `[~]`).
- Box 4 (no cross-domain bleed): `python3 -B verifiers/check_province_core.py --rev <rev>` after the § Core bullet lands, plus the `^## Adjacent` re-grep and `check_sibling_census.py`.
