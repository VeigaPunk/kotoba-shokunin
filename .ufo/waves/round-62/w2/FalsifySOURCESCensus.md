# FalsifySOURCESCensus — round 62 wave 2

Seat: `L1kotoba62.FalsifySOURCESCensus`. Read-only except this file. No tools installed.

Assigned tip in the dispatch was `e6da78bbe420722dd18a13182a7c4b64ce02f005`. During this seat `HEAD` moved to its child `3f911504ce76d9ca186f297d6d4a9cd8ed77508a` (message: wave-2 dispatch + final census receipt). `corpus/SOURCES.md` is the same blob at both revisions and in the worktree: `fb053cd6952b730937803130589ad8547a44858d` (`git rev-parse <rev>:corpus/SOURCES.md` and `git hash-object corpus/SOURCES.md`). Worktree dirt at write time does not touch `corpus/SOURCES.md`, the lesson, the knowledge entry, or either census receipt.

## Verdict

Round-end census predicates **hold**. Append-only gate **exit 0**. One ledger timing defect: at `e6da78b` `LOG.md` already names `.ufo/waves/round-62/census-after.txt`, and that path is absent from that commit. The file lands in `3f91150` and its validator body matches the re-run.

## Census re-run

Command (worktree; SOURCES blob = both tips above):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

Exit **0**. Stdout (17 lines; sha256 `90b8d5167b04a35a8dd9a12ea1ff7ce088d6feb6e3ac661bf0dd55d134f698c3`):

```
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
```

No `E` lines. An earlier run in this seat, while `HEAD` was still `e6da78b` and the SOURCES blob already matched, also exited 0 with the same 16 `W04` lines plus `ok`.

## Before vs after

`.ufo/waves/round-62/census-before.txt` (committed at `45a7ecfa`, present at both tips): 15 `W04` lines, ids `S018 S019 S021 S054 S055 S056 S065 S086 S103 S104 S106 S110 S111 S114 S115`, then `kotoba ok`, recorded `exit=0`.

Committed after receipt `HEAD:.ufo/waves/round-62/census-after.txt` (`3f91150`, `receipt_rev=e6da78b`, `2026-10-23T21:33:52Z`): the 17 `kotoba` lines are byte-identical to the re-run, then a recorded `exit=0`.

W04 delta: **15 → 16**. The only id in the re-run and not in census-before is **S118**. The other 15 `W04` lines and the `ok` line match census-before. S118's duplicate URL is `code.claude.com/docs/en/memory.md`, the same URL census-before already warns on for S103. That is a warning, not an error (`scripts/sources-census.sh` header: W04 does not fail the lane).

## S118 is the only new row

Registry rows (`(?m)^\|\s*(S\d+)\s*\|` on `git show <rev>:corpus/SOURCES.md`):

| range | rows | added | removed |
|---|---:|---|---|
| `45a7ecfa` → `e6da78b` | 115 → 116 | `S118` | none |
| `e6da78b` → `HEAD` (`3f91150`) | 116 → 116 | none | none |

Cell diff of every registry row `45a7ecfa` vs `e6da78b`: the only changed id is the added S118 line. No pre-existing row's cells changed in the round-62 window.

`git log --oneline 45a7ecfa..HEAD -- corpus/SOURCES.md` is one commit: `3e7aed9` (S118 row/snapshot). S118 `used-by` at both tips is `corpus/lessons/round-62.md, corpus/knowledge/erratum-absorption-round62.md`. Both paths are absent at `3e7aed9` and present at `e6da78b` (that commit adds them). `scripts/sources-census.sh` E11 is "used-by path missing on disk" (script comment line 29; emit at lines 565-567). That is why a census at `3e7aed9` exits 1 and a census at `e6da78b` / `HEAD` exits 0.

## Append-only gate

```
python3 -B verifiers/check_sources_append_only.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005 --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin
```

Exit **0**. Same command with `--rev HEAD` (`3f91150`) also exit **0**. Emitted body (script-truncated; identical both revs):

```
log  5a097e12b S046 used-by: …les-round53.md -> …les-round53.md, corpus/l…
log  6de8e2eb4 S028 used-by: …les-round50.md -> …les-round50.md, corpus/k…
sources append-only rows clean: 11 commits scanned, 0 protected-cell changes
```

Those two notes are permitted used-by appends, not new rows, and both commits are ancestors of the round-62 plan freeze `45a7ecfa` (`5a097e12b` round 54, `6de8e2eb4` round 58). The 11 commits are the SOURCES-touching commits in `422ffd10..HEAD` (rounds 54–62). Zero protected-cell changes in that span. The round-62 addition is the new S118 row, which the gate does not treat as a protected-cell edit.

## What does not hold at the assigned tip

`LOG.md` at `e6da78b` line 2558 (R-d) says `.ufo/waves/round-62/census-after.txt` carries the validator body and its `exit=` line. `git cat-file -e e6da78b:.ufo/waves/round-62/census-after.txt` fails: the path is not in that commit. Parent of `3f91150` is `e6da78b`. The file's first commit on `master` is `3f91150`, and its body is the exit-0 receipt above, not an exit-1 transcript.

The interim exit 1 is not inside `census-after.txt` in any commit this seat found (`git log --all -S 'missing used-by' -- .ufo/waves/round-62/census-after.txt` empty). It is recorded in `HEAD:.ufo/waves/round-62/w1/ScoutRegistry.md:84-86`:

```
kotoba	E11	S118 missing used-by corpus/lessons/round-62.md
kotoba	E11	S118 missing used-by corpus/knowledge/erratum-absorption-round62.md
exit=1
```

That matches the cause above (used-by paths named before the files existed). LOG line 2558's "recorded rather than hidden" is true of that wave-1 report, not of `census-after.txt`. LOG line 2562 ("before 15 W04 exit=0 → after 16 W04 exit=0", S118 the new row) matches the re-run and the `3f91150` receipt.

At the start of this seat, before `HEAD` moved, the worktree `census-after.txt` was an uncommitted interim (header `# round-62 census-after`, `receipt_rev=3e7aed9b`, the two E11 lines, `exit=1`, no `ok` line). That text is not the blob now at `HEAD`. It was replaced when `3f91150` landed. Confidence on those earlier bytes: the initial file read in this seat, not a stored blob.

## Unresolved

- Whether any later commit after `3f91150` rewrites `census-after.txt` or `SOURCES.md`. Not true at write time (`HEAD` is `3f91150`; SOURCES blob unchanged).
- `jj` has an undescribed working-copy change `myorzxww` on top of `3f91150`. Not inspected beyond `git status` (sibling wave-2 reports and `SCORECARD.md` / two `w1` scribe files dirty; not this seat's inputs).
