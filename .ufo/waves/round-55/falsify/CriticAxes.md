Result: MIXED — C1 verifies as declared under the v2 counter (reproduced at `96155796` and at the tip), but its "new ground 4" holds only on the counter's letter: two forms are new to the base corpus, which is the bar exactly. C2 is a miss as declared (exit 1 at `e966cd59` and at the tip), and given M50 it could not have verified even at exit 0. No axis score is harmed by the content. Calibration is harmed if the record keeps "new ground 4" unbounded and the unreceipted `@ 96155796` attribution.

Seat: KotobaR55.CriticAxes (critic, read-only on the lane). Sandbox: `/fast/scratch/hyaku/kotoba-r55/CriticAxes`, a clone checked out at `f0e6b695b746775823b65a8c45de7d50ea33e84f`; scratch is under `scratch/` there. Counter bytes in the sandbox: C1 sha256 `e13eb88d…` (erratum v2) and C2 sha256 `0c1258e2…` (plan bytes). `git diff --quiet a10240c0 HEAD -- verifiers/check_could_not_evaluate.py` gave exit 0, and `git diff --quiet f0e5de82 HEAD -- verifiers/verify_surfaces.py` gave exit 0. No installs. No processes left running (`pgrep -af CriticAxes` printed nothing at 2026-10-23T00:16:18Z).

## One-line verdicts

| Item | Verdict | Evidence (below) |
|---|---|---|
| C1 depth (v2, after erratum 1) | **Verifies as declared.** The frozen v2 `--fetch` prints `5 of 5; new ground 4`, exit 0, at `96155796` and at `f0e6b695`. Bound the record: F=5 is robust, but G is 2 on the substance (Cursor `/skill-name`, opencode `@skill-id`), which is exactly the bar | A1–A4 |
| C2 operability | **Miss as declared.** It exits 1 at `e966cd59` and at the tip (`25 of 25; controls held 12 of 13`; the assertion-floors V check exited 2 because a nested self-test timed out at a load average of about 90). It is also **not verifiable as declared** (M50): an exit 0 would not separate the patches from a remap, a preflight or a shadow module. Outside guards show the probed classes are honestly fixed, with no regression. No operability score move | B1–B4 |
| Axis harm | **None found on depth, consistency, operability, coverage, freshness or adjacency.** Calibration is at risk: two record defects can be fixed before closure | C |
| Trend: expansion | **improved**, provisional on non-author admission. One entry on Frontier ground the coverage map listed as a gap; bounded to two forms new to the corpus | D |
| Trend: quality | **improved**, bounded. The routed precision gaps were narrowed and no entry was found false and left unmarked. The new opencode `SKILL.md` cell drops the "V2" scope its own entry states (a new precision gap, routed) | D |
| Trend: discernment | **improved** on round-54 learning: the outside spot-check's disagreements became Q34–Q36 with lessons M45, M47 and M48. Round 55's own gate is not yet checked from outside, and it holds one internal inconsistency (the `$skill` reject against the S066 admit) | D |

## A. C1 — depth

**A1. Reproduced on the frozen v2 counter at the tip and at the landing commit.**
```
2026-10-23T00:08:46Z  (sandbox, --rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch)
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
exit 0
self-test: 0 failure(s) over 44 assertions   (selftest exit 0)

2026-10-23T00:14:03Z  (sandbox, --rev 96155796059c297da0f08424a172ea1cbf30caa4 --fetch)
… identical rows …
user-typed invocation forms found on the live page 5 of 5; new ground 4
exit 0
```
Between `96155796` and the tip, the C1 surface changed only in `corpus/lessons/round-55.md` (+34 lines). Command: `git diff --stat 96155796 HEAD -- SKILL.md corpus/knowledge/explicit-invocation-round55.md corpus/SOURCES.md corpus/lessons/round-55.md verifiers/check_explicit_invocation.py`.

**A2. The erratum was not tuned to pass.** The plan admits that the L1 read the draft rows before v2 (`plans/round-55.md:101-102`). At least one rule v2 added costs the draft data a count: the "quote holds `skill`" rule drops VS Code from F (6 to 5). A rule shaped to pass would not remove the claim's own row. The base-URL rule marks Claude Code `new=False`, but G is unchanged, because Cursor holds the same distinct token `/skill-name`. The W1 and W3 shortcut receipts fail under v2 (`controls/C1-shortcut-W1W3.txt`). The v1 line must still be reported beside the v2 line (`plans/round-55.md:109-110`).

**A3. Counterexample: "new ground 4" re-scores held ground twice by the counter's letter, and once more by the corpus.**

1. **Codex `$setup-demo-app` is an example-name variant of a held form.** Base `corpus/knowledge/skill-overlap-levers-round51.md:26` holds "explicit `$skill` invocation still works" (`git grep … f0e5de82 -- SKILL.md corpus/knowledge`). The lesson's own Gate rejects the learn.chatgpt.com `$skill` quote because "re-citing it would re-score held knowledge (critic world W3)" (`corpus/lessons/round-55.md:31`). It then lets S066 earn new ground for the same held form, because the example name evades the string test. Q37 (`corpus/QUALITY.md:48`) itself names "a case or placeholder variant of held knowledge". v2 handles case only.
2. **opencode `@skill-id` comes from a mirror of a page that was already a base row.** Base S064 cites `https://opencode.ai/v2/docs/skills`, served from `services/www/src/docs/content/skills.mdx`, and it already anchors "§ Loading `:184`" (`git show f0e5de82:corpus/SOURCES.md`, the S064 row). S071 cites the raw-GitHub copy of that same file at a pinned commit. Seat Srcopencode states the same sentence is on the served V2 page at HTML line 289 (`.ufo/waves/round-55/build/Srcopencode.md:13,39`). The v2 URL rule drops only the scheme, `www.`, a trailing `/` and `.md`/`.mdx`. So the same rule that zeroes Claude Code (S065 has S053's URL) is passed by a mirror URL. The form `@skill` occurs nowhere in the base corpus (git grep `@skill|@<` over `SKILL.md` and `corpus` at `f0e5de82`: no hits). That makes it new as a fact, but not as a source.
3. **Copilot CLI's slash form was held in the base registry, outside the counter's haystack.** The base S031 `teaches` cell reads "… while `/SKILL-NAME` stays available …" (`git show f0e5de82:corpus/SOURCES.md`, the S031 row), and base `corpus/lessons/round-51-verifier-spotcheck.md:120` quotes "via `/SKILL-NAME` or automatically by the agent". The frozen haystack (`SKILL.md` plus `corpus/knowledge/*.md`) is declared in the plan, so this is legitimate under the letter. Still, it is held ground on the substance.
4. **Cursor `/skill-name`** is new under every reading. The Cursor skills page is not a base row, and the only Cursor command at base is the `/skills` listing (`SKILL.md:190` at base).

The resulting G under each reading:

| Reading | New-ground clients | G | Meets G≥2? |
|---|---|---|---|
| Frozen v2 counter (the declared predicate) | Codex, Copilot CLI, Cursor, opencode | 4 | yes |
| Form not held anywhere in the base corpus (`SKILL.md`, knowledge, SOURCES cells, lessons) | Cursor, opencode | 2 | yes, with margin 0 |
| Form not held, and source page not a base row (counting mirrors) | Cursor | 1 | no |

The declared predicate is the counter, so C1 verifies. The record must not say "new ground 4" without this bound. Impacted axes: depth (the size of the increment) and calibration.

**A4. The opencode row is wider than its source** (the over-wide-record defect class from rounds 50–54).
- The `SKILL.md` row (`SKILL.md:205`) says `opencode | @skill-id` with no version.
- The entry (`explicit-invocation-round55.md:33`) and the index (`corpus/README.md:87`) both say "opencode V2".
- The served V1 page carries no such form. Fetch at 2026-10-23T00:14:05Z: `https://opencode.ai/docs/skills.md` returned HTTP 200, 5,365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`. That is byte-identical in prefix to base S059's `f10ced73…`, so S059 re-verifies. `grep -n -E '@skill|@<|mention'` found no hits. `https://opencode.ai/docs/skills/` returned 200, 73,201 B, with `grep -c '@skill'` giving 0.
- The V1 page documents `/name` behind `opencode/slash: "true"` (Srcopencode.md:7). The row's action would therefore miss V1 explicit turns.
- The installed client prints `opencode --version` → `1.19.4`. [INFERENCE] Whether 1.19.4 serves the V2 `@` form is not checked.
- Smallest correction: state "V2" in the row's "What it does" cell, and add the V1 `/name` form (with `opencode/slash`) to the action cell. Leave the client cell alone: the counter matches the client name against the whole first cell (docstring: "case-insensitive, whole cell"), so `opencode V2` there would drop F to 4. The L1 should re-run the counter after the edit.

## B. C2 — operability

**B1. The frozen predicate misses at the tip.**
```
21:08:46 up 16:13, load average: 62.93, 85.41, 87.29
2026-10-23T00:08:46Z
measured f0e6b695b746775823b65a8c45de7d50ea33e84f
check_assertion_floors.py          V expect 0|1 got 2 MISS      (every other line: ok)
could-not-evaluate probes honoured 25 of 25; controls held 12 of 13
exit 1
2026-10-23T00:12:00Z  load average: 83.48, 81.42, 85.12
```
This agrees with the L1's `.ufo/waves/round-55/C2-measure-e966cd59.txt` (`25 of 25; 12 of 13`, exit 1, load 104.62). Plan line 80 says "A miss … is reported as a miss", so C2 is a miss as declared.

**B2. The miss is the environment, not the patch.** A direct run of the V form, `python3 -B verifiers/check_assertion_floors.py` (no arguments, as the counter's GATES table has it at `check_could_not_evaluate.py:80`), started at 2026-10-23T00:12:39Z (load 93.98). It printed `FAIL harness_independent self-test timed out after 120s (hung?)` among 12 PASS lines and exited 2 (`V exit 2`; real 2m16s; ended 2026-10-23T00:14:56Z at load 77.97). The 120 s cap is `SELF_TEST_TIMEOUT_S = 120` (`check_assertion_floors.py:147`), and the timeout is reported at `:536`; both are unchanged from base. The floors patch adds only a `git --version` preflight and self-test arm F30 (`git diff f0e5de82 HEAD -- verifiers/check_assertion_floors.py`). It does not touch the nested timeout. CriticC2Sizing Q5 recorded the same 12 of 13 on the untouched base under load. So this is not harm from the patch. It is also not a pass: the plan does not permit an idle-host re-measure as the declared result.

**B3. Even an exit 0 would not verify as declared (M50).** The frozen predicate is met by D (remap 1→2, `9c992b8d`), P (preflight only, `65f5d237`) and S (`verifiers/argparse.py` shadow, `eb97c954`) (`.ufo/waves/round-55/build/CriticC2Sizing.md:7-12`). The lesson's wording, "not verifiable as declared" (`corpus/lessons/round-55.md:47`), and the LOG's "miss as declared" (`LOG.md:2460,2466`) are both true and should both stay. Neither should be softened into "honours could-not-evaluate" (CriticC2Sizing Q3).

**B4. Guards outside the counter, run on the tip gate bytes in the sandbox.** They show the probed classes are honestly fixed and nothing regressed.
- **Red anchors** (2026-10-23T00:10:33Z, tip; 00:10:48Z, base worktree). All nine exit 1 at both revisions: box proof `--rev f3046466`; finding delta `--base e3371548 --head a10240c0`; overlap `43ca0bfb` and `7c81a787`; mcp `c8579a4c` and `4c003a4b`; description thresholds `422ffd10` and `e3371548`; correction sweep `c8579a4c`. So real findings are not remapped to 2, which rules out the D and A shapes.
- **`--root .` with git absent** (`env PATH=<dir with python3 only>`, where `shutil.which('git')` gives `None`). Correction sweep, mcp, description thresholds and overlap all exit 0 at tip and at base. The P-shape regression CriticC2Sizing Q4 predicted is absent.
- **R and G probes, hand-run outside the counter's temp-path and `nogit-bin` names** (2026-10-23T00:11:40Z). The random revision was `ad411f2cacf6409a4e94cdd4c574d8332bcc1e06`; the PATH directory was named `plainbin`.
  - R exits 2: box proof, mcp, overlap, description thresholds, finding delta (base form), finding delta (head form).
  - G exits 2: box proof, mcp, correction sweep, finding delta, assertion floors and corpus independent. The last two print stderr `could-not-evaluate: git not runnable: [Errno 2] No such file or directory: 'git'`, which names git rather than a timeout.
  - So the fixes are not keyed on labels, which rules out shape L.
- **Standard-library shadows:** `[p.stem for p in verifiers/*.py if p.stem in sys.stdlib_module_names]` printed `[]`, which rules out shape S at the tip.

These guards support a bounded statement: at the tip, the eight patched gates exit 2 on an unknown revision and with git absent from PATH, and none remaps a finding. They do not turn the declared C2 into a pass, so the operability score holds.

## C. Is any axis harmed?

- **depth:** not harmed. The new table adds no contradiction, and `SKILL.md` is 598 lines (≤600; base 599).
- **consistency:** not harmed, but drift risk remains. § Overlap levers (`SKILL.md:429-430`) and the new table (`:199`, `:201`) both state Claude Code `/name` and VS Code manual `/`, and they agree. Neither cross-references the other: two authorities for one fact (CriticC1Sizing correction 4 was not applied).
- **operability:** not harmed. All anchors exit 1; the `--root` no-git runs exit 0; every S and V control except the load-timed floors held at the tip (B1).
- **coverage, freshness, adjacency:** surfaces untouched; `verify_surfaces.py` is unchanged.
- **calibration:** at risk. Two record defects can be fixed before closure:
  1. `SCORECARD.md:140,282` record `5 of 5; new ground 4 … exit 0 @ 96155796`, but no committed receipt names `96155796`. `git grep '5 of 5; new ground 4' HEAD` finds only `MutC1Counter.md:234`, `LOG.md` and `SCORECARD.md`, and `LOG.md:2464` says "on the working tree that became `96155796`". That is the M48 class, against Q36 written in this same round. A1 above is a receipt naming `96155796`; commit it, or one like it.
  2. `.ufo/waves/round-55/C2-measure-e966cd59.txt` is cited by `LOG.md:2465`, but it is untracked at the tip (`git status --porcelain` → `?? .ufo/waves/round-55/C2-measure-e966cd59.txt`).

  Leaving "new ground 4" unbounded (A3) would overstate novelty, the over-wide-record defect from rounds 50–54.

## D. Trends (LEARNING.md table)

- **expansion: improved**, provisional on the non-author closure (`SCORECARD.md:140`: "verdicts belong to the non-author closure"). One knowledge entry, `explicit-invocation-round55.md`, has a `source:` citing mined rows S065–S071 and an index row (`corpus/README.md:87`). Its ground is the Frontier row the coverage map lists as a gap (`corpus/README.md:98,152`). Bound: two forms are new to the corpus (A3), plus the Gemini distinction between a model tool call and a user-typed form.
- **quality: improved**, bounded. Routed defect 3 narrowed the precision gaps the round-54 spot-check left (`ed3e8996`; precedent `round-54-verifier-spotcheck.md:202`). S059 re-verifies at the same sha (A4). No admitted entry was found false and left unmarked. The new opencode `SKILL.md` cell omits "V2" (A4): route it before closure, or it becomes a stale, unmarked precision gap.
- **discernment: improved.** The round-54 outside spot-check's disagreements became grounded criteria: Q34 (M45), Q35 (M47) and Q36 (M48) (`corpus/QUALITY.md:45-47`). Q37 rests on lane-critic findings M49 and M50 and has a lesson behind it. Round 55's own admits and rejects still await the outside spot-check. The checker should look first at the inconsistency between Gate reject row 2 (`$skill` as held ground) and the S066 admit counted as new ground (A3.1), and at S071 as a mirror of S064 (A3.2).

## Smallest safe corrections (record only; counters frozen)

1. Record C1 as `found on the live page 5 of 5; new ground 4 (counter, v2)`, with the bound "2 forms new to the base corpus (Cursor `/skill-name`, opencode `@skill-id`); Codex `$…` and Copilot `/…` were held at base (round-51 entry `:26`; S031 `teaches`)". Report the v1 line beside it.
2. Commit a C1 receipt that names the measured revision (A1 is one). Commit `C2-measure-e966cd59.txt`, or strike the citation.
3. Scope the opencode `SKILL.md` row to V2 in its "What it does" cell (not the client cell, which the counter matches as a whole cell), and add the V1 `/name` form (`opencode/slash`); then re-run C1 `--fetch`.
4. Add a cross-reference between § Overlap levers and § Explicit invocation by client, or name one of them the authority.
5. Next C1-style counter (Q37): normalize example names and placeholders, and treat a mirror of a base-row page (raw source of the same docs file) as a base URL.

Checks for the L1: `python3 -B verifiers/check_explicit_invocation.py --rev <integrated rev> --fetch` (and `--self-test`); `python3 -B verifiers/check_could_not_evaluate.py --rev <integrated rev>` with `uptime` pasted; and the B4 anchor script at `/fast/scratch/hyaku/kotoba-r55/CriticAxes/scratch/anchors.sh <tree>` (it expects `NOGIT` set to a directory holding only `python3`).
