Result: MIXED — the census rows and hook-config paths survive scrutiny (no sibling lane or older kotoba corpus contradicts them factually), but the landed SKILL.md section and entry do not state the three scopes, so an unscoped reading collides with `plugin-manifests-round57.md` and `instruction-surface-census-round13.md`.

## Evidence

- Landed section (commit `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, `SKILL.md` lines 121-133, "### Hook files by client"): rows name client hook-config files (`.claude/settings.json`, `~/.codex/hooks.json`, `.github/hooks/*.json`, `~/.copilot/hooks/*.json`, `.gemini/settings.json`, `.cursor/hooks.json`, opencode "no hook file"). The header says only "writing or running hook code is out of scope (round-13 census)"; it does not say the rows are client *config-file* paths rather than plugin-bundled or omp-discovered hook surfaces.
- Landed entry (same commit, `corpus/knowledge/hook-files-round59.md`): "Scope boundary (province)" covers authoring/running hook code and tsukuroi host hooks, but has no scope sentence separating client config file vs. plugin-bundled `hooks/hooks.json` vs. omp executable roots.
- Kotoba older corpus that an unscoped reader could read as contradicting:
  - `corpus/knowledge/plugin-manifests-round57.md:54-59` (commit `bc09a8307f253fafca3f1461bcc45627d7b6eea7`): every census client "ships hooks" as a plugin component, e.g. Gemini "hooks (in `hooks/hooks.json`, not in the manifest)", Cursor "discover … `hooks/hooks.json`", Claude/Codex/VS Code/Copilot "hooks". These are plugin-bundled surfaces, not the client config files the new rows name.
  - `corpus/knowledge/instruction-surface-census-round13.md:265` (commit `e792607e85c78998bbf0ae4e2b5d350683eec0f7`): "Extension/hook/tool module roots (`.gemini/extensions`, `.codex/tools`, `.claude/hooks`) — executable surfaces, out of prompt-craft province." `.claude/hooks` is an omp-discovered executable root, distinct from `.claude/settings.json`.
  - `corpus/knowledge/instruction-surface-census-round13.md:283` (same commit): opencode's plugin `experimental.chat.system.transform` hook is a non-file prompt surface. The landed opencode row lists only `execute.before` / `execute.after` tool-execution events, so an unscoped reading understates the hook vocabulary.
- Sibling lanes (read-only): no client hook-config path or event token appears in any sibling `corpus/` except:
  - `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/README.md:25,50` (commit `366bb02f87a2557d54bc5c5e4d817c45ccf67a9a`): plugin-bundled `hooks/hooks.json` + `SessionStart` bash script; consistent with the census plugin scope, not a client config file.
  - `kumitate-shokunin/corpus/knowledge/kimi-modes-machinery.md:148,152,423,485` (commit `364f1d5954158ef8844bca4a5fef57b05d2f2ca5`): omp's own `.omp/hooks/pre/…`; omp is not a census client, so this is an adjacent mechanism, not a missing row.
  Neither contradicts the census paths once scope is stated.

## Affected axes

- Adjacency / consistency: the census rows themselves are consistent with the vendor pages and with the older corpus, but the landed artifacts do not make the three scopes explicit, so a reader can derive false contradictions (Gemini plugin `hooks/hooks.json` vs. `.gemini/settings.json`; Claude `.claude/hooks` executable root vs. `.claude/settings.json`; opencode prompt-transform hook vs. tool-execution events).
- Depth: no factual correction to paths or events is required; the defect is documentation adjacency, not data.

## Proposed move

Add one scope sentence to both landed artifacts (SKILL.md section header and the entry's "Scope boundary"): the rows name each client's hook *config file*; plugin-bundled hooks live in the plugin's `hooks/hooks.json` per `corpus/knowledge/plugin-manifests-round57.md:54-59`; omp's own hooks live under `.omp/hooks/` (sibling lane kumitate); `.claude/hooks` is an omp-discovered executable root per `instruction-surface-census-round13.md:265`, not the config file; and the opencode row covers tool-execution hooks only and does not exhaust the prompt-transform hook at `instruction-surface-census-round13.md:283`. No row path or event should change.

## Risks

- If the scope sentence is omitted, a falsifier can read the Gemini row as denying `hooks/hooks.json` in extensions, or the Claude row as denying `.claude/hooks` as an executable root, producing a false contradiction with `plugin-manifests-round57.md` and `instruction-surface-census-round13.md`.
- If the opencode row is read as the complete hook vocabulary, it understates the prompt-transform hook documented at `instruction-surface-census-round13.md:283` and `plugin-manifests-round57.md:60`.
- The opencode row cites the v2 plugin API (`execute.before` / `execute.after` from S085); sibling `kagi-shokunin` records the v1-style key `tool.execute.after`. These are version-scoped and do not contradict, but the row should name the API version to prevent confusion.

## Verification

- Sibling-lane search: `grep -rn` for client hook-config tokens and event names across `*-shokunin/corpus` (excluding `kotoba-shokunin`) returned matches only in `game-dev-3d-shokunin` (plugin scope) and `kumitate-shokunin` (omp scope), cited above.
- Kotoba citations verified by `nl -ba` on `plugin-manifests-round57.md` and `instruction-surface-census-round13.md` at the commits cited.
- Counter run (read-only, no fetch): `python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a` → `hook files backed on committed snapshots 6 of 6; live not run; new ground 0`, counter sha256 `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`, exit 0, with `reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client` (expected, by design).