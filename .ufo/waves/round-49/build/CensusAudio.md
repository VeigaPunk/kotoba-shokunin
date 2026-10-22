ROW | audio | main (detached HEAD) | 7a2fcd4f08831154686e4e323031f41fffdb077f | NONE | none | no | no | PROVINCE.md:3-4 | "Owns: game audio production — SFX (UI, impacts, movement, ambience) and soundtrack (motifs, loops, stems, adaptive layers)"

# Round 49 C1 — sibling-overlap census: audio-shokunin

Date 2026-10-22. Seat KotobaR49.CensusAudio (leaf, no dispatch). Surface:
`/home/vgpnk/Projects/shokunin/audio-shokunin`, read-only via
`git -C … rev-parse/symbolic-ref/ls-tree/show/grep/log`. No edit, no jj, no git write, no
pacman transaction, no tool installs (nothing needed).

## Findings

1. **Classification `none`.** audio-shokunin owns game-audio *content*: SFX, ambience,
   soundtrack motifs/loops/stems/layers, plus headless measurement (duration, loudness,
   spectral content, loop-seam continuity). It holds no claim over SKILL.md craft,
   frontmatter/trigger discipline, agent definitions, AGENTS.md-class files, dispatch
   prompts, or any executable instrument over those surfaces. It has no `verifiers/`
   directory (0 files) and never ships a SKILL.md on any ref.
2. **No SKILL.md at the pinned commit, and none in history.** README.md:12-13 says the
   file is "absent on lanes still in shonen seed form"; SHONEN.md:5 still has its
   `SKILL.md contains real decision tables, error patterns, checklists, cited sources`
   box unchecked (`[ ]`). The promotion checklist is fleet-mint text, not an audio
   province claim.
3. **The lane names no kotoba anywhere.** `git grep -li kotoba HEAD` over 50,576 tracked
   files returns 0 files. No frontmatter description exists (no SKILL.md), so the
   description-names-kotoba and arbitration-clause fields are both `no` by absence.
4. **audio does its own adjacency bookkeeping without kotoba.** PROVINCE.md:53 names
   game-dev-2d, game-dev-3d, lore, chousa and the operator as its adjacent parties;
   PROVINCE.md:13-15 refuses perceptual claims, rights clearance, engine mutation, game
   mechanics (game-dev-2d) and narrative canon (lore). kotoba is not a party to it.
5. **Residual (not a gap in the row, a rule for the census author).** The boundary is
   *latent*: if audio ever promotes, its own SKILL.md would sit on kotoba's form surface
   while its content stays audio's. The rule I applied is observed-claim-at-pin: a lane is
   `none` unless it claims craft ownership (own or other lanes') or a live interface
   exists at the pinned commit. kumitate shows the `adjacent` shape (both sides name the
   same split); audio shows neither side naming the other.
6. **Unknown left open.** The 11 `wt-r90`…`wt-r100` branches were spot-checked only on
   `wt-r100`/`wt-r99` (0 SKILL.md each); the row pins `HEAD` == `main`, which is the
   lane's integrated tip, so other worktree heads are not part of this row.

## Evidence

### Pin (Q13: command + date)

```
$ git -C /home/vgpnk/Projects/shokunin/audio-shokunin rev-parse master
fatal: ambiguous argument 'master': unknown revision or path not in the working tree.
EXIT=128
$ git -C … symbolic-ref -q HEAD
fatal: ref HEAD is not a symbolic ref            # SYM_EXIT=128
$ git -C … rev-parse HEAD
7a2fcd4f08831154686e4e323031f41fffdb077f       # EXIT=0
$ git -C … rev-parse main
7a2fcd4f08831154686e4e323031f41fffdb077f       # EXIT=0, HEAD == main tip
$ git -C … log -1 --format='%H %ad %s' --date=iso-strict HEAD
7a2fcd4f08831154686e4e323031f41fffdb077f 2026-10-21T10:19:08-03:00 considerthese: 2026-10-21 daily reflection
$ git -C … branch --format='%(refname:short)'
(no branch) main wt-r100 wt-r99 wt-r95 wt-r94 wt-r96 wt-r97 wt-r98 wt-r90 wt-r91 wt-r92 wt-r93
```

Branch recorded as `main (detached HEAD)`: `master` does not exist (exit 128) and `HEAD`
is not symbolic (exit 128); the detached commit is byte-identical to `main`.

### Top-level skill files

```
$ git -C … ls-tree --name-only 7a2fcd4
.gitignore LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md considerthese corpus generate_timings.sh ports reports
$ git -C … ls-tree -r --name-only 7a2fcd4 | grep -E '^(skills?/[^/]+/)?SKILL\.md$'
(no output)                                       # exit 1
$ git -C … ls-tree -r --name-only 7a2fcd4 | grep -E 'SKILL\.md$'
(no output)                                       # exit 1, all depths
$ git -C … ls-tree -r --name-only 7a2fcd4 | wc -l
50576
$ git -C … log --all --diff-filter=A --name-only --pretty=format: -- '*SKILL.md'
(no output)                                       # exit 0, never added on any ref
$ git -C … ls-tree -r --name-only wt-r100 | grep -cE 'SKILL\.md$'   # 0
$ git -C … ls-tree -r --name-only wt-r99  | grep -cE 'SKILL\.md$'   # 0
```

### Required `none` sweep (Q14: negative claim carries its sweep)

```
PAT='SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'
for f in README.md PROVINCE.md SHONEN.md SCORECARD.md LOG.md; do
  git -C … show 7a2fcd4:$f | grep -cE "$PAT"; done
README.md 1 · PROVINCE.md 3 · SHONEN.md 1 · SCORECARD.md 3 · LOG.md 9      TOTAL 17 lines
per pattern over the same 5 files (grep -ciE):
SKILL\.md 2 · prompt 1 · AGENTS\.md 0 · frontmatter 0 · trigger 12 · description 4 · kotoba 0
$ git -C … grep -li kotoba HEAD | wc -l                     # 0 files
$ git -C … grep -liE 'AGENTS\.md|frontmatter' HEAD | wc -l  # 0 files
$ git -C … ls-tree -r --name-only HEAD | grep -E '(^|/)(AGENTS|CLAUDE)\.md$' | wc -l      # 0
$ git -C … ls-tree -r --name-only HEAD | grep -E '^(skills?|\.agents|\.claude)/' | wc -l  # 0
$ git -C … ls-tree -r --name-only HEAD | grep -E '^verifiers/' | wc -l                    # 0
$ git -C … show 7a2fcd4:corpus/QUALITY.md | grep -cEi 'SKILL\.md|frontmatter|prompt|AGENTS\.md|kotoba'
0                                          # exit 1
```

Every one of the 17 sweep lines is an audio-domain sense or a reference to the lane's own
absent deliverable, not skill/prompt craft:

- README.md:12, SHONEN.md:5 — `SKILL.md` as the lane's own future output.
- PROVINCE.md:26,27 — "layer triggers/mixer", "runtime trigger".
- PROVINCE.md:53 — "Engine integration/triggers".
- LOG.md:1622-1624 — "C1 trigger → action → outcome" claim-ledger rows.
- SCORECARD.md:70,831,832 — "description" = derived-vs-passthrough `pactl` module arg.
- LOG.md:311 — the only `prompt` token: `rlm.spawn(prompt, "name=" + "r17-replay")`, a
  runtime API argument in a verifier log, not prompt authoring.
- `frontmatter`, `AGENTS.md`, `kotoba`: zero hits anywhere in the tree.

### Quotes (located at 7a2fcd4)

- Scope, PROVINCE.md:3-4 — `Owns: game audio production — SFX (UI, impacts, movement,
  ambience) and soundtrack (motifs, loops, stems, adaptive layers)` (17 tokens,
  ≤25; the em dash is one token).
- Corroborating, README.md:6 — `**Domain:** Game audio production — SFX and soundtrack —
  verified by headless analysis: duration, loudness, spectral content, loop-seam
  continuity.`
- Seed-form evidence, README.md:12-13 — `` `SKILL.md` — the distilled expertise: decision
  tables, error patterns, checklists (absent on lanes still in shonen seed form — see
  `corpus/`) ``.
- No-overlap quote, PROVINCE.md:53 (full line) — `Engine integration/triggers, bus
  routing, runtime peak monitoring, and game mechanics (game-dev-2d / game-dev-3d);
  narrative canon (lore); sample-rights clearance and publishing (operator); research
  method (chousa); middleware licensing/integration (FMOD/Wwise — record only).`

### Verification discipline

No web source was needed: the question is answered entirely by the sibling's own tracked
bytes, so no URL/byte-count/sha256 record applies. All counts above are from the commands
shown, run 2026-10-22 (UTC) against pinned commit 7a2fcd4. Unrun: no build, test or lint
applies to this read-only census seat.

Report: .ufo/waves/round-49/build/CensusAudio.md
