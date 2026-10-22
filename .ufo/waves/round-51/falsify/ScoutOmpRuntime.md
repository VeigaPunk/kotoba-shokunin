# ScoutOmpRuntime — C1 bound probe (omp 18.12.6 shipped docs)

VERDICT: **HOLDS-BOUNDED** — C1's counter reproduces at HEAD (7 of 7, exit 0), and omp's own
shipped docs independently name loader paths for seven of the eight declared classes; the eighth
(`gemini/system.md`) is documented only by the embedded registry description, the doc page names
`SYSTEM.md`, and no runtime load of the foreign classes is exercised on this host. C1's "freshness"
therefore means *loader literals resynced to the installed binary*, not *omp loads these files*.

## Scope

The gate reads `strings` of the binary; it never runs omp (`plans/round-51.md` § Re-sizing: "Not
measured: whether omp actually loads these files at run time"). This probe asks, without a model
call, whether omp's shipped documentation confirms that the eight literals are loaders with the
inventory's paths, and records what is only extracted.

## Findings

1. **The shipped docs belong to the hash-verified binary.** `omp --version` prints `omp/18.12.6`
   (exit 0). Three running omp processes (`2750`, `3591`, `9003`) point at
   `/home/vgpnk/.local/bin/omp`, inode `95850823`, the file whose sha256 is
   `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`. The binary embeds the doc
   asset `/$bunfs/root/context-files-g5egp2as.md` and the docs manifest containing
   `context-files.md` (strings dump lines 118706, 595304, 926669). The `omp://` pages read below
   are served from that bundle — inference from the inode identity and the bundled asset path, not
   from a per-page hash.
2. **`omp --help` documents none of the eight.** Its only related flag is line 55,
   `--no-rules  Disable rules discovery and loading`; no context-file, `AGENTS.md`, `CLAUDE.md`,
   `GEMINI.md`, `SYSTEM.md` or copilot text appears. The documentation is in the `omp://` bundle
   (`context-files.md`, `system-prompt-customization.md`, `rulebook-matching-pipeline.md`,
   `settings.md`), not in the CLI help.
3. **Seven of eight are documented with the inventory's path and scope.** Code callsites below are
   from the `strings` dump of the verified binary; doc lines are from the `omp://` pages.

| class | shipped doc (line) | code callsite (strings line) | path match |
|---|---|---|---|
| `omp:agents-md/AGENTS.md` | context-files.md:78 — standalone project `AGENTS.md` walk to repo root | `bq(u, v$, "AGENTS.md")` (397439) | yes |
| `omp:claude-md/CLAUDE.md` | context-files.md:79 — standalone project `CLAUDE.md` walk | `bq(u, S$, "CLAUDE.md")` (397447) | yes |
| `omp:opencode/AGENTS.md` | context-files.md:75 — user `~/.config/opencode/AGENTS.md` only | `Kl(u, "opencode", "AGENTS.md")` (400662) | yes |
| `omp:gemini/GEMINI.md` | context-files.md:74 — user `~/.gemini/GEMINI.md`; project `<cwd>/.gemini/GEMINI.md` only | `Kl`/`Ho(u, "gemini", "GEMINI.md")` (400482, 400490) | yes |
| `omp:gemini/system.md` | none exact; system-prompt-customization.md:37 names `SYSTEM.md` and `.gemini` base | `Ho`/`Kl(u, "gemini", "system.md")` (400589, 400591) | **case gap** |
| `omp:gemini/SYSTEM_TEMPLATE.md` | system-prompt-customization.md:37 (both filenames, `.gemini` base) | `Ho`/`Kl(u, "gemini", "SYSTEM_TEMPLATE.md")` (400588, 400590) | yes |
| `omp:github/copilot-instructions.md` | context-files.md:76 — `<cwd>/.github/…`, user `~/.copilot/…` (`COPILOT_HOME`) | `Ho(u, "github", …)` (400845) + `xrt(home)` user path (400857), gated by `Mi("github", u)` (400856) | yes |
| `omp:windsurf/memories/global_rules.md` | rulebook-matching-pipeline.md:123 — user `~/.codeium/windsurf/memories/global_rules.md`, fixed rule name `global_rules`; a rule, not a context file (context-files.md:85) | `Kl(u, "windsurf", "memories/global_rules.md")` (401593), read at 401594 | yes |

4. **`gemini/system.md` is extracted-only in the doc contract.** The binary registers lowercase
   `system.md` at both scopes for the `.gemini` base; no provider registers uppercase `SYSTEM.md`
   at that base (all 8 uppercase `SYSTEM.md` callsites are native, `.agent`/`.agents`, `.claude`
   and `.codex`: strings 398336-398338, 399091/399104, 399758-399760, 400319-400321). The doc page
   states the capability, not the basename: it says "`.claude`, `.codex`, and `.gemini` project
   bases resolve at the launch cwd" (line 37) while its table names `SYSTEM.md`. On this
   case-sensitive filesystem a reader who creates `.gemini/SYSTEM.md` gets no gemini-provider
   load; `.gemini/system.md` is the literal the code reads. The registry description string ("Load
   system.md custom system prompt files", strings 400594) ships in the binary but is not the doc
   page. Code fact: high confidence. Whether the doc intends `SYSTEM.md` as the role name or the
   basename: unresolved, the page never says.
5. **The gate's shapes are real reads at the checked sites, but the check itself is presence.**
   `Ho`/`Kl` return a path and the caller reads it with `Ue(path)` (gemini 400483-400500, github
   400846-400860, windsurf 401594-401600). `bq` is the walk-up loader used by agents-md/claude-md.
   A literal match in a path-resolver call does not by itself prove a read; here the read follows
   the call. The gate does not model scopes or gates.
6. **Runtime gating bounds "loads" on this host.** `Mi()` (strings 371028-371047) implements
   `enabledProviders`: default-disabled foreign user sources return true only when the provider id
   (or `*`/`all`) is listed; `settings.md:344` says the default is empty, so Cursor, Codex, Claude,
   Gemini, OpenCode, Windsurf and GitHub **user** roots are normally excluded while project roots
   stay enabled. `~/.omp/agent/config.yml` has no `enabledProviders` key (`grep` exit 1), so this
   host loads no foreign user-level source. Host state: in the lane, only `AGENTS.md` exists among
   the declared paths; `.gemini/`, `.github/copilot-instructions.md`, `.opencode/`, `.claude/`,
   `.agent/`, `.windsurf/`, `.codex/` are absent; user `~/.omp/agent/RULES.md` exists (native
   sticky rule, not one of the eight). Seven of the eight classes are therefore never exercised by
   a session in this lane today; the eighth (`agents-md/AGENTS.md`) is present but was not traced
   loading. "Freshness" cannot mean observed runtime loading from this evidence.
7. **C1 arithmetic reproduced.** In a private clone at `59903b2` (the lane HEAD),
   `python3 -B verifiers/verify_surfaces.py --json` gives `pass 7`, `fail 0`, `exit_code 0`;
   `substrate.omp.sha256` is `85d9daf3…` from the binary path; `surfaces.literal_present` reports
   "42 loader-kind entries verified against the dumps" and `surfaces.no_uncovered_class` reports
   "all 8 extracted loader class(es) declared". The number of loader-group entries is 8, matching
   the eight classes above. Nothing in the output speaks to runtime.

## Bound on what C1 may claim

- May claim: against the installed omp 18.12.6 (sha256 `85d9daf3…`), the two omp checks pass
  (5 of 7 → 7 of 7, exit 1 → 0), and seven of the eight literals match a shipped-doc loader path.
- May not claim: that omp loads these files in a session. No model-free runtime observation was
  made; four user-level scopes are gated off by an empty `enabledProviders` on this host; no
  project-level declared file except `AGENTS.md` exists in the lane.
- The `gemini/system.md` case divergence is a freshness artifact: the gate tracked the code
  literal while the doc page names a different case. A future binary that renames the literal
  would still pass `literal_present` if a doc-shaped call is present; the doc/code mismatch would
  persist silently.

## Remaining unknowns

- Whether `SYSTEM.md` in system-prompt-customization.md means the role or the basename; the page
  never states the lowercase `.gemini/system.md` filename.
- Whether `/extensions` (interactive) would list any of the eight as loaded; not run.
- Whether a project-level `.gemini/system.md` actually reaches the prompt; the code reads it
  (`kind: "text"`), but no session was started to observe injection.

## Evidence (commands, exit codes)

- `omp --version` → `omp/18.12.6`, exit 0.
- `omp --help | grep -n -- '--no-rules'` → line 55, `--no-rules  Disable rules discovery and loading`, exit 0; no other instruction-file flag.
- `for d in /proc/[0-9]*; do readlink $d/exe; done` → pids `2750`, `3591`, `9003` are `/home/vgpnk/.local/bin/omp`; `stat -Lc %i` on each and on the file → `95850823`.
- `strings -n 12 /home/vgpnk/.local/bin/omp > omp.strings; wc -l` → `927686 omp.strings`, exit 0; `grep -Fn '/$bunfs/root/context-files-' omp.strings` → lines 118706, 595304, 926669.
- `grep -Fn 'return bq(u,' omp.strings` → 397439 (`AGENTS.md`), 397447 (`CLAUDE.md`); `grep -Fn '"GEMINI.md"'` → 400482, 400490; `grep -Fn '"system.md"'` → 400589, 400591; `grep -Fn 'copilot-instructions.md'` → 400845-400970; `grep -Fn 'memories/global_rules.md'` → 401593-401600.
- `grep -n enabledProviders /home/vgpnk/.omp/agent/config.yml` → exit 1 (key absent).
- `git clone -q <lane> lane && git -C lane checkout -q 59903b2… && git -C lane rev-parse --short HEAD` → `59903b2`, exit 0.
- `python3 -B lane/verifiers/verify_surfaces.py --json` → `pass 7`, `fail 0`, `exit_code 0`, `substrate.omp.sha256 85d9daf3…`, exit 0.

## Tool installs

None.

## Probe disclosure

`omp docs` is not a registered subcommand (cli-reference.md lists no `docs`); it routed to launch,
printed `Working...`, and was backgrounded as `bg_10017`. I cancelled it immediately; no model
output was received. No other command could start a model call.
