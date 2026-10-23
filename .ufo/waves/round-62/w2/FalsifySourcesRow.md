# FalsifySourcesRow — wave-2 attack on corpus/SOURCES.md S118

Verdict: **S118 survives every assigned attack — zero defects found.**

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Row under attack:
`corpus/SOURCES.md:129` (920 B). All commands run on committed/working bytes at
corpus tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`; the live checkout `HEAD` is
`3f911504ce76d9ca186f297d6d4a9cd8ed77508a` (w2 dispatch commit, touches no
SOURCES/corpus row — `git diff --name-only e6da78b HEAD` lists only
census-after/seat-counts receipts, w2 dispatch files, LOG.md, SCORECARD.md, and
the two r62 corpus files).

## A1 — cell count and contract order (PASS)

```
$ python3 - <<'EOF'   # corpus/SOURCES.md line 129
line.count('|')          -> 12          # NF=13
cells = split('|')[1:-1] -> 11 cells
header (line 12)         -> 11 cells
EOF
```

Cell order matches header `id|source|kind|tier|scope|anchor|teaches|status|opened|recheck|used-by`:
`S118 | Claude Code Docs — … — https://code.claude.com/docs/en/memory.md | docs | A | <scope> | <anchor> | re-opens S103 — … | mined | 2026-10-23 | 90d | corpus/lessons/round-62.md, corpus/knowledge/erratum-absorption-round62.md`.

## A2 — no embedded `|` (PASS)

12 pipe chars on the line = 11 cell separators between outer delimiters. No cell
contains a literal `|` (inline code spans are backticked, none carry a pipe).

## A3 — URL / access / sha256 vs snapshot (PASS, re-verified live)

- Snapshot `.ufo/waves/round-62/snapshots/S118.page` is committed at
  `e6da78b` (`git ls-tree -r e6da78b -- .ufo/waves/round-62/snapshots/`).
- `sha256sum .ufo/waves/round-62/snapshots/S118.page` =
  `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` — byte-equal
  to the row's anchor sha; `wc -c` = `55354` — matches the row's `55,354 B`.
- Access record corroborated by `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md:20-24`
  (`access_time_utc=2026-10-23T20:49:56Z`, `http_status=200`, `size_download=55354`,
  same sha) and by `corpus/lessons/round-62.md:14` (§ Gate record, same values).
- Fresh re-fetch (this seat, 2026-10-23T21:35:09Z):

  ```
  $ curl -fsSL --max-time 25 -A 'Mozilla/5.0 …' -H 'Accept: text/markdown, …' \
      -o /tmp/s118_refetch.md -w 'http=%{http_code} size=%{size_download} url=%{url_effective}\n' \
      'https://code.claude.com/docs/en/memory.md' && sha256sum /tmp/s118_refetch.md
  http=200 size=55354 url=https://code.claude.com/docs/en/memory.md
  02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /tmp/s118_refetch.md
  ```

  Live bytes are still identical to the snapshot — the recorded sha is not stale.

- Anchor citations checked against snapshot lines: `memory.md:244` =
  `#### Rule frontmatter reference`; `:250` = the `paths` field row
  ("Glob patterns that scope the rule to matching files. Accepts a YAML list or
  a comma-separated string"); `:194-200` = the § Path-specific rules body and
  its `paths:` YAML example. All land as cited.

## A4 — `re-opens S103 —` prefix per S114/S115 (PASS)

```
S114 teaches -> "re-opens S048 — canonical scope-key set: …"
S115 teaches -> "re-opens S108 — Cursor project rule files live under …"
S118 teaches -> "re-opens S103 — opened this round because the round-62 C1 E2e …"
```

Same `re-opens SNNN — ` convention; the reopened row exists and its scope is
distinct (S103 scoped the directory overview; S118 scopes the `paths` matching
syntax — the declared re-open condition, consistent with ExecCensus62's W04/E04
contract reading).

## A5 — status `mined` with both used-by paths existing (PASS)

Both `used-by` paths exist at tip and cite S118:

- `corpus/lessons/round-62.md` — `:12`, `:14` (§ Gate access record + ≤25-word
  quote at `memory.md:250`), `:29` (status-flip note `queued` → `mined`).
- `corpus/knowledge/erratum-absorption-round62.md` — `:1` (source line),
  `:43` (quote locator). Present at `e6da78b`; touched again by `3f91150` —
  the used-by link does not depend on the newer commit.

## A6 — census validator: exit 0, 16 W04 (PASS — exact output)

Command re-run by this seat at 2026-10-23T21:35Z:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

16 W04 lines + 1 `ok` line, `exit=0` — byte-equal to committed receipt
`.ufo/waves/round-62/census-after.txt` (receipt_rev=e6da78b). S118's W04 is the
expected cross-scope duplicate-URL warning for a declared `re-opens S103` row
(S103 holds the same URL); before-count was 15 W04 (`census-before.txt`), so the
delta is exactly the new row.

## A7 — row byte-identity across revisions (PASS)

`sha256` of `corpus/SOURCES.md` line 129 = `5de6da911d59a63971311363136b0e70592cd613e0697f30148f67208ba8aafa`
identically at `e6da78b` (`git show e6da78b:corpus/SOURCES.md | sed -n 129p`),
at `HEAD` `3f91150`, and in the worktree.

## Notes (non-defects)

- `git status --porcelain` on `corpus/SOURCES.md` and the snapshot: clean.
- W04 is a warning, not a failure — validator exit stays 0; the count matches
  the claimed 16 exactly.
- No tool installs were needed (bash/python3/curl/git only; pacman untouched).
