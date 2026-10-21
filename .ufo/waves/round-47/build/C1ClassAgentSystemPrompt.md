verdict: EXISTS — `omp:agent-system-prompt/SYSTEM.md` still has five live provider registrations in omp 18.12.5 (native/`.omp`, claude, agents, codex, gemini); the row's checker is a substring-only PASS, and the census's quoted gemini call shape is stale (sibling rows, not this row).

# C1 per-class witness — omp `agent-system-prompt` family

Lane repo BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (scratch clone
`/fast/scratch/kotoba-r47/C1ClassAgentSystemPrompt-9/lane`, detached at that sha; `git rev-parse HEAD` exit 0).
Substrate: frozen snapshot `/fast/scratch/kotoba-r47/shared/`, verified read-only.

## 1. Baseline rows in scope

| Source | Line(s) | Entry |
|---|---|---|
| `verifiers/surfaces-baseline.json` | 139–143 | `omp:agent-system-prompt/SYSTEM.md`, harness `omp`, literal `SYSTEM.md`, `loader-literal`, `governed` — the ONLY class id starting `omp:agent-system-prompt` (index 19 of 38 classes) |
| `corpus/knowledge/instruction-surface-census-round13.md` | 99 | family row; cites the per-provider registry strings plus `~/.omp/agent` + nearest `<ancestor>/.omp` as second witness §3 |
| `verifiers/surfaces-baseline.json` | 34, 41 | sibling family rows `omp:gemini/system.md` (loader-group) and `omp:gemini/SYSTEM_TEMPLATE.md` (loader-group) — checked because they are loader rows for the same filename family |
| `verifiers/verify_surfaces.py` | 61–67, 508–534 | `loader-literal` contract: literal must occur in the dump; no call shape required. Probe is `e["literal"] not in dump` (substring) |

Snapshot integrity (exit 0): `sha256sum -c SHA256SUMS` → all four `OK`;
`bin/omp-18.12.5 --version` → `omp/18.12.5` (exit 0).

## 2. Registration evidence in omp 18.12.5

All dump lines below are `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` (`strings -n 4`).

Capability definition (the object every registration keys on):
- 892241 `// packages/coding-agent/src/capability/system-prompt.ts`
- 892242 `var xy = Jo({`
- 892243 `id: "system-prompt",`
- 892245 `description: "Custom system prompt files (SYSTEM.md, SYSTEM_TEMPLATE.md) that modify agent behavior",`

Five `Le(xy.id, { id: <provider>, ..., load: <fn> })` registrations (grep `Le\(xy\.id` → 5 hits):

| # | Registration (dump lines) | Provider id | Registry description (verbatim) | Loader + file call |
|---|---|---|---|---|
| 1 | 896220–896226 | `Pr` = `"native"` (896038), displayName `Mo` = `"OMP"` (896039) | 896223 `Custom system prompt from SYSTEM.md and SYSTEM_TEMPLATE.md` | `xZ` (896200–896219): 896215 `sr.join(M.dir, "SYSTEM.md")` with `M = await dR(u)` (896213); 896217 `sr.join(Se(), "SYSTEM.md")` |
| 2 | 897233–897239 | `mi` = `"claude"` (896820) | 897236 `Load system prompt from .claude/SYSTEM.md` | `Dee` (897111–897145): table 897116–897117 `["SYSTEM_TEMPLATE.md","template"], ["SYSTEM.md","text"]`; project `Ir.join(T,I)` with `T = ym(u)` (896834–896836, `gm = ".claude"` 896823), user `el(u)` (896829–896833, claude config dir) |
| 3 | 897972–897978 | `jo` = `"agents"` (897787) | 897975 `Load SYSTEM.md and SYSTEM_TEMPLATE.md from .agent and .agents (project walk-up + user home)` | `vte` (897958–897971): 897966 `Gj(u,"SYSTEM.md")` project walk-up, 897968 `Uj(u,"SYSTEM.md")` user home; `HO = [".agent",".agents"]` (897786), `Gj` 897840–897850, `Uj` 897838–897839 |
| 4 | 898671–898677 | `ti` = `"codex"` (898296) | 898674 `Load SYSTEM.md and SYSTEM_TEMPLATE.md from .codex (project cwd + user home)` | `Nte` (898654–898670): 898667 `Yr.join(T,"SYSTEM.md")` with `T = nl(u) = join(cwd,".codex")` (898299–898300); 898669 `Yr.join(M,"SYSTEM.md")` with `M = ua(u)` = `~/.codex`, provider-gated (898301–898305) |
| 5 | 898997–899003 | `mo` = `"gemini"` (898802) | 899000 `Load system.md custom system prompt files` | `zte` (898982–898996): 898993/898995 lowercase `system.md` text (project/user) via path helpers `Fo` (862510–862514) / `Xl` (862506–862509, gate `Ii` then `nLe` 862497–862505); 898992/898994 `SYSTEM_TEMPLATE.md` template |

Path semantics for the row's own claim:
- Project `.omp`: `vu.projectDir = fO.native.projectDir` (896042); `fO.native` block 862444–862452; `Jf = ".omp"` (644414). `dR` (896088–896093) walks `xOe` (896080–896086) → `TBt` (896061–896079) from cwd up to `u.repoRoot ?? u.home`, and returns the first directory with a non-empty `.omp` subdir (`cR` 896043–896051). So "nearest `<ancestor>/.omp`" is code-confirmed.
- User agent dir: `Se()` (644704–644706) returns `L.agentDir`; `M` constructor sets `agentDir = configRoot/agent` (644571–644574); `configRoot = T(profile)` (644440–644443) and `T` → `L7()` (644438–644439) → `join(homedir(), Zf())` (`Zf` 644556–644558, `Jf=".omp"` 644414). Default no-profile path is therefore `~/.omp/agent`; with `OMP_PROFILE`/`PI_PROFILE` it is `~/.omp/profiles/<p>/agent` (`m0` 644448–644449, profile resolver `y3` 644422–644430). [Observed from code; not executed.]

Conclusion: the family still exists; every description the census quotes at line 99 is present at 896223, 897236, 897975, 898674, 899000 (the census adds markdown backticks around path tokens; the registry strings themselves carry none), and the `.omp` variant that the census carried only as "second witness §3" is a first-class registry entry at 896220–896226 in 18.12.5.

## 3. Machine check on this row (scratch clone, BASE)

- `python3 -B verifiers/verify_surfaces.py --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --check surfaces.literal_present --json` → **exit 1**, 8 unreachable loader literals. `omp:agent-system-prompt/SYSTEM.md` is **not** in the failure list; the 8 are `omp:agents-md/AGENTS.md`, `omp:claude-md/CLAUDE.md`, `omp:opencode/AGENTS.md`, `omp:gemini/GEMINI.md`, `omp:gemini/system.md`, `omp:gemini/SYSTEM_TEMPLATE.md`, `omp:github/copilot-instructions.md`, `omp:windsurf/memories/global_rules.md`.
- Isolated row probe in the same clone: `check_literal_present([row])` → `(True, '1 loader-kind entry verified against the dumps')`; mutated literal `SYSTEM.md.ABSENT` → `(False, "... not verifiable ...")`. The declared check is live for the row but proves only substring presence.
- `extract_classes(dump, 'omp')` → **0 pairs total** (0 SYSTEM pairs). The 18.12.5 minification has renamed/dropped every `(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(v, group, "*.md")` shape; the system-prompt family was never in that shape anyway — its registration form is `Le(<capability>.id, { id: <provider>, description, load })`.

## 4. Counterexamples / calibration notes

1. **Substring weakness (row-level).** The literal probe is `e["literal"] not in dump`. `SYSTEM.md` also occurs inside `APPEND_SYSTEM.md` (526567, 1200766, 1200769) and `TITLE_SYSTEM.md` (541902, 1069218, 1069221, 2422923) and the bundled docs/registry index (557624, 557892, 557958, 557979, 557990). Demonstrated `'SYSTEM.md' in 'APPEND_SYSTEM.md'` → True. A vanished family would still pass this row's machine check; the human witness in §2, not the checker, is what establishes existence. (These extra names are separately excluded at census line 238.)
2. **Stale sibling call shape.** Census line 78 quotes `Cl(e,"gemini","SYSTEM_TEMPLATE.md")`. `grep -n -E 'Cl\([^)]*"gemini"' omp-18.12.5.strings` → **exit 1, 0 hits**. In 18.12.5 the gemini SYSTEM files are path-helper loads (`Fo(u,"gemini",...)` / `Xl(...)`, 898992–898995), not registration calls. Under the baseline's loader-group contract both `omp:gemini/system.md` and `omp:gemini/SYSTEM_TEMPLATE.md` FAIL (confirmed in the 8-failure detail above). The `omp:agent-system-prompt/SYSTEM.md` row is `loader-literal`, so it is not implicated; any re-verdict belongs to those two sibling rows.
3. **`.omp` evidence upgraded, not lost.** Census line 99 attributes `~/.omp/agent` + nearest `<ancestor>/.omp` to second witness §3; 18.12.5 carries it as registry entry 896220–896226 (`native`/`OMP`, loader `xZ`) with the walk-up (896080–896093) and agent-dir (644438–644442, 644556–644558, 644704–644706) code. Not proof it existed in earlier versions — I did not diff older dumps.
4. **Profile caveat.** "`~/.omp/agent`" is the default-profile path. With `OMP_PROFILE`/`PI_PROFILE`, `T` resolves `~/.omp/profiles/<p>` first (644440–644444). The census sentence is accurate for the default only.
5. **No fabricated call shape.** No allowlisted callee (`Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo`) forms a SYSTEM.md registration call in 18.12.5 (extraction set empty); the family's registration form is `Le(<capability>.id, { id: <provider>, ... })`. Declaring the row `loader-literal` remains consistent with the substrate; do not re-kind it to `loader-group` on this evidence.

## 5. What I did NOT check

- No runtime execution of any loader; the strings dump is static and proves compiled-in paths, not that they fire or reach a prompt.
- Did not decode helper predicates `vZ`, `zfe`, `El`, `Ii`, `Ue`, `Ot` beyond their one-line roles; the `.omp` walk's skip rules are cited from `xOe` source, not exercised.
- Did not inspect older substrate dumps (18.12.2/18.12.3) to date the native registry entry, so "new in 18.12.5" is not claimed.
- Did not run the remaining surfaces checks (`table_parity`, `literal_parity`, `kind_parity`, `excluded_reason`, `no_uncovered_class`, `opencode_extract`) or any lane-wide gate in the fleet root; only the isolated `literal_present` path in my scratch clone.
- Did not read host `~/.omp`, `~/.claude`, `~/.codex`, `~/.gemini` contents (host-private and irrelevant to the substrate witness).
- No production files touched, no patch produced (witness only), no tools installed/updated.
