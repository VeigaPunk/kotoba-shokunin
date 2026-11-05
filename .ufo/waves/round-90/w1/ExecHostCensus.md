# ExecHostCensus — round-90 w1, C2 host installed-skill census (seat report)

Seat: ExecHostCensus (leaf). Date: 2026-11-05. Host: Linux 7.2.11-arch1-1, omp/18.15.0.
Lane: kotoba-shokunin. Read-only census; the only lane files written are the two owned `c2-*`
receipts, this report, and the `CENSUS_READY` handoff.

## Gate

`ROOTS_READY` (ScoutHostRoots) appeared with content `83` — the SKILL.md-holding count equals the
frozen bound N == 83, so the measured run proceeded against the right bound. roots-data.md §1:
83 entries = 78 real dirs + 5 symlinked dirs, every entry holds a `SKILL.md`; the plan-time
`ls | wc -l` number and the SKILL.md-holding number agree.

## Frozen predicate — measured, holds

```
$ python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills \
    --fleet-root /home/vgpnk/Projects/shokunin      # run from the lane root
exit: 0
host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83
```

I + D + A == 0 + 0 + 83 == N == 83. Transcript receipt:
`.ufo/waves/round-90/receipts/c2-host-census.txt`, first line
`measured-rev: 6fa5bb6d4ceeb51f0455e512a52d8b75628f404c` (Q36), then root paths, the exact command,
the 83 per-surface rows and the summary. The instrument's `--self-test` passed beforehand
(`0 failure(s) over 12 assertions`). The census matches by directory name; zero installed names
intersect fleet-root entry names (ScoutHostRoots §3a), so every surface is `lane-absent` — a valid
honest outcome: the instrument guards measurability, not expected identity (plan C2).

## A1 name-uniqueness ledger

`.ufo/waves/round-90/receipts/c2-name-collisions.txt` — round-72 A1 / round-84 C2 method (first
frontmatter `name:` line, first 12 lines, per installed `*/SKILL.md`), read-only. Result: 83
distinct names over 83 surfaces, **0 NAME-COLLISION pairs** in the live root; two independent
extractions (this seat's awk pass, ScoutHostRoots §4 sed pass) agree; every installed `name:`
equals its directory name. Counting command after: `grep -c 'NAME-COLLISION'
.ufo/waves/round-90/receipts/c2-name-collisions.txt` → 1 — the mandated count line is the only
line in the receipt carrying the uppercase marker, so the count decomposes as 0 pair rows + the
count line itself; the stated pair count is 0.

Cross-root check (recorded from ScoutHostRoots' data): only one live root is named by the frozen
predicate (`/home/vgpnk/.agents/skills`); the brief's three candidate roots
(`~/.omp/agent/skills`, `~/.omp/skills`, `~/.config/opencode/skills`) are absent on this host.
A wider sweep found other agent-harness roots (`.zcode/skills` 20 SKILL.md dirs — 18 symlinks into
`~/.agents/skills`, 2 local; `.claude/skills` 24; `.grok/bundled/skills` 22; `.ecc/skills` 311; …);
none is named by the predicate and the census scope was not widened. The 18 cross-root duplicate-name
pairs over `.agents` + `.zcode` are all the SAME surface reached twice via symlinks (identical
sha12 prefixes) — 0 distinct-surface collisions; the round-84 Windows class (live dir + dated
`.pre-adapt-backup-20260927` dir, pairs godspeed/ufo, differing sha12s) does not exist on this host.

## Findings (read-only, routed; nothing repaired)

1. **Census split is 0 identical / 0 drifted / 83 lane-absent.** Not a defect — the fleet root
   carries `*-shokunin` lane skills while the installed root carries omp tool skills; the predicate
   requires only I+D+A == N == 83. Routed to L1 as context for the C2 claim text.
2. **Counting-method sensitivity (ScoutHostRoots §2, confirmed here):** `find` without `-L` sees 78
   SKILL.md files (5 symlinked entries invisible); `ls`, the shell glob and Python `pathlib`
   `iterdir()`/`is_dir()` see 83. The frozen instrument uses the symlink-following expression, so
   the measurement is correct; any future census arm written with plain `find` would measure 78 ≠ 83
   and falsely trip the N == 83 guard. Implementation hazard for future seats, not a host defect.
3. **A1 is clean in the live root and the round-84 defect class is absent host-wide** (no
   `.pre-adapt-backup-*` entries; symlink aliases are not name collisions in the round-84 sense).
4. No drifted or identical finding exists on this host, so the plan's findings clause is vacuous
   beyond the lane-absent context above.

## Bounds honored

Wrote only: the two owned receipts, `CENSUS_READY`, this report. Scratch
`/fast/scratch/hyaku/kotoba-r90/ExecHostCensus/` (TMPDIR; transcript + pre-count only) is deleted
before yield; nothing copied into it from the lane, and no lane file needed preserving. No git/jj
write anywhere; the lane working tree was never used as a second checkout (live-root reads were
direct, read-only). No network, no pacman, no tool installs. Only KotobaR90's roster was relevant;
no peer message was needed (handoff files carried the contract). Messaged no one; final result via yield.

## Handoff

`CENSUS_READY` written with the measured line:
`host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`
