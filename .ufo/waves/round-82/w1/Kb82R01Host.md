# Kb82R01Host — current host installation map

Axes: freshness; operability. Read-only reconnaissance for round 82, declared base `47dbe8781657de563ff867caca6244d28e3db504`. No production gates or after-values scored; no code changes, installation, commits, clone, or delegation.

## Observed host identity (high confidence)

Commands used the installed operator binary, not commands taken from fetched content. `command -v omp` and `type -a omp` resolve only `/home/vgpnk/.local/bin/omp`; `readlink -f` returns that same path. `file -L` reports:

```text
ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked,
interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0,
BuildID[sha1]=588d7307f333293c728b74df19b7323c20736899, not stripped
```

`omp --version` returned exactly `omp/18.14.0`, command-owned exit 0.

- SHA-256: `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`
- Bytes: `276244656`
- mtime: `2026-10-29 23:19:46.168359786 -0300`
- Targeted `/home/vgpnk/.local/bin/omp*` enumeration returned `omp`, `omp-swarm`, not `omp.real`.
- `omp` is therefore the ELF itself, not a shell wrapper or symlink to `omp.real`.
- `omp-swarm` is a separate 11185-byte shell script, SHA-256 `3c95602c9888652b5fe74a97e62d94f698904a702d02e2142fe248d3ec65d946`. Its unsupported `--version` returned exit 1 (`unknown option`); it is not evidence of the omp version.
- `go version -m .../omp` returned exit 1, `not a Go executable`. Embedded `/$bunfs/root/` paths and `---- Bun! ----` identify a Bun-compiled payload, rather than evidence that a stray `rustc` or `node_modules` string identifies the application language.
- Embedded literal `--user-agent=omp/18.14.0` occurs at byte offset `276191085`, consistent with the executed version.

Disk guard status was explicitly run, exit 0, elapsed 8.12 s: scratch 47% used / 432.4G free; no heavy gate executed. No scratch was created, so no scratch cleanup was needed.

## Documented discovery roots (documentation, not a runtime coverage claim)

Sources: installed documentation accessed 2026-10-30, `omp://config-usage.md:48-125`, `omp://skills.md:85-135`, `omp://context-files.md:18-34,55-97`, and `omp://task-agent-discovery.md`.

- Generic config source order: `.omp`, `.claude`, `.codex`, `.gemini`. User bases normally `~/.omp/agent`, `~/.claude`, `~/.codex`, `~/.gemini`; project bases `<cwd>/<source>`.
- Native agent relocation: `PI_CODING_AGENT_DIR` affects default-profile native discovery, not every generic helper. `PI_CONFIG_DIR` affects generic OMP roots. Named profiles normally use `~/.omp/profiles/<name>/agent`; foreign-tool user roots are not profile-scoped. Existing XDG category directories can relocate data/state/cache independently.
- Native project context stops at the nearest non-empty ancestor `.omp`; absent `AGENTS.md` or `RULES.md` there does not resume the walk.
- Skills: ordinary provider roots enumerate `skills/<name>/SKILL.md` one level deep, not arbitrary recursive nesting. Custom-directory skills override same-named provider skills; managed skills defer to authored skills.
- Additional conventional skill roots: `~/.agent/skills`, `~/.agents/skills` and their project walk-up counterparts; Claude/Codex skill directories; `~/.config/opencode/skills` and `.opencode/skills`; project `.github/skills`. Plugin and registry sources have their own roots.
- Foreign user-level discovery is opt-in via `enabledProviders`; project roots generally remain enabled. `.agent`/`.agents` user sources and native sources default on. `disabledProviders` wins. Do not infer that every installed root was actually enabled this session.
- Task agent definitions: `~/.omp/agent/agents/*.md`, project `.omp/agents/*.md`.
- User context exceptions: Codex context is user `~/.codex/AGENTS.md`, not project `.codex/AGENTS.md`; standalone project `AGENTS.md` is a different provider.

## Embedded implementation and registration (high confidence textual evidence)

The current ELF contains source-labeled JS chunks under `packages/coding-agent/src/`. Important distinction: these are embedded source labels, not proof those filesystem paths exist locally. The bundle sometimes splits a module across repeated labels; extracting only its first label yields an import-only fragment and a false absence. The supplied artifact reconstructs every selected matching chunk.

Capability registration trace, literal fallback because LSP is unavailable:

- `capability/index.ts`, byte `172498464`: bundled `De(e,t)` looks up the capability, records provider IDs, and inserts providers by descending priority. Its loader loop invokes `g.load.bind(g)`.
- `capability/skill.ts`, byte `173411360`: bundled `Ul = bs({id: "skills", ...})`.
- `discovery/builtin.ts`, implementation chunk byte `173525517`: `Ir="native"`, priority `Wo=100`; `De(Ul.id,{id:Ir,...load:x7})`; `x7` scans project/native skills and `join(ve(),"skills")`.
- `discovery/agents.ts`, byte `173575373`: `Vo="agents"`, priority 70, roots `[".agent", ".agents"]`; `xne` scans project `w9(...,"skills")` plus user `b9(...,"skills")`. Same module registers rules, prompts, commands, context, system prompts.
- `discovery/claude.ts`, byte `173548789`: priority 80, conventional Claude skill root descriptions and scanning.
- `discovery/codex.ts`, implementation chunk byte `173590268`: `Jr="codex"`, priority 70; separate cwd `.codex` and gated user-home root helpers.
- `discovery/gemini.ts`, byte `173603464`: priority 60; context/system/settings/extensions/MCP surfaces, not a documented standalone skill provider.
- `discovery/opencode.ts`, byte `173609567`: `Mo="opencode"`, priority 55; skill loader `hre` explicitly calls `Ac(u,"opencode","skills")` and `ts(u,"opencode","skills")`. **Opencode strings and this provider remain embedded.** This does not contradict a historical removal ledger scoped to particular obsolete classes; do not reinterpret that ledger as global string absence or silently delete classes.
- `discovery/omp-plugins.ts`, byte `173625703`: priority 90; `discovery/skillshare.ts`, implementation chunk byte `173637428`: registry skill description. Installed skill docs additionally enumerate `agent-plugins`, `claude-plugins`, `github`, and managed skills.

Internal URL registration is separate from discovery-provider registration. `internal-urls/router.ts`, implementation byte `177255020`, bundled class `Se`, constructs handlers through `this.register(...)`, maintains a handler map, and exposes `getHandler`. Handler source modules include `agent-protocol.ts`, `artifact-protocol.ts`, `history-protocol.ts`, `issue-pr-protocol.ts`, `local-protocol.ts`, `omp-protocol.ts`, `proc-protocol.ts`, `rule-protocol.ts`, `skill-protocol.ts`, `ssh-protocol.ts`, `xd-protocol.ts`, `mcp-protocol.ts`, plus additional internal schemes. These embedded modules corroborate the installed documentation's separation of skills, context, capability registration, and URL resolution.

## Source checkout search and confidence limits

Embedded project/package identity: `github:can1357/oh-my-pi`, `git+https://github.com/can1357/oh-my-pi.git`, and build path `/workspace/oh-my-pi`. That build path is absent on this host.

No local source checkout was located in inspected Projects root, `~/src` (llama.cpp only), `~/go` (module cache), `~/.local/opt`, `/opt`, or targeted conventional `omp`/`oh-my-pi` locations under home, Work, and fast storage. Initial recursive Projects glob timed out; a direct directory listing replaced it. This is a bounded search, **not proof that no source checkout exists anywhere**. Consequently no checkout revision or source-to-binary parity is asserted. Embedded source and installed documentation agree on the inspected provider roots and module names; exact upstream commit equivalence remains unknown.

`read xd://lsp` reported `No such tool`; semantic definition/reference operations were unavailable. All symbol traces above are explicitly textual bundled-source evidence, not LSP semantic proof. Minified symbol spellings repeat across unrelated bundle scopes; definitions were constrained to the matching capability module before tracing callers.

One broad `strings -n 14` exploration returned truncated output and is not the evidence artifact. One overly broad regex extraction timed out at 60 s; the final bounded extraction instead uses exact module markers and byte offsets. No arbitrary bundled code was evaluated. No production after-value, checklist self-test, or 6/6 battery claim is made.

## Deliverables and hashes

- `build/Kb82R01Host-embedded.txt`: selected source-labeled provider chunks and router; SHA-256 `b037604e223735972723ef098aadc592a20773deab3f44e5fc73158acf4bcf48`.
- `build/Kb82R01Host-namespaces.json`: namespace module labels, byte offsets, chunk lengths, literal scheme assignments; SHA-256 `d40fac2a60201ff1e46818dbdf5a4a01be10c46c341d4aa38b642a056881fb89`.

No tools installed or updated. Main integration should retain the unchanged C1 counter and independently rederive/pin loader pairs against the measured ELF; these findings do not certify its target.

VERDICT: Host omp 18.14.0 is the current Bun-compiled ELF, not omp.real; documented roots and embedded registrations mapped; exact local checkout provenance unresolved.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82R01Host.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R01Host-embedded.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R01Host-namespaces.json
