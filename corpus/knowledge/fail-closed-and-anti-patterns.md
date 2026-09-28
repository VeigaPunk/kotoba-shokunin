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
