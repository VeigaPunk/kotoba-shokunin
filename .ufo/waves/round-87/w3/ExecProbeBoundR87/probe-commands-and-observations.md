# Probe commands — ExecProbeBoundR87 (r87-w3, C1 conjunct-4 `{cwd}/` bound)

Environment for every omp run below: `env -i HOME="$S/home" TMPDIR="$S" PATH=/home/vgpnk/.local/bin:/usr/bin:/bin TERM=dumb`
(with `PATH=/usr/bin:/bin` for the strace run, which execs the omp binary by absolute path). No
credential environment variables were passed to any run; every run used `timeout 60`. All guidance
say "record exactly what you ran": commands verbatim, in order.

Pinned binary: /home/vgpnk/.local/bin/omp, sha256
6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f (verified: `sha256sum` matches the
round-87 frozen pin; ground-truth receipt: omp_help.txt banner "omp v18.15.0").

Fixture (step 1 of the item):
  S=/fast/scratch/hyaku/kotoba-r87/ExecProbeBoundR87
  mkdir -p "$S/home/u/proj/sub" "$S/home/.agents/skills/probe-skill" "$S/home/u/proj/sub/.agents/skills/local-skill"
  SKILL.md written in both skills dirs (frontmatter name+description, one body line).

P1 — help discovery (cwd=$S/home/u/proj/sub):
  cd "$S/home/u/proj/sub" && HOME="$S/home" TMPDIR="$S" timeout 60 /home/vgpnk/.local/bin/omp --help
  -> exit 0 (receipt: omp_help.txt)

P2 — subcommand help:
  cd "$S/home/u/proj/sub" && HOME="$S/home" TMPDIR="$S" timeout 60 /home/vgpnk/.local/bin/omp skill --help
  -> exit 0 (receipt: omp_skill_help.txt)

P3 — DECIDING RUN: local skills enumeration, pinned geometry (cwd=$S/home/u/proj/sub, HOME=$S/home):
  cd "$S/home/u/proj/sub" && env -i HOME="$S/home" TMPDIR="$S" PATH=/home/vgpnk/.local/bin:/usr/bin:/bin TERM=dumb timeout 60 /home/vgpnk/.local/bin/omp skill list --json
  -> exit 0 (receipt: skill_list_json.txt); human variant `omp skill list` -> exit 0 (skill_list.txt)
  Observed: BOTH skills listed; local-skill source=agents:project (baseDir under cwd),
  probe-skill source=agents:user (baseDir directly under $S/home = scratch HOME).

P4 — strace of the same invocation (system-call level):
  cd "$S/home/u/proj/sub" && env -i HOME="$S/home" TMPDIR="$S" PATH=/usr/bin:/bin TERM=dumb timeout 60 strace -f -qq -e trace=%file -o "$S/strace_skilllist.txt" /home/vgpnk/.local/bin/omp skill list --json
  -> exit 0 (receipt: strace_skilllist.txt, 545 lines)
  Observed: project walk-up probed .../u/proj/sub/.agents/skills (opened fd 16),
  .../home/u/.agents/skills (ENOENT), .../home/u/proj/.agents/skills (opened fd 17);
  ZERO opens of any .agents/skills path above .../home (regex
  "ExecProbeBoundR87/\.agents|scratch/hyaku/\.agents|scratch/\.agents|/fast/\.agents|\"/\.agents" -> 0 matches);
  ZERO `..`-segment probes (regex "sub/\.\.|proj/\.\.|/u/\.\.|home/\.\." -> 0 matches);
  .../home/.agents/skills was opened exactly once (unnamed channel, thread 566092 — attribution
  discussed in the report; independent user-channel evidence in P5); both skills' SKILL.md files
  were opened and read during the same run (fresh discovery, not a cache). The `unfinished` openat
  completions above are shown under the "openat resumed" greps of the same receipt.
  Note the codex/opencode/claude-row probes (`.../home/u/proj/sub/.codex/skills`,
  `.../home/u/proj/.codex/skills`, `.../home/.config/opencode/skills`, `.claude` etc. ENOENTs on
  threads 565634/566076/566089/566070) — those are the OTHER ledger rows firing, all below/at HOME
  as sanctioned, none above.

P5 — supplementary channel test (cwd=$S/outside, HOME unchanged; confirms agents:user is a
HOME-rooted channel independent of cwd geometry):
  mkdir -p "$S/outside" && cd "$S/outside" && env -i ... timeout 60 /home/vgpnk/.local/bin/omp skill list --json
  -> exit 0 (receipt: skill_list_outside.txt)
  Observed: ONLY probe-skill, source=agents:user. local-skill gone (project channel strictly
  cwd-rooted), probe-skill still found from a cwd where $HOME is not an ancestor -> the
  .../home/.agents/skills read seen in P3/P4 is the user-home pass (ledger row 11 ~/.agents/skills),
  not the project walk-up reaching $HOME.

Cleanup at exit (step 4): rm -rf -- "$S" (whole scratch tree incl. fixture home, strace, helps).
