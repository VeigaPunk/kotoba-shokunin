# Round 61 — ScribeLesson report

**Scope:** report-only draft of `corpus/lessons/round-61.md` for round 61, attempt 1, hyaku run 5. This seat did not write the lesson into the lane. The draft below is for the L1 integrator; it is not landed evidence or a round verdict.

## Behavior and gates

Prepared the complete proposed lesson text with the requested frontmatter, Gate records for the planned S112–S115 and S117 rows, an explicit S116 no-owner note, M91 with the requested class and R-a/R-c calibration evidence, no unsupported M92+ assertion, and an empty `## Falsify corrections` section for the L1.

The source-row fetch and quote records below are copied from the named source-seat reports. They are reported observations, not independently re-executed by this seat. Their scratch copies are not committed evidence; L1 must land/refetch and verify source snapshots before using them as committed C1 inputs. The sibling S117 evidence is separately pinned in `RevKamaRow.md`.

**No gate, test, build, lint, or counter was run by ScribeLesson.** The C2 base result below is an existing committed receipt, corroborated by a distinct run recorded by `MutC2.md`; neither is this seat's execution.

## Draft deliverable

### Target: `corpus/lessons/round-61.md`

```markdown
---
author: kotoba L1 round 61
date: 2026-10-23
round: 61
lane: kotoba
---

# Round 61 — lesson (kotoba, hyaku run 5, attempt 1)

## Gate

The following source rows were opened on 2026-10-23 by the named seats. Their source snapshots are proposed integration targets, not claimed landed bytes.

- **S112 Claude Code** — https://code.claude.com/docs/en/claude-directory.md — accessed 2026-10-23T19:12:44Z (HTTP 200, 31,144 B, sha256 `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`; seat `ScribeS112`; snapshot target `.ufo/waves/round-61/snapshots/S112.page`) — `claude-directory.md:94`: "| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |"
- **S113 VS Code** — https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md — accessed 2026-10-23T19:13:53Z (HTTP 200, 25,556 B, sha256 `b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9`; seat `ScribeS113`; snapshot target `.ufo/waves/round-61/snapshots/S113.page`) — `custom-instructions.md:45`: "Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`."
- **S114 Copilot CLI (re-opens S048)** — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md — accessed 2026-10-23T19:11:44Z (HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; seat `ScribeS114`; snapshot target `.ufo/waves/round-61/snapshots/S114.page`) — `add-custom-instructions.md:32`: "Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with."
- **S115 Cursor (re-opens S108)** — https://cursor.com/docs/rules — accessed 2026-10-23T19:09:41Z (HTTP 200, 17,403 B, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`; seat `ScribeS115`; snapshot target `.ufo/waves/round-61/snapshots/S115.page`) — `rules.md:131`: "Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas."
- **S116 — no source row assigned.** The frozen plan assigns S112–S115 to C1 and S117 to C3; the wave census finds no S116 owner. No URL, access, or quote is claimed for S116; no row is invented.
- **S117 kama-shokunin — writing-revision calibration** — `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` — opened read-only 2026-10-23 (33 lines, 5,831 B, sha256 `cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959`; last committed in kama as `6de225c289b7682bf280cffb4a07de3fb7d1275c` at `2026-10-23T16:09:39-03:00`; seats `ScribeC3`, `RevKamaRow`) — `self-assessment-at-writing.md:7`: "a calibration check, not a freshness-only check"

## Mistakes

- **M91 — class: self-assessment overstatement** · The round-60 report's “32 reports, 0 dead” claim conflicts with the closure's count of 29 committed build reports (59/65 seat reports overall); its joint citation also points at `C1-measure.txt` for a base measurement committed in `receipts/freeze2-selftest.txt` (`corpus/lessons/round-60-verifier-spotcheck.md`, §7 defects 2–3). · captured-by: none — no committed-bytes count guarded report claims before this round · fix: the R-a/R-c patterns in `verifiers/check_routed_repairs.py` correct the committed-report count with its counting path and name the precise base-measurement pointer · shown able to fail: the base control reports `routed repairs verified 0 of 6`, exit 1.
- **M92+ — no additional mistake is asserted in this draft.** In-wave reports remain evidence for the L1 to adjudicate; this seat assigns no further lesson class.

## Falsify corrections
```

## Source and measurement provenance

The exact commands and pasted outputs here are copied from the named reports. They do not turn the underlying scratch copies into committed evidence. No measurement listed below was run by ScribeLesson.

### S112 — Claude Code

Fetch command (reported by `wave/ScribeS112.md`):

```sh
date -u && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' 'https://code.claude.com/docs/en/claude-directory.md' -o /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
```

Pasted output:

```text
Fri 23 Oct 2026 07:12:44 PM UTC

200 https://code.claude.com/docs/en/claude-directory.md31144 /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14  /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page
```

Fetch exit 0. The report's quote-count command and pasted output were:

```sh
sed -n '94p' /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page && sed -n '94p' /fast/scratch/hyaku/kotoba-r61/ScribeS112/claude-directory-candidate.page | wc -w
```

```text
| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |
8
```

Quote-count exit 0. This command did not include a `date -u` capture; the report gives the source-fetch time, not a separate quote-count timestamp. No rerun was made to decorate the report. The quote is deliberately in a bullet, not a pipe-delimited table cell.

### S113 — VS Code

Pinned-source fetch command (reported by `wave/ScribeS113.md`):

```sh
date -u && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md -w '\n%{http_code} %{url_effective}' 'https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md' && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && wc -l /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

Pasted output:

```text
Fri 23 Oct 2026 07:13:53 PM UTC
200 https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md25556 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9  /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
  380 25556 /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

Fetch exit 0. Quote-count command and pasted output:

```sh
sed -n '45p' /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md && printf '%s\n' 'Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.' | wc -w && sed -n '177p' /fast/scratch/hyaku/kotoba-r61/ScribeS113/custom-instructions-vscode-docs-5f82fce.md
```

```text
> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`. The Local harness-specific settings in the sections below control discovery.
10
applyTo: '**/*.py'
```

Quote-count exit 0. This command did not include a `date -u` capture; the report gives the source-fetch timestamp, not a separate quote-count timestamp. No rerun was made to decorate the report.

### S114 — Copilot CLI

Counter-compatible fetch command (reported by `wave/ScribeS114.md`):

```sh
set -eu; date -u; curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' -o /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md'; printf '\n'; sha256sum /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page; wc -c /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```

Pasted output:

```text
Fri 23 Oct 2026 07:11:44 PM UTC

200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
8730 /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ScribeS114/S114.page
```

Fetch exit 0. Quote-count command and pasted output:

```sh
date -u; printf '%s\n' 'Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with.' | wc -w
```

```text
Fri 23 Oct 2026 07:11:14 PM UTC
18
```

Quote-count exit 0.

### S115 — Cursor

Canonical no-suffix fetch command (reported by `wave/ScribeS115.md`):

```sh
mkdir -p /fast/scratch/hyaku/kotoba-r61/ScribeS115 && curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page -w '\n%{http_code} %{url_effective}' https://cursor.com/docs/rules && sha256sum /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && wc -c /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && date -u
```

Pasted output:

```text
200 https://cursor.com/docs/rules884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page
17403 /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page
Fri 23 Oct 2026 07:09:41 PM UTC
```

Fetch exit 0. Quote-count command and pasted output:

```sh
sed -n '131p' /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page && sed -n '131p' /fast/scratch/hyaku/kotoba-r61/ScribeS115/S115.page | wc -w && date -u
```

```text
Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
16
Fri 23 Oct 2026 07:11:03 PM UTC
```

Quote-count exit 0. This report also records that the `.md` suffix URL returned HTTP 404 (curl exit 0 without `--fail`); the selected Gate URL is the successful unsuffixed canonical route. Its fresh response hash matches S108's recorded hash, so this is a reopen, not new page bytes.

### S117 — kama sibling source

The independent open and pin recorded by `wave/RevKamaRow.md`:

```sh
cd /home/vgpnk/Projects/shokunin/kama-shokunin && date -u && sha256sum corpus/knowledge/self-assessment-at-writing.md && wc -c -l corpus/knowledge/self-assessment-at-writing.md && git log -1 --format='%H %cI' -- corpus/knowledge/self-assessment-at-writing.md
```

```text
Fri 23 Oct 2026 07:10:28 PM UTC
cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959  corpus/knowledge/self-assessment-at-writing.md
  33 5831 corpus/knowledge/self-assessment-at-writing.md
6de225c289b7682bf280cffb4a07de3fb7d1275c 2026-10-23T16:09:39-03:00
```

Command exit 0. Quote check from the independent reviewer:

```sh
cd /home/vgpnk/Projects/shokunin/kama-shokunin && date -u; grep -c 'a calibration check, not a freshness-only check' corpus/knowledge/self-assessment-at-writing.md; printf '%s\n' 'a calibration check, not a freshness-only check' | wc -w
```

```text
Fri 23 Oct 2026 07:12:09 PM UTC
1
7
```

Command exit 0: the chosen phrase occurs once at line 7 and is 7 words. This is a local sibling artifact, opened read-only; the row remains a draft and its path/commit/hash pin must survive integration.

### C2 base control for M91

The precommitted `.ufo/waves/round-61/controls/C2-base.txt` has no command or run timestamp. `wave/MutC2.md` records an independent base rerun during its mutation work, with all its runs dated 2026-10-23, 19:10–19:13 UTC. That report gives:

```sh
python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
```

```text
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

The committed receipt separately records those six `missing` lines, `routed repairs verified 0 of 6`, and `base-exit=1`. This is prior/peer evidence, not a ScribeLesson run. The rerun report supplies a date range rather than an isolated `date -u` command output for this invocation; no claim is made that the receipt itself has a timestamp it does not contain.

## Findings and conflicts for the canonical judge

### M91 assignment conflict — preserve both statements verbatim

Frozen ScribeLesson assignment:

```text
M91 (class: self-assessment overstatement — the r60 '32 reports, 0 dead' claim vs 29 committed + the joint-citation sloppiness; evidence: corpus/lessons/round-60-verifier-spotcheck.md defects 2-3; captured-by: none — no committed-bytes count guarded report claims before this round; fix: R-a/R-c patterns in verifiers/check_routed_repairs.py, shown able to fail: base control 0 of 6 exit 1)
```

Conflicting `wave/ScribeQuality.md:18` proposal:

```text
- **M91 `report-evidence-overclaim`** · The round-60 report said “32 reports, 0 dead” although the closure found 29 committed build reports (59/65 seat reports committed overall); it pointed to `C1-measure.txt` for the base measurement that is recorded in `receipts/freeze2-selftest.txt`; and its summary called the S106/S107 quotes “byte-exact” despite S106's documented `&#124;` escape and S107's whitespace normalization (`corpus/lessons/round-60-verifier-spotcheck.md` §7 defects 2, 3, and 5). · captured-by: round-60 non-author closure, §7 · fix: reconcile report counts with committed outputs, name the exact base-measurement receipt, and reserve `byte-exact` for literal byte equality; call a quote requiring the documented escape or normalization “quote-equal after documented shaping” (Q56). · used-by: `corpus/QUALITY.md` Q56.
```

The lesson draft follows the frozen ScribeLesson assignment (defects 2–3, class `self-assessment overstatement`, `captured-by: none`, R-a/R-c). It does not merge defect 5/Q56 into M91. L1/canonical judge should resolve the separate proposed M91 wording without averaging the two claims.

### S116 identifier gap

`plans/round-61.md` names S112–S115 as C1 sources and S117 as C3. `wave/RevCensus.md:235-240` independently reports that the planned set is five rows and that “S116 has no owner anywhere in `wave-spec.json`/`wave-dispatch.json`.” The draft Gate records the gap rather than fabricating an S116 source. If a late S116 row is introduced, it needs its own opened-source evidence and row-shape/W04 audit.

### S117 quote and bleed boundary

`wave/ScribeC3.md:15` proposed “evaluates the statement against the committed tree/history at W, not just against the current tip.” `wave/RevC3Bleed.md:52-55` notes that the source line literally has backticks around `W`, omitted from that quote, so the span is not strictly verbatim. `wave/RevKamaRow.md:109-120` supplies a different, independently opened, verbatim quote (“a calibration check, not a freshness-only check”); that is the quote selected in the draft above. The same review says the draft S117 anchor should add the source commit and SHA-256 to meet the contract's revision pin requirement; the Gate draft includes those pins. `wave/RevC3Bleed.md:7-10,39` reports the practice-only borrowing as bleed-clean: no kama domain content, findings, measurements, implementation, parser rules, source data, or conclusions are imported. These are peer review findings, not a C3 gate run by this seat.

### C2 in-wave mutation note — not assigned as M92 here

`wave/MutC2.md:79-90` reports 3 of 7 declared checker mutants killed and four surviving its self-test, including removal of the R-a `claimed 32` check and the R-c `C1-measure.txt` check. The report records those survivor self-tests as `0 failure(s)`, exit 0. This seat did not replay the mutations or assign a new mistake ID. The existing base-world receipt still shows the counter rejecting the all-missing base; the survivor results narrow what that base result proves about individual R-a/R-c arms and the self-test's regression coverage.

## Touched surfaces, out-of-scope items, and limits

- **Actually written by this seat:** `.ufo/waves/round-61/wave/ScribeLesson.md` only.
- **Draft target, not changed by this seat:** `corpus/lessons/round-61.md`.
- **Read-only support:** `plans/round-61.md`, `corpus/SOURCES.md`, `corpus/lessons/round-60-verifier-spotcheck.md`, `verifiers/check_routed_repairs.py`, `.ufo/waves/round-61/controls/C2-base.txt`, source-seat reports S112–S115, C3 source/reviewer reports, and the read-only kama file.
- No lane product, fleet, sibling, `.ufo/state`, git-index, or jj file was changed. No git/jj mutation, dispatch, ask, commit, push, integration, test, build, lint, or tool install was performed by this seat.
- This report does not claim C1, C2, C3, overall round acceptance, or source snapshots as landed. The fetch/quote outputs above remain source-seat report observations until integration lands and verifies their bytes. S112 and S113 quote-count commands did not capture a separate `date -u`; this missing timestamp is disclosed and was not repaired by rerunning.
- Read `/home/vgpnk/.omp/agent/RULES.md` before considering tooling; no install was needed.

## Artifact paths

- Report: `.ufo/waves/round-61/wave/ScribeLesson.md`
- Full lesson draft: `corpus/lessons/round-61.md`
- Supporting source/attack reports: `.ufo/waves/round-61/wave/ScribeS112.md`, `ScribeS113.md`, `ScribeS114.md`, `ScribeS115.md`, `ScribeC3.md`, `RevKamaRow.md`, `RevC3Bleed.md`, `RevCensus.md`, `ScribeQuality.md`, and `MutC2.md`.

Installs: no installs.
Blockers: none for this scoped report; the S116 gap and M91 wording conflict are explicitly surfaced for L1/canonical-judge disposition.
Produced: a complete lesson-file draft with source Gates S112–S115/S117, an honest S116 no-owner record, M91, and its auditable provenance and conflicts.
