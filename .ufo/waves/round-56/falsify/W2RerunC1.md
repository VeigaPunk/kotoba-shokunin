Result: DONE — the C1 predicate reproduces verbatim at `c22fdd39` (7 of 7, new ground 3, exit 0) and at base (`0 of 0`, exit 1) under counter sha256 `2f672bd1…` (byte-identical to the `e02f5f5d` counter at both revisions), and all four dispatched no-harm gates are green at `c22fdd39` including the registry gate that was red at `e02f5f5d` (now 28 of 28); no harm found.

# W2RerunC1 — C1 predicate re-run + no-harm gates at c22fdd39

Sandbox (bounds layout): `/fast/scratch/hyaku/kotoba-r56/W2RerunC1/{clone,mirror/kotoba-shokunin}`.
`git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin … && git checkout -q c22fdd390e10623209024c9bbc2fa86b0cdfc333` → `rev-parse HEAD` = `c22fdd390e10623209024c9bbc2fa86b0cdfc333` in both (re-read after runs; `git status --porcelain --ignored=matching` empty). The mirror dir holds a symlink to every entry of `/home/vgpnk/Projects/shokunin` except the lane itself (the round-49 NoHarmGates layout, per `.ufo/waves/round-56/build/ExecBaseReceipts.md` finding 1). No lane file was written except this report; no lane git/jj command was run.

## Counter bytes (the e02f5f5d v1.3 counter)

- `git cat-file blob e02f5f5d:verifiers/check_agent_definitions.py` → sha256 `2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47` — matches the plan's `2f672bd1…` and the receipt header of `.ufo/waves/round-56/C1-measure.txt:1`.
- `git show c22fdd390e10623209024c9bbc2fa86b0cdfc333:verifiers/check_agent_definitions.py | sha256sum` → the same `2f672bd1…`; `diff -q` with the extracted e02f5f5d bytes → `IDENTICAL`. So the counter has not moved since the erratum freeze; running the clone's copy at c22fdd39 is running the e02f5f5d bytes literally.
- `git cat-file blob b0b7140b:verifiers/check_agent_definitions.py` → exit 128 (file absent at base, as expected — the counter is round-56 content).

## C1 predicate re-runs (counter v1.3 bytes, `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch`)

At `c22fdd390e10623209024c9bbc2fa86b0cdfc333` (03:08:24Z, cwd = clone):

```
agent-definition locations found on the live page 7 of 7; new ground 3
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
Codex        BACKED token=.codex/agents/ norm=.codex/agents found=yes base_count=5
VS Code      BACKED token=.github/agents norm=.github/agents found=yes base_count=0
Copilot CLI  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
Gemini CLI   BACKED token=.gemini/agents/*.md norm=.gemini/agents found=yes base_count=0
Cursor       BACKED token=.cursor/agents/ norm=.cursor/agents found=yes base_count=0
opencode     BACKED token=.opencode/agents norm=.opencode/agents found=yes base_count=10
exit 0
```

→ **MET, exit 0** — reproduces `C1-measure.txt:15-23` verbatim (7 of 7, G=3 ≥ 2, F=7 ≥ 5).
At `b0b7140b` (03:08:32Z, same counter bytes, cwd = clone):

```
agent-definition locations found on the live page 0 of 0; new ground 0
Claude Code  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Codex        no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
VS Code      no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
```

→ **NOT MET, exit 1** — reproduces `C1-measure.txt:4-12` verbatim. The predicate is discriminating on the re-run: same bytes, same host, base fails / head passes.

## No-harm gates at c22fdd39 (revision printed; cwd = mirror/kotoba-shokunin, HEAD = c22fdd39)

| Gate | Exit | Key output | vs base-receipts.txt |
|---|---|---|---|
| `check_gate_registry.py --rev c22fdd39…` (03:08:43Z) | 0 | `gate registry rows conformant 28 of 28 lane verifiers; phantom 0`; `check_agent_definitions.py OK`, `check_agentdef_boxes.py OK` | base: 26 of 26 green; routed finding 5 (red 26 of 28 at `0f58a469`/`e02f5f5d`) is **fixed at c22fdd39** — the content commit's message confirms "registry rows for the two round-56 counters". Tree has exactly 28 `verifiers/*.py|*.sh` files (`git ls-tree` count 28). |
| `check_sources_append_only.py --base b0b7140b --rev c22fdd39…` (03:08:43Z) | 0 | `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes` | range is 6 commits (`git rev-list --count b0b7140b..c22fdd39` = 6); the gate counts only commits touching SOURCES.md — the C1 content commit `c22fdd3` is the 1 scanned. Non-vacuous green this time (base run was vacuous, 0 commits). |
| `verify_skill_checklist.py` in mirror (03:09:12Z) | 0 | 11 PASS, 0 FAIL: `checklist.box_map_complete 41 boxes mapped`; `trigger.name_directory 'kotoba-shokunin' == directory 'kotoba-shokunin'`; `line_budget 596/600 (box at line 296)`; `citation_resolves 124/124`; `governance.citation_resolves 1042/1042` | base mirror: 11 PASS exit 0 — same green. In a plain-named clone (`W2RerunC1/clone`, 03:09:38Z) the same three layout artifacts fail as at base: `trigger.name_directory`, `trigger.citation_resolves` (line 586 `../.ufo/reports/round-7/kotoba.md`), `governance.citation_resolves` — layout artifact, not a revision fact, matching ExecBaseReceipts finding 1. |
| `check_gate_finding_delta.py --base b0b7140b --head c22fdd39…` (03:08:43Z) | 0 | `base drift 5, head drift 5; new: none; resolved: none; finding delta: new 0, resolved 0` | identical drift-id set; **no new findings** introduced by the round's 6 commits. |
| SKILL.md line count | — | `git show c22fdd39…:SKILL.md \| wc -l` = **596** (base 598; budget 600 per checklist `trigger.line_budget`) | within budget; the line-budget verbatim move freed 4 lines net and the C1 table fits. |

Supplemental (not dispatched, for the DRIFT-set comparison ExecBaseReceipts finding 3 recommends): `verify_corpus_integrity.py` at c22fdd39 (mirror, 03:09:39Z) → exit 1, `4/9 checks pass` with the **same five DRIFT ids** as base (`corpus.index.tracked_files` 87 vs 81, `.unindexed` 3 vs 0, `pointers.report_total` 56 vs 51, `.commit_total` 33 vs 32, `.commit_unresolvable` 1 vs 0). The unindexed count grew 1→3 — the two new corpus files `agent-definition-files-round56.md` and `lessons/round-56.md` are unindexed — but this is the same pre-existing DRIFT id (baseline still expects round-54 numbers), and `check_gate_finding_delta` (the gate that owns new-vs-old comparisons) reports `new 0`. No new integrity defect.

## Findings

1. **No defect.** C1 predicate and all no-harm gates reproduce; the measurement receipt `C1-measure.txt` is accurate (both runs verbatim-identical).
2. **Registry gate routed defect resolved at c22fdd39** — 28 of 28 conformant, phantom 0; both new counters have rows. ExecBaseReceipts finding 5's fix prediction ("adding those two rows restores the base value") is confirmed.
3. **Sources append-only green is non-vacuous** (1 SOURCES-touching commit scanned, 0 protected-cell changes) — the round's S072–S078 append respected protected cells.
4. **Corpus-integrity DRIFT set unchanged** (supplemental run): same five ids as base; the unindexed count grew 1→3 only because C1's two new corpus files are unindexed — same pre-existing DRIFT id, and the delta gate (`new 0`) confirms no new finding.

## Evidence notes

- Commands and exits pasted above; every block names its revision (`git rev-parse HEAD` printed before each gate run = `c22fdd390e10623209024c9bbc2fa86b0cdfc333`).
- `base-receipts.txt` sha256 verified while reading: `1e8ebad1b70730272781eafd1805271fe87b07fdd67685a84094dc3aca7f3b36` (matches `ExecBaseReceipts.md` line 6).
- `--fetch` runs performed plain HTTP GETs via the counter itself (urllib, pinned hosts); no headless browser, no challenge bypass.
- No tool installed or updated (none needed); no paid model call; no subagent/labrat spawned; all commands under `timeout ≤900`.
- Sandbox writes only under `/fast/scratch/hyaku/kotoba-r56/W2RerunC1/`; lane untouched except this file.

Report: .ufo/waves/round-56/falsify/W2RerunC1.md
