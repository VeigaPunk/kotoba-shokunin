# Bounds (binding on every seat)
- Message target: only agent://KotobaR57 (your L1). Never agent://all. Seats are leaves: no task spawns, no swarms (an executor may spawn at most one read-only labrat probe).
- Write ONLY your own report file (executors: also the patch/receipt files their item names, inside your scratch dir or the report dir). Every `Report:` trailer path is relative to /home/vgpnk/Projects/shokunin/kotoba-shokunin — write it at /home/vgpnk/Projects/shokunin/kotoba-shokunin/<that path>. Never write anything else in the lane, never in the fleet root /home/vgpnk/Projects/shokunin, never in a sibling lane. Never edit lane files: you deliver text or a patch; the L1 integrates.
- Anything that writes or executes lane code (self-tests, probes, mutated copies, counters, sandbox worlds) runs in your OWN sandbox clone: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57/<YourSeatName> && git -C /fast/scratch/hyaku/kotoba-r57/<YourSeatName> checkout -q <the revision your item names>`; scratch files under /fast/scratch/hyaku/kotoba-r57/<YourSeatName>/ only. Git writes (sandbox commits) are allowed only inside that clone; every sandbox commit hash you cite is labelled `sandbox <hash> (/fast/scratch/hyaku/kotoba-r57/<YourSeatName>)`, never cited bare. Never push.
- Never run git writes (add, commit, stash, checkout, switch, reset, pull, push, worktree) in the lane, and never mutate lane jj state or the lane Git index. Read-only git in the lane is fine (prefer `git --no-optional-locks`). jj only read-only with --ignore-working-copy, in the lane only; never any git or jj command with the fleet root /home/vgpnk/Projects/shokunin as cwd. Never mutate the fleet repo, sibling lanes, MANIFEST.json, .ufo/state or .ufo/watchdog.log.
- Process hygiene (round-56 lesson M56): cap every run you start with `timeout` (at most 900 s per command); no unbounded recursive test runs. Kill only by the PIDs you started (record `$!` or use `timeout`), never with `pkill -f`/`killall` or any pattern over a shared path such as /fast/scratch/hyaku/. Contention or load tests: at most 4 concurrent processes and 120 s wall time, and only when your item asks for one; the host is shared by many lanes.
- Sources are opened by ordinary means only (curl, the read tool, web search). Never use a headless browser or any tool to pass a bot challenge, captcha or access control. Record URL, UTC access time (paste the `date -u` line), HTTP status, byte count and sha256 of what you fetched; quote verbatim (at most 25 words per quote, byte-exact; if you strip markdown say exactly which bytes) with line numbers in the fetched bytes. Prefer a quote that needs no shaping. Before recording that a client documents nothing about a topic (Q30), open its changelog or release notes AND its current docs source tree AND grep the lane corpus; a sweep missing any of the three makes the client `not checked`, never `silent`.
- Never make paid model calls through any client CLI (no `claude -p`, `codex exec`, `opencode run`, `gemini -p`); version, help, debug and config introspection only.
- Never pass a `model` parameter; never call `ask`.
- Tooling: you and every seat may install or upgrade tools that help the task — read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate, record tool/version/channel/reason in your report). Pacman guard: all pacman transactions are PAUSED host-wide (install via uv tool, npx or an official binary in ~/.local/bin, or report the need); never -Sy, -Syu, -U, -R, downgrade, or restart a host service.
- Honesty: an unrun check has not passed; paste commands with exit codes and observed output; mark inference as [INFERENCE]. A record states only what was verified; a statement may say no more than its evidence. Plain English.
- Report shape: first line `Result: DONE|PARTIAL|BLOCKED|HOLDS|BREAKS|MIXED — <one sentence>`; then findings with evidence pointers (path:line, command + exit code + output).

# Tooling directive — operator, 2026-10-19 (always on, every agent)

Any agent — main session or subagent, any lane, any wave — installs or updates any tool that
helps its task or is a strict upgrade, with full privilege, without asking first. Passwordless
`sudo` is available.

- Channel order: `sudo pacman -S --needed --noconfirm <pkg>` → `uv tool install <pkg>` →
  official release binary into `~/.local/bin` → `cargo install` / `npm -g`. Official sources
  only; never pipe an unverified remote script into a shell.
- Full-system upgrades (`pacman -Syu`) go through tsukuroi-shokunin's update-safety gate first:
  boot-chain packages can break boot (mkinitcpio 42 moves root to `/sysroot`; the host's
  `btrfs-overlayfs` and `plymouth` hooks still expect `/new_root`). Never run a partial upgrade
  (`pacman -Sy <pkg>`). If an install fails on a stale sync database, report it.
- Record every install or update — tool, version, channel, reason — in your report or handoff.
