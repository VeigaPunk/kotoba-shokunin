# Kb82E10Loader — C1 independent extraction probe, group `claude-md` (host omp 18.14.0)

Seat: Kb82E10Loader (leaf, lane L1 KotobaR82). Round 82, wave 1.
Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch clone, `--shared`, toplevel asserted before any git use).
Assignment: C1 freshness outside guard — independent host sha256/mtime measurement and loader-pair
derivation for group `claude-md` against the CURRENT host ELF `/home/vgpnk/.local/bin/omp`.
No production edit; probe + receipts only.

## VERDICT (up-front)

`omp:claude-md/CLAUDE.md` **re-derives on the live 18.14.0 host binary**: exactly ONE registration
call extracts — callee `F9(u, rD, "CLAUDE.md")` with `var rD = "claude-md"`, in module
`// packages/coding-agent/src/discovery/claude-md.ts` (dump line 972681). Distinct pair set for the
group is `{("claude-md","CLAUDE.md")}`, an EXACT two-way match against
`verifiers/surfaces-baseline.json` at base. Independent probe and the gate's own round-52
`extract_classes` agree (8 pairs, same 8). Full-pattern sweep over the whole dump shows no
unresolved-var, no param-shadowed, no near-miss, no case-decoy, and no historical-callee
registration for this group. Host binary sha256 unchanged by the probe.

## Host substrate measurement (independent)

| item | before | after (probe is read-only) |
|---|---|---|
| path | `/home/vgpnk/.local/bin/omp` | same |
| sha256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` | identical |
| mtime (epoch) | `1793326786` (2026-10-29 23:19) | identical |
| size | `276244656` | identical |
| kind | ELF 64-bit x86-64, not stripped, BuildID 588d7307… | — |
| `omp.real` | ABSENT (matches `.ufo/waves/round-82/receipts/before-pins.txt` UNREADABLE rows) | — |

Version evidence without executing the ELF: `version: "18.14.0"` (multiple), `var A0 = "18.14.0";`
present in strings. Before-surfaces receipt at base: exit 2, `omp binary not found:
/home/vgpnk/.local/bin/omp.real` — the gate default this round must re-pin (L1 owns that edit; this
seat changed nothing).

Dump: `strings -n 4` (verifier-documented method, `dump_via_strings`) →
`/fast/scratch/hyaku/kotoba-r82/Kb82E10Loader/receipts/strings-omp-18.14.0.txt`,
exit 0, stderr 0 bytes, 47,434,077 bytes, 2,546,731 lines, sha256
`81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`.
3,262 source-path module markers → module scoping is live on this bundle (not a one-scope dump).
Tools used: GNU strings (binutils 2.47), Python 3.14.8. No installs/upgrades this seat.

## Documented grammar (source of the probe)

From `verifiers/verify_surfaces.py` at base: call shape
`<callee>(<v>, <group>, "<file>.md")` followed by `,`/`)` with ANY callee admitted only via a
declared pair (round-52 `OMP_GENERIC_CALL_RE`); bindings `<ident> = "<string>"` (≤80 chars, no
escapes); dump-wide first-seen table with drop-on-conflict; own-module-scope table (spans from
`^// <path>.{ts,tsx,js,...}$` markers) decides names the dump-wide table cannot settle; dump-wide
wins wherever it has an entry; nearest-preceding function-header parameter shadowing fails closed;
unresolved surfaces as `<unresolved-var:NAME>`.

## Probe (independent implementation)

`Kb82E10Loader_probe.py` (build artifact): restates the grammar independently (no import of
`verify_surfaces`), resolves every call shape in the dump with module-scoped variable resolution,
anchors every hit to dump line/byte-offset and nearest preceding module marker, and emits the
full-pattern sweep plus decoy analysis as JSON.

### claude-md findings (18.14.0 dump)

- Call shapes total: **11**; distinct (group, file) pairs: **8** — exactly the 8 baseline-declared
  omp loader-group pairs: agents-md/AGENTS.md, **claude-md/CLAUDE.md**, gemini/GEMINI.md,
  gemini/SYSTEM_TEMPLATE.md, gemini/system.md, github/copilot-instructions.md,
  opencode/AGENTS.md, windsurf/memories/global_rules.md.
- Group `claude-md`: **1 call**, callee `F9`, group arg identifier `rD` resolved **dump-wide**
  (`var rD = "claude-md"`, single dump-wide binding, no conflict — module fallback not needed),
  file `"CLAUDE.md"`, offset 20,518,891 / line 972,681, module anchor
  `// packages/coding-agent/src/discovery/claude-md.ts` (marker offset 20,518,762, span 1067).
  Source: `async function j3t(u) { return F9(u, rD, "CLAUDE.md"); }`.
- Distinct pairs for the group: `{("claude-md","CLAUDE.md")}`.
  vs baseline (`omp:claude-md/CLAUDE.md`, literal `CLAUDE.md`, loader-group, governed):
  extracted−baseline = ∅, baseline−extracted = ∅, **match: True**.
- Baseline comparison for the full sweep: extracted-minus-baseline-declared = ∅ (no undeclared
  class surfaces from any resolved pair; the only declared-pair-bearing extra rows in
  `declared_loader_pairs` are loader-literal/config kinds outside this call-shape extractor, as
  documented).

### Literal anchors

- `"claude-md"` occurs exactly **1** time in the whole dump (line 972,678 — the `rD` binding,
  claude-md.ts module).
- `"CLAUDE.md"` occurs **6** times: lines 972,679 and 972,681 (claude-md.ts), 974,448 and 974,458
  (`// packages/coding-agent/src/discovery/claude.ts` — different discovery class), 1,086,569
  (`sharpshooter/consolidate.ts`), 1,323,630 (`commit/agentic/index.ts`). None of the other five is
  a `(group, file)` registration for group claude-md; only the rD call pair extracts.

### False-match decoys (all negative — none pollutes the pair)

- **Callee rotation**: historical names `Id|Cl|jDe|jDf|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq`
  appear at **zero** `.md` registration sites on 18.14.0 — a quoted-only/allowlist extractor would
  find nothing; the round-52 any-callee-admitted rule finds `F9`.
- **Alias decoy**: `F9` has one strings-level alias-looking hit `F=F9"` (line 93,917) — inside a
  data string (quote-terminated), not a JS alias binding; no `var F = F9`-style assignment exists.
  No call sites via any alias; the alias surfaces nothing.
- **Two-char callees** registering pairs: `Ac` (gemini×3, opencode/AGENTS.md,
  windsurf/memories/global_rules.md), `F9` (agents-md/AGENTS.md, claude-md/CLAUDE.md), `ts`
  (gemini×3, github/copilot-instructions.md). Same pairs reachable via multiple callees is the
  documented wrapped-call norm; admission is pair-driven, so no false class is minted.
- **Out-of-grammar F9 calls**: `F9(e)`, `F9(e,t,n)`, `F9(u, Yy, V)` (variable file arg) — fail the
  quoted-`.md`-literal requirement by design and extract nothing.
- **Unresolved / shadowed**: 0 unresolved-var calls with file `CLAUDE.md`; 0 param-shadowed
  group idents at the claude-md call.
- **Near-miss literals**: 0 occurrences of `"claude-md"` outside the call grammar; 0 non-`.md`
  claude-md call shapes; case variants `Claude-md`/`CLAUDE-MD`/`claude_md`/`Claude-MD` all 0.
- Dump-wide conflict names on this bundle: 293 (the 18.12.6 `S$`-style hazard class is real
  generally), but `rD` is not among them — its dump-wide resolution is sound.

### Cross-check (parity, not production scoring)

Ran the base revision's own `extract_classes` in the asserted scratch clone against this seat's
dump with the baseline's declared omp pairs (round-52 generic mode): 8 pairs, claude-md pair
`("claude-md","CLAUDE.md")` — **identical to the independent probe**. Receipt:
`Kb82E10Loader-gate-extractor-crosscheck.json` (sha256 `dd9cd2e80d1b…`). This is loader-pair
derivation evidence for L1's re-pin; it is NOT a production after-value score — the unchanged
round-72 counter and integration remain L1's gate.

## Risks / notes for L1

- New host pin material: sha256 `e7dd2b60…`, mtime `1793326786`, size `276244656`; path default
  must move `omp.real` → `omp` (or equivalent) — seat made no production change.
- Callee rotation is real (F9 new since 18.12.6's bq/Kl/Ho): keep the round-52 admission rule;
  do not resurrect a callee allowlist.
- `"CLAUDE.md"` literal appears in 3 non-claude-md modules (claude.ts, consolidate.ts,
  commit/agentic/index.ts) — literal-presence checks must stay paired with the call-shape
  extraction, as the verifier already does for loader-group rows.
- `strings` artifact `F=F9"` shows decoy scanners must quote-check; harmless here.

## Receipts (all under this seat's paths; dump retained in scratch)

- `.ufo/waves/round-82/build/Kb82E10Loader_probe.py` — sha256 `6cd12bb4ac560ab94d387bf5bc2ecbd37f9fb247d34be704094e033ca47637ec`
- `.ufo/waves/round-82/build/Kb82E10Loader-probe-report.json` — sha256 `be2ec38e7598f0e0bfb967099f1c441dc1fd55c4fe56ef89754c1d72593b55a9`
- `.ufo/waves/round-82/build/Kb82E10Loader-gate-extractor-crosscheck.json` — sha256 `dd9cd2e80d1b29bbdad6e4cdec12a315864b63edb801b394507b6f3455f3a992`
- `.ufo/waves/round-82/build/Kb82E10Loader-binary-before.txt` / `Kb82E10Loader-binary-after.txt` — identical sha256/mtime
- `.ufo/waves/round-82/build/Kb82E10Loader-sha256-receipts.txt` — includes the 47MB strings dump sha256 (`81277d357227…`)
- Scratch (deletable on lane close): `/fast/scratch/hyaku/kotoba-r82/Kb82E10Loader/` (dump, probe, receipts, clone at base)

No installs. Pacman untouched. No subagents, no commits, no production writes; fleet repo mutated
only in the two seat-named paths above.

VERDICT: `omp:claude-md/CLAUDE.md` independently re-derived on live omp 18.14.0 (sha256 e7dd2b60…) — single `F9(u, rD, "CLAUDE.md")` call in discovery/claude-md.ts; pair set exactly matches baseline both directions; probe and gate extractor agree 8/8 pairs; binary unchanged before/after; zero false-match decoys.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E10Loader.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader_probe.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader-probe-report.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader-gate-extractor-crosscheck.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader-binary-before.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader-binary-after.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E10Loader-sha256-receipts.txt
