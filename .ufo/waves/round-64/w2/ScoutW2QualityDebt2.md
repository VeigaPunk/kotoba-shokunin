# ScoutW2QualityDebt2 — carry-forward quality debt at c019919c

Measured revision: `c019919c97ab5fe98e87a7754b4449ea4e699c99`.
Axis: freshness. Read-only investigation; only this report was written in the lane. No subagent dispatch, Git/jj writes, installation, production edits, or full battery.

## Findings

**All six debts are named, but none is evidenced closed at c019919c.** Four are recommended correction notes; two are process/receipt deferrals. `corpus/lessons/round-64.md:156-158` lists all six and explicitly calls them **open**. It does not supply the four recommended corrective statements. Its shorthand `ScoutQualityDebt` resolves to the committed `.ufo/waves/round-64/w1/ScoutQualityDebt.md`; that report's underlying evidence pointers all resolve at the measured revision.

**Freshness discrepancy:** the requested “now named in the Next line” is true at the subsequent measurement commit `b99fb79c27042e0f8a598cbbb4d81479a806b518`, **not c019919c**. At c019, `SCORECARD.md:371` remains **Next: round 64**, with the six older debts and no governance-red clause. The lesson's “carried to the round-65 Next line” is therefore anticipatory at this revision. b99 supplies Next-65 and the explicit `ScribeSHONEN` F2 carry-forward; it leaves the lesson blob unchanged.

| Item | State at c019919c | Name/note in round-64 lesson | Resolving c019 evidence |
|---|---|---|---|
| SentBounds pre-wave baseline receipt | **OPEN / deferred** | Name present at `:156`; no baseline receipt | `.ufo/waves/round-61/wave/SentBounds.md:68-70,172-181` defines the required pre-dispatch fleet/lane/runtime/siblings/jj-op snapshot. `.ufo/waves/round-64/w1/ScoutQualityDebt.md:27,40-54` carries it. All four round-61–64 `bounds.md` paths remain absent; payload-key search finds only the proposal, not captured values. |
| Helper-invocation receipts | **OPEN / deferred** | Name present at `:156`; no invocation receipt | `SentBounds.md:72-80` requires trusted before/after op IDs and helper path/hash/argv. `ScoutQualityDebt.md:28,57-71` resolves. Searches find proposals/debt mentions, not a populated ledger. Live fleet helper search also finds no receipt/ledger/argv/op-log terms; that live helper observation is not a c019 fleet-version pin. |
| M93 hollow-diagnostic wording | **OPEN** | Name present at `:157`; recommended correction absent | `corpus/lessons/round-62.md:25` still calls the diagnostic a missing `check_scoped_rules.py` path. `.ufo/waves/round-62/controls/absorption-hollow.txt:8-9` actually says `absorption self-test failed: guard-mutation direction is missing for one or more errata`, `exit=1`. `ScoutQualityDebt.md:29,75-92,226` resolves. |
| `LOG.md:2549` clock | **OPEN** | Exact line pointer present at `:157`; corrected clock absent | `LOG.md:2549` still gives `2026-10-23T20:53:36Z`; `.ufo/waves/round-62/controls/absorption-before.txt:2` gives `date_utc=2026-10-23T20:57:43Z`. `ScoutQualityDebt.md:30,94-103,227` resolves. |
| r62 SCORECARD no-harm sentence | **OPEN** | Name present at `:157`; recommended qualification absent | `SCORECARD.md:36` still ends “No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged.” `.ufo/waves/round-62/noharm-tip.txt:12,17,23` records `FAIL reg_gate`, `FAIL corpus-idx`, `Battery exit code: 124`. `LOG.md:2573` qualifies the **report's** no-harm summary, not this SCORECARD sentence. `ScoutQualityDebt.md:31,105-119,228` resolves. |
| r61 R-b complete-list omission | **OPEN (list only)** | Name present at `:157`; omitted-path correction absent | `LOG.md:2557` still says “complete list to date” without `corpus/lessons/round-61-verifier-spotcheck.md`. The file exists and is indexed at `corpus/README.md:108`; the **index gap is closed**, not reopened here. `ScoutQualityDebt.md:32,121-129,229` resolves. |
| `governance.citation_resolves` / ScribeSHONEN F2 | **OPEN / red** | Not in lesson's six-item list; **not named on c019's Next line** | `.ufo/waves/round-64/w1/ScribeSHONEN.md:168-188,222-225` resolves. Fresh run of the c019 checker and governance files: FAIL, evaluated 1190, exit 1. Original three unresolved subjects remain; c019 also references three receipt subjects not yet committed (details below). **Named at b99 `SCORECARD.md:371`, not c019.** |

“Name present” is a closed naming/retention check, **not closure of the debt**. The lesson itself says open. The four corrective sentences recommended in `ScoutQualityDebt.md:225-229` are not reproduced there: no guard-direction diagnostic, `20:57:43`, `FAIL reg_gate`, or omitted spot-check path occurs in the round-64 lesson.

## Revision-pinned procedure and command evidence

The worktree had advanced to b99, so worktree-only reads would misattribute Next-65 to c019. I extracted the immutable c019 tree under `/tmp/kotoba-r64-quality-mapwldo4/measured`:

```text
$ git archive --format=tar --output=/tmp/kotoba-r64-quality-mapwldo4/measured.tar c019919c97ab5fe98e87a7754b4449ea4e699c99
exit=0
$ tar -xf /tmp/kotoba-r64-quality-mapwldo4/measured.tar -C /tmp/kotoba-r64-quality-mapwldo4/measured
exit=0
$ git rev-parse c019919c97ab5fe98e87a7754b4449ea4e699c99:SCORECARD.md b99fb79c:SCORECARD.md c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/lessons/round-64.md b99fb79c:corpus/lessons/round-64.md
70d791e52e6cdd8fae83bff6c769d6cf406a367e
5b2f57324f59758ffbd3be80161bd52624038cb8
58ff37c04ae048ce00dcbbc53f1c2fa71693ef98
58ff37c04ae048ce00dcbbc53f1c2fa71693ef98
exit=0
$ git log --format=%H\ %s c019919c97ab5fe98e87a7754b4449ea4e699c99..HEAD -- SCORECARD.md corpus/lessons/round-64.md LOG.md
b99fb79c27042e0f8a598cbbb4d81479a806b518 round-64: measurements — C1/C2 receipts at c019919c, SCORECARD round-64 annotations + Next-65, SHONEN refresh, README corpus-index rows, w2 spec/dispatch
exit=0
```

All paths in the four correction rows were checked with `git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:<path>`; **each exited 0**: `corpus/lessons/round-62.md`, `LOG.md`, `SCORECARD.md`, `.ufo/waves/round-62/controls/absorption-hollow.txt`, `.ufo/waves/round-62/controls/absorption-before.txt`, `.ufo/waves/round-62/noharm-tip.txt`, `corpus/README.md`, and `corpus/lessons/round-61-verifier-spotcheck.md`. The two w1 reports and `SentBounds.md` also exited 0. Relevant line contents were read from the extracted measured tree, not assumed from file existence.

### Deferrals: no closing lane receipt found

```text
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-61/bounds.md
fatal: path '.ufo/waves/round-61/bounds.md' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-62/bounds.md
fatal: path '.ufo/waves/round-62/bounds.md' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-63/bounds.md
fatal: path '.ufo/waves/round-63/bounds.md' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/bounds.md
fatal: path '.ufo/waves/round-64/bounds.md' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
```

Specialized `grep` searches (tool results have no process exit code):

- Across the entire extracted c019 tree, pattern `^\s*"(fleet_status|jj_op_head|op_before|op_after|helper_argv|before_op_id|after_op_id)"\s*:` returned **only** `SentBounds.md:177` (`"fleet_status": git_status(FLEET),`) and `:181` (`"jj_op_head": ops[0]["id"],`) — executable proposal text, not a capture.
- Across rounds 61–64 plus LOG/SCORECARD, `fleet_status|jj_op_head|op_before|op_after|helper-invocation|helper invocation|invocation receipt|pre-dispatch snapshot|pre-wave baseline` returned the proposal, dispatch prompts, prior debt reports, and SCORECARD/scribe carry-forward wording; no captured receipt.
- In the live fleet `scripts/hyaku/jj-lane.sh`, `op log|argv|invocation receipt|receipt|ledger` (case-insensitive) returned **No matches found**. Live helper SHA-256: `319a56f7f0641915bdb636d88b2d6b34987a20f430d7b06896150f8ae4c1e429` (`sha256sum scripts/hyaku/jj-lane.sh`, exit 0).
- Round-64 `census-before.txt:1-17` is 16 SOURCES duplicate-URL warnings plus `kotoba ok …/corpus/SOURCES.md`; it contains none of the required baseline state. It is not a substitute baseline.

[INFERENCE] These independent path/payload/phrase checks support leaving both deferrals open. They do **not** prove that no arbitrarily named private receipt exists outside the measured lane tree; no such external receipt or committed pointer is supplied.

### Governance red: freshly exercised on measured bytes

A bare `/tmp` export initially adds relocation-only failures for `../` fleet pointers. I restored its parent context with scratch-only symlinks for `.ufo`, `AXES.md`, `MISSION.md`, `PROTOCOL.md`, `SCORECARD.md`, and `kasegi-shokunin`, each pointing to its real fleet counterpart. The **measured lane subtree remains the c019 archive**. This preserves the check's actual parent-relative existence context without changing the lane or fleet.

```text
$ (cd /tmp/kotoba-r64-quality-mapwldo4/measured; python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --json)
{
  "checks": [
    {
      "detail": "LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from /tmp/kotoba-r64-quality-mapwldo4/measured; LOG.md:2580: '.ufo/watchdog.log' does not resolve from /tmp/kotoba-r64-quality-mapwldo4/measured; LOG.md:2602: '.ufo/waves/round-64/receipts/C1-span-measure.txt' does not resolve from /tmp/kotoba-r64-quality-mapwldo4/measured; LOG.md:2603: '.ufo/waves/round-64/receipts/C2-r64-measure.txt' does not resolve from /tmp/kotoba-r64-quality-mapwldo4/measured \u2026 (+2 more); 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused",
      "evaluated": 1190,
      "id": "governance.citation_resolves",
      "status": "FAIL"
    }
  ],
  "exit_code": 1,
  "fail": 1,
  "na": 0,
  "pass": 0
}
exit=1
```

Definition-level enumeration using the measured module's own `citation_subjects`, `errata_problems`, and `citation_resolve` yielded these **six** unresolved subjects (`ERRATA_PROBLEMS=[]`):

```text
LOG.md:2533: .ufo/reports/round-60/kotoba.md
LOG.md:2580: .ufo/watchdog.log
LOG.md:2602: .ufo/waves/round-64/receipts/C1-span-measure.txt
LOG.md:2603: .ufo/waves/round-64/receipts/C2-r64-measure.txt
LOG.md:2610: .ufo/waves/round-64/receipts/
SCORECARD.md:158: .ufo/reports/round-60/kotoba.md
```

The extra receipt absences are real at this revision, not relocation failures:

```text
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/C1-span-measure.txt
fatal: path '.ufo/waves/round-64/receipts/C1-span-measure.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/C2-r64-measure.txt
fatal: path '.ufo/waves/round-64/receipts/C2-r64-measure.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
exit=128
```

The subsequent b99 Next-65 suffix, observed via `git show b99fb79c:SCORECARD.md` (exit 0), says:

> the new base red `verify_skill_checklist.py` `governance.citation_resolves` over bare fleet-relative report paths (`ScribeSHONEN` F2 — red at `078eec4`, outside the four SHONEN boxes).

This closes the **naming** question only at b99. It does not close F2 or backdate that naming to c019.

## Confidence and remaining gaps

- **High:** all six names retained; four substantive lesson corrections absent; their committed evidence paths/line anchors resolve; governance remains red; Next-65/F2 naming belongs to b99 rather than c019.
- **High within the committed lane search:** neither deferred receipt was found. Global absence outside the lane is not claimed.
- The LSP device is unavailable: `read xd://lsp` returned `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` Consequently source navigation used the literal fallback, not semantic-reference claims. Relevant measured implementation: `verify_skill_checklist.py:1484-1507` (bounded resolver), `:1669-1721` (governance predicate), `:2612-2614` (dispatch). The fresh execution, not text matching, establishes the FAIL result.
- Requested tooling rules path `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was absent; a scoped glob also found no `.omp/agent/` directory. No install/update was needed or attempted; no pacman transaction.
- No correction, integration, score, or claim verdict is performed by this scout.
