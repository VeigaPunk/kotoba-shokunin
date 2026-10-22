Result: DONE — on omp 18.12.6 the always-on (AGENTS.md-class) set is chosen by ten priority-ordered discovery providers, not by a filename list; a standalone `AGENTS.md` and `CLAUDE.md` in one directory collide on one key at equal priority 10 and `AGENTS.md` wins by registration order; a `CLAUDE.md` `@AGENTS.md` import and a `CLAUDE.md → AGENTS.md` symlink are both honoured.

# Scout — omp 18.12.6 always-on file names, order, and the both-files case

Seat: `KotobaR53.ScoutOmpAlwaysOn` (leaf, no dispatch, no model calls). Lane checkout read-only at
`e78dff66`; sandbox clone at plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` under
`/fast/scratch/hyaku/kotoba-r53/ScoutOmpAlwaysOn/repo`. No lane file touched; this report is the only write.

## Substrate, and exactly what was measured

| Item | Value |
|---|---|
| Binary | `/home/vgpnk/.local/bin/omp`, 256,702,432 B, `sha256 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4` (matches the `85d9daf3…` pin in `plans/round-53.md` C1) |
| Self-report | `omp --version` → `omp/18.12.6`, exit 0 |
| Strings dump | `LC_ALL=C strings -n 4 omp-18.12.6.bin > omp-18.12.6.str4.txt` — 2,444,467 lines, 48,148,449 B, `sha256 953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f` |
| Agent dir | `omp config path` → `/home/vgpnk/.omp/agent`, exit 0 |
| Settings | `omp config list --json` → 559 keys; `enabledProviders=[]`, `disabledProviders=[]`, `contextFiles.extra=[]` |
| Shipped docs | `omp://context-files.md` and `omp://system-prompt-customization.md`, served by the same installed build (the markdown is an embedded compressed asset: `/$bunfs/root/context-files-g5egp2as.md`, dump 524267) |
| Source on disk | **none** — `find /home/vgpnk -maxdepth 4 -type d -name 'oh-my-pi*'` and a `.npm` search for `pi-coding-agent` both return nothing; the binary is the only readable source |
| External fetches | none this seat; no SOURCES row is owed by this report |

**Line numbers are this dump's** (`strings -n 4`, one candidate per line). The census's round-13 numbers come
from a different extractor and do not transfer; every claim below also carries the literal so it can be
re-found after a dump change.

`strings` cannot see the docs' prose (they are a compressed asset), so doc quotes below are from
`omp://context-files.md` / `omp://system-prompt-customization.md` by section name, and code quotes are from
the dump.

## 1. The loader is a capability table, not a name list

There is no ordered name array (that is opencode's model, not omp's). Context files are a **capability**
whose items are deduplicated by a scope key, fed by providers registered with a numeric priority.

Dump 892543-892549 — the capability and its key:

```
892543: var Tl = Zo({
892544:   id: "context-files",
892545:   displayName: "Context Files",
892546:   description: "Persistent instruction files (CLAUDE.md, AGENTS.md, etc.) that guide agent behavior",
892547:   key: (u) => {
892548:     const p = u.level === "user" ? "user" : `project:${Math.max(0, u.depth ?? 0)}`;
892549:     return u.additive ? `${p}:additive:${ey.resolve(u.path)}` : p;
```

Consequences of that one function: exactly **one user-level context file** total (`user`), exactly **one
project file per directory depth** (`project:<depth>`), and `additive` items (only `custom-context`) sit
outside the slot with their own path key. No `equivalent` hook exists on this capability, so the key is the
whole dedupe rule.

Dump 862468-862473 — registration inserts by descending priority, and inserts **after** equals because the
scan is for a *strictly* lower priority:

```
862468:   const r = n.providers;
862469:   const s = r.findIndex((o) => o.priority < t.priority);
862470:   if (s === -1) {
862471:     r.push(t);
862472:   } else {
862473:     r.splice(s, 0, t);
```

Dump 862558-862564 — first item to claim a key keeps it, later ones are marked shadowed:

```
862558:     const v = u.has(k);
862559:     u.add(k);
862560:     const R = !v && b !== undefined && p.some((x) => !a.has(x) && b(x, f));
862561:     if (v || R) {
862562:       f._shadowed = true;
862563:     } else {
862564:       p.push(f);
```

So: **selection order = descending provider priority; ties = registration order (first registered = first in
the array = wins the slot).** A shadowed item is not injected; `/extensions` lists it as `shadowed`
(dump 1132506-1132510: `if (l)` → `return { state: "shadowed", disabledReason: "shadowed" };`).

## 2. The ten providers that contribute context files (all ten registrations on this binary)

`grep -c 'Le(Tl\.id' → 10`. There is no eleventh. Names, scope and priority as read from each registration;
the priority variable's value is quoted from its own definition line.

| # | provider id | literal(s) it can read | scope | priority | registration (dump) | authority for the priority |
|---|---|---|---|---|---:|---|
| 1 | `native` | `AGENTS.md` | user (`<agent dir>/AGENTS.md`) + project (`<nearest non-empty .omp>/AGENTS.md`) | 100 | 897183-897188 | `var _o = 100;` 896508 |
| 2 | `claude` | `CLAUDE.md` | user (`~/.claude/CLAUDE.md`, opt-in) + project (`<cwd>/.claude/CLAUDE.md`) | 80 | 897658-897663 | `var Qa = 80;` 897289 |
| 3 | `agents` | `AGENTS.md` | user (`~/.agent/`, `~/.agents/`) + project walk (`.agent`/`.agents` per ancestor) | 70 | 898419-898424 | `var Pu = 70;` 898256 |
| 4 | `codex` | `AGENTS.md` | user only (`~/.codex/AGENTS.md`) | 70 | 899067-899072 | `var ca = 70;` 898765 |
| 5 | `gemini` | `GEMINI.md` (also `system.md`, `SYSTEM_TEMPLATE.md` via the system-prompt capability) | user + `<cwd>/.gemini/` | 60 | 899443-899448 | `var Au = 60;` 899271 |
| 6 | `opencode` | `AGENTS.md` | user only (`~/.config/opencode/AGENTS.md`) | 55 | 899751-899756 | `var $u = 55;` 899494 |
| 7 | `github` | `copilot-instructions.md`, plus `AGENTS.md` from `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` | user (`~/.copilot/`) + `<cwd>/.github/` | 30 | 899943-899948 | `var xm = 30;` 899791 |
| 8 | `agents-md` | `AGENTS.md` | project walk only | 10 | 895597-895602 | inline `priority: 10,` 895601 |
| 9 | `claude-md` | `CLAUDE.md` | project walk only | 10 | 895608-895613 | inline `priority: 10,` 895612 |
| 10 | `custom-context` | any basename in `contextFiles.extra` (e.g. `AGENTS.local.md`) | user (`<agent dir>/<name>`) + project walk + primary checkout of a linked worktree | 9 | 896357-896362 | inline `priority: 9,` 896361 |

Registration literals, verbatim (each ≤300 chars):

```
895592: // packages/coding-agent/src/discovery/agents-md.ts
895594: var _7 = "AGENTS.md";
895596:   return bq(u, v$, "AGENTS.md");
895600:   description: "Standalone AGENTS.md files (Codex/Gemini style)",
895601:   priority: 10,
895603: // packages/coding-agent/src/discovery/claude-md.ts
895605: var I7 = "CLAUDE.md";
895607:   return bq(u, S$, "CLAUDE.md");
895611:   description: "Standalone CLAUDE.md files (Claude Code style)",
895612:   priority: 10,
897186:   description: "Load AGENTS.md from .omp/ directories",
897661:   description: "Load CLAUDE.md files from .claude/ directories",
898422:   description: "Load AGENTS.md from .agent and .agents (project walk-up + user home)",
898424:   load: wte
899070:   description: "Load context files from ~/.codex/AGENTS.md (user-level only)",
899446:   description: "Load GEMINI.md context files",
899754:   description: "Load AGENTS.md from ~/.config/opencode/",
899946:   description: "Load copilot-instructions.md from .github/ and ~/.copilot/; AGENTS.md from COPILOT_CUSTOM_INSTRUCTIONS_DIRS",
896360:   description: "Extra context filenames from contextFiles.extra (additive; does not replace AGENTS.md)",
```

The shipped doc lists the same ten contributors and the same full priority registry, and names the providers
that contribute **no** context files — `cursor`, `windsurf`, `cline`, `vscode`, `mcp-json`, `claude-plugins`,
`omp-plugins`, `agent-plugins`, `ssh-json`, `builtin-defaults` (`omp://context-files.md`
§ Other supported context conventions). Code agrees: `grep -c 'Le(Ws\.id' → 9` — cursor (899255), windsurf
(900733), cline (898246) and `.github/instructions` (899955) register **rules**, not context files. So
`.cursorrules`, `.windsurfrules` and `.clinerules` are always-on rule text but never occupy an AGENTS.md slot;
the census's `omp:cursor/rules` / `omp:windsurf/rules` / `omp:clinerules/.clinerules` rows are right about the
literal and belong to that other capability.

In one line, the always-on **context-file** names this build reads are: `AGENTS.md` (native `.omp` user +
project, `.agent`/`.agents` user + project walk, `~/.codex/` user, `~/.config/opencode/` user, standalone
project walk, and `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`), `CLAUDE.md` (`.claude/` user + cwd, standalone project
walk), `GEMINI.md` (`.gemini/` user + cwd), `copilot-instructions.md` (`.github/` cwd + `~/.copilot/`), and any
basename listed in `contextFiles.extra`. Adjacent always-on files that are **not** context files: `RULES.md`
(native only, loaded as an always-apply sticky rule, § Sticky rules vs normal context), `SYSTEM.md` /
`SYSTEM_TEMPLATE.md` (system-prompt capability `Ry`, 892709-892715), `APPEND_SYSTEM.md` / `PERSONALITY.md` /
`TITLE_SYSTEM.md`, and the rules capability `Ws` (862929-862933) fed by `.cursor/rules`, `.windsurfrules`,
`.clinerules`, `.agent(s)/rules` and `.github/instructions/**/*.instructions.md`.

The walk itself (standalone classes 8 and 9) is `bq`, dump 863364-863398: resolve boundary, then from cwd
upward, skip a file whose **parent directory name starts with `.`**, depth = separator distance from cwd:

```
863379:   while (true) {
863380:     const v = ee(k, p);
863381:     const R = f && ee(k, o);
863382:     if (!(R || v && !b)) {
863383:       const C = c.join(k, n);
863384:       const j = await Ue(C);
863385:       if (j !== null && j !== "") {
863386:         const U = c.dirname(C);
863387:         const D = U.split(c.sep).pop() ?? "";
863388:         if (!D.startsWith(".")) {
863389:           const Ee = c.dirname(C);
863390:           const Ae = Gw(a, Ee, c.sep);
863391:           r.push({
863392:             path: C,
863393:             content: j,
863394:             level: "project",
863395:             depth: Ae,
863396:             _source: Ze(t, C, "project")
863397:           });
863398:         }
```

`native`'s project file is *not* produced by that walk: it uses `cR`, the nearest non-empty `.omp` ancestor,
and inherits the **ancestor's** depth (896559 `return { dir: R, depth: p.depth };`), which is why a
`.omp/AGENTS.md` lands in the same slot as the `AGENTS.md` beside it. Codex is user-only (899067-899072);
opencode is user-only (899751-899756); gemini and github are cwd-config only, no ancestor walk
(`Ho(u,t,n)` = `join(u.cwd, SO[t].projectDir, n)`, 863062-863066).

User-level foreign bases are **opt-in**: `Kl(e,t,n)` returns `null` unless `Mi(t,e)` (863058-863061), and
`Mi` admits only providers outside the opt-in set, or ones listed in `enabledProviders` / `*` / `all`
(862609-862626); the opt-in set is `cursor, codex, claude, claude-plugins, gemini, opencode, windsurf,
github` (862432-862441). Project-level paths are never gated. `agents-md`, `claude-md`, `native`, `agents` and
`custom-context` are outside the set, so those user/project sources load unconditionally.

## 3. What happens when `AGENTS.md` and `CLAUDE.md` both exist in one directory

`claude-md` and `agents-md` are the two providers that read those two names from an arbitrary project
directory, and they hold **the same priority, 10** (895601, 895612). Same name-free key: both go through `bq`,
so both land on `project:<depth>` for that directory. One of them must lose.

Mechanism, in three observed steps:

1. `Le` inserts a provider before the first **strictly** lower priority, i.e. **after** an equal one
   (862469-862473, quoted above). Equal priority therefore keeps registration order.
2. The two registrations are contiguous module bodies in one bundle region, `agents-md.ts` first
   (895592-895602) and `claude-md.ts` second (895603-895613), with no chunk boundary or import block between
   them; their `Le` calls are top-level module side effects. [INFERENCE] bundle text order is module execution
   order here, so `agents-md` is earlier in the provider array.
3. `$e` iterates that array in order and first key claim wins (862558-862564).

**Therefore: `AGENTS.md` wins, `CLAUDE.md` is marked `_shadowed` and is not injected at that depth.**
Confidence: high on the mechanism (two independent reads: the insertion rule and the first-wins loop, plus the
shipped doc's own prose order "`native` > `claude` > `agents/codex` > `gemini` > `opencode` > `github` >
`agents-md` > `claude-md`", § The wrong file wins); **[INFERENCE]** only on the tie direction, because the
doc's table prints 10 and 10 without stating the tie-break and no runtime state was read (no session run —
bounds forbid it).

Related cases, same rule, and each one is documented or code-visible:

- `.claude/CLAUDE.md` (provider `claude`, 80) **beats** a standalone `AGENTS.md` (10) at the same depth. The
  doc says so outright ("In a project holding both `.claude/CLAUDE.md` and `AGENTS.md`, `CLAUDE.md` normally
  wins the depth-0 scope", § Disabling a single context file) and `pm(u)` is `join(u.cwd, ".claude")`
  (897301-897303), depth 0. So "CLAUDE.md beats AGENTS.md" is true only for the config-directory file; it is
  false for the standalone pair.
- `.omp/AGENTS.md` (100) beats both at that depth, and the doc confirms the native winner also swallows
  `RULES.md` selection for that `.omp` directory.
- Empty files contribute nothing (`bq` requires `j !== ""`, 863385), so an empty `AGENTS.md` does not hold the
  slot; a non-empty `CLAUDE.md` beside it takes the depth.
- `disabledProviders: [agents-md]` moves the slot to `CLAUDE.md` rather than emptying it (doc § Disabling a
  single context file: "a disabled file is dropped before deduplication … The file it used to shadow is loaded
  in its place"). `disabledExtensions` is the per-file switch: `context-file:<user|project>:<basename>`,
  matched on level + basename only, so `context-file:project:AGENTS.md` disables it at **every** depth.

## 4. Order the loaded files reach the prompt in

Two sorts and one collapse, all in `Hxe` (the prompt's context-file loader) and `L`:

Dump 1069413-1069420 — user file first, then farther ancestors, then closer; then paragraph-containment
collapse keeping the later copy:

```
1069413: function L(t) {
1069414:   const o = [...t].sort((n, a) => {
1069415:     const r = n.depth ?? Number.POSITIVE_INFINITY;
1069416:     const c = a.depth ?? Number.POSITIVE_INFINITY;
1069417:     return c - r;
1069418:   });
1069419:   const s = o.map((n) => Z(n.content));
1069420:   return o.filter((n, a) => !s.some((r, c) => c > a && Ce(r, s[a])));
```

Dump 1069427-1069440 — every surviving item is `@`-expanded before ordering, and the redundant pre-sort runs
descending by depth with `undefined` treated as `-1`:

```
1069427:   const n = await Promise.all(s.items.map(async (a) => {
1069428:     const r = a;
1069429:     return {
1069430:       path: r.path,
1069431:       content: await TM(r.content, r.path),
1069432:       depth: r.depth
1069433:     };
1069434:   }));
1069435:   n.sort((a, r) => {
1069436:     const c = a.depth ?? -1;
1069437:     const m = r.depth ?? -1;
1069438:     return m - c;
1069439:   });
1069440:   return L(n);
```

So the injected sequence is: **the surviving user-level file, then the deepest (repository-root-most) project
ancestor, …, then the cwd's own file last.** This matches the doc's closing sentence: "Final injection order
is **the surviving user-scope file first**, then farther project ancestors, then project files closer to the
cwd." `L`'s containment filter removes an earlier item whose normalized paragraph sequence is contained in a
later one (`c > a`), which is why an identical copy (symlink, or a verbatim `@` import) arrives once, from the
inner file.

Injection site: the prompt builder awaits `Hxe` and hands the array to the template as `contextFiles`
(1069643-1069644 `w("loadProjectContextFiles", st, P.contextFiles).then(L)`; 1069728 `contextFiles: de`),
which the doc renders as one `<repo-rules>` block of `<file path="…">` elements inside the trailing
`<project-context>` block (`omp://context-files.md` § Injection behavior). The block form is live in this
build: the renderer strips `<repo-rules>` blocks during compaction (dump 1072394
`/<repo-rules>\n[\s\S]*?\n<\/repo-rules>/g,`) and the template asset is
`/$bunfs/root/project-prompt-hmr4vt9d.md` (1069255).

## 5. Is a `CLAUDE.md` `@AGENTS.md` import honoured? — **yes**

Imports are expanded for **every** discovered context file, before dedupe and before the containment collapse
(1069431). The module is literally `discovery/at-imports.ts` (1009117).

Dump 1009120-1009123 and 1009129-1009131:

```
1009117: // packages/coding-agent/src/discovery/at-imports.ts
1009118: import * as x from "os";
1009119: import * as g from "path";
1009120: var rNt = 5;
1009121: var w = /(^|[ \t])@([./~A-Za-z0-9_-](?:\\ |[^\s])*)/g;
1009122: var S = /[.,;:!?)\]}"']+$/;
1009123: async function TM(t, r, e = {}) {
…
1009129: async function b(t, r, e, n, o, c) {
1009130:   if (e >= n)
1009131:     return t;
```

Dump 1009176-1009186 — resolve, cycle skip, missing target leaves the token:

```
1009176: async function I(t, r, e, n, o, c) {
1009177:   const s = T(t, r, o);
1009178:   if (c.has(s)) {
1009179:     l("@-import: skipping cyclic include", { path: s });
1009180:     return null;
1009181:   const i = await Ue(s);
1009182:   if (i === null) {
1009183:     l("@-import: file not found", { path: s });
1009184:     return null;
1009185:   c.add(s);
1009186:   return await b(i, g.dirname(s), e + 1, n, o, c);
```

Dump 1009135-1009156 — code blocks are copied through untouched, then the per-line scanner:

```
1009135:     if (u.kind === "code") {
1009136:       i.push(u.text);
1009137:       continue;
1009138:     }
1009139:     i.push(await k(u.text, r, e, n, o, c));
1009140:   return i.join("");
1009141: async function k(t, r, e, n, o, c) {
1009142:   const s = t.split(`
1009143:   for (let i = 0;i < s.length; i++) {
1009144:     s[i] = await A(s[i], r, e, n, o, c);
1009145:   return s.join(`
1009146: async function A(t, r, e, n, o, c) {
1009147:   if (!t.includes("@"))
1009148:     return t;
1009149:   const s = [];
1009150:   for (const a of t.matchAll(w)) {
1009151:     const f = a.index ?? 0;
1009152:     const h = a[1];
1009153:     const m = a[2];
1009154:     const p = f + h.length;
1009155:     if (M(t, p))
1009156:       continue;
```

Behaviour, all four sources agreeing (regex, `T`, `Ue`, `omp://context-files.md` § `@` imports):

- a token counts only when `@` is at line start or after a space/tab — so `git@github.com:…` and
  `user@example.com` are never imports;
- relative paths resolve from **the importing file's directory**, `~/` from home, absolute as-is;
- trailing `.,;:!?)]}"'` is trimmed, so `@AGENTS.md.` imports `AGENTS.md`;
- nested expansion stops after 5 hops (`rNt = 5`), repeats/cycles are skipped and left literal, a missing
  target leaves the `@token` text in place, and fenced/inline code is untouched.

Direct answer for the alwayson.07 form: put `@AGENTS.md` in a `CLAUDE.md` and omp inlines `AGENTS.md`'s bytes
into the `CLAUDE.md` item. Note the practical corollary: when both files exist in the same directory, the
`CLAUDE.md` item loses the depth slot anyway (§3), so the import is only *necessary* when `CLAUDE.md` is the
only rule file present (or `agents-md` is disabled) and it needs to pull a file that is not a context-file
candidate, or one from another directory. The doc also warns that `@`-imported text is not filtered by the
subagent `agents.md` drop (system-prompt-customization § Inputs by session type, note 1).

## 6. Is a symlink honoured? — **yes** (code-read; not exercised)

The reader follows links and has no symlink branch:

Dump 862121-862132 — `stat` (follows), then read the path:

```
862121: async function Ue(e) {
862122:   const t = z(e);
862123:   if (M.has(t)) {
862124:     return M.get(t) ?? null;
862125:   try {
862126:     const n = await ie.promises.stat(t);
862127:     if (!n.isFile()) {
862128:       M.set(t, null);
862129:       return null;
862130:     }
862131:     const r = await Bun.file(t).text();
862132:     M.set(t, r);
862133:     return r;
862134:   } catch {
862135:     M.set(t, null);
862136:     return null;
```

Supporting facts: the discovery region contains **no** `lstat` and **no** `realpath` on context-file paths —
the only `lstat`/`realpath` hits in 862000-901000 are plugin lockfile/stale-entry and installed-plugin-root
code (895045, 895390-895395); the cache key is `path.resolve`, not `realpath` (862119-862122); the walk never
lists directories, it just tries the joined path (863383-863384). The shipped doc says nothing about
symlinks, and the embedded changelog has **zero** `AGENTS.md` / `CLAUDE.md` mentions in 2423282-2444467
(`# Changelog` at 2423282 starts at `## [18.12.6] - 2026-10-21`), so there is no documented special case
either way.

Reading, therefore: a `CLAUDE.md` that is a symlink to `AGENTS.md` contributes that file's bytes under the
`CLAUDE.md` id; when both names exist at one depth the slot still goes to the real `AGENTS.md` (§3), so the
kimi-code-style link is redundant but harmless; a `CLAUDE.md` symlink pointing anywhere else is read normally.
[INFERENCE] the final step only — `Bun.file(path).text()` follows a symlink on Linux; `stat` (which already
follows) is what admits the file.

Unrun falsifier for wave 2 (needs a sanctioned session/probe, not this seat): a scratch dir with
`AGENTS.md` + `CLAUDE.md` (a) as a symlink and (b) carrying `@AGENTS.md`, then read `/extensions` — it prints
each discovered context file with level, source and state, so it shows `shadowed` vs `active` and whether the
link was read.

## 7. Live host consequence (observation, not the claim)

On this host none of the foreign user bases exist and none is opted in, so the user slot resolves without
them: `ls` of `~/.omp/agent/AGENTS.md`, `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`,
`~/.config/opencode/AGENTS.md` → all "No such file or directory" (exit 2); `~/.agents/AGENTS.md` exists
(949 B, 2026-10-20 09:18). By §2's priorities the surviving user-level context file is therefore
`~/.agents/AGENTS.md` (provider `agents`, 70, ungated). `contextFiles.extra` is `[]`, so nothing additive.
`--no-rules` does **not** touch this surface: it sets `R.rules = []` (dump 1201581-1201582), while context
files are discovered by the separate `context-files` capability and rendered from `contextFiles`.

Adjacent and **unresolved** (not this seat's question; flagged because it bears on C2's population): the
shipped doc places the user append file at `<agent dir>/APPEND_SYSTEM.md` (`~/.omp/agent/APPEND_SYSTEM.md`,
system-prompt-customization § Recipes) and the shared user-base table resolves native to
`~/.omp/agent` (`Bmt()` = `${nh()}/agent`, dump 644600-644602; `gL` at 893095-893100). The host's file sits at
`~/.omp/APPEND_SYSTEM.md`, i.e. one directory above that base. `ScoutAlwaysOnPop.md` § 5 records that block
as reaching a session prompt; this session's prompt does not contain that text. Two readings are possible
(the base is broader than the doc says, or the block in that session came from another route such as a task
prompt); settling it needs a `/extensions` or `/context` reading, not strings.

## Census reconciliation (short)

- § A's omp rows hold on 18.12.6: the registration in this build is `Le(Tl.id, { id, priority, load })` and
  the shared loader is `bq(u, <provider id>, "<name>")`; the census's callee names (`Id|Cl|jD[ef]`,
  `Tl|dr|GW`) no longer describe it, which the census itself already flagged as expected. Literals unchanged,
  and of the descriptions the only overstatement I can falsify is the native base name (description says
  `~/.omp`; the code and the doc say `~/.omp/agent`).
- § A2's model — "capability table sorted by descending priority, merged with first-wins dedupe by `key()`" —
  is **confirmed** on this binary (862469-862473, 862558-862564), with one addition the census omitted:
  `custom-context` at priority 9 with an `additive` key, so extra filenames never take or shadow a slot.
- § A2 also listed cursor/windsurf/cline in the priority ladder; on this binary they are rules-only providers
  and cannot win a context-file slot.
- Census line numbers are not reusable (different extraction); its rule "anchors are literals, never offsets"
  still governs long-term bookkeeping — the dump numbers here are this seat's measurement, not a new anchor
  policy.

## Confidence and remaining unknowns

| Statement | Confidence | Basis |
|---|---|---|
| Ten context-file providers, these names, these priorities | observed | 10 `Le(Tl.id` registrations + doc table, identical |
| One user file, one project file per depth | observed | `key()` 892547-892549; doc § Load order and shadowing |
| Selection order = priority, ties = registration order | observed (mechanics) | 862469-862473 + 862558-862564 |
| `AGENTS.md` beats `CLAUDE.md` at equal depth | [INFERENCE] | tie mechanics plus contiguous module order 895592-895613; the doc prints 10/10 and states no tie-break; not exercised at runtime |
| Final prompt order user → farthest → closest | observed | 1069413-1069420, 1069435-1069440; doc agrees |
| `@AGENTS.md` honoured inside `CLAUDE.md` | observed | `at-imports.ts` 1009117-1009186; applied to every item at 1069431; doc § `@` imports |
| Symlink honoured | high, final step [INFERENCE] | `stat` + no `lstat`/`realpath` gate, 862121-862132 |
| Exact `<repo-rules>` rendering in this session's own prompt | unknown | code strips the block (1072394) and the doc specifies it; the prompt text visible to this seat shows a bare `<file path="AGENTS.md">` form, and the asset is compressed so the prose cannot be diffed from strings |
| Whether a task subagent inherits these files | observed in doc only | system-prompt-customization § Inputs by session type: inherited except basenames `agents.md` (case-insensitive); not verified against a live subagent here |
