# CtlC1HeldVariant — C1 held-variant control (round 57, attempt 1, pre-freeze)

Result: MIXED — the held-variant control MEETS C1's frozen predicate (`--fetch` exit 0, F=5, G=3) with three case/suffix variants of words already held at base (`Plugins`, `Extensions`, `plugin.json`) quoted from page navigation/boilerplate and zero per-client manifest facts, while every re-cited base-URL variant (8 normalisation forms, 1 redirecting alias host) is correctly rejected by the frozen counter.

## Counter, revisions, receipts

- Counter under test: the FROZEN `verifiers/check_plugin_manifests.py` at `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`, copied unmodified into the sandbox. Counter sha256 (printed by the counter itself on every run): `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b` — identical to the lane copy at freeze (sha256 over the freezer file's own bytes).
- Base: `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`; measured revisions are sandbox commits, labelled per bounds:
  - sandbox `bb261d31b0b8a40a17fcb6613a625cee4ca18635` (/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1HeldVariant) — World B (case/suffix variants, same token on two client rows): **exit 0**.
  - sandbox `0fc9ffa861ac703eb52abd3ee79f3ebe99d69389` — World A2 (re-cited base URLs): exit 1 as expected.
- Raw counter output receipt: `.ufo/waves/round-57/controls/CtlC1HeldVariant.txt` (both scored runs verbatim, plus frozen-code probes). This report is the second receipt. No data seat exists; both worlds are hollow sandbox-only controls, never intended for landing.

## How the passing world is built (World B, sandbox bb261d31)

Five client rows (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI), the cached `### Plugin manifests by client` table, entry rows quoting live pages, and new SOURCES rows S086–S090 (opened 2026-10-23, tier A, `mined`, on each client's pinned host). The manifest tokens are:

| client | token | live page (requested URL) |
|---|---|---|
| Claude Code | `Plugins` | code.claude.com/docs/en/plugins |
| Codex | `Plugins` | developers.openai.com/codex/plugins (→ learn.chatgpt.com/docs/plugins) |
| VS Code | `Extensions` | code.visualstudio.com/docs/editor/extension-marketplace (→ …/configure/extensions/…) |
| Copilot CLI | `plugin.json` | docs.github.com/en/copilot/concepts/agents/about-plugins (→ …/customizations/plugins) |
| Gemini CLI | `Extensions` | geminicli.com/docs/extensions/ |

The quotes are contiguous word-windows of the counter's own page normalisation (case-preserving) — they are navigation/boilerplate, e.g. “Claude Code Search... Navigation Plugins Plugins overview Getting started Build with”, “Shortcuts Settings Settings Sync Extensions Overview Extension Marketplace Extension Runtime Security”. Every quote was verified with the frozen `found_on_page` before writing the world; the counter then re-fetched each page itself. Sentences and tokens are byte-verbatim page text, not invented (fetch receipts: UTC 2026-10-23 ~04:17Z, HTTP 200; sha256 of the fetched bytes in the raw receipt; the counter's own fetch re-verified them at run time).

Output (verbatim in the raw receipt):

```
plugin manifests found on the live page 5 of 5; new ground 3
Claude Code  BACKED token=Plugins norm=Plugins found=yes held-at-base=no
Codex        BACKED token=Plugins norm=Plugins found=yes held-at-base=no
VS Code      BACKED token=Extensions norm=Extensions found=yes held-at-base=no
Copilot CLI  BACKED token=plugin.json norm=plugin.json found=yes held-at-base=no
Gemini CLI   BACKED token=Extensions norm=Extensions found=yes held-at-base=no
[exit 0]
```

## Counterexample: G and F are both inflatable

1. **G inflation by case/suffix variant of base-held text (assignment arm 2).** The new-ground test is case-sensitive (frozen spec: “the held test itself stays case-sensitive”, round-56 R4). The base tree holds `plugins`, `extensions`, `plugin`, `Extension`, `Plugin` (probe, raw receipt); it does not hold the spellings `Plugins`, `Extensions`, `plugin.json`. Held lookup is keyed by the token as spelled, while G dedupes only among the *counted* found clients. So the same underlying English word, written with a capital letter (or with `.json` appended), counts as new ground. Probe (frozen `held_in_base` on meta): `Plugins` held=False, `Extensions` held=False, `plugin.json` held=False; `plugins` held=True, `extensions` held=True, `plugin` held=True. All three new-ground values are therefore variants of text already present at base — the table adds zero new corpus knowledge, and the manifest cells are not manifest locations at all (a bare word, a bare word, a generic filename).

2. **F inflation by the same token on two client rows (assignment arm 3).** F counts found *clients*, not distinct tokens: `Plugins` appears on the Claude Code and Codex rows, `Extensions` on the VS Code and Gemini CLI rows. F=5 is reached from 3 distinct tokens; the predicate is met exactly (F=5 ≥ 5, G=3 ≥ 3). The world states no “What a plugin can ship” fact (all action cells are the same three words), no per-client manifest location, nothing beyond generic navigation prose.

3. **URL re-citation (assignment arm 1) is rejected — verified, not assumed.** All seven World A2 rows are rejected solely on `S### URL '…' is already a base SOURCES URL`: `http://` scheme, trailing `/`, `.md`, `?query`, `#fragment`, path case (`SKILLS`), and `.md/` — each maps to the same `url_key` as a base row (probe prints all eight normalisations). The redirecting alias host `docs.anthropic.com/en/docs/claude-code/skills` passes the row-level checks (new url_key, pinned host) and is BACKED, but is not FOUND: the frozen `fetch()` raises `OSError: reached a base SOURCES URL https://code.claude.com/docs/en/skills`. The alias serves byte-identical content (sha256 `6418a66d…` == `6418a66d…`), and `found_on_page` on those bytes is True — so the post-redirect guard is load-bearing and works.

## Impacted axes

- **depth** — the axis C1 claims to advance: the frozen predicate certifies a 5-client, 3-ground world in which no manifest location, no per-client manifest, and no shipping rule is stated. The counter cannot distinguish depth from three case-variants of words already in the base tree.
- **calibration** — a Q25-style mutant exists and *passes*: removing all real content (replacing manifest cells with English words) does not change the counter's verdict; the counter thus has no discriminating power for the claimed content.
- **consistency** — the G rule is asymmetric: it casefolds *across* found clients but not *against* the base tree. `Plugins` on two clients counts once, yet `Plugins` vs base-held `plugins` is treated as brand-new ground. Also the token grammar accepts a bare word (`plugin`, `Plugins`) with no path separator, so “manifest token” ≠ manifest path.

## Smallest safe correction (for the L1 / counter owner; a stricter erratum committed before any content per the plan)

1. Make the new-ground held test case-insensitive: casefold the normalised token and scan the base blobs for the casefolded form at the same boundaries (FOUND's exact-case token match on the live page can stay). This alone drops World B's G to 1 (`plugin.json`), so the predicate fails (G=1 < 3).
2. Require the manifest token to contain at least one `/` (a directory component) — or to be exactly one of a frozen per-client filename list — which rejects bare words and `plugin.json`. With (1), World B's G becomes 0. Either change alone breaks the passing world; both together also make `plugin.json`-style generic filenames unusable.
3. Optionally, count F by distinct casefold(normalise(token)) (as G already is), so duplicated tokens across client rows cannot inflate F.

## Residuals / what was not claimed

- If a pinned alias host served byte-identical content with HTTP 200 and no redirect, the counter has no content-hash check and would accept it as a new source. Not observed on the tested alias (docs.anthropic.com redirects today). [INFERENCE] applies to *other* alias pairs.
- Segment variants of base-held paths also escape: `.opencode/plugins` is not held (base holds `.config/opencode/plugins`) and is found on opencode.ai/docs/plugins/ — a fourth ground available to the same construction; not used in the passing world.
- The control worlds are hollow and sandbox-only; no real C1 content was written in the lane or intended for landing. No tools were installed (probe used the frozen counter module and curl only).

## v2 re-score (erratum 1)

V2 counter copied from `01312a77e36317feb6e961aba77841ddab1225ca` into the same sandbox clone, unmodified; counter sha256 printed on every run: `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`.

- Re-scored the exact v1 worlds: sandbox `0fc9ffa861ac703eb52abd3ee79f3ebe99d69389` (World A2) → `0 of 0; new ground 0`, exit 1; sandbox `bb261d31b0b8a40a17fcb6613a625cee4ca18635` (World B) → `0 of 0; new ground 0`, exit 1. The `Plugins`/`Extensions` bare tokens and `plugin.json` are now rejected by the v2 path shape; duplicated tokens are also rejected. World A's URL variants still report base-URL duplicates on the rows that reach that check.
- Best adaptation scored: sandbox `eda859eea320eba917d1140c2f4bf77211c4e254` (/fast/scratch/hyaku/kotoba-r57/KotobaR57.CtlC1HeldVariant), using three distinct v2-shaped tokens found on the three client pages scanned: Claude Code `.claude-plugin/plugin.json`, Gemini CLI `gemini-extension.json`, Cursor `.cursor-plugin/plugin.json`. Each quote is at least six words, each token is unique to its client row, and the counter reports each found and not held at base. Score: **F=3 of K=3; G=3; exit 1**. The v2 predicate is not met because F<5.
- This adaptation did not recover a five-client hollow pass: the original v1 hollow world is closed by v2's final-`.json`/path-shape checks, case-insensitive held scan, quote floor and duplicate-token disqualification. In my scan of the cached pinned pages and the additional Gemini/opencode pages, only these three distinct client tokens matched the v2 token shape and page-boundary test; this finite scan is not a claim about every possible pinned URL.
- v2 therefore closes the specific v1 G/F counterexample in this held-variant world. No v2 predicate-meeting hollow world was found. All v2 receipts and full reject details are appended to `CtlC1HeldVariant.txt`.
