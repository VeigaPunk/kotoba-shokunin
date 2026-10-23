# Round 57 — lessons (kotoba, hyaku campaign, attempts 1–3)

Base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`; plan and frozen counters `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`;
erratum 1 (C1 counter v2, C2 withdrawn before data) `01312a77e36317feb6e961aba77841ddab1225ca`; v2 re-control receipts
`27af04a7ed8cee74291fd8237f5c73c43243ce02`. Claim: C1 depth (plugin manifests by client; the learning and sourced
claim). C1 content `ac22ca8791980314a37eb1daa69b846f80a1b9e2`; C1 measured (miss) `07c33d73ddce769d9cea2846a6313164401b5478`.
Attempts 1 and 2 died with the orchestrator (05:25Z, 06:19Z); attempt 3 ran the falsify wave. Seat reports:
`.ufo/waves/round-57/w0/`, `.ufo/waves/round-57/controls/`, `.ufo/waves/round-57/build/`, `.ufo/waves/round-57/a3/falsify/`.

## Gate

### Admitted (rows opened this round; fetch records in the seat reports named)

| row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat |
|---|---|---|---|---|---|---|
| S079 | https://code.claude.com/docs/en/plugins-reference.md | 2026-10-23T04:46:45Z | 42,124 B, sha256 `f2910dd6…` | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." | `plugins-reference.md:34` | SrcClaudeCode |
| S080 | https://developers.openai.com/plugins/build/plugins.md | 2026-10-23T04:47:08Z | 38,036 B, sha256 `c37e330d…` | "The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin." | `build-plugins.md:135-137` | SrcCodex |
| S081 | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 2026-10-23T04:47:13Z | 21,972 B, sha256 `d6e10328…` | "A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics." | `agent-plugin-reference.md:97` | SrcVSCode |
| S082 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | 2026-10-23T04:47:14Z | 7,711 B, sha256 `c0642867…` | "Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory." | `plugins-creating.md:27` | SrcCopilotCLI |
| S083 | https://geminicli.com/docs/extensions/reference.md | 2026-10-23T04:46:46Z | 12,022 B, sha256 `8b9eecb2…` | "Each extension must have a `gemini-extension.json` file in its root directory." | `extensions-reference.md:106-107` | SrcGeminiCLI |
| S084 | https://cursor.com/docs/plugins.md | 2026-10-23T04:46:52Z | 20,323 B, sha256 `74387ff9…` | "plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and" | `plugins.md:28` | SrcCursor |
| S085 | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | 2026-10-23T04:47:59Z | 60,780 B, sha256 `e505931a…` | "Plugins under `.opencode/plugins/` are loaded automatically, like the local example above." | `index.mdx:21` | Srcopencode |
| S086 | https://developers.openai.com/plugins/build/plugins.md (correction row for S080) | 2026-10-23T06:47:23Z | 38,036 B, sha256 `c37e330d…` | "Only `.codex-plugin/plugin.json` is always created." | `plugins.md:76` | A3CandS086 |
| S087 | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx (correction row for S085) | 2026-10-23T06:46:53Z | 4,371 B, sha256 `39afa299…` | "Global plugins use the same discovery layout under the OpenCode config directory." | `plugins.mdx:57` | A3CandS087 |
| S088 | https://cursor.com/docs/reference/plugins.md | 2026-10-23T06:46:23Z | 30,324 B, sha256 `3bbf36f3…` | "Treated as a single-skill plugin (only if no `skills/` dir and no manifest `skills` field)" | `reference-plugins.md:164` | A3CandS088 |

Quote notes (attempt 1, each re-opened against the seat's fetched bytes by the L1, Q42): S079, S081, S084 and S085 are one line
each and unshaped (S084 is a contiguous substring: the list marker and bold label before it and the link after it are
not quoted); S080 folds two line breaks (`:135-137`); S082 omits the list number `2. ` before it; S083 folds one line
break (`:106-107`).

Quote notes corrected (attempt 3; every page re-fetched by the falsify seats `A3ReopenS079`–`A3ReopenS085` at
2026-10-23T06:45Z, each sha256 identical to its row; M65): no quote has markup stripped inside its span. S079 is the
first of three sentences on `:34`; S081 the middle of three sentences on `:97`; S084 a contiguous substring of `:28`
(the list marker and bold label before it and the `variables` link after it are not quoted); S085 the first sentence
of `:21` (the line continues `To load published packages`); S080 folds two line breaks (`:135-137`, ending mid-line
137); S082 omits the list number `2. ` before `:27`; S083 folds one line break (`:106-107`, beginning mid-line 106
after the load-path sentence). S086 (`:76`), S087 (`:57`) and S088 (`:164`, a substring of a table cell) are unshaped
spans of one line each (located in their own fetches by `A3RerunC1ByHand`, `A3Shipopencode` and `A3ShipCursor`).

### Rejected (opened or built this round, not admitted)

| item | when | reason | flip |
|---|---|---|---|
| C2 claim (info-less fence line classes, counter `check_infoless_fences.py` at `ee50d8fa`) | 04:20Z–04:45Z | four pre-freeze controls met the frozen predicate without the claimed work: a fence-blind patch keyed on case-directory names and the fixed real command lines (`CtlC2GeneratorKeyed`, 120 of 120 on two seed sets and 240 of 240 over six seeds), a patch keyed on the extraction path (`CtlC2DoNothingJunk`, 120 of 120 with the instrument self-test green and the live run byte-identical), character skips with an echo fallback (`CtlC2CharShortcuts`, 120 of 120), and a 50-line stub replacing the gate (`MutC2Counter`) | a counter that also requires the measured instrument's own self-test at its base assertion count, drives its scoring end to end in its self-test, and draws every token, name and command line from one distribution (`build/ExecC2CounterV3.md`, redesign input) |
| C1 counter v1 as the claim's rule (`ee50d8fa`) | 04:20Z–04:40Z | `CtlC1RealNoForm` (`5 of 7; new ground 4`), `CtlC1HeldVariant` (`5 of 5; new ground 3`), `CtlC1DoNothingJunk` world C and `CtlC1Fabricated` W5 (`7 of 7; new ground 3`) met it with bare words, nav text, a changelog line and case variants of held words | v2 (erratum 1), re-scored by the same five seats: best hollow world `found 1 of 7` (`controls/CtlC1*.md` § v2 re-score) |
| VS Code row token `.plugin/plugin.json` (Legacy OpenPlugin, `SrcVSCode` draft) | 05:05Z | VS Code's default manifest is the root `plugin.json` (`agent-plugin-reference.md:97`); leading with a legacy third-party format's path would pass the counter and say less than the truth (`CriticC1Rows`) | VS Code documents a VS Code-named manifest path |
| opencode `package.json` as the row token (`Srcopencode` draft) | 05:05Z | a published package's `package.json` (the build guide calls it a minimal manifest, `index.mdx:1769-1773`), not a plugin-specific manifest, and it fails the counter's grammar; the row names the plugin folder (wording corrected in attempt 3, `A3CriticMissHonesty` § 4) | none |
| GitHub Flavored Markdown spec as a new row for C2 (`ScoutC2Source`) | 04:55Z | C2 was withdrawn, and the CommonMark spec is already row S005; neither spec states that an info-less fence declares no language (the claim would rest on [INFERENCE]) | a C2 redesign that needs the source |
| Copilot CLI legacy manifest paths (`.github/plugin/plugin.json`, `.plugin/plugin.json`) | 05:05Z | they are listed on the CLI plugin reference, base row S028; re-citing a base URL for a counted row is barred, and the creation guide S082 names only the root `plugin.json` | none |
| Q42 quote swaps for S080 (`plugins.md:676`) and S083 (`reference.md:69`) (`A3ReviewEntryShape`) | 07:00Z | the quotes are counted by the frozen C1 counter, so a swap after measurement re-scores the claim; and two re-open seats read those lines as not stating the manifest location (`A3ReopenS080`: `:676` states path resolution; `A3ReopenS083`: `:69` names no root) | a round that re-quotes before measuring |
| Attempt-2 uncommitted candidate (`.ufo/waves/round-57/a3/a2-candidate.patch`, sha256 `2e681cf5…`) as landed text | 06:42Z–07:05Z | untrusted scratch of a dead attempt: its S086–S088 provenance cites residual seats and L1 re-opens no commit holds; its S079 note says "two sentences" (the line has three, `A3ReopenS079`); its S088 teaches cell says `or` where the page has a conjunction (`A3CandS088`); its opencode cell says `package.json` is "the only file its docs call a manifest" and quotes "a minimal manifest" across a line break (`A3Shipopencode`, `A3ReviewQuoteNotes`); its SKILL Cursor cell drops the `skills` field condition (`A3ShipCursor`). Each hunk was re-derived by an attempt-3 seat; only re-derived text landed | none |
| Band-10 attribution relabel in `SCORECARD.md:29` (`A3CriticScorecardCalib` M01) | 07:00Z | it re-grades a held score (consistency 10) from historical witnesses; the evidentiary ruling belongs to the non-author closure, not the lane; routed in the report | a closure ruling |
| Correction-sweep registry row for `agent-definition-files-round56.md:91` (`A3ReviewR2R6` F1) | 07:05Z | the text was corrected; adding a registry row changes a gate whose current arms let 7 of 11 mutants survive (`A3MutCorrectionSweep`, M68), so new rows wait for the arm repair | round 58 repairs the arms |

### Rows touched (old → new)

None in place. S079–S088 are new rows; S086 and S087 are append-only correction rows that supersede S080's teaches clause (scaffold contents) and S085's anchor (`plugins.mdx` does not resolve beside `index.mdx`); S080 and S085 stay `mined` → `mined`, recheck `90d` → `90d`, used-by unchanged. S005 and S028 are unchanged (S028 is now cited by the plugin entry for Copilot CLI component fields only).

## Corrections to round 56 (R2 — quote provenance)

- **S076 (Gemini CLI).** The quote recorded in `corpus/lessons/round-56.md:18` and
  `corpus/knowledge/agent-definition-files-round56.md:25` is the user-level location at `subagents.md:324`; it states
  `~/.gemini/agents/*.md` and supports the project token `.gemini/agents/*.md` only through substring matching. The
  project location is at `:323`, and the 23-word span `:320-323` (attempt 1 wrote 24, inherited from `ReopenS076S077.md:188`; `A3ReviewR2R6` F2) witnesses it without shaping. The quote cells are
  unchanged; the entry carries the correction in its quote-notes paragraph, registered in
  `verifiers/check_correction_sweep.py` (row `r57-r2-s076-note`).
- **S078 (opencode).** The recorded quote joins prose at `agents.mdx:41`, the fence info string `text` at `:43` and the
  example body at `:44`, with backticks stripped and whitespace folded; `text` is a fence label, not prose. Registered
  as `r57-r2-s078-note`.
- **`SKILL.md:109` clause.** "singular `agent/` still loads per a 2026-01-17 docs commit" had no SOURCES basis
  (`ReopenS078` F3); it now cites the pinned migration page `migrate-v1.mdx:486` (re-opened in round 56, HTTP 200,
  20,805 B, sha256 `f3d42b36…`, `.ufo/waves/round-56/falsify/ReopenS078.md:138-142`), which is not a SOURCES row.
  Registered as `r57-r2-skill-singular-agent`.
- **Round-56 report line 14.** `40c2b5eb`, `41c2f484` and `7639deba` are sandbox commits in
  `/fast/scratch/hyaku/kotoba-r56/` clones (their receipts: `controls/CtlC2Heuristics.md:5`,
  `CtlC2GeneratorKeyed.md:140`, `CtlC1RealNoForm.txt:27` in `.ufo/waves/round-56/`). The fleet report is not edited.

## Mistakes

M58–M61 are the round-56 spot-check routes R1, R2, R4 and R7, drafted by seat `ScribeMistakes` (`.ufo/waves/round-57/build/ScribeMistakes.md`) and checked by the L1; M62–M64 are this round's own.

- **M58 `sandbox-hash-unlabelled`** · `.ufo/reports/round-56/kotoba.md:14` cites `40c2b5eb`, `41c2f484` and `7639deba` without a `sandbox` label; the non-author spot-check says they do not resolve in the lane and are scratch-clone commits (`corpus/lessons/round-56-verifier-spotcheck.md:30-31,219-221`) · captured-by: the round-56 non-author spot-check (R1) · fix: label sandbox hashes with `sandbox` and their clone path in each context/report, or cite the committed receipt lines (`plans/round-57.md:81-85`; `.ufo/waves/round-57/bounds.md:4`) · shown able to fail: this read-only scan skips tokens explicitly introduced by `sha256` (digest prefixes, not commit references), checks unresolved 7–40-hex commit candidates with `git rev-parse --verify -q <h>^{commit}`, and prints the three unlabelled references:

  ```sh
  python3 -B -c 'import pathlib,re,subprocess; p=pathlib.Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md"); repo="/home/vgpnk/Projects/shokunin/kotoba-shokunin"; out=sorted({h for line in p.read_text().splitlines() if not re.search(r"\bsandbox\b",line,re.I) for h in re.findall(r"(?<![0-9a-fA-F])[0-9a-fA-F]{7,40}(?![0-9a-fA-F])",line) if not re.search(r"\bsha256\s+`?"+re.escape(h)+r"(?![0-9a-fA-F])",line,re.I) and subprocess.run(["git","-C",repo,"rev-parse","--verify","-q",h+"^{commit}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode != 0}); print("\n".join(out))'
  ```

  ```text
  40c2b5eb
  41c2f484
  7639deba
  exit code: 0
  ```

- **M59 `shaped-quote-note-unverified`** · the round-56 lesson's quote-note paragraph describes S076's project line and S078's fenced example inaccurately (`corpus/lessons/round-56.md:22-25`); the re-open found S076's quote verbatim but a better unshaped quote across `:320-323`, and that S078's `text` is a fence info string, not quote prose (`corpus/lessons/round-56-verifier-spotcheck.md:107-121,222-228`) · captured-by: the round-56 non-author source spot-check (R2) · fix: correct the S076/S078 notes (prefer S076 `:320-323`), accurately mark what was removed/normalized, and source or drop the separate `SKILL.md:109` clause as routed in R2 (`round-56-verifier-spotcheck.md:222-228`; `plans/round-57.md:83-85`) · shown able to fail: the source re-open caught the note/source mismatch for both entries; the spot-check says neither choice changed G's substance (`round-56-verifier-spotcheck.md:107-121`).

- **M60 `case-folded-held-ground`** · the round-56 counter case-folded held-ground counts and treated `.claude/AGENTS.md` and `.codex/AGENTS.md` as the lowercase agent directories, understating G (3 rather than 5) (`corpus/lessons/round-56-verifier-spotcheck.md:63-67,233-236`) · captured-by: the round-56 non-author spot-check (R4) · fix: the round-57 C1 v2 rule checks held paths case-insensitively at segment boundaries while keeping distinct new-ground values case-folded (`plans/round-57.md:35-40,114-118`; `verifiers/check_plugin_manifests.py:960-979`) · shown able to fail: CtlC1HeldVariant re-scored its exact v1 held-variant world under v2 as `0 of 0; new ground 0`, exit 1 (`.ufo/waves/round-57/controls/CtlC1HeldVariant.md:65-72`). This closes that world, but its bare tokens and duplicate rows also trigger other v2 guards, so it is not an isolated demonstration of the case-fold check. The frozen counter has explicit case-variant, segment-boundary and memory-file-analogue self-test cases (`verifiers/check_plugin_manifests.py:1681-1690`); I did not execute that self-test.

- **M61 `pattern-kill-no-cap`** · round-56's `ExecFloorsTimeout` used `pkill -f` on a shared scratch path, killed three sibling runs and ran a contention test that drove load to 96 (`.ufo/reports/round-56/kotoba.md:36`; `corpus/lessons/round-56.md:61-64`); R7 notes that M56's PID-only fix and contention cap had not been shown able to fail (`corpus/lessons/round-56-verifier-spotcheck.md:241-246`) · captured-by: the round-56 non-author spot-check (R7) · fix: round-57 bounds require killing only PIDs started by the seat and cap requested contention tests at 4 processes/120 seconds (`.ufo/waves/round-57/bounds.md:6`; `plans/round-57.md:85-87`) · shown able to fail: the required presence check distinguishes the old context from the new bound (the grep tests the PID sentence; the cap is independently visible on bounds line 6):

  ```sh
  grep -c 'Kill only by the PIDs you started' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-56/build-spec.json
  ```

  ```text
  0
  exit code: 1
  ```

- **M62 `target-above-reachable-population`** (the mined mistake) · C1's frozen target was F ≥ 5 of seven clients
  (`plans/round-57.md` § Claims), set before any census of how many clients document an own-format plugin manifest; the
  honest count is 4 (Claude Code, Codex, Gemini CLI, Cursor), so the landed table scores `plugin manifests found on the
  live page 4 of 4; new ground 4`, exit 1 (`.ufo/waves/round-57/C1-measure.txt`). The zero margin was reported
  during the build wave (`CriticAxisFit`, `ScoutPluginMcp`, `CriticC1Rows`, ~04:50–04:54Z), after the target was frozen · captured-by: none (the
  pre-freeze control wave asks whether a do-nothing control reaches the target, not whether honest content can) ·
  fix: Q45 — before freezing a per-client target, a seat that writes no content counts the clients whose own
  documentation states the claimed form under the counter's token rule, and the plan records that census with the target
  set at or below it; not yet shown able to fail (no round-58 plan exists).
- **M63 `bound-carried-by-reference`** · the pre-freeze control call's context named `bounds.md` and summarised the kill
  bound in lower case, so `grep -c 'Kill only by the PIDs you started' .ufo/waves/round-57/controls-call.json` prints 0
  (`.ufo/waves/round-57/r7-bound-grep.txt`) while the w0 and build contexts carry it verbatim · captured-by: Q44 (this
  round) · fix: every later context inlines `bounds.md`; the falsify call's grep is recorded in the report.
- **M64 `hollow-control-met-both-v1-counters`** · both v1 counters frozen at `ee50d8fa` were met by hollow worlds within
  25 minutes (Gate, Rejected rows 1–2): C1's token grammar admitted bare words and nav text; C2's generator leaked case
  names, fixed command lines and the extraction path · captured-by: the phase-4 pre-freeze control wave · fix: C1 v2
  (erratum 1), shown able to fail by the five seats' v2 re-scores (best hollow world `found 1 of 7`, exit 1); C2
  withdrawn, redesign input `build/check_infoless_fences_v3.py`.

### Attempt 3 (falsify wave of 40 seats, `.ufo/waves/round-57/a3/falsify/`; corrections to the rows above, then new rows)

- **M62 corrected** (`A3CriticMissHonesty` § 2–3, `A3CriticTargetCensus` § 1–2, `A3RerunC1ByHand`): "the honest count
  is 4" holds only under the row rule the entry chose after the freeze (own-format path, else the documented default).
  It is not a ceiling of the frozen grammar: VS Code's own page S081 documents Legacy OpenPlugin `.plugin/plugin.json`
  (`agent-plugin-reference.md:103-104`), which the grammar accepts, so a different client-neutral rule could reach
  F = 5 [INFERENCE: no seat built that world]; a reader accepts 6 of 7 rows as source-backed manifest locations
  (`A3RerunC1ByHand`). The shortfall under the chosen rule is one row, not zero margin. The miss stands as declared;
  no row was changed after measurement. · Q45 shown able to fail: `A3CriticTargetCensus` § 2 runs a record check over
  `plans/round-57.md` that prints `Q45 FAIL: no complete pre-Claims C1 census record; missing population, margin,
  command, receipt, seat; frozen target F>=5`, exit 1. Q45's census must count the population under the row rule the
  plan freezes with the target, not under the token grammar alone.
- **M63 corrected** (`A3ReviewContextsQ44`; receipt `.ufo/waves/round-57/a3/q44-context-grep.txt`): the build
  contexts did not carry the bound verbatim. A file-level grep finds it in `build-taskcall-sent.json` only inside the
  `ScribeMistakes` item prompt; the context itself prints 0 (`jq -r .context … | grep -c` → w0 1, controls 0, build 0,
  attempt-1 falsify 1, attempt-3 falsify 1). Q44's grep must read the `context` field, never the whole file. Shown
  able to fail: the context-level grep prints 0 on the controls and build records.
- **M64 clarified** (`A3ReviewMistakes` finding 1): `CtlC1HeldVariant`'s v2 world scores `found 3 of 3; new ground 3`
  because its tokens are the clients' real own-format paths (real ground, not hollow); the best hollow world is
  `found 1 of 7` (`CtlC1DoNothingJunk` world D). `A3ReplayHollowC1` rebuilt four worlds under v2: `0/0, 0/0, 0/6, 1/6`,
  all exit 1, matching the receipts.
- **M65 `quote-note-repeated-the-routed-defect`** · the same round that landed Q42 (from round-56 R2) wrote quote notes
  that call S079, S081 and S085 "one line each and unshaped" without saying each is one sentence cut out of a longer
  line, and the S080/S083 notes omitted that the quote ends or begins mid-line (`A3ReopenS079`, `A3ReopenS080`,
  `A3ReopenS081`, `A3ReopenS083`, `A3ReopenS085`, `A3ReviewQuoteNotes` F2) · captured-by: Q42 (landed this round, not
  applied to this round's own notes) · fix: the notes are corrected in the entry and in § Gate above; shown able to fail:
  five re-open seats each found the attempt-1 note incomplete against live bytes whose sha256 equals the row's.
- **M66 `dead-attempt-scratch-carried-provenance`** · attempt 2 left uncommitted SOURCES rows S086–S088 whose access
  cells cite its residual seats and "re-opened by the L1 05:44:34Z", records no commit holds (`a3/a2-candidate.patch`)
  · captured-by: the orchestrator rule that a dead attempt's uncommitted files are untrusted scratch · fix: the patch
  was saved, the files were reset to the branch, and each row was re-opened by an attempt-3 seat; the landed rows cite
  only those fetches. Shown able to fail: `grep -c 'residual seat' corpus/SOURCES.md` prints 0 at the attempt-3 tip and
  1 or more on the candidate patch (`grep -c 'residual seat' .ufo/waves/round-57/a3/a2-candidate.patch` → 4).
- **M67 `negative-overstated-against-own-source`** · "opencode plugins are code modules with no JSON manifest" (entry,
  SKILL.md row, LOG, Gate) while the pinned build guide S085 calls a published package's `package.json` a minimal
  manifest (`index.mdx:1769-1773`; `A3CriticMissHonesty` § 4, `A3RerunC1ByHand` F2) · captured-by: Q30 (a negative
  needs its sweep; the sweep missed a positive statement on the cited page itself) · fix: the entry, SKILL.md row and
  Gate reason now name the folder for local modules and `package.json` for published packages. Not yet shown able to
  fail as a rule.
- **M68 `correction-registry-arms-weak`** · the four new self-test arms and three new registry rows of
  `verifiers/check_correction_sweep.py` (round-56 R2 corrections) let 7 of 11 mutants survive: three weakened
  declaration patterns and all four dropped arms (`A3MutCorrectionSweep`) · captured-by: none (R5 asked this of the C1
  counter, not of the sweep) · fix: routed to round 58 (one arm per row that fails when the row's stale pattern is
  weakened); not fixed this round.
- **M69 `item-premise-false`** · the attempt-3 falsify item `A3RerunC1Counter` asked for the counter's sha256 at the base
  revision, where the file does not exist (`fatal: path 'verifiers/check_plugin_manifests.py' exists on disk, but not
  in '47c05558…'`); the seat reported it and verified the frozen bytes at `01312a77` instead · captured-by: the seat ·
  fix: an item that names a file at a revision checks `git cat-file -e <rev>:<path>` before dispatch.
