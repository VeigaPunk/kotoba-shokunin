Result: HOLDS — the round-57 Frontier note at `corpus/README.md:147-155` re-derives exactly: `4 of 4; new ground 4` (C1-measure.txt) and `105 of 171` (ExecC2FleetBefore.tsv, counting command below), every relative path resolves from `corpus/`, no Core claim is made, and the plugin row is correctly described as recorded-not-held.

Seat: A3ReviewFrontierNote (reviewer, falsify wave). Read-only lane verification at `07c33d73ddce769d9cea2846a6313164401b5478`. No subagent dispatch, no tool installs, no git writes.

## F1 — `4 of 4; new ground 4` re-derived (VERIFIED)

- Receipt `.ufo/waves/round-57/C1-measure.txt:5` (fetch run): `plugin manifests found on the live page 4 of 4; new ground 4`, `exit 1` (line 13). The note's quoted `found on the live page 4 of 4; new ground 4` is a byte-exact substring of that line (prefix `plugin manifests` elided; on change of meaning).
- Print format matches frozen counter `verifiers/check_plugin_manifests.py:1024`. File sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` == frozen counter v2 (C1-measure.txt:3) — the receipt ran the frozen counter.
- Predicate (verifier:173, 181-182): exit 0 iff F >= 5 AND G >= 3. F=4 < 5 => exit 1; G=4 >= 3. The note's "short of its F >= 5 target" is the operative, binding clause; it omits the G >= 3 conjunct, but G is satisfied, so the statement is accurate.
- "recorded, not held as a verified claim" matches the declared miss (goal: F >= 5 and G >= 3 not met).

## F2 — `105 of 171` re-derived (VERIFIED)

Counting command (over `.ufo/waves/round-57/build/ExecC2FleetBefore.tsv`):

```
$ wc -l ExecC2FleetBefore.tsv
171 ExecC2FleetBefore.tsv
$ awk -F'\t' '{print $4}' ExecC2FleetBefore.tsv | sort | uniq -c
    105 info-less fence
     39 inline span
     27 shell-tagged fence
$ awk -F'\t' '$4=="info-less fence"' ExecC2FleetBefore.tsv | wc -l
105
$ awk -F'\t' '$4=="info-less fence" && $5=="real command"' ExecC2FleetBefore.tsv | wc -l
0
```

- 105/171 info-less fence matches the note exactly; 105+39+27 = 171 (all rows accounted).
- "none of them a real command": exactly 0 info-less rows carry shape `real command` (shapes: key: value 45, other 27, table 18, arrow 15 = 105). Corroborated by the build report `ExecC2FleetBefore.md:85` (`real command | 0`) and `:98-101` (no head is a binary, no argument is a command path).
- TSV provenance: header-free, columns `lane, head, line, source, shape, subject` (ExecC2FleetBefore.md:218-224); 171 rows = FAIL subjects across 10 lanes measured from 18 lanes with a root SKILL.md (3 skipped, no SKILL.md). "fleet FAIL subjects" is accurate for this fleet-wide instrument run.
- Note's `(lessons/round-57.md` § Gate; redesign inputs in the round's build wave): resolves (see F3); redesign inputs are the build wave's before-state/rule artifacts (ExecC2FleetBefore.tsv/.md, ExecC2CounterV3.md, CriticC2Rule.md, MutC2Rule.md, ReviewC2Counter.md, ScoutC2Source.md); plan `plans/round-57.md:131-132` states "C2 seats produce redesign inputs only".

## F3 — every relative path resolves from `corpus/` (VERIFIED)

| note text | resolved from `corpus/` | present |
|---|---|---|
| `knowledge/plugin-manifests-round57.md` | `corpus/knowledge/plugin-manifests-round57.md` | yes (S079–S085 rows in `corpus/SOURCES.md:92-98`) |
| `lessons/round-57.md` § Gate | `corpus/lessons/round-57.md:8` | yes |
| `../SKILL.md` § Plugin manifests by client | `SKILL.md:111` | yes |
| `../verifiers/check_plugin_manifests.py` | `verifiers/check_plugin_manifests.py` | yes (sha256 == frozen v2) |
| S028 base row | `corpus/SOURCES.md:41` | yes (legacy plugin fields per the CLI plugin reference, unchanged) |

## F4 — no Core claim; plugin row recorded-not-held (VERIFIED)

- The note text never uses "Core"; it explicitly frames the plugin half as "recorded, not held as a verified claim". That framing is correct: the frozen counter miss means the claim is not held, and the knowledge is documented (corpus/knowledge + SKILL.md section) but not verified.
- The parenthetical content matches the knowledge file row rule (`corpus/knowledge/plugin-manifests-round57.md:9`): "Claude Code, Codex, Gemini CLI and Cursor document an own-format path; VS Code and Copilot CLI default to the shared Agent Plugins root `plugin.json`; opencode plugins are code modules with no JSON manifest" — exactly four own-format clients, VS Code/Copilot shared root, opencode code modules. Row quotes corroborate (S079 `.claude-plugin/plugin.json`; S080 `.codex-plugin/plugin.json`; S083 `gemini-extension.json`; S084 `.cursor-plugin/plugin.json`; S081/S082 root `plugin.json`; S085 `.opencode/plugins/` module).
- "met by four hollow controls before data and the claim was withdrawn": lesson § Gate Rejected lists exactly four C2 v1 controls (CtlC2GeneratorKeyed, CtlC2DoNothingJunk, CtlC2CharShortcuts, MutC2Counter); plan `plans/round-57.md:124` — "C2 — withdrawn before data." C2 is not a claim this round.

## F5 — PROVINCE.md round-57 line: NOT required

Recommendation: no round-57 line should be added to `PROVINCE.md`, for these reasons:

1. `PROVINCE.md:26` delegates the live frontier list: "Explored, not held — the live list is `corpus/README.md` § Frontier". The round-57 note is an append-only note in exactly that list; PROVINCE's § Frontier bullet already covers the unaffected classification ("plugin surfaces and measured client behaviour stay here", `PROVINCE.md:28`). Round 57 changes no ownership: plugin surfaces remain Frontier, command-extraction row remains Frontier.
2. § Core lines are added only for held, verified surfaces (rounds 52–56 knowledge entries each entered Core with a passing counter). Round 57's counter missed, so plugin manifest location knowledge is recorded-not-held; adding a Core line would falsely assert governance of a claim that failed F >= 5. The SKILL.md section is a craft row with basis, but the claim is not held — consistent with the note's own framing.
3. The only historical precedent for a within-Frontier annotation in PROVINCE (round 52 correction, M36, `PROVINCE.md:18`) exists because a previously *declared* Core claim failed verification; round 57 declared the miss up front and never moved the item. No correction is needed.

If the integrator wants maximal explicitness, an *optional* one-line note in the § Frontier bullet (e.g., "plugin manifest locations recorded round 57, counter not met — not held") is harmless but duplicative; it is not required for accuracy.

## Findings by severity

- No actionable defects found. Two informational observations (no fix proposed):
  1. F1: the note's quote elides the `plugin manifests` prefix and the G >= 3 conjunct — both non-misleading (exact substring; non-binding conjunct). 
  2. F5: PROVINCE.md unchanged by design; no line required.

## Residual risk / verification gaps

- I did not re-run the verifier with `--fetch` against the live page (receipt is the committed evidence; counter sha256 matches the frozen v2, and the receipt's exit/exit-line are self-consistent). C1's measurement at `ac22ca8` is trusted as recorded; the declared-result trajectory (`0 of 0` base → `4 of 4` at content) is corroborated by receipt lines and the counter's own predicate.
- The 105/171 figures are re-derived from the committed TSV (byte-identical to the delivered artifact, sha256 `bfa7f262…`), not from a fresh instrument run; the TSV is the durable deliverable per ExecC2FleetBefore.md:213-224.
- `105 of 171` counts FAIL subjects (rows), not distinct lane/line pairs (129 distinct pairs per report line 207); the note says "fleet FAIL subjects", which matches rows and the report's own phrasing (ExecC2FleetBefore.md:1, 177).
