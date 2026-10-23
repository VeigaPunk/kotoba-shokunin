Result: DONE — verdict ADMIT AS WRITTEN: the untrusted S087 row's URL, bytes, anchors and every factual claim verify byte-exact against the pinned opencode tree, and its 11-column shape conforms to the v1 contract.

# A3CandS087 — verification of candidate SOURCES row S087 (untrusted)

Source of the row under test (claims, never evidence): `.ufo/waves/round-57/a3/a2-candidate.patch` line 38. Scratch dir: `/fast/scratch/hyaku/kotoba-r57a3/A3CandS087/` (fetched bytes only; the lane was read-only). Lane revision checked: `07c33d73ddce769d9cea2846a6313164401b5478`. No tools installed (curl, git, awk, sha256sum already present; pacman untouched).

## Access record — this seat's opening (round 57, attempt 3)

```
$ date -u
Fri 23 Oct 2026 06:46:53 AM UTC
$ curl -sS -o plugins-mdx.bin -w 'HTTP %{http_code} | %{size_download} bytes\n' \
  'https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx'
HTTP 200 | 4371 bytes        (curl_exit=0)
$ sha256sum plugins-mdx.bin
39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3
```

Byte-identical to the row's claim (HTTP 200, 4,371 B, sha256 `39afa2…`) and to S085's committed sibling-fetch record (04:47:59Z, same byte count and sha). The row's source is therefore admitted as opened this round: this is that opening.

Supporting fetches/probes, same session:
- `date -u` `Fri 23 Oct 2026 06:47:18 AM UTC` — `…/services/www/src/docs/content/build/plugins/plugins.mdx` → **HTTP 404**, 14 B body `404: Not Found`; `…/content/build/plugins.mdx` → **HTTP 404**, 14 B.
- `…/content/build/plugins/index.mdx` (S085's page) → HTTP 200, 60,780 B, sha256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` — matches S085's committed record.
- `date -u` `Fri 23 Oct 2026 06:49:00–06:49:01 AM UTC` — GitHub tree API `…/git/trees/bdf7572…?recursive=1` → HTTP 200, 2,971,864 B, `"truncated": false`, 9,534 paths. Under `services/www/src/docs/content/` exactly two files named `plugins.mdx` exist: `content/plugins.mdx` (the fetched page) and `content/cli/plugins.mdx` (blob sha `c1ecb0ff…` ≠ `39afa2…` — a different page). **No `plugins.mdx` anywhere under `content/build/`** — the 404 claim is exhaustive, not a two-URL sample.

## Claim-by-claim vs fetched bytes (line numbers in `plugins-mdx.bin`)

| Claim in row | Evidence | Verdict |
|---|---|---|
| URL = `…/content/plugins.mdx` @ `bdf7572…` | fetch reproduces 200 / 4,371 B / `39afa2…` | holds |
| `§ Discover (plugins.mdx:44-60)` | `:44` = `## Discover`; `:46-47` = "OpenCode also loads direct `.ts` and `.js` files and immediate plugin package directories from every discovered `.opencode/plugins/` directory."; `:49-55` = tree diagram `.opencode/ └── plugins/` | holds |
| `global folder :57,60` | `:57` = "Global plugins use the same discovery layout under the OpenCode config directory."; `:60` = `~/.config/opencode/plugins/` | holds |
| scope "discovery folders, project and global (vendor documentation; not runtime behavior)" | project folder `:46-47,50-55`; global `:57,60`; page also states `:63-64` a `plugins/` dir beside `opencode.json(c)` is *not* auto-discovered — consistent, no contradiction | holds |
| teaches: "its anchor names this page only as `plugins.mdx`" | S085's committed anchor tail (patch line 36 = tip's row): "sibling discovery page `plugins.mdx:46-61,141-142`" — basename only. It genuinely names *this* page: S085's recorded sibling fetch (4,371 B, `39afa2…`) is byte-identical to my fetch, and its cited lines land here (`:46-61` = Discover body, `:141-142` = `<Card title="Build a plugin" href="/build/plugins">`) | holds |
| teaches: "a path that does not resolve beside `index.mdx` (HTTP 404)" | `index.mdx` sits in `content/build/plugins/`; sibling `plugins.mdx` there → 404 (above); tree API confirms no `plugins.mdx` under `content/build/`; the real file lives two levels up at `content/plugins.mdx` | holds |
| teaches: "the global discovery folder `~/.config/opencode/plugins/` is stated here, not on S085's page" | literal at `plugins.mdx:60`; `grep -niE 'global\|config.*dir\|\.config' index-mdx.bin` → only `:1185` and `:1255`, both about "canonical directory"/"configuration adapters", unrelated to plugin discovery; `grep -n '.config/opencode' index-mdx.bin` → no hits | holds |
| teaches opens `supersedes S085 —` | contract v1 rule 2 correction format | holds |

## Column shape vs contract

- Header at tip `corpus/SOURCES.md:12` = 11 columns: `id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by` (v1 contract at `/home/vgpnk/Projects/shokunin/CORPUS.md:86-108`).
- Reconstructed row parses `awk -F'|'` → **NF=13** (11 cells), no `|` inside cells. Cells: `S087 | <source> | docs | A | <scope> | <anchor> | <teaches> | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md` — order and enum values all valid.
- `id` S087: absent from tip's SOURCES.md (registry ends at S085); S086 is the companion row in the same patch — "next unused" rule intact.
- `used-by` target exists at tip (`corpus/knowledge/plugin-manifests-round57.md`, blob `9e0a027`) and the same patch extends that entry to cite S087 (`S087 plugins.mdx:44-60` at patch lines 54-55 and 107), so `mined` status will be honestly earned at integration.
- Rule 1 (opened in the round that writes it): satisfied by this seat's fetch above; rule 6: no credential material.

## Caveats (not defects)

- The source-cell label "plugin discovery page" is descriptive, not the literal frontmatter title (`title: "Plugins"`, `plugins.mdx:2`). Same convention S085 itself uses ("V2 plugin documentation" vs literal `title: "Overview"`) — acceptable.
- The anchor parenthetical's seat history (RvS085Entry 05:33:18Z; "re-opened by the L1 05:44:34Z") is unverifiable by me; it is internally consistent with S085's committed sibling-fetch record (same sha256) — [INFERENCE], no contradiction found.
- A second `plugins.mdx` exists at `content/cli/plugins.mdx` (different blob) — harmless to the row's claims, noted only so the anchor stays read as "beside `index.mdx`" rather than "anywhere".

## Verdict

**Admit as written.** Every factual statement in the row verified against bytes fetched this round; column shape and enums conform to contract v1; correction-row form (`supersedes S085 —`) is correct; no edit proposed.

Report: .ufo/waves/round-57/a3/falsify/A3CandS087.md
