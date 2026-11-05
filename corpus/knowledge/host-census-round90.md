source: own-work — round-82 capability `verifiers/check_host_skill_surfaces.py` (the host installed-skill surface census, read-only) re-measured this round against this host's live skills root, plus this round's receipts `.ufo/waves/round-90/receipts/c2-host-census.txt` (transcript, first line `measured-rev: 6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`) and `.ufo/waves/round-90/receipts/c2-name-collisions.txt` (the round-72 A1 name-uniqueness ledger); the population data behind the census is `.ufo/waves/round-90/w1/ScoutHostRoots/roots-data.md`
verified-at: 2026-11-05 @ lane tip 6fa5bb6d4ceeb51f0455e512a52d8b75628f404c — the CENSUS_READY handoff content is the measured line `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, and the census command exited 0 (receipt `.ufo/waves/round-90/receipts/c2-host-census.txt`, last line `exit: 0`)
recheck: python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills --fleet-root /home/vgpnk/Projects/shokunin (expect `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, exit 0 — the census guards measurability, not expected identity) and grep -c 'NAME-COLLISION' .ufo/waves/round-90/receipts/c2-name-collisions.txt (expect 1: the mandated count line, 0 collision-pair rows)

# Host installed-skill census (round 90 C2): the Windows-root claim re-pinned to this host's live root

## The measured line

    host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83
    exit: 0

Command (receipt `.ufo/waves/round-90/receipts/c2-host-census.txt`, first line `measured-rev:
6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`):

    python3 -B verifiers/check_host_skill_surfaces.py --skills-root /home/vgpnk/.agents/skills --fleet-root /home/vgpnk/Projects/shokunin

`83` is the plan's frozen population (`plans/round-90.md` § C2: N == 83), and 83 = 0 + 0 + 83 holds. The two
independent counts agree: the SKILL.md-holding directory count is 83 and the plan-time `ls | wc -l` is also 83
(`.ufo/waves/round-90/w1/ScoutHostRoots/roots-data.md` § 1a and § 1b). The root holds 78 real directories and 5
symlinked directories; all 83 hold a `SKILL.md`.

**Counting-method sensitivity, named.** `find` sees 78, because it does not follow symlinks; `ls`, the
`for d in .../*/` shell glob and `pathlib` see 83. The census instrument uses the symlink-following expression
(`[p for p in skills_root.iterdir() if p.is_dir()]`), so it measures 83 and matches the frozen N. A census arm
written with `find` would measure 78 and trip the frozen `N == 83` guard — a hazard for an implementer, not a
host defect.

## Why every surface is `lane-absent`

The census classifies an installed surface by matching its **directory name** against the fleet root's
`<name>/SKILL.md`. The intersection of the 83 installed names with the fleet-root entry names is **empty** — the
installed root is populated with omp skill names (`godot-*`, `blender-*`, `unity-*`, `unreal-*`, `speech-*`), while
the fleet root holds `*-shokunin` lane directories plus tooling. So every surface is `lane-absent`: 0 identical,
0 drifted.

This is a measurability classification, not an identity claim about any skill. The round-82/84 Windows hosts had
`identical 0, drifted 6, lane-absent 3` because those roots held shokunin lane copies; this host's root holds
none. No installed `SKILL.md` is byte-identical to any fleet lane `SKILL.md` either (0 of 83 sha256 prefixes
intersect the 19 fleet lane digests).

**The plan's findings duty is vacuous on this host.** `plans/round-90.md` § C2 names every `drifted` and
`identical` finding as a read-only finding routed to the owning lane. Neither class exists here: there are no
drifted surfaces and no identical surfaces, so there is nothing to route. That is an honest all-clear under the
plan's "the census guards measurability, not expected identity" reading, not a skipped duty.

## The NAME-COLLISION ledger

The round-72 A1 rule ("name is unique among the skills likely installed alongside it", `SKILL.md:295`) is
re-verified by extracting the frontmatter `name:` value (the first `name:` line within the first 12 lines) of
every installed `SKILL.md` and grouping by value.

    extracted names: 83, all distinct — duplicate frontmatter-name pairs found: 0

**NAME-COLLISION count: 0** — `grep -c 'NAME-COLLISION' .ufo/waves/round-90/receipts/c2-name-collisions.txt`
prints **1**, which is the mandated count line itself (0 collision-pair rows plus that line). The pair-row count is
0. Two independent extractions agree (the seat's awk pass and the scout's `sed -n '1,12{s/^name:...//p}'` pass),
and every installed entry's `name:` equals its directory name (0 mismatches, 0 empty extractions).

**Cross-root.** Across the two roots the round-84 ledger covered (`.agents` + `.zcode`) there are 18 duplicate-name
pairs, but every pair is the **same** surface reached twice through a `.zcode` → `.agents` symlink (identical
sha12 prefixes, e.g. `music 7d868f6f5a09` in both roots). Only 2 names are `.zcode`-local (`voicestudio`,
`voicestudio-maintainer`) and both are unique. So the round-84 Windows **class** — two distinct surfaces sharing
a name, each pair a live dir against a dated `.pre-adapt-backup-20260927` dir with different digests — **does not
exist on this host**: neither root holds a `.pre-adapt-backup-*` entry.

**One live root.** Only `/home/vgpnk/.agents/skills` is named by the frozen predicate. The three candidate roots
the scout brief named (`~/.omp/agent/skills`, `~/.omp/skills`, `~/.config/opencode/skills`) are **absent** on this
host. A wider read-only sweep found other agent-harness roots (`.ecc/skills` with 311 SKILL.md directories,
`.claude/skills` 24, `.grok/bundled/skills` 22, `.zcode/skills` 20, and more), none of which the frozen predicate
names; the census scope was **not** widened. The root's last mtime is 2026-10-29 03:33:05 -0300, so no entry has
been added, removed or renamed since then and the measured population is the population the census sees.

## Findings routed read-only (nothing repaired from here)

1. **No drifted and no identical finding exists on this host.** The plan's "name every drifted or identical
   finding" clause has nothing to name. There is no drift to route to a lane and no drift to fix.
2. **The A1 duplicate-name class is absent** in the live root (0 pairs). The 18 cross-root pairs are aliases of
   one surface under two root paths, not two surfaces under one name.
3. **Sibling surfaces overlap by root, not by identity.** The connector seat (`ConnectorOverlap`, § 2) found that
   kaidoku owns the REA skill identity on this same root (`kaidoku-shokunin/corpus/README.md:353`; its
   `corpus/knowledge/2026-10-13-rea-skill-contract.md`), and that game-dev-3d-shokunin names the same installed
   REA source as a reference. **kotoba's `lane-absent` classification for an installed skill is a measurability
   class, not an identity claim**; the REA-identity reading stays owned by kaidoku, and kaidoku's
   destination-drift finding is not kotoba's to fix.
4. **A census arm written with `find` would miscount this root** (78, not 83) — routed to whoever writes the
   next census arm; the frozen instrument is unaffected.

## Bounds

- The census hashes every installed `SKILL.md` read-only and matches by **directory name**. It does not read
  frontmatter, so it says nothing about a skill's declared identity, its description, or its trigger behaviour.
- `lane-absent` means "no fleet-root `<name>/SKILL.md` counterpart exists". It is not a claim that the skill is
  unowned, duplicated, or misinstalled.
- The census guards **measurability**, not expected identity: exit 0 means every installed surface was read and
  classified, and drift would be a named finding rather than an instrument failure. No pin exists for installed
  copies, so no drift is expected and none is demanded.
- The scope is the one root the frozen predicate names. The other live roots on this host were enumerated
  read-only by the scout and left unscored.
- The A1 ledger is a **name**-uniqueness check over the frontmatter `name:` value only. Two different directories
  with different names and identical bodies are invisible to it, and two directories with the same name and
  different bodies are visible — which is exactly the round-84 class.
- Nothing outside this lane was modified: no installed surface, host root, or file outside this repository was
  written by the census or the ledger.
