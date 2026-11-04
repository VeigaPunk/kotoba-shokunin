# RevengerPrecedence — round 86 w1 probe: same-name precedence in omp 18.15.0

Hypothesis H: "when the same skill name exists under two roots omp reads, omp 18.15.0 renders the copy from the root it scans first, and the fixture shows it."

## Verdict

**`other rule: provider-priority first-registration keeps the bare name; a later copy with a different body/frontmatter is NOT dropped but re-registered as "<namespace>/<name>" (name-collision warning); only same-realpath or byte-identical (body === and Bun.deepEquals(frontmatter)) copies are dropped; custom directories and non-skillshare copies displace an earlier copy (last-wins for those two classes)`.**

The fixture does **not** exercise the rule: the two roots that produce all 215 lines hold **0** common names, and the catalogue has **0** namespaced (`/`) names. "Scans first" is also the wrong frame: providers load concurrently (`Promise.all`); order is the provider priority list, not scan timing.

## Inputs (read-only)

- Fixture `verifiers/fixtures/omp-catalogue-r86/catalogue.json` sha256 `0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488` (matches plan pin), 215 entries, 228 cache rows (42 bare-key, 186 `:anthropic/claude-haiku-5-5`).
- ELF `/home/vgpnk/.local/bin/omp` (omp/18.15.0), read with python mmap + re; offsets are byte offsets into the ELF; every quote below occurs exactly once in the file.
- Lane `preview`, `parse_frontmatter`, `omp_key` imported from `verifiers/verify_harness_claims.py` (base, unmodified). Template = fixture `template_hex`.
- Host census: `find /home/vgpnk /etc /usr/share /usr/lib/node_modules -xdev` (prune .git/.cache/sessions/Trash//fast) → 6144 `SKILL.md`; plus direct listing of the two read roots following symlinks.

## Which roots produce the 215 lines

| root | provider (priority) | names | render predicted exactly |
|---|---|---|---|
| `~/.omp/plugins/node_modules/ecc-pi-core/skills` (symlink → `~/.ecc/pi/core/skills`) | omp-plugins (90) [INFERENCE: installed-plugin root via `XQ`→`AP`; `uie` scans `<plugin>/skills`] | 132 | 132/132 |
| `~/.agents/skills` (5 symlinks: omarchy, shokunin, swarm, tower, ufo) | agents user (70) | 83 | 83/83 |

Prediction = bare-key cache row `sha256(template‖0‖name‖0‖description)` if present (35 names), else `preview(description)` (180 names): **215/215 equal the fixture render**. Union = exactly the 215 fixture names, 0 extra, **0 names in both roots**. The 132 R1 names are exactly the base receipt's 132 `not-discovered`; the 83 R2 names are the base's 83 reproduced.

Project walk-up roots (`/home/vgpnk/Projects/shokunin` = git toplevel = repoRoot, so the walk is cwd only): no `.omp/skills`, `.agents/skills`, `.agent/skills`, `.claude/skills`, `.codex/skills`, `.opencode/skills`, `.github/skills` exist. `~/.omp/agent/skills` absent. `config.yml` sets no `skills.*`, `enabledProviders` or `disabledProviders` key → defaults apply (`enableClaudeUser=false`, `enableCodexUser=false`, claude-plugins/opencode/codex/github… opt-out user sources off, `CLAUDE_CONFIG_DIR` unset).

## Evidence table — names with ≥2 distinct-realpath host copies whose descriptions differ

132 fixture names qualify (all host dirs, not only read roots). In **every** case the rendered line matches the copy in the read root (R1/R2). For 102 names the read copy is the *only* copy whose prediction equals the render (discriminating); for 30 a differing copy predicts the same line (description differs only past the 100-char cliff or in whitespace), so those rows cannot discriminate.

Columns: rendered-copy root, how the render is predicted, differing copies, of which also predict the render, where the differing copies live.

| name | rendered copy | via | differing copies | also match | differing copies by location |
|---|---|---|---|---|---|
| `2d-pixel-perfect` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `accessibility` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `agent-architecture-audit` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `agent-eval` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `agent-harness-construction` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `agent-introspection-debugging` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `agentic-engineering` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `agents` | R2 | preview | 4 | 2 | ~/.codex/plugins ×2; ~/.config/OpenBot ×1; ~/.cursor ×1 |
| `ai-first-engineering` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `android-clean-architecture` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `angular-developer` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `api-connector-builder` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `api-design` | R1 | preview | 15 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `architecture-decision-records` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `audio-setup-mixers` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `backend-patterns` | R1 | preview | 21 | 9 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `benchmark` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `blueprint` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `bun-runtime` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `click-path-audit` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `clickhouse-io` | R1 | preview | 12 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `code-tour` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `codebase-onboarding` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `coding-standards` | R1 | cache | 21 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `compose-multiplatform-patterns` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `computer-use` | R2 | preview | 8 | 0 | ~/.config/OpenBot ×4; ~/.hermes ×2; ~/.zcode ×2 |
| `content-hash-cache-pattern` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `cost-aware-llm-pipeline` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `cpp-coding-standards` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `cpp-testing` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `csharp-testing` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `dart-flutter-patterns` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `dashboard-builder` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `database-migrations` | R1 | preview | 15 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `deployment-patterns` | R1 | preview | 15 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `design-system` | R1 | preview | 7 | 0 | ~/.config/OpenBot ×1; ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `django-celery` | R1 | cache | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `django-patterns` | R1 | preview | 15 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `django-security` | R1 | preview | 9 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `django-tdd` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `django-verification` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `docker-patterns` | R1 | cache | 15 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `dotnet-patterns` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `e2e-testing` | R1 | preview | 15 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `error-handling` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `fastapi-patterns` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `flutter-dart-code-review` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `foundation-models-on-device` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `frontend-patterns` | R1 | preview | 21 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `fsharp-testing` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `git-workflow` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `godspeed` | R2 | cache | 14 | 0 | ~/.prime ×1; ~/.zcode ×3; ~/Projects/* (off walk-up) ×10 |
| `golang-patterns` | R1 | preview | 21 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `golang-testing` | R1 | cache | 21 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `hexagonal-architecture` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `initialize-ai-navigation` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `java-coding-standards` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `jpa-patterns` | R1 | preview | 15 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `kotlin-coroutines-flows` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `kotlin-exposed-patterns` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `kotlin-ktor-patterns` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `kotlin-patterns` | R1 | preview | 15 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `kotlin-testing` | R1 | preview | 15 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `laravel-patterns` | R1 | preview | 12 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `laravel-security` | R1 | preview | 12 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `laravel-tdd` | R1 | preview | 12 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `laravel-verification` | R1 | preview | 12 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `liquid-glass-design` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `localization` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `make-interfaces-feel-better` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `manage-sprite-atlas` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `mcp-server-patterns` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `migrate-birp-to-urp` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `mle-workflow` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `motion-advanced` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `motion-foundations` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `motion-patterns` | R1 | cache | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `mysql-patterns` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `nestjs-patterns` | R1 | cache | 9 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `new-unity-project` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `nextjs-turbopack` | R1 | preview | 21 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `nuxt4-patterns` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `optimize-audio` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `optimize-text-mesh-pro` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `optimize-web` | R2 | preview | 3 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1; ~/.grok ×1 |
| `parallel-execution-optimizer` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `perl-patterns` | R1 | cache | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `perl-security` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `perl-testing` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `physics-3d-collision` | R2 | cache | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `postgres-patterns` | R1 | preview | 21 | 9 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×7; ~/.zcode ×14 |
| `product-capability` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `product-lens` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `production-audit` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `python-patterns` | R1 | preview | 15 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `python-testing` | R1 | cache | 15 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `pytorch-patterns` | R1 | cache | 9 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `quarkus-patterns` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `quarkus-security` | R1 | preview | 9 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `quarkus-tdd` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `quarkus-verification` | R1 | preview | 9 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `redis-patterns` | R1 | preview | 3 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×1; ~/.zcode ×2 |
| `regex-vs-llm-structured-text` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `reverse-engineer-anything` | R2 | cache | 2 | 0 | /home/vgpnk/.lane-work/rea-backup/plugin-official-6.4.0/skills ×1; /home/vgpnk/.local/share/rea/.agents/skills ×1 |
| `rust-patterns` | R1 | preview | 15 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `rust-testing` | R1 | preview | 15 | 6 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `security-review` | R1 | cache | 18 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×6; ~/.zcode ×12 |
| `setup-api-key` | R2 | cache | 2 | 0 | ~/.codex/plugins ×1; ~/.cursor ×1 |
| `shader-graph-create-custom-node` | R2 | preview | 2 | 2 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `shokunin` | R2 | cache | 8 | 0 | ~/.kimi-code ×1; ~/.prime ×1; ~/.zcode ×1; ~/Projects/* (off walk-up) ×5 |
| `springboot-patterns` | R1 | preview | 15 | 9 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `springboot-security` | R1 | preview | 15 | 9 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×5; ~/.zcode ×10 |
| `springboot-tdd` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `springboot-verification` | R1 | preview | 12 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×4; ~/.zcode ×8 |
| `sprite-editor` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `swarm` | R2 | cache | 4 | 1 | ~/.cursor ×1; ~/.grok ×1; ~/Projects/* (off walk-up) ×2 |
| `swift-actor-persistence` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `swift-concurrency-6-2` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `swift-protocol-di-testing` | R1 | preview | 9 | 3 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×3; ~/.zcode ×6 |
| `swiftui-patterns` | R1 | preview | 6 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×2; ~/.zcode ×4 |
| `tdd-workflow` | R1 | preview | 24 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×8; ~/.zcode ×16 |
| `text-to-speech` | R2 | preview | 2 | 2 | ~/.codex/plugins ×1; ~/.cursor ×1 |
| `tower` | R2 | cache | 2 | 0 | ~/Projects/* (off walk-up) ×2 |
| `ufo` | R2 | cache | 17 | 0 | ~/.prime ×1; ~/Projects/* (off walk-up) ×16 |
| `ui` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `ui-ugui` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `ui-uitk` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `unity-cli` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `unity-package-management` | R2 | preview | 3 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1; ~/.grok ×1 |
| `unreal-mcp` | R2 | preview | 1 | 0 | ~/.hermes ×1 |
| `urp-postprocessing` | R2 | preview | 2 | 0 | ~/.claude/plugins/cache (claude-plugins, opt-out) ×1; ~/.config/OpenBot ×1 |
| `verification-loop` | R1 | preview | 24 | 0 | ~/.ecc (not a read root; R1 realpath target is ~/.ecc/pi/core/skills) ×8; ~/.zcode ×16 |

Nearest real test of H: 19 names also have a **differing** copy under `~/.claude/plugins/cache/…` (claude-plugins, priority 70, registered *before* agents at equal priority 70 — byte order 173861810 < 173866263). Were that provider enabled, the source rule gives the bare name to the claude-plugins copy and renders the `~/.agents` copy as `agents/<name>`. Observed: 18/19 render the `~/.agents` copy (the 19th, `shader-graph-create-custom-node`, is non-discriminating) and no `agents/…` line exists → claude-plugins is not read (opt-out default), consistent with enablement, not with an ordering test.

## Source: the code that decides (omp 18.15.0 ELF)

| what | offset | quote |
|---|---|---|
| capability/index.ts Fe: provider insert by descending priority | 172,771,631 | `const s = r.findIndex((o) => o.priority < t.priority);` |
| capability/index.ts Be: providers loaded concurrently, results kept in provider order | 172,771,981 | `const S = await Promise.all(t.map(async (g) => {` |
| capability/index.ts Be: first key wins, later marked shadowed | 172,773,835 | `const v = c.has(x);⏎    c.add(x);` |
| capability/index.ts Be: shadow flag | 172,773,969 | `g._shadowed = true;⏎    } else {⏎      p.push(g);` |
| capability/skill.ts: dedupe key is the skill name | 173,700,262 | `key: (u) => u.name,⏎  toExtensionId: (u) => `skill:${u.name}`` |
| extensibility/skills.ts Dp: consumes .all (shadowed items included), not .items | 177,500,886 | `const ke = he.all.filter((et) => {` |
| extensibility/skills.ts Dp: same realpath skipped | 177,502,514 | `if (ye.has(vt)) {⏎      continue;⏎    }⏎    const pt = {` |
| extensibility/skills.ts u0e: identical body+frontmatter copies dropped | 177,496,938 | `he.body === R && Bun.deepEquals(he.frontmatter, k)` |
| extensibility/skills.ts u0e: installed/custom displacement branch | 177,497,011 | `if (U && (X && !z \|\| Y && !Q)) {` |
| extensibility/skills.ts u0e: later differing copy renamed, kept | 177,497,979 | `warning: `name collision: "${x.name}" from ${x.filePath} differs from ${oe}; available as "${re}"`` |
| extensibility/skills.ts u0e: namespace suffix | 177,497,593 | `let re = `${_}/${x.name}`;` |
| extensibility/skills.ts Dp: final catalogue sort by name | 177,505,946 | `Et.sort((et, Ye) => dne(et.name, et.filePath, Ye.name, Ye.filePath));` |
| discovery/helpers Ba: one level, per-dir sort by name | 172,791,803 | `n.sort((S, c) => dne(S.name, S.path, c.name, c.path));` |
| discovery/builtin.ts native priority | 173,814,367 | `var Ko = 100;` |
| discovery/skillshare.ts priority | 173,926,209 | `var Aie = 95;` |
| discovery/omp-plugins.ts priority | 173,914,660 | `var wd = 90;` |
| discovery/claude.ts priority | 173,837,613 | `var cl = 80;` |
| discovery/agent-plugins.ts priority | 173,777,287 | `var uD = 75;` |
| discovery/claude-plugins.ts priority | 173,849,304 | `var ju = 70;` |
| discovery/agents.ts priority | 173,864,213 | `var Vu = 70;` |
| discovery/codex.ts priority | 173,879,063 | `var _a = 70;` |
| discovery/opencode.ts priority | 173,898,454 | `var ep = 55;` |
| discovery/github.ts priority | 173,906,379 | `var fh = 30;` |
| discovery/builtin.ts omp-managed priority (separate last pass) | 173,820,386 | `var P7 = 5;` |
| discovery/agents.ts walk-up/user subdirs | 173,864,226 | `var y1 = [".agent", ".agents"];` |
| settings.ts enableClaudeUser default | 172,765,302 | `var Fye = h({ id: "skills.enableClaudeUser", type: "boolean", default: false });` |
| settings.ts enableCodexUser default | 172,765,222 | `var Dye = h({ id: "skills.enableCodexUser", type: "boolean", default: false });` |
| capability/index.ts opt-out user providers | 172,770,804 | `"claude-plugins": true,` |

Reconstructed contract (skills, default settings):
1. `Fe` registers each provider into the capability's list before the first provider of strictly lower priority → list sorted by descending priority, ties in registration order. Skills providers: native 100 > skillshare 95 > omp-plugins 90 > claude 80 > agent-plugins 75 > claude-plugins 70 = agents 70 = codex 70 > opencode 55 > github 30; omp-managed 5 is filtered out and merged in a last pass only for names nobody else provides.
2. `Be` loads all providers concurrently and concatenates results in that list order; each `Ba` scan reads one directory level and sorts by name (`dne`). `Be` marks later same-`name` items `_shadowed` (first wins) — but `Dp` (loadSkills) iterates `he.all`, which includes shadowed items, so the capability-level first-wins is **not** what decides the catalogue.
3. `Dp` drops an item whose realpath was already accepted, filters by provider/level enablement (`ue`: claude user / codex user off by default; agents/native on), then `u0e` resolves a name collision: identical body + frontmatter → dropped; existing installed (skillshare) vs new non-installed, or new custom vs existing non-custom → the new copy takes the bare name and the old one moves to `<namespace>/<rawName>`; otherwise the new (later) copy becomes `<namespace>/<name>` (`~2`, `~3` … on repeat) with warning `name collision: "<name>" from <path> differs from <first path>; available as "<ns>/<name>"`. Namespace `q5` = plugin name, else the path component before `skills` (a leading-dot component falls back to the provider id).
4. Custom directories (`skills.customDirectories`, default `[]`) are merged after every provider with the same `Le`/`u0e`, so they displace provider copies.
5. The final list is sorted by `dne` (case-insensitive name, then name, then path); the fixture is name-sorted (checked).

## Divergences from the lane model (for ExecModel / reviewer; not patched)

- `discover_skills` docstring "First root wins per name (omp resolves duplicates by root order)" + `offered.setdefault(...)` drops later differing copies; omp keeps them as `<ns>/<name>` lines. Harmless on this fixture (0 overlaps in read roots) but a wrong model of omp.
- `USER_ROOTS` order (`.agents`, `.omp/agent`, opencode, claude) is not omp's priority order (native `.omp` 100 before agents 70; opencode/claude user are opt-out/off by default).
- `preview` cut: omp `dnt` keeps the word cut only when the last space index `o >= 40` (`const c = o >= E ? r.slice(0, o).trimEnd() : r;`), else cuts at 99 chars; the lane uses `s[:s.rfind(" ")]` with no floor. No fixture line hits the difference (215/215 predicted).
- The agents provider passes no `requireDescription` (native/github/omp-plugins/custom pass `true`); `Ba` also skips `enabled: false` frontmatter and reads frontmatter `name` before the dir name. Not exercised here.

## Confidence

- Source rule: high (quotes unique, read from the shipping ELF; logic read, not executed). Tie order among the three priority-70 providers rests on module evaluation = bundle byte order [INFERENCE].
- "Fixture does not show precedence": high (exhaustive: 215/215 lines from two disjoint roots).
- R1 attributed to omp-plugins (90) rather than agent-plugins (75): medium [INFERENCE]; irrelevant to the verdict since R1 and R2 share no name.

## Method notes

- No omp session or model call was run (revenger bound). `omp --help` and `omp skill --help` were run once each inside a read-only bwrap (`--ro-bind / /`) to confirm no skill-listing command exists (`omp skill list` is registry installs).
- Scratch `/fast/scratch/hyaku/kotoba-r86/RevengerPrecedence/` removed before yield. No lane/fleet VCS write; ExecModel `CANDIDATE_READY` absent at write time (not needed: this probe is on the base model and the fixture).
