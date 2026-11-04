# ReviewerRoots — C1 roots review (round 86, w1)

Seat: ReviewerRoots (non-author). I derived the independent table from the ELF before opening ExecModel's files. Candidate: ExecModel CANDIDATE_READY (commit 903bd78e, files `verify_harness_claims.py` sha256 bd793b6c…, `omp-skill-roots.tsv` sha256 36021309…).

## 1. Independent root table (derived from the omp 18.15.0 ELF before reading ExecModel's files)

ELF `/home/vgpnk/.local/bin/omp`, sha256 `6737ee24…7b0f` (matches plan pin). Offsets are byte offsets of the first match (python mmap + re).
Mechanism: `loadSkills` (`Dp`, skills.ts) calls the capability loader `kn(zl.id)` and iterates `he.all` (every provider's items, NOT the per-name deduped list; `const ke = he.all.filter((et) => {` @177500886). Provider order = descending `priority`, ties keep registration order (`const s = r.findIndex((o) => o.priority < t.priority);` @172771631). Per provider, `Ba(dir)` reads one level `<dir>/<child>/SKILL.md` (`const c = d.join(s, S.name, "SKILL.md");` @172791679), skips dot-children (@172791566), name = frontmatter `name` else dir basename (`const v = typeof x === "string" ? x.trim() || g : g;` @172790973), drops description-less files only when the provider passes `requireDescription` (@172790850). Then `loadSkills` dedups by realpath (@177502514); first name wins; a later same-name skill with identical body+frontmatter is dropped (@177496904), a differing one is renamed `<namespace>/<name>` (``let re = `${_}/${x.name}`;`` @177497593); final list sorted by name (@177505946).

| # | provider (priority) | root(s) omp reads | gate on this host (no `skills.*` keys in `~/.omp/agent/config.yml`, `CLAUDE_CONFIG_DIR` unset) | located quote(s) | host state / fixture names |
|---|---|---|---|---|---|
| R1 | native "OMP" (100) | `~/.omp/agent/skills` (user); `<d>/.omp/skills` for each `d` from cwd up to repoRoot (home, tmp excluded) | on (`enablePiUser`/`enablePiProject` default true) | `dir: fr.join(we(), "skills"),` @173820135; `dir: fr.join(k, Ou.projectDir, "skills"),` @173819979; `var Ko = 100;` in `var Or = "native"…` @173814273; agentDir `const a = h.join(this.configRoot, "agent");` @166888442 | absent on host; 0 names |
| R2 | skillshare (95) | `~/.omp/agent/<lock>` store (`omp skill install`) | on | `const R = iF(ab.join(we(), sb), "user", p);` @173927768 | no lock on host; 0 names |
| R3 | omp-plugins "OMP Extension Packages" (90) | `<pkg>/skills` for each package in `<pluginsDir>/node_modules/<name>` whose package.json has `omp` or `pi` and is in package.json deps or (symlinked) `omp-plugins.lock.json`, not disabled; pluginsDir = `~/.omp/plugins` | on (not opt-out) | `dir: Zo.join(R.path, "skills"),\n    providerId: xo,` @173914936; `var wd = 90;` @173914660; `const R = yo.join(u, "node_modules");` @173767148; `path: yo.join(R, te),` @173769102; `const ue = oe.omp \|\| oe.pi;` @173768743; `const U = yo.join(u, "omp-plugins.lock.json");` @173767575; `return c.rootSubdir("plugins", "data");` @166892424 | `~/.omp/plugins/node_modules/ecc-pi-core` → symlink `/home/vgpnk/.ecc/pi/core` (package.json `"pi": {"skills": ["./skills"]}`, lock `enabled: true`): **132 fixture names**. `unreal-engine-skills-omp` has no `skills/`: 0 |
| R4 | claude (80) | user `~/.claude/skills` (or `$CLAUDE_CONFIG_DIR/skills`); project `<d>/.claude/skills` walk-up | user: **off** — `enableClaudeUser` default false and `claude` is opt-out-by-default (`var me = { … claude: true`) unless opted in or `CLAUDE_CONFIG_DIR` set; project: on | `if (Ye === "claude" && vt === "user")\n      return k \|\| zi("claude");` @177499816; `enableCodexUser: R = false,\n    enableClaudeUser: k = false,` @177499208; `var me = {\n  cursor: true,\n  codex: true,\n  claude: true,` @172770744; `dir: Fr.join(k, eh, "skills"),` @173840364 | `~/.claude/skills` exists (24 names, 23 of them also in R6) but is NOT read; no project `.claude/skills` |
| R5 | agent-plugins (75), claude-plugins (70) | plugin install paths from `~/.claude/plugins/installed_plugins.json` / omp registry | claude-origin user-scope plugins **off** (opt-in) | `const k = zi("claude-plugins", u) \|\| zi("claude", u);` @173849406 | 4 Claude marketplace plugins installed, not read; 0 names |
| R6 | agents "Agent Dirs (.agent/.agents)" (70) | user `~/.agent/skills`, `~/.agents/skills` (+ WSL USERPROFILE twin); project `<d>/.agent/skills`, `<d>/.agents/skills` for `d` from cwd up to repoRoot ?? home, **excluding home itself** | on (`enableAgentsUser`/`Project` default true) | `var y1 = [".agent", ".agents"];` @173864226; `const x = z9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "user" }));` @173866025; `const p = V9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "project" }));` @173865932; `if (Ye === "agents" && vt === "user")\n      return z;` @177500070; `var Vu = 70;` @173864154 | `~/.agents/skills`: **83 fixture names** (78 real dirs + symlinked dirs); `~/.agent/skills` absent; no project `.agent(s)/skills` under `/home/vgpnk/Projects/shokunin` |
| R7 | codex (70) | user `~/.codex/skills`; project `<cwd>/.codex/skills` (cwd only, no walk-up) | user **off** (opt-out-by-default, `enableCodexUser` false) | `if (Ye === "codex" && vt === "user")\n      return R \|\| zi("codex");` @177499744; `var _a = 70;` @173879020 | `~/.codex/skills` exists (2) but not read |
| R8 | opencode (55), github (30) | user `~/.config/opencode/skills` (opt-in); project `<cwd>/.opencode/skills`, `<cwd>/.github/skills` | opencode user off (opt-in) | `const p = Ac(u, "opencode", "skills");` @173903113 | all absent |
| R9 | custom (`skills.customDirectories`) | each listed dir | default `[]` | `id: "skills.customDirectories",\n  type: "array",\n  default: V` @172765812 | none configured |
| R10 | omp-managed (5) | `~/.omp/agent/managed-skills` (only names that no other provider has) | on | `return Zm.join(u, "managed-skills");` @173809938 | absent |

**Independent conclusion:** on this host with cwd `/home/vgpnk/Projects/shokunin` omp 18.15.0 reads exactly two non-empty roots: R3 `~/.omp/plugins/node_modules/ecc-pi-core/skills` (132, priority 90, `requireDescription: true`) and R6 `~/.agents/skills` (83, priority 70). 132 + 83 = 215 = fixture; the two sets are disjoint, so no collision rename fires. `~/.claude/skills`, `~/.codex/skills`, `~/.config/opencode/skills` and the Claude marketplace plugin caches are NOT read by default. The base model's `USER_ROOTS` includes `~/.claude/skills` and `~/.config/opencode/skills` (both opt-in in omp, so wrong for this host), omits R3 and models walk-up at cwd only.

## 2. Per-row verdicts on `verifiers/omp-skill-roots.tsv` (working tree, sha256 `36021309…c7800`)

Ledger quotes' offsets are the first match in the ELF. The description strings sit in the bun string table (~114.48 M) and again next to each `Fe(zl.id, {…})` registration in the embedded source.

| # | root_pattern | ledger quote (@offset) | verdict | reason | my located quote (@offset) |
|---|---|---|---|---|---|
| 1 | `{cwd}/.omp/skills` | `Native OMP configuration from ~/.omp and .omp/` (@114486488) | **located but irrelevant** | `Js` is the native provider's generic description, shared by 11 `description: Js,` registrations (settings, MCP, commands, rules, …). It never mentions skills or a `.omp/skills` walk-up. The root itself is right. | `dir: fr.join(k, Ou.projectDir, "skills"),` (@173819979), inside `T7`, which is registered as `Fe(zl.id, { id: Or, … load: T7 })` (@173820529) |
| 2 | `{cwd}/.claude/skills` | `Load skills from .claude/skills/*/SKILL.md` (@114489000) | **sound** | This is the description of the claude provider's skills registration (`description: "Load skills from .claude/skills/*/SKILL.md"` @173847145). The project level is on by default. | `dir: Fr.join(k, eh, "skills"),` (@173840364); gate `if (Ye === "claude" && vt === "project")\n      return _;` (@177499890) with `enableClaudeProject: _ = true,` (@177499273) |
| 3 | `{cwd}/.agent/skills` | `Load skills from .agent/skills and .agents/skills (project walk-up + user home)` (@114490024) | **sound** | Description of the agents skills registration. It states the project walk-up. | `const p = V9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "project" }));` (@173865932); `var y1 = [".agent", ".agents"];` (@173864226) |
| 4 | `{cwd}/.agents/skills` | same as row 3 | **sound** | Same as row 3. | same as row 3 |
| 5 | `{cwd}/.codex/skills` | `Load skills from ~/.codex/skills and .codex/skills/` (@114490716) | **sound** (the pattern is looser than omp) | Codex skills registration. omp reads `<cwd>/.codex/skills` only, with no walk-up (`ul(u)` = `Xr.join(u.cwd, ".codex")`). G4's `{cwd}/` also matches every ancestor. | `const k = Xr.join(R, "skills");` (@173882193) |
| 6 | `{cwd}/.opencode/skills` | `Load skills from ~/.config/opencode/skills/ and .opencode/skills/` (@114492072) | **sound** (cwd only, same caveat as row 5) | OpenCode skills registration. The project level passes `ue()` (falls through to `return true`). | `const x = os(u, "opencode", "skills");` (@173903154) |
| 7 | `{cwd}/.github/skills` | `Load skills from .github/skills/*/SKILL.md` (@114492692) | **sound** (cwd only) | GitHub skills registration. | `const p = os(u, "github", "skills");` (@173910415) |
| 8 | `~/.omp/agent/skills` | `Native OMP configuration from ~/.omp and .omp/` (@114486488) | **located but irrelevant** | Same generic `Js` string as row 1. The root is right but empty on the host. | `dir: fr.join(we(), "skills"),` (@173820135); `we()` returns `c.agentDir`, where `const a = h.join(this.configRoot, "agent");` (@166888442) |
| 9 | `~/.omp/plugins/node_modules/*/skills` | `var Gh = ".omp";` (@166884553) | **located but irrelevant** (as the only citation) | This is the config-dir constant behind every `~/.omp` path (`qh()` returns `process.env.PI_CONFIG_DIR \|\| Gh`). It names the `.omp` segment and nothing else: no `plugins`, no `node_modules`, no `skills`. **This row carries 132 of the 215 names.** omp does read this root (I derived it independently; see R3), so the root is sound and the citation is not. Root cause in the counter: addendum-1's dot-segment rule requires the quote to contain `.omp` verbatim, and the ELF has no literal `.omp/plugins` or `omp/plugins` (searched: 0 hits). The code that reads the root can therefore never satisfy G4, and a bare constant is the only quote that passes. | `dir: Zo.join(R.path, "skills"),\n    providerId: xo,` (@173914936, `uie`, priority `var wd = 90;` @173914660); `const R = yo.join(u, "node_modules");` (@173767148); `path: yo.join(R, te),` (@173769102); `const ue = oe.omp \|\| oe.pi;` (@173768743); `const U = yo.join(u, "omp-plugins.lock.json");` (@173767575); `return c.rootSubdir("plugins", "data");` (@166892424) |
| 10 | `~/.agent/skills` | row-3 quote | **sound** | The agents description names the user home. | `const x = z9(u, "skills").map((k) => Ba(u, { dir: k, providerId: Yo, level: "user" }));` (@173866025); `return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));` (@173865523) |
| 11 | `~/.agents/skills` | row-3 quote | **sound** | Same as row 10. **This row carries 83 of the 215 names.** | same as row 10; gate `if (Ye === "agents" && vt === "user")\n      return z;` (@177500070) |
| 12 | `~/.omp/agent/managed-skills` | `Auto-generated managed skills from ~/.omp/agent/managed-skills` (@114486660) | **sound** | Description of the managed provider's skills registration (`Fe(zl.id, { id: sl, … })` @173820620). It states the path. | `return Zm.join(u, "managed-skills");` (@173809938) |

Tally: 9 sound, 3 located but irrelevant (rows 1, 8, 9), 0 wrong. The ledger includes no root that omp 18.15.0 does not read on this host. It correctly leaves out `~/.claude/skills`, `~/.codex/skills`, `~/.config/opencode/skills` and the Claude marketplace caches, all of which are opt-in (`var me = {\n  cursor: true,\n  codex: true,\n  claude: true,` @172770744; `enableCodexUser: R = false,\n    enableClaudeUser: k = false,` @177499208). The base model had included `~/.claude/skills` and `~/.config/opencode/skills`. Not modelled: skillshare (priority 95, `const R = iF(ab.join(we(), sb), "user", p);` @173927768) and custom directories (default `[]`). Both are empty on this host, so this is a coverage gap, not an error.

## 3. Precedence verdict (diff `e5d966b..working tree -- verifiers/verify_harness_claims.py`, 229+/52−)

What the model gets right, compared with my derivation:
- The root set: native, omp-plugins (`omp_plugin_skill_roots` reproduces `eD`: package.json deps ∪ lock keys, undeclared lock entries only when symlinked, `oe.omp || oe.pi`, `if (he && !he.enabled) continue`, then `<pkg>/skills`), agents, managed. Claude, codex and opencode user roots are dropped.
- `Ba`'s per-root scan: one level deep, dot entries skipped, the frontmatter `name` (trimmed) or else the directory name, path-separator names skipped.
- `managed` placed last. omp only fills managed names that no other root has, so this is equivalent.

Where it diverges from omp's order and precedence. None of these is exercised on this host:
- **P1 order across lists.** omp orders providers by priority. Native (100), project then user, comes first; then omp-plugins (90); then claude (80); then agents (70, project then user); then codex (70), opencode (55), github (30). The counter fixes the root order as `WALKUP_REL + USER_ROOTS`, and the model puts every project root first. So `{cwd}/.claude/skills`, `{cwd}/.agent(s)/skills` and `{cwd}/.codex/skills` outrank `~/.omp/agent/skills` and the omp plugins, and `{cwd}/.codex/skills` outranks `~/.agents/skills`. Probe D below: with `foo` in both `{cwd}/.claude/skills` and `~/.omp/agent/skills`, the model picks `proj/.claude/skills`. omp would keep the native-user `foo` and expose the claude one as `<ns>/foo`. The code comment "Provider priority … orders each list below" holds within each list but not across the two.
- **P2 collisions.** omp keeps the first-seen name. A later skill with the same name is dropped only if body and frontmatter are identical; otherwise it is renamed `<ns>/<name>` (`let re = \`${_}/${x.name}\`;` @177497593) and the renamed entry appears in the catalogue. The model drops it (`setdefault`). The code comment discloses this. On this host there are no cross-root duplicate names among the roots omp reads (probe A: `{}`).
- **P3 `requireDescription`.** omp drops description-less SKILL.md files for native, omp-plugins, github and managed (`requireDescription: true`) but not for agents. `discover_skills` does not model this. It does not matter here (every fixture name has a description).
- **P4 sandbox fallback is not omp semantics.** When neither `package.json` nor `omp-plugins.lock.json` is readable, `omp_plugin_skill_roots` takes every package that has a manifest. In that case omp's `eD` yields zero plugins: an ENOENT on package.json leaves `k=[]`, and an ENOENT on the lock gives `qg({})`, so the candidate set `X` is empty. Probe C: a lock with `enabled:false` gives `[]` (correct); with the registry hidden, the model returns `node_modules/disabledpkg/skills` (wrong for omp). The counter's sandbox hides all of `~/.omp` and rebinds only `plugins/node_modules` and `agent/skills` (`default_rebind`). The counter run therefore scores this fallback branch, not the registry branch. The two agree on this host only because both lock entries are `enabled: true` and `unreal-engine-skills-omp` has no `skills/`.

Does it reproduce lines by accident? No. Ablation on the host (probe A): of the 215 offered names, 132 come from `~/.omp/plugins/node_modules/ecc-pi-core/skills` and 83 from `~/.agents/skills`. These are exactly the two roots my independent derivation says omp reads. There are no extra names (`extra []`), and no name is reached through a root omp does not read. Identical copies of the 132 also sit at `~/.ecc/skills`, `~/.zcode/.../ecc/.../skills` and elsewhere; the model does not use them. Its path goes through the node_modules symlink, as omp's does.
**Precedence verdict: the root set and the per-root scan follow omp. Cross-provider order (P1), namespaced collisions (P2), requireDescription (P3) and the registry-hidden fallback (P4) do not. All four are latent on this host and none contributes to N.**

### Probe receipts (scratch `/fast/scratch/hyaku/kotoba-r86/ReviewerRoots`, candidate module imported from the scratch clone)
```
A offered 215 fixture-in-offered 215 extra []
A root /home/vgpnk/.agents/skills 83
A root /home/vgpnk/.omp/plugins/node_modules/ecc-pi-core/skills 132
A cross-root duplicate dir names: {}
C with registry (lock enabled:false): []
C registry hidden (omp eD: package.json ENOENT -> deps [], lock ENOENT -> {} -> 0 plugins): ['node_modules/disabledpkg/skills']
D model winner for foo: proj/.claude/skills
```

## 4. Counter re-run (mine, scratch clone)
```
D=/fast/scratch/hyaku/kotoba-r86/ReviewerRoots/repo; git clone -q --shared <lane> "$D"   # HEAD b9ee5484a139c4428a2d53e572868abe86844821
cp <lane>/verifiers/{verify_harness_claims.py,omp-skill-roots.tsv} "$D/verifiers/"   # sha256 bd793b6c…0ab7, 36021309…c7800 (= CANDIDATE_READY)
git -C "$D" -c user.name=seat -c user.email=seat@local commit -qam cand              # bb5973526b0e19f4c204d8be9469bc2c2386a667
TMPDIR=$S python3 -B <lane>/verifiers/check_omp_catalogue_repro.py --repo "$D" --rev bb5973526b0e19f4c204d8be9469bc2c2386a667
```
Last 6 lines (+ exit):
```
rev bb5973526b0e19f4c204d8be9469bc2c2386a667 fixture sha256 0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488 session_cwd /home/vgpnk/Projects/shokunin
guard G1 no-echo PASS
guard G2 provenance PASS
guard G3 fixture PASS
guard G4 roots PASS
omp catalogue lines reproduced 215 of 215
exit=0
```
This matches ExecModel's CANDIDATE_READY (215 of 215, G1–G4 PASS, exit 0) on a different scratch commit with the same file hashes.

## 5. Counter findings (reported, not patched)
- **CF1:** G4 checks only that a quote is located, plus addendum-1's dot-segment rule. It accepts `var Gh = ".omp";` for the plugin root. The dot rule makes a code-relevant quote for `~/.omp/plugins/...` impossible, because the ELF has no `.omp/plugins` literal. So G4 PASS on row 9 carries no meaning, and the meaning check rests entirely on this review.
- **CF2:** `{cwd}/` expands to `cwd` and every ancestor, including `$HOME` and `/`. omp's project walk-ups stop at the repo root (or `$HOME`) and skip `$HOME` itself (`if (R !== u.home)`). Codex, opencode and github read cwd only. As a result, a `{cwd}/.agents/skills` row alone would cover `~/.agents/skills`.
- **CF3:** The sandbox hides `~/.omp/plugins/{package.json,omp-plugins.lock.json}`, which omp's `eD` needs. Any faithful model therefore sees zero plugins inside the sandbox, and a model must carry a non-omp fallback (P4) to score.
- **CF4 (process, not roots):** the counter at lane HEAD (`b9ee548`, "addendum-1 before any candidate data", 19:27:12) differs from the freeze `ecfad51`, while plan § Kill rule says "the counter … changed after this freeze" kills C1. The amendment's ordering relative to candidate data is for the L1/closure to adjudicate; I did not check it.

## 6. Residual risk and gaps
- Host-config dependence: the verdict assumes no `skills.*` keys, no opt-in providers and `CLAUDE_CONFIG_DIR` unset in the rendering session. I checked `~/.omp/agent/config.yml` (no such keys) and my own environment. I did not check the 21:55 session's environment, nor project-level omp settings under `/home/vgpnk/Projects/shokunin/.omp/`.
- Provider tie order at priority 70 (claude-plugins, agents, codex) is inferred from bundle order of the `Fe(...)` calls, not observed at runtime.
- Fixes needed before landing: rows 1, 8 and 9 should cite the code quotes in column 6. Row 9 cannot pass G4 with a code quote (CF1), so the closure should record that row 9's meaning rests on this review.

C1 roots: sound
