---
author: kotoba L1 (hyaku run 7, round 73, attempt 1)
date: 2026-10-25
round: 73
lane: kotoba
---

# Round 73 lessons — kotoba

Claims (frozen in `plans/round-73.md` at `b337035fedc2a776fb84c5e885834fe77ed3df98`; errata E1 `3da11a5`, E2 `8c7029c`, freeze 2 `ccac253`
with `plans/round-73-addendum-3.md`): **C1 depth** (sourced, assimilation): four Chinese-vendor skill surfaces, counted by
`verifiers/check_cn_vendor_surfaces.py --rev <rev>`; **C3 operability**: the tip battery counter runs as documented in both
invocation forms, counted by `verifiers/check_tip_battery.py --rev <rev>`. The planned C2 (registry out of `SKILL.md`) and its
replacement (own description) were withdrawn before any data — see § Round honesty. Round shape: two v1 waves (wave 1 dispatched 36, 34 spawned).

## Gate

Assimilation theme (addendum §10; nothing written, run or fetched inside `/home/vgpnk/Projects/shokuknow`): **the Chinese-vendor skill
surfaces** from `merge/kotoba/` — staged entry `chinese-client-skill-surfaces.md` (staged rows S214, S216, S217, S218, S219, S221).

**Id collision check** (`.ufo/waves/round-73/assimilation/`): the lane registry held 142 ids (`reg-ids`), the package stages 188
(`staged-ids`), `collisions` lists 14 — `S203`–`S216`, the lane's own rows from rounds 69–72, which the package numbered earlier.
**Guard proof:** `assimilation/guard-proof/proof.txt` (a scratch registry with an indented row yields the id under the 0–3-space pattern and
not under the column-zero pattern; `mirror-e03.txt` shows the guard catching a duplicate id). **Renumber map, by document (URL), not arithmetic:**
staged S214 `docs.trae.cn/ide_skills` → **S217**; staged S216 CodeBuddy IDE → **S218**; staged S217 CodeBuddy CLI → **S219**; staged S219
`www.kimi.com/code/…/skills.html` → **S220**; staged S218 `moonshotai/kimi-cli` GitHub page → **S221**; staged S221 Zhipu → **S222**. Staged rows
are campaign-schema: the lane rows were rewritten in the 11-column schema (no `|` in a cell; `recheck` `60d`; `used-by` the one admitted entry; `opened`
2026-10-25; anchors carry the fetch record). The staged rows' own `scope`, `anchor` and `teaches` cells were **not** copied: they carry the
package's 2026-10-23 opening. Scratch validation before the registry append: `assimilation/validate-final/census.txt` (the base registry plus the six
final rows plus the entry, `scripts/sources-census.sh validate --file …` exit 0; the full mirror was trimmed after the run, its SOURCES.md kept).
Stripped staged recheck prose is recorded in `assimilation/../w1/build/ExecIdNormalize/gate-notes.md` (not adopted).

**Rows opened this round** (all fetched by a wave-1 seat and re-fetched by the L1: raw sha256 identical in both fetches; the TRAE URL answers HTTP
400 without a browser user agent):

- **S217** — https://docs.trae.cn/ide_skills; snapshot `.ufo/waves/round-73/snapshots/cn-trae-skills.md:193-195`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "项目技能：项目所在路径下的 `.trae/skills/` 目录。 全局技能： macOS/Linux：本地根目录 `~/.trae-cn/skills`。"
- **S218** — https://www.codebuddy.ai/docs/zh/ide/Features/Skills; snapshot `.ufo/waves/round-73/snapshots/cn-codebuddy-ide-skills.md:157`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "每个 Skill 由一个必需的 `SKILL.md` 文件和可选的打包资源组成。Skill 应建立在工作区的 `.codebuddy/skills/` 目录下。"
- **S219** — https://www.codebuddy.ai/docs/zh/cli/skills; snapshot `.ufo/waves/round-73/snapshots/cn-codebuddy-cli-skills.md:921-925`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "Skills 通过在特定目录中创建 `SKILL.md` 文件来定义： 项目级 Skills：`.codebuddy/skills/`（项目根目录下） 用户级 Skills：`~/.codebuddy/skills/`（用户主目录下）"
- **S220** — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html; snapshot `.ufo/waves/round-73/snapshots/cn-kimi-zh-skills.md:273-281`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "按作用域分四档扫描，越具体的作用域优先级越高：Project > User > Extra > Built-in。 用户级（对所有项目生效）： `$KIMI_CODE_HOME/skills/`（默认：`~/.kimi-code/skills/`） `~/.agents/skills/`"
- **S221** — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md; snapshot `.ufo/waves/round-73/snapshots/cn-kimi-en-skills.md:34-37`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "**Brand group** (mutually exclusive): 1. `~/.kimi/skills/` 2. `~/.claude/skills/` 3. `~/.codex/skills/`"
- **S222** — https://docs.bigmodel.cn/cn/managed-agents/skills.md; snapshot `.ufo/waves/round-73/snapshots/cn-zhipu-skills.md:83`; access date 2026-10-25 (L1 re-fetch 2026-10-26T00:34:39Z, HTTP 200); quote (whitespace-collapsed snapshot text, ≤25 words, code spans are the snapshot's own backticks): "Skill 非空时必须同时声明 agent\_toolset\_20260601；Agent 使用的 Skill 最多 20 个，目录不得重复。运行目录为 `/workspace/skills/<目录名>/`，按需读取。"

Fetch record per page: `.ufo/waves/round-73/snapshots/FETCH-LOG.tsv`; snapshots pinned in `snapshots/MANIFEST.sha256`; the snapshot of each HTML page is
reproducible from the raw bytes with `snapshots/extract_html.py` (checked for TRAE: `cmp` identical). The anchor cell of each row carries `fetched
<ISO8601>Z, HTTP 200, <bytes> B, sha256 <snapshot sha>`; the Z date is 2026-10-26 because the L1 re-fetch ran at 21:34 local (UTC−3) — the row's `opened`
cell is the local round date 2026-10-25.

**Admitted:** `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (six rows; documentary evidence only). Expansion credit: ground the coverage
map did not hold — `grep -rniE 'trae|codebuddy|kimi code|kimi-code|zhipu|bigmodel|moonshot' corpus SKILL.md PROVINCE.md` printed one line at the base (a host
config path, `corpus/knowledge/opencode-offer-trace-round8.md:84`; `receipts/base-sweeps.txt`).
**Entry rewrites forced by this round's opening** (staged claims the live bytes do not carry; each re-derived on the live page, evidence
`.ufo/waves/round-73/w1/ScoutCnCensus.md`, `ExecSrcTrae.md`, `ExecSrcKimiEn.md`, `ExecSrcZhipu.md`, `ReviewerDivergence.md`): `~/.trae/skills/` "international" root absent (0 hits);
the GitHub Kimi page documents `~/.kimi/skills/`, `~/.claude/skills/` and not `.kimi-code` (a product/version split, "translation drift" refuted); the Zhipu
row needed a placement token the page carries; "all four read `.agents/skills/`" has 0 hits on the CodeBuddy and Zhipu pages (two of four); the CodeBuddy-CLI
"examples emit `disable-model-invocation`" is one occurrence in the frontmatter table; the Qwen allowlist "silently dropped" is inference.
**Rejected, with reason and flip** (Q62: each on an observed fact): (1) staged `client-surface-census-extension.md` (Qwen Code, staged S205–S208): its
`allowedTools` sentence holds on the English page only (`ReviewerDivergence` 1a) and a fifth client would move C1's frozen vendor set; flip: a round that
declares Qwen Code a client of its own claim. (2) staged `translation-drift-across-vendors.md`: refuted by the Kimi pages — both languages exist on both
hosts and the difference is layout/version (`ReviewerDivergence` 3b); flip: a vendor page stating a translation-only difference. (3) staged
`trae-build-vs-translation-axis.md`: translation commentary, another lane's ground (`ConnScopeSiblings`: refuse); flip: a TRAE page that documents a skill
surface for the second build. (4) `skill-craft-rules-from-chinese-vendors.md` and `skill-body-authority-and-context-placement.md`: pointer-only (their rules
rest on rows no admitted entry cites; CORPUS rule 4). Staged rows not appended: S215 (TRAE best practice), S220 (Kimi hosted agents), S205–S208 (Qwen),
and every other row of the package (no admitted entry cites them). **Quarantine:** the 13-row register slice (`assimilation/quarantine-slice`, re-derived this
round: 13 data rows, each with an S id) holds no row this round's entry cites — none is appended; the round-72 hand-check verdicts
(`corpus/lessons/round-72.md` § Gate) stand.
**Spot-check sample for the non-author closure (≥1 admit, ≥1 reject):** admit S220 (kimi.com page) and S222 (Zhipu `/workspace/skills/<目录名>/`); reject the
Qwen entry (flip above) and the "translation drift" claim (refuted by the two Kimi pages, `cn-kimi-zh-skills.md` vs `cn-kimi-en-skills.md` root counts `2 0` and `0 2`).

**considerthese:** none worked. `considerthese/2026-10-25.md` item 2 (registry out of `SKILL.md`) contradicts `PROTOCOL.md:398`; item 5 (own description) was
withdrawn after two wave-1 attacks. The frontier mining for this round is `merge/kotoba/`; considerthese items 1, 2, 4 and 5 stay open (item 2 is an L0 question).

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M128 | reference-drift (third recurrence after capture) | the r72 report cited `tip-check_tip_battery.txt` and `receipts/tip-check_substrate_repin_v2.txt`, which exist at no revision (`receipts/pointers-red-before.txt`: `34 of 37; unresolved 3`) | Q36, Q50, Q60 (prose; Q60 was minted for this defect in r64) — each existed at the r72 tip and none is a command that opens a report | `verifiers/check_report_pointers.py`, red-before on the r72 report at the r72 tip (exit 1); green-after on the r73 report is run before filing and cited in the report |
| M129 | scope (append placement) | `corpus/SOURCES.md` at `072048f` lines 214 and 217: the r72 note inserted inside the r64 note; the census exits 0 on it (`CriticMistakeClass` F7) | none | an appended correction note (this round); **no structural guard landed** — a section-order check is a candidate, so the fix is not counted as shown able to fail |
| M130 | counter defect (path derivation) | `verifiers/check_tip_battery.py:609-610` derived the fleet root from `Path(args.repo).parent`; with `--repo .` that is the lane, the sandbox's `../` citations died and two gates read red against the same gates by hand (`receipts/m127-l1-repro.txt`; r72's M127 "unresolved") | none — the self-test never drove `main()` with a relative `--repo` (mutant M23 survived, `MutTipBatteryGuards`) | `Path(args.repo).resolve()`, fleet-equals-lane is exit 2, six new arms; M23 now killed (`receipts/c3-mutation-rerun.txt`: 22 of 23 killed, M10 equivalent); both invocation forms read `6 of 6` (`receipts/c3-formA-11b05d9.txt`, `c3-formB-11b05d9.txt`) |
| M131 | landing (seat identity) | `w1-results.json`: seats `CriticC1Counter` and `CriticC3Counter` returned kake r57's work — the dispatcher keys handles by seat name, so my same-named seats were skipped (34 of 36 spawned); I messaged Main | none | lane-unique seat names in every wave (wave 2 names end `-R73`); Q69 |
| M132 | stale-premise | the plan's C2 moved the 56 registry rows out of `SKILL.md`; `PROTOCOL.md:398,418-421` makes `SKILL.md` the registry home and closure grades no gate conformant without a row there — found by my reading of PROTOCOL after freezing | none (the load order names PROTOCOL.md; I read § Gate standard after the plan froze) | E1 before any data, an L0 question for item 2; Q67 |
| M133 | vacuous (caught before data) | addendum-1 C2 read `3 of 3` on nine descriptions that were worse for a reader (`w1/CriticC2Counter.md`, `counter-world-scores.txt`) | the §9 shortcut-control rule worked — nine worlds met the counter on the drafted instrument | claim withdrawn before data (E2); recorded as a control that did its job, not as a fix |

## Routed defects (r72 spot-check § 6)

1. M127 / honest `instrument-size` cap → C3: cause fixed (M130); the cap stays 40 and is measured against the r73 base (`LINE_CAP` comment in the counter).
2. The skipped falsify wave → wave 2 of this round (see the report for seats).
3. SOURCES.md search-log damage → appended correction note (M129); no in-place rewrite.
4. `resident-index-and-rungs-round72.md:45` → "format's rules." (one line, `LOG.md` § Round 73).
5. Receipt filenames cited by the r72 report → named in the r73 report as a correction (never a rewrite of the r72 report); gate: `check_report_pointers.py`.
6. SHONEN boxes stay `[~]`; no non-author verifier is available to this lane.

## Round honesty

The planned C2 and its replacement were withdrawn before data (E1: protocol conflict; E2: two attacks), so the round carries two claims. Wave 1 dispatched 36
seats and 34 spawned (M131). The wave sat in the dispatcher queue about 70 minutes behind other lanes' waves; it was re-sized from 49 to 36 seats to fit the
shared capacity rule (`plans/round-73.md` is unchanged by that).

## Status changes

S217–S222 `mined` at landing (new rows, no change to an existing row). No other `status`, `recheck` or `used-by` cell changes.
