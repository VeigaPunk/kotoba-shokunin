# ScoutRootsSource — omp 18.15.0 skill roots, located in the ELF

ELF: `/home/vgpnk/.local/bin/omp`, `omp/18.15.0`, sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` (equals the plan pin).
Method: python3 mmap of the ELF; module bounds = consecutive `b"// packages/…ts\n"` headers (2684 found); entry point
`async function Dp(` in `packages/coding-agent/src/extensibility/skills.ts` (export alias `Dp as loadSkills`, `uFe as loadSkillsFromDir`,
`_ge as rediscoverSkills`); providers found by `re.finditer(rb"Fe\(zl\.id", M)` (`zl` = capability `id: "skills"`): 11 registrations
in 10 modules. Each quote below was located by `M.find(quote, module_start, module_end)`; the offset is the first hit inside that module;
"ELF count" = occurrences in the whole file. In cells, `\|` stands for a literal `|` (Markdown escape); the ELF bytes have a bare `|`.
`″` = same as the row above. Rows are statements; several rows per root class.

| root class | path expression | gate setting + default | layout | precedence | offset | quote |
|---|---|---|---|---|---|---|
| native project (.omp) | `<d>/.omp/skills` for each d from {cwd} up to git root (inclusive), else up to home (exclusive) | `skills.enablePiProject`, default **true** | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description required | provider `native` priority 100 (highest); project dirs listed before user dir | 173819979 (`discovery/builtin.ts`; ELF count 1) | `dir: fr.join(k, Ou.projectDir, "skills"),` |
| ″ | ″ | ″ | ″ | ″ | 172765562 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enablePiProject", type: "boolean", default: true` |
| ″ | walk: X4t stops (exclusive) at home, os.tmpdir, /tmp, /var/tmp; stops (inclusive) at repoRoot | ″ | ″ | ″ | 173815038 (`discovery/builtin.ts`; ELF count 1) | `if (R.has(U))` |
| ″ | walk end = repoRoot ?? home | ″ | ″ | ″ | 173815282 (`discovery/builtin.ts`; ELF count 1) | `for (const x of X4t(u.cwd, u.repoRoot ?? u.home)) {` |
| ″ | skips d == home and any d whose `.omp` is ~/.omp or the plugins-dir parent | ″ | ″ | ″ | 173815338 (`discovery/builtin.ts`; ELF count 1) | `if (Mt(x.dir) === p \|\| une(x.dir))` |
| ″ | with no git root, skips d having its own `.omp/agent` (≠ agentDir) | ″ | ″ | ″ | 173815393 (`discovery/builtin.ts`; ELF count 1) | `if (!u.repoRoot && await Xye(x.dir, Ou.projectDir))` |
| ″ | repoRoot = nearest ancestor of cwd holding a `.git` entry | ″ | ″ | ″ | 172762094 (`capability/fs.ts`; ELF count 1) | `if (n.some((s) => s.name === ".git")) {` |
| ″ | ″ (computed once per discovery) | ″ | ″ | ″ | 172774946 (`capability/index.ts`; ELF count 1) | `const o = await one(r);` |
| ″ | ″ | gate applied in Dp `ue()` | ″ | ″ | 177500009 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "native" && vt === "project")` |
| native user (.omp agent) | `<agentDir>/skills` = `~/.omp/agent/skills` (`PI_CONFIG_DIR` replaces `.omp`; profile → `~/.omp/profiles/<p>/agent`) | `skills.enablePiUser`, default **true** | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description required | priority 100; after native project dirs | 173820135 (`discovery/builtin.ts`; ELF count 1) | `dir: fr.join(we(), "skills"),` |
| ″ | ″ | ″ | ″ | ″ | 172765486 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enablePiUser", type: "boolean", default: true` |
| ″ | agentDir = `<configRoot>/agent` | ″ | ″ | ″ | 166888442 (`dirs.ts`; ELF count 1) | `const a = h.join(this.configRoot, "agent");` |
| ″ | config dir name | ″ | ″ | ″ | 166884553 (`dirs.ts`; ELF count 1) | `var Gh = ".omp";` |
| ″ | ″ | gate in Dp `ue()` | ″ | ″ | 177499951 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "native" && vt === "user")` |
| ″ | provider description string | ″ | ″ | ″ | 173814318 (`discovery/builtin.ts`; ELF count 2) | `Native OMP configuration from ~/.omp and .omp/` |
| ″ | ″ | ″ | ″ | priority constant | 173814367 (`discovery/builtin.ts`; ELF count 1) | `var Ko = 100;` |
| skillshare (registry installs) | lock `<d>/.omp/skills.lock.json` (same walk as native project) and `~/.omp/agent/skills.lock.json`; skill files in `~/.omp/skillshare/@<scope>/<name>/<version>` | no skills.* gate (provider `skillshare`; removable via `disabledProviders`) | lock-driven, not a directory scan | priority 95, but **loses names**: a later non-skillshare skill of the same name takes the bare name, the skillshare one becomes `<ns>/<name>` | 173927698 (`discovery/skillshare.ts`; ELF count 1) | `x.push(iF(ab.join(_, ZO.native.projectDir, sb), "project", p));` |
| ″ | ″ | ″ | ″ | ″ | 173927768 (`discovery/skillshare.ts`; ELF count 1) | `const R = iF(ab.join(we(), sb), "user", p);` |
| ″ | lock file name | ″ | ″ | ″ | 173922748 (`skillshare/manifest.ts`; ELF count 1) | `var sb = "skills.lock.json";` |
| ″ | store dir | ″ | ″ | ″ | 173923748 (`skillshare/manifest.ts`; ELF count 1) | `return Ys.join(Ys.dirname(we()), "skillshare");` |
| ″ | ″ | ″ | ″ | displacement warning | 177497485 (`extensibility/skills.ts`; ELF count 1) | `is overridden by ${x.filePath}; available as "${he}"` |
| ″ | ″ | ″ | ″ | priority constant | 173926209 (`discovery/skillshare.ts`; ELF count 1) | `var Aie = 95;` |
| ″ | provider description | ″ | ″ | ″ | 173927967 (`discovery/skillshare.ts`; ELF count 2) | `Registry skills installed with `omp skill install` (skills.lock.json)` |
| omp-plugins (extension packages) | `<pkg>/skills` for each extension root: `extensions:` entries (project `.omp/config.yml`/`settings.json`, else `~/.omp/agent/config.yml`/`settings.json`) + installed npm plugins `~/.omp/plugins/node_modules/<name>` (and project `<root>/.omp/plugins/node_modules/<name>`) | provider `omp-plugins` not opt-in → on unless `disabledProviders`; plugin skipped if lock `enabled: false` | fixed `<pkg>/skills/<name>/SKILL.md` (manifest `skills` key not consulted here); description required; root dropped if it has an invalid `plugin.json`, routed to agent-plugins if a valid one | priority 90 | 173914936 (`discovery/omp-plugins.ts`; ELF count 1) | `dir: Zo.join(R.path, "skills"),` |
| ″ | root enumeration | ″ | ″ | ″ | 173914701 (`discovery/omp-plugins.ts`; ELF count 1) | `const x = await X9(u);` |
| ″ | merge mode default | ″ | ″ | ″ | 173772524 (`discovery/omp-extension-roots.ts`; ELF count 1) | `var bC = "merge";` |
| ″ | `extensions` key read from config.yml | ″ | ″ | ″ | 173774163 (`discovery/omp-extension-roots.ts`; ELF count 1) | `const _ = "extensions" in k ? k.extensions : undefined;` |
| ″ | installed npm plugin roots added | ″ | ″ | ″ | 173776587 (`discovery/omp-extension-roots.ts`; ELF count 1) | `AP(u.cwd, { home: u.home }),` |
| ″ | npm plugin roots already listed by the Claude/omp registries are excluded | ″ | ″ | ″ | 173776865 (`discovery/omp-extension-roots.ts`; ELF count 1) | `return k.filter((_) => !R.has(_.realpath)).map(({ path: _, scope: F }) => ({ path: _, level: F }));` |
| ″ | plugins dir `<home>/.omp/plugins` | ″ | ″ | ″ | 166892383 (`dirs.ts`; ELF count 1) | `return h.join(p, qh(), "plugins");` |
| ″ | plugin root scan reads `node_modules` | ″ | ″ | ″ | 173767148 (`extensibility/plugins/loader.ts`; ELF count 1) | `const R = yo.join(u, "node_modules");` |
| ″ | members = package.json deps ∪ omp-plugins.lock.json keys | ″ | ″ | ″ | 173767575 (`extensibility/plugins/loader.ts`; ELF count 1) | `const U = yo.join(u, "omp-plugins.lock.json");` |
| ″ | lock-only entries kept only if `node_modules/<name>` is a symlink | ″ | ″ | ″ | 173768289 (`extensibility/plugins/loader.ts`; ELF count 2) | `plugins: skipping stale lockfile entry not declared in package.json` |
| ″ | package must carry an `omp` or `pi` field | ″ | ″ | ″ | 173768743 (`extensibility/plugins/loader.ts`; ELF count 1) | `const ue = oe.omp \|\| oe.pi;` |
| ″ | ″ | lock `enabled: false` → skipped | ″ | ″ | 173768871 (`extensibility/plugins/loader.ts`; ELF count 1) | `if (he && !he.enabled) {` |
| ″ | user root | ″ | ″ | ″ | 173769583 (`extensibility/plugins/loader.ts`; ELF count 1) | `const k = await eD(R, x, "user");` |
| ″ | ″ | ″ | ″ | priority constant | 173914660 (`discovery/omp-plugins.ts`; ELF count 1) | `var wd = 90;` |
| ″ | provider description | ″ | ″ | ″ | 173914558 (`discovery/omp-plugins.ts`; ELF count 2) | `Sub-discovery (skills, hooks, tools, commands, rules, prompts, .mcp.json) inside extension packages` |
| claude project (.claude) | `<d>/.claude/skills` for each d from {cwd} up to repoRoot ?? home (inclusive), skipping d == home | `skills.enableClaudeProject`, default **true** | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description **not** required | provider `claude` priority 80 | 173840364 (`discovery/claude.ts`; ELF count 1) | `dir: Fr.join(k, eh, "skills"),` |
| ″ | walk end | ″ | ″ | ″ | 173840465 (`discovery/claude.ts`; ELF count 1) | `if (k === (u.repoRoot ?? u.home))` |
| ″ | ″ | ″ | ″ | ″ | 172765399 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enableClaudeProject",` |
| ″ | ″ | gate in Dp `ue()` | ″ | ″ | 177499890 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "claude" && vt === "project")` |
| ″ | ″ | default in Dp | ″ | ″ | 177499273 (`extensibility/skills.ts`; ELF count 1) | `enableClaudeProject: _ = true,` |
| ″ | provider description | ″ | ″ | ″ | 173847159 (`discovery/claude.ts`; ELF count 2) | `Load skills from .claude/skills/*/SKILL.md` |
| ″ | ″ | ″ | ″ | priority constant | 173837613 (`discovery/claude.ts`; ELF count 1) | `var cl = 80;` |
| claude user | `<claudeConfigDir>/skills` = `$CLAUDE_CONFIG_DIR/skills` else `~/.claude/skills` | `skills.enableClaudeUser`, default **false**; also on if `enabledProviders` ∋ claude/`*`/`all` or `CLAUDE_CONFIG_DIR` set | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description not required | priority 80 | 173840218 (`discovery/claude.ts`; ELF count 1) | `const x = p ? Fr.join(p, "skills") : null;` |
| ″ | ″ | setting passed as force flag | ″ | ″ | 173840190 (`discovery/claude.ts`; ELF count 1) | `const p = dl(u, f1(Fye));` |
| ″ | ″ | otherwise gated by opt-in check | ″ | ″ | 173837767 (`discovery/claude.ts`; ELF count 1) | `if (!p && !zi("claude", u))` |
| ″ | ″ | ″ | ″ | ″ | 172765316 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enableClaudeUser", type: "boolean", default: false` |
| ″ | ″ | Dp gate | ″ | ″ | 177499816 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "claude" && vt === "user")` |
| ″ | ″ | Dp gate: setting OR zi(claude) | ″ | ″ | 177499860 (`extensibility/skills.ts`; ELF count 1) | `return k \|\| zi("claude");` |
| ″ | config dir resolution | ″ | ″ | ″ | 170545369 (`config/claude-paths.ts`; ELF count 1) | `const r = process.env.CLAUDE_CONFIG_DIR?.trim();` |
| ″ | ″ | ″ | ″ | ″ | 170545531 (`config/claude-paths.ts`; ELF count 1) | `return { configDir: i.join(o, ".claude"), configFile: i.join(o, ".claude.json") };` |
| ″ | ″ | zi: `CLAUDE_CONFIG_DIR` turns claude on | ″ | ″ | 172775748 (`capability/index.ts`; ELF count 1) | `if (n === "claude" && process.env.CLAUDE_CONFIG_DIR?.trim())` |
| agents project (.agent/.agents) | `<d>/.agent/skills`, `<d>/.agents/skills` for each d from {cwd} up to repoRoot ?? home (inclusive), skipping d == home | `skills.enableAgentsProject`, default **true** | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description not required | provider `agents` priority 70; project dirs before user dirs; `.agent` before `.agents` | 173865932 (`discovery/agents.ts`; ELF count 1) | `const p = V9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "project" }));` |
| ″ | both dir names | ″ | ″ | ″ | 173864226 (`discovery/agents.ts`; ELF count 1) | `var y1 = [".agent", ".agents"];` |
| ″ | skip home | ″ | ″ | ″ | 173865668 (`discovery/agents.ts`; ELF count 1) | `if (R !== u.home) {` |
| ″ | walk end | ″ | ″ | ″ | 173865771 (`discovery/agents.ts`; ELF count 1) | `if (R === (u.repoRoot ?? u.home))` |
| ″ | ″ | ″ | ″ | ″ | 172765723 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enableAgentsProject",` |
| ″ | ″ | Dp gate | ″ | ″ | 177500128 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "agents" && vt === "project")` |
| ″ | provider description | ″ | ″ | ″ | 173866320 (`discovery/agents.ts`; ELF count 2) | `Load skills from .agent/skills and .agents/skills (project walk-up + user home)` |
| ″ | ″ | ″ | ″ | priority constant | 173864213 (`discovery/agents.ts`; ELF count 1) | `var Vu = 70;` |
| agents user | `~/.agent/skills`, `~/.agents/skills` (+ same under the Windows profile via `wslpath` when on WSL) | `skills.enableAgentsUser`, default **true** | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped | priority 70, after agents project | 173866025 (`discovery/agents.ts`; ELF count 1) | `const x = z9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "user" }));` |
| ″ | WSL profile lookup | ″ | ″ | ″ | 173864614 (`discovery/agents.ts`; ELF count 1) | `return rMt(["wslpath", "-u", u]);` |
| ″ | ″ | ″ | ″ | ″ | 172765641 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enableAgentsUser", type: "boolean", default: true` |
| ″ | ″ | Dp gate | ″ | ″ | 177500070 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "agents" && vt === "user")` |
| codex user | `~/.codex/skills` | `skills.enableCodexUser`, default **false** (or `enabledProviders` ∋ codex) | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description not required | provider `codex` priority 70 | 173882103 (`discovery/codex.ts`; ELF count 1) | `const p = Ia(u, lre());` |
| ″ | ″ | opt-in check when setting false | ″ | ″ | 173879160 (`discovery/codex.ts`; ELF count 1) | `if (!p && !zi("codex", u))` |
| ″ | ″ | ″ | ″ | ″ | 172765236 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enableCodexUser", type: "boolean", default: false` |
| ″ | ″ | Dp gate | ″ | ″ | 177499744 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "codex" && vt === "user")` |
| ″ | `.codex` base | ″ | ″ | ″ | 172784538 (`discovery/helpers.ts`; ELF count 1) | `userBase: ".codex",` |
| codex project | `{cwd}/.codex/skills` only (no walk-up) | no setting; always on (Dp falls through to `return true` for non-user levels) | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped | priority 70 | 173879095 (`discovery/codex.ts`; ELF count 1) | `return Xr.join(u.cwd, ".codex");` |
| ″ | provider description | ″ | ″ | ″ | 173887155 (`discovery/codex.ts`; ELF count 2) | `Load skills from ~/.codex/skills and .codex/skills/` |
| ″ | ″ | ″ | ″ | priority constant | 173879063 (`discovery/codex.ts`; ELF count 1) | `var _a = 70;` |
| claude-plugins (marketplace) | roots from `<claudeConfigDir>/plugins/installed_plugins.json`, `~/.omp/plugins/installed_plugins.json`, nearest project `<d>/.omp/plugins/installed_plugins.json`; skill dirs = manifest `skills` entries else `<installPath>/skills`, plus `<dir>/SKILL.md` itself | Claude-origin user-scope roots only if `zi(claude-plugins)` or `zi(claude)` (opt-in, default off); omp-origin or project-scope roots on | `<dir>/<name>/SKILL.md` + includeSelf; description not required | provider `claude-plugins` priority 70 | 173849462 (`discovery/claude-plugins.ts`; ELF count 1) | `const _ = k ? x : x.filter((U) => U.scope === "project" \|\| U.origin !== "claude");` |
| ″ | ″ | opt-in test | ″ | ″ | 173849406 (`discovery/claude-plugins.ts`; ELF count 1) | `const k = zi("claude-plugins", u) \|\| zi("claude", u);` |
| ″ | ″ | Dp gate for non-claude origin | ″ | ″ | 177500189 (`extensibility/skills.ts`; ELF count 1) | `if (Ye === "claude-plugins" && et.origin !== undefined && et.origin !== "claude")` |
| ″ | Claude registry path | ″ | ″ | ″ | 172801532 (`discovery/helpers.ts`; ELF count 1) | `const a = [d.join(n, "plugins", "installed_plugins.json"), r];` |
| ″ | omp registry path | ″ | ″ | ″ | 172801398 (`discovery/helpers.ts`; ELF count 1) | `const r = d.join($o(e), "installed_plugins.json");` |
| ″ | project registry | ″ | ″ | ″ | 172800004 (`discovery/helpers.ts`; ELF count 1) | `return d.join(s, o, "plugins", "installed_plugins.json");` |
| ″ | fallback dir | ″ | ″ | ″ | 173852593 (`discovery/claude-plugins.ts`; ELF count 1) | `fallback: "skills",` |
| ″ | ″ | ″ | root SKILL.md included | ″ | 173852800 (`discovery/claude-plugins.ts`; ELF count 1) | `includeSelf: true,` |
| ″ | provider description | ″ | ″ | ″ | 173861867 (`discovery/claude-plugins.ts`; ELF count 2) | `Load skills from Claude Code marketplace plugins (~/.claude/plugins/cache/)` |
| ″ | ″ | ″ | ″ | priority constant | 173849304 (`discovery/claude-plugins.ts`; ELF count 1) | `var ju = 70;` |
| agent-plugins (agent-plugins.org) | `<realRoot>/skills/<name>/SKILL.md` for each plugin root (Claude/omp registries ∪ omp extension roots) whose root holds a valid `plugin.json` | no opt-in (provider not in opt-in set) | one level; SKILL.md must resolve inside the plugin root; strict frontmatter (description required); name = dir name | priority 75 | 173778070 (`discovery/agent-plugins.ts`; ELF count 1) | `const _ = await FS(u, Ym.join(u, "skills"));` |
| ″ | root sources | ″ | ″ | ″ | 173777364 (`discovery/agent-plugins.ts`; ELF count 1) | `IA(u.home, u.cwd),` |
| ″ | roots without root `plugin.json` contribute nothing | ″ | ″ | ″ | 173779995 (`discovery/agent-plugins.ts`; ELF count 1) | `if (k.kind === "none")` |
| ″ | classification reads `<root>/plugin.json` | ″ | ″ | ″ | 173712468 (`discovery/agent-plugin-format.ts`; ELF count 1) | `const x = await FS(p, nd.join(p, "plugin.json"));` |
| ″ | provider description | ″ | ″ | ″ | 173777198 (`discovery/agent-plugins.ts`; ELF count 2) | `Portable Agent Plugins packages (plugin.json, skills/, mcp.json) per agent-plugins.org` |
| ″ | ″ | ″ | ″ | priority constant | 173777287 (`discovery/agent-plugins.ts`; ELF count 1) | `var uD = 75;` |
| opencode user | `~/.config/opencode/skills` | opt-in `zi("opencode")`, default off | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped | provider `opencode` priority 55 | 173903113 (`discovery/opencode.ts`; ELF count 1) | `const p = Ac(u, "opencode", "skills");` |
| ″ | ″ | ″ | ″ | ″ | 172785565 (`discovery/helpers.ts`; ELF count 1) | `if (!zi(t, e))` |
| ″ | ″ | ″ | ″ | ″ | 172784759 (`discovery/helpers.ts`; ELF count 1) | `userAgent: ".config/opencode",` |
| opencode project | `{cwd}/.opencode/skills` only | always on | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped | priority 55 | 172784794 (`discovery/helpers.ts`; ELF count 1) | `projectDir: ".opencode"` |
| ″ | project path = cwd/projectDir/skills (no walk) | ″ | ″ | ″ | 172785704 (`discovery/helpers.ts`; ELF count 1) | `return d.join(e.cwd, r.projectDir, n);` |
| ″ | provider description | ″ | ″ | ″ | 173905684 (`discovery/opencode.ts`; ELF count 2) | `Load skills from ~/.config/opencode/skills/ and .opencode/skills/` |
| github project | `{cwd}/.github/skills` only | always on | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description required | provider `github` priority 30 | 173910415 (`discovery/github.ts`; ELF count 1) | `const p = os(u, "github", "skills");` |
| ″ | ″ | ″ | ″ | ″ | 172785178 (`discovery/helpers.ts`; ELF count 1) | `projectDir: ".github"` |
| ″ | provider description | ″ | ″ | ″ | 173911210 (`discovery/github.ts`; ELF count 2) | `Load skills from .github/skills/*/SKILL.md` |
| ″ | ″ | ″ | ″ | priority constant | 173906379 (`discovery/github.ts`; ELF count 1) | `var fh = 30;` |
| custom directories | each entry of `skills.customDirectories` (`~` expanded), scanned directly | `skills.customDirectories`, default `[]` | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description required | processed after all providers; a custom skill **displaces** an earlier non-custom skill of the same name (that one is renamed `<ns>/<name>`) | 177503195 (`extensibility/skills.ts`; ELF count 1) | `const vt = await Ba({ cwd: p, home: gx.homedir(), repoRoot: null }, {` |
| ″ | ″ | ″ | ″ | ″ | 172765812 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.customDirectories",` |
| ″ | ″ | default in Dp | ″ | ″ | 177499434 (`extensibility/skills.ts`; ELF count 1) | `customDirectories: Y = [],` |
| ″ | ″ | ″ | ″ | source tag | 177503873 (`extensibility/skills.ts`; ELF count 1) | `source: "custom:user",` |
| ″ | ″ | ″ | ″ | displacement rule | 177497011 (`extensibility/skills.ts`; ELF count 1) | `if (U && (X && !z \|\| Y && !Q)) {` |
| managed (auto-learn) | `~/.omp/agent/managed-skills` | none (provider `omp-managed`) | one level: `<root>/<name>/SKILL.md`; entries starting `.` skipped; dir **or symlink** entries accepted (`existsSync` follows link); name = frontmatter `name` else dir name; `enabled: false` skipped; description required, name must match `^[a-z0-9][a-z0-9-]{0,63}$` | added last, only if no other enabled provider has an item with that name | 173809938 (`autolearn/managed-skills.ts`; ELF count 1) | `return Zm.join(u, "managed-skills");` |
| ″ | ″ | ″ | ″ | excluded from main loop | 177500925 (`extensibility/skills.ts`; ELF count 1) | `if (et._source.provider === sl)` |
| ″ | ″ | ″ | ″ | ″ | 177504756 (`extensibility/skills.ts`; ELF count 1) | `const ze = he.all.filter((et) => et._source.provider === sl && kD(et.name)` |
| ″ | ″ | ″ | ″ | ″ | 177505278 (`extensibility/skills.ts`; ELF count 1) | `if (rt.has(Ye.name))` |
| ″ | provider description | ″ | ″ | ″ | 173820704 (`discovery/builtin.ts`; ELF count 2) | `Auto-generated managed skills from ~/.omp/agent/managed-skills` |
| ″ | ″ | ″ | ″ | priority constant 5 | 173820771 (`discovery/builtin.ts`; ELF count 1) | `priority: P7,` |
| ALL (provider order) | providers sorted by priority, ties keep registration order | `disabledProviders` (default []) removes a provider; `enabledProviders` (default []) opts in | — | insert before first provider with lower priority | 172771631 (`capability/index.ts`; ELF count 1) | `const s = r.findIndex((o) => o.priority < t.priority);` |
| ″ | ″ | disabled provider filter | ″ | ″ | 172774496 (`capability/index.ts`; ELF count 1) | `let r = e.providers.filter((s) => !n.has(s.id));` |
| ″ | ″ | opt-in provider set (claude, codex, claude-plugins, opencode, github…) | ″ | ″ | 172770804 (`capability/index.ts`; ELF count 1) | `"claude-plugins": true,` |
| ″ | ″ | non-opt-in providers always on | ″ | ″ | 172775479 (`capability/index.ts`; ELF count 1) | `if (me[n] !== true)` |
| ″ | ″ | enabledProviders wildcard | ″ | ″ | 172775619 (`capability/index.ts`; ELF count 1) | `if (r.has(n) \|\| r.has("*") \|\| r.has("all"))` |
| ″ | ″ | ″ | ″ | ″ | 172769040 (`config/model-settings.ts`; ELF count 1) | `id: "enabledProviders",` |
| ″ | ″ | ″ | ″ | ″ | 172769155 (`config/model-settings.ts`; ELF count 1) | `id: "disabledProviders",` |
| ALL (dedupe) | capability-level key=name shadowing is bypassed: Dp reads `he.all` (includes shadowed) | — | — | first pass: skip a SKILL.md whose realpath was already accepted (symlinked duplicates collapse) | 172774366 (`capability/index.ts`; ELF count 1) | `all: o.size > 0 ? s.filter((g) => !o.has(g)) : s,` |
| ″ | ″ | ″ | ″ | ″ | 177500357 (`extensibility/skills.ts`; ELF count 1) | `const he = await kn(zl.id, {` |
| ″ | ″ | ″ | ″ | ″ | 177502338 (`extensibility/skills.ts`; ELF count 2) | `return await Ef.realpath(et.path);` |
| ″ | ″ | ″ | ″ | ″ | 177502514 (`extensibility/skills.ts`; ELF count 1) | `if (ye.has(vt)) {` |
| ″ | ″ | ″ | ″ | same name + identical body and frontmatter → later copy dropped | 177496904 (`extensibility/skills.ts`; ELF count 1) | `const te = F.filter(([ue, he]) => he.body === R && Bun.deepEquals(he.frontmatter, k)).map(([ue]) => ue);` |
| ″ | ″ | ″ | ″ | same name, different content → later copy kept as `<ns>/<name>` (ns = plugin name or dir before `skills`, provider id if that starts with `.`), `~2`… on clash | 177497593 (`extensibility/skills.ts`; ELF count 1) | `let re = `${_}/${x.name}`;` |
| ″ | ″ | ″ | ″ | ″ | 177498036 (`extensibility/skills.ts`; ELF count 1) | `differs from ${oe}; available as "${re}"` |
| ″ | ″ | ″ | ″ | namespace derivation | 177496206 (`extensibility/skills.ts`; ELF count 1) | `const k = R.lastIndexOf("skills");` |
| ALL (filters + order) | — | `skills.enabled` default true; `skills.ignoredSkills` / `skills.includeSkills` (globs, default []); `disabledExtensions` `skill:<name>` | — | ignored glob drops | 177500730 (`extensibility/skills.ts`; ELF count 1) | `return Q.some((Ye) => new Bun.Glob(Ye).match(et));` |
| ″ | ″ | include glob keeps only matches | ″ | ″ | 177500606 (`extensibility/skills.ts`; ELF count 1) | `return te.some((Ye) => new Bun.Glob(Ye).match(et));` |
| ″ | ″ | disabledExtensions | ″ | ″ | 177500816 (`extensibility/skills.ts`; ELF count 1) | `.filter((et) => et.startsWith("skill:")).map((et) => et.slice(6))` |
| ″ | ″ | ″ | ″ | ″ | 172764925 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.enabled", type: "boolean", default: true` |
| ″ | ″ | ″ | ″ | ″ | 172765894 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.ignoredSkills",` |
| ″ | ″ | ″ | ″ | ″ | 172765972 (`extensibility/settings.ts`; ELF count 1) | `id: "skills.includeSkills",` |
| ″ | ″ | ″ | ″ | final list sorted by name (case-insensitive, then case-sensitive, then path) | 177505946 (`extensibility/skills.ts`; ELF count 1) | `Et.sort((et, Ye) => dne(et.name, et.filePath, Ye.name, Ye.filePath));` |
| ALL (catalogue render) | — | frontmatter `hide: true` or `disableModelInvocation: true` → discovered but not rendered | — | render input = skills with hide !== true | 178835365 (`system-prompt.ts`; ELF count 1) | `.render(be ? ue.filter((e) => e.hide !== true) : [])` |
| ″ | ″ | ″ | ″ | ″ | 180946502 (`session/agent-session.ts`; ELF count 1) | `this.#Zn.render(s ? this.skills.filter((g) => g.hide !== true) : [])` |
| ″ | ″ | ″ | ″ | ″ | 177502945 (`extensibility/skills.ts`; ELF count 2) | `Ye.frontmatter?.disableModelInvocation === true,` |
| ALL (rediscovery) | rediscoverSkills re-runs loadSkills with the session settings | — | — | same rules | 177506492 (`extensibility/skills.ts`; ELF count 1) | `const p = await Dp({` |
| ″ | ″ | ″ | ″ | ″ | 177506517 (`extensibility/skills.ts`; ELF count 1) | `...xc.get(u.settings),` |

## Host state read (read-only)

- `~/.omp/agent/config.yml`: top-level keys `setupVersion, extendedContext, enabledModels, modelRoles, task, retry, dev, tools, async, tier, textVerbosity, hideThinkingBlock, omitThinking, codexResets`; **no** `skills`, `extensions`, `enabledProviders`, `disabledProviders` or `disabledExtensions` key → every gate above is at its default. No `~/.omp/agent/settings.json`.
- `CLAUDE_CONFIG_DIR`, `PI_CONFIG_DIR`, `PI_PROFILE`, `OMP_PROFILE`, `CODEX_HOME` unset in this seat's shell (the rendering session's environment was not observable).
- omp plugin manifests: `~/.omp/plugins/package.json` (`dependencies: {}`), `~/.omp/plugins/omp-plugins.lock.json` lists `ecc-pi-core` 2.2.3 and `unreal-engine-skills-omp` 3.1.1, both `enabled: true`; both `node_modules/<name>` are symlinks (so the stale-lock filter keeps them). `ecc-pi-core/package.json` has `"pi": {"skills": ["./skills"], …}` and `skills/` with 132 entries; `unreal-engine-skills-omp` has an `omp` field but no `skills/` dir. No root `plugin.json` in either.
- `~/.claude/plugins/installed_plugins.json`: 4 Claude-origin user-scope plugins (frontend-design, unity, unreal-engine-skills, superpowers) — filtered out (claude/claude-plugins opt-in off); none has a root `plugin.json`, so agent-plugins ignores them too.
- Present roots: `~/.agents/skills` 83, `~/.claude/skills` 27 (gate off), `~/.codex/skills` 2 (gate off), `~/.omp/agent/skills` absent, `~/.omp/agent/managed-skills` absent, no skills.lock.json. Fleet cwd `/home/vgpnk/Projects/shokunin` is itself the git root (walk-up = cwd only) and holds no `.omp/.claude/.agent/.agents/.codex/.opencode/.github` skills dir.
- Predicted catalogue for that cwd: `~/.agents/skills` (83) + `~/.omp/plugins/node_modules/ecc-pi-core/skills` (132) = 215, 0 name overlap (`comm -12`, LC_ALL=C). All 132 base `not-discovered` names exist as `ecc-pi-core/skills/<name>/SKILL.md` (132/132).

## Unresolved

- Execution order of equal-priority (70) registrations (`claude-plugins`, `agents`, `codex`): byte order is claude-plugins 173861810 < agents 173866263 < codex 173887098; that registration follows byte order is [INFERENCE] (I did not check for lazy module init wrappers). No effect on this host (no overlapping names).
- `yne` (per-plugin manifest reader for claude-plugins `skills` key) and `AP`'s project root (`Jl`) were read only in part; neither applies on this host.
- I did not trace the render step after the `hide` filter (`skill-descriptions.ts`, owned by the plan's render claim).
