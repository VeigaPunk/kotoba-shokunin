# r86-w1 Sentinel report

Full audit: `.ufo/waves/round-86/w1/Sentinel/audit.md`. Receipts: `.ufo/waves/round-86/w1/Sentinel/receipts/`.

- **S5 (High, open): C1 fail-open in G4 (counter b9ee548).** `guard_g4` fnmatches the unresolved
  reported root, and fnmatch's `*` matches across `/` and `..`. The candidate's row
  `~/.omp/plugins/node_modules/*/skills` therefore also accepts
  `~/.omp/plugins/node_modules/../../../.zcode/…/skills`, a zcode copy that omp does not read. I
  scored the candidate's files with that one `USER_ROOTS` line changed: `215 of 215`, G1–G4 PASS,
  exit 0 (`g4-launder-world.txt`). Separately, `{cwd}/` expands to every ancestor, so the opt-in
  `~/.claude/skills` and `~/.codex/skills` pass too (`g4-pattern-probe.txt`).
- **S4 (High, open): `/run/docker.sock` is reachable from the amended sandbox.** connect() returns OK,
  and the user is in the `docker` group. The system D-Bus socket is also reachable. A module could use
  Docker to start a container with the host `/` mounted and write anywhere (inferred, not executed).
  Fix: `--tmpfs /run`, or an allowlist sandbox.
- **S1–S3 (High/Medium): fixed by addendum-1.** These were raised by this seat against ecfad51: the
  `~/.omp/logs` http-400 dumps held 215/215 renders and were visible; host network, the full
  environment (3 token-named vars) and `/run/user` sockets were visible; a `setsid` grandchild
  outlived bwrap. On b9ee548 the probe shows `lo` only, 4 env vars, pid ns of 2, no orphan, and no
  visible copy of an LLM-hint render (an in-sandbox scan of 1.25 M files).
- **S6 (Low):** a `TimeoutExpired` ends at exit 1 where the exit ladder wants 2. It fails closed.
- **Fixture:** no credential shapes. The only private paths are the session file and cwd. Every
  string is at most 116 chars, and I see no redistribution concern.
- **Candidate 903bd78:** it adds import-time reads of `~/.omp/plugins` registries and can crash on a
  malformed registry (fails closed under the counter). A dependency key containing `..` escapes
  `node_modules` (the registry is operator-trusted). It executes nothing, and a frontmatter name cannot
  cause traversal. Its own 215 roots are `~/.agents/skills` (83) and `ecc-pi-core/skills` (132); it
  does not use S5.
- **Writes:** every lane change sits under its owner's path or a wave dir, except `corpus/QUALITY.md`
  (+Q77), which the L1 should confirm it authored. The fleet has nothing under kotoba or round-86.

Verdict: S5, a G4 fail-open (unresolved `..` and `*` crossing `/`), plus S4 (docker socket in the sandbox).
