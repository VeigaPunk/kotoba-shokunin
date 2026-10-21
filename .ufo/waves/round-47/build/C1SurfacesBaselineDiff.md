verdict: All 38 baseline class literals are PRESENT in both frozen dumps (omp 18.12.5, opencode 1.19.3); the BASE omp callee allowlist is fully stale (extracts 0/8, vacuity), but a re-derived `{lq,Xl,Fo}` allowlist restores exact 8/8 parity with zero undeclared pairs; opencode OC-2/OC-3/OC-5 match, OC-1/OC-4/OC-6 fail on renamed anchors whose behavior literals partially survive — complete evidence base for the C1 re-verdict, no baseline entry needs dropping.

# C1 surfaces baseline diff — BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd

Seat: MoriR22R.C1SurfacesBaselineDiff-9 (leaf executor). 2026-10-21.
Artifact: `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json` (37,644 bytes ≤ 1 MiB).
Script: `/fast/scratch/kotoba-r47/C1SurfacesBaselineDiff/diff_surfaces.py` (scratch only; imports the BASE clone's `verifiers/verify_surfaces.py` as a module so regexes/extraction are byte-identical to the checker). Probe: `…/probe_new_allowlist.py`.

## 1. Inputs and integrity

| input | value |
|---|---|
| baseline | `verifiers/surfaces-baseline.json` @ BASE, sha256 `f142506c…c427`, 38 entries (25 governed omp, 5 opencode governed, 8 omp excluded — rows at `verifiers/surfaces-baseline.json:5-280`) |
| omp dump | `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`, 48,115,461 B, 2,443,339 lines, sha256 `33df0aef…01` |
| oc dump | `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`, 67,839,091 B, 750,049 lines, sha256 `f4d8f34a…c3` |
| snapshot check | `sha256sum -c SHA256SUMS` → **exit 0**, all 4 files (both binaries + both dumps) OK |

Census target: `corpus/knowledge/instruction-surface-census-round13.md:64` (`## Class inventory`), omp loader-group rows at `:71-79`.

## 2. Per-class diff (38/38 present, 0 absent)

`presence` = substring of harness dump (same semantics as `check_literal_present`, `verifiers/verify_surfaces.py:508`); `lines` = dump lines containing the literal; `occur` = total occurrences. Counts independently reproduced with `grep -cF` (§5).

| class_id | kind | verdict | present | lines | occur | registration note |
|---|---|---|---|---|---|---|
| omp:agents-md/AGENTS.md | loader-group | governed | YES | 37 | 37 | allowlist 0; nearest `lq(u, f$, "AGENTS.md")` |
| omp:claude-md/CLAUDE.md | loader-group | governed | YES | 15 | 15 | allowlist 0; nearest `lq(u, m$, "CLAUDE.md")` |
| omp:opencode/AGENTS.md | loader-group | governed | YES | 37 | 37 | allowlist 0; census site `Xl(u, "opencode", "AGENTS.md")` |
| omp:gemini/GEMINI.md | loader-group | governed | YES | 5 | 5 | allowlist 0; `Xl(u, "gemini", "GEMINI.md")` + `Fo(…)` twin |
| omp:gemini/system.md | loader-group | governed | YES | 22 | 22 | allowlist 0; `Fo(u, "gemini", "system.md")` + `Xl(…)` twin |
| omp:gemini/SYSTEM_TEMPLATE.md | loader-group | governed | YES | 19 | 19 | allowlist 0; nearest-by-distance is a `join` (see §3 caveat); real calls `Fo`/`Xl` |
| omp:github/copilot-instructions.md | loader-group | governed | YES | 6 | 6 | allowlist 0; `Fo(u, "github", "copilot-instructions.md")` |
| omp:windsurf/memories/global_rules.md | loader-group | governed | YES | 4 | 4 | allowlist 0; `Xl(u, "windsurf", "memories/global_rules.md")` |
| omp:cursor/rules | loader-literal | governed | YES | 275 | 416 | — |
| omp:windsurf/rules | loader-literal | governed | YES | 275 | 416 | — |
| omp:github/instructions | loader-literal | governed | YES | 376 | 432 | — |
| omp:clinerules/.clinerules | loader-literal | governed | YES | 7 | 7 | — |
| omp:omp-dir/RULES.md | loader-literal | governed | YES | 4 | 4 | — |
| omp:provider-gate/enabledProviders | loader-config | governed | YES | 3 | 3 | — |
| omp:agents/rules | loader-literal | governed | YES | 275 | 416 | — |
| omp:agents-md-walkup/AGENTS.md | loader-literal | governed | YES | 37 | 37 | — |
| omp:omp-dir/AGENTS.md | loader-literal | governed | YES | 37 | 37 | — |
| omp:claude-dir/CLAUDE.md | loader-literal | governed | YES | 15 | 15 | — |
| omp:codex/AGENTS.md | loader-literal | governed | YES | 37 | 37 | — |
| omp:agent-system-prompt/SYSTEM.md | loader-literal | governed | YES | 27 | 27 | — |
| omp:marketplace/plugin-rules | loader-literal | governed | YES | 528 | 561 | — |
| omp:agents/prompts | loader-literal | governed | YES | 469 | 491 | — |
| omp:github/prompts | loader-literal | governed | YES | 469 | 491 | — |
| omp:codex/prompts | loader-literal | governed | YES | 469 | 491 | — |
| omp:agents/skills | loader-literal | governed | YES | 419 | 492 | — |
| omp:discovery/mcp-configs | loader-config | excluded | YES | 60 | 69 | — |
| omp:discovery/settings | loader-config | excluded | YES | 35 | 41 | — |
| omp:discovery/extensions | loader-literal | excluded | YES | 443 | 550 | — |
| omp:discovery/plugins | loader-literal | excluded | YES | 528 | 561 | — |
| omp:discovery/commands | loader-literal | excluded | YES | 708 | 758 | — |
| omp:discovery/skills-roots | loader-literal | excluded | YES | 419 | 492 | — |
| omp:unknown/managed-skills | loader-literal | excluded | YES | 10 | 10 | — |
| omp:unknown/subagent-roster | loader-config | excluded | YES | 739 | 801 | — |
| opencode:project/AGENTS.md | loader-literal | governed | YES | 25 | 30 | — |
| opencode:config/AGENTS.md | loader-config | governed | YES | 25 | 30 | — |
| opencode:read-hook/AGENTS.md | loader-literal | governed | YES | 25 | 30 | — |
| opencode:api-entries/instructions | loader-config | governed | YES | 104 | 190 | — |
| opencode:config/instructions | loader-config | excluded | YES | 104 | 190 | — |

**No class literal went missing on the substrate bump.** The C1 failures are extractor drift, not corpus drift — no entry needs re-verdicting out of existence.

## 3. omp 18.12.5: the BASE allowlist is 100% stale; re-derivation restores 8/8

`OMP_CALL_RE` allowlist at BASE (`verifiers/verify_surfaces.py:155-158`, names `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo`, last pinned 18.12.2 per the comment at `:141-146`) matched **zero** calls in the 18.12.5 dump → `check_no_uncovered_class` vacuity 0/8, exactly the before-value.

Callee-agnostic census (any `Ident(v, group, "*.md")` call, 3 args) over the whole omp dump finds exactly **3 distinct callees, 11 call sites** — the complete 18.12.5 registration family:

```
895129:  return lq(u, f$, "AGENTS.md");                       # f$ = "agents-md"  (dump line 895126: var f$ = "agents-md";)
895140:  return lq(u, m$, "CLAUDE.md");                      # m$ = "claude-md"  (dump line 895137: var m$ = "claude-md";)
898856:  const T = Xl(u, "gemini", "GEMINI.md");
898867:  const M = Fo(u, "gemini", "GEMINI.md");
898992:  await R(Fo(u, "gemini", "SYSTEM_TEMPLATE.md"), "project", "template");
898993:  await R(Fo(u, "gemini", "system.md"), "project", "text");
898994:  await R(Xl(u, "gemini", "SYSTEM_TEMPLATE.md"), "user", "template");
898995:  await R(Xl(u, "gemini", "system.md"), "user", "text");
899090:  const T = Xl(u, "opencode", "AGENTS.md");
899328:  const T = Fo(u, "github", "copilot-instructions.md");
900239:  const T = Xl(u, "windsurf", "memories/global_rules.md");
```

All 8 baseline loader-group pairs are covered by `{lq, Xl, Fo}`; the var-bound groups `f$`/`m$` resolve through the BASE `constant_table`/`ASSIGN_RE` (`verify_surfaces.py:168-171, 299-313`) unchanged.

**Falsifiable probe** (`probe_new_allowlist.py`): swap `vs.OMP_CALL_RE` for the `{lq|Xl|Fo}` pattern, re-run BASE `extract_classes` verbatim over the snapshot dump → **extracted 8, unextracted declared: none, undeclared extracted: none, PASS 8/8 parity** (exit 0). This is re-derivation evidence for the integrator's re-pin; the production edit is not mine to make.

Counterexamples found while working (recorded, not suppressed):
- My first probe computed the declared pair set with `rsplit("/",1)`, which parses `omp:windsurf/memories/global_rules.md` as group `windsurf/memories` and reported a false MISMATCH. The verifier's `CLASS_ID_RE` (`verify_surfaces.py:172`) puts only the first path segment in the group. Any re-pin tooling must reuse `CLASS_ID_RE`, not ad-hoc splitting.
- For `omp:gemini/SYSTEM_TEMPLATE.md` the "nearest registration-like line" (line-distance metric) is a `path.join`-shaped loader at dump line 896216 (`await T(sr.join(M.dir, "SYSTEM_TEMPLATE.md"), "project", "template")`), nearer than the true `Fo`/`Xl` registrations at 898992/898994. Nearest-by-distance is a hint, not a verdict; the callee census above is the authoritative site list.

## 4. opencode 1.19.3: OC rule status, anchor by anchor

From `extract_opencode_rules` at BASE (`verify_surfaces.py:406-449`) run over the snapshot dump; counts via `grep -cF` (grep exits 1 on zero matches — the zeros are the signal):

| rule | verdict @1.19.3 | anchor counts |
|---|---|---|
| OC-1 project walk-up | **unmatched** | `ConfigInstructionPlugin` ×0; **BUT** the behavior shape is live: `…OPENCODE_DISABLE_PROJECT_CONFIG\|\|!h?[]:yield*H.up({targets:["AGENTS.md"],start:S,stop:$})…` (`targets:["AGENTS.md"]` ×1). ⚠️ trap: the lone `projectSource` hit (×1) is an unrelated session-pagination flag (`projectSource:!0` in a messages context) — loosening OC-1 to that token would false-positive |
| OC-2 global `<config>/AGENTS.md` | **matched** | `X(r.config,"AGENTS.md")` regex ×1; a second twin with a different receiver var (`jX(L.config,"AGENTS.md")`) sits beside the OC-1 walk-up — the receiver name is minification-volatile, worth anchoring on the argument shape instead |
| OC-3 ambient schema | **matched** | `ambient instructions` ×2 |
| OC-4 read-tool channel | **unmatched** | all four anchors ×0 (`ReadTool.Plugin`, `targets:[a$]`, `a$="AGENTS.md"`, `SessionInstructions.load`); generic `ReadTool` ×4, `SessionInstructions` ×0 — the channel's names are gone; whether the behavior survives needs a runtime trace, not a string pin |
| OC-5 resolution switch | **matched** | `OPENCODE_DISABLE_PROJECT_CONFIG` ×7; `OPENCODE_CONFIG_PROJECT_DISABLE` ×0 |
| OC-6 API entries | **unmatched** | route `/instructions/entries` ×1 survives; announced-tool ids `session.instructions.entry*` ×0 |

Net: `surfaces.opencode_extract` at BASE fails on exactly OC-1/OC-4/OC-6 (matches the before-SUMMARY). OC-1 is re-anchorable today on the live walk-up shape; OC-4 and OC-6 need fresh derivation (OC-4 possibly a dynamic probe; OC-6 route anchor + new tool-id discovery).

## 5. Commands run (all in scratch or read-only)

| cmd | exit | key output |
|---|---|---|
| `git clone -q --no-hardlinks …/kotoba-shokunin /fast/scratch/kotoba-r47/C1SurfacesBaselineDiff/lane && git -C … checkout -q --detach c61a973b…` | 0 | HEAD `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` | 0 | 4/4 OK (2 binaries + 2 dumps) |
| `python3 /fast/scratch/kotoba-r47/C1SurfacesBaselineDiff/diff_surfaces.py` | 0 | table above; JSON 37,644 B |
| `python3 -B verifiers/verify_surfaces.py --json --omp-strings …/omp-18.12.5.strings --opencode-strings …/opencode-1.19.3.strings` (scratch clone @BASE) | 1 | 4 PASS / 3 FAIL — `literal_present` (8 omp pairs lack call shape), `no_uncovered_class` (vacuity 0/8), `opencode_extract` (OC-1/OC-4/OC-6); `table_parity` 38 ids, `literal_parity` 38, `kind_parity` 38, `excluded_reason` 9 — all PASS. Identical failure set to `.ufo/waves/round-47/before/SUMMARY.md` → the frozen snapshot reproduces the before-values exactly |
| `grep -cF '<lit>' omp-18.12.5.strings` for AGENTS.md / copilot-instructions.md / memories/global_rules.md / SYSTEM_TEMPLATE.md | 0 | 37 / 6 / 4 / 19 — equal to script `line_hits` |
| same for opencode AGENTS.md / instructions | 0 | 25 / 104 — equal |
| `grep -nE '(lq|Xl|Fo)\(…' \| grep -F '.md'` | 0 | the 11 sites in §3 |
| `python3 …/probe_new_allowlist.py` | 0 | PASS 8/8 parity |

Tools installed/updated: none (no need arose; no pacman/uv/npm activity).

## 6. What I did NOT check

- The production re-pin itself (`verify_surfaces.py` allowlist + OC rules): production files are read-only to this seat; the probe is scratch-only evidence for the L1 integrator.
- OC-4 read-hook and OC-6 announced-tool behavior at runtime — literal/anchor presence only; no opencode process was launched (wrapper ban respected; nothing executed from the npx cache).
- Whether the `join`-shaped loader at omp dump line 896216 is itself a live registration path (only its text was observed).
- Diff against the predecessor binaries (omp 18.12.3, opencode 2.x-era) — not on disk; before/after rests on `before/SUMMARY.md` and census prose.
- `check_substrate_pins.py` — another lane's item, out of my scope.
- `dump_line` indexes in the JSON are ordering-only navigation; per census method (`instruction-surface-census-round13.md`, "Anchors are literals, never offsets") no evidence here rests on an offset.

## 7. Lane writes

- `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json` (37,644 B) — the machine evidence.
- `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.md` — this report.
- Scratch (outside the lane): clone @BASE, `diff_surfaces.py`, `probe_new_allowlist.py`. No git/jj mutations in the fleet repo; no binaries or dumps copied into the repo.
