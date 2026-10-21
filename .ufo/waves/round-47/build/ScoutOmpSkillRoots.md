verdict: The SKILL.md:12-15 claim holds for every `*-shokunin` lane file at BASE — none is under an omp 18.12.5 discovery root, and 0/806 live session catalogues offer a lane skill; but the root list in SKILL.md:91 (and corpus rule 12) is stale: `~/.claude/skills` is double-gated OFF by default in 18.12.5, and several other root classes are missing.

# omp 18.12.5 skill discovery roots — C2 evidence

Scope: frozen snapshot `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`
(`strings -n 4` of `bin/omp-18.12.5`, ELF sha256 `fdbc8136084c9a10…` per
`SHA256SUMS`; strings sha256 `33df0aeffc456596…`), host `omp --version` →
`omp/18.12.5` (exit 0), `~/.omp/agent/config.yml` (read in full), environment
(`CLAUDE_CONFIG_DIR`, `PI_CODING_AGENT_DIR`, `OMP_PROFILE` all unset).
**Line numbers below are lines of the strings dump, not omp source lines.**
BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; BASE `SKILL.md` sha256
`c8b245b7dd2cfeb9…`.

## The roots, as 18.12.5 actually composes them

Ten skill providers register on capability `Tl.id`: native, omp-managed,
agents, claude, claude-plugins, codex, opencode, github, skillshare,
omp-plugins — plus `skills.customDirectories`. A scan is `<root>/<dirname>/SKILL.md`,
dot-entries skipped (`S.name.startsWith(".")`, dump:862720), symlinked dirs
followed, `frontmatter.enabled: false` and (where `requireDescription`) empty
descriptions dropped (`ga`, dump:862672-862730).

| # | Provider (id) | Root(s) | Level / walk | Effective at BASE on this host | Dump evidence |
|---|---|---|---|---|---|
| 1 | native (`native`, priority 100) | `<agentDir>/skills`; `<walk-dir>/.omp/skills` | user; project walk-up | ON (`enablePiUser`/`enablePiProject` default true); both dirs absent | 896038, 896040, 896226-896258; agentDir 644704 + 644569-644575; `.omp` 644414, 862444-862457 |
| 2 | omp-managed (`omp-managed`, 5) | `<agentDir>/managed-skills` | user | always on; absent | 895904, 895907, 896247-896265 |
| 3 | agents (`agents`) | `~/.agent/skills`, `~/.agents/skills`; `<walk-dir>/.agent/skills`, `<walk-dir>/.agents/skills` | user; project walk-up | ON (`enableAgentsUser`/`Project` default true); **`~/.agents/skills` = the only populated root** | 897787, 897790 (`HO=[".agent",".agents"]`), 897825 (`fte`), 897838-897868 |
| 4 | claude (`claude`, 80) | `<walk-dir>/.claude/skills`; `~/.claude/skills` | project walk-up; user | project ON (`enableClaudeProject` true); **user OFF — two gates**: `skills.enableClaudeUser=false` AND provider opt-in `Ii("claude")` false (no `enabledProviders`, no `CLAUDE_CONFIG_DIR`) | 896820, 896829-896836 (`el`), 896920-896960 (`Pee`), 897200; 861723; 862059-862079 (`Ii`); 861880-861889 (`ge`) |
| 5 | claude-plugins (`claude-plugins`) | `~/.claude/plugins/**` marketplace plugin skill dirs | user/project, origin-tagged | OFF (opt-in `ge["claude-plugins"]`); 35 `SKILL.md` exist under `~/.claude/plugins/{marketplaces,synced}` but none is offered (`cache/` itself absent) | 897273, 897376, 897701, 861880-861889 |
| 6 | codex (`codex`, 70) | `<cwd>/.codex/skills`; `~/.codex/skills` | **cwd only**; user | project ON but cwd-only; user OFF (`enableCodexUser=false`, no opt-in); `~/.codex/skills` holds 5 `SKILL.md` under `.system/`, all skipped as dot-entries | 898296-898306 (`ua`), 898422-898441 (`Ete`), 898615; 861722; 862720 |
| 7 | opencode (`opencode`) | `<cwd>/.opencode/skills`; `~/.config/opencode/skills` | **cwd only**; user | project ON but cwd-only; user OFF (`Xl` → `Ii("opencode")` false); user dir absent | 899025, 899200-899215 (`ene`), 899299; 862506-862509 (`Xl`); 862510-862514 (`Fo`) |
| 8 | github (`github`) | `<cwd>/.github/skills` | **cwd only**, no user root (`userAgent: null`) | project ON; absent | 899322, 899466-899476 (`mne`), 899497; 862487-862491, 862510-862514 |
| 9 | skillshare (`skillshare`, 95) | store `~/.omp/skillshare/@scope/name/<version>/SKILL.md`, driven by `~/.omp/agent/skills.lock.json` and `<walk>/.omp/skills.lock.json` | user/project | none installed (both lock files ENOENT) | 899870, 899972, 900000-900032 |
| 10 | extension packages (`omp-plugins`, 90) | `<extension-package>/skills` for configured extension roots | user/project | none (`bu=[]`; no `extensions:` in config) | 894772, 894840-894860, 899611-899630 |
| 11 | custom (`custom`) | each `skills.customDirectories` entry (`dir/*/SKILL.md`, `requireDescription`) | user | none configured (`skills` key absent) | 861736, 964289, 964376-964400, 964509-964520 |

Master switch / filters: `skills.enabled` default true (861712); `skills.ignoredSkills`
and `skills.includeSkills` are glob name filters, not roots (defaults
964376-964400; applied 964427-964436).

Walk-up semantics: `xOe` walks `cwd → repoRoot ?? home` (`TBt`, stops at
home/tmpdir/`/tmp`/`/var/tmp`; skips the home dir itself) — dump:896061-896088,
862985-862994. So "project walk-up" applies to `.agent`, `.agents`, `.claude`,
`.omp` only; `.codex`, `.opencode`, `.github` scan **cwd only** (`Fo` =
`join(cwd, projectDir, n)`, 862510-862514).

Provider gates (`df`, dump:964395-964415): native user→`enablePiUser`, native
project→`enablePiProject`, agents user/project→`enableAgents*`, claude
project→`enableClaudeProject`, claude user→`enableClaudeUser || Ii("claude")`,
codex user→`enableCodexUser || Ii("codex")`, other user→`Ii(provider)`, project
otherwise true. `Ii` (862059-862079) refuses any provider in the `ge` opt-in map
(dump:861880-861889: cursor, codex, claude, claude-plugins, gemini, opencode,
windsurf, github) unless named in `enabledProviders`/explicitly included — here
the config has no provider keys at all.

## Claim check — SKILL.md:12-15 at BASE

Claim as written: "the shokunin files are not in an omp skill discovery root, so
their descriptions never reach the `<skills>` router".

- All 18 `*-shokunin/SKILL.md` in the working tree under
  `/home/vgpnk/Projects/shokunin` (lane BASE checkout; the fleet root is its own
  git repo), including the five named at SKILL.md:10-11 and this lane's own file, resolve
  outside every root shape: a scripted ancestor scan
  (`*/{.agent,.agents,.claude,.omp,.opencode,.codex,.github}/skills`) returned
  `root_hit=none` for kagi, kake, kasegi, kengaku, kumitate, kotoba, chousa and
  the rest.
- User roots: `~/.agents/skills` has 10 entries whose realpaths are
  `~/Projects/ompskills/.omp/skills/{shokunin,tower,tower/swarm,ufo}`,
  `~/.local/share/omarchy/default/omarchy-skill`, and five self dirs
  (`create-toolset`, `godspeed`, `reverse-engineer-anything`, `unreal-mcp`,
  `unreal-skill`); `~/.agent`, `~/.omp/agent/skills`,
  `~/.omp/agent/managed-skills`, `~/.config/opencode/skills`,
  `~/.omp/skillshare` and both lock files are ENOENT. `~/.claude/skills` exists
  but its user root is gated off (row 4); `~/.codex/skills` exists with five
  `SKILL.md` under `.system/` (dot-dir, never scanned).
- Project roots: `/home/vgpnk/Projects/shokunin/.omp/` contains only
  `agents/executor.md`; no `.agent(s)`, `.claude`, `.opencode`, `.codex`,
  `.github`, `.omp/skills` anywhere to depth 3.
- Live second witness: 806 `/home/vgpnk/Projects/shokunin` session transcripts
  (store spans 2026-10-14 → 2026-10-21; newest under the current 18.12.5
  install) carry a `<skills>` block; every offered name is one of the 10
  `~/.agents/skills` entries (seven names in all 806; `create-toolset`,
  `unreal-mcp`, `unreal-skill` only in the 177 newest). Catalogue line count 10, source
  `…/sessions/-Projects-shokunin/2026-10-21T03-31-39-302Z_…/MadoR22.jsonl`
  (byte offset 2322). Zero occurrences of any lane name as a catalogue entry
  across the slug; the one `kagi-shokunin:` string hit is prose in a task
  prompt (`CloseKama18.jsonl`), not a catalogue line. Template `<skills>` is
  in the ELF at dump:2423496.

**Verdict: true for the lane files.** But the sentence is falsifiable as read
broadly — see counterexample 1 — and the parenthetical root list at SKILL.md:91
is factually stale for 18.12.5.

## Counterexamples and near-misses (do not pad these away)

1. `~/.agents/skills/shokunin` **is** a discovery-root entry: a symlink to
   `/home/vgpnk/Projects/ompskills/.omp/skills/shokunin/SKILL.md` (4 477 B,
   name `shokunin`), offered in 806/806 catalogues. The lane sentence means the
   five `*-shokunin` files, but a reader who checks `~/.agents/skills/shokunin`
   finds a counterexample. Scope the noun, not the mechanism.
2. The fleet's own skills reach no root by design; sibling projects do it by
   symlink — `tower`, `swarm`, `ufo` in `~/.agents/skills` all point into
   `~/Projects/ompskills/.omp/skills/…`. That symlink is the one operation that
   would falsify the claim.
3. `/home/vgpnk/Projects/shokunin/.devin/skills/{flashseat,glmseat}/SKILL.md`
   are skills at a bare(ish) fleet path, but `.devin` is a Devin surface:
   `grep -c '".devin"' omp-18.12.5.strings` → 0. Not an omp root.
4. `~/.claude/skills` is present (omarchy symlink + `synced/<uuid>/…`, no
   `synced/SKILL.md`), and `~/.claude/plugins` holds 35 `SKILL.md`
   (`marketplaces/claude-plugins-official` 33, `synced/…` 2); both roots are
   inert here — `enableClaudeUser` false, no opt-in, and no `claude-plugins`
   enablement. Listing `~/.claude/skills` as an omp root without the gate is
   wrong for the default config.
5. SKILL.md:48 evidence base cites `~/.config/opencode/skills/ufo/SKILL.md`;
   `~/.config/opencode/` holds only `cli.json`, `opencode.json`, `service.json`
   — that path does not exist at BASE (adjacent stale citation; opencode root
   is gated off here anyway).
6. Corpus rule 12 (`corpus/knowledge/frontmatter-trigger-surface.md:150-155`,
   BASE sha256 `ec78527661548975…`) says "the six `*-shokunin` files"; the fleet
   root now has **18** `*-shokunin/SKILL.md`. Same unconditional
   `.claude/skills, marketplace cache` phrasing as SKILL.md:91.

## C2 wording implications (advice, not a production edit)

- The `<skills>` token C2 removes sits inside the folded `description` scalar
  (SKILL.md:3-15; frontmatter `<skills>` count 1, folded description 814 chars).
  The claim sentence is therefore description text, not body text.
- Keep the claim, but name the object: "the `*-shokunin` lane SKILL.md files
  (this one included) sit at bare repo roots, outside every omp discovery root,
  so their descriptions never reach the `<skills>` catalogue." That stays true
  after the tag removal and survives check of `~/.agents/skills/shokunin`.
- Do **not** add a root list to the description (already 814 chars, and the
  deterministic preview of it would be
  `Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /…`
  — 94 chars, `[INFERENCE]` by replaying `xze`, dump:1066738-1066750 with
  `v = 100` at 1066684). Root enumeration belongs in the body table.
- If L1 also fixes SKILL.md:91 and corpus rule 12 this round, use the table
  above; the minimal correction is "(+ `.omp`, `.agent`, `.opencode`, `.codex`,
  `.github`, managed-skills, custom dirs; `~/.claude/skills` and
  `~/.codex/skills` are opt-in user roots, project roots for codex/opencode/
  github are cwd-only)".
- Cache-key note (C2 calibration): the description is part of the key
  (`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ description)`, dump:1066734); since
  kotoba is not offered there is no row to invalidate, so the edit is
  render-neutral today.

## Commands run (exit codes)

- `sha256sum /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` → `33df0ae…`; dump `SHA256SUMS` matches; `omp --version` → `omp/18.12.5` (0).
- `grep -c -F '.agents/skills' omp-18.12.5.strings` → 2 (0); `grep -c -F '.omp/agent/skills'` → 0 (1); `grep -c -F 'Load skills from'` → 12 (0, six provider descriptions ×2: docs + registration).
- `grep -c '^skills:' ~/.omp/agent/config.yml` → 0 (1); `enabledProviders` → 0 (1); `^extensions:` → 0 (1); `customDirectories` → 0 (1).
- `ls -d ~/.omp/agent/skills ~/.omp/agent/managed-skills ~/.config/opencode/skills ~/.omp/skillshare ~/.agent` → all ENOENT (2); `~/.claude/skills`, `~/.codex/skills`, `~/.claude/plugins` exist (0). `find ~/.codex/skills -maxdepth 6 -name SKILL.md | wc -l` → 5 (all under `.system/`); `find ~/.claude/plugins -maxdepth 8 -name SKILL.md | wc -l` → 35.
- `find /home/vgpnk/Projects/shokunin -maxdepth 2 -name SKILL.md -path '*-shokunin/*' | wc -l` → 18 (0); ancestor-root scan over those files → `root_hit=none` (python, 0).
- `git show c61a973…:SKILL.md | sha256sum` → `c8b245b7…` (0); frontmatter `<skills>` count 1, folded description 814 chars (python, 0).
- Catalogue census over `~/.omp/agent/sessions/-Projects-shokunin/*/*.jsonl` → 806 files with `<skills>`, names = 10 agents-root entries, no lane names (python, 0); same census for `-Projects-shokunin-tameshi-shokunin` (50) and `-tmp` (38) also shows only those names.
- No tool installed or upgraded this seat.

## What I did NOT check

- Did not run `omp skill list` or any omp session (the contract permits only `omp --version`); root activity is derived from the 18.12.5 dump, the config, the filesystem, and the captured catalogues, not from a live planted-skill probe.
- Did not run `verifiers/verify_harness_claims.py`, `verify_surfaces.py`, `check_substrate_pins.py` or any lane gate — none is named in my item.
- Did not compare against omp 18.12.3/earlier dumps, so "stale" means "contradicted by 18.12.5", not "changed at a named version".
- Did not verify the opencode-side root list (opencode 1.19.3 dump); SKILL.md:92 is out of this item's scope.
- `~/.claude/plugins/cache` is absent; the 35 plugin `SKILL.md` live under
  `marketplaces/` and `synced/`, so marketplace offering was reasoned from the
  code gate, not from a run. Extension-package roots checked by code + absence
  of config.
- Session census covers three project slugs, not every slug on the host.
