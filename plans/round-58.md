# Round 58 — plan (kotoba, hyaku phase 4, attempt 1)

Base `f56f6e191762c27c1aa2af11a204db9e2ca4edec` (round-57 spot-check tip). L1 `KotobaR58`, dispatched 07:28Z
2026-10-23; freeze 09:28Z, hard stop 10:28Z. Round 57 was rejected (C1 depth target F ≥ 5 above the reachable
population, max 4). This plan is committed in two steps: **draft** (this text, row rule fixed, C1 targets `TBD`)
before any census seat returns, then **freeze** (census record + targets + counters + control receipts) before
any C1 or C2 data. A rule changed after the freeze is a second measurement, never the declared one (Q28).

## Routed defects from `corpus/lessons/round-57-verifier-spotcheck.md` § 7

| R | defect | route this round |
|---|---|---|
| R1 | `check_infoless_fences.py` registered as a `gate` though its r57 claim was withdrawn | registry row re-labelled `probe` with the withdrawal reason (build wave) |
| R2 | README r57 note cites only S079–S085 | append-only corrected note naming S086–S088 (build wave) |
| R3 | correction-sweep arms: 7 of 11 mutants survive | **claim C2** below |
| R4 | C1 v2 self-test never reaches a successful `main()` | arm added to `check_plugin_manifests.py` self-test; the new C1 counter carries one from birth |
| R5 | dead lowercase `/home/vgpnk/projects/` at `SKILL.md:514-515` | corrected to the live path (build wave) |
| R6 | Q45 census before freezing a per-client target | the C1 census below, recorded before the targets |
| R7 | C2 (info-less fence) redesign; kill-by-PID bound in every context | redesign **carried, not attempted** (no claim rests on it; a second withdrawal on the same counter would repeat r57); the bound sentence `Kill only by the PIDs you started` is inlined in every wave `context` and grepped on the `context` field (Q44) |
| R8 | band-10 attribution `SCORECARD.md:29` | operator item; left untouched |

## Claims (2; causally separable)

### C1 — depth (lowest owned axis, 9): custom command files by client (sourced; the learning claim)

Surface: `SKILL.md` gains `### Custom command files by client` — per client, the folder (or file pattern) that
holds a user-authored reusable prompt / slash command, what such a file sets, and what a skill author does with it;
grounded in `corpus/knowledge/command-files-round58.md` and new `corpus/SOURCES.md` rows opened 2026-10-23. A
different frontier area from r54–r57 (no `SKILL.md` section on it; the base tree holds `.claude/commands`,
`.gemini/commands`, `.cursor/commands`, `.opencode/commands` 0 times).

Counter: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` (built pre-freeze from
`check_plugin_manifests.py` v2; everything not named here is v2 behaviour). Row rule (fixed in this draft):

- Section heading line exactly `### Custom command files by client`; first table header
  `| Client | Command files | What a file sets | Action |`; clients Claude Code, Codex, VS Code, Copilot CLI,
  Gemini CLI, Cursor, opencode; HOSTS = the v2 pinned map; token = first backticked span of the Command files cell;
  action cell ≥ 3 words.
- Token well-formed iff: path regex of v2; after stripping one leading `~/` or `./` it has ≥ 2 path segments and its
  first segment starts with `.`; the final non-empty segment, split on `-`, `.`, `_`, holds a word equal
  case-insensitively to `command`, `commands`, `prompt` or `prompts`; no segment split on `-._` holds `skill`,
  `skills`, `agent`, `agents`, `rule`, `rules`, `plugin`, `plugins`, `extension`, `extensions`; no non-final
  segment holds a dot other than as its first character (E7); no other client's marker (foreign-name guard);
  E5 (a token shared by two client rows disqualifies both).
- Backed iff v2's backing conjuncts hold with the entry table `| Client | Command files | Source | Quote |`, the
  quote 6–25 words containing the token (or its normalised form) case-sensitively at segment boundaries and
  matching `(?i)\b(commands?|prompts?)\b` outside the token span, the source a new tier-A `mined` row opened
  2026-10-23 on the client's pinned host (not changelog/release/news/blog), the quote in the lesson `## Gate`, and
  with `--fetch` the quote found on the live page.
- Prints `custom command files found on the live page F of K; new ground G`; G = distinct casefold(normalise(token))
  of backed rows with 0 case-insensitive segment-boundary hits in the base tree (`':!.ufo'`).
- **Census (Q45, R6): `TBD` — filled at freeze from the W0 census seats, which write no lane content.**
- **Targets: `TBD` at or below the census.** Predicate (the same sentence in the counter, the receipt label and
  here): *exit 0 iff F ≥ T_F and G ≥ T_G*.

### C2 — operability (advisory, 8.5): correction-sweep arms discriminate (R3, M68)

Surface: `verifiers/check_correction_sweep.py` self-test arms. Counter `python3 -B verifiers/check_sweep_mutants.py
--rev <rev>` applies 11 frozen mutants (M01–M11, the `A3MutCorrectionSweep` set) and 5 frozen equivalent rewrites
(E1–E5) to the revision's `check_correction_sweep.py` in a temp git repo and runs its `--self-test`. A mutant is
killed iff its old text occurs exactly once and the mutated self-test exits non-zero; an equivalent survives iff
its old text occurs exactly once and the self-test exits 0; the pristine self-test must exit 0 (else exit 2).
Prints `sweep mutants killed K of 11; equivalents survived E of 5`. Predicate: *exit 0 iff K = 11 and E = 5*.
Expected base: K = 4, E = 5, exit 1. The equivalents are the shortcut control built into the counter: a
snapshot/hash self-test kills them.

## Frontier step

SOURCES rows for C1 (≥ T_F new rows), the census before/after (`scripts/sources-census.sh validate`), one mined
mistake in `corpus/lessons/round-58.md` `## Mistakes`, C1 the sourced claim.

## Shape

Pre-freeze W0 (census + counter builds, ordinary `task`), pre-freeze controls (ordinary `task`), then the default
two v1 waves (build, falsify). The L1 holds the §3 planner seat.
