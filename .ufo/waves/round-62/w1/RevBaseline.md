# RevBaseline — round 62 wave 1 baseline reproduction

Seat: `KotobaR62.RevBaseline` (reviewer, operability). Date: 2026-10-23.
Scope: reproduce the base/tip baseline the round cites at dispatch tip
`45a7ecfac9e203297f3146c45d63f5e79367470c`; flag drift from the r61 receipts.
Bounds held: read-only lane/fleet, no git/jj mutation (all git calls were
rev-parse/log/diff/show/cat-file/merge-base/status — read-only), scratch only at
`/fast/scratch/hyaku/kotoba-r62/RevBaseline/`, no dispatch, no asks, ≤4 concurrent
processes.

## Verdict

**All six commanded baselines reproduce exactly; zero drift from the r61
receipts.** Findings below are advisories about tip movement during the audit,
not baseline defects.

## Tip/pin facts (read-only git)

```
$ git rev-parse HEAD                          # audit start  ~20:54 UTC
a1cb8abc3911a5df3a2877915509118e384651a4
$ git rev-parse HEAD                          # audit end    ~20:57 UTC
5c924b02deb89228fb6247dbb71bf4e264bf597c
$ git merge-base --is-ancestor 45a7ecfa… HEAD ; echo exit=$?   # both instants
exit=0
$ git cat-file -e 45a7ecfa…:plans/round-62.md ; echo exit=$?
exit=0          # plan existed at dispatch tip; 45a7ecfa IS the r62 freeze commit
$ git log --format='%h %s' 45a7ecfa~3..45a7ecfa
45a7ecf round-62: plan + census-before (C1 depth = erratum absorption matrix …)
a745411 round-61: no-harm battery receipt — no-harm OK exit 0 at 147ac42e …
8a8d332 round-61: SCORECARD completion entry … + round-62 candidates
```

Commits that landed during this audit (all descendants of the dispatch tip):
`07c8167` wave-1 spec+dispatch payload · `a1cb8ab` + `fecb3d6` r61 verifier
spot-check (integrator admit/reject + appended count correction) · `5c924b0`
round-62 plan erratum E1.

Every input the six commands measure is byte-stable across the whole window:

```
$ git diff --name-only 45a7ecfa..HEAD -- corpus/SOURCES.md corpus/LOG.md \
    corpus/QUALITY.md verifiers scripts
(empty)
$ git diff --stat HEAD -- verifiers scripts corpus plans        # worktree vs HEAD
(empty)
```

## Commanded runs (pasted verbatim; `date -u` and exit code per run)

### 1. `sha256sum verifiers/check_scoped_rules.py` — expect `5a5adc94…`

```
$ sha256sum verifiers/check_scoped_rules.py verifiers/check_routed_repairs.py \
    verifiers/check_gate_registry.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  verifiers/check_routed_repairs.py
01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce  verifiers/check_gate_registry.py
$ date -u
Fri 23 Oct 2026 08:56:10 PM UTC        # re-hash at final instant identical
```

`check_scoped_rules.py` sha matches the r61 freeze pin exactly
(`5a5adc94…`, recorded in `receipts/C1-worlds.txt:6,14,52` and the r61 report).
Pinned at both anchor revisions for completeness:

```
$ git show 45a7ecfa:verifiers/check_scoped_rules.py | sha256sum   → 5a5adc94…
$ git show 45a7ecfa:verifiers/check_routed_repairs.py | sha256sum → 95ade9be…
$ git show a745411c:verifiers/check_scoped_rules.py | sha256sum   → 5a5adc94…
$ git show a745411c:verifiers/check_routed_repairs.py | sha256sum → 95ade9be…
```

### 2. `python3 -B verifiers/check_scoped_rules.py --self-test` — expect r61 line, exit 0

```
$ python3 -B verifiers/check_scoped_rules.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
self-test: 0 failure(s) over 189 assertions
exit=0
$ date -u
Fri 23 Oct 2026 08:54:56 PM UTC
```

Matches the committed r61 receipt `.ufo/waves/round-61/receipts/C1-worlds.txt:14-25`
line-for-line (all eight world lines, the predicate line, the 189-assertion
footer, `exit=0`). **No drift.**

### 3. `python3 -B verifiers/check_routed_repairs.py --self-test` — 12 arms, exit 0

```
$ python3 -B verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
$ date -u
Fri 23 Oct 2026 08:54:55 PM UTC
```

12 arms, 0 failures — byte-identical to the r61 receipts
(`wave/ExecC2Tip.md:34-48`, `wave/ExecC2Audit.md:57-71`). **No drift.**

### 4. `python3 -B verifiers/check_routed_repairs.py --rev f3246d14` — 0 of 6, exit 1

```
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d14
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
$ date -u
Fri 23 Oct 2026 08:55:23 PM UTC
```

Byte-exact against the committed base control:

```
$ { python3 -B verifiers/check_routed_repairs.py --rev f3246d14; \
    echo "base-exit=$?"; } > …/live-c2-base.txt
$ diff -u .ufo/waves/round-61/controls/C2-base.txt …/live-c2-base.txt
(empty)
diff-exit=0
$ date -u
Fri 23 Oct 2026 08:56:57 PM UTC
```

All eight lines of `controls/C2-base.txt` reproduce: six `missing` verdicts,
`routed repairs verified 0 of 6`, `base-exit=1`. **No drift.**

### 5. `python3 -B verifiers/check_gate_registry.py --rev 45a7ecfa`

```
$ python3 -B verifiers/check_gate_registry.py --rev 45a7ecfa
verifiers/box_proof_case_deletion.py         OK
verifiers/check_agent_definitions.py         OK
verifiers/check_agentdef_boxes.py            OK
verifiers/check_alwayson_boxes.py            OK
verifiers/check_assertion_floors.py          OK
verifiers/check_callee_rename.py             OK
verifiers/check_command_files.py             OK
verifiers/check_correction_sweep.py          OK
verifiers/check_could_not_evaluate.py        OK
verifiers/check_description_thresholds.py    OK
verifiers/check_explicit_invocation.py       OK
verifiers/check_gate_finding_delta.py        OK
verifiers/check_gate_registry.py             OK
verifiers/check_hook_files.py                OK
verifiers/check_infoless_fences.py           OK
verifiers/check_mcp_instructions.py          OK
verifiers/check_opencode_repin.py            OK
verifiers/check_overlap_levers.py            OK
verifiers/check_plugin_manifests.py          OK
verifiers/check_routed_repairs.py            OK
verifiers/check_scoped_rules.py              OK
verifiers/check_sibling_census.py            OK
verifiers/check_sources_append_only.py       OK
verifiers/check_substrate_pins.py            OK
verifiers/check_sweep_mutants.py             OK
verifiers/compare_harness_independent.py     OK
verifiers/fault_injection_corpus.sh          OK
verifiers/verify_alwayson.py                 OK
verifiers/verify_corpus_independent.py       OK
verifiers/verify_corpus_integrity.py         OK
verifiers/verify_dispatch_prompts.py         OK
verifiers/verify_harness_claims.py           OK
verifiers/verify_harness_independent.py      OK
verifiers/verify_skill_checklist.py          OK
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 35 of 35 lane verifiers; phantom 0
exit=0
$ date -u
Fri 23 Oct 2026 08:55:23 PM UTC
```

Consistent with the r61 report's "gate 35/35 exit 0 at tip". The registry row for
`check_scoped_rules.py` reads at the dispatch revision as conformant — the r62
SKILL.md annotation (absorption finding) is wave work, not a baseline defect.

### 6. Census — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
$ date -u
Fri 23 Oct 2026 08:55:23 PM UTC
```

Byte-exact vs the committed before-receipt (lines 4+ of
`.ufo/waves/round-62/census-before.txt`, i.e. excluding only its `date_utc=`
header and the `$`-prefixed command echo — the invoked command is identical):

```
$ diff -u <(sed -n '4,$p' census-before.txt) live-census.txt   # via scratch files
(empty)
diff-exit=0
$ date -u
Fri 23 Oct 2026 08:57:42 PM UTC
```

Same 14 W04 duplicate-url warnings, same `kotoba ok` row, `exit=0`. **No drift.**

## Drift analysis vs the r61 receipts

| Checked item | r61 receipt value | Reproduced | Drift |
|---|---|---|---|
| `check_scoped_rules.py` sha256 | `5a5adc94…` (`C1-worlds.txt:6,14,52`) | `5a5adc94…` | none |
| scoped-rules self-test line | `worlds reject 7 of 7; eligible rows pass 4 of 4` + `0 failure(s) over 189 assertions` | identical, exit 0 | none |
| routed-repairs self-test | 12 arms + `self-test: 0 failure(s)` | identical, exit 0 | none |
| base control text | `controls/C2-base.txt` 8 lines, `0 of 6`, `base-exit=1` | byte-exact (`diff` empty), exit 1 | none |
| gate registry at tip | r61 report: "gate 35/35 exit 0" | `35 of 35; phantom 0`, exit 0 at `45a7ecfa` | none |
| census before | `census-before.txt` (14 W04 + ok + exit 0) | byte-exact body | none |

## Advisories (not baseline defects)

1. **Moving tip.** HEAD advanced `45a7ecfa → a1cb8ab → fecb3d6 → 5c924b02`
   during the audit window (~20:50–20:57 UTC). All are descendants of the
   dispatch tip; `45a7ecfa` remains an ancestor of HEAD, and every measurement
   input (`verifiers/`, `scripts/`, `corpus/{SOURCES,LOG,QUALITY}.md`) is
   byte-identical dispatch-tip → HEAD → worktree. Baseline reproduction is
   unaffected; any r62 receipt should cite the rev it measured, not `master`.
2. **Plan amended post-dispatch.** `5c924b0` adds a pre-data E1 erratum to
   `plans/round-62.md` (C1 predicate counts computed K/N; the E2f successor moved
   out of the counted predicate; E2c/E2e/E2f absences measured before data).
   Seats drafted against the dispatch-time plan text should cite the HEAD plan
   for the claim sentences; the frozen baseline commands here are unchanged.
3. **Untracked files appeared mid-audit** (sibling wave-1 writes):
   `.ufo/waves/round-62/{controls,snapshots,w1}/` and a new verifier draft
   `verifiers/check_seat_counts.py`. The gate-registry run is rev-scoped
   (`--rev 45a7ecfa`), so the untracked file does not enter its 35-verifier
   universe; when it lands tracked, the registry row for it becomes a
   conformance obligation.
4. **Routed-repairs sha lineage (explained, not drift).** Mid-wave r61 audit
   `ExecC2Audit` recorded sha `9ee77d47…` at `eb5e149`; the counter now hashes
   `95ade9be…`. `git log f3246d14..HEAD -- verifiers/check_routed_repairs.py`
   shows r61's own pre-close hardening commits `daf4ad7` (29-printing count
   exemplar) and `ee19e9c` (R-d empty-file guard) after `eb5e149`; the sha is
   identical at r61 close `a745411c` and dispatch tip `45a7ecfa`. The six frozen
   `check_repairs()` checks were untouched throughout (r61 report:12).
5. **r61 report location.** `.ufo/reports/round-61/kotoba.md` lives in the FLEET
   repo (`/home/vgpnk/Projects/shokunin/.ufo/reports/`), not the lane — expected,
   flagged only because the dispatch context quotes the lane-relative path.

## Residual risk / verification gaps

- Self-tests are in-counter fixtures; my runs confirm *byte reproduction* of the
  committed receipts, not world semantics (that is the wave-1 builders' and
  wave-2 falsifiers' job). No `--fetch` run was commanded; none was run.
- The census body diff excluded the committed file's header (`date_utc=` line
  and `$`-prefixed command echo) by construction — content rows and `exit=0`
  compared byte-exact.
- `check_gate_registry.py`'s internal pass criteria were observed only through
  its printed verdict + exit code, matching r61's recorded result.
- Scratch files (`live-c2-base.txt`, `live-census.txt`, `committed-census-body.txt`)
  under `/fast/scratch/hyaku/kotoba-r62/RevBaseline/` are execution artifacts,
  not evidence citations; the diffs are reproduced above verbatim.

Installs: no installs (pacman paused host-wide; nothing needed).
Blockers: none.
Attacked/produced: reproduced the round-62 base/tip baseline — six commanded
runs at dispatch tip `45a7ecfa` — byte-exact against the r61 receipts; zero
drift; five advisories filed (moving tip, post-dispatch plan E1 erratum,
untracked sibling artifacts, explained routed-repairs sha lineage, fleet-side
r61 report path).
