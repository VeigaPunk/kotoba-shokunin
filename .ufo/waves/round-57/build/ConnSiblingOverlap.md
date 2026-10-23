Result: DONE — scanned 20 sibling lanes read-only; no sibling claims the 7-client plugin-manifest ground (surface 1 = none across the board), and the only command/checklist instruments are the already-adjacent kagi checklist-run.sh and tameshi mutation cases on it (surface 2).

# Sibling-overlap scan — round 57 (ConnSiblingOverlap)

Leaf seat; no subagent dispatch. Read-only scans over `/home/vgpnk/Projects/shokunin/*-shokunin` (kotoba excluded). Classification per `corpus/knowledge/sibling-overlap-census-round49.md` § Classification rule and the round-50 precedence rule (contested only on a sibling scope-surface claim over an element of kotoba's `PROVINCE.md` § Core; adjacent on a stated split of one artifact/function/trigger area; none otherwise). Wave reports and run logs are not scope surfaces.

## Method

- Surface 1 (plugin manifests): `grep -rIl -i -E 'plugin\.json|claude-plugin|gemini-extension|marketplace\.json'` over each sibling's `SKILL.md`, `PROVINCE.md`, and `corpus/` (then narrowed to `SKILL.md`/`PROVINCE.md` for scope claims; incidental `corpus/` hits recorded separately). Plus `grep -in 'manifest'` over `SKILL.md`/`PROVINCE.md`.
- Surface 2 (command extraction gates): `grep -rIl -E 'command_binary_resolves|info-less fence|infoless|surface.probe|surface_probe|checklist.run|checklist-run'` over each sibling's scope surfaces, plus targeted `grep` for `checklist`/`command.*resolv`/`surface probe` in `SKILL.md` and `PROVINCE.md`.
- Census cross-check: `corpus/knowledge/sibling-overlap-census-round49.md` adjacent rows (kagi, kumitate, tameshi) and the kagi/tameshi split quoted there.

## Surface 1 — Plugin manifests by client

No sibling lane's `SKILL.md` or `PROVINCE.md` claims the 7-client plugin/extension manifest ground that kotoba's C1 table holds. The four incidental mentions below are substrate or upstream-artifact references, not scope claims, and none of them is a PROVINCE claim:

| lane | file:line | what it is | PROVINCE claim? |
|---|---|---|---|
| game-dev-3d | `SKILL.md:47` | `.claude-plugin/plugin.json` appears inside a vendored upstream (unreal-mcp) byte-identity command (`jq -e . upstream/.claude-plugin/plugin.json …`); verifies upstream bytes, not a client manifest table | no |
| tabi | `SKILL.md:64,581,672,1372,1418` | `kimi.plugin.json` of the kimi-webbridge plugin substrate; tabi owns that plugin (`PROVINCE.md:6`) | no — different client (kimi), different artifact |
| kumitate | `corpus/knowledge/kimi-skills-plugins.md` | Kimi Code CLI `~/.kimi-code/plugins/installed.json` installation manifest; Kimi-only, no `.json` manifest per skill | no |
| kagi | `PROVINCE.md:30,43` | a global opencode plugin file (`~/.config/opencode/plugin/fnm-nudge.js`) and a 1Password native-messaging manifest pin | no — single global file, not a client plugin-manifest table |

Classification: **none** for all 20 siblings on this surface. There is no stated split and no claim on kotoba's § Core, so neither `adjacent` nor `contested` fires. No routing to the integrator is required for C1; the new table does not collide with any sibling's owned ground. (If a later round extends plugin manifests to kimi, coordinate with tabi/kumitate at that point — not this round.)

## Surface 2 — Command extraction / checklist instruments

Kotoba's C2 is withdrawn this round (no writes to `verifiers/verify_skill_checklist.py`), so no contradiction arises from C1; this is an alignment scan for the eventual C2 redesign.

- **kagi** — owns `corpus/checklist-run.sh` + `corpus/checklist.tsv` over its own `SKILL.md` checklist (16 items). Census row: **adjacent** — kagi pins the bytes, kotoba owns the checklist/shape reading (`kagi corpus/README.md:97`). Evidence: `kagi-shokunin/corpus/README.md:33-35`.
- **tameshi** — owns mutation cases on kagi's `checklist-run.sh` (`corpus/knowledge/mutation-case-kagi-checklist.md`, 15 defects, 7 killed / 8 survived). Census row: **adjacent** (tameshi `PROVINCE.md:14-18`: every lane's gate remains its own). Evidence: `tameshi-shokunin/corpus/knowledge/mutation-case-kagi-checklist.md:1,21,130`.
- **kumitate** — owns `scripts/surface-probe.mjs` and the live-surface-probe knowledge, but its `PROVINCE.md:27` routes "Prompt and skill craft → kotoba"; it is not a command-resolution instrument over kotoba's `SKILL.md`. Census row: **adjacent** on orchestration/surface probe, not on command extraction.
- **kasegi** — its "checklist" references are per-program submission checklists for bounty claims (`SKILL.md:54,167,550`); no command-extraction or checklist instrument targeting kotoba. Classification: **none**.
- All other siblings — sweep over `SKILL.md`/`PROVINCE.md` for `command_binary_resolves`, `info-less`/`infoless`, `surface.probe`/`surface_probe`, `checklist-run`/`checklist.run` returned no instrument. Classification: **none**.

Classification summary: kagi and tameshi **adjacent** (command/checklist instruments, already recorded in the census); kumitate **adjacent** (existing row, different surface); all others **none**.

## Route to integrator

1. No change needed for C1: no sibling ground is contested or adjacent on plugin manifests; no integration action beyond kotoba's own C1 landing.
2. For the eventual C2 (info-less fence command extraction), the redesign must preserve the kagi split — kagi pins bytes, kotoba owns checklist/shape reading — and be measured against tameshi's mutation-case kill rates before admission. C2 is withdrawn this round, so this is a forward constraint, not a current contradiction.
3. C1's new backticked manifest paths (e.g. `.claude-plugin/plugin.json`) are not heads in the declared command vocabulary and do not begin with `corpus/`/`verifiers/`/`opencode/`/`.ufo/`/`../`, so they should not register as command or citation subjects in kotoba's own checklist gate; confirm with the lane's checklist run after integration (not run here).
4. No `contested` rows arise from either surface; nothing to escalate beyond the existing integrator items already recorded in the census (kaidoku/revenger reverse-engineering overlap, kagi opencode-config ownership).