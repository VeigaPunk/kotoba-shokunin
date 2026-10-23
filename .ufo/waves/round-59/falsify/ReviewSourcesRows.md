Result: HOLDS — S096–S102 all satisfy the 11-cell rule set at c63ccc6823e1f6a8577acbb43d19551eadbbee9a; every field cell is valid, every used-by path exists and cites its row, each row carries a real full 64-hex sha256 (byte-matched to the committed snapshots), and both census runs (live assignment command and data-commit sandbox) exit 0 with only the eight pre-existing W04s.

# Scope
Review S096–S102 in `corpus/SOURCES.md` at c63ccc6823e1f6a8577acbb43d19551eadbbee9a (data commit), per `/home/vgpnk/Projects/shokunin/CORPUS.md` SOURCES-CONTRACT-v1 (`:64-129`) and `.ufo/waves/round-59/build/ScoutSourcesRules.md`. Read-only in the lane; all file/state reads and script runs done in the sandbox clone `/fast/scratch/hyaku/kotoba-r59/ReviewSourcesRows` checked out at that revision, plus one read-only live-lane validate run. No tools installed (none needed).

# Field-cell checks (11 cells, rows at `corpus/SOURCES.md:108-114` in the data commit)

Each row: `NF=13` (11 data cells, outer pipe empties), id `^S[0-9]{3,}$`, row inside `## Registry`, before `## Paths` (`:116`), no raw pipe inside any cell (E01-clean).

| Row | kind | tier | status | opened | recheck | used-by | full 64-hex sha256 in anchor |
|---|---|---|---|---|---|---|---|
| S096 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| S097 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| S098 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md, corpus/lessons/round-59.md | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| S099 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| S100 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| S101 | docs | A | mined | 2026-10-23 | 90d | corpus/knowledge/hook-files-round59.md, corpus/lessons/round-59.md | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |
| S102 | docs | A | mined | 2026-10-23 | 90d | corpus/lessons/round-59.md | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |

- kind ∈ enum (`docs`), tier ∈ {A,B,C} and not community-at-A (no E10), status ∈ {queued,mined,rejected} (`mined` is earned: every used-by is a real path, not `—`; no W03), opened = 2026-10-23 (ISO, passes E08 at `--today 2026-10-23`), recheck = `90d` (legal NNd cadence, no E09). S102's teaches opens `supersedes S089` and repeats S089's scope text, so the shared first URL with S089 (code.claude.com/docs/en/slash-commands.md) triggers neither W04 (same scope) nor E04 (supersedes escape) — matches `ScoutSourcesRules.md:20,45-47`.
- Full 64-hex sha256 present in every one of S096–S102 (verified with `grep -oE '[0-9a-f]{64}'` per row; exactly 1 full hash per row). Cross-check: `sha256sum` of the committed snapshots `.ufo/waves/round-59/snapshots/S096.page`–`S101.page` produces byte-identically these same hashes (see commands below), so the hashes are real fetches, not decoration.

# Used-by paths exist and cite the row (data commit tree)

Both paths exist (sandbox `ls -l`):
- `corpus/knowledge/hook-files-round59.md` (6181 B) — cites S096 (5×), S097 (4×), S098 (4×), S099 (4×), S100 (4×), S101 (5×), e.g. `:23` `| Claude Code | .claude/settings.json | S096 | …`, `:25` `| VS Code | .github/hooks/*.json | S098 | …`, `:26-28` for S099/S100/S101; `:14` `each sha256 equals its SOURCES row`.
- `corpus/lessons/round-59.md` (11980 B) — cites S098 (3×), S101 (2×), S102 (4×), incl. Gate rows `:12` (S098: URL + access `2026-10-23T09:35:04Z` + HTTP 200), `:15` (S101), `:16` (S102); `:34` documents that S089 is byte-identical and S102 supersedes its anchor. Every row's used-by list is a subset of files that actually mention the row id (S098 and S101's lesson citations confirmed; S096's single lesson mention is outside its used-by list, which is fine).

# Census runs

1. Assignment command (read-only, live lane, run from /tmp so no repo is cwd):
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
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit:0
```
Exit 0, final `file ok`, exactly the eight pre-existing W04 ids (S018/S019/S021/S054/S055/S056/S065/S086), zero E lines, and no W04/E04/E01–E12 line naming S096–S102 (matches `ScoutSourcesRules.md:89-90` pass criteria).

2. Same validator bound to the data-commit file in the sandbox:
```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /fast/scratch/hyaku/kotoba-r59/ReviewSourcesRows/corpus/SOURCES.md --today 2026-10-23
file	W04	S018 duplicate url agentskills.io/specification across scopes
… (identical eight W04 lines)
file	ok	/fast/scratch/hyaku/kotoba-r59/ReviewSourcesRows/corpus/SOURCES.md
exit:0
```
3. State pin: `git diff c63ccc6823e1f6a8577acbb43d19551eadbbee9a..d64d945b3435e2532203c505ad64ecf5d91b780e -- corpus/SOURCES.md` is empty — the registry is unchanged between the data commit and tip, so the live run above validates exactly the reviewed rows.

# Findings
No actionable defect found in scope. All eleven field cells of S096–S102 are valid; every used-by path exists and genuinely cites its row; each row carries the full 64-hex sha256 and it matches the committed snapshot bytes; validator exits 0 on both the data commit and the live lane with only pre-existing W04s. Residual verification gap: contract rule 1's ≤25-word quote wording and snapshot byte content against the live pages are owned by other seats (ReviewLessonGate / C1 seats); not re-verified here.
