# derived | r86 | r87 — skill-root pattern set

| # | derived root (re-derived from the ELF) | join-site offset in the ELF | r86 | r87 |
|---|---|---|---|---|
| 1 | `{cwd}/.omp/skills` | 173819979 | yes | yes |
| 2 | `{cwd}/.claude/skills` | 173840364 | yes | yes |
| 3 | `{cwd}/.agent/skills` | 173865724 | yes | yes |
| 4 | `{cwd}/.agents/skills` | 173865724 | yes | yes |
| 5 | `{cwd}/.codex/skills` | 173882193 | yes | yes |
| 6 | `{cwd}/.opencode/skills` | 172785704 | yes | yes |
| 7 | `{cwd}/.github/skills` | 172785704 | yes | yes |
| 8 | `~/.omp/agent/skills` | 173820135 | yes | yes |
| 9 | `~/.omp/plugins/node_modules/*/skills` | 173914936 | yes | yes |
| 10 | `~/.agent/skills` | 173865523 | yes | yes |
| 11 | `~/.agents/skills` | 173865523 | yes | yes |
| 12 | `~/.omp/agent/managed-skills` | 173809938 | yes | yes |
| 13 | `~/.claude/skills` | 173840218 | **NO** | **NO** |
| 14 | `~/.codex/skills` | 173882129 | **NO** | **NO** |
| 15 | `~/.config/opencode/skills` | 172785499 | **NO** | **NO** |
| 16 | `~/.omp/skillshare/@scope/*/*` | 173923798 | **NO** | **NO** |
| 17 | `<plugin-root>/skills (claude marketplace)` | 173851107 | **NO** | **NO** |
| 18 | `<plugin-root>/skills (agent plugins)` | 173778070 | **NO** | **NO** |

Notes per derived row:
1. `{cwd}/.omp/skills` — native (builtin.ts): join(projectDir=".omp", "skills") over project dirs  [offsets: [173819979]]
2. `{cwd}/.claude/skills` — claude.ts Zte(): walk-up join(dir, ".claude", "skills")  [offsets: [173840364]]
3. `{cwd}/.agent/skills` — agents.ts Gne(): V9() walk-up, y1=[".agent",".agents"], p="skills"  [offsets: [173865724]]
4. `{cwd}/.agents/skills` — agents.ts Gne(): same site, second element of y1  [offsets: [173865724]]
5. `{cwd}/.codex/skills` — codex.ts mre(): R = join(cwd, ".codex")  [offsets: [173882193]]
6. `{cwd}/.opencode/skills` — helpers.ts os(): ZO.opencode.projectDir=".opencode", n="skills"  [offsets: [172785704]]
7. `{cwd}/.github/skills` — helpers.ts os(): ZO.github.projectDir=".github", n="skills"  [offsets: [172785704]]
8. `~/.omp/agent/skills` — builtin.ts T7(): join(we()=agentDir, "skills")  [offsets: [173820135]]
9. `~/.omp/plugins/node_modules/*/skills` — omp-plugins.ts uie(): join(pluginPath, "skills"); plugin root = $o()/node_modules  [offsets: [173914936]]
10. `~/.agent/skills` — agents.ts Gne(): z9() over Wne(u) home dirs, p="skills"  [offsets: [173865523]]
11. `~/.agents/skills` — agents.ts Gne(): same site, second element of y1  [offsets: [173865523]]
12. `~/.omp/agent/managed-skills` — autolearn/managed-skills.ts w9(): join(agentDir, "managed-skills")  [offsets: [173809938]]
13. `~/.claude/skills` — claude.ts Zte(): p = dl(u)=CLAUDE_CONFIG_DIR|~/.claude -> USER-level skills root  [offsets: [173840218]]
14. `~/.codex/skills` — codex.ts mre(): p = Ia(u)=~/.codex -> USER-level skills root  [offsets: [173882129]]
15. `~/.config/opencode/skills` — helpers.ts V$e(): ZO.opencode.userAgent=".config/opencode" -> USER-level skills root  [offsets: [172785499]]
16. `~/.omp/skillshare/@scope/*/*` — skillshare.ts: Tie()=join(dirname(agentDir),"skillshare"); VH() joins @scope/name/version  [offsets: [173923798]]
17. `<plugin-root>/skills (claude marketplace)` — claude-plugins.ts g1(): fallback "skills" under each marketplace plugin root (~/.claude/plugins/cache/...)  [offsets: [173851107]]
18. `<plugin-root>/skills (agent plugins)` — agent-plugins.ts QQ(): join(pluginRoot, "skills")  [offsets: [173778070]]

derived rows: 18
r86 carries 12 patterns; r87 carries 12 patterns
derived∩r86 = 12; derived∩r87 = 12

Holes (derived root the round's model does not carry):
  - ~/.claude/skills
  - ~/.codex/skills
  - ~/.config/opencode/skills
  - ~/.omp/skillshare/@scope/*/*
  - <plugin-root>/skills (claude marketplace)
  - <plugin-root>/skills (agent plugins)

False rows (carried in r86/r87 but NOT a derived skill root):
  (none)

coverage: 18 derived, 12 matched, holes=['~/.claude/skills', '~/.codex/skills', '~/.config/opencode/skills', '~/.omp/skillshare/@scope/*/*', '<plugin-root>/skills (claude marketplace)', '<plugin-root>/skills (agent plugins)'], false=[]
