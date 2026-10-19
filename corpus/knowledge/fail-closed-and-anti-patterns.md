# Fail-closed prerequisites & anti-patterns

Sourced 2026-09-28.

## Fact — the fail-closed gate sentence has a stable shape

- bailian-cli / bailian-gen / bailian-finetune: `If that protocol file is
  missing, stop and run \`bl skill init\`; do not guess auth/consent.` —
  `~/.agents/skills/bailian-cli/SKILL.md` L23 (CRITICAL block).
- ufo: `If none can be read, fail closed — do not synthesize a replacement.` —
  `~/.config/opencode/skills/ufo/SKILL.md` load-order step 1.
- sekhmet-l3: `Never symlink titanium as codex` + resolve order with explicit
  skip rule — `~/.agents/skills/sekhmet-l3/SKILL.md` Host resolve.

Shape: `if <prereq> missing → <named recovery> ; do not <tempting shortcut>`.
A gate without the shortcut prohibition is only half a gate.

## Fact — failure knowledge earns lines only with a signature

bailian-train-deploy 反幻觉清单 carries observed signatures, not warnings:

- zsh `status` readonly-variable trap → `read-only variable` + exit 1 (L120).
- Deploy 404 `Model not exist` on fresh RUNNING = propagation delay, retry ~1
  min (L169).
- `--learning-rate` must be string `"3e-4"`, not number — JSON precision (L65).
- `--model-name` (deploy create) vs `--model` (inference) are different
  namespaces; reusing the finetune output name 404s (L157).

Contrast (opinion): "be careful with X" without the observed error text teaches
the agent nothing it can pattern-match at runtime.

## Fact — soft hand-off by name beats hard path deps

bailian-protocol L53–70: business skills route to siblings **by name** —
"已安装则 Read 其 SKILL.md，未安装则用 `bl <cmd> --help`，或提示整包安装".
Only the shared protocol gets a hard relative path (`../bailian-protocol/…`)
because it ships in the same `bl skill init` package. Hardcoding
`../sibling/SKILL.md` as an execution prerequisite = dead skill when the
sibling isn't installed.

## Fact — flag truth lives at the CLI, not in prose

Every bailian skill repeats: `Flags, usage, and examples: see reference/ or
bl <command> --help — do not guess flags.` Stale-risk facts (flags, model
names, prices) are deferred to generated reference trees or `--help`; the
skill body keeps only stable semantics.

## Anti-pattern table (distilled)

| Smell | Observed consequence | Counter-pattern source |
|-------|---------------------|------------------------|
| Anti-trigger in body only | false activation (router reads description only) | bailian-* frontmatter 反触发 |
| Flags in prose | drift vs `--help`; agents guess | bailian-cli "do not guess flags" |
| Gate without shortcut prohibition | agent guesses auth/consent | bailian-cli L23 |
| Warning without signature | no runtime pattern-match | bailian-train-deploy 反幻觉清单 |
| `../sibling/` hard dep | dead skill on partial install | bailian-protocol L53–70 |

## Anti-pattern table (full, moved from `SKILL.md`, round 15)

The 20-row table as it stood in `SKILL.md` before the round-15 line-budget move.
The distilled 5-row table above is a subset of this one — where they differ, this
is authoritative. `SKILL.md` § Anti-patterns keeps the five highest-frequency
rows plus this pointer.

| Smell | Why it fails | Fix |
|-------|--------------|-----|
| Description = capability only, no triggers | Router can't match unseen phrasings — the shonen mint template produces exactly this (`Domain specialist — scopes X`); 5/5 sibling SKILL.md files failed items 2–3 in the round-5 fleet audit | Add quoted trigger strings + implicit intents |
| Anti-trigger only in body | The offer stage never sees it (frontmatter-only catalogue); false activation | Move exclusion clause into `description` |
| Flags documented in prose | Drifts from `--help`; agents guess | Pointer to `reference/` or `--help` |
| Procedures before scope | Agent acts before knowing boundaries | Anatomy order: gate → decide → act |
| Warning without signature | "Be careful" teaches nothing | Attach observed error text / version / exit code |
| Sibling skill hardcoded as path dep | Missing sibling = dead skill | Soft hand-off by name + `--help` fallback (bailian family rule) |
| Recursive skill load | Skill that must read itself to work | In-line the essential rule; reference the rest |
| 600+ line monolith | Router and agent both lose the thread | Split at anatomy boundary 3↔4 |
| Procedures in AGENTS.md | Always-loaded bytes pay every session; procedures belong in opt-in files | Move how-to to SKILL.md; keep only constraints |
| Dispatch prompt missing a stanza | Blank-context subagent fails unrecoverably | Role → context → job → routing → report → `| godspeed` |
| Copy-pasted posture block in durable files | One drifts silently — 13 copies observed, one file already carries it twice | Centralize: `agent:`/`agents_md:` frontmatter flags or a shared include |
| Per-task job text in an agent-definition body | Body loads for every delegation; the job goes stale while the identity persists | Identity + constraints in body; the job lives in the dispatch prompt |
| Dated operational note in frontmatter | No freshness mechanism — `cascade_note` past its `until` date still routes | Move dated facts to a status file; frontmatter holds stable policy |
| Command file that re-states skill procedures | Two owners of the same steps; the skill drifts, command contradicts | Pointer-then-rules: name the skill, keep only rules that must hold anyway |
| Spawn-mode prompt used for a round ignite | 6-stanza completeness when the reader re-loads its own repo is pure drag | 3–4 lines: role+round, method, land-scope, `| godspeed` |
| Bin invoked without declared location | `command -v` returns nothing; agent guesses a path (kake: `webzites` on no PATH) | Declare the bin path or a prerequisite check step |
| Trigger list past the omp 99-char cliff | omp's render is `cache.get(key) ?? slice(0,99)`+`…`: all 13 observed `Triggers:`/反触发/`Excludes` clauses sit past the cut and never reach the router when the cache misses (85.5% of quoted trigger spans lost); the cliff is omp-only — opencode's system-prompt catalogue renders the full description | Capability + WHEN-hint inside the first ≤99 chars; the rest is body material on omp; on opencode nothing is cut, so trigger order is not survival-critical |
| Trigger list in sentence 2 (omp) | omp's ≥40-char first-sentence branch renders sentence 1 verbatim and drops everything after — godspeed loses its own trigger list this way; opencode renders every sentence | Put trigger material inside sentence 1, or keep the description to one sentence |
| CJK description with incidental ASCII spaces (omp) | omp's sentence regex knows only `[.!?]`; CJK text cuts at an incidental space mid-clause (549→44 chars observed) | CJK skills must front-load harder; expect sub-90-char keeps |
| Copy-pasted round prompt restating durable policy | The routing map in a round prompt drifts with every bucket change — 38 files carry `m_composer`/`m_antigravity`/`m_grok` aliases retired by MISSION.md | Round prompt carries delta only; durable policy lives where the lane re-reads it (MISSION.md) |
