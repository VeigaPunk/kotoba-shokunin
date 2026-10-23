# RevScoutKeys — independent re-verification of ScoutKeyPagesA candidate URLs

Seat `kotoba-r61-wave-RevScoutKeys` (reviewer, depth). Date: 2026-10-23 (fetches below at
2026-10-23T19:4xZ, `date -u` per batch). Lane read-only; no git/jj mutation; no dispatch.
Candidate set is the five URLs returned by ScoutKeyPagesA (`.ufo/waves/round-61/wave/ScoutKeyPagesA.md`).

Method: each candidate was re-fetched with the counter's **frozen curl argv**, replicated verbatim
from `verifiers/check_scoped_rules.py:1169-1197` (`curl_argv`): `curl -sSL --max-time 30 -A
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
-H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' <url>`,
run via `subprocess.run(..., capture_output=True)` exactly as `run_curl` does. Status/effective-URL
come from curl's own write-out trailer; sha256 over the captured body bytes. Key lines located in the
re-fetched bodies at the claimed line numbers.

## Per-URL results (counter's own argv)

| URL | status | bytes | sha256 | final URL (redir) | claimed key line — verified |
|---|---|---|---|---|---|
| `https://code.claude.com/docs/en/claude-directory.md` | 200 | 31144 | `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14` | same (0) | :94 `| `rules/*.md` | `paths` | [Rule frontmatter](…) |` — rule row names exactly `paths` |
| `https://code.claude.com/docs/en/memory.md` (re-open S043/S103) | 200 | 55354 | `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` | same (0) | :246 "`paths` is the only field Claude Code reads from a rule"; :250 `` `paths` | No | Glob patterns … `` |
| `https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide.md` | 200 | 46556 | `9d76ff1414cca75440157d253ccdfd83848daacd77f27ec9bec6cc482adfb59b` | same (0) | :62 "create a frontmatter block containing the `applyTo` keyword"; :68 `applyTo: "app/models/**/*.rb"` |
| `https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md` | 200 | 22858 | `c29d67f0a342f2ae8de6bda04b8c7e7ce9a1341d61eaffdeee9a4fc8c9ced635` | same (0) | :154 applyTo-keyword step; :160 `applyTo: "app/models/**/*.rb"` |
| `https://cursor.com/docs/rules` (re-open S049; byte-identical to S108) | 200 | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | same (0) | :65 table row `` `alwaysApply` | `description` | `globs` ``; :85 `globs: src/components/**/*.tsx` |

All five: curl exit 0, HTTP 200, zero redirects, body < 5 MiB (counter `MAX_BYTES`), final URL on
the client's pinned host (`host_ok`, `HOSTS` at check_scoped_rules.py:262-279). Every measured
sha256/byte count is **identical** to ScoutKeyPagesA's reported values — the scout's fetches are
reproducible byte-for-byte with the counter's argv.

## Canonicality (per rejection taste standard)

All five paths carry no locale segment (`/de/`, `/ja/`), no `enterprise-cloud@latest` alias, no
change-note word (changelog/release/news/blog) in the decoded path, and no tracker segment. The
GitHub candidates use `/en/`. None is a nav/index/changelog page; all are how-to/reference articles
that name the keys. Cursor candidate is the unsuffixed canonical form, not the alias.

## Rejections confirmed byte-level

- `https://cursor.com/docs/rules.md` (S049's recorded URL) → **404**, 389 B, sha
  `4f98eb063d1914a3…` (body begins `# Page not found`). Dead. The canonical live page is the
  unsuffixed `/docs/rules`.
- `https://cursor.com/docs/reference/plugins.md` (S088's recorded `.md`) → **404**, same 389 B body.
- `https://cursor.com/docs/context/rules` → 200 but redirects (redir=1) to `/docs/rules`, byte-identical
  (17403 B, same sha) — alias; correctly rejected (round-60 practice).
- `https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md` (S047's recorded
  URL) → **404**, 9 B `Not Found` — S047 cannot be re-opened there; the successor page is already S105.

## Findings for the L1 (actionable)

1. **Pin-compatibility constraint on the two applyTo candidates (must decide row client).** Both
   GitHub-docs URLs sit on `docs.github.com`, which `HOSTS` pins only for **Copilot CLI** (line 271);
   the VS Code pins are `code.visualstudio.com` / `github.com/microsoft/vscode-docs` (lines 268-270).
   If either URL is used for a **VS Code** row, the counter's own `--fetch` will fail `host_ok` at
   data-measurement time and the row will be non-found — despite the URL byte-fetching fine. Scout's
   "VS Code / Copilot" label needs this caveat: both candidates are usable only as **Copilot CLI**
   rows. (Verify by inspection of `HOSTS`; no counter run — measurement rides the L1.)
2. **memory.md bytes drifted since r60.** Live bytes today are 55354 B / sha
   `02632438…` vs the committed `S103.page` snapshot 54043 B / sha `82d60341…`; direct line diff shows
   47 differing lines of 664 (first at :24,:36,:51,…). Ground lines :246/:250 are unchanged. Any new
   row re-opening memory.md must commit a fresh snapshot of today's bytes; the old S103.page would fail
   the A4 byte-equality conjunct for a row opened today.
3. **Cursor row URL form.** Use `https://cursor.com/docs/rules` (unsuffixed); the `.md` form 404s and
   S049's recorded URL is dead. This page is byte-identical to committed S108 — a new Cursor row
   re-opens S108, so it must be declared a re-open (duplicate-URL census rule), not a fresh open.

No other defect found in the candidate set; all five key-grounding lines exist verbatim in the
re-fetched bytes at the claimed line numbers.

## Installs
no installs

## Blockers
none

## Attacked/produced
Independently re-verified all five ScoutKeyPagesA candidates with the counter's frozen curl argv
(status/bytes/sha/key lines all confirmed; scout's measurements byte-exact), confirmed four dead/alias
URL rejections by byte-level probes, and filed three integration constraints (docs.github.com applyTo
pages are Copilot-CLI-pin-only, memory.md byte drift vs S103, Cursor row must use the unsuffixed URL).
