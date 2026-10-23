# MutWorldW24 — independent rebuild of W2 (alias) and W4 (redirect) under the committed v2 counter

Seat: `kotoba-r61-wave-MutWorldW24` (mutation-tester, round 61 single v2 wave).
Date of runs: 2026-10-23, 19:10–19:18 UTC. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(read-only to this seat; my only lane write is this report). Scratch:
`/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-MutWorldW24/` (untrusted; named for
reproduction only, never cited as evidence — every measurement below is pasted in this file).

## Verdicts (up front)

| world | mutant | rel. | no-fetch (summary / exit) | `--fetch` (summary / exit) | verdict |
|---|---|---|---|---|---|
| pristine | none (canonical rows) | eab2dc24e933a4b93cb235f6c333e1bc32f7f46d | `3 of 3; live not run` / 1 | `3 of 3; found on the live page 3 of 3` / **0** | baseline valid |
| **W2 alias** | locale Claude + enterprise Copilot URLs with their real pages, pins/quotes/action updated | c2e57d793469db1b92a071c6fad1aff7b737cd8b | `3 of 3; live not run` / 1 | `3 of 3; found on the live page 3 of 3` / **0** | **SURVIVED, exactly as r60 recorded** — v2 predicate MET; known coverage finding for v3 A3, not a contract change |
| **W4 redirect** | Cursor request URL `https://cursor.com/docs/context/rules` (carries `re-opens S052 —`) live-redirects to `https://cursor.com/docs/rules`, a base key (S049) | a45e26e7beb60758b1708c54e71c550e1cb9ca73 | `3 of 3; live not run` / 1 | `3 of 3; found on the live page 2 of 3` / **1**, reject `Cursor: live fetch failed: reached a base SOURCES URL https://cursor.com/docs/rules` | **KILLED, exactly as r60 recorded** |

Both recorded r60 outcomes reproduce. W2 meets the frozen v2 predicate (`S 3 / F 3`, exit 0);
W4 exits 1 with the same reject line as `.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md`
§ (c). The alias survival is the defect class round-61 C1 arm **A3** (URL byte-identical to the
base row's URL) exists to close; it is a coverage finding, not permission to change the
contract, and nothing in the lane was changed by this seat.

## Counter identity (committed v2)

The counter is byte-identical to the r60 freeze `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`
and to the lane tree at every tip I read (lane moved during the seat, read-only):

```sh
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show HEAD:verifiers/check_scoped_rules.py | sha256sum
sha256sum verifiers/check_scoped_rules.py        # inside the scratch world repo
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

`TARGET = 3` is read from the committed counter (`verifiers/check_scoped_rules.py:249`), not
from task text. The r60 freeze commit is in the lane history and carries the same bytes:

```sh
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py | sha256sum
```

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -
```

The scratch repo is a fetch of the lane (read-only `git fetch`), checked out at
the plan freeze `7827628a939b0333c89892dfcedc72e390ccfb60`; base revision
`31092dc6f875370bddd6eb1e4da4ca0d210c56af` is present, so the counter's base-row and
re-open checks run against real committed history. The worlds are commits on top of that
freeze. The lane itself was read only (`git show`/`rev-parse`/`for-each-ref`/fetch); no lane,
fleet, sibling, `.ufo/state` or jj/git-index file was written.

Base-row facts used by the structural checks (read at `31092dc6`, `git show ...:corpus/SOURCES.md`):
S043 holds `https://code.claude.com/docs/en/memory.md`, S048 holds the canonical Copilot
instructions URL, S049 holds `https://cursor.com/docs/rules.md`, S052 holds
`https://cursor.com/help/customization/rules.md`; `paths`, `applyTo` and `globs` occur **0**
times in S043/S048/S049 respectively (so the pristine re-opens are structurally admissible,
and ids S103/S104/S106 are absent at base: `grep -cE '^\| S1(03|04|06) '` → 0).

## What was rebuilt and how it was derived

Derived from `CtlReopenHeldKey.md` (r60 control, § "World content and evidence locations" and
§ "Full detector receipts"), not from its probe code: K=3 clients (Claude Code, Copilot CLI,
Cursor) under new ids S103/S104/S106; pristine rows re-open S043/S048/S049; the alias world
replaces Claude and Copilot with the real locale/enterprise renderings and their real bytes,
updating URL, sha pin, quote and Action accordingly, while Cursor stays a genuine S049
re-open; the redirect world changes only the Cursor request URL to
`https://cursor.com/docs/context/rules` with `re-opens S052 —` in `teaches`, leaving the
snapshot and all other cells pristine.

Because the live pages drift, I rebuilt the worlds from **fresh fetches of the same URLs**
(the r60 report's byte values were treated as expected, not as input), and pinned each
snapshot to the exact bytes I committed:

| URL | fetched (UTC) | HTTP / final | bytes | sha256 |
|---|---|---|---|---|
| `https://code.claude.com/docs/en/memory.md` | 2026-10-23T19:12:53Z | 200 / same | 55,354 | `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` |
| `https://code.claude.com/docs/de/memory.md` | 2026-10-23T19:10:54Z | 200 / same | 64,758 | `c72a26ddf4163793b74f9588642e9848e5d02edaa3ac94943f346d976b950e04` |
| `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | 2026-10-23T19:12:53Z | 200 / same | 8,730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | 2026-10-23T19:10:54Z | 200 / same | 8,826 | `70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e` |
| `https://cursor.com/docs/rules` | 2026-10-23T19:10:54Z | 200 / same | 17,403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |
| `https://cursor.com/docs/context/rules` | 2026-10-23T19:10:54Z | 200 / **`https://cursor.com/docs/rules`** | 17,403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |

Re-fetch at 19:17:51Z returned the same bytes for the two drifted pages
(`02632438…`/55,354 and `c72a26dd…`/64,758), so the pins and the 19:16 detector runs saw one
page generation. The Copilot canonical/alias and both Cursor fetches are byte-identical to the
r60 record; the Claude pages drift (see § Divergences).

The committed snapshots per world (from `git show <rev>:<path> | sha256sum`):

```text
== pristine eab2dc24e933a4b93cb235f6c333e1bc32f7f46d
S103.page 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
S104.page 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
S106.page 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
== alias c2e57d793469db1b92a071c6fad1aff7b737cd8b
S103.page c72a26ddf4163793b74f9588642e9848e5d02edaa3ac94943f346d976b950e04
S104.page 70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e
S106.page 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
== redirect a45e26e7beb60758b1708c54e71c550e1cb9ca73
S103.page 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
S104.page 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
S106.page 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
```

## Drafts — exact world content

Per output discipline these are the full texts committed into the scratch worlds; target paths
are relative to the scratch repo root (a reconstructor can drop them into any checkout of the
lane at the plan freeze and commit). The lane was **not** edited with any of them. SKILL.md,
the entry and the lesson are minimal reconstructions: the counter reads only the
`### Scoped rule files by client` first table, the entry's first table with the frozen header,
the `## Gate` section, the SOURCES rows and the snapshots. Everything measured below is the
committed counter's own output over these exact bytes.

### Pristine world (`eab2dc24…`)

`SKILL.md`:

```markdown
# x

### Scoped rule files by client

| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194) |
| Copilot CLI | `.github/instructions/**/*.instructions.md` (modular repository instruction files, S104 :18) | `applyTo` (e.g. `app/models/**/*.rb`, S104 :66) | Create a path-specific instruction file with an `applyTo` glob; use glob syntax to specify the files or directories the instructions apply to. (S104 :60) |
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S106 :32) | `globs` (example `src/components/**/*.tsx`, S106 :85) | Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S106 :131) |
```

`corpus/knowledge/scoped-rules-round60.md`:

```markdown
# e

| Client | Rule files | Source | Quote |
|---|---|---|---|
| Claude Code | .claude/rules/ | S103 | "For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory." |
| Copilot CLI | .github/instructions/**/*.instructions.md | S104 | "&#124; `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         &#124;" |
| Cursor | .cursor/rules | S106 | "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled." |
```

`corpus/lessons/round-60.md`:

```markdown
# l

## Gate

- S103 https://code.claude.com/docs/en/memory.md: "For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory."
- S104 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md: "&#124; `.github/instructions/**/*.instructions.md`              &#124; Modular repository instructions, discovered in the standard locations but not intermediate directories.                                                         &#124;"
- S106 https://cursor.com/docs/rules: "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled."
```

`corpus/SOURCES.md` — the three world rows (other rows are the lane's committed rows unchanged):

```markdown
| S103 | Claude Code Docs — How Claude remembers your project docs — https://code.claude.com/docs/en/memory.md | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801 | re-opens S043 — Claude Code documents .claude/rules/ files and YAML frontmatter paths | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
| S104 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI docs — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 | re-opens S048 — Copilot CLI documents modular instruction files | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
| S106 | Cursor Docs — Rules docs — https://cursor.com/docs/rules | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | re-opens S049 — Cursor documents project rules and the globs key | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

Snapshots: `.ufo/waves/round-60/snapshots/S103.page` = canonical Claude bytes (55,354,
`02632438…`); `S104.page` = canonical Copilot bytes (8,730, `00e45ea5…`); `S106.page` =
Cursor bytes (17,403, `884c67ca…`).

### W2 alias world (`c2e57d79…`) — differs from pristine only as shown

`SKILL.md` Claude Action cell (the German line-194 action; key cell unchanged):

```markdown
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Regeln können mit YAML-Frontmatter mit dem Feld `paths` auf bestimmte Dateien beschränkt werden. (S103 :194) |
```

`corpus/knowledge/scoped-rules-round60.md` Claude quote:

```markdown
| Claude Code | .claude/rules/ | S103 | "* [Regeln auf bestimmte Dateitypen beschränken](#organize-rules-with-claude/rules/) mit `.claude/rules/`" |
```

`corpus/lessons/round-60.md` Claude Gate line:

```markdown
- S103 https://code.claude.com/docs/de/memory.md: "* [Regeln auf bestimmte Dateitypen beschränken](#organize-rules-with-claude/rules/) mit `.claude/rules/`"
```

`corpus/SOURCES.md` changed rows (Copilot and Claude; Cursor row and all other cells pristine):

```markdown
| S103 | Claude Code Docs — How Claude remembers your project docs — https://code.claude.com/docs/de/memory.md | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 c72a26ddf4163793b74f9588642e9848e5d02edaa3ac94943f346d976b950e04 | re-opens S043 — Claude Code documents .claude/rules/ files and YAML frontmatter paths | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
| S104 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI docs — https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e | re-opens S048 — Copilot CLI documents modular instruction files | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

Snapshots: `S103.page` = German locale bytes (64,758, `c72a26dd…`); `S104.page` = enterprise
bytes (8,826, `70aef679…`); `S106.page` unchanged (`884c67ca…`).

### W4 redirect world (`a45e26e7…`) — differs from pristine only in the Cursor row

`corpus/SOURCES.md` Cursor row:

```markdown
| S106 | Cursor Docs — Rules docs — https://cursor.com/docs/context/rules | docs | A | scoped rule files | § rules, fetched HTTP 200, sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | re-opens S052 — Cursor rules help page | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

`corpus/lessons/round-60.md` Cursor Gate line uses the redirect URL in the URL field (quote
text and snapshot pin unchanged):

```markdown
- S106 https://cursor.com/docs/context/rules: "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled."
```

`SKILL.md` is byte-identical to pristine (same hash `5f199190…`); the entry is byte-identical
to pristine (`3b7a6cb3…`); snapshots are pristine. This isolates the one behaviour-bearing
change: the request URL and its `teaches` re-open marker.

## Detector receipts (committed v2 counter, exact commands and full stdout)

All commands run with cwd = scratch repo root. `date -u` values are the actual clock at the
run; the three no-fetch runs were one batch.

### Pristine — baseline

Actual `date -u` (batch): `Fri 23 Oct 2026 07:16:14 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d
```

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit `1` (contractual: without `--fetch` the predicate is always 1). Stderr empty.

Actual `date -u`: `Fri 23 Oct 2026 07:16:28 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d --fetch
```

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit `0`. C1 predicate met for the baseline; stderr empty. A baseline failure would have been
inconclusive; it passed.

### W2 alias — mutant (locale/enterprise renderings with real content)

Actual `date -u` (no-fetch batch): `Fri 23 Oct 2026 07:16:14 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev c2e57d793469db1b92a071c6fad1aff7b737cd8b
```

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev c2e57d793469db1b92a071c6fad1aff7b737cd8b
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit `1` (contractual). Actual `date -u`: `Fri 23 Oct 2026 07:16:31 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev c2e57d793469db1b92a071c6fad1aff7b737cd8b --fetch
```

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev c2e57d793469db1b92a071c6fad1aff7b737cd8b
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit **`0`**. Stderr empty. No `reject Claude Code` / `reject Copilot CLI` line: both alias rows
are backed on their committed snapshots and found on their live pages. **The mutant survives
the v2 predicate exactly as the r60 record says; this is the coverage finding for v3 A3.**
The alias pages were reached at the requested URLs with HTTP 200 and no redirect (curl
trailers above); the live guard only rejects a final URL that is a BASE SOURCES key, and a
locale/enterprise rendering is a distinct URL in the frozen `url_key` normalisation.

A second, mechanical v2 weakness is visible in the same row: the German quote passes the
quote rule only because the untranslated anchor slug `#organize-rules-with-claude/rules/`
supplies the required `rules` word outside the token span (verified with the frozen helpers:
`token_span(q_plain, ".claude/rules/")` = `(88, 102)`, `rule_word_outside` True, the two
outside matches at offsets 58 and 76 are both inside that anchor; 8 words; a key-form `paths`
site exists at live line 198). This is the anchor-slug disclosure W0b/r60 already recorded,
reproduced here — the row is accepted although no German prose names rules outside the
token.

### W4 redirect — mutant (live redirect to a different base key)

Actual `date -u` (no-fetch batch): `Fri 23 Oct 2026 07:16:14 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a45e26e7beb60758b1708c54e71c550e1cb9ca73
```

```text
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a45e26e7beb60758b1708c54e71c550e1cb9ca73
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit `1` (contractual). Actual `date -u`: `Fri 23 Oct 2026 07:16:35 PM UTC`.

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a45e26e7beb60758b1708c54e71c550e1cb9ca73 --fetch
```

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 2 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a45e26e7beb60758b1708c54e71c550e1cb9ca73
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: live fetch failed: reached a base SOURCES URL https://cursor.com/docs/rules
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit **`1`**. Stderr empty. Killed by the live guard at
`verifiers/check_scoped_rules.py:1200-1230` (`URL key of final in base_keys and != own_key`),
as the r60 record says. Note the limit already disclosed by r60: the request URL is non-base,
so the structural `reopen_why` check is skipped; this row carries a wrong re-open marker
(`S052`) rather than proving a structurally valid cross-base re-open. The kill is the live
final-URL guard, nothing else.

Request counting (transparent logger that only records argv and `exec`s `/usr/bin/curl`; no
argument changed, no stored page supplied). The probe wrapper is `probe/bin/curl`:

```sh
#!/bin/sh
printf "%s\n" "$*" >> "$CTL_CURL_LOG"
exec /usr/bin/curl "$@"
```

Exact command (actual log mtime 19:17:19Z; `$PROBE` =
`/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-MutWorldW24/probe`):

```sh
PATH="$PROBE/bin:/usr/local/bin:/usr/bin:/bin" CTL_CURL_LOG="$PROBE/curl-redirect.log" \
  timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a45e26e7beb60758b1708c54e71c550e1cb9ca73 --fetch
```

Full stdout, exit `1`:

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 2 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a45e26e7beb60758b1708c54e71c550e1cb9ca73
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: live fetch failed: reached a base SOURCES URL https://cursor.com/docs/rules
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

5 curl GETs: Claude ×1, Copilot ×1, Cursor `…/docs/context/rules` ×3 (the frozen 3-attempt
cap; the log has 10 lines because the `-w` argument itself contains a newline, giving two log
lines per invocation). Each Cursor GET reached `https://cursor.com/docs/rules`, so all three
attempts hit the same guard.

## Restoration evidence

The counter reads committed bytes with `git show` and never writes. Restoration was verified
by hashing the working tree before the first detector run, after the alias and redirect runs,
and after the final pristine re-run. All world files were byte-identical in the restored
state; the counter hash was identical before and after every run.

Before (pristine build) and after (restored, 19:16:55Z) — identical:

```text
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
5f199190d9623c436afcfb696124f61e83d79ff7a1ec69afe22a9833ed10aa29  SKILL.md
a1d34fc0e761cfd45368435890a50802178af7f1b41d8874d657334161502441  corpus/SOURCES.md
3b7a6cb3d9f90fd82ce6d6c43cd65010bb66c236f512f12f60a3dbed049cf68e  corpus/knowledge/scoped-rules-round60.md
456a98b4a355f6960c74fffc28fe094db7bec1e9ebef1c6e80a7c82455c1aeb9  corpus/lessons/round-60.md
02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  .ufo/waves/round-60/snapshots/S103.page
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  .ufo/waves/round-60/snapshots/S104.page
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  .ufo/waves/round-60/snapshots/S106.page
```

Final restored-state detector re-run (actual `date -u` `Fri 23 Oct 2026 07:16:55 PM UTC`):

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d --fetch
```

```text
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev eab2dc24e933a4b93cb235f6c333e1bc32f7f46d
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Exit `0`. Mutated-state file hashes (for the record, from the committed worlds):

| world | file | pristine sha256 | mutated sha256 |
|---|---|---|---|
| alias | `SKILL.md` | `5f199190…` | `4f4f5e99cd6ac7d7d5f4a341dd0832051574545342d4dc6a4221f93b0ffe2101` |
| alias | `corpus/SOURCES.md` | `a1d34fc0…` | `ad497710bf0a2445b33d276889568a6b709f3561c1f545dc8975d73e0fd977f3` |
| alias | `corpus/knowledge/scoped-rules-round60.md` | `3b7a6cb3…` | `eff23f129d0c5bb875954cfc1b82db08ca6a62459586952daf06c5bab3de61b5` |
| alias | `corpus/lessons/round-60.md` | `456a98b4…` | `68e39489c434b28ef11e1fd404af396040b7652a49af47bebd8a2f0cd36eebd8` |
| alias | `S103.page` | `02632438…` | `c72a26dd…` |
| alias | `S104.page` | `00e45ea5…` | `70aef679…` |
| redirect | `corpus/SOURCES.md` | `a1d34fc0…` | `0e5c4cafe9c15ae1e5829ecce4cb4673733aa11b2479db4d03da36cdfc775571` |
| redirect | `corpus/lessons/round-60.md` | `456a98b4…` | `9da1a312496b7d95d815c095d162020dc49d797d1021290bf48bb03dc6e5ed62` |
| redirect | `SKILL.md`, entry, snapshots | unchanged | same as pristine |

## Divergences observed (byte drift, not verdict drift)

- **Claude canonical page drifted since r60.** The committed r60 snapshot / r60 fetch was
  54,043 B `82d60341…`; live 2026-10-23T19:12:53Z is 55,354 B `02632438…`. Lines 168
  (English quote), 194 (English Action) and 198 (`paths:` + `- "src/api/**/*.ts"`) are
  byte-identical, so the pristine world still backs and fetches.
- **German alias page drifted since r60's 12:07 fetch.** r60 fetched 63,447 B `c568aae2…`
  (still present under its r60 scratch probe directory as a cross-check, and matching its
  report). Live 2026-10-23T19:10:54Z is 64,758 B `c72a26dd…`; both have 664 lines with 53
  lines replaced, and lines 18 (German quote), 194 (German Action) and 198 (`paths:`) are
  byte-identical. The W2 snapshot pin in this rebuild is the fresh `c72a26dd…`; the recorded
  r60 verdict (`S 3 / F 3`, exit 0) still reproduces. This is expected page drift, not a
  counter divergence, and it does not change the alias-survival finding.
- Copilot canonical (8,730 B `00e45ea5…`), Copilot enterprise (8,826 B `70aef679…`), Cursor
  canonical/redirect body (17,403 B `884c67ca…`) are byte-identical to the r60 record.
- The lane tip moved during this seat (I first read `7827628` at ~19:09 UTC; a read-only
  `git fetch` at ~19:14 UTC saw `c630c4c`; a later read at ~19:18 UTC saw `eb5e149`). This
  seat wrote nothing there; the counter's sha256 stayed `ca2585a4…` at every tip. Worlds were
  built from the plan-freeze tree `7827628`, so the moving tip cannot have contaminated them.

## Limits

- The three worlds are minimal reconstructions of the checked structures (SKILL section, entry
  table, Gate, SOURCES rows, snapshots), not byte-copies of the r60 sandbox. The frozen counter
  reads exactly those structures; the pristine baseline passing at S=3/F=3 demonstrates the
  reconstruction exercises the same detector path.
- Live fetches hit the real network with the counter's own curl argv (browser UA, Accept,
  30 s cap, ≤3 attempts, 5 MiB cap). The counter does not log success details; the URL/byte
  evidence above is from my own same-header fetches and curl trailers, and the request count
  from the transparent logger.
- Per the frozen v3 A4 limit declared in the plan, no wall-clock-vs-commit-date authentication
  was attempted; this probe is about v2's URL/redirect behaviour only.
- No `--self-test` was run: the assigned detector is the world measurement
  (`--rev … --fetch`); the counter's own fixture suite is a different instrument.

installs: none.
blockers: none.

Attacked: rebuilt the r60 alias-survival world (W2) and the different-base redirect world (W4)
independently from `CtlReopenHeldKey.md` against the committed v2 counter and reproduced both
recorded verdicts — W2 survives (`S 3 / F 3`, exit 0) as the known v3-A3 coverage finding, W4
is killed (`S 3 / F 2`, exit 1) by the live final-URL guard — with exact restoration and with
the Claude-page byte drift disclosed.

Report: .ufo/waves/round-61/wave/MutWorldW24.md
