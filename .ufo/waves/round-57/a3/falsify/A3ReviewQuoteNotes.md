Result: MIXED — the candidate's plugin-folder sentence, its new quote-position notes (except one miscount), and the row-rule additions verify byte-true against live pages I fetched myself; but the candidate's S079 note counts two sentences where the line has three, its residual-reports citation dangles, its `"a minimal manifest"` is itself a shaped quote, and the committed lesson Gate quote-notes paragraph (`corpus/lessons/round-57.md:22-25`) still carries the round-56 R2 defect class — S079/S081/S085 are called `unshaped` while being the same kind of contiguous substring as S084.

Scope: opening paragraph + quote-location paragraph of `corpus/knowledge/plugin-manifests-round57.md` @ `07c33d73ddce769d9cea2846a6313164401b5478`, reviewed against `.ufo/waves/round-57/a3/a2-candidate.patch` (untrusted); lesson Gate quote-notes `corpus/lessons/round-57.md:22-25`. Adjacent clauses touched only where they share a sentence I must verify.

## Fetches (ordinary curl, no shaping)

`date -u`: start Fri 23 Oct 2026 06:49:09 AM UTC, end 06:49:10 AM UTC (+404 check 06:51:47Z). Bytes under `/fast/scratch/hyaku/kotoba-r57a3/A3ReviewQuoteNotes/fetch/`. Every seat-recorded sha256 reproduced exactly — seat bytes and live bytes are identical.

| tag | URL | HTTP | bytes | sha256 | matches seat receipt |
|---|---|---|---|---|---|
| S079 | https://code.claude.com/docs/en/plugins-reference.md | 200 | 42,124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` | yes |
| S080 | https://developers.openai.com/plugins/build/plugins.md | 200 | 38,036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` | yes |
| S081 | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 200 | 21,972 | `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e` | yes |
| S082 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | 200 | 7,711 | `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64` | yes |
| S083 | https://geminicli.com/docs/extensions/reference.md | 200 | 12,022 | `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` | yes |
| S084 | https://cursor.com/docs/plugins.md | 200 | 20,323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` | yes |
| S085 | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | 200 | 60,780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` | yes |
| S087 | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx | 200 | 4,371 | `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3` | yes (new row's claimed sha) |
| S088 | https://cursor.com/docs/reference/plugins.md | 200 | 30,324 | `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204` | yes (new row's claimed sha) |
| S028 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` | yes (matches row's `d0d362cc…`, 47,200 B) |
| beside-path | `…/build/plugins/plugins.mdx` (same dir as `index.mdx`) | **404** | — | — | confirms S087's correction basis |

## Verified claims (candidate holds)

- **Gemini folder**: `S083:106` reads `Gemini CLI loads extensions from `<home>/.gemini/extensions`. Each extension` — the candidate's `<home>/.gemini/extensions` (S083 `:106`) is byte-exact and correctly located. HOLD.
- **Cursor folder**: `S084:211` reads `You can also develop either format from `~/.cursor/plugins/local`. See` — "either format" is Agent Plugins + Cursor Plugins per the paragraph above (`:207-210`). Candidate claim byte-exact and correctly located. HOLD.
- **opencode folders**: `S087` `## Discover` at `:44`; `.opencode/plugins/` at `:46` + tree `:48-53`; `Global plugins use the same discovery layout under the OpenCode config directory.` `:57`; `~/.config/opencode/plugins/` `:59`. Candidate's `plugins.mdx:44-60` cite and both folder claims verify. HOLD.
- **`package.json` "minimal manifest" context**: `S085:1768` `## Publish`; `:1769-1770` `A package plugin uses the same default export as a local plugin. A minimal` / `manifest is:`; `:1773` `json title="package.json"`. The build guide does call it a minimal manifest — the *claim* holds (see F4 for the quoting defect). HOLD (claim), BREAKS (as quoted).
- **`.github/plugin/plugin.json` meets the counter's token grammar**: walked `token_well_formed` @ `07c33d73` (`verifiers/check_plugin_manifests.py:535-558`): TOKEN_RE matches, `plugin` word in segments, no `marketplace`, no interior-dot segment (E7 allows a leading dot: `.github`), final `.json` segment carries `plugin`, ≥2 segments, foreign-marker check clean (`github`/`plugin` name no other client; `MARKERS` at `:245`). S028's page lists it (`S028:402`, legacy locations). Candidate parenthetical "base row S028" is accurate — `git grep` at tip shows the literal `.github/plugin/plugin.json` only inside `corpus/lessons/round-57.md`'s rejected table, and S028's row is dated 2026-10-22. HOLD.
- **S082 creation guide default**: step 2 at `:27` names root `plugin.json`; `.github/plugin` appears nowhere on the S082 page (grep: 0 hits). "neither own-format nor the default its creation guide names" HOLD.
- **Candidate quote-position notes**: S080 "paragraph's first sentence, ending mid-line 137" TRUE (`:135-137`, period mid-line). S081 "middle sentence of a three-sentence line" TRUE (`:97`). S082 `plugins-creating.md:27` TRUE. S083 "quote begins mid-line 106, after the load-path sentence" TRUE (`:106` carries the load-path sentence then the quote's start). S084 "quote ends on `and`, and the link's word `variables` is not quoted" TRUE (`:28` ends `…hooks, and [variables](…)`). HOLD.
- **S085 sibling-name defect (corroborates S087)**: `plugins.mdx` beside `index.mdx` returns HTTP 404 (06:51:47Z); the real `content/plugins.mdx` has 143 lines and its Discover section sits at `:44-60`, not the `plugins.mdx:46-61,141-142` S085's anchor claims. The committed S085 anchor names a non-resolving file with ranges that fit no file in that tree position. HOLD (the correction is needed and correct).
- **Committed text still accurate where candidate doesn't touch it**: committed S080 "line breaks folded to spaces" (2 breaks), S083 "one line break folded", S084 substring note, S082 `step 2` note — all byte-true.

## Findings

### F1 — candidate S079 note miscounts the line's sentences (medium; same defect class it is fixing)

Candidate writes: `S079 plugins-reference.md:34, the first of two sentences on the line`. Fetched `S079:34` has THREE sentences:

`Save the manifest at `.claude-plugin/plugin.json` under the plugin root. Put every other plugin file at the plugin root, not inside `.claude-plugin/`. That includes `skills/`, `commands/`, and `hooks/`.`

Quote is sentence 1 of 3, not 1 of 2. old→new (in the candidate's replacement for the quote-location paragraph):

old: `S079 `plugins-reference.md:34`, the` / `first of two sentences on the line;`
new: `S079 `plugins-reference.md:34`, the` / `first of three sentences on the line;`

### F2 — committed lesson quote-notes `:22-25` keep an R2-class inconsistency (medium)

Byte facts: S079 quote = first sentence of three on `:34`; S081 quote = middle sentence of three on `:97`; S085 quote = first sentence of a line whose second sentence runs onto `:22` (`To load published packages` / `or plugin directories…`); S084 = strict interior substring (flagged). Under the paragraph's own standard — S084's same-line omissions are disclosed and it is still called "one line… and unshaped" — `unshaped` can only mean byte-verbatim; but then the S084 carve-out is noise, and under the stricter reading (nothing omitted around the quote) S079, S081 and S085 are shaped exactly like S084. Either way the sentence is internally inconsistent, and S083's fold note omits that the quote starts mid-line 106 — the round-56 R2 class (inaccurate quote notes; `corpus/lessons/round-56-verifier-spotcheck.md:189,222`).

old→new for `corpus/lessons/round-57.md:22-25`:

old:
```
Quote notes (each re-opened against the seat's fetched bytes by the L1, Q42): S079, S081, S084 and S085 are one line
each and unshaped (S084 is a contiguous substring: the list marker and bold label before it and the link after it are
not quoted); S080 folds two line breaks (`:135-137`); S082 omits the list number `2. ` before it; S083 folds one line
break (`:106-107`).
```
new:
```
Quote notes (each re-opened against the seat's fetched bytes by the L1, Q42): S079, S081, S084 and S085 are verbatim
contiguous substrings of one line each (S079 the first of three sentences on `:34`; S081 the middle of three on `:97`;
S084 a mid-line item: the list marker and bold label before it and the `variables` link after it are not quoted; S085
the first sentence of `:21`, which continues mid-sentence); S080 folds two line breaks (`:135-137`) and ends mid-line;
S082 omits the list number `2. ` before it (`:27`); S083 folds one line break (`:106-107`) and begins mid-line 106.
```
(each claim byte-checked above; keep or drop the position clauses together — partial disclosure was the R2 defect)

### F3 — candidate cites `.ufo/waves/round-57/attempt2/residual/`, absent at tip (low-medium)

`Re-derived against live bytes by the round-57 attempt-2 residual seats (`.ufo/waves/round-57/attempt2/residual/`)`. Neither the tip tree (`git ls-tree -r 07c33d73 -- .ufo/waves/round-57/attempt2/` → empty) nor the worktree has that path, and the patch adds no such files. If the L1 lands residual reports at that path the cite resolves; otherwise:

old: `by the round-57 attempt-2 residual seats` / `(`.ufo/waves/round-57/attempt2/residual/`).`
new: `by the round-57 attempt-2 residual seats` / `(seat reports under `.ufo/waves/round-57/attempt2/residual/`).` — only if landed; else `against the live bytes fetched 2026-10-23 (Gate-table sha256s).`

### F4 — candidate's `"a minimal manifest"` is itself a shaped quote (low)

Bytes `S085:1769-1770`: `A minimal` LF `manifest is:` — `"a minimal manifest"` folds a line break and downcases `A`. The same defect class the candidate corrects. Fix: paraphrase without quote marks — `which its build guide calls a minimal manifest` → `which its build guide introduces as "A minimal manifest" example`, or write `(a "minimal manifest" example, S085 `index.mdx:1769-1773`)` with `A` capitalized as the line starts it. Minimal-diff fix:

old: `calls a published package's `package.json` "a minimal manifest",` / `S085 `index.mdx:1770-1773`)`
new: `calls a published package's `package.json` "A minimal` / `manifest",` — awkward; RECOMMENDED instead: `introduces a published package's `package.json` as a minimal manifest (S085 `index.mdx:1769-1773`)` — drops the quote marks, no misquotation.

### F5 — S085 quote position left undisclosed in candidate's new paragraph (low)

S085 quote = first sentence of a line that continues mid-sentence (`:21` → `:22`). The candidate annotates the same shape for S079/S081/S084 but stops at `S085 `index.mdx:21`.` Optional disclosure, folded into the F2/first-block old→new: append `, the first sentence of the line, which continues mid-sentence onto :22` after `S085 `index.mdx:21``.

## Not re-verified (sibling scope)

S086 row body, SKILL.md cell edits, the Findings `4 of 4` parenthetical, and ship-cell content claims — assigned to sibling seats; nothing in my scope contradicts them. `~/.config/opencode/plugins/` and `~/.cursor/plugins/local` verified only against the two doc pages named, not against runtime behavior (candidate already labels both "vendor documentation").

## Residual risk

The `attempt2/residual/` cite is the only candidate reference I could not resolve to bytes; if the L1 lands the residual reports under that exact path, F3 closes with no edit. All fetched sha256s reproduce the seat receipts, so line-cited findings are stable against any same-pin refetch.

Tools installed/updated: none (curl, git already present; pacman untouched per pause).
