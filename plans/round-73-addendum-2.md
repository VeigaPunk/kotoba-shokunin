# Round 73 — plan addendum 2 (erratum E2, before any claim data)

Written after wave 1's attack seats reported (`.ufo/waves/round-73/w1/`) and before any claim was scored: no
counter has been frozen, no claim content has landed, no `check_*` counter of this round has produced a measured
value on a landed revision. Supersedes parts of `plans/round-73.md` and all of `plans/round-73-addendum-1.md`;
every change below is the smallest correction the named seat finding supports (seat, section, and command in
each bullet). Claims are renumbered: the round declares **two** claims (prompt `:424`: prefer 2).

## Withdrawn before data — the planned C2 and its addendum-1 replacement (no claim, no count)

- *Original C2 (registry out of SKILL.md)*: withdrawn in addendum 1 on `PROTOCOL.md:398` (registry home is
  `SKILL.md`). Wave 1 confirms: `CriticSeparability` V1; `ReviewerBaseValues` re-measured the base figures it rested on.
- *Addendum-1 C2 (own-description rules)*: withdrawn. `CriticC2Counter` ran nine worlds that read `own-description
  rules held 3 of 3` on the drafted counter (one period plus a quoted repeat of `SKILL.md`, a first sentence that
  evicts the domain statement, punctuation-only edits) — the kill rule would have fired on its first run;
  `ReviewerDescFeasibility` and `CriticSeparability` V10 find it re-scores a held rule (`check_description_thresholds.py`,
  round 54) on one string: quality work, never depth (prompt `:435-438`); and the description's own `Note:` says the
  file never reaches a router. No landing, no counter committed. considerthese item 5 is therefore not worked this
  round, and **no considerthese proposal is worked**: the round's assimilation duty is carried by C1 (a theme from
  `merge/kotoba/`). The depth obligation moves to C1 (below).

## C1 — redeclared as `depth` (owned, 9); conjuncts added; target stays 4 of 4

**Axis.** `depth`, not `coverage`: the lane's six per-client maps of rounds 55–60 (explicit invocation, agent
definitions, plugin manifests, command files, hook files, scoped rules) were all declared depth, for the same kind
of surface (a per-client table with a located quote per cell, `AXES.md:11`: "decision tables with real thresholds,
named error signatures, cited sources"). `CriticSeparability` V6 asks the claim to name the map it moves: it moves
`PROVINCE.md` § Core (conjunct (f)). Because the lane's lowest owned axis is `depth`, the §2 lowest-axis duty is
met by this claim. Census: `ScoutCnCensus` — 4 of 4 vendors back to the rule on the live pages (7 fetches HTTP
200, snapshot hashes in its report), so the target `N == 4` stands, **not lowered** (the plan's lowering rule did not fire).

**Predicate (unchanged sentence, with the clarifications V7 asks for and three added conjuncts):**

```
python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>  ->  prints "vendor skill surfaces backed N of 4", exit 0 when N == 4
```

- **Clarified (V7).** The manifest is `.ufo/waves/round-73/snapshots/MANIFEST.sha256`; a vendor's table row is the one whose
  `product` cell names `V` (case-insensitive, backticks stripped; the vendor/company column is not the key); a host
  test is a URL prefix (`https://docs.trae.cn/`, `https://www.codebuddy.ai/`, `https://www.kimi.com/`,
  `https://github.com/moonshotai/kimi-cli/`, `https://docs.bigmodel.cn/`). A backticked token matches word-bounded:
  neighbours may be CJK or punctuation, never `[A-Za-z0-9_.-]` (`ExecCnCounter` worlds 20, 21). A path token is matched
  as written first; the counter's frozen ruling for a trailing `/` (`ScoutCnCensus`: the live TRAE page writes
  `~/.trae-cn/skills` without it) is in the counter's docstring and its self-test arms.
- **(e) opened this round (V5, `CriticSeparability`).** Each cited row's `opened` cell equals the entry's `verified-at:`
  cell and the round's capture date `2026-10-25`, and the row's anchor cell records `fetched <ISO8601>Z, HTTP 200, <bytes> B,
  sha256 <hex>` whose sha256 equals the snapshot's pin; any cited row dated otherwise is exit 2 (could not evaluate),
  never a backed vendor. The counter prints `opened this round R of R`.
- **(f) the map moves (V6).** `PROVINCE.md` § Core carries one bullet naming all four vendors and the entry path; the
  counter prints `province surfaces named N of 4` and exit 0 requires `N == 4` as well.
- **(g) registry home (V1).** The tree's own `check_gate_registry.py --rev <rev>` exits 0 and its output names
  `verifiers/check_cn_vendor_surfaces.py` among conformant rows (the counter's own row sits in `SKILL.md`'s registry,
  its protocol home); the counter prints `registry home ok`.
- **Content corrections the entry must carry (seat findings, each re-derived on live pages today):** `ScoutCnCensus` and
  `ExecSrcTrae`: only `~/.trae-cn/skills` (slash-less) is on the TRAE page — no `~/.trae/skills/` "international" root;
  `ExecSrcKimiEn` and `ReviewerDivergence` 3b: the GitHub `kimi-cli` page documents a different layout
  (`~/.kimi/skills/`, `~/.claude/skills/`…) from `www.kimi.com/code` (`.kimi-code`, `whenToUse`…): the Kimi Code row cites
  the kimi.com page only; "translation drift" is refuted as a product/version split; `ExecSrcZhipu` and `ScoutCnCensus`: the
  Zhipu row needs a placement token present on the page (`/v1/skills`); `ReviewerDivergence` 1b/2b: the Qwen allowlist
  "silently dropped" and the CodeBuddy-CLI "examples emit `disable-model-invocation`" sentences are documentary inference
  and unsupported respectively; `ReviewerDivergence`: "all four now read `.agents/skills/`" has 0 hits on CodeBuddy and
  Zhipu pages. The entry states only what its located quotes carry.

Do-nothing control unchanged (base `0 of 4`, exit 1, `held at base: 0`; `ExecCnCounter` evidence). Shortcut worlds:
the seven of the plan plus the draft counter's 47 self-test worlds, plus a world with the staged entry's text
re-pointed at fresh rows but an `opened` date of 2026-10-23 (must exit 2) and a world with `PROVINCE.md`
unchanged (must read `province surfaces named 0 of 4`). Kill rule unchanged.

## C3 — redeclared as `operability` (advisory, 8.5): the tip battery counter runs as documented

**Axis.** `operability` (`AXES.md:13`: "commands that exist, scripts that run": the documented invocation of the counter
produces the stated outcome). `CriticSeparability` V2: a battery reading is not a calibration claim (prompt `:422`: a
calibration claim counts self-assessment mismatches) and moving it onto the `consistency` row's 10 by a gate-health number
is what the old label implied; the consistency row is not claimed.

**Cause (confirmed by two independent reproductions and a counter-side probe).** `verifiers/check_tip_battery.py:609-610`:
`repo = Path(args.repo)`; `fleet = ... else repo.parent`. With the documented `--repo .`, `Path(".").parent` is `Path(".")`:
the sandbox symlinks (relative, self-referential) the lane's own entries, every `../.ufo/…` citation fails, and the
checklist and floors gates exit 1 (`.ufo/waves/round-73/receipts/m127-l1-repro.txt`; `ExecBatteryFix` §1, form A vs form B
at the same rev; `RevengerBatteryDiag`). The gates are right; the counter's derivation is wrong.

**Predicate (replaces the plan's; `CriticSeparability` V3/V4):**

```
python3 -B verifiers/check_tip_battery.py --rev <rev> --repo <lane>  ->  prints "fleet root <realpath>; guards G of 5; tip battery exit 0: N of 6", exit 0 when G == 5 and N == 6
```

measured in **both invocation forms** — `--repo .` from the lane root and `--repo <absolute lane path>` — one run per form,
each wall-timed with its own receipt (a single run takes ~45–150 s; two runs in one invocation would exceed the 300 s
per-command bound); the printed fleet root must equal the real fleet root in both. The five guards, enumerated:
`no-deletions`, `floors`, `instrument-size`, `instrument-pin`, `spotcheck-identity`. Changes frozen with this erratum:
(1) `repo = Path(args.repo).resolve()` and `fleet = Path(args.fleet).resolve() if args.fleet else repo.parent`; a fleet root equal
to the lane is exit 2 (could not evaluate), never a battery reading; (2) the guard base moves to the r73 base `072048f…`, the
cap stays **40** (`instrument-size` then measures this round's delta of the six battery scripts, not r72's growth: arithmetic —
the r72 delta was 76 added / 24 deleted; this round's edit to the six scripts is expected 0; the base figure drops out), and
`corpus/lessons/round-72-verifier-spotcheck.md` is a base file compared by `spotcheck-identity`; (3) the counter's
`--self-test` closes the twelve survivors `MutTipBatteryGuards` found (M05, M06, M07, M10, M12, M13, M15, M19, M20, M21, M22,
M23) — measured by re-running that committed driver on the landed counter — and adds fleet-root arms (relative `--repo`, fleet
equals lane, the wrong parent).

**Do-nothing control:** base `072048f`, form A `fleet root` = the lane itself, `2 of 6`, guards `4 of 5` (instrument-size
FAIL), exit 1 (`receipts/c3-base-battery-counter.txt`); form B `4 of 6` (`receipts/m127-l1-repro.txt`). **Shortcut controls:** the
r72 worlds (`.ufo/waves/round-72/w1/build/ExecBatteryControls/`), plus `ExecBatteryControls` of this round (stubbed gate, lowered
floor, blessed DRIFT values, raised timeout, skipped failing gates, reused second sandbox). Kill rule unchanged.
**Land order** (separability): the C3 commit lands first and contains no new `verifiers/*.py` (the registry gate stays 56 of 56);
the corpus index row for `round-72-verifier-spotcheck.md` and the baseline re-record sit in the same commit (the corpus gates are
two of the six). C1 lands after, with its counter's registry row in its own commit (V1); the six gates are re-run at the final
tip as no-harm evidence, not claim data.

## Frontier step — the mined mistake restated (`CriticMistakeClass`)

`captured-by: none` was false: Q36, Q50 and Q60 existed at the r72 tip, the lane owns report scanners (`check_report_hashes.sh`, Q41)
and a one-off arm for exactly this defect (`check_r67_routed_repairs.py` D2): the r72 pointer drift is the **third recurrence after
capture**, and the SOURCES.md splice is a second class (append placement, invisible to report gates) — two rows in `## Mistakes`.
The fix gate `verifiers/check_report_pointers.py` is not a claim and is held to `ExecPointersGate`'s draft plus
`CriticMistakeClass`'s F3–F5 corrections (token rule, `--round`, no fourth resolver without naming why the three do not apply)
before it lands; if those cannot be met in-round it is not landed and the Mistakes row records `fix: none landed`.
