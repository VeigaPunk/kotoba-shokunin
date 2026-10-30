# Kb82R03Baseline — baseline evolution and preservation map

Axes: freshness and operability. Read-only reconnaissance; supplied intake revision `47dbe8781657de563ff867caca6244d28e3db504`. Inspected working-source bytes are fingerprinted below; no independent git revision/content equality assertion. No production after-values, gates, selftests, host binaries, installs, scratch clones, or mutations exercised.

## Observed history

- **Round 51:** `verifiers/baseline.json:5-9` pins omp 18.12.6, SHA256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, mtime `2026-10-21T20:37:24.615549837-03:00`. This replaced round47's 18.12.5 pin `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`. `corpus/lessons/round-51.md:3-7` records the historical 5/7→7/7 surfaces claim. `verify_surfaces.py:182-198,245-248,1828-1871` records bq/Kl/Ho, module-scoped v$/S$ resolution, and a historical allowlist discriminator. These are historical observations, not current host measurements.
- **Round 52 intervening contract change:** `verify_surfaces.py:225-244` changes normal omp extraction to declared-pair callee admission, not ongoing allowlist re-pinning. A new minifier callee name alone is not grounds to add a production allowlist. Shape changes and no admitted callees remain failure conditions. Round51 fixtures and old allowlist mode remain deliberately discriminating historical evidence.
- **Round 72 omp:** `baseline.json:15` and `.ufo/waves/round-72/w1/ExecOmpHalf.md:3-17,31-45` record a path-only move to `omp.real`: identical r51 ELF SHA/mtime; command `omp` was then a 1,680-byte wrapper, SHA `ed62a41ec662fd80b3ca522896375b75cec4638e413dd2592f109a716853b2e1`. The receipt explicitly says path repair did not repair population drift or the independent comparator's census race. Do not recast it as full historical harness green.
- **Round 72 opencode:** `baseline.json:16` and `census-removals.json:4-10` pin v2.1.4 at `~/.opencode/bin/opencode`, binary SHA `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7`, dump SHA `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089`. This supersedes npm 1.19.4, not its fixture provenance.
- **Round 82 declared condition:** `plans/round-82.md` says `omp.real` is absent and `omp` is now an 18.14.0 ELF. This scout did not independently remeasure that host condition; the round82 receipt owner supplies the new SHA/mtime and loader derivation. Consequently this is not another justified path-only update.

## Current declared inventory (source enumeration, not runtime completeness)

`surfaces-baseline.json:5-306` and `corpus/knowledge/instruction-surface-census-round13.md:64-270` retain **42 declared classes**: omp 33 (25 governed, 8 excluded), opencode 9 (all still declared governed). Omp governed classes comprise 8 loader-group pairs, 16 loader-literal classes and 1 loader-config class; excluded omp classes comprise 5 loader-literal and 3 loader-config classes. Opencode comprises 5 loader-literal and 4 loader-config classes.

The eight omp extracted loader-group identities must remain:

- `omp:agents-md/AGENTS.md`
- `omp:claude-md/CLAUDE.md`
- `omp:opencode/AGENTS.md`
- `omp:gemini/GEMINI.md`
- `omp:gemini/system.md`
- `omp:gemini/SYSTEM_TEMPLATE.md`
- `omp:github/copilot-instructions.md`
- `omp:windsurf/memories/global_rules.md`

The eight excluded omp identities remain `discovery/mcp-configs`, `discovery/settings`, `discovery/extensions`, `discovery/plugins`, `discovery/commands`, `discovery/skills-roots`, `unknown/managed-skills`, `unknown/subagent-roster` (all prefixed `omp:`). Their exclusion reasons are not established absence; retain them unless separately traced and explicitly dispositioned.

The six opencode non-ledgered identities remain `instructions/AGENTS.md`, `config/AGENTS.md`, `config/instructions`, `config/instructions-remote`, `read-hook/instructions`, `instruction-context/AGENTS.md` (all prefixed `opencode:`). The other three are ledgered, not deleted:

| Declared class | Ledger absence discriminator |
|---|---|
| `opencode:instructions/CONTEXT.md` | `CONTEXT\\.md` absent |
| `opencode:instructions/CLAUDE.md` | `disableClaudeCodePrompt` and old AGENTS/CONTEXT array shape absent |
| `opencode:claude-home/CLAUDE.md` | old home/.claude/*.md join shape absent |

`census-removals.json:14-36` preserves exact regexes and reasons. **CLAUDE.md literal presence alone does not resurrect either CLAUDE loader class**: the ledger explicitly distinguishes prose/string-table mentions from loader roles.

Textual contract trace (not LSP semantic proof): `verify_surfaces.main:2498-2570` loads baseline, ledger, inventory, and dumps; `load_removals:324-363` permits only declared opencode ids with nonempty regexes/reasons; `removal_problems:366-378` excuses only when every anchor is absent; `main:2555-2568` applies this to literal/extraction checks while inventory parity still uses the full baseline. `check_substrate_repin_v2.py:122-145,173-190,231-246,668-678` independently freezes the r72 base and exactly three removals, preserving `(literal, context_kind, verdict)` signatures for non-ledgered opencode classes. It does not establish full omp class-set preservation: L1's separate unchanged-class-set guard remains necessary.

## Source comments requiring current-default correction

| Location | Stale operational assertion after host move | Bounded disposition |
|---|---|---|
| `verifiers/check_substrate_pins.py:64-68` | omp currently wrapper / ELF currently `omp.real` | Update omp default and explain r82 ELF provenance; leave opencode unchanged absent evidence. |
| `verifiers/verify_surfaces.py:163-169` | defaults follow real binaries but selects absent `omp.real`; says current SHA is r51 | Update default/comment after independent r82 derivation. |
| `verifiers/verify_harness_claims.py:53` | inline `omp is a wrapper script` | Update current path and scope/date comment. |
| `verifiers/verify_harness_independent.py:123-124` | current wrapper premise and `omp.real` default | Move together with claims default; avoid a split substrate. |
| `verifiers/verify_surfaces.py:178-185` | says callee allowlist is FIRST thing to re-pin | Already superseded by r52 declared admission at 225-244. Preserve dated rename history; describe allowlist as historical mode, not live remedy. |
| `verifiers/verify_surfaces.py:11-23` | introductory extraction description lists old concrete callees without making normal generic admission clear | Clarify alongside r82 receipt if documentation touched; do not expand historical allowlist merely to fit 18.14.0. |

## Historical claims that must remain audit trail

- Keep `baseline.json`'s round21/44/47/51/53/72 notes, including old SHA/mtime, old wrappers and superseded opencode channels. Append a distinct round82 note and update only current omp pin fields once derived. The dated round51 phrase “opencode pin ... still holds” is historical context, not a present-host guarantee.
- Keep `surfaces-baseline.json:3`'s assembled evolution (r14→r18→r47), the census's older loader witnesses and its historical section/round47 class ledger (`instruction-surface-census-round13.md:289-321`). Add scoped current-generation evidence rather than erase old class history. Its round47-last assembled metadata is incomplete chronology, not permission to remove r72-ledgered classes.
- Keep round51 module-scope/parameter-shadow arms and minifier fixtures; preserve round72 opencode-generation comments and 1.19.x fixture arms (`verify_surfaces.py:1245-1248,1828-2029,2216-2363`). They are dated regression evidence, not stale present-tense defaults.
- **Keep `check_substrate_repin_v2.py` byte-identical.** Its docstring at 12-15 describes the frozen round72 claim, including its then-valid path move; that sentence is historical even though false as a current host description. Preserve BASE_REV and FROZEN_REMOVALS. The target remains 3/3 pins, 7/7 surfaces, 3/3 ledger; no tip-battery 6/6 implication.
- Preserve historical reported assertion counts and failure receipts; do not rewrite them into r82 after-results. C2 operability is independent and no selftest result is claimed here.

## Evidence limits and fingerprints

LSP unavailable: `read xd://lsp` returned `No such tool`; no semantic server/status device was mounted. Definition/caller tracing above is explicit source-text fallback, not semantic references proof. Confidence high for inspected source declarations and chronology; current host loader identity/absence remains unmeasured here. No scratch or heavy work was needed; no installs or service changes.

Executed metadata command: `sha256sum` over the nine absolute source paths below via `subprocess.run(..., capture_output=True)`, no pipeline; command-owned exit **0**. Exact SHA256 output (paths abbreviated relative to lane solely for readability):

```text
945eb49e6ab368938d7eeaddc0b53308205ab69f3362aea0cd0f69c64300c149  verifiers/baseline.json
6b23c3d1c8766e4effea9f5502b638de7b22cd0d61be20426ba99482c7d1260b  verifiers/surfaces-baseline.json
c8944913bb802822f80aeee44e99c1f4886e0110fdfeb2ebbc7bea9e2729f3e2  verifiers/census-removals.json
df0c7ccaab930bf22359d7c5ec174a1429d11e78e856b7e3272d9fe29baf8bab  verifiers/verify_surfaces.py
c896e5b91dd998de845905ff23ddc4c03e8964e3efbabefadac8b7bedb5d9667  verifiers/check_substrate_pins.py
629487a116bdf287f2bcd43652ead051b052efd0a32632b38a45fece6ed4b348  verifiers/check_substrate_repin_v2.py
d7b767d61798d2ede4ab6ec98c7f4b2792a77f2c179c1b93b71591139b394114  verifiers/verify_harness_claims.py
8201a3a09d5c8892db25d8b44306959a512b1ee6f2f71d70ce445340ce286b32  verifiers/verify_harness_independent.py
872262c3e79d0c4441a46104eb7dd9d1f3151090bbc6773f0a59fb7744389e28  corpus/knowledge/instruction-surface-census-round13.md
exit=0
```

VERDICT: Source history mapped; four active omp defaults/comments need coordinated r82 refresh, historical r51/r72 evidence and all 42 classes must remain; host re-derivation is not performed by this scout.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82R03Baseline.md
