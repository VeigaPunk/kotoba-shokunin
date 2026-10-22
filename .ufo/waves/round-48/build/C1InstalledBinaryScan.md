# C1 source, second channel — installed opencode 1.19.3 binary strings

Seat `KotobaR48.C1InstalledBinaryScan`, round 48 build wave, 2026-10-22. Read-only on the lane;
no delegation; no web source used; no tool installed or upgraded. `opencode` executed only as
`--version`. Byte offsets below are offsets into the single installed artifact.

## Findings (observed)

1. **The npm channel ships no JS bundle.** `opencode-ai@1.19.3` installs one 186,013,824-byte
   compiled Bun ELF at `bin/opencode.exe`; the only shipped `.mjs` (`postinstall.mjs`) copies that
   binary and contains zero `skill` / `SKILL` / `skills` occurrences. All loader logic is embedded
   in the ELF as plain printable JS, so "search its shipped JS/binary strings" is a scan of the ELF.

2. **The installed loader names exactly the two configured roots in the C1 claim.** The v2 chain
   registers, per config directory entry, `path.join(configDir,"skill")` and
   `path.join(configDir,"skills")` as directory sources. `--oc-config/skill` and
   `--oc-config/skills` are therefore real skill roots in this build, and the repair's added roots
   are path-identical to the roots the binary itself constructs.

3. **The v1 chain reaches the same two roots by glob, not by join.** Its config-directory scan uses
   the brace pattern `{skill,skills}/**/SKILL.md` over `ConfigPaths.directories` =
   `[Global.Path.config, <.opencode dirs up from cwd to worktree>, ~/.opencode, OPENCODE_CONFIG_DIR]`.
   Two independent code paths in one artifact agree that both spellings are roots.

4. **`--oc-config` equals `Global.Path.config` in the harness environment.**
   `Global.Path.config = OPENCODE_CONFIG_DIR ?? join(XDG_CONFIG_HOME || ~/.config, "opencode")`,
   and the ruler's recorded environment sets `XDG_CONFIG_HOME=<arm>/home/.config` with
   `--oc-config <arm>/home/.config/opencode`. The two derivations coincide.

5. **The `directory:` token shape in the harness log is opencode's own source-key rendering.**
   `SkillV2.Source.key` renders a directory source as `` `directory:${o.path}` `` — the exact
   token the instrument's `directory:([^"\\]+)` regex and the ruler's
   `sources="[directory:ABSOLUTE_ROOT]"` fixture both use.

6. **The configured-root pattern is recursive, so the repair is deliberately narrower than the
   loader.** The glob engine is a minimatch wrapper (`GLOBSTAR = Symbol("globstar **")`), so
   `{skill,skills}/**/SKILL.md` also admits `<root>/skill/SKILL.md` and
   `<root>/skill/a/b/SKILL.md`, and the v2 per-source pattern `{*.md,**/SKILL.md}` additionally
   admits a flat `<root>/skill/<name>.md`. `oracle/config-root-cases.json` `contract.scope`
   already declares direct-child enumeration as the bounded input class and disclaims whole-loader
   parity; the binary evidence confirms that declaration is accurate and quantifies the gap.

7. **External roots are plural-only and separately gated**, matching the sibling upstream-source
   channel: `.claude` and `.agents` are scanned with `skills/**/SKILL.md` over `home` and over the
   cwd-to-stop ancestor walk, gated by `disableExternalSkills` / `disableClaudeCodeSkills`
   (`OPENCODE_DISABLE_EXTERNAL_SKILLS`, `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS`). They are not
   configured roots and are outside the C1 repair.

## Literal context lines (offset into the ELF; `…` elides unrelated bytes)

- `99142741` — `…var bA=".claude",xA=".agents",GA="skills/**/SKILL.md",SA="{skill,skills}/**/SKILL.md",KA="**/SKILL.md",MA="customize-opencode"…`
- `99145242` — `…if(!B){if(!X)Z.push(bA);Z.push(xA);for(let G of Z){let Y=y.join(z.home,G);if(!(yield*K.isDir(Y)))continue;yield*u($,Y,GA,{dot:!0,scope:"global"})}let O=yield*K.up({targets:Z,start:M,stop:T})…for(let G of O)yield*u($,G,GA,{dot:!0,scope:"project"})}let _=yield*j.directories();for(let O of _)yield*u($,O,SA);let N=yield*j.get();for(let O of N.skills?.paths??[])…yield*u($,Y,KA)}for(let O of N.skills?.urls??[])…yield*u($,Y,KA)}`
- `99144903` — `…ZA.scan(K,{cwd:J,absolute:!0,include:"file",symlink:!0,dot:z?.dot})…` (`ZA` = the minimatch-wrapper `scan`)
- `104727920` — `M=N("ConfigPaths.directories")(function*(o,t){let r=yield*T.Service;return H([A.Path.config,…!_.OPENCODE_DISABLE_PROJECT_CONFIG?yield*r.up({targets:[".opencode"],start:o,stop:t}):[],…yield*r.up({targets:[".opencode"],start:A.Path.home,stop:A.Path.home}),…_.OPENCODE_CONFIG_DIR?[_.OPENCODE_CONFIG_DIR]:[]])})`
- `104597749` — `var Ds=g({id:"config-skill",effect:n.fn(function*(o){…let c=yield*e.entries(),l=c.flatMap((s)=>s.type==="directory"?[s.path]:[]),d=c.flatMap((s)=>s.type==="document"?s.info.skills??[]:[]);for(let s of l)…`
- `104598100` — `…a.source(M.DirectorySource.make({type:"directory",path:q.make(ro.join(s,"skill"))})),a.source(M.DirectorySource.make({type:"directory",path:q.make(ro.join(s,"skills"))}));…`
- `99480131` — `…e.glob("{*.md,**/SKILL.md}",{cwd:f,absolute:!0,include:"file",symlink:!0,dot:!0})…`
- `99468698` — ``…key:(o)=>o.type==="directory"?`directory:${o.path}`:o.type==="url"?`url:${o.url}`:…``
- `105676175` — `…Y=R.XDG_CONFIG_HOME||(X?Z.join(X,".config"):void 0)…`
- `105676475` — `…var W="opencode",…Tn=H.join(Y,W)…config:Tn…`
- `105677075` — `function y(N={}){return{home:G.home,data:G.data,cache:G.cache,config:e.OPENCODE_CONFIG_DIR??G.config,…}}`
- `105784450` — `…function Q(K){return{cwd:K.cwd,absolute:K.absolute,dot:K.dot,follow:K.symlink??!1,nodir:K.include!=="all"}}async function J(K,V={}){return y0(K,Q(V))}D8.scan=J…`
- `106407337` — `…L.GLOBSTAR=Symbol("globstar **")…`
- `104668506` / `104668701` / `104668850` — shipped doc table rows: ``| Project skills | `.opencode/skill(s)/<name>/SKILL.md` |``, ``| Global skills | `~/.config/opencode/skill(s)/<name>/SKILL.md` |``, ``| External skills (auto-loaded) | `~/.claude/skills/<name>/SKILL.md`, `~/.agents/skills/<name>/SKILL.md` |``
- `104671915` / `104672077` — ``opencode's skill loader scans for `**/SKILL.md` inside skill directories``, ``.opencode/skills/my-skill/SKILL.md``
- `96896293` — `…let n=Dt.dirname(i.location),y=n,u=yield*e.find({cwd:n,pattern:"!**/SKILL.md",hidden:!0,follow:!1,…` (the `skill` tool excluding SKILL.md from its sampled file list)

## Evidence (commands, exit codes, hashes)

- `command -v opencode` → `/home/vgpnk/.local/bin/opencode`, exit 0. That file (1,460 bytes) is a bash
  wrapper resolving `opencode-ai` through `mise where node@latest` (`/home/vgpnk/.local/share/mise/installs/node/26.12.0`)
  and `npx --yes --prefer-online --package opencode-ai`. The npm-channel artifact is therefore the
  npx cache, not a global `node_modules` tree: `npm root -g` →
  `/home/vgpnk/.local/share/fnm/node-versions/v24.21.0/installation/lib/node_modules`, which holds no
  opencode package. `/home/vgpnk/.opencode/bin` does not exist (no curl-channel install).
- Install root: `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/`; cache manifest
  `/home/vgpnk/.npm/_npx/e2094862b59aac7b/package.json` pins `opencode-ai: ^1.19.3`
  (sha256 `010ba32eed9480c5aaabf3223238d5395a4927bce5933f2f4f66e5f35c521696`);
  `opencode-ai/package.json` declares `"version": "1.19.3"`, `"bin": {"opencode": "./bin/opencode.exe"}`
  (sha256 `5be8a944b51ab4d2b457885d278765595e1f7e8d68ba070c30649775f5814d53`).
- File read and scanned: `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`,
  size 186,013,824, sha256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`,
  `file` → `ELF 64-bit LSB executable, x86-64 … not stripped`. Identical sha256 for
  `opencode-linux-x64/bin/opencode` (hard link, inode 95909422) and
  `opencode-linux-x64-baseline/bin/opencode` (separate inode 95909409). The baseline copy was not
  scanned separately; hash equality is the basis for treating the scan as covering it.
- `opencode --version` → `1.19.3`, exit 0. Nothing else was executed.
- `postinstall.mjs` sha256 `5a7c990fe552e76b16422cdba3f4b0550590c7a487f7932c773362f74317c87b`;
  literal counts inside it: `skill` 0, `SKILL` 0, `skills` 0.
- Occurrence counts in the ELF: `SKILL.md` 23, `opencode/skill` 4, `skills/*` 1, `{skill,skills}` 1,
  `".claude"` 3, `".agents"` 1, `"skills/**/SKILL.md"` 1, `"{skill,skills}/**/SKILL.md"` 1,
  `"**/SKILL.md"` 1, `ro.join(s,"skill")` 1, `ro.join(s,"skills")` 1, `"{*.md,**/SKILL.md}"` 1,
  `ConfigPaths.directories` 1, `"config-skill"` 1, `OPENCODE_CONFIG_DIR` 12.
- Ruler-side environment corroboration (lane file, read only):
  `.ufo/round-48/tools/config-root-ruler.py:217-221` sets `HOME`/`XDG_CONFIG_HOME` inside the arm
  root; `.ufo/round-48/verification/before-configured-root.json` records
  `--oc-config /fast/scratch/hyaku/kotoba-r48-author-handoff/parent-before-root-matrix-01/…/home/.config/opencode`
  with `XDG_CONFIG_HOME` at `…/home/.config`. Matches finding 4.
- Access time for this report's own work: 2026-10-22T08:16Z (host clock).

## Inference (not executed, marked)

- [INFERENCE] minimatch globstar `**` matches zero or more path segments, so
  `{skill,skills}/**/SKILL.md` admits `<root>/skill/SKILL.md`. This is minimatch's documented
  behaviour and the engine is a minimatch wrapper, but no glob was executed this session; the bound
  forbids running opencode beyond `--version`.
- [INFERENCE] Both loaders are reachable in one process (v1 `@opencode/Skill` exposes
  `{get,require,all,dirs,available}`; the `tool/skill` handler calls `.list()`, which only the v2
  `@opencode/v2/Skill` service exposes), so the v2 config-skill joins are the path the `skill` tool
  reads. Which loader emits the harness's `sources="[directory:…]"` line was not determined.

## Unresolved

- No live loader run: the mapping from pattern to enumerated names is read from embedded source,
  not observed at runtime.
- The producer of the harness's `sources="[…]"` log line (opencode's own log vs the harness's
  rendering of `SkillV2.sources()`) is unidentified in this channel; only the token shape
  (`directory:<abs path>`) is confirmed to match the binary's `Source.key`.
- The v2 path does not consult `OPENCODE_CONFIG_DIR` in the config-entry list I read
  (`ct = $.make(r.config)`, which is already `OPENCODE_CONFIG_DIR ?? <xdg>/opencode`), so an
  `OPENCODE_CONFIG_DIR` distinct from the XDG config dir was not traced to its v2 directory entry.
  It is out of scope here: the ruler sets `XDG_CONFIG_HOME`, not `OPENCODE_CONFIG_DIR`.
