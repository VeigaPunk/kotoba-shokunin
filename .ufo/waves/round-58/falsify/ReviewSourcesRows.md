Result: HOLDS — the SOURCES append at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` is pure-append, every new row carries all 11 contract cells with valid enums and an on-disk used-by target, both named commands exit 0, and no new W-codes (or E-codes) appear.

# Scope

Attack item (calibration axis): `git diff f56f6e19..46b4a706 -- corpus/SOURCES.md` adds only rows; each new row has the contract's cells (`CORPUS.md` § SOURCES.md); run the append-only verifier and the census validate; report new W-codes.

# Checks run

## 1. Append-only diff — HOLDS

```
$ git --no-optional-locks diff --stat f56f6e191762c27c1aa2af11a204db9e2ca4edec 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe -- corpus/SOURCES.md
 corpus/SOURCES.md | 6 ++++++
 1 file changed, 6 insertions(+)
```

The only `-` line in the whole diff is the `--- a/corpus/SOURCES.md` header (`grep -cE '^[+-]'` on the diff = 8: 4 header lines + 6 added rows + `+++` counted; filtered check found zero deletion content lines). Six added rows: S089, S090, S091, S093, S094, S095, placed at the end of the `## Registry` table before `## Paths` (diff context confirms).

- **S028 "re-opened" is not an in-place edit**: `git show f56f6e19:corpus/SOURCES.md` and `git show 46b4a706:corpus/SOURCES.md` produce a byte-identical S028 row (line 41 in both). The re-open is recorded only in `corpus/lessons/round-58.md:38` (`re-opened 2026-10-23T08:08:39Z (HTTP 200, 47,200 B, sha256 d0d362cc…)`) — consistent with the append-only contract, which never rewrites an existing row's evidence.

## 2. Contract cells per new row — HOLDS

Header contract: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` = 11 cells, NF=13 under `awk -F'|'` (`CORPUS.md:86-108`).

```
S089 NF=13  kind=docs tier=A status=mined opened=2026-10-23 recheck=90d used-by=corpus/knowledge/command-files-round58.md
S090 NF=13  (same values)
S091 NF=13  (same values)
S093 NF=13  (same values)
S094 NF=13  (same values)
S095 NF=13  (same values)
```

- No empty cells in any of the six rows (per-column trim check printed nothing).
- Enums valid: `kind=docs`, `tier=A`, `status=mined` — all in-contract; `docs` may be tier A (the `community`-never-A rule does not apply).
- `id`s are `S`+3 digits, previously unused, unique in the registry (base max was S088; census reports zero E03 duplicate-id errors).
- `source` cells carry title — canonical URL (raw.githubusercontent pin for S095 at `4e0bc522…`).
- `anchor` cells name `§`-sections with `file.md:line` positions plus fetch evidence (UTC timestamp, HTTP 200, byte count, sha256) — matches the style of adjacent rows S086–S088 and satisfies "exact section plus revision" (commit pin or fetch timestamp+sha256 act as the revision for unpinned doc pages).
- `teaches` cells are grounded one-benefit claims; none are `REJECTED:` rows.
- `used-by` target exists at the attack rev: `git cat-file -e 46b4a706:corpus/knowledge/command-files-round58.md` → present (new file, not at base), and its `source:` line (line 2) cites all six new ids plus S028.
- `opened=2026-10-23` is today (present, not future); `recheck=90d` is a valid cadence.

## 3. Named verifier — exit 0

Sandbox: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/ReviewSourcesRows && git checkout -q 46b4a706…`; sandbox `corpus/SOURCES.md` sha256 `41320ab6caba893d8b9655dfa0af11b56c5602964c145a80aabc42d7c72f640f`, byte-identical to `git show 46b4a706:corpus/SOURCES.md` from the lane. Run inside the sandbox:

```
$ timeout 300 python3 -B verifiers/check_sources_append_only.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe
log  5a097e12b S046 used-by: …les-round53.md -> …les-round53.md, corpus/l…
sources append-only rows clean: 6 commits scanned, 0 protected-cell changes
EXIT=0
```

- `422ffd10` is the round-53 integrator commit ("round-53 verifier spot-check"), a proper ancestor of the base — the scan covers every SOURCES-touching commit since, not just this round's append, and still finds 0 protected-cell changes.
- The single `log` line is a permitted `used-by` change at round-53 commit `5a097e12` (S046) — the verifier's own change log; `used-by` is one of the three in-place-mutable columns. Pre-existing, out of this item's scope.
- Round-58's own append commit contributes no `log` line — nothing was changed in place this round, consistent with the pure-append diff.

## 4. Named census validate — exit 0, no new W-codes

```
$ timeout 300 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

- All 8 W04s name rows ≤ S086 — all present in the base file (`grep -oE '^\| S[0-9]{3}'` on base: max S088). **No new W-codes from this round's append.**
- W04 names only the later-seen duplicate, so I also counted each new URL's occurrence in the full registry: each of the six new URLs appears exactly once (`grep -c` = 1 each) — no new row shares a URL with an older row, so no hidden W04 exists.
- Zero E-codes: no malformed rows, no duplicate ids, no enum violations, no future `opened`, no bad `recheck`, no missing used-by paths, no rows outside `## Registry`.
- Validated file is the live lane working copy at tip `8e52f064`; `git diff 46b4a706 8e52f064 -- corpus/SOURCES.md` is empty and `git status` shows the file clean, so the census verdict applies byte-for-byte to the attacked revision (confirmed by the identical sha256 above).

# Observations (not findings)

- **S092 gap**: the registry jumps S091 → S093. The build spec reserves S092 as conditional (`S092 unused unless the Copilot CLI seat needs a new non-base page`); Copilot CLI re-opened S028 instead. The gap is planned and contract-safe (unused ids are not reuse).
- **S094 anchor** carries a supporting page and a supplemental changelog page inline — still one `|`-free cell, NF=13 intact.
- No tool installs were needed for this item (verifier + census + git/awk only).
