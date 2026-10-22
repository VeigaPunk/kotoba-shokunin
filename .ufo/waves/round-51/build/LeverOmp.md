# LeverOmp — what the lane's own harness (omp 18.12.6) documents/implements for keeping one of two overlapping skills from being chosen

HOLDS-BOUNDED — applies to the advisory "omp (the lane's harness)" paragraph of
`corpus/knowledge/skill-overlap-levers-round51.md`, which is **outside the 7-client counter**
(`verifiers/check_overlap_levers.py` pins 7 clients; omp is not one of them and is not counted).
omp documents **no** tie-break between two differently named skills whose descriptions both match;
what it implements is *removal from the model's candidate set*, keyed on frontmatter, name, source
or operator config — never on description wording. The draft paragraph is delivered as text for
the L1 to integrate; I did not write the knowledge file (it does not exist yet; another seat owns it).

## 1. The arbitration rule omp states (and its absence)

- The only selection rule the harness gives the model is description matching, in the bundled
  model-facing skill prompt: "Use the read tool to load a skill's file when the task matches its
  description." — embedded prompt `/$bunfs/root/skill-6kx0z31r.md`, source
  `packages/coding-agent/src/prompts/internal-urls/skill.md` (bundle comment at binary byte
  158603513); prompt bytes 249892437–249893142, quoted sentence at byte 249892527. **Not in the
  `omp://` doc tree** (code-only location).
- `omp://skills.md:21`: "The capability validator only requires `name` and `path`; individual
  providers impose additional frontmatter requirements. Matching quality depends on `description`
  being meaningful." — the same conclusion as the round-50 finding for the other clients.
- Sweep for a multi-match rule: `strings` over the 18.12.6 binary for `if more than one skill`,
  `when multiple skills`, `more than one skill matches`, `two skills match`, `skills match`,
  `unique skill name(s)` → **no output**. The listing template carries only `<name>`,
  `<description>`, `<location>` — no precedence field.

## 2. Levers, one by one (key term — quote — documented / code-only)

| # | key term | located quote | status |
|---|---|---|---|
| 1 | `hide` | `omp://skills.md:144` "include the discovered skills list, excluding hidden skills"; `:151` "`hide: true` does not disable the skill. Hidden skills are still loaded and remain reachable through `skill://<name>` and `/skill:<name>` when skill commands are enabled." | documented; code at bundled `packages/coding-agent/src/system-prompt.ts` (byte 161658102, `pe.filter((e) => e.hide !== true)`) |
| 2 | `disableModelInvocation` | `omp://skills.md:59` "`disableModelInvocation?: boolean` (Agent Skills equivalent of `hide`; normalized from kebab-case `disable-model-invocation`)" | documented; code sets `hide` from it at bundled `src/extensibility/skills.ts` (byte 158594813); kebab normalization observed in probe (§3) |
| 3 | `enabled` | `omp://skills.md:61` "`enabled: false` skips a skill in conventional scanners and Skillshare discovery" | documented; code at bundled `src/discovery/helpers.ts` (byte 154025981) and `src/discovery/skillshare.ts` (byte 155142196) |
| 4 | `ignoredSkills` | `omp://skills.md:112` "`ignoredSkills` (exclude; glob patterns)"; `:135` "applied to both the raw and the final name, so a namespaced alias cannot bypass an exclusion" | documented; config key `skills.ignoredSkills` |
| 5 | `includeSkills` | `omp://skills.md:113` "`includeSkills` (include allowlist; glob patterns; empty means include all)"; `:135` "applied to the final listing only, after every name is resolved" | documented; config key `skills.includeSkills` |
| 6 | `disabledExtensions` | `omp://skills.md:111` "`disabledExtensions` entries with `skill:<name>`"; filter order `:117` "1. not disabled by `disabledExtensions`" | documented; config key `disabledExtensions` |
| 7 | source toggles | `omp://skills.md:110` "source toggles: `enableCodexUser`, `enableClaudeUser`, `enableClaudeProject`, `enablePiUser`, `enablePiProject`, `enableAgentsUser`, `enableAgentsProject`"; `:122` "Foreign user-level providers are opt-in through `enabledProviders`" | documented; config keys `skills.enable*`, `enabledProviders` |
| 8 | `skills.enabled` | `omp://skills.md:83` "If `skills.enabled` is `false`, discovery returns no skills." | documented; config key `skills.enabled` |
| 9 | `enableSkillCommands` | `omp://skills.md:157` "If `skills.enableSkillCommands` is true, interactive mode registers one slash command per discovered skill." | documented, but it governs the **user**-invocation path, not the model's candidate list — not a model-choice lever |
| 10 | `skillful` | settings-registry description "List available skills in the system prompt; disable to save context and toggle per-session with /skillful"; slash command "Toggle listing available skills in the system prompt (session only)" | **code-only** (absent from `omp://skills.md`, `omp://settings.md`, `omp://config-usage.md`); binary bytes 96162649 / 164561124 / 165052788 |
| 11 | `--skills` / `--no-skills` | `omp://cli-reference.md:159` "`--skills <globs>` \| Comma-separated glob patterns to filter [skills](./skills.md) (e.g. `git-*,docker`)."; `:160` "`--no-skills` \| Disable skills discovery and loading." | documented (CLI surface) |
| 12 | `<namespace>/<name>` | `omp://skills.md:130` "the higher-precedence skill keeps the bare name and every other variant receives a `<namespace>/<name>` suffix" | documented, but keyed on **name collision**, not on overlapping descriptions — a same-name lever, not an overlap lever |
| 13 | `globs` / `alwaysApply` (**negative**) | `omp://skills.md:63` "`globs` and `alwaysApply` are metadata here, not automatic skill-invocation controls." | documented negative: omp has **no** path-glob activation lever of the kind Claude Code documents |
| 14 | `readsSkillUris` | `omp://skills.md:143` "if an active tool declares `readsSkillUris: true`" → listing included; otherwise "omit the discovered list" | documented; tool capability, not a per-skill lever |

Levers 1–8 and 10–11 all satisfy the C2 shape ("a documented lever **other than description
wording** for stopping one of two overlapping skills from being chosen"): they remove or hide one
skill so the model never sees the pair, rather than describing one better.

## 3. Behaviour observed on this host (omp 18.12.6)

Probe tree (all under my scratch dir, nothing written to the lane):
`/fast/scratch/hyaku/kotoba-r51/build/LeverOmp/probe/proj/.omp/skills/{alpha,beta,gamma,delta}`.

- `alpha` (plain) → listed, `hide=false`; `beta` with `hide: true` → listed, `hide=true` →
  excluded from the prompt listing; `gamma` with `enabled: false` → **not listed at all** (skipped
  by discovery); `delta` with kebab-case `disable-model-invocation: true` → listed, `hide=true` →
  the doc's "normalized from kebab-case" claim holds in this build.
- Project `.omp/config.yml` `skills.ignoredSkills: [alpha]` → alpha gone (others kept);
  `skills.includeSkills: ["beta"]` → only beta kept; `disabledExtensions: ["skill:alpha"]` → alpha
  gone.

## 4. Draft entry paragraph (deliver as text; the L1 integrates it)

Place it **after** the `## Levers by client` table of
`corpus/knowledge/skill-overlap-levers-round51.md` (the verifier takes the *first* table after that
marker) and keep it out of that table, so the 7-client count is unchanged. The same text is at
`/fast/scratch/hyaku/kotoba-r51/build/LeverOmp/draft-omp-entry.md` as clean markdown.

> ### omp (the lane's harness — outside the seven-client counter)
>
> This entry is not one of the seven pinned clients and is not counted by `verifiers/check_overlap_levers.py`; it records what kotoba's own harness, omp 18.12.6 (`/home/vgpnk/.local/bin/omp`, sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`), documents and implements for the same question. Like the seven clients, omp states no rule that arbitrates between two differently named skills whose descriptions both match: the only selection rule it gives the model is description matching — "Use the read tool to load a skill's file when the task matches its description." (bundled skill prompt `/$bunfs/root/skill-6kx0z31r.md`, source `packages/coding-agent/src/prompts/internal-urls/skill.md`; code-only, not in the `omp://` doc tree) — and "Matching quality depends on `description` being meaningful." (`omp://skills.md:21`). What omp adds is a set of levers keyed on something other than the description, all of which remove one skill from the model's candidate set instead of ranking two: `hide: true` (or the Agent Skills spelling `disableModelInvocation`, normalized from kebab-case `disable-model-invocation`) keeps the skill loadable but out of the system-prompt listing, so a hidden overlapping skill cannot be picked while it stays reachable through `skill://<name>` and `/skill:<name>` (`omp://skills.md:59`, `:144`, `:151`); `enabled: false` skips the skill in discovery altogether (`omp://skills.md:61`); operator-side `skills.ignoredSkills` and `skills.includeSkills` glob lists, `disabledExtensions` entries of the form `skill:<name>`, and the `skills.enable*` source toggles drop skills by name or by source (`omp://skills.md:110-113`, `:117-120`); `skills.enabled: false` turns the subsystem off (`omp://skills.md:83`); the `skillful` setting and the `/skillful` command omit the listing from the prompt for a session (settings registry and slash-command table only — not in the `omp://` doc tree); and the CLI `--skills <globs>` / `--no-skills` flags filter discovery at launch (`omp://cli-reference.md:159-160`). Two documented negatives matter for kotoba: a skill's `globs` and `alwaysApply` are "metadata here, not automatic skill-invocation controls" (`omp://skills.md:63`), so omp has no path-glob activation lever of the kind Claude Code documents; and the listing template carries only name, description and location, with no precedence field for the model to weigh. Same-name collisions are settled by a documented precedence and a `<namespace>/<name>` suffix (`omp://skills.md:130`), which is a name lever, not an overlap lever.
## 5. Evidence (commands, exit codes, verbatim outcomes)

```
sha256sum /home/vgpnk/.local/bin/omp
  85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4   (exit 0)

/home/vgpnk/.local/bin/omp --version            -> "omp/18.12.6"                       (exit 0)
/home/vgpnk/.local/bin/omp --help | grep -n -E '\-\-skills|\-\-no-skills'
  53:      --no-skills                       Disable skills discovery and loading
  54:      --skills=<value>                  Comma-separated glob patterns to filter skills (e.g., git-*,docker)
  (exit 0)

find /home/vgpnk/.local/share /home/vgpnk/.omp -maxdepth 4 -iname '*skill*'   (exit 0)
  -> only unrelated skills (omarchy-skill, uv skills-ref, prime-agent/skills); no omp doc files
find /home/vgpnk/.local /home/vgpnk/.omp -maxdepth 6 -name 'skills.md'         (exit 0)
  -> no output: the omp doc tree ships INSIDE the 18.12.6 ELF (/$bunfs/root/*.md, read through
     the binary's own `omp read omp://<path>`), not as loose files on disk
/home/vgpnk/.local/bin/omp read omp://           -> "# Documentation", "134 files available:" (exit 0)
  includes skills.md, skills/authoring-*.md, cli-reference.md, config-usage.md, settings.md
/home/vgpnk/.local/bin/omp read omp://skills.md  -> 17971 bytes, 258 lines             (exit 0)
/home/vgpnk/.local/bin/omp read omp://cli-reference.md -> 298 lines                     (exit 0)
copies cached under /fast/scratch/hyaku/kotoba-r51/build/LeverOmp/ompdocs/ so the L1 can quote the
same bytes

/home/vgpnk/.local/bin/omp config list --json    -> 559 keys                          (exit 0)
  skill-related keys and values quoted in §2 (no secret values read; config.yml not modified)
/home/vgpnk/.local/bin/omp config get skills.enabled / skills.ignoredSkills /
  skills.includeSkills / skills.customDirectories / skillful
  -> true / [] / [] / [] / true                                                     (exit 0)

grep -n -i 'skill' /home/vgpnk/.omp/agent/config.yml   -> no match (exit 1)
  (the operator config carries no skills.* key; the levers above are unset defaults there)

probe (cwd = my scratch proj), all `omp skill list --json` runs exit 0:
  plain / hide:true / enabled:false / disable-model-invocation:true
    -> alpha hide=False; beta hide=True; gamma ABSENT; delta hide=True
  .omp/config.yml skills.ignoredSkills:[alpha]      -> native skills ['beta','delta']
  .omp/config.yml skills.includeSkills:["beta"]     -> native skills ['beta']
  .omp/config.yml disabledExtensions:["skill:alpha"] -> native skills ['beta','delta']

strings -n 12 <omp> | grep -i -E 'if more than one skill|when multiple skills|
  more than one skill matches|two skills match|skills match|unique skill name'
  -> no output                                                                (exit 1, no match)
```

## 6. Scope and limits

- **Out of the 7-client counter.** No SOURCES row is proposed for omp: the entry is the harness,
  not a pinned client; the counter's `CLIENTS` list is pinned in the script.
- **Read-only lane.** The lane checkout was modified only by this report file; no git or jj
  command was run against the lane, the fleet repo, or a sibling lane. All probes wrote only to my
  scratch dir.
- **The operator config was read, never edited.** No secret values were read or quoted; only key
  names and non-secret booleans/arrays are reported.
- **No tool was installed or upgraded** for this item (no pacman, uv, npm or cargo action); nothing
  to record in the tooling log.
- **Code locations are byte offsets in the 18.12.6 binary** plus the bundled source path from the
  bundle's own `// packages/coding-agent/src/...` comments; upstream source lines were unavailable
  offline.
- `omp://` docs were read through the installed binary's own read-only doc tree (the only route the
  assignment allows); the same bytes are cached in my scratch `ompdocs/` directory.
- **Known limit:** the `skillful` lever and the `hide`/`disableModelInvocation` prompt filter were
  verified in code and by `omp skill list` output, not by observing a live model turn; the model-side
  effect (the skill absent from the prompt listing) follows from the documented filter at
  `omp://skills.md:144` and the code at `src/system-prompt.ts`.

## 7. Artifacts

- `/fast/scratch/hyaku/kotoba-r51/build/LeverOmp/ompdocs/` — cached copies of the `omp://` docs I
  read (skills.md, cli-reference.md, config-usage.md, settings.md, system-prompt-customization.md,
  context-files.md, rulebook-matching-pipeline.md, task-agent-discovery.md, tools/manage_skill.md,
  magic-keywords.md, skills/authoring-*.md) plus `omp config list --json`.
- `/fast/scratch/hyaku/kotoba-r51/build/LeverOmp/probe/` — the four-skill probe tree and the
  project `.omp/config.yml` variants used in §3.
- `/fast/scratch/hyaku/kotoba-r51/build/LeverOmp/draft-omp-entry.md` — the §4 paragraph as clean
  markdown, ready to paste after the `## Levers by client` table of the C2 entry file.

Report: .ufo/waves/round-51/build/LeverOmp.md
