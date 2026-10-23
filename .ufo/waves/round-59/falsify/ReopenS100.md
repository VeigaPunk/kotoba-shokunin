# Reopen S100 — Gemini CLI Docs — Hooks Best Practices

Result: HOLDS — the S100 row, its snapshot, and both cited quotes survive re-opened
verification; the live page is byte-identical to the committed snapshot and to the
row's recorded sha256/size/status.

## Attack 1: the row (corpus/SOURCES.md:112 at c63ccc6823e1f6a8577acbb43d19551eadbbee9a)

Row text confirmed at the pinned data commit (not just working tree):

```
$ git show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:corpus/SOURCES.md | sed -n '112p'
| S100 | Gemini CLI Docs — Hooks Best Practices — https://geminicli.com/docs/hooks/best-practices.md | docs | A | Gemini CLI's documented project hook configuration and lifecycle events (vendor documentation, not runtime behavior) | § Cache expensive operations (`best-practices.md:28-31`); § Project Hook Security (`:411-416`); fetched 2026-10-23T09:34:48Z (HTTP 200, 17,650 B, sha256 `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc`) | Gemini CLI names `.gemini/settings.json` for project hook configuration and identifies `BeforeTool` and `AfterModel` as hook events | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md |
```

Every recorded fetch metric re-verified by fresh fetch:

```
$ date -u
Fri 23 Oct 2026 09:52:40 AM UTC
$ timeout 120 curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" \
    -o live-S100.page -w "status=%{http_code} bytes=%{size_download} url=%{url_effective}\n" \
    https://geminicli.com/docs/hooks/best-practices.md
status=200 bytes=17650 url=https://geminicli.com/docs/hooks/best-practices.md
(exit 0)
$ sha256sum live-S100.page
fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc  live-S100.page
$ wc -c live-S100.page
17650 live-S100.page
```

Recorded bytes (17,650), status (200), and sha256 (`fb44fbcf…`) all match the live page.
Row's fetch timestamp (09:34:48Z) is earlier than mine (09:52:40Z); content unchanged between.

## Attack 2: the snapshot (.ufo/waves/round-59/snapshots/S100.page)

```
$ cmp live-S100.page /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/snapshots/S100.page
(exit 0 — byte-identical)
```

Snapshot blob at the data commit, size check:

```
$ git ls-tree c63ccc6823e1f6a8577acbb43d19551eadbbee9a .ufo/waves/round-59/snapshots/
100644 blob 8d5ae2a0fb311346016f94697831577d785481e9	.ufo/waves/round-59/snapshots/S100.page
$ git cat-file -s c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/S100.page
17650
```

Snapshot is byte-identical to the committed blob and to the live fetch; no drift, no
stale/truncated copy.

## Attack 3: the quotes

Entry quote 1 — § Cache expensive operations (`best-practices.md:28-31`), live lines 28-31
(directly above the cited range):

```
### Cache expensive operations

Store results between invocations to avoid repeated computation, especially for
hooks that run frequently (like `BeforeTool` or `AfterModel`).
```

Entry quote 2 — § Project Hook Security (`best-practices.md:411-416`), live lines 411-416:

```
#### Project Hook Security

When you open a project with hooks defined in `.gemini/settings.json`:

1. **Detection**: Gemini CLI detects the hooks.
2. **Identification**: A unique identity is generated for each hook based on its
```

Gate quote (circle lesson `corpus/lessons/round-59.md:14`): `best-practices.md:413`
"“ you open a project with hooks defined in `.gemini/settings.json`:" — byte-exact match
with live line 413 (quoted above).

## Teaches-cell check against anchor lines

- "Gemini CLI names `.gemini/settings.json` for project hook configuration" — supported by
  live line 413 ("hooks defined in `.gemini/settings.json`"), the source table row at line 409
  (`Project (`./.gemini/...`)`), and line 379 (`git add .gemini/settings.json`).
- "identifies `BeforeTool` and `AfterModel` as hook events" — supported by live line 31
  ("hooks that run frequently (like `BeforeTool` or `AfterModel`)"), the "Use appropriate
  events" section (lines 74-77, `AfterModel` "Fires after every chunk"), and configuration
  examples using `BeforeTool` as an event key (lines 307, 615, 655). No overreach.

No contradiction found in the downstream knowledge entry `corpus/knowledge/hook-files-round59.md:47-49`
("Project hooks in `.gemini/settings.json` (`best-practices.md:413`); the page prints
`BeforeTool` and `AfterModel` (`:31`)"), consistent with the row.

## Housekeeping

- No tools installed (curl already present; no pacman/uv/cargo/npx change). No lane or
  fleet writes; fetch artifact only under /fast/scratch/hyaku/kotoba-r59/ReopenS100/.
- All commands run under `timeout` (120 s; exit 0), max 1 concurrent process.

## Residual risk / verification gaps

- Only the `.md` route was re-fetched; the HTML route (not cited by S100) was not checked —
  out of scope for this row.
- Server-side content negotiation with other UAs was not exercised; irrelevant for byte
  identity evidence, which already holds for the cited route.
