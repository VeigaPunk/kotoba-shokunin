Result: DONE — the round's agent-definition surface is held almost entirely by kotoba itself; the only sibling-held evidence on the seven clients' paths is kumitate's omp-side exclusion of `.claude/agents`, `.codex/agents`, `.gemini/agents`, alongside sibling-owned omp/Kimi card families and one unresolved kagi parent-path row; the drafted "Cross-domain evidence encountered" item is ready to paste.

# ConnSiblingOverlap — cross-domain evidence for the agent-definition surface (round-55 routed defect 7)

Advisory connector report for kotoba round 56. It is not a C1/C2 verdict and not an integration.
No counter, SKILL.md, entry, SOURCES row, sibling file or map disposition was touched. The only
file written is this one. Nothing was executed: no lane code, counter, self-test or runtime; no
sandbox clone was needed; no tool was installed; no process remains.

## Scope and method

Target (assignment): scan sibling lanes read-only for agent-definition files, subagent rosters,
`.claude/agents`, `opencode/agents`, `.github/agents` and agent-card craft, focused on kumitate
(dispatch runtime), kama (agent files and model wording split), kagi, tameshi, kengaku; report each
overlap with path:line at the sibling's current HEAD; classify kotoba-owned / sibling-owned /
contested; draft the round-56 report's cross-domain item.

Commands used (read-only; cwd `kotoba-shokunin/`; scan run 2026-10-23, HEADs read at the
`date -u` line below):

- `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/<lane>-shokunin rev-parse HEAD`
- `git --no-optional-locks -C <lane> ls-files | grep -iE 'agent'`
- `git --no-optional-locks -C <lane> grep -n -I -E '<path patterns>' HEAD -- <surfaces>` (HEAD-scoped, so working-tree dirt cannot move a cited line)
- fleet-wide `git grep -l -I -E '\.(claude|codex|gemini|cursor|github|copilot)/agents' HEAD` over all 21 `*-shokunin` lanes (and separately `\.github/agents|\.copilot/agents`, and the kimi/omp card family)
- read-only `ls` of host/fleet agent-card directories; `date -u` → `Fri 23 Oct 2026 02:50:13 AM UTC`

This is a lane-corpus sweep at each lane's HEAD, not a docs/release/source-tree silence sweep
(Q30): a negative below means "not found in the lane tree at that HEAD", never "the client is
silent".

## Sibling HEADs at scan time (kotoba `PROVINCE.md` pin in brackets)

| lane | HEAD (observed) | kotoba pin | moved? |
|---|---|---|---|
| kumitate | `3632602c6f68945ce973043f6d47bf3990afff13` | `fac39171ac28c606e90da75fc2ba2ed3df52f4ea` | yes |
| kama | `1560e4d83f42b04f40336357de6f9637eafa0f4b` | `c808ba07f09c4be55413d3d6516c542ab69b64f8` | yes |
| kagi | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | no |
| tameshi | `9bb699ad2d9f795dff95df85eb967129c54927d6` (moved from `7a45f7b9d6a2542a553276330c8b02ac2e28c7ef` mid-scan) | `3b20f073c7305a582562cd323982991464c324f3` | yes |
| kengaku | `1f3b0f1ec41ec297130e8944ff97968d32324632` | `1f3b0f1ec41ec297130e8944ff97968d32324632` | no |

Pin drift is an observation, not a gate claim. The boundary line kotoba's PROVINCE row quotes for
kumitate (`PROVINCE.md:27`) and the split kama states (`cross-lane-scope.md:29`) both still read as
pinned at these HEADs. Working-tree note: kagi has ` M corpus/claim-ledger.tsv`, ` M
corpus/lessons/round-28.md` and an untracked `corpus/__pycache__/`; all kagi lines below are
HEAD-scoped. tameshi has an untracked `corpus/lessons/round-29.md`.

## Overlaps, path:line at the sibling's current HEAD, classified

### kumitate @ `3632602c` — dispatch runtime

| path:line @ HEAD | what it holds | classification |
|---|---|---|
| `corpus/knowledge/omp-task-contract.md:168` | "Direct `.claude/agents`, `.codex/agents`, and `.gemini/agents` roots are excluded; their schemas are not OMP task-agent definitions." | kotoba-owned (client-side location claim) / kumitate-owned (omp runtime side) — compatible split, no contest |
| `corpus/knowledge/omp-task-contract.md:174` | S003 quote: "Direct cross-harness roots such as `.claude/agents`, `.codex/agents`, and `.gemini/agents` are intentionally skipped" | same |
| `corpus/knowledge/omp-task-contract.md:160-167` | omp's own agent-discovery precedence: nearest project `.omp/agents`, user `.omp/agents`, extension roots, Claude marketplace roots, bundled | kumitate-owned (omp client is not one of C1's seven) |
| `corpus/knowledge/kimi-lane-definitions.md:5` | `~/.kimi-code/agents/secondary/` holds 18 agent markdown files | sibling-owned (Kimi substrate dispatch) |
| `corpus/knowledge/kimi-lane-definitions.md:28-32` | agent-file frontmatter fields (`name`, `description`, `whenToUse`) | sibling-owned; kotoba craft rules would apply if Kimi entered the checklist |
| `corpus/knowledge/kimi-lane-definitions.md:248-252` | S012: Kimi docs § Agent Locations — "more specific scopes take higher priority: Explicit (--agent-file) > Project > Extra > User > Plugin > Built-in"; recursive `.md` scan | sibling-owned |
| `SKILL.md:331`; `corpus/knowledge/native-judge-pipeline.md:131` | "agent cards" are members of the 66-file native contract-hash registry | sibling-owned (dispatch runtime); kotoba's own census declares the omp roster ungoverned (`kotoba-shokunin/corpus/knowledge/instruction-surface-census-round13.md:497-500`) |
| `corpus/knowledge/remaining-scripts-census.md:594-596` | `scripts/project-devin-subagents.mjs` projects the `devin-native-v1` seat profiles from canonical `agents/*.md` cards plus `config/ufo.json` | sibling-owned (fleet agent-card family; cards live in the origin repo, `SKILL.md:7`) |
| `PROVINCE.md:27` | "Local model serving and endpoints → kama. Prompt and skill craft → kotoba." | sibling-stated route to kotoba; supports all kotoba-owned classifications above |

### kama @ `1560e4d8` — agent files and model wording split

| path:line @ HEAD | what it holds | classification |
|---|---|---|
| `corpus/knowledge/cross-lane-scope.md:29` | "**Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of the target endpoint" | kotoba-owned (by kama's own statement) |
| `corpus/knowledge/cross-lane-scope.md:41` | kama's report-out: janitor.md's no-fallback 8080 statement and distiller.md's cascade "are agent surfaces for kotoba" | kotoba-owned |
| `corpus/knowledge/consumer-registry.md:91-92` | consumer rows for `~/.config/opencode/agents/janitor.md` and `distiller.md`, owner cell `kotoba [INFERENCE] (agent-instruction surface)` | kotoba-owned (marked as kama's inference, not a kotoba citation) |
| `corpus/knowledge/consumer-registry.md:56-57` | `~/.config/opencode/agents/` listed among consumer files "Deleted since round 2" | sibling-owned record; host-verified live below |
| `SKILL.md:99-100`; `PROVINCE.md:11`; `MINT.md:42` | historical janitor/distiller model pins; "kotoba | prompt & skill craft | instruction surfaces, not services" | kotoba-owned / historical |

### kagi @ `899c50b4` — secret/credential side of the same opencode agent file

| path:line @ HEAD | what it holds | classification |
|---|---|---|
| `PROVINCE.md:28` | `~/.config/opencode/agents/janitor.md` — `steps: 4`, `permission: {"*": deny, janitor_auth: allow}` | sibling-owned (credential isolation byte/contract pin) |
| `corpus/drift-baseline.tsv:7`; `corpus/surface-census.tsv:27`; `corpus/checklist.tsv:37` | byte sha pin; asset row "agent contract: steps 4, permission deny ceiling"; runnable H4 that parses the frontmatter permission block | sibling-owned (kagi instrument over the file) |
| `corpus/knowledge/config-layering.md:21` | "markdown agent | `~/.config/opencode/agents/janitor.md` | global agents dir | yes — frontmatter overrides the whole `agent.janitor` object from JSON layers" | sibling-held fact about what an opencode agent file sets; kotoba-owned shape reading |
| `corpus/README.md:96` | `$HOME/.config/opencode` row: "**`unresolved`** — no fleet artifact names a single owner (24/14/9/2 files in kotoba/kama/kengaku/kumitate); … ruling owed to the integrator" | **contested** (kagi's own census; report as-is, do not rule) |
| `corpus/README.md:97` | `$HOME/.agents/AGENTS.md`: "kagi pins its bytes; kotoba owns the checklist/shape reading" | kotoba-owned (shared-read, declared) |

### kengaku @ `1f3b0f1e` and tameshi @ `9bb699ad` — no agent-definition surface

| path:line @ HEAD | what it holds | classification |
|---|---|---|
| kengaku `PROVINCE.md:30`, `:138` | kotoba owns prompt- and skill-craft rules; kengaku keeps only measured capability effects | sibling-stated split; no file surface overlap |
| kengaku `corpus/evidence/round9-fleet/sweep.tsv:130`; `corpus/lessons/round-4-aggregator-audit.md:65` | historical echo rows for `~/.config/opencode/agents/janitor.md` | none (historical reference only) |
| tameshi — no current-surface hit at either observed HEAD | only `AGENTS.md` (its own always-on file); the 14 matches at `7a45f7b9` are all `.ufo/` wave evidence quoting kagi's asset (e.g. `.ufo/waves/round-29/w1/BuildF6B.md:226`; `.ufo/evidence/round-29/f6/original/host.tsv:7`); at `9bb699ad`: 0 current-surface matches | none |

### Fleet-wide (beyond the named five), same sweep

- kasegi @ `1fafde8f`: `SKILL.md:369` — every non-k3 lane has exactly one `.omp/agents/kx-<lane>.md` card (registry bijection, `ops/registry-check.mjs:57-80`). Sibling-owned agent-card family.
- souji @ `4edb25df`: `census/round-1/census.tsv:119` — the fleet root `/home/vgpnk/Projects/shokunin/.omp` holds a single tracked file `.omp/agents/executor.md`. Sibling-owned record.
- game-dev-3d @ `89dd182b`: `reports/round-101/probes/kimi-surfaces.md:614` — subagent profiles at `~/.kimi-code/agents/<set>/*.md`, `--agent-file`, plugin `agents`. Sibling-owned.
- `.github/agents` / `.copilot/agents`, fleet-wide at HEAD including `.ufo/`: the **only** tree containing these strings is kotoba's own (`plans/round-56.md`, `verifiers/check_agent_definitions.py`, `.ufo/waves/round-56/controls-call.json` and `controls/*`). Kotoba is sole claimant; no sibling evidence and therefore no cross-lane cross-check for C1's VS Code / Copilot CLI rows.
- Client-path sweep `\.(claude|codex|gemini|cursor|github|copilot)/agents` over current surfaces, all 21 lanes: only kotoba (its round-56 plan/counter) and kumitate (`omp-task-contract.md`). No other lane holds any of the seven clients' agent-definition paths.

### Host facts observed read-only (2026-10-23, relevant to all rows above)

- `~/.config/opencode/agents/` does not exist (`ls` → "No such file or directory") — kama's deletion record is live-confirmed; the opencode agent files kama/kagi/kotoba describe are historical.
- `~/.omp/agent/agents/` holds 13 `.md` cards (connector … simplifier, mtimes 2026-10-08) — kotoba's round-13 count was 37 (`instruction-surface-census-round13.md:498-500`).
- `/home/vgpnk/Projects/ufo-fsd-alpha/agents/` holds 13 cards (2026-10-03) — the canonical `agents/*.md` family kumitate's census names.
- `/home/vgpnk/Projects/shokunin/.omp/agents/` holds one project-local card, `executor.md` (1606 B, 2026-10-14).

## Drafted item for the round-56 report (`.ufo/reports/round-56/kotoba.md`)

Ready to paste; every pointer below is at the sibling HEAD named here, not at the stale PROVINCE pin.

> **Cross-domain evidence encountered** (round-55 routed defect 7; sibling scan 2026-10-23, read-only,
> HEAD-scoped `git grep`; HEADs kumitate `3632602c`, kama `1560e4d8`, kagi `899c50b4`, tameshi
> `9bb699ad` [moved mid-scan], kengaku `1f3b0f1e`):
>
> - **kumitate — compatible, no contest.** omp's task-agent discovery excludes the cross-harness
>   roots `.claude/agents`, `.codex/agents`, `.gemini/agents`
>   (`kumitate-shokunin/corpus/knowledge/omp-task-contract.md:168`; S003 quote `:174`). Same three
>   paths as three of C1's clients, disjoint claims: kotoba records what each client documents for
>   itself; kumitate records that omp skips them. kumitate routes prompt/skill craft to kotoba
>   (`kumitate-shokunin/PROVINCE.md:27`).
> - **kumitate — the fleet's live dispatch agents are omp-format cards, outside C1's seven
>   clients.** Kimi lane files at `~/.kimi-code/agents/secondary/` with their frontmatter and
>   doc-sourced scope precedence (`kumitate-shokunin/corpus/knowledge/kimi-lane-definitions.md:5,28-32,248-252`);
>   canonical `agents/*.md` cards projected to Devin subagent profiles by
>   `scripts/project-devin-subagents.mjs` (`corpus/knowledge/remaining-scripts-census.md:594-596`);
>   "agent cards" are contract-hash members (`SKILL.md:331`). Sibling-owned (dispatch runtime);
>   kotoba's own census declares the omp roster ungoverned
>   (`kotoba-shokunin/corpus/knowledge/instruction-surface-census-round13.md:497-500`). No C1
>   interaction; do not read C1's table as the whole agent-definition surface.
> - **kama — kotoba-owned by sibling statement.** "Kotoba owns the instruction/agent surface and
>   its model/fallback wording; kama owns independent verification of the target endpoint"
>   (`kama-shokunin/corpus/knowledge/cross-lane-scope.md:29`); janitor/distiller consumer rows carry
>   `kotoba [INFERENCE]` (`corpus/knowledge/consumer-registry.md:91-92`); the
>   `~/.config/opencode/agents/` deletion is recorded at `:56-57` and live-confirmed (directory
>   absent on the host 2026-10-23).
> - **kagi — sibling-owned pin, contested parent.** `~/.config/opencode/agents/janitor.md`
>   frontmatter pinned (`kagi-shokunin/PROVINCE.md:28`; sha `corpus/drift-baseline.tsv:7`;
>   runnable H4 `corpus/checklist.tsv:37`; frontmatter-overrides-JSON semantics
>   `corpus/knowledge/config-layering.md:21`). kagi's own census leaves `$HOME/.config/opencode`
>   **unresolved** — "ruling owed to the integrator" (`kagi-shokunin/corpus/README.md:96`). Reported,
>   not ruled.
> - **kengaku / tameshi — no agent-definition surface.** kengaku holds only historical echo rows
>   for the same file (`corpus/evidence/round9-fleet/sweep.tsv:130`) and states the kotoba split
>   (`PROVINCE.md:30,138`). tameshi holds none at either observed HEAD; its matches are wave
>   evidence quoting kagi's asset. Fleet-wide, `.github/agents`/`.copilot/agents` appear in no
>   sibling tree — kotoba is the sole claimant, so C1's VS Code / Copilot CLI rows have no
>   cross-lane cross-check (relevant to the v1.2 control that used issue-tracker text naming
>   `.github/agents`).
> - **Pin drift observed:** kumitate, kama and tameshi HEADs have moved past kotoba's PROVINCE
>   pins; the quoted boundary lines still read as pinned at HEAD. No claim, counter or sibling file
>   changed; no ownership transferred.

## One bounded proposed move

Add the item above to the round-56 report. It is the exact content routed defect 7 asks for
(round-55 spot-check §7.7 and conformance defect 3), it touches no counter, SKILL.md, entry,
SOURCES row or sibling file, and it changes no claim. Optional [INFERENCE], not proposed for this
round: a later round's C1 entry limits (Q31) could name that the omp/Kimi card families sit outside
the seven clients, so "agent-definition files" is not read as opencode-only.

Axes: adjacency improves (the report gains its PROTOCOL-minimum cross-domain item, evidence
pointed and classified); depth, consistency, coverage, operability, freshness and calibration are
untouched — no claim content, predicate, counter or lane file changes.

## Risks

- Sibling HEADs move (tameshi moved twice during this scan; three of five pins are stale). Every
  pointer is revision-bound to the HEAD printed beside it; re-cite only with a fresh `rev-parse`.
- The item must not be read as an ownership ruling: the kagi `$HOME/.config/opencode` row stays
  `unresolved` (integrator-owned), and the kotoba-owned classifications are sibling statements
  (kama) or sibling routes (kumitate), not adjudications.
- [INFERENCE] The `.github/agents` negative is a fleet-corpus negative at HEADs (git grep,
  including `.ufo/`); it does not establish what the client docs say — that stays C1's sources.

## Verification performed / handoff

Performed: read-only `git rev-parse`, HEAD-scoped `git grep -n/-l` sweeps over the five named lanes
and all 21 lanes for the client paths, `git ls-files`, read-only `ls` of the host/fleet card
directories, `date -u` (output above). No exit code is asserted beyond what is printed
(`rev-parse HEAD` for kotoba → `rc=0`; tameshi `ls-files | grep agent` → `AGENTS.md`, `rc=0`).
No counter, self-test, lane code or runtime was executed; no sandbox clone was used; no tool was
installed or updated; no process was left running; no sibling was written.

For Main if integrating: re-run the listed `git -C <lane> grep -n … HEAD` commands at the cited
HEADs to confirm each path:line; confirm the pasted item lands in `.ufo/reports/round-56/kotoba.md`;
confirm no file other than the report changed.

Report: .ufo/waves/round-56/build/ConnSiblingOverlap.md
