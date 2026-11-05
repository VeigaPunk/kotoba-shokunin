# ScoutHostRoots — round 90 C2 host skills-root population (raw data)

Seat: **ScoutHostRoots**. Wave `r90-w1`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
All paths in this report are relative to that lane root. Measured read-only on 2026-11-05;
host Linux 7.2.11-arch1-1, omp/18.15.0.

## What I did

Enumerated this host's live skills root read-only and recorded **both** population numbers the
seat brief asks for (the SKILL.md-holding count and the plan's frozen `ls | wc -l` number),
checked the three candidate roots the brief names, listed the root's directory names, and
matched them against the fleet-lane names. **No census run** — `verifiers/check_host_skill_surfaces.py`
execution and the two `c2-*` receipts belong to ExecHostCensus. I wrote raw data only.

## Headline: the plan's frozen N == 83 is confirmed, both methods agree

```
$ for d in /home/vgpnk/.agents/skills/*/; do [ -f "$d/SKILL.md" ] && echo "$d"; done | wc -l
83
$ ls /home/vgpnk/.agents/skills | wc -l
83
```

**Both = 83.** No difference to reconcile; the two counts agree because every one of the 83
root entries is a directory holding a `SKILL.md` (`comm -3` between the two name sets: empty).
The plan's frozen `N == 83` holds for the census.

Structure of the 83: **78 real directories + 5 symlinks-to-directories + 0 plain files**; 5 of the
83 surfaces are symlinks pointing outside the root (`omarchy`, `tower`, `shokunin`, `ufo`,
`swarm` → `/home/vgpnk/Projects/ompskills/.omp/skills/…` and the omarchy default skill dir).

**Counting-method sensitivity (named finding, for ExecHostCensus):** `find` reports **78**, not
83, because `find` does not follow symlinks. `ls`, the `for d in …/*/` glob, and Python
`pathlib` (`iterdir()` + `is_dir()`) all report 83. The frozen instrument
(`verifiers/check_host_skill_surfaces.py:census()`) uses the pathlib expression, so it measures
83 and is unaffected — but any census arm written with `find` would measure 78 ≠ 83 and trip the
frozen `N == 83` guard. That is an implementation hazard for the census seat, not a host defect.

## Candidate roots named in the brief — all three ABSENT

```
$ ls -d ~/.omp/agent/skills ~/.omp/skills ~/.config/opencode/skills 2>&1
ls: cannot access '/home/vgpnk/.omp/agent/skills': No such file or directory
ls: cannot access '/home/vgpnk/.omp/skills': No such file or directory
ls: cannot access '/home/vgpnk/.config/opencode/skills': No such file or directory
(exit 2)
```

The live root is `~/.agents/skills` alone. A wider read-only sweep found other agent-harness
roots on this host (`.ecc/skills` 311 SKILL.md dirs, `.claude/skills` 24, `.grok/bundled/skills`
22, `.zcode/skills` 20, `.grok/skills` 14, `.minimax/skills` 13, `.config/devin/skills` 13,
`.kimi-code/skills` 7, `.gemini/skills` 3, `.cursor/skills` 3, `.prime/agent/skills` 3,
`.codex/skills` 2, `.pi/agent/skills` 1, `.hermes/skills` 1, plus empty `.config/alma/skills` and
`.local/state/skills`) — none is named by the frozen predicate; the census scope is not widened
here.

## Fleet-lane-name match: NONE

```
$ comm -12 <(ls -1 /home/vgpnk/.agents/skills | sort) \
         <(ls -1 /home/vgpnk/Projects/shokunin | sort)
(no output)   # intersection count = 0
```

Zero installed skill directory names equal a fleet-root entry name. The installed root carries
omp skill names (`godot-*`, `blender-*`, `unity-*`, `unreal-*`, `speech-*`, …); the fleet root
carries `*-shokunin` lanes plus tooling. Content level agrees: the sha256 sets of the 83 installed
`SKILL.md` and the 19 fleet lane `SKILL.md` intersect in **0** files.

**Consequence (inference from the instrument's own matching expression, not a census run):** the
census classifies by `fleet_root/<installed_dir_name>/SKILL.md`, a directory-name match. With an
empty intersection, all 83 surfaces will classify **lane-absent** → the summary will read
`host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, exit 0, and
`I + D + A == N == 83` holds. The plan's "every `drifted` or `identical` finding … named in the
report" clause is **vacuous on this host** — there will be no drifted and no identical surface.
An honest all-lane-absent outcome is valid under the plan's "guards measurability, not expected
identity" reading; nothing here rescues a counter or changes a frozen predicate.

## A1 name-uniqueness (round-72 rule): 0 collisions in the live root

Method = the round-84 ledger's method (first `name:` line within the first 12 lines of each
`*/SKILL.md`).

- Within `~/.agents/skills`: **0 duplicate names** over 83 entries; every frontmatter `name:`
  equals its directory name; 0 empty extractions.
- Across `~/.agents/skills` + `~/.zcode/skills`: **18 duplicate-name pairs** (`agents`,
  `computer-use`, `dubbing`, `heuer-planning`, `music`, `onboarding`, `orca-cli`,
  `orchestration`, `realtime`, `reverse-engineer-anything`, `setup-api-key`, `sound-effects`,
  `speech-engine`, `speech-to-text`, `text-to-speech`, `update-skills-from-changelog`,
  `voice-changer`, `voice-isolator`) — but **every pair is the same surface reached twice** (the
  `.zcode` entry is a symlink into `.agents`; the sha12 prefixes match exactly, e.g. `music
  7d868f6f5a09` in both). This is **not** the round-84 Windows-host defect class, where each
  colliding pair had two *different* shas (live dir vs dated `.pre-adapt-backup-20260927` dir).
  This host has no `.pre-adapt-backup-*` entries.
- Only 2 names are genuinely `.zcode`-local: `voicestudio` (368463ad5179),
  `voicestudio-maintainer` (6e4fd239a362) — both unique.

## Files written (mine only)

- `.ufo/waves/round-90/w1/ScoutHostRoots/roots-data.md` — the full raw receipt: every command
  with its observed output, the 83-name listing, the 5 symlink targets, the per-surface sha12
  map (83 lines), the fleet-lane frontmatter names, the A1 ledger, and the findings.
- `.ufo/waves/round-90/w1/ROOTS_READY` — content `83` (the SKILL.md-holding count).
- `.ufo/waves/round-90/w1/ScoutHostRoots.md` — this report.

Nothing under `corpus/`, `plans/`, `verifiers/`, `LOG.md`, `SCORECARD.md` or `MANIFEST.json` was
touched; no git or jj write was run in the lane or the fleet (read-only `git status`/`rev-parse`
only). Scratch was created at `/fast/scratch/hyaku/kotoba-r90/ScoutHostRoots` and removed before
yield.

## Remaining unknowns (routed, not answered here)

1. Whether the census seat's census arm uses `find` (78) or `pathlib`/`ls` (83) — a naming
   mismatch in a control would surface as a spurious `N != 83` red. ExecHostCensus's call.
2. Whether the round-90 census is meant to cover the `.zcode` root as well. The frozen
   predicate names only `--skills-root /home/vgpnk/.agents/skills`, so the 18 symlink-alias
   pairs are outside the frozen scope; the A1 ledger in `c2-name-collisions.txt` is ExecHostCensus's
   to compose (my ledger is raw input for it).
3. The root's mtime is `2026-10-29 03:33:05 -0300` — unchanged since then, so the population
   measured at 10:28 on 2026-11-05 is the population the census will see. If another seat or
   the operator installs a skill before the census runs, N moves off 83 and the frozen guard
   reds; that is a timing dependency for the census seat, not a defect in the host.
