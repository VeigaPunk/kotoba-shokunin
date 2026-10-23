# Round 61 — RevCensus report (operability)

**Scope:** SOURCES census only — verify `census-before.txt` at tip, then census a
copy of the tree with the planned S112–S117 rows appended and report row counts /
W04 consequences for the "round ends exit 0" requirement. Read-only lane and
fleet; no git/jj mutation; no dispatch. Attempt 1, 2026-10-23.

## 1. Tip-state note

- `date -u` at start of run: `2026-10-23T19:09:41Z`.
- Working-copy commit: `c12b3c8d75125d2a4afa168e5456bc9b39e0336d` — an **empty**
  jj working-copy commit (no description). Parent: `7827628a939b` = `master` =
  "round-61: plan freeze …", which itself sits on plan base `f3246d1493b6`
  ("round-60 verifier spot-check"). `SOURCES.md` is unchanged relative to base —
  so tip, master, and base give the same census result.
- `jj status`: "The working copy has no changes."

## 2. Step 1 — census validate at tip vs committed `census-before.txt`

Command (run from anywhere; absolute paths):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

Pasted output, `date -u` `2026-10-23T19:09:46Z`, exit code `0`:

```text
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
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Committed `.ufo/waves/round-61/census-before.txt` (full file, 15 lines):

```text
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
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Diff verification command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba > /tmp/census-tip-run.txt 2>&1
{ cat /tmp/census-tip-run.txt; echo "exit=0"; } | diff -u - .ufo/waves/round-61/census-before.txt
```

Result: **byte-identical** (`diff` prints nothing; `IDENTICAL`). The file is the
validator's stdout plus a recorded `exit=0` trailer line; the trailer is not
validator stdout, it is the recorded exit code, and my run's exit code was 0, so
the appended `exit=0` matches too. **No diff. The committed receipt is honest.**

## 3. Step 2 — census on a copy with the planned rows

### 3.1 What "planned S112–S117" resolves to

| Row | Seat (wave-dispatch.json) | Source URL | W04 expectation |
|---|---|---|---|
| S112 | ScribeS112 | `code.claude.com/docs/en/memory.md` (re-open of S043/S103) | +1 |
| S113 | ScribeS113 | VS Code custom-instructions page — *may be unopened*; worst case re-open of S105's `code.visualstudio.com/docs/agent-customization/custom-instructions.md` | +1 worst case, 0 if unopened URL |
| S114 | ScribeS114 | `docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` (re-open of S048/S106) | +1 |
| S115 | ScribeS115 | `cursor.com/docs/rules` (re-open of S049/S108) | +1 |
| S116 | **no seat** — see finding F1 | — | — |
| S117 | ScribeC3 (report already in `wave/ScribeC3.md`) | sibling repo path `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` — **no URL** | 0 |

S112–S115 teach `re-opens …`, never `supersedes S0NN` — that distinction is load-bearing (F3).

### 3.2 Method

Copy of the lane (`.jj`/`.git` excluded) at
`/fast/scratch/hyaku/kotoba-r61/RevCensus/lane-copy/` behind a scratch fleet root
(`fleet-root/shokunin.conf` = copied conf; `fleet-root/kotoba-shokunin` = symlink
to the copy, so the lane label stays `kotoba` and the command line stays the
assigned one). Scratch is untrusted — this simulates the future integrated tree;
the real run rides the L1.

Because the scribes' row texts are not yet returned, I used stand-in rows built
from the frozen dispatch briefs: the real re-open URLs, `docs | A`, a fresh scope
cell ("Canonical Scope key set for the <client> client under the scoped-rules
counter arm A1 …"), `opened 2026-10-23`, `mined`, `used-by` =
`corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md`;
S117 used ScribeC3's committed draft verbatim (`own-work | B | … | queued |
180d`, used-by the new entry path). Only shape/URL/scope/status feed the census —
the stand-in anchors' `PENDING-SCRIBE` sha placeholders are census-inert. The
five rows were inserted inside `## Registry` after the S111 row (line 123),
before `## Paths` — see F2 for why that is load-bearing.

### 3.3 Scenario B — rows landed, used-by files absent (integration-order probe)

`date -u` `2026-10-23T19:13:01Z`, same validate command against the scratch root:

```text
… (13 base W04 lines unchanged) …
kotoba	W04	S112 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S113 duplicate url code.visualstudio.com/docs/agent-customization/custom-instructions.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	E11	S112 missing used-by corpus/knowledge/scoped-rules-counter-round61.md
kotoba	E11	S112 missing used-by corpus/lessons/round-61.md
kotoba	E11	S113 missing used-by corpus/knowledge/scoped-rules-counter-round61.md
kotoba	E11	S113 missing used-by corpus/lessons/round-61.md
kotoba	E11	S114 missing used-by corpus/knowledge/scoped-rules-counter-round61.md
kotoba	E11	S114 missing used-by corpus/lessons/round-61.md
kotoba	E11	S115 missing used-by corpus/knowledge/scoped-rules-counter-round61.md
kotoba	E11	S115 missing used-by corpus/lessons/round-61.md
exit=1
```

**F2: E11 is the round-killer.** `usedby_findings` (sources-census.sh:538-571)
checks every `mined` row's used-by paths on disk. S112–S115 are planned `mined`
(their used-by entry + lesson are part of the claim). If the SOURCES row lands in
any commit where `corpus/knowledge/scoped-rules-counter-round61.md` or
`corpus/lessons/round-61.md` does not yet exist, validate exits 1 with 8 E11
lines (2 files × 4 rows). Rows and their used-by files must land **in the same
commit** (or files first). S117 is `queued`, so its entry path is not checked —
queued rows are immune to E11.

### 3.4 Scenario A — rows landed, used-by files present

Stub files created in the copy (`scoped-rules-counter-round61.md`,
`round-61.md`, `writing-revision-calibration-round61.md`). `date -u`
`2026-10-23T19:13:05Z`, same validate command:

```text
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
kotoba	W04	S112 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S113 duplicate url code.visualstudio.com/docs/agent-customization/custom-instructions.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	ok	/fast/scratch/hyaku/kotoba-r61/RevCensus/fleet-root/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

`census` mode on the same mutated copy (live base run pasted first for comparison):

```text
# base (live lane, read-only), date -u 2026-10-23T19:13:42Z, exit 0
kotoba	rows	110
kotoba	tier.A	108
kotoba	tier.B	1
kotoba	tier.C	1
kotoba	status.mined	102
kotoba	status.queued	7
kotoba	status.rejected	1

# copy + S112–S115, S117, exit 0
kotoba	rows	115
kotoba	tier.A	112
kotoba	tier.B	2
kotoba	tier.C	1
kotoba	status.mined	106
kotoba	status.queued	8
kotoba	status.rejected	1
```

Contract § Census blocks on the mutated copy: `rows 115` · malformed `0` ·
`A=112 B=2 C=1` · `mined=106 queued=8 rejected=1` · dup ids none · enum/tier
violations none · mined used-by missing none. `grep -c
'self-assessment-at-writing' corpus/SOURCES.md` → `1` (C3's counting gate moves
0 → 1 as planned).

### 3.5 Isolation probes (minimal registries in scratch; each pasted with exit)

**F3 — E04 verbatim-scope trap.** A re-open row that copies the existing row's
scope cell verbatim fails, because `re-opens` does not match the E04 escape
`/supersedes S[0-9]{3}/` and the briefs freeze `teaches` as `re-opens …`:

```text
# e04-shokunin: S106 fixture + S114 with S106's scope cell verbatim, teaches 're-opens S048 …'
e04-shokunin	E04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md within scope Copilot CLI repository-scoped modular instruction files and their path selector (vendor documentation; not a runtime test)
exit=1
```

The `supersedes` escape (same URL+scope, teaches opens `supersedes S106 —`):

```text
sup-shokunin	ok	…/sup-shokunin/corpus/SOURCES.md
exit=0
```

Consequence for integration: each re-open row's **scope cell must differ** from
every existing row sharing its URL (the natural "canonical scope-key set" scope
text does — scenario A shows W04, not E04), **or** teaches must open
`supersedes S0NN —`. Either is safe; a verbatim scope copy with the frozen
`re-opens` teaches is exit 1.

**F4 — E12 tail-append trap.** "Appended" must mean appended inside
`## Registry`, i.e. after S111 / before `## Paths`. A row appended at file tail
(after `## Leads`) is caught:

```text
e12-shokunin	E12	S117 row outside Registry section
exit=1
```

## 4. Findings

- **F1 (scope note, medium):** the planned set is **five** rows — S112–S115 + S117.
  **S116 has no owner anywhere in `wave-spec.json`/`wave-dispatch.json`**
  (68 seats; verified by search — the only S116 hits in the wave dir are this
  report's own name pattern). Id gaps are contract-legal (r60 reserved S112), so
  exit 0 is unaffected; but if a late row claims S116 it needs its own
  row-shape/W04 audit, and the lesson Gate should say why the gap exists.
- **F2 (integration constraint, exit-1 capable):** `mined` rows and their used-by
  files must commit together — S112–S115's `used-by` names
  `corpus/knowledge/scoped-rules-counter-round61.md` and
  `corpus/lessons/round-61.md`; row-first/file-later lands 8 E11 (observed).
  S117 `queued` is immune; flipping it to `mined` requires its entry committed.
- **F3 (row-shape constraint, exit-1 capable):** re-open rows must not copy the
  same URL's existing scope cell verbatim under the frozen `re-opens` teaches —
  E04 fires (observed, exit 1). New scope wording (as briefed) or a `supersedes`
  teaches both clear it (observed, exit 0).
- **F4 (placement constraint, exit-1 capable):** rows must be inserted inside
  `## Registry` (before `## Paths`), not at file tail — E12 fires otherwise
  (observed, exit 1).
- **W04 forecast:** +4 → **17 total** (S112, S113 if S105's page is re-opened,
  S114, S115); +3 if ScribeS113 lands an unopened canonical URL; +1 more if an
  S116 row ever lands on a duplicate URL. W04s are warnings — validate still
  exits 0, satisfying "the round must end exit 0". The new W04s are the declared
  re-opens, same pattern as S103–S109's entries in census-before.
- **Counts forecast:** 110 → **115 rows** (tier.A 108→112, tier.B 1→2;
  status.mined 102→106, queued 7→8). S117 makes `grep -c
  'self-assessment-at-writing'` go 0 → 1.
- **Step-1 verdict:** committed `census-before.txt` is byte-identical to a live
  tip run + its `exit=0` trailer. No drift since freeze.

## 5. Limits

- S112–S115 row texts are stand-ins built from the frozen briefs (real URLs,
  realistic cells); the scribes' final texts may differ in scope wording — that
  is exactly what F3 watches. If a scribe picks an unopened URL (S113's brief
  prefers one), the W04 delta drops by one.
- The copy excludes `.jj`/`.git`; E11 checks working-tree paths, unaffected.
- I did not re-fetch any page; no sha values are asserted here.
- The E12/E04/minimal-lane probes are scratch fixtures, evidence only for the
  validator's behavior, not lane state.

Installs: no installs.
Blockers: none.
Produced: tip-vs-receipt verification (identical), simulated post-append census
(115 rows, 17 W04, exit 0), and three observed exit-1 traps (E11 ordering, E04
verbatim-scope, E12 tail-append) that gate the L1's integration order.
