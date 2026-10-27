# Round 79 — kotoba (attempt 1)

Base: `b10bcbc6b00f8f56b202ccbadca311007b5b463c`; author: `KotobaR79`. Two declared claims on distinct axes: **C1 consistency (calibration sub-axis)** — `check_tip_battery.py` must print `guards 5 of 5` and `tip battery exit 0: 6 of 6` at the tip, both `--repo` forms, against `1 of 6` at base (`.ufo/waves/round-79/receipts/tipbattery-base-dot.txt`, `-abs.txt`) — and **C2 depth (sourced)** — `check_allowed_tools.py` must print `allowed-tools surfaces backed N of 6`, N ≥ 5, against `0 of 6` at base, over rows S226–S231 and the entry `corpus/knowledge/allowed-tools-surfaces-round79.md`. This lesson is the round's frontier record: the gate disposition, the mined mistake and the SOURCES census.

## Gate

Admitted — six new SOURCES rows, each opened this round (2026-10-27), each cited by the new entry `corpus/knowledge/allowed-tools-surfaces-round79.md`, whose header opens `source:` lines for all six ids, then `verified-at: 2026-10-27`, then `recheck:`. The grant label per row is the plan's frozen label; the located quote must carry the page token shown.

- S226 — Open specification — https://agentskills.io/specification.md — accessed 2026-10-27 — grant label `experimental` (quote must carry `Experimental`) — located quote ({{WC_S226}} words): “{{QUOTE_S226}}”
- S227 — Claude Code — https://code.claude.com/docs/en/skills.md — accessed 2026-10-27 — grant label `pre-approves` (quote must carry `without asking permission`) — located quote ({{WC_S227}} words): “{{QUOTE_S227}}”
- S228 — Factory — https://docs.factory.ai/cli/configuration/skills — accessed 2026-10-27 — grant label `metadata-only` (quote must carry `does not add tools`) — located quote ({{WC_S228}} words): “{{QUOTE_S228}}”
- S229 — Microsoft Agent Framework — https://learn.microsoft.com/en-us/agent-framework/agents/skills — accessed 2026-10-27 — grant label `experimental` (quote must carry `Experimental`) — located quote ({{WC_S229}} words): “{{QUOTE_S229}}”
- S230 — pi — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md — accessed 2026-10-27 — grant label `experimental` (quote must carry `Experimental`) — located quote ({{WC_S230}} words): “{{QUOTE_S230}}”
- S231 — Mistral Vibe — https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md — accessed 2026-10-27 — grant label `unstated` (quote must carry `allowed-tools:`) — located quote ({{WC_S231}} words): “{{QUOTE_S231}}”

Every cited row is an 11-cell registry row, status `mined`, tier A or B, `used-by` naming the entry, host+path-prefix equal to the surface's frozen host; its snapshot under `.ufo/waves/round-79/snapshots/` carries the sha256 pinned in `MANIFEST.sha256` and in its anchor cell's fetch record. A row seat that used another URL form on the same host and path prefix, because the first form returned no usable text, says so in its report and in the row's anchor cell. The parenthesised token in each row line is the frozen (f) page token: a quote that omits it fails (d)/(f), and no quote is bent to fit — the L1 substitutes a located quote that carries the token, or that surface stays unbacked. Rows landed: {{ROWS_LANDED}}. The counter's tree-level conjuncts (g) one `SKILL.md` rule line citing the entry path and naming ≥3 surfaces plus a conformant `gate` registry row, (h) one `PROVINCE.md` `## Core` bullet naming the entry path, (i) the `script-only world: {{SCRIPT_ONLY}} of 6` self-test line — are reported on their own lines; a script-only world reaching the field evidence is declared form-level, never semantic proof.

Rejected — screened, not admitted, each as its own record rather than a row:

- Twelve client pages screened by the four C2 negative-sweep scouts. Nine are recorded `not checked` because the Q30 four-part sweep did not complete (GitHub code search answers HTTP 401 unauthenticated; `<url>.md` routes answer 404): opencode, Gemini CLI, Cursor (`w1/Kb79S02SilentB.md`); Amp, Roo Code, Kilo Code (`w1/Kb79S03SilentC.md`); JetBrains Junie, Hermes Agent, Goose (`w1/Kb79S04SilentD.md`). Their fetched bytes carry no `allowed-tools`/`allowedTools` occurrence in raw or tag-stripped text, and that is all they establish: no `silent`/`documents nothing` verdict and no S232+ row is claimed, and a later round that wants one must finish the source-tree sweep or record the limitation. The tenth, Codex, reads `silent (sweeps 1–4 all empty)` inside a 120 s-capped tree walk (`w1/Kb79S01SilentA.md`); the eleventh, VS Code / Copilot in VS Code, is `not checked`, and its row seat found the key present in two `.github/skills/*/SKILL.md` examples in the `microsoft/vscode` tree — examples that carry the field but document no VS Code client semantics, so no row; the twelfth, GitHub Copilot CLI/cloud, has no fetched page and is `not checked`.
- Census re-derivation (`w1/Kb79S08CensusRederive.md`, independent fetch 2026-10-27, not re-fetched by this seat): the six-page literal-`allowed-tools` population reproduces — all six return HTTP 200 with at least one occurrence — and one extension client is a candidate for a later round, **not** a row this round: Qwen Code, https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/ — “Qwen Code reads the allowedTools frontmatter field. An allowed-tools field written for another agent is ignored.” (16 words) — camelCase spelling only, so it does not enter a census frozen on the literal token `allowed-tools`. Six further pages returned 200 with zero occurrences (Windsurf, Cline, Zed, Kiro steering, JetBrains AI Assistant, Aider conventions): fetched bytes only, no negative sweep, so `not checked`; eight URLs returned 404 (Continue, Warp, Augment, Crush, OpenHands, Cody, Devin, both Goose candidates) and a 404 is not evidence of absence.
- Staged package entry `client-frontmatter-and-discovery-divergence.md` (merge/kotoba, `verified-at: 2026-10-23`; header cites S250 Deep Code, S252 Junie, S255 `agentskills.io/skill.md`, S256 client-implementation) — **not adopted**: its ids are campaign ids that collide with the lane registry (`corpus/lessons/round-77.md:9`: 23 staged ID collisions) and nothing in it was re-grounded this round (none of its four cited pages was reopened; the C2 cross-check fetched only the six C2 surfaces, `w1/Kb79S06AssimStaged.md`), and it states no per-client `allowed-tools` semantics to adopt (its sole mention is the specification's frontmatter list).

Registry changes — `status` / `recheck` / `used-by`: **none**; no existing row is edited, and the six new rows carry `mined` from the moment they land. The check is the diff itself, which must show only `+` lines for S226–S231 and no `-` line:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff b10bcbc6b00f8f56b202ccbadca311007b5b463c..{{TIP_REV}} -U0 -- corpus/SOURCES.md | grep -E '^[-+]\|'
```

{{ROW_DIFF}}

considerthese `2026-10-26.md` proposal 1 (byte ceiling, max-line check) — mined as a measurement, **no new rule claimed**. Measured at base `b10bcbc6`: `SKILL.md` 78,647 B, 590 lines, 147 lines over 120 chars, 129 over 200, 77 over 300, longest 1,095; `## Gate registry` 24,809 B, 31.5 % of the file (`build/Kb79A03-base-figures.txt`, exit 0; independent re-derivation with per-file table in `w1/Kb79S07BudgetCensus.md`). A 70,000-byte ceiling is falsifiably red-before by 8,647 B at this base, while the existing `trigger.line_budget` gate counts lines only (590 of 600) — so the line cap passes while the file grows. Proposal 1 stays a proposal: a byte ceiling would have to enter the floors guard through its own round with its own do-nothing control, and a ceiling written this round would be a rule changed after data. Proposals 2–5 not taken (proposal 2 is an L0 matter, Q67).

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| landing | `.ufo/waves/round-79/receipts/tipbattery-base-dot.txt` (and `-abs.txt`): at base `guards 5 of 5` but `tip battery exit 0: 1 of 6`, exit 1 — red `check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`; rounds 76, 77 and 78 each closed without the no-harm battery being completed | Q50 (a gate result stated for the tip carries a committed receipt naming that exact revision) and Q65 (a plan's no-harm battery runs at its own base before the plan freezes, and what is red is named red) — both criteria existed and neither was run | C1 of this round, plus a battery receipt per revision: one runner invoked per measured revision, each receipt recording `cmd > out 2>&1; rc=$?` and the revision it measured. No `run-battery*` script exists at base (`find . -name 'run-battery*'` → no output), so adding that runner is the fix's first step; until it exists the plan's named battery commands are run one at a time and each receipt names its revision. |
| number-drift | `corpus/lessons/round-77.md` § Mistakes row 4: r76's `base-battery.txt` captured a pipeline `tail` status, not the verifier's (`plans/round-76-addendum-2.md`, `base-gate-correction.txt`); the same defect class is what makes a battery unusable as a tip receipt | Q36 (a count carries its command) and Q50 (a tip result carries a receipt naming that revision) | Every battery receipt captures the child command's own status, `cmd > out 2>&1; rc=$?`, and names the revision it measured — the receipt form C1's `run-battery.sh` must emit. |

Sweep that found the landing row — the mistake-sweep scout's command (rounds 76–78 of this lane class by class); the L1 fills the block from `w1/Kb79S05MistakeSweep.md`:

```sh
{{MISTAKE_SWEEP_CMD}}
```

Draft-time sweep run by this seat over the same three rounds (exit 0): each round's battery/tip receipts against its report's battery mentions.

```sh
for r in 76 77 78; do n=$(ls .ufo/waves/round-$r/receipts/ 2>/dev/null | grep -ciE 'batter|tip'); f=/home/vgpnk/Projects/shokunin/.ufo/reports/round-$r/kotoba.md; c=$(grep -coiE 'tip battery|no-harm battery' "$f" 2>/dev/null); printf 'round-%s battery-or-tip-receipts=%s report-battery-mentions=%s report=%s\n' "$r" "${n:-0}" "${c:-0}" "$([ -f "$f" ] && echo present || echo ABSENT)"; done
```

```
round-76 battery-or-tip-receipts=2 report-battery-mentions=2 report=present
round-77 battery-or-tip-receipts=6 report-battery-mentions=1 report=present
round-78 battery-or-tip-receipts=0 report-battery-mentions=1 report=present
```

`round-78` is the sharpest cell: `.ufo/waves/round-78/receipts/` does not exist (`ls -d` → `No such file or directory`) and the report's own line 29 reads “no-harm battery not run” — an honest statement that the criterion was skipped, which is exactly what three skipped rounds accumulate into: five of six tip gates red at the r79 base (`receipts/tipbattery-base-dot.txt`).

## Sources & frontier

SOURCES census before: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`, 20 `W04 duplicate url` warnings (`.ufo/waves/round-79/receipts/census-before.txt`). Row count before, `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `151` (exit 0, `build/Kb79A03-base-figures.txt`; next id S226 as planned). Census after: {{CENSUS_AFTER}}. Row count after: {{ROW_COUNT_AFTER}}.

Rows added by tier: A `{{TIER_A}}`, B `{{TIER_B}}`, C `{{TIER_C}}` — S226–S231, each cited by the C2 entry; the frozen predicate (b) admits only tier A or B, so a C tier on any of the six is a red row, not a softer one. No row is added without an admitted entry citing it. Rows touched: none; every pre-existing row keeps its `status`, `recheck` and `used-by` cells (the diff command and its observed output are in the Gate section).

Assimilation: **none**. The staged package entry is read-only input to the C2 cross-check and nothing is appended from it — ids collide with the lane registry and no entry was re-grounded this round (Gate, rejected). Outside spot-check: pending non-author closure — no non-author judgment of this round exists yet.
