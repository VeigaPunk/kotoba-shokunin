# MutTester-2 — round 86 w1 mutation battery (C1 counter + candidate model)

Seat MutTester-2 (a revived r85 seat also runs as `MutTester` in the parent dir; KotobaR86 assigned this report path). Scratch `/fast/scratch/hyaku/kotoba-r86/MutTester-2/` (removed at yield); every mutant ran on a `git clone --shared` copy, never on a lane file. Receipts: `partA-mutants.json` (freeze counter), `partA-amended-b9ee548.json`, `partB-candidate.json`, `g4-dotdot-bypass.txt`, `worlds-sources.txt`, `partA-forgery-modules.txt`.

## Headline

1. **The amended frozen counter (b9ee548, sha `39a014f2…`) is falsified unmutated:** round-base model + one `USER_ROOTS` line `HOME / ".omp/../.zcode/cli/plugins/marketplaces/ecc/pi/core/skills"` + ledger rows `~/.omp/*<TAB>var Gh = ".omp";` and `~/.agents/skills<TAB>Load skills from .agent/skills and .agents/skills (project walk-up + user home)` → `omp catalogue lines reproduced 215 of 215`, G1–G4 PASS, **exit 0** (`g4-dotdot-bypass.txt`). The control without `..` (direct `~/.zcode/...` row) → G4 FAIL, exit 1. Cause: `guard_g4` takes `root = str(Path(offered).parent.parent)` without normalising, and fnmatch `*` spans `/` and `..`, so `~/.omp/*` covers `~/.omp/../<anything>`. Critic-2's F1 root (which omp never reads) passes again. Reported to KotobaR86; not patched.
2. Battery A on the amended counter: 51 mutants, 20 killed, 31 survived. Six survivors give a real forgery world exit 0 that pristine refuses: M05 (TARGET), M11 (ctime), M12 (quote location), M25 (main drops the render epoch), A03 (dot-segment wildcard), A04 (no-dot pattern). M12 used to be killed on the freeze counter; on the amended counter it survives because the self-test's fake quote also fails the new dot-name check, so that check hides the location check.
3. Battery B on the candidate (scratch rev of b9ee548 + candidate files sha `bd793b6c…`/`36021309…`, scored 215 of 215 exit 0): 33 mutants, 8 killed, 25 kept N ≥ 205 with every guard PASS. The counter tests **2 of the model's 12 roots** (`~/.agents/skills` → 83 names, the plugin roots → 132 names). The other 10 ledger roots are absent on this host. Discovery order, the plugin-registry branch, the frontmatter-name rule, both preview edge branches and a block-scalar parse defect (207 of 215) are all untested.

Freeze counter ecfad51 (historical, superseded during the wave): 30 mutants, 14 killed. 4 survivors exploited: M05, M09 (hide list emptied → `A_echo_unsandboxed` 215 exit 0), M11, M25.

## A. Frozen counter `verifiers/check_omp_catalogue_repro.py`

### A (scored version) — amended counter b9ee548

Counter sha256 `39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520`; pristine self-test `0 failure(s) over 46 assertions` (exit 0); restored self-test `0 failure(s) over 46 assertions` (exit 0), bytes restored to the same sha after every mutant.

| mutant | expected | observed (copy's --self-test) | verdict | survivor: real forgery world |
|---|---|---|---|---|
| M01 G1 disabled | self-test fails | exit 1, `4 failure(s) over 46 assertions`; first FAIL `echo forgery exit 1` | killed | — |
| M02 G2 disabled | self-test fails | exit 1, `6 failure(s) over 46 assertions`; first FAIL `provenance exit 1` | killed | — |
| M03 G3 disabled | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `fixture pin exit 1` | killed | — |
| M04 G4 disabled | self-test fails | exit 1, `16 failure(s) over 46 assertions`; first FAIL `w_noledger exit 1` | killed | — |
| M05 TARGET 205->83 | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **cand_minus_plugins_N83**: pristine exit 1 (83 of 215 FAIL) → mutant exit 0 (83 of 215) |
| M06 threshold compare dropped (n>=0) | self-test fails | exit 1, `6 failure(s) over 46 assertions`; first FAIL `empty roots exit 1` | killed | — |
| M07 TOTAL 215->214 | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M08 TOTAL check dropped from G3 | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M10 scratch list emptied (default_scratch -> []) | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M11 ctime check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **F_forge_backdated_outside_scratch**: pristine exit 1 (208 of 215, G2 FAIL) → mutant exit 0 (208 of 215) |
| M12 G4 quote-location check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **Z_unlocated_quote**: pristine exit 1 (215 of 215, G4 FAIL) → mutant exit 0 (215 of 215) |
| M13 G4 quote length floor dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M14 G4 pattern match always-true | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `w_otherroot exit 1` | killed | — |
| M15 G4 header check dropped | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `w_header exit 1` | killed | — |
| M16 G4 {cwd} ancestors dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M18 render compare loosened to strip() | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M19 G2 SKILL.md filename check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M20 G2 forbidden-tree check dropped (scratch only) | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `provenance exit 1` | killed | — |
| M21 G1 echo token '.jsonl' dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M22 G1 echo token 'sessions' dropped | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `echo forgery exit 1` | killed | — |
| M23 G1 hardcode floor 40->200 | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `hardcode forgery exit 1` | killed | — |
| M25 main: render epoch not passed (frozen_epoch=None) | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **F_forge_fresh_outside_scratch**: pristine exit 1 (208 of 215, G2 FAIL) → mutant exit 0 (208 of 215); **F_forge_backdated_outside_scratch**: pristine exit 1 (208 of 215, G2 FAIL) → mutant exit 0 (208 of 215) |
| M26 main: forbidden trees emptied | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M27 main: fixture pin not enforced | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M28 main: omp binary sha pin dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M29 main: ledger not read (ledger=None) | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M30 G2 mtime/ctime compare inverted guard (frozen_epoch+1e12) | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `post-render file exit 1` | killed | — |
| M09 hide list emptied (default_hide -> []) | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M09b ~/.omp dropped from hide list | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| M17 cache precedence swapped (preview before cache) | self-test fails | exit 1, `4 failure(s) over 46 assertions`; first FAIL `good world exit 0` | killed | — |
| M24 sandbox: hidden dirs not masked | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `hidden root exit 1` | killed | — |
| A01 _pattern_problem always None | self-test fails | exit 1, `6 failure(s) over 46 assertions`; first FAIL `w_star exit 1` | killed | — |
| A02 first-segment wildcard check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A03 dot-segment wildcard check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **Z_dotwild_pattern**: pristine exit 1 (215 of 215, G4 FAIL) → mutant exit 0 (215 of 215) |
| A04 no-dot-directory check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | **Z_nodot_pattern**: pristine exit 1 (215 of 215, G4 FAIL) → mutant exit 0 (215 of 215) |
| A05 quote-names-dot check dropped | self-test fails | exit 1, `2 failure(s) over 46 assertions`; first FAIL `w_quotemiss exit 1` | killed | — |
| A06 empty-pattern check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A07 parent dir-name check dropped | self-test fails | exit 1, `1 failure(s) over 46 assertions`; first FAIL `one-path forgery dir-name MISS` | killed | — |
| A08 parent desc-in-file check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A09 parent key==reference check dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A10 parent preview==reference check dropped | self-test fails | exit 1, `4 failure(s) over 46 assertions`; first FAIL `wrong floor exit 1` | killed | — |
| A11 parent render from module preview | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A12 ref_preview o>=E dropped | self-test fails | exit 1, `4 failure(s) over 46 assertions`; first FAIL `good world exit 0` | killed | — |
| A13 ref_preview sentence floor 40->39 | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A14 ref_preview cut 99->100 | self-test fails | exit 1, `4 failure(s) over 46 assertions`; first FAIL `good world exit 0` | killed | — |
| A15 ref_key separator dropped | self-test fails | exit 1, `10 failure(s) over 46 assertions`; first FAIL `good world exit 0` | killed | — |
| A16 --unshare-net dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A17 --clearenv dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A18 rebind widened to all of ~/.omp | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A19 /run/user + /dev/shm dropped from hide | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |
| A20 malformed-output guard dropped | self-test fails | exit 0, `0 failure(s) over 46 assertions` | survived | no tested world gains exit 0 |

Killed 20 of 51; survived 31.

### A0 (historical) — freeze counter ecfad51 (superseded by addendum-1 during this wave)

Counter sha256 `2390eec230743e3bc464b4253f563a6c45095360c6d3e2d14d6c054421ad6514`; pristine self-test `0 failure(s) over 34 assertions` (exit 0); restored self-test `0 failure(s) over 34 assertions` (exit 0), bytes restored to the same sha after every mutant.

| mutant | expected | observed (copy's --self-test) | verdict | survivor: real forgery world |
|---|---|---|---|---|
| M01 G1 disabled | self-test fails | exit 1, `4 failure(s) over 34 assertions`; first FAIL `echo forgery exit 1` | killed | — |
| M02 G2 disabled | self-test fails | exit 1, `6 failure(s) over 34 assertions`; first FAIL `provenance exit 1` | killed | — |
| M03 G3 disabled | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `fixture pin exit 1` | killed | — |
| M04 G4 disabled | self-test fails | exit 1, `8 failure(s) over 34 assertions`; first FAIL `w_noledger exit 1` | killed | — |
| M05 TARGET 205->83 | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | **C_base_catchall_ledger**: pristine exit 1 (omp catalogue lines reproduced 83 of 215 FAIL) → mutant exit 0 (omp catalogue lines reproduced 83 of 215) |
| M06 threshold compare dropped (n>=0) | self-test fails | exit 1, `4 failure(s) over 34 assertions`; first FAIL `empty roots exit 1` | killed | — |
| M07 TOTAL 215->214 | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M08 TOTAL check dropped from G3 | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M09 hide list emptied (default_hide -> []) | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | **A_echo_unsandboxed**: pristine exit 1 (omp catalogue lines reproduced 0 of 215 FAIL) → mutant exit 0 (omp catalogue lines reproduced 215 of 215) |
| M10 scratch list emptied (default_scratch -> []) | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M11 ctime check dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | **B_forge_backdated_outside_scratch**: pristine exit 1 (omp catalogue lines reproduced 215 of 215, G2 FAIL) → mutant exit 0 (omp catalogue lines reproduced 215 of 215) |
| M12 G4 quote-location check dropped | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `w_fakequote exit 1` | killed | — |
| M13 G4 quote length floor dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M14 G4 pattern match always-true | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `w_otherroot exit 1` | killed | — |
| M15 G4 header check dropped | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `w_header exit 1` | killed | — |
| M16 G4 {cwd} ancestors dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M17 cache precedence swapped (preview before cache) | self-test fails | exit 1, `4 failure(s) over 34 assertions`; first FAIL `good world exit 0` | killed | — |
| M18 render compare loosened to strip() | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M19 G2 SKILL.md filename check dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M20 G2 forbidden-tree check dropped (scratch only) | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `provenance exit 1` | killed | — |
| M21 G1 echo token '.jsonl' dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M22 G1 echo token 'sessions' dropped | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `echo forgery exit 1` | killed | — |
| M23 G1 hardcode floor 40->200 | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `hardcode forgery exit 1` | killed | — |
| M24 sandbox: hidden dirs not masked | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `hidden root exit 1` | killed | — |
| M25 main: render epoch not passed (frozen_epoch=None) | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | **B_forge_fresh_outside_scratch**: pristine exit 1 (omp catalogue lines reproduced 215 of 215, G2 FAIL) → mutant exit 0 (omp catalogue lines reproduced 215 of 215); **B_forge_backdated_outside_scratch**: pristine exit 1 (omp catalogue lines reproduced 215 of 215, G2 FAIL) → mutant exit 0 (omp catalogue lines reproduced 215 of 215) |
| M26 main: forbidden trees emptied | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M27 main: fixture pin not enforced | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M28 main: omp binary sha pin dropped | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M29 main: ledger not read (ledger=None) | self-test fails | exit 0, `0 failure(s) over 34 assertions` | survived | no tested world gains exit 0 |
| M30 G2 mtime/ctime compare inverted guard (frozen_epoch+1e12) | self-test fails | exit 1, `2 failure(s) over 34 assertions`; first FAIL `post-render file exit 1` | killed | — |

Killed 14 of 30; survived 16.

Forgery worlds (sources in `worlds-sources.txt`; all are commits in the scratch clone, scored by the real counter or its mutant):

- Amended: `cand` (candidate, 215); `cand_minus_plugins_N83` (candidate with no plugin roots, 83, guards PASS); `Z_dotdot_bypass` (see headline); `Z_direct_control`; `Z_unlocated_quote` (zcode row whose invented quote names `.zcode`); `Z_nodot_pattern` (`/home/vgpnk/*` + located `loadSkillsFromDir`); `Z_dotwild_pattern` (`/home/vgpnk/.*/cli/...` + located quote `G may not use "TABLE.*" wildcards`); `Z_firstwild_pattern`; `F_forge_*`: a module whose root holds forged `<name>/SKILL.md` files carrying the 215 renders (208 reach parent-side checks; 7 renders are > 100 chars) — fresh or backdated (mtime 2026-10-01), placed in scratch or bound at `/mnt/.agents` by an outer bwrap. That bind stands in for a writable non-scratch directory, which this seat may not create on the host.
- Freeze: `A_echo_unsandboxed` (module reads the fixture by an obfuscated path, offers one old SKILL.md for every name, serves renders through `preview`) plus `B_forge_*` and `C_base_*` (catch-all `*` ledger: G4 PASS on the freeze counter, the defect addendum-1 fixed).

## B. Candidate model (ExecModel, CANDIDATE_READY 903bd78; re-committed here as 1a70e9b8085b850a3fab2fa000f7c2617c3a9b25)

Expected: every mutant drops N below 205 or flips a guard. Observed: real counter (amended, unmodified) on a scratch commit per mutant.

| mutant | expected | observed | verdict |
|---|---|---|---|
| B01 drop walk-up root {cwd}/.omp/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B02 drop walk-up root {cwd}/.claude/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B03 drop walk-up root {cwd}/.agent/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B04 drop walk-up root {cwd}/.agents/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B05 drop walk-up root {cwd}/.codex/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B06 drop walk-up root {cwd}/.opencode/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B07 drop walk-up root {cwd}/.github/skills | N drops or G-flip | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B08 drop user root HOME / ".omp/agent/skills" | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B09 drop user root *omp_plugin_skill_roots(HOME / ".omp/plugins") | N drops | exit 1, N=83, G1–G4 PASS, MISS {'not-discovered': 132} | killed |
| B10 drop user root HOME / ".agent/skills" | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B11 drop user root HOME / ".agents/skills" | N drops | exit 1, N=132, G1–G4 PASS, MISS {'not-discovered': 83} | killed |
| B12 drop user root HOME / ".omp/agent/managed-skills" | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B13 reorder: USER_ROOTS reversed | N drops (first-root-wins shadowing) | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B14 reorder: WALKUP_REL reversed | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B15 reorder: agents before native (~/.agents first) | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B16 nested: scoped @scope/pkg flattened to scope dir | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B17 nested: node_modules fallback branch disabled | N drops | exit 1, N=83, G1–G4 PASS, MISS {'not-discovered': 132} | killed |
| B18 nested: plugin root <pkg>/skills -> <pkg> | N drops | exit 1, N=83, G1–G4 PASS, MISS {'not-discovered': 132} | killed |
| B19 nested: omp/pi manifest gate dropped | N drops or unchanged | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B20 nested: lock enabled gate dropped | N drops or unchanged | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B21 nested: undeclared-lock symlink rule dropped | N drops or unchanged | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B22 discover: frontmatter name ignored (dir name only) | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B23 discover: dot-entry skip dropped | N drops or unchanged | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B24 discover: last-root-wins (setdefault -> assign) | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B25 preview cut 99 -> 100 | N drops (preview-differs) | exit 1, N=193, G1–G4 PASS, MISS {'preview-differs-from-reference': 22} | killed |
| B26 sentence floor 40 -> 39 (sentence test only) | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B27 SENTENCE_MIN constant 40 -> 39 | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B28 last-space o>=E test dropped (base rule) | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B29 CLIFF 100 -> 101 | N drops | exit 1, N=193, G1–G4 PASS, MISS {'preview-differs-from-reference': 22} | killed |
| B30 ellipsis U+2026 -> '...' | N drops | exit 1, N=38, G1–G4 PASS, MISS {'preview-differs-from-reference': 177} | killed |
| B31 omp_key separator dropped | N drops (cache misses) | exit 1, N=0, G1–G4 PASS, MISS {'key-differs-from-reference': 215} | killed |
| B32 parse_frontmatter: plain continuation folding dropped | N drops | exit 0, N=215, G1–G4 PASS | survived (part of the model the measure does not test) |
| B33 parse_frontmatter: block-scalar keep-newline dropped | N drops (cache misses) | exit 0, N=207, G1–G4 PASS, MISS {'render-differs': 8} | survived (part of the model the measure does not test) |

Killed 8 of 33.

What the measure does not test (named per survivor group):

- **10 of 12 roots (B01–B08, B10, B12):** all seven `{cwd}` walk-up roots, `~/.omp/agent/skills`, `~/.agent/skills` and `~/.omp/agent/managed-skills` are absent on this host, so no fixture line can depend on them. The counter checks their ledger rows for a located quote and a dot name, never for meaning. The sandbox also hides the whole fleet tree (= the session cwd), so a `{cwd}` root could not be observed even if it existed. `managed-skills` is additionally hidden (not in `default_rebind`).
- **Root order (B13–B15, B24 last-root-wins):** no fixture name exists in two roots, so precedence is never exercised.
- **Plugin registry branch (B16, B19–B21):** the sandbox hides `~/.omp/plugins/package.json` and `omp-plugins.lock.json`, so the counter only ever runs the model's `node_modules` fallback branch, which exists for the sandbox. B17 (fallback disabled) is killed only in the sandbox. Run unsandboxed on the host, B16/B17/B19/B20/B21 all give the same two plugin roots and 215 discovered names (`partB-candidate.json` → `host_side_unsandboxed`), so the registry branch omp actually uses is never scored. There are no scoped `@scope/pkg` plugins on the host (B16).
- **Frontmatter `name` vs directory (B22):** every discovered dir name equals its declared name, and the counter separately requires the dir name to equal the skill name.
- **Preview edge branches (B26 sentence floor 40→39, B27 SENTENCE_MIN 39, B28 `o >= E` dropped):** no description on the host has a first sentence of exactly 39 chars or a last space before index 40 in its 99-char cut. The counter's parent-side `preview == ref_preview` check never sees a differing input. The required sentence-floor mutant survives.
- **Block-scalar keep-newline (B33):** 8 lines become `render-differs` (207 of 215), which stays above the 205 target with every guard PASS. The 10-line slack absorbs a real parse defect.
- Killed as expected: plugin roots (B09/B17/B18 → 83), `~/.agents/skills` (B11 → 132), preview cut 99→100 and CLIFF 101 (193, 22 `preview-differs`), ellipsis (38), key separator (0).

## Risks

- The F-world exploits for M11/M25 use an outer-bwrap bind at `/mnt/.agents` in place of a real non-scratch host directory. Real ctimes are fresh, and only the mutant's dropped check lets them through.
- A16 (`--unshare-net` dropped) was not re-run with network access. Its exploit is ReviewerCounter-2's F3 (fixture fetched from the pushed freeze), cited from addendum-1, not observed here.
- The candidate bytes were copied from the lane working tree at 19:3x (sha-matched to CANDIDATE_READY). Later edits by ExecModel are not covered.
