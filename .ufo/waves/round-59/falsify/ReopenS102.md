Result: HOLDS — S102 (routed-R4 correction row for S089) survives every check: live fetch byte-matches the row's record, every anchor cell resolves in the fetched bytes, teaches opens `supersedes S089 —` per CORPUS.md § SOURCES.md rule 2, S089 is byte-untouched, and the census validates with exit 0.

Seat: KotobaR59.ReopenS102 (leaf reviewer, round-59 falsify). Assignment: re-open S102 at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`; attacks: the R4 repair. No subagents spawned; no tools installed (tooling directive: nothing needed).

## 1. Live fetch matches the row's record (no drift)

Command (scratch dir /fast/scratch/hyaku/kotoba-r59/ReopenS102):
```
timeout 120 curl -sS --max-time 100 -L -o slash-commands.md -D headers.txt -w 'HTTP_STATUS=%{http_code} BYTES=%{size_download} URL=%{url_effective}\n' https://code.claude.com/docs/en/slash-commands.md
```
Observed: `HTTP_STATUS=200 BYTES=114542 URL=https://code.claude.com/docs/en/slash-commands.md`, curl exit 0.
Access time: `Fri 23 Oct 2026 09:52:44 AM UTC` (`date -u`).
`wc -c` = 114542; `sha256sum` = `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`.
Row S102 records: fetched 2026-10-23T09:34:33Z, HTTP 200, 114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`. The live bytes fetched at 09:52:44Z are identical (same byte count, same sha256) — the recorded hash is accurate and the page was stable across the 18-minute window. No drift.

## 2. Line 152 is exactly `## Choose where skills load`

`sed -n '152p'` + `od -c`: bytes `# # space C h o o s e space w h e r e space s k i l l s space l o a d \n` — exact, no trailing whitespace. `grep -nE '^#{1,3} (Choose where skills load|Frontmatter reference|How a skill gets its command name|Where skills live)$'` → only `152:## Choose where skills load` and `376:### Frontmatter reference`; there is **no** `Where skills live` heading anywhere in the doc — confirming S089's old anchor (§ Where skills live, `:172`) was wrong and the correction targets a real heading. Heading inventory (excerpt): `152:## Choose where skills load`, `439:#### How a skill gets its command name`.

## 3. Anchor cells resolve in the fetched bytes

Row S102 anchor = `§ Choose where skills load (slash-commands.md:152); Command files bullet (:172); § Frontmatter reference (:378,402-403); § How a skill gets its command name (:450-451); fetched … (R4 re-open)`.
- `:152` — heading `## Choose where skills load` (exact, verified above). KEEPS.
- `:172` — `sed -n '172p'` = `* **Command files**: a Markdown file in `.claude/commands/` is the older format and still works. It supports the same [frontmatter](#frontmatter-reference) except `name` and `paths`.` — matches "Command files bullet". KEEPS.
- `:378,402-403` — `378` is the section intro line under `### Frontmatter reference` (heading at 376): `Configure a skill with YAML [frontmatter](...) between `---` markers…`; `402`/`403` are the `argument-hint` and `arguments` rows of the frontmatter table (`| `argument-hint` | No | Hint shown during autocomplete … |`, `| `arguments` | No | Named positional arguments … |`). Both lie inside § Frontmatter reference. KEEPS.
- `:450-451` — `450` = `| File under `.claude/commands/` | File name without extension | `.claude/commands/deploy.md` → `/deploy` |`; `451` = `| File in a subdirectory of `.claude/commands/` | Subdirectory path relative to `commands/` … |` — both under `#### How a skill gets its command name` (heading at 439). KEEPS.

All four anchors resolve to the cited content; no mis-reference (unlike S089's original `:172` "Where skills live" anchor).

## 4. Row follows CORPUS.md § SOURCES.md (correction shape)

`awk -F'|'` on the S102 row at c63ccc68: id=`S102`, source=`Claude Code Docs — Extend Claude with skills (custom command files; S089 anchor correction) — https://code.claude.com/docs/en/slash-commands.md`, kind=`docs`, tier=`A`, scope identical to S089's, teaches=`supersedes S089 — Claude Code documents `.claude/commands/` Markdown command files as still-working older-format files; …`, status=`mined`, opened=`2026-10-23`, recheck=`90d`, used-by=`corpus/lessons/round-59.md`, NF=13 (11 columns + boundary pipes, well-formed).
- teaches opens exactly `supersedes S089 —` → CORPUS.md § SOURCES.md rule 2 ("A correction is a new row whose `teaches` opens `supersedes S0NN —`"). Exactly one row in the registry carries `supersedes S089` (grep -c = 1), so the correction row is unique.
- id discipline: ids at c63ccc68 include `S100`, `S101`, `S102` each exactly once; no S103+; no duplicate rows (census duplicate-id check clean).
- used-by exists: `git ls-tree c63ccc68 -- corpus/lessons/round-59.md` → `100644 blob 4fd8bf4149be932e22f43d6c9d2f1abfa2c5e676 corpus/lessons/round-59.md`; file present on disk (11980 B).

## 5. S089 untouched

- Byte-compare: `git show a975cbbf00534443c49bf02e29c813a3db0bf0f8:corpus/SOURCES.md | grep -F '| S089 '` vs the same at c63ccc68 → `cmp` exit 0 (`S089_IDENTICAL`), 1 line each.
- Diff: `git diff a975cbbf00534443c49bf02e29c813a3db0bf0f8 c63ccc6823e1f6a8577acbb43d19551eadbbee9a -- corpus/SOURCES.md` → `--stat` = `corpus/SOURCES.md | 7 +++++++ / 1 file changed, 7 insertions(+)`, **0 deletions**. The literal `grep '^-'` prints exactly one line — the unified-diff file header `--- a/corpus/SOURCES.md` (which begins with `---`, so it matches the pattern) — and zero actual removal lines (`grep '^-' | grep -v '^---'` prints nothing, exit 1). The corpus change is pure addition of the 7 new rows S096–S102; S089's row text is byte-identical. The R4 repair added a correction row without rewriting S089, as the append-only rule requires.

## 6. Census validates (exit 0)

Command: `timeout 900 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
Exit = 0. Output ends `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`. Output also lists pre-existing W04 duplicate-url warnings (S018/S019/S021/S054/S055/S056/S065/S086) — none involve the slash-commands.md URL (code.claude.com/docs/en/slash-commands.md), none affect the exit code, and none are touched by this row.

## Findings

No actionable defects found. Severity-ordered:
- (info) The literal `grep '^-'` from the spec prints the diff header line `--- a/corpus/SOURCES.md` because a unified diff always carries that header when the file changed at all; the test still passes in intent — zero deletion lines exist, stat confirms 7 insertions/0 deletions, S089 row byte-identical. If a stricter literal reading ("prints nothing at all") is wanted, the grep would need `grep '^-' | grep -v '^---'`; this is a test-harness nuance, not an S102 defect.
- (info) `§ Frontmatter reference (:378,…)` cites line 378, which is the first paragraph under the `### Frontmatter reference` heading at 376; `§ How a skill gets its command name (:450-451)` cites table rows under the `####` heading at 439. Both stay within their named sections — consistent with the contract's "exact section/heading/page/line" intent (the cited lines are content of the named sections). Not a defect.

## Residual risk / verification gaps

- Live-page drift after 2026-10-23T09:52:44Z is unobserved; the recorded sha256 was confirmed valid at that time and matches the 09:34:33Z record, so the row is honest as of the window.
- I verified S102's own cells and S089's intactness; other registry rows (S096–S101 etc.) are out of this seat's scope (owned by other falsify seats).
- Census W04 warnings are pre-existing and unrelated; they are worth a separate look by the L1 if not already tracked, but they do not block S102.

Evidence pointers: fetched bytes `/fast/scratch/hyaku/kotoba-r59/ReopenS102/slash-commands.md` (114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`); row source `corpus/SOURCES.md:114` at c63ccc68 (S102), `:102` (S089); contract `CORPUS.md` § SOURCES.md rule 2 (lines 116-118); census `scripts/sources-census.sh validate` exit 0.
