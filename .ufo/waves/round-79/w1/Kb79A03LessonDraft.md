# Kb79A03LessonDraft — round 79 lesson draft (`corpus/lessons/round-79.md`)

Deliverable: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A03LessonDraft.md` — 12,263 B, 67 lines, sha256 `d105f3b349c78dfe4e79e47e7289acdb107e2d1e7f81583bdd9b1bd81e5d52f0`. Nothing was written into `corpus/lessons/`; the L1 integrates the draft after the wave. No counter was run and no claim data was scored on the frozen C1/C2 counters.

## Requirement → draft location

| Requirement (seat item) | Where it landed |
|---|---|
| round-77/78 shape (title, base+author line, Gate, Mistakes, Sources & frontier) | whole file; base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`, author `KotobaR79` |
| one admit candidate = the six C2 rows + the allowed-tools entry | `## Gate`, six `S226`–`S231` bullets, entry path named, plus the (g)/(h)/(i) tree-conjunct lines |
| per new row: URL, access date, ≤25-word located quote | each bullet carries URL, `accessed 2026-10-27`, and `{{QUOTE_Sxxx}}`/`{{WC_Sxxx}}` markers for the L1 to fill from the row seats (S226 spec, S227 claude, S228 factory, S229 msaf, S230 pi, S231 vibe) |
| grant label + page token per row (plan §C2 (f)) | each bullet names the frozen label (`experimental`/`pre-approves`/`metadata-only`/`unstated`) and the token its quote must carry |
| one reject candidate (negative-sweep scouts + census seat) | `## Gate`, first two reject bullets: twelve client pages (S01–S04) and the S08 extension sample (Qwen Code) |
| staged merge/kotoba entry as NOT adopted, one line, ids collide + nothing re-grounded | `## Gate`, third reject bullet, with the header's four campaign ids (S250/S252/S255/S256) and the r77 23-collision pointer |
| status/recheck/used-by changes old→new | `## Gate`, "Registry changes … none", plus the diff command and its `{{ROW_DIFF}}` slot |
| considerthese proposal-1 disposition (byte ceiling, base figures, no new rule) | `## Gate`, final bullet |
| `## Mistakes` table with the round's mined mistake (landing; Q50/Q65; fix C1 + per-rev receipts) | `## Mistakes`, row 1; a second row for the number-drift class r77 already mined; the sweep block below the table |
| the sweep command the mistake-sweep scout produces | `{{MISTAKE_SWEEP_CMD}}` block, fill from `w1/Kb79S05MistakeSweep.md` (that seat had not landed a report when this draft was written), plus this seat's own verified sweep with output |
| `## Sources & frontier`: census before/after, row counts 151 before, tiers, `Assimilation: none`, spot-check pending | `## Sources & frontier` |

## Checks this seat ran (receipts)

Receipt: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A03-base-figures.txt` (whole `{ … } > receipt; echo receipt-exit=$?` block → `receipt-exit=0`), contents:

```
git -C <lane> show b10bcbc6…:SKILL.md > $S/SKILL.md   show-exit=0
bytes: 78647      lines: 590
gt120=147 gt200=129 gt300=77 longest=1095             awk-exit=0
gate-registry-section-bytes: 24809
sources-rows: 151                                     grep-exit=0
```

The row-count command is `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (151). Census before re-read: `receipts/census-before.txt` ends `kotoba ok …/corpus/SOURCES.md` / `exit=0`, with `grep -c 'W04'` → `20`. The base battery receipt re-read: `guards 5 of 5; tip battery exit 0: 1 of 6`, `exit=1`, red gates `check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`, green `check_correction_sweep.py`.

Draft-time mistake sweep (exit 0), quoted in the lesson with its exact output:

```
for r in 76 77 78; do n=$(ls .ufo/waves/round-$r/receipts/ 2>/dev/null | grep -ciE 'batter|tip'); f=/home/vgpnk/Projects/shokunin/.ufo/reports/round-$r/kotoba.md; c=$(grep -coiE 'tip battery|no-harm battery' "$f" 2>/dev/null); printf 'round-%s battery-or-tip-receipts=%s report-battery-mentions=%s report=%s\n' "$r" "${n:-0}" "${c:-0}" "$([ -f "$f" ] && echo present || echo ABSENT)"; done
→ round-76 battery-or-tip-receipts=2 report-battery-mentions=2 report=present
  round-77 battery-or-tip-receipts=6 report-battery-mentions=1 report=present
  round-78 battery-or-tip-receipts=0 report-battery-mentions=1 report=present
```

`ls -d .ufo/waves/round-78/receipts` → `No such file or directory`; `/home/vgpnk/Projects/shokunin/.ufo/reports/round-78/kotoba.md:29` reads `- quality — unchanged: … no-harm battery not run.` `find . -name 'run-battery*'` (lane and `scripts/hyaku/`) → no output, which is why the fix row states that adding the runner is its first step instead of citing a script that does not exist.

## Rejections recorded, with their sources

- Twelve client pages: S01 (`w1/Kb79S01SilentA.md` — Codex bounded `silent`, VS Code `not checked` with two `microsoft/vscode` `.github/skills/*/SKILL.md` example hits, GitHub Copilot CLI page not fetched), S02 (`opencode`, Gemini CLI, Cursor), S03 (Amp, Roo Code, Kilo Code), S04 (JetBrains Junie, Hermes Agent, Goose) — 11 of 12 `not checked`, no `silent`/"documents nothing" claim and no S232+ row.
- S08 (`w1/Kb79S08CensusRederive.md`): the six-page literal-field population reproduces (all HTTP 200, ≥1 occurrence); Qwen Code documents `allowedTools` (camelCase) with a 16-word quote — recorded as a later-round candidate, not a row.
- Staged entry `client-frontmatter-and-discovery-divergence.md`: not adopted — its S250/S252/S255/S256 are campaign ids colliding with the lane registry (`corpus/lessons/round-77.md:9`, 23 staged collisions), none of its four pages was reopened this round (S06 fetched only the six C2 surfaces), and it carries no per-client semantics.

## Marker checklist (22 markers, each once)

| Marker | Fill from |
|---|---|
| `{{QUOTE_S226}}`…`{{QUOTE_S231}}` (6) | the row seats' reports: `w1/Kb79R01SpecRow.md`, `Kb79R02ClaudeRow.md`, `Kb79R03FactoryRow.md`, `Kb79R04MsafRow.md`, `Kb79R05PiRow.md`, `Kb79R06VibeRow.md` — the located quote, unmodified; it must carry the bullet's token or the surface stays unbacked |
| `{{WC_S226}}`…`{{WC_S231}}` (6) | word count of each filled quote, ≤25 |
| `{{ROWS_LANDED}}` | the S-ids actually committed by the L1 (expected S226–S231) |
| `{{SCRIPT_ONLY}}` | `check_allowed_tools.py` self-test line `script-only world: M of 6` |
| `{{TIP_REV}}` | the final lane tip revision the C1 receipt measures (both `--repo` forms) |
| `{{ROW_DIFF}}` | output of the Gate's diff command at `{{TIP_REV}}` (expect six `+` lines S226–S231, no `-` line) |
| `{{MISTAKE_SWEEP_CMD}}` | the command block in `w1/Kb79S05MistakeSweep.md`; if that seat died, delete the block and keep the draft-time sweep already quoted |
| `{{CENSUS_AFTER}}` | round-end `sources-census.sh validate --root … kotoba` output and exit code (exit 0 required) |
| `{{ROW_COUNT_AFTER}}` | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at the tip |
| `{{TIER_A}}` `{{TIER_B}}` `{{TIER_C}}` (3) | tier counts of the six new rows as committed (each cited row must be tier A or B) |

## Limits and scope

- `w1/Kb79S05MistakeSweep.md` had not landed when this draft was written (checked repeatedly up to the end of the seat); its command is a marker and a verified substitute sweep is already in the lesson, so the section is not hollow if the scout never reports.
- No quote was filled: the item assigns quotes to the row seats and the L1's post-wave fill.
- No counter, gate or battery was executed by this seat. `check_allowed_tools.py` does not exist at base (it is built this wave), so no C2 value is asserted anywhere; no C1 value is asserted beyond the committed base receipt.
- Writes: the draft, `build/Kb79A03-base-figures.txt`, this report. No lane file, jj state, git index or fleet file was touched; no git/jj mutating command was run.
- Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79A03LessonDraft` (held one `SKILL.md` copy, `TMPDIR` passed explicitly) — removed in the same command (`rm -rf -- "$S"`); nothing left on disk.
- Tool installs/upgrades: none.

VERDICT: Lesson draft complete in shape and in every mandated section; grounded values come from committed receipts and from commands run this seat (exit codes recorded), and 22 L1-fill markers remain, each listed above with its source.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A03LessonDraft.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A03-base-figures.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79A03LessonDraft.md
