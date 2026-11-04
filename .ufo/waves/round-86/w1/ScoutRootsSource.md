# ScoutRootsSource — r86 w1 report

Scope: which directories omp 18.15.0 scans for skills when it builds a session's `<skills>` catalogue, in what order, and how it resolves a name found in two roots. Everything below comes from the source embedded in `/home/vgpnk/.local/bin/omp` (sha256 `6737ee24…7b0f`, matches the plan pin). The full table is in `w1/ScoutRootsSource/source-packet.md`: 138 statement rows, each with a byte offset and a quote, and each quote re-checked byte-for-byte against the ELF (138/138). Excerpts are in `w1/ScoutRootsSource/extract.txt`: 298 lines, each line re-checked at its offset.

## Observed (source)

- Entry point: `async function Dp(` (exported as `loadSkills`) in `extensibility/skills.ts` @177499125. It calls the capability registry, `kn(zl.id, …)` with `zl` = `id: "skills"`. Eleven providers register for that capability, listed here by priority:
  - native `.omp`: 100
  - skillshare: 95
  - omp-plugins: 90
  - claude: 80
  - agent-plugins: 75
  - claude-plugins, agents, codex: 70 each
  - opencode: 55
  - github: 30
  - omp-managed: 5

  On top of the providers, `Dp` scans the custom directories itself.
- Setting defaults (`extensibility/settings.ts` @172765236–172765972):
  - `skills.enableCodexUser` false, `skills.enableClaudeUser` false
  - `skills.enableClaudeProject` true
  - `skills.enablePiUser` true, `skills.enablePiProject` true (these gate the native `.omp` roots)
  - `skills.enableAgentsUser` true, `skills.enableAgentsProject` true
  - `skills.customDirectories`, `skills.ignoredSkills` and `skills.includeSkills` all default to `[]`

  The opt-in providers are claude, codex, claude-plugins, opencode, github, cursor, gemini and windsurf. They load at user level only when the matching setting is on, `enabledProviders` lists them (or `*`/`all`), or, for claude, `CLAUDE_CONFIG_DIR` is set.
- Layout: the scanner `Ba` (`discovery/helpers.ts` @172790251) reads only `<root>/<name>/SKILL.md`. It does not recurse and skips names starting with `.`. It accepts directory and symlink entries. The skill name is the frontmatter `name`, falling back to the directory name. `enabled: false` drops a skill. `requireDescription` applies only to native, custom, managed, github and omp-plugins.
- Project walk-up:
  - Native `.omp`, `.claude` and `.agent`/`.agents` walk every ancestor from cwd up to the nearest ancestor that holds a `.git` entry (inclusive), or up to home if there is none. Home itself is skipped.
  - The native walk also stops at the tmp directories, skips the `~/.omp` lookalikes, and when there is no git root it skips any directory that has its own `.omp/agent`.
  - `.codex`, `.opencode` and `.github` are read in cwd only.
- Name collisions, step by step:
  1. Providers run in priority order. A `SKILL.md` whose realpath was already accepted is skipped.
  2. If the name is already taken and the body and frontmatter are identical, the later copy is dropped.
  3. If the content differs, the later copy is kept under the name `<ns>/<name>` (with `~2`, `~3`… on a further clash).
  4. There are two exceptions. A custom-directory skill takes the bare name from an earlier non-custom skill. A skillshare skill loses the bare name to a later non-skillshare skill. The loser in either case is renamed `<ns>/<name>`.
  5. Managed skills are added last, and only for names no other provider claimed.
  6. The `ignoredSkills` / `includeSkills` globs and `disabledExtensions` entries of the form `skill:<name>` are applied.
  7. The list is sorted by name.
  8. The catalogue renders only skills with `hide !== true`. `hide` is set when the frontmatter has `hide: true` or `disableModelInvocation: true` (`system-prompt.ts` @178835365).

## Observed (host, read-only)

- `~/.omp/agent/config.yml` has no skills, extensions or provider keys, so every gate is at its default.
- The plugin lock lists `ecc-pi-core` (a symlink, with a `pi` manifest and `skills/` holding 132 entries) and `unreal-engine-skills-omp` (no `skills/` directory).
- The Claude marketplace plugins are Claude-origin and user-scope, so they are filtered out.
- The fleet cwd is its own git root and has no project skill directories.
- Result: `~/.agents/skills` (83) + `~/.omp/plugins/node_modules/ecc-pi-core/skills` (132) = **215**, with 0 overlapping names. All 132 base `not-discovered` names are in `ecc-pi-core/skills`.

## Findings

- F1: the root the model is missing is the **omp-plugins extension root** (`~/.omp/plugins/node_modules/<pkg>/skills`, found through `~/.omp/plugins/package.json` + `omp-plugins.lock.json`). For the ledger, `const R = yo.join(u, "node_modules");` @173767148, `const ue = oe.omp || oe.pi;` @173768743 and `dir: Zo.join(R.path, "skills"),` @173914936 are located quotes (exact offsets are in the packet).
- F2: `~/.claude/skills` and `~/.codex/skills` exist on the host but are **off by default** in 18.15.0. A model that adds them would add names the catalogue does not have (27 + 2 dirs).
- F3: omp-plugins hard-codes `<pkg>/skills`. It ignores the manifest's `skills` key, so `pi.skills: ["./skills"]` only matches by coincidence.

## Risks / unresolved

- I inferred the order of the three equal-priority-70 providers from byte order. It has no effect on this host.
- I did not observe the rendering session's environment variables (`CLAUDE_CONFIG_DIR` etc.). This seat's shell has them unset.
- I read `yne` (the claude-plugin manifest key) and the project plugin-registry walk only in part. Neither applies on this host.

No tools were installed. I wrote nothing outside `w1/ScoutRootsSource/` and this report.
