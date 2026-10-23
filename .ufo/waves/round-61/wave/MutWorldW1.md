# MutWorldW1 — world-instrumentation receipt for W1 (`CtlReopenForged d`)

Result: DONE — W1 rebuilt independently in scratch; the committed v2 counter reproduces the r60
record on it: offline `S=3` exit 1, `--fetch` `S=3/F=3` exit 0, and the restored bytes repeat the
pristine verdict. No predicate divergence. The surviving-mutant coverage finding is confirmed: v2
authenticates the row's sha256 against the committed snapshot bytes and never when those bytes were
acquired.

The tasking names the fixture `CtlResopenForged.md`; the file on disk is
`.ufo/waves/round-60/controls-v2/CtlReopenForged.md` (letter transposition). That is the file read.

## 1. Inputs, sandbox, independence

Read-only lane inputs (all absolute paths):

- Frozen counter: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py`,
  sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` (same bytes the r60
  receipt printed).
- Base revision pinned in the counter: `31092dc6f875370bddd6eb1e4da4ca0d210c56af` (`BASE`,
  `verifiers/check_scoped_rules.py:243`).
- Freeze revision of the r60 world construction: `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`.
- Fixture document: `.ufo/waves/round-60/controls-v2/CtlReopenForged.md`.
- Round-53 page bytes (the recycled bytes): named in the fixture document and read from
  `/fast/scratch/hyaku/kotoba-r53/…` (scratch, untrusted; their evidence value is that their
  sha256 equals the pin committed in the base SOURCES rows — see §4).

Independence: the world files below were written from the fixture document, the frozen counter's
own format, the lane's base SOURCES and freeze SKILL bytes, and the round-53 page files. The r60
sandbox's world commits were **not** opened; its `control-receipts/` were not used. The three page
files are the only r60-era bytes touched, and they are the files the fixture document itself names.

Sandbox (all writes under `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-MutWorldW1/`):

```text
$ git clone --shared --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin repo
Cloning into 'repo'...
done.
exit 0
$ cat repo/.git/objects/info/alternates
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.git/objects
$ git -C repo cat-file -e 31092dc6f875370bddd6eb1e4da4ca0d210c56af^{commit} && echo BASE present
BASE present
$ git -C repo cat-file -e b1cd64bb45eee744c4ec93be8631f1eddb28fddd^{commit} && echo FREEZE present
FREEZE present
$ cp /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py repo/verifiers/check_scoped_rules.py
$ sha256sum repo/verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  repo/verifiers/check_scoped_rules.py
```

`--shared` keeps the lane's object store read-only via alternates; the sandbox only ever reads it.
`lane_dir()` (`verifiers/check_scoped_rules.py:351`) resolves to the sandbox because the script sits
in `<sandbox>/verifiers/` and the sandbox carries `SKILL.md` and `corpus/SOURCES.md`; the printed
`rev` line in every run below is the sandbox commit, never a lane commit.

The world commits were built with git plumbing on a temporary index, parented on the real base
commit, so `git show 31092dc6…:corpus/SOURCES.md` resolves and no lane file was checked out or
copied en masse:

```text
$ GIT_INDEX_FILE=.idx-p git -C repo read-tree 31092dc6f875370bddd6eb1e4da4ca0d210c56af
$ GIT_INDEX_FILE=.idx-p git -C repo update-index --add --cacheinfo 100644,<blob>,<path>   # 7 world paths
$ tree=$(GIT_INDEX_FILE=.idx-p git -C repo write-tree)
$ commit=$(git -C repo commit-tree $tree -p 31092dc6f875370bddd6eb1e4da4ca0d210c56af -m 'world p')
```

Commit chain (each a descendant of the previous; the last two differ from their parent only in the
paths listed):

| World | Commit | Tree | Parent | Change from parent |
|---|---|---|---|---|
| P (pristine, my construction fetch) | `955c7eb1a5551e86a690589578b7765f82ff4454` | `05f1ac70f25316d8993bb7ed2101cd3aad3cf746` | base `31092dc6…` | adds the 7 world files |
| D (mutant `d`) | `a414727c2eb12dd61156570fe6b86c6a896d2d68` | `efbec4977360a93c28046a820226c4217fbde7db` | P | `corpus/SOURCES.md`, `.ufo/waves/round-60/snapshots/S103.page` |
| R (restored) | `b16ee1eb966349a15ee381dada3b7e3ec814c5e8` | `05f1ac70f25316d8993bb7ed2101cd3aad3cf746` | D | same two paths, bytes back to P |

Base SOURCES bytes in the sandbox equal the lane's base bytes (observed):

```text
$ git -C repo show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:corpus/SOURCES.md | sha256sum
3f63a11ffeedccf710aa872d08fd4b159ca8a52e89e0c11b3576c456c973779a  -
```

Structural anchors corroborate the r60 fixture document: the base SOURCES table's last row is line
114 (S102), so three appended rows land at 115–117; the freeze `SKILL.md` line 135 is
`## Router model — which harness, which gate`, so a 7-line section inserted before it lands at
135–141. Both are exactly the line ranges the fixture document states (`SOURCES.md:115–117`,
`SKILL.md:135–141`), which the r60 seat's prose differs from only in wording.

## 2. World files (full text; target paths relative to the sandbox world root)

### `SKILL.md` — section inserted after line 134 (occupies 135–141)

```markdown
### Scoped rule files by client

| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Claude Code | `.claude/rules/` | `paths` (S103 :198) | Scope rules to specific files using YAML frontmatter and matching patterns (S103 :194) |
| Copilot CLI | `.github/instructions` | `applyTo` (S104 :66) | Create a frontmatter block containing `applyTo` and use glob syntax to specify files or directories (S104 :60) |
| Cursor | `.cursor/rules` | `globs` (S105 :85) | Use `globs` to scope a rule to specific files or directories; separate multiple patterns with commas (S105 :131) |
```

### `corpus/knowledge/scoped-rules-round60.md` (full file)

```markdown
# Scoped rule files by client (round-60 control world)

| Client | Rule files | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/rules/` | S103 | "For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory." |
| Copilot CLI | `.github/instructions` | S104 | "2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files." |
| Cursor | `.cursor/rules` | S105 | "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled." |
```

### `corpus/lessons/round-60.md` (full file)

```markdown
## Gate

| row | URL | quote |
|---|---|---|
| S103 | https://code.claude.com/docs/en/memory.md | "For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory." |
| S104 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | "2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files." |
| S105 | https://cursor.com/docs/rules | "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled." |
```

### `corpus/SOURCES.md:115–117` — pristine world P

```text
| S103 | Claude Code — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Which scoped rule file Claude Code documents, its `paths` frontmatter key, and the matching-pattern form (vendor documentation, not a measurement of the client binary) | § Organize rules with `.claude/rules/` (memory.md:168), § Path-specific rules (:194, `paths:` block :198-199); fetched 2026-10-23T19:12:53Z, HTTP 200, 55,354 B, sha256 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801 | re-opens S043 — the base row's URL, re-read for the scoped-rules table | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
| S104 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Which instruction-file folder GitHub Copilot CLI documents, its `applyTo` frontmatter key, and the glob form for scoping instructions (vendor documentation for Copilot CLI; not a measurement of the CLI binary) | § Custom instructions for Copilot CLI (`copilot-cli-custom-instructions.md:56`), § frontmatter block (:60, `applyTo:` :66); fetched 2026-10-23T19:12:53Z, HTTP 200, 8,730 B, sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 | re-opens S048 — the base row's URL, re-read for the scoped-rules table | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
| S105 | Cursor Docs — Rules — https://cursor.com/docs/rules | docs | A | Which rule folder Cursor documents, its `globs` frontmatter key, and the pattern form for scoping a rule (vendor documentation, not a measurement of the agent) | § Project rules (`rules.md:32`), § `globs:` frontmatter (:85), § Glob pattern examples (:131); fetched 2026-10-23T19:12:53Z, HTTP 200, 17,403 B, sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | re-opens S049 — the base row's URL, re-read for the scoped-rules table | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

### `corpus/SOURCES.md:115–117` — mutant world D (only line 115 differs)

```text
| S103 | Claude Code — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Which scoped rule file Claude Code documents, its `paths` frontmatter key, and the matching-pattern form (vendor documentation, not a measurement of the client binary) | § Organize rules with `.claude/rules/` (memory.md:168), § Path-specific rules (:194, `paths:` block :198-199); fetched 2026-10-23T19:12:53Z, HTTP 200, 51,971 B, sha256 971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff | re-opens S043 — the base row's URL, re-read for the scoped-rules table | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

S104 and S105 are byte-identical in P and D (their fresh construction bytes already equal the
round-53 bytes). The mutation is one plausible defect: the snapshot pin and the committed page
bytes for S103 are swapped for the round-53 bytes, while the row keeps the fresh-fetch assertion
and the correct `re-opens S043 —` prefix.

### Snapshot provenance

| Path | P bytes / sha256 | D bytes / sha256 | Source of D bytes |
|---|---|---|---|
| `.ufo/waves/round-60/snapshots/S103.page` | 55,354 / `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` | 51,971 / `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` | `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md` |
| `.ufo/waves/round-60/snapshots/S104.page` | 8,730 / `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | same | `/fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md` |
| `.ufo/waves/round-60/snapshots/S105.page` | 17,403 / `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | same | `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4` |

The page bodies are not pasted (53 KB); the sha256 above is over the exact committed bytes. The D
page is byte-identical to the named round-53 file (observed):

```text
$ git -C repo show a414727c2eb12dd61156570fe6b86c6a896d2d68:.ufo/waves/round-60/snapshots/S103.page | sha256sum
971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  -
$ sha256sum /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md
971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md
$ git -C repo show a414727c2eb12dd61156570fe6b86c6a896d2d68:.ufo/waves/round-60/snapshots/S103.page > /tmp/d_s103.page
$ cmp /tmp/d_s103.page /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md && echo cmp exit $?
cmp exit 0
```

Both committed pages still carry the cited sites at the cited lines (observed from the committed
blobs): quote at line 168, action at line 194, `paths:` at line 198 with the block value at 199;
S103 has 664 lines (P) and 638 lines (D).

## 3. Construction fetch receipts (pristine P snapshots)

`date -u` printed immediately before the three fetches: `Fri Oct 23 07:12:53 PM UTC 2026`
(2026-10-23T19:12:53Z). One explicit fetch per page, frozen UA/Accept, `-D` headers saved:

```text
$ timeout 45 curl -D fetch/S103.headers -o fetch/S103.page -sSL --max-time 30 \
    -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
    -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' \
    https://code.claude.com/docs/en/memory.md
200 https://code.claude.com/docs/en/memory.md
exit 0
stderr: (empty)
HTTP/2 200
content-type: text/markdown; charset=utf-8
bytes 55354
sha256 02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801

$ … same for https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
exit 0
stderr: (empty)
HTTP/2 200
content-type: text/markdown; charset=utf-8
content-length: 8730
bytes 8730
sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980

$ … same for https://cursor.com/docs/rules
200 https://cursor.com/docs/rules
exit 0
stderr: (empty)
HTTP/2 200
content-type: text/markdown; charset=utf-8
bytes 17403
sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
```

No other page was fetched by this seat for construction. The counter's `--fetch` runs its own
fetches (up to three attempts per page); those are the runs in §4.

## 4. Detector runs (committed v2 counter, `python3 -B`, cwd `<sandbox>/repo`)

All six commands are `timeout 900 python3 -B verifiers/check_scoped_rules.py …`; every run printed
counter sha `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` and stderr was empty.
The rev in each block is the sandbox commit.

### Pristine P — offline; `date -u`: `Fri Oct 23 07:15:22 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 955c7eb1a5551e86a690589578b7765f82ff4454
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 955c7eb1a5551e86a690589578b7765f82ff4454
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

### Pristine P — live; `date -u`: `Fri Oct 23 07:15:22 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 955c7eb1a5551e86a690589578b7765f82ff4454 --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 955c7eb1a5551e86a690589578b7765f82ff4454
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: `--fetch` exit 0 (F>=TARGET) — MET

### Mutant D — offline; `date -u`: `Fri Oct 23 07:15:22 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a414727c2eb12dd61156570fe6b86c6a896d2d68
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a414727c2eb12dd61156570fe6b86c6a896d2d68
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

### Mutant D — live; `date -u`: `Fri Oct 23 07:15:23 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a414727c2eb12dd61156570fe6b86c6a896d2d68 --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev a414727c2eb12dd61156570fe6b86c6a896d2d68
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: `--fetch` exit 0 (F>=TARGET) — MET. **SURVIVED**, exactly as the r60 receipt recorded.

### Restored R — offline; `date -u`: `Fri Oct 23 07:15:22 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev b16ee1eb966349a15ee381dada3b7e3ec814c5e8
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev b16ee1eb966349a15ee381dada3b7e3ec814c5e8
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

### Restored R — live; `date -u`: `Fri Oct 23 07:15:23 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev b16ee1eb966349a15ee381dada3b7e3ec814c5e8 --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev b16ee1eb966349a15ee381dada3b7e3ec814c5e8
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: `--fetch` exit 0 (F>=TARGET) — MET

| World | S (backed) | F (live found) | Offline exit | Live exit | Verdict |
|---|---:|---:|---:|---:|---|
| P pristine (my construction bytes) | 3 | 3 | 1 | 0 | satisfying baseline |
| D `CtlReopenForged d` (round-53 bytes under a fresh-fetch claim) | 3 | 3 | 1 | 0 | SURVIVED |
| R restored (P bytes) | 3 | 3 | 1 | 0 | restoration passes |

`--self-test` was not run (not part of this assignment; an unrun check is not a passed check).

## 5. Before / mutant / restored hashes

Observed with `git -C repo show <rev>:<path> | sha256sum` per world:

| File | P `955c7eb1…` | D `a414727c…` | R `b16ee1eb…` |
|---|---|---|---|
| `SKILL.md` | `f383634f6bd795e4af3109e83c544ace899544697c3e3bd8756c6dade32a0d1d` (61,786 B) | same | same |
| `corpus/SOURCES.md` | `efc980c1493ab9df2031ab6b50ac0fee6e330a4490bfc47ad81deef7e40e4874` (106,719 B) | `87c540bb2e3b564d39c221862e36890efb919d971a0a5e835e4858c309472ffa` (106,719 B) | `efc980c1…` |
| `corpus/knowledge/scoped-rules-round60.md` | `f19270b541c8c55cd8834530f8e6c11935af7ee41f86764414af34c772bdcd94` (543 B) | same | same |
| `corpus/lessons/round-60.md` | `b853fece5e1b20753c7f7beb9dd01fff22d88dbff25eacaab08cb201a6b3f42f` (552 B) | same | same |
| `.ufo/waves/round-60/snapshots/S103.page` | `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` (55,354 B) | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` (51,971 B) | `02632438…` |
| `.ufo/waves/round-60/snapshots/S104.page` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` (8,730 B) | same | same |
| `.ufo/waves/round-60/snapshots/S105.page` | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` (17,403 B) | same | same |

Restoration evidence:

```text
$ git -C repo diff --name-status 955c7eb1a5551e86a690589578b7765f82ff4454 a414727c2eb12dd61156570fe6b86c6a896d2d68
M	.ufo/waves/round-60/snapshots/S103.page
M	corpus/SOURCES.md
$ git -C repo diff --name-status a414727c2eb12dd61156570fe6b86c6a896d2d68 b16ee1eb966349a15ee381dada3b7e3ec814c5e8
M	.ufo/waves/round-60/snapshots/S103.page
M	corpus/SOURCES.md
```

P and R trees are identical (`05f1ac70f25316d8993bb7ed2101cd3aad3cf746`), and every one of the
seven committed files compares equal between P and R (`True` for all seven comparisons). The
sandbox working tree was left on P's bytes; the counter file in the sandbox still hashes
`ca2585a4…`; no `__pycache__` exists anywhere in the sandbox (all runs used `python3 -B`).

## 6. What the probe shows

1. P and D produce byte-identical detector stdout after normalizing the rev line (6 lines each,
   same summary, same four reject lines): `P vs D live stdout identical after rev normalization:
   True`. The only thing that distinguishes the forged world from the honest one is invisible to v2.
2. The v2 code points that constitute its whole snapshot-provenance rule: `reopen_why`
   (`verifiers/check_scoped_rules.py:972–994`, prefix binding), the sha equality test
   (`:1078–1080`, `row_sha` vs `hashlib.sha256(committed snapshot)`), the quote test on the
   committed page (`:964–970`), and the predicate (`:1245–1249`). There is no acquisition-time,
   base-row, or history check anywhere in the counter.
3. The D row claims `fetched 2026-10-23T19:12:53Z, HTTP 200, 51,971 B, sha256 971d75bf…`; the same
   sha is the base row S043's committed pin with `opened 2026-10-22` and
   `fetched 2026-10-22T20:04:43Z, HTTP 200, 51,971 B, sha256 971d75bf…`
   (`corpus/SOURCES.md:56` at `31092dc6…`). The row therefore asserts a fresh fetch of bytes whose
   only lane-grounded provenance is yesterday's fetch, and v2 accepts it because the pin equals the
   committed bytes it itself supplied.
4. The live check is independent of the committed snapshot: the live S103 page fetched at
   19:12:53Z is 55,354 B / `02632438…`, not D's 51,971 B / `971d75bf…`, yet D's live run still
   reports `found on the live page 3 of 3`. v2 asks only that the quote and a key-form site exist
   on whatever the live URL serves.

## 7. Divergence check against the r60 receipt

The v2 predicate is reproduced: `S 3/F 3`, `--fetch` exit 0 on the mutant; offline exit 1 with
S=3; restored bytes repeat it. **No predicate divergence to file.**

Observed differences from the r60 world bytes, all explained and none detector-relevant:

- The r60 pristine S103 page was 54,043 B / `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7`
  (fetch 12:06:23Z). My construction fetch at 19:12:53Z is 55,354 B / `02632438…`: the live page
  changed during 2026-10-23. The live page's cited lines (168, 194, 198) did not move, so the
  detector's live check is unaffected. My baseline is my own fetch, so the P→D differential remains
  a clean provenance mutation.
- The r60 world's pristine `corpus/SOURCES.md` sha (`355349418cf599…`) and `SKILL.md` sha
  (`0168a9ee5f4c…`) differ from mine because the row prose and the section wording are mine; the
  structural line anchors (135–141, 115–117) and the recycled snapshot sha match exactly.
- The r60 d sandbox rev `7f05968a…` is not reused; my world has its own commits and receipts above.

## 8. Note for the v3 A4 arm (inference, not a v3 run)

The frozen A4 sentence is: "the earliest commit introducing those bytes must be no older than the
row's recorded open date (rejects recycled bytes: W1, round-53 scratch under a fresh-fetch claim)."
The rebuilt W1 shows why that mechanism alone cannot reject this world:

- In my sandbox the earliest (and only) commit introducing the `971d75bf…` bytes is the mutant
  commit `a414727c…`, dated 2026-10-23T19:15:17Z — the same day as the row's recorded open date
  (2026-10-23), so a date comparison passes.
- The lane's entire history contains **no** blob with sha256 `971d75bf…`: a scan over all
  `git rev-list --all --objects` blobs of the three relevant sizes (51,971 / 8,730 / 17,403 B)
  found only three candidates, and only the 8,730 B and 17,403 B ones match (`00e45ea5…`,
  `884c67ca…`). Those two were first introduced by the r60 data commit
  `7b80ae80cda69a95b6fc90879395113a99a57912` at 2026-10-23T09:28:13-03:00 (12:28:13Z), as
  `.ufo/waves/round-60/snapshots/S106.page` and `S108.page`, not as S048/S049 snapshots — the same
  calendar date as the row's open date.
- The only lane-grounded older signal is the base row S043's pin (`opened 2026-10-22`, fetch
  2026-10-22T20:04:43Z).

So, as written, A4 rejects W1 only if the v3 fixture backdates the recycled bytes' introducing
commit before 2026-10-23, or if A4 additionally rejects a snapshot sha already pinned by a base row
whose opened date precedes the row's open date. If the L1 reuses my fixture bytes, note that my
introducing commit is today. This is a fixture/arm-design caveat for the L1 before freezing v3; it
is not permission to change the contract, and no v3 code was run (none exists yet).

## 9. Bounds, integrity, disclosures

- Lane and fleet were read-only. No lane, fleet, sibling, `.ufo/state`, or jj/git-index file was
  written. No git/jj mutation was performed. No dispatch, no subagent, no ask tool.
- The only lane write is this report, `.ufo/waves/round-61/wave/MutWorldW1.md` (this file).
- All scratch lives under `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-MutWorldW1/` (world
  drafts, `repo/`, `fetch/`, `receipts/`). Scratch is untrusted and is cited only as the mechanical
  location of the round-53 page files; their evidentiary value is the sha256 match against the
  committed base SOURCES pins.
- Disclosures: three transient probe files were written under `/tmp` while reading lane bytes
  (`/tmp/base_sources_probe.md`, `/tmp/base_skill_probe.md`, `/tmp/d_s103.page`); they are removed
  and none is cited. One `jj log -r @` was run at the start as a read-only display (lane was clean;
  no file changed, and no further jj commands were run). All other lane git commands were
  `log`/`show`/`cat-file`/`rev-list` reads.
- Could not verify: the round-53 bytes' wall-clock fetch time except as recorded by base row S043;
  v3 behaviour (no v3 exists).

## 10. Close

Installs: no installs.

Blockers: none.

Attacked the v2 snapshot-provenance invariant with an independent rebuild of W1 (`CtlReopenForged d`):
round-53 S043/S048/S049 page bytes committed under fresh-fetch rows; the committed v2 counter passes
it S=3/F=3 live exit 0, reproducing the r60 survival, and P and D are indistinguishable to it.
