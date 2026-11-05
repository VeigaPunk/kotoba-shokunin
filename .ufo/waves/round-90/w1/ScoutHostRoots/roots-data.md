# ScoutHostRoots — host skills-root population (raw data only)

Seat: ScoutHostRoots. Round 90, wave r90-w1, C2 freshness (host installed-skill census re-pinned
to this host's live root). Measured read-only on 2026-11-05; host Linux 7.2.11-arch1-1, omp/18.15.0.

Scope note: this receipt is RAW DATA. No census run was performed here (ExecHostCensus owns
`verifiers/check_host_skill_surfaces.py` execution and the two `c2-*` receipts). No file outside
this seat's directory was written.

---

## 1. Live skills root population — both counts

### 1a. SKILL.md-holding directory count (the count the seat brief specifies)

```
$ for d in /home/vgpnk/.agents/skills/*/; do [ -f "$d/SKILL.md" ] && echo "$d"; done | wc -l
83
```

### 1b. The plan's frozen number (`ls | wc -l` at plan time)

```
$ ls /home/vgpnk/.agents/skills | wc -l
83
```

**Both numbers are 83 — they agree.** The plan's frozen `N == 83` (from `ls | wc -l`) equals the
SKILL.md-holding count. No difference to reconcile.

### 1c. Why the two counts agree here (structural, not coincidence)

```
$ cd /home/vgpnk/.agents/skills
$ find . -mindepth 1 -maxdepth 1 -type d  | wc -l     # real directories only
78
$ find . -mindepth 1 -maxdepth 1 -type l  | wc -l     # symlinks to directories
5
$ find . -mindepth 1 -maxdepth 1 -not -type d -not -type l | wc -l   # regular files
0
```

83 entries = 78 real dirs + 5 symlinked dirs + 0 plain files. All 83 resolve to a directory
holding a `SKILL.md`:

```
$ comm -3 <(ls -1 /home/vgpnk/.agents/skills | sort) \
         <(for d in /home/vgpnk/.agents/skills/*/; do [ -f "$d/SKILL.md" ] && basename "$d"; done | sort)
(no output)
```

The two sets are identical: every entry in the root holds a `SKILL.md`, and every `SKILL.md`
holder is an entry in the root. `ls | wc -l` counts the same 83 entries.

Note the counting-method sensitivity (a census implementer must know this):

```
$ find /home/vgpnk/.agents/skills -mindepth 2 -name SKILL.md | wc -l
78
```

`find` does **not** follow symlinks by default, so it sees 78, not 83. The 5 symlinked entries
(their targets are outside the root) are invisible to `find` but visible to `ls`, to the
`for d in .../*/` shell glob, and to Python `pathlib` (`Path.iterdir()` + `Path.is_dir()` follows
symlinks). `check_host_skill_surfaces.py:census()` uses
`[p for p in skills_root.iterdir() if p.is_dir()]` and then `(entry / "SKILL.md").exists()` —
both follow symlinks, so the instrument measures **83**, matching the frozen N. Verified by
replaying that exact expression:

```
$ python3 -c "
from pathlib import Path
r=Path('/home/vgpnk/.agents/skills')
dirs=[p for p in r.iterdir() if p.is_dir()]
rows=[p for p in dirs if (p/'SKILL.md').exists()]
print('iterdir is_dir entries:',len(dirs))
print('rows with SKILL.md:',len(rows))
print('symlinked rows:',len([p for p in rows if p.is_symlink()]))
print('real-dir rows:',len([p for p in rows if not p.is_symlink()]))"
iterdir is_dir entries: 83
rows with SKILL.md: 83
symlinked rows: 5
real-dir rows: 78
```

No nested `SKILL.md` below depth 2 (`find -mindepth 3 -name SKILL.md` → 0).

### 1d. The 5 symlinked entries and their targets

```
$ cd /home/vgpnk/.agents/skills && find . -mindepth 1 -maxdepth 1 -type l -printf '%p -> %l\n'
./omarchy -> /home/vgpnk/.local/share/omarchy/default/omarchy-skill
./tower   -> /home/vgpnk/Projects/ompskills/.omp/skills/tower
./shokunin -> /home/vgpnk/Projects/ompskills/.omp/skills/shokunin
./ufo     -> /home/vgpnk/Projects/ompskills/.omp/skills/ufo
./swarm   -> /home/vgpnk/Projects/ompskills/.omp/skills/tower/swarm
```

All five targets are outside the skills root, all five targets are readable, all five hold a
`SKILL.md`. `shokunin` is a symlink into `/home/vgpnk/Projects/ompskills/.omp/skills/shokunin`
(3 entries there: `shokunin`, `tower`, `ufo`); `swarm` resolves to a subdirectory of `tower`.

### 1e. Full entry list (83 names, `ls -1`)

```
2d-pixel-perfect          heuer-planning                optimize-audio
aaron                     initialize-ai-navigation      optimize-text-mesh-pro
agents                    localization                  optimize-web
agents-sdk                manage-sprite-atlas           orca-cli
aseprite                  migrate-birp-to-urp           orchestration
audio-setup-mixers        music                         physics-3d-collision
blender-animation-rigging new-unity-project             project-auditor-fixes
blender-compositing-nodes omarchy                       realtime
blender-geometry-nodes    onboarding                    reverse-engineer-anything
blender-modeling-modifiers openai-api-troubleshooting    setup-api-key
blender-physics-simulation openai-platform-api-key       shader-graph-create-custom-node
blender-python-scripting  optimize-audio                sound-effects
blender-scene-rendering   optimize-text-mesh-pro        speech-engine
blender-shader-nodes      optimize-web                  speech-to-text
blender-to-unity          orca-cli                      sprite-editor
build-chatgpt-app         orchestration                 swarm
chatgpt-app-submission    physics-3d-collision          text-to-speech
computer-use              project-auditor-fixes         tower
create-2d-physics         realtime                      tripo-cli
create-tile-palette-or-rule-tiles reverse-engineer-anything ufo
create-toolset            setup-api-key                 ui
dubbing                   shader-graph-create-custom-node ui-ugui
godot-2d-movement         sound-effects                 ui-uitk
godot-3d-essentials       speech-engine                 unity-cli
godot-animation           speech-to-text                unity-mcp-orchestrator
godot-audio               sprite-editor                 unity-package-management
godot-export              swarm                         unity-pipeline
godot-gdscript            text-to-speech                unreal-mcp
godot-gdscript-headless-testing tower                    unreal-skill
godot-multiplayer         tripo-cli                    update-skills-from-changelog
godot-nodes-scenes        ufo                           urp-postprocessing
godot-physics             ui                            voice-changer
godot-resources           ui-ugui                       voice-isolator
godot-shaders             ui-uitk
godot-signals-groups      unity-cli
godot-tilemap             unity-mcp-orchestrator
godot-ui-control          unity-package-management
godspeed                  unity-pipeline
```

## 2. Other candidate skills roots on this host

Command from the seat brief:

```
$ ls -d ~/.omp/agent/skills ~/.omp/skills ~/.config/opencode/skills 2>&1
ls: cannot access '/home/vgpnk/.omp/agent/skills': No such file or directory
ls: cannot access '/home/vgpnk/.omp/skills': No such file or directory
ls: cannot access '/home/vgpnk/.config/opencode/skills': No such file or directory
(exit 2)
```

**All three candidates named in the brief are ABSENT on this host.** `~/.omp/agent/` exists but
holds no `skills/` subdirectory (contents: `RULES.md`, `agent.db*`, `agents/`, `blobs/`,
`cache/`, `config.yml*`, …); `~/.omp/` itself holds `agent/`, `plugins/`, `profiles/`, `run/`,
`cache/`, `natives/`, `logs/`, `wt/`, … — no `skills/`.

Wider sweep for candidate roots (read-only), with counts of directories holding a `SKILL.md`:

```
/home/vgpnk/.zcode/skills          EXISTS  dirs_with_SKILL.md=20   entries=20
/home/vgpnk/.claude/skills         EXISTS  dirs_with_SKILL.md=24   entries=27
/home/vgpnk/.codex/skills          EXISTS  dirs_with_SKILL.md=2    entries=2
/home/vgpnk/.grok/skills           EXISTS  dirs_with_SKILL.md=14   entries=14
/home/vgpnk/.gemini/skills         EXISTS  dirs_with_SKILL.md=3    entries=3
/home/vgpnk/.minimax/skills        EXISTS  dirs_with_SKILL.md=13   entries=13
/home/vgpnk/.pi/agent/skills       EXISTS  dirs_with_SKILL.md=1    entries=1
/home/vgpnk/.prime/agent/skills    EXISTS  dirs_with_SKILL.md=3    entries=3
/home/vgpnk/.ecc/skills            EXISTS  dirs_with_SKILL.md=311  entries=311
/home/vgpnk/.hermes/skills         EXISTS  dirs_with_SKILL.md=1    entries=13
/home/vgpnk/.kimi-code/skills      EXISTS  dirs_with_SKILL.md=7    entries=7
/home/vgpnk/.cursor/skills         EXISTS  dirs_with_SKILL.md=3    entries=3
/home/vgpnk/.config/devin/skills   EXISTS  dirs_with_SKILL.md=13   entries=13
/home/vgpnk/.config/alma/skills    EXISTS  dirs_with_SKILL.md=0    entries=0
/home/vgpnk/.grok/bundled/skills   EXISTS  dirs_with_SKILL.md=22   entries=23
/home/vgpnk/.local/state/skills    EXISTS  dirs_with_SKILL.md=0    entries=0
/home/vgpnk/.ecc/.agents/skills    EXISTS  dirs_with_SKILL.md=46   entries=46
/home/vgpnk/.config/omarchy/skills ABSENT
/home/vgpnk/.config/claude/skills  ABSENT
```

The only root the plan's frozen predicate names is `/home/vgpnk/.agents/skills`. The
`~/.zcode/skills` root is the second root the round-84 A1 name-uniqueness ledger covered
(`C:/Users/jpvei/.zcode/skills` on the other host); on this host it exists with 20 SKILL.md
directories, of which **18 are symlinks into `~/.agents/skills`** and 2 are local
(`voicestudio`, `voicestudio-maintainer`).

```
$ cd /home/vgpnk/.zcode/skills && find . -mindepth 1 -maxdepth 1 -type l -printf '%p -> %l\n'
./agents -> ../../.agents/skills/agents
./computer-use -> ../../.agents/skills/computer-use
./dubbing -> ../../.agents/skills/dubbing
./heuer-planning -> ../../.agents/skills/heuer-planning
./music -> ../../.agents/skills/music
./onboarding -> ../../.agents/skills/onboarding
./orca-cli -> ../../.agents/skills/orca-cli
./orchestration -> ../../.agents/skills/orchestration
./realtime -> ../../.agents/skills/realtime
./reverse-engineer-anything -> ../../.agents/skills/reverse-engineer-anything
./setup-api-key -> ../../.agents/skills/setup-api-key
./sound-effects -> ../../.agents/skills/sound-effects
./speech-engine -> ../../.agents/skills/speech-engine
./speech-to-text -> ../../.agents/skills/speech-to-text
./text-to-speech -> ../../.agents/skills/text-to-speech
./update-skills-from-changelog -> ../../.agents/skills/update-skills-from-changelog
./voice-changer -> ../../.agents/skills/voice-changer
./voice-isolator -> ../../.agents/skills/voice-isolator
```

## 3. Fleet-lane-name matching

Fleet-root entries, filtered exactly as the seat brief specifies:

```
$ ls /home/vgpnk/Projects/shokunin | grep -v -e '^\.' -e '\.md$' -e '\.sh$' -e '\.json$' -e '\.conf$'
audio-shokunin
chousa-shokunin
exp-full
game-dev-2d-shokunin
game-dev-3d-shokunin
history-recheck
kagi-shokunin
kaidoku-shokunin
kake-shokunin
kama-shokunin
kasegi-shokunin
kengaku-shokunin
kotoba-shokunin
kotodama-shokunin
kumitate-shokinin
kumitate-shokunin
lore-shokunin
m-rev-vs-rev.py
mado-shokunin
mori-shokunin
research
revenger-shokunin
scripts
souji-shokunin
tabi-shokunin
tameshi-shokunin
templates
tools
tsukuroi-shokunin
```

(The filter leaves non-lane entries in: `exp-full`, `history-recheck`, `research`, `scripts`,
`templates`, `tools`, `m-rev-vs-rev.py`.)

### 3a. Exact installed-name ∩ fleet-entry-name intersection

```
$ ls -1 /home/vgpnk/.agents/skills | sort > /tmp/inst.txt
$ ls -1 /home/vgpnk/Projects/shokunin | sort > /tmp/fleet.txt
$ comm -12 /tmp/inst.txt /tmp/fleet.txt
(no output)
$ comm -12 /tmp/inst.txt /tmp/fleet.txt | wc -l
0
```

**Zero installed skill directory names equal a fleet-root entry name.** The installed root is
populated with omp skill names (`godot-*`, `blender-*`, `unity-*`, `unreal-*`, `speech-*`, …);
the fleet root holds `*-shokunin` lane directories plus tooling. No installed name matches a
lane name.

### 3b. Consequence for the census classification (inference, not a census run)

`check_host_skill_surfaces.py:census()` classifies by
`lane = fleet_root / entry.name / "SKILL.md"` — a **directory-name** match against the fleet
root. Since the intersection is empty, every one of the 83 installed surfaces resolves to
`lane-absent`. Verified by replaying the instrument's own expression:

```
$ python3 -c "
from pathlib import Path
r=Path('/home/vgpnk/.agents/skills')
fr=Path('/home/vgpnk/Projects/shokunin')
rows=[p for p in r.iterdir() if p.is_dir() and (p/'SKILL.md').exists()]
m=[p.name for p in rows if (fr/p.name/'SKILL.md').is_file()]
print('rows:',len(rows),'lane counterparts present:',len(m),m)"
rows: 83 lane counterparts present: 0 []
```

Expected summary for the frozen predicate's run (ExecHostCensus measures and records it; not run
here): `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83` — exit 0, since
the instrument guards measurability, not expected identity, and `I + D + A == N == 83` holds.

The 19 fleet lanes that DO carry a `SKILL.md` are named `*-shokunin`; their frontmatter `name:`
matches the directory name (except `lore-shokunin`, `revenger-shokunin`, `souji-shokunin`, whose
first-12-lines frontmatter has no `name:` line — those are lane-side facts, not installed-surface
facts):

```
$ for d in /home/vgpnk/Projects/shokunin/*/; do [ -f "$d/SKILL.md" ] && printf '%s -> %s\n' "$(basename "$d")" "$(sed -n '1,12p' "$d/SKILL.md" | sed -n 's/^name:[[:space:]]*//p' | head -1)"; done
chousa-shokunin -> chousa-shokunin
game-dev-3d-shokunin -> game-dev-3d-shokunin
kagi-shokunin -> kagi-shokunin
kaidoku-shokunin -> kaidoku-shokunin
kake-shokunin -> kake-shokunin
kama-shokunin -> kama-shokunin
kasegi-shokunin -> kasegi-shokunin
kengaku-shokunin -> kengaku-shokunin
kotoba-shokunin -> kotoba-shokunin
kotodama-shokunin -> kotodama-shokunin
kumitate-shokunin -> kumitate-shokunin
lore-shokunin ->
mado-shokunin -> mado-shokunin
mori-shokunin -> mori-shokunin
revenger-shokunin ->
souji-shokunin ->
tabi-shokunin -> tabi-shokunin
tameshi-shokunin -> tameshi-shokunin
tsukuroi-shokunin -> tsukuroi-shokunin
```

### 3c. Content-level overlap between installed surfaces and fleet lane copies

```
$ for f in /home/vgpnk/.agents/skills/*/SKILL.md; do [ -f "$f" ] && sha256sum "$f"; done | sort > /tmp/inst.sha   # 83 lines
$ for f in /home/vgpnk/Projects/shokunin/*/SKILL.md; do [ -f "$f" ] && sha256sum "$f"; done | sort > /tmp/fleet.sha # 19 lines
$ comm -12 <(cut -d' ' -f1 /tmp/inst.sha | sort) <(cut -d' ' -f1 /tmp/fleet.sha | sort) | wc -l
0
```

No installed `SKILL.md` is byte-identical to any fleet lane `SKILL.md`. Combined with the empty
name intersection, no installed surface is a copy of a lane copy under any name.

## 4. A1 name-uniqueness (round-72 rule) — raw measurement on this host

Extraction method = the round-84 ledger's method (`sed -n '1,12{s/^name:[[:space:]]*//p}'`,
i.e. the first `name:` line within the first 12 lines of each `*/SKILL.md`).

```
$ for d in /home/vgpnk/.agents/skills/*/; do
    sed -n '1,12p' "$d/SKILL.md" | sed -n 's/^name:[[:space:]]*//p' | head -1
  done | sort | uniq -c | awk '$1>1'
(no output)
$ ... | sort | uniq -c | awk '$1>1' | wc -l
0
```

**Within the live `.agents` root: 0 duplicate frontmatter names** (83 distinct names over 83
entries). The round-84 Windows host had 2 duplicate pairs (`godspeed`, `ufo`, each against a
dated `.pre-adapt-backup-20260927` dir); this host has **no** `.pre-adapt-backup-*` entries in
either root.

Every installed entry's frontmatter `name:` equals its directory name (0 mismatches, 0 empty
extractions, 83 extracted names).

Cross-root (`.agents` + `.zcode`, the two roots the round-84 ledger covered):

```
$ for r in /home/vgpnk/.agents/skills /home/vgpnk/.zcode/skills; do for f in "$r"/*/SKILL.md; do
    [ -f "$f" ] && sed -n '1,12p' "$f" | sed -n 's/^name:[[:space:]]*//p' | head -1
  done; done | sort | uniq -c | awk '$1>1'
      2 agents
      2 computer-use
      2 dubbing
      2 heuer-planning
      2 music
      2 onboarding
      2 orca-cli
      2 orchestration
      2 realtime
      2 reverse-engineer-anything
      2 setup-api-key
      2 sound-effects
      2 speech-engine
      2 speech-to-text
      2 text-to-speech
      2 update-skills-from-changelog
      2 voice-changer
      2 voice-isolator
(count = 18)
```

**18 duplicate-name pairs across the two roots — but every one of them is the SAME directory
reached twice** (the `.zcode` entry is a symlink into `.agents`). Their sha12 prefixes match
exactly (e.g. `agents 3bc7a5c3deb8` in both roots, `music 7d868f6f5a09` in both, `voice-isolator
2f2d5a9f330e` in both), which is the fingerprint of one surface under two root paths, not two
distinct surfaces. So the A1 "two skills with the same name" hazard is **not** present here in
the round-84 sense (there, the two members of each pair had DIFFERENT sha12s — a live dir and a
stale backup dir). Only 2 names are genuinely `.zcode`-local (`voicestudio` 368463ad5179,
`voicestudio-maintainer` 6e4fd239a362) and both are unique.

The A1 ledger on this host is a **0-collision** outcome for the live `.agents` root and an
18-alias / 0-distinct-collision outcome across the two roots.

## 5. Per-surface sha12 map for the census ledger (83 installed surfaces)

```
$ for f in /home/vgpnk/.agents/skills/*/SKILL.md; do
    printf '%s %s\n' "$(basename "$(dirname "$f")")" "$(sha256sum "$f" | cut -c1-12)"
  done | sort
2d-pixel-perfect 7bfae98a2cfa      audio-setup-mixers c1c5f7c8a678
aaron abbd19c74da4                 blender-animation-rigging ee3c26c76391
agents 3bc7a5c3deb8                 blender-compositing-nodes eccc10b164e3
agents-sdk 61830dccd552             blender-geometry-nodes ecb1106d47b6
aseprite def5a540600e               blender-modeling-modifiers bb5273698469
blender-physics-simulation e6c6fc917605   blender-python-scripting 48d51ed7a7df
blender-scene-rendering dab3b3ba6b23      blender-shader-nodes fad37a202b03
blender-to-unity 744edbee220f      build-chatgpt-app b4ba5e0847e9
chatgpt-app-submission c9b43ca8fe60  computer-use 2839933fd352
create-2d-physics 8c10bd5758ad    create-tile-palette-or-rule-tiles b3e5f3035ceb
create-toolset e9d050087f36        dubbing 790312851779
godot-2d-movement ea396576540a     godot-3d-essentials 6164f0230077
godot-animation 43a339c8445c      godot-audio 9ed39d72403e
godot-export 473552185df5          godot-gdscript 9039fb6de098
godot-gdscript-headless-testing 980ecf1815cb   godot-multiplayer 353319ed2559
godot-nodes-scenes fc0096a774a8    godot-physics e318719b4509
godot-resources 1c89eb8eaef4      godot-shaders e96ac075c0d8
godot-signals-groups eccc8d79a708  godot-tilemap c92a7103c764
godot-ui-control 0b2cc92d670c     godspeed 1d6167238784
heuer-planning 5ebc2548935e       initialize-ai-navigation aa6e28104296
localization ed9c68a34b58          manage-sprite-atlas fdd7ca9b5b7d
migrate-birp-to-urp d98dc798d150  music 7d868f6f5a09
new-unity-project b092707b6325    omarchy becd149e4d1c
onboarding b30585073f65            openai-api-troubleshooting 9fb4e152430c
openai-platform-api-key 780670286fb0   optimize-audio 2bfc211f6d8c
optimize-text-mesh-pro 6f5cf0b5b2d3   optimize-web e9ed91ca4009
orca-cli e9759aea664f              orchestration ce9a81cb2e6b
physics-3d-collision 5025949c81c   project-auditor-fixes f0103b324460
realtime 7fc54e609b36              reverse-engineer-anything 056dee0476d1
setup-api-key cc3dcecd5397         shader-graph-create-custom-node 927d3d953454
shokunin 59ca05018dbf              sound-effects f032efd85342
speech-engine 531737834dc9         speech-to-text 79744163f4ef
sprite-editor c959d892be2d         swarm fc1b8d8359bf
text-to-speech fcc105566df4        tower bec21921ce2b
tripo-cli 05665a14ab18             ufo 1553b46251e6
ui 5dbdf432ca8b                    ui-ugui a6fc4d59abe1
ui-uitk 23acfcdf652e               unity-cli b262ee34bba3
unity-mcp-orchestrator 3ac889d099d7  unity-package-management 047c293692b4
unity-pipeline 9a0c0c0ac50e        unreal-mcp 7ef8b991a82f
unreal-skill 7a0af781c458          update-skills-from-changelog 538f33eb86bf
urp-postprocessing 19735c6952ea    voice-changer 3ad09904d45b
voice-isolator 2f2d5a9f330e
```

## 6. Snapshot metadata

```
$ stat -c '%n mtime=%y' /home/vgpnk/.agents/skills
/home/vgpnk/.agents/skills mtime=2026-10-29 03:33:05.070317265 -0300
$ date -Is
2026-11-05T10:28:51-03:00
$ /home/vgpnk/.local/bin/omp --version
omp/18.15.0
$ uname -sr
Linux 7.2.11-arch1-1
```

The root's last mtime is 2026-10-29 03:33:05 -0300 — **no entry has been added, removed or
renamed in the root since then**, so the population measured at 10:28 on 2026-11-05 is the same
population the census sees when it runs.

## 7. Findings for the owning seats (read-only; nothing repaired)

1. **N == 83 confirmed on both counting methods.** The plan's frozen number and the
   SKILL.md-holding count agree; the census will measure 83. No discrepancy to route.
2. **Counting-method sensitivity is real and named**: `find` sees 78 (does not follow symlinks);
   `ls`, the `for d in …/*/` glob and `pathlib` see 83. Any census arm written with `find`
   instead of the instrument's `iterdir()` expression would measure 78 ≠ 83 and trip the frozen
   `N == 83` guard — that is an implementation hazard for ExecHostCensus, not a host defect.
   The frozen instrument (`verifiers/check_host_skill_surfaces.py`) already uses the
   symlink-following expression, so it is unaffected.
3. **The census will classify all 83 surfaces `lane-absent`** (0 identical, 0 drifted): the
   instrument matches on directory name and no installed name equals a fleet-root entry name.
   The frozen predicate's `I + D + A == N == 83` holds; an all-lane-absent outcome is a valid
   honest result under the plan's "guards measurability, not expected identity" reading.
   No `drifted` finding and no `identical` finding will exist on this host — the plan's
   "every drifted or identical finding … named in the report" clause is vacuous here.
4. **A1 name-uniqueness: 0 collisions in the live `.agents` root** (83 distinct names). Across
   `.agents` + `.zcode` there are 18 duplicate-name pairs, but each pair is the SAME surface via
   a `.zcode → .agents` symlink (identical sha12), unlike the round-84 Windows host where each
   pair had two different shas (live dir vs dated backup dir). The round-84 class of defect
   (two distinct surfaces sharing a name) does **not** exist on this host.
   The `.zcode` root is a second live root on this host (20 SKILL.md dirs) that the round-84
   ledger covered on the other host; the round-90 plan names only `.agents` as the census root.
5. **The three roots named in the seat brief are absent** (`~/.omp/agent/skills`,
   `~/.omp/skills`, `~/.config/opencode/skills`); the live root is `~/.agents/skills` alone.
   Many other agent-harness roots exist on this host (`.ecc/skills` with 311 SKILL.md dirs,
   `.claude/skills` 24, `.grok/bundled/skills` 22, …) but none is named by the frozen
   predicate; the census is scoped to `.agents` and that scope is not widened here.
