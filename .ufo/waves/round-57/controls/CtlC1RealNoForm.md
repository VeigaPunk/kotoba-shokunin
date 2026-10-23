Result: BREAKS — the frozen C1 predicate is MET by a hollow world: `plugin manifests found on the live page 5 of 7; new ground 4`, exit 0, where not one row states its client's own plugin manifest; four of the five found tokens are changelog prose, a site-nav label, an extension *source file*, and a docs-page *link filename*.

## What was run (counter identity + measured revision)

Frozen counter copied from `ee50d8fa7b5d260fff8bc332f4a90513bee518ff` (never modified):
sha256 `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b`
(same bytes as the plan's C1-base receipt; `--self-test` not rerun here).

Sandbox: `/fast/scratch/hyaku/kotoba-r57/CtlC1RealNoForm`, cloned from the lane and checked out at
`ee50d8fa7b5d260fff8bc332f4a90513bee518ff`. Control commit **sandbox `a656c692be00793edb8c0b7296e32cdca0def688`**.
Measured revision = that sandbox commit. No lane or fleet git/jj writes.

Raw output: `.ufo/waves/round-57/controls/CtlC1RealNoForm.txt` (contains both runs, the `date -u` line, and exit codes).

```
$ python3 -B verifiers/check_plugin_manifests.py --rev a656c692... --fetch
counter sha256 2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b
counter rev a656c692be00793edb8c0b7296e32cdca0def688
plugin manifests found on the live page 5 of 7; new ground 4
Claude Code  BACKED token=plugin.json norm=plugin.json found=yes held-at-base=no
Codex        BACKED token=Extensions norm=Extensions found=yes held-at-base=no
VS Code      BACKED token=extension.ts norm=extension.ts found=yes held-at-base=no
reject Copilot CLI: no entry row names the client
Gemini CLI   BACKED token=writing-extensions.md norm=writing-extensions.md found=yes held-at-base=no
reject Cursor: entry row S105: quote holds no plugin/extension word outside the token
opencode     BACKED token=plugins norm=plugins found=yes held-at-base=yes
exit 0
$ python3 -B verifiers/check_plugin_manifests.py --rev a656c692...
plugin manifests backed 5 of 7; new ground not computed (needs --fetch)
exit 1
```

World scores: control world `--fetch` **F=5, K=7, G=4, exit 0 (MEETS)**; same world without `--fetch` B=5, exit 1.
Base comparison (from the plan's committed receipt `.ufo/waves/round-57/controls/C1-base.txt`): F=0 of 0, G=0, exit 1.

## Counterexample: what the five found rows actually are

Each row's "manifest" token is the first backticked span of the SKILL.md manifest cell; each entry quote is genuine page text, byte-verified (fetched bytes, line numbers below).

| client | SKILL "manifest" token | what it really is | what the quote really says |
|---|---|---|---|
| Claude Code | `plugin.json` | bare filename, not the documented `.claude-plugin/plugin.json` | a CHANGELOG bullet about `claude plugin validate` (line 1840) |
| Codex | `Extensions` | a **site-navigation label** on the docs shell, not a path | "Extensions Authenticate users Build skills Package your plugin" (line 51) |
| VS Code | `extension.ts` | the extension's **TypeScript source file**, not its manifest (`package.json`) | "However, let's focus on `package.json` and `extension.ts` …" (line 52) |
| Gemini CLI | `writing-extensions.md` | the filename of a **link to another docs page**; page never names `gemini-extension.json` | "- **[Build extensions](writing-extensions.md):** Create your first extension" (line 30) |
| opencode | `plugins` | a bare word in CHANGELOG prose | "- Added startup plugin seeding … `OpenCode.create({ plugins })` …" (line 558) |

Cursor was rejected only because its one real sentence holds `plugin` once ("no plugin/extension word outside the token"); Copilot CLI was rejected because `docs.github.com` paths I tried 404'd (evidence below). Neither rejection is a form check.

The underlying shortcut is structural and cheap: `token_well_formed` only requires *some* path segment, split on `-._`, to case-fold to `plugin(s)`/`extension(s)`. So `extension.ts`, `writing-extensions.md`, `Extensions`, `plugins` are all "manifests". The counter then checks that the token occurs on the cited page and in the quote — never that the token names a manifest file, that it is the client's documented location, or that the page states it. Provenance (`kind docs`, `tier A`, `status mined`, the "teaches" claim) is entirely self-declared in the author's own SOURCES row, and a changelog/file link is accepted as `docs`.

## Second defect: G counts a capitalised word as new ground

`new_ground` case-folds for *distinctness* but looks the held map up with the case-preserved token (`if not held.get(t)`), and `held_in_base` is case-sensitive. Measured: the base tree **holds** `extensions` (case-sensitive, path-segment boundary) but does **not** hold `Extensions`. Probe against the frozen counter's own functions at `BASE_REV`:

```
HELD 'extensions'   wf=True held=True
HELD 'Extensions'   wf=True held=False      (implied by counter line: held-at-base=no)
HELD 'plugins'      wf=True held=True
HELD 'plugin.json'  wf=True held=False
HELD 'extension.ts' wf=True held=False
```

So a data seat can manufacture new ground by capitalising a word already held at base. In this world G=4 instead of the honest 3 (`plugin.json`, `extension.ts`, `writing-extensions.md`); the predicate would still pass at G=3, which shows the case hole is a free bonus, not the only route.

## Source access evidence (quote is genuine; page does not state the manifest)

Access times are the pasted `date -u`-stamped lines in the raw output / fetch log; status, bytes and sha256 from the fetch that fed the counter.

| URL | UTC | HTTP | bytes | sha256 | quote line |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2026-10-23T04:17:01Z | 200 | 1,081,887 | `adb803f8e1d19f3f678b8374de6db1223e9cb8afe2f8034f4b7cb618989997d9` | 1840 |
| https://developers.openai.com/codex/changelog | 2026-10-23T04:18:15Z | 200 | 1,714,171 | `ff7fcbe9319a5eb49a7eb9eafc6bcad824c41061ea3fd1825435dabe8a51a772` | 51 |
| https://raw.githubusercontent.com/microsoft/vscode-docs/main/api/get-started/extension-anatomy.md | 2026-10-23T04:17:48Z | 200 | 7,518 | `e9dba3344a4b189117ac848136508ab844dbf8aafa9331ff388f8693e6dee931` | 52 |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/extensions/index.md | 2026-10-23T04:17:02Z | 200 | 1,781 | `ba0bfc2f0dde9d780e29ad2b37446eeeff7c760052682c0f25e592a02bbffecf` | 30 |
| https://raw.githubusercontent.com/sst/opencode/dev/CHANGELOG.md | 2026-10-23T04:17:02Z | 200 | 50,001 | `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b` | 558 |
| https://cursor.com/changelog (rejected row) | 2026-10-23T04:17:49Z | 200 | 204,106 | `f1bb810497168fff3aa28afab07c4a0b3b1eeb9c069ca23ddaf782b18486d15a` | 33 |
| https://docs.github.com/en/copilot/concepts/agents/copilot-extensions (rejected) | 2026-10-23T04:17:49Z | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` | — |
| https://raw.githubusercontent.com/github/copilot-cli/main/CHANGELOG.md (rejected) | 2026-10-23T04:18:15Z | 404 | 14 | `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed` | — |

Quotes (≤25 words, byte-exact from the fetched bytes; `extension.ts` page line 52, etc.) are recorded in the sandbox files `corpus/knowledge/plugin-manifests-round57.md`, `corpus/lessons/round-57.md` (§ Gate) and `corpus/SOURCES.md` rows S101–S106 at sandbox `a656c692`. Gemini check: `grep -c gemini-extension gemini-extindex` → `0` (the page names no manifest at all).

## Impacted axes

- **depth (C1's axis)**: the predicate is satisfied with zero knowledge about where any client's plugin manifest lives. A reader following the control's table would look for `extension.ts`, `writing-extensions.md`, a nav label and a changelog word. The claim's own sentence ("where the plugin (or extension) manifest lives") is not measured.
- **calibration**: the predicate cannot distinguish the claim from a real-text pastiche; short-circuiting is cheap (one fetch of any page on a pinned host with the word "plugin"/"extension" plus a changelog quote).
- **consistency**: `token_well_formed` admits non-path words (`Extensions`, `plugins`) and source files (`extension.ts`), so SKILL.md's vocabulary and the claim's vocabulary diverge; the case-sensitive held map vs case-folded distinctness is an internal inconsistency (round-56 R4 fixed a false *match*; it also opened a false *miss*).
- **adjacency/freshness**: not moved; stated for completeness.

## Smallest safe correction (for the canonical judge to weigh, not applied)

1. **One rule in `judge`**: after `token_well_formed`, require the token to hold **at least two path segments and a final segment ending `.json`** (a manifest *file path*). Kills every token in this world (`plugin.json` has one segment; `Extensions`, `plugins`, `extension.ts`, `writing-extensions.md` fail), without touching a genuine row (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `gemini-extension.json`). [INFERENCE] VS Code is the awkward client under this rule because its extension manifest is `package.json` (no plugin/extension word), so either VS Code's row needs a documented plugin-bearing path (e.g. `.vscode/extensions.json`, unverified here) or the plan drops VS Code from the seven; the control shows the frozen token rule cannot tell which of the two it is.
2. **Ground hole (independent, one line)**: make the held lookup match case-insensitively for the *ground* decision only — count a norm as not-new whenever `casefold(norm)` has any base occurrence in any case — keeping the held *report* case-sensitive as round-56 R4 requires.
3. **Cheap provenance hardening (optional)**: require the SOURCES `anchor` cell to name a line/heading and the quote's surrounding page heading to contain `plugin`/`extension` (one extra regex pass), which rejects site-nav and changelog-sentence rows without new fetch logic.

With (1) alone, this control scores F=0; with (1)+(2) the G inflation route closes too.

## Bounds compliance

Sandbox clone at the freeze commit; sandbox commit labelled; all shell commands wrapped in `timeout`; no `pkill`/`killall`; no lane/fleet git or jj writes; only this report and the named raw-output file were written in the lane; no model CLI calls; no tool installs or upgrades were needed (none performed).

## v2 re-score

Counter v2, copied verbatim from `01312a77e36317feb6e961aba77841ddab1225ca:verifiers/check_plugin_manifests.py`,
sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` (matches the erratum). Run in the same
sandbox `/fast/scratch/hyaku/kotoba-r57/CtlC1RealNoForm`, same control world commit **sandbox `a656c692be00793edb8c0b7296e32cdca0def688`**, `--fetch`:

```
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev a656c692be00793edb8c0b7296e32cdca0def688
plugin manifests found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md manifest token 'plugin.json' is not well-formed; entry row S101: S101 URL '…/claude-code/main/CHANGELOG.md' is a changelog/release/news/blog page, not documentation
reject Codex: SKILL.md manifest token 'Extensions' is not well-formed; … shared by rows Codex, Copilot CLI; entry row S102: S102 URL 'https://developers.openai.com/codex/changelog' is a changelog/release/news/blog page, not documentation
reject VS Code: SKILL.md manifest token 'extension.ts' is not well-formed
reject Copilot CLI: SKILL.md manifest token 'extensions' is not well-formed; … shared by rows Codex, Copilot CLI; no entry row names the client
reject Gemini CLI: SKILL.md manifest token 'writing-extensions.md' is not well-formed
reject Cursor: SKILL.md manifest token 'plugin' is not well-formed; entry row S105: quote holds no plugin/extension word outside the token; S105 URL 'https://cursor.com/changelog' is a changelog/release/news/blog page, not documentation
reject opencode: SKILL.md manifest token 'plugins' is not well-formed; entry row S106: … CHANGELOG.md … changelog/release/news/blog page, not documentation
exit 1
```

**v2 world score: F=0 of 0, G=0, exit 1 — not met.** Every v1 route this world used is closed: the `.json`
final-segment + ≥2-segment/own-marker rule rejects all five found tokens; the changelog-path rule rejects all four
changelog sources; the shared-token rule fires on the bare words `Extensions`/`extensions`.

### Adaptation attempt (time-boxed, hollow only)

Scanned all 15 pages already fetched for a v2-valid token (final segment `.json`, plugin/extension word, ≥2 segments
or the row's own marker) that does **not** state the client's own manifest location. The only hit anywhere was
`.codex-plugin/plugin.json` on `https://developers.openai.com/codex/changelog` — rejected twice over (changelog path;
and it is Codex's own manifest, not hollow). One further fetch,
`https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/configure/extensions/extension-marketplace.md`
(2026-10-23T04:37:09Z, HTTP 200, 30,018 B, sha256 `fc8cda0b49e569524cd6d2bce34ad28e22e5502de961ca5d90bcc3293514a16a`),
mentions `extensions.json` only as a bare filename (lines 260, 264) and never the path `.vscode/extensions.json`, so no
v2-valid non-manifest token exists there either (single-segment `extensions.json` carries no client marker).

No hollow world was found within the 5-minute adaptation box; best v2 score is the re-score above, `0 of 0; new ground 0`,
exit 1. Non-defect check: v2's `token_well_formed(token, client)` is grammar-only per client and the foreign-marker
guard is still applied in `judge` (v2 lines 741-744), so the `.codex-plugin` token would also be rejected for any other
client. The residual surface v2 still does not measure (self-declared `kind docs`/`tier A` naming a page's nature) was
not exercised: no page found that both lacks changelog/release/news/blog in its path and carries a v2-valid token.
