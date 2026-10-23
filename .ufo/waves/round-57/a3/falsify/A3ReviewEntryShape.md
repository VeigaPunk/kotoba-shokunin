Result: MIXED — `corpus/knowledge/plugin-manifests-round57.md` @ `07c33d73ddce769d9cea2846a6313164401b5478` clears front matter, recheck, sweeps and per-quote verification, but keeps two folded quotes although eligible unshaped quotes exist on the same pages (Q42), asserts an unmarked "documents none" negative for VS Code and Copilot CLI (Q30/Q14), and its Limits bullet both under-describes the counter and misdescribes the dotted-folder rule (Q31).

Scope: entry shape only — Q12–Q14, Q26, Q30, Q31, Q42, plus `verify_corpus_integrity.py` / `verify_corpus_independent.py` at the pinned rev. Reviewed state: `git show 07c33d73…:corpus/knowledge/plugin-manifests-round57.md` (80 lines) in a sandbox clone `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/clone` (HEAD `07c33d73`, read-only lane). The untrusted `a2-candidate.patch` was not used as evidence; every check below is against live fetched bytes or the committed tree.

## Fetches (all `curl -sSL`, ordinary means; `date -u` 2026-10-23T06:52:10Z)

| id | URL (final == requested) | HTTP | bytes | sha256 (matches seat record) |
|---|---|---|---|---|
| S079 | code.claude.com/docs/en/plugins-reference.md | 200 | 42,124 | `f2910dd6…` = SrcClaudeCode/SOURCES |
| S080 | developers.openai.com/plugins/build/plugins.md | 200 | 38,036 | `c37e330d…` = SrcCodex/SOURCES |
| S081 | code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 200 | 21,972 | `d6e10328…` = SrcVSCode/SOURCES |
| S082 | docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | 200 | 7,711 | `c0642867…` = SrcCopilotCLI/SOURCES |
| S083 | geminicli.com/docs/extensions/reference.md | 200 | 12,022 | `8b9eecb2…` = SrcGeminiCLI/SOURCES |
| S084 | cursor.com/docs/plugins.md | 200 | 20,323 | `74387ff9…` = SrcCursor/SOURCES |
| S085 | raw.githubusercontent.com/anomalyco/opencode/bdf75720…/index.mdx | 200 | 60,780 | `e505931a…` = Srcopencode/SOURCES |
| S028 | docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 200 | 47,200 | `d0d362cc…` = base SOURCES record |

Saved under `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/fetched/`; all eight sha256s reproduce the committed SOURCES/seat records byte-for-byte.

## Findings

### F1 — Q42: two shaped quotes kept although an unshaped quote exists on the same page (BREAKS Q42)

Q42 (QUALITY.md:53): "a quote that needs shaping (folded lines, stripped markup, a fence info string) is replaced by an unshaped quote from the same page when one exists."

- **S083 (entry :28, note :34):** quote `"Each extension must have a `gemini-extension.json` file in its root directory."` admits "(one line break folded)" — the fetched bytes are two lines:
  - `reference.md:106-107`: `must have a `gemini-extension.json` file in its root directory.` continues :106 `Gemini CLI loads extensions from `<home>/.gemini/extensions`. Each extension`.
  - **Unshaped eligible alternative exists** at `reference.md:69`, one physical line, 10 words, token inside backticks, `extension` outside the token:
    `Update an extension to the version specified in its `gemini-extension.json``
  - The seat itself drafted exactly this quote (`SrcGeminiCLI.md` § "Quote for the entry and `## Gate`"); the integrator chose the folded :106-107 instead. The only other token-bearing lines fail the quote grammar (:4 lacks a plugin/extension word outside the token; :222,:244,:304,:354 end in fragments or lack the outside word), so :69 is *the* replacement Q42 names.
  - Proposed fix (entry row :28, and the same swap in `corpus/lessons/round-57.md` § Gate row 11, since the counter requires the quote in Gate):
    - old: `"Each extension must have a `gemini-extension.json` file in its root directory."`
    - new: `"Update an extension to the version specified in its `gemini-extension.json`"`
    - and the note :34 `:106-107` (one line break folded)` → `:69` (one physical line, unshaped)`.

- **S080 (entry :25, note :33):** quote `"The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin."` admits "(line breaks folded to spaces)" over `plugins.md:135-137` — verified the fold: the sentence spans three physical lines at `:135-137`.
  - **Unshaped eligible alternative exists** at `plugins.md:676`, one physical line, 9 words, token inside backticks, `plugin` outside the token (`the plugin root`):
    `` `.codex-plugin/plugin.json`; the path still resolves from the plugin root. ``
    (context `:673-676`: `For the Codex compatibility format, put the same `extensions.com.openai.onboardingSkill` field in` / `:676`.) The other token-bearing lines fail the grammar (:26 plugin-word-only-inside-token span issue — `plugin` occurs only inside the token; :54, :66, :76, :136(=the folded one), :144, :563 are fragments or lack an outside plugin word).
  - Proposed fix (entry row :25 and § Gate row 8):
    - old: `"The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin."`
    - new: `"`.codex-plugin/plugin.json`; the path still resolves from the plugin root."`
    - and the note :33 `:135-137` (line breaks folded to spaces)` → `:676` (one physical line, unshaped)`.
  - Trade-off to record: :676 evidences the manifest path but not the scaffold sentence; if the L1 prefers :135-137 for content, the choice needs a stated reason — the criterion's default is replace.

### F2 — Q30/Q14: "where the client documents none" is an unmarked negative for VS Code and Copilot CLI (breaks-as-written; true on the evidence)

Entry :15-16: "The manifest cell leads with the client's own-format manifest path — a path whose folder or file name names the client — and, where the client documents none, with the default manifest its page names." For VS Code and Copilot CLI this asserts *the client documents no own-format path* — a "client X documents nothing about Y" negative (Q30, QUALITY.md:41; the sweep requirement, Q14 :25).

- The claim is **true**: S081's formats table (`agent-plugin-reference.md:99-104`: `plugin.json` ×2, `.claude-plugin/plugin.json`, `.plugin/plugin.json`) and Copilot CLI's documented locations (S082 `plugins-creating.md`; S028 `cli-plugin-reference.md:402`: root `plugin.json`, `.plugin/plugin.json`, `.github/plugin/plugin.json`, `.claude-plugin/plugin.json`) contain no `vscode`-/`copilot`-naming path. The absence is checkable by enumerating a closed list, not by open-ended search.
- But the entry **names no sweep and marks nothing**: the seat reports state the Q30 sweep was *not run* (`SrcVSCode.md` "Q30 is not applicable"; `SrcCopilotCLI.md` "not run because this page confirms a JSON manifest exists"). Q30's fallback is "the client is 'not checked', not 'silent'." The entry itself demonstrates the required disclosure elsewhere — the opencode negative carries "and its sweep in `Srcopencode.md` (docs tree, changelog, lane corpus)" (:77-78) — so the two parallel negatives are unmarked by the entry's own standard.
- Proposed fix (:15-16): old `and, where the client documents none, with the default manifest its page names` → new `and, where the client's documented locations name no client-named path — the enumeration of S081 `:99-104` for VS Code and S082 plus S028 `:402` for Copilot CLI is the sweep; no wider absence is claimed — with the default manifest its page names`.

### F3 — Q31: the Limits bullet under-describes the counter and misdescribes the dotted-folder rule (medium)

Entry :67-74. Two defects against `verifiers/check_plugin_manifests.py` @ `07c33d73` (sha256 `bf11a4ef…`, self-test `0 failure(s) over 235 assertions`):

- **Misdescription:** "(… no dotted folder, …)" (:68-69). The code's E7 accepts a non-final segment whose dot is the *first* character — `.claude-plugin`, `.codex-plugin`, `.cursor-plugin` are dotted folders and are the four passing tokens in the entry's own table (:24-29). As written the bullet names a stricter test than the code runs and contradicts the rows above it. Fix: `(E7) no dot inside a non-final segment other than a leading dot`.
- **Omission:** the bullet's implicit "these are the checks" reading leaves out checks a reader cannot re-derive, several of which fire at the tip revision. Observed `python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73… --fetch` prints `reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code` — the `shared by rows` disqualification (E5), the per-client unique-row rule, the Action-cell ≥3-word test, the exact heading/table-header read, quote-token case sensitivity, the SOURCES `docs` kind, tracker-URL rejection, and the `--fetch` redirect/boundary rules are all real checks (`check_plugin_manifests.py:64-69,100-144` spec; rejects observed live). The `docs`-kind and E5 gaps are material at tip: VS Code and Copilot CLI are rejected *by checks the Limits never mention*.
  - Proposed addition to the bullet: `… the quote in `corpus/lessons/round-57.md` § Gate, the SKILL.md row's uniqueness (one row per client, no token shared across client rows), an action cell of at least three words, the SOURCES row's `docs` kind and non-tracker URL, the case-sensitive token-in-quote match, and with `--fetch` the redirect rules and the token's page boundary;`.
- What the bullet gets right (verified against code): nothing it names is a cell or test the code does not read (Q31's core direction holds), and the trailing `It does not check the `What a plugin can ship` cells, the row rule above, or whether a client loads a plugin as documented` is accurate — the counter reads the ship column only as a header position.

### F4 — Corpus verifiers red at tip; the entry is one of the new unindexed files (medium, integration-level)

In the clone at `07c33d73`:
- `python3 -B verifiers/verify_corpus_integrity.py` → exit **1**: `unindexed: corpus/knowledge/plugin-manifests-round57.md` (also `corpus/lessons/round-57.md`, `corpus/lessons/round-56-verifier-spotcheck.md`); `commit_unresolvable: corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`; `4/9 checks pass`.
- `python3 -B verifiers/verify_corpus_independent.py` → exit **1**: same three unindexed files, same unresolvable commit.
- Before/after at base `47c05558` (fresh clone `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/base`): integrity exit 1 with `unindexed=1` (round-56-verifier-spotcheck only) and the same `451a02ff`; that commit is a known false positive — `round-54-verifier-spotcheck.md:147` already records it as the pinned `google-gemini/gemini-cli` upstream hash, not a lane object. **New drift attributable to this wave: `plugin-manifests-round57.md` and `round-57.md` have no coverage-map row in `corpus/README.md`** — the README's `:149` prose links the entry, but the index check reads only the File column of the coverage-map table. Fix is a README row, outside the entry file itself (L1 integration).

### F5 — Nits (low)

- **Citation-name inconsistency:** the S080 note (:33) cites `build-plugins.md:135-137` — the seat's scratch filename — while the SOURCES row and the front-matter URL name the same bytes `plugins.md`. Every other note names the SOURCES name (`agent-plugin-reference.md`, `plugins-creating.md`, `extensions-reference.md`, `plugins.md`, `index.mdx`). Recommend `plugins.md:135-137` (or the replacement cite from F1).
- **S082 cite granularity:** the note says `plugins-creating.md` step 2 (entry :34); the fetched bytes put it at `:27` (the lesson Gate table uses `:27`). Recommend adding the line number.
- **S081 substring unmarked:** the quote at :26 is a contiguous substring of `agent-plugin-reference.md:97` (mid-sentence start, mid-sentence end) and the note names only `:97`; S084's parallel substring carries an explicit "(…not quoted)" note (:35-36) while S081's does not. S085's quote is likewise a substring of `index.mdx:21` (sentence continues ` To load published packages…`). Q42 does not require notes for substring quotes — only shaped ones — but the asymmetry is worth one clause for consistency.
- **S084 note wording:** "(the list marker and bold label before it and the link after it are not quoted)" names categories, not the literal bytes (`- **Cursor Plugins**: ` before, ` [variables](https://cursor.com/docs/reference/plugins.md#variables)` after). "Names exactly which bytes" is met in substance — the bytes are uniquely identified — but the literal form used for `2. ` (:34) is tighter.
- **Counts without commands (borderline Q13):** `Seven clients` (:16), `Four of seven clients document` (:52), `One package` (:55) carry no command. Sibling precedent tolerates bare population counts (`agent-definition-files-round56.md:7` "seven clients' own documentation"), so this is convention-tolerance vs the literal `/CORPUS.md:34` rule; flagging because the assignment asked for it, not recommending a change.
- **`source:` front matter lacks anchors:** sibling entries name `(URL, `file:lines`)` per source; this entry's `source:` line (:2) names only URLs. The anchors do appear in the quote-locations paragraph (:32-36) — acceptable, noted for consistency.
- **`would pass the counter` (:19):** accurate for the token grammar but abbreviates — `.plugin/plugin.json` passes the *token rule*; backing still needs the other checks. The lesson Gate (:26 of the Gate table) records the fuller reason; suggesting `would pass the counter's token rule`.

## Verified — holds

- **Q12 front matter:** `source:` names S079–S085 with URLs matching the SOURCES rows; `verified-at: 2026-10-23` matches every row's `opened 2026-10-23`; `recheck:` resolves and runs.
- **Recheck runs as written:** `python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch` in the clone → exit **1**, output `counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` (the frozen v2 hash) and `plugin manifests found on the live page 4 of 4; new ground 4`. Exit 1 is the declared MISS reproducing (F=4 < 5); the command runs, which is what Q04/Q12 require. Rejects: VS Code + Copilot CLI (bare `plugin.json` — not well-formed, and E5-shared), opencode (`.opencode/plugins/` not well-formed) — exactly what the row rule predicts.
- **Every quote verified byte-exact at its cited location** against the fetched pages (all eight sha256s match the seat records): S079 `:34` ✓; S080 `:135-137` folded as noted ✓; S081 `:97` (substring) ✓; S082 `:27` minus the literal `2. ` as noted ✓; S083 `:106-107` folded as noted ✓; S084 `:28` contiguous substring as noted ✓; S085 `:21` (substring) ✓. Notes that exist are accurate.
- **opencode negative carries its three-part sweep** (:77-78 → `Srcopencode.md` § "Q30 sweep completed": CHANGELOG.md at the pinned commit, sparse-cloned docs source tree, lane-corpus search; all recorded with commands and results) — satisfies Q30/Q14.
- **S028 claim verified:** Limits :75-76 "Copilot CLI's legacy manifest locations are listed on the CLI plugin reference page" — `cli-plugin-reference.md:402` lists `.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, `.claude-plugin/plugin.json` for legacy plugins; S028 is a base row ✓ (present in `git show 47c05558:corpus/SOURCES.md`).
- **Q26:** the entry makes no counter-backed headline; its quantities are table-derived observations, and cross-client claims are labelled (`S081 :103` verified — the :99-104 formats table lists Claude's path; `ScoutPluginSweep.md` labelled "host observation"; `ScoutPluginMcp.md` labelled "reviewer reading"; the omp bullet :79-80 labelled "binary evidence… not a documented source"). No clause asserts what only the counter could show.
- **`What a plugin can ship` cells** are source-anchored per row and sit on the declared reviewer-judgment side; spot-checks passed (Claude `plugins-reference.md:617-629`; Gemini `:240-244` hooks-in-`hooks/hooks.json`; Cursor `:22-30` two-format split; opencode module-registration model `:10-22` verified).
- **Counter self-test:** `python3 -B verifiers/check_plugin_manifests.py --self-test` → `0 failure(s) over 235 assertions`, exit 0, sha256 `bf11a4ef…` = the declared frozen v2 hash.

## Residual risk / verification gaps

- The shaped-quote replacements in F1 must also land in `corpus/lessons/round-57.md` § Gate (rows 8, 11) — the counter matches the quote in both places; updating only the entry would desynchronize the pair (that file is another seat's scope; flagged for the L1).
- The `documents none` fix in F2 asserts only an enumeration-checked absence; if the L1 wants the stronger vendor-wide claim, the full three-part sweep must actually run for VS Code and Copilot CLI — it has not (both seats say so).
- `verify_corpus_*` DRIFT lines for `tracked_files`/`report_total`/`commit_total` are stale-`corpus-baseline.json` noise by design (same at base); the actionable drift is the two new unindexed files plus the pre-existing `451a02ff` false positive, which has no exclusion mechanism in either verifier.
- Not re-verified (out of scope): per-word quote counts beyond the observed counter run (the run's BACKED/reject lines already exercise them); the ship-cell line-anchors exhaustively (spot-checks only, listed above); whether `.plugin/plugin.json` for VS Code would have been found on the live page (the row was never drafted — the reject lines confirm it was not used).

Tooling: none installed or updated (pacman paused host-wide; nothing required). Sandbox clones: `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/clone` @ `07c33d73`, `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/base` @ `47c05558`; fetched pages under `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewEntryShape/fetched/`. No lane git/jj writes; only this report was written in the lane.
