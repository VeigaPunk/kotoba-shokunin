# ExecProbeBoundR87 — r87-w3 bounded read-only probe of C1's `{cwd}/` bound (conjunct 4)

Seat: ExecProbeBoundR87. Lane tip verified before probing:
`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master` →
`760e1c5edfdefb4767420f711d08f669952de013` (matches the frozen tip). Pinned ELF verified:
`sha256sum /home/vgpnk/.local/bin/omp` → `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`
(matches the frozen sha256).

Under a scratch HOME (`/fast/scratch/hyaku/kotoba-r87/ExecProbeBoundR87/home`, never the real HOME;
fixture SKILL.md files per item step 1), with session cwd `/fast/scratch/hyaku/kotoba-r87/ExecProbeBoundR87/home/u/proj/sub`
and `HOME=<scratch>/home`, the non-interactive enumeration of omp v18.15.0 is the verb behind
`omp skill list --json` (the `skill` registry command's local-discovery `list` action; receipts:
`skill_list_json.txt`, `skill_list.txt`, `skill_list_outside.txt`, `strace_skilllist.txt`,
`omp_help.txt`, `omp_skill_help.txt`, `probe-commands-and-observations.md`, all under
`.ufo/waves/round-87/w3/ExecProbeBoundR87/`).

## Verdict

bound probe: home-hidden

Deciding command (exit 0, `timeout 60`, `env -i HOME="$S/home" TMPDIR="$S" PATH=/home/vgpnk/.local/bin:/usr/bin:/bin TERM=dumb`, cwd=`$S/home/u/proj/sub`):

```
/home/vgpnk/.local/bin/omp skill list --json
```

which printed both probe skills with distinct source scopes: `local-skill` from the cwd chain with
`"source":"agents:project"`, and the skill placed directly under the scratch HOME
(`$S/home/.agents/skills/probe-skill`) with `"source":"agents:user"` — never a project-scope hit.
The `{cwd}/.agents/skills`-row expansion therefore surfaced only cwd-chain content and did not
reach `$HOME`: the HOME-level skill is hidden from the cwd-bound channel, exactly as C1 conjunct 4
predicts ("a `{cwd}/` row's expansion set excludes `$HOME` and above"); the skill sitting directly
under `$HOME` is visible only through the separate user-scope channel, which the frozen 12-row
ledger `verifiers/omp-skill-roots-semantics.tsv` at the tip explicitly carries as its `~/` row 11
(`~/.agents/skills`) — the "unless the row is a `~/` row" carve-out. No probe mode in which a
cwd-row expansion reached `$HOME` was observed, so the probe is conclusive, not inconclusive.

## Evidence (all below from receipts in `.ufo/waves/round-87/w3/ExecProbeBoundR87/`)

1. Pinned geometry (`$S/home/u/proj/sub` cwd, scratch HOME), `omp skill list --json` (exit 0):
   `local-skill` baseDir `.../ExecProbeBoundR87/home/u/proj/sub/.agents/skills/local-skill`,
   source `agents:project`; `probe-skill` baseDir `.../ExecProbeBoundR87/home/.agents/skills/probe-skill`,
   source `agents:user`; `"warnings":[]`.
2. `strace -f -qq -e trace=%file omp skill list --json` (exit 0, 545 lines): the project walk-up
   probed `.../home/u/proj/sub/.agents/skills` (fd 16), `.../home/u/.agents/skills` (ENOENT),
   `.../home/u/proj/.agents/skills` (fd 17); ZERO opens of any `.agents/skills` path above
   `.../home` (regex `ExecProbeBoundR87/\.agents|scratch/hyaku/\.agents|scratch/\.agents|/fast/\.agents|"/\.agents`
   → 0 matches) and ZERO `..`-segment probes (regex `sub/\.\.|proj/\.\.|/u/\.\.|home/\.\.` → 0
   matches); both SKILL.md files were opened and read during the run (fresh discovery). The
   unnamed openat of `.../home/.agents/skills` (thread 566092's enqueue) cannot be attributed to a
   channel by syscall alone, but P3 settles it: that exact read happens for the user channel even
   with cwd outside HOME. The `resumed` completions for those called-out probes were decreed:
   209 → 565634 =16; 293 → 566092 =17; 298 (`.../home/u/proj/.claude/skills/`) = -1 ENOENT;
   299 (`.../home/u/proj/.codex/skills/`) = -1 ENOENT; 303 (`.../home/.config/opencode/skills/`)
   = -1 ENOENT; 304 = -1 ENOENT (companion of 293); 318 (`.../home/u/proj/sub/.claude/skills/`)
   = -1 ENOENT; 328-329/companion-ENOENT pattern as printed under "codex/opencode/claude-row
   probes" in `probe-commands-and-observations.md`. The codex/opencode/claude rows all fire at
   `$HOME`, cwd-chain ancestors, and sub-cwd — never above `$HOME`.
3. Supplementary channel test at cwd `$S/outside` (scratch HOME unchanged), exit 0: only
   `probe-skill`, still `agents:user`; `local-skill` absent. The user channel is HOME-rooted and
   independent of cwd geometry; the project channel is strictly cwd-rooted.
4. Frozen ledger cross-check (`git show 760e1c5e...:verifiers/omp-skill-roots-semantics.tsv`,
   receipt copy `semantics-ledger-760e1c5e.tsv`): 12 rows; row 4
   `{cwd}/.agents/skills` → module `coding-agent/src/discovery/agents.ts`, reader quote
   `x.push(Rs.join(R, _, ...p));` — the project walk-up row; row 11 `~/.agents/skills` same
   module, reader quote `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` — the
   user-home row. The observed two-channel split matches the ledger's own two-row structure:
   conjunct 4's "unless `~/`" carve-out is live in the real binary at v18.15.0.

## Bounds and hygiene

Wave-scope C1/C2 gate re-verification, counter mutants, D5 drift measurement: NOT performed by
this seat — that is sibling w3 seats' assignment; this seat's item is the single bounded probe
above (only my `.ufo/waves/round-87/w3/ExecProbeBoundR87/` receipts and `.ufo/waves/round-87/w3/ExecProbeBoundR87.md`
were written in the lane; no verifiers/TSV/plan/corpus/LOG/SCORECARD/SKILL file touched; no other
seat or lane touched; no labrat child spawned — the item's one-shot probe succeeded on the first
mode, so the optional second probe attempt was unnecessary). Scratch
`/fast/scratch/hyaku/kotoba-r87/ExecProbeBoundR87` (fixture home, strace log, help captures) is
deleted at seat exit after receipts were copied into the lane (step 4). No PACMAN transaction, no
git write anywhere (FIFO discipline kept: lane tip read-only before and after the probe), no raw
environment dump written to the lane (probe env vars statuses are named in
`probe-commands-and-observations.md`, values are only the scratch paths themselves).
