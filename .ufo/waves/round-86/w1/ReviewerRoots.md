# ReviewerRoots — scoped findings (round 86, w1)

Full review: `.ufo/waves/round-86/w1/ReviewerRoots/review.md`. Counter receipt: `.ufo/waves/round-86/w1/ReviewerRoots/counter-rerun.txt`.

- **Independent derivation (omp 18.15.0 ELF, before reading ExecModel's files):** with cwd `/home/vgpnk/Projects/shokunin` and this host's config, omp reads two non-empty skill roots:
  - `~/.omp/plugins/node_modules/ecc-pi-core/skills`: omp-plugins provider, priority 90, 132 names.
  - `~/.agents/skills`: agents provider, priority 70, 83 names.

  132 + 83 = 215, which equals the fixture. `~/.claude/skills`, `~/.codex/skills`, `~/.config/opencode/skills` and the Claude plugin caches are opt-in and are not read.
- **Ledger, row by row:** 9 sound, 3 located but irrelevant, 0 wrong.
  - Rows 1 and 8 cite the generic native-provider description `Js`.
  - Row 9 cites `var Gh = ".omp";` for the plugin root, which carries 132 names. omp does read that root; the quote is just not the code that makes it do so. The code quotes are in review.md.
- **Precedence:** the root set and the per-root `Ba` scan match omp. Four divergences are latent and contribute nothing to N:
  - P1: project roots are ranked above native-user and plugin roots across the two lists. Probe D shows it.
  - P2: on a name collision the model keeps the first root's skill and drops the other; omp exposes the second as `<ns>/<name>`.
  - P3: `requireDescription` is not modelled.
  - P4: when the plugin registry is hidden, the model takes every plugin; omp would yield 0. Probe C shows it.
- **No accidental reproduction:** ablation gives 215 of 215, all from the two roots omp reads, and no extra names.
- **Counter re-run** (scratch commit bb59735, same file hashes as CANDIDATE_READY): `omp catalogue lines reproduced 215 of 215`, G1–G4 PASS, exit 0.
- **Counter defects (reported, not patched):**
  - CF1: G4's dot rule rules out any code-relevant quote for `~/.omp/plugins/...`; there is no `.omp/plugins` literal in the ELF.
  - CF2: `{cwd}/` expands to `$HOME` and `/`.
  - CF3: the sandbox hides the plugin registry that omp needs.
  - CF4: the counter changed after freeze ecfad51 (addendum-1, b9ee548). The L1 should adjudicate this against the plan's kill rule.

C1 roots: sound
