# Kb82E12Loader — Round 82 C1 independent extraction probe (group github)

Seat: Kb82E12Loader (leaf). Assignment: C1 independent extraction probe for
group `github`; inspect `verify_surfaces.py` documented extraction grammar and
the current host ELF via `strings`; write a bounded Python probe extracting
calls/literals for THIS group with module-scoped variable resolution and source
anchors; output distinct pairs vs `surfaces-baseline.json` at base, sha256 of
the binary before/after, and false-match decoys. Return probe+receipts, not a
production edit. Base: `47dbe8781657de563ff867caca6244d28e3db504`.

## What was measured

- Host substrate: `/home/vgpnk/.local/bin/omp` is now the ELF itself
  (`file`: 64-bit LSB x86-64, dynamically linked, **not stripped**, BuildID
  `588d7307f333293c728b74df19b7323c20736899`), `omp --version` = `omp/18.14.0`.
  The round-72 default `~/.local/bin/omp.real` no longer exists; the wrapper
  generation is gone and the pinned path moved onto the ELF.
- Binary identity (read-only; sha256 taken before and after all work, equal):
  `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`,
  size 276244656, mtime `2026-10-29T23:19:46-0300`.
  Old pin was `85d9daf3…` (round-51 `omp.real`) — the 18.14.0 ELF is a new
  substrate byteset, exactly the condition C1 re-derivation exists for.
- Dump: `strings -n 4` (GNU binutils 2.47, same invocation as the lane's
  `dump_via_strings`), sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`,
  47434077 bytes / 2546731 lines. Unlike the minified 18.12.x bundles, the
  18.14.0 dump carries readable TS source and `// packages/...` module markers.
- Tools: Python 3.14.8 (`python3 -B`); no installs/upgrades this seat.

## Probe

`Kb82E12Loader-probe.py` (build dir) re-implements the grammar documented in
the lane `verifiers/verify_surfaces.py` docstrings **independently** (no lane
import on the primary path): the round-52 generic registration-call shape
`callee(<v>, <quoted|ident group>, "<file>.md")` with any-identifier callee;
first-seen constant table with conflict-drop; module scopes from source-path
comment lines; scope-then-global identifier resolution; the function-parameter
shadow guard (fail-closed); and callee admission by "registers at least one
declared pair". Source anchors (the module-marker line scoping each call) are
recorded per call. After the primary extraction it optionally cross-checks
against the lane's own `verify_surfaces.extract_classes()` run on the same
dump. It also runs a 7-case false-match decoy battery on synthetic dumps.

## Findings — group github

1. **Distinct github pairs vs baseline at base: exact agreement, both
   directions empty.** Baseline declares one github loader-group pair
   `(github, copilot-instructions.md)` (class `omp:github/copilot-instructions.md`);
   the independent probe extracts exactly that one pair.
   `missing = []`, `extra = []`.
2. **Single registration call, new callee name, quoted group.** The full
   pattern sweep (11 grammar-matching calls, 8 admitted pairs over all groups)
   finds exactly ONE github-group registration on the 18.14.0 dump:
   `ts(u, "github", "copilot-instructions.md")` in module
   `// packages/coding-agent/src/discovery/github.ts` (loader `xre`,
   registered by `De(Hl.id, {id: Ko, displayName: Zm, description: "Load
   copilot-instructions.md from .github/ and ~/.copilot/; AGENTS.md from
   COPILOT_CUSTOM_INSTRUCTIONS_DIRS", …, load: xre})`). Callee `ts` is a
   minifier rename vs the round-18 `Cl` / round-50 `Fo` the census rows cite —
    the callee-rename-robust grammar absorbs it without an allowlist edit.
3. **Module-scoped binding present but not needed.** The same module binds
   `var Ko = "github"` and uses `Ko` in `_source: et(Ko, …)` tagging, but the
   registration call itself carries the QUOTED group `"github"`, so resolution
   is direct (no constant-table hop; param-shadow guard not triggered). Anchor
   recorded: `// packages/coding-agent/src/discovery/github.ts`.
4. **Same-token non-matches (shape discipline holds).** `ts(u, "github",
   "instructions")` (×2) and `ts(u, "github", "prompts")`, `ts(u, "github",
   "skills")` share the callee and first two args but their file literal is not
   `*.md`, so the grammar correctly extracts nothing from them; the enable gate
   `ji("github", u)` and the description/prose tokens likewise extract nothing.
5. **Loader-literal classes witnessed.** `omp:github/instructions`
   (literal `instructions`, 449 dump occurrences) and `omp:github/prompts`
   (literal `prompts`, 491) both occur; their census semantics ("Load
   `*.instructions.md` from `.github/instructions/`…" ×2, Copilot-scoped;
   "Load `*.prompt.md` from `.github/prompts/`…") are byte-present in the new
   dump (lines 977031/977037/977043/977048), matching the round-13 census
   registry text. All three github baseline classes are therefore fresh on the
   new substrate.
6. **Auxiliary full sweep (github was the scope; this is supporting
   evidence):** the independent probe's full-pattern extraction over the whole
   dump yields exactly the 8 pairs of the baseline's omp loader-group set —
   agents-md/AGENTS.md, claude-md/CLAUDE.md, gemini/{GEMINI.md,
   SYSTEM_TEMPLATE.md, system.md}, github/copilot-instructions.md,
   opencode/AGENTS.md, windsurf/memories/global_rules.md. No undeclared github
   pair hides under another callee.
7. **Lane cross-check:** running the lane's own `verify_surfaces.extract_classes`
   (from the base clone) on the same dump gives the same github pair set;
   `matches_independent = True`.

## False-match decoy battery (all 7 pass)

- `alias-decoy-callee` — undeclared `q(u,"evil","EVIL.md")` never admitted; only the declared github pair extracts.
- `param-shadowed-ident` — `Ko` as a function parameter does NOT resolve to `github`; call surfaces as `<unresolved-var:Ko>` (fail-loud), github pair absent.
- `conflicting-rebind` — two `var Ko = …` in one module drop the name; unresolved, github pair absent.
- `cross-module-binding` — a call in another module using module A's single `Ko="github"` binding resolves through the dump-wide table: pair extracts.
- `non-md-file` — `ts(u,"github","instructions")` / `"prompts"` shapes extract nothing (grammar requires `.md`).
- `token-without-role` — `ji("github", u)` + description prose extract nothing.
- `unresolved-declared-file` — an unresolvable group over a declared file is admitted per the documented CriticC1Escape rule and surfaces as unresolved, never silently as `github`.

## Interpretation for C1 (advisory; L1 owns integration)

The current host substrate 18.14.0 (sha `e7dd2b60…`) re-derives the github
group cleanly under the unchanged extraction grammar: the github slice of the
re-pin target is `pins 3/3`-compatible for this group's classes (loader-group
pair exact, both loader-literals live). The callee rename (`Cl`→`Fo`→`ts`)
and the substrate move (`omp.real`→`omp`) are exactly the events the
round-52 robust rule and this re-derivation guard were built for. No baseline
class needs removal on the github evidence; no new github class appears.

## Boundaries kept

Read-only on the binary; no production file, pin, ledger, census, or sibling
touched; no seat commit/push; no subagent/background work; scratch clone used
for the base baseline only (`git -C`, toplevel asserted). Pacman untouched.
TMPDIR under the seat scratch root.

## Receipts

- Probe: `Kb82E12Loader-probe.py` (sha `b93628f9…`)
- Machine report: `Kb82E12Loader-probe-report.json` (sha `40bd6f69…`)
- Human receipt: `Kb82E12Loader-receipt.txt` (sha `8cda2cb1…`)
- Dump: `Kb82E12Loader-omp-18.14.0-strings.txt` (sha `81277d35…`)
- Manifest: `Kb82E12Loader-SHA256MANIFEST.txt`

VERDICT: group github independently re-derived on host omp 18.14.0
(sha256 e7dd2b60…, unchanged before/after) — extracted pair set
{(github, copilot-instructions.md)} matches the base baseline exactly
(missing 0, extra 0); both loader-literal classes witnessed live; 7/7
false-match decoys rejected; independent result agrees with the lane
verifier on the same dump.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E12Loader.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E12Loader-probe.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E12Loader-probe-report.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E12Loader-receipt.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E12Loader-omp-18.14.0-strings.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E12Loader-SHA256MANIFEST.txt
