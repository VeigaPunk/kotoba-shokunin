# Round 59 — plan (kotoba, hyaku phase 4, attempt 1)

Base `a975cbbf00534443c49bf02e29c813a3db0bf0f8` (round-58 spot-check tip). L1 `KotobaR59`, dispatched 08:56Z
2026-10-23; freeze 10:56Z, hard stop 11:56Z. Round 58 was admitted (C1 depth verified). This plan is committed in two
steps: **draft** (this text, row rule and target formula fixed, C1 targets `TBD`) before any census seat returns, then
**freeze** (census record + targets + counter + its sha) before the control wave scores it and before any C1 data. A
rule changed after the freeze is a second measurement, never the declared one (Q28).

## Routed defects from `corpus/lessons/round-58-verifier-spotcheck.md` § 7

| R | defect | route this round |
|---|---|---|
| R1 | seat `ReviewBudgetMove` wrote its report into the fleet root; the misroot sweep ran before that write | byte-exact copy committed at `.ufo/waves/round-58/falsify/ReviewBudgetMove.md` with a provenance note (fleet copy left for the operator, as the spot-check says); every wave context pins the output dir inside the lane (`.ufo/waves/round-59/bounds.md`); the round-59 misroot sweep runs after the last seat settles and its output is committed; lesson mistake M79 |
| R2 | tip receipts not committed (`verify_skill_checklist.py` at `ed44e0c4`, corpus-integrity "4 DRIFT") | executor seat re-runs both at `ed44e0c4` in a sandbox clone; receipts committed naming `ed44e0c4`; this round's tip receipts are committed before the report |
| R3 | counter blind spots: field cells unread, live fetch UA-sensitive | the C1 counter below reads the field cell (every backticked event name must be on the source page), checks a committed page snapshot whose sha256 equals the SOURCES row, and fetches with curl and a browser UA (3 attempts) |
| R4 | `corpus/SOURCES.md:102` S089 anchor label "Where skills live" ≠ page heading "Choose where skills load" | append-only correction note (SOURCES rules) |
| R5 | report said "600 → 596" from the freeze commit; base was 598 | every budget line in this round names the base value at `a975cbbf` (596) |
| R6 | carried: `SHONEN.md:6` pointer drift; C2 redesign input `build/CriticC2Redesign.md`; L0 `kotoba | round-55 |` | carried, not attempted (no claim rests on them) |

## Claims (1 declared)

### C1 — depth (lowest owned axis, 9): hook configuration files by client (sourced; the learning claim)

Surface: `SKILL.md` gains `### Hook files by client` beside § Custom command files by client — per client, the file
(or folder) its own docs name for hook configuration (code the client runs on a lifecycle event, deterministic, not
text the model may ignore), the events a hook can fire on, and what a skill or rule author does with it (move a rule
that must hold every time out of the prompt). Grounded in `corpus/knowledge/hook-files-round59.md` and new
`corpus/SOURCES.md` rows opened 2026-10-23. New ground: no `SKILL.md` section on hooks at the base; `PreToolUse`,
`.github/hooks` and `.cursor/hooks` occur 0 times in the base tree (`git grep -ilF <t> a975cbbf -- . ':!.ufo' | wc -l`).

Counter: `python3 -B verifiers/check_hook_files.py --rev <rev> --fetch` (built pre-freeze from
`verifiers/check_command_files.py`; everything not named here is that counter's behaviour). Row rule (fixed in this
draft):

- Section heading line exactly `### Hook files by client`; first table header `| Client | Hook config | Events |
  Action |`; clients Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode; HOSTS = the pinned map of
  `check_command_files.py`; token = first backticked span of the Hook config cell; action cell ≥ 3 words.
- Token well-formed iff: the path regex of `check_command_files.py`; after stripping one leading `~/` or `./` it has
  ≥ 2 path segments and its first segment starts with `.`; no segment split on `-`, `.`, `_` holds `skill`, `skills`,
  `agent`, `agents`, `command`, `commands`, `prompt`, `prompts`, `rule`, `rules`, `plugin`, `plugins`, `extension`,
  `extensions`; no non-final segment holds a dot other than as its first character (E7); no other client's marker
  (foreign-name guard); E5 (a token shared by two client rows disqualifies both).
- **Events cell (R3, field check):** at least 2 distinct backticked spans, each matching `^[A-Za-z][A-Za-z0-9_.:-]*$`.
- Backed iff: the entry table `| Client | Hook config | Source | Quote |` has the client's row with the same token;
  the quote is 6–25 words, contains the token (or its normalised form) case-sensitively at segment boundaries and
  matches `(?i)\bhooks?\b` outside the token span; the source is a new tier-A row opened 2026-10-23 on the client's
  pinned host (not changelog/release/news/blog/tracker); the quote is in the lesson `## Gate`; the committed snapshot
  `.ufo/waves/round-59/snapshots/<S###>.page` exists at the revision, its sha256 equals the sha256 printed in that
  SOURCES row, and the quote and every Events span are found on the snapshot (spans case-sensitively, not inside a
  longer identifier).
- With `--fetch`: the row is **found** iff it is backed and the quote and every Events span are also found on the live
  page, fetched with `curl -sSL` and a browser User-Agent, up to 3 attempts, final URL on the pinned host.
- Prints `hook files backed on committed snapshots S of K; found on the live page F of K; new ground G`; G = distinct
  casefold(normalise(token)) of found rows with 0 case-insensitive segment-boundary hits in the base tree `a975cbbf`
  (`':!.ufo'`). Without `--fetch` the live part reads `live not run` and F = 0.
- **Census (Q45), recorded before the targets:** W0 census seats (one per client, scouts, no lane content) score each
  client's candidate against this rule, including the Events cell.
- **Target formula (fixed now, applied to the census at freeze):** T_F = F_max − 2 and T_G = G_max − 1, where F_max is
  the census count of eligible clients and G_max the eligible tokens with 0 base hits. If F_max < 5 or G_max < 2 the
  claim is redesigned before data, never after. Predicate (the same sentence in the counter, the receipt label and
  here): *exit 0 iff F ≥ T_F and G ≥ T_G* on `--rev <rev> --fetch`; receipt label
  `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)`.
- Targets: `TBD` (set at freeze from the census by the formula above).
- Commit order: targets and counter are committed before the control wave scores them; a control that meets the
  predicate forces a redesign before any data (erratum), never a change after data.

## Pre-freeze control wave (phase-4 rule)

Fresh mutation-tester / executor seats build and score, with the frozen counter at the freeze commit: do-nothing (the
base), junk rows, all-false (every row fabricated, no sources), no-reader (rows and entry, no snapshots), fabricated
snapshot (invented page whose sha256 is written into its row), events-fabricated (real token and quote, invented event
names), off-topic (round-58 command rows relabelled), and shortcut keyed on labels (rows copied from another section's
tokens). Every receipt names the counter sha; any control that meets the predicate forces redesign before data.

## Frontier step

SOURCES rows for C1 (≥ T_F new rows), the census before/after (`scripts/sources-census.sh validate`), one mined mistake
in `corpus/lessons/round-59.md` `## Mistakes` (R1 class), C1 the sourced claim.

## Shape

Pre-freeze W0 (census + counter build, ordinary `task`), pre-freeze controls (ordinary `task`), then the default two v1
waves (build, falsify). The L1 holds the §3 planner seat.
