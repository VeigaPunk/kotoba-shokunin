# C1 join-definition history — why the round-47 independent join moved 21/24 → 20/24

Seat: KotobaR48.C1JoinDefinitionHistory (leaf; no subagents dispatched). Lane read-only except this
file. Date 2026-10-22. No tool installed or upgraded (stock python3 + coreutils + git sufficed);
no pacman transaction attempted.

## Findings

**1. The move is exactly one joined row: `oc.roots.names_plus_builtin`.**
Round 47 changed one load-bearing constant: `verifiers/verify_harness_claims.py:56` moved `OC_BIN`
from `~/.opencode/bin/opencode` (dead — the v2.0.26 standalone channel was removed from the host
2026-10-20) to the live npx ELF
`~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` (opencode-ai 1.19.3,
sha256 `179ca421…`, 186,013,824 B). The producer's builtin term at `:477-479` is
`builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0`; at BASE the dead path made
`binary.is_file()` false → `builtin_names=0`, producer reading 10 (10 host names + 0). At TIP the
ELF carries the marker → `builtin_names=1`, producer 11. The independent instrument
(`verifiers/verify_harness_independent.py`) never reads the opencode binary and states
"built-in names: 0 by declaration" → 10. The comparator's `equal` predicate
(`compare_harness_independent.py:210-213`) is strict equality → `predicate_agree('equal', 11, 10) = False`
→ a fourth disagreement. Falsify receipts: frozen-carrier join BASE 21/24 (3 disagreements) vs
TIP 20/24 (4 disagreements), identical otherwise (`.ufo/waves/round-47/falsify/W2DepthNoHarm.md` §3.2);
a 2×2 code×binary matrix isolates the constant as the entire cause, and TIP run with the BASE
(dead) path reproduces BASE's 3-disagreement set exactly (§3.3; `W2HarnessNoHarm.md` §3, F-1).

**2. What "customize-opencode built-in marker" means.** It is the producer's byte-substring probe
above: `customize-opencode` is the name of the built-in skill opencode historically embedded
(round-10 doc: "18 == 17+1 … builtin `customize-opencode` confirmed present in the opencode ELF",
`corpus/knowledge/harness-verifier-round10.md:126`). The probe returns 1 iff the installed ELF
embeds that name. v2.0.26 dropped the string (0 occurrences — probe degenerate, round-21 R1
defect 6), and the later dead path made it silently 0; the 1.19.3 npx ELF restores it (I measured:
2 matching lines, 3 occurrences — line-vs-occurrence counting explains the 2-vs-3 difference
between the two W2 receipts). The round-47 spot-check names the disagreement definitional:
"the producer observes a `customize-opencode` built-in marker, while the independent instrument
fixes built-ins to zero by declaration" (`corpus/lessons/round-47-verifier-spotcheck.md`, C3 row).

**3. The move falsifies a still-live r37 prediction.** `corpus/knowledge/harness-independent-round37.md:464-465`:
"the string `customize-opencode` is absent from the binary; a future binary carrying it would move
both readings together, un-adjudicated." Both halves are now false — the string is back, and the
readings moved *apart*, because only the producer side reads the binary. The W2 receipts also note
the pass count itself never moved (21/28 at BASE and TIP, same seven DRIFT ids; the row was already
in DRIFT vs pin 7 at both commits) — the harm is confined to the independent join.

**4. Which check ids disagree, and does C1 touch them.** Frozen-carrier join at TIP, per the
W2DepthNoHarm §3.2 receipt (`expected` = independent, `observed` = live; the four `omp.catalogue.*`
rows are SCOPED_OUT and leave the join by name):

| check id | producer (observed) | independent (expected) | mode | cause | touched by C1 |
|---|---|---|---|---|---|
| `oc.roots.names_plus_builtin` | 11 (10 names + 1 builtin) | 10 (builtins 0 by declaration) | equal | `OC_BIN` now points at an ELF carrying the marker; IND never reads the binary — definitional, exposed by the round-47 constant move | **Yes** — C1 rewrites this row's IND derivation (configured-root union); the builtin cause is explicitly NOT resolved (plan: "stays routed") |
| `omp.cache.misses` | 3 | 3 | zero | both readings 3 — 3 of the 10 host skills fall back to preview descriptions (Q09 debt, host grew 7→10 on 2026-10-20); the zero-mode predicate requires both readings empty, so even 3-vs-3 counts as disagreement | No |
| `omp.cache.verified_skills` | 10 | 7 | equal | live verifies all 10 host skills; IND's blind key reproduction covers the 7 whose cache keys it reproduces (3 rows are preview fallbacks; cf. `.ufo/waves/round-47/build/C1HarnessDriftRoot.md:64-65`) | No |
| `omp.descriptions.unmodelled` | 0 | 3 | zero | the 3 skills born 2026-10-20 are outside IND's descriptions substrate (it counts 3 unmodelled); the live counter reads 0 over its own population [INFERENCE on the live-side mechanism; the 3-vs-0 values are receipted] | No |

**5. What C1 (configured-root enumeration) does and does not change on this row.** The configured-
root change lives in `verifiers/verify_harness_independent.py` (present in the lane working tree,
uncommitted, +13/−8 vs HEAD `75f671b`; attempt 1's `c0185da` landed the ruler and the `oc_config`
substrate field): the derivation loop becomes `for directory in sorted(sources | configured)` over
`s.oc_config/skill` and `s.oc_config/skills` in addition to the log-named sources (working tree
`:605-615`), fixing the invisibility defect a skill planted in a configured root would exploit.
It keeps "built-in names: 0 by declaration" verbatim, so the production-marker disagreement is
untouched by design. On this host `~/.config/opencode/{skill,skills}` are absent (measured), so the
union adds 0 names, IND stays 10, and the 20/24 join keeps this fourth disagreement after C1.
Side observation: HEAD's evidence string already said "configured dirs present" while iterating
only `sources` — the candidate also repairs that stale text.

**6. Default live join remains exit 2 at both commits (pre-existing, not part of the move).** The
committed scope probe recomputes over the live `~/.omp/agent/sessions` tree mid-run (TOCTOU):
"false blocker: scoped row omp.catalogue.found declares observable {…23882…} but recomputation
gives {…23892…}" → exit 2 at BASE and TIP alike (`W2HarnessNoHarm.join-blocked.txt`,
`W2DepthNoHarm.md` §3.1). All 21/24 and 20/24 numbers are frozen-carrier measurements.

## Evidence (commands run this session; exit codes verbatim)

- `git log --oneline -4` (lane) → `75f671b`, `c0185da`, `197b5a4`, `92aa937`; exit 0.
  `git status --porcelain` → ` M verifiers/verify_harness_independent.py` (sibling integration in
  flight; untouched by me); `?? .ufo/waves/round-48/`, `?? plans/round-48.md`.
- `git diff HEAD -- verifiers/verify_harness_independent.py` → 1 file, +13/−8 (artifact
  `artifact://842`); `git show HEAD:verifiers/verify_harness_independent.py` roots block confirms
  HEAD enumerates `sources` only.
- ELF marker probe (exit 0): `grep -c -a -F customize-opencode <npx ELF>` → `2`;
  `grep -a -o -F customize-opencode <npx ELF> | wc -l` → `3`.
- Configured roots (exit 0): `test -d ~/.config/opencode/skill` → absent; `…/skills` → absent;
  `ls ~/.agents/skills | wc -l` → 10.
- Receipts read (not re-executed; the 14 GB live session tree makes a join rerun a race):
  `.ufo/waves/round-47/falsify/W2DepthNoHarm.md` (§3.2: TIP exit 1 `agreement: 20/24 … disagree: 4`,
  strict 17/24; BASE exit 1 `21/24 … disagree: 3`, strict 18/24; §3.3 2×2 matrix),
  `W2HarnessNoHarm.md` (§2: 21/28 both commits; §3: matrix + marker counts; F-1: join-row divergence),
  `W2HarnessNoHarm.observations.json` (live tip `roots_plus_builtin: 11, builtin_names: 1,
  root_live_names: 10`; independent 10; `omp.cache.misses: 3, omp.cache.verified_skills: 10`),
  `W2HarnessNoHarm.join-blocked.txt` (both arms exit 2).
- Corpus/docs: `LOG.md:2317-2343` (round-47 landing + falsify entry, "possible harm" paragraph),
  `corpus/lessons/round-47-verifier-spotcheck.md` (definitional ruling, C3 row),
  `corpus/knowledge/harness-independent-round37.md` (§1-3, falsified sentence at :464-465),
  `plans/round-48.md` C1 ("Built-ins stay 0 by declaration — the production-marker disagreement is
  NOT resolved by this claim and stays routed").
- Instrument code read at HEAD and working tree: `verify_harness_claims.py:55-56,477-479,504`;
  `verify_harness_independent.py:588-632` (both versions); `compare_harness_independent.py:54-66,
  210-218,709-754,1214-1218`.

Confidence: the 21/24→20/24 mechanism, the four disagreeing ids and their values, and the
configured-root diff are receipted/measured (high). The IND-side derivation mechanism for
`omp.cache.verified_skills`/`unmodelled` is grounded in the r37 doc and C1HarnessDriftRoot but not
re-derived line-by-line this session (marked where inferential).
